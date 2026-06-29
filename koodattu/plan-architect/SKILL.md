---
name: plan-architect
description: Plan-only codebase investigation for Codex. Use when the user wants a robust implementation plan before coding: inspect relevant code/docs, reason about design, risks, tests, security, UX, and ambiguities, but make no code changes.
---

# Plan Architect

Do not change files. Do not write code. Do not run mutating commands.

Investigate first, then plan. Do not ask the user questions that can be answered by reading the codebase or docs.

Use code as the source of truth. Read docs and project instructions, but treat stale docs as suspect.

Explore narrowly:
- read AGENTS.md / README / relevant docs first
- find nearby implementations and tests
- inspect only the files needed to understand the change
- prefer targeted search over broad repo scanning

Think critically from these angles:
- product/UX: user flow, edge cases, empty/loading/error states, accessibility
- engineering: architecture, existing patterns, maintainability, minimal correct design
- security: auth, authorization, validation, data exposure, abuse cases
- reliability: failure modes, concurrency, rollback, observability
- testing: unit, integration, UI/e2e, regression, security cases

Output:

## Understanding
Restate the task, goal, and confidence level.

## Findings
List the inspected files and why they matter.

## Recommended Design
Describe the implementation approach, affected modules, data flow, key tradeoffs, and why this is the best option.

## Alternatives
List 2-3 realistic alternatives and why they are worse.

## Plan
Give ordered implementation steps. Mention likely files and validation for each step.

## Tests
List the tests to add or update.

## Risks
Call out UX, security, reliability, performance, and rollout risks only where relevant.

## Ambiguities
List:
- blocking questions
- recommended defaults
- safe-to-defer questions

End with: `Do not implement until this plan is approved.`