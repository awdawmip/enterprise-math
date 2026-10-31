# D25 — Frobenius coefficient plateau and the second-digit Green scalar defect

2026-10-31. Author-side TASK_RESEARCH lane \`chatgpt-research-hourly-enterprise-math-20260923\`; logical lane distinct from maintenance and the on-hour Research lane. Parent: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; task publication \`TP2-B6F4FC938FF94941C1B7\`. Scientific Source pin: \`c47e13e4aba0e006366f989d6334d443f6333ae3\` (NOT moved by current control HEAD). P000 ACTIVE is unaffected. **AUTHOR-DERIVED / EXACT-ALGEBRA / EXACT-MODULAR-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is external finite-field/p-adic mathematics, neither a native H0/B0 experiment nor an accepted all-prime D25/LIFT proof.

## Reused exact inputs (not new authorship)

The hourly split-Green note \`20261031_hourly_d25_split_green_log_residue_18.md\` (Enterprise Math commit \`5a19591c6841efd21acd1bba1b123d2d90ab66ff\`) gives, for \(p=6\ell+1\) prime, \(M=3\ell\),
\[
G_\ell(z)=\sum_{i=0}^{\ell}{\ell\choose i}{2\ell\choose i}z^i,\quad
S_\ell=\sum_{i=0}^{\ell}{\ell\choose i}{2\ell\choose i}{p-1+i\choose M},
\quad \Gamma_\ell=\frac{(-1)^\ell}{18S_\ell}.
\]
The separate on-hour note \`20261031_onhour_d25_terminal_gamma_second_digit_harmonic.md\` (commit \`cfa1e3fd82e2780a8aefe2ff0414e6bfaf15fc55\`) proves, for
\[
\mathcal H_\ell=-\sum_{j=1}^M\frac1j+
\sum_{i=1}^{\ell}(-1)^i
\frac{\binom{\ell}{i}\binom{2\ell}{i}}{i\binom{M}{i}}\in\mathbb Z_{(p)},
\]
that \(S_\ell\equiv(-1)^\ell(1+p\mathcal H_\ell)\pmod{p^2}\), hence
\[
\Gamma_\ell-\frac1{18}\equiv-\frac{p\mathcal H_\ell}{18}\pmod{p^2}.
\]
The inherited first-jet Green polynomials \(F_{\rm exact}=F_{\rm low}-\Gamma_\ell z^{p-1}G_\ell(z)\) and \(F_\sharp=F_{\rm low}-z^{p-1}G_\ell(z)/18\) differ by
\[
F_\sharp-F_{\rm exact}=(\Gamma_\ell-\tfrac1{18})z^{p-1}G_\ell(z).
\]
The original full source has exact zero logarithmic residue. Previously established \(E(F_\sharp)\equiv E(F_{\rm exact})\pmod p\) is valid only for the declared regularized scalar. This note does NOT re-prove these prior results.

## Theorem 1 — exact inverse-binomial expansion and modular Frobenius plateau

For every integer \(\ell\ge1\), the coefficients of \(G_\ell(1-y)=\sum_{j=0}^{\ell}q_j y^j\) are
\[
\boxed{q_j=(-1)^j{\ell\choose j}{3\ell-j\choose\ell}},\qquad
\sum_{j=0}^{\ell}q_j=1.
\tag{1}
\]
**Proof.** The coefficient of \(y^j\) is
\[
(-1)^j\sum_{i=j}^{\ell}{\ell\choose i}{2\ell\choose i}{i\choose j}
=(-1)^j{\ell\choose j}\sum_{r=0}^{\ell-j}{\ell-j\choose r}{2\ell\choose j+r}.
\]
Vandermonde convolution yields \({3\ell-j\choose2\ell-j}={3\ell-j\choose\ell}\). The sum of \(q_j\) is \(G_\ell(0)=1\). QED.

For every prime \(p=6\ell+1\ge7\), write
\[
B_\ell(y)=(1-y)^{p-1}G_\ell(1-y)=\sum_{k=0}^{p+\ell-1}b_ky^k,\qquad
C_k=\sum_{j=0}^kq_j \quad(0\le k<\ell).
\]
Then the full **source coefficient vector** has the following plateau and paired-endpoint law modulo \(p\):
\[
\boxed{b_k\equiv
\begin{cases}
C_k,&0\le k<\ell,\\
1,&\ell\le k\le p-1,\\
1-C_{k-p},&p\le k\le p+\ell-1,
\end{cases}\pmod p.}
\tag{2}
\]
**Proof.** In \(\mathbb F_p[y]\), \((1-y)^{p-1}=\sum_{a=0}^{p-1}y^a\) because \((-1)^a\binom{p-1}a\equiv1\). Convolve this finite all-ones interval with \(\sum_jq_jy^j\) and use \(\sum_jq_j=1\). The wrapped endpoint pairs satisfy \(b_k+b_{p+k}\equiv1\), not \(b_k=b_{p+k}\). The middle plateau includes the resonant index \(M=3\ell\), so \(b_M\equiv1\pmod p\). QED.

## Theorem 2 — closed finite quotient and its previously invisible second digit

Let the **regularized nonresonant Green scalar** be the exact rational linear observer
\[
E(F)=\sum_{\substack{0\le k\le7\ell\\k\ne M}}
[y^k]F(1-y)\frac{1-2^{M-k}}{k-M}.
\]
It explicitly omits the independent logarithmic-residue coordinate at \(k=M\).
Define
\[
\mathcal T_\ell=
\sum_{\substack{0\le k\le p+\ell-1\\k\ne M}}
b_k\frac{1-2^{M-k}}{k-M}\in\mathbb Z_{(p)}.
\]
All denominators \(k-M\) are nonzero and have absolute value at most \(4\ell<p\). Therefore the following is an **exact rational identity**, not merely a congruence:
\[
\boxed{E(F_\sharp)-E(F_{\rm exact})
=(\Gamma_\ell-\tfrac1{18})\mathcal T_\ell.}
\tag{3}
\]
Further, (2) reduces the many coefficients of \(\mathcal T_\ell\bmod p\) to one symmetric core and \(\ell\) endpoint repairs:
\[
\boxed{\mathcal T_\ell\equiv
\sum_{j=1}^{3\ell}\frac{2^j-2^{-j}}j+
\sum_{k=0}^{\ell-1}(1-C_k)\frac{2^{3\ell-k-1}}{k-3\ell}
\pmod p.}
\tag{4}
\]
**Proof.** Compare (2) with the baseline coefficients \(1\) on \(0\le k\le p-1\), \(0\) above. The baseline becomes the symmetric sum after setting \(k=M\pm j\). At each \(0\le k<\ell\), the difference from that baseline is \((C_k-1)w_k+(1-C_k)w_{p+k}\), where \(w_n=(1-2^{M-n})/(n-M)\). Fermat gives
\[
w_{p+k}-w_k\equiv
\frac{2^{M-k-1}}{k-M}\pmod p
\]
using \(2^{p-1}\equiv1\). Summing proves (4). QED.

Combining (3) with the **inherited on-hour gamma theorem** gives the newly resolved higher-precision defect:
\[
\boxed{\frac{E(F_\sharp)-E(F_{\rm exact})}{p}
\equiv-\frac{\mathcal H_\ell\mathcal T_\ell}{18}\pmod p.}
\tag{5}
\]
Here the quotient is well-defined in \(\mathbb Z_{(p)}\) because the numerator is \(p\)-divisible.

The separate exact source residue obeys
\[
r_\sharp=[y^M]F_\sharp(1-y)
=(\Gamma_\ell-\tfrac1{18})b_M
=\frac{1-(-1)^\ell S_\ell}{18},
\]
hence
\[
\boxed{\frac{r_\sharp}{p}\equiv-\frac{\mathcal H_\ell}{18}\pmod p.}
\tag{6}
\]
Equations (5),(6) are **distinct provenance/observer coordinates**. In particular, a mod-\(p\) scalar shortcut is legitimate, but without both repair data it does not preserve either a mod-\(p^2\) scalar or exact rational Green primitive. This is a concrete signed, p-adic BRC-style observer-fiber witness, not positive-mass BRC cancellation and not a transfer into native P000 coordinates.

## Exact computed witnesses and check scope

Executed standard-library integer/Fraction checker \`d25_frobenius_plateau_green_defect_check_20261031.py\`: independent exact binomial coefficient identity for \(\ell=1,\dots,14\); all 94 primes \(p=6\ell+1\le1200\) satisfy (2), (4), gamma correction and (5),(6); selected anchors independently convolve the original binomials; small cases verify exact rational residue/scalar formulas. The algebraic proofs above, rather than these finite tests, establish the universal statements.

| p | \(\ell\) | \(\mathcal H_\ell\bmod p\) | \(\mathcal T_\ell\bmod p\) | \(r_\sharp/p\bmod p\) | \((E_\sharp-E)/p\bmod p\) |
|---:|---:|---:|---:|---:|---:|
| 19 | 3 | 3 | 17 | 3 | 13 |
| 67 | 11 | 65 | 59 | 15 | 14 |
| 373 | 62 | 192 | 248 | 238 | 90 |

These distinct ports cannot be identified with the separate signed reflector \(R_p\) (old independent anchors \(R_{19}=12,R_{67}=21,R_{373}=196\)). At \(p=373\), the previously unobserved scalar digit is explicitly \(E_\sharp-E\equiv373\cdot90\bmod373^2\), while the source log residue is \(r_\sharp\equiv373\cdot238\bmod373^2\). Neither is inferred to vanish.

## Frontier, execution boundary and next discriminating action

The original frozen D25/LIFT hard target remains \(A_p(1)\equiv p\bmod p^3\) for \(p\bmod24\in\{13,19\}\). The known source-sensitive four-port congruence
\[
(A_p-p)/p^2\equiv(L_0N_0-1)/p+L_0N_1-12\,2^{-3\ell}E(F_{\rm exact})-R_p\pmod p
\]
is **OPEN as a uniform cancellation theorem**. In this mod-\(p\) identity, replacing \(E\) with \(E_\sharp\) is still safe. At higher precision the exact repair (5) must be included; the independent logarithmic source residue (6) cannot be set to zero or silently discarded.

**Next:** seek a single finite WZ/CM/adjoint certificate for the four-port mod-\(p\) cancellation, preserving the fixed \(216\), the original integer carry and first jet, the exact two-piece Green source and the independent signed \(R\) boundary. When lifting beyond mod \(p\), incorporate the distinct \(\mathcal H_\ell\) and \(\mathcal T_\ell\) repair ports rather than treating mod-\(p\) scalar equality as source equivalence. Do not redo the prior split-residue, gamma p² or finite Green inverse derivations. Native p373 H0/B0, Frobenius/\(\eta\), \(\kappa\) remain unexecuted in this author-only work.

Gateway 0.6.11 checked in this run: \`research_authority_granted=false\`, \`executor_binding_configured=false\`, \`CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED\`, active control jobs 5/5. Its current connector exposes \`em_status\` but no callable \`recovery_status\`; earlier same-task continuation returned \`CONTROL_QUOTA\`, not \`NO_DISPATCH\`. Control repair remains issue #1558. No new native session, CLAIM, OPEN, Source checkpoint, Result, review or mathematical admission is asserted. Registered activity remains pending; this Git publication is author-side only.