# EC49DG — Six-axis neutral gates and true full rank on an affine-collinear weight locus

Date 2026-11-01. AUTHOR_ANALYTIC_DERIVATION / EXACT_FINITE_CHECK_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED. Not a native CLAIM, formal Result, or independent mathematical review.

Frozen source input: GLOBAL_KNOWLEDGE_V1 main@59047e95917578f32bf5f56061663514733436da; Enterprise Math main@85f90349600ef59f4cf9fcda5201d50be257772e; predecessor EC49DE/EC49DF at Enterprise Math PR #1730 commit d9210ed913bbc7cc904d3f484b05ce740cbfc880. P000 and ACTIVE worldview unchanged. Native em_status 0.6.11 returned research_authority_granted=false, executor_binding_configured=false and active-job quota 5/5; owner lookup returned CONTROL_QUOTA, so the active Owner is not confirmed.

## Model, inherited results and BRC reuse

Genuine signed primitive X6 paths have fixed prefix length n and endpoint D=(2s,2v,0,0,0,0), v>=0, |s|+v<=h. Ordered adjacent positive tags A=(+E1,+E2), B=(+E2,+E1) are tracked jointly, including the prefix/future seam. Complete future operations are a=(-1,-1), b=(-2,-2), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3). Future words must return to the chosen Cell and contain exactly h, or 1..h, complete operations. Three separate additive channels per tag: product Wx of positive step-axis weights x_j, product Wy of positive step-axis weights y_j (negative weights 1), and unweighted count. The weights are strictly positive. Ranks are Q-linear for rational weights and R-linear for arbitrary real weights. This is not signed-amplitude cancellation or a physical propagation model.

Direct reuse, at its exact author-side status: EC49DE's genuine length-(2h+6) tag-only witness gives an invertible r-by-r future/label matrix T for every h>=2 and fiber. Here r=4 for delta=h-|s|-v=0, r=5 for exact positive odd delta, and r=6 for the other positive defects (including cumulative observations). EC49DF supplies the upper bound 3r and the sharp lower obstruction n>=2h+8. Neither predecessor has independent native mathematical admission.

## Theorem 1 — every axis, including E1/E2, supports a tag-safe two-step gate

For any distinct i,j,k in {1,...,6}, define

G_ijk = [[x_i,x_j,x_k],[y_i,y_j,y_k],[1,1,1]].

If det(G_ijk) != 0 for at least one triple, then for ALL integers h>=2 and ALL returning fibers the three-channel rank at n=2h+8 equals 3r. The exact and cumulative observations have the simultaneous sharp earliest saturation length n_sat(h)=2h+8. Equivalently the six planar points (x_j,y_j) are not all affine-collinear.

**Proof.** For every axis j, prepend the *ordered native pair* g_j=(+Ej,-Ej) to each EC49DE prefix p_i. The pair has zero endpoint, contains no A/B, ends negative and therefore creates no new A/B at the gate/prefix seam, EVEN for j=1 or 2. It does not change the old prefix/future seam. Its weight-count vector is exactly (x_j,y_j,1). Thus, with Bx_a,By_a denoting the positive suffix products and Ax_i,Ay_i the positive prefix products, the true path observation matrix has entries

M[(a,Wx),(i,j)]=Bx_a Ax_i T[a,i] x_j,
M[(a,Wy),(i,j)]=By_a Ay_i T[a,i] y_j,
M[(a,C ),(i,j)]=T[a,i].

For every group of three columns apply G_ijk inverse, and permute rows and columns. The three diagonal blocks become diag(Bx) T diag(Ax), diag(By) T diag(Ay), and T. Hence up to permutation sign

det(M)=det(G_ijk)^r det(T)^3 (product_a Bx_a By_a) (product_i Ax_i Ay_i) != 0.

This exactly realizes the inherited 3r upper bound; the inherited extreme-fiber obstruction proves minimality. Finite tests are not the proof. If all six-axis triple minors vanish, this particular one-base/two-step-gate factorization is insufficient, but the full observer may still have rank 3r.

**Concrete contrast with EC49DF:** x=(2,3,1,2,3,4), y=(4,7,3,5,7,9). Every triple among E3,E4,E5,E6 has zero determinant because these four weight pairs lie on y=2x+1. However det(G_{1,3,4})=-1. Prepending (+E1,-E1) (rather than the potentially tag-altering (-E1,+E1)) gives a valid all-h full-rank certificate on every fiber.

