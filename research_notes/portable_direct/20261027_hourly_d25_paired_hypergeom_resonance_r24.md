# D25/LIFT R24 — Paired W/S hypergeometric rank jets and non-removable finite-field boundary sources

2026-10-27, Asia/Hong_Kong. TASK_RESEARCH lane: chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Mother D25/LIFT/JT2 OPEN.

AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This evidence is not a native Source checkpoint, CM/Frobenius experiment, frozen Result or Driver review.

## Exact prior inputs and source types

Consume without recredit R22 (953a90bc8d1d8cf252c1e671741a4b7d5e3625e8) and R23 (a88573ebcb030a8ddedc6a3d8020805ec88cb1d7). The external Guo–Zudilin two-truncation S supercongruence from *A q-microscope for supercongruences*, Adv. Math. 346 (2019), arXiv:1803.01830, is a proved input only for S, not an identity between W and S.

For p=6m+1>=7 prime in F_p, R23 gave these genuinely distinct p²-divided, Wilson-reflected source terms for 2m<=j<=3m-1:

    A_j=(6j+5)*216^j*(j!)^5 / ((2j+1)!*(3j-6m+1)!),   W-high;
    B_j=2*(8j+7)*2304^j*(j!)^4 / (4j-6m+2)!,        S-mid;
    U_p = sum_(j=2m..3m-1) A_j;   M_p = sum_(j=2m..3m-1) B_j.

R23's external-input-supported identity M_p+T_p=0 concerns the S full-sum observer; it does not remove the W-high source U_p.

## Theorem A: a shared numerator, two different exact observer ports

Use theta=X*d/dX, reduced rational Pochhammers in F_p, and 0<=r<=m-1:

    a_r = ((2/3)_r)^3 / ((7/6)_r*(4/3)_r*r!);
    b_r = ((2/3)_r)^3 / ((11/12)_r*(7/6)_r*(17/12)_r);
    F_W(X)=sum_(r=0..m-1) a_r*X^r;
    F_S(X)=sum_(r=0..m-1) b_r*X^r.

All denominators are p-units within this strict cutoff. The r=m hypergeometric coefficient is NOT defined by these fractions; do not cross its singularity.

    C_m=3*216^(2m)*((2m)!)^5/(4m+1)!
       =-9*216^(2m)*((2m)!)^6 !=0  (mod p);
    D_m=2*2304^(2m)*((2m)!)^4/(2m+2)! !=0  (mod p).

Then, term by term,

    A_(2m+r)=C_m*(2r+1)*2^r*a_r  (mod p);
    B_(2m+r)=D_m*(8r+13/3)*9^r*b_r  (mod p).

In particular, the genuine source totals have rank-jet readouts

    U_p=C_m*[F_W(2)+2*theta F_W(2)];
    M_p=D_m*[(13/3)*F_S(9)+8*theta F_S(9)]       (mod p).

Proof. In the exact R23 factorial source, substitute j=2m+r and divide by the unit r=0 factorial block. The ratios are

    A_(2m+r)/C_m = ((12m+6r+5)/(12m+5))
         * 216^r*(2m+1)_r^5/[(4m+2)_(2r)*(2)_(3r)];
    B_(2m+r)/D_m = (16m+8r+7)
         *2304^r*(2m+1)_r^4/(2m+3)_(4r).

Modulo p, 2m+1=2/3, 4m+2=4/3, 2m+3=8/3, 12m+5=3, and 16m+8r+7=8r+13/3. Use the exact Pochhammer factorization laws

    (4/3)_(2r)=4^r*(2/3)_r*(7/6)_r;
    (2)_(3r)=27^r*(2/3)_r*(1)_r*(4/3)_r;
    (8/3)_(4r)=256^r*(2/3)_r*(11/12)_r*(7/6)_r*(17/12)_r.

The constants become 216/(4*27)=2 and 2304/256=9, with the common (2/3)_r^3 numerator. Wilson gives (4m+1)!*(2m-1)!=1 mod p and 2m=-1/3 mod p, hence C_m=-9*216^(2m)*((2m)!)^6. Rank-jet summation proves the displayed U,M formulas. QED.

## Theorem B: exact inhomogeneous Picard–Fuchs boundary, W source

Let

    L_W=theta*(theta+1/6)*(theta+1/3)-X*(theta+2/3)^3.

Then for every prime in scope,

    L_W F_W(X)=(a_(m-1)/8)*X^m,  a_(m-1)!=0  in F_p[X].   [W]

Indeed for 1<=r<m, the exact recurrence is

    r*(r+1/6)*(r+1/3)*a_r=(r-1/3)^3*a_(r-1).

All coefficients below X^m cancel. At X^m the absent term leaves -(m-1/3)^3*a_(m-1); m=-1/6 mod p makes this +a_(m-1)/8. Every factor in a_(m-1) is a unit; (7/6)_m first vanishes at r=m.

Sharp impossibility: no formal series f in F_p[[X]] with f(0)=1 solves L_W f=0. Unit coefficient equations uniquely force f_r=a_r through r=m-1. At r=m, the coefficient of f_m is m(m+1/6)(m+1/3)=0 whereas the required previous-term coefficient (m-1/3)^3*a_(m-1) is nonzero. No adjustment of f_m can erase this finite-field boundary. This does NOT exclude an inhomogeneous transfer or an alternate gauge/operator. QED.

## Theorem C: a different, independently nonzero S boundary

