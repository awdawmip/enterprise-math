# D25 — two-digit complementary-shell product and one-seed paired certificate

2026-11-06 · TASK_RESEARCH · AUTHOR-SIDE EXACT DERIVATION / FINITE INTEGER CHECKED / UNREVIEWED / NOT_ADMITTED.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7. Immutable scientific input: c47e13e4aba0e006366f989d6334d443f6333ae3.
Research conversation: chatgpt-research-onhour-enterprise-math-20260923 (separate from maintenance).

## Theorem 1 — new second digit of complementary valuation-one/two product

Let \(a_k=(2k)!(3k)!/(216^k(k!)^5)\). For **every prime \(p>3\)** and integer \(p/3<k<p/2\), write \(r=3k-p\), \(\ell=p-k\); then \(v_p(a_k)=1\), \(v_p(a_\ell)=2\). Put \(H_j=\sum_{i=1}^{j}i^{-1}\in\mathbb F_p\), \(H_0=0\), and \(q_p(216)=(216^{p-1}-1)/p\pmod p\). Then in \(\mathbb Z_{(p)}/p^2\),

\[
\boxed{
\frac{a_k}{p}\frac{a_{p-k}}{p^2}
\equiv\frac{1}{36k^3}
\bigl[1+p\bigl(2H_{2k-1}+3H_{3k-p-1}-5H_{k-1}-q_p(216)\bigr)\bigr]\pmod{p^2}.}
\tag{1}
\]

All divisions by powers of \(p\) are taken in the original rational coefficient *before* reduction; all other denominators are \(p\)-units. This refines the previous first-digit product theorem.

**Proof.** For \(0<d<p\), direct multiplication and inversion of \(p-i\) gives
\[
(p+d)!/p=(p-1)!\,d!\,(1+pH_d)\pmod{p^2},\qquad
d!(p-d)!=(-1)^{d-1}d(p-1)!(1+pH_{d-1})\pmod{p^2}.
\]
In \(a_ka_{p-k}/p^3\), the three large numerator factorials \((3k)!, (2p-2k)!, (3p-3k)!\) have precisely one \(p\)-factor each. Their residual indices are \(r=3k-p,\ p-2k,\ p-r\). Expand these three with the first identity. Pair \((2k)!\) with \((p-2k)!\), \(r!\) with \((p-r)!\), and \(k!\) with \((p-k)!\) by the second. The five factors \((p-1)!\) cancel; the overall parity is \((-1)^{3-p}=+1\). Hence
\[
\frac{a_ka_{p-k}}{p^3}\equiv
\frac{2k(3k-p)}{216^p k^5}
[1+p(H_{2k-1}+H_{r-1}-5H_{k-1}+H_r+H_{p-2k}+H_{p-r})]\pmod{p^2}.
\]
Use \(H_{p-d}\equiv H_{d-1}\pmod p\), \(H_r=H_{r-1}+1/r\); the bracket correction becomes \(2H_{2k-1}+3H_{r-1}-5H_{k-1}+1/r\). Now \(216^{-p}\equiv216^{-1}(1-pq_p(216))\) and \(2k(3k-p)/(216k^5)=(36k^3)^{-1}(1-p/(3k))\). Since \(1/r\equiv1/(3k)\pmod p\), the last two corrections cancel. This proves (1). QED.

## Theorem 2 — original-shell signed single-seed reduction

Let \(p=6m+1\), \(h=3m\), \(s=3m+1\), \(u_j=a_{h-j}/p\bmod p^2\) for \(0\le j<m\). Then each \(u_j\) is a unit and all are determined by the **single** middle seed \(u_0=a_h/p\bmod p^2\) and the exact, \(p\)-unit-denominator recursion
\[
\boxed{u_{j+1}=u_j\,\frac{36(h-j)^3}{(2h-2j-1)(3h-3j-1)(3h-3j-2)}\pmod{p^2},\quad 0\le j<m-1.}\tag{2}
\]
This is the unmodified ratio \(a_{k-1}/a_k\) with \(k=h-j\); the denominator factors are nonzero modulo \(p\) within the recurrence interval. The previously verified two-digit seed can be reused:
\[
u_0\equiv-2\varepsilon_p[1+p(3+2q_p(2)-\tfrac32 q_p(6))]\pmod{p^2},
\quad\varepsilon_p=(6/p).
\]
The upper-shell partner is now **determined solely by the middle-shell unit**:
\[
\boxed{\frac{a_{s+j}}{p^2}\equiv[36(h-j)^3u_j]^{-1}\pmod p.}\tag{3}
\]

