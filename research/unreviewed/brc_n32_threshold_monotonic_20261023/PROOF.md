# BRC N32: Strictly increasing single-pulse thresholds and finite positive-gain lifespan

Status: AUTHOR-SIDE EXACT DERIVATION; UNREVIEWED; NOT A FORMAL TASK RESULT; NOT ADMITTED.
Date: 2026-10-23. Scope: independent nonadaptive four-label positive-mass auxiliary occupancy observer, NOT native P000 X6 dynamics.

## Source pins and transport limitations

GLOBAL_KNOWLEDGE_V1 canonical main at 7a56e3a5a31c6af97f47a09befb54ae4443c9b41; P000 original Blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (verified matching P000_STARTUP projection). Enterprise Math main pinned to f768a9f34aa7b0a9521325c52e0638dc7fba0a27; current portable-research protocol docs/PORTABLE_RESEARCH_PROTOCOL.md at Blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5c. Reuses N31 author note research/unreviewed/brc_uniform_pulse_20261023/N31_AUTHOR_THEOREMS.md at commit b70c8cf71b9557569da66eddf44ebdd4057d082c.
Control em_control_tasks returned CONTROL_QUOTA; em_session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Active Owner, native Researcher ID, CLAIM, review and admission were NOT established. This is a non-canonical unreviewed research document.

Reuse: REUSE_APPLIED, existing N31 exact occupancy formula and positive Weighted-BRC hidden-label provenance, not signed branch amplitudes or an X6 embedding.

## Exact question and polynomial

For one protected action-2 pulse after k-1 action-0 rounds, the N31 author result states that for every n>k>=4 and z in [0,1],

    R_n-R_(n-1) = max(Z_n(z),0)/3^n,

    Z_n(z)=4-2^(n-2)-2(1-z)(2+z)^(n-2)
           -(1+z)(2-z)^(n-2)+(2-z)(1+z)^(n-2).

Here the observer is the probability that the independent hidden-label occupancy set is one of {0,1},{1,2},{1,3},{2,3}; R is the stated cumulative positive increment less its historical maximum. This formula is only a post-pulse statement; do not apply it to t=k itself.

Set m=n-2>=2, F_m(z)=Z_(m+2)(z), and w=1-z. Directly,

    F_m(1-w)=4-2^m-2w(3-w)^m-(2-w)(1+w)^m
             +(1+w)(2-w)^m.                            (1)

## Lemma 0: unique positive root, restated with a self-contained argument

For each m>=2 the coefficients of F_m, in increasing powers of z, are
A_(m,0)=6-4*2^m, A_(m,m+1)=1+(-1)^(m+1), and for 1<=j<=m,

    A_(m,j)=(2+(-1)^j)*2^(m-j)*(2*C(m,j-1)-C(m,j))
            +2*C(m,j)-C(m,j-1).

For m>=4, put r=j/(m+1-j), H=(2+(-1)^j)*2^(m-j). Then

    A_(m,j)/C(m,j)=H(2r-1)+2-r.

When 3j>=m+1, r>=1/2 so the expression is at least r+1>0.
When 3j<m+1, r<1/2 and (2-r)/(1-2r)=1+(m+1)/(m+1-3j)<=m+2,
whereas H>=2^ceil(2m/3)>m+2. To verify the final strict bound for
all m>=4: m=4,5,6 give respectively 8>6,16>7,16>8, and adding 3 to m
quadruples the left side while adding only 3 to the right side.
For m=2,3, direct expansion gives
F_2=9z^2+3z-10 and F_3=2z^4+4z^3+21z^2+z-26.

All polynomials therefore have exactly one coefficient sign change in
descending order. Descartes' rule gives at most one positive root counted
with multiplicity; F_m(0)=6-4*2^m<0 and F_m(1)=2>0 give a root in (0,1).
Hence the unique positive root theta_(m+2) is simple, with F_m negative
below it and positive above it in [0,1]. This is the existing author-side
N31 root lemma, restated, not an independent Driver verdict.

## Lemma 1: uniform exact rational root localization

For every integer m>=2,

    1-2/3^m < theta_(m+2) < 1-1/(2*3^m).               (2)

