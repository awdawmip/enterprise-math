# Prime Coordinate Factorization Complexity and Failure Classification — Research Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION`  
Publication-ID: `TP2-8F7443BCAF2BC5243574`  
Researcher-ID: `EM-PCF7-A156DB`  
Claim-ID: `chatgpt-pcf7-20260831-1028-sol`  
Execution record: `ER-A156DB0F0B38FE774AFB`

## 1. Frozen verdict

Primary task verdict:

`COMPLEXITY_FRONTIER_FROZEN`

Hard target:

`FACTOR_ALGORITHM_COMPLEXITY_AND_FAILURE_CLASSIFIED`

is met at Researcher-return strength.

The decisive classification is not that the accepted PCF4 public-prefix object is expensive. It is sharper:

> The PCF4 public-prefix object can have polynomial per-query cost in the input bit length while still failing to be a polynomial-time factorization algorithm, because every query is exactly a gcd against an `N`-independent integer and polynomial prefix schedules have infinitely many balanced semiprime inputs on which the split probability is exactly zero.

The accepted public-prefix lane therefore freezes at

`SUCCESS_PROBABILITY_NOT_LOWER_BOUNDED / CLOSE_AS_GENERIC_FACTORING_CANDIDATE_AT_PUBLIC_PREFIX_SCOPE`.

The separate composite-length lift `L=N`, under the frozen term-by-term recurrence, freezes at

`SQRT_SCALE_OR_WORSE_PROVED`

because it already requires at least `N=Omega(2^n)` recurrence stages for an `n`-bit input before the final gcd, and it also has a conditional synchronization failure mechanism.

The frozen 64-seed quadratic and sixth-power Enterprise probes are likewise finite fixed-integer gcd families: their good finite benchmark scores do not supply a worst-case success lower bound.

No generic factorization speedup, universal factorization lower bound, Foundation promotion or Working Truth grant is claimed.

## 2. Authority boundary and dependency pins

This task was recovered from a stale publication-time dependency label by the canonical PCF7 Driver recovery review. The dependency gate is satisfied by:

1. the frozen PCF2 factor-blind benchmark; and
2. the accepted PCF4 exact no-go object.

Operational mathematical input:

- PCF4 Result: `RR-A33E88150B0DAD0B13B8`;
- accepted scope: `PUBLIC_PREFIX_FIXED_INTEGER_SUPPORT_NO_GO`;
- PCF4 return: `research_returns/PRIME_COORD_FACTOR_BLIND_PADIC_GCD_BRIDGE_RETURN_20260827.md`;
- PCF4 exact theorem: `gcd(G_N(L),N)=gcd(F_L,N)` for `gcd(N,6)=1`.

Frozen benchmark control surface:

- PCF2 verdict: `BENCHMARK_FROZEN_AND_SEALED`;
- 89 cases across all eight required families and three bit bands;
- generation-3 recovery is integrity-only with `NO_CORPUS_DELTA / NO_PARAMETER_DELTA / NO_SCORE_DELTA`.

Two later Researcher returns are visible but are **not operational authority in this return** because their Driver reviews are still pending:

- PCF5 Draft PR #816: `RESTRICTED_SUPPORT_COMPRESSION_PROVED`;
- PCF6 Draft PR #790: `FUNCTORIAL_REALIZATION_OBSTRUCTED`.

They are analyzed only in a clearly typed conditional appendix below. Nothing in this PCF7 return promotes them.

P000 remains the project root premise. None of the complexity arguments here changes the 6D-space + 1D-time ontology or promotes a three-axis research slice to full-world status.

## 3. Common cost model

Let

\[
n=\lceil\log_2 N\rceil.
\]

Let `M(b)` denote the bit complexity of multiplying `b`-bit integers and let

\[
G(b)=O(M(b)\log b)
\]

be a standard gcd envelope.

Classification is always in the input length `n`:

- `poly(n)` is polynomial;
- `2^{o(n)}` is subexponential in `n`;
- `2^{cn}` for fixed `c>0` is exponential in `n`, even when `c<1/2`;
- ordinary deterministic trial-divisor enumeration has square-root candidate scale `sqrt(N)=2^{n/2+O(1)}`.

The PCF2 `ops` counters are retained as exact algorithm-local benchmark proxies only. They are not converted into fake cross-algorithm wall-clock units.

## 4. Accepted PCF4 object: exact bit-cost derivation

PCF4 uses

