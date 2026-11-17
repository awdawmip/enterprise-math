# R5: universal four-monomial obstruction at a shared downstream gate

**2026-10-31 (Asia/Shanghai). AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** Auxiliary finite two-measure stopping experiment, **not** a claim about native X6 geometry, Heartbeat time dynamics, physical probabilities, or formal Source task admission.

## Frozen sources and question

- GLOBAL_KNOWLEDGE_V1 canonical main@c7fcc26913ced2dbf663c420ee058e3cade936dd; Enterprise Math main@991bcd37fb61895b06655e1416dec064ace4d7d9 (connector-confirmed in this research turn). The global P000 startup projection's SHA agrees with its canonical V4 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. The current Enterprise Math P000 V5, ACTIVE worldview, Heartbeat X6/time, provenance-preserving joint-observer constraint and portable protocol were read. Protected definitions are unchanged.
- Predecessor: research_notes/brc_r5_yl_merger_path_error_20261031_t1042/RESEARCH.md, immutable commit 2c48777a3b4524da8b135bc98fcd437a87434e9b, Draft PR #1663. Its source-exact Y→L merger has equal actual real two-time images, an invertible four-observer map for nonzero path-sensitive error contrast, actual LR nonconvexity, and a specific signed support gap. It remains author-side, not independently admitted.
- **Question:** Can tuning only terminal response rays of direct L versus Y→L align *every* signed four-observer support direction while keeping affine dimension four, within this four-monomial model?

## BRC carrier and observer scope

Retain positive P/Q probability on every labelled path, both A-origin identities, and the distinct direct L and via-Y→L branches until the terminal observation. No spatial interpretation or future-operation-preserving collapse is assumed. The only declared observer is O=(e_P,e_Q,T_P,T_Q), a typed final readout of the finite process. Use positive weighted BRC path propagation; a signed support functional is applied to the *resulting observer vector*, never used to cancel positive branch mass.

For exchangeable labelled origins, let the four source-averaged positive-action monomials be
  a = average(x_i),
  b = average(x_i u_i),
  c = average(x_i v_D,i),
  d = average(x_i u_i v_Y,i),
with every behavioral action probability in [0,1]. FULL may choose the direct-L and via-Y→L terminal decisions separately; a seedless likelihood-ratio (LR) policy shares them and also identifies otherwise equal time/LR-key actions. This study assumes **the complete observer** factors as the *same* affine map
  O_FULL = b0 + M(a,b,c,d)^T;
  O_LR = b0 + M(x,xu,xv,xuv)^T,
where M is a real m×4 matrix and b0 is fixed. For the mother question m=4. The complete four-monomial factorization, not just the state topology, is a necessary assumption. Source-asymmetric coefficients, additional independently observed monomials and additional gates lie outside it.

## Theorem 1 — exact FULL and LR behavioral polytopes

The **actual real** FULL monomial image is already the convex polytope
  P_F = {(a,b,c,d): 0≤b≤a≤1, 0≤c≤a, 0≤d≤b}.
Its seven vertices are
  F0=(0,0,0,0), F1=(1,0,0,0), F2=(1,0,1,0),
  F3=(1,1,0,0), F4=(1,1,1,1),
  F-=(1,1,0,1), F+=(1,1,1,0).

The seedless real LR set is
  P_L={(x,xu,xv,xuv):x,u,v in [0,1]}.
Its convex hull is exactly the four-dimensional simplex conv(F0,F1,F2,F3,F4), and the unique barycentric coefficients of any point (a,b,c,d) in that vertex order are
  (1-a, a-b-c+d, c-d, b-d, d).
The two extra FULL vertices lie strictly outside: F- has c-d=-1; F+ has a-b-c+d=-1.

**Proof.** FULL variables obey the inequalities by positivity. Conversely take any feasible (a,b,c,d) and choose the *same* actions for every origin: x=a, u=b/a when a>0 (else 0), v_D=c/a when a>0 (else 0), and v_Y=d/b when b>0 (else 0). This realizes the quadruple exactly. Independent binary choices of x,u,v_D,v_Y yield precisely the seven vertices; multi-affinity places every real policy in their convex hull, while the feasible region is convex and contains all seven. For LR, binary choices x,u,v give precisely five distinct vertices, and direct solution of the linear convex-combination equations gives the stated five coefficients. QED.

## Theorem 2 — two-point all-signed criterion and universal rank-four no-go

For every real m×4 affine matrix M and offset b0,
  conv(O_FULL) = conv(O_LR)
**if and only if** M F- and M F+ both belong to conv(M F0,...,M F4).

If rank(M)=4, the convex hulls are strictly different. In particular, full four-dimensional affine rank and equal FULL/LR convex hulls are mutually incompatible **within this class**. Equality forces rank(M)≤3, but rank≤3 alone is not sufficient; both convex-combination checks remain necessary.

When m=4 and M is invertible, two explicit normalized observer support directions are
  q-=(0,0,-1,1)^T; q+=(-1,1,1,-1)^T;
  h-=M^{-T} q-; h+=M^{-T} q+.
