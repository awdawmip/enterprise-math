# EC49Q — Action-label capacity needs resource compatibility

Status: AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED (2026-10-29).
Author attribution: R4-LOCAL-EC49Q-20261029T0226-AUTHOR (local, not a native session or Task claim).
Previous independent author candidate: EC49P Draft PR #1654, head 566bf7710a0712b0d2979dc7bac02f7c38d9af1a.
Frozen GLOBAL_KNOWLEDGE_V1 main@45f3fcf5797f8a443fbb352e7919127fa64426f3;
Enterprise Math main@e7c95b1aaf9de68dd4165a40de5c7257abbb62bd.
P000 original Blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches its startup projection.
P000 and ACTIVE worldview are unchanged.

## Exact auxiliary positive-BRC observer

Two source probabilities P and Q live on four strictly positive rational leaves (W,Z) in {0,1}²:

| W | Z | Q | P | P-Q |
|---|---|---|---|---|
|0|0|1/4|3/8|+1/8|
|0|1|1/4|1/8|-1/8|
|1|0|1/4|1/8|-1/8|
|1|1|1/4|3/8|+1/8|

Both W and Z marginals are P/Q neutral, each uniform on {0,1}. At stage zero an observer sees W, and chooses immediate ACCEPT, immediate REJECT, or buys one sensor A or B. Both purchases reveal *exactly the same* binary Z from the latent leaf. A costs 1, B costs 2. No second purchase exists. On purchasing, W is forgotten; the agent remembers its own action A/B and sees Z, then accepts or rejects. A full controller also remembers W. A compressed controller retains exactly one external memory state (zero extra W bits); no other private coin outcome is retained beyond the action. Source-independent real fresh behavioral randomization is allowed at every information set; no persistent shared random seed. First-action labels K=2, external memory states m=1, |W|=2, hence the bare counting test K*m>=|W| passes.

Let O=(alpha,beta,E_PT,E_QT) be the coupled raw P acceptance, Q acceptance, and two expected sensor costs; T is paid price, not physical time. S_0 and S_full are the raw four-vector sets for compressed and W-retaining policies, respectively. Define L=alpha-beta and
H(O)=alpha-beta-(E_PT+E_QT)/16.

## Theorem 1 — sharp all-real four-vector separation

For every legal real behavioral policy,
sup_{S_0} H = 1/16, whereas sup_{S_full} H = 1/8.
A full controller buys cheap A in both W branches and accepts exactly Z=W, attaining
O_full=(3/4,1/2,1,1), L=1/4 and H=1/8.
Therefore this four-vector lies outside conv(S_0) with exact sharp linear-support gap 1/16. The inequality is valid for all real behavioral probabilities; the verification grid is auxiliary.

PROOF. Write x_w=Pr(buy A|W=w), y_w=Pr(buy B|W=w), with x_w,y_w>=0 and x_w+y_w<=1. Since W has equal P/Q mass 1/2,
C=E_PT=E_QT=[x_0+x_1+2(y_0+y_1)]/2.
Immediate acceptance contributes zero to L because the W marginal is source-neutral. After the purchased action a and observed Z=z, a compressed strategy uses an acceptance probability r_{a,z} independent of forgotten W. Directly summing the labeled P-Q leaf differences gives
L=(1/8)(x_0-x_1)(r_{A,0}-r_{A,1})+(1/8)(y_0-y_1)(r_{B,0}-r_{B,1}).
For fixed first-stage probabilities the exact maximum over terminal decisions is
L_max(x,y)=[|x_0-x_1|+|y_0-y_1|]/8.
Consequently,
16H <= 2|x_0-x_1|+2|y_0-y_1| - (x_0+x_1)-2(y_0+y_1)
= max(x_0,x_1)-3min(x_0,x_1)-4min(y_0,y_1) <= 1.
Equality is attained by the compressed controller that buys A only for W=0, otherwise rejects, and after A accepts only Z=0 (cost C=1/2, L=1/8, H=1/16). Another equality witness has x_0=1, y_1=1/2, all other x,y zero; after A accept Z=0, after B accept Z=1. It attains
O_compressed=(9/16,3/8,1,1), L=3/16 and H=1/16.

For full W recall, the total positive P-Q contribution after a purchase at any given W is at most 1/8. Thus
H <= (1/8) sum_w (x_w+y_w) -(1/16) sum_w (x_w+2y_w)
= (1/16) sum_w x_w <= 1/8.
Buying A in both W branches and accepting Z=W attains this. The linear separator carries through to convex hulls. QED.

## Theorem 2 — sharp all-real sensor-budget frontier

For C>=0, let F_j(C) be the supremum of alpha-beta over S_j with expected Q sensor cost at most C (automatically equal to P expected cost). Then:
F_full(C)=min(C/4,1/4).
F_0(C)=C/4 for 0<=C<=1/2;
F_0(C)=(C+1/2)/8 for 1/2<=C<=3/2;
F_0(C)=1/4 for C>=3/2.

