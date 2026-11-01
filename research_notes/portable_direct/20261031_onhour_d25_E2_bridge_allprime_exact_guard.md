# D25 — Signed 216 / Van Hamme E.2 bridge: exact finite evidence and fourth-digit boundary

Research date: 2026-10-31 (Asia/Hong_Kong). Classification: AUTHOR-SIDE / PROVED E.2 TERMINATION-TAIL LEMMA / EXECUTED 667-PRIME EXACT CHECK / EXPLICIT p^4 BRIDGE COUNTEREXAMPLES / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. **The modular 216↔E.2 bridge is a candidate, not a proved universal congruence.**

Mother objective: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3; task's original target remains p ≡ 13,19 (mod 24) and p^3. Author lane chatgpt-research-onhour-enterprise-math-20260923 (not maintenance). P000 ACTIVE_LOCKED unchanged.

## 1. Exact arithmetic objects

For p>3 prime, keep the *original* weighted 216 quantity

$$
A_p=\sum_{n=0}^{p-1}(6n+1)
\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
=\sum_{n=0}^{p-1}(6n+1)\,
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3\,2^n}.
$$

The unit-denominator coefficient a_n satisfies the exact rational recurrence

$$
a_0=1,\qquad
\frac{a_{n+1}}{a_n}
=\frac{(2n+1)(3n+1)(3n+2)}{36(n+1)^3}.
$$

Define the distinct **Van Hamme E.2** truncated quantity with original alternating sign:

$$
B_p=\sum_{n=0}^{N_p}(-1)^n(6n+1)
\frac{(1/3)_n^3}{(n!)^3},\qquad
N_p=\begin{cases}(p-1)/3,&p\equiv1\pmod3,\\
(2p-1)/3,&p\equiv2\pmod3.\end{cases}
$$

Its summand coefficient b_n (including (-1)^n, excluding 6n+1) obeys

$$b_0=1,\qquad b_{n+1}/b_n=-(3n+1)^3/[27(n+1)^3].$$

These are two *different* hypergeometric sources. Equality of truncated sums is not assumed.

## 2. Proved finite-support p-adic lemma

**Lemma.** For each prime p>3 and all N_p<n<p,
$$v_p\left((1/3)_n^3/(n!)^3\right)=3.$$
Consequently extending B_p's summation to n=p-1 does not change B_p modulo p^3.

Proof. For n<p, n! is a p-unit. The ordered product (1/3)_n contains exactly one factor divisible by p. If p≡1 mod3 that factor is (1+3r)/3=p/3 at r=(p-1)/3=N_p; if p≡2 mod3 it is 2p/3 at r=(2p-1)/3=N_p. The factor first occurs at n=N_p+1. Every other factor in the range 0≤r<p is a p-unit, since 3r+1 takes values in [1,3p-2] and no other multiple of p has remainder 1 mod3 in this interval. Cubing gives valuation exactly 3. This is a general theorem about the E.2 source, not a theorem about A_p.

## 3. Known theorem versus newly tested bridge

Existing published Van Hamme E.2 supercongruences, proved by Swisher and discussed by Guo–Schlosser (2023), give, at the indicated terminal index,

$$
B_p\equiv
\begin{cases}p,&p\equiv1\pmod3,\\-2p,&p\equiv2\pmod3
\end{cases}
\pmod{p^3}.
$$

Reference: V. J. W. Guo and M. J. Schlosser, *New q-Analogues of Van Hamme's (E.2) Supercongruence and of a Supercongruence by Swisher*, Results in Mathematics 78, 105 (2023), DOI 10.1007/s00025-023-01885-8, https://link.springer.com/article/10.1007/s00025-023-01885-8. The present author did not independently re-prove that published theorem.

**Candidate bridge (OPEN):**

$$
A_p\stackrel{?}{\equiv}
\begin{cases}B_p,&p\equiv1\pmod3,\\
2^{-1}B_p,&p\equiv2\pmod3
\end{cases}
\pmod{p^3}.
$$

The prime-to-3 factor 2 is inverted in Z/p^3Z. If the p≡1 mod3 branch is proved, then by the cited E.2 theorem the *frozen* task's A_p≡p (mod p^3), p≡13,19 (mod24), follows directly. This is a conditional implication. Neither the bridge nor the 216 all-prime signed supercongruence is promoted as a theorem here.

## 4. Executed, independently reproducible finite check

Exactly executed with Python standard-library integer modular arithmetic:

research_notes/portable_direct/d25_van_hamme_E2_216_crosscheck_20261031.py

