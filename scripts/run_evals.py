#!/usr/bin/env python3
import argparse
import csv
import statistics
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from llm_playground import DEFAULT_MODELS, run

REPO_ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(description="Run eval cases through llm_playground.run()")
    parser.add_argument("--provider", choices=list(DEFAULT_MODELS), required=True)
    parser.add_argument("--model", default="", help="Override the model from .env")
    parser.add_argument("--cases", default=str(REPO_ROOT / "evals/test_cases.csv"))
    parser.add_argument("--limit", type=int, default=0, help="Only run the first N cases")
    args = parser.parse_args()

    cases_path = Path(args.cases)
    if not cases_path.exists():
        raise FileNotFoundError(f"Cases file not found: {cases_path}")

    with open(cases_path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if args.limit:
        rows = rows[: args.limit]

    out_dir = REPO_ROOT / "evals/eval_results"
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_file = out_dir / f"results_{args.provider}_{stamp}.csv"

    fields = [
        "id",
        "provider",
        "model",
        "schema_valid",
        "task_success",
        "latency_ms",
        "input_tokens",
        "output_tokens",
        "validation_error",
        "task_error",
    ]
    results = []
    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()

        for row in rows:
            out = run(args.provider, row["prompt"], args.model or None)
            usage = out["usage"] or {}
            results.append(out)
            writer.writerow(
                {
                    "id": row["id"],
                    "provider": args.provider,
                    "model": out["model"],
                    "schema_valid": out["schema_valid"],
                    "task_success": out["task_success"],
                    "latency_ms": out["latency_ms"],
                    "input_tokens": usage.get("input_tokens"),
                    "output_tokens": usage.get("output_tokens"),
                    "validation_error": out["validation_error"],
                    "task_error": out["task_error"],
                }
            )
            print(f"case {row['id']}: schema_valid={out['schema_valid']} task_success={out['task_success']}")

    n = len(results)
    if n:
        valid = sum(r["schema_valid"] for r in results)
        success = sum(r["task_success"] for r in results)
        latency = statistics.mean(r["latency_ms"] for r in results)
        print(f"\nCases: {n}")
        print(f"Schema valid: {valid / n:.0%}")
        print(f"Task success: {success / n:.0%}")
        print(f"Avg latency: {latency:.0f} ms")

    print(f"Wrote eval results to {out_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
