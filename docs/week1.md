# Week 1 Plan

## Goal
Stand up a prompt-to-JSON pipeline with baseline metrics.

## Tasks

1. Create `.env` from `.env.example`
2. Install deps: `pip install -r scripts/requirements.txt`
3. Run: `python scripts/llm_playground.py --provider openai --input "Summarize this account update."`
4. Run eval harness: `python scripts/run_evals.py --provider openai`
5. Capture results in `docs/week1-review.md`

## Done Criteria

- Script runs end-to-end
- At least 10 cases evaluated
- Metrics file created in `evals/eval_results/`
