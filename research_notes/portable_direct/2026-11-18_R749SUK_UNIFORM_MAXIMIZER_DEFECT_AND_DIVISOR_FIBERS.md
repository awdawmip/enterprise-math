# R749SUK — Uniformly bounded maximizer defect and exact two-Port divisor fibers

Date: 2026-11-18 (Asia/Shanghai). Evidence: AUTHOR_EXACT_NOT_REVIEWED.

## Source and meaning

Continuation of R749SUJ, immutable predecessor awdawmip/enterprise-math@e1b4072bf3c57382a2c3b8068130087ffd73c00f:research_notes/portable_direct/2026-11-18_R749SUJ_FIRST_NONUNIT_Q_MAXIMIZER_COUNTEREXAMPLE.md; reuse R749SUI's uniform competitor at @7836316b174a1182703fd3595244d88460f68438. Original frozen WBRC-T30–T32 scientific inputs remain pinned to awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.

This is an **auxiliary, labeled, positive-rational two-Port feedback-bin observer** calculation. P000's six-dimensional native X6 spatial model, separately typed time, triadic closure, source and resource guards, and future-operation observer provenance remain unchanged. No native X6 physical-event admission or formal shared Task CLAIM is inferred.

For M >= 2 define U_M = {(a,u,v,d) in [1,M]^4 of integers: ad-uv=1}. Write tau=max(u,v)ad and Q=u+v-a-d. The adjacent-diagonal canonical family is a=d and {u,v}={a-1,a+1}. Write T*(M) for maximal tau over **noncanonical** members, and Opt(M) for the full labeled maximizer set.

## Theorem 1 — the zero-defect fiber is exactly canonical (all M)

For every positive determinant-one tuple, **Q=0 if and only if it is adjacent-diagonal canonical.** In particular every member of Opt(M) has nonzero integer Q.

Proof. The determinant identity is

    u Q = (u-a)(u-d)-1.                         (1)

Indeed u(u+v-a-d)=u²+ad-1-u(a+d). If Q=0 then (u-a)(u-d)=1, so either both factors are +1 or both are -1. The +1 case gives a=d=u-1, v=u-2; the -1 case gives a=d=u+1, v=u+2. Both are exactly the canonical adjacent-diagonal family (with opposite orientations). Conversely its off-diagonal sum is 2a, equal to a+d. QED.

This replaces the syntactic canonical exclusion by the intrinsic relational observable Q != 0, without forgetting the labeled Port directions.

## Theorem 2 — a complete exact divisor-fiber parametrization

For an oriented tuple with u=max(u,v) >=2, put x=u-a and y=u-d. For each fixed integer q its Q=q fiber is in bijection with integer triples (u,x,y) satisfying

    2 <= u <= M,
    x*y = q*u + 1,
    u-M <= x,y <= u-1,
    1 <= u-x-y+q <= u,

via

    a=u-x, d=u-y, v=u-x-y+q.                    (2)

The remaining u=1 cases are (a,u,v,d)=(1,1,1,2),(2,1,1,1), with Q=-1. Equation (2) retains the exact labeled integer divisor pair, not merely the product q*u+1. Proof: substitute the inverse formulas in ad-uv and obtain xy-qu=1; the displayed bounds express exactly a,d in [1,M] and v in [1,u]. Conversely these equations imply ad-uv=1 and the required range. QED.

Thus any proposed shortcut based solely on |Q|=1 discards genuine divisor fibers, including the known M=58 and 93 optimal Q=2 witnesses.

## Theorem 3 — bounded defect of ALL threshold maximizers

For every integer M >= 2 and every noncanonical labeled maximizer,

    |Q| <= 20.                                 (3)

Further, for every M >= 249999 the analytic argument alone proves

    |Q| <= 16.                                 (4)

The bound (3) combines a rigorous infinite-range estimate with a complete finite exact certificate; (4) needs no finite search. Neither constant is claimed sharp.

### Infinite-range proof

Reuse the explicit R749SUI noncanonical competitor for M >=15: let

    t=floor(sqrt(M+1)), m=t²-1, delta=M-m in [0,2t],
    W=m(m-t)².

Its determinant is one and its tau equals W. The product union bound gives

    0 <= M³-W <= (3delta+2t) M².