For each sign,
  max_FULL h·O - max_LR h·O = 1.

**Proof.** By Theorem 1 the FULL convex hull adds only F- and F+ to the LR simplex. An affine map preserves convex combinations, proving the if-and-only-if statement. A rank-four map is injective and cannot send either excluded point into the LR simplex image. More constructively, for every LR behavioral tuple, d-c=xv(u-1)≤0 and b+c-a-d=x(1-u)(v-1)≤0. Their respective maximum over all LR real policies is zero. Each form has maximum exactly one over P_F, at F- for d-c and at F+ for b+c-a-d. Invertible M transports these functionals to the stated observer directions; b0 cancels in support differences. QED.

**Interpretation:** The predecessor's signed separator is not an isolated numerical accident; it is the image of a universal facet inequality of the seedless LR monomial simplex. Changing only terminal readout coefficients cannot cure this signed support defect without losing rank or violating the four-monomial hypothesis.

## Corollary 3 — actual LR nonconvexity coexists with the rank-four obstruction

If M is injective, the actual seedless LR observer image is nonconvex. The point
  p*=(1,1/2,1/2,1/2)
is the midpoint of seedless points (1,0,0,0) and (1,1,1,1), is realized by FULL with x=1,u=1/2,v_D=1/2,v_Y=1, but cannot be realized by seedless LR. Every seedless tuple satisfies ad=bc, while p* has ad-bc=1/4.

For invertible M, the polynomial ad-bc is 4-Lipschitz on [0,1]^4 in infinity norm. Therefore
  dist_infty(b0+M p*, O_LR_actual) ≥ 1/(16 ||M^{-1}||_infty),
where the matrix infinity norm is its largest absolute row sum. This is a separate **actual-image** nonmembership bound, not the convex-hull separator.

## The Y→L strictly positive rational instance

At y=1/8, l=1/4 and terminal errors 1/8 and 7/8, the previously source-derived complete observer map is
  b0=(1/8,1/8,1,1)
  M=[[0,3/512,0,9/512],
     [0,3/256,0,3/256],
     [31/32,1/32,3/32,3/128],
     [15/32,1/32,1/16,1/64]].
Exact determinant: det(M)=153/67108864.

The normalized directions are
  h-=(448/17,3424/51,480/17,-992/17);
  h+=(-320/3,160/3,-32,64).
The integer separator J=(42,107,45,-93) from the predecessor equals (51/32) h-, hence has exact support gap 51/32. FULL witnesses:
  O(F-)=(19/128,19/128,259/128,97/64);
  O(F+)=(67/512,35/256,67/32,25/16).

The dual L1/L∞ inequality bounds distance to the **entire LR convex hull**, stronger than mere actual-image nonmembership:
  dist_infty(O(F-),conv O_LR) ≥ 1/||h-||_1 = 51/9184;
  dist_infty(O(F+),conv O_LR) ≥ 1/||h+||_1 = 1/256.
The separate seedless nonconvex midpoint satisfies
  O(p*)=(35/256,35/256,523/256,195/128),
  ||M^{-1}||_infty=13024/51,
  dist_infty(O(p*),O_LR_actual) ≥ 51/208384.
These are different FULL witnesses and different target sets.

For **every** real y,l>0 with 2y+3l/2<1 and nonzero terminal error contrast k=eta_hi-eta_lo, the predecessor's same four-monomial response columns have exact symbolic determinant
  det M = k² l y² (y+2) / 2048 > 0.
Consequently the **entire positive-kernel Y→L family with k≠0** has unequal four-observer convex hulls. More generally, any altered terminal response map still factored through these same four monomials must choose between loss of four-dimensional rank and a strict hull gap. This does not rule out a new source-specific kernel or extra interacting decision monomial.

## Verification, status and next action

The sibling standalone Python standard-library fractions.Fraction verifier was executed on the actual predecessor matrix. It enumerates five LR and seven FULL unique binary monomial vertices; checks both separating facets and barycentric formula, 125 rational LR tuples and 625 FULL tuples, matrix inverse/determinant, exact normalized separators and two FULL witnesses, the convex-hull distance bounds, and the actual LR nonconvex midpoint. Its exact stdout is saved as EXACT_OUTPUT.txt, ending PASS_EXACT_R5_TWO_TAIL_AFFINE_RANK_FOUR_NO_GO. All-real theorems are proved algebraically above, not by finite samples; the symbolic determinant also follows by direct expansion. No independent review, Lean theorem checking, Source Result admission or native X6 transfer was performed.

**Solved search branch:** Terminal response-ray-only tuning that retains an injective four-monomial four-observer map cannot satisfy the mother target. **Next scientific unit:** Introduce a genuinely independent fifth (or higher) observer-control monomial through a second interacting chance merger, source-dependent history or upstream/downstream coupling; preserve strictly positive P/Q labelled flows. Require exact rational all-signed convex-hull equality certificates (or a Farkas counter-certificate) before seeking actual real LR image nonmembership. Maintain P000, ACTIVE worldview and explicit project role/admission boundaries.
