# EC48Z — Reachability-relative quotient kernels and exact finite-memory LP

Date: 2026-10-28 Asia/Shanghai. Author-side continuation of EC48Y Draft PR #1609, commit 60b1e18231fb996bc49accdee0118b0ac190eba9. Local contribution tag R4-EC48Z-20261028-0931-LOCAL, not a service-issued identity. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASS / UNREVIEWED / NOT_ADMITTED.

## Model, information scope and type

This work extends the auxiliary finite, strictly positive rational dual-source P/Q *stopping observation* model from EC48Y, not native signed-amplitude BRC, native X6 heartbeat evolution or a physical claim. At each decision time t a fine history h includes previous actions and sensor history. Source-neutral behavioral controller chooses acc (stop/accept), rej (stop/reject), or cont (continue, unavailable at the terminal time). Q(h)>0 is the pre-action live mass and L(h)=P(h)/Q(h)>0 is the exact full fine-history pre-action joint likelihood ratio. A fixed deterministic, source-neutral causal register updater maps each allowed observation/action to one of m register states. The compressed readout y=q_t(h,r) includes time, current sensor, register state and the full fine-history L(h); it cannot otherwise consult erased history. All cells in the same y have the same action set. Time is a separately typed finite stop-stage counter. No hidden persistent random seed is allowed.

