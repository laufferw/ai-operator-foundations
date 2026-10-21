# Week 1 Plan

## Goal
Stand up a prompt-to-JSON pipeline with baseline metrics.

## Tasks

1. Create `.env`: `cp .env.example .env`, then add your API keys
2. Install deps: `pip install -r scripts/requirements.txt`
3. Run: `python scripts/llm_playground.py --provider anthropic --input "Summarize this account update."`
4. Run eval harness: `python scripts/run_evals.py --provider anthropic` (repeat with `--provider openai`)
5. Capture results in `docs/week1-review.md`

## Done Criteria

- Script runs end-to-end on both providers
- At least 10 cases evaluated
- Results CSV created in `evals/eval_results/`, with schema-valid %, task-success %, latency, and token usage
