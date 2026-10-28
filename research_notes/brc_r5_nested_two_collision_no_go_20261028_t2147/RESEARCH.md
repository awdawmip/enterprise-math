# R5: a single nested LR collision chain has no convex-hull-equal / image-unequal example

Date: 2026-10-28 Asia/Shanghai. Research author: local TASK_RESEARCH identity LOCAL_EMR5_20261028_2147_NOGO_E51C, GitHub account awdawmip. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.

Frozen authority inputs: GLOBAL_KNOWLEDGE_V1 main@3c35bc5fca7735427aa7eb24db858c38ffe90b01; Enterprise Math main@d251140e90dad87106e825c2c83fd8c56fab0b4e. Read global bootstrap/manual, ACTIVE worldview, mathematical/code/BRC/activity policies and TASK_RESEARCH route; project AGENTS, P000, HEARTBEAT X6+time, observer-preservation, portable/autonomous research protocols, and predecessor research_notes/brc_r5_two_collision_occupation_bellman_20261028_t2040/RESEARCH.md. The global P000_STARTUP projection blob did not match current project P000 blob, so the full project p000_reality_foundation.json was read. All deductions below concern a finite N2 two-law sequential statistical observer, not a native X6 embedding. BRC usage is source-preserving positive-rational branch masses, P/Q likelihood-ratio moment transport, and source-specific Bellman increments.

## Precise model

At time 1, exactly two nonterminal hidden histories A,B have the same LR r=P(h)/Q(h)>0 and positive Q arrival masses a,b. Other time-1 histories are terminal and have different LR values. A,B can stop/declare P or Q, or continue to time 2. Their conditional Q kernels q_A,q_B over distinct positive child LR signatures s_1<...<s_n satisfy sum(q_hi)=1 and sum(s_i q_hi)=r; P(child i|h)=s_i q_hi/r. Only one time-2 LR signature s*=s_j distinct from r remains nonterminal. At s* the positive-A/B-arrival source histories have conditional kernels z_A,z_B over positive terminal time-3 LR signatures t_1<...<t_m, with sum(t_j z_hj)=s*. All other time-2 nodes and every time-3 node are terminal. All corresponding branch masses are positive. Full policies may condition stopping/continuing on source A/B; LR-only policies share one local randomized action at each (time,LR), with no persistent random seed. All local behavioral probabilities are real in [0,1].

O=(e_P,e_Q,T_P,T_Q), where e_P=P(declare Q), e_Q=Q(declare P), T_mu=E_mu[stopping time]. Denote achievable true images O_full and O_LR. The goal is to compare all signed four-coordinate objectives, without replacing actual image equality by convex hull equality.

## Theorem (complete minimal-chain classification)

In this precise model, the following are equivalent:

(1) for every signed lambda in R^4, min_{O_full} lambda.O = min_{O_LR} lambda.O;
(2) conv(O_full)=conv(O_LR);
(3) q_A=q_B AND z_A=z_B;
(4) O_full=O_LR as actual sets of real behavioral-policy observables.

Thus this structure cannot satisfy convex-hull equality and true-image inequality simultaneously. When either kernel is heterogeneous, a finite rational separating direction exists whenever the signatures and kernels are rational.

### Proof, first ingredient: stop-loss hinge separates distinct fixed-mean kernels

Take lambda_1=1, lambda_2=c>0. Optimal stopping declaration at LR u incurs Q-mass-normalized error cost phi_c(u)=min(u,c). For d_i=q_Ai-q_Bi, sum d_i=sum s_i d_i=0. H(c)=sum_i d_i min(s_i,c) is a continuous piecewise-linear function with knots s_i, and H(s_1)=H(s_n)=0. If H also vanished at all interior knots, it would vanish on each intervening segment; its slope on (s_k,s_{k+1}) equals sum_{i>k} d_i. All tail sums zero imply every d_i=0. Consequently if q_A != q_B, some rational c=s_k (when signatures rational) gives different E_qA phi_c(s) and E_qB phi_c(s). Identical argument for z_A,z_B with parent s*. (With <=2 distinct signatures, mass+mean already enforce identical kernels.)

