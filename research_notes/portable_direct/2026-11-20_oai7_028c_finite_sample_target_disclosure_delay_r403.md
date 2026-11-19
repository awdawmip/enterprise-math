# OAI7 r403 — Finite-horizon detection and delayed emergence of target information

Date: 2026-11-20 (Asia/Shanghai). Context: `RS-OAI7-028-C-20261007-6F2A81` / immutable publication `TP2-96FAC49786245691AE19`. Source status: **new Driver-authored mathematical derivation**, not an independent Native Review, frozen Result, Task completion or proof of an improved Gaussian moat schedule. Preserve prior Researcher `EM-EMF6D046-5A2844` and Driver authorship separately.

## Theorem: m-1 iid profiles suffice to detect whether a target carries type information

Let `A` be a finite mixing variable, `X=f(A)` a finite target, and `W_1,W_2,...` conditionally iid on a common finite alphabet `Omega` with law `q_A`. Let `V=q_A` be the **exact** law type, taking `m` distinct values `q_1,...,q_m`. Let `B_n` be the unordered histogram of `W_1,...,W_n`. All mutual information is measured in nats.

For `m >= 2`,

```text
I(X;V) > 0  if and only if  I(X;B_(m-1)) > 0.
```

Equivalently, `I(X;B_(m-1))=0` **forces** `I(X;B_n)=0` for every finite `n` and `I(X;V)=0`. In contrast, knowing only `I(X;B_1)=0` does not in general control subsequent samples. For `m=1`, both type and all sample data have zero mutual information with `X`.

**Proof.** Conditional on `X=x`, every ordered sample word `w_1...w_n` has mass
```text
P(w_1,...,w_n | X=x) = sum_(v=1)^m pi_v(x) product_(j=1)^n q_v(w_j),
pi_v(x)=P(V=v | X=x).
```
This depends on the word only through its histogram. Thus `B_n` is sufficient for `X`: `I(X;B_n)=I(X;W_1,...,W_n)`.

The distinct vectors `q_1,...,q_m` admit a real vector `t=(t_w)_(w in Omega)` for which the scalar values `lambda_v=sum_w t_w q_v(w)` are pairwise distinct. Indeed, forbidden `t` lie in finitely many proper hyperplanes.

If `I(X;B_(m-1))=0`, then `W_1,...,W_(m-1)` have a law independent of `X`. Every prefix of length `r<=m-1` therefore also has a law independent of `X`. Writing `g(W_j)=t_(W_j)`, conditional iid sampling gives
```text
E[product_(j=1)^r g(W_j) | X=x] = sum_v pi_v(x) lambda_v^r.
```
The left side is independent of `x` for `r=1,...,m-1`; for `r=0` the same holds because `sum_v pi_v(x)=1`. The `m x m` Vandermonde matrix with entries `lambda_v^r` for `r=0,...,m-1` is invertible. Hence all `pi_v(x)` are independent of `x`, so `I(X;V)=0`. Conversely, if `X` and `V` are independent, the Markov chain `X -> V -> (W_j)` makes `X` independent of every `B_n`. QED.

## Sharpness: the first detectable sample may be exactly m-1

For every `m>=2`, there is a full-support rational conditional mixing example on a **binary** profile alphabet with
```text
I(X;B_n)=0 for n=1,...,m-2, yet I(X;B_(m-1))>0.
```
Choose distinct rational Bernoulli parameters `q_i=i/(m+1)`, `i=1,...,m`. Define the nonzero rational barycentric coefficients
```text
a_i = 1 / product_(j != i) (q_i - q_j).
```
The leading-coefficient identity for Lagrange interpolation gives
```text
sum_i a_i q_i^r = 0 (0<=r<=m-2),  and  sum_i a_i q_i^(m-1)=1.
```
Take `X` a fair bit, and put `P(V=i|X=0)=1/m+epsilon a_i`, `P(V=i|X=1)=1/m-epsilon a_i`, with any positive rational `epsilon<min_i (1/m)/|a_i|`. Both conditional type distributions are strictly positive and sum to one. For any binary word of length `n<=m-2`, the probability under `V=i` is `q_i^k(1-q_i)^(n-k)`, a polynomial of degree at most `n`, so its mixture laws agree exactly for `X=0,1`. At `n=m-1`, the probability of the all-ones word differs by `2 epsilon` between the two targets. Thus the bound `m-1` cannot be decreased uniformly.

As an especially transparent `m=3` boundary example, let `X` be fair. Given `X=0`, choose a Bernoulli law `q=0` or `q=1`, each with probability `1/2`; given `X=1`, choose the single Bernoulli law `q=1/2`. Each sample is an exact fair coin marginally, so `I(X;W_1)=0`, while repeated samples disclose type mixture. For all `n>=1`,
```text
I(X;B_n)=log 2 - (1/2+2^(-n)) h_2(1/(2^(n-1)+1)).
```
In particular `I(X;B_1)=0`, `I(X;B_2)=log 2-(3/4)h_2(1/3)=0.2157615543388357...` nats, and `I(X;B_n) -> log 2` as `n -> infinity`.

**Exact checks:** for `m=2,...,9` rational arithmetic was used to verify `sum_i a_i q_i^r=0` through `r=m-2` and equals one at `r=m-1`, as well as positivity of an explicit rational perturbation and equality of all conditional Bernoulli word probabilities for `n<=m-2`. Numerical decimal values here are only evaluations of the closed-form exact entropy expression, not proof of the theorem.

## Gaussian transfer relevance and interpretation

r400's decreasing-increment theorem concerns the **complete mixing variable A (or exact type V)** under conditional iid sampling. It does **not** automatically extend to a target residue `X=F_S(Y)` that does not determine the conditional law type: mixing over different `V` conditional on `X` can hide the target from individual samples while making it detectable jointly. The explicit `m=3` example proves this distinction.

r402's target-aware clustered inequality remains valid because it upper-bounds `I(X;B_n)` through the full conditional type before using sample redundancy. This new theorem adds a sharp qualitative detection horizon but does not supply a quantitative small-information budget for the fixed-start Gaussian laws. To apply it to the pinned schedule, first determine or bound the number and conditional mixture weights of **distinct residual-profile laws**, with the exact-start quantifier and independent signed-subset selection retained. The original Gaussian schedule's already-proved Shannon data budget remains valid unchanged.

Scientific inputs and context: [pinned `coverage-transfer.tex`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex), [r396](https://github.com/awdawmip/enterprise-math/blob/9725b1dab7c8d8fa293bab5f2eec54896020e729/research_notes/portable_direct/2026-11-20_oai7_028c_information_theoretic_cost_refinement_r396.md), [r402](https://github.com/awdawmip/enterprise-math/blob/a2fda95ce1be673461b113b16fad7db2527b11a0/research_notes/portable_direct/2026-11-20_oai7_028c_targeted_cluster_twosample_info_r402.md). This is new Driver-authored research with shared-source exposure, not independent nonauthor review. Exact Result intake, Native Review, Source/Activity linkage, formal Task DONE and parent objective completion remain distinct gates.
