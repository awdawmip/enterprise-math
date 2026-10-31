# R5 — Complete no-go for every real source-labelled 24-terminal linear fourth observer

Date: 2026-11-01 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
This proves a mathematical statement inside one finite auxiliary two-measure stopping model; it is NOT a native X6, three-dimensional native slice, physical, or accepted Foundation theorem.

## Frozen sources, permissions and provenance

GLOBAL_KNOWLEDGE_V1 canonical main verified: 1cea747f65ceda1d892eccbcbb27dcf84dbeadd1. Account bootstrap/manual, current Enterprise Math router, P000_STARTUP with full canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview and mathematical/code/BRC research guidance were read.

Enterprise Math canonical main verified: ac48238d40c28c9ad139faa5b0e11cb7defdd8f9. AGENTS.md, P000 project V5, joint-relation observer preservation, native X6 time, autonomous research and PORTABLE_RESEARCH_PROTOCOL.md were read. Exact predecessor: research_notes/brc_r5_six_port_fiber_20261101_t0443/RESEARCH.md at commit 24ec5484b8eb5bc64e12a37ba9b9953e78017ad7, draft PR 1663. We consume its six-ingress codimension-five exposed-face lemma; this note completes the wider 24-terminal classification. No protected source changes.

Native em_status 0.6.11 returned research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED, active jobs 5/5; no current live owner verified, no source-issued session/CLAIM/Result/independent review obtained. GitHub author material does not confer Source rights. BRC reuse: exact positive source/route-labelled P,Q carrier with signed linear observers, preservation of all 24 provenance-labelled terminal masses; no assertion of positive-mass cancellation, no native heartbeat/BRC-Shor calculation.

## Model and exact question

Two origins i=0,1, each with Q and P initial mass 1/2. Parameters alpha_0=1/4, alpha_1=1/5, kappa_0=3/4, kappa_1=1/6. Each origin has independent binary decisions A,D,Y,LD,LY,LC: A stops at time 1 or continues to D,Y,C with conditional probabilities alpha_i,alpha_i,1-2alpha_i; D either stops at 2 or continues to DH (fraction 2/3, time 3), L ingress from D (fraction 1/3); Y stops at 2 or continues to YH (fraction 1/2, time 3), L ingress from Y (fraction 1/2); C stops at 2 with probability 1-kappa_i or enters L from C with kappa_i. Each L ingress stops at time 3 or continues to time 4.

Twelve terminal tags per origin in order A,D,Y,C,DH,YH,LD,LY,LC,L4D,L4Y,L4C have stopping times 1,2,2,2,3,3,3,3,3,4,4,4 and P/Q ratios 1,1/2,3/2,1,1/4,2,1,1,1,1,1,1. Every Q atom is nonnegative and sums to 1; the P-weighted masses also sum to 1 for every policy. FULL uses twelve origin-and-ingress-specific controls, with 4096 deterministic corners. Seedless LR uses one shared key each for A,D,Y,L, with 16 deterministic corners; in the LR class each key has one independent behavioral continuation probability. All terminal masses are multiaffine in the corresponding unrepeated controls, so the convex hull of either real behavioral image equals the convex hull of its deterministic corners.

Retain the entire 24-dimensional labelled Q terminal carrier m=240Q (an integer vector). The three fixed real observations are x=Q(DH), u=Q(YH), t=T_Q. For any real coefficient vector c in R^24, the fourth is z_c=sum_(i,leaf) c_(i,leaf) Q(i,leaf). Question: can any c give LR four-dimensional affine rank 4 AND conv V_FULL(x,u,t,z_c)=conv V_LR(x,u,t,z_c)?

### THEOREM (all real coefficients, full 24-leaf family)

For every c in R^24, either the LR four-observation convex hull has affine rank at most 3, or the FULL/LR four-observation convex hulls are strictly unequal. No fourth linear expectation of these 24 source/path-labelled terminal atoms solves the mother convex-hull requirement for this fixed model and first three observers.