### Proof, second ingredient: independent time tilts

The extra cost of one step at LR u with Q arrival mass w is w beta(u), beta(u)=lambda_3 u + lambda_4, since its P mass is u*w. Because s* != r, any beta_1=beta(r) and beta_2=beta(s*) can be prescribed independently:

lambda_3=(beta_2-beta_1)/(s*-r);
lambda_4=beta_1-r lambda_3.

All terminal decisions are still optimized by phi_c independent of the time coefficients.

### Case I: heterogeneous first kernel

Assume q_A != q_B. Choose c from the hinge lemma and set H_h=E_qh[phi_c(s)]-phi_c(r), so H_A != H_B. Choose beta_2 sufficiently large positive that, for both h, beta_2+E_zh phi_c(t)-phi_c(s*)>0. All optimizers then stop at every reached second-layer node. Set beta_1=-(a H_A+b H_B)/(a+b). Source-specific first-layer continuation increments become:

D_A= b*(H_A-H_B)/(a+b);
D_B=-a*(H_A-H_B)/(a+b).

LR policies share one continuation probability, and their total slope aD_A+bD_B=0; they cannot improve the all-stop baseline. Full-history policies continue only the source with negative D. The exact gap is

V_LR(lambda)-V_full(lambda) = ab/(a+b)*abs(H_A-H_B) > 0.

All other time-1 terminal histories contribute an identical baseline. The claimed gap covers all real behavioral parameters because each local objective is affine in its own action probability.

### Case II: equal first kernel but heterogeneous second kernel

Assume q_A=q_B=q but z_A != z_B. Choose c from the hinge lemma at s*, and J_h=E_zh[phi_c(t)]-phi_c(s*), with J_A != J_B. Set w_A=a q(s*), w_B=b q(s*)>0 and beta_2=-(w_A J_A+w_B J_B)/(w_A+w_B). The two second-layer Bellman increments have opposite signs and Q-weighted sum zero. Choose beta_1 sufficiently negative so both full-history sources and the shared LR policy strictly prefer to continue at time 1 (possible independently of the fixed beta_2). Thus first-layer behavior is fixed for all optimizers. At second layer, LR policies cannot improve while full-history policies can select the negative-increment source, yielding

V_LR(lambda)-V_full(lambda) = w_A w_B/(w_A+w_B)*abs(J_A-J_B)>0.

### Case III: both kernels equal

For arbitrary real full-history policy, at each (time, LR) fiber average its action and conditional declaration probabilities using the actual Q arrival masses. Identical future LR kernels transport these averages to the same Q flow at the next fiber, and P/Q=LR on every history makes the P flow match as well. Inductively all (time,LR,declaration) stopping masses under P and Q coincide; therefore e_P,e_Q,T_P,T_Q coincide. This constructs an actual unseeded LR policy, so O_full subseteq O_LR; the reverse subset is immediate. Hence actual image equality. (Any zero-arrival fiber can choose an arbitrary default action.)

Finite policy images are compact. Equality of all signed linear minima is equivalent to equality of their closed convex hulls; a single strict signed gap refutes convex-hull equality. This completes all equivalences.

Scope: exactly one downstream nonterminal LR fiber, with s* != r, and no other free nonterminal decisions. Multiple downstream nonterminal fibers, s*=r, or richer history-state dependencies require separate work.

## Exact uniform rational exclusion for the previous R5 g-family

Freeze first stage: Q(A)=Q(B)=1/4, P(A)=P(B)=3/8; terminal O has Q=1/2, P=1/4 and LR=1/2. r=3/2, s=(1/2,1,2,3), 0<g<4/25. Set

