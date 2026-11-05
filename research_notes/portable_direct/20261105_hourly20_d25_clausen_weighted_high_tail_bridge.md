# D25 — Finite Clausen square and the nontrivial weighted high-index tail

2026-11-05 (Asia/Hong_Kong). TASK_RESEARCH author-side, same parent Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, frozen input \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. AUTHOR-DERIVED / EXACT FINITE-POLYNOMIAL PROOF / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED. This is a separate second unit following the new Euler–Green same-prime gauge bridge.

## Exact weighted finite Clausen identity

For a prime \(p\ge5\), work in \(\mathbb Z_{(p)}\). Define
\[
g_k=\frac{(1/8)_k(3/8)_k}{(k!)^2 9^k},\quad
F_p=\sum_{k=0}^{p-1}g_k,\quad
D_p=\sum_{k=0}^{p-1}k g_k,
\]
\[
b_k=\frac{(4k)!}{(k!)^4 2304^k},\qquad
V_p=\sum_{k=0}^{p-1}(8k+1)b_k .
\]
The classical Clausen identity is
\[
{}_2F_1(1/8,3/8;1;x)^2
={}_3F_2(1/4,1/2,3/4;1,1;x),
\]
and the right-hand coefficients at \(x=1/9\) are exactly \(b_k\). For every \(0\le k<p\),
\[
b_k=\sum_{i+j=k}g_i g_j\quad \text{in }\mathbb Q,
\]
with \(g_i,g_j\) restricted to \(i,j\ge0\). Thus the square of the finite \(p\)-term Gauss sum has one additional, exactly determined **upper convolution strip**:
\[
T_p=\sum_{\substack{0\le i,j<p\\i+j\ge p}}
 (8(i+j)+1) g_i g_j .
\]
Applying the weighted observer \(1+8\theta_x\) *before* specializing \(x=1/9\) proves the exact rational identity
\[
\boxed{V_p+T_p=F_p(F_p+16D_p).}\tag{1}
\]
Proof: the square of the polynomial \(\sum_{k<p} f_kx^k\) agrees with the full Clausen coefficients below degree \(p\); its coefficients at degrees \(p,\dots,2p-2\) give \(T_p\) upon evaluation. The product rule gives \((1+8\theta)F^2=F^2+16F(\theta F)\). No division by \(p\) is used.

For primes \(p=8q+5\), set \(\ell=(5p-1)/8\). The exact Gauss coefficient recurrence shows \(g_j\equiv0\bmod p\) when \(\ell<j<p\). Therefore, modulo \(p^2\), the upper strip has a faithful two-source decomposition
\[
\begin{aligned}
T_p\equiv&
\sum_{\substack{0\le i,j\le\ell\\i+j\ge p}}
 (8(i+j)+1)g_i g_j\\
&+2\sum_{\substack{0\le i\le\ell<j<p\\i+j\ge p}}
 (8(i+j)+1)g_i g_j
\pmod{p^2}.
\end{aligned}\tag{2}
\]
The excluded high–high portion is in \(p^2\mathbb Z_{(p)}\). The surviving unit–unit portion can contain individual \(p\)-units; any final cancellation is an *aggregate*, so neither portion should be silently discarded. This is an explicit BRC typed-valuation/provenance separation in the auxiliary hypergeometric model.

## Signed second-digit corollary and its open hypothesis

For \(p\equiv5\pmod8\), assume the previously observed selected *Gauss* second-digit factor is divisible by \(p^2\):
\[
p\equiv13\pmod{24}:\quad F_p\equiv0\bmod p^2;\qquad
p\equiv5\pmod{24}:\quad F_p+16D_p\equiv0\bmod p^2.
\]
Then (1) implies \(T_p\equiv-V_p\bmod p^2\). Combined with the previously sourced Guo–Zudilin quartic weighted theorem \(V_p\equiv p(\tfrac{-3}{p})\bmod p^3\), this gives the **conditional all-prime upper-strip digit**
\[
\boxed{T_p/p\equiv-\left(\frac{-3}{p}\right)\pmod p.}\tag{3}
\]
The selected factor's universal \(p^2\)-divisibility remains a separate proof obligation. Equation (1) and source split (2) are unconditional exact identities; (3) holds under the explicit selected-factor premise.

This is an exact bridge from the newly normalized finite Gauss second-digit observer to the original quartic **2304** weighted source, but it does not identify it with original **216** or with the native \(373\) H0/B0 run.

## Exact computation

A standalone stdlib Python checker constructs all \(g_j\) modulo \(p^3\), computes \(V_p\) from its *independent original quartic factorial recurrence*, and sums the entire high-index convolution \(T_p\) without using (1) as a shortcut. For all **20 primes \(5\le p\le373,\ p\equiv5\bmod8\)** it checks (1) modulo \(p^3\), the known quartic benchmark, the selected Gauss factor modulo \(p^2\), and the digit (3): PASS 20/20. These are finite observations for the latter two assertions.

At \(p=373\), modulo \(p^3=51\,895\,117\):
\[
(F_p,D_p,V_p,T_p,F_p(F_p+16D_p))
=(1669548,\ 37945668,\ 373,\ 29773233,\ 29773606).
\]
Here \(T_p\equiv-373\bmod 373^2\), while the product is \(214\cdot373^2\bmod373^3\). At \(p=13\): \((V_p,T_p,\mathrm{product})=(13,1170,1183)\bmod2197\), so \(T_p/p\equiv12\pmod{13}\). At \(p=5\), the quartic character is \(-1\) and \(T_p=5\bmod125\).

## Next science and evidence boundaries

The next smallest source-preserving question is to prove the aggregate upper-strip digit (3) *directly* from the mixed valuation portions in (2), or disprove the universal selected-factor premise, without substituting the known quartic theorem for an original-216 proof. Compare to the existing signed original-216 three-valuation-port transport at \(p=13,373\). Preserve the original mother objective \(\Delta_p-R_p\equiv0\pmod p\), the frozen \(p=13,19\pmod{24}\) classes, the actual original 216 coefficient source, and the unexecuted native p373 H0/B0/\([X]U\bmod p^2\)/semilinear normalization/independent review.

Both new units are author-side portable; no native session/CLAIM/OPEN/checkpoint/Result or mathematical admission has been established by this artifact.
