# 2026-10-15 / Unreviewed six-source BRC horizon

Auxiliary positive-support Boolean-reset model (not native X6 dynamics): I={0,...,5}; actions I\\{j}; secret reset of a chosen source; feedback after each action [remaining residual >= 3]; terminal universal safety [remaining residual >= Q].

**Exact finite-search conclusion:** H_6(Q=1,T=3)=6 and H_6(Q=2,T=3)=6, self-checked/unreviewed.

Proof outline: clip each residual d_i to min(d_i,3), preserving both threshold predicates for every reset subset and every future action. Check 4^6 clipped states, 4^12=16777216 ordered pairs via 54264 simultaneous-S6 pair orbits. For each ordered pair, directed BFS over (all X reset sets compatible with one public feedback spine, one Y reset set), in both orientations; correctness follows by pruning other feedback branches of an X-safe/Y-unsafe policy. Exact orbit-weight totals and histograms pass.

Q=1: 2638 signatures; 529848 pairs first separate at depth 6; none first separate later.
Q=2: 3904 signatures; 4032 pairs first separate at depth 6; none first separate later. 2570 ordered pairs have different static signatures but permanently equivalent safety behavior.

Independent two-belief policy DP checked strict depth-six witnesses for both Q values. All-orbit proof depends on finite C++ verification and search-completeness argument, not an independent full recalc.

Status: no RA/CLAIM/Driver review (native write denied); no admission to main. Evidence ZIP (local conversation artifact): EM_BRC_20261015_T3_N6_EXACT_H6_FULL_ORBIT_EVIDENCE.zip, SHA256 38f277803289bbe278b819580fc4e7d14af6f844dd0efa8f75602a4c77bb6dc6.
Next: prove H_n=n symbolically for T=3,Q=1,2 or find n>=7 counterexample.