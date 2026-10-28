# D25/LIFT GH-31 — birational elliptic carrier of the missing G-port square-fiber residual

2026-10-28. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. GH-31 extends the author-side GH-29/GH-30 F/G source-preserving partition; it is not an admitted Result, native Source checkpoint, independent review or proof of original W/S.

Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, Objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Current Research logical lane chatgpt-research-hourly-enterprise-math-20260923 is distinct from maintenance.

## A genuine source-preserving elliptic bridge

Let p=8m+3>=19 prime, k=F_p, chi the quadratic character including zero, and retain the exact original GH-22 G weight

\[
h_G(x)=\chi(x)[x(x+1)]^{3m+1}(1+9x)^{m-1}(5-9x).
\]

The GH-29 **signed square-fiber residual** B_p is the sum of h_G(x) over original x whose quotient parameter v=(1+9x)/(9x(x+1)) is a nonzero square. It is NOT the full G source or an F-to-G scalar transfer. Define the elliptic curve already identified in GH-25:

\[
E:\quad y^2=x(x+1)(9x+1).
\tag{31.1}
\]

**Theorem A (root-choice-free E point moment).** The *exact original* residual satisfies

\[
\boxed{B_p=\frac12\sum_{(x,y)\in E(k),\,y\ \mathrm{affine}} h_G(x).}
\tag{31.2}
\]

Equivalently,

\[
B_p=\frac12\sum_{x\in k}
\bigl(1+\chi(x(x+1)(9x+1))\bigr)h_G(x).
\tag{31.3}
\]

This retains both the original x label and the G channel; it is a **weighted** elliptic moment, not merely a point count or a CM trace.

**Proof.** For x outside {0,-1,-1/9}, the quadratic characters of v and Q(x)=x(x+1)(9x+1) agree, since v=Q(x)/(9x^2(x+1)^2). Hence v is a square iff Q(x) is a nonzero square. Exactly then E has two rational points (x,+y),(x,-y), both carrying the same h_G(x). If Q(x) is nonsquare, E has no point with that x. At the three Q roots E has one affine point y=0, but h_G(x)=0 because m>=2. Thus the half-weighted full affine E sum is exactly the original square-fiber source sum. QED.

**Theorem B (explicit quartic birational model).** Let

\[
C:\quad \delta^2=9z^4-14z^2+9
\tag{31.4}
\]

and remove the z=0 points. The following are **mutually inverse** rational maps on the indicated open loci:

\[
\boxed{z=\frac{y}{3x(x+1)},\qquad
\delta=(6x+3)z^2-3}
\quad
E(k)\setminus\{O,(0,0),(-1,0),(-1/9,0)\}
\longrightarrow C(k)_{z\ne0},
\tag{31.5}
\]

\[
\boxed{
x=\frac{\delta+3}{6z^2}-\frac12,\qquad
y=3x(x+1)z}
\quad
C(k)_{z\ne0}\longrightarrow E(k)\setminus\{O,\text{three 2-torsion points}\}.
\tag{31.6}
\]

Here O is E's projective point at infinity. Under this bijection z^2 equals the **exact original quotient** v, and the GH-29 quadratic-fiber root t equals x+1:

\[
z^2=\frac{1+9x}{9x(x+1)},\qquad
t=\frac{3(z^2+1)+\delta}{6z^2}=x+1.
\tag{31.7}
\]

**Proof.** Squaring z in (31.5) and using E's defining equation immediately gives the first relation in (31.7). Rewriting its exact quadratic-fiber equation in t=x+1 yields
\[
9z^2t^2-9(z^2+1)t+8=0.
\]
Its discriminant is 9(9z^4-14z^2+9), and direct substitution of delta=(6x+3)z^2-3 gives (31.4). Conversely (31.4) and (31.6) imply the quadratic relation and then E's defining equation. There are no excluded extra affine points for p>3: z=0 on C corresponds to excluded E branches, and the original x=0,-1,-1/9 each has y=0. Applying either map after the other gives the identity on these open loci. QED.

**Consequences (exact).** For p>3, C is a nonsingular genus-one quartic (the derivative and polynomial have no common root since the discriminant of 9v²-14v+9 is -128). This is the **same birational elliptic carrier** as the proven non-CM E of GH-25, not a new CM curve. In particular, GH-25's 8 | #E(k) gives the exact affine count

\[
\#C(k)_{z\ne0}=\#E(k)-4\equiv4\pmod 8.
\tag{31.8}
\]

Moreover the GH-29 discriminant expression is a *complete* elliptic/quartic weighted source reconstruction:

\[
\boxed{
B_p=\frac{9^{m+1}}{16}
\sum_{\substack{z\in k^\times,\;\delta\in k\\
\delta^2=9z^4-14z^2+9}}
z^{2m-2}\chi\!\left(\frac{3(z^2+1)+\delta}{6z^2}\right)\delta.
}
\tag{31.9}
\]

For each occupied square quotient fiber there are four pairs (z,delta) over its two original x roots. Changing delta reverses the root and chi(t), leaving the product chi(t)*delta invariant; changing z to -z leaves z^{2m-2} unchanged. Thus the 1/16 coefficient is correct, not an unverified symmetry multiplier.

## Exact check and boundaries

The companion standard-library checker independently enumerated both E and C rational points, proved the two explicit maps invert each other pointwise, verified the exact original x-source classification, and computed B_p from (31.2), (31.3) and (31.9) for **all 75 primes 19<=p<2001, p=3 mod8**. All passed. Examples (p,B_p,#E affine,#C with z!=0): (19,8,15,12), (43,37,47,44), (67,47,63,60), (83,5,79,76). These finite checks support, but do not replace, the algebraic proof. No separate native p=373 experiment was performed.

BRC COMPOSE_APPLIED: source population is original labeled x, with two signed G roots and elliptic y sheet; observer is the original full G weighted sum, not a positive point count. The elliptic point moment is an **exact repaired observer**, while collapsing it to #E or GH-28's F-only Legendre scalar would erase the signed G source. Auxiliary elliptic coordinates are not native X6 spatial axes; the ACTIVE P000 6+1 basis is unchanged.

Open: universal class-19 F/Legendre vanishing, a closed arithmetic evaluation of the weighted E moment B_p, GH-15/20/21 coupling, original H0/B0, six Hasse ports, [X]U mod p², Frobenius eta/kappa, native p=373 and independent Driver review. Next smallest unit: investigate whether the weighted E moment admits a finite-character or higher-isogeny correspondence **without** falsely using a CM trace; alternatively produce a prime-specific obstruction. Exact E source, y sheet, x label, G port and endpoints must be retained.

Control boundary: current connected Site gateway version 0.6.11 still has research_authority_granted=false and no write relay, with no fresh Source winning own claim/open. Historical identity/session, staging and requests remain untouched. Existing owner support is enterprise-math#1558. GitHub files are portable author evidence only, REGISTER_PENDING. Existing scheduled task was not modified.
