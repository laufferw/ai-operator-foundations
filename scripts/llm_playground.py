#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone

from dotenv import load_dotenv

SYSTEM_PROMPT = (
    "You are a RevOps analyst. Summarize the input in one or two sentences, "
    "list concrete next actions, and list the risks it implies."
)

# Shared output contract. Both providers enforce it server-side, so a valid
# response always parses; validate_payload() still checks it as a guardrail.
OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "actions": {"type": "array", "items": {"type": "string"}},
        "risks": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["summary", "actions", "risks"],
    "additionalProperties": False,
}

DEFAULT_MODELS = {
    "openai": ("OPENAI_MODEL", "gpt-5-mini"),
    "anthropic": ("ANTHROPIC_MODEL", "claude-opus-5-5"),
}


def call_openai(prompt: str, model: str) -> dict:
    from openai import OpenAI

    client = OpenAI()
    response = client.responses.create(
        model=model,
        instructions=SYSTEM_PROMPT,
        input=prompt,
        text={
            "format": {
                "type": "json_schema",
                "name": "revops_summary",
                "schema": OUTPUT_SCHEMA,
                "strict": True,
            }
        },
    )

    usage = response.usage
    return {
        "raw": response.output_text or "",
        "stop_reason": response.status,
        "usage": {
            "input_tokens": getattr(usage, "input_tokens", None),
            "output_tokens": getattr(usage, "output_tokens", None),
        },
    }


def call_anthropic(prompt: str, model: str) -> dict:
    from anthropic import Anthropic

    client = Anthropic()
    # fallbacks="default" retries a safety-classifier refusal on a suitable
    # model server-side instead of returning an empty answer.
    msg = client.beta.messages.create(
        model=model,
        max_tokens=16000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
        output_config={"format": {"type": "json_schema", "schema": OUTPUT_SCHEMA}},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )

    content = "".join(block.text for block in msg.content if block.type == "text")

    return {
        "raw": content,
        "stop_reason": msg.stop_reason,
        "usage": {
            "input_tokens": msg.usage.input_tokens,
            "output_tokens": msg.usage.output_tokens,
        },
    }


def validate_payload(raw: str) -> tuple[bool, dict | None, str | None]:
    try:
        parsed = json.loads(raw)
    except Exception as exc:
        return False, None, f"invalid_json: {exc}"

    if not isinstance(parsed, dict):
        return False, None, "not_an_object"

    missing = [k for k in OUTPUT_SCHEMA["required"] if k not in parsed]
    if missing:
        return False, parsed, f"missing_keys: {','.join(missing)}"

    if not isinstance(parsed["summary"], str):
        return False, parsed, "bad_type: summary"
    for key in ("actions", "risks"):
        if not isinstance(parsed[key], list) or not all(isinstance(i, str) for i in parsed[key]):
            return False, parsed, f"bad_type: {key}"

    return True, parsed, None


def check_task(payload: dict | None) -> tuple[bool, str | None]:
    """Baseline task-success check: the answer is non-empty and actionable."""
    if payload is None:
        return False, "no_payload"
    if not payload["summary"].strip():
        return False, "empty_summary"
    if not [a for a in payload["actions"] if a.strip()]:
        return False, "no_actions"
    return True, None


def run(provider: str, prompt: str, model: str | None = None) -> dict:
    env_var, default = DEFAULT_MODELS[provider]
    model = model or os.getenv(env_var, default)
    call = call_openai if provider == "openai" else call_anthropic

    started = time.perf_counter()
    try:
        result = call(prompt, model)
        error = None
    except Exception as exc:
        result = {"raw": "", "stop_reason": None, "usage": None}
        error = f"api_error: {type(exc).__name__}: {exc}"
    duration_ms = round((time.perf_counter() - started) * 1000, 2)

    if error:
        is_valid, payload = False, None
    elif result["stop_reason"] in ("refusal", "max_tokens", "incomplete"):
        is_valid, payload, error = False, None, f"stop_reason: {result['stop_reason']}"
    else:
        is_valid, payload, error = validate_payload(result["raw"])

    task_ok, task_error = check_task(payload) if is_valid else (False, error)

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "provider": provider,
        "model": model,
        "latency_ms": duration_ms,
        "schema_valid": is_valid,
        "validation_error": error,
        "task_success": task_ok,
        "task_error": task_error,
        "payload": payload,
        "raw": result["raw"],
        "usage": result["usage"],
    }


def main() -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(description="Simple LLM playground for structured JSON outputs.")
    parser.add_argument("--provider", choices=list(DEFAULT_MODELS), required=True)
    parser.add_argument("--input", required=True, help="Prompt text")
    parser.add_argument("--model", default="", help="Override the model from .env")
    parser.add_argument("--save", default="", help="Optional output json file path")
    args = parser.parse_args()

    output = run(args.provider, args.input, args.model or None)

    print(json.dumps(output, indent=2))

    if args.save:
        with open(args.save, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2)

    return 0 if output["schema_valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