PROOF. For 0<=w<=1, use (2-w)^m<=2^m,
(1-w/3)^m>=1-mw/3 and (1+w)^m>=1 in (1):

    F_m(1-w) <= -2+w*(2^m+1+4m/3).                    (3)

At w=2/3^m this upper bound is
-2+2*((2/3)^m+(1+4m/3)/3^m).
The summands decrease with m>=2 and their sum at m=2 is 23/27.
Therefore F_m(1-2/3^m)<=-8/27<0.

For the other endpoint use
(2-w)^m>=2^m*(1-mw/2), (1+w)>=1,
(3-w)^m<=3^m, and (2-w)<=2:

    F_m(1-w) >= 4-m*w*2^(m-1)-2*w*3^m-2*(1+w)^m.     (4)

At w=1/(2*3^m), this is at least

    1-m*2^(m-1)/(2*3^m)-2*((1+w)^m-1).

For m>=2, m*(2/3)^m<=8/9 and m*w<=1/9. Since C(m,j)<=m^j,
(1+w)^m<=sum_(j>=0)(mw)^j=1/(1-mw)<=9/8. Hence (4)
is >=1-2/9-1/4=19/36>0. The single-root sign property proves (2). QED.

## Theorem 2: strict monotonicity, with a uniform gap

For every integer n>=4,

    theta_n < theta_(n+1) < 1,
    Z_(n+1)(theta_n) < -2/5.                            (5)

PROOF. Put m=n-2, z=theta_n, w=1-z. Exact expansion gives

    F_(m+1)(z)-2F_m(z)
       =-4-2zw(2+z)^m+z(1+z)(2-z)^m
          -w(2-z)(1+z)^m.                              (6)

By Lemma 1, 0<w<2/3^m, so mw<2m/3^m<=4/9 for m>=2.
The binomial/geometric bound gives

    (1+w)^m <=1/(1-mw)<9/5.

Therefore 0<z(1+z)(2-z)^m<2*9/5=18/5. All other terms
in the right side of (6), aside from -4, are negative. At
z=theta_n, F_m(z)=0; thus F_(m+1)(theta_n)<-4+18/5=-2/5.
Since F_(m+1) changes from negative to positive at its one
positive root, theta_n<theta_(n+1). QED.

This is an all-integer-n proof; no floating numerical root comparisons
and no finite cutoff or asymptotic unproven premise are used.

## Consequences: no post-pulse gain resurrection; finite horizon

For a fixed parameter z in [0,1) and pulse k>=4, the post-pulse positive
residual increments are exactly those n>k with z>theta_n. Since theta_n
strictly increases, such n form an initial interval (possibly empty).
Once a post-pulse increment is nonpositive, subsequent post-pulse increments
cannot become positive again. This does not classify the pulse round,
pre-pulse transients, or arbitrary multi-pulse protective words.

The rational/integer stopping certificate is

    (1-z)*3^(n-2) >= 2   ==>   Z_n(z)<0.                (7)

For any such n>k, R_n-R_(n-1)=0, and the same holds for all larger rounds.
In contrast, z=1 yields Z_n(1)=2 for every n>=4, hence every post-pulse
gain equals 2/3^n. Consequently z=1 is a singular boundary for
the duration of post-pulse positive gain within this observer,
not a physical transition claim.

In particular,

    1/(2*3^(n-2)) < 1-theta_n < 2/3^(n-2),

and theta_n increases to 1. The finer leading-asymptotic constant
from N25 is not re-proved here.

## Exact validation and limitations

The companion pure-Python Fraction checker verifies (for 4<=n<=50) 47
pairs of rational sign brackets and 376 recurrence instances, plus
13 exact dyadic isolating intervals and 4 fixed-parameter stopping
examples. These finite checks are evidence against transcription
mistakes; the argument above supplies the all-n proof.

No n=31+ full strategy classification, no global second-rebound
minimal-length update, no non-single-pulse theorem, no native X6
faithfulness bridge, no formal CLAIM, independent Driver review, or
canonical Source acceptance has been obtained.

Next exact task: two action-2 pulse strategies of the form
0^a 2 0^b 2 0^c with a>=3,b>=1,c>=1. Retain pulse order and the
full 16 occupancy states; determine whether a post-second-pulse
strict negative-to-positive revival occurs or establish a typed
invariant precluding it. A total-count-only quotient is not
automatically sufficient under pulse insertion.
