# D25: dual extremal-layer reflection and original fourth-digit source port

2026-11-04. TASK_RESEARCH. AUTHOR-DERIVED / EXACT SCOPED PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical conversation chatgpt-research-onhour-enterprise-math-20260923; maintenance conversation chatgpt-hourly-enterprise-math-20260921 remains separate.

Prior inputs are the already-published finite signed fourth-digit experiment, Green two-seam source grading, other Research lane's Clausen work, and Guo–Zudilin (2019)'s proved quartic V model p³ theorem. This note does not re-claim those results.

## Original coefficients and all-prime reflection theorem

For every prime p >= 5 and every 0 <= k < p, retain the **original** rational families (in the p-local rationals):

\[
a_k=\frac{(2k)!(3k)!}{(k!)^5 216^k}
=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k},
\qquad
b_k=\frac{(4k)!}{(k!)^4 2304^k}
=\frac{\binom{2k}{k}^{2}\binom{4k}{2k}}{2304^k}.
\]

Let \(m_a=\lfloor(p-1)/3\rfloor\) and \(m_b=\lfloor(p-1)/4\rfloor\). For every \(1\le k\le m_a\), \(a_k\) is a p-unit, \(v_p(a_{p-k})=3\), and

\[
\boxed{k^3a_k\,\frac{a_{p-k}}{p^3}\equiv-\frac1{18}\pmod p.}\tag{A}
\]

For every \(1\le k\le m_b\), \(b_k\) is a p-unit, \(v_p(b_{p-k})=3\), and

\[
\boxed{k^3b_k\,\frac{b_{p-k}}{p^3}\equiv-\frac1{96}\pmod p.}\tag{B}
\]

**Proof.** For \(j<p\), Legendre gives

\[
v_p(a_j)=\lfloor2j/p\rfloor+\lfloor3j/p\rfloor,\qquad
v_p(b_j)=\lfloor4j/p\rfloor.
\]

These yield low valuations 0 and reflected high valuations exactly 3 on the stated ranges. The exact rational recurrences are

\[
R_a(j)=\frac{a_{j+1}}{a_j}
=\frac{(2j+1)(3j+1)(3j+2)}{36(j+1)^3},\qquad
R_b(j)=\frac{b_{j+1}}{b_j}
=\frac{(4j+1)(4j+2)(4j+3)}{576(j+1)^3}.
\]

For \(1\le k<m_a\), respectively \(1\le k<m_b\), direct reflected index substitution \(j=p-k-1\) (all inverted factors are p-units on these intervals) gives

\[
\frac{R_a(k)}{R_a(p-k-1)}
\equiv\frac{k^3}{(k+1)^3}\pmod p,\qquad
\frac{R_b(k)}{R_b(p-k-1)}
\equiv\frac{k^3}{(k+1)^3}\pmod p.
\]

Therefore the two expressions in (A), (B) are independently **constant in k**, since their successive quotient is 1 mod p. It remains to evaluate them at k=1. Wilson's theorem and p-block products give

\[
(2p-2)!/p\equiv-1,\quad
(3p-3)!/p^2\equiv-1,\quad
(4p-4)!/p^3\equiv-1\pmod p.
\]

For the second, the removed multiples p and 2p contribute 2, while the remaining p-free blocks contribute -1/2; for the third, multiples p,2p,3p contribute 6, and the p-free product -1/6. Using \((p-1)!\equiv-1\) and Fermat \((216)^{p-1}\equiv(2304)^{p-1}\equiv1\pmod p\) gives

\[
a_{p-1}/p^3\equiv b_{p-1}/p^3\equiv-1\pmod p.
\]

Finally \(a_1=1/18\) and \(b_1=1/96\), which yields (A),(B) for every p >= 5, including p=5 and p=7. QED.

## Full original fourth-digit high layer recovered from low-unit coefficients

Define the exact complete original valuation-three layers

\[
A_3=\sum_{n=p-m_a}^{p-1}(6n+1)a_n,\qquad
B_3=\sum_{n=p-m_b}^{p-1}(8n+1)b_n.
\]

Reindex \(n=p-k\) and apply (A),(B) with weights reduced mod p. **For every prime p >= 5**:

