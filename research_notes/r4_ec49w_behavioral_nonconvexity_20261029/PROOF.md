# EC49W — exact always-S cost face; strict behavioral/convex-hull separation

**Scientific status (2026-10-29):** author-proved analytical nonattainment, exact Fraction finite calculation, UNREVIEWED / NOT_ADMITTED. The parent is EC49V [Draft PR #1670](https://github.com/awdawmip/enterprise-math/pull/1670), immutable scientific commit 1b6afb0b3d015c383812de56378e834ea8742006. This author-side continuation is not a native CLAIM, Result, or independently accepted theorem.

## Model, frozen input and scope

Preserve the EC49U/V positive-weight auxiliary BRC observer. Let w,z∈{0,1,2}, u∈{0,1}, sigma=(1,0,-1), eta=1/200. Source laws are Q(w,z)=1/9 and P(w,z)=1/6 for z=w, 1/12 otherwise. Let t_w(u)=1/2+(2u-1)eta sigma_w. All 18 source leaves R(w,u,z)=R(w,z)t_w(u) are strictly positive, and the readout difference is

\[
\Delta_w(u,z)=t_w(u)(3{\bf1}_{w=z}-1)/36.
\]

The controller knows W while choosing STOP or buying A/B (stage-1 cost 1/2) and writing D∈{0,1}. After W is erased it recalls (A/B,D), observes U, can purchase S (stage-2 cost 1) to see Z, and then accepts or rejects using only its retained information. All behavioral randomness is independent, fresh, source-blind, and not preserved as a shared seed. Define alpha=P(accept), beta=Q(accept), delta=alpha-beta and expected source-equal costs C1,C2. P(W,U)=Q(W,U), so no decision before observing Z can increase delta.

Study eta=1/200 and fixed C1=43/48, C2=7/8. EC49V established, for arbitrary real behavior probabilities,

\[
J=\delta-(C_1-C_2)/6\le1/9,\qquad \delta\le11/96.
\]

EC49V also supplied a shared-seed convex-hull witness for the upper endpoint and an ordinary behavioral witness with delta=59/576. We distinguish these feasibility notions below.

## Theorem A — always-buy-S exact optimum

Within the subclass that buys S after every A/B purchase, despite arbitrary real randomness in the first decision and terminal accept/reject,

\[
\boxed{\max_{\mathrm{always\ S};\ C_1=43/48,C_2=7/8}\delta=59/576.}
\]

Attaining independent-coin rational policy: W0→A0, W1→A1, W2→STOP (3/8) or A0 (9/16) or B0 (1/16). Always buy S. Terminal A0 accepts Z∈{0,2}; A1 accepts Z=1; B0 accepts Z=2. Source probabilities and costs are exactly

\[
(\alpha,\beta,C_1,C_2)=(109/192,67/144,43/48,7/8).
\]

**All-real reduction to exactly 144 vertices.** For w and retained code c∈{A0,A1,B0,B1}, let p_wc be first-stage probability and s_w be STOP probability. Always S implies

\[
\sum_w s_w=3/8,\quad \sum_w(p_{w,B0}+p_{w,B1})=1/16,\quad s_w+\sum_c p_{wc}=1.
\]

Let b_w=p_{w,B0}+p_{w,B1}. As total Σ_w(s_w+b_w)=7/16<1, every row capacity is automatically slack, and (s_w),(b_w) range over independent nonnegative simplexes of total masses 3/8 and 1/16. On a fixed source-blind prefix, optimal terminal acceptance is by positive signs:

\[
\delta(p)=\sum_{c,u,z}\left[\sum_w p_{wc}\Delta_w(u,z)\right]_+.
\]

This is convex and piecewise linear in p. Holding s,b fixed, replace each A and B tag split by a pure tag without decreasing the maximum, using convexity. Holding these pure tags fixed, p is affine in (s,b); convexity moves each simplex to a vertex. Therefore it suffices to evaluate 3 STOP indices × 3 B indices × 2³ A labels × 2 B labels = 144 vertices. The attached standard-library exact-Fraction checker evaluates all 144 and, independently, the eight terminal masks in each code/U cell. Its maximum is 59/576, with 48 labeled maximizing vertices. Combined with the proved convex extreme-point reduction and rational witness, this is a complete proof for the stated all-real subclass (not an extrapolation from samples).

## Theorem B — the EC49V convex-hull endpoint is behaviorally impossible

In the **full** protocol, even permitting arbitrary real, adaptive post-U decisions not to buy S, the point

\[
(C_1,C_2,\delta)=(43/48,7/8,11/96)
\]

does **not** belong to the unseeded behavioral image. Hence the cost-constrained maximum δ* is attained and

\[
\boxed{59/576\le\delta^*_{\rm behavioral}<11/96}.
\]

The exact δ* and full achievable (alpha,beta) section remain OPEN.

**Proof of strict nonattainment.** For the objective J, buying S after a paid action and U strictly improves the attainable value: without S, the P-Q acceptance advantage is zero; buying S adds a nonnegative optimal advantage and strictly increases the favorable +C2/6 term. Thus every deterministic J-maximizer buys S on all reached purchased paths.

For a deterministic prefix code fiber F⊆{0,1,2}, its best post-S discrimination is B(F)=Σ_{u,z}[Σ_{w∈F}Δ_w(u,z)]_+. Exact source signs at eta=1/200 yield B(F)=1/18 when |F|=1 or 2, and B({0,1,2})=eta/6=1/1200. An A fiber contributes B(F) to J, a B fiber contributes B(F)-|F|/18, and STOP contributes zero. There are only two A codes. Therefore J≤1/9, with equality **only if both A codes are nonempty fibers of size at most two, and any B fiber is a singleton**. In a deterministic maximizing prefix STOP and B cannot occur simultaneously: only three W histories exist, leaving at most one for the two required A codes. The 125 possible pure prefixes and all equality cases are independently checked exactly by VERIFY.py.

A behavioral policy with independent fresh coins is the expectation over **product-supported deterministic complete plans**, obtained by independently sampling one action for each information set. Because every deterministic plan has J≤1/9, equality for a behavioral policy would force **every positively supported complete plan** to maximize J. Under the fixed costs and all-S necessity, Σ_w Pr(STOP|w)=3/8>0 and Σ_w Pr(B|w)=1/16>0. If STOP were positively possible at history i and B at a different history j, the independent product support would include a deterministic prefix with both STOP_i and B_j, impossible at J equality. Hence both STOP and B choices are confined to one history w*.

The other two histories can choose only A codes, which must be *different fixed tags* for every supported pure plan; otherwise w* choosing STOP would leave fewer than two occupied A codes. History w* has remaining A probability 1-3/8-1/16=9/16>0 and must merge with one of those two histories w′ when it chooses A. Compare two supported prefix decisions with the **same** retained code: in the first, w* chooses STOP and the code's only history is w′; in the second, w* chooses A into that code and the fiber is {w*,w′}. At observation z=w*, the former has strictly negative signed coefficient -t_{w′}(u)/36 and its unique optimal terminal rule must reject. The latter has strictly positive coefficient (2t_{w*}(u)-t_{w′}(u))/36 for both u at eta=1/200, so its unique optimal rule must accept. The terminal rule at the same (code,u,z) cannot independently coordinate with the erased prefix coin. Contradiction.

The full behavioral policy parameter cube is compact; the fixed-cost feasible section is closed and nonempty. Its continuous δ attains a maximum. Since the global EC49V bound 11/96 is unattainable, its inequality is strict. Theorem A supplies the lower endpoint. This is a **nonconvexity witness in the (C1,C2,delta) projection**, not merely a failure of an unproven convexity conjecture.

For comparison, an **ex-ante shared** lottery on deterministic all-S prefixes (STOP,A0,A1), (A0,A0,A1), (A0,A1,B0) with probabilities 3/8, 9/16, 1/16 gives exactly (43/48,7/8,11/96), as the checker verifies. That joint lottery is allowed in the convex hull but **not** in the specified memory-erasing independent-coin behavioral protocol.

## Evidence, boundaries and provenance

Execute VERIFY.py using Python standard-library fractions.Fraction. It checks 18 positive normalized source leaves per source; 144 complete extremal first-stage rows and 8 local masks per code/U; the attained P,Q acceptance witness; 125 pure J prefix cases and exact equalities; and the shared-seed convexified point. EXACT_REPORT.json is its generated output. Theorem A uses a valid convex reduction; Theorem B uses an analytic all-real product-support obstruction and compactness. Neither conclusion is a native theorem about signed/phase BRC amplitudes, Enterprise X6, a three-dimensional native slice, or physical heartbeat time; transfer requires a typed embedding, readout and relation preservation.

Frozen global knowledge: awdawmip/chatgpt-global-knowledge main@f7ab5d4dc91d41a028048a691a3b40b111ffdf48. Project main: awdawmip/enterprise-math main@3d715614576c0687380028e764a179eeaa346fc8. Read canonical bootstrap/manual, P000 startup plus original (canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched), ACTIVE worldview, actual portable protocol and current source. P000 and worldview are unchanged. Owner-list lookup returned CONTROL_QUOTA and native context manifest authority_granted=false; this research is authorship-side, UNREVIEWED / NOT_ADMITTED.
