# Stage250 — Exact N=10 asymmetric sequential minimax theorem

**Provenance and classification (2026-10-28).** AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. External IID auxiliary model, not a theorem about native P000 X6 heartbeat dynamics. Continues Stage249 in Draft PR #1571 (immutable source a71f7fcf055342aca54e5d969f31102cc926929e). The verifier is STAGE250_EXACT_REPRO.py, generated from the Stage249 executed source by replacing the explicitly listed horizon, support, policy and witness constants, then executed again.

## Statement

Let symbols 0,1,2 be IID under either P=(3,1,20)/24 or Q=(2,2,20)/24. An arbitrary policy may randomize at any ordered observation history, must stop at tau<=N, and decide P or Q. Define eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP=E_P(tau), tQ=E_Q(tau). Write V_N(a,b) for the infimum of max(tP,tQ) over policies with eP<=a and eQ<=b.

**Theorem.** For N=10, a=3/10, b=19/40,

    V_10(3/10,19/40) = 46306027119263/7618838952960
                      = 6.077832515579374...

The minimum is attained by the rational policy below. All full ordered-history randomized policies, including those with irrational coins, are within the lower-bound scope.

## Exact descent limited to four observers

At ordered history h of count state s=(i,j,k), the two positive history masses satisfy

    Q(h)/P(h) = L(s) = (2/3)^i * 2^j.

For any full-history stopping and classification policy, aggregate the P-weighted occupancy and each action mass of all paths with the same count s. Their Q counterparts are exactly L(s) times the P action masses. Upon continuation by symbol z, the next state is s+e_z with conditional P and Q multipliers P_z and Q_z, independent of the earlier order. Consequently normalizing the P action flows gives a count-state randomized policy satisfying the same P and Q flow equations. Thus the exact four outputs eP,eQ,tP,tQ are preserved through the declared finite IID horizon. This is a scope-typed sufficient statistic; it makes no assertion about additional future observables, native paths, BRC identities or X6 state reduction.

## Global dual lower bound

Choose K=5223528/75601>0 and define J=tP+K(eP+eQ). At count s, the P-normalized finite-horizon Bellman function is

    H(s) = min( K*L(s) [decide P],
                K [decide Q],
                1 + sum_{z=0}^2 P_z*H(s+e_z) [continue if |s|<10] ).

At |s|=10 the continue choice is absent. This recursion minimizes J over all full-history policies, because the conditional Q/P multiplier at each history depends only on s. The exact Fraction computation enumerates C(13,3)=286 count states and finds exactly two ties: A=(1,0,3), choose P versus continue; B=(0,0,10), choose P versus choose Q. The other 504 action gaps are strictly positive.

At A, the tied candidate affine costs are (2/3)*K and

    2687/2304 + (2910383/4478976)*K.

Their equality gives exactly K=5223528/75601. Root value:

    H(0,0,0)=90854952632659/1523767790592.

For every feasible policy,

    max(tP,tQ) >= tP >= H(0,0,0)-K*(3/10+19/40)
                =46306027119263/7618838952960.

This is a universal exact inequality, not interpolation from finite numerical samples.

## Matching rational policy and exact four-observer witness

At A=(1,0,3), continue with probability

    x=180342429/189002500

and otherwise decide P. At B=(0,0,10), decide P with probability

    y=339279246393/590632812500

and otherwise decide Q. Elsewhere choose the unique Bellman-minimizing action. Both probabilities lie in (0,1). Independent exact P and Q observer recursion yields

    (eP,eQ,tP,tQ)
      = (3/10,19/40,
         46306027119263/7618838952960,
         44393556226507/7618838952960).

Hence tP-tQ=478117723189/1904709738240>0 and

    tP+K(eP+eQ)=H(0,0,0).

The primal achieves the global lower bound. The support for expected time is one-sided: thetaP=1, thetaQ=0, so no interior time dual is needed at N=10.

Relative to Stage249 V9=65983208881/10195269120, the exact improvement is 364524197256449/924927048889344. Stage248 already proves the bound 27/5 for N>=13; this theorem concerns only N=10.

## Executed arithmetic and evidence limits

The published STAGE250_EXACT_REPRO.py is byte-identical (Git blob 82a9a3e7942d8e6f5421e50e98ea2bae6a952706) to the source actually run with Python standard-library Fraction. It checks all 286 Bellman states, two ties, 504 positive gaps, both rational coins, the root dual identity, all four exact suffix observers, and an independent ordered-history DFS. The latter never merges prefixes, propagates positive P/Q branch masses separately, visits 676 nodes, and sums 456 terminal action branches. Both terminal probability masses equal exactly one. RUN_STAGE250.txt contains its actual program output. These are author-level exact proof/computation evidence, pending independent mathematical review.

Source snapshots for this iteration: GLOBAL_KNOWLEDGE_V1 main@5bec6b0ac9cd7d648fd4d2d90b4be385b92c2812, Enterprise Math main@c9448cadfbbc9a41d93e13bf759332e7a662a205; P000 V5 and current ACTIVE worldview, joint-relation observer preservation and portable research rules were read. The count compression is proved for the specified IID observer family only; no correspondence theorem to native X6/BRC dynamics has been established.

## Next exact question

Stage251: compute V_11(3/10,19/40) with a rational primal/dual match (or exact obstacle), determine whether thetaP=1 persists, enumerate C(14,3)=364 Bellman states, and verify four observers by non-merged P/Q source-labeled ordered-history recursion. Publish the next handoff to this same Draft PR.
