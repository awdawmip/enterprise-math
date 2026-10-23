# Two-pulse absorption: authoritative handoff note (unreviewed)

Date: 2026-10-23. Scope: **auxiliary four-label, independent positive-mass BRC observer**, actions 0/2, 0<=z<=1. Not an admitted Source Result, not independently reviewed, not native six-dimensional P000 dynamics.

## New mathematical increment

A complete symbolic proof now shows **for every n>=4 and every action word with at least two 2 symbols, the final occupancy probability is strictly decreasing**. Exceptional n=2/3 transitions do not grow the historical residual. Once a second action 2 occurs at tau, the residual is frozen at its previous value for **all future actions**: R_n=R_(tau-1) for n>=tau. This does not erase already accumulated residual.

The proof has an exact arbitrary-word count-sufficient occupancy formula, careful treatment of b=0 and a=0 boundary words, a five-case inequality proof and the complete 220/202/022/222 exception audit. Source of mathematical proof: TWO_PULSE_ABSORPTION_AUTHOR_PROOF.en.md.

## Independently executable check

verify_two_pulse_absorption.py (Python standard library, fractions.Fraction) uses independent 16-state occupancy-mask DP and separate exact count formulas. Verification covers all words length 1..8 at nine rational parameters, plus count classes for n=9..80. Captured output: verification_report.json; ALL_CHECKS_PASSED. The finite checks do not replace the general algebraic proof.

## Source pins, authority and next unit

GLOBAL_KNOWLEDGE_V1 main@abed76a9c866347d9c3b3ba2844853229a4e8c22; Enterprise Math main@af2df115aa4f2641452c5a788dab0a4cf57f594b. P000 projection was checked against original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Prior context only: N32 author manuscript c080c43ac34563bf1d5a549a1456fcf7103a993f.

Native em_control_tasks: CONTROL_QUOTA. Native em_session_start: STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No verified live owner, researcher session, formal CLAIM or canonical mathematical admission. This branch is a GitHub artifact-preservation branch only.

**Next scientific unit**: independently prove the zero-pulse all-z unimodality question or find its exact counterexample; resolve first-pulse positions k<=3. Only then synthesize a full all-word all-n residual-increment theorem. Preserve the distinct obligation of mapping the auxiliary four-label observer faithfully to the P000 X6 Cell native dynamics.

Global-Knowledge-Sync: main@abed76a9 / GLOBAL_KNOWLEDGE_V1
