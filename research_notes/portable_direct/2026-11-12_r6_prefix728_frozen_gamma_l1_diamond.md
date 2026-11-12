# PREFIX-728-R6 — Exact enlarged L1 diamond for the frozen BRC–Gamma maximum

Date: 2026-11-12 (Asia/Shanghai). Mother objective: PREFIX-675. Prior frontier: PREFIX-727-R6.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Theorem: uniform witness domination on a larger continuous region

Use the same external auxiliary frozen 189-row BRC survivor observer with independent conditional unit-rate Gamma completion clocks. For p,z in [0,1/2], let Y(p,z)=max(T_p,T_z), mu=E[Y], M2=E[Y²], W=M2-mu², f_t=W-t*mu, and V_q=q² f_(1/q), for all real q>=2 (0<t<=1/2). The limiting t=0 is included in the comparison envelope.

Let c=(11/96,11/96), e=(0,73/500), and define the closed L1 diamond

    D728 = {(p,z): |p-11/96|+|z-11/96| <= 1/975}.

For every real q>=2 and every (p,z) in D728,

    V_q(e)-V_q(p,z) > (4/15)*q² > 0.

Hence no point of D728 globally maximizes the declared frozen auxiliary objective over [0,1/2]^2. This is a continuous real-parameter theorem under the pinned Gamma observer, not a native six-axis geometric assertion.

## Exact computation: re-evaluation on the enclosing interval

The predecessor PREFIX-727 derivative certificate was valid only on a square of half-width 1/2000. Its gradient bound must not be extrapolated to the larger diamond. We therefore independently recomputed all 189 frozen survivor rows under the same original strict integer width predicate and repeated the exact Bernstein maximum calculation on the larger interval

    I = [11/96-1/975, 11/96+1/975]
      = [1181/10400, 3607/31200].

There are exactly 9,529 nonzero frozen survivor cells, row 189 vanishes, and 8,904 normalized Bernstein controls b_(n,k)=w_(n,k)/C(n,k) are strictly fractional. All 189 normalized control rows are symmetric and nondecreasing towards their centers. As in PREFIX-727 this implies s'_n(x)>=0 throughout [0,1/2].

For each nonzero adjacent difference of Bernstein controls, compute the exact rational maximum on I at x=clamp(k/(n-1), I) and round each positive contribution UP to the next millionth. The checker obtains the precise integer upward-rounded totals:

    10^6 * U1 = 549269886;  U1 < 550,
    10^6 * U2 = 81257510320; U2 < 81260,

where U1 bounds sum_n |s'_n| and U2 bounds sum_n 2(n+1)|s'_n| throughout I.

An independent exact Fraction evaluation at the upper endpoint proves sum_(n<189) s_n(b) < 357/5 = 71.4. The verified symmetry/monotonicity gives E[T_x] <357/5 for every x in I, hence mu(p,z)<714/5 throughout I².

The frozen independent-Gamma nonnegative influence coefficients satisfy 0<=a_n<=1 and 0<=h_n<=2(n+1), as shown by the negative-binomial kernel identities reproduced in PREFIX-726. For all t in [0,1/2] and (p,z) in I²,

    |partial_p f_t|, |partial_z f_t|
      < 81260 + (2*(714/5)+1/2)*550
      = 238615 =: L728.

The source comparator gap from PREFIX-726 was certified by exact rational moments at both t endpoints:
f_0(e)-f_0(c)>245 and f_(1/2)(e)-f_(1/2)(c)>245.
Its affine dependence on t proves f_t(e)-f_t(c)>245 throughout [0,1/2].

Every point of D728 belongs to I², and the coordinatewise path from c stays inside I². Thus

    f_t(e)-f_t(p,z)
      > 245 - L728*(|p-c_p|+|z-c_z|)
      >= 245 - 238615/975 = 4/15.

Multiplication by q² gives the theorem.

## Geometric gain and exact discrete-grid boundary

PREFIX-727 certified the square of half-width 1/2000 and area 1/1,000,000. It lies entirely in D728 because its largest L1 displacement is 1/1000 <1/975.
The new diamond has area 2/950625. Its exact area ratio to that entire old square is 3200/1521 (>2.10); this is an explicit increase in *geometrically certified continuous territory* for the same fixed comparator.

The center c is the 384-grid vertex (44/384,44/384). Since 1/975 < 2/384=1/192, this single-center diamond is contained in the four cells adjacent to that vertex and does not fully cover any one of them. The previous whole-cell union 139018/147456 therefore remains the recorded aggregate; no additional grid cell is counted. With a certificate of the same center and L1-radius form, a whole adjacent cell requires radius >=1/192. Combining only a center gap floor of 245 with a constant coordinate Lipschitz bound would require L<=47040; the measured present bound 238615 makes further re-centering, tighter variance-gradient analysis, or direct cell-wise witnesses the relevant new calculation.

## Reproduction and next scientific question

Companion: PREFIX728_R6_FROZEN_GAMMA_DIAMOND.py; result: PREFIX728_R6_RESULTS.json. The standard-library checker reconstructs original frozen integer survivor counts, proves symmetric-unimodal normalized controls by integer cross multiplication, evaluates exact Bernstein maximum terms, uses outward upward rounding, then checks all numerical inequalities with fractions. Local execution: ALL_CHECKS_PASS PREFIX728-R6. The comparator gap is an explicitly inherited independently published exact-checked claim from PREFIX-726; the present computation does not recompute that 36,000-term pair moment sum.

Next scientific unit: calculate exact local *variance* derivative (rather than separate M2/mu envelopes) for one adjacent 384x384 cell and attempt a full-cell constant-comparator or switched-comparator certificate, checking inherited-grid disjointness before adding any new count. Preserve original frozen pin.
