# BRC N=4 BU: exact lawful strategy strictly below the post-rho splice formula

Date: 2026-10-29. Status: AUTHOR_SIDE / EXACT_RATIONAL_WITNESS / UNREVIEWED / NOT_ADMITTED / NOT_A_NATIVE_DRIVER_REVIEW.

## Scope and upstream evidence

This is a single explicit **falsifier of extrapolating** the root formula h=b*cstar/(4+cstar) beyond its proven range b/a<=rho. It does **not** contradict the theorem within b/a<=rho, prove that rho is the actual minimax phase boundary, close any canonical Task, or make a P000/native-X6 physics claim.

Model: the same external strictly-positive 16-leaf Q/P BRC N=4 experiment as research_notes/brc_n4_bu_full_causal_reduction_audit_20261029_r1t11/PROOF.md and research_notes/brc_n4_bu_optimal_splice_rho_20261029_emr1/PROOF.md at Enterprise Math main@4ffdef264544aeea65b68be98a36ab5a829d9f12. Observer O=(T,Decision,Z_BU) retains the BU source bit at/after time 3. The candidate competitor is a concrete legal behavioral S23 policy, so this upper bound does not rely on accepting the broader unreviewed four-atom reduction.

## Exact target and counterexample

Take target a=1/2, b=872/10793, and formal root cstar=9/25. Then b/a=1744/10793, which exceeds rho=(sqrt(5889)-25)/329. One exact route: cstar=9/25 < c0=(sqrt(5889)-73)/10 since 25*5889 > 383^2, and r(c)=(1-c)(4+c)/(3c²+8c+14) is strictly decreasing. The quadratic

    f(c)=(a+3b)c²+(3a+8b)c+14b-4a

vanishes exactly at cstar, and the extrapolated formula equals

    h=b*cstar/(4+cstar)=72/10793.

Now choose a competing strategy with first-stage rates A=503/1000, B=399/5000; shared AU/BU time-two continuation c=1/3; AV rate U/A with U=53/500; BV rate V/B with V=B=399/5000. All rates are in [0,1] and 0<=U<=A, 0<=V<=B. Every time-one/two stop decides Q. All branches that reach time three stop there, deciding Q on BU and P on non-BU. The BU time-three likelihood ratios {1/5,9/5} are disjoint from the non-BU ratios {9/10,11/10,1/4,2}, so this decision is a valid function of the current ratio alone. The shared AU/BU conditional kernel and every S23 equality constraint are respected.

Direct summation of the 16 strictly positive P/Q leaf masses for the complete O observer yields

    TV_Q = 133/20000,
    TV_P = 6470029/971370000,
    e = max(TV_Q, TV_P) = 6470029/971370000,
    h - e = 9971/971370000 > 0.

Thus the actual lawfully attainable minimax values satisfy d23(a,b) <= e < h and d2(a,b) <= e < h. Even if the stronger full causal reduction is not admitted, this one legal 16-leaf strategy already disproves the proposed global continuation of the root formula at this parameter point. It does **not** demonstrate what the exact optimal value is there, or whether rho is a universal phase boundary.

## Reproduction and proof boundary

VERIFY.py enumerates the full 16 Q/P leaves using Q masses (AU,AV,BU,BV)=(1/6,1/3,1/4,1/4), time-three P/Q ratios ((9/10,11/10),(1/4,1/4),(1/5,9/5),(2,2)), and equal time-four daughter masses; applies the target and competitor pathwise stopping kernels; compares both terminal O distributions using exact Python Fraction arithmetic; and separately reproduces the four-atom signed differences as a cross-check. Local execution passed all assertions with the printed exact fractions above.

Next independently review the observer specification, conditional policy admissibility and direct enumeration; then determine a new lower-bound certificate / exact minimax expression on r>rho, distinguishing true phase structure from this single counterexample. Retain source/provenance and exposure; do not create a duplicate official Task or relabel author verification as a native Driver reference pass.

Research contribution: current exposed automation conversation's author-side computational finding; no authenticated Driver DA/session, independent reviewer, native Result, Reference, Synthesis or Follow-up is claimed.
