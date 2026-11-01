# R5: source-symmetric law-sensitive answer-changing K tails retain the exact FULL/LR support gap

Date: 2026-11-01 Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Frozen inputs and domain
GLOBAL_KNOWLEDGE_V1 main@529a3dfc7f127bd262e0b0571696a5ae2735d200 (both canonical entries, P000_STARTUP projection with matching original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview, BRC/mathematical activity routing). Enterprise Math main@f1e437bcd8fae1135b671780b8f7a64006f7f1ff (AGENTS, P000, residual/joint-preservation and portable research). Exact predecessor: PR #1663 commit 8406dcd9f4545d0f52ddb2964c046744b05c5161, research_notes/brc_r5_third_genuine_collision_uniform_gap_20261101_t1640/RESEARCH_INVARIANT.md. This is an auxiliary finite classical two-measure stopping model, not a native X6/heartbeat implementation. No mathematical admission or independent review is claimed.

## Model and BRC positive flow
Preserve initial source P/Q masses A1=(1/8,1/8), A2=(1/8,1/8), B=(1/4,1/8), C=(1/2,5/8). Each A source at I=(time 1,LR 1) stops with answer P under p_i, or continues to P/Q high nature probabilities (1/2,3/4), stopping time 2 answer Q, and low (1/2,1/4), reaching J=(time 2,LR 2). At J, stopping q_i answers P at time 2. Continuing takes P/Q tail-P fractions (2/5,1/2) and tail-Q (3/5,1/2); tail Q answers Q at time 3. B at J stops P at time 2 under qB and otherwise at time 3. C stops Q at time 1 under r and otherwise P at time 3.

Each A-tail-P source has pre-split two-law mass (1-p_i)(1-q_i)*(1/40,1/64). A fraction 1-epsilon ends at time 3 answering P; fraction epsilon enters the true shared K=(time 3,LR 8/5). At K FULL uses k1,k2 independently; LR uses common k. Stopping at K answers P at time 3. Continuing K reaches a *law-sensitive* nature branch: probability a under P, b under Q ends answer Q at time 4, complementary probabilities 1-a and 1-b end answer P at time 3+h. Assume 0<epsilon,a,b<1 and integer h>=2. Both laws assign strictly positive nature probability to both outcomes. Since times 4 and 3+h>=5 differ, the continuation branches with different answers cannot conflict at the same time/LR terminal key. All other equal time/LR keys preserve their response; no decision key repeats along one trajectory. Example epsilon=1/2,a=3/4,b=1/4,h=2 gives continuation terminal LRs 24/5 and 8/15.

Carry ordered source/path labels and two positive probability masses (BRC positive rational branch carrier) until applying the observer O=(eP,eQ,TP,TQ), with eP=Pr_P(answer P), eQ=Pr_Q(answer Q), TP and TQ expected stopping times. The signed dual support functional H=5eP+5TP-8TQ does not make the positive masses signed. The observer projection is NOT declared safe for arbitrary future operations or native X6. BRC reuse status: REUSE_APPLIED (exact branch-flow and observer laws, no claim of running a native toolbox executable).

## All-real theorem, including a much broader K continuation
More generally, replace K's fixed two-terminal continuation by ANY fixed source-symmetric terminal process (no additional source-dependent behavior decisions) whose conditional outcome law is identical for A1 and A2 under P respectively under Q, but whose P law may differ from Q law, including changed terminal answers and arbitrary finite-mean stopping times. Let
 u=Pr_P(final answer Q | K continued),
 dP=E_P[T-3 | K continued], dQ=E_Q[T-3 | K continued],
 gamma=-u+dP-dQ, alpha=epsilon*gamma.
For the explicit strict-positive two-terminal example gamma=b*(h-1)-a*h. These are model parameters; gamma can have either sign or any finite magnitude.

For ALL real policy parameters in [0,1], exact positive source mass accounting proves
 H_FULL=-33/8+SUM_{i=1,2}[13*p_i/16-p_i*q_i/8+q_i/8+alpha*(1-p_i)*(1-q_i)*(1-k_i)/8]-qB/4+5*r/2,
 H_LR=-33/8+(13*p-2*p*q+20*r)/8+alpha*(1-p)*(1-q)*(1-k)/4.

