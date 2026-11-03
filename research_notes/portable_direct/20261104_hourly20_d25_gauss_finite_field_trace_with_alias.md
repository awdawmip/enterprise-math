# D25 — Exact finite-field trace realization of the Gauss first-root observer

Date: 2026-11-04 (+08). **Author algebraic proof and finite exact check / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** No native CLAIM, OPEN or Source checkpoint. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Research logical lane \`chatgpt-research-hourly-enterprise-math-20260923\`.

This independent second scientific unit follows the author-side second-jet/Hensel study \`research_notes/portable_direct/20261104_hourly20_d25_gauss_second_jet_root_displacement.md\` and provides an explicit finite-field trace route for the previously unresolved Jacobi first-root selection. The finite-class vanishing remains a conjecture.

## Statement and exact source

For any prime \`p>=5\`, define the source indices \`0<=a,b<p\` by
\[
8a+1=mp,\qquad 8b+3=hp,
\]
with \`m,h\` among \`1,3,5,7\` determined by the prime residue. Let \`L=min(a,b)\` and \`z in F_p\`. Set
\[
P(z)=\sum_{k=0}^{L}\binom ak\binom bk z^k,\qquad
Q(z)=P(z)+16zP'(z).
\]
These are precisely the modulo-\`p\` reductions of the **original** truncated 2304 Gauss observers \`F_p(z)=sum_(k<p)(1/8)_k(3/8)_k z^k/(k!)²\` and \`G_p(z)=F_p(z)+16zF_p'(z)\`: before \`k=p\` each denominator is a p-unit, and the two numerator Pochhammer factors reduce to \`(-a)_k(-b)_k\`.

Define the finite-field trace sums
\[
T_F(z)=-\sum_{x\in\mathbf F_p}x^{p-1-b}(1+x)^a(x+z)^b,
\]
\[
T_G(z)=-\sum_{x\in\mathbf F_p}x^{p-1-b}(1+x)^a(x+z)^{b-1}
\bigl(x+(1+16b)z\bigr).
\]
All powers are polynomial powers, including \`x^0=1\`. Then the **exact coefficient-trace theorem** is
\[
\boxed{P(z)=T_F(z)-\epsilon_p,\qquad Q(z)=T_G(z)-\epsilon_p
\quad\text{in }\mathbf F_p[z],}
\]
where \`\epsilon_p=1\` exactly when \`a=p-1\`, and \`0\` otherwise. For the present \`a=-8^{-1} mod p\`, the exceptional case is exactly \`p=7\`.

**Proof.** The ordinary binomial product gives
\[
P(z)=[x^b](1+x)^a(x+z)^b,\qquad
Q(z)=[x^b](1+x)^a(x+z)^{b-1}\bigl(x+(1+16b)z\bigr).
\]
For a polynomial \`H(x)\` of degree \`a+b\`, multiply by \`x^(p-1-b)\` and sum over \`F_p\`. For positive exponents \`e\`, the power sum is \`-1\` if \`p-1 | e\`, and \`0\` otherwise. The exponent \`e=0\` gives the sum \`p=0\` in the field. Since \`0<=a<p\`, only the coefficient at \`x^b\` and, when \`a=p-1\`, the highest coefficient at \`x^(b+p-1)\` survive. Both displayed polynomials have leading coefficient \`1\`. Thus \`T_H=[x^b]H+1_{a=p-1}\` for each, proving the formulas. The exceptional correction is an exact top-degree alias, not a numerical fitting term.

## Actual independent exact check and discriminating route

The companion standalone Python standard-library checker separately computes \`P,Q\` from the binomial coefficients and \`T_F,T_G\` by **all** residues \`x=0,...,p-1\`, with the top-degree alias retained. It ran for all **622 primes** with \`5<=p<=10000\` and \`p mod8 in {5,7}\`. It passed both trace equalities and observed the earlier class selection in every case: \`P(1/9)=0, Q(1/9)!=0\` for **309 primes** in \`p mod24=13,23\`, and \`Q(1/9)=0, P(1/9)!=0\` for **313 primes** in \`p mod24=5,7\`. This is a second computational representation independent of the p² Gauss recurrence. It is a finite observation, not yet a proof of uniform residue allocation.

Sample \`(p,a,b,T_F-\epsilon,T_G-\epsilon)\` values: \`(13,8,11,0,7)\`, \`(23,20,14,0,13)\`, \`(29,18,25,26,0)\`, \`(373,233,326,0,80)\`, \`(2053,1283,1796,0,1686)\`. The \`p=7\` alias is essential: omitting \`\epsilon_p=1\` gives an exact false equality, fixed and rerun before publication.

**Research reuse:** This is a finite-field trace/character-sum representation with explicit source exponents \`(a,b,p)\`, index provenance, and signed weights. It supplies a concrete finite polynomial whose zero is precisely the first-digit Jacobi root. The next unit is to identify a Frobenius/CM or finite-field involutive certificate for the corresponding trace vanishing, with the exact \`p=7\` alias, then feed the result into the previously derived Hensel displacement and p² parameter jet. Continue the signed original 216–2304 mod-p³ comparison; the frozen mother objective \`W216(p-1)=p mod p³\` for \`p mod24=13,19\` remains open.

**BRC carrier and limits:** Original Pochhammer integer indices, both modulo-\`p\` coefficient observers, full \`F_p\` sampling population and the alias fiber are preserved. The quotient from the p-adic source to \`P,Q\` is certified for this first-digit observer only; second-digit/p³ operations continue to use the original source, second-jet endpoint and Clausen-tail ports. All claims here are about the declared finite field, not X6 spatial compression or external physical dynamics.

**Control:** Source author evidence may be durably stored via GitHub; gateway 0.6.11 on 2026-11-04 still reported \`UPSTREAM_CODE_REVIEW_REQUIRED\`, \`research_authority_granted=false\`. No old session/claim/run/staging mutated.