## Theorem 2 — all six-axis weights can be affine-collinear without actual rank loss

Let x=(2,3,1,2,3,4) and y=(5,7,3,5,7,9)=2x+1 componentwise. All 20 determinants det(G_ijk) vanish. Nevertheless, for EVERY integer h>=2 the extreme returning fiber D=(-2h,0,0,0,0,0) has the full 12-dimensional three-channel observation rank already at n=2h+8, which is the earliest possible length by the inherited EC49DF obstruction.

**Explicit universal-h native witness.** For a four-digit positive-axis word q=q1q2q3q4, let m_j(q) count occurrences of axis j, and set

P_h(q)=(+E_q1,+E_q2,+E_q3,+E_q4) followed by (-E1) repeated (2h+m_1(q)) times, followed by (-Ej) repeated m_j(q) times for j=2,...,6.

Then P_h(q) has exactly 2h+8 primitive steps and endpoint -2h E1. The negative tail cannot create A or B. The only future word of exactly h complete operations that returns to the chosen Cell is e^h. This suffix contains no A/B, starts +E3 after a negative tail, and contributes positive BRC factors Wx(e^h)=4^h and Wy(e^h)=75^h. The final tag is therefore precisely the tag of q.

Pick these twelve q, divided by the four independent final-tag atoms; each block's three rows are Wx, Wy, count:

tag 0: q = 3333, 3334, 3344; base 3-by-3 determinant -18.
tag A-only: q = 1233, 1234, 1244; base determinant -420.
tag B-only: q = 2133, 2134, 2144; base determinant -420.
tag both: q = 1213, 1214, 2123; base determinant +420.

For example the tag-both block has rows (12,24,18), (525,875,735), (1,1,1); its exact determinant is 420. The full 12-by-12 native observation matrix is block-diagonal in final tag, and its **exact integer determinant** is

(-18)*(-420)*(-420)*(420)*(4^h*75^h)^4
= -1333584000 * 300^(4h) != 0.

This is an analytic, all-h witness of true full rank INSIDE the all-axis-collinear stratum, even though every single-base neutral-gate 3-by-3 determinant vanishes. It does **not** prove full rank on the other fibers of that stratum. Since the four determinant polynomials remain nonzero at this collinear parameter point, their simultaneous nonvanishing holds on a nonempty relatively Zariski-open dense subset of the parametrized positive affine-collinear family y=a*x+b, for this specified extreme fiber.

## Actually executed exact finite checks

The adjacent VERIFY_EC49DG.py imports the unchanged predecessor VERIFY_EC49DD.py, VERIFY_EC49DE_COMPACT.py and VERIFY_EC49DF_Q0.py. It reconstructs literal signed-X6 paths, displacement, both A/B ordered tags including seams, actual positive integer BRC products and complete future words. New E1/E3/E4 gates: 172 distinct nonzero 3r-square modular determinants covering every returning fiber and both exact/cumulative future languages for h=2..5. They reproduce dimension pairs at h=2,3,4,5: (123,132),(228,246),(366,396),(537,582). All-axes-collinear example: 19 genuine 12-by-12 extreme-fiber matrices for h=2..20, each modular determinant equals the exact analytic formula reduced mod 1,000,003 and is nonzero. Actual stdout in EC49DG_EXECUTED.json has status PASS. The checker uses prime-modulus nonzero witnesses only; no floating-point or simulated semantic placement.

Certificate size: conditionally reusing EC49DE's explicit r<=6 tag witnesses, each mode at each of (h+1)^2 fibers needs <=18 primitive prefixes and <=18 selected suffix/tag rows, each O(h) symbols. The complete explicit certificate's output size is O(h^3) primitive symbols, without expanding all 5^h future words. This is an output-size bound, NOT a benchmark or a proved runtime bound for the existing enumerative checker.

## Next EC49DH

Classify actual three-channel ranks on the positive all-six-axis affine-collinear locus, beginning with the smallest h=2 interior fiber and its exact/cumulative response ranks. Try tag-isomorphic, weight-distinct 4-positive-step blocks as alternative uniform lifts, or exhibit a true defect with exact witness. Independently audit EC49DE's tag-only uniform lemma and EC49DF's upper/lower bounds; these are inherited author-side dependencies. No Source-native CLAIM/Result/Driver admission was obtained.