Let

    L_S=theta*(theta-1/12)*(theta+1/6)*(theta+5/12)
        -X*(theta+1)*(theta+2/3)^3.

Then

    L_S F_S(X)=-(b_(m-1)/48)*X^m,  b_(m-1)!=0  in F_p[X]. [S]

For 1<=r<m the exact coefficient recurrence is

    r*(r-1/12)*(r+1/6)*(r+5/12)*b_r
       =r*(r-1/3)^3*b_(r-1).

At r=m, the leading factor m+1/6=0, but the right source is -m*(m-1/3)^3*b_(m-1)=-b_(m-1)/48, a unit multiple of b_(m-1). Hence no normalized homogeneous F_p[[X]] solution extends this finite source, for the same sharp coefficient obstruction. Despite their common numerator, W and S have different operator orders, rational coefficients and boundary sources; no termwise equality is claimed.

As an exact weighted source counterexample to naive unit-proportional pairing, p=13,m=2,j=2m gives B_j=0 mod13 (its weight 8j+7=39), while A_j=C_m=9 mod13. This does not disprove any WZ telescope that keeps extra source/endpoint terms. QED.

## Relation to the still-open original scalar

R23's source-faithful reduction of the desired p³ bridge was

    sum_(k=0..3m)(w_k-s_k)=-p²*U_p  (mod p³).  [OPEN]

Substituting the now-proved rank jet yields the equivalent, *still unproved* condition

    [p^(-2)*sum_(k=0..3m)(w_k-s_k)] mod p
        + C_m*[F_W(2)+2*theta F_W(2)]=0 in F_p,

where the p² quotient is defined using the accepted first-digit input. Separately the proved external S half-truncation gives T_p=-M_p=-D_m*[(13/3)*F_S(9)+8*theta F_S(9)]. Neither relation proves W=S. A future cross-port WZ transformation must carry the exact inhomogeneous W/S boundaries as typed source data rather than erase them.

## Executed exact arithmetic and source preservation

The accompanying standard-library Python checker independently rebuilds R23's A_j/B_j factorial sources and both normalized recurrence coefficient arrays, verifies every j=2m+r term identity, checks all coefficients of the two differential operators through X^m, verifies that both boundary coefficients are nonzero, and checks both rank jets. Executed PASS for all 148 primes 7<=p<2000, p=1 mod6. These are exact F_p calculations; the general propositions are proved by algebra, not by finite sampling.

Selected records (all entries taken modulo p):

| p | U | C | F_W(2) | theta F_W(2) | W boundary | M | D | F_S(9) | theta F_S(9) | S boundary |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 10 | 9 | 2 | 1 | 9 | 7 | 1 | 10 | 9 | 10 |
| 19 | 9 | 13 | 4 | 2 | 16 | 3 | 17 | 3 | 16 | 2 |
| 181 | 152 | 70 | 17 | 171 | 62 | 0 | 83 | 132 | 19 | 6 |
| 373 | 266 | 203 | 334 | 361 | 251 | 92 | 200 | 66 | 10 | 15 |
| 733 | 67 | 168 | 420 | 665 | 729 | 174 | 461 | 232 | 20 | 55 |

For p=181 (an earlier genuine S-tail cancellation), M=T=0 but U=152 !=0; both operator boundary sources remain nonzero. The p=13 weighted-zero example is an independent warning against losing the origin/weight information.

BRC COMPOSE_APPLIED. The typed carrier retains series W/S, index j=2m+r, true p² filtration, factorial provenance, finite-field coefficient arrays, distinct theta readouts, r=m singular cutoff, and two nonzero inhomogeneous residuals. A shared numerator justifies partial algebraic compression, not source-identity or exact post-operation erasure. No P000 native axis or physical CM statement is inferred.

## Recovery, non-repeat and next action

Previously successful own read-only recovery #6571 and complete continuation #6572/#6573/#6574: current Research service session MCP-3a7c6c3a67bd4e52b1cdf49064751829; no pending mutation, authorized run, unopened own claim or unpublished own uploads; two neutral protected staging dispositions. Actual Source continuation reports persisted_checkpoint=SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED, NO_LIVE_CLAIM, NEEDS_DISPATCH, execution_authorized=false, old latest claim MCP-d0d70cd041b01e5db192870a versus checkpoint claim MCP-87631b892b41fa18d799f2d8. Current native status v0.6.11 research_authority_granted=false. These read-only projections do not grant role/write authority. Control owner remains enterprise-math#1558. No session_close, new Researcher impersonation, claim/open/checkpoint/freeze/review or maintenance-lane writes occurred.

NEW PORTABLE UNITS: the paired W/S finite-source hypergeometric rank jets; two all-prime nonzero forced finite-field boundary operators and formal-series no-extension certificates; 148-prime exact checks. Do not recredit R22/R23, accepted UR/JT0, previous Source-completed units, native experiments or other lanes. Registration/Source publication of this increment remains REGISTER_PENDING / SYNC_DEBT.

NEXT exact mathematical step: construct or disprove a source-preserving finite WZ/contiguous transfer from this paired coefficient/derivative interface to the explicitly unsolved low-half p² defect. In a proposed transfer track both forcing terms [W] and [S] and the p=13 weight-zero port. Separately original-class H0/B0, [X]U mod p², semilinear eta, kappa, genuine p373 native CM runtime and independent Driver remain NOT_DONE; native runtime cannot be replaced by this finite-field proof. Scientific pin and ACTIVE P000/worldview unchanged; no scheduler/Actions/cron changes.