# S23/AV: exact five-fiber n=1000 packing and an exponential-tail convergence bound

Date: 2026-11-07. Author-side mathematical continuation. Frozen scientific source: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34` (unchanged). Predecessor: Draft PR #1777, commit `8ef8ee1a2b19e692963ccec79b4ca70d0f8a7024` (all-n same-fiber reconstruction-radius limit and three-point n=1000 certificate).

## Statistical experiment and quantifiers

Let `a,c` range over `[1/2,7/8]` and set `z=(1-a)c`. The fully observed single-run stopping-label law is `P_(a,c)=(a,z,1-a-z)` on labels `(1,3,4)`, and the compressed binary law is `B_(a,c)=(z,1-z)`. Conditional on one unknown common `(a,c)`, take `n` independent trials. Define

`delta_n = inf_{L:{Y,N}^n -> {1,3,4}^n stochastic} sup_{a,c} TV(P_(a,c)^tensor n, B_(a,c)^tensor n L)`.

The reconstruction kernel `L` may create arbitrary dependencies among decoded coordinates, but cannot depend on the unknown parameters. This is the scoped S23/AV auxiliary observer, **not** a claim about the six-source ten-label S23 mother optimization.

## Theorem A: five-point exact finite-n strengthening

At `n=1000`, `delta_1000 > 7361/10000 = 0.7361`.

### Complete rational proof

Fix observer fiber `z=1/4`. Choose the five rational stop-1 probabilities

`a_j = (1/2, 5551/10000, 381/625, 6627/10000, 5/7)`.

Choose `c_j = 1/[4(1-a_j)] = (1/2, 2500/4449, 625/976, 2500/3373, 7/8)`. Every pair is inside the legal parameter box; the fully observed stop law is `(a_j,1/4,3/4-a_j)`, whereas the compressed law for every pair is exactly `B=(1/4,3/4)`.

For any fixed stochastic `L`, its decoded distribution `Q=B^tensor 1000 L` is therefore independent of `j`. Partition the complete ordered sequences according to the count `X` of stop-1 labels into five disjoint events:

`E_0={X<=527}`, `E_1={528<=X<=582}`, `E_2={583<=X<=636}`, `E_3={637<=X<=688}`, `E_4={X>=689}`.

Under fully observed hypothesis `j`, `X~Binomial(1000,a_j)`. Put

`S_j = sum_{k in I_j} binom(1000,k) a_j^k (1-a_j)^(1000-k)`,

where the five integer intervals are `I_0=[0,527]`, `I_1=[528,582]`, `I_2=[583,636]`, `I_3=[637,688]`, `I_4=[689,1000]`.

For each `j`, `TV(P_j^tensor 1000,Q) >= P_j^tensor 1000(E_j)-Q(E_j)=S_j-Q(E_j)`. Summing over `j`, and using `sum_j Q(E_j)=1`, yields

`max_j TV(P_j^tensor 1000,Q) >= (S_0+S_1+S_2+S_3+S_4-1)/5 =: D`.

This inequality holds for every `L`, hence `delta_1000 >= D`. All `S_j` are *finite rational sums*, and the supplied `VERIFY.py` computes them by arbitrary-precision **integer** binomial numerators, then checks the exact rational inequality `D > 7361/10000`. No floating-point rounding is used for this assertion. Only the human-readable decimal uses a rounded `Decimal` readout:

`D = 0.73610947618143607110... > 0.7361`.

Previous three-point certificate was `delta_1000 >= 0.666338327539439...`; this five-point certificate strengthens the finite-n lower bound by more than `0.06977` absolute.

## Theorem B: all-n exponential-tail lower bound and explicit approach rate

For every integer `n>=1` and `m>=2`,

`delta_n >= max{0, 1-1/m-2*exp(-9*n/[392*(m-1)^2])}`.

Consequently for every integer `n>=1000`,

`1-delta_n <= (28/3)*sqrt(log(n)/n) + 2/n^2`.

### Proof

Choose the `m` equally spaced legal fiber points from the predecessor:

`a_j = 1/2 + 3j/[14(m-1)]`, `c_j = 1/[4(1-a_j)]`, `j=0,...,m-1`.

Their compressed law is always `B=(1/4,3/4)` and the adjacent stop-1 mass spacing is `Delta=3/[14(m-1)]`. Classify the empirical fraction `X/n` to the closest `a_j`, using deterministic tie breaking, yielding disjoint decision events `E_j`. A wrong classification under `j` requires `|X/n-a_j| >= Delta/2`. The standard two-sided Bernoulli Hoeffding inequality bounds this probability by

`2 exp[-2n(Delta/2)^2] = 2 exp[-9n/(392(m-1)^2)]`.

Since the reconstructed law `Q` is common to all `m` hypotheses, the same disjoint-event total-variation sum gives

`delta_n >= 1-1/m-2 exp[-9n/(392(m-1)^2)]`.

The lower bound `0` is always valid. For the explicit rate choose `m=1+floor[(3/28)*sqrt(n/log n)]`; for `n>=1000`, `m>=2`. Then `m-1 <= (3/28)*sqrt(n/log n)` makes the exponent at most `-2 log n`, and `m > (3/28)*sqrt(n/log n)` implies `1/m < (28/3)*sqrt(log n/n)`. Rearrangement proves the displayed convergence rate. In particular `delta_n -> 1` with an explicit stronger rate compared with the predecessor's Chebyshev-based `O(n^(-1/3))` construction (when optimized over `m`).

Hoeffding reference: Wassily Hoeffding, *Probability Inequalities for Sums of Bounded Random Variables*, Journal of the American Statistical Association 58(301), 13–30 (1963), DOI `10.1080/01621459.1963.10500830`.

## BRC / provenance and interpretation

This is an exact positive-rational probability-fiber construction. The binary observer retains `z=1/4` but removes the independently varying stop-1/stop-4 split `a` vs `3/4-a`. The five lawful hypotheses preserve their **source parameter identities** before applying the coarse observer; the loss is demonstrated by disjoint future counts. This uses the BRC observer/provenance discipline directly; there is no claim that the calculation implemented native Heartbeat dynamics or changed P000.

## Verification, status, limits

`VERIFY.py` evaluates the five rational binomial intervals exactly with `math.comb`, integer powers and `Fraction`, verifies every lawful parameter, the shared fiber and the strict rational bound. `RUN_EVIDENCE.txt` records actual local execution. The all-n exponential rate is a separate analytic proof using Hoeffding; the code's finite n=1000 verification does not substitute for that derivation. Author-side result awaiting independent mathematical review and native formal registration; no admitted theorem or formal Result/Review is asserted. The untouched mother objective is a typed lawful connection to six-source/ten-label S23 and its decoder/encoder quantifiers.
