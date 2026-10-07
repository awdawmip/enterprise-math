# P11 standard references and exact applicability

Prepared 2026-10-07 after authorized OPEN `RUN-85b48f2b4121a8b72c6c03a1`, generation 1 (#2959). This is a shared-context support audit, not an independent Driver review. All imported results concern the classical arithmetic facade of the frozen task; they add no native P000 geometry or ontology. Full source bytes remain local and need not be uploaded with the return.

## R1. Integral generalized Nagell–Lutz and Mordell

Hector Pasten, *Diophantine equations with few solutions*, AGRA IV 2021 lecture notes, compiled 14 August 2021, printed/PDF p.7, Theorems 1.5 and 1.6.

- URL: https://indico.ictp.it/event/9617/session/2/contribution/4/material/1/0.pdf
- Local PDF: `ICTP_rational_points.pdf` (377,059 bytes).
- SHA-256: `bbe956e9e6b9dafc837b62eb01af900a95ca8b922b6ef664977131649d15bffe`.
- Retrieved: 2026-10-07 14:14:56 UTC, official ICTP event archive.

**Theorem 1.6 (Nagell–Lutz), precise content.** For a nonsingular integral equation
\[
y^2=x^3+a_2x^2+a_4x+a_6,
\qquad a_2,a_4,a_6\in\mathbf Z,
\]
all affine rational torsion points have integral coordinates. If their ordinate is nonzero, its square divides the **cubic discriminant**. Points with ordinate zero are precisely the points of order two. The cited theorem does not assume a minimal equation and permits an integral quadratic term.

**Theorem 1.5 (Mordell), precise content.** For an elliptic curve over \(\mathbf Q\), its rational group is finitely generated: \(E(\mathbf Q)\cong T\oplus\mathbf Z^r\), with finite torsion group \(T\) and finite nonnegative rank \(r\).

**P11 applicability.** For positive integers \(P>Q\),
\[
E_{P,Q}:\eta^2=\xi(\xi-P^2)(\xi-Q^2)
\]
has integral coefficients \(a_2=-(P^2+Q^2),a_4=P^2Q^2,a_6=0\) and three distinct roots. Its cubic discriminant is
\[
\delta=P^4Q^4(P^2-Q^2)^2\ne0;
\]
the elliptic Weierstrass discriminant is \(16\delta\). Thus Theorem 1.6 applies directly, without a short-Weierstrass coordinate change.

For the fixed core \((r,s)=(11,8)\), \(P=233,Q=119\). Once the exact checker verifies
\[
H=(194089,69872040)\in E_{233,119}(\mathbf Q),
\]
the non-torsion certificate is especially short: \(5\mid69872040\), whereas \(5\nmid233\cdot119\cdot(233^2-119^2)\), so \(5\nmid\delta\). This contradicts \(\eta(H)^2\mid\delta\) if \(H\) were torsion. The point is not of order two since its ordinate is nonzero. Hence \(H\) has infinite order; Mordell then implies \(r\ge1\), without determining the exact rank.

**Limits.** Integral coordinates alone do not imply torsion. A nonintegral affine coordinate of a finite multiple is another valid non-torsion certificate, but it is unnecessary for this witness. Neither theorem yields a complete generator list, a uniform rank bound in the core, an algorithm guaranteed to finish every rank computation, or primitive integer reconstruction.

## R2. Rational two-division and full-two-torsion Mazur list

Boris M. Bekker and Yuri G. Zarhin, *The divisibility by 2 of rational points on elliptic curves*, arXiv:1702.02255v2, 9 February 2017.

- Versioned record: https://arxiv.org/abs/1702.02255v2
- Versioned PDF: https://arxiv.org/pdf/1702.02255v2
- Local PDF: `Bekker_Zarhin_1702.02255.pdf` (368,067 bytes); downloaded from the unversioned PDF endpoint, whose saved title page identifies v2.
- SHA-256: `7e9674695454557d58233417151459398bc061b474df57e369eed8f444dff01a`.
- Saved: 2026-10-07 14:11:27 UTC.

**Theorem 2.1, p.2.** Suppose \(\operatorname{char}K\ne2\), \(\alpha_1,\alpha_2,\alpha_3\in K\) are distinct, and \(E:y^2=\prod_i(x-\alpha_i)\). An affine point \((x_0,y_0)\in E(K)\) lies in \(2E(K)\) if and only if all three \(x_0-\alpha_i\) are squares in \(K\). Zero counts as a square; affine two-torsion is included. Equations (3)–(8), pp.3–4, provide explicit halves with square-root signs satisfying \(r_1r_2r_3=-y_0\).

**Theorem 4.2, p.7.** As a consequence of Mazur's theorem, any noncyclic rational torsion subgroup is
\[
\mathbf Z/2\oplus\mathbf Z/(2m),\qquad m\in\{1,2,3,4\}.
\]
Full rational two-torsion therefore gives exactly the candidate list
\[
(2,2),\quad(2,4),\quad(2,6),\quad(2,8),
\]
where \((a,b)\) means \(\mathbf Z/a\oplus\mathbf Z/b\).

**P11 applicability.** The distinct roots \(0,Q^2,P^2\) are rational and \(K=\mathbf Q\) has characteristic zero. Thus both stated results apply. The theorem is a divisibility test for an already given point, not by itself a complete two-Selmer computation or rank determination.

## R3. Strong Fermat descent statement

Chris Smyth, *Maths 4 Number Theory Notes 2012*, University of Edinburgh, §7, Theorem 7.1, printed/PDF p.25.

- URL: https://webhomes.maths.ed.ac.uk/~chris/NTh/Number_Theory_Notes2012.pdf
- Local PDF: `Edinburgh_Number_Theory_2012.pdf` (346,762 bytes).
- SHA-256: `ee12af77e50bb0c36115eec4eee7c14369e72387267c112b38446cc9bfc5611a`.
- Saved: 2026-10-07 14:16:48 UTC, author's university page.

The theorem states that \(a^4+b^4=c^2\) has no positive integer solution. The displayed proof is credited to H. Davenport, *The Higher Arithmetic*, Longmans, 1952, p.162. This stronger exponent-four descent statement is the exact input; the weaker assertion \(a^4+b^4\ne c^4\) would not be enough.

## R4. Uniform torsion consequence, proved from R2–R3

Use the task's primitive Euclidean core:
\[
A=r^2-s^2,\ B=2rs,\ C=r^2+s^2,\quad
P=A+B,\ Q=|A-B|,
\]
where \(r>s>0\), \(\gcd(r,s)=1\), and \(r,s\) have opposite parity. Then \(A,B>0\), \(\gcd(A,B)=1\), \(A^2+B^2=C^2\), and \(P>Q>0\).

By R2, the two-torsion points \((0,0)\) and \((Q^2,0)\) cannot be twice rational points, because respectively \(-P^2\) and \(Q^2-P^2\) would need to be rational squares. The point \((P^2,0)\) is divisible by two precisely when
\[
P^2-Q^2=4AB
\]
is a rational square. That would make the integer \(AB\) a square. Coprimality would force \(A=a^2,B=b^2\) with positive integers \(a,b\), giving \(a^4+b^4=C^2\), prohibited by R3. No nonzero two-torsion point is divisible by two, so no point of order four exists.

The full-two-torsion Mazur list therefore reduces uniformly to
\[
E_{P,Q}(\mathbf Q)_{\rm tors}\cong
\mathbf Z/2\oplus\mathbf Z/2
\quad\text{or}\quad
\mathbf Z/2\oplus\mathbf Z/6.
\]
This does not exclude rational three-torsion, does not claim that both possibilities occur in the core family, and does not settle a uniform classification of primitive P11 solutions. Exact birational maps, parity, denominator clearing, root-gcd normalization, and distinct primitive reconstruction remain the task-specific proof components.

The earlier local `REFERENCE_APPLICABILITY.md` also records optional real-group and birational-curve references. No real-topology density result is needed as a dependency of this final compact reference set.

## R5. Torsion injection at good reduction

Bjorn Poonen, *Elliptic Curves*, author-hosted text dated 25 July 2001; published in J.P. Buhler and P. Stevenhagen (eds.), *Algorithmic number theory: lattices, number fields, curves and cryptography*, MSRI Publications 44, Cambridge University Press, 2008, pp.183–207. Exact locator: §6.5, unnumbered theorem, printed/PDF p.10.

- URL: https://math.mit.edu/~poonen/papers/elliptic.pdf
- Local PDF: `Poonen_elliptic.pdf` (344,773 bytes).
- SHA-256: `942986e154c57544ab20d7a88e7cc9c7eede63cb6e0bf3173430cfc5ed4e7e74`.
- Saved: 2026-10-07 14:11:27 UTC, author's MIT page.

**Exact content.** If an elliptic curve over \(\mathbf Q\) has good reduction at a prime \(p>2\), reduction injects its rational torsion subgroup into \(E(\mathbf F_p)\). Thus in particular its prime-to-\(p\) torsion injects. The printed theorem gives the stronger full-torsion assertion at odd primes, rather than only the latter restricted statement.

**Fixed-core application.** At \((P,Q)=(233,119)\), the integral model has discriminant prime to five, so it has good reduction at five. Its reduced equation is
\[
\eta^2=\xi(\xi-4)(\xi-1)\pmod5.
\]
For \(\xi=0,1,2,3,4\), the respective affine solution counts are \(1,1,2,2,1\); adding the point at infinity gives \(\#E(\mathbf F_5)=8\). The three-primary part of rational torsion therefore vanishes even using only the prime-to-five injection. Combined with R4's two remaining possibilities, this proves
\[
E_{233,119}(\mathbf Q)_{\rm tors}\cong\mathbf Z/2\oplus\mathbf Z/2.
\]
This fixed-core reduction does not rule out three-torsion for every Euclidean core and supplies no uniform rank result.
