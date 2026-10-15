# BRC: 单坐标严格 n 步观察延迟；Q1T3 图轮廓碰撞谱

**UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM** · 2026-10-16

Read pins: GLOBAL_KNOWLEDGE_V1 `main@eb18d97a4d08010532579a2db03d4bea86555bc7`; Enterprise Math `main@f44e946d38af85d3198a27a8a099d4af11476095`. P000 and ACTIVE worldview read. Follows prior Q1T3 pair-graph sufficient profile and n≤6 finite full-pair results; does not restate them as new discoveries.

## Model
n≥2 labeled sources with nonnegative integer residual masses d_i. Operation G_j=I\\{j} secretly chooses any i≠j with positive support and resets d_i to 0; choosing a previously reset source is permitted. The bit observed **after** each action is [sum of remaining masses≥T]. Initial feedback is not exposed. A public strategy chooses actions and stop rules based on feedback; its only output is whether **every** possible terminal hidden path has remaining mass≥Q, with 1≤Q<T. This is a positive-support BRC auxiliary observer, not a native X6 physical or signed-amplitude model.

## Theorem A: one-coordinate change forces n steps, all integer thresholds
For every n≥2, 1≤Q<T, let X=(Q,Q,...,Q), Y=(T,Q,...,Q). They differ on exactly one labeled coordinate and satisfy X≡_{n−1}Y yet X≢_nY.

Proof: Before n resets, at least one of the n originally positive sources remains; every such source contributes ≥Q in either state. Every strategy of depth ≤n−1 therefore has Boolean terminal Safe_Q=true for both states. Construct an n-step strategy: execute G_0 exactly n−1 times irrespective of intermediate feedback; after the last feedback, stop if it is high and otherwise execute G_1 and stop. Y always retains source 0 of mass T during the prefix, hence always gives high and terminates safely. In X there is a positive-support trace resetting 1,...,n−1 during the prefix, leaving Q<T and triggering low; G_1 permits resetting 0, leaving 0<Q. Thus Y is universally safe and X has an unsafe trace at n steps. QED.

This strengthens the earlier all-threshold n-delay witness by demanding **Hamming distance one**, not n independently changed coordinates.

## Theorem B: Hamming-one n-delay without any individually high source
For n≥3, T≥2Q+1, set a=T−Q. Let X=(Q,Q,a,...,a) and Y=(Q,a,a,...,a); both have full positive support and **every coordinate <T**. They differ at source1 only, and X≡_{n−1}Y yet X≢_nY.

Proof: Each mass is ≥Q, so all <n-step strategies remain terminally safe for both. Execute G_0 n−2 times, inspect the feedback after the last such action, and stop if high. On low, execute G_0 once more, then G_1, then stop. In Y, source0 retains Q and at least one of n−1 other sources with mass a remains after at most n−2 resets, so residual≥Q+a=T; low is impossible, and Y stops safely. X admits the trace that first resets all n−2 indices 2,...,n−1, leaving 2Q<T; the following G_0 can reset index1 and G_1 index0, leaving 0<Q. QED.

For Q=1,T=3, this is precisely (1,1,2,...,2) versus (1,2,2,...,2). Both have the same support and empty single-source-heavy set. Their pair graph differs only at the edge {0,1}. Thus a **single two-source threshold residual** can be necessary for adaptive observability at maximal n-step depth, for every n≥3. This does not establish arbitrary-n minimality of the whole pair-graph quotient.

## New exact collision spectrum of the previously proved Q1T3 subset profile
For clipped states in {0,1,2,3}^n, the known profile (Z,H,M,E) has one fiber of size m+1 for each choice of a medium-set M with |M|=m and a 0/3 assignment outside M; every other fiber is singleton. The nontrivial fiber-size spectrum is

F_{n,m}=binom(n,m)2^(n−m), m=1,...,n.

Hence the total number of nontrivial fibers is 3^n−2^n, and **the number of ordered pairs of states with identical complete subset threshold profile**, including diagonal, is

C_n=4^n+n(n+5)3^(n−2).

Proof: For fixed M, the size-(m+1) fiber consists of assignments with zero or exactly one coordinate 1 (its 1–1 edge graph is empty). All 2^m−m−1 remaining assignments have distinct nonempty clique graphs. Thus C_n=Σ_m binom(n,m)2^(n−m)[(m+1)^2+2^m−m−1]
=4^n+Σ_m binom(n,m)2^(n−m)m(m+1)
=4^n+n(n−1)3^(n−2)+2n3^(n−1).
In particular the distinct unordered identical-profile pairs number n(n+5)3^(n−2)/2.

n=5 gives P=619,C=2374; n=6 gives P=2638,C=9442; n=7 gives P=11281,C=36796. The n=6 (2638,9442) pair agrees with the **earlier** full-orbit Q1T3 certificate, which additionally reported that all distinct static profiles are adaptive distinguishable. That older finite observation entails A_6(1,3)=2638 if its certificate is accepted; this turn did not rerun the whole 54,264-orbit BFS. No claim for A_n=P_n when n≥7.

## Verification / limitations / follow-up
Local exact checker `verify_single_coordinate.py`: 376 theorem-parameter instances (2≤n≤9,1≤Q≤6,Q<T≤9 within scope); 66 independently enumerated hidden-sequence checks (n≤5); exhaustive clipped-state graph fiber count for n=2..8, with independent all-subset threshold signatures n≤5. All assertions passed locally. Complete proof, program, JSON, log and SHA-256 manifest retained in local evidence package. NOT a native Source Researcher activity, claim, review or Foundation theorem.

Next unresolved unit: construct a uniform separating feedback strategy for *every* pair of different Q1T3 pair graphs for n≥7, or find the first exact extra-equivalence counterexample; the theorem B feedback-gate template is a suggested restricted case.