Put B=3delta+2t <=8t. For an oriented maximizer u=max(u,v), tau=uad >= W, with u,a,d <=M; therefore u,a,d >=M-B. Put h=M-u, r=M-a, s=M-d, S=h+r+s, D=M³-uad. Then 0<=h,r,s<=B, 0<=D<=BM², and

    D=M² S-M(hr+hs+rs)+hrs
     >= M² S(1-B/M),                           (5)

because hr+hs+rs <= B S. Whenever B<M, equation (5) yields S <= B/(1-B/M).

Let x=u-a=r-h, y=u-d=s-h. When u>=2 and v<=u, x,y cannot both be nonpositive: if either is zero then uQ=-1 contradicts integrality; if both are negative then (1) gives Q>=0 while Q=x+y+(v-u)<0. If x,y are positive, xy <=rs <= S²/4; if signs are opposite, |xy|<=rh or sh <=S²/4. Hence

    |uQ|=|xy-1| <= S²/4+1.                     (6)

For t>=100, M>=t²-1 implies B/M<=8t/(t²-1)<=1/12. Thus

    S <= (96/11)t,
    u >= (11/12)(t²-1),

and combining with (6),

    |Q| <= [ (2304/121)t²+1 ] /
           [ (11/12)(t²-1) ] < 21             (t>=100).

The final strict inequality follows by clearing positive denominators (its coefficient difference is 303/1452 times t², exceeding the fixed remainder for t>=100). Since Q is an integer, |Q|<=20 for all M>=9999.

For t>=500, instead B/M<=8t/(t²-1)<=1/60, giving

    S <= (480/59)t,
    u >= (59/60)(t²-1),
    |Q| <= [ (57600/3481)t²+1 ] /
           [ (59/60)(t²-1) ] < 17.

Thus |Q|<=16 whenever floor(sqrt(M+1))>=500, equivalently M>=249999. The u=1 case directly has Q=-1.

### Finite certificate needed for (3)

The companion dependency-free C++17 certificate exhaustively enumerates all oriented positive determinant-one candidates with maximum entry <=10000 **once**, using gcd(a,u)=1, the inverse residue d=a^(-1) mod u, and all positive d in that residue with v=(ad-1)/u <=u. Each candidate enters the exact bucket L=max(a,u,d); the running maximum across L<=M therefore equals T*(M) for every M<=10000. Equal-score Q fibers are retained, and an independently implemented (a,d,u)-brute-force enumeration crosschecks every M=2..120.

The execution passed. For ALL M=2..10000, the maximizing Q values are only {-1,1,2}; the only M with any nonunit maximizer defect are exactly 58 and 93, with scores 127890 and 579576. The count of enumerated **oriented noncanonical** candidates at M=10000 is 60,779,744. In particular this covers M<9999. Together with the analytical argument it proves (3), subject to the explicit finite certificate's correctness, which remains author-verified and not independently reviewed.

The finite scan does **not** prove Q in {-1,1,2} for arbitrary M, eventual unit defect, or an infinite nonunit-optimal family. The universal boundedness statement only concerns threshold **maximizers**, not every feasible determinant-one Port tuple.

## Reproducibility and provenance

Companions: R749SUK_Q_FIBER_UNIFORM_BOUND_CERT.cpp and R749SUK_Q_FIBER_RESULTS.json, stored beside this note. Compile with a C++17 compiler using -O3, run with no arguments (N=10000), and compare exact stdout JSON with the companion result. Signed 64-bit arithmetic safely covers all products through M=10000; the exact modular inverse and exhaustive loops use integers only, no floats. Each finite M has a complete candidate-domain argument as above. The analytical infinity-range arguments are separate handwritten proofs.

## New research frontier

Determine whether the true eventual optimal defect is |Q|<=2 or even |Q|=1, or exhibit a Q=3 maximizer beyond the 10000 exact search. Exploit the factor pair condition xy=q*u+1 and determinant-one Farey structure to obtain a sharper universal bound without a large finite base case. Independently require an explicit source-pinned six-coordinate native Cell/Link/Port event with triadic lift, resource/time guard and a preservation map before transferring auxiliary Port observations to the real X6 event interface.

Scientific evidence: AUTHOR_EXACT_NOT_REVIEWED; no shared CLAIM/Result/Review/working-truth promotion.