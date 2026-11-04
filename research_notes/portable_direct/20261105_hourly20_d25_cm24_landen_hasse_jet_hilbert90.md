# D25 / CM−24: the split Hasse first-jet Hilbert-90 residual line

Date 2026-11-05. Status **AUTHOR-PROVED THEOREM / EXACT FINITE CHECKED / UNREVIEWED / NOT_ADMITTED**. Scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Read this with the two same-date author-side CM−24 Frobenius/isogeny notes; none substitutes the native H0/B0 source.

## Definitions and theorem

Let p≥5 be any prime with p≡5 (mod 24), m=(p−1)/2 and

    H_p(z)=Σ_{j=0}^m binom(m,j)² z^j ∈Fp[z].

Let a²=2 in F_(p²), a^p=−a. Let b²=3 with b^p=−b, use the exact CM−24 labelled s=3+2e a+d(2b+eab) and t=s². The prior exact identity is

    s^p = r := (1−s)/(1+s),       t^p = r².

Denominators 2, s, 1±s, t, 1±t and H_p(t) are nonzero: Q(t) evaluated at 0,±1 is 1,16,576; the split CM curve has ordinary reduction by the Deuring/previous Hasse selection theorem.

Define the Hasse jet D=H'_p(t)/H_p(t) and the explicit rational candidate

    D_0(t) = −(1+2t−7t²)/[16t(1−t)(1+t)].

**Theorem 1 (Landen Hasse first jet).** The cyclic 2-isogeny E_t→E_(t^p) with differential scaling ρ=i(1+s), i²=−1∈Fp (p≡1 mod4), yields

    H_p(s²) = (1+s)^(p−1) H_p(r²).

This standard finite Hasse invariant covariance is also the polynomial Landen identity for these p; it can be proved by extracting the coefficient x^(p−1) in (x(x−1)(x−t))^m and transporting the invariant differential under the explicit separable 2-isogeny. Since m is even, the coefficient is exactly H_p(t) (no sign). Differentiating this **polynomial** identity in Fp[s], then dividing by H_p(t), gives the exact Frobenius first-jet equation

    2s D(t)+4r/(1+s)² D(t)^p = −1/(1+s).            (L)

Here r=(1−s)/(1+s), D(t)^p=D(r²); the derivative of (1+s)^(p−1) contributes −1/(1+s) in characteristic p.

**Theorem 2 (explicit affine Hilbert-90 reduction).** D_0 satisfies the same inhomogeneous equation (L); this is a rational identity over Q(s):

    2s D_0(s²)+4r/(1+s)² D_0(r²)+1/(1+s)=0.

Therefore the residual δ=D(t)−D_0(t) obeys

    δ^p = −s(1+s)^3/[2(1−s)] δ.                     (H90)

Let g=a(1−s)/(1+s)². Since a^p=−a, s^p=r and (1+r)=2/(1+s), one directly computes

    g^p/g = −s(1+s)^3/[2(1−s)].

Since g≠0, every solution of (H90) in F_(p²) is g times a unique c_p∈Fp:

    BOXED: D(t)=D_0(t)+c_p a(1−s)/(1+s)²,   c_p∈Fp.     (R)

Thus the split-class Hasse derivative target from the previous note, equivalent to J'_p(1)=0, is **precisely the single scalar equation c_p=0**. The Landen isogeny/Hasse covariance alone leaves a one-dimensional Fp residual fiber. This fiber is a legitimate, explicitly retained BRC first-jet observer, not an inferred vanishing theorem.

Proof of the Hasse covariance: in characteristic p, for a separable elliptic isogeny φ with φ*ω'=ρ ω, the Hasse coefficient as a section of ω^(p−1) transforms by H(E,ω)=ρ^(p−1)H(E',ω') (same choice of differential normalization). Our prior exact rational 2-isogeny and ρ=i(1+s), together with i^(p−1)=1, give the displayed factor. Equivalently it can be checked as the finite binomial Landen polynomial identity. All other claims follow by the explicit differentiation and field algebra above.

## Exact checks and evidence

The accompanying Python 3 standard-library checker used F_(p²)=Fp[a]/(a²−2), exact modular inverse, and direct binomial evaluations of H and H'. It examined **all 281** split primes 5≤p≤20000, p≡5 (mod24), including 281 value Landen identities, 281 differentiated identities, 281 typed H90 tests and 281 residual scalars. It found **c_p=0 for each of the 281 tested primes**. Thus universal c_p=0 remains a precise open conjecture, now with a one-dimensional obstruction certificate. For example at p=29, choose sqrt6=8 and s=(11+10a); D=(3+8a), D0=(3+8a), c=0. At p=5 choose sqrt6=1, D=(1+2a)=D0. A separate exact symbolic rational simplification produced zero for the D0 equation over Q(s).

BRC original labels (e,d), CM j branch, Frobenius s→r, invariant differential ρ, and the nonzero Hilbert-90 residual basis g are maintained explicitly. Taking only the norm or trace of D would erase the c_p observer. This author-side CM certificate is not an authenticated original-class H0/B0 crystalline [X]U/eta/kappa or a native p=373 experiment.

## Next action

Identify the CM endomorphism/2-isogeny relation sufficient to force c_p=0 for **all** split primes; equivalently find a finite modular/Hasse derivative certificate selecting the zero residual fiber. Insert the general split first-jet proof into the prior Jacobi–Green–Wronskian p² formula. Independently obtain authenticated fixed-p373 native H0/B0 and Δp−Rp information. Existing Source-authenticated predecessor checkpoint and contributor histories remain intact, with no new native execution authorization or mathematical admission.
