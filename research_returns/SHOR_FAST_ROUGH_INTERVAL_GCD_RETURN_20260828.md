# Research Return — Shor bridge prime-sensitive FAST_ROUGH_INTERVAL_GCD

- Task: `RS-SHOR-FAST-ROUGH-INTERVAL-GCD`
- Publication: `TP2-C193F8CB279ADF29D4ED`
- Researcher: `EM-SHOR-47F805`
- Claim: `chatgpt-shor-20260828-1434-47f805`
- Execution record: `ER-B55AFFE878F086432061`
- Verdict: `UNRESOLVED_EXACT_FRONTIER`
- Hard target: `FAST_ROUGH_INTERVAL_GCD_B1_ALGORITHM_OR_EXACT_CROSS_BLOCK_OBSTRUCTION`
- Hard-target disposition: **not achieved**.  No `B^{1+o(1)}` algorithm and no lower bound covering both frozen canonical candidate models is proved here.

## 1. Executive result

The task admits a substantial exact reduction that removes most of the apparent projector complexity.

Let `B>=2`, let `d<=B^6` be `B^2`-rough, and let `B^2<=x<y<=B^3`.  Then:

1. `Omega(d)<=2` (prime factors counted with multiplicity).
2. After deterministic primality and perfect-square tests, the only nontrivial case is a **distinct semiprime**
   `d=pq`, `B^2<p<q`.
3. For squarefree legal `d`, the ordinary factorial prefix already has the exact factor semantics

   `F_d(z):=gcd(d,z!) = product_{r|d prime, r<=z} r`,

   and therefore

   `G_B(x,y;d)=F_d(y)/F_d(x)`.

   Thus the truncated Mobius-factorial projector is not logically necessary for correctness after the roughness/rank reduction.  It remains a valid representation, but the real obstruction is computational: evaluating the needed prefix factor information below the square-root barrier.
4. `FAST_ROUGH_INTERVAL_GCD` is, up to polylogarithmic overhead, equivalent to deterministic factoring of the resulting `B^2`-rough semiprime class.
5. David Harvey's rigorous deterministic `n^{1/5+o(1)}` factoring theorem immediately solves every legal input with `d<=B^5` within `B^{1+o(1)}`.  Hence the only unresolved size regime is

   `B^5 < d <= B^6`.
6. A strictly lower-information sufficient primitive is isolated:

   `ROUGH_SEMIPRIME_B2_COARSE_LOCATOR` — given a legal hard-regime semiprime `d=pq`, output one interval of additive width `B^{2+o(1)}` containing the least factor `p`.

   Once such an interval is known, the deterministic interval-divisor algorithm of Peng–Lu–Kunihiro–Zhang–Hu (2018), building on Kim–Cheon, refines it to a factor in `B^{1+o(1)}` time.  Conversely a FAST oracle gives such a locator (indeed the exact factor) using `O(log B)` prefix queries.

The research therefore relocates the frontier from “evaluate a complicated Mobius/factorial cross-block object” to “coarsely localize the least factor of a rough semiprime to additive uncertainty `B^{2+o(1)}`”.

## 2. Exact roughness-rank theorem

### Theorem 2.1 — rough legal inputs have at most two prime factors

If all prime divisors of `d` exceed `B^2` and `d<=B^6`, then `Omega(d)<=2`.

**Proof.**  If `Omega(d)>=3`, then, counting multiplicity,

`d > (B^2)^3 = B^6`,

contrary to the input bound.  QED.

Hence exactly three arithmetic types remain:

- `d` prime;
- `d=p^2` with `p>B^2`;
- `d=pq` with distinct primes `B^2<p<q`.

Primality testing and exact integer-square testing have cost polynomial in `log d`, hence `B^{o(1)}`.  In the square case, `p=sqrt(d)` is explicitly recovered, and every target interval answer is simply `p` if `x<p<=y`, otherwise `1`.  Therefore only the distinct-semiprime case needs further work.

This reduction is consistent with Harvey's general deterministic factoring preprocessing: after removing prime factors through the `N^{1/3}` scale, the surviving input has at most two prime factors.  Here the task's stronger `B^2`-roughness and `d<=B^6` imply the same conclusion directly.

## 3. Ordinary factorial-prefix factor theorem

### Theorem 3.1 — squarefree rough prefix identity

Let `d` be squarefree.  For every integer `z>=0`,

`gcd(d,z!) = product_{r|d prime, r<=z} r`.

