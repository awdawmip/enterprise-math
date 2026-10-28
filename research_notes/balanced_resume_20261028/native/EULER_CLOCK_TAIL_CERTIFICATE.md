# Finite-mean clock budget for the inherited Euler response

Author: EM-NATIVE-A8C19E. Activity: RA-BALANCE-NATIVE-20261028-A8C19E.
Date: 2026-10-28 (Asia/Shanghai).
Status: CONDITIONAL_COROLLARY / independent review pending; no physical clock claim.

Use the exact model and exposure of `EULER_CLOCK_BRIDGE.md`: positive-integer iid waits independent of the complete source edge process, held state between edge completions, N(t)=max{n:T_n<=t}, normalized response a_t=E[c_N(t)]. The old source proves

    |c_n| <= alpha^floor(n/4),   alpha=2/9.

Assume additionally mu=E W<infinity. The mean does not determine a_t, as the main note's two clocks show. It nevertheless supplies a conservative uniform convergence budget without a tail-distribution model.

For every integer n>=1 and t>=0,

    |a_t| <= min(1, n mu/(t+1) + alpha^floor(n/4)).        (1)

Proof. Split the expectation into N(t)<n and N(t)>=n. On the first event use |c_N|<=1; on the second use the monotone source envelope alpha^floor(n/4). Since positive integer waits imply

    {N(t)<n} = {T_n>t} = {T_n>=t+1},

Markov's inequality and E T_n=n mu give P(N(t)<n)<=n mu/(t+1). Combining the two pieces proves (1); the outer minimum uses the trivial normalized bound. The expectation and independence requirements are exactly those of the main note, with finite mean added only here.

In particular for any k>=1,

    |a_t| <= min(1, 4k mu/(t+1) + alpha^k).               (2)

For t+1>mu choose k as the least positive integer with alpha^k<=mu/(t+1). Then

    |a_t| <= min(1, (4k+1)mu/(t+1)),

so a sufficient bound is O(mu[1+log((t+1)/mu)]/(t+1)). This is an upper certificate, not an asserted sharp asymptotic or a universal exponential rate.

An entirely rational target-error interface avoids numerical logarithms. Given 0<delta<1 and a known finite upper bound mu_bar>=E W, choose the least positive integer k with

    (2/9)^k <= delta/2.

Every integer t satisfying

    t+1 >= 8 k mu_bar/delta

then obeys |a_t|<=delta. For a non-normalized source bound W_total, multiply the right-hand response bound by W_total. This is a clock-error certificate conditional on the independently justified mean bound and whole-process independence, not a derivation of those assumptions from native physics.

The method is ordinary Markov inequality composed with the previously proved Euler envelope and the explicit renewal clock. No new general tool family or novel probability theorem is claimed. The contribution is a quantitative, auditable substitute for the invalid direct replacement of edge index by elapsed time. Unlike an exact response prediction, this guarantee does not require the entire waiting distribution.

Researcher-ID: EM-NATIVE-A8C19E / TASK_RESEARCH
