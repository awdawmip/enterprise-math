# D25 — Explicit X_0(6) Fricke (6,8) maps, common CM fiber and first-jet gauge

Date: 2026-11-07. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific input: enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3. Consumed frontier: 948d2a02273b7b4db83372b760ff69c5cc3a7c0e (minimal Fricke common cover). Status: AUTHOR_SIDE_PROVED / EXACT_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED. Source identity and task claim remain unverified.

## I. The two **explicit** maps on one rational coordinate

Write eta for Dedekind's eta and define three level-6 modular functions:

[
t=rac{eta(	au)^5eta(3	au)}{eta(2	au)eta(6	au)^5},quad
h_2=left(rac{eta(	au)}{eta(2	au)}ight)^{24},quad
h_3=left(rac{eta(	au)}{eta(3	au)}ight)^{12}.
]

The eta-quotient congruence and square-character criteria give trivial-character weight-zero functions. The cusp-order formula on Gamma_0(6), for denominator d in {1,2,3,6}, is
[
operatorname{ord}_{1/d}(f)=rac6{24gcd(d^2,6)}
sum_{deltamid6}rac{gcd(d,delta)^2r_delta}{delta}.
]
For t, the order tuple (d=1,2,3,6) is (1,0,0,-1), so t is a Hauptmodul for the genus-zero curve X_0(6). The cusp poles of h_2 on X_0(6) are infinity of order 1 and 1/2 of order 3; those of h_3 are infinity of order 1 and 1/3 of order 2.

**Theorem 1.** Exact identities of modular functions on X_0(6):
[
oxed{h_2(t)=rac{t^3(t+8)}{(t+9)^3},qquad
h_3(t)=rac{t^2(t+9)}{(t+8)^2}.}
]
Proof by the modular function divisor principle: the Laurent series at infinity begin
[
t=q^{-1}-5+6q+4q^2-3q^3-12q^4-8q^5+12q^6+cdots,
]
[
h_2=q^{-1}-24+276q-2048q^2+11202q^3-49152q^4+184024q^5-614400q^6+cdots,
]
[
h_3=q^{-1}-12+54q-76q^2-243q^3+1188q^4-1384q^5+cdots.
]
Exact eta-product multiplication establishes that (t+9)^3 h_2-t^3(t+8)=O(q^4) and (t+8)^2 h_3-t^2(t+9)=O(q^3). The first difference has at most 3 possible poles away from infinity (at cusp 1/2); the second has at most 2 (at cusp 1/3). A nonzero modular function has a degree-zero divisor, so the displayed zero orders 4 and 3 force both differences to vanish identically. No numeric interpolation is used as a theorem.

Let the Fricke-invariant Hauptmoduls be u_3=h_3+729/h_3 and u_2=h_2+4096/h_2. Normalize the cusp to hypergeometric variable 0, the order-2 elliptic point to 1, and the order-6 or order-4 point to infinity:
[
z=rac{108}{u_3+54}=rac{108h_3}{(h_3+27)^2},qquad
w=rac{256}{u_2+128}=rac{256h_2}{(h_2+64)^2}.
]
The elliptic assignments follow from the Fricke fixed points h_3=+27,-27 (orders 2,6) and h_2=+64,-64 (orders 2,4), respectively; equivalently check the standard j-maps at the original elliptic loci. Factoring
[
h_3+27=rac{(t+12)^3}{(t+8)^2},qquad
h_2+64=rac{(t^2+36t+216)^2}{(t+9)^3}
]
gives the **same-coordinate degree-(6,8) maps**
[
oxed{z(t)=rac{108t^2(t+9)(t+8)^2}{(t+12)^6},qquad
w(t)=rac{256t^3(t+8)(t+9)^3}{(t^2+36t+216)^4}.}
]
Degrees are 6 and 8 after checking no numerator/denominator cancellation. Cusp and elliptic fibers agree with the previously constructed unramified orbifold cover.

## II. The frozen special arguments occur over exactly the same quadratic fiber

