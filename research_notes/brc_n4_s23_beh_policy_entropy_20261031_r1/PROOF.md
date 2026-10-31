# BRC N=4 / stopping-time-only: exact behavioral policy-label quantization and six-dimensional entropy obstruction

Date: 2026-10-31. Portable mathematical author proof with exact integer checker. Status: UNREVIEWED / NOT_ADMITTED; not a native P000 Cell dynamics theorem and not an S2 result.

## Frozen experiment

Use the predecessor BRC N=4 external *positive-mass* P/Q matrix. Latent cells are (AU0, AU1, AV, BU0, BU1, BV) and the six prepared rows are

\[
M=\frac1{20}\begin{pmatrix}
10&10&0&0&0&0\\
9&11&0&0&0&0\\
0&0&20&0&0&0\\
0&0&0&10&10&0\\
0&0&0&2&18&0\\
0&0&0&0&0&20
\end{pmatrix}.
\]

S23's actual third-stage grammar permits six distinct latent-cell stopping decisions. Continue deterministically in stages one and two; on latent cell x, independently stop at T=3 with probability u_x∈[0,1], otherwise stop at T=4. These are all lawful *behavioral randomized* S23 policies, with

\[
P_i^u(T=3)=(Mu)_i,\qquad P_i^u(T=4)=1-(Mu)_i. \tag{1}
\]

The earlier paper's *fixed category* quantifiers are essential: a common six-latent-cell-to-k-state stochastic encoder E is chosen before the policy; m fixed label-decoding kernels D_l are selected in advance. After a policy H is specified a deterministic label l(H) may be chosen based on that policy alone. The decoder does NOT additionally observe the actual latent cell, stopping coin, full policy, outcome, or a continuously-valued side channel. A stochastic mixture of policy labels as an extra analog messaging mechanism is outside this fixed-category definition.

For a policy family F the minimax TV risk is

\[
R_{k,m}(F)=\inf_{E,D_1,\dots,D_m}\sup_{H\in F}\min_{l\le m}
\max_{1\le i\le6}{\rm TV}(P_i^H,(MED_l)_i). \tag{2}
\]

The six fixed rows and common encoder respect the source information structure; the observed alphabet is T∈{1,2,3,4}.

## Theorem A — exact four-group operational cube

Let F4 be the legal subclass of (1) in which the AU0 and AU1 third-stage stop probabilities are a shared parameter theta_AU, BU0 and BU1 share theta_BU, and AV/BV have independent parameters theta_AV, theta_BV. Four parameters theta∈[0,1]^4 are free and the resulting six input rows have time-three probabilities exactly theta_(group of row).

For all positive integers m and all k≥4,

\[
\boxed{R_{k,m}(F4)=\frac{1}{2\lfloor m^{1/4}\rfloor}.}\tag{3}
\]

For k=1 the same restricted family has R_(1,m)(F4)=1/2 for every m.

**Lower proof (all k).** For each fixed decoder label, select the reconstructed probability of event T=3 on one prepared row in each of AU, AV, BU and BV. This gives a point c_l∈[0,1]^4 independent of theta. For that label, total variation on the binary event {T=3} is at least ||theta-c_l||_infinity. Thus m labels must cover the unit four-cube by m L-infinity balls of radius r.

Let n=floor(m^(1/4)), so n^4≤m<(n+1)^4. Take the (n+1)^4 grid points whose coordinates belong to {0,1/n,...,1}. Any two distinct points have L-infinity separation at least 1/n. If r<1/(2n), a single radius-r ball contains at most one grid point, and m<(n+1)^4 balls cannot cover the cube. Hence r≥1/(2n), regardless of stochastic encoding.

**Upper construction (k≥4).** Encode the four AU/AV/BU/BV provenance groups exactly using four states. Use n^4 labels whose centers are the product of n interval midpoints (a+1/2)/n. Choose the nearest center to theta and let decoder l output Bernoulli(c_(l,j)) on times 3 and 4 for encoded group j. TV on every prepared row equals |theta_j-c_(l,j)|≤1/(2n). This proves equality.

**k=1.** A single encoded state produces the same decoded law for every prepared row at a fixed label. The lawful theta=(0,1,0,1) requires both point masses at T=3 and T=4 across the groups; no common law is closer than 1/2 in maximum TV. Outputting the uniform law on those times attains 1/2.