\[
A_k=\binom{2k}{k}^2\binom{3k}{k},
\]

with recurrence

\[
A_0=1,
\qquad
A_{k+1}
=A_k\frac{6(2k+1)(3k+1)(3k+2)}{(k+1)^3}.
\]

For public prefix `L`,

\[
G_N(L)=\sum_{k=0}^{L-1}(6k+1)A_k216^{-k}\pmod N,
\]

and the denominator-cleared integer is

\[
F_L=\sum_{k=0}^{L-1}(6k+1)A_k216^{L-1-k}.
\]

PCF4 proved

\[
216^{L-1}G_N(L)\equiv F_L\pmod N,
\]

and, since `216` is a unit when `gcd(N,6)=1`,

\[
\boxed{\gcd(G_N(L),N)=\gcd(F_L,N).}
\tag{4.1}
\]

### 4.1 Intermediate integer growth

The accepted PCF4 bound is

\[
0<F_L<6L^2 216^{L-1}.
\]

Therefore

\[
\operatorname{bits}(F_L)
<
\log_2(6L^2)+(L-1)\log_2 216+1
=O(L+\log L).
\]

Likewise `A_k` has `O(k)` bits from the elementary binomial bound `A_k<=128^k`.

### 4.2 Arithmetic stages

The frozen recurrence performs `L-1` exact recurrence updates, one prefix accumulation per term, then one final gcd. With monotone multiplication cost this gives the conservative PCF4 envelope

\[
\boxed{
T_{\rm PCF4}(N,L)
=O\!\left(LM(L+n)+G(n)\right).
}
\tag{4.2}
\]

The exact constant is not frozen as a universal machine model; the important dependence is linear in the number of recurrence stages and quasi-linear or better only inside each integer operation.

### 4.3 Memory

A streaming implementation keeps the current `A_k`, current prefix accumulator and `N`. Thus

\[
\boxed{S_{\rm PCF4}(N,L)=O(L+n)\text{ bits}.}
\tag{4.3}
\]

No `L`-term table is required.

### 4.4 Polynomial-cost regime

If

\[
L\le P(n)
\]

for a fixed polynomial `P`, (4.2) and (4.3) are polynomial in `n` under the frozen recurrence implementation.

This establishes only **polynomial evaluation cost**. It does not establish polynomial-time factorization, because success is a separate theorem obligation.

## 5. Exact seed-success and amplification theorem

For `N=pq` with distinct primes `p,q>3`, PCF4 gives the exact one-query split criterion:

\[
\gcd(G_N(L),N)\in\{p,q\}
\]

iff exactly one of `p,q` divides `F_L`.

For a public seed distribution `mu`, define

\[
\theta_N
=
\mu\{L:p\mid F_L,\ q\nmid F_L\}
+
\mu\{L:q\mid F_L,\ p\nmid F_L\}.
\tag{5.1}
\]

This is the exact single-trial success probability.

For `T` independent public trials, success of at least one trial is exactly

\[
\boxed{
1-(1-\theta_N)^T.
}
\tag{5.2}
\]

Therefore

\[
\boxed{
\theta_N=0\Longrightarrow 1-(1-\theta_N)^T=0
}
\tag{5.3}
\]

for every finite `T`.

This is the amplification boundary: repetition amplifies a positive seed probability; it cannot manufacture asymmetry when the exact one-trial probability is zero.

The same zero statement remains true for an adaptive schedule if every queried prefix lies in a set on which both hidden primes are outside every `F_L` support: previous `gcd=1` outputs do not create a nonzero supported prefix.

## 6. New PCF7 theorem: polynomial-prefix balanced zero-success family

This is the principal new classification result of PCF7.

### Theorem 6.1 — balanced zero family for every polynomial prefix cap

Let `P(n)` be any polynomial eventually taking positive integer values. Consider any PCF4 public-prefix campaign—deterministic, randomized or adaptive—whose every queried prefix on an `n`-bit input satisfies

\[
1\le L\le P(n).
\]

Then there exist infinitely many **balanced semiprimes**

\[
N=pq,
\qquad 1<p<q<2p,
\]

for which

\[
\gcd(G_N(L),N)=1
\]

for every allowed prefix `L`. Hence the exact split probability is zero for every such campaign.

### Proof

PCF4 proved

\[
\omega(F_L)
<
\log_2(6L^2)+(L-1)\log_2 216,
\tag{6.1}
\]

where `omega` counts distinct prime divisors.

For a bit length `t`, let

