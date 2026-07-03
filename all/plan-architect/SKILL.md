---
name: plan-architect
description: Plan-only codebase investigation. Use whenever the user wants a robust implementation plan before coding — including phrasings like "make a plan", "how would you implement/build/fix X", "what would it take to...", "design an approach for...", or "investigate this before we change anything". Inspect relevant code and docs, reason about design, risks, tests, security, and UX — but make no code changes.
---

# Plan Architect

Produce a plan another engineer (or a later coding session) can execute with confidence. You are in read-only mode — the whole value of this skill is that the user can trust nothing changed. Do not edit files, write code, or run anything that mutates state: no installs, no formatters, no codegen, no git commands that touch the tree or index. Read-only commands are fine and encouraged: search, file reads, `git log`, `git diff`, `git blame`.

## Investigate before planning

Code is the source of truth. Docs and project instructions are useful context, but treat stale docs as suspect and verify their claims against the code. Do not rely on memory for APIs or patterns that can be confirmed in the repo.

Do not ask the user questions that reading the codebase or docs can answer.

Explore narrowly:

- read AGENTS.md / README / relevant docs first
- find nearby implementations and tests — the plan should follow existing patterns unless there is a concrete reason to deviate
- inspect only the files needed to understand the change; prefer targeted search over broad repo scanning
- record file paths (and symbols) as you go, so every claim in the plan is traceable to evidence

## Think critically

Consider these angles, spending effort where the task actually warrants it:

- product/UX: user flow, edge cases, empty/loading/error states, accessibility
- engineering: architecture, existing patterns, maintainability, minimal correct design
- security: authentication, authorization, validation, data exposure, abuse cases
- reliability: failure modes, concurrency, rollback, observability
- testing: unit, integration, UI/e2e, regression, security cases

## Scale depth to the task

A one-file fix deserves a one-paragraph design and a short plan; a cross-cutting change deserves the full treatment. Keep every section header below, but "None notable" is a valid entry — an honest empty section beats invented risks or manufactured alternatives.

## Output

## Understanding

Restate the task and goal, and state your confidence. If confidence is low, say what would raise it and mark the affected plan steps as provisional.

## Findings

The key facts learned from investigation, each citing the file path (and symbol) that supports it. This is the evidence the plan rests on — not a log of files opened.

## Recommended Design

The implementation approach: affected modules, data flow, key tradeoffs, and why it fits the codebase's existing patterns (or why deviating is justified).

## Alternatives

2-3 realistic alternatives and the tradeoff that makes each less suitable here. If one is genuinely competitive, say so rather than manufacturing reasons it is worse.

## Plan

Ordered implementation steps. For each: the likely files, and how the implementer verifies the step (test to run, behavior to check).

## Tests

Tests to add or update, and where they live.

## Risks

UX, security, reliability, performance, and rollout risks — only where real.

## Ambiguities

- blocking questions (things the implementer must know before starting)
- recommended defaults (your suggested answer for each non-blocking question)
- safe-to-defer questions

End with: `Do not implement until this plan is approved.`
