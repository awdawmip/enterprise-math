# R5 — Frozen-LR-key rigidity through stochastic splitting and reconvergence

Date: 2026-10-30 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**.

Scientific predecessor: `research_notes/brc_r5_static_origin_chain_hull_rigidity_20261029_t2357/RESEARCH.md` at project commit `db5f207ba5e5768039835139005835cca8731cc6`. Frozen canonical-main inputs for this author-side unit: GLOBAL_KNOWLEDGE_V1 `main@f9bc230e04ba3d082a862bc7f18ae58ba535c36e`; enterprise-math `main@c69bb3d08f7d258f118891e01f9bf8aec610d054`. P000 and ACTIVE worldview remain untouched. This is an auxiliary finite stochastic stopping theorem and explicitly **not** a demonstrated native X6 embedding, physical claim or formal Source Result.

## Exact question and scope

A finite absorbing two-law experiment has a labeled initial source S, strictly positive probabilities P_s,Q_s, m>=2 times, and an exogenous finite tree of nature signals observed upon continuation. Nature may split after the initial source, change terminal signal and reconverge at a coarser current observation; a FULL controller remembers the entire history. Each history h at time j has strictly positive P(h),Q(h), and terminal Bernoulli error probabilities 0<p_j(h),q_j(h)<1 under P,Q. A policy chooses stop/continue, with forced stop at time m. There is no action other than stop/continue before absorption. The four original observers are O=(e_P,e_Q,T_P,T_Q), with error at terminal stop and stopping time as usual.

A seedless LR controller sees only the time j and exact preterminal likelihood ratio L(h)=P(h)/Q(h), and uses real, law-independent behavioral hazards; it cannot retain its own ex ante random seed across decisions. Assume that for each source s and every positive prefix descended from it, **the LR key is frozen**:
[
  L(h)=r_s=P_s/Q_s .
]
This holds in particular when, conditional on S=s and the whole earlier nature history, the same nature-transition kernels are used under P and Q; P and Q may differ in initial source weights and terminal Bernoulli error kernels. Sources with the same r_s form one class g. Crucially, nature can undergo arbitrarily many strictly positive stochastic splits and mergers in the FULL tree; terminal errors may depend on all source and path coordinates.

## Theorem 1 — all-real hull-to-actual-image rigidity with stochastic nature

**For every finite model satisfying the stated frozen-key hypothesis and every real behavioral hazard including 0 and 1, the actual LR observer image and the actual FULL observer image are convex polytopes. Consequently**
[
oxed{operatorname{conv}(mathcal O_{m FULL})=operatorname{conv}(mathcal O_{m LR})
       quadLongleftrightarrowquad
       mathcal O_{m FULL}=mathcal O_{m LR}.}
]

