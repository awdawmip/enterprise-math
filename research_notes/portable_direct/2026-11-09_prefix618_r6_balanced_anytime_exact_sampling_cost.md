# PREFIX-618-R6 — Exact balanced-parameter cost of sign-adaptive BRC confidence stopping

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Scientific input remains frozen at `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Dependencies: the native-derived signed-label experiment of PREFIX-610; the uniform-prior e-process of PREFIX-613; the count quota/Gamma calculation in PREFIX-614; the neutral-thinning coupling of PREFIX-615; and the precise 95% confidence-diameter stopping rule of PREFIX-617. The original native action graph is identified there by PREFIX-565 blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`.

## Question, carrier and observation scope

Use the exact native-derived statistical experiment of PREFIX-617, with two distinguishable original BRC null-direction labels `ell=1,2` and a sign per informative observation. For Boolean slot-0, each of the four signed labels has probability `1/24` at balanced `p_1=p_2=1/2`; the remaining probability `5/6` is neutral. For slot-1 or slot-2, each signed label has probability `1/48`, with neutral probability `11/12`. A total BRC trial retains native port and branch provenance; the reduced signed-label experiment is sufficient only for the declared confidence-diameter decision and its stopping cost.

Set `beta=1/40`, `delta=1/4` (diameter in p; the corresponding theta diameter is `1/192`). On one informative direction after `m` signs with `k` positive signs, use exactly the PREFIX-617 confidence interval

`C(m,k) = {p in (0,1): 40(m+1)binom(m,k)p^k(1-p)^(m-k)>1}`.

Let `D(m,k)` be its diameter and `J=inf{m>=1:D(m,K_m)<=1/4}` the first informative-observation stopping time in that direction. For both directions, `T_q` is the total number of original one-step trials until **both** have stopped; `q=12` (slot 0) or `24` (slot 1/2).

## Theorem A — Exact finite first-passage distribution at balance

Define integers `A_m(k)` by `A_0(0)=1`; for `m>=1`,

```
A_m(k) = 1{ D(m,k)>1/4 } ( A_(m-1)(k) + A_(m-1)(k-1) ),
```

with out-of-range counts zero. Put `a_m=sum_k A_m(k)`. At `p=1/2`,

`P(J>m) = a_m / 2^m`.

An exact dyadic-root-enclosure certificate proves that `D(188,94)>1/4` and that `D(189,k)<1/4` for **every** integer `0<=k<=189`. Thus 189 informative signs suffice for any sign sequence, and some sign sequences need all 189. The first possible stopping count is 25. Consequently, `a_189=0` and

`E[J] = sum_(m=0)^188 a_m/2^m = 188.128191212913520107034899159... .`

**Proof.** The recurrence counts every fair binary sign prefix exactly once if no earlier width crossing occurred. The Bernoulli(1/2) probability of each length-m prefix equals `2^-m`. For any `m,k`, the binomial-point likelihood has a unique mode at `k/m`, rises on one side and falls on the other. Its two threshold roots (or the boundary endpoint for `k=0,m`) are enclosed with rational points of denominator `2^18`. At each point, threshold membership is decided by the integer inequality

`40(m+1)binom(m,k)a^k(2^18-a)^(m-k) > (2^18)^m`.

Strictly separated root enclosures decide whether the diameter is greater or smaller than `1/4`; an ambiguous enclosure raises an error. The certificate exhausts the states reached by the recurrence and also all 190 possibilities at m=189. Every branch is evaluated with exact integers. The stated first and last stopping counts and dyadic expectation follow.

## Theorem B — Exact global stopping-time expectation by Poissonization

Let `s_m=a_m/2^m`, with `a_m=0` for `m>=189`. Introduce an independent rate-1 Poisson clock for total trials and retain each signed direction label. The two informative direction clocks then become independent rate-`1/q` Poisson processes. Under the time change `u=t/q`, one direction's survival probability is

