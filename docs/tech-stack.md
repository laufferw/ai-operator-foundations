# Standard Tech Stack

## Core
- Python 3.11+
- FastAPI
- Postgres/Supabase (pgvector for retrieval)

## AI
- Anthropic API (structured outputs, tool use, prompt caching)
- OpenAI API (structured outputs, embeddings, comparison baseline)
- Model Context Protocol (MCP) for exposing business tools to agents
- Claude Agent SDK or SDK tool runners for agent loops

## Integrations
- Salesforce API
- Slack API

## Infra
- AWS Lambda
- API Gateway
- EventBridge

## Observability
- Structured logs (JSON)
- Eval outputs in CSV
- OpenTelemetry tracing (Month 9)
