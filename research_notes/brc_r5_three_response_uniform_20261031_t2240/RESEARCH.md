# R5 — uniform all-real three-response no-go with positive compensated P/Q flows

2026-10-31 Asia/Shanghai. Status **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is a theorem about a precisely declared *auxiliary* finite stopping model. It is neither a native Heartbeat-X6 theorem nor an admission/solution of the original full-hull-equality/behavior-set-inequality mother problem.

## Frozen source and provenance

Global knowledge canonical main `18e4eea156c607319d3f83019da98b5a5f176c14`; Enterprise Math canonical main `adccf931b55c7460362ca035fac7c8d468f04e8d`, both verified and fixed for this study. Read global `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, ACTIVE `我眼中的世界.md`, math/code research preferences and Task researcher route, Enterprise Math `p000_reality_foundation.json`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, and current control authority. P000 and ACTIVE worldview are unmodified. Exact scientific predecessor: `a9f9c9966dfaaf1d4d6293db26a8b91451816f15:research_notes/brc_r5_affine_response_global_nogo_20261031_t2143/RESEARCH.md`. It excluded the two-feature (DH,L4) response square; this new study **adds an independent YH feature**.

Native EM status returned `research_authority_granted=false` and `executor_binding_configured=false`. The Source owner query `em_control_tasks` returned `CONTROL_QUOTA`; no live Owner or CLAIM was established. Proof publication is an unreviewed portable-author research artifact and does not claim an accepted Result, official Owner continuation, or independent Driver review.

## Exact finite model

Two hidden sources `i=0,1`, each carrying Q mass `1/2` and P mass `1/2`, enter A at time 1 and likelihood ratio 1. On A CONTINUE, source i splits into D,C,Y at time 2 with Q conditional weights `(alpha_i,1-2alpha_i,alpha_i)` and likelihood ratios `(1/2,1,3/2)`. At D, CONTINUE yields DH at time 3, LR 1/4 (Q conditional 2/3), or L at time 3, LR 1 (Q conditional 1/3). At Y, CONTINUE yields YH at time 3, LR 2 (Q conditional 1/2), or L at time 3, LR 1 (Q conditional 1/2). At C, nature stops at C at time 2 with probability `1-kappa_i`, and otherwise enters L at time 3 with probability `kappa_i`. At L one STOPs at time 3 or CONTINUEs to L4 at time 4, LR 1. D and Y may alternatively STOP at time 2. The leaves are A,D,Y,C,DH,YH,L,L4; on every terminal cylinder P=lambda*Q, and both measures are normalized.

Natural parameters are `(alpha_0,kappa_0)=(1/4,3/4)`, `(alpha_1,kappa_1)=(1/5,1/6)`; all natural transition weights are strictly positive. The source-compensation parameter `theta_i=(1+kappa_i(1-2alpha_i))/alpha_i` is identically 11/2. Retain source and route provenance in the full positive path flow; the following scalar observer is a typed projection, not an erasure of physical or BRC provenance.

FULL may condition decisions on the source and route history, using six binary keys `(A,D,Y,LD,LY,LC)` per origin (4096 deterministic policies). Seedless LR sees only present (time,likelihood-ratio) keys `(A,D,Y,L)`, no hidden source/route or persistent random seed (16 deterministic policies). No such key is revisited along a history. Consequently a linear support score in the four independent real behavioral probabilities is multi-affine; its maximum occurs at an LR binary policy. This justifies the **all-real** LR support reduction (we require no enumeration to establish a FULL lower bound).

Let all terminal Bernoulli-error probabilities equal 1/2 except `r_DH=1/2+v`, `r_L4=1/2+w`, `r_YH=1/2+z`; all legal real parameters lie in `[-1/2,1/2]^3`. This response is shared between FULL and LR and P and Q; `gamma=2r_C-r_A-r_L=0` identically. Let `x=Q(DH)`, `y=Q(L4)`, `u=Q(YH)` be **nonnegative** source-labeled terminal probabilities. For the full observer `O=(e_P,e_Q,T_P,T_Q)`,

`e_P=1/2+(v/4)x+w*y+2z*u`,   `e_Q=1/2+v*x+w*y+z*u`.

These equalities follow immediately from P=lambda*Q, P and Q total mass 1, and the displayed Bernoulli responses. Signed H below is a dual observer, never a signed Q mass.

## Theorem A: complete legal real-z exclusion at baseline v,w

For `v=1/8,w=1/4` and **every real `-1/2≤z≤1/2`**, the FULL and LR *complete four-observer convex hulls* differ. More strongly, for each z one of two explicit FULL policies has a signed support advantage of at least `m=26581/77360>0` in one of two fixed directions

`H_-=(100,180,-130,107)`,   `H_+=(102,79,35,-54)`.

**Step 1 (exact LR support, all real behavioral policies).** Any deterministic LR policy has `u=Q(YH)` either 0 or `(alpha_0+alpha_1)/4=9/80` (YH occurs iff both A and Y CONTINUE). Thus for either H, its score is a line in z, with slope either 0 or `(2H_{eP}+H_{eQ})*9/80`. Explicit evaluation of all 16 LR binary policies gives the *maximum intercept in each of the two slope groups*: for H_- they are 117 and 16321/160; for H_+ they are 143/2 and 4547/80. The group maximizers are respectively A STOP `0000`, A,D,Y,L CONTINUE `1111`, A STOP `0000` and `1011`. Therefore, for every real z,

`sup_LR H_-·O = L_-(z)=max(117,16321/160+(171/4)z)`,
`sup_LR H_+·O = L_+(z)=max(143/2,4547/80+(2547/80)z)`.

This is not an approximation from sampled directions: it is a complete, exact, finite reduction of each **specified** real-policy support. The 16 intercept computations and P/Q normalizations are reproduced in `VERIFY.py`.

**Step 2 (two FULL witnesses).** For `W_-`, origin 0 uses six binary actions `(1,1,0,1,0,1)`, and origin 1 STOPs at A. Its score `H_-·O(W_-)=3819/32`, independent of z; hence its **witnessed support margin**

`g_-(z)=3819/32-L_-(z)=min(75/32,1387/80-(171/4)z)`.

For `W_+`, origin 0 uses `(1,0,1,0,1,1)`, and origin 1 STOPs at A. Its score `H_+·O(W_+)=1037/16+(283/16)z), hence

