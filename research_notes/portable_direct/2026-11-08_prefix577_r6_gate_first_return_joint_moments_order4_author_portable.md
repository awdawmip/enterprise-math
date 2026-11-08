# PREFIX-577-R6 gate-cycle bivariate first-return law and fourth-order exact joint moments

**Scientific input:** frozen `f42f2906d77f24085c123f3ccfe9667d41caa96d`, original tagged transition Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`. **Evidence:** AUTHOR_EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. No Source task CLAIM, OPEN, Result, review, native experiment, or mathematical admission is claimed. Original 96 ports and 576 tagged edges, all seven rewards and six native axes retained. Parent author notes on ordered-word symmetry `7dc57fac1334e39470685e63ee4f6a3c28668c21` and regenerative first gate `1ef152800b51d4a6b4e364078b1564764014474c` are *reused*, not new predecessor completed research.

Let `p*=9` be the unique marked-edge landing port, `T` the first subsequent step with native mark `K=1`, `U=R5(T)`, `V=R6(T)` the total rewards including the marked step. For original phase/bit ports define polynomial matrices

`C_pq(x,y) = sum_{tagged alpha: p->q,K(alpha)=0} x^{r5(alpha)} y^{r6(alpha)}` and
`g_p(x,y) = sum_{tagged alpha: p->9,K(alpha)=1} x^{r5(alpha)} y^{r6(alpha)}`.

The exact rational three-variable generating function is

```text
F(z,x,y)= E_9[z^T x^U y^V]
        = z e_9^T (6I - z C(x,y))^{-1} g(x,y)
        = z e_9^T adj(6I-zC(x,y)) g(x,y) / det(6I-zC(x,y)).
```

It is specified by the unchanged 96x96 original integer transfer data, with denominator constant term `6^96`. This is an **exact unexpanded rational presentation**, not a claimed minimal polynomial denominator. From the previously author-proved ordered seven-reward word exchange symmetry for starting law delta_9, the first gate is invariant under fifth/sixth exchange, hence `F(z,x,y)=F(z,y,x)` as a formal power series. The inherited nine-root endpoint coboundary makes each complete tagged gate cycle's six-axis total root-independent; the computational carrier here is root 0.

**New exact joint cycle statistics (time index separate from the six native axes):**

| quantity | exact rational value |
|---|---:|
| E[T]; E[U]=E[V] | 192; 32 |
| Var(T) | 36064 |
| E[TU]=E[TV] | 12176 |
| Cov(T,U)=Cov(T,V) | 6032 |
| E[U²]=E[V²] | 6128/3 |
| E[UV] | 6080/3 |
| Var(U)=Var(V) | 3056/3 |
| Cov(U,V) | **3008/3** |
| E[U³]=E[V³] | 1173395/6 |
| E[U² V]=E[U V²] | 1161259/6 |
| E[U⁴]=E[V⁴] | 3594924359/144 |
| E[U³ V]=E[U V³] | 3553230437/144 |
| E[U²V²] | 3539477423/144 |
| E[TUV] | 10414850/9 |
| E[T²U]=E[T²V] | 6941178 |

For `D=U−V`, **`E[D²]=32`, `E[D³]=0`, `E[D⁴]=6040`, `cum4(D)=2968`**, `E[T D²]=12128`, `Cov(T,D²)=5984`. These are excursion *cycle* quantities, not per-step asymptotic cumulant rates.

**Exact proof and certificate method.** Set `A=6I-C(1,1)`, `H_m(p)=E_p[T^a U^b V^c]` for multiindex `m=(a,b,c)`, `H_000=1`. The inherited bounded access to marked gate implies `A` nonsingular over `Q`. For nonzero `m`, the original first-step decomposition reads

```text
(A H_m)_p =
  sum_{tagged alpha gate from p} 1^a r5^b r6^c
 +sum_{tagged alpha non-gate p->q} sum_{0<k<=m}
    binomial_multi(m,k) * 1^k0 * r5^k1 * r6^k2 * H_(m-k)(q).
```

Thus induction in total degree gives *all* raw joint moments. Exact SymPy rational inversion of the original 96x96 system plus direct integer tagged paths verifies 34 nonzero multiindices `a+b+c<=4`, **3264 row residuals**; 35 moments including the constant. Independent direct path checks through first-gate depth 10 contain the known exact counts `20, 448, 18608` at depths 4,6,8 and the symmetric `(U,V)` histograms. Regression anchors `E[T]=192`, `E[T²]=72928`, `E[T³]=41550000`, `E[(U−V)²]=32` all match the earlier separate renewal/moment proof. Finite paths do not serve as proof of infinite identities; exact rational systems do.

**Reproducible author-side evidence:** original helper `frozen_native_kernel_prefix577.py`; new `verify_gate_joint_moments.py`; complete `GATE_JOINT_MOMENTS_ORDER4_CERTIFICATE.json` SHA256 `5399d0ef5fde264eb6ad829f1d02fea06d5f0a42eebedc548828b5523cd9e15f`. Full five-file local ZIP SHA256 `af4b3aff46d326f1e37c7a1287a4e2e95508da686fbebfed00dffde75833f82e` (not asserted as GitHub-published ZIP). This repo note records the mathematics and code/cert fingerprints, while the complete local package is separately supplied in the ChatGPT task.

**Next unit:** find an observer- and future-operation-safe smaller symbolic presentation of `F(z,x,y)`, with exact minimal denominator degree over `Q(x,y)`, rather than silently identifying a 37-class gate-pair quotient with this first-hit automaton. Formal Source D25 original-class H0/B0 / divided-power / Frobenius / CM `NOT_RUN` frontier remains separate; own service session was just issued without effective CLAIM, and no duplicate Result/Review is requested.
