# 90-Day Sprint (Execution First)

## Phase 1 (Weeks 1-4): Control and Measure LLM Outputs

### Week 1
- Set up env + API keys (`cp .env.example .env`)
- Run `scripts/llm_playground.py` on both providers
- Run `scripts/run_evals.py` on the 10 cases in `evals/test_cases.csv`

### Week 2
- Grow the eval set to 30 cases, including messy and adversarial inputs
- Add an `expected` column and a stricter task-success check

### Week 3
- Add an LLM-as-judge grader for summary quality
- Compare OpenAI vs Anthropic, and two settings per provider, on quality, latency, and cost

### Week 4
- Publish a short report in `docs/week4-review.md`

## Phase 2 (Weeks 5-8): Integrate Business Systems

### Week 5
- Build Salesforce fetch prototype (or a CSV export stand-in)

### Week 6
- Add AI summary generation for account-level data, reusing the Week 1 schema

### Week 7
- Post structured summary to Slack

### Week 8
- Add retries, idempotency keys, and error logging

## Phase 3 (Weeks 9-12): Tools, Agents + Deployment

### Week 9
- Wrap the Salesforce fetch as an MCP server with read-only tools

### Week 10
- Build a small agent that uses those tools to produce an account-health report
- Add a human approval step before any write action

### Week 11
- Package the summary workflow as a FastAPI microservice

### Week 12
- Deploy to AWS Lambda + API Gateway
- Publish sprint retrospective