**FULL flow proof, including all boundary policies.** Let x_h be the Q occupancy of a preterminal FULL history, u_h its Q stop mass and v_h its Q continue mass. At initial histories s, x_s=Q_s. At each nonfinal history x_h=u_h+v_h, and for every nature successor h' reached after continuation x_{h'}=K_Q(h'|h)v_h; at final time v_h=0. All entries are nonnegative. These finitely many linear equations and inequalities define a bounded convex flow polytope F_Q. Every feasible flow is realized by the real FULL hazard u_h/x_h when x_h>0 and any hazard at zero occupancy. Since the policy is common to the two laws, P stop mass at h is L(h)u_h, even when the nature kernels differ between P and Q: pathwise P/Q likelihood ratios multiply only nature probabilities, and policy factors cancel. Therefore
[
 e_P=sum_h L(h)u_hp_j(h),quad e_Q=sum_hu_hq_j(h),quad
 T_P=sum_h jL(h)u_h,quad T_Q=sum_hju_h .
]
The FULL image is a linear image of F_Q, hence a convex polytope. This FULL argument, in fact, does not require the frozen-key hypothesis.

**LR simplex proof.** Under the frozen-key hypothesis, LR actions for class g depend only on (j,r_g), not on the realized source/path. Every real LR policy induces a common conditional stop-time distribution d_g=(d_g1,...,d_gm) in the simplex Δ_m. Conversely, every such d_g is implemented by successive hazards d_gj/(sum_{k>=j}d_gk), with arbitrary choices on zero-survival nodes. Let ar p_{sj}=E_P[p_j(H_j)|S=s] and ar q_{sj}=E_Q[q_j(H_j)|S=s], where H_j is the nature path under the always-continue coupling. Then
[
 e_P=sum_gsum_j d_{gj}sum_{sin g}P_sar p_{sj},quad
 e_Q=sum_gsum_j d_{gj}sum_{sin g}Q_sar q_{sj},
]
[
 T_P=sum_g P_gsum_jj d_{gj},qquad T_Q=sum_g Q_gsum_jj d_{gj}.
]
Thus the actual LR image is the affine image of ∏_g Δ_m, a convex polytope. LR is a subclass of FULL; equality of convex hulls therefore is exactly equality of actual images. QED.

This theorem extends the static-origin/no-post-initial-nature rigidity frontier to arbitrary finite genuine stochastic branching and reconvergence **provided no new exact LR-key information is generated**. It does not assume path-insensitive terminal kernels, predictor lumpability of terminal outcomes, or zero residual. It rules out an entire class of candidate constructions, not all changing-key multi-merger models.

## Theorem 2 — BRC path-covariance residual, exactly typed

Under the same frozen-key assumptions, use the *potential all-continue nature path* H in class g, with conditional law μ_g; because P_s/Q_s is constant within g and all continuation likelihood ratios stay r_g, P(H|g)=Q(H|g)=μ_g. For an arbitrary FULL real behavioral policy, define d_j(H) as its conditional probability of stopping at j along this complete path; it is a product of the history-dependent earlier continuation hazards and current stop hazard. For every path ∑_j d_j(H)=1, including zero-reach and forced-stop cases. Let d_gj=E_{μ_g}d_j(H), an honest time distribution.

Construct the seedless LR schedule using this d_g. It preserves BOTH stopping-time observers T_P,T_Q exactly. Its two terminal error discrepancies are **precisely**
[
 e_P^{m FULL}-e_P^{m LR(d)}
   =sum_gP_gsum_joperatorname{Cov}_{mu_g}(d_j(H),p_j(H)),
]
[
 e_Q^{m FULL}-e_Q^{m LR(d)}
   =sum_gQ_gsum_joperatorname{Cov}_{mu_g}(d_j(H),q_j(H)).
]
Proof: expand E(d_j p_j)=E(d_j)E(p_j)+Cov(d_j,p_j) in each class. The same μ_g is valid for P and Q by frozen path likelihood ratios; positive BRC source/path masses and provenance remain separate until this explicit finite-horizon expectation. This is an exact four-observer, fixed-horizon projection certificate, **not** a claim that provenance may be erased for any future operation. A nonzero covariance shows only that the *specific time-flow-matched* LR policy differs, not by itself that the FULL point is outside the entire LR image.

## Strictly positive stochastic split/reconvergence example and exact separation

Three initial sources have:
| s | P_s | Q_s | r_s | P(Y=1|s)=Q(Y=1|s) |
|--|--:|--:|--:|--:|
| A | 1/8 | 1/4 | 1/2 | 3/4 |
| B | 1/8 | 1/4 | 1/2 | 1/4 |
| C | 3/4 | 1/2 | 3/2 | 1/2 |

Nature signal Y is generated after continuing at j=1. After continuing at j=2, a new binary Z has P(Z=1|Y=1)=Q=2/3 and P(Z=1|Y=0)=Q=1/3. All four nature-branch alternatives have positive probabilities. Thus at j=3 distinct sources and histories (s,Y) can reach the same latest (r_s,Z) observation, while FULL retains both coordinates. At j=1,2,3 stopping is optional; j=4 is forced stop.

For j=1,...,4 the baseline terminal Bernoulli rates are
|s|p_1,p_2,p_3,p_4|q_1,q_2,q_3,q_4|
|--|--|--|
|A|(1/5,3/10,1/5,1/2)|(1/5,1/5,3/10,2/5)|
|B|(1/4,7/20,1/4,11/20)|(1/4,1/4,7/20,9/20)|
|C|(1/4,1/4,1/2,1/3)|(1/4,1/2,1/4,2/3)|

Write a_s=P(Y=1|s), b_s=(1+a_s)/3=E(Z|s). For histories where the signal exists, replace the terminal kernels by the following explicit path-sensitive probabilities:
[
 p_2(s,Y)=p_{s2}+(Y-a_s)/4,quad q_2(s,Y)=q_{s2}+(Y-a_s)/8,
]
[
 p_3(s,Y,Z)=p_{s3},quad q_3(s,Y,Z)=q_{s3}+(Z-b_s)/8.
]
At j=1 and j=4 use the baseline rates. All specified P/Q Bernoulli rates are strictly in (0,1); under the conditional nature laws the added offsets have mean zero, so every LR deterministic observation vector equals the value obtained from the baseline rates. The 16 deterministic LR schedules choose one of four stopping times per class AB and C. Their minimum P error is
[
oxed{min_{m LR} e_P =39/160 .}
]
The four LR deterministic displacement columns (change AB from time1 to 2 or 3, and C from time1 to 2 or 3) are
[
 (1/40,0,1/4,1/2),quad (0,1/20,1/2,1),quad
 (0,1/8,3/4,1/2),quad (3/16,0,3/2,1);
]
their exact 4×4 determinant is **1/1280**. The LR image is a **full-dimensional four-dimensional convex polytope**, despite unrecoverable within-class path information.

Now take the legal FULL strategy: source A continues at time1, stops at time2 if Y=0 and at time3 if Y=1, and sources B,C stop immediately at time1. Its precise observer is
[
oxed{O^*=(617/2560, 323/1280, 39/32, 23/16).}
]
Since (min_{m LR}e_P=624/2560), all real LR policies satisfy (e_Pge39/160), yet (e_P(O^*)=617/2560). Therefore
[
oxed{Delta_{e_P}=7/2560>0,qquad
 operatorname{dist}_infty(O^*,mathcal O_{m LR})ge7/2560.}
]
This candidate has **unequal** convex hulls, so it is excluded from the mother target; it separately verifies that genuine stochastic splits and source/path-dependent terminal readouts need not confer equality.

The LR schedule matching the FULL policy's P/Q time flows has
[
 d_{AB}=(1/2,1/8,3/8,0),qquad d_C=(1,0,0,0),
]
and observer ((79/320,41/160,39/32,23/16)). The exact BRC covariance residual is therefore
[
oxed{(e_P^*-e_P^{LR},e_Q^*-e_Q^{LR})=(-3/512,-1/256).}
]
Note that matching time flows does not imply observer-safe compression here. Proof of the general theorem uses potential-path coupling and linear Q flow, not enumeration of behavioral probabilities.

## Evidence and verification boundary

The actually executed pure-BigInt rational `VERIFY.mjs` checks the normalized initial P/Q masses, all 12 positive potential nature leaves (3×2×2), 48 pairs of positive P/Q terminal rates, continuation likelihood-ratio constancy, sourcewise centered kernel averages, the 16 deterministic LR stop schedules, the explicit legal FULL witness, time-flow matching and two exact covariance residuals, plus determinant 1/1280. The saved `EXACT_OUTPUT.txt` contains that execution output. Finite checks establish this **specific rational instance**; the all-real, all-finite-tree theorems come from the flow and simplex proofs above. No Lean proof, prior-art priority claim, native X6 dynamics bridge, independent Driver review, or Source CLAIM/Result is asserted.

At this run the native service reported research_authority_granted=false, code-control verification pending and active-jobs quota 5/5. Exact active-owner inventory returned CONTROL_QUOTA; therefore author-side GitHub evidence is stored without impersonating a Source owner.

## Next mathematical discriminator

Seek a genuinely changing-key model with (exists h	o h') for which (L(h')
e L(h)), later distinct histories reconverge to the **same** (time,exact LR) key, and at least three LR decision keys influence the four-observer map. Retain strict positivity and actual absorbing outputs. First construct an exact rational *all-signed* hull certificate for every FULL deterministic vector (≤5 LR deterministic vertices per convex combination) or a rational Farkas separating functional. Only once that passes seek an all-real nonmembership witness, including every zero-reach and 0/1 behavioral boundary. See `NEXT_TASK.md`.