**Proof.**  Since `d` is squarefree, each prime divisor `r|d` occurs in `d` with exponent exactly one.  Also `r|z!` if and only if `r<=z`.  Taking the gcd selects exactly those prime divisors.  QED.

For `x<y`, the prefix products are nested, so `F_d(x)|F_d(y)` and

`F_d(y)/F_d(x) = product_{r|d, x<r<=y} r`.

Because the target packet `product_{x<p<=y} p` is squarefree, this is exactly

`G_B(x,y;d)=gcd(d, product_{x<p<=y}p)`.

### Square multiplicity guard

One must not silently apply Theorem 3.1 to `d=p^2`.  For example

`B=3, d=11^2, z=22`

has

`gcd(121,22!)=121`,

whereas the desired prime-prefix factor is only `11`.  This is why the perfect-square test belongs before the factorial-prefix simplification.

### Consequence

The canonical truncated rational projector

`T_B(z)=product_{1<=k<=B} (floor(z/k)!)^{mu(k)}`

remains correct, and its denominator remains a unit modulo every legal rough `d`, but it is no longer the smallest exact representation after the rank theorem.  The minimal squarefree representation is simply `gcd(d,z!)`.

This does **not** produce the requested `B^{1+o(1)}` algorithm: generic fast factorial/product evaluation at `z=Theta(B^3)` is still at the `B^{3/2+o(1)}` scale.  The simplification is semantic, not yet asymptotic.

## 4. Exact equivalence with rough-semiprime factoring

Define `FAST(B,d,x,y)` to return the task target `G_B(x,y;d)`.

### Theorem 4.1 — FAST implies factoring

Suppose `d=pq` is a legal distinct semiprime.  Then a FAST oracle factors `d` using `O(log B)` calls and polylogarithmic additional work.

**Proof.**  The least factor satisfies

`B^2 < p <= sqrt(d) <= B^3`.

For integer `z` in `[B^2,B^3]`, query

`H(z)=FAST(B,d,B^2,z)`.

Then `H(z)=1` exactly when `z<p`; once `z>=p`, `H(z)>1`.  Binary search therefore finds the least integer `z` with `H(z)>1`, which is precisely `p`.  Return `p` and `q=d/p`.  There are `O(log B)` queries.  QED.

### Theorem 4.2 — factoring implies FAST

If the prime factorization of legal `d` is known, FAST is computed in polylogarithmic time by multiplying the distinct prime factors of `d` lying in `(x,y]`.  There are at most two such factors by Theorem 2.1.  QED.

### Corollary 4.3

At the exponent scale relevant to this task,

`FAST_ROUGH_INTERVAL_GCD  <=>  deterministic factoring of B^2-rough d<=B^6`,

up to polylogarithmic overhead.

This is stronger than the one-way end-to-end reduction in the taskbook: the purportedly weaker GCD projector is not asymptotically weaker on the frozen rough, size-bounded input class.

## 5. Size stratification from the known one-fifth theorem

Harvey proved a rigorous deterministic classical integer-factorization algorithm with complexity `n^{1/5+o(1)}`; Harvey–Hittmeir later improved logarithmic factors without changing the exponent.

Therefore, if a legal task input satisfies `d<=B^5`, general deterministic factoring costs

`d^{1/5+o(1)} <= B^{1+o(1)}`,

and FAST is solved by Theorem 4.2.

Hence the unresolved regime may be frozen as

`B^5 < d <= B^6`, `d=pq`, `B^2<p<q`.

In this hard regime, because `d<=B^6`,

`d^{1/3} <= B^2 < p <= sqrt(d)`.

So the remaining least factor lies in the same post-`N^{1/3}` semiprime wedge that appears after the standard `N^{1/6+o(1)}` small-factor preprocessing in general deterministic factoring.

## 6. The smallest surviving primitive: B^2 coarse localization

### Definition 6.1

`ROUGH_SEMIPRIME_B2_COARSE_LOCATOR(B,d)` receives a hard-regime legal semiprime `d=pq`, `p<q`, and outputs integers `A,H` with

- `p in [A,A+H]`,
- `H <= B^2 * (log B)^{O(1)}`.

It need not return `p`, a prime list, an interval product, or any factorial residue.

### Theorem 6.2 — coarse localization suffices for FAST at B1

If the coarse locator runs in `B^{1+o(1)}` bit operations, then FAST runs in `B^{1+o(1)}` bit operations.

