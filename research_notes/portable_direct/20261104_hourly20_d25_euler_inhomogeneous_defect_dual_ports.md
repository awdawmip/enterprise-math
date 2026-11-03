# D25 — Exact inhomogeneous Euler defect and two second-digit Gauss ports

Date: 2026-11-04 (+08). Author-side portable algebra, finite exact integer checks. `UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable task publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Research logical lane: `chatgpt-research-hourly-enterprise-math-20260923`. No Source CLAIM/OPEN/checkpoint is asserted. This extends the previously verified mod-p Euler polynomial identity at `bb2ea87c1904e495a1d8f407a7ed586bed9d8478`, retaining rather than re-proving that scientific front.

## New theorem: an exact inhomogeneous polynomial lifting equation

Let p>=5 be prime with p mod 8 in {5,7}. Write q=floor(p/8), h=(p+1)/2, and define the integer tuple

- p=8q+5: (a,b,c,d)=(5q+3,7q+4,q,3q+1);
- p=8q+7: (a,b,c,d)=(7q+6,5q+4,3q+2,q).

Thus a+b=(3p-1)/2, c+d=(p-3)/2 and a+d=b+c=p-1.
In Z[z] define

H(z)=sum_{k=0}^{min(a,b)} binom(a,k)binom(b,k) z^k,
J(z)=sum_{k=0}^{q} binom(c,k)binom(d,k) z^k,
Y(z)=(1-z)^h J(z),  E(z)=(H(z)-Y(z))/p.

The previously proved mod-p Euler equality H=Y mod p shows that **E is an integer polynomial**. All polynomial degrees are <p.

Define the original terminating H differential operator

L_H = z(1-z) d²/dz² + [1+(a+b-1)z] d/dz - ab.

**Theorem (exact over Z[z]):**

    L_H Y(z) = -p h (1-z)^(h-1) J(z),
    L_H E(z) =  h (1-z)^(h-1) J(z).

In particular E(0)=0 and, with E=sum e_k z^k and
w_k=[z^k](1-z)^(h-1)J(z), it satisfies the exact coefficient recurrence

    (k+1)^2 e_(k+1) - (k-a)(k-b)e_k = h w_k.       (1)

Equation (1), initialized by e_0=0, determines E coefficient-by-coefficient. For 0<=k<h+q<p its denominator (k+1)^2 is a p-adic unit, so it also computes E mod p *without constructing or dividing H-Y*. The coefficients w_k are finite binomial convolution coefficients. The final e_(h+q) may be nonzero and is retained.

### Proof

The terminating Gauss equations for H and J are

    L_H H=0,
    L_J J=0,
    L_J=z(1-z)d²/dz² + [1+(c+d-1)z]d/dz -cd.

Let f=(1-z)^h. The product rule gives L_H(fJ)/f, after subtracting L_J J, a J' coefficient of (a+b-c-d-2h)z=0. The remaining J coefficient is

    [-h+h(h-a-b)z]/(1-z) -ab+cd.

Using a+b=h+p-1 and c=p-1-b, d=p-1-a, we get ab-cd=(p-1)h. The coefficient simplifies to -ph/(1-z); hence L_H Y=-ph(1-z)^(h-1)J. Reducing modulo p, Y and H solve the same normalized recurrence (k+1)^2 u_(k+1)=(k-a)(k-b)u_k and share u_0=1. Since all degrees are <p, this proves coefficientwise H=Y modulo p, so E belongs to Z[z]. Subtracting L_H Y from L_H H and dividing by p proves the second identity. Coefficient extraction gives (1). No input theorem beyond the stated terminating binomial recurrences is assumed.

## Two exact original Gauss-port identities

Put z0=1/9, u=8/9, and theta=z d/dz. Let the **original** (not substituted) p-adic Gauss polynomial be

    F_p(z)=sum_{k=0}^{p-1} ((1/8)_k (3/8)_k/(k!)²)z^k,
    G_p(z)=(1+16 theta)F_p(z).

Work in Z_(p)[z]. Because (-a,-b)=(1/8,3/8) modulo p, the **original-source correction**

    A_p(z)=(F_p(z)-H(z))/p

belongs to Z_(p)[z], including its original one-p-factor band and two-p-factor tail. A_p is distinct from the Euler integer carry E; do not merge their source labels before the intended readout.

The exact identities at z0 are

    F_p(z0)=u^h J(z0)+p[E(z0)+A_p(z0)],           (2)

    G_p(z0)=u^h[(16/9)J'(z0)-p J(z0)]
            +p(1+16 theta)[E+A_p](z0).          (3)

To prove (3), apply (1+16 theta) to H=(1-z)^h J+pE. The J coefficient is 1-(1+16h)z, and 1+16h=9+8p. At z=1/9 this becomes -8p/9 and produces the required **-p J** term exactly. Adding the original coefficient correction p A_p gives (2)-(3).

Both (2)-(3) are exact equalities in Z_(p), hence also mod p². In the empirically selected F-vanishing branch (p mod24 in {13,23}), when J(z0)=0 mod p, the second digit is the explicitly distinct residue

    F_p(z0)/p = u^h [J(z0)/p] + E(z0)+A_p(z0)       (mod p).

In the empirically selected G-vanishing branch (p mod24 in {5,7}), when J'(z0)=0 mod p,

    G_p(z0)/p = u^h[(16/9)J'(z0)/p - J(z0)]
                +(1+16 theta)(E+A_p)(z0)           (mod p).

These are **conditional second-digit certificates**, not an all-prime proof of the residue-class selector or of its cancellation. The two displayed source corrections are separately necessary until a stronger observer-safe collapse has been established.

## Exact checks, source separation and conclusions

The attached standard-library Python checker was executed against all 157 primes 5<=p<=2000 with p mod8 in {5,7}. It performs 157 direct original Gauss p² checks, dual Euler-port reductions, and an independent mod-p computation of E and its weighted port by inverting (1). On all 28 selected primes p<=251 it separately constructs integer polynomials and tests the **exact integer** recurrence coefficientwise (not merely congruences).

Results: PASS 157 scalar/original checks; PASS 28 exact polynomial checks. Example rows are
(p, E(z0), (1+16theta)E(z0), A_p(z0), (1+16theta)A_p(z0)) mod p:
(13,2,11,5,10), (23,22,7,7,14), (29,6,16,25,12), (373,199,87,298,242).
The source branches used for additional p² checks are finite observed patterns, not universal evidence. Original hypergeometric coefficients are independently constructed in the checker; no original/native experiment is claimed.

**BRC resolution: COMPOSE_APPLIED.** Population: original k=0..p-1 Gauss terms; binomial H and q-degree J are separate transformed branches. The observers are F_p(z0) and (1+16theta)F_p(z0), precision p². Exact repair coordinates E and A_p retain the Euler Frobenius carry and original numerator-shift provenance; the second observer also retains -p J. Equations (1)-(3) certify recovery for these exact observers and horizon, not arbitrary future jets, tail couplings, or the native D24 LIFT.

**Next exact scientific action:** Use (1) to compute E and E' from the low J source with explicit branch choices, and identify an algebraic symmetry/CM certificate for J(z0)=0 when p mod24 in {13,23} and J'(z0)=0 when p mod24 in {5,7}. Then discharge the corresponding second-digit E+A_p cancellation, keeping the frozen mother D24 Delta_p−R_p and the independent signed 216–2304 p³ comparison. Native Source, claim/run/review/admission remain unverified and unchanged.
