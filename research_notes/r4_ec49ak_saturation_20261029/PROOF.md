# EC49AK — exact post-capacity support facet

Date: 2026-10-29. Author-side analytical proof plus exact rational arithmetic; PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. This theorem concerns the 18+18 positive-probability *auxiliary* BRC observer; no native signed BRC, X6 or heartbeat transfer is asserted.

## Theorem: full saturation interval and exact cutoff

Fix k=177/172 and exact first-stage cost C1=43/48. For any real 0<=eta<1/2 and every real second-stage cost 0<=C2<=25/32, the maximum of H=alpha-k beta over every legal real causal behavioral randomized strategy with erased first-stage history and fresh independent sensor/acceptance coins is EXACTLY

    Hmax(eta,C2) = (27/172) C2.

A fixed first-stage prefix attains (alpha,beta)=(C2/2,C2/3). The same upper bound holds for all feasible 25/32<C2<=43/48, but is STRICT for the maximum on that interval. Thus C2=25/32 is the exact saturation threshold of the universal information-efficiency envelope.

At epsilon=1/10 in the EC49AJ convention C2=7/8-epsilon=31/40, the sharp global value is Hmax=837/6880 with alpha=31/80, beta=31/120, and a fresh sensor coin of probability 124/125. At the inherited boundary C2=25/32, the formula yields 675/5504, exactly the EC49AJ result.

## Joint source law and actual observation protocol

Let w,z in {0,1,2}, u in {0,1}, t_eta(w,u)=1/2+(2u-1)(1-w)eta. Original strictly-positive leaves:

    P(w,u,z)= t_eta(w,u)*(1/6 if z=w else 1/12),
    Q(w,u,z)= t_eta(w,u)/9.

Both sources normalize to 1 and have the same (w,u) marginal t_eta(w,u)/3. First-stage actions A0,A1,B0,B1,STOP have costs 1,1,2,2,0. A paid action reveals action label c and bit u, NOT w or the original random seed. The post-observation S-buy probability r(c,u) is a new local coin, cost 1 and observation z if purchased. A terminal accept coin depends only on the actually observed (c,u,z) or available coarser output. Expected stage costs are exact equalities.

Define x[w,c] row-stochastic and q[w,c,u]=x[w,c]*t_eta(w,u)/3. For any paid (c,u) sensor and any acceptance vector a_z in [0,1], the contribution to alpha-k beta equals

 r(c,u)*sum_w q[w,c,u] * [ a_w*(1/2-k/3) + sum_{z!=w}a_z*(1/4-k/3) ].

The coefficients are 1/2-k/3=27/172>0 and 1/4-k/3=-4/43<0, so each square bracket is <=27/172. STOP and no-S outcomes are P/Q-uninformative; accepting there has factor 1-k<0 and cannot improve H. Therefore

 H <= (27/172) sum_{c,u} r(c,u) sum_w q[w,c,u] = (27/172) C2

for EVERY real legal causal policy, without any finite-grid assumption, convexification or shared random seed.

Equality on a purchased (c,u) with positive mass requires a_w=1 and a_z=0 for every z!=w and every w contributing q[w,c,u]>0. Since t_eta(w,u)>0, this is possible only if paid label c has positive x[w,c] from ONE history w: a 'pure label'. A mixed label purchased with positive probability forces strict loss. This equality condition is a statement about actual erased-history observability, not permission to recover w.

## One explicit all-real sharp witness

First-stage probabilities (columns A0,A1,B0,B1,STOP):

 w=0 : 1, 0, 0,     0, 0
 w=1 : 0, 1, 0,     0, 0
 w=2 : 0, 0, 11/32, 0, 21/32.

Each row sums to one. Uniform history marginals give

 C1 = (1+1+2*(11/32))/3 = 43/48,
 mass(paid)=(1+1+11/32)/3=25/32.

For each observed paid pair (c,u), buy S with an INDEPENDENT fresh coin of probability r=(32/25)*C2, in [0,1] precisely when 0<=C2<=25/32. Accept after S exactly if z=0 when c=A0, z=1 when c=A1, z=2 when c=B0; reject B1, STOP and all unpurchased outcomes. The observed label is single-history by construction, so the terminal coin never reads hidden history.

Under P, each matched z=w has conditional probability 1/2; under Q, 1/3. Hence stage-2 cost =r*(25/32)=C2, alpha=r*(25/32)/2=C2/2, beta=r*(25/32)/3=C2/3. The upper bound is met exactly. For the requested epsilon=1/10: C2=31/40, r=124/125, alpha=31/80, beta=31/120 and H=837/6880.

## Sharp capacity obstruction for larger C2

Write unnormalized first-stage totals s=total STOP, b=total B0+B1, a=total A0+A1. All row sums and C1 imply

    a+b+s=3,   a+2b=43/16,
    s=b+5/16,   a=43/16-2b,   b<=43/32.

Let p be the total unnormalized probability mass on paid action labels that are pure (used by at most one history). Claim p<=75/32:

Case 1: at most one A label is pure. Its total mass is <=1 since one history row totals one. Every pure B label together contributes <=b. Thus p<=1+b<=1+43/32=75/32.

Case 2: both A labels are pure. Two labels serve at most two distinct histories; another history must use B or STOP only, so s+b>=1. With s=b+5/16 this gives s>=21/32. Therefore p<=total paid mass=3-s<=75/32.

If H=(27/172)C2, ALL purchased positive-mass labels must be pure by the per-atom equality condition. Their total Q purchase mass is <=p/3, since r(c,u)<=1 and sum_u t_eta(w,u)=1. Hence equality forces C2<=p/3<=25/32. Conversely our construction reaches the bound at and below 25/32.

For every feasible 25/32<C2<=43/48, equality is impossible. The finite-dimensional legal-policy space, with exact costs, is compact and H is continuous; thus an optimum exists and is strictly BELOW (27/172)C2. C2 up to 43/48 is feasible, e.g. b=0, s=5/16 and fractional sensor purchases. This proves strictness for the maximum, not just for a particular witness.

## Exact capacity polytope audit at epsilon=1/10

The first-stage feasible polytope has 15 nonnegative x[w,c], three row-sum equalities, exact stage-1 cost s-b=5/16, and b<=B=1/16+3epsilon=29/80. Any vertex supported in the interior of b<B has <=4 positive coordinates (rank of equality system); on the b=B face it has <=5 (one extra active row). Exhaustively solve all independent 4-column and 5-column bases with Fraction: C(15,4)+C(15,5)=4368 exact candidate bases. The runnable checker finds EXACTLY 288 distinct feasible vertices, classified by b value as 24 at b=0, 24 at b=11/32, 240 at b=29/80. The middle value records a genuinely binding STOP/B same-row capacity s+b=1. This is a complete finite polytope audit, but the real-policy theorem relies on the analytic per-atom bound and pure-label capacity proof, not an extrapolation of this enumeration.

## Information-preservation boundary and status

The source retains the (w,u,z,c) provenance and history erasure at the observation fiber. A pure c label is a sufficient readout for this ONE terminal likelihood-ratio decision; mixed labels may lose information. No external physical-discreteness claim, signed amplitude cancellation, X6 full-cell identity, heartbeat evolution, or automatic transfer to native BRC is asserted. The exact next unit is to quantify the strictly positive mixed-label gap above 25/32 as a function of eta and C2, while separately constructing typed signed/phase carrier and future-operation observer maps.

STATUS: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.