## Proof part I: eight necessary independent exposed-edge equations

Let x,u,t be the unscaled observations and let LR indices be lexicographic four-bit A,D,Y,L. All sixteen LR corners satisfy f0=4t-39x-8u-4 >= 0, f1=2t-3x-26u-2 >=0, and x,u>=0. The first eight LR corners stop at A and have the identical terminal mass carrier (regardless of their unreachable keys).

Three FULL corners produce the same (x,u,t) as a **unique** LR carrier interpolation on three exposed edges:
FULL[48] has (x,u,t)=(1/15,0,33/20), equals (5/9)LR[0]+(4/9)LR[12] in the base coordinates, and is on {f0=u=0}.
FULL[56] has (1/15,1/20,7/4), equals (5/9)LR[0]+(4/9)LR[14], and is on {f0=f1=0}.
FULL[40] has (0,1/20,33/20), equals (5/9)LR[0]+(4/9)LR[10], and is on {f1=x=0}.
Each edge has only the two distinct LR terminal carrier vectors stated (the first eight indices denote the same A-stop carrier). If FULL/LR four-dimensional convex hulls were identical, these three fourth coordinates would agree. Thus c must annihilate
E_early(j,k)=9m_FULL[j]-5m_LR[0]-4m_LR[k],
for (j,k)=(48,12),(56,14),(40,10).

On the maximal exposed face (x,u)=(3/20,9/80), only distinct LR endpoints LR[14], LR[15] remain. The six positive source+ingress Q*240 weights, indexed (0,D),(0,Y),(0,C),(1,D),(1,Y),(1,C), are w=(10,15,45,8,12,12), W=102. For each port p, let m_port[p] be FULL with all upstream A,D,Y continuing and exactly port p continuing at L. The unique LR time-matched edge mixture forces
E_port[p]=W*m_port[p]-(W-w_p)*m_LR[14]-w_p*m_LR[15].
All six equations c·E_port[p]=0 are necessary. Their sum vanishes, and five are independent. Assemble the three early residual rows and the first five port residual rows into the 8 by 24 integer matrix E. Exact row reduction gives rank(E)=8, pivot columns (0,1,2,6,7,8,18,19), and the selected 8 by 8 minor
det E[:,pivots] = -5817825199521792000000 != 0.
Every failed E equation yields a strict real signed Farkas separator (construction immediately below).

General constructive separation: for a violated forced edge, let D(x,u,t) be a nonnegative LR-face deficit that vanishes only on its two distinct endpoints: D48=f0+u, D56=f0+f1, D40=f1+x, or Dport=(3/20-x)+(9/80-u). Let g(t) be the unique affine line in (t,z_c) between the edge's endpoints. At the FULL point there is a nonzero residual rho=z_c(FULL)-g(t_FULL). For each other LR corner k, D_k>0; set sigma=sign(rho) and M=1+max_(k:D_k>0) |z_c(LR_k)-g(tLR_k)|/D_k. The affine functional H=sigma*(z_c-g(t))-M D is zero on the LR edge, strictly negative on every other LR corner and positive (=|rho|) on the FULL witness. This is an exact finite expression for EVERY real coefficient vector with E c != 0, not a sampled-coefficient argument.

## Proof part II: the entire surviving effective observer space is five-dimensional

The full 4096-by-24 integer mass matrix m has linear row rank exactly 13: all 4096 rows lie in the span of the thirteen explicitly selected indices
(0,2048,3072,2560,3328,2688,2112,32,48,40,52,42,33);
their nonzero 13 by 13 minor on column indices
(0,1,2,3,6,7,8,12,13,14,18,19,20)
is -870712934400000000. The attached exact checker independently reduces every 4096 row against this basis. All E rows are linear combinations of FULL mass rows because all LR corners are also FULL corners. Hence rank(M)=13, rank(E)=8 and row(E) is a subspace of row(M).

