# 12-Month AI Operator Plan

## North Star

Become a systems builder who designs, deploys, and operates AI workflows for real business outcomes.

## What Changed (Oct 2026 revision)

- Agents, tool use, and MCP move from Month 7 to Months 4-5. They are now the default way AI systems touch business data, not an advanced topic.
- Evals become their own month (Month 2) and run through every later month.
- Structured outputs are schema-enforced by the provider, so Month 1 starts there instead of with prompt-only JSON.
- Prompt-injection and permission design are explicit topics, because agents now act on real systems.
- Original Months 3+4 (Python automation, integrations) and 5+8 (orchestration, data pipelines) are merged to make room.

## Month-by-Month

### Month 1: LLM Foundations + Structured Outputs
- Learn: tokens, context windows, model tiers, reasoning/effort settings, schema-enforced outputs
- Build: `scripts/llm_playground.py` against both providers
- Ship: first eval run on `evals/test_cases.csv` with schema-valid and task-success rates

### Month 2: Evals as a Discipline
- Learn: golden datasets, code-graded vs model-graded checks, regression testing, comparing models and settings
- Build: grow the eval set to 50+ cases with expected outputs; add an LLM-as-judge grader
- Ship: reliability report comparing two models and two prompt versions

### Month 3: Integrations + Workflow Automation
- Learn: REST, OAuth, webhooks, pagination, retries, idempotency keys
- Build: Salesforce (or CSV export) pull → AI summary → Slack post
- Ship: `apps/revops-summary-pipeline` with retries and error logging

### Month 4: Tool Use + MCP
- Learn: tool/function calling, strict tool schemas, Model Context Protocol (servers, tools, resources)
- Build: an MCP server exposing read-only CRM tools (account lookup, opportunity list, activity history)
- Ship: `apps/revops-mcp-server`, usable from Claude Code / Claude Desktop and from your own scripts

### Month 5: Agentic Workflows
- Learn: agent loops (SDK tool runners, Claude Agent SDK), planning, failure handling, human-in-the-loop approval
- Build: account-health agent that uses the Month 4 MCP tools and proposes actions for approval
- Ship: agent with guardrails, a deterministic output contract, and an eval set of agent tasks

### Month 6: RAG + Context Engineering
- Learn: chunking, embeddings, hybrid search, citations, when long context beats retrieval
- Build: RevOps knowledge assistant grounded on playbooks and policies
- Ship: `apps/knowledge-assistant-rag` with citation-only answers and an "insufficient evidence" path

### Month 7: Orchestration + Data Pipelines
- Learn: n8n/Make vs code, batch vs event-driven, queues, batch APIs for cheap bulk jobs
- Build: nightly ingestion → analysis → alert chain
- Ship: event-driven pipeline with retry strategy and a no-code vs code tradeoff write-up

### Month 8: Cloud Deployment
- Learn: serverless architecture, secrets management, IAM basics
- Build: AI microservice on AWS (Lambda + API Gateway)
- Ship: `apps/ai-microservice` running endpoint + deployment docs

### Month 9: Observability + Cost
- Learn: tracing (OpenTelemetry), prompt caching, model routing, effort tuning, cost per completed task
- Build: dashboards for quality, latency, and cost across your deployed workflows
- Ship: cost/quality report with at least one measured optimization

### Month 10: Product Layer
- Learn: AI UX, feedback loops, approval flows, quality telemetry
- Build: RevOps assistant UI and API backend
- Ship: usable internal alpha with user feedback

### Month 11: Architecture, Security + Scale
- Learn: prompt injection, least-privilege tool permissions, audit logs, multi-model and multi-agent patterns
- Build: threat model and architecture docs for your capstone
- Ship: architecture decision record set, including a security review

### Month 12: Capstone
- Build: AI RevOps Copilot (or CS Account Management Engine)
- Ship: production-style capstone with docs, demos, evals, and metrics

## Definition of Done (per month)

- One repo artifact or major module
- One architecture/decision document
- One metrics snapshot (quality, latency, cost) from an eval run
- One short demo video

## Tooling Note

Use an AI coding agent (Claude Code or similar) for the building hours. Part of the skill being trained is directing agents well: writing clear specs, reviewing their diffs, and keeping evals as the source of truth.
