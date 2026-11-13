# PREFIX-766 / R6 — An exact local square lowers the Gamma mixed-curvature phase threshold

Date: 2026-11-14. Scientific input frozen at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: `AUTHOR_EXACT_INTEGER_PROOF / UNREVIEWED / NOT_ADMITTED`.
Scope: external 189-layer stopped-BRC / independent two-Gamma-clock auxiliary model. The scalar `p,z` parameters are not native X6 coordinates.

## Statement

Use the previously defined `Y(p,z)=max(C_p,C_z)`, `mu=E[Y]`, `W=Var(Y)`, `V_q=q^2 W-q mu` for real `q>0`. Let `Delta_R f=f(b,b)-2f(a,b)+f(a,a)` on the rational square

```
R=[51/1024,52/1024] x [51/1024,52/1024].
```

With the frozen BRC survivor recurrence and Gamma kernels, exact integer arithmetic establishes

```
Delta_R mu < 0,  Delta_R W < 0,
28519/1000000 < q_R := (Delta_R mu)/(Delta_R W) < 28520/1000000.
```

Thus `Delta_R V_q=q Delta_R W(q-q_R)<0` for every `q>=28520/1000000`. From the positive mixed rectangle in PREFIX-762, `[0,1/4]x[1/4,1/2]`, one also has `Delta_(R+) V_q>0` for every `q>0`. Hence for all real `q>=0.028520`, `V_q` is neither globally supermodular nor globally submodular on the auxiliary half-square. In the phase notation of PREFIX-763,

```
0 < q_c <= q_R < 28520/1000000 = 0.028520.
```

This strengthens PREFIX-765's `q_c<0.069741061` by a factor `0.069741061/0.028520 > 2.44`.

## Proof: finite integer certificate with no numerical cancellation

For `i=0,...,188` let `s_i(x)=Pr(T_x>i)`. The frozen integer killed-Pascal recurrence is reproduced exactly from PREFIX-760. Define the rational Gamma kernel entries

```
K_ij = binom(i+j,i)/2^(i+j+1),
L_ij = (i+j+1)K_ij.
```

For any `p,z`, the exact first and second raw moments of `Y` are

```
mu(p,z) = sum_i(s_i(p)+s_i(z)) - sum_ij s_i(p)K_ij s_j(z),
M2(p,z) = 2 sum_i (i+1)(s_i(p)+s_i(z))
          - sum_ij s_i(p)L_ij s_j(z).
```

Take `a=51/1024`, `b=52/1024`, and `d_i=s_i(b)-s_i(a)`. Symmetry of the kernels gives the exact square mixed identities

```
Delta_R mu = -sum_ij d_i K_ij d_j,
Delta_R W  = -sum_ij d_i L_ij d_j
              - [mu(b,b)^2-2mu(a,b)^2+mu(a,a)^2].
```

All terms are rational. To avoid huge intermediate fraction reductions, the companion checker uses a single exact integer denominator. Write `s_i(x)=U_i(x)/2^1880`, with `U_i(x)` an integer obtained by multiplying its width-surviving Bernstein numerator (denominator `1024^i`) by `2^(10(188-i))`. Define `E=2^4137`. Then

```
C_xy = sum_ij U_i(x) U_j(y) binom(i+j,i) 2^(376-i-j),
D = U(b)-U(a),
C_DD = sum_ij D_i D_j binom(i+j,i) 2^(376-i-j),
L_DD = sum_ij (i+j+1)D_i D_j binom(i+j,i)2^(376-i-j).
```

The three exact mean numerators on denominator `E` are

```
m_aa = 2 sum_i U_i(a) * 2^2257 - C_aa,
m_ab = (sum_i U_i(a)+sum_i U_i(b))*2^2257 - C_ab,
m_bb = 2 sum_i U_i(b) * 2^2257 - C_bb.
```

Consequently the following *integers* represent the mixed differences:

```
dMU  = -C_DD                                    [denominator E],
dVAR = -L_DD*E-(m_bb^2-2m_ab^2+m_aa^2)          [denominator E^2].
```

The checker verifies `dMU<0`, `dVAR<0`, `dMU=m_bb-2m_ab+m_aa`, and by two integer multiplications the strict rational interval

```
28519*(-dVAR) < 1000000*(-dMU*E) < 28520*(-dVAR).
```

This is a finite proof of the sign and bounds, not a floating-point decision. The visible decimals are only displays:

```
Delta_R mu       ≈ -0.002777495464378069
Delta_R variance ≈ -0.097389217210423235
q_R              ≈  0.028519537829089392
```

The checker reconstructs all 189 BRC rows, checks 9,529 surviving positions and a zero final row, checks the first 25 exact survivor identities and evaluates the symmetric kernel on exactly `189*190/2=17,955` index pairs. Run locally with Python 3 standard library:

```bash
python PREFIX766_R6_SQUARE_PHASE_VERIFY.py
```

Observed result: `ALL_CHECKS_PASS PREFIX766`. The exact fractions are reproducible by this published code; they are not replaced by the displayed decimal approximations.

## Dependencies, meaning and next frontier

The proof is conditional only on the same frozen integer width predicate and the 189-layer stopped-BRC auxiliary interpretation inherited from PREFIX-760; its cross-moment identities are elementary Gamma-integral identities. The positive-sign rectangle is the separately exact PREFIX-762 result. This is an author-level certificate and does not establish the global minimizer of `q_c`, an independent review, a native X6 relation, or additional `1/768` comparator-cell coverage.

Next scientific question: seek a certified rational neighborhood around the maximizing mixed-ratio point (rather than relying on discrete sample minima), or apply the same integer-kernel technique to a genuinely unverified comparator box with a full continuous-box sign enclosure. Do not count new excluded area until the actual box is certified.
