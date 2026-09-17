# Geometry–BRC residual systems: objective, R1/R2 and Driver publication

Source snapshot: `d9d7db8f175b39e7d4fb3cda5117c8a6f9bcd98b`  
Parent objective: `OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS` / `OG-1012C66C67B7F797E30D`  
Publisher: `EM-DVR-4B13E4` as `RESEARCH_DRIVER`  
Policy digest: `sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4`

This transaction converts the frozen R1 program into canonical task definitions, adds a bounded evidence-gated R2 continuation set, and adds three Driver governance units for persistent routing, R1 evidence review and eventual portfolio synthesis.

## Published research structure

R1 contains six tasks. Only `RS-GBRC-R1-TYPED-CARRIER` is initially READY; every other R1 task is BLOCKED on exact upstream artifacts. R2 contains six tasks and all are initially BLOCKED. The five substantive R2 routes are explicit CONTINUATION tasks with complete successor gates; `RS-GBRC-R2-INTEGRATION-ACCEPTANCE` is an INTEGRATION task.

The three governance tasks are:
- `GV-GBRC-PERSISTENT-LINE-DRIVER-20260917` — READY, persistent recovery/routing/handoff.
- `GV-GBRC-R1-EVIDENCE-REVIEW-20260917` — BLOCKED until six R1 terminal outputs or exact obstructions exist.
- `GV-GBRC-R2-PORTFOLIO-SYNTHESIS-20260917` — BLOCKED until the R1 Driver disposition and R2 integration outcome exist.

## Authority and truth boundary

The new objective generation is OPEN and selected before the task publication timestamp. All task records pin `OG-1012C66C67B7F797E30D`. The publication defines claimable tasks and dependency gates only. It creates no research execution claim, accepts no Result, changes no P000 premise, grants no Working Truth or Foundation authority, and records no final mathematical disposition.

Exact taskbook Git-blob identities and immutable V2 publication IDs are listed in `manifest.json`. The scoped preflight and its limitations are recorded in `preflight.json`.
