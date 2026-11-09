# PREFIX-653-R6 — BRC variance boundary exclusion and four-slot shape extrapolation

Date: 2026-11-10 (Asia/Shanghai). Mode: independent TASK_RESEARCH. Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Status: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Model, target and immutable predecessors

Mother target: the global maximum of discrete marked sampling-stop variance for the frozen signed two-informative-direction BRC 189-layer first-stop statistical observer. Its retained provenance/branch structure is the frozen BRC observer, not a newly constructed native two-dimensional plane.

Let Y(p,z) be the Poissonized maximum of the two first-stop clocks; mu=E[Y], W=Var(Y), and T_q the corresponding discrete count. The exact inherited relation (PREFIX-622,645) is

Var(T_q) = q^2 W - q mu = q^2 F_q,   F_q = W - mu/q.

We use the continuous center-strip certificate of PREFIX-643 and the cumulant interval and shape formulae of PREFIX-649. Native 96-port dynamics and original 189-layer survivors are inherited; neither was re-executed this round.

## Theorem 653.1 — Reduction of the variance maximum on a continuous parameter strip

Write L=3/20, R=1/6, z0=19/128, h=2^-18, Z0=[z0-h,z0+h]. The inherited PREFIX-643 theorem states for every real 12<=q<=24, z in Z0 and p in [L,R],

  F_q,pp(p,z) > 1930.

Then for every interior L<p<R,

  Var(T_q)(p,z)
  < max{Var(T_q)(L,z), Var(T_q)(R,z)} - 965 q^2 (p-L)(R-p).

In particular,

  max_{p in [L,R], z in Z0} Var(T_q)(p,z)
  = max_{z in Z0} max{Var(T_q)(L,z), Var(T_q)(R,z)}.

At p=(L+R)/2=19/120, the strict variance gap from the larger first-coordinate endpoint exceeds 193/20 (q=12) and 193/5 (q=24).

**Proof.** For fixed q,z, set f(p)=F_q(p,z), theta=(p-L)/(R-L). From f''>1930, the function f(p)-(1930/2)p^2 is strictly convex. Thus

  f(p) < (1-theta)f(L)+theta f(R)
         - (1930/2)(p-L)(R-p)

for L<p<R. Multiply by q^2 and use Var(T_q)=q^2 F_q. Continuity on a compact rectangle gives an attained maximum, which must be on an edge p=L or p=R. The midpoint factor is (1/120)^2=1/14400, giving gaps q^2*193/2880, equal to 193/20 and 193/5 for q=12,24. QED.

The remaining discriminating scalar is the exact boundary difference D_q(z)=Var(T_q)(R,z)-Var(T_q)(L,z). Certifying its sign on Z0 identifies the controlling p edge; then the strip maximum is a one-coordinate boundary optimization.

## Theorem 653.2 — Strict one-sided fourth-order shape extrapolation

On the inherited PREFIX-649 parameter rectangle |p-1/6|<=2^-29, |z-19/128|<=2^-29, set a=E[Y], b=Var(Y), c=kappa3(Y), d=kappa4(Y). The exact prior enclosures are

  108<a<110, 335<b<338, -1266<c<-1153, 14638<d<86111.

For t=1/q in [0,1/12], B=b-a*t>325. The previous exact cumulant transforms give skewness g1(t) and excess kurtosis g2(t):

  g1(t) = (c-3*b*t+a*t^2) / B^(3/2),
  g2(t) = (d-6*c*t+7*b*t^2-a*t^3) / B^2.

Four differentiations yield exact identities

  g1''''(t) =
   -15*a^3*(a^2*t^2+5*a*b*t-63*a*c+120*b^2)/(16*B^(11/2)),

  g2''''(t) =
    24*a^2*(5*a^2*d+11*a*b^2*t-6*a^2*c*t-24*a*b*c+19*b^3)/B^6.

All numerator bracket terms in these signed expressions are positive. Bounding positive terms using a<110, b<338, -c<1266, d<86111, t<=1/12, B>325 and sqrt(B)>18 yields

  -215605092307/501245550000 < g1''''(t) < 0,
  0 < g2''''(t) < 82383535243328/47136806640625.

Exact rational verification shows the useful simplified bounds

  -1/2 < g1''''(t) < 0 < g2''''(t) < 7/4.

For any model-admissible q>=12, define R_i(q) for i=1,2 using four slot values:

  R_i(q) = -gamma_i(q)/21 + (2/3)*gamma_i(2q)
           -(8/3)*gamma_i(4q) + (64/21)*gamma_i(8q),

where gamma_i(q)=g_i(1/q). Then

  0 < R_1(q)-gamma_1(infinity) < 1/(3072*q^4),

  -7/(6144*q^4) < R_2(q)-gamma_2(infinity) < 0.

At q=12 the absolute errors are strictly below 1/63700992 and 7/127401984. q=48 and q=96 are derived mathematical observer values rather than newly executed native-sampling runs.

**Proof.** The Lagrange interpolation weights at evaluation point t=0 for nodes t,t/2,t/4,t/8 are (-1/21,2/3,-8/3,64/21). They reproduce degree zero and cancel degrees 1,2,3. For a C^4 function g, interpolation's remainder at zero is

  g(0)-R(q) = g''''(xi)*t^4/(4!*2*4*8)
            = g''''(xi)/(1536*q^4), 0<xi<t.

Insert the strict fourth-derivative signs and bounds. QED.

## Verification, provenance, uncompleted unit

The companion Python-stdlib Fraction certificate checks 21 exact rational assertions: strip width and midpoint variance margins, interpolation weight moment equations, derivative upper bounds, and both q=12 error margins. Local execution returned ALL_CHECKS_PASS 21. Symbolic differentiation of both fourth-derivative identities was independently checked with SymPy at derivation time. This is a precise mathematical implication certificate built on earlier results, not independent mathematical review or new original-graph computation.

Dependencies:
- PREFIX-643: ae7872ca18676397fcc0dd9424fb77e08928bee7 / research_notes/portable_direct/2026-11-09_prefix643_r6_binomial_score_146fold_valley_strip.md
- PREFIX-645: f11c0345bf89321aba48d90671c244bdec25d416
- PREFIX-649: cb21c9452f5bc094493cd92bfa37be99ab988782
- PREFIX-651: fffa4e08af63ebf4caff3117a6ffcfa88a3d0b8f

Next exact unit: compute rational Bernstein/interval certificates for D_12(z) and D_24(z) on Z0, with any isolating subintervals for unresolved sign. Distinguish the strip boundary reduction from the full two-parameter global maximum, which remains the parent objective. Formal CLA(I)M/Result/Review and independent admission were not created by this research note.
