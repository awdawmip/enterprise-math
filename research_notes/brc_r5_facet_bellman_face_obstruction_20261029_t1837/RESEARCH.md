# R5 — Exact facet/Bellman audit and exposed-face rank obstruction

2026-10-29, author-side portable result. Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Finite two-law stop/continue/declare experiments only. This is not a physical Heartbeat-X6 theorem or a solution of the coupled-two-merger mother problem.

## Input pins and BRC semantics

GLOBAL_KNOWLEDGE_V1 canonical `main@7b33f8066e9993e7c941959a9d738ed405248eb8`, project source `main@479458b79fdae1e6328bd0d674d2e5cc24cdf81a`. Loaded global/project bootstraps, manuals, P000, ACTIVE worldview and portable protocol. Prior verified R5 one-merger rigidity: `5406ce8808c74dbdeb17ee64b6cc12bdb9468eee`; the previous positive-cost separator is not newly claimed. BRC **REUSE_APPLIED**: preserve each source's positive Q and P path masses, exact likelihood ratios and terminal declaration observer `(e_P,e_Q,T_P,T_Q)` before quotienting into LR keys. P000 six spatial axes/one time axis and rotation premises are preserved, not interpreted as consequences of this external probability model.

Gateway control status: `research_authority_granted=false`; active-owner query returned `CONTROL_QUOTA`. No active Source owner/CLAIM/Result or independent Driver review certified. GitHub handoff is author-side only.

## Lemma A — the FULL real behavioral observer image is convex

For finite full observable histories h including previous actions (perfect recall), let `q_pi(h,a)` denote Q flow for a FULL policy pi. Given FULL policies pi,sigma and scalar alpha in [0,1], define
`tau(a|h)=[alpha*q_pi(h,a)+(1-alpha)*q_sigma(h,a)]/[alpha*q_pi(h)+(1-alpha)*q_sigma(h)]`
whenever denominator>0 and arbitrary otherwise. The P/Q ratio `r(h)` at a fixed history is independent of policy: both P and Q path probabilities acquire identical behavioral action factors. Consequently `p_pi(h,a)=r(h)q_pi(h,a)`. Induction on history length shows tau reproduces the convex mixture of both laws' terminal/action flows; any four linear error/time observables are mixed with the same alpha. A persistent random seed is not required by FULL; it is the full observable history that permits this occupancy-flow construction. This argument does *not* imply LR history compression.

## Lemma B — exact LR behavioral product expansion

A seedless LR policy specifies independent local action probabilities at each key k=(t,r), and no trajectory visits the same time-labelled key twice. Any path mass is a product of the action probabilities of keys on that path, each at exponent<=1. Expanding those products gives the multi-affine identity
`O_LR(x) = sum_{D deterministic LR} [prod_k x_{k,D(k)}] O(D)`.
Its convex hull is the rational polytope of deterministic LR observer vectors. Product weights are *not* arbitrary convex combination weights: they have cross-key independence constraints.

## Theorem 1 — complete finite all-signed facet/Bellman test

Let C be the convex hull of all deterministic exact-LR four-observer vectors of a finite rational experiment. Since LR policies are FULL policies and FULL image is convex, hull equality holds **iff** every affine-hull equality of C holds on FULL, and for every oriented rational relative facet `w_j·z>=b_j` of C the exact FULL Bellman minimum obeys `min_FULL w_j·O>=b_j`.

Proof: The relative facets and affine-hull equations form an exact finite H-representation of the rational LR polytope. The listed comparisons are precisely the assertion `O_FULL subset C`. Reverse inclusion follows from LR subset FULL and FULL convexity. Backward Bellman induction optimizes a signed linear terminal/time cost over every real FULL behavioral policy by choosing a best action at each full history; all masses are rational. A failed facet furnishes an exact rational separating hyperplane and deterministic FULL witness. In ambient R4, the equivalent primal certificate for each FULL deterministic vector uses at most five LR vertices by Caratheodory. Unlike finite signed-grid checks, the finite facet list establishes **all** signed directions.

