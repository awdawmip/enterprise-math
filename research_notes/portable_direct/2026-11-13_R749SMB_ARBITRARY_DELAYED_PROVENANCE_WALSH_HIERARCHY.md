# R749SMB — Arbitrarily deep delayed signed-provenance prediction: exact Walsh ranks and statistical cost

2026-11-13 Asia/Shanghai. Status: author-side exact proof with finite rational checker; no independent review or native V29/V39 event permission.

Scientific pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (P000 signed X6). Predecessors: R749SM `@9415de46856d44d72988953f636287d3643f2df3:research_notes/portable_direct/2026-11-13_R749SM_PREDICTIVE_HANKEL_MEMORY_HORIZON.md` and R749SMA `@436ce1325ade1b46d5a14afb17786c2ebfa2804f:research_notes/portable_direct/2026-11-13_R749SMA_PARAMETER_UNIFORM_PROVENANCE_RANK.md`. This uses the R749SF *conditional* signed-Port kernel PLUS an explicitly declared finite, sign-history-dependent public-support controller. The private memory is time-tagged historical source data, not a seventh native spatial axis.

## 1. A legal six-axis nonforced cycle with arbitrary-length hidden history

Let `S_i={i,(i+1) mod 6}` for the six named native axes, with indices modulo six. An unsigned directed-support state is `(A,B)` with each support of size two and `|A∩B|=1`. Exactly eight legal next supports `C` satisfy `|B∩C|=1`. The unique forced/C1 next support is `A △ B`; the other seven are nonforced.

The periodic sequence `S_0,S_1,...,S_5,S_0,...` is legal and every consecutive triple is nonforced: `S_(i+2) != S_i △ S_(i+1)`. At any `0≤p<1`, a specified nonforced support step has positive unconditional probability `(1-p)/8`. Conditional on such a step, the R749SF sign-lift kernel copies the two current support signs and draws a fresh independent fair sign at the new target slot (including on a reused named axis, whose previous value was discarded).

For every directed cycle phase, three subsequent nonforced steps replace all three signed axes: `S_i ∪ S_(i+1)={i,i+1,i+2}` and `S_(i+3) ∪ S_(i+4)={i+3,i+4,i+5}`, disjoint modulo six. Consequently a controller may save the newly sampled signed-Port sign at each of `d` consecutive steps, labeled with its historical time, then perform three more nonforced washout steps. Denote those saved signs `Z=(Z_1,...,Z_d)∈{±1}^d`. Every history `z` is permitted and, conditional on any `Z=z`, the *current* eight signed lifts after washout have the identical uniform distribution `1/8`. This is true for every finite `d≥1`, `0≤p<1`, and any reweighted prior on the hidden histories. Time-tagged values must not be silently identified merely because their axis names may reappear.

## 2. Exact adaptive observation law

Choose an invertible multiplicative binary linear basis `W(Z)=(W_1,...,W_d)`. To extend R749SM literally, take `W_1=Z_1 Z_2, W_2=Z_1, W_i=Z_i (i≥3)` for `d≥2`; take `W_1=Z_1` when `d=1`. In each subsequent public-choice stage `i`, independently conditional on private `Z`, select an allowed forced support for public bit `A_i=+1`, or a fixed allowed nonforced support for `A_i=-1`, with

`Pr(A_i=a | Z=z)=(2+a W_i(z))/4`, `a∈{±1}`.

Both support alternatives exist at *every* directed-support context. Conditional on any chosen public word and fixed history, the current sign lift remains uniform: a forced R749SF transition is a doubly-stochastic binary symmetric channel on the old-only sign, and a nonforced transition is a fair reset. Therefore future public choices, conditional on `Z`, follow precisely the independently drawn controller coins. The h-letter likelihood matrix (`0≤h≤d`) is

`M_h(a,z)=4^{-h} ∏_(i=1)^h (2+a_i W_i(z))`.

All source-fiber path weights are explicit positive rationals and all words are positive probability.

## 3. Exact hierarchy, minimal source carrier and singular spectrum

**Theorem 1.** For each finite `d≥1` and `0≤h≤d`, the likelihood matrix `M_h` has rank `2^h`. The point-history predictive-equivalence relation (same probabilities for every public word of length at most h) has exactly `2^h` classes. Over arbitrary strictly interior priors on the `2^d` histories, the smallest number of independent *affine-linear expectation coordinates* preserving all these probabilities is **`c_h=2^h−1`**.