Set beta=min(0,alpha). The exact global extrema are
 min_FULL H=-35/8+beta/4,
 min_LR H=-33/8+beta/4.
Hence max_FULL(-H)-max_LR(-H)=1/4 throughout the stated *all-real* family, including all strict-positive a,b,epsilon and all integer h>=2. Every FULL minimizer W has distance_infinity(W,conv(LR)) >= (1/4)/(5+0+5+8)=1/72. The LR observation image retains affine rank exactly 4: the k=1 slice recovers the previous bilinear four-column chart with determinant magnitude 59/20480.

## Proof
At K, one A source has P entry mass x=epsilon*(1-p_i)*(1-q_i)/40 and Q mass 5*x/8. Continuing instead of immediately answering P at time 3 changes eP by -x*u, TP by x*dP and TQ by (5*x/8)*dQ. It therefore changes H by 5*x*(-u+dP-dQ)=alpha*(1-p_i)*(1-q_i)/8 (times the continuation probability 1-k_i). No equality of conditional P/Q nature laws is used. Other branch contributions are the predecessor's exact positive mass formulas, yielding the two displayed global H identities.

For FULL, minimize over k_i, leaving beta*(1-p_i)*(1-q_i)/8 >= beta/8. The remaining source contribution p_i*(13/16-q_i/8)+q_i/8 is >=0 for all real p_i,q_i in [0,1], attaining 0 at p_i=q_i=0. Set qB=1,r=0. This gives min_FULL H=-33/8+2*beta/8-1/4=-35/8+beta/4.

For LR, minimize over k, leaving beta*(1-p)*(1-q)/4 >= beta/4. The remaining p*(13-2*q)/8+(5/2)*r is nonnegative, attaining zero at p=r=0; choosing q=0 attains the beta/4 term. This proves min_LR H=-33/8+beta/4. For beta<0 the extrema choose k1=k2=k=0; for beta=0 choose all k=1. The FULL minimizer additionally chooses qB=1 while LR necessarily couples qB=q=0. Extrema of a linear functional are invariant under convexification, establishing a strict support gap. The L-infinity lower bound follows from Holder inequality with ||H||_1=18. With k=1, K's continuation vanishes and the inherited four-dimensional chart has exact determinant magnitude 59/20480. QED.

## Exact arithmetic and boundaries
Independent standalone Python standard-library Fraction verifier: 54 rational parameter tuples epsilon in {1/3,2/3}, a,b in {1/4,1/2,3/4}, h in {2,3,7}; all 16 LR and 256 FULL deterministic policies per tuple; 14,688 exact observer evaluations, positive two-law normalization, all formula comparisons, extrema and four-dimensional rank. Of the 54 tuples, 36 have a!=b. The executable and genuine stdout appear as VERIFY.py and EXACT_OUTPUT.txt alongside this proof. The finite grid checks implementation fidelity; the all-real result is proved algebraically, not inferred from sampling.

Explicit law-sensitive, answer-changing case epsilon=1/2,a=3/4,b=1/4,h=2 has gamma=-5/4, min_LR=-137/32, min_FULL=-145/32, support gap 1/4. It changes *both* P/Q nature law and final answers and still fails hull equality.

Scope limit: the theorem assumes that the two A sources have the same continuation conditional laws under each measure. It DOES NOT exclude K branches whose continuation advantage genuinely depends on source identity, new source-sensitive future decision collisions, changes at I/J/B/C, or all conceivable three/four-key stopping models. The R5 mother question remains OPEN. No full convex-hull equality, actual image inequality, native X6 transfer, or independent science review is asserted. Current native gateway status was research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED and active job quota 5/5; no live owner, CLAIM or Result receipt has been verified.

## Next concrete unit
Construct a strict-positive source-dependent continuation at K with different signed advantages gamma1!=gamma2 across A1/A2 while preserving true time/LR keys and consistent terminal answers. First test exact signed H support; positive gap is a kill. A zero gap is only a screening condition, NOT full hull equality. Then provide complete four-dimensional FULL-vertex LR-hull rational primal combinations or signed Farkas separation certificates, and only upon exact full-hull equality seek an actual real LR behavioral nonmembership witness. Preserve source labels before observer projection.