Write x_t^π(h,r) for Q fine live mass under one common source-neutral behavioral policy π, and x_t^π(y) for its sum over fine states in fiber y. L_y is constant on the fiber because full LR is in the readout. Let K_Q(y'|h,r,cont) be the Q next-readout distribution with the specified updater.

## Theorem Z1 — reachable-kernel invariance suffices for *raw* region linearization

Assume for every nonterminal readout y which is reachable with positive Q mass there exists a *single rational* probability vector \bar K_Q(·|y,cont), such that for EVERY permitted behavioral π and successor y':

\[
\sum_{(h,r):q_t(h,r)=y}x_t^\pi(h,r)K_Q(y'|h,r,\mathrm{cont})
 = x_t^\pi(y)\bar K_Q(y'|y,\mathrm{cont}). \tag{R}
\]

The zero-mass case is vacuous. This condition compares kernels only after weighting them by **reachable** fine occupancies; it does not demand equality for individual h in the same fiber.

Then the exact original, potentially nonconvex-a-priori, four-observation region S_m for (α,β,E_PT,E_QT) equals the projection of the finite *rational linear occupancy polytope*:

\[
x_1(y)=Q(Y_1=y),\quad z_t(y,a)\ge 0,\quad\sum_a z_t(y,a)=x_t(y);
\]
\[
x_{t+1}(y')=\sum_y z_t(y,\mathrm{cont})\bar K_Q(y'|y,\mathrm{cont});
\]
\[
\alpha=\sum_{t,y} L_yz_t(y,\mathrm{acc}),\quad
\beta=\sum_{t,y}z_t(y,\mathrm{acc});
\]
\[
E_PT=\sum_{t,y} L_yx_t(y),\quad E_QT=\sum_{t,y}x_t(y).\tag{LP}
\]

Use only original reachable y, not invented successor states. Consequently S_m is convex, polyhedral and rational. Every rational target O∈S_m admits a rational source-neutral behavioral policy; every infeasible rational target admits a rational LP dual/separation certificate. These conclusions are restricted to fixed updater, full LR oracle, finite horizon, observed four coordinates and the declared control actions.

**Forward proof.** On each readout fiber, source neutrality implies Q action mass z_t(y,a)=x_t^π(y)π_t(a|y). Since π_t(cont|y) is the same for every fine state in the fiber, summing the fine Q flow and using (R) gives the LP transition. Full fine-history LR is unchanged by the source-neutral action factors and updater. Thus the P mass on the fiber is L_y times Q mass, for both live and action occupation. Summing accepting masses gives α,β; the finite integer-valued stopping-time tail identity E_sT=Σ_t Pr_s(T≥t) gives the two expected times. All four coordinates are reproduced exactly.

**Reverse proof.** For any LP solution (x,z), on x_t(y)>0 set π_t(a|y)=z_t(y,a)/x_t(y); on zero-live fibers choose any legal action distribution. This uses only allowed readouts. Starting with the same Q initial quotient law, assume the constructed controller realizes x_t(y). It induces z_t(y,a) because it applies the common π on every fine state in the fiber. Apply (R) to this actual controller: its next quotient Q occupancy is exactly the specified LP x_{t+1}. Induction proves all quotient Q occupations. Full fine LR gives the P masses and all four LP outputs. This is a **single behavioral-policy construction** and does not invoke convexifying mixtures of arbitrary policies. The rational polytope with rational target O has a rational feasible solution (e.g. a rational vertex); dividing rational z/x yields rational action probabilities wherever live. Standard rational Farkas/linear separation supplies an exact infeasibility certificate. QED.

## Theorem Z2 — finite deterministic-policy test

Let D be all deterministic assignments of one legal action to each time-labelled readout under the same fixed updater. It is finite. Compute exact Q fine live occupancy x_t^δ for every δ∈D. Condition (R) is equivalent to requiring the same rational \bar K_Q to satisfy (R) on every such x_t^δ (zero-reach fibers omitted).

Proof: necessity is immediate. For a behavioral π, imagine preselecting independently an action at each distinct time-labelled readout according to π there. This defines a distribution over deterministic maps δ of weight ∏_y π(δ(y)|y). Each physical trajectory visits each time-labelled y at most once. Summing all unused deterministic choices shows the trajectory and thus its fine live occupancy under π equals the mixture of the corresponding deterministic occupancies. Both sides of (R) are linear in occupancy, so deterministic equalities extend to all behavioral π. A positive-reachable deterministic policy yields the candidate rational \bar K by a ratio of rational masses. Hence (R) is decidable via finite exact arithmetic, although its naive enumeration can be exponential. QED.

EC48Y Y2's *pointwise controlled-Markov* condition K_Q(y'|h,cont)=\bar K_Q(y'|y,cont) for each h implies (R). The strict converse fails, as the following complete example shows. Thus Z1 provides an exactly LP-reducible class properly larger than EC48Y's pointwise class. It is related to **weak lumpability** for restricted initial mixtures and control policies; the broad idea predates this project.

## Strict-positive 12-leaf, 3-decision-time example

A historical sensor H∈{0,1} is observed and then erased by a fixed one-state register *before* any decision. Initially P(H)=Q(H)=1/2; the t1 sensor is constant and L=1. Upon continuing, the t2 sensor Z∈{A,B,C} has the following strictly positive Q transition probabilities:

| H | Q(A|H) | Q(B|H) | Q(C|H) |
|---|---:|---:|---:|
| 0 | 1/4 | 1/2 | 1/4 |
| 1 | 1/8 | 3/4 | 1/8 |

Set L_A=1/2, L_B=1, L_C=3/2 and P(Z=z|H)=L_z Q(Z=z|H). Each P conditional row sums to 1, because Q(A|H)=Q(C|H). At t2 the controller observes Z and the full L_z, still not H. On further continuation it observes W∈{0,1} at t3, with P(W=1|H=0,Z)=Q(W=1|H=0,Z)=1/4 and P(W=1|H=1,Z)=Q(W=1|H=1,Z)=3/4. At t3 readout (W,full L_z) distinguishes Z via its distinct likelihood ratios but not H. All terminal leaves have P(h,z,w)=L_zQ(h,z,w)>0 and Q(h,z,w)=(1/2)Q(z|h)Q(w|h,z)>0, with totals 1 for each source.

The exact quotient data are:

\[
Q(Z)=(3/16,5/8,3/16),\qquad
P(Z)=(3/32,5/8,9/32);
\quad
\bar K_Q(W=1|Z)=(5/12,11/20,5/12).
\]

Why (R) holds: for *every* policy, first continuation probability c1 is identical for both H. Hence its t2 live masses are x_2(h,z)=c1(1/2)Q(z|h), so Q(H|Z,live) is a fixed Bayes mixture independent of policy. At t2 the continuation probability c2(z) is also identical for H in each Z fiber and cannot change that hidden mixture. Therefore the Q quotient kernel to W is the same displayed \bar K under every policy. This verifies (R) algebraically across all real behavioral probabilities.

Yet pointwise controlled-Markov fails at **both** transitions: at t1, Q(Z=A|H=0)=1/4 differs from Q(Z=A|H=1)=1/8. At t2, Q(W=1|H=0,Z)=1/4 differs from Q(W=1|H=1,Z)=3/4. The model is genuinely nonlumpable by EC48Y Y2's finer condition and source-informative already at Z (L_A≠L_C).

For a concrete rational strategy choose (acc,rej,cont)=(1/8,1/4,5/8) at t1; at t2 for Z=A,B,C respectively (1/4,1/4,1/2), (1/8,3/8,1/2), (1/2,1/4,1/4); at t3 accept with probabilities (1/3,2/3,1/4,3/4,2/5,4/5) for (A0,A1,B0,B1,C0,C1). Direct fine-leaf summation and quotient LP both yield the **raw four-vector**

\[
O=(1283/3072,\;1255/3072,\;1939/1024,\;977/512).
\]

The two source expected times differ, so the four-coordinate timing conditions are nontrivial.

## Upstream correction found during continuation

EC48Y PROOF.md, Theorem Y1 consequence paragraph, prints “raw S_full subset S_m”. This direction is reversed: every m-register policy is simulable by a full-history policy, hence **S_m⊆S_full**. The corrected direction does not change Y1's necessary/sufficient rank-one occupancy result nor the separate Z1 LP theorem. This is an author-side source erratum, not an independent Driver review and does not overwrite the immutable EC48Y artifact.

## Executed exact verification and boundaries

The accompanying Python stdlib Fraction verifier passed strict positivity, P/Q normalization, every fine-history full LR identity, the two non-Markov transition differences, all rational aggregate kernels, and 5,184 **exhaustive deterministic one-register** policies (3×3³×2⁶). Every such policy's four fine-source outputs and quotient outputs agree exactly. It also checked 1,000 reproducibly seeded rational randomized behavioral policies: **6,184 exact policy evaluations** total. See VERIFY.py and its actual stdout EXACT_REPORT.json. Z1/Z2 are general algebraic proofs, not numerical extrapolations from the sample. No general quantifier elimination or native signed-BRC/X6 code was executed.

This quotient preserves only the declared finite-horizon action/readout language and four outcome coordinates. It need not preserve H-joint signal laws, later added information channels, signed/phase cancellations, or native six-dimensional Heartbeat World operations. Such stronger claims require a separate future-operation/fiber certificate and native-state/readout relation bridge. Original P000 and ACTIVE worldview remain unmodified.

Prior art provenance: Buchholz (1994) DOI 10.2307/3215235, Ledoux (1997) DOI 10.2307/3215001 on lumpability/weak lumpability; Altman (1994) DOI 10.1287/moor.19.1.169 and Wei & Chen arXiv:1408.5497 on occupation-measure/LP methods. These are contextual sources, not direct proofs of Z1's precise assumptions.
