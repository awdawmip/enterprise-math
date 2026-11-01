# D25 / LIFT: Global root-multiplicity theorem for the original 216-weighted polynomial and bounded signed-character census

Date: 2026-10-31 (Asia/Hong_Kong). Scope: GH-176 / GH-177, PORTABLE_AUTHOR_PROVED / EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3, preserved. Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Own logical conversation: chatgpt-research-hourly-enterprise-math-20260923 (not maintenance or the on-hour lane). This is an author-side arithmetic result, not an authorized Source CLAIM/run/checkpoint.

## Exact original object

For a prime p>=5 define

\[
a_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n},\qquad
\mathcal A_p(X)=\sum_{n=0}^{p-1}(6n+1)a_n X^n\in\mathbb Z_p[X].
\]

The frozen objective is \(\mathcal A_p(1)\equiv p\pmod{p^3}\) for p mod 24 equal to 13 or 19. The parameter X=1 remains fixed in that objective.

## GH-176: Theorem, with proof, for ALL primes p=6m+1>=7

Let

\[
 f(X)=\sum_{n=0}^{m}\binom mn\binom{2m}n(X/2)^n,\qquad
 L(X)=f(X)+12Xf'(X)\quad\text{in }\mathbb F_p[X].
\]

**Full polynomial factorization:** \(\overline{\mathcal A_p}(X)=f(X)L(X)\) coefficientwise in \(\mathbb F_p[X]\). This follows from the formal rational Clausen identity for \({}_3F_2(1/2,1/3,2/3;1,1;X/2)\) as the square of \({}_2F_1(1/6,1/3;1;X/2)\), followed by \(1+6X\partial_X\). Here \(1/6\equiv-m\), \(1/3\equiv-2m\pmod p\); the Gauss factor terminates at m, and all full-series three-hypergeometric coefficients with n>2m and n<p vanish modulo p. Thus the factorization does NOT merely hold at X=1.

**Precise root classification:** Over the algebraic closure of \(\mathbb F_p\), every zero of \(\overline{\mathcal A_p}\) is simple except possibly \(X=2/3\). If \(L(2/3)=0\), that root has multiplicity EXACTLY TWO, with

\[
 \boxed{\overline{\mathcal A_p}''(2/3)=\frac9{32}\,f(2/3)^2\ne0.}
\]

In particular, any zero at X=1 is simple, whether it arises from f=0 or L=0. No hypothesis about CM branch type is required for this structural theorem.

**Proof.** The terminated polynomial f satisfies the coefficientwise exact finite-field ODE

\[
 X(2-X)f''+(2-\tfrac32 X)f'-\tfrac1{18}f=0. \tag{1}
\]

At any ordinary point \(\alpha\notin\{0,2\}\), simultaneous f(\(\alpha\))=f'(\(\alpha\))=0 would force every higher Taylor coefficient to vanish by (1) and its derivatives. Since \(\deg f=m<p\), that contradicts f(0)=1. At X=0, f(0)=L(0)=1. At X=2, Vandermonde gives \(f(2)=\binom{3m}{m}\ne0\pmod p\); evaluating (1) yields \(f'(2)=-f(2)/18\), so \(L(2)=-f(2)/3\ne0\). Therefore f and L have no common root, and neither endpoint is a root.

Differentiating L and substituting (1) gives the exact rational identity at X not equal to 2:

\[
 L'(X)=\frac{(2+5X)f'(X)+\tfrac23 f(X)}{2-X}. \tag{2}
\]

At a root \(\alpha\) of f, L(\(\alpha\))=12\(\alpha f'(\alpha)\ne0\), so

\[
 \mathcal A'_p(\alpha)=12\alpha [f'(\alpha)]^2\ne0 \quad\text{in }\mathbb F_p.
\]

