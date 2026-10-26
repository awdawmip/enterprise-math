# R4-EC49 — Exact sign-profile memory sweep and sharp private-memory ceiling

**Scientific status:** Author-side mathematical proof with independent finite computational checks. This is not a native Enterprise Math CLAIM, frozen Result, independent Driver approval, Foundation admission or a native X6 heartbeat-dynamics theorem.

## Source and authority

The GLOBAL_KNOWLEDGE_V1 snapshot is awdawmip/chatgpt-global-knowledge main@9ae025b14147776280a94834aecb8dfb19d3ee41. Its canonical 00_BOOTSTRAP.md and OPERATING_MANUAL.md, Enterprise Math project/TASK bootstraps, P000 projection (canonical P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE 我眼中的世界.md, mathematical evidence policy, BRC rules and research registration contract were read from that single commit. Enterprise Math Source snapshot is main@e8992339dbbb511df56bf9a22f5095fd6ea1e123; its portable research protocol, exact weighted BRC substrate, project persistence policy and Chat research control protocol were read.

Scientific input: EC47 author-side threshold conflict theorem at 85a523ba6a887395c47d924fe037f772242f6a25; EC48 finite face-compatibility theorem at 82fab35f1a10cc86209881131c9788a321a0efeb. These are provenance, not assumptions of accepted mathematical authority: the central proofs here are supplied in full below.

GitHub actor was authenticated as awdawmip with repository admin/push access. Native active owner and task enumeration returned CONTROL_QUOTA; native session creation returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No other owner's formal task or claim was taken. REUSE_APPLIED: labelled positive rational BRC microbranch multiplicities and ordered (history, future-label) provenance. No signed amplitudes, physical heartbeat update, source cancellation, X6 native path dynamics or three-axis slice embedding is claimed. P000 has no fixed heartbeat update.

## Exact model

Fix nonempty finite history alphabet H and future-label alphabet Y, with r=|Y| and n=|H||Y|. Let p(h,y)>0 and q(h,y)>0 be rational joint distributions under two competing hypotheses, each totalling 1. By a common positive denominator M one may equivalently use integer microbranch counts P(h,y)=Mp(h,y), Q(h,y)=Mq(h,y), with both count totals M. The observed ordered pair (h,y) is retained as provenance.

A K-state hypothesis-blind private memory encoder π_h(m) first observes history h, then, after h has been forgotten, a decoder u_m(y)∈[0,1] sees y and chooses hypothesis P with that probability. All real stochastic kernels are allowed. The resulting detection probabilities are

α = Σ_{h,y,m} p(h,y) π_h(m) u_m(y),
β = Σ_{h,y,m} q(h,y) π_h(m) u_m(y).

Call their attainable set S_K. A full-history observer may choose an arbitrary w(h,y)∈[0,1] and has region Z=Σ_{h,y}[0,(p(h,y),q(h,y))], a compact planar zonotope. The four fixed-depth quantities are (e_P,e_Q,t_P,t_Q)=(1−α,β,2,2). The stage count 2 is not a native physical time or heartbeat interval. We distinguish equality of the convexified region conv(S_K)=Z from the generally stronger unconvexified equality S_K=Z.

## Theorem EC49.1 — Convex-hull memory is the number of generic sign profiles

Let R be the finite set of strictly positive rational ratios p(h,y)/q(h,y). For λ>0 with λ∉R define the binary sign profile

σ_λ(h) = (1_{p(h,y)>λ q(h,y)})_{y∈Y}.

Set D(λ)=#{σ_λ(h):h∈H}. Then the minimum K for conv(S_K)=Z is exactly

**K_conv = max_{λ>0, λ∉R} D(λ).**

For generic λ the EC47 threshold-conflict graph is a complete multipartite graph, whose independent-set parts are precisely equal-sign-profile classes; its chromatic number is D(λ).

**Proof.** Consider the linear support functional α−λβ. The unconstrained full-history support maximum is Σ_{h,y}max(p(h,y)−λq(h,y),0), attained only by w(h,y)=1 at strictly positive coefficient cells and w(h,y)=0 at strictly negative coefficient cells, with arbitrary values at zero coefficients. In a compressed observer w(h,y)=Σ_mπ_h(m)u_m(y) is a convex combination. Equality to the unrestricted support forces every memory m with π_h(m)>0 to output u_m(y)=1 at positive cells and u_m(y)=0 at negative cells. If two distinct histories differ in a generic profile bit, they have conflicting required output at that y; their positive-support memory sets are disjoint. At least one memory state is used by each history. Selecting one used memory per distinct profile proves K≥D(λ), **even when both encoder and decoder use arbitrary real randomization**. Conversely, encode each profile to a single distinct memory state and decode its bits deterministically, achieving the unrestricted support maximum.

For any tied threshold λ∈R, each strict conflict survives at every sufficiently close generic λ on either side. The strict conflict graph is therefore a subgraph of the nearby generic graph, and one such nearby generic optimal encoding achieves the tied-threshold optimum because tie cells have coefficient zero. Thus the generic profile bound covers all positive λ including ties. All same-sign support directions are attained by the always-P or never-P decoder. The other class of opposite-sign directions, −α+λβ, is covered by complementing terminal decisions, which sends (α,β) to (1−α,1−β). Hence equality of support functions in every direction is equivalent to K≥max D(λ). Since the convex hull of the compact S_K and Z are compact convex sets, equality of their support functions yields conv(S_K)=Z, and missing any generic optimum yields strict inequality. The complete multipartite claim follows immediately: two histories have a graph edge iff their generic profiles differ. QED.

**Scope warning:** Convex-hull equality is not asserted to imply S_K=Z. EC48's neutral exposed-face compatibility intervals remain necessary for that stronger claim.

## Theorem EC49.2 — Exact near-linear event sweep

Sort the at most n distinct ratios P(h,y)/Q(h,y) by exact rational comparison, grouping all equal thresholds. At any λ immediately above zero, all sign bits are positive. As λ passes a grouped ratio event, switch **simultaneously** all corresponding bits from positive to negative. Count the number of distinct history profiles in each open chamber before, between, and after events. The largest count equals K_conv.

The algorithm uses O(n log n) exact rational comparisons for sorting and O(n) amortized profile-frequency updates and O(n) event storage, with integer bitsets of width r. The bit complexity of arbitrary-precision rational comparisons, bitsets and dictionary operations is not claimed constant, and this does not give a polynomial algorithm for the stronger EC48 unconvexified compatibility-face test.

**Proof.** Each cell's strict sign is constant on every open interval between sorted ratios; crossing its unique ratio changes that bit exactly once. Grouped updates preserve the simultaneous threshold semantics and reconstruct exactly all successive generic profiles. Induction over the ordered event values shows that the maintained frequency map equals the true multiset of profiles in every chamber. Theorem EC49.1 converts the maximal distinct-profile count to K_conv. There are n source cells to process, at most n distinct events and at most n sorting keys, proving the stated arithmetic-operation bounds. A partial update of a tied group could invent a chamber that no real λ realizes and is therefore expressly excluded. QED.

An equivalent implementation may encode the **negative** bits rather than the positive bits: complementing all bits is a bijection on profiles and leaves each chamber's distinct count unchanged. The attached Python exact checker uses this equivalent increasing-negative-bit representation.

## Theorem EC49.3 — Universal exact memory ceiling and sharpness

For all finite positive-rational experiments with r future-label symbols,

**K_full ≤ min(|H|,2^r),** where K_full is the least K giving the **actual** equality S_K=Z.

The universal bound 2^r is sharp for every integer r≥1; there is a strictly positive integer-count family with |H|=2^r for which K_conv=K_full=2^r.

**Upper-bound proof.** A memory with |H| states can store h itself. For the alternative 2^r bound, let the memory alphabet be all binary words m=(m_y)_{y∈Y}. Choose *any* full-history stochastic response w(h,y)∈[0,1]. Encode h by the private stochastic distribution

π_h(m)=∏_{y∈Y} [w(h,y) when m_y=1, and 1−w(h,y) when m_y=0],

and set the terminal decoder u_m(y)=m_y. This distribution is normalized, depends only on the observed h and no unknown hypothesis, and has marginal Pr(m_y=1 | h)=w(h,y) for every y. Consequently Σ_mπ_h(m)u_m(y)=w(h,y) pointwise. The same full-history policy, hence its complete (α,β) pair, is exactly reproduced by 2^r private memory states. Neither a persistent ex-ante public random seed nor an external observer of h is used after encoding. Therefore S_(2^r)=Z, proving the ceiling.

**Sharpness proof.** Let H={0,1}^r and Y={1,…,r}. For a binary history word b and label j define

P(b,j) = 2 if b_j=1, otherwise 1;
Q(b,j) = 1 if b_j=1, otherwise 2.

All microbranch counts are positive integers, and each total is M=3r·2^(r−1). At λ=1, the coefficient P(b,j)−Q(b,j) has positive sign exactly when b_j=1 and negative sign otherwise. Every one of the 2^r histories has a **distinct** r-bit sign profile. Theorem EC49.1 gives K_conv≥2^r; the universal upper bound gives K_full≤2^r, while always K_full≥K_conv. Hence **K_conv=K_full=2^r for all r≥1**. This is a proof over an arbitrary integer parameter, not finite extrapolation. QED.

The upper bound was foreshadowed by EC46-style decision-plan encodings; the sharp worst-case equality and efficient sign-profile scan are the present new contributions.

## Strictly positive nonmonotone chamber witness

Use H with three histories, Y with two labels, both hypothesis totals M=42:

P = [[3,12],[12,3],[6,6]],
Q = [[7,7],[7,7],[7,7]].

All 12 source counts are positive. The sorted distinct event ratios are 3/7, 6/7 and 12/7. The distinct-profile counts in the four open chambers are **1,3,3,1**; therefore K_conv=3. Checking only λ≈0 and λ→∞, or presuming monotonic profile count, would incorrectly predict K_conv=1.

## Reproducible exact evidence and limitations

The accompanying EC49_scan.py uses only Python arbitrary-precision integers and fractions.Fraction. It executes grouped-ratio event sweeps on 375 seeded positive-integer models, compares **2,372** open-chamber profile counts against independently recomputed exact signs, and for |H|≤4 independently enumerates graph colorings for **1,669** checks. It also checks the 3×2 peaked witness and r=1,…,8 sharpness instances. The generated EC49_REPORT.json records all_checks=PASS. This verifies the implemented finite checks and examples, **not** the universal theorems, which rest on the proofs above.

Unperformed and not inferred: native EM CLAIM/session/Result/Guard, independent Driver review, Lean formal proof, empirically verified discrete physics, native X6 update, selected three-dimensional slice, third-coordinate semantics or calibrated time dynamics.

**Precise next unit EC50.** Decide whether K_conv from the sweep always suffices for S_K=Z at fixed two-stage binary terminal decision. Either prove that EC48's compatibility interval gaps are impossible under this profile ceiling, or exhibit the smallest strictly-positive integer-count example with conv(S_K)=Z but S_K≠Z. After settling that question, separately extend to stop/continue and variable-depth (e_P,e_Q,t_P,t_Q) observers; any native X6 transfer would additionally require a verified state-update and observer bridge.
