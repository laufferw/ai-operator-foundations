# 90-Day Sprint (Execution First)

## Phase 1 (Weeks 1-4): Control LLM Outputs

### Week 1
- Set up env + API keys
- Run `scripts/llm_playground.py`
- Evaluate 10 cases from `evals/test_cases.csv`

### Week 2
- Add strict JSON schema validation to outputs
- Add latency and token usage tracking

### Week 3
- Build baseline scoring function (schema-valid + task-complete)
- Compare OpenAI vs Anthropic quality and cost

### Week 4
- Publish a short report in `docs/week4-review.md`

## Phase 2 (Weeks 5-8): Integrate Business Systems

### Week 5
- Build Salesforce fetch prototype

### Week 6
- Add AI summary generation for account-level data

### Week 7
- Post structured summary to Slack

### Week 8
- Add retries, idempotency keys, and error logging

## Phase 3 (Weeks 9-12): RAG + Deployment

### Week 9
- Ingest internal docs into vector index

### Week 10
- Implement citation-only Q&A behavior

### Week 11
- Package as FastAPI microservice

### Week 12
- Deploy to AWS Lambda + API Gateway
- Publish sprint retrospective