`g_+(z)=min((283z-107)/16,(319-566z)/40)`.

Both strategies are legal full source/history-dependent controls, not randomized mixtures.

**Step 3 (entire continuum and uniform margin).** Put `z_*=1922/4835` and `m=26581/77360`. Exact fraction reduction yields `g_-(z_*)=g_+(z_*)=m>0`. Since g_- is nonincreasing, `z≤z_*` implies `g_-(z)≥m`. The minimum of two affine functions g_+ is concave; on `[z_*,1/2]` its smallest value is attained at an endpoint; the endpoint values are `g_+(z_*)=m` and `g_+(1/2)=9/10>m`. Thus `z≥z_*` implies `g_+(z)≥m`. The cases cover every real legal z (including boundaries). At least one FULL witness is strictly separated from the **entire** LR hull. QED.

## Theorem B: robust open (v,w) box, uniform in real z

Hold the same positive natural kernels and take all real response parameters obeying

`|v-1/8|≤1/1000,` `|w-1/4|≤1/1000,` `|z|≤1/2`.

Then the FULL and LR four-observer hulls are unequal **throughout** this complete box; one of the same two fixed directions/witnesses has a support gap at least

`m_box = 749817/3868000 > 0`,

and its FULL witness has four-coordinate infinity distance at least `m_box/517=749817/1999756000` from the LR convex hull.

**Proof.** Positive flow bounds from the declared source routes imply, for **every** FULL or LR policy, `0≤x≤3/20` and `0≤y≤17/40` (attained by deterministic FULL decisions; verified exhaustively). For any fixed H with first two coefficients (p,q), changing v,w by `dv,dw` changes its score difference (a fixed FULL witness minus an arbitrary LR policy) by

`(p/4+q)*dv*(x_FULL-x_LR)+(p+q)*dw*(y_FULL-y_LR)`.

Since x and y are nonnegative and separately bounded, `|x_FULL-x_LR|≤3/20` and `|y_FULL-y_LR|≤17/40`. Hence the potential loss of witnessed margin is at most

`B_H=|p/4+q|*(3/20)|dv|+|p+q|*(17/40)|dw|`.

For H_- this is `(123/4)|dv|+119|dw|≤599/4000`. For H_+ it is `(627/40)|dv|+(3077/40)|dw|≤463/5000<599/4000`. At any z, Theorem A guarantees one base witnessed margin ≥m. The same witness retains margin ≥`m-599/4000=749817/3868000` throughout this box. By duality `|H·(W-L)|≤||H||_1 ||W-L||∞` and `||H_-||_1=517,||H_+||_1=270`, proving the claimed distance from the entire LR convex hull. QED.

This is not a theorem for arbitrary v,w outside the box, nor an assertion of external physical applicability. In the strict interior the terminal Bernoulli errors are also strictly between 0 and 1; at z endpoints the errors are legal but may equal 0 or 1. Natural transitions remain strictly positive everywhere.

## Theorem C: exact baseline LR rank transition

At v=1/8,w=1/4, the LR observation hull has affine rank **4 iff z≠1/8**. The five LR policies `0000,1000,1001,1010,1100` have affine difference determinant

`D(z)=(152361/1310720000)(1-8z)`.

To derive it, note that the entire policy-observation matrix gains the same rank-one update `z*u*(2,1,0,0)`: any such determinant is affine in z. Direct exact evaluations at z=0,1/4 are `+152361/1310720000` and `-152361/1310720000`. Thus rank is 4 away from z=1/8. At z=1/8, every LR deterministic observer satisfies the exact affine identity

`8(e_P-e_Q)-T_P+T_Q=0`.

It therefore holds for all real behavioral LR observations and their convex hull, forcing rank ≤3. Theorem A still separates at z=1/8, so rank collapse does not recover hull equality. QED.

## Execution and boundaries

Actually executed `VERIFY.py` uses Python standard-library `fractions.Fraction`. It checks all 16 LR scores for both directions, explicit FULL witnesses, probability normalization, exact real-proof constants, 101 rational regression z points (the grid is **not** the real-continuum proof), 4096 FULL binary policy flow feature bounds, rank minor and the z=1/8 LR identity. Actual output is saved verbatim in `EXACT_OUTPUT.txt`; final assertion is `PASS_EXACT_R5_THREE_RESPONSE_UNIFORM_RECTANGLE_NO_GO`.

The continuum proofs use elementary affine-support comparisons, monotonicity, concavity, and positive-flow upper bounds; not empirical induction from the grid. No independent scientific review, novelty search, formal checker, native BRC/Heartbeat-X6 embedding or accepted Source Result is claimed.

**Next research unit:** classify arbitrary legal triples (v,w,z) outside the box while preserving positive source-specific cylinders and `gamma=0`. Seek a finite *all-signed* separating-family theorem using the 5D feature-flow polytope `(x,y,u,T_P,T_Q)`, or find a full-rank four-hull equality candidate with exact ≤5 LR-vertex convex-combination certificates for **all** 4096 FULL observations. Only after four-hull equality is proven attempt real seedless LR-image nonmembership and separately prove native X6 observer transfer.
