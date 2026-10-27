# D25/LIFT R46 — 原始 W/S 反射配对的仿射秩权重不可能性与 397 例外

2026-10-27 (Asia/Hong_Kong). Portable original mathematics, logical lane \`chatgpt-research-hourly-enterprise-math-20260923\`; Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, parent D25/LIFT/JT2 OPEN. Frozen *scientific* Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Consume R43–R45 without recredit. Evidence: \`AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY\`. No native Task CLAIM/open or formal Source checkpoint is asserted.

## Exact inherited source and first-digit observer

Use **unchanged** original rational W and S terms
\[
w_k=\frac{(6k+1)(2k)!(3k)!}{(k!)^5 216^k},\qquad
s_k=\frac{(8k+1)(4k)!}{(k!)^4 2304^k}
\]
and the R45 reflected-pair auxiliary observable
\[
E_{p,k}=\frac{s_ks_{p-k}}{w_kw_{p-k}}.
\]
For prime \(p=6m+1\ge19\) and strictly low ranks \(1\le k<p/4\) with \((1-36k^2)(1-64k^2)\not\equiv0\pmod p\), R45-A proved
\[
E_{p,k}\equiv F(k):=\frac3{16}\frac{1-64k^2}{1-36k^2}\pmod p.
\]
The first-digit formula is a theorem, not a statistical fit; W/S labels and their weights remain separately defined, and a multiplicative pair observer is not an additive WZ cancellation.

## R46: no affine-in-rank scalar transfer, including prime-dependent coefficients

**Theorem.** For every prime \(p=6m+1\ge19\), there are **no** coefficients \(a_p,b_p\in\mathbb F_p\) satisfying
\[
E_{p,k}\equiv a_p+b_pk\pmod p
\]
at **all nonsingular low-band ranks** \(1\le k<p/4\). It already fails on the following bounded exact observation stencil:

- \(p=19\): ranks \(\{1,2,4\}\);
- \(p=31\): ranks \(\{1,2,3\}\);
- \(p\ge37\): ranks \(\{1,2,3\}\), **except** \(p=397\), when the fourth rank must be added. For all \(p\ge37\), the four ranks \(1,2,3,4\) suffice.

**Proof.** Compute the four values exactly in \(\mathbb Q\):
\[
F(1)=\frac{27}{80},\quad
F(2)=\frac{765}{2288},\quad
F(3)=\frac{1725}{5168},\quad
F(4)=\frac{3069}{9200}.
\]
Every affine function has a vanishing second finite difference. Here
\[
\Delta^2 F(1)=F(3)-2F(2)+F(1)
=\frac{1191}{461890}
=\frac{3\cdot397}{2\cdot5\cdot11\cdot13\cdot17\cdot19}.
\tag{R46-2}
\]
For all \(p\ge31\) the denominator is a unit; the residue is nonzero except at the **actual prime** \(p=397\). At 397, use four ranks. An affine function has a vanishing third difference, whereas
\[
\Delta^3F(1)=F(4)-3F(3)+3F(2)-F(1)
=-\frac{58644}{26558675}
=-\frac{2^2 3^4\cdot181}{5^2\cdot11\cdot13\cdot17\cdot19\cdot23}.
\tag{R46-3}
\]
Its residue at \(p=397\) is nonzero. Indeed for all \(p\ge37\), the 397-only possible zero of (R46-2) cannot coincide with the 181-only possible zero of (R46-3). All first four ranks are strict low-band and weight-unit for these primes.

For \(p=19\), rank 3 has a singular \(6(p-k)+1\) source weight; do **not** divide by it. Ranks 1,2,4 are valid, and an affine function obeys \(F(4)-3F(2)+2F(1)=0\), but exactly
\[
F(4)-3F(2)+2F(1)=\frac{909}{164450}
=\frac{3^2\cdot101}{2\cdot5^2\cdot11\cdot13\cdot23}
\not\equiv0\pmod{19}.
\tag{R46-19}
\]
For \(p=31\), ranks 1,2,3 are valid and (R46-2) is nonzero. Every case is covered. QED.

The \(p=397\) exact cancellation of the rank-1 second difference is a **stencil-specific exception**, not vanishing of the original W/S discrepancy or a new S-tail phenomenon; the fourth-rank certificate resolves it. Separately, \(p=181\) makes (R46-3) vanish but (R46-2) is nonzero, so no affine map arises there either.

## Author execution / finite checks

An independently implemented stdlib checker recomputed original p-free factorial W/S kernels and both original linear weights on every stencil rank, then compared the raw modular pair to the rational closed form \(F(k)\); it did not evaluate only the stated rational differences. Actual execution on all **78** primes \(19\le p\le997\), \(p\equiv1\pmod6\), covered **310** raw source-pair observations and confirmed each finite-difference obstruction. Exact \(p=397\) certificate: \((F(1),F(2),F(3),F(4))=(45,89,133,79)\pmod{397}\), so \(\Delta^2=0\) and \(\Delta^3=299\ne0\). All checks PASS. General theorem is algebraic; the finite run is author verification, not independent review or formal admission.

Companion script: \`research_notes/portable_direct/20261027_hourly_d25_reflected_affine_stencil_r46_check.py\`.

## Scope, BRC and next work

This is a **more precise restricted obstruction** than R45's rank-independent scalar no-go: even affine \(a_p+b_pk\), chosen separately for each prime, fails at an explicitly bounded stencil of unchanged source pairs. It does not exclude quadratic/rational rank dependence, nonlocal cross-rank WZ sums or the original target \(W_p\equiv S_p\pmod{p^3}\). Original factorial valuations, source provenance, singular weights and exact finite/positive-infinity/high-high boundary labels remain untouched.

BRC \`COMPOSE_APPLIED\`: rank, reflection, first-digit observer, operation class and source provenance are carried independently. These are hypergeometric auxiliary ranks, not native X6 spatial axes; P000 and the fixed \(z=2\) six-channel Hasse J/E observer stay unchanged.

**Next executable unit:** use the rational \(F(k)\) as a minimal required rank-dependent boundary condition for a *source-labelled additive* cross-rank telescoper, and test a controlled two-port \(W_2/S_2\) plus endpoint Green ansatz against R23's \(p^2\)-divided low-half discrepancy, including isolated \(p=181\) S-tail zero. Native original H0/B0, \([X]U\bmod p^2\), Frobenius \(\eta/\kappa\), \(p=373\) and independent Driver review remain separate pending parent obligations. Control successor/predecessor repair stays with #1558.
