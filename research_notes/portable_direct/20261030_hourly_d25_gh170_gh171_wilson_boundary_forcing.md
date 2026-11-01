# D25/LIFT GH-170–GH-171 — exact Wilson boundary forcing for truncated Gauss and Clausen operators

2026-10-30 Asia/Hong_Kong. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Logical Research conversation chatgpt-research-hourly-enterprise-math-20260923, not maintenance. P000 and ACTIVE native worldview preserved. This is auxiliary classical arithmetic, not an X6/native H0/B0 theorem.

## Exact objects and frozen scope

Let p>5 be prime, theta=X d/dX, and all rational coefficients be p-local. Define

\[
b_n=\frac{(1/6)_n(1/3)_n}{(n!)^2\,2^n},\quad
a_n=\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3\,2^n},
\quad G_p(X)=\sum_{n=0}^{p-1}b_nX^n,\quad
F_p(X)=\sum_{n=0}^{p-1}a_nX^n.
\]

The original weighted-216 scalar is precisely \(A_p=(1+6\theta)F_p(1)\) for \(p=6m+1\) with \(p\bmod24\in\{13,19\}\), at the fixed parameter \(X=1\). Consider the exact differential operators

\[
L_2=\theta^2-\frac X2(\theta+\tfrac16)(\theta+\tfrac13),\qquad
L_3=\theta^3-\frac X2(\theta+\tfrac12)(\theta+\tfrac13)(\theta+\tfrac23).
\]

## GH-170 — a sharp nonhomogeneous Gauss equation

For every prime \(p\equiv1\bmod6\), \(p\ge7\), the following holds as a **polynomial** congruence:

\[
\boxed{L_2G_p(X)\equiv-\frac{p^2}{36}X^p\pmod{p^3}.}\tag{G1}
\]

For \(p\equiv5\bmod6\), \(p\ge11\), the coefficient is instead \(-5p^2/18\). The boundary has exact p-adic valuation two, so \(G_p\) solves the homogeneous equation modulo \(p^2\) but not modulo \(p^3\).

**Proof.** From
\[
b_{n+1}/b_n=(6n+1)(3n+1)/(36(n+1)^2)
\]
all coefficients through degree \(p-1\) of \(L_2G_p\) vanish exactly. The only remaining coefficient is
\[
L_2G_p=-\frac{(6p-5)(3p-2)}{36}\,b_{p-1}X^p.\tag{G2}
\]
For \(p>5\), if \(r,s\) are p-units and precisely one entry \(sj+r\) for \(0\le j\le p-2\) equals \(qp\), the other entries run through every nonzero residue except \(r-s\). Wilson and Fermat yield
\[
(r/s)_{p-1}/p\equiv q/(s-r)\pmod p.\tag{W}
\]
For \(p=6m+1\), the divisible entry in both \((1/6)_{p-1}\) and \((1/3)_{p-1}\) is \(p\). Formula (W) yields units \(1/5\) and \(1/2\), respectively. As \(((p-1)!)^2 2^{p-1}\equiv1\bmod p\),
\[
\boxed{b_{p-1}\equiv p^2/10\pmod{p^3}.}
\]
Substitution into (G2) gives (G1), and \(36\) is invertible. For \(p=6m+5\ge11\), the divisible entries are \(5p\) and \(2p\), so \(b_{p-1}/p^2\equiv1\bmod p\) and the alternative coefficient follows. QED.

## GH-171 — one-higher exact cubic Clausen boundary

For every prime \(p>5\),

\[
\boxed{L_3F_p(X)\equiv-\frac{p^3}{18}X^p\pmod{p^4}.}\tag{C1}
\]

Thus the cubic truncation satisfies the homogeneous equation modulo \(p^3\) but has a nonzero source modulo \(p^4\). It is not valid to transport the Gauss homogeneous approximation from modulo \(p^2\) to modulo \(p^3\).

**Proof.** The exact recurrence
\[
a_{n+1}/a_n=(2n+1)(3n+1)(3n+2)/(36(n+1)^3)
\]
cancels all cubic operator coefficients through degree \(p-1\), leaving
\[
L_3F_p=-\frac{(2p-1)(3p-2)(3p-1)}{36}\,a_{p-1}X^p.\tag{C2}
\]
Use (W) for \((1/2)_{p-1},(1/3)_{p-1},(2/3)_{p-1}\): if \(p=1\bmod6\), the normalized units are \(1,1/2,2\); if \(p=5\bmod6\), \(p>5\), they are \(1,1,1\). The product in either case is one. Wilson gives \(((p-1)!)^3\equiv-1\bmod p\), hence
\[
\boxed{a_{p-1}\equiv-p^3\pmod{p^4}.}
\]
Reducing (C2)'s prefactor modulo p gives \(-1/18\); combining signs yields (C1). Nonzero for \(p>5\). QED.

## Observer preservation and verification

The source \(X^p\) is not zero as a polynomial. For the frozen class its Gauss coefficient \(-p^2/36\) survives modulo \(p^3\), while its first formal derivative \(-p^3X^{p-1}/36\) vanishes modulo \(p^3\). Therefore pointwise Fp evaluation, first derivative and second-digit polynomial differential observation are different typed observers. Preserve exponent, p-valuation, boundary coefficient, source provenance and downstream operation rather than collapsing them. This is an exact arithmetic BRC information-preservation instance, not a native six-axis theorem.

An **actually executed Python standard-library checker** covered all 666 primes \(7\le p<5000\), including all 166 frozen-class primes. It evaluated rational coefficient recurrences modulo \(p^3\) and \(p^4\) and tested both exact boundary formulas and normalized Wilson units. Terminal: PASS_GH170_GH171_WILSON_BOUNDARY_FORCING_EXACT. Finite checks support these instances; the all-prime argument is the recurrence/Wilson proof.

For p=373: \(b_{372}=15582448\pmod{51895117}\) with unit \(b_{372}/373^2=112\); \(a_{372}=19304983524\pmod{19356878641}\) with unit \(372\); coefficient \([X^{373}]L_2G=36034411\bmod51895117\) (unit 259); coefficient \([X^{373}]L_3F=7524791965\bmod19356878641\) (unit 145). No floating-point computation. Companion checker d25_gh170_gh171_boundary_forcing_exact.py, with exact executed local source retained in the attached evidence bundle.

## Scope and next true research frontier

The fixed-parameter scalar hard target
\[
\frac{(1+6\theta)F_p(1)-p}{p^2}\equiv0\bmod p
\]
is still OPEN for the two prescribed residue classes. A boundary forcing coefficient does **not** determine the solution's constant at X=1. Next: construct an actual p-adic connection/summation identity coupling the Gauss boundary source, the already-preserved signed high-tail GH-166/GH-167 three-port combination, and the frozen original weighted216 constant. Test any candidate on p=13,19,157,373; do not repeat previously settled parameter jets or the separate onhour Research lane's ruled-out scalar Gosper equation.

Gateway v0.6.11 observed 2026-10-30: research_authority_granted=false; executor_binding_configured=false; active native jobs 5/5; Source CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. Consequently GitHub author-side durability only, no new native CLAIM, authorized OPEN, Source checkpoint, frozen Result or independent review. Protected old sessions/requests/staging untouched; project issues #1558 and #1559 retain control and original native p373 obligations. Scheduler, notifications, P000 and frozen source pin unchanged.