\[
Q_t=\bigcup_{1\le L\le P(t)}\{r\text{ prime}:r\mid F_L\}.
\]

By (6.1),

\[
|Q_t|
\le
\sum_{L=1}^{P(t)}O(L+\log L)
=O(P(t)^2),
\tag{6.2}
\]

which is polynomial in `t`.

Now fix a large integer `m` and let

\[
R_m=\{r\text{ prime}:2^{m-1}<r<2^m\}.
\]

By the prime number theorem (equivalently, the standard exponential prime-abundance consequence for dyadic intervals),

\[
|R_m|\asymp \frac{2^m}{m},
\]

so for all sufficiently large `m`, `R_m` contains more primes than the polynomial-size set

\[
Q_{2m-1}\cup Q_{2m}.
\]

Choose two distinct primes

\[
p,q\in R_m\setminus(Q_{2m-1}\cup Q_{2m}).
\]

Then `q/p<2`. Also

\[
2^{2m-2}<pq<2^{2m},
\]

so

\[
n=\lceil\log_2(pq)\rceil\in\{2m-1,2m\}.
\]

By construction neither `p` nor `q` divides any `F_L` with `1<=L<=P(n)`. Using (4.1), every allowed query has gcd `1`. This is independent of how the campaign randomizes or adapts among those prefixes. ∎

### Corollary 6.2 — no worst-case positive seed lower bound

For every polynomial-prefix PCF4 campaign,

\[
\inf_{N\in\mathcal B}\theta_N=0,
\]

where `B` contains balanced semiprimes.

Thus no uniform inverse-polynomial, constant or merely positive worst-case seed-success bound exists at the accepted public-prefix scope.

The operative verdict is therefore

`SUCCESS_PROBABILITY_NOT_LOWER_BOUNDED`.

This closes the apparent paradox: the evaluation routine can be polynomial while the factorization success theorem fails exactly.

## 7. Fixed 64-seed Enterprise probes: the same structural obstruction

The frozen PCF2 public quadratic family evaluates, for fixed public seeds `s=0,...,63`,

\[
\gcd(N,s^2+1),
\qquad
\gcd(N,s^2+s+1).
\]

The frozen sixth-power family evaluates

\[
\gcd(N,s^6-1),
\qquad
\gcd(N,s^6+1).
\]

For each fixed `s`, every polynomial value is an ordinary integer independent of `N`. Therefore each frozen campaign is a finite set of gcd probes against fixed integers.

Let `C` be the product of all nonzero probe integers in a frozen family. Any two primes `p,q` outside the finite prime support of `C` give a semiprime `N=pq` on which every gcd is `1`.

Hence both frozen Enterprise probe families have infinitely many exact zero-success semiprimes.

This is fully consistent with, and explains the scope of, their finite benchmark results:

- quadratic probes: `74/89`, with `15` exact fixed-budget failures;
- sixth-power probes: `84/89`, with `5` exact synchronized/trivial-only failures.

Those are useful finite regressions. They are not universal factorization theorems and cannot supply a worst-case positive success probability.

Both freeze at

`SUCCESS_PROBABILITY_NOT_LOWER_BOUNDED / BENCHMARK_BASELINE_ONLY`.

## 8. Composite-length lift `L=N`: cost and synchronization

The PCF4 return also analyzes the natural `L=N` lift.

Under the frozen term-by-term recurrence, an `n`-bit input satisfies

\[
N\ge2^{n-1}.
\]

Setting `L=N` therefore forces at least

\[
\boxed{\Omega(N)=\Omega(2^{n-1})}
\tag{8.1}
\]

recurrence stages before the final gcd.

This alone exceeds the ordinary square-root candidate-count scale

\[
\sqrt N=2^{n/2+O(1)}.
\]

The conservative PCF4 bit upper envelope becomes

\[
O\!\left(NM(N+n)+G(n)\right),
\]

with streaming memory `O(N+n)` bits because the exact recurrence intermediates have `O(N)` bit length.

Thus this concrete lift is not a hidden sub-square-root factoring algorithm. Its task-local verdict is

`SQRT_SCALE_OR_WORSE_PROVED`.

PCF4 additionally proved an exact conditional synchronization theorem: if the weak prime shadow holds for both hidden factors, then

\[
G_{pq}(pq)\equiv0\pmod{pq},
\]

so the gcd returns `N`, not a proper factor.