The effective dimension of linear functions of m obtained from coefficients satisfying E c=0 is exactly rank(M)-rank(E)=5. (Precisely: dim M(ker E)=rank(M)-rank(E), since ker M is contained in ker E.)

Five independent E-neutral functions are 1, x, u, t, and
z_A=(5/4)Q(origin0,A)+Q(origin1,A).
All eight E rows annihilate their coefficient vectors. On FULL corners with indices (0,32,33,40,48), the corresponding 5 by 5 evaluation minor, in the integer-scaled columns (240,240x,240u,240t,240z_A), equals -66355200 != 0. They therefore span the five-dimensional effective E-neutral observer space.

Thus, for EVERY c with E c=0, there are real b0,bx,bu,bt,bA such that for all FULL and LR behaviors
z_c=b0+bx*x+bu*u+bt*t+bA*z_A.
Equality holds on all 4096 deterministic corners by the rank certificate, and extends to real behavioral probabilities by multi-affinity. If bA=0, LR's four-coordinate affine rank is <=3. If bA!=0, the map
(x,u,t,z_c) -> (x,u,t,(z_c-b0-bx*x-bu*u-bt*t)/bA)
is an invertible affine coordinate change, so both convex hulls have exactly the geometry of the z_A observer.

## Proof part III: the sole remaining fourth direction is also separated

For LR real controls (a,d,y,l) in [0,1]^4, exact probability calculation gives:
x=(3/20)ad,
u=(9/80)ay,
z_A=(9/8)(1-a),
t=1-a+a[179/80+9(d+y)/40+l(19/80+3d/40+9y/80)].
Consequently the affine functional
H=45t+59z_A-90x-135u-891/8
factors identically as
H=-a(1-l)[171/16+(27/8)d+(81/16)y] <= 0.
In particular every LR deterministic corner and every real seedless-LR behavior satisfies H<=0.

The legal FULL deterministic policy indexed 2112, with 12 bits
(1,0,0,0,0,1;0,0,0,0,0,0),
has (x,u,t,z_A)=(0,0,15/8,1/2), where H=5/2 > 0. The LR (x,u,t,z_A) augmented affine evaluation matrix has exact rank 5, i.e. four-dimensional affine rank 4. Invertible affine changes transfer this support gap to every E-neutral c with bA!=0. Therefore E c=0 never yields BOTH LR rank 4 and equal FULL/LR convex hulls. Combining the two cases E c!=0 and E c=0 proves the theorem. QED.

## Exact validation, limitations, and next question

Attached VERIFY.py executes with only standard Python fractions/integers: generates all 4096 FULL and 16 LR corners; checks P and Q normalization; directly checks all LR early-face inequalities and their forced endpoints; tests the eight independent signed edge residuals and their exact minor; proves the 4096-row basis containment and nonzero minor; verifies E neutrality, effective five-function rank, LR four-rank, exact LR support extrema, and FULL strict witness. EXACT_OUTPUT.txt contains actual run output. All-real quantification follows from analytic linear algebra and factored LR formula, not finite sampling of c. No Lean proof, independent mathematical review, Source admission, or native X6 embedding is claimed.

Compared with predecessor codimension-five maximal-face constraint, three genuinely independent early-face constraints yield codimension eight. The entire E-neutral effective 24-terminal linear observer family collapses to one fourth direction modulo affine base readings, and that last direction has an exact strict support separator. Do NOT search more linear coefficients on these same 24 atoms with fixed first three observers.

Next: test the smallest new **stopping mechanism or nonlinear path interaction** not representable as a single-terminal-event expectation on these 24 leaves. For example, include an additional return to L with explicit repeated-key memory semantics; retain source, phase, full route, likelihood and time. Before using extreme-corner reductions, prove whether repeated behavioral keys preserve multiaffinity. Find exact LR base-fiber rank and a new independent residual; give signed separators or <=5-vertex rational convex certificates. Only when rank 4 and complete four-dimensional hull equality are established should strict real behavioral-image nonmembership be tested. Original mother problem remains OPEN outside this auxiliary model.