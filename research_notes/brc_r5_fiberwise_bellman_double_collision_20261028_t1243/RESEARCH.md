# R5 — Fiberwise Bellman coherence and two-collision exact certificate (2026-10-28)

**Source/authority:** TASK_RESEARCH author Researcher-ID EM-R5-6D91B (locally assigned, not service-issued; initial provenance label LOCAL_EMR5_20261028_T1243_6D91B); AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. No Source CLAIM, native Result, Driver review or native-X6 dynamical conclusion. Frozen account GLOBAL_KNOWLEDGE_V1 main@9d3ce260cda21bf85d85bdf1fd2d3ee832c7e624; Enterprise Math input main@07c2115ae6e256a11b4ff67e523a592e18f19bfd. Immediate predecessor: research_notes/brc_r5_face_normal_gate_leakage_20261028_t11/PROOF.md at ab903f363f0b6f4630e0bce2401f969c28152450. P000, native X6/time, joint observer-preservation, portable protocol and BRC priority are respected. This is a *typed external passive finite P/Q observation experiment*, with explicitly indexed time, not a native X6 experiment.

**Mother problem:** seek strictly positive rational finite trees whose real no-persistent-seed LR strategies have equal four-dimensional convex hull but unequal true image. The new eight-leaf tree below has a **strict signed support gap**, so it is a mathematical screening certificate, not the target witness.

## Definitions

For each history h at time t: p_h=P(h)>0, q_h=Q(h)>0, r_h=p_h/q_h. Stop and declare P with behavioral probability z_h, or Q with probability 1-z_h. Let O=(e_P,e_Q,T_P,T_Q), where e_P=P(declare Q), e_Q=Q(declare P), T_P=E_P[tau], T_Q=E_Q[tau]. LR behavior may depend only on (t,r), with fresh local randomness and no persistent seed. Full behavior sees the entire history.

## Theorem 1 (terminal-label fiber averaging: exact for the **true** four-image)

Fix arbitrary full-history stop/continue behavioral kernels. Let c_h be conditional probability flow of stopping at h, w_h=q_h c_h its Q-stopped mass. At each fiber F=(t,r) with W=sum_F w_h>0, set a *single* declaration probability z_F=(sum_F w_h z_h)/W. For W=0 choose any z_F. The exact contribution to the observer is

e_P(F)=r W(1-z_F); e_Q(F)=W z_F; T_P(F)=t r W; T_Q(F)=t W.

Hence replacing **all terminal labels** by their time/LR-fiber averages preserves all four coordinates, for every choice of prior full-history stop/continue controls. Proof: p_h=r q_h within F, so sum_h p_h c_h(1-z_h)=r[W-sum_h w_h z_h]; the other three equalities follow by summation. This establishes declaration-only quotient sufficiency, not LR-only *stopping* sufficiency; branch/provenance information remains needed for upstream and future actions. It retains no assertion about full stopped trajectory laws.

## Theorem 2 (sourcewise Bellman coherence and quantitative gap)

Fix any signed lambda∈R^4, a full or LR policy pi, and one reached LR information set F of mutually exclusive histories. Let x∈[0,1] be pi's common continuation probability. Freeze all earlier and downstream conditional actions, including stop-label kernels. Define **unconditional** D_h as lambda·O when h continues surely minus lambda·O when h stops surely, holding all other local actions fixed. Then choosing independent full-history continuation probabilities x_h changes the baseline cost by sum_h x_h D_h. Thus the full-history modification choosing each x_h=1_{D_h<0} improves upon common x by exactly

G_F(pi)=x sum_F D_h - sum_F min(0,D_h) >=0.

If pi is globally LR-optimal for minimizing lambda·O, then V_LR(lambda)-V_full(lambda)>=G_F(pi). When sum_F D_h=0, the bound is the **x-independent** half-L1 residual

G_F(pi)=(1/2)sum_F |D_h|.

Consequently all-direction convex-hull equality requires sourcewise sign coherence at *every* globally optimal LR policy: if x=0 all D_h>=0; if x=1 all D_h<=0; if 0<x<1 all D_h=0. Proof: reach masses at F are determined upstream; after fixing conditional descendants, disjoint subtrees give an affine sum. Minimizing each x_h in [0,1] gives the identity; independent full-history changes are feasible.

**Global exposed-face corollary:** for a bilinear patch B(x,y)=B00+xu+yv+xyw whose four corners are truly globally optimizing lambda·O, each reached hidden-source D_h(y) for the x-fiber vanishes at y=0 and y=1. If it is affine in y, D_h(y)≡0. In particular the aggregate equations lambda·u=lambda·(u+w)=0 are insufficient: require per-source Bellman ties and a separate full Bellman global-optimality check. The condition is necessary, not sufficient.

## Theorem 3 (strictly positive rational eight-leaf double-collision model)

First observation mandatory at t=1. The four observed source histories HA,HB,LA,LB may stop at t=1 or take a final binary observation +/- and stop at t=2. Their unconditional terminal probability table is

