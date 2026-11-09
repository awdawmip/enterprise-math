# D25 — W216 original terminal coefficient and sharp p⁴ Picard–Fuchs boundary

Date: 2026-11-10. Status: **AUTHOR_SIDE / EXACT_ELEMENTARY_PROOF / 11-PRIME INDEPENDENT REGRESSION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Scientific input frozen at `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research conversation: `chatgpt-research-onhour-enterprise-math-20260923`; not the Maintenance lane. This is a **new author-side boundary/precision certificate for the original weighted 216-model coefficients**, not the native H0/B0 experiment, a Result, or proof of LIFT.

## Exact statement and operator

Let p>3 be prime and work in Z_(p). For 0<=k<p define

[
c_k=rac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}
    =rac{inom{2k}{k}^{,2}inom{3k}{k}}{108^k},
qquad F_p(z)=sum_{k=0}^{p-1}c_kz^k.
]

The original weighted model is `W_p=[(1+6 theta)F_p(z)]_{z=1/2}`, with `theta=z d/dz`. Its p-local finite operator is

[
mathcal L=	heta^3-z(	heta+	frac12)(	heta+	frac13)(	heta+	frac23).
]

**Theorem (all primes p>3).** Exact valuation and first terminal unit:

[
v_p(c_{p-1})=3,qquad rac{c_{p-1}}{p^3}equiv-1pmod p.
	ag{1}
]

The finite Picard–Fuchs equation has one exact endpoint forcing term:

[
mathcal L F_p(z)
=-c_{p-1}(p-	frac12)(p-	frac23)(p-	frac13)z^p
equiv-rac{p^3}{9}z^p pmod{p^4}.
	ag{2}
]

Consequently at the frozen original z=1/2,

[
[mathcal L F_p](1/2)/p^3equiv-1/18pmod p.
	ag{3}
]

The actual **last weighted W coefficient** (k=p-1, z=1/2) is

[
(6p-5)c_{p-1}2^{-(p-1)}
equiv5p^3pmod{p^4}.
	ag{4}
]

For the target primes p≡13,19 (mod24), p>=13, (3) and (4) are both nonzero modulo p after dividing p³. Thus the finite ODE is homogeneous through p³, but the **first omitted p⁴ digit is a fixed, signed, source-preserving boundary**, and truncation of W at p-2 versus p-1 is safe mod p³ but not mod p⁴.

## Proof

For a numerator factor `(r/d)_(p-1)`, with (r,d)=(1,2),(1,3),(2,3), write

[
(r/d)_{p-1}=d^{-(p-1)}prod_{j=0}^{p-2}(dj+r).
]

Precisely one factor `dj+r=mu p` occurs in this range, of valuation one. All other factors are the distinct nonzero residues modulo p, except the omitted index j=p-1 whose residue is r-d. Wilson and Fermat give

[
rac{(r/d)_{p-1}}pequivrac{mu}{d-r}pmod p.
]

For (r,d)=(1,2), mu=1. For (1,3),(2,3), the pair of values is (1,2) if p≡1 (mod3) and (2,1) if p≡2 (mod3); the product of the three normalized units is
`1 * (mu_1/2) * mu_2=1`. Since `(p-1)! ≡ -1 (mod p)`, division by `((p-1)!)^3` yields (1) and exact valuation three.

For every n=1,...,p-1, the Pochhammer recurrence gives

[
n^3c_n=(n-1+	frac12)(n-1+	frac13)(n-1+	frac23)c_{n-1}.
]

The constant coefficient also vanishes under `L`; the only unmatched coefficient is that of z^p, giving the **exact** finite identity in (2). Substituting (1) and reducing the three terminal factors modulo p gives the coefficient `-1/9` modulo p. Finally Fermat implies `2^{-p} ≡ 1/2 (mod p)` and `2^{-(p-1)} ≡ 1 (mod p)`; thus (3) and (4) follow.

All reductions and divisions by p are taken in their stated order. The nonzero obstruction concerns the ODE at p⁴, not the value of `W_p-p` at p³.

## Executed exact checks and reuse value

The independent standard-library checker `research_notes/portable_direct/d25_W216_terminal_boundary_20261110.py` computes `c_k` by a modular Pochhammer recurrence and **independently** by integer binomial coefficients. It checks every polynomial coefficient of `L F_p`, including the z^p coefficient and the two z=1/2 readouts, mod p⁴. Executed: p=5,7,11,13,17,19,23,37,43,73,373; 11/11 PASS. At p=373 the normalized residual forcing coefficient is 290 mod373, at z=1/2 it is 145 mod373. These finite checks are a regression; the above argument is the theorem proof.

This is a BRC source/observer audit: preserve the original k=p-1 branch, p-valuation three, sign, weighted readout and the post-differentiation boundary; reducing the terminal c modulo p³ before applying the operator erases the p⁴ forcing. No claim is made about the native rank, Frobenius/eta, kappa, the p373 original `Delta=R=196` port, or proving the two-class universal `Delta_p-R_p=0`.

## Durable continuation

Highest canonical Source continuation read: request `onhour11-20261110-0500-current-continuation`, SUCCEEDED, observed 2026-11-09T21:02:50Z, Source commit `cb21c9452f5bc094493cd92bfa37be99ab988782`; route requests genuine Researcher capability and CLAIM. Own recovery status attempt returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`. No own winning CLAIM/run is verified, and no Source checkpoint is published.

Mother target remains original two-class LIFT `Delta_p-R_p`. The **highest native missing unit** remains same-original-class H0/B0 divided-power `[X]U mod139129` at p373, module rank, semilinear Frobenius, eta, signed kappa, Delta-R and independent reproduction; support Issue #1559 is OPEN, responsible executor PENDING_OWNER. Prior accepted UR, prior Source checkpoint units, signed Green/Hesse branch and frozen original inputs remain intact.

Next math-only action if an authorized portable unit is selected: use the explicit p³ terminal forcing to audit a finite WZ/Picard–Fuchs telescoping certificate for the exact original `(W_p-p)/p²`, retaining z^p boundary, without re-proving UR or rerunning broad prime scans. **No known native experimental acceptance is implied.**