**Theorem 2.** Over an algebraic closure of Q, for finite t away from poles,
[
oxed{z(t)=	frac12;land;w(t)=	frac19iff t^2=72.}
]
Proof: clear the denominators of 2z-1 and 9w-1:
[
P(t)=216t^2(t+9)(t+8)^2-(t+12)^6,
]
[
Q(t)=2304t^3(t+8)(t+9)^3-(t^2+36t+216)^4.
]
Exact Euclidean polynomial gcd over Q[t] gives the monic gcd t^2-72; both roots are non-poles. Hence t=+6sqrt(2),-6sqrt(2) are all common preimages. Their exact first-coordinate Jacobian is
[
oxed{left.rac{dz}{dw}ight|_{t=pm6sqrt2}=pmrac{27sqrt2}{16}.}
]
This resolves the previously open *special-point matching* unit: it is TRUE, not merely an inferred consequence of group indices.

## III. Exact differential gauge, with branch port preserved

Let F_A(z)={}_2F_1(1/6,1/3;1;z), F_B(w)={}_2F_1(1/8,3/8;1;w). Writing a Gauss equation in t as Y''+P(t)Y'+Q(t)Y=0 gives
[
P_X=rac{1-(a+b+1)X}{X(1-X)}X'-rac{X''}{X'},quad
Q_X=-rac{ab}{X(1-X)}(X')^2.
]
For X=z and X=w, exact rational symbolic simplification yields
[
d=rac{P_B-P_A}{2}=rac{6t}{(t+12)(t^2+36t+216)},quad
Q_B=d'+d^2+P_A d+Q_A.
]
As d=(log G)' for G=(t+12)/sqrt(t^2+36t+216), the two pullback differential operators are conjugate by G. Normalizing at the common cusp t=infinity (both Gauss series are 1+O(1/t), G->1) proves the **local analytic germ** identity
[
oxed{F_A(z(t))=G(t),F_B(w(t))quad	ext{near }t=infty.}
]
This is an equation of branch-normalized analytic germs, not an unqualified equality of principal real Gauss values throughout the t-plane.

**Exact branch diagnostic.** On decreasing positive real t, w(t)=1 at t=36+18sqrt(6), whereas z(t)=1 at t=12+12sqrt(3). Each has ramification 2, so continuation through those points changes local square-root branches. At the shared special point t=6sqrt(2), the *formal gauge square* is G^2=1/sqrt(2)<1. However, using positivity of hypergeometric coefficients,
F_A(1/2)>1+1/36, while F_B(1/9)<1+3/512, hence F_A(1/2)^2/F_B(1/9)^2>1. Therefore substitution of the principal real special values into the cusp-germ identity without a connection matrix is rigorously invalid. Prior ~110-digit evidence for A_infty/B_infty=3sqrt(2)/4 is compatible with a nontrivial branch multiplier, but this note does not promote it to a theorem.

## IV. BRC observer, evidence status and next exact action

This is COMPOSE_APPLIED reuse of the two-legged Gauss/Fricke construction and provenance-retaining BRC observer: carrier=(t, branch of sqrt, Gauss solution port, Fricke leg A/B, cusp/elliptic fiber, ramification, derivative, source). Allowed operation is substitution followed by differentiation/analytic continuation; forgetting the branch and using only (z,w) discards exactly the data required for the special-value readout. The common quadratic fiber and the rational Jacobian are exact; the p-adic third-digit lift and the native p373 experiment are not claimed.

Accompanying SymPy checker: `research_notes/portable_direct/d25_fricke_68_explicit_check_20261107.py`. It executes eta-product exact q-coefficients, polynomial gcd and field substitutions, and exact Gauss operator conjugacy. Local execution 2026-11-07: PASS. This is author-side symbolic validation; no independent review or Source admission.

**Smallest remaining unit:** determine the two elliptic crossing/monodromy connection matrices that transport the cusp-normalized solution to the principal positive special point t=6sqrt(2). Test whether the resulting period factor closes the earlier 3sqrt(2)/4 candidate *without* assuming it; only then attempt the finite-truncation p-adic/Frobenius first jet and the conjectural 2V_p-W_p-p(-3/p)=0 mod p^4. Keep original p373 H0/B0/divided-power/Frobenius/Hesse-kappa benchmark (issue #1559) unchanged.

Source request `onhour11-20261106-1400-exact-research-lane-continuation` remains UNKNOWN_NOT_RESENT. This run: em_status, original receipt and reconcile each returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; Site CONFIGURED_NOT_LIVE_VERIFIED, Researcher authority false. Fixed Research conversation `chatgpt-research-onhour-enterprise-math-20260923`, never the maintenance conversation. Session/CLAIM/run not verified; REGISTER_PENDING/SYNC_DEBT, author-side GitHub evidence only.