## New complete seven-facet audit: genuine two-law source-sensitive one-merger

At time t=1 histories A,B have P and Q mass rho_A=rho_B=1/2 and the same LR r=1. Source choices are stop+declare P, stop+declare Q, or continue to terminal t=2, then declare P/Q. Terminal exact LR multipliers are (1/2,1,3/2). Strictly positive normalized kernels are:

- A: Q=(1/4,1/2,1/4), P=(1/8,1/2,3/8).
- B: Q=(1/3,1/3,1/3), P=(1/6,1/3,1/2).

FULL actions may differ by source. LR must share source action and terminal declarations at equal LR atoms. Both sets satisfy `T_P=T_Q=T`, verified over all policies and from equal source P/Q incoming weights. Therefore project to exact 3D coordinates `(e_P,e_Q,T)`, keeping the affine equation `T_P-T_Q=0`.

Exact `Fraction` enumeration gives 24 raw deterministic LR policies (10 distinct observer vectors), 576 raw FULL deterministic policies (83 distinct observer vectors), and LR affine rank three. An exhaustive exact triple-of-vertices supporting-plane construction yields **exactly seven primitive integer LR facets** `(a,b,c)·(e_P,e_Q,T)>=bound`:

| Normal n=(a,b,c) | LR bound | FULL Bellman minimum | FULL minus bound |
|---|---:|---:|---:|
| (-48,-48,7) | -41 | -83/2 | **-1/2** |
| (-2,-3,0) | -3 | -3 | 0 |
| (-2,-1,0) | -2 | -2 | 0 |
| (0,0,-1) | -2 | -2 | 0 |
| (2,1,0) | 1 | 1 | 0 |
| (2,3,0) | 2 | 2 | 0 |
| (48,48,7) | 55 | 109/2 | **-1/2** |

**Completeness:** Every facet of a full-dimensional 3D rational polytope contains three noncollinear vertices. All triples from the ten LR vertices were considered. A candidate plane was retained only when every LR vertex lay on one side; primitive integer orientations were deduplicated. Every retained plane contains >=3 noncollinear vertices. Thus no supporting facet is omitted. Each listed FULL minimum was independently computed by sourcewise Bellman and exhaustive FULL deterministic enumeration. For n=(a,b,c) and masses rho_i=1/2, the exact all-real formulas are

`V_FULL = sum_i rho_i * min{b+c, a+c, 2*c+sum_j min(a*p_ij,b*q_ij)}`;

`V_LR = min{b+c, a+c, 2*c+sum_i rho_i*sum_j min(a*p_ij,b*q_ij)}`.

They apply to *signed* costs and all real random action probabilities: optimal terminal declaration depends only on terminal LR, so terminal sharing causes no extra minimization defect.

The known positive facet corresponds to `96e_P+96e_Q+7(T_P+T_Q)>=110`, violated by FULL vector `O_plus=(1/12,5/6,3/2,3/2)` with left side 109. **New independent opposite-error facet:** every real LR strategy satisfies
`-96e_P-96e_Q+7(T_P+T_Q)>=-82`,
but legal FULL vector `O_minus=(1/4,5/6,3/2,3/2)` has left side exactly **-83**. In either direction the explicit L-infinity distance from that FULL witness to the LR image is at least `1/206` by Holder. Exactly two of the seven LR facets fail for FULL; the other five hold on all FULL policies. The model is **not** a mother counterexample, since its convex hulls already differ.

## Theorem 2 — an exposed rank-three policy rectangle forces ACTUAL nonmembership

Suppose a rational signed direction w exposes exactly four deterministic LR policies `D_00,D_10,D_01,D_11`, differing in exactly two binary LR keys and identical at every other key. Suppose their observer vectors `V_ij` are affinely independent (rank 3) and at least one LR deterministic policy lies off that face. Then
`U=(V_00+V_11)/2`
is in the genuine FULL *real* image, by Lemma A, but **outside** the seedless LR real image.

