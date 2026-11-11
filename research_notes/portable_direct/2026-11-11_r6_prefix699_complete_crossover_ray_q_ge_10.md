# PREFIX-699-R6 — Glue BRC observer crossing bridge to the singular ray

Date: 2026-11-11 Asia/Shanghai.
Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Evidence: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.

This is an auxiliary two-branch 189-row BRC *observer* result, not a native heartbeat evolution or 6D geometric theorem. The labelled Y(z,z), Y(0,z), survivor counts and K/J moment kernels are retained.

## Theorem 699.1 — Complete integer parameter ray

Define A(z)=Var(Y(z,z))-Var(Y(0,z)), B(z)=E[Y(z,z)]-E[Y(0,z)], Q(z)=B(z)/A(z) and F_q(z)=qA(z)-B(z). Let

    L=211/4000=0.05275
    R=213/4000=0.05325
    S=2663/50000=0.05326
    U=53261/1000000=0.053261

Let z_A in (S,U) be the unique A-zero certified by PREFIX-682/683/684 and used in PREFIX-687.

On (L,z_A), A,B are positive, A'<0, B'>0, and Q is analytic and strictly increasing with lim_(z->z_A-) Q(z)=+infinity. Moreover

    9.166464293188 < Q(L) < 9.166464293189.

For any real q, the equation qA(z)=B(z) has exactly one solution in (L,z_A) if and only if q>Q(L). For every nonnegative integer q this holds if and only if q>=10. The crossing is transverse, F'_q(z_q)<0. The inverse z(q) is analytic and strictly increasing.

Spatial partition by integer q:

* 10<=q<=446: z_q in (L,R), inherited from PREFIX-698.
* 447<=q<=9872: z_q in (R,S), established by the new connector lemma.
* q>=9873: z_q in (S,z_A), inherited from PREFIX-687.

The new connector also obeys Q'(z)>29,000,000, yielding for 447<=q<=9871:

    0 < z_(q+1)-z_q < 1/29,000,000.

## New connector lemma on the missing interval [R,S]

At b=53/1000, use the exact 10^8-scaled derivative floor ticks through j=5 from PREFIX-695:

    a=[44000296,-168056589514,-6667624082229,
       39352687679231,3189837819999830,-36266294695911132]
    c=[789752024,12845959424,-99127959112,
       -1326952329685,-14895243921676,-1960958310350017]

These encode a_j < 10^8*A^(j)(b) < a_j+1 and c_j < 10^8*B^(j)(b) < c_j+1. Reuse the global sixth-derivative envelopes from PREFIX-693/695:

    M_A=201273663850076722544640
    M_B=17896441402901698560.

For h=S-b=13/50000 and G=A,B, Taylor's theorem and strictly enclosing rational floor ticks give, for k=1,2,

    g_k/10^8-E_(G,k)(h) < G^(k)(z) <
        (g_k+1)/10^8+E_(G,k)(h),  |z-b|<=h,

    E_(G,k)(h) =
       sum_(j=k+1)^5 max(|g_j|,|g_j+1|)*h^(j-k)/
                           (10^8*(j-k)!)
       + M_G*h^(6-k)/(6-k)!.

The companion Python Fraction program verifies, for the entire [b,S],

    -40,000,000 < A''(z) < 40,000,000
    128 < B'(z) < 129.

By PREFIX-687, A'(S)<-1600. Since S-R=1/100000, the mean value theorem proves for all z in [R,S],

    A'(z) < -1600 + (40,000,000)/100000 = -1200.
    B'(z) > 128.

At S, PREFIX-685 gives A(S)>803334881118283114227/10^24>0 and B(S)>7930886194096894324395803/10^24>0. The signs of derivatives show A,B positive on [R,S]; B(R)>7.92 also follows independently from PREFIX-698. PREFIX-698 proves A>0,B>0,A'<0,B'>0 on [L,R]. PREFIX-687 proves the same needed signs on [S,z_A), since z_A is the unique zero of A in [S,U] and B>7.93 there. Thus the monotonicity is glued across the full open interval (L,z_A).

For any z in (R,S), A(z)<A(R)<0.018, B(z)>B(R)>7.92; hence

    Q'(z)=(B'(z)A(z)-B(z)A'(z))/A(z)^2
         > (7.92*1200)/(0.018^2)
         > 29,000,000.

## Exact endpoint classification

The inherited strict rational endpoints (all comparisons exact):

    9.166464293188 < Q(L) < 9.166464293189  [PREFIX-698]
    446.012343644423 < Q(R) < 446.012343644424 [PREFIX-698]
    9872.453419496357 < Q(S) < 9872.453419496358 [PREFIX-685 corrected]

A(z_A)=0, A(z)>0 for z<z_A, B(z_A)>0, and A,B are polynomials. It follows that Q:(L,z_A)->(Q(L),infinity) is an analytic increasing bijection, establishing the exact integer partition without enumeration. For q>Q(L), the inverse function theorem gives analytic z(q), and F'_q=qA'-B'<0.

## Evidence, scope, next unit

Companion proof checker: PREFIX699_R6_GLUED_BRANCH.py.
Machine evidence: PREFIX699_R6_RESULTS.json.
Local exact-rational run: ALL_CHECKS_PASS PREFIX699-R6.

The checker verifies the Taylor implication and endpoint arithmetic from existing independently preserved author certificates; it DOES NOT reexecute the 189-row recurrence. Frozen provenance: PREFIX-685/687/693/695/698; immutable science pin is unchanged. Result has not passed independent mathematical review or formal Source Result admission.

Remaining mother objective: maximize sampled variance over the full *auxiliary* triangle 0<=p<=z<=1/2, with particular attention to two-parameter interior candidates and other boundary comparisons. Next unit: reuse PREFIX-675 edge comparison to derive a certified two-parameter sign or extremum partition; the q>=10 edge-crossover classification is now complete on (L,z_A).