**Proof.**  Apply the locator.  Peng, Lu, Kunihiro, Zhang and Hu (ACISP 2018) give a deterministic Strassen-based algorithm for finding a divisor known to lie in an interval with the same square-root-of-interval-length scale as the earlier Kim–Cheon interval-prime-divisor algorithms.  For

`H=B^2 (log B)^{O(1)}`,

that refinement costs `B^{1+o(1)}`.  It yields `p`, hence `q=d/p`, after which Theorem 4.2 gives the requested interval GCD in polylogarithmic work.  QED.

### Theorem 6.3 — FAST suffices for coarse localization

By Theorem 4.1, a FAST oracle finds `p` exactly in `O(log B)` queries, so it trivially supplies a width-zero (hence width-`B^{2+o(1)}`) locator.  QED.

Thus, at the target exponent, the task may be replaced by the strictly lower-information question:

> Can the least factor of a `B^2`-rough hard-regime semiprime be localized to additive uncertainty `B^{2+o(1)}` in `B^{1+o(1)}` deterministic time?

This is the one smallest surviving primitive recommended by this return.

## 7. Current deterministic-factorization literature audit

### Harvey 2020/2021

Harvey's 2020 algorithm proves deterministic `N^{1/5+o(1)}` factoring.  In the same paper, after presenting the Lehman/BSGS framework, he explicitly notes that a full square-root speedup for Lehman's original `r asymp N^{1/3}` choice would presumably yield `N^{1/6+o(1)}`.

His Proposition 4.2 gives, for the main search with parameters `r,m`, a cost of the form

`O(((N^{1/2}/(r^{1/2}m) + r) log^4 N + m log^2 N))`.

The explicit additive `r` term is relevant here.

### Harvey–Hittmeir 2026 large-order improvement

Harvey and Hittmeir (arXiv:2601.11131, 2026) show that the former lower-bound restriction on the target order `D` can be dropped: deterministically one can obtain an element of order exceeding arbitrary `D` (or a factor/primality outcome) in essentially `D^{1/2}` times polylogarithmic factors.

This is important but does not by itself close the present task.  For a worst legal semiprime near

`N=d asymp B^6`, `p just above B^2`,

the Harvey search precondition

`(N/r)^{1/2} <= p`

forces

`r >= N/p^2 = B^{2-o(1)}`.

The `+r` term in Proposition 4.2 then already exceeds the target `B^{1+o(1)}`.  Thus cheap access to large-order elements removes one bottleneck but leaves the global Lehman-candidate / factor-location coupling unresolved.

This is an obstruction only to that frozen parameterized Harvey search realization; it is **not** a general lower bound and is not promoted to `EXACT_MODEL_BARRIER`.

## 8. Complexity ledger

| Component | Exact status | Bit complexity at task scale |
|---|---|---:|
| primality / square preprocessing | inherited deterministic arithmetic | `B^{o(1)}` |
| square case `d=p^2` | exact | `B^{o(1)}` after integer sqrt |
| legal `d<=B^5` | Harvey deterministic factoring | `B^{1+o(1)}` |
| generic `gcd(d,z!)`, `z=Theta(B^3)` | inherited fast factorial/product baseline | `B^{3/2+o(1)}` |
| taskbook independent Mobius harmonic blocks | frozen baseline | `B^{3/2+o(1)}` |
| general Harvey factorization at `d=Theta(B^6)` | inherited | `B^{6/5+o(1)}` |
| interval refinement after width `B^{2+o(1)}` locator | Peng et al. deterministic interval-divisor method | `B^{1+o(1)}` |
| producing that locator | **open** | target `B^{1+o(1)}` |

No line in this table hides a factorization oracle inside a claimed new algorithm.  The only `B1` route left open by the return is the locator itself.

## 9. Rational denominators and nonunit intermediates

The taskbook's rational projector remains algebraically sound.  For

`T_B(y)/T_B(x)=A/C` in lowest terms,

all prime divisors of `C` are at most `B^2`; hence a legal `B^2`-rough modulus has `gcd(C,d)=1`.  Therefore `C` is invertible modulo `d`, and

`gcd(d, A*C^{-1} mod d)`

has exactly the intended high-prime support.

The new prefix reduction does not rely on rational inversion at all in the squarefree case.  In the square case, the precheck is mandatory, as shown by the `11^2` multiplicity guard.

No theorem in this return claims that factor-revealing nonunit intermediates can be arranged in `B^{1+o(1)}` time.  That candidate remains subsumed by the unresolved locator/factoring equivalence.

## 10. Exact finite replay

Run:

```text
python scripts/check_shor_fast_rough_interval_gcd.py
```