Proof: write `h=min_D w·O(D)`. A seedless LR policy realizing U must achieve face value w·U=h. Its product mixture from Lemma B cannot give any positive probability to an off-face deterministic policy, since every off-face policy has strictly positive w-slack. With exactly four exposed policies and all other keys fixed, the surviving two-key probabilities form a product table:
`mu00=(1-p)(1-q), mu10=p(1-q), mu01=(1-p)q, mu11=pq`.
Thus `mu00*mu11=mu10*mu01`. Affine independence of the four face V's makes barycentric coordinates unique, but U has coordinates (1/2,0,0,1/2), violating this equality (1/4 != 0). Contradiction. This is a genuine no-CAD certificate **conditional on** the existence of such a face; it does not assert one has been found in an admissible two-merger model.

**Quantitative all-real certificate.** Pick affine extensions `L_ij(z)=a_ij·z+c_ij` of barycentric coordinates on the face, and let `C=max||a_ij||_1`, `R=max_{ij,D}|L_ij(O(D))|`, `gamma=min_{D off-face}(w·O(D)-h)>0`, `N=||w||_1`. Then for every real LR output Y,
`||Y-U||_infty >= 1 / [4*(C+(R+1)*N/gamma)]`.
Indeed let epsilon be off-face product mixture weight. Face exposure gives `epsilon<=N||Y-U||_infty/gamma`. Conditional on the face the two key probabilities remain a product table mu. Every product mu has max coordinate deviation at least 1/4 from target (1/2,0,0,1/2), since deviation strictly below 1/4 would give mu00*mu11>1/16 and mu10*mu01<1/16. Each affine L gives
`|mu_ij-L_ij(U)| <= C||Y-U||_infty+(1+R)*epsilon`. Combine. This handles probabilities that put mass *off* the face as well.

**Isolated algebraic fixture (not a stop experiment):** Three binary controls p,q,s, four face corners `V00=(0,0,0,0),V10=(1,0,0,0),V01=(0,1,0,0),V11=(0,0,1,0)`, and any s=1 corner `W=(0,0,0,1)`. Image
`Y=((1-s)p(1-q),(1-s)(1-p)q,(1-s)pq,s)`. For face w=(0,0,0,1), target `U=(0,0,1/2,0)`, choose L00=1-x-y-z and L10=x,L01=y,L11=z; constants C=3,R=1,gamma=1,N=1 give rigorously `||Y-U||_infty>=1/20` for all real p,q,s in [0,1]. A 1331-point rational grid in the executable is only a numerical regression; the bound is an algebraic proof. This fixture is explicitly **not** a claimed two-law realization and is not the open mother solution.

## Execution and related scientific literature

Local Python 3 standard-library `Fraction` verification executed twice and produced identical stdout `EXACT_OUTPUT.txt`; final marker `PASS_EXACT_R5_FACET_BELLMAN_AND_FACE_RECTANGLE`. It checks positive kernels, terminal ratios, both deterministic spaces, all seven exact facets, independent Bellman optima, two witnesses and the algebraic fixture. There was no formal proof assistant or independent scientific review.

Background, not proof or novelty attribution: Anderson & Montufar, *The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes*, arXiv 2606.03048, posted 2026-06-02 (infinite-horizon POMDP); Laroche & Tachet des Combes, *On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs*, ICML 2023, https://proceedings.mlr.press/v202/laroche23a.html (different occupancy setting).

**Next:** build genuinely coupled, source-sensitive, two-exact-merger rational DAGs. Check every LR facet with exact FULL Bellman, plus affine-hull equations. If ALL pass, search for four exposed LR deterministic policy corners differing at only two binary keys with affine rank three; that makes an explicit FULL point with provable LR nonmembership, bypassing CAD. Otherwise return exact violated facet/Farkas certificate; if hull passes but no qualifying rectangle, perform an all-real semialgebraic test with zero-flow boundaries. Do not reuse this one-merger audit as a new model.
