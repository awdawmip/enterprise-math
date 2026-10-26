# Stage155 — next exact Bellman/primal research unit (OPEN)

Frozen model: EXTERNAL auxiliary ternary iid N14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Errors eP=P(decide Q), eQ=Q(decide P); times tP=E_P tau, tQ=E_Q tau; V14(alpha)=min max(tP,tQ) with eP,eQ<=alpha.

Consume Stage154 PROOF_STAGE154.md and VERIFY_STAGE154.py (author-proved, no independent Driver acceptance). The Stage154 endpoint is

    alpha154=18373341782531446925/52808422392537808896
    V154=318626571958867301813/26404211196268904448.

At this endpoint S=(10,5,4) has Q-stop coin 0 (always continue); B=(11,0,1) stays strictly mixed Q/continue. The next exactly scanned dual candidate preserves B equality on dL/dK=112/129, with additional t=20479008/3386893:

    K155=L155=5736/17,
    T=(14,0,0) P/Q terminal tie; B Q/C tie,
    680-state Bellman; 1238 positive gaps; minimum 4961/892296,
    H(root)=459776515302494289181/1862537719238885376.

This is only an exact dual candidate, NOT a proved primal interval.

First scientific question: compute literal ordered first-hit B/T prefixes and P/Q masses; determine their overlap or ancestry. Compute all four deterministic observer corners independently via exact conditional Fraction recursion and literal integer-weight DFS. Keep bilinear terms if history cones overlap. Solve error-equalizing legal randomization, time domination, dual attainment, entire REAL optimum interval and right sharpness, or an exact no-go witness. Reuse existing positive weighted BRC and Stage154 verifier. Preserve P000, ACTIVE worldview, portable research protocol, source exposure and actual owner/CLAIM boundaries. No native owner, Result or independent Driver acceptance is inferred.
