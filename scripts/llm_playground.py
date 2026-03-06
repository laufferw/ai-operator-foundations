#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
from datetime import datetime

from dotenv import load_dotenv


def call_openai(prompt: str, model: str) -> dict:
    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "system",
                "content": "You are a precise assistant. Return valid JSON with keys: summary, actions, risks.",
            },
            {"role": "user", "content": prompt},
        ],
        text={"format": {"type": "json_object"}},
    )

    text_output = ""
    if getattr(response, "output_text", None):
        text_output = response.output_text

    return {
        "raw": text_output,
        "usage": getattr(response, "usage", None),
    }


def call_anthropic(prompt: str, model: str) -> dict:
    from anthropic import Anthropic

    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    msg = client.messages.create(
        model=model,
        max_tokens=800,
        system="You are a precise assistant. Return valid JSON with keys: summary, actions, risks.",
        messages=[{"role": "user", "content": prompt}],
    )

    content = ""
    for block in msg.content:
        if getattr(block, "type", "") == "text":
            content += block.text

    return {
        "raw": content,
        "usage": {
            "input_tokens": getattr(msg.usage, "input_tokens", None),
            "output_tokens": getattr(msg.usage, "output_tokens", None),
        },
    }


def validate_payload(raw: str) -> tuple[bool, dict | None, str | None]:
    try:
        parsed = json.loads(raw)
    except Exception as exc:
        return False, None, f"invalid_json: {exc}"

    required = ["summary", "actions", "risks"]
    missing = [k for k in required if k not in parsed]
    if missing:
        return False, parsed, f"missing_keys: {','.join(missing)}"

    return True, parsed, None


def main() -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(description="Simple LLM playground for structured JSON outputs.")
    parser.add_argument("--provider", choices=["openai", "anthropic"], required=True)
    parser.add_argument("--input", required=True, help="Prompt text")
    parser.add_argument("--save", default="", help="Optional output json file path")
    args = parser.parse_args()

    started = time.perf_counter()

    if args.provider == "openai":
        model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
        result = call_openai(args.input, model)
    else:
        model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5")
        result = call_anthropic(args.input, model)

    duration_ms = round((time.perf_counter() - started) * 1000, 2)

    is_valid, payload, error = validate_payload(result["raw"])

    output = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "provider": args.provider,
        "model": model,
        "latency_ms": duration_ms,
        "schema_valid": is_valid,
        "validation_error": error,
        "payload": payload,
        "raw": result["raw"],
        "usage": result.get("usage"),
    }

    print(json.dumps(output, indent=2))

    if args.save:
        with open(args.save, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2)

    return 0 if is_valid else 1


if __name__ == "__main__":
    sys.exit(main())