PROOF. Full recall gives L <= (sum_w x_w+y_w)/8 <= C/4 and L <=1/4. It achieves equality by purchasing A independently with probability min(C,1) in each W branch, then accepting Z=W.

Compressed controllers obey L_max(x,y) above. If the signs of x_0-x_1 and y_0-y_1 agree, then L<=1/8 because x_w+y_w<=1. Otherwise relabel W so x_0>=x_1 and y_1>=y_0. Removing x_1 and y_0 does not reduce L or increase cost; set u=x_0 and v=y_1 with u,v<=1 and u/2+v<=C. The maximum of (u+v)/8 is achieved by filling cheaper u first, giving precisely the three pieces stated: u=2C,v=0 to C=1/2; u=1,v=C-1/2 through 3/2; u=v=1 after 3/2. For C<=1/2, same-sign strategies also satisfy L<=(sum x+sum y)/8<=C/4; for C>=1/2 their 1/8 bound is below the displayed frontier. This proves the sharp all-real result. In particular, at budget 1, full L_max=1/4, compressed L_max=3/16, gap 1/16. QED.

## Theorem 3 — raw-region equality when action labels are free resource-compatible clones

Take arbitrary finite W and Z and two strictly positive P/Q source tables on (W,Z). At first stage W is observed, then forgotten after an optional one-stage purchase. Suppose K available purchase actions are *exact source-wise observational clones*: they all induce the same conditional Z kernel given W for both sources and charge the same deterministic price c. A compressed observer remembers the chosen action, the sensor output Z, and one of m causal external-memory states D. If |W|<=K*m, its *entire raw coupled four-vector region* equals that of a full W-retaining observer, for all real fresh source-independent behavioral randomization. If the source masses and c are rational, every attainable rational four-vector admits an all-rational compressed fresh behavioral strategy.

PROOF. Fix any injection f:W -> {1,...,K} x {1,...,m}. For any full controller, let n_w be its immediate-acceptance probability, r_w its total purchase probability, and a_{wz} its terminal acceptance probability after purchasing, averaged over its possibly randomized original first-action label. Clone equivalence makes the original first-action label independent of Z conditional on W and purchase, so a_{wz} is source-independent. When W is visible the compressed controller accepts immediately with n_w, purchases clone f_1(w) with probability r_w while recording D=f_2(w), otherwise rejects. At the terminal information set (action,D,Z) decodes W; accept with probability a_{wz}. This preserves both sources' acceptance and price expectations with no shared seed. The full controller can simulate the compressed one, proving equality of raw sets, not just convex hulls.

For rational realization, set t_{wz}=r_w a_{wz}; use variables n_w,r_w,t_{wz} with 0<=n_w, 0<=r_w, n_w+r_w<=1 and 0<=t_{wz}<=r_w. Their source-coupled coordinates are LINEAR:
alpha=sum_w P_W(w)n_w + sum_{w,z} P(w,z)t_{wz};
beta=sum_w Q_W(w)n_w + sum_{w,z} Q(w,z)t_{wz};
E_PT=c sum_w P_W(w)r_w; E_QT=c sum_w Q_W(w)r_w.
The feasible variable polytope is rational and bounded. For any rational target in its linear image, the nonempty rational polyhedral fiber contains a rational point. Reconstruct each a_{wz}=t_{wz}/r_w (or zero if r_w=0) and implement the displayed code. QED.

## Meaning, BRC scope, and executed checks

Theorem 3's price-compatibility hypothesis is essential: Theorem 1 has K*m=|W| and identical observation kernels, yet every code identifying W by action must sometimes use the higher-priced action B. A full controller retains W and can always use the cheapest A. There is no cost-neutral padding channel at the budgeted frontier. EC49P's previous exact one-bit variable-order compilation has additional structure and a fourth disjoint padding code; it remains valid for its specifically declared model.

Typed branch audit: the carrier is two labeled positive rational four-leaf weighted BRC measures; derived P-Q is a source-comparison signed observer, not native BRC signed/phase amplitude. Preserve joint (W,Z,action) provenance through acceptance and resource evaluation. This result does not define or execute X6 or heartbeat dynamics, nor alter P000/ACTIVE worldview. Native morphism, higher-stage padding cone and independent scientific review remain open.

Actual local execution: Python standard-library Fraction VERIFY.py verifies positivity and all one-variable marginals; evaluates 256 compressed and 4096 full-memory deterministic policies; verifies both displayed sharp witnesses; evaluates 849 feasible rational initial-policy grid cases across eight price budgets; and checks 4096 equal-price-clone deterministic policies. EXACT_REPORT.json is the emitted report. All finite assertions passed. The all-real proofs above use direct identities and inequalities, not extrapolation. See SOURCES.md and NEXT_TASK.md for references and the smallest independent successor question.
