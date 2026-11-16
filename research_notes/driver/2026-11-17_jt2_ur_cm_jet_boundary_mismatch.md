# JT2 UR — CM-point divided second-jet and hypergeometric boundary correction

Date: 2026-11-17. Status: **PROVED EXACT FINITE-POLYNOMIAL IDENTITY AND CONDITIONAL MOD-p COROLLARY; author-side result**.

## Scope, definitions and provenance

Preserve the existing JT2 mother objective and the authors of its original UR/Sun parity, CM0, norm-jet and independent scoped Results. This note is a further **author-side derivation by Driver EM-DVR-DEBB5E in a shared research context**, not an independent Native Result review. It starts from the exact coefficientwise ODE in [the existing Driver note](https://github.com/awdawmip/enterprise-math/blob/71851b1a6040b4a32ce7e84e6ca56ea0001c9b1f/research_notes/driver/2026-11-17_jt2_ur_universal_spectral_basepoint_padic_deformation.md), with the same prime, polynomial cutoff and normalizations.

Let p=6m+1 be prime, p>3, m>=1; work in Z_(p). Define

- Y_*=1/2; F_m(Y)=sum_{j=0}^m f_j Y^j, f_j=(1/6)_j(1/3)_j/((1/2)_j j!).
- Q_m(Y)=P_(2m)(sqrt(Y))=sum_{j=0}^m c_jY^j, with c_0=(-1)^m binom(2m,m)/4^m and C_*=m(2m+1).
- v_m=F_m(Y_*)/p mod p and u_m=Q_m(Y_*)/p mod p only **under CM0**: Q_m(Y_*)=0 mod p. Because Q_m=c_0 F_m mod p and c_0 is a p-unit, this also ensures F_m(Y_*)=0 mod p.
- d_m=Q'_m(Y_*) mod p; S_p=sum_{j=0}^m c_j 2^{-(m+j)}/(2m+2j+1) mod p; epsilon_p is the previously defined UR residual 18u_md_m-2J_m(Y_*)-3 mod p.

All finite coefficients, their Y-derivatives and the displayed denominators are p-integral. Theorem 1 does not assume CM0; later divided statements do.

## Theorem 1: exact rational endpoint ODE identity

For **every** m>=1, without any prime reduction or CM0 premise,

    F''_m(1/2)-F'_m(1/2)
      = (2/9) F_m(1/2) - [p(p+1)/(9*2^m)] f_m,    p:=6m+1.    (E1)

Also, for the terminating Legendre polynomial,

    Q''_m(1/2)-Q'_m(1/2)=-2m(2m+1)Q_m(1/2).       (E2)

**Proof.** The exact finite-polynomial hypergeometric boundary equation is

    [Y(1-Y)d_Y^2+(1/2-3Y/2)d_Y-1/18]F_m
        = -p(p+1) f_m Y^m/36.

At Y=1/2, multiply by 4: the coefficients of the first two derivatives are respectively +1 and -1, and the constant term becomes -2F_m/9. Rearranging gives (E1). For Q_m, the exact terminating spectral equation has C_*=m(2m+1), with +C_*/2 replacing -1/18; evaluating at Y=1/2 and multiplying by 4 gives (E2). The endpoint error in (E1) is **exactly** the highest-degree truncation term; it is not a fitted finite-data parameter.

## Theorem 2: divided CM-point jet identity

Suppose p is prime and CM0 holds (in particular in the inherited JT2 class p mod 24 in {13,19}). Then

    F''_m(1/2)=F'_m(1/2) mod p,
    Q''_m(1/2)=Q'_m(1/2) mod p.                    (J0)

Define the p-integral divided mismatch

    Delta_m := [F''_m(1/2)-F'_m(1/2)]/p mod p.

Then

    Delta_m = (2/9)v_m - f_m*2^(-m)/9 (mod p),
    v_m = [9 Delta_m + f_m*2^(-m)]/2 (mod p).      (J1)

Likewise,

    [Q''_m(1/2)-Q'_m(1/2)]/p
       = -2C_* u_m = (2/9)u_m (mod p).            (J2)

**Proof.** Under CM0 the special values F_m(1/2) and Q_m(1/2) belong to p Z_(p). The right side of (E1), and also that of (E2), therefore belongs to p Z_(p); this proves the divisibility in (J0). Divide (E1) by p and reduce modulo p, observing p+1=1 mod p, to obtain (J1). Divide (E2) by p; C_*=(p^2+p-2)/18=-1/9 mod p, which yields (J2). All divisions are performed in Z_(p), not on a merely mod-p polynomial.

## Corollary: an alternative UR boundary-jet certificate

The inherited norm/Lagrange reduction in the cited prior proof gives, under CM0,

    epsilon_p = 18 c_0 d_m v_m - 2c_m S_p - 3 (mod p),

and c_m=c_0 f_m (mod p) coefficientwise. Substitute (J1):

    epsilon_p
      = 81 c_0 d_m Delta_m
        + 9 c_m d_m 2^(-m)
        - 2 c_m S_p - 3 (mod p).                 (UR-JET)

Thus the remaining all-prime UR congruence is **equivalently** a congruence on the first p-adic mismatch between the second and first Y-jets of the finite truncated basepoint solution, plus one explicit boundary term and the existing O(m) S_p sum.

This is a *different representation of the same open obstruction*. It does not independently establish epsilon_p=0, and it does not prove an asymptotic speedup. Its prospective use is to test a p-adic differential-equation/jet-transport argument instead of direct quotient summation.

## Exact checks and reproducibility

Using the rational recurrences

    f_0=1,
    f_(j+1)=f_j*(6j+1)*(3j+1)/[9*(2j+1)*(j+1)],
    c_0=(-1)^m*binom(2m,m)/4^m,
    c_(j+1)=c_j*(j-m)*(2m+2j+1)/[(j+1)*(2j+1)],

form F_m, Q_m, the two derivatives and S_p in Q. Evaluate at 1/2 exactly, verify (E1)-(E2) in Q, and reduce fractions with denominator prime to p modulo p or p^2. For the following eight CM-class primes, direct rational computation matched (J1), (J2) and (UR-JET) against the original quadratic norm convolution:

| p | m | v_m mod p | Delta_m mod p | old epsilon_p | UR-JET epsilon_p |
|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 8 | 10 | 0 | 0 |
| 19 | 3 | 18 | 1 | 0 | 0 |
| 37 | 6 | 26 | 11 | 0 | 0 |
| 43 | 7 | 21 | 0 | 0 | 0 |
| 61 | 10 | 36 | 23 | 0 | 0 |
| 67 | 11 | 18 | 37 | 0 | 0 |
| 109 | 18 | 22 | 5 | 0 | 0 |
| 139 | 23 | 70 | 82 | 0 | 0 |

The formulas (E1), (E2) and (J1)-(J2) have complete algebraic proofs above; the eight-prime checks are crosschecks, **not** an all-prime proof of UR vanishing.

## Result, contribution and next discriminating question

- Completed here: exact endpoint finite-polynomial identity; CM-point p-divided jet relation; alternate UR-JET residue. **Author-side algebraic subunit**, sourced to Driver EM-DVR-DEBB5E.
- Existing inputs and their original contributors remain untouched. The older coefficientwise deformation, CM0 premise, source proofs and Lagrange norm identity are reused at their actual scope.
- Not completed: an independent review/Native Result acceptance, uniform evaluation of Delta_m or v_m, the all-prime epsilon_p=0 statement, audit/final integration, or JT2 mother-objective closure.
- Useful next discriminating target: find an independent p-adic transport formula for Delta_m that cancels the boundary and S_p terms in (UR-JET), or construct a precise counterexample to that prospective cancellation. Such a transport identity cannot be assumed as a new axiom.