At a root \(\alpha\) of L, f(\(\alpha\)) is nonzero and \(f'(\alpha)=-f(\alpha)/(12\alpha)\), whence

\[
 \boxed{\overline{\mathcal A_p}'(\alpha)
 =\frac{f(\alpha)^2(3\alpha-2)}{12\alpha(2-\alpha)}.} \tag{3}
\]

This is nonzero unless \(\alpha=2/3\). If L(2/3)=0, (1) yields \(f'(2/3)=-f(2/3)/8\) and \(f''(2/3)=13 f(2/3)/64\). Differentiate (2) once: \(L''(2/3)=9 f(2/3)/32\ne0\). Consequently the product fL has precisely a double zero, establishing the claimed classification. This argument is algebraic over characteristic p>3, not a finite-sample extrapolation. QED.

The exceptional-coordinate nonvanishing \(L_p(2/3)\ne0\) for all primes is NOT proved; the theorem classifies its possible effect exactly.

## GH-177: Executed bounded arithmetic and an exact p-adic connection

The attached executed standard-library checker exhaustively evaluated the *original* weighted 216 series in \(\mathbb Z/p^3\), with original index n=0,...,p−1, for every one of the 1436 primes 5<=p<12000. Every tested prime obeyed

\[
 \boxed{\mathcal A_p(1)\equiv p\left(\frac{-3}{p}\right)\pmod{p^3}}
 \qquad\text{FOR THE 1436 TESTED PRIMES ONLY}. \tag{4}
\]

The sign is +1 for p=1 mod 6, −1 for p=5 mod 6. A universal signed supercongruence and its prior-art status are OPEN; (4) is a finite exact census, not a proof over all primes.

The eight counts for residue classes r=1,5,7,11,13,17,19,23 modulo 24 are (164,185,184,181,181,177,182,182). Among the 711 tested p=1 mod 6, the complete branch split at X=1 was 363 cases f(1)=0 (181 residue 13 plus 182 residue 19) and 348 cases L(1)=0 (164 residue 1 plus 184 residue 7). The derivative from (3) or the f-zero branch was nonzero for all 711. For all these 711 primes, the exact computation also found L(2/3) nonzero. The theorem thus certifies *all geometric roots* of these 711 particular weighted polynomials are simple. The program independently confirmed ten anchors from the raw binomial formula; a longer companion checker independently verified eleven full polynomial identities and Euclidean GCDs.

Examples (p, \(\mathcal A_p(1)\pmod{p^3}\), \(\mathcal A_p'(1)\pmod p\)):
(5,120,4), (7,7,5), (11,1320,10), (13,13,3), (19,19,12), (31,31,29), (157,157,10), (373,373,292), (1327,1327,1165).

Executable path: research_notes/portable_direct/d25_gh176_gh177_weighted_census_core.py .
Run from repository root: python research_notes/portable_direct/d25_gh176_gh177_weighted_census_core.py .
Observed completion marker: PASS_GH176_GH177_SIGNED_EXACT_BOUND_12000.
The output row-string SHA256 for its 1436 samples is eb94d6b99c91474043b2e37837e6dea22fad2ec5fb9b3d2c6e9cc1532c451f37. A separate, longer local checker with polynomial GCD and CSV evidence is preserved in the portable deliverable; its row-string SHA256 is 0ba1a04b031051dbb6d7076674c5d9361799cd62560ccc4a2a89762971437a88. Different row formats account for different hashes; sample data and arithmetic agree.

**Hensel alignment for the FROZEN target, using prior theorem assumptions at original strength.** Suppose p mod 24 is 13 or 19 and consume the previously established/author-verified first digit and CM/Hasse branch, \(\mathcal A_p(1)\equiv p\pmod{p^2}\) and \(f_p(1)=0\). Let

\[
 u_p=12f_p'(1)^2=\bar h_p^2/12\in\mathbb F_p^\times,\quad
 \bar h_p=12f_p'(1),\quad
 \delta_p=\frac{\mathcal A_p(1)-p}{p^2}\pmod p.
\]

By Hensel's lemma the equation \(\mathcal A_p(\xi_p)=p\) has a **unique** p-adic solution \(\xi_p\equiv1\pmod p\). The first-digit condition strengthens its congruence to \(\xi_p\equiv1\pmod{p^2}\), and Taylor expansion with the certified derivative gives

\[
 \boxed{\xi_p\equiv1-p^2u_p^{-1}\delta_p\pmod{p^3}.} \tag{5}
\]

If, and only if, one also consumes the previous author-side GH-166 signed three-port reduction with its exact original hypotheses, its residual \(\delta_p=\Delta_p^<+K_{\rm head}+K_{\rm bulk}\pmod p\) yields the source-aware conditional formula

\[
 \boxed{\xi_p\equiv1-\frac{12p^2}{\bar h_p^2}
 (\Delta_p^<+K_{\rm head}+K_{\rm bulk})\pmod{p^3}.} \tag{6}
\]

This is a **diagnostic**, not a moving-parameter solution to fixed-X LIFT. Under the stated source assumptions, the frozen congruence is equivalent to \(\xi_p\equiv1\pmod{p^3}\). The 363 bounded frozen cases have \(\delta_p=0\) by the executed original sum; only a genuine global CM/WZ/p-adic proof can make this statement infinite.

## BRC observer, provenance, and next executable science

BRC COMPOSE_APPLIED: preserve source (p,n,a_n,X), the signed weight 6n+1, the Gauss-factor branch (f or L), derivative operator, and p-adic digit \(\delta\). Observing only A(1) does not preserve all derivative/root information. Equations (3), (5) and (6) identify exactly what an observer must retain for root and digit operations; the coordinate X is an external arithmetic parameter, NOT a P000 native X6 axis. The active P000 discrete X6, 120-degree native relation and triadic closure starting axioms are unchanged and not asserted to be proven by this auxiliary arithmetic.

Classical external identity reference: NIST DLMF §16.12.2 (Clausen); related 216 Ramanujan series: MathOverflow question 508786; Dirichlet character table: MathWorld LegendreSymbol. These external references establish the known identity/context, not priority or the unproved all-prime signed statement.

Unfinished parent: for BOTH p mod 24 = 13,19 find a full fixed-X=1 evaluation or finite WZ/CM/p-adic identity that forces \(\delta_p=0\) in the signed three-port combination. Related follow-on: investigate universal nonvanishing of L(2/3), using the exact exceptional classification, without diverting from the mother LIFT. Do not repeat the earlier GH-168 special-branch derivative, GH-172 truncated window, GH-174 p^4 tail, or adjacent on-hour Researcher's Euler square-root port.

Control boundary observed on gateway version 0.6.11: research_authority_granted=false; executor_binding_configured=false; 5/5 active job quota; CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. The native original p=373 H0/B0 divided-power, [X]U mod p^2, semilinear Frobenius/eta, signed Green/Hesse, kappa, independent reproduction and Source admission remain owned by canonical authorized execution paths (existing issue #1559; control issue #1558). No own session/CLAIM/OPEN/run/checkpoint/Result/review is asserted here. Logical conversation identity remains stable; prior service identities and protected staging were not modified. Existing original source pins and parent obligation are unchanged.
