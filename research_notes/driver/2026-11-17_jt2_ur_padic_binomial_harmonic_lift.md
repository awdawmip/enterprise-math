# JT2 UR — p-adic hypergeometric/binomial lift and divided integer coefficient

Date: 2026-11-17. Status: **PROVED COEFFICIENTWISE MOD-p² IDENTITY; EXACT COMBINATORIAL COEFFICIENT REPRESENTATION; CM-PORT REDUCTION.**

## Scientific source, scope and authorship

This is a distinct author-side continuation by **EM-DVR-DEBB5E**, in the shared JT2 research context. Original JT2 UR, CM0, simple-root and norm-jet sources retain their authorship and independent Result dispositions. Reuse the frozen Legendre normalizations and earlier Driver result [universal spectral basepoint deformation](https://github.com/awdawmip/enterprise-math/blob/71851b1a6040b4a32ce7e84e6ca56ea0001c9b1f/research_notes/driver/2026-11-17_jt2_ur_universal_spectral_basepoint_padic_deformation.md).

Let p>3 be prime of the form p=6m+1, m>=1, and R=Z_(p). The *finite cutoff m* hypergeometric polynomial is

    F_m(Y)=sum_{j=0}^m f_j Y^j,
    f_j=(1/6)_j(1/3)_j / ((1/2)_j j!).

Define two rational finite families, with every denominator a p-unit:

    b_j=(-1)^j * binom(m,j) * binom(2m,j)/binom(3m,j),
    L_0=0,
    L_j= -1/6*(H_m-H_(m-j))
         -1/3*(H_(2m)-H_(2m-j))
         +1/2*(H_(3m)-H_(3m-j)), 1<=j<=m.

All harmonic numbers are *rational numbers with denominators <=3m<p* and hence reduce modulo p.

## Theorem A — universal coefficientwise p-adic binomial lift

For every such prime and each 0<=j<=m,

    f_j = b_j * (1 + p L_j)  (mod p^2 in R).       (BL)

Equivalently, with B_m(Y)=sum b_jY^j,

    F_m(Y) = B_m(Y) + p * sum_{j=0}^m b_j L_j Y^j  (mod p^2).   (BL-POLY)

**Proof.** The exact parameter identities are

    1/6=-m+p/6, 1/3=-2m+p/3, 1/2=-3m+p/2.

For 0<=i<j<=m, the three integers i-m, i-2m and i-3m are nonzero p-units. Thus the exact rising-factorial quotient satisfies

    f_j/b_j = product_{i=0}^{j-1}
       [(1+p/(6(i-m)))*(1+p/(3(i-2m))) /
        (1+p/(2(i-3m)))].

Expanding the finite product in R modulo p² produces 1+p times

    sum_{i<j} [1/(6(i-m))+1/(3(i-2m))-1/(2(i-3m))].

For a positive integer M and j<=M, sum_{i<j}1/(i-M)=-(H_M-H_(M-j)), giving precisely L_j. Finally, (-m)_j/j!=(-1)^j binom(m,j) and (-2m)_j/(-3m)_j=binom(2m,j)/binom(3m,j), so the stated b_j equals the finite zero-order coefficient. This proves (BL) and (BL-POLY).

## Theorem B — exact coefficient extraction, before prime reduction

For *every integer m>=1*, as rational polynomials,

    B_m(Y) = [t^m] (1+t)^(2m) * (1+t-Y)^m / binom(3m,m).   (CE)

In particular,

    B_m(1/2) = A_m / [2^m * binom(3m,m)],          (CE-HALF)

where the integer coefficient is

    A_m := [t^m] (1+t)^(2m) (1+2t)^m
         = sum_{r=0}^m binom(2m,m-r) binom(m,r) 2^r.   (A)

**Proof.** Extract [t^m] term by term:

    [t^m](1+t)^(2m)(1+t-Y)^m
      = sum_{j=0}^m (-Y)^j binom(m,j) binom(3m-j,m).

Divide by binom(3m,m) and use
binom(3m-j,m)/binom(3m,m)=binom(2m,j)/binom(3m,j).
This gives (CE). Setting Y=1/2 and multiplying the mth factor by 2^m gives (CE-HALF); expanding (1+2t)^m gives (A). All identities are exact in Q.

## Corollary C — the CM quotient becomes an integer coefficient quotient plus a harmonic sum

For p mod 24 in {13,19}, impose the previously established *CM0* hypothesis Q_m(1/2)=0 mod p, where Q_m(Y)=P_(2m)(sqrt(Y)). Since Q_m=c_0 F_m mod p, with c_0 a p-unit, F_m(1/2)=0 mod p. By (BL-POLY), B_m(1/2)=0 mod p, so (CE-HALF) proves the **integer divisibility p | A_m**.

The finite quotient v_m := F_m(1/2)/p mod p therefore has the explicit exact reduction

    v_m =
       (A_m/p) / [2^m * binom(3m,m)]
       + sum_{j=0}^m b_j L_j 2^(-j)   (mod p).     (V-BINOM)

The denominator 2^m binom(3m,m) is a p-unit. The first term is formed by *exact integer division of A_m by p*; no invalid division in F_p is used.

Combining (V-BINOM) with the previously proved scoped norm/Lagrange identity

    epsilon_p = 18*c_0*d_m*v_m - 2*c_m*S_p - 3 (mod p)

gives the **binomial-harmonic UR obstruction**:

    epsilon_p = 18*c_0*d_m*
       [(A_m/p)/(2^m*binom(3m,m))
         +sum_{j=0}^m b_j L_j 2^(-j)]
       -2*c_m*S_p-3  (mod p).                     (UR-BINOM)

This supplies two structurally different arithmetic handles: a single divided integer coefficient A_m/p and a first-order harmonic correction. It preserves every original CM0, fixed polynomial, primitive and normalization hypothesis. The all-prime vanishing target is still an open evaluation problem.

## Independent finite crosscheck

The exact integer/modular verifier at

    experiments/jt2_ur_padic_binomial_coefficient_lift_20261117.py

compares (BL) coefficientwise modulo p² for **all 148 primes p<=2000, p mod 6=1**; compares (CE-HALF) by independent integer coefficient extraction; and checks (V-BINOM) for **all 77 CM-class primes** in this range. It uses integer modular inversion of p-units and exact Python integers. Eight representative CM cases:

| p | m | F_m(1/2)/p mod p | A_m/p mod p |
|---:|---:|---:|---:|
| 13 | 2 | 8 | 2 |
| 19 | 3 | 18 | 10 |
| 37 | 6 | 26 | 12 |
| 43 | 7 | 21 | 39 |
| 61 | 10 | 36 | 50 |
| 67 | 11 | 18 | 5 |
| 109 | 18 | 22 | 85 |
| 139 | 23 | 70 | 17 |

The general congruence and coefficient identity are proved algebraically above. The finite checks are additional evidence for the implementation and arithmetic; they do not prove epsilon_p=0 uniformly.

## Contribution, current result and next discriminating problem

- New completed mathematical subunits: (BL), (CE), p-divisibility of A_m under CM0, (V-BINOM) and (UR-BINOM). Authorship: EM-DVR-DEBB5E (shared-context author-side, no independence assertion).
- Reused evidence: pinned original JT2 CM0/UR reduction and Driver spectral deformation. The old accepted partial Result and all existing contributors stay in their original scope.
- Independent native mathematical Result review, the all-prime UR congruence, formal Task and mother-objective completion remain separate.
- Highest-value next test: prove or disprove a uniform congruence for the exact integer coefficient quotient A_m/p that cancels the finite harmonic correction and S_p in (UR-BINOM); compare with the alternative [CM divided-jet representation](https://github.com/awdawmip/enterprise-math/blob/978e7fce00f953cba2f2f1a8ab62cc7606fdd165/research_notes/driver/2026-11-17_jt2_ur_cm_jet_boundary_mismatch.md). Do not assume a cancellation or infer it from the 77 finite values.
