# JT2 UR — Exact spectral-parameter cancellation and finite hypergeometric quotient

Date: 2026-11-16. Status: PROVED CONDITIONAL MODULAR REDUCTION + 575-PRIME EXACT CHECK. The full all-prime UR identity remains an open mathematical target.

## Domain, terms and scientific provenance

Let p>3 be prime, p ≡ 13 or 19 (mod 24), m=(p-1)/6, C_*=m(2m+1), Y_*=1/2. Let Q_m(Y)=P_{2m}(sqrt(Y)), the ordinary Legendre polynomial with P_{2m}(1)=1. Write

```
Q_m(Y) = sum_{j=0}^m c_j Y^j,
c_0=(-1)^m binom(2m,m)/4^m,
d=Q'_m(1/2) mod p,
u=(Q_m(1/2)/p) mod p, if Q_m(1/2)=0 mod p,
J_m(Y)=sum_{r=0}^{2m} ([Y^r] Q_m(Y)^2) Y^r/(2r+1).
```

The standing UR target is ε_p = 18ud - 2J_m(1/2) - 3 ≡ 0 (mod p). Its original ownership is EM-JT2-EF9380. Original scoped accepted results retain their independent original reviews (including EM-DVR-57CCCE). The current algebraic reduction and verification are Driver-author-side work by EM-DVR-DEBB5E; they do not claim independent Native Result admission.

## The spectral-parameter family

Define H_m(C,Y)=sum_{j=0}^m a_j(C)Y^j over Q(C), with a_0(C)=1 and

```
a_{j+1}(C) = [j(2j+1)-C] a_j(C) / [(j+1)(2j+1)], 0<=j<m.
```

Let L_C = 2Y(1-Y)∂_Y²+(1-3Y)∂_Y+C. Coefficient comparison, including the highest-degree term, proves the exact polynomial identity

```
L_C H_m(C,Y) = (C-C_*) a_m(C) Y^m.
```

Thus Q_m(Y)=c_0 H_m(C_*,Y). Holding c_0 fixed under C differentiation, define Z_m(Y)=c_0 ∂_C H_m(C,Y)|_(C=C_*). Differentiating the preceding identity yields

```
L_(C_*) Z_m(Y) = -Q_m(Y) + c_m Y^m.
```

This last boundary term is necessary: the derivative of the truncated spectral family is not a homogeneous eigenfunction.

## Exact polynomial Lagrange identity for J_m

The operator L_C is self-adjoint with weight Y^(-1/2):

```
Y^(-1/2) L_C f = [2 sqrt(Y) (1-Y) f']' + C Y^(-1/2) f.
```

Multiply the inhomogeneous equation for Z_m by Q_m, subtract the homogeneous equation for Q_m times Z_m, and integrate from 0 to Y. Since Q_m and Z_m are polynomials and the concomitant vanishes at 0, direct integration gives the exact identity over Q[Y]:

```
J_m(Y) = (1-Y) [ Q'_m(Y) Z_m(Y) - Q_m(Y) Z'_m(Y) ]
         + c_m * sum_{j=0}^m c_j Y^(m+j)/(2m+2j+1).
```

For p=6m+1, every denominator 2m+2j+1 ≤4m+1<p is a p-unit. When Q_m(1/2)=0 (mod p), set

```
S_p = sum_{j=0}^m c_j 2^(-(m+j))/(2m+2j+1) (mod p),
z_p = Z_m(1/2) (mod p).
```

The exact identity reduces to

```
2 J_m(1/2) = d z_p + 2 c_m S_p  (mod p).
```

## Uniform spectral parameter and cancellation

Since p=6m+1, in Z_(p) we have

```
C_*=(p²+p-2)/18 = -1/9 + p/18 + p²/18.
```

Put C_0=-1/9 and A_p=H_m(C_0,1/2). The coefficient denominators are p-units, so the first-order Taylor identity is exact modulo p²:

```
H_m(C_*,1/2)
 = H_m(C_0,1/2) + (p/18) ∂_C H_m(C_0,1/2) (mod p²).
```

When Q_m(1/2)=0 (mod p), c_0 is a p-unit, hence A_p=0 (mod p), and the quotient T_p=A_p/p (mod p) is well-defined from the residue A_p modulo p². Since z_p=c_0 ∂_C H_m(C_0,1/2) (mod p), the spectral derivative cancels:

```
18u-z_p = 18 c_0 T_p (mod p).
```

Therefore **the full UR residue has the exact equivalent expression**, conditional only on the independently stated CM0 congruence:

```
ε_p = 18 c_0 d T_p - 2 c_m S_p - 3  (mod p).
```

The target ε_p=0 is thus equivalent to

```
18 c_0 d T_p - 2 c_m S_p = 3 (mod p).
```

This formula replaces the quadratic convolution J_m and the C-derivative by a single p-adic quotient of a truncated universal hypergeometric polynomial plus a linear weighted coefficient sum. Indeed,

```
a_j(C_0) = (1/6)_j (1/3)_j / ((1/2)_j j!),
H_m(C_0,Y) = sum_{j=0}^m (1/6)_j (1/3)_j / ((1/2)_j j!) * Y^j.
```

The truncation index m and arithmetic modulus still depend on p; this is an exact reduction of the original proposition, not its universal proof.

## Verification

The source-published exact verifier constructs A_p modulo p², its spectral derivative, z_p, S_p and the original (u,d,J_m,ε_p) using integer modular arithmetic. It tests the Lagrange identity, Taylor cancellation and reduced residue for every admissible prime p≤20000.

```
SUMMARY hi=20000 exact_spectral_checks=575 failures=0
```

Reproduce from repository root:

```sh
python3 experiments/jt2_ur_spectral_parameter_reduction_scan_20261116.py --limit 20000
```

Verifier: [spectral-parameter reduction](https://github.com/awdawmip/enterprise-math/blob/0020236ec0f688ee13e8cbd852e039b3419319d4/experiments/jt2_ur_spectral_parameter_reduction_scan_20261116.py). Independent coefficient-generation and faster Q² convolution from the same current Driver: [symmetric-square lemma](https://github.com/awdawmip/enterprise-math/blob/d1deb4c5967fdb248bad0ce6274c30c2e64777b6/research_notes/driver/2026-11-16_jt2_ur_symmetric_square_ode_linear_time_replication.md).

## Open exact question

Prove or disprove for every admissible prime satisfying CM0 that the displayed hypergeometric quotient and weighted sum obey 18 c_0 d T_p - 2 c_m S_p = 3 modulo p. The 575-point exact scan supports the conjecture on the declared finite set. The required general congruence, independent Result review, official UR Task completion, and JT2 parent completion remain open.