The all-prime weak shadow itself remains unproved and is not promoted here. The complexity classification does not need that conjecture: (8.1) already makes the frozen `L=N` implementation worse than square-root candidate scale.

## 9. Failure-family atlas

### 9.1 Balanced semiprimes

For every polynomial public-prefix cap, Theorem 6.1 supplies infinitely many balanced semiprimes with exact zero success. This is a theorem-level adversarial family, not merely a benchmark observation.

### 9.2 Near-twin semiprimes

Near-twin structure does not rescue a fixed-support gcd family. If both near primes lie outside every queried `F_L` support, every PCF4 query still returns `1`.

The frozen benchmark independently records finite failures in near-twin cases for both quadratic and sixth-power probes.

### 9.3 Unbalanced semiprimes

The fixed-support theorem is agnostic to balance and therefore also supplies unbalanced zero-success inputs.

The frozen benchmark records eight unbalanced failures for the 64-seed quadratic probes and six unbalanced failures for the capped Fermat baseline.

### 9.4 Prime powers

For a fixed-support gcd probe on `N=p^e`, if `p` divides no queried fixed integer, every gcd is `1`; if it divides one, the gcd may expose a power of `p` depending on valuation. No universal success theorem follows from polynomial query cost.

The frozen quadratic probe has two prime-power failures.

### 9.5 Multifactor inputs

For `N=prod p_i^{e_i}`, a fixed-support query succeeds only through overlap of the fixed integer's prime support with a proper nonempty subset of hidden prime support. Inputs whose hidden primes all avoid the queried supports produce only gcd `1`.

### 9.6 Carmichael and strong pseudoprime families

Nothing in the PCF4 fixed-integer equivalence depends on Fermat-pseudoprime behavior. These families are therefore governed by the same support condition for the public-prefix object. Their special classical pseudoprime properties do not create factor asymmetry in `F_L`.

### 9.7 Synchronized coordinate / equal-response families

PCF4's `L=N` block law exposes an explicit synchronization mechanism: under the weak prime shadow at both factors, the candidate returns the whole modulus.

This is precisely a `gcd=N` failure, which the frozen PCF2 verifier correctly excludes from successful splits.

## 10. Frozen benchmark comparison under one typed metric

The frozen PCF2 scores are:

| Candidate / baseline | Frozen success | Frozen failure | Scope |
|---|---:|---:|---|
| public quadratic, 64 seeds | 74/89 | 15 | polynomial fixed-budget probe; no worst-case lower bound |
| public sixth-power, 64 seeds | 84/89 | 5 | polynomial fixed-budget probe; no worst-case lower bound |
| trial division | 89/89 | 0 | deterministic on frozen small corpus; square-root candidate scale asymptotically |
| Fermat, cap 4096 | 83/89 | 6 | family-sensitive; six unbalanced cap failures |
| Pollard rho, frozen public schedule | 89/89 | 0 | finite benchmark evidence only; no worst-case theorem inferred here |
| Pollard p-1, B1=256 | 39/89 | 50 | smoothness-sensitive fixed budget |

The PCF4 public-prefix candidate was **not** part of the sealed PCF2 benchmark generation. Therefore this return does not invent a `x/89` score for PCF4 and does not mutate the sealed benchmark.

The direct comparison is instead theorem-safe:

- PCF4 with polynomial `L` has polynomial evaluation cost, but its worst-case split probability is exactly zero on infinitely many balanced semiprimes;
- trial division has exponential `2^{n/2}` candidate scale but a deterministic worst-case factor-search guarantee;
- the frozen quadratic/sixth-power campaigns also have polynomial evaluation cost but exact infinite zero-success families;
- the PCF4 `L=N` lift is already `Omega(2^n)` recurrence stages and is therefore worse than square-root candidate scale under its frozen implementation.

A numerical PCF4 score against the same 89 inputs requires a **new authorized benchmark generation**. Retrofitting it into the sealed generation would violate the benchmark control boundary.

## 11. Conditional appendix: PCF5 pending Driver review

This section is nonoperational evidence only.

PCF5 Draft PR #816 reports, at Researcher-return strength, the N-dependent rule

\[
m=\max(2,\lceil(\kappa N)^{1/6}\rceil)
\]

with `m^2` Perfect-Prime-Table cells and coverage whenever

\[
P^+(N)^2\le\kappa N.
\]

If, and only if, the Driver accepts that result at its stated scope, its cost statement becomes algorithmically important:

\[
m^2=O_\kappa(N^{1/3})=O_\kappa(2^{n/3}),
\]

