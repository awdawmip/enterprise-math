# D25 / AF4 — explicit cubic jet of the ORIGINAL low-band finite boundary

Date 2026-11-09. Research lane chatgpt-research-onhour-enterprise-math-20260923; source Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; original science pin c47e13e4aba0e006366f989d6334d443f6333ae3. AUTHOR-SIDE EXACT PROOF / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.

This continues the just-published finite Hasse-jet quadratic boundary from `20261109_onhour_d25_AF4_low_band_hasse_quadratic_boundary.md`. Its finite differential operator is `D_X=theta^3-z prod_i(theta+alpha_i(X))`, on `F_N(X,z)=sum_{n=0}^N z^n prod_i(alpha_i(X))_n/(n!)^3`, with exact residual `B(X,z)=-z^(N+1)u_N(X)prod_i(N+alpha_i(X))`.

## Uniform third boundary coefficient (new)

For every prime p=6m+1>3, BOTH original W (216) and V (2304) low-band finite deformations have `B(X,z)=X^2 B_2(z)+X^3 B_3(z)+O(X^4)`, with `B_2` exactly as in the preceding theorem. The following closed, nontrivial HARMONIC ratios hold in Q (therefore in Z_(p)):

**Original W, N=3m, alpha=(-3m+X/2,-2m+X/3,-4m+2X/3):**
```
B_3/B_2 = J_W
 = -(1/2) H_(3m) + (H_(m-1)-H_(2m))/3
   -(2/3)(H_(4m)-H_m) - 1/(3m).
```

**Original V with p=4t+1, N=2t, alpha=(-t+X/4,-2t+X/2,-3t+3X/4):**
```
B_3/B_2 = J_V_plus
 = -3/(4t) - (1/2) H_(2t) - (3/4)(H_(3t)-H_t).
```

**Original V with p=4t+3, N=2t+1, alpha=(-3t-2+3X/4,-2t-1+X/2,-t+X/4):**
```
B_3/B_2 = J_V_minus
 = -1/(2(t+1)) - (1/2) H_(2t+1)
   -(3/4)(H_(3t+2)-H_(t+1)).
```
Here `H_n=sum_{k=1}^n 1/k` and `H_0=0`. All harmonic denominators are <p, and the nonzero leading `B_2` has invertible coefficient modulo p after specializing to z=1/2 (W) or z=1/9 (V). Hence these ratios can be computed exactly modulo p without loss of any original signed observer. The affine X variable is a finite arithmetic deformation parameter, NOT a new native spatial/time coordinate.

## Proof

Write the three negative-integer roots as `alpha_i(X)=-a_i+c_i X` and `u_N(X)=X u_1(1+L X+O(X^2))` where the unique crossed short root a_s<N contributes X. Then
```
L = sum_{i=1}^3 c_i sum_{0<=j<N, j!=a_i} 1/(j-a_i),
```
where terms with j=a_i are omitted only when they occur in the product for i=s. The middle root a_h=N gives
```
prod_i(N+alpha_i(X))=X P_1(1+T X+O(X^2)),
T=sum_{i!=h} c_i/(N-a_i).
```
Therefore `B_3/B_2=L+T` exactly. For W, these sums are
```
L= -H_(3m)/2+(H_(m-1)-H_(2m))/3 -2(H_(4m)-H_m)/3,
T=1/(3m)-2/(3m)=-1/(3m).
```
For V with p=4t+1,
```
L= -1/(4t)-H_(2t)/2-3(H_(3t)-H_t)/4,
T=1/(4t)-3/(4t)=-1/(2t).
```
For V with p=4t+3,
```
L= -3(H_(3t+2)-H_(t+1))/4-H_(2t+1)/2,
T= -3/(4(t+1))+1/(4(t+1))=-1/(2(t+1)).
```
The formulas follow. No conjectural analytic transformation is used.

## Exact calculation and discriminating use

For all 80 primes p=6m+1 in 7<=p<=1000 the direct polynomial multiplication of original affine numerator factors modulo p^4 produced `B_0=B_1=0`, the previous factorial `B_2`, and the new congruence `B_3=B_2 J` modulo p. Examples:

p | W (B2,B3,J modp) | V (B2,B3,J modp)
---|---|---
13 | (2,2,1) | (6,10,6)
19 | (5,5,1) | (6,5,4)
37 | (18,17,3) | (14,19,4)
43 | (40,20,22) | (10,2,26)
73 | (1,21,21) | (55,33,59)
373 | (57,163,173) | (79,314,207)

Companion exact-regression script `d25_AF4_low_band_cubic_boundary_20261109.py` reuses the preceding original-carrier polynomial calculator and independently evaluates all rational harmonic formulae modulo p. Both 13 and 19 target residues are represented.

**New direct next unit:** attempt an explicit pair of finite WZ/Fricke comparison certificates at z_W=1/2 and z_V=1/9, with both B2 and B3 forcing matched in the *signed two-model combination*. The cubic forcing is now fixed, so a candidate that only matches the X^2 boundary but fails X^3 can be rejected on p13/p19 before inferring any all-prime identity. Incorporate the low-band `ell_p` and existing W2 firstjet `b_p` and high tail `t_p` with its carry. The true native p373 H0/B0 [X]U mod139129 remains an independent pending original-class experiment under #1559. This file is not native Source checkpoint/Result/review.
