# R5 — A two-facet physical phase cube and four exact adjacent strata

Date: 2026-11-10 (Asia/Shanghai). Author-side exact-rational continuation of PRs #1939 and #1947. Immutable frozen science: global \`a01383f825ef9d43b4b754254303298c64041568\`, Enterprise Math \`86149263e38c22292c9def1e0f69092efa1be77e\`. This note does not assert a formal R5 CLAIM, Result or independent mathematical review. The seven likelihood ratios are statistical nodes, not the native X6 spatial axes.

## New theorem and precise scope

Use the frozen eight-dimensional physical tangent map of PR #1947, \`p(z)=p0+P(t*+z)\`, \`t*=(0,0,0,-23/17050000,23/17050000,0,0,-23/17050000)\`. Coordinates are zero-indexed. Define the two separate physical residuals

\`m(z)=mu_1(z)=z_3/80-z_4+13*z_7/4\`
\`s(z)=s_25(z)=63/34100000+9*z_3/40-z_5+z_7\`.

Set \`R=49948501046391/3920403670319950000\`, approximately 1.2740652556912494e-5.

**Theorem.** For every real 8-vector with \`||z||_infinity<R\`, the original physical source/target capacities, \`g=b\`, seedless-F constraints and both stopped-time equalities hold **if and only if** \`m(z)>=0\` and \`s(z)>=0\`. Every physically legal point admits a valid Blackwell coupling whose minimal strictly positive support is **exactly 14 for m=0 and exactly 15 for m>0**. The independent faces \`m=s=0\` contain a six-dimensional relative-open minimal-14 stratum. Relative-open seven-dimensional minimal-14 and minimal-15 facets and a full eight-dimensional minimal-15 interior occur in the same cube.

In particular, all these claims hold on the **closed** rational cube \`||z||_infinity<=1/100000\`, extending the PR #1947 useful one-facet radius \`273/225912500\` by the exact radius factor \`18073/2184\` after the second source-defined capacity facet is retained. The number \`R\` is the current *support-exclusion certificate radius*, not a claimed sharp physical phase boundary.

## Proof

The 26 affine source/target capacity slacks are \`c+A*z\` with \`A=Jac(phys)*P\`. In the exact construction, slacks 4, 15, 23 and their tangent rows vanish identically; slack 19 is exactly \`m\`; slack 25 is \`s\`; every other center slack is positive. The five defining physical equalities are preserved by \`P\`.

For any positive-centered slack \`i\`, minimization over the half-cube \`||z||_infinity<=rho, m(z)>=0\` gives the exact linear-programming dual formula

\`min(c_i+A_i*z)=c_i-rho*H_i\`, where \`H_i=min_{lambda>=0} sum_k |A_ik-lambda*m_k|\`.

The one-variable convex piecewise-linear minimizer is attained at zero or a nonnegative rational breakpoint \`A_ik/m_k\`. Recomputing the frozen 26-slack linearization gives the first nonzero thresholds \`273/225912500\` (index 25) and \`17073/93775000\` (index 2). Therefore every slack besides the three structural zeros, \`m\` and \`s\`, is strictly positive for \`||z||_infinity<R\` with \`m>=0\`, because \`R<17073/93775000\`. It follows that adding \`s>=0\` is exactly the remaining physical legality condition.

For support cardinality, reuse the **exact immutable** 10 forced-edge dual inequalities and 4,845 four-extra-edge and 1,140 three-extra-edge exhaustive certificates of PR #1939. Their published sufficient radii are: positivity of the 14 other fixed-basis weights \`50915668197609/1202833246639750000\`; exclusion of <=13 supports on \`m=0\` within \`49948501046391/841518836618948125\`; exclusion of the 3,814 distinct four-extra-edge supports within \`R\`, with the remaining 1,031 support spans implying \`m=0\`; and forced-edge dual validity for \`||t*+z||_infinity<18052765669/423284426970000\`.

Exact rational comparison verifies

\`R<min(17073/93775000, 50915668197609/1202833246639750000, 49948501046391/841518836618948125, 18052765669/423284426970000-23/17050000)\`.

Thus the fixed 15-edge Blackwell basis stays feasible with its 14 other weights strictly positive, and the remaining weight equals \`E_(1,3)=m\`. When \`m>0\`, no <=14-edge support exists by the four-column certificates; when \`m=0\`, no <=13-edge support exists by the three-column certificates. This holds under either value of \`s\` as long as the physical point is lawful.

## Four rational witness strata

Write \`q=273/225912500\`, \`epsilon=1/10000000\`, \`x=(0,0,0,-1,-1,1,0,-79/260)\`, and \`e4=(0,0,0,0,1,0,0,0)\`. All listed points have norm less than \`1/100000\` and satisfy every other capacity slack strictly:
- **8D interior, minimal 15:** \`z=-epsilon*e4\`; \`m=epsilon\`, \`s=63/34100000\`.
- **7D m facet, minimal 14:** \`z=0\`; \`m=0\`, \`s=63/34100000\`.
- **7D capacity facet, minimal 15:** \`z=q*x-epsilon*e4\`; \`m=epsilon\`, \`s=0\`.
- **6D two-facet junction, minimal 14:** \`z=q*x\`; \`m=s=0\`.

The normals of \`m\` and \`s\` are linearly independent: the z4 coefficient of m is -1 whereas that of s is zero, and the z5 coefficient of s is -1. All other physical slacks are strict at the four displayed witnesses. The relative local stratum dimensions follow.

## Validation, BRC semantics, and next problem

The accompanying \`VERIFY.py\` was executed using exact Python Fraction/SymPy arithmetic, recomputing physical equality rank, 26 capacity-slack gradients, half-cube LP thresholds, all required strict radius inequalities, and the four exact witnesses. \`EXACT_OUTPUT.txt\` is output from that exact program. The predecessor's 4,845+1,140 exhaustive support checks are **reused**, not rerun here. This dependency is material to support *minimality*; the new physical two-facet calculations are independently reproducible.

BRC scope: retain the 30 transport branches and exact rational masses; use the established quotient only for its certified support-feasibility observer. Two residuals \`(m,s)\` suffice to test *local physical legality* in the specified cube, without replacing the full physical state or native X6 coordinates.

Next smallest concrete unit: identify which four-column support attains the previous separator radius \`R\`, evaluate actual nonnegative coupling feasibility at the certificate boundary and decide whether the two-facet 14/15 classification extends further or a new support cell begins. Seek a lawful 13-edge contact by exact constrained search, preserving all physical capacities. Full mathematical admission and R5 Owner/CLAIM remain controlled separately.

## Immutable research origins

- Frozen phase proof: PR #1939, \`9f39dc7f2145548c2a9a04e387d9f33fdec1ce4e\`, \`research_notes/brc_r5_exact_14edge_7d_facet_20261110_t0940/RESEARCH.md\`.
- Sharp one-facet physical cube: PR #1947, \`6bf9691e9022ac31e3597e7989988ffe5185c50b\`, \`research_notes/brc_r5_sharp_physical_halfcube_20261110_t11/RESEARCH.md\` and \`VERIFY_HALF_CUBE.py\`.
- Frozen scientific inputs: global \`a01383f825ef9d43b4b754254303298c64041568\`, EM \`86149263e38c22292c9def1e0f69092efa1be77e\`.
