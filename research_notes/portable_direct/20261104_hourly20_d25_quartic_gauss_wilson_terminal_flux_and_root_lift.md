# D25 — Quartic Gauss terminal Picard–Fuchs flux and selected-root transport

Date: 2026-11-04. Original task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; immutable scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. This is portable author-side mathematics, **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. It creates no native CLAIM, Result, native H0/B0 experiment, or independent review.

## 1. Exact all-prime terminal-flux theorem

For each prime \`p>=5\`, define the original Gauss coefficients and the finite polynomial

\[
v_k=\frac{(1/8)_k(3/8)_k}{(k!)^2 9^k},\qquad
F_p(z)=\sum_{k=0}^{p-1}v_kz^k,\qquad \theta=z\,d/dz.
\]

All denominators of \(v_0,\ldots,v_{p-1}\) are \(p\)-units. Introduce the **integer-scaled** Gauss operator

\[
\mathscr D=576\theta^2-z(8\theta+1)(8\theta+3).
\]

The coefficient recurrence is \(576k^2v_k=(8k-7)(8k-5)v_{k-1}\) for \(1\le k<p\), so the following is an **exact polynomial identity over \(\mathbb Q\)**:

\[
\boxed{\mathscr D F_p(z)=-(8p-7)(8p-5)v_{p-1}z^p.}\tag{1}
\]

Set \(\varepsilon_p=3\) for \(p\equiv1,3\pmod8\) and \(\varepsilon_p=35\) for \(p\equiv5,7\pmod8\). Then, for **every prime \(p\ge5\)**,

\[
\boxed{\mathscr D F_p(z)\equiv-\varepsilon_p p^2z^p\pmod{p^3}.}\tag{2}
\]

This identifies a universal third-digit terminal anomaly, constant within each pair of mod-8 residue classes.

### Proof of the terminal coefficient via Wilson

Assume first \(p\ge11\), and let \(a,b\in\{1,3,5,7\}\) be the unique odd integers with \(a p\equiv1\pmod8\), \(b p\equiv3\pmod8\). Both indices

\[
j_1=(ap-1)/8,\qquad j_3=(bp-3)/8
\]

belong to \(0,\ldots,p-2\). The products \(\prod_{j=0}^{p-2}(8j+1)\) and \(\prod_{j=0}^{p-2}(8j+3)\) each contain exactly one \(p\)-divisible factor, respectively \(ap\) and \(bp\). Removing those factors and using that multiplication by 8 permutes \(\mathbb F_p\), the missing nonzero residues are \(-7\) and \(-5\). Hence Wilson's theorem gives

\[
\prod_{j\ne j_1}^{p-2}(8j+1)\equiv\frac{(p-1)!}{-7}=\frac17,\quad
\prod_{j\ne j_3}^{p-2}(8j+3)\equiv\frac{(p-1)!}{-5}=\frac15\pmod p.
\]

Because \(576^{p-1}((p-1)!)^2\equiv1\pmod p\), the original full product yields

\[
\boxed{\frac{v_{p-1}}{p^2}\equiv\frac{ab}{35}\pmod p,\qquad p\ge11.}\tag{3}
\]

In the mod-8 classes \(1,3,5,7\), the ordered pairs \((a,b)\) are \((1,3),(3,1),(5,7),(7,5)\), so \(ab=\varepsilon_p\). Since \((8p-7)(8p-5)\equiv35\pmod p\), (1)–(3) prove (2) for \(p\ge11\).

At \(p=5\), \(v_4\) contains \(25\) and \(8p-5=35\) contains 5, giving a \(p^3\) terminal term. At \(p=7\), \(v_6\) contains 7 and \(8p-7=49\) contains \(p^2\), again giving \(p^3\). In both cases \(-35p^2=0\pmod{p^3}\), completing the proof.

The stronger terminal-coefficient statement (3) is restricted to \(p\ge11\), with \(v_{p-1}\) having **exactly** valuation 2 there; the all-prime operator statement (2) includes both small primes.

## 2. Third-digit first-moment transport

Put \(S=F_p(1)\), \(D=(\theta F_p)(1)\), \(Y(z)=(1+16\theta)F_p(z)\) and \(Y_1=Y(1)=S+16D\). Evaluating (1) at \(z=1\) yields exactly

\[
\boxed{32(\theta Y)(1)-4Y_1+S=-(8p-7)(8p-5)v_{p-1},}\tag{4}
\]

hence the universally valid congruence

\[
\boxed{32(\theta Y)(1)-4Y_1+S\equiv-\varepsilon_p p^2\pmod{p^3}.}\tag{5}
\]

The term on the right is the full, source-preserved Picard–Fuchs truncation defect. In particular, \(\theta Y(1)\equiv(4Y_1-S)/32\pmod{p^2}\).

For \(p\equiv5\pmod8\), use the previous, independently recorded first-digit product fact \(SY_1\equiv0\pmod p\), along with the previous exclusive-factor lemma that exactly one of \(S,Y_1\) vanishes modulo \(p\). The two respective derivative slopes are

\[
\boxed{S\equiv0\pmod p\implies F_p'(1)=D\equiv Y_1/16\not\equiv0\pmod p,}\tag{6}
\]
\[
\boxed{Y_1\equiv0\pmod p\implies Y'(1)\equiv-S/32\not\equiv0\pmod p.}\tag{7}
\]

Thus the selected zero of either the Gauss or weighted-derivative observer at \(z=1\bmod p\) is simple, and it has a **unique Hensel root** \(\xi_p\in\mathbb Z_p\) congruent to 1 modulo \(p\). This supplies a local root-transport interface beyond the previous exclusive-factor assertion.

If the selected factor \(G\in\{F_p,Y\}\) additionally vanishes modulo \(p^2\), Hensel's lemma and a first-order Taylor expansion imply the exact third-digit root-displacement formula

\[
\boxed{\frac{\xi_p-1}{p^2}\equiv-\frac{G(1)/p^2}{G'(1)}\pmod p.}\tag{8}
\]

For the observed \(p\equiv13\pmod{24}\) branch, the right-hand side is \(-16(S/p^2)Y_1^{-1}\). For \(p\equiv5\pmod{24}\), it is \(32(Y_1/p^2)S^{-1}\). The class-selected hypothesis \(G(1)\equiv0\pmod{p^2}\) is a **finite observation**, not assumed in (2)–(7). Formula (8) is a conditional exact theorem. It identifies a canonical third-digit CM-root displacement for future comparison with native or Jacobi structures.

## 3. Exact execution and scope

The script \`d25_quartic_gauss_terminal_flux_hensel_20261104.py\` was run locally using Python standard library modular arithmetic. It independently generates the original \(v_k\) from the coefficient recurrence, checks (1)/(4) at \(z=1\) and the all-prime endpoint prediction (2)/(5) modulo \(p^3\) for all **667 primes \(5\le p\le5000\)**, and checks (3) for all \(p\ge11\). Direct rational coefficients via \`Fraction\` cross-check \(p=5,7,11,13,17,19,23\). For the **168** primes \(p\equiv5\pmod8\) in this range, the selected branch does vanish modulo \(p^2\), and direct polynomial evaluation at \(1+p^2\rho_p\) verifies (8) modulo \(p^3\).

Representative exact outputs: \((p,\varepsilon_p,\rho_p)=(13,35,7),(29,35,7),(37,35,1),(53,35,13),(373,35,296)\). The \(p=5\) root has \(\rho_5=0\). All assertions passed. These are finite checks, not a proof of the class selector.

## 4. BRC observer and exact continuation

BRC status: **COMPOSE_APPLIED**: source index \(k\), original rational coefficient \(v_k\), prime valuation, operator \(\mathscr D\), signed terminal coefficient, first moment and derivative observer, and future \(p^3\)/Hensel operations remain separately typed. Only the proved reductions (1)–(8) are used. This is a Gauss/Jacobi arithmetic port, not a native X6/crystalline Frobenius identification.

Next smallest unresolved science: prove the class-selected \(p^2\) vanishing uniformly, or derive a finite CM/Jacobi relation forcing the Hensel root \(\xi_p\equiv1\pmod{p^2}\) in each mod-24 class. Use the explicit third-digit terminal forcing \(-3p^2/-35p^2\) when building that relation; retain the \(p=5,7\) exceptions. Then return to the quartic triangular correction and original signed 216–2304 Green comparison. The separate native p=373 H0/B0 and D24 \(\Delta_p-R_p\) obligations remain open.

Canonical control continuation read: \`hourly20-20261104-1821-fresh-continuation-read\` succeeded against Source \`ad411ab2843c23acb22d86c5bc7fabf09e366f42\`; it showed the previous native checkpoint \`SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED\`, route \`REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION\`, and \`execution_authorized=false\`. This author-side file does **not** replace or overwrite that native checkpoint; pending session/staging disposition remains separately governed. The prompt-provided Research conversation ID is \`chatgpt-research-hourly-enterprise-math-20260923\` (not platform-attested); maintenance ID remains wholly separate.
