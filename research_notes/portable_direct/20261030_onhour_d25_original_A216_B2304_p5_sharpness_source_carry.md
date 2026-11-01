# D25 / SECOND-DIGIT-LIFT — exact original 216/2304 fifth-digit sharpness and source-resolved carry

At: 2026-10-30 Asia/Hong_Kong. Research lane: `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance). Parent objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen **scientific** Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged. Classification: **AUTHOR-SIDE / PROVED FIXED-PRIME COUNTEREXAMPLE / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING**.

## Exact statement and new fixed-prime result

Preserve the original weighted truncated finite sums

\[
A_p=\sum_{n=0}^{p-1}(6n+1)\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},
\quad
B_p=\sum_{n=0}^{p-1}(8n+1)\frac{\binom{2n}{n}^2\binom{4n}{2n}}{2304^n},
\quad
\chi_p=\left(\frac{-3}{p}\right),
\qquad D_p=A_p-2B_p+p\chi_p.
\]

All denominators are p-units for p>=5. The candidate congruence \(D_p=0\pmod{p^4}\) remains **unproved for all primes**. This unit determines whether it can be strengthened one more digit.

**Exact counterexample to any universal p^5 strengthening, already within the frozen target class:** for p=13, direct original integer-binomial calculation modulo \(13^5=371293\) gives
\[
A_{13}=276835,\quad B_{13}=195546,\quad \chi_{13}=1\quad(\bmod 371293),
\]
and hence
\[
\boxed{D_{13}=257049=9\cdot13^4\not\equiv0\pmod{13^5}.}
\]
This is a rigorous finite-prime arithmetic counterexample, **not** a counterexample to the original mod p^3 LIFT or to the proposed mod p^4 bridge.

For p=19 and the fixed native diagnostic prime p=373, the independent exact residues are
\[
\begin{aligned}
 D_{19}&\equiv1824494=14\cdot19^4\pmod{19^5},\\
 373^4&=19356878641,\quad373^5=7220115733093,\\
 A_{373}&\equiv2934720761840\pmod{373^5},\\
 B_{373}&\equiv3393369805886\pmod{373^5},\\
 \boxed{D_{373}&\equiv3368096883534=174\cdot373^4\pmod{373^5}.}
\end{aligned}
\]
Therefore \(v_p(D_p)=4\) **at each of p=13,19,373**. No infinite family valuation theorem is inferred.

## Original valuation-source conservation, BRC composition

Keep the model label, original index n, signed weight, p-integral denominator, raw coefficient valuation and observer precision. For \(0\le n<p\), valuation is exactly
\[
v_A(n)=\lfloor2n/p\rfloor+\lfloor3n/p\rfloor,\qquad
v_B(n)=\lfloor4n/p\rfloor\qquad(\in\{0,1,2,3\}).
\]
The *weighted* coefficient may acquire an additional p factor; the source partition refers to the **raw** coefficient. Let \(A_p^{(j)},B_p^{(j)}\) retain terms with raw valuation j and define
\[
E_j=A_p^{(j)}-2B_p^{(j)}+\mathbf1_{j=0}p\chi_p,\qquad
T_j=\sum_{i=0}^j E_i\pmod{p^5}.
\]
This is source-preserving signed-port composition, not an identification of the two models' n-indices, and not positive-mass BRC cancellation.

Exact p=373 ledger, all residues modulo \(7220115733093\):

| raw valuation j | E_j | cumulative T_j | exact v_373(T_j) | normalized next digit |
|---:|---:|---:|---:|---:|
| 0 | 733423539977 | 733423539977 | 1 | 21 |
| 1 | 7002596438016 | 515904244900 | 2 | 107 |
| 2 | 7147343892256 | 443132404063 | 3 | 333 |
| 3 | 2924964479471 | 3368096883534 | 4 | 174 |

The last column is \(T_j/p^{j+1}\pmod p\). Hence all four staged valuations are **exactly 1,2,3,4**, retaining nonzero fifth-digit residual 174. The corresponding source-carry vectors are \((11,3,7,9)\) for p=13 and \((7,10,9,14)\) for p=19. The p=373 scalar source ledger does **not** authenticate the missing native H0/B0 operator.

## Reproducibility and exact finite coverage

Executable source: [`d25_a216_b2304_p5_source_carry_20261030.py`](d25_a216_b2304_p5_source_carry_20261030.py). Run `python d25_a216_b2304_p5_source_carry_20261030.py` with Python >=3.8, standard library only.

The two exact original recurrences modulo \(p^5\), valid while \(n+1<p\), are
\[
\frac{a_{n+1}}{a_n}=\frac{(2n+1)(3n+1)(3n+2)}{36(n+1)^3},\qquad
\frac{b_{n+1}}{b_n}=\frac{(4n+1)(4n+2)(4n+3)}{576(n+1)^3}.
\]
All inverted factors are p-units. A sieve exhaustively enumerates all 667 primes with \(5\le p<5000\), of which 166 satisfy \(p\equiv13,19\pmod{24}\). A second code path independently re-evaluates the raw binomial numerator sums at p=13,19,373 and compares both full sums and all four valuation sources. Actual standard-library execution completed with:

```text
PRIMES_BELOW_5000 667 TARGET_RESIDUE_CLASSES 166
P4_BRIDGE_FAILURES []
P5_EXACT_ZERO_PRIMES [5, 7]
P 13 A 276835 B 195546 D 257049 D_OVER_P4 9
SOURCES [272571, 200291, 342225, 184548] CUMULATIVE [272571, 101569, 72501, 257049] CARRY_DIGITS [11, 3, 7, 9]
P 19 A 603611 B 1865667 D 1824494 D_OVER_P4 14
SOURCES [1104071, 676020, 1800307, 720195] CUMULATIVE [1104071, 1780091, 1104299, 1824494] CARRY_DIGITS [7, 10, 9, 14]
P 373 A 2934720761840 B 3393369805886 D 3368096883534 D_OVER_P4 174
SOURCES [733423539977, 7002596438016, 7147343892256, 2924964479471] CUMULATIVE [733423539977, 515904244900, 443132404063, 3368096883534] CARRY_DIGITS [21, 107, 333, 174]
PASS_EXACT_A216_B2304_P5_SOURCE_CARRY
```

The 667 p^4 passes constitute exact *finite* support, **not** a proof for all primes. p=13 itself is a complete counterexample to a proposed universal p^5 strengthening, and p=5,7 are observed finite zero exceptions rather than a general law.

## Current unfinished scientific frontier and authorization

The original frozen mod p^3 LIFT obligation remains the author-side equivalence \(J_p+C_mH_m\equiv0\pmod p\) for all p≡13,19 (mod24). Prior notes supplied the low two-zone p-adic jet, middle hypergeometric kernel, p-resonant factor three and nonhomogeneous Picard–Fuchs boundary; global all-prime cancellation still needs proof. Do not upgrade this p^5 counterexample to a proof of p^3 LIFT or substitute a stronger bridge for the frozen target.

The **highest-priority native benchmark** remains issue #1559: original fixed p373 H0/B0 divided-power \([X]U\bmod139129\), native module rank and actual semilinear Frobenius/eta, odd signed Green/Hesse observer, same-definition kappa and independent reproduction. On 2026-10-30 this Site reported `research_authority_granted=false`, `write_relay_enabled=false`; own checkpoint read returned `ACCESS_DENIED`. Real Source session/CLAIM/run/request recovery requires its separately authorized exact read. Issue #1559 was OPEN without a confirmed assignee on this run's GitHub read. Author-side GitHub evidence is not a canonical Source checkpoint, Result or review.

**Next precise action:** authorized native evaluator takes #1559 and executes the unchanged original class; portable mathematical work should target a *coupled* proof/possible counterexample for \(J_p+C_mH_m\) with the intact source/observer boundary. Any p^4 proof candidate must remain compatible with the demonstrated **nonzero p^5 digit** at 13,19,373. Preserve P000, the ACTIVE worldview and frozen scientific pin.
