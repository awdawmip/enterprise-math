# R4 eight-leaf BRC observer: signed support loss and minimal one-bit residual repair

**Contributor:** EM-R004-8LEAF11, locally allocated TASK_RESEARCH identity; activity RA-EMR4-20261027-1600-T11-EIGHTLEAF. **Research status:** author proof and exact finite verification; UNREVIEWED / NOT_ADMITTED. Native owner inventory returned CONTROL_QUOTA; there is no native CLAIM, Result or independent Driver acceptance.

**Pinned context:** GLOBAL_KNOWLEDGE_V1 main a3c59d04ad4cdb1e444c785b4ca3b3732674d4fd (bootstrap, operating manual, P000 V4, ACTIVE worldview and mathematical policy); Enterprise Math main 99eb207957daa0395c1915f32cff9752a32b3b2a (portable research protocol). This is a new eight-leaf external finite observation model, distinct from the earlier ten-leaf signed-cone model at commit e3fd6ac5377322c042cc0afb17b7001abbc1604b.

## 1. Model and observer classes

The optional-stop observation times are t=1,2,3. Stage 1 reveals U or V, with common P and Q masses u and (1-u). Stage 2, conditional on U, reveals A or B with common probabilities (1-v), v. Conditional on V, reveals C or D with common probabilities 1/2, 1/2. Stage 3 emits + or -. All paths other than UB have the same final conditional (1/2,1/2) under P and Q. UB has conditional P(+|UB)=p and Q(+|UB)=q. Assume 0<u,v<1 and 0<q<p<1. Thus both measures assign positive mass to all eight terminal leaves.

Current likelihood ratio L_t=P(history)/Q(history) equals 1 at every stage-1 and stage-2 node; at stage 3 it equals p/q on UB+, (1-p)/(1-q) on UB-, and 1 on the six neutral leaves.

The readout of a causal binary terminal decision D, with stopping time T, is

    O=(alpha,beta,tP,tQ)=(P(D=1),Q(D=1),E_P T,E_Q T).

F permits full-history stochastic action kernels. L permits decisions only as functions of time, current L_t and fresh local private randomness; it does not carry any extra historical or persistent random state. B additionally carries a single causal memory bit. At t=1 the bit distinguishes U and V; at t=2 it distinguishes UB from UA, VC, VD. Terminal L_t distinguishes UB+/- from all neutral leaves. B uses only (t,L_t,bit) and private local randomization. Clearly S_L subset S_B subset S_F.

The model is auxiliary positive finite-measure BRC observer mathematics. It performs no typed native heartbeat/BRC–Shor operation, no six-axis spatial calculation and no physical residual attribution. Its exact integer/rational arithmetic is confined to the explicitly declared external probability model.

## 2. Exact five-parameter support theorem

Define the signed functional J_c(O)=alpha-beta-c(tP+tQ) with c>0, and delta=uv(p-q). Then, for **every real tuple in the declared domain**,

    sup_F J_c = -2c + max(0,delta-2cu(1+v)),
    sup_L J_c = -2c + max(0,delta-4c).

Proof. The first observation necessarily occurs at t=1, costing 2c across the two source expectations. Every node before stage 3 has equal P and Q mass. Stopping on any such node has zero value for alpha-beta, regardless of choosing D=0 or D=1. Only the terminal UB+ outcome has strictly positive mass difference, and the optimal terminal test accepts UB+ but not UB-. Its total gain is delta; all neutral leaves have zero difference.

For a full-history observer, reaching stage 2 only on U incurs incremental time price 2cu. There it is optimal to observe stage 3 only on UB, with incremental cost 2cuv and potential gain delta. Continuing on V, UA, VC or VD pays a strictly positive time price for zero discrimination gain. The Bellman improvement over immediate stopping is therefore

    max(0,-2cu+max(0,delta-2cuv))
      = max(0,delta-2cu(1+v)).

For L, time and current likelihood ratio are identical at all first-stage histories and again at all second-stage histories. A deterministic L-policy must stop at stage 1, continue then stop at stage 2 (strictly worse due to 2c cost), or continue everywhere to stage 3 (incremental cost 4c, reward delta). The Bellman improvement is max(0,delta-4c). Every locally randomized policy has value affine in each local decision distribution and cannot exceed the deterministic Bellman maximum. Both identities follow without finite-sample extrapolation.

The gap is

    G=max(0,delta-2cu(1+v))-max(0,delta-4c).

Since u(1+v)<2, the nonempty interval

    delta/4 <= c < delta/[2u(1+v)]

gives G=delta-2cu(1+v)>0. Hence the four-dimensional observable convex hull is strictly reduced by time/current-likelihood-ratio compression on an open family of strictly positive source models.

