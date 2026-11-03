# D25 — Exact Euler reduction of the 2304 first-digit Gauss observers

Date: 2026-11-04 (+08). Author algebraic proof + finite exact checks. UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is portable D25 evidence under Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3, logical Research lane chatgpt-research-hourly-enterprise-math-20260923. Native CLAIM, OPEN and Source checkpoint not established.

## Exact theorem and source

Let p >= 5 be prime, p ≡ 5 or 7 (mod 8); work in F_p. Define the representatives 0 <= a,b,c,d < p by
a = -1/8, b = -3/8, c = -5/8, d = -7/8 (mod p), and h=(p+1)/2.
Write

H(z) = Σ_(k=0)^min(a,b) binom(a,k)binom(b,k) z^k,
J(z) = Σ_(k=0)^min(c,d) binom(c,k)binom(d,k) z^k,
G(z) = H(z)+16zH'(z).

Then the following are **exact polynomial identities in F_p[z]**:

\[
\boxed{H(z)=(1-z)^h J(z),}
\]
\[
\boxed{G(z)=(1-z)^{h-1}\big((1-9z)J(z)+16z(1-z)J'(z)\big).}
\]

In particular, z0=1/9 is a unit point:

\[
\boxed{H(1/9)=(8/9)^h J(1/9),\qquad
G(1/9)=(16/9)(8/9)^h J'(1/9).}
\]

These H and G are the original truncated 2304 Gauss observers F_p and F_p+16 D_p **after modulo-p reduction** of (1/8)_k(3/8)_k/(k!)², k<p. The proof does not change the p² parameter-jet or truncation-tail source obligations.

## Complete proof

For p=8q+5, the exact integer tuple (a,b,c,d,h) is (5q+3,7q+4,q,3q+1,4q+3); thus deg H=5q+3=h+q and deg J=q. For p=8q+7 it is (7q+6,5q+4,3q+2,q,4q+4); thus deg H=5q+4=h+q and deg J=q. In both cases deg((1-z)^h J)=deg H<p, with nonzero leading coefficient.

The terminating binomial sequences satisfy over F_p the Gauss equations

\[
z(1-z)H''+(1-\tfrac32 z)H'-\tfrac3{64}H=0,
\]
\[
z(1-z)J''+(1-\tfrac52 z)J'-\tfrac{35}{64}J=0.
\]

These follow directly from k² u_k=(k-1-a)(k-1-b)u_{k-1}, respectively the (c,d) recurrence, and the terminating numerator zero. Since h ≡ 1/2 (mod p), a direct product-rule substitution shows that (1-z)^h J solves the same first equation as H. Both have constant coefficient 1, and are polynomials of degree <p. For every 1<=k<p the normalized Gauss coefficient recurrence divides by the unit k²; hence the common initial value uniquely determines all coefficients. This proves H=(1-z)^h J.

The G identity follows by applying 1+16z∂_z. Its undifferentiated coefficient is 1-(1+16h)z ≡ 1-9z. At z0=1/9 the J coefficient disappears, leaving the exact derivative readout.

### Ordinary-point zero separation

At z0=1/9 the J equation gives

\[
J''(1/9)=\tfrac{81}{8}(\tfrac{35}{64}J(1/9)-\tfrac{13}{18}J'(1/9)).
\]

For p>=11 in the selected classes, J(z0) and J'(z0) cannot both vanish: the differential equation is ordinary at z0, so repeated differentiation and the invertibility of factorials below degree p would make J identically zero, contradicting J(0)=1. If J'(z0)=0, then J''(z0)=2835 J(z0)/512 ≠ 0 for p>=11 in these classes. The stationary point is simple. The edge primes p=5,7 have J=1, J'=0; the main identities still hold.

## New information / executable certificate

The first-digit observer pair reduces to one polynomial of degree q=floor(p/8) and its derivative. The direct H coefficient count is 5q+4 (p=8q+5) or 5q+5 (p=8q+7), versus q+1 for J; in the second class this is exactly a fivefold reduction in coefficient terms. Actual operations still include source-residue construction, inverse 9, coefficient recurrence and the power (8/9)^h. This is a BRC provenance-preserving finite-field readout for the two declared observers; second-digit and signed-tail ports remain separately carried.

A Python standard-library integer checker compared H,G to reduced J,J' at z0 for all 622 primes p<=10000 with p mod8 in {5,7}; for 28 primes p<=251 it also compared **every polynomial coefficient and all p field-point evaluations** of both identities. All checked identities passed.

The existing residue-class zero selection was observed again in the new reduced coordinate:
309 primes p mod24 in {13,23}: J(z0)=0, J'(z0)≠0;
313 primes p mod24 in {5,7}: J'(z0)=0, J(z0)≠0.
These are exact finite observations, not an all-prime proof. Sample (p,H(z0),G(z0),J(z0),J'(z0)):
(13,0,7,0,4), (23,0,13,0,12), (29,26,0,7,0), (373,0,80,0,369), (2053,0,1686,0,954).

## Continuation

Next: seek an explicit finite-field/CM or p-dependent terminating certificate deciding whether J(z0)=0 for p mod24 in {13,23} and J'(z0)=0 for {5,7}. Discriminate candidates simultaneously at 13,23,29,373,2053; then use the previously established parameter jet/endpoint data for a p² lift. Preserve the separate signed 216–2304 mod p³ comparison and the *frozen* parent D24 scalar LIFT Δ_p−R_p. This author note proves no native parent completion, Result, admission or independent review. Old service session, protected staging and maintenance lane have not been touched.
