# EC49R — Two-purchase cost-neutral action coding: exact obstruction and robust informative-sensor extension

Status: AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED (2026-10-29). This is an author-side portable positive-weighted-BRC observation result, **not** a service-issued CLAIM, Result, review, or P000 modification. Contributor: local research4 execution, no native identity implied.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 \`main@8c25fc7adfa02dd5733c2a3d0b368d99e4f46f51\`; Enterprise Math \`main@b362cfdb90eceb0ad5baf46a7b6b85c55ff6c16c\`; EC49Q PR #1657 immutable head \`34c70ec566efbb9a2551700aad6fc8d88abee583\`. P000 original blob \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\` equals startup projection's canonical blob. P000 and ACTIVE worldview are unchanged.

## Model and typed BRC audit

Let W=Z={0,1,2}. Under Q, each of the nine labeled (W,Z) leaves has mass 1/9. Under P, P(w,z)=1/6 for z=w and 1/12 otherwise. All 18 source-specific weights are strictly positive rationals and both source measures sum to 1; P_W(w)=Q_W(w)=1/3. Write Δ(w,z)=P(w,z)-Q(w,z), so Δ=1/18 on the diagonal and −1/36 otherwise. This difference is a comparison of *two positive BRC branch measures*, not a native signed/phase BRC amplitude.

Finite-horizon information structure: initially W is visible. The observer may accept, reject, or buy first sensor A or B. A costs 1, B costs 2, both initially output the same constant symbol \`*\`. Upon buying, W is erased, but the chosen action label is always retained. The compressed controller additionally stores D∈{0,1}, chosen causally while W is visible; the full controller retains W. After first purchase it may stop (accept/reject) or buy the second sensor S, costing 1 and revealing Z; after S it may accept/reject as a function of precisely its retained action, memory and observations. No S purchase is legal before the first purchase. The agent may stop after either stage. Fresh behavioral coins are source-independent and independent across information sets; the controller retains neither a shared random seed nor forgotten W through an undeclared private register.

Let O=(α,β,E_PT,E_QT), acceptance under P/Q and expected total sensor cost under P/Q. T is a resource bill, not heartbeat time. Define the linear functional
\[
H(O)=\alpha-\beta-\frac{E_PT+E_QT}{48}.
\]
Let S_full, S_2bitcode denote feasible raw four-vector regions with full-W recall and with two action labels times one-bit D respectively. (The subscript indicates the *four available action/memory codes*, not two actual external-memory bits.)

## Theorem 1: sharp all-real two-purchase separation

For **every** source-independent legal real behavioral policy with fresh independent randomization,
\[
\max_{O\in S_{\mathrm{full}}}H(O)=\frac1{12},
\qquad
\max_{O\in S_{\mathrm{2bitcode}}}H(O)=\frac5{72}.
\]
The sharp gap is \(1/72>0\), although K*m=2*2=4≥|W|=3.

Full witness: buy A for each W, then S, accept exactly when Z=W. This gives
\[
O_f=(1/2,1/3,2,2),\quad H(O_f)=1/12.
\]
Compressed witness: encode W=0 as (A,D=0), W=1 as (A,D=1), W=2 as (B,D=0). Buy S and accept Z=W using the decoded code. Its vector is
\[
O_c=(1/2,1/3,7/3,7/3),\quad H(O_c)=5/72.
\]
Consequently \(O_f\notin\operatorname{conv}(S_{\mathrm{2bitcode}})\).

**Proof of the all-real bound.** Each W marginal is source-neutral, so acceptance before S contributes zero to α−β. Buying a first sensor but not S incurs positive cost and no discrimination; for maximizing H that route can be discarded. For a deterministic compressed controller, each active W is assigned to exactly one code (a,d), a∈{A,B}, d∈{0,1}; other W are stopped free. An active code fiber G contains n∈{1,2,3} W values. Under that fiber, optimal post-S acceptance is precisely the set of Z for which \(\sum_{w\in G}\Delta(w,z)>0\), yielding
\[
L(G)=\sum_z\max\{0,\sum_{w\in G}\Delta(w,z)\}
=\frac{n(3-n)}{36}.
\]
Here L(G) equals 1/18 for n=1 or n=2 and zero for n=3. Under source-neutral W, buying a then S for all n fiber elements incurs expected cost n(c_a+1)/3 in *each* source. Its H contribution is
\[
V_{a,n}=\frac{n(3-n)}{36}-\frac{n(c_a+1)}{72}.
\]
In particular \(V_{A,1}=1/36\), \(V_{B,1}=1/72\), \(V_{A,2}=0\), \(V_{B,2}=-1/36\), and size-three fibers have negative value. Skipping S after paying the first cost gives \(-n c_a/72<0\), so no n≥2 fiber makes positive H. At most two A singleton code fibers exist; with only three W values at most one additional singleton can occupy a B code. Thus H≤2/36+1/72=5/72, attained by the displayed code.

For full recall each W can buy A+S and earn diagonal positive mass 1/18 at source-coupled cost 2/3 each, net \(1/18- (4/3)/48=1/36\); B+S earns less and premature stopping earns at most zero. Summing three W gives 1/12. Finally, for a finite acyclic behavioral controller, each local behavioral distribution enters each path probability at most once. The expectation H is multi-affine in these distributions, so maximizing over independent fresh coins has a deterministic optimizer (successively select simplex vertices). Therefore the deterministic fiber bound applies to **all real** legal behavioral probabilities; the finite enumeration is auxiliary. QED.

## Theorem 2: exact price floor on the maximal-discrimination face

On the face α−β=1/6 (the largest possible total branch discrimination), every compressed controller has
\[
 E_PT=E_QT\ge7/3,
\]
while the full controller realizes \(E_PT=E_QT=2\).

**Proof.** Each W row has positive Δ mass exactly 1/18, hence reaching the sum 1/6 forces purchase of S and correct Z=w classification with probability one for every W. A compressed code cell mixing two distinct W cannot perfectly classify the diagonal event for each W: for a group of size two its maximum is only 1/18 rather than 2/18. Consequently the code supports of all three W must be disjoint (also under real randomization); only two A codes exist, so at least one W must always use first action B. First-stage cost is at least (1+1+2)/3=4/3 per source, second-stage cost exactly 1, total 7/3. The witness attains this. QED.

## Theorem 3: strictly positive informative first sensor retains a certified gap

Replace A/B's constant output with the same binary first observation U, where, *conditionally on W and independently of Z under either source*,
\[
\Pr(U=1\mid W=w)=\tfrac12+\eta\sigma_w,\quad
\eta=\tfrac1{200},\quad(\sigma_0,\sigma_1,\sigma_2)=(1,0,-1).
\]
The second sensor still reveals Z. All 18 joint atoms (W,U,Z) in each source are strictly positive rationals. U now genuinely carries information about W, and the observer may adapt its second purchase and terminal choice to U. For this perturbed model:
\[
\sup_{S_{\mathrm{full},\eta}} H-
\sup_{S_{\mathrm{compressed},\eta}} H
\ \ge\ \frac{49}{7200}>0.
\]

**Proof.** Compare with the intermediate model η=0 where U is a fair coin independent of W,Z and of the source. For a fixed first-stage encoding, conditioning on U merely mixes two allowed post-first-stage controllers. Consequently the original deterministic-fiber argument still bounds \(\sup_{\mathrm{compressed},0}H=5/72\). The full witness above ignores U and still gives 1/12 for every η.

For either source, the full joint-measure total variation between η and 0 equals
\[
\operatorname{TV}(M_\eta,M_0)
=\eta\sum_w M_W(w)|\sigma_w|
=\frac{2\eta}{3}=\frac1{300}.
\]
For any fixed legal policy, data processing bounds the change in each acceptance expectation (range [0,1]) by TV and in each cost expectation (range [0,3]) by 3 TV, even when the continuation depends on U. Hence
\[
|H_\eta(\pi)-H_0(\pi)|
\le (2+6/48)\operatorname{TV}
=\frac{17}{2400}.
\]
This bound is uniform over all real compressed behavioral policies. Taking the supremum gives
\[
\sup_{\mathrm{compressed},\eta}H
\le\frac5{72}+\frac{17}{2400}=\frac{551}{7200},
\quad
\sup_{\mathrm{full},\eta}H\ge\frac1{12}=\frac{600}{7200},
\]
and the claimed gap is 49/7200. This is a **certified positive lower bound**, not an assertion of sharp perturbed optima. QED.

## Verification, significance and limits

Executed Python standard-library Fraction checker enumerated **125 initial compressed maps** (5 choices per W: stop, A0, A1, B0, B1), optimized each used code over all **8 terminal Z-acceptance masks** and the stop-after-first option, and inspected **27 full-controller first-stage maps**. It checked source positivity/normalization and both explicit four-vector witnesses; all assertions PASS. It also constructed all 18 rational positive atoms per source for the informative U variant and verified TV=1/300 and the 49/7200 certificate. See VERIFY.py and its actually emitted EXACT_REPORT.json. The all-real proof is the multi-affine reduction and inequalities above, not the finite exhaustive count alone.

This is a direct application of source-labeled positive-rational weighted BRC: the relevant carrier is the exact (source,W,U,Z,action,D) branch measure with two acceptance observers and two resource observers. Compressing to action-label count K*m discards resource compatibility and source-coupled conditional discrimination. The findings concern a finite *auxiliary probability observer*; no signed/phase BRC cancellation, native X6 coordinate computation, three-dimensional slice theorem, or physical heartbeat dynamics is claimed. The minimal necessary/sufficient stochastic padding criterion for general multi-stage protocols remains EC49S.