### Fully explicit rational certificate

Take u=v=1/2, p=3/4, q=1/4 and c=1/16. In leaf order UA+,UA-,UB+,UB-,VC+,VC-,VD+,VD-,

    16 P = (2,2,3,1,2,2,2,2),
    16 Q = (2,2,1,3,2,2,2,2).

Both sums equal 16 and every leaf is strictly positive. A full observer stops/rejects V at t=1, continues U, stops/rejects UA at t=2, continues UB, and accepts only UB+ at t=3. It realizes

    O_full=(3/16,1/16,7/4,7/4);
    sup_F J_c = -3/32.

An optimal L-observer stops/rejects at t=1, with O_L=(0,0,1,1) and

    sup_L J_c = -1/8.

The exact strict separating gap is 1/32. This single linear normal proves the two convex hulls differ; it is not an exhaustive enumeration of all facet normals.

## 3. One binary residual state recovers the ORIGINAL readout region

**Theorem.** For every real parameter tuple in section 1, S_B=S_F, for the full original four-coordinate readout set (not only its convex hull). No persistent public random seed is necessary. In the strict-gap interval, the supplement of one binary bit is minimal in state count compared with the LR-only, zero-bit observer.

**Proof by exact source-symmetric occupation aggregation.** One inclusion is immediate because F can imitate B. To prove F subset B, begin with any randomized full-history stopping/decision policy, including arbitrary dependence on prior observed branches. Replicate its stage-1 actions separately on U and V; the bit stores that distinction.

At stage 2, the state UB is individually recognizable by bit=1 and its full action kernel can be copied. The remaining reachable states G0={UA,VC,VD} have bit=0. For each h in G0, let w_h be the source mass reaching that state (including survival). Because P=Q on every history up to stage 2, w_h is identical under P and Q. Let k_h(a) be the original conditional probability of action a in {stop0,stop1,continue}. If W=sum_h w_h>0, set the bit-0 action probabilities to

    k_0(a) = (sum_h w_h k_h(a))/W.

If W=0, that state is unreachable and its kernel is irrelevant. This one source-independent stochastic action kernel preserves, separately under P and Q, the exact aggregate early-reject mass, early-accept mass and mass continuing to t=3. It also preserves the time contributions at t=2 and t=3, because all aggregated histories have the same stage index.

If any bit-0 neutral paths continue to stage 3, their final + and - observations are source-neutral under both P and Q. Set the terminal LR=1 acceptance probability equal to the total full-policy acceptance mass across those continued neutral leaves, divided by their total reached mass. The numerator and denominator are the same under P and Q. The final acceptance contributions to alpha and beta agree exactly and all such paths stop at t=3. UB+ and UB- remain distinguishable by their final likelihood ratios p/q and (1-p)/(1-q), so their original conditional terminal decision kernels can be copied. Thus the four readout coordinates match any chosen full policy with ordinary local stochastic kernels. This proves S_F subset S_B and hence equality.

The strict linear witness in section 2 excludes any zero-bit L implementation of the entire set. Since the displayed causal bit transducer realizes all of it, one bit is state-count minimal in that interval. The bit stores a *future-informative history class*; it is not an extra native X6 dimension or a physical force/residual claim.

## 4. Exact independent check and boundaries

The executable GitHub file VERIFY.js was run as exactly the source string submitted to GitHub using the available JavaScript runtime. It checks the full explicit rational leaf table, enumerates all 3^6*2^8 = 186624 deterministic full observers, and all 3^2*2^3 = 72 deterministic L observers. For each of the 186624 full policies it also constructs the one-bit pooled occupation readout and checks all four integer-scaled coordinates. It confirms full optimum -24/256, L optimum -32/256, exact gap 8/256=1/32, and full-witness observer (3/16,1/16,7/4,7/4); all assertions pass. These finite enumerations exactly cover the declared rational witness; the all-real five-parameter theorem follows from the Bellman and occupation-flow algebra above.

A larger independent Python Fraction implementation additionally enumerated the same finite policies, checked all one-bit projections, verified 243 rational parameter tuples by node Bellman recursion (141 strict-gap cases), and produced a local proof/verification evidence package. Project admission and independent adversarial review remain distinct from author checks.

**Next open question:** in a horizon-2 strictly positive tree with LR-colliding first histories and different conditional future experiments, identify the minimum leaf count giving a strict four-observer separation, and characterize when one residual bit restores the complete original region. Preserve P/Q time observables and causal memory semantics. Native BRC/X6 transfer must independently establish state/path typing, slice embedding, readout and future-operation preservation.