*Proof.* The basis change `Z→W` permutes the columns. On the first h bits the likelihood is a tensor product `B^{⊗h}`, where `B=[[3/4,1/4],[1/4,3/4]]` in `-1,+1` ordering, with `2^{d-h}` identical columns for each remaining history fiber. `det B=1/2`, so `rank M_h=2^h`. Two histories have identical word laws exactly when their first h W-values agree, since each biased coin distinguishes its input and all prefixes have positive probability. R749SM's general affine predictive span theorem gives `rank(M_h)-1` expectation coordinates; no arbitrary/nonlinear encoding optimality is asserted. ∎

At the end of d stages the full `2^d×2^d` channel is a column permutation of `B^{⊗d}`:

`|det M_d|=2^{-d 2^{d-1}}`.

Its singular values are `2^{-k}`, each with multiplicity `binomial(d,k)` for `k=0,...,d`; its spectral condition number is `2^d`. If the controller becomes memory-independent after stage d, the predictive rank remains `2^d` thereafter.

**Corollary.** Across the family of finite historical-memory-dependent controllers, there is no fixed finite-size universal affine predictive source carrier, even though the visible *current signed-lift* marginal always has only eight states over the fixed six-axis space. Each individual d-controller remains finite and has its own sufficient augmented state. The increase is historical BRC provenance, not a new native spatial dimension.

## 4. Walsh reconstruction, Fisher information and exact finite testing bound

For every `J⊆{1,...,d}`, let `χ_J(W)=∏_(i∈J)W_i`. Independently of the history prior,

`E[∏_(i∈J) A_i] = 2^{-|J|} E[χ_J(W)]`.

Hence the `2^d−1` nonempty source Walsh moments are exactly invertible from the full public word law; an *individual* point history has d binary bits while an arbitrary unknown prior has `2^d−1` independent affine expectations. At the uniform history prior, the Fisher information for the Walsh-moment coordinate vector of one d-bit word is exactly

`I_(J,K)=1_(J=K) 4^{-|J|}`, `J,K` nonempty,

so the value `4^{-k}` occurs `binomial(d,k)` times. Full algebraic rank and small statistical distinguishability are distinct properties.

For a strictly positive source-prior witness define
`μ_±(w)=2^{-d}(1 ± (1/2)∏_(i=1)^d w_i)`.
They agree on every *proper* Walsh moment and differ only in the top-degree source parity. Their public laws are
`P_±(a)=2^{-d}(1 ± δ ∏_i a_i)`, `δ=2^{-(d+1)}`,
so `TV(P_+,P_-)=δ`. Their exact affinity is `√(1−δ²)`. For N independent full-word samples from one unknown fixed prior, Cauchy–Schwarz and Bernoulli's inequality imply
`TV(P_+^N,P_-^N) ≤ √(1−(1−δ²)^N) ≤ √N δ`.
Thus for **every integer `N≤4^d`**, the optimal equal-prior binary testing error is **at least 1/4**. Error strictly below 1/4 requires `N>4^d`. This lower bound concerns the declared pair of strictly interior priors in this abstract controller experiment. For a uniformly random *point history*, one d-bit public word yields optimal joint MAP recovery probability `(3/4)^d`.

## 5. Exact checker and evidence scope

Companion `R749SMB_DELAYED_WALSH_RANK_EXACT_CHECK.py` uses integer and `fractions.Fraction` arithmetic, verifies all 120 legal unsigned directed supports, every move on the six-support nonforced loop, three-step washout, all source/public word matrices for `d=1,...,5`, exact rank/absolute determinant, every Walsh column identity, Fisher matrix entries at uniform prior, MAP success and the two interior-prior TV formula. Its executed `R749SMB_DELAYED_WALSH_RANK_EXACT_RESULTS.json` reports `status=PASS`. The algebra above proves every finite d; executable coverage is d≤5. No approximate arithmetic or numerical fit is used.

Next discriminating question: characterize the subset of source Walsh characters exposed by **restricted** allowable controller operations and compute its minimal future-safe BRC quotient; independently inspect native V29/V39 event guards and actual closure certificates before asserting any such construction is a physical event.