Let \(b_k=(4k)!/(2304^k(k!)^4)\),
\(W_p=\sum_{k=0}^{p-1}(6k+1)a_k\),
\(V_h=\sum_{k=0}^{h}(8k+1)b_k\).
Set \(B_p=\sum_{k=0}^{2m}(6k+1)a_k\) and, whenever \(B_p-V_h\equiv0\pmod p\), let \(D_p=(B_p-V_h)/p\pmod{p^2}\). Then
\[
\boxed{\frac{W_p-V_h}{p}\equiv D_p+
\sum_{j=0}^{m-1}
\left[(3p-2-6j)u_j+\frac{p(6j+4)}{36(h-j)^3u_j}\right]\pmod{p^2}.}\tag{4}
\]
**Proof.** The exact factorial valuation \(v_p(a_k)=\lfloor2k/p\rfloor+\lfloor3k/p\rfloor\) (for \(k<p\)) kills the terms \(k>4m\) modulo \(p^3\). Thus \(W_p=B_p+M_p+p^2U_p\pmod{p^3}\), with the middle \(M_p=\sum_{2m<k\le3m}(6k+1)a_k\) and upper \(U_p=\sum_{3m<k\le4m}(6k+1)a_k/p^2\). Match each middle index \(h-j\) to upper \(s+j=p-(h-j)\); their actual weights are \(3p-2-6j\) and \(3p+4+6j\), respectively. Divide by \(p\), then use the mod-\(p\) reduction of (1) for the upper term and reduce the upper weight modulo \(p\). This gives (3) and (4), with all signed indices and valuation provenance intact. QED.

The open frozen scalar third-digit problem for \(p\equiv13,19\bmod24\) is now exactly the vanishing of the RHS of (4), under the already sourced 216/2304 scalar bridge. Its **uniform cancellation, including bottom \(D_p\), remains UNPROVED**. Formula (4) replaces the two-shell finite hypergeometric computation by a **single rational recurrence seeded once**. The additional correction in (1) is available for higher precision, but no native crystalline claim follows.

## Reproducible finite diagnostics

The attached integer checker works in \(\mathbb Z/p^3\) using original factorial \(p\)-unit products, not floating-point or a different H0/B0 model. It checked **166 primes \(5\le p\le997\), 12,688 admissible pairs** for (1), **80 primes \(p\equiv1\bmod6\)** for the seed, and **all 45 primes \(p\equiv13,19\bmod24\)** for the one-seed shell reconstruction and equality (4). All assertions passed (finite scope only).

Examples \((p,D_p,M_p/p,U_p,\text{paired shell})\), with \(D_p,\ M_p/p,\text{paired shell}\bmod p^2\), \(U_p\bmod p\):

| p | D | M/p | U | paired shell | D+paired mod p² |
|---:|---:|---:|---:|---:|---:|
| 13 | 59 | 149 | 10 | 110 | 0 |
| 19 | 297 | 254 | 9 | 64 | 0 |
| 67 | 2013 | 3079 | 58 | 2476 | 0 |
| 139 | 18239 | 18596 | 13 | 1082 | 0 |
| 373 | 75319 | 103721 | 266 | 63810 | 0 |

Nonzero paired witnesses: \(p=13,k=5,p-k=8\): product is \(137\bmod169\), correction digit \(12\bmod13\); \(p=19,k=7,p-k=12\): product \(85\bmod361\), correction digit \(8\bmod19\). Signed cancellation is across shells/bottom, not termwise.

## Next action and precise status

Seek an explicit creative-telescoping/adjoint for the single sequence (2) *together with* the bottom \(D_p\), respecting nonzero boundary terms. Start with \(p=13,19\) signed endpoints, then try general \(p\equiv13,19\bmod24\). Current Source request onhour11-20261106-0357-d25-exact-continuation was reconciled by exact read as SUCCEEDED / execution_authorized=false. New read-only request onhour11-20261106-0504-d25-readonly-cont was RUNNING at last read; retain the same request, no duplicate. Historical researcher metadata does not supply a private session, current claim/run, or acceptance. No native fixed 373 H0/B0 divided-power [X]U, semilinear eta/kappa, original odd Green/Hesse diagnostic or independent verification was executed here; support issue #1559 remains an independent unmet obligation.