Expected stdout:

```text
PASS generated_legal_cases=21477 rational_projector_checks=1280 square_multiplicity_guard=B3_p11_z22
```

The checker performs:

- generated exhaustive legal prime/square/distinct-semiprime cases for `B=2,...,8` (all composite legal cases are exhaustive because for `pq<=B^6` with `p>B^2`, the larger factor is `<B^4`);
- the `Omega(d)<=2` assertion;
- exact `gcd(d,z!)` prefix identity for every generated squarefree case at multiple boundary/interior endpoints;
- open-left/closed-right interval quotient identities;
- 1,280 exact `Fraction` evaluations of the original truncated Mobius-factorial projector, checking denominator invertibility modulo legal `d` and the resulting GCD;
- an explicit square-multiplicity counterexample guarding against an invalid squarefree generalization.

A local independent execution during research produced the expected line exactly.

## 11. Closed shortcuts respected

- No prime list through `B^3` is assumed or materialized.
- No factorization of `d` is used as an input oracle to any claimed new algorithm.  Small-case factor lists in the checker are only verification certificates.
- No `Theta(B^2)` packet family and no `Theta(B^3)` candidate scan is constructed.
- The independent harmonic-factorial `B^{3/2+o(1)}` route is not renamed or reopened.
- No exact giant `L(y)/L(x)` integer is constructed and charged unit cost.
- No quantum primitive is used.
- No probabilistic or distributional hypothesis is promoted to a theorem.
- The 2026 large-order theorem is treated as an inherited subroutine improvement only; the remaining `r`/candidate coupling is kept explicit.

## 12. Theorem-status table

| Statement | Status |
|---|---|
| legal rough `d<=B^6` has `Omega(d)<=2` | **PROVED** |
| prime/square cases are polylogarithmically reducible | **PROVED** |
| squarefree prefix identity `gcd(d,z!)` | **PROVED** |
| arbitrary interval GCD is prefix quotient in squarefree case | **PROVED** |
| FAST and legal rough-semiprime factoring are exponent-equivalent | **PROVED** |
| `d<=B^5` subregime is B1 via known deterministic `n^{1/5+o(1)}` factoring | **PROVED modulo cited theorem** |
| width `B^{2+o(1)}` coarse locator suffices for B1 FAST | **PROVED modulo cited deterministic interval-divisor theorem** |
| 2026 large-order improvement alone closes FAST | **REFUTED for the frozen Harvey Prop. 4.2 realization** |
| exact B1 FAST algorithm | **OPEN** |
| exact obstruction covering both canonical taskbook candidate models | **OPEN** |

## 13. Literature used

1. David Harvey, **An exponent one-fifth algorithm for deterministic integer factorisation**, arXiv:2010.05450 (2020).  Rigorous deterministic `N^{1/5+o(1)}` factoring; Proposition 4.2 parameterized main-search cost; discussion that a full square-root speedup at Lehman's `r~N^{1/3}` would suggest `N^{1/6+o(1)}`.
2. David Harvey and Markus Hittmeir, **A log-log speedup for exponent one-fifth deterministic integer factorisation**, arXiv:2105.11105 (2021).
3. David Harvey and Markus Hittmeir, **Deterministic methods for finding elements of large multiplicative order**, arXiv:2601.11131 (2026).
4. Minkyu Kim and Jung Hee Cheon, **Computing prime divisors in an interval**, Mathematics of Computation 84 (2015), 339–354, DOI `10.1090/S0025-5718-2014-02840-8`.
5. Liqiang Peng, Yao Lu, Noboru Kunihiro, Rui Zhang, Lei Hu, **A Deterministic Algorithm for Computing Divisors in an Interval**, ACISP 2018, LNCS 10946, pp. 3–12, DOI `10.1007/978-3-319-93638-3_1`.

## 14. Recommended next route

Do not continue optimizing the Mobius coefficient vector or evaluating independent factorial blocks.  Freeze the next mathematical target as:

`ROUGH_SEMIPRIME_B2_COARSE_LOCATOR`

with the hard question:

> For `B^5<d=pq<=B^6`, `B^2<p<q`, can one deterministically output in `B^{1+o(1)}` time an additive interval of width `B^{2+o(1)}` guaranteed to contain `p`?

A positive result closes FAST by deterministic interval refinement.  A negative result should be model-specific and must identify which information channel is being restricted; no unconditional computational lower bound is claimed here.

This task return is terminal only at task scope and does not claim completion of the broader deterministic `N^{1/6}` factoring objective.