c=(3g/2, 1/5-5g/4, 1/5-5g/4, g);
q_A=c+(9/25,0,0,6/25);
q_B=c+(0,3/10,3/10,0).
At s*=3, t=(1,2,4,5), z_A=(3/8,1/8,1/8,3/8) and z_B=(1/8,3/8,3/8,1/8). All Q/P kernels are positive and normalized.

A single fixed signed direction works for EVERY g:

lambda=(1,1,1,-27/20), or integer multiple (20,20,20,-27).

Here phi(u)=min(u,1); beta(r)=3/20 and beta(s*)=33/20. Since phi(t_j)=phi(s*)=1, continuing at s* strictly increases the target and hence is suppressed. First-layer continue-minus-stop increments are

D_A=-3/100-3g/4 <0,    D_B=3/20-3g/4 >0.

The optimal all-stop baseline is L_0=2/5. Exact Bellman minima are

V_full=2/5-3/400-3g/16;
V_LR=2/5+min(0,3/100-3g/8);

Delta=V_LR-V_full =
  3/400+3g/16, for 0<g<=2/25;
  3/80-3g/16, for 2/25<=g<4/25.

Thus Delta(g)>3/400 throughout the STRICT positive family; its maximum is 9/400 at g=2/25. In that instance, an actual full-history optimal vector (continue A only at time 1; all stop at time 2; resolve LR=1 terminal tie by declaring P) is

O*=(31/100,19/50,11/8,5/4),
lambda.O*=151/400,  inf_{O_LR} lambda.O=2/5.

Since ||lambda||_1=87/20, every real unseeded LR O satisfies

||O-O*||_infinity >= (9/400)/(87/20)=3/580.

For each other g, its corresponding full-history optimal vector is at distance >1/580 from every LR O. This is full-real nonattainment AND convex-hull separation, not a mother-target example. It extends the previous g=23/200 result to an entire family with ONE fixed INTEGER direction, without using heterogeneity of z.

## Independent second-collision-only witness

Take g=23/200, q=(q_A+q_B)/2 at the first stage (so q_A=q_B=q), keep z_A != z_B. Then q(s*)=47/200. Use lambda'=(1,2,3/2,-17/4), integer multiple (4,8,6,-17). Its beta(r)=-2 forces both first-layer sources to continue; beta(s*)=1/4 gives second-layer increments (-1/8,+1/8). Exact all-real optima:

V_full=-18399/6400;
V_LR=-1147/400;
Delta=47/6400 >0.

This independently witnesses Case II, distinct from the first-kernel obstruction.

## Exact checking, prior art, admissibility and next question

VERIFY.py uses Python fractions.Fraction and enumerates all 16 deterministic full source action profiles and all 4 deterministic LR action profiles for each tested rational model. A 159-value strict g sweep and four named cases check both-law normalization, signed gaps, exact witness and second-only construction. Output in EXACT_OUTPUT.txt. Algebra proves the all-real statement; finite checks corroborate its explicit rational instances. No Lean check or independent reviewer is claimed.

External intellectual context, not proof or novelty certification: Khan, Yu, Zhang, Economics Letters 247 (2025), 112146, doi:10.1016/j.econlet.2024.112146; same authors, Journal of Economic Theory 218 (2024), 105841, doi:10.1016/j.jet.2024.105841 (Blackwell information comparisons).

Next smallest unit: introduce TWO downstream nonterminal LR fibers (ideally s_-<r<s_+) so a single affine time tilt cannot independently suppress each, or study the degenerate s*=r chain. First seek a strict all-real separating lambda; only if all signed supports are proved equal proceed to a semialgebraic real-image nonattainment certificate. Keep source occupation/provenance, the X6 future-observer bridge obligation, and formal Source Task/Driver authorization distinct.

Permissions at research time: GitHub authenticated awdawmip with push=true; native Enterprise Math 0.6.11 status research_authority_granted=false, active task inventory query returned CONTROL_QUOTA. Current Source owner could not be verified; no CLAIM, Result, reviewer or admission is asserted. GitHub notes/RA storage are author-side evidence, not formal Task owner mutation.