Immutable program commit 989600dc551435393ccea5e03a81eac1e83cb995, blob baa30bee12e450528e6189769f6796f252860868.

The program exhaustively enumerates all **667 primes 5≤p<5000**, including 330 with p≡1 mod3, 337 with p≡2 mod3, and the 166 frozen p≡13,19 mod24. For every prime it independently calculates A_p and B_p by their *different* rational recurrences using exact inverses modulo p^3, and verifies:

$$
A_p\equiv p\,\left(\frac{-3}{p}\right)\pmod{p^3},
\qquad
A_p\equiv B_p\ (p\equiv1\pmod3),\quad
2A_p\equiv B_p\ (p\equiv2\pmod3).
$$

Here the Kronecker/Legendre symbol (-3/p) is +1 on p≡1 mod3 and -1 on p≡2 mod3. Additionally, the original integer-binomial 216 formula is separately evaluated at 11 diagnostic primes 5,7,11,13,19,31,37,43,67,73,373 and agrees exactly modulo p^3. These are explicit finite results, **not** a proof for infinitely many primes.

Execution summary:

- EXACT_PASS primes 5<=p<5000: 667.
- p mod3 1: 330; p mod3 2: 337; frozen p mod24=13,19: 166.
- Original integer binomial cross-check samples: 11 exact independent evaluations.

## 5. A proved limitation at the next digit

The candidate bridge **does not** generally extend to p^4. Independent exact calculations give

$$
A_{13}\equiv19786\pmod{13^4},\qquad
B_{13}\equiv26377\pmod{13^4},
$$
hence
$$A_{13}-B_{13}=-3\cdot13^3\not\equiv0\pmod{13^4}.$$

Likewise
$$A_{19}-B_{19}=-6\cdot19^3\pmod{19^4},$$
and at the frozen diagnostic p=373,
$$A_{373}-B_{373}\equiv170\cdot373^3\pmod{373^4}.$$

This is a strict fixed-prime *counterexample* to the fourth-digit upgrade, not to the p^3 bridge or the original LIFT. It identifies p^3 as an essential precision boundary for any sought source transformation.

## 6. Typed provenance, research dependency and next action

The original 216 term index, 216 denominator, factor (6n+1), and entire upper range 0≤n<p remain fixed. The E.2 object has its own alternating sign, upper parameters and exact terminal index N_p. Their observed scalar agreement modulo p^3 is an observer-level comparison. In BRC terms this only licenses a quotient for this scalar arithmetic readout *once the bridge is proved*; it does not silently identify original sources, native H0/B0, X6 coordinates, odd Green/Hesse, κ or Frobenius. No synthetic native axes or observer replacement are introduced.

**Next smallest mathematical obligation:** obtain a source-typed, fully checked hypergeometric/WZ (or modular transformation with controlled truncation error) proof of A_p-B_p∈p^3 Z_p for p≡13,19 mod24, preserving the previous eleven Euler–Clausen ports at any step that divides by p^2. First use the p≡1 branch alone; the wider p≡2 observation is exploratory and does not change the frozen target. Search known E.2 quadratic transformations before introducing new auxiliary constraints. p^4 equality is excluded by the explicit examples above.

**Higher-priority native obligation preserved:** awdawmip/enterprise-math#1559 (H0/B0 divided-power [X]U mod139129 at p373, original module rank, semilinear Frobenius direction/eta, signed odd Green/Hesse, κ and independent acceptance). At the latest checked Issue state it is OPEN, without a confirmed executor. The native acceptance requirements stay intact; this scalar bridge program has not executed them. The executor path is a real authorized native owner/evaluator under Source, not the author-side arithmetic loop.

**Control / immutable frontier:** recovery request research-onhour-20261031-0202-recovery-r15 in awdawmip/kimi-query-bridge#6632 reported local active own Researcher session MCP-de3e5bafb24f43f4a5e6285e7601676a, no own claim/run, source_authority_verified=false and no pending request. Fresh dispatch research-onhour-20261031-0205-dispatch-r15 (#6633) returned FAILED / UPSTREAM_CODE_REVIEW_REQUIRED. This is not NO_DISPATCH and no replay/new ID is authorized for that same failed effect. Neutral historical staging SD-d7c23e7984c2ddaac60a remains source-separated. Source write permission must be actually granted and code review deployed before new native recovery/dispatch; this author-side Git file gives no CLAIM, checkpoint, accepted Result or Driver review.

Author-side document classification remains UNREVIEWED / NOT_ADMITTED; formal Source checkpoint and activity registration are SYNC_DEBT. No scheduler, workflow, protected worldview or scientific pin was modified.