and the reported product-tree / multipoint implementation has

\[
\widetilde O_\kappa(2^{n/3}M(n))
\]

bit cost plus the same support order of gcds.

For fixed balance ratio this is strictly below `2^{n/2}` square-root candidate scale, but it is still exponential—not subexponential—in input length `n`.

The same pending return gives an arbitrary-imbalance one-full-layer lower boundary of

\[
\Omega(N^{2/3})=\Omega(2^{2n/3})
\]

cells, which is worse than square-root scale.

PCF7 therefore recommends:

`PCF5 = REMAIN_RESTRICTED_AND_PRIORITY_DRIVER_REVIEW`.

If Driver-accepted, it is the first visible lane in this program that escapes PCF4's fixed-integer reduction by using a genuinely `N`-dependent support and therefore merits an authorized new benchmark generation on its **fixed-balance covered family only**.

This recommendation is not an acceptance or promotion.

## 12. Conditional appendix: PCF6 pending Driver review

PCF6 Draft PR #790 reports that the corrected channel-oriented rank-2 mixed realization carries a trace selector `c` with

\[
c\equiv0\pmod p,
\qquad
c\equiv1\pmod q,
\]

so `gcd(c,N)` already gives a factor. Conversely that selector constructs the mixed carrier.

At that pending scope, exact mixed realization is therefore equivalent to having obtained the factor split, not an upstream factoring mechanism. The same return reports that fixed `N`-independent determinant probes reduce to fixed integer resultants.

PCF7 recommendation:

`PCF6_CORRECTED_MIXED_REALIZATION = CLOSE_AS_FACTORING_SHORTCUT_IF_DRIVER_ACCEPTS_SCOPE`.

Preserve only genuinely `N`-dependent observables that do not presuppose the CRT selector.

Again, this is a conditional portfolio recommendation, not a Driver disposition.

## 13. Theorem-ready assumption package

The following package is suitable for later formalization.

### Definitions

1. `n=ceil(log2 N)`.
2. `A_k`, `G_N(L)` and `F_L` as in Section 4.
3. `Support(L)={p prime:p|F_L}`.
4. `Q_t=union_{1<=L<=P(t)} Support(L)` for a fixed polynomial `P`.
5. `theta_N` as in (5.1).

### Imported exact theorem assumptions

From accepted PCF4:

1. denominator-clearing equivalence (4.1);
2. `0<F_L<6L^2 216^{L-1}`;
3. `omega(F_L)<log2(6L^2)+(L-1)log2 216`;
4. the frozen recurrence implementation and its term-by-term execution semantics.

### Standard external theorem

Prime abundance in dyadic intervals, for example the prime number theorem consequence

\[
|\{p:2^{m-1}<p<2^m\}|\asymp2^m/m.
\]

This is the only non-PCF4 theorem needed for the infinite **balanced** zero-family strengthening.

### Derived PCF7 theorems

1. exact independent-trial amplification (5.2);
2. zero remains zero under amplification (5.3);
3. polynomial-prefix balanced zero-family theorem 6.1;
4. no worst-case positive seed lower bound;
5. fixed 64-seed quadratic/sixth-power finite-support no-go;
6. `L=N` frozen recurrence lower bound `Omega(N)=Omega(2^{n-1})` arithmetic stages.

### Explicitly empirical / non-theorem inputs

Do not formalize as mathematical premises:

- PCF2 89-case success counts;
- PCF4 finite weak-shadow regression;
- authoring-time finite regression cases in the PCF7 checker;
- PCF5 and PCF6 Researcher returns unless and until Driver-accepted at exact scope.

## 14. Deterministic checker and certificate

Task-local checker:

`research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py`

Machine-readable certificate:

`research_artifacts/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION/PCF7_COMPLEXITY_FAILURE_CERTIFICATE_V1.json`

The checker independently verifies:

1. the exact `A_k` recurrence against the direct binomial formula;
2. the denominator-clearing congruence and gcd equivalence over multiple composites and prefixes;
3. the PCF4 support-size bound on the finite regression range;
4. an exact balanced semiprime on which every prefix `L<=18` has gcd `1`;
5. an exact balanced semiprime on which all frozen 64-seed quadratic/sixth-power fixed probes have gcd `1`;
6. the exact amplification identity and the `theta=0` boundary;
7. the exponent ordering used only in the pending-PCF5 conditional appendix.

Authoring-time run of the identical checker source:

`PCF7_CHECK_PASS recurrence_terms=18 gcd_cases=108 pcf4_balanced_zero=1009x1013 fixed_probe_balanced_zero=10007x10009 amplification=PASS regime_order=PASS`

The finite witnesses are regression guards, not substitutes for Theorem 6.1.

Tool-reuse resolution:

`NOT_APPLICABLE / TASK_LOCAL_CERTIFICATE_CHECKER_ONLY / NO_NEW_GENERAL_PURPOSE_MECHANISM`.

## 15. Candidate-by-candidate terminal classification

### PCF2 public quadratic probes

Primary verdict:

`SUCCESS_PROBABILITY_NOT_LOWER_BOUNDED`.

Disposition:

`RETAIN_AS_FROZEN_BENCHMARK_BASELINE`.

### PCF2 public sixth-power probes

Primary verdict:

`SUCCESS_PROBABILITY_NOT_LOWER_BOUNDED`.

Disposition:

`RETAIN_AS_FROZEN_BENCHMARK_BASELINE`.

### PCF4 public-prefix lift

Primary verdict:

`SUCCESS_PROBABILITY_NOT_LOWER_BOUNDED`.

Disposition:

`CLOSE_AS_GENERIC_FACTORING_CANDIDATE_AT_PUBLIC_PREFIX_SCOPE`.

Preserve only the explicit successor interface

`N_DEPENDENT_SECOND_OBSERVABLE_NOT_FIXED_INTEGER_REDUCTION`.

### PCF4 `L=N` lift

Primary verdict:

`SQRT_SCALE_OR_WORSE_PROVED`.

Disposition:

`DO_NOT_ADVANCE_AS_SPEEDUP`.

### PCF5 pending result

Authority state:

`UNREVIEWED_RESEARCHER_RETURN`.

Portfolio recommendation:

`REMAIN_RESTRICTED / PRIORITY_DRIVER_REVIEW / IF_ACCEPTED_BENCHMARK_FIXED_BALANCE_SCOPE_IN_NEW_GENERATION`.

### PCF6 pending result

Authority state:

`UNREVIEWED_RESEARCHER_RETURN`.

Portfolio recommendation:

`IF_ACCEPTED_CLOSE_CORRECTED_MIXED_REALIZATION_AS_FACTORING_SHORTCUT / PRESERVE_GENUINELY_N_DEPENDENT_ALTERNATIVES`.

## 16. Final portfolio verdict

The program-level picture is now sharply separated:

1. **Fixed public integer probes** can be cheap and empirically useful but have no generic worst-case success lower bound.
2. **PCF4 public prefixes** are an exact enlarged member of that class and are now closed as a generic factoring route.
3. **PCF4 `L=N`** escapes fixed-prefix independence only at an already worse-than-square-root recurrence scale and has a synchronization frontier.
4. The next mathematically meaningful candidate must be genuinely `N`-dependent before the final modular reduction and must come with a nonzero success theorem on an explicit infinite family.
5. The pending PCF5 result is structurally important precisely because it claims such `N`-dependence and a restricted `N^{1/3}` support; it must be Driver-reviewed before operational consumption.
6. The pending PCF6 mixed realization does not currently provide an upstream factor-blind algorithm.

Frozen portfolio token:

`ACCEPTED_PUBLIC_PREFIX_LANE_CLOSED_AS_GENERIC_FACTORING_ROUTE / PRESERVE_N_DEPENDENT_SECOND_OBSERVABLE_FRONTIER / DO_NOT_PROMOTE_PENDING_PCF5_PCF6_WITHOUT_DRIVER_REVIEW`.

## 17. Smallest unresolved unit and next control action

There is no unresolved unit inside the PCF7 Researcher hard target.

The smallest program-level unresolved units are external:

1. Driver review of PCF5 at its exact restricted-family theorem and bit-cost scope;
2. Driver review of PCF6 at its exact realization-obstruction scope;
3. only after an accepted genuinely `N`-dependent candidate exists, publish an authorized new benchmark generation rather than modifying the sealed PCF2 scores.

Recommended next action:

`DRIVER_REVIEW_THIS_PCF7_RESULT_AND_FREEZE_COMPLEXITY_FRONTIER; THEN REVIEW_PCF5_PCF6_INDEPENDENTLY; NO_AUTOMATIC_SUCCESSOR_PUBLICATION`.

Researcher scope is terminal after immutable Result freeze and scheduler handoff.