In particular, for k≥4 and m=64, the exact F4 risk is 1/4, NOT zero. This does not conflict with the predecessor's zero-error result on the finite set of 64 **deterministic** source signatures.

## Theorem B — genuine six-parameter policy entropy

Let F6 consist of the entire legal six-coin subclass (1). For **all** k,m≥1,

\[
\boxed{R_{k,m}(F6)\ge\frac{1}{2(50m)^{1/6}}.}\tag{4}
\]

For k≥6, also

\[
\boxed{R_{k,m}(F6)\le\frac{1}{2\lfloor m^{1/6}\rfloor}.}\tag{5}
\]

Thus the exact asymptotic exponent for this six-parameter behavioral subclass with k≥6 is m^(-1/6), up to the displayed explicit constants.

**Lower proof.** The two-dimensional *auxiliary matrix* blocks AU and BU have determinants 1/20 and 2/5; AV/BV are identity blocks. Therefore det M=1/50. The image parallelepiped P=M[0,1]^6⊂R^6 has ordinary auxiliary parameter-space volume 1/50. This is an external measure used for a mathematical covering proof; it does not assert any native P000 plane or transform the X6 axes.

For a fixed encoder and each fixed label l, let c_l∈[0,1]^6 be the six probabilities assigned to T=3 by the reconstructed prepared rows (MED_l)_i. If TV error is at most r under some label, then the event {T=3} forces ||Mu-c_l||_infinity≤r. Covering all u∈[0,1]^6 therefore requires

\[
P\subseteq\bigcup_{l=1}^m(c_l+[-r,r]^6).
\]

Each cube on the right has volume (2r)^6; by finite subadditivity, 1/50≤m(2r)^6. This proves (4) even after allowing arbitrary independent output-row centers, a relaxation of any finite-state encoder.

**Upper construction.** With k=6 keep each latent source cell exactly. Let n=floor(m^(1/6)), quantize each of six policy coin probabilities u_x to the nearest of n interval midpoints using n^6≤m labels. At cell x the label decoder emits time 3 with probability uhat_x, time 4 otherwise. Every prepared row is a convex combination M_i of the six cells, so

\[
{\rm TV}(P_i^u,P_i^{\hat u})=|(M(u-\hat u))_i|
\le\sum_x M_{ix}|u_x-\hat u_x|\le\frac1{2n}.
\]

This gives (5); extra k states and labels remain unused.

**Policy information corollary.** For any target worst-case TV accuracy r on the *full* randomized S23 family, the fixed policy-label count must satisfy

\[
\boxed{m\ge1/[50(2r)^6].}\tag{6}
\]

Thus **no finite number of deterministic policy-category labels yields exactly zero error for all lawful behavioral S23 policies, regardless of source encoding capacity**. This cleanly separates the earlier finite deterministic 64-signature zero-error claim from the continuous behavioral model.

## Universal full-S23 lower bound and limits

Because F4⊆F6⊆S23_behavioral,

\[
\boxed{R_{k,m}^{S23,beh}(T)\ge
\max\left\{\frac1{2\lfloor m^{1/4}\rfloor},
\frac1{2(50m)^{1/6}}\right\}}\quad\text{for every }k,m\ge1.\tag{7}
\]

The separate author-side S64 deterministic-signature certificate gives an additional 1/2 lower bound when m≤63, but (7) does not rely on that certificate.

**The open ten-tag problem is not solved here.** For m=10 this proof still gives only 1/2 as a lower bound; the predecessor's lawful heavy-time strategy gives a 2/3 upper bound for k≥4. This new result instead fixes the full operational-label rate for a four-control behavioral subclass, and proves an intrinsic rank-six asymptotic information burden for continuous operations even with unbounded original storage.

## Actual computation and remaining obligations

The saved VERIFY.js was executed with JavaScript exact integer arithmetic. It checks both products of M with the explicit inverse, det M=1/50, 3,750 four-group prepared-row identities, 4,374 six-cell conditional law rows, and 9,668 exact four-cube grid-point evaluations for n=1,2,3,4. Exact output is in RUN_EVIDENCE.txt. Finite checks audit the frozen algebra and constructive examples; arbitrary-real universal claims follow from the analytic packing, volume and convexity arguments, not finite extrapolation.

NEXT_TASK.md retains the sharp full behavioral m=10 question, decoder freedom, S2 causality and native X6/time observer-update bridge. No P000 worldview amendment, native CLAIM/Result, independent review, theorem admission or physical applicability is asserted.
