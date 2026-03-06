#!/usr/bin/env python3
import argparse
import csv
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run basic eval cases through llm_playground.py")
    parser.add_argument("--provider", choices=["openai", "anthropic"], required=True)
    parser.add_argument("--cases", default="evals/test_cases.csv")
    args = parser.parse_args()

    cases_path = Path(args.cases)
    if not cases_path.exists():
        raise FileNotFoundError(f"Cases file not found: {cases_path}")

    out_dir = Path("evals/eval_results")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"results_{args.provider}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.csv"

    with open(cases_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    fields = ["id", "provider", "schema_valid", "latency_ms", "validation_error"]
    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()

        for row in rows:
            prompt = row["prompt"]
            cmd = [
                "python",
                "scripts/llm_playground.py",
                "--provider",
                args.provider,
                "--input",
                prompt,
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True)

            parsed = {}
            try:
                parsed = json.loads(proc.stdout)
            except Exception:
                parsed = {
                    "schema_valid": False,
                    "latency_ms": None,
                    "validation_error": "non_json_stdout",
                }

            writer.writerow(
                {
                    "id": row["id"],
                    "provider": args.provider,
                    "schema_valid": parsed.get("schema_valid"),
                    "latency_ms": parsed.get("latency_ms"),
                    "validation_error": parsed.get("validation_error"),
                }
            )

    print(f"Wrote eval results to {out_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
