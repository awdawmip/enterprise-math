# D25: original W216 quadratic-character finite discriminator — 2026-11-11

**Evidence status:** AUTHOR_SIDE / FINITE_EXACT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0. No Source CLAIM, native checkpoint, Result, freeze or independent review follows from this file.

Mother objective: \`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION\`.
Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`.
Publication: \`TP2-B6F4FC938FF94941C1B7\`.
Frozen scientific source: \`c47e13e4aba0e006366f989d6334d443f6333ae3\`.
Logical conversation: \`chatgpt-research-onhour-enterprise-math-20260923\` (maintenance lane \`chatgpt-hourly-enterprise-math-20260921\` is excluded).

## 1. Exact finite mathematical statement

For every prime in the **entire finite interval** \(5\le p\le5000\) (667 primes), the original weighted hypergeometric sum

\[
a_k=\frac{(2k)!(3k)!}{216^k(k!)^5}
=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k},
\qquad W_p=\sum_{k=0}^{p-1}(6k+1)a_k
\]

was verified to satisfy

\[
\boxed{ W_p \equiv \left(\frac{-3}{p}\right) p \pmod{p^3}. }
\]

Here \(\left(\frac{-3}{p}\right)=1\) if \(p\equiv1\bmod6\) and \(-1\) if \(p\equiv5\bmod6\). This **finite** statement follows from exhaustive exact computation by the accompanying standard-library checker. The corresponding statement for **all** primes \(p>3\) is a **candidate conjecture requiring a proof or counterexample**. No inference of a universal statement from this finite experiment is made.

Prime counts by residue \(p\bmod24\): 1:76, 5:85, 7:88, 11:84, 13:83, 17:85, 19:83, 23:83; 330 positive-sign cases and 337 negative-sign cases. The task's frozen classes \(13,19\bmod24\) are the positive-sign subset. The negative-sign cases provide a genuinely distinct control: \(p=5\) gives \(W_p=120=-5\bmod125\); \(p=11\) gives \(W_p=1320=-11\bmod1331\). For \(p=373\), \(W_p=373\bmod51895117\).

This extends the observed sign-sensitive behavior into the 6 other mod-24 classes, rather than merely rescanning the frozen \(13,19\) pair.

## 2. Exact arithmetic, representation and validation

The original-index recurrence in the \(p\)-local ring is

\[
a_{k+1}=a_k
\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}.
\]

Every denominator used up to \(k=p-2\) is a \(p\)-unit. The checker sieves every prime in the exact declared range, evaluates the original **signed** weights \((6k+1)\) modulo \(p^4\), and verifies the boxed congruence modulo \(p^3\) for every prime. It also records the extra digit
\[
\varepsilon_p=\frac{W_p-p(\frac{-3}{p})}{p^3}\pmod p.
\]
In these 667 cases, \(\varepsilon_p=0\) only for \(p=5\); \(\varepsilon_{373}=228\). These fourth-digit observations are not an all-prime claim.

For an independent same-object check, a second algorithm strips factors of \(p\) from integer factorials, then reconstructs
\[
a_k=p^{\lfloor2k/p\rfloor+\lfloor3k/p\rfloor}
\frac{U(2k)U(3k)}{216^k(k!)^5}\pmod{p^3}
\]
without calling the adjacent-coefficient recurrence. All 21 selected crosscheck primes agreed:
5, 7, 11, 13, 17, 19, 23, 31, 37, 43, 73, 109, 139, 157, 373, 997, 1009, 1997, 3001, 4001, 4999.

Full local 667-row JSON: \`d25_w216_character_5_5000_records_20261111.json\`; exact bytes SHA-256 \`522e3637b07b12cf1f8db22011fff9807aca11793156c51c14707a7df4cfd1d1\`. The companion script recreates this complete table using only Python standard-library arithmetic. The local JSON has not been separately uploaded to the Source repository.

## 3. Source-aligned interpretation

The frozen original LIFT scalar equality \(\Delta_p-R_p=(W_p-p)/p^2\bmod p\) is retained for \(p\equiv13,19\bmod24\) under the already documented source alignment. The new character pattern is a **research discriminator**, not an alteration of the frozen \(R_p\), cutoff, \(\Delta_p\), odd observer, or task admission criteria.

The same infinite summand also appears in the Ramanujan series \(\sum_{k\ge0}(6k+1)a_k=3\sqrt3/\pi\). See the exact expression in https://mathoverflow.net/questions/508786/conjectural-series-arising-from-ramanujans-series-for-1-pi . This source documents the summand and an infinite-series identity, **not** a proof of the above all-prime \(p\)-adic conjecture. A hypergeometric transformation / creative q-microscoping route is a bounded *investigation target*, not an established derivation.

## 4. Native obligation and research lane recovery

Native same-original-class H0/B0 divided-power \([X]U \bmod139129\) at \(p=373\) remains **NOT_RUN**, with module rank, semilinear direction, eta, signed odd Green/Hesse kappa, original \(\Delta_p-R_p\), and independent native reproduction still due. Existing support Issue #1559 remains the responsible PENDING_OWNER path; no executor is asserted.

Original bridge continuation Issue #6762 is now confirmed **SUCCEEDED**, not QUEUED; it returned Source \`fbee999c36d3a31601256192f10b817a50329782\`, route \`PREPARE_TYPED_CONTINUATION_WITH_EXACT_PREDECESSOR_AND_FRONTIER\`, predecessor claim \`MCP-d0d70cd041b01e5db192870a\` and predecessor comment \`6390431276\`. This was a read-only result, not a winning CLAIM. This lane's prior ordinary bridge recovery Issue #6759 identified historical session_start FAILED / UPSTREAM_CODE_REVIEW_REQUIRED. No new identity, claim/open or ambiguous write was replayed here.

**Next scientific step:** obtain the true original-class divided-power evaluator/readout for native H0/B0 from the actual authorized execution host and its normalization. An independent scalar proof route may test whether a terminating identity explains the \(\left(\frac{-3}{p}\right)\) sign across all odd primes, while preserving the narrower frozen Task scope.