| source | P(+) | Q(+) | P(-) | Q(-) |
|---|---:|---:|---:|---:|
| HA | 9/32 | 1/16 | 3/32 | 3/16 |
| HB | 3/16 | 1/8 | 3/16 | 1/8 |
| LA | 3/32 | 1/16 | 1/32 | 3/16 |
| LB | 1/16 | 1/8 | 1/16 | 1/8 |

Each Q root mass is 1/4; P root masses respectively 3/8,3/8,1/8,1/8. Both laws sum exactly to one. There are two collided t=1 LR groups H (r=3/2) and L (r=1/2). t=2 has ratios 9/2,3/2,1/2,1/6, including cross-group *terminal* collisions. These terminal collisions do not themselves impose a classification limitation by Theorem 1.

For L=e_P+e_Q+(1/8)T_P (lambda=(1,1,1/8,0)), optimal stop classification cost at h is min(p_h,q_h); optimal continuation classification cost is sum_s min(P(hs),Q(hs)). Exact gains from observing one more binary outcome are

g_HA=3/32, g_HB=0, g_LA=1/32, g_LB=0.

At a source, its unconditional continue-minus-stop cost is D_h=p_h/8-g_h, giving

(D_HA,D_HB,D_LA,D_LB)=(-3/64,+3/64,-1/64,+1/64).

The aggregate advantage within *each* LR group vanishes. So every shared H continuation x∈[0,1] and L continuation y∈[0,1] achieves the same LR-minimized loss. Nevertheless full history continues only HA and LA, stopping HB and LB. Stopping everywhere has e_P+e_Q=3/4, T_P=1, L=7/8. Therefore

**V_LR=7/8, V_full=13/16, V_LR-V_full=1/16.**

An explicit complete-history optimizer declares P after HA+, Q after HA-, P when stopping HB, P after LA+, Q after LA-, and Q when stopping LB; it yields exactly **O_full=(1/4,3/8,3/2,3/2)** and L=13/16. A fully valid LR policy stopping immediately at t=1 and using the optimal ratio label yields **O_LR=(1/4,1/2,1,1)** and L=7/8. The exhaustive checker also proves no LR policy achieves lower loss; this is not inferred from only those two samples.

Theorem 2 yields exactly 3/64+1/64=1/16 as the hidden-source advantage at the two LR fibers. This explicitly shows a flat aggregate LR score can conceal strictly opposing sourcewise Bellman actions. The model has unequal convex hulls, so it fails the mother objective's first gate.

More generally, for two equal-Q-mass sources where one has gain g>0 and the other zero, and each continuation incurs identical unconditional time cost k, the exact price-loss gap is

Delta(g,k)=min(0,2k-g)-min(0,k-g)-min(0,k).

It equals min(k,g-k) for 0<=k<=g, and zero for k<0 or k>g. In this model (g_H,k_H)=(3/32,3/64), (g_L,k_L)=(1/32,1/64).

**Nontrivial terminal-fiber averaging check:** at t=2 and r=3/2, the leaves HB+, HB-, LA+ with parent continuations 1/2 and 3/4 have Q-stopped weights (1/16,1/16,3/64). Their source-specific probabilities to declare P (1,0,1/3) average to z_F=5/11 at W=11/64; both before and after compression contribute (e_P,e_Q)=(9/64,5/64).

## Exact validation and scope

Accompanying VERIFY.py uses Python Fraction throughout, with 1296 exhaustive full deterministic strategies (6^4) and 144 exhaustive LR deterministic strategies (3^2·2^4), checking normalization, all ratio groups, both minima, local Bayes gains, sourcewise residuals, triangular gap and exact terminal-label averaging. All real behavior policies are included in the extremum claim because this finite objective is multi-affine in each independent conditional randomization variable and attains minimum at a vertex. Captured output: EXACT_OUTPUT.txt, ending `ALL EXACT DOUBLE-COLLISION SIGN-COHERENCE CHECKS PASSED`.

BRC interface: REUSE_APPLIED to positive-rational labeled branch masses and likelihood ratio, preserving source, joint P/Q weights, time and terminal labels until the declared four-coordinate observation. External Fraction computations do **not** constitute native Heartbeat/BRC–Shor arithmetic or physical X6 validation. For native interpretation, a six-dimensional Cell-state embedding and future-observer preservation bridge are separate proof obligations.

Relevant historical background, not sources of this new certificate: Blackwell (1953), *Equivalent Comparisons of Experiments*, DOI 10.1214/aoms/1177729032; Bahadur (1954), *Sufficiency and statistical decision functions*, DOI 10.1214/aoms/1177728715.

**Next:** build at least two **nonterminal causally interacting** LR collisions (with shared downstream stop/continue decisions). Before testing rank-three/nonconvexity, compute every D_h for candidate exposed normals, demand sourcewise coherence and full Bellman global exposure, then use Theorem 1 to quotient terminal labels, certify all-direction support equality, and finally attempt true-image nonrealizability. Owner, CLAIM, Source Result and independent Driver admission remain separate.