\[
\boxed{\frac{A_3}{p^3}\equiv-\frac1{18}
\sum_{k=1}^{m_a}\frac{1-6k}{k^3a_k}\pmod p},\qquad
\boxed{\frac{B_3}{p^3}\equiv-\frac1{96}
\sum_{k=1}^{m_b}\frac{1-8k}{k^3b_k}\pmod p.}\tag{C}
\]

Each inverse is legal by the unit ranges already proved. The BRC observer retains original ordered index pairs \((k,p-k)\), exact p-adic valuation, sign-weighted residue and the future operation (low-to-high reflection); original source identities are not quotient-erased.

Let \(W_p=\sum_{k=0}^{p-1}(6k+1)a_k\), \(V_p=\sum_{k=0}^{p-1}(8k+1)b_k\), \(\varepsilon_p=(-3/p)\), and \(J_p=W_p-2V_p+\varepsilon_pp\). Let \(H_a=A_3/p^3\bmod p\), \(H_b=B_3/p^3\bmod p\) and the lower-valuation bulk

\[
J_{\rm bulk}=(W_p-A_3)-2(V_p-B_3)+\varepsilon_pp.
\]

An **unconditional** exact source identity now follows for every p >= 5:

\[
\boxed{J_p\equiv J_{\rm bulk}+p^3(H_a-2H_b)\pmod{p^4}.}\tag{D}
\]

The global relation \(J_p\equiv0\pmod{p^4}\) remains a conjecture. A normalized bulk digit \(J_{\rm bulk}/p^3\bmod p\) is used only when its divisibility is actually established; this holds in the stated finite checks. The frozen mother objective is the original \(W_p-V_p\equiv0\pmod{p^3}\) and \(\Delta_p-R_p\equiv0\pmod p\) for p congruent to 13,19 modulo 24; the fourth-digit path is optional.

## Executed exact validation and examples

A companion Python standard-library script, d25_dual_extremal_reflection_checker_20261104.py, **actually executed** on all 667 primes from 5 to 5000, with original coefficient rational recurrences in Z/p^4. There were 515,709 a-source and 386,697 b-source low/high reflected-pair checks: **902,406 exact pair checks passed**, zero failures. Formula (C), exact decomposition (D), and finite signed J=0 mod p^4 checks passed for 667/667. Original integer binomial formulas independently rebuilt every coefficient at p=5,7,11,13,19,97,373 (also all passed).

| p | H_a | H_b | signed H_a-2H_b mod p | J_bulk/p³ mod p, finite sample |
|---:|---:|---:|---:|---:|
| 11 | 6 | 1 | 4 | 7 |
| 13 | 5 | 6 | 6 | 7 |
| 19 | 4 | 16 | 10 | 9 |
| 97 | 44 | 68 | 5 | 92 |
| 373 | 278 | 119 | 40 | 333 |

The last two columns sum to zero mod p in these finite cases. Signed high is nonzero at **665 of the 667 tested primes**, with observed exceptions p=107,1289. For original p=373, the signed high fourth digit is 40 and the lower-valuation bulk is 333. This is a genuine nonzero cross-source compensation.

## Native recovery, remaining obligations, exact continuation

The original onhour request research-onhour-20261031-0205-dispatch-r15 was read at its own bridge Issue #6633: **COMPLETE/FAILED, UPSTREAM_CODE_REVIEW_REQUIRED**; it was not NO_DISPATCH and was not resubmitted. Historical recovery_status #6632, dated 2026-10-30, recorded an active Researcher session MCP-de3e5bafb24f43f4a5e6285e7601676a but no own claim/run or pending mutation. This old read-only projection gives no current Source execution ownership. Three old staging uploads were neutrally preserved in #6634-6636; they were not incorporated into any accepted Result. No new role-bound session, CLAIM, open, checkpoint, HANDOFF or Result was issued. Existing control support is #1558.

The **same-original-class** p=373 native H0/B0 divided-power [X]U modulo 139129, module rank, semilinear Frobenius direction and basis normalization, odd signed observer, and independent replay remain UNEXECUTED / PENDING_OWNER at support Issue #1559; this mathematical finite-modular port does not replace that native experiment.

**Next smallest scientific unit:** seek an independently checkable terminating Green/WZ/Clausen certificate for the **original W216−V2304 mod p³** cancellation. Use (C) as an optional mechanism discriminator for higher precision, preserving exact original sources, signed terms and boundary; test p=11,13,19,97,373. The parent D24 second digit remains open; no formal mathematical admission or new scheduler was created.
