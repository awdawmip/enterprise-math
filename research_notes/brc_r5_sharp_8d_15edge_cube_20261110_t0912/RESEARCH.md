# R5 — sharp 8D cube threshold for the 15-edge Blackwell requirement

Date: 2026-11-10 (Asia/Shanghai). Status: AUTHOR DERIVATION + EXACT RATIONAL REPRODUCTION; independent review and native Result admission pending.

## Frozen input and dependency scope

Scientific inputs remain fixed: account \`a01383f825ef9d43b4b754254303298c64041568\` and Enterprise Math \`86149263e38c22292c9def1e0f69092efa1be77e\`. Reuse the seven-likelihood-ratio P/Q–BRC physical mass, stop-time and slack maps and the exact physical center from PR #1902 at commit \`684ded4d951a0f1b8d314a421b29c39dd1afee64\`; reuse the eight RREF physical directions and 15-edge basis from PR #1930 at \`d616f7a934e36006fc07201c9ec475aabc401cf8\`. The seven statistical likelihood-ratio nodes are not the six native P000 axes. No change to P000, scientific pins, runtime ownership, or source-exposure classification.

Here \`p(t)=p0+P*t\` is the 14-vector of source/target physical coordinates; \`P\` is the 14x8 rational RREF tangent matrix selected by basis indices (0,1,2,4,5,6,7,8). The target-side mass is \`mu\` and source-side mass is \`nu\`. Let \`D\` be all 30 permitted Blackwell transport edges, \`C_full\` their 21-row rational constraint matrix, and \`b(t)=b0+Jb P t\` the exact 21-row transport RHS.

## Sharp-radius theorem

Let \`r*=23/17050000\`. For **every real eight-parameter vector** with \`|t_i|<r*\` for all i=0,...,7, the physical source is legal with \`g=b\`, the seedless-F target is legal, both specified stopping-time coordinates match, and

\[
\min_{E\ge0,\ C_{\rm full}E=b(t)}|\operatorname{supp}(E)|=15.
\]

The radius is sharp for the specified center, RREF coordinate basis and symmetric infinity-norm cube: at the explicit boundary point

\[
t_\partial=(0,0,0,-r_*,+r_*,0,0,-r_*),
\]

the physical pair is still legal and admits a Blackwell transport supported on **exactly 14** edges. Hence the supremal radius of centered cubes on which every point has minimum support 15 equals \`r*\` (the property holds for every radius strictly below \`r*\`, and fails at \`r*\`).

In particular, \`|t_i|<=10^-6\` is an explicit closed **eight-dimensional** cube of exactly-15-edge lawful physical instances. Relative to PR #1930's \`10^-40\` cube radius, this improves the guaranteed radius by \`10^34\` in the *same* coordinate basis.

## Proof: 4845 exact quotient separators

Let \`F\` be the ten mandatory edges independently certified by the rational dual vectors of PR #1902:
\`(0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6)\`.

Select the same 15 independent transport rows
\`I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)\`.
Multiply moment rows by 20, producing the exact integer \`15x30\` matrix \`C\`. The ten columns \`C_F\` have rank 10. Choose an exact integral 5x15 matrix \`L\` with independent rows spanning the left kernel of \`C_F\`, so \`L C_F=0\`.

Write \`D\F=\{d_1,...,d_{20}\}\`, \`V_j=L C_{d_j}\`, and \`q(t)=L b_I^{(20)}(t)=q0+Q t\`. A hypothetical feasible coupling with at most 14 positive edges must contain all ten forced edges and use at most four of the other 20. Therefore it would satisfy

\[
q(t)\in\operatorname{span}_{\mathbb R}\{V_j:j\in S\}
\]

for some four-subset \`S\subseteq\{1,...,20\}\`.

For all \(\binom{20}{4}=4845\) subsets, an exact 5D integer normal \`w_S\` was constructed and checked:

\[
w_S^\top V_j=0 \quad(j\in S),\quad w_S^\top q_0\ne0.
\]

For rank-four supports, \`w_S\` is the 4x4 cofactor normal. For ranks three or two, choose an independent subfamily and complete it to four vectors using standard coordinate basis columns; the exact checker verifies the resulting normal annihilates *all* original columns and separates \`q0\`. The exact rank distribution is rank 4: 3669; rank 3: 1143; rank 2: 33. The finite loop checks every subset, with no floating arithmetic.

Define the certified separation radius of each witness as

\[
 R_S=\frac{|w_S^\top q_0|}
 {\sum_{k=1}^8 |w_S^\top Q_{:,k}|},
\]

interpreting zero denominator as infinity. An independent exact rational reproduction finds

\[
\boxed{\min_{|S|=4} R_S=\frac{23}{17050000}=r_*}.
\]

A minimizer has four extra edges \`(2,1),(3,1),(4,1),(5,1)\`. Thus for any \`|t_k|<r*\`, every \`w_S^\top q(t)\` stays nonzero, and no support of size <=14 can solve the transport equations, provided the ten mandatory-edge inequalities remain strict.

## Proof: strict forcing and existence, with exact margins

For the ten original full-30-carrier rational duals \`y_e\` satisfying \`y_e^T C_full,f<=1_{f=e}\`, the strict positivity radius is

\[
\min_e\frac{y_e^\top b_0}
 {\sum_{k=1}^8|y_e^\top J_bP_{:,k}|}
=\frac{18052765669}{423284426970000}>r_*.
\]

Therefore those same ten edges are forced in every feasible coupling throughout the claimed cube. This check covers all 300 full-carrier dual inequalities again in the independent reproducer.

The physical constraints and fixed fifteen-edge solution are affine in \`t\`. Their independent exact margin tests yield

\[
\min_{\ell\ {\rm nonconstant\ slack}}
\frac{\ell(p_0)}{\|\nabla_t\ell\|_1}=r_*,
\qquad
\min_{e\in B}
\frac{E^B_e(0)}{\|\nabla_t E^B_e\|_1}=r_*.
\]

The three zero physical slacks have identically zero derivatives. Hence for all \`|t_i|<r*\`, every physical capacity inequality holds and every entry of the fixed 15-edge Blackwell solution remains strictly positive; the 21 transport equations continue to hold identically because \`C_full E^B(t)=b(t)\`.

These facts combined with the 4845 strict separators prove minimum support exactly 15.

## Sharpness witness

The fixed-basis edge \`(1,3)\` has

\[
E^B_{1,3}(0)=23/4000000,\quad
\nabla_t E^B_{1,3}=(0,0,0,1/80,-1,0,0,13/4).
\]

At \`t_partial=(0,0,0,-r*,r*,0,0,-r*)\`, this edge becomes exactly zero. All other fourteen basis edges remain strictly positive, the original physical constraints remain nonnegative (one physical slack also reaches zero), and all five physical affine equalities, as well as all 21 Blackwell equalities, remain satisfied. This is a legal explicit 14-positive-edge boundary example. Since larger centered cubes contain that boundary point, the uniform minimum-15 property is absent for every radius at least \`r*\`.

## Evidence, method and open unit

The companion \`VERIFY_SHARP.py\` contains the parent exact physical reconstruction plus the integer cofactor/minor algorithm, all 4845 exact support checks, dual checks and boundary witness assertions. \`EXACT_OUTPUT.txt\` records actual stdout from an independent local exact-rational reproduction of the same model and test, including the 4845 case totals and the exact sharp radius. Distinguish executed independent reproduction from execution of the newly published combined checker, which is supplied for subsequent direct verification. The proof is a finite exact-rational computation plus linear-affine inequalities; no approximate optimizer was used.

Reuse resolution: \`COMPOSE_APPLIED\` (PR #1902 forced support duals and exact central source, PR #1930 physical tangent and fixed basis, new finite quotient separator family). The BRC observer here is statistical marginalization of positive branch transport; the 1D physical kernel remains a separately typed physical-residual fiber. Only the 8D observed tangent basis was used for this exact cube.

**Next mathematics:** classify the adjacent 14-edge strata at the \`(1,3)\` vanishing face; test whether other rank-3/rank-2 quotient support strata meet that same boundary; extract a parameter-space chamber map with exact facet descriptions rather than a radius-only certificate. Formal R5 owner, native checkpoint and independent mathematical review are not claimed.
