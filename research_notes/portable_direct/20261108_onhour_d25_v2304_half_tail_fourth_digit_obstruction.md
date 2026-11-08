# D25 — Original V2304 half-tail fourth digit: a source-band transport certificate and half-truncation obstruction

Date: 2026-11-08 (Asia/Hong_Kong).
Status: **AUTHOR_SIDE_PROVED_CONDITIONAL_ON_CITED_DUAL_TRUNCATION / EXACT_301_PRIME_CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.
Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; immutable scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`.

## Scientific question

The previously checked, still-open C4 candidate is
\[
W_p-2V_p+p\chi_p\equiv0\pmod{p^4},\qquad \chi_p=(-3/p),
\]
with original full truncations at \(p-1\). Guo–Zudilin's *A q-microscope for supercongruences* (Adv. Math. 346 (2019), 329–358, arXiv:1803.01830) proves \(V_p(p-1)\equiv V_p((p-1)/2)\equiv p\chi_p\pmod{p^3}\). Does substituting the half-truncation preserve C4 at fourth-digit precision? The exact answer is **no**, already at p=13. The full/half difference has a nontrivial, explicitly derived fourth-digit two-band certificate.

## Theorem: exact fourth-digit half-tail carrier

For every prime \(p>3\), put
\[
v_n=(8n+1)\frac{(4n)!}{(n!)^4\,2304^n},\quad
V_p^{\rm full}=\sum_{n=0}^{p-1}v_n,\quad
V_p^{\rm half}=\sum_{n=0}^{(p-1)/2}v_n.
\]
All rational denominators are p-units. Let \(R=\mathbf Z_{(p)}\), \(\omega_p=((p-1)!+1)/p\bmod p\), and \(H_j=\sum_{i=1}^j i^{-1}\bmod p\). On the *original* grade-2 indices
\(I_2=\{n:(p+1)/2\le n<p,\ 2p\le4n<3p\}\), define \(r_n=4n-2p\) and
\[
c_n=2(8n+1)\frac{r_n!}{(n!)^4\,2304^n}\in R,\quad
C_p=\sum_{n\in I_2}c_n\pmod{p^2},
\quad L_p=\sum_{n\in I_2}2c_n(H_{r_n}-\omega_p)\pmod p.
\]
On the original grade-3 indices \(I_3=\{n:3p\le4n<4p,\ 0\le n<p\}\), define \(s_n=4n-3p\) and
\[
T_{3,p}=\sum_{n\in I_3}-6(8n+1)
\frac{s_n!}{(n!)^4\,2304^n}\pmod p.
\]
The three carriers retain **index, model, grade, sign, coefficient and observer**; neither the whole tail nor a surrogate weighted polynomial is used to define them. Then the cited dual-truncation theorem implies \(C_p\equiv0\pmod p\), so the p-adic quotient \(\mathcal Q_p=C_p/p\pmod p\) is well-defined from the p-unit sum. Moreover,
\[
\boxed{\frac{V_p^{\rm full}-V_p^{\rm half}}{p^3}
\equiv\mathcal Q_p+L_p+T_{3,p}\pmod p.}\tag{H4}
\]
The left side is a p-adic integer by the published dual-truncation congruence. This statement is a rigorous consequence of that published result and the proved factorial-complement expansions; it is not a new proof of C4.

### Proof

The half-tail has only original valuation grades 2 and 3: \(g_V(n)=\lfloor4n/p\rfloor\). For grade 2 the exact factorial-complement expansion, valid for every \(0\le r<p\), is
\[
(2p+r)!/p^2\equiv2r![1+2p(H_r-\omega_p)]\pmod{p^2}.
\]
Therefore \(\sum_{I_2}v_n\equiv p^2C_p+p^3L_p\pmod{p^4}\).
For grade 3, Wilson's theorem gives
\((3p+s)!/p^3\equiv-6s!\pmod p\), so
\(\sum_{I_3}v_n\equiv p^3T_{3,p}\pmod{p^4}\).
The two bands exactly partition \(V_p^{\rm full}-V_p^{\rm half}\). The cited theorem implies this difference vanishes modulo \(p^3\); reducing its grade-two-plus-three expansion modulo \(p^3\) gives \(C_p\equiv0\pmod p\). Divide the expansion by \(p^3\), retaining the \(\bmod p\) observer, proving (H4). QED.

The invariant \(C_p/p\) depends on the exact p-adic lift of the *grade-two p-unit sum* modulo \(p^2\), not merely on its residue modulo \(p\). It is essential to preserve this digit when reducing the BRC grade carrier.

## Exact numeric certificates and falsifier

| \(p\) | \(\mathcal Q_p=C_p/p\) | \(L_p\) | \(T_{3,p}\) | half-tail fourth digit | \(V^{full}-V^{half}\bmod p^4\) |
|---:|---:|---:|---:|---:|---:|
| 13 | 3 | 0 | 6 | 9 | 19773 |
| 19 | 14 | 11 | 16 | 3 | 20577 |
| 373 | 69 | 165 | 119 | 353 | 18318976301 |

For \(p=13\), the full original sums give \(W_{13}=19786\), \(V_{13}^{full}=24180\), \(V_{13}^{half}=4407\pmod{13^4=28561}\). Thus
\[
W_{13}-2V_{13}^{full}+13\equiv0\pmod{13^4},
\quad
W_{13}-2V_{13}^{half}+13\equiv10985=5\cdot13^3\not\equiv0\pmod{13^4}.
\]
This is an **exact counterexample** to replacing \(V^{full}\) with \(V^{half}\) in the unmodified C4 formula. At \(p=373\), the corresponding half-truncation residual equals \(333\cdot373^3\bmod373^4\). The Guo–Zudilin half-truncation can still be consumed for the *modulo p³* mother target, but fourth-digit cross-model transport must account for the explicit H4 boundary.

Source-preserving arithmetic script: \`d25_v2304_half_tail_fourth_digit_20261108.py\`. Independent original-coefficient recurrence and factorial/Wilson band evaluator agree for **all 301 primes \(5\le p\le2000\)**; the script also checks \(C_p\equiv0\pmod p\) and tail divisibility by \(p^3\). Finite coverage independently validates the implementation, not an infinite theorem.

## Task and native benchmark separation

Reused parent author-side fourth-grade jets and previously verified Guo–Zudilin double truncation; did not rerun or recredit D24 accepted UR work. The native p373 same-original-class H0/B0 divided-power benchmark remains **NOT_EXECUTED / PENDING_OWNER**, tracked by existing support issue #1559: it needs [X]U mod 139129, module rank, Frobenius direction/eta, signed Hesse/Green kappa, Delta-R and independent reproduction. H4 is an original V2304 arithmetic *portable* discriminator, not the native H0/B0 computation.

Source original target request \`onhour11-20261106-1400-exact-research-lane-continuation\` was read as **SUCCEEDED** for a preexisting continuation packet, but not as a Researcher session/claim for this caller. Research authority for this Site remains unverified (\`research_authority_granted=false\`); this research output is **UNREVIEWED/NOT_ADMITTED**, with native registration/checkpoint pending. The historical Research conversation ID is a routing label, not proof of a platform-signed session.

Next scientific action: distinguish fourth-digit full-versus-half sources in any proposed Fricke/Cartier/WZ bridge, keeping \(\mathcal Q_p,L_p,T_{3,p}\) separately until the declared observer; test candidate cancellation on p=13 (nonzero H4) before claiming C4. Next native action: authorized executor runs #1559 original-class p373 H0/B0 and records raw reproducible output.