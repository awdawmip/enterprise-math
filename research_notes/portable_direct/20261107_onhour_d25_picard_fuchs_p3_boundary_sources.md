# D25 — Exact p³ Picard–Fuchs boundary sources for the two Fricke legs

2026-11-07. Continuation of D25 Fricke first-cutoff theorem \`0ef8b2a4954a7fe0ffa74f67127765f867e236ad\`. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen science input \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Author-side mathematical proof / exact modular checks; UNREVIEWED, NOT_ADMITTED.

## Theorem (exact rational polynomials; for any integer n>=1)

Define
\[
C_k=\frac{\binom{2k}{k}^2\binom{3k}{k}}{108^k},\qquad
D_k=\frac{\binom{2k}{k}^2\binom{4k}{2k}}{256^k};
\quad U_{<n}(z)=\sum_{k=0}^{n-1}C_k z^k,\quad B_{<n}(w)=\sum_{k=0}^{n-1}D_kw^k.
\]
Let \(\theta_x=x\,d/dx\). Consider the original third-order hypergeometric operators
\[
\mathcal L_U=\theta_z^3-z(\theta_z+\tfrac12)(\theta_z+\tfrac13)(\theta_z+\tfrac23),
\qquad
\mathcal L_B=\theta_w^3-w(\theta_w+\tfrac14)(\theta_w+\tfrac12)(\theta_w+\tfrac34).
\]
Their **exact, single-source finite-cutoff identities** are
\[
\boxed{\mathcal L_U U_{<n}(z)=-n^3 C_n z^n,\qquad
\mathcal L_B B_{<n}(w)=-n^3 D_n w^n.}\tag{1}
\]
This is an identity over \(\mathbb Q[z]\) and \(\mathbb Q[w]\), not a numerical approximation, and holds for arbitrary n.

For every prime \(p>3\), integer coefficients of the two cutoff objects are p-adically integral. Applying Lucas' theorem,
\[
C_p\equiv\tfrac19,\qquad D_p\equiv\tfrac3{32}\pmod p.
\]
Therefore the **first mod-\(p^4\) inhomogeneous Picard–Fuchs signatures** are
\[
\boxed{
 \mathcal L_U U_{<p}(z)\equiv-\frac{p^3}{9}\,z^p,\quad
 \mathcal L_B B_{<p}(w)\equiv-\frac{3p^3}{32}\,w^p\pmod{p^4}.
}\tag{2}
\]
At the frozen special arguments \(z=1/2\), \(w=1/9\), Fermat gives
\[
\boxed{
 (\mathcal L_U U_{<p})(\tfrac12)\equiv-\frac{p^3}{18},\qquad
 (\mathcal L_B B_{<p})(\tfrac19)\equiv-\frac{p^3}{96}\pmod{p^4}.
}\tag{3}
\]
The two exact source coefficients are distinct; their quotient in the p-adic unit group is \(16/3\). This is an observer/operation signature of the original 216 and 2304 coefficient streams, not a coefficient relation between their finite sums.

## Proof

Each \(C_k\) is the coefficient of \({}_3F_2(1/2,1/3,2/3;1,1;z)\), hence
\[
 k^3 C_k=(k-\tfrac12)(k-\tfrac23)(k-\tfrac13) C_{k-1}
\]
for k>=1. Likewise
\[
 k^3 D_k=(k-\tfrac34)(k-\tfrac12)(k-\tfrac14)D_{k-1}.
\]
For degrees 1 through n-1, the coefficient of each hypergeometric operator applied to the truncated polynomial is zero by its corresponding recursion. The sole remaining coefficient in degree n is \(-\prod_i(n-1+\alpha_i)C_{n-1}=-n^3 C_n\), and analogously for D. Degree zero vanishes. This proves (1) coefficient by coefficient without an analytic limit.

Lucas yields \(\binom{2p}{p}\equiv2\), \(\binom{3p}{p}\equiv3\), \(\binom{4p}{2p}\equiv6\pmod p\). Thus \(C_p\equiv4\cdot3/108=1/9\) and \(D_p\equiv4\cdot6/256=3/32\), proving (2). Fermat gives \(z^p\equiv z\pmod p\) at z=1/2 and w=1/9 (p>3), proving (3).

## Actual exact checks

The companion standard-library integer checker verifies the full truncated polynomial coefficients for p=5,7,11,19,373 modulo p^4, and at the two frozen rational arguments. In all ten instances the coefficients of degrees 0..p-1 vanish and the sole degree-p source agrees with the theorem. The exact output residues of (3) for p=19 are 6859 and 123462 modulo 130321; for p=373 they are 7524791965 and 12299142729 modulo 19356878641.

## Relation to mother objective and next work

The preceding Fricke t-cutoff computation finds an order-\(t^{2p}\) source; (1)-(3) now identify the **separate order-\(p^3\)** differential-operator sources at the frozen fibers. These are complementary coordinate/observer valuations; do not combine t-adic and p-adic orders as one scalar. They provide exact inhomogeneous data for a future Fricke gauge-pullback plus Frobenius continuation at t=6sqrt2. The remaining decisive calculation is the transported homogeneous boundary constants and Dwork unit-root normalization, sufficient to discriminate the p^4 residuals 5 (p19) and 199 (p373), and ultimately establish or refute 2V_p-W_p-p(-3/p)=0 mod p^4 for all relevant p. Native H0/B0, divided-power, Frobenius and independent p373 reproduction in #1559 remain a separate requirement.

Research identity: \`chatgpt-research-onhour-enterprise-math-20260923\`. Previous native request \`onhour11-20261106-1400-exact-research-lane-continuation\`: status UNKNOWN, current read returned \`BACKEND_IDENTITY_OR_VERSION_MISMATCH\` and \`operation_sent=false\`; REGISTER_PENDING / SYNC_DEBT, no native session/claim/run/Result inferred.
