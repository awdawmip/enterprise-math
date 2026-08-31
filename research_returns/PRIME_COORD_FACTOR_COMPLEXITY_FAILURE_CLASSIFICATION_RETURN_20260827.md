# Prime Coordinate Factorization Complexity and Failure Classification — Research Return

Status: `FROZEN / AWAITING DRIVER REVIEW`  
Task: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION`  
Publication: `TP2-8F7443BCAF2BC5243574`  
Researcher-ID: `EM-PCF7R-8595E3`  
Claim: `chatgpt-pcf7-20260831-1028-8595e3`  
Execution branch: `research/prime-coord-factor-complexity-failure-classification-em-pcf7r-8595e3`  
Base: `d94620f2f6fc8799811c648e0cc1fbc7bb4908b7`  
Frozen: `2026-08-31`

## 0. Hard-target disposition

Hard target: `FACTOR_ALGORITHM_COMPLEXITY_AND_FAILURE_CLASSIFIED`.

Disposition: `ACHIEVED`.

The accepted dependency surface supports two load-bearing algorithmic objects:

1. the factor-blind fixed-public-prefix p-adic/GCD bridge, whose observable reduces to gcd against an input-independent integer \(F_L\);
2. the accepted N-only valuation-wall streaming extractor for distinct odd semiprimes \(N=pq\), \(3<p<q\).

PCF5/PCF6 objects still awaiting Driver acceptance are not promoted into this return. The later valuation-wall compression work is recorded only as pending-control supplementary evidence and is not used to change the accepted-scope verdict.

### Frozen primary verdicts

| Candidate | Primary verdict | Reason |
|---|---|---|
| Fixed-public-prefix / fixed-support GCD bridge | `SUCCESS_PROBABILITY_NOT_LOWER_BOUNDED` | For every fixed finite factor-independent seed support there are infinitely many semiprimes with gcd 1 for every seed; amplification is exactly powerless when \(\alpha_N=0\). |
| N-only valuation-wall streaming extractor | `SQRT_SCALE_OR_WORSE_PROVED` | It is deterministic and universal on the promised semiprime domain, but the accepted streaming realization performs \(\Theta(p)\) recurrence work; balanced \(p=\Theta(\sqrt N)\) gives square-root scale in \(N\), exponential in input bit length. |
| Portfolio | `COMPLEXITY_FRONTIER_FROZEN` | Correctness and complexity separate cleanly: the cheap fixed-prefix probe has no uniform success floor; the universal N-only splitter has no accepted asymptotic speedup over smallest-factor-scale trial division. |

No `POLYNOMIAL_OR_SUBEXPONENTIAL_BOUND_PROVED` or `STRICT_SUB_SQRT_BOUND_PROVED` verdict is supported by the presently accepted dependency surface.

---

## 1. Cost model

Let
\[
n=\lceil \log_2 N\rceil,
\]
and let \(M(n)\) be the bit cost of multiplying two \(n\)-bit integers. GCD and extended-GCD/inversion are charged \(O(M(n)\log n)\). Memory is peak working memory in bits. Finite benchmark counters are retained only as regression evidence; they are not treated as interchangeable units across algorithms.

All comparisons below use this one metric:

- number and size of integer/modular arithmetic operations;
- peak working memory;
- input-dependent preprocessing;
- seed/probe count;
- exact success model.

One-time data independent of \(N\) is separated from online work.

---

## 2. Candidate A — fixed-public-prefix p-adic/GCD bridge

### 2.1 Exact accepted reduction

For public prefix \(L\), define
\[
A_j=\binom{2j}{j}^2\binom{3j}{j},\qquad B_j=216^jA_j,
\]
and \(d_j=2j+1\). The accepted PCF4 reduction gives an integer \(F_L\), depending on \(L\) only, such that for \(\gcd(N,6)=1\),
\[
\gcd(G_N(L),N)=\gcd(F_L,N).
\]

Thus the online factor observable is not an N-dependent geometric evolution after normalization; it is a gcd between \(N\) and a fixed public integer.

### 2.2 Line-by-line bit cost

For one prefix \(L\):

1. Generate \(A_j,B_j\) for \(0\le j\le L\) by the exact recurrence.  
   Count: \(O(L)\) arithmetic stages.

2. Form/normalize \(F_L\).  
   Accepted dependency bound: \(F_L\) has \(O(L+\log L)\) bits, and a conservative exact-generation bound is polynomial in \(L+\log N\), e.g.
   \[
   O(L\,M(L+n)).
   \]

3. Reduce/calculate \(\gcd(F_L,N)\).  
   Online cost:
   \[
   O(M(n+L)\log(n+L)).
   \]

4. Streaming memory:
   \[
   O(n+L)
   \]
   bits.

If \(F_L\) is precomputed and cached independently of \(N\), the online probe is essentially one reduction/GCD. Therefore a fixed \(L\), or any fixed finite set of \(L\)'s, is polynomial in \(n\) per input.

That cheap per-probe cost is not a factoring complexity theorem, because success is the missing resource.

### 2.3 Exact seed-success theorem

Let \(S\) be a finite public seed set and let \(\mu\) be any probability distribution supported on \(S\). Define
\[
\alpha_N
=\mu\{L\in S:1<\gcd(F_L,N)<N\}.
\]

For \(k\) independent trials,
\[
P_N(\text{success by }k)=1-(1-\alpha_N)^k.
\]

Let
\[
\mathcal P_S=\bigcup_{L\in S}\{r\text{ prime}:r\mid F_L\}.
\]
This is finite. Choose distinct primes \(p,q>3\) outside \(\mathcal P_S\) and set \(N=pq\). Then
\[
\gcd(F_L,N)=1\qquad\forall L\in S,
\]
hence
\[
\alpha_N=0,\qquad
P_N(\text{success by }k)=0
\quad\forall k.
\]

Therefore no universal positive lower bound on success probability exists for the fixed finite factor-independent seed model, and repeated sampling from the same support cannot repair the failure.

### 2.4 Bit-budget strengthening

The same obstruction extends to any factor-independent seed family determined only by the public size parameter \(n\) whose accessible prefixes satisfy \(L\le P(n)\) for a polynomial \(P\).

There are only \(P(n)+1\) such prefix values. Each \(F_L\) has \(O(L+\log L)\) bits and therefore only \(O(L+\log L)\) distinct prime divisors. Hence the union of all prime supports reachable by such prefixes has polynomial cardinality in \(n\).

Using the classical prime-density lower bound in a dyadic interval, the number of primes of \(\Theta(n)\) bits is exponential in \(n\). For all sufficiently large \(n\), two balanced primes can therefore be chosen outside the entire reachable support, producing a balanced semiprime on which every such prefix probe returns gcd 1.

This strengthening is explicitly limited to factor-independent prefix selection controlled by \(n\). It does **not** claim a no-go for an arbitrary N-dependent rule \(L=f(N,\text{history})\); that is a different constructor class.

### 2.5 Failure atlas

- **Balanced semiprimes:** fail on infinite adversarial families outside the finite support. Under polynomial prefix budget, balanced adversarial examples also exist for all sufficiently large sizes.
- **Unbalanced semiprimes:** same support obstruction; no rescue from imbalance.
- **Near-twin factors:** the support criterion remains exact, but no infinite near-twin family theorem is imported here. Finite examples are regression-only.
- **Prime powers:** if \(p\nmid F_L\) for every allowed seed, then \(p^a\) also yields gcd 1 for every allowed seed. If \(p\mid F_L\), valuation determines whether the gcd is proper.
- **Multifactor inputs:** gcd extracts exactly the product/powers supported by \(F_L\); if all prime factors are outside support, gcd is 1; if all are supported strongly enough, gcd may be \(N\).
- **Carmichael / strong pseudoprime classes:** pseudoprime status is not the controlling variable. The exact criterion is still divisibility of prime factors into \(F_L\). No separate infinite-family theorem for these labels is asserted.
- **Synchronized sectors / equal response:** if both semiprime factors divide the same \(F_L\), the output is \(\gcd(F_L,N)=N\), which is synchronization rather than a split. The checker includes \(L=3,N=35\) as an exact finite witness.
- **Exceptional congruence classes:** all accepted exceptional behavior is absorbed into the arithmetic condition \(p\mid F_L\); no additional geometric exception is promoted.

Primary verdict: `SUCCESS_PROBABILITY_NOT_LOWER_BOUNDED`.

---

## 3. Candidate B — N-only valuation-wall streaming extractor

### 3.1 Exact accepted object

For
\[
N=pq,\qquad 3<p<q
\]
distinct odd primes, use
\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}.
\]

For prime \(r>3\) and \(0\le s<r\),
\[
v_r(A_s)=\left\lfloor\frac{2s}{r}\right\rfloor+
\left\lfloor\frac{3s}{r}\right\rfloor.
\]
Thus the first divisibility wall occurs at
\[
s=\left\lceil\frac r3\right\rceil.
\]

The accepted N-only algorithm computes residues from the public input \(N\) using
\[
\frac{A_s}{A_{s-1}}
=
\frac{6(2s-1)(3s-2)(3s-1)}{s^3},
\]
takes gcd probes at dyadic \(s\), and stops at the first nonunit gcd.

If that gcd is \(p\), factorization is done. If it is \(N\), synchronization implies \(q<2p\). Then with
\[
t=\left\lfloor \frac{\sqrt N}{3}\right\rfloor,
\]
the exact fallback checks \(A_t,A_{t+1}\) and returns \(p\).

No hidden factor is supplied to the constructor.

### 3.2 Line-by-line bit cost

A streaming modular realization avoids materializing the enormous exact integer \(A_s\).

For each recurrence step \(s\):

1. compute \(\gcd(s,N)\) as a denominator-safety/factor check;
2. form \(s^3\bmod N\);
3. compute its inverse modulo \(N\);
4. multiply by the four linear numerator factors modulo \(N\);
5. on dyadic indices, compute one extra gcd with \(N\).

All stored residues are \(<N\), so they need \(O(n)\) bits. Since \(s<p\le\sqrt N\) before the decisive wall, \(s\) also has \(O(n)\) bits.

Per step:
\[
O(M(n)\log n)
\]
conservatively, dominated by extended-GCD/inversion plus modular arithmetic.

The number of streaming steps before the first decisive dyadic wall is \(\Theta(p)\) in the worst case at the accepted implementation granularity. The synchronized fallback can be recomputed in another \(O(p)\) steps and does not change the order.

Therefore:
\[
T_{\rm wall}(N)
=
O\!\left(p\,M(n)\log n\right),
\qquad
\text{memory}=O(n).
\]

The exact unmodded integers satisfy \(\log A_s=\Theta(s)\); at \(s=\Theta(p)\) they would have exponentially many bits in \(n\) for balanced semiprimes. The modular streaming implementation is therefore essential merely to keep memory polynomial.

### 3.3 Input-family classification

- **Balanced semiprimes:** \(p=\Theta(\sqrt N)\), hence
  \[
  T_{\rm wall}=N^{1/2+o(1)}
  \]
  bit-arithmetic scale, exponential in \(n\).
- **Unbalanced semiprimes:** cost tracks the smaller factor \(p\). If \(p=N^\theta\), \(0<\theta<1/2\), then the recurrence has \(N^{\theta+o(1)}\) scale. This is smaller than \(\sqrt N\) but is not a uniform worst-case improvement.
- **Near-twin semiprimes:** included in the universal theorem; correctness remains 1, but these are the balanced regime and retain square-root-scale streaming cost.
- **Synchronized semiprimes:** not a failure. The exact \(q<2p\) certificate activates the \(t,t+1\) fallback.
- **Prime powers / multifactor / Carmichael / strong pseudoprime:** outside the accepted universal theorem. Any finite behavior is typed as descriptive only and is not extrapolated.
- **Small factors 2 or 3:** explicitly outside the theorem assumptions and should be stripped/handled separately.

On the promised semiprime domain the success probability is exactly 1; there is nothing to amplify. The bottleneck is work, not probability.

Primary verdict: `SQRT_SCALE_OR_WORSE_PROVED`.

---

## 4. Common-metric classical baseline comparison

Let \(p\) denote the smallest prime factor of a semiprime.

| Method | Arithmetic scale under the common model | Peak memory | Success qualification | Comparison |
|---|---:|---:|---|---|
| Trial division | \(O(p\,M(n))\) up to division/polylog factors | \(O(n)\) | deterministic | Same smallest-factor \(p\)-scale as the accepted streaming wall; the wall does not improve the exponent. |
| Fermat | \(T_F=(p+q)/2-\lceil\sqrt N\rceil+O(1)\) square tests; each test poly\((n)\) | \(O(n)\) | deterministic | Excellent near twins; can be much worse on unbalanced inputs. |
| Pollard rho | heuristic expected \(O(\sqrt p)\) modular steps | \(O(n)\) in low-memory variants | randomized heuristic | Balanced scale \(N^{1/4+o(1)}\), asymptotically below the accepted \(\Theta(p)\) wall traversal. |
| Pollard \(p-1\) | roughly bound-dependent modular exponent/product work through smoothness bound \(B\) | \(O(n)\) plus sieve/product state | succeeds when a factor's \(p-1\) has suitable smoothness and synchronization is avoided | Can be very fast on smooth \(p-1\); fixed \(B\) has no universal success guarantee. |
| Fixed-prefix bridge | polynomial per probe for \(L=\mathrm{poly}(n)\) | polynomial | no universal success floor | Cheap probes do not yield a uniform factoring algorithm. |
| N-only wall streaming | \(O(p\,M(n)\log n)\) | \(O(n)\) | deterministic on distinct semiprimes \(3<p<q\) | Correct, but no accepted exponent gain over trial division; worse than rho's standard heuristic scale. |

The frozen blind benchmark is retained as a finite regression surface, not as an asymptotic oracle. Its algorithm-local counters cannot be equated directly with bit operations. Consequently, benchmark successes/failures are used to detect implementation regressions and family-specific behavior, while the table above supplies the required no-tuning common complexity metric.

No finite benchmark score is used as a premise in either universal theorem.

---

## 5. Seed/amplification theorem summary

### Fixed-prefix route

For seed distribution \(\mu\) on finite \(S\):
\[
\alpha_N=\mu\{L:1<\gcd(F_L,N)<N\},
\qquad
P_k=1-(1-\alpha_N)^k.
\]

There exist infinitely many semiprimes with \(\alpha_N=0\). Thus no polynomial number of repeated trials from the same support can create a positive success probability on those inputs.

### N-only wall route

On \(N=pq\), \(3<p<q\), the deterministic algorithm succeeds with probability 1. Repetition cannot improve correctness; only a lower-cost realization of the same decisive wall could improve complexity.

---

## 6. Finite checker evidence

Task-local checker:
`research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py`

Frozen run:

- 40 exact recurrence/direct-integer checks;
- 30 fixed-prefix adversarial semiprimes with \(\alpha_N=0\);
- 60 outside-support prime-power checks;
- 10 outside-support multifactor checks;
- synchronized fixed-prefix witness \(L=3,N=35\);
- all 13,695 distinct prime pairs \(5\le p<q<1000\) factored by the public-N wall algorithm with zero failures;
- 2,996 synchronized wall cases all recovered;
- 165 neighboring-prime pairs and 4,237 \(q\ge4p\) unbalanced pairs included;
- observed modes: 10,699 dyadic direct splits, 2,925 `FALLBACK_T`, 71 `FALLBACK_T1`.

These counts are regression evidence only. The infinite support obstruction and universal semiprime splitter statements are proof-driven.

---

## 7. Theorem-ready assumption package

### Package A — fixed-prefix no-go

A1. \(\gcd(N,6)=1\).  
A2. The accepted exact reduction \(\gcd(G_N(L),N)=\gcd(F_L,N)\).  
A3. \(F_L\in\mathbb Z\) depends only on public prefix \(L\), not on hidden factors.  
A4. Seed support is fixed finite for the exact no-go theorem; the polynomial-budget strengthening additionally assumes factor-independent prefix choice controlled by \(n\) and polynomially bounded \(L\).  
A5. Standard integer arithmetic/GCD semantics.  
A6. The bit-budget strengthening uses a classical lower bound giving exponentially many \(\Theta(n)\)-bit primes.  
A7. No benchmark outcome is a theorem premise.

Formal target:
\[
\forall S\text{ finite}\;\exists^\infty pq:
\forall L\in S,\ \gcd(F_L,pq)=1.
\]

### Package B — N-only wall extractor

B1. \(N=pq\) with distinct primes \(3<p<q\).  
B2. \(A_s=(2s)!(3s)!/(s!)^5\).  
B3. For \(r>3,\ 0\le s<r\),
\[
v_r(A_s)=\lfloor2s/r\rfloor+\lfloor3s/r\rfloor.
\]
B4. Exact recurrence
\[
A_s/A_{s-1}=6(2s-1)(3s-2)(3s-1)/s^3.
\]
B5. Every denominator inverted before the decisive wall is a unit modulo \(N\), with gcd fallback if not.  
B6. Dyadic first-nonunit rule and the synchronization lemma \(g=N\Rightarrow q<2p\).  
B7. Fallback \(t=\lfloor\sqrt N/3\rfloor\), checking \(t,t+1\), returns \(p\).  
B8. Bit-cost model uses \(M(n)\), extended gcd/inversion \(O(M(n)\log n)\), streaming residues \(O(n)\) bits.  
B9. No empirical premise is needed for correctness.

Formal complexity target:
\[
T(N)=O(p\,M(n)\log n),\qquad S(N)=O(n).
\]

---

## 8. Pending-control evidence and strict boundary

The later valuation-wall complexity-compression work appears mathematically to connect the factorial/wall object to a classical block-factorial/product-tree/multipoint route with balanced scale near \(N^{1/4+o(1)}\), i.e. classical Pollard-Strassen territory rather than a new exponent.

However its current result envelope was not terminally accepted under the active result schema when this task was executed. Therefore:

- it is **not** a load-bearing premise of this PCF7 return;
- it does **not** change the accepted-scope `SQRT_SCALE_OR_WORSE_PROVED` verdict for the streaming realization;
- if later accepted, PCF7 should be reviewed only for whether Candidate B's implementation-level verdict is superseded by a classical-equivalence `STRICT_SUB_SQRT_BOUND_PROVED` result, while preserving the statement that no novel factoring exponent has been established.

PCF5/PCF6 pending returns are likewise excluded from accepted dependency synthesis.

---

## 9. Method/tool harvest

Toolbox check: the valuation reasoning already belongs to accepted
`T1_SCALE_ENUMERATION_VALUATION`.

No new global tool is proposed. The only new executable is a task-local regression checker, not a reusable enterprise tool payload.

Method harvest classification:
`NO_NEW_GLOBAL_TOOL / REUSE_T1_SCALE_ENUMERATION_VALUATION / TASK_LOCAL_CHECKER_ONLY`.

---

## 10. Smallest unresolved units

1. **N-dependent prefix rule:** the fixed-support no-go does not classify an arbitrary constructor choosing \(L=f(N,\text{history})\). Any future claim in that class must expose exact bit cost and cannot cite the fixed-support theorem as a complete rejection.
2. **Accepted sub-\(\sqrt N\) realization of the wall object:** pending current-schema review of the separate complexity-compression work. Until then the accepted implementation remains \(\Theta(p)\).
3. **Beyond-semiprime wall theorem:** prime powers and multifactor inputs are outside the accepted N-only universal proof.
4. **Pollard-rho comparison:** its \(O(\sqrt p)\) figure is a classical heuristic/expected baseline, not a deterministic theorem premise for this return.

None of these residues prevents the required classification of the currently accepted candidates.

---

## 11. Portfolio recommendation

Freeze the current portfolio as `COMPLEXITY_FRONTIER_FROZEN`.

- **Close as a generic factoring route:** fixed factor-independent finite/public-prefix seed bridge, because success has no universal positive lower bound.
- **Retain as an exact arithmetic result, not as a speedup claim:** N-only valuation-wall splitter.
- **Do not restart PCF1–PCF6:** consume them only through accepted Driver results.
- **Next highest-value control action:** terminally review/repair the separate valuation-wall complexity-compression result under the current result schema. If accepted, classify it explicitly as a classical-equivalence speedup (or refute that equivalence) before any claim of new factorization complexity is allowed.

This task itself should transition to Driver review with:
`FACTOR_ALGORITHM_COMPLEXITY_AND_FAILURE_CLASSIFIED / COMPLEXITY_FRONTIER_FROZEN`.
