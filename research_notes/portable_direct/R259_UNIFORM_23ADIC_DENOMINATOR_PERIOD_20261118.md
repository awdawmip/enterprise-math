# R259 — Uniform finite-state 23-adic denominator-dip criterion and three new all-horizon certificates

Date: 2026-11-18 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_MODULAR_CERTIFICATE / NOT_REVIEWED**.
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Input and notation: R255B@6c12b514, R256@c7b15b95, R257/R258@8a0b7214. All 63 labelled masks are retained; no native signed-port/BRC equivalence is asserted. This is a positive rational auxiliary scalar observer, not a modification of P000.

## Main theorem (all rational parameters with a 23-adic pole)

Let `s` be rational with `39/100 < s < 41/100`, `t=(1691s-2615)/(2615s-3539)`, and `v_23(t)=-r <= -2`. Let `a=(1/5,1/4,3/10,9/20,s,2/3,t)`, `b_0=13/60`, and `b_i=(5/18)|1/2-a_i|` for i>=1. Source mask `D_m={0} union {i+1 : bit_i(m)=1}`, m=0,...,62; `P_D[i,j]=a_i delta_ij+(1-a_i)*b_j/(1-a_j)`; `rho_i=b_i/(Z(1-a_i)^2)` with `Z=sum b_i/(1-a_i)^2`; `h_(m,k)=W_popcount(m)*rho_D^T P_D^k*1`, `W=(144,576,1440,4320,17280,86400,518400)`.

Let `T=T_min(s)` be the positive integer from R255B making every `C_m(y)=T^d c_m(y/T)` integral. At the 23-adic pole `v_23(T)=r-1`. Write `F_23=Z/23Z`. Define units
`u = T*(t+b_6) (mod 23)` and, when r=2, `v=T^2*t (mod 23)`. Then u is nonzero; for r=2 so is v.

**Characteristic-polynomial reduction:**

* If 6 is absent from D_m, then `C_m(y) = y^d (mod 23)`.
* If 6 belongs to D_m and r=2, then
  `C_m(y) = y^(d-2) * (y^2 - u*y + v*B_m) (mod 23)`,
  where `B_m=sum_(i in D_m, i!=6) b_i (mod 23)`.
* If 6 belongs to D_m and r>=3, then
  `C_m(y) = y^(d-1)*(y-u) (mod 23)`.

Pick **any** positive integer normalization J and K for which `A_k=J*T^k/K` is integral for k>=3 and `q_(m,k)=A_k*h_(m,k)` is integral at the d_m consecutive bases `k=3,...,d_m+2` for every mask (such a choice always exists by clearing finitely many rational denominators). Integral recurrence extends this to all k>=3. Each `q_(m,k)` modulo 23 is jointly periodic for all k>=9 with a period dividing

`L_23 = 12144 = 23*(23^2-1)` if r=2, or `L_23 = 22` if r>=3.

For all k>=9, `23|A_k` (since v_23(T)>0). At such k the common reduced denominator of the 63 h-values **loses at least one factor 23 relative to A_k** if and only if `q_(m,k)=0 (mod 23)` for every m. Hence the first-factor 23-drop indicator is periodic with the same bound. To decide it for *all* k>=3, it suffices to check the six early indices k=3,...,8 and one finite window k=9,...,9+L_23-1. If `23` does not divide `A_k` at an early index, no 23-drop is at issue at that index. The theorem concerns first-factor divisibility, not the entire 23-adic deficit exponent.

### Proof

The rank-one determinant identity is
`c_D(x)=product_(i in D)(x-a_i) - sum_(i in D) b_i product_(j in D, j!=i)(x-a_j)`.
For 6 in D, put R=D\{6}, `A_R(x)=product_(i in R)(x-a_i)`, `A_(R\{i})(x)=product_(j in R,j!=i)(x-a_j)`, and `c_R(x)=A_R(x)-sum_(i in R)b_i*A_(R\{i})(x)`. Exactly,
`c_D(x)=x*c_R(x) -(t+b_6)*A_R(x) + t*sum_(i in R)b_i*A_(R\{i})(x)`.

At a 23-adic pole of t, R255B gives `v_23(T)=r-1>=1` and `s` is a 23-adic integer; all a_i,b_i for i!=6 are 23-integral. Moreover `t+b_6=(23/18)*t-5/36` has valuation `1-r`. After the substitution x=y/T and multiplication by `T^d`, the three displayed terms reduce respectively to `y^d`, `-u*y^(d-1)`, and `v*B_m*y^(d-2)` if r=2; the third vanishes if r>=3 because `v_23(T^2*t)=r-2`. For 6 absent, all nonleading coefficients vanish. This proves the polynomial reductions and u!=0.

Cayley-Hamilton gives the integral monic C_m recurrence of the normalized q-values from the stated d_m bases. The companion operator over F_23 for a mask lacking 6 is nilpotent of index <=d_m<=6; when 6 is present, its nonzero-primary component has dimension <=2 and its zero-primary component has nilpotent index <=d_m-1<=5 (u!=0). Thus all components are on their invertible periodic part by k=9. Every invertible matrix of dimension at most 2 over F_23 has order dividing `lcm(23*(23-1),23^2-1)=12144`: split distinct roots have orders dividing 22, irreducible quadratic roots divide 528, and the repeated-root Jordan case divides 23*22=506. For r>=3 only the nonzero root u remains, of order dividing 22. Taking the product over all 63 masks does not increase these universal divisibility bounds. Finally, `h_(m,k)=q_(m,k)/A_k`; if 23|A_k, all 63 reduced denominators lose a 23 factor exactly when every numerator q is 0 mod 23. QED.

## Three *new* all-horizon no-first-23-drop parameters

The standalone exact checker `R259_23adic_uniform_period_certificate.py` reconstructs all 63 original mask matrices and all 249 integer bases, checks every reduced characteristic coefficient, and enumerates full state cycles after k=9. It checks early k=3,...,8 and the complete bounded period. Results:

| s | t | r | T | J | K | period | minimum nonzero masks in complete window |
|---|---|---:|---:|---:|---:|---:|---:|
| 35597/90113 | 411/529 | 2 | 2238406920 | 28499307077 | 9732204000 | 12144 | 2 |
| 24911/60947 | 412/529 | 2 | 1513923480 | 4197801049 | 2194092000 | 12144 | 2 |
| 804575/2062139 | 9445/12167 | 3 | 1178141253480 | 15106173046037 | 5122353276000 | 22 | 29 |

All three have zero joint-zero indices in the early window and in their full later periods; the entire 63-state vector returns after the bound. Consequently **none of these three exhibits any first-factor 23 denominator dip for k>=3 relative to the displayed J*T^k/K normalization**. This is an all-horizon result for the three exact parameters, not extrapolation from short tests.

The computations use only Python standard-library `Fraction` and integers. Evidence file: `R259_23adic_uniform_period_verification.json`.

## Scope and next research

The universal result gives a bounded decision procedure for whether a given rational 23-adic pole loses its *first* 23 factor at any future event, independent of the enormous 249-dimensional naive finite-state bound. The method still asks for full 63-mask data for an arbitrary parameter; exploiting subset algebra to reduce this check and determining whether there exist any genuinely dipping 23-adic pole parameters are open. Higher 23-power deficit valuations require modulo `23^e` refinements. The independent continuous-real R247–R249 270/403 threshold remains open. No claim of formal Task/CLAIM, independent review, Foundation adoption, or native BRC signed/port execution.
