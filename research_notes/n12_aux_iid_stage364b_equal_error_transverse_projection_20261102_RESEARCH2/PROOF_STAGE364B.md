# Stage364-B — a quantitative equal-error projection from off-arc points onto the r1 kink

Date: 2026-11-02 (Asia/Shanghai). Research2 portable author result, **not** an accepted native Result. Global scientific pin `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; Enterprise Math scientific pin `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; original task P000 V4. Separately read current control GLOBAL main `5e6228882955de015d4738f43080d5001dad1046`, Enterprise Math main `f0088f95e173a47c7f899ca8a1dca59c358570e3`. The P000 current projection and original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` were checked; the auxiliary observer is **not** a native X6 or three-dimensional slice.

## Exact original labeled observer

For k=0,1,2,3, put `B_k(z)=z^k(1-z)^(3-k)`, `w=(1,3,3,1)`, `m=(61,21,9,9)` and

`r_k(x,y)=[4 B_k(x)+B_k(y)]/5 - m_k/160`,

`b(x,y)=(5/32) sum_k w_k |r_k(x,y)|`,

`D_3(a,z)=(1/2) sum_k w_k |B_k(a)-B_k(z)|`,

`c(x,y)=[63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)]/256`.

The 16 individual source/word labels are retained in the four port comparisons. Do not cancel the signed terms before evaluating the original absolute values.

## Theorem — uniform transverse sharpness with **exact same error**

Let the **outer** rational rectangle and **inner** rectangle be

`R=[2311/10000,29/125] × [1111/2000,559/1000]`,

`K=[2312/10000,2318/10000] × [139/250,279/500]`,

and let `eta=1/100000`. For every real point `p=(x,y)∈K` with `|r_1(p)|<=eta`, there exists a point `q∈R` on the `r_1(q)=0` kink, satisfying **exactly** `b(q)=b(p)`, and the quantitative strict projection bounds

* If `r_1(p)>0`, then `c(p)-c(q)>(4/25) r_1(p)`.
* If `r_1(p)<0`, then `c(p)-c(q)>(2/3)(-r_1(p))`.
* If `r_1(p)=0`, choose `q=p` with equality of cost.

The construction is the unique trajectory starting at p which varies `t=r_1` at fixed `b` toward zero on the appropriate smooth sign cell. No rationality is claimed for q (p may be irrational). In the two-source additive model, replacing such an off-arc source by q **preserves the absolute error budget exactly** and strictly reduces the total original four-port cost. Hence no unrestricted global minimizer can have an off-arc source in this explicitly stated near-star tube. The theorem applies to the original four-parameter two-source budget model, but only when an individual source lies in K and its `|r_1|<=eta` condition holds; it is **not** global optimality of the entire r1=0 arc or a theorem about the distant audit-tag cusp.

## Proof

**1. Signs, source fidelity, and two smooth error branches.** The Bernstein basis derivative identities are `B_1'(z)=(1-z)(1-3z)=u_1(z)` and `B_2'(z)=z(2-3z)=u_2(z)`. On R, `r_0<0`, `r_2>0`, `r_3<0`, certified respectively by `r_0(XL,YL)<0`, `r_2(XL,YL)>0`, `r_3(XU,YU)<0` and the basis monotonicities. The weighted sum `sum_k w_k r_k=0` is an exact identity since `sum_k w_k B_k=1` and `sum_k w_k m_k=160`. Thus

`b=(15/16) (r_2+max(r_1,0))`.

Write `b_-=(15/16)r_2` when `r_1<0` and `b_+=(15/16)(r_2+r_1)` when `r_1>0`. Their gradients are

`grad b_-=(3/4 u_2(x), 3/16 u_2(y))`,

`grad b_+=(3/4 (1-2x), 3/16 (1-2y))`.

Across R all 16 original absolute-value comparison signs remain constant as four four-tuples `(-,+,+,+)`, `(-,-,+,+)`, `(+,+,-,-)`, `(-,-,+,+)` at ports `(1/4,x)`, `(3/4,x)`, `(1/4,y)`, `(3/4,y)` respectively. Expanding all 16 terms independently yields the same smooth cost gradient on both sides:

`c_x=-3(1-x)(63-61x)/256`, `c_y=3y(1-y)/64`.

**2. Positive shared Jacobian.** Put `f=r_1`. Then `f_x=(4/5)u_1(x)`, `f_y=(1/5)u_1(y)`. For either sign branch, the determinant

`J=f_x b_y - f_y b_x = (3/20)[u_1(x)u_2(y)-u_1(y)u_2(x)]`

is the **same**: adding `(15/16)r_1` to b does not alter its wedge product with `dr_1`. In R, `u_1(x)>0`, `u_1(y)<0`, `u_2(x)>0`, `u_2(y)>0`. Using monotone rational corner bounds,

`J_lower=(3/20)[u_1(XU)u_2(YU)-u_1(YL)u_2(XL)] > 1/60`,

`J_upper=(3/20)[u_1(XL)u_2(YL)-u_1(YU)u_2(XU)] < 1/40`.

**3. Quantitative opposite-sided cost gradients.** Along an iso-b curve with increasing `t=f`, the cost derivative is `dc/dt=D/J`, where `D=c_x b_y-c_y b_x`. Let `g_min=3(1-XU)(63-61 XU)/256`, `h_min=3 YU(1-YU)/64`, `h_max=3 YL(1-YL)/64`. Positive and negative branches give, uniformly throughout R,

`D_- <= -g_min*(3/16)u_2(YU) - h_min*(3/4)u_2(XL) < -1/60`,

`D_+ >= g_min*(3/16)(2 YL-1) - h_max*(3/4)(1-2 XL) > 1/250`.

The first estimate uses that `u_2` decreases for y>1/3, while the second uses `b_{+,y}=(3/16)(1-2y)<0`. All displayed constants are checked with exact `Fraction` arithmetic. Dividing by `0<J<1/40` yields

`dc/dt < -2/3` for `t<0`, and `dc/dt > 4/25` for `t>0`.

**4. Existence through t=0 without leaving R.** Fix any p in K with `t_0=f(p)` and `|t_0|<=eta`. On its smooth sign side solve the explicit ODE

`dx/dt=b_y/J`, `dy/dt=-b_x/J`, `x(t_0)=p_x`, `y(t_0)=p_y`.

Because J>1/60, `|b_x|<41/100` and `|b_y|<1/25` throughout R, every trajectory remaining in R satisfies

`|dx/dt|<12/5`, `|dy/dt|<123/5`.

The K-to-R horizontal margin is at least `1/10000`, and the vertical margin is at least `1/2000`; hence `(12/5)eta<1/10000` and `(123/5)eta<1/2000`. A maximal solution therefore cannot reach the boundary of R before t=0; the smooth ODE extends to t=0, giving q in R. Exactly `dr_1/dt=1` and `db/dt=0` on either sign side, so `f(q)=0`, `b(q)=b(p)`. The path does not cross any other residual or audit-tag boundary in R.

**5. Integrate to the kink.** If t0>0, integrate `dc/dt>4/25` on (0,t0). If t0<0, integrate `dc/dt<-2/3` on (t0,0). The corresponding asserted strict inequalities follow. For `t0=0`, q=p. This proves the theorem for **every real** admissible p, not only a sampled grid.

## Validation, scope, next question

`REPRO_STAGE364B.py` independently re-expands all 16 port signs and c gradients, verifies the weighted residual identity, both b-branch gradient polynomials, the shared Jacobian identity, the exact corner bounds, and the K-to-R distance barrier. It uses Python `Fraction` and SymPy and was run twice with byte-identical stdout ending `STAGE364B_EXACT_OFF_ARC_EQUAL_ERROR_SHARP_PROJECTION_PASS`. The continuum ODE/compactness/integration reasoning is the proof behind the certified premises; finite checks alone are not being interpreted as universal verification.

BRC reuse: original four-port labeled Bernoulli observer and its weighted residual/total-variation forms are preserved, without merging source labels or introducing a new state representation. No native P000 X6, triadic closure, independent-time dynamics or registered six-field Cell address mapping is claimed.

Next: extend the same-equal-error transverse projection analysis along the farther right r1=0 arc toward the first audit-tag cusp (`E_dagger≈0.0021814072`), where an original label changes sign. Check whether the determinant bounds survive or a rational off-arc competitor appears; treat the cusp by the correct two-sided piecewise gradients. If the local projection survives, combine with Stage363-B budget splitting only on its declared near-star interval, keeping complete global competitor exclusion open.
