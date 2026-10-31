# D25/LIFT — exact finite inverse and non-erasure for the signed-boundary holonomic operator

2026-10-31, second author-side research unit. AUTHOR-DERIVED / EXACT RATIONAL PROOF / EXACT FIELD CHECK / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
Research lane: chatgpt-research-hourly-enterprise-math-20260923; no maintenance identity borrowed.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen science Source c47e13e4aba0e006366f989d6334d443f6333ae3 and P000 ACTIVE unchanged.

## Research question and inherited source

The preceding same-lane proof at Enterprise Math commit 5a75ce46ffbfd469b3153104a25b1e0c4a5b62e2 proved the finite inhomogeneous third-order holonomic relation

    L F_ell = -20*ell^3*c_ell*z^ell,
    L = theta*(theta+5/6)*(theta+2/3)-2*z*(theta+1)^3,
    theta = z*d/dz,
    F_ell = 10*C_ell(z)/z,   F_ell(0)=1,
    c_1=1/10, c_{a+1}/c_a=36*a^2/((6*a+5)*(3*a+2)).

It encodes the ORIGINAL signed-R Clausen overdegree boundary, not the distinct finite first-jet Green E_p. The exact original 216 target A_p = p (mod p^3) for p mod24 in {13,19} is NOT settled by this equation.

## Theorem — exact finite Green inverse

For every integer ell>=1, over Q, the linear map

    L : Q[z]_(degree<ell)  ->  {y in Q[z]_(degree<=ell): y(0)=0}

is an ISOMORPHISM. The same holds over any field with 2,3,6 and all 1,...,ell invertible; in particular F_p for every prime p=6ell+1>=7.

For an arbitrary source polynomial y(z)=sum_(n=1)^ell y_n*z^n, write f_ell=0 and solve downwards:

    f_(n-1) = [n*(n+5/6)*(n+2/3)*f_n-y_n]/(2*n^3),
    n=ell,ell-1,...,1.                                             (A)

This is the unique finite polynomial f(z)=sum_(k=0)^(ell-1) f_k*z^k with L f=y. Equivalently, the FINITE Green kernel is

    f_k = -sum_(n=k+1)^ell { y_n/(2*n^3) *
             product_(j=k+1)^(n-1) [(j+5/6)*(j+2/3)/(2*j^2)] }.     (B)

Empty products equal 1. All denominators in (A)-(B) are p-units in the claimed prime regime. The backwards algorithm costs O(ell) field operations; expanded (B) gives an exact symbolic certificate.

### Proof

For f_ell=0, the coefficient of z^n in L f is

    y_n = n*(n+5/6)*(n+2/3)*f_n-2*n^3*f_(n-1),  1<=n<=ell.

The constant coefficient is always zero. For each 1<=n<=ell, 2*n^3 is invertible. Starting with f_ell=0 and n=ell, (A) determines every f_(n-1), so every target y has exactly one preimage. Thus both surjectivity and injectivity hold. Iteration gives (B) and proves denominator bounds. No analytic or divergent infinite Green integration is used.

## Theorem — terminal SOURCE is a p-adic unit and cannot be omitted

At EVERY prime p=6ell+1>=7, the recurrence yields c_ell a p-unit: c_1=1/10 is a unit, and for 1<=a<ell, each of 36,a,6a+5,3a+2 is nonzero modulo p. Also 20 and ell are p-units (p>=7). Hence

    v_p(-20*ell^3*c_ell)=0.                                         (C)

The kernel of L on F_p[z]_(degree<ell) is zero, as is already implied by the isomorphism. Therefore a nonzero normalized polynomial F_ell(0)=1 cannot satisfy L F_ell=0 after discarding the terminal source. The degree-ell truncation term is an EXACT nonremovable boundary value in this declared source/readout language, not numerical error and not a second independent R definition.

The only finite polynomial solution to the ACTUAL terminal source is the inherited F_ell; the inverse (A) recovers its coefficients f_k=10*c_(k+1), with f_0=1, from the terminal alone. This reconstruction is scoped to this L/source/degree interface; it cannot be used to erase other 216 jet or native H0/B0 information.

## Executed proof-support checks

Python standard-library exact Fraction tests for Q: ell=1,..,12, including arbitrary source bijectivity. Over F_p, all 330 primes 7<=p<=5000 with p=1 mod6 were independently tested on a nontrivial arbitrary source, exact inverse, original f_k recovery, f_0=1, and NONZERO terminal. All PASS.

Anchors (p, terminal mod p, recovered f0 mod p):
(13,3,1), (19,11,1), (37,28,1), (67,48,1), (373,259,1).
Executed marker: PASS_D25_FINITE_HOLONOMIC_GREEN_INVERSE_NO_ERASURE.
Companion checker is author-side exact computation, not a native H0/B0 execution, Lean proof or mathematical admission.

## Typed BRC boundary and next action

BRC COMPOSE_APPLIED: preserve original source label R, prime p, ell, Gauss/overdegree index, signed 216 W-weight, holonomic order and terminal source. A single terminal coordinate reconstructs F_ell ONLY for this exact finite L inverse; no claimed reconstruction of E_p, L0N0 carries, L0N1 or P000-native X6 observation. The residual source must not be erased.

Continue by seeking an explicit finite WZ/adjoint coupling of the new inverse with the distinct first-jet Green E_p and original carry, preserving nonzero p=19,67,373. Still unproved universally:

    (L0*N0-1)/p + L0*N1 - 12*2^(-3ell)*E_p - R_p = 0 (mod p).

Mother D25/LIFT/JT2 remains OPEN. Fixed373 original-class native H0/B0 [X]U modulo 139129, semilinear Frobenius, normalization, independently replayed benchmarks remain under enterprise-math#1559. Control issue #1558 remains the existing Source authorization/recovery path; no new CLAIM/OPEN/native checkpoint/Result or activity registration was generated by this author-side publication.
