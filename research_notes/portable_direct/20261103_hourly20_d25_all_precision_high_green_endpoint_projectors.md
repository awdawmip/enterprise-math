# D25 — Exact all-precision original-216 high-strip Green normal form and directed endpoint projectors

2026-11-03 (+08). TASK_RESEARCH author-side portable mathematics; **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Logical lane: \`chatgpt-research-hourly-enterprise-math-20260923\` (maintenance lane not used). Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, frozen scientific input pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. No native session, winning CLAIM, OPEN, Source checkpoint, Result or review is asserted by this note.

## Original source and all-precision polynomial observer

For every prime \(p=6r+1\ge7\), retain the *original* coefficient
\[
b_k=\frac{(2k)!(3k)!}{(k!)^5\,216^k},\quad
\frac{b_{k+1}}{b_k}=\frac{A(k)}{36(k+1)^3},\quad
A(k)=(2k+1)(3k+1)(3k+2)=18k^3+27k^2+13k+2.
\]
Put
\[
k_s=3r+1+s=\frac{p+1}{2}+s,\quad 0\le s\le r,\qquad Y_s=\frac{b_{k_s}}{p^2}\in\mathbb Z_{(p)}.
\]
Legendre's formula gives \(v_p(b_{k_s})=2\) for \(0\le s<r\), and \(v_p(b_{k_r})=3\). For any polynomial \(P\in\mathbb Z_{(p)}[s]\), define
\[
\mathscr D_pP(s)=\frac{A(k_s)}{36}P(s+1)-k_s^3P(s).
\tag{A1}
\]
**Exact rational telescoping theorem:**
\[
\boxed{\sum_{s=0}^{r-1}(\mathscr D_pP)(s)Y_s
=k_r^3P(r)Y_r-k_0^3P(0)Y_0.}\tag{A2}
\]
Proof: the original coefficient recurrence gives \((k_s+1)^3Y_{s+1}=A(k_s)Y_s/36\), so each summand is the forward difference of \(k_s^3P(s)Y_s\). The sum telescopes without approximation.

**All-digit rank-three theorem.** For every \(N\ge1\), \(R_N=\mathbb Z/p^N\mathbb Z\), every polynomial weight \(W\in R_N[s]\) admits a unique decomposition
\[
\boxed{W=\mathscr D_pP+d_0+d_1s+d_2s^2,\qquad
R_N[s]=\mathscr D_p(R_N[s])\oplus R_N\{1,s,s^2\}.}\tag{A3}
\]
It also holds over \(\mathbb Z_{(p)}[s]\). Indeed, \(A(k_s)/36\) and \(k_s^3\) have respective leading coefficients \(1/2\) and \(1\), so the leading term of \(\mathscr D_pP\), for any nonzero degree-\(m\) \(P\) with leading coefficient \(a\), is \(-a s^{m+3}/2\). Multiplication by \(-1/2\) is a unit in either ring and preserves nonzero leading coefficients. Repeated leading-term cancellation produces a degree-at-most-2 remainder and the same leading-term property proves uniqueness, including when \(R_N\) has zero divisors.

Define \(M_j=\sum_{s=0}^{r-1}s^jY_s\). Combining (A2)–(A3) gives an **exact original-source observer reconstruction**:
\[
\boxed{\sum_{s=0}^{r-1}W(s)Y_s=
d_0M_0+d_1M_1+d_2M_2+k_r^3P(r)Y_r-k_0^3P(0)Y_0.}\tag{A4}
\]
In particular, \(P=1\), \(K_j=\sum k_s^jY_s\), yields
\[
\boxed{-18K_3+27K_2+13K_1+2K_0=36(k_r^3Y_r-k_0^3Y_0).}\tag{A5}
\]
The physical signed high strip is already in the low-degree remainder:
\[
\boxed{\frac{H_2(p)}{p^2}=
\sum_{s=0}^{r-1}(6k_s+1)Y_s=(3p+4)M_0+6M_1.}\tag{A6}
\]

## Independent directed endpoint projectors

Since \(1\le r<p\), \(r^{-1}\in\mathbb Z_{(p)}\). The explicit polynomials
\[
P_{\rm in}(s)=1-\frac{s}{r},\qquad P_{\rm out}(s)=\frac{s}{r}
\]
have complementary endpoint values. Put \(W_{\rm in/out}=\mathscr D_pP_{\rm in/out}\); explicitly
\[
W_{\rm out}(s)=\frac{A(k_s)(s+1)/36-k_s^3s}{r},\qquad
W_{\rm in}(s)=\frac{A(k_s)}{36}-k_s^3-W_{\rm out}(s).
\]
They are p-integral **degree-four polynomial weights** satisfying the exact, separately addressable flux certificates
\[
\boxed{\sum_{s=0}^{r-1}W_{\rm in}(s)Y_s=-k_0^3Y_0,}
\qquad
\boxed{\sum_{s=0}^{r-1}W_{\rm out}(s)Y_s=k_r^3Y_r.}\tag{B1}
\]
Proof: apply (A2) to the two complementary endpoint conditions. The formulas hold modulo \(p^N\) for every \(N\), with the original source and separate orientation.

**Comparison / BRC scope.** Earlier D25 established a global 216 polynomial Gosper three-moment form; the new contribution is its exact original *high-strip p-adic source* interface together with independent directed endpoint projectors and arbitrary precision. The earlier Hensel-lifted four-moment form at commit \`5123cbd362e87cc13edf7856e2b11ab54cfd1293\` applies to the **different** rational observer \(W(s)Y_s/(2s+3)\) modulo \(p^2\). This three-moment form applies to \(W(s)Y_s\) for polynomial \(W\), at all precisions. The preserved source fields are the original factorial coefficients, valuation, directed \(s\mapsto k_s\), declared polynomial, exact precision and typed entrance/exit endpoints; no native X6 structural promotion is claimed.

## Exact integer execution

The checked-in companion Python stdlib script uses original factorial units, verifies the source ratio, (A2), (B1), normal-form coefficient elimination and moment reconstruction for \(s^3,\ldots,s^{10}\) over \(\mathbb Z/p^4\mathbb Z\). It **actually ran and passed** for all 148 primes \(7\le p\le2000,\ p\equiv1\pmod6\), covering 22,952 high-strip positions. The expanded local checker additionally cross-checked small primes \(p\le37\) against the independent original binomial formula modulo \(p^6\). Representative residues:

| \(p\) | \(r\) | entrance flux mod \(p^4\) | exit flux mod \(p^4\) | \(H_2/p^2\bmod p\) |
|---:|---:|---:|---:|---:|
| 13 | 2 | 7295 | 25246 | 10 |
| 19 | 3 | 21152 | 66291 | 9 |
| 373 | 62 | 2860891407 | 11524594801 | 266 |

Theorems (A2)–(B1) have exact algebraic proofs. Finite testing is supplementary, not an independent review or formal native experiment.

## Next mother-objective unit / control status

Construct a genuinely \(p\)-dependent signed original-source low/middle/high Green–WZ relation using separately addressable \(2r,3r,4r\) fluxes, preserving the **actual signed interior moments** in (A6) rather than replacing them with manufactured projector weights. Evaluate exact original endpoint/residual equations at \(p=13,19,373\) before a universal conclusion. The frozen mother target \(W_{p-1}\equiv p\pmod {p^3}\) for \(p\bmod24\in\{13,19\}\) is still open.

Live authenticated Gateway 0.6.11 on 2026-11-03 reports \`UPSTREAM_CODE_REVIEW_REQUIRED\`, \`research_authority_granted=false\`, \`executor_binding_configured=false\`, and active-job quota \`5/5\`. The historical genuine-lane read-only recovery #6637 and terminal failed continuation #6638 are not replayed; support owner remains existing Enterprise Math issue #1558. This source note is **author evidence / not native Source checkpoint / UNREVIEWED / NOT_ADMITTED**.