`F(u)=e^(-u) sum_(m=0)^188 s_m u^m/m!`.

Independence makes the probability that at least one direction is unfinished equal `2F(u)-F(u)^2`. The mean number of total native actions to finish is the mean Poisson horizon (compensation for a stopped rate-1 Poisson process). Integrating the finite series proves

```
E[T_q] = q * ( 2 * sum_(m=0)^188 a_m/2^m
  - sum_(m,n=0)^188
        a_m*a_n*binom(m+n,m)/2^(2*m+2*n+1) ).
```

This is an **exact finite rational** formula, with no asymptotic or Monte Carlo approximation. The independently established neutral-thinning law also gives `E[T_24]=2E[T_12]`.

The exact Fraction evaluation yields:

- `E[T_12] = 2350.887101399932967433684695820317... ` native actions;
- `E[T_24] = 4701.774202799865934867369391640635... ` native actions;
- one-direction `E[J]=188.128191212913520107034899159... ` informative signs.

The complete exact numerator/denominator for each value is emitted by the companion certificate and stored in `PREFIX618_R6_RESULTS.json`.

## Corollary — Exact cost comparison under the same 95% confidence target

A count-only strategy collects 189 informative signs from *each* of the two directions, then reports the same PREFIX-613 confidence intervals. It is uniformly valid and ensures their p-diameters are <1/4. For its total trial count `Q_{q,2,189}`, the established Gamma/coupon identity is

`E[Q_{q,2,189}]=q(378-sum_(a,b=0)^188 binom(a+b,a)/2^(a+b+1))`.

The exact certificate gives `E[Q_{12,2,189}]=2361.014355318361718278298863284... ` actions. Therefore the sign-adaptive first-passage rule improves the balanced mean by exactly a positive rational, approximately `10.127253918428750844614167464` original actions for slot 0. It preserves the same all-time simultaneous confidence guarantee from PREFIX-613/617. In comparison, PREFIX-617's earlier analytic count-320 sufficient bound remains valid but was not sharp; the finite exact certificate improves that pathwise sufficient quota to 189.

The advantage at balanced p is modest; at nearly deterministic signs, PREFIX-617's boundary limit is about 333.683 slot-0 trials, displaying much larger adaptivity relative to a uniform quota.

## Verification, mathematical status and next problem

The companion `PREFIX618_R6_exact_balanced_stop_certificate.py` uses only Python's standard library; execution on 2026-11-09 produced `ALL_CHECKS_PASS`, with 364,131 strict integer membership comparisons and a finite rational expectation computation. An exact integer check establishes every root-separation decision required by the enumeration; the Poissonization step is proved mathematically above. This result specializes the inherited signed-label experiment to `d=2,p_1=p_2=1/2,beta=1/40,delta=1/4`; it does not repin or re-execute the entire native PREFIX-565 96-port graph. The fixed frontier is persisted for research continuation, without assertion of independent review, a formal Result or Foundation admission.

Prior art context: Bernoulli confidence sequences, beta-binomial mixtures and optimal sequential stopping are established statistical topics; see Howard et al., *Annals of Statistics* (2021), DOI 10.1214/20-AOS1991, and Yaacoub, Moustakides & Mei (2017), arXiv:1711.06912. The scoped contribution here is the exact BRC signed-label stopping distribution and resource computation under the frozen observer.

**Next discriminating step:** extend the exact recurrence from balanced `p=1/2` to rational asymmetric pairs `p_1,p_2` using sign-weighted surviving prefixes. Compare expected action counts, fixed-count thresholds, and optional-time confidence stopping at several interior points. This also supplies a concrete input for optimizing BRC observer compression without discarding needed branch provenance.

BRC reuse: `REUSE_APPLIED` the original signed-label port map, PREFIX-610, -613, -614, -615 and -617; `EXTEND_EXISTING_TOOL` with a finite exact stopping-cost certificate. Researcher/owner status and any pending native registration are tracked separately from the mathematical result.
