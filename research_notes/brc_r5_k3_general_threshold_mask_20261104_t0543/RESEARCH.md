# R5 K3: general clock threshold mask and exposed error-fiber theorem
Date: 2026-11-04 Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Frozen scientific pins: GLOBAL_KNOWLEDGE_V1 a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current normative policy read separately; P000 and ACTIVE worldview unchanged.

## Model (exact)
S=(C,I,BJ,IJ), c=(1/8,1/6,1/16,3/32), all positive. FULL upstream 0<=x,y<=1 and 0<=i<=1-x. Seedless LR forces i=(1-x)y. w=(1/8,(1-x)/6,y/16,3i/32); d=y/16+3i/32. FULL may choose independent local (z_s,t_s,u_s) in [0,1]^3; seedless LR must use common local (z,t,u). Set M_s=w_s z_s, S_s=2M_s t_s/3, U_s=S_s u_s. All 16 clock and terminal parameters r_s,v_s,p_s,q_s are independently real in (0,1). Four observers:
eP=107/128-21x/128+d/4-(sum S_s)/2+sum(p_s S_s)/8;
eQ=13/64+3x/64-d/2+(sum S_s)/8+sum(q_s S_s)/32;
TP=3+sum M_s+(3/2)sum S_s+sum r_s U_s;
TQ=3+(sum M_s)/2+(3/8)sum S_s+sum v_s U_s/4.
Exact observer source: predecessor 052f159cca1094de533d40b2de5860d50666abc1, research_notes/brc_r5_k3_two_level_fiber_complete_20261104_t0435/RESEARCH.md. This is an auxiliary finite two-law experiment, not an asserted physical X6 embedding. BRC reuse: REUSE_APPLIED; preserve provenance labels, positive capacities and d fiber.

## Theorem (all real K3 parameters)
Define mu_s=(9+2v_s)/(8(3+r_s)). For any tau in (0,3/8) not equal to any mu_s, let D={s: tau>mu_s}. If D is a nonempty proper subset of S, then the four-observer convex hulls of FULL and seedless LR differ, for every p_s,q_s in (0,1). Therefore a sufficient open clock region for separation is
min_s mu_s < min(max_s mu_s,3/8).
This includes independently nonproportional time kernels.

Exact normal n0=(0,0,tau,-1). Define b=3tau-3 and g_s=(2+2r_s/3)tau-3/4-v_s/6. The signed support functions satisfy
h_FULL(n0)=b+sum_s c_s max(g_s,0),
h_LR(n0)=b+max_{B in M} sum_{s in B} c_s g_s,
M={empty,{C},{C,I},{C,BJ},S}.

Proof. For one source unit weight the four deterministic stopping stages 0,1,2,3 have normal increments 0, tau-1/2, 2tau-3/4, and g_s. In (0,3/8) the middle two are negative. FULL chooses stage 3 exactly at positive g_s and stage 0 otherwise; the FULL upstream (x,y,i)=(0,1,1) realizes all positive capacities c_s simultaneously. Algebra gives g_s>0 iff tau>mu_s. LR's common stage must be 0 or 3. At stage 3 its source score is bilinear in (x,y); the four upstream corners correspond to {C,I}, S, {C}, {C,BJ}. Together with stage 0 they give the mask family M, proving both support formulas.

For the nonempty proper set D of positive g_s, define P=sum_{s in D}c_s g_s>0. For any LR mask B,
P-sum_{s in B}c_s g_s = sum_{s in D\B}c_s g_s + sum_{s in B\D}c_s(-g_s).
Every term is nonnegative, and equality requires B=D because all c_s>0 and each g_s !=0. If D is not in M, n0 itself strictly separates: h_FULL(n0)>h_LR(n0).

The only accessible nonempty proper masks are D={C}, {C,I}, {C,BJ}. Their sole LR maximizers on the n0-exposed face are, respectively, common stage 3 with upstream (1,0,0), (0,0,0), (1,1,0). Uniqueness holds for real LR behavior: the bilinear score is a convex combination of corner scores, the maximizer corner is unique by strict g_s signs, and stages 1 and 2 are strictly inferior.

Let H be that unique LR four-observer point. Construct FULL point W with upstream (0,1,1), source stage 3 at s in D and stage 0 elsewhere. All four sourcewise M_s,S_s,U_s agree between W and H, so time coordinates and all p_s,q_s-dependent error terms agree. Substituting the baseline x,d yields
D={C}: W-H=(13/64,-1/8,0,0);
D={C,I}: W-H=(5/128,-5/64,0,0);
D={C,BJ}: W-H=(3/16,-3/32,0,0).
Thus W is distinct from the singleton LR n0-exposed face, and so W lies outside the entire LR four-hull. A sufficiently small rational positive perturbation of n0 along eP gives a strict signed support separator because LR has finitely many deterministic vertices and a unique clock maximizer. This establishes the theorem. For the open-region corollary choose tau strictly between min mu_s and min(max mu_s,3/8), avoiding finitely many thresholds. QED.

## Exact arithmetic evidence
The companion standard-library Fraction verifier enumerates all 1536 FULL and 16 LR deterministic observer vectors per case, testing the support equations and the exhibited normal or exposed-fiber separator. It covers three genuinely nonproportional examples and all 14 nonempty proper source masks using rational high/low clock kernels. There were 139 passing exact assertions; the accompanying EXACT_OUTPUT.txt is literal executed stdout. The all-real conclusion follows from the proof, not finite sampling.

Nonproportional D={C,BJ} instance: r=(4/5,1/5,4/5,1/5), v=(2/5,1/8,1/3,1/10), tau=1/3, p=(1/4,1/2,3/4,1/3), q=(3/4,1/2,1/4,2/3). Exposed LR H=(485/768,727/3072,139/40,9079/2880), actual FULL W=(629/768,439/3072,139/40,9079/2880). At n=(1/4096,0,1/3,-1) exact h_FULL=-94083877/47185920 and h_LR=-94086037/47185920. Support gap 3/65536; dist_infinity(W,conv O4(LR))>=9/262192.
Inaccessible D={BJ} instance: r=(1/5,1/5,4/5,1/5), v=(1/10,1/10,3/10,1/10), tau=1/3. Clock support gap 1/360 and distance bound >=1/480.
Nonproportional D={C,I} instance: r=(4/5,7/10,1/5,3/10), v=(2/5,1/3,1/10,1/5), tau=1/3. Mixed support gap 5/524288; distance bound >=15/2097536.

## Frontier and control state
Within this exact K3 model, a necessary condition for four-hull equality is that all mu_s coincide OR min_s mu_s>=3/8. Investigate this complementary region with new signed normals, exact rational four-hull primal/Farkas certificates and subsequent real image membership.
GitHub identity awdawmip is admin/push. Native EM Site read at 2026-11-04: static_machine_readonly, research_authority_granted=false. Native owner query returned CONTROL_QUOTA. No current native CLAIM/Result/independent Driver review was obtained; this PR branch is author-only durable research, not admission.
