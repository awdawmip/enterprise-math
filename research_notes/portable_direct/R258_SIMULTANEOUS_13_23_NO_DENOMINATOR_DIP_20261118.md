# R258 — Both spectral-scaling exceptions can coexist without output-denominator dips

Date: 2026-11-18 (Asia/Shanghai). Evidence status: **AUTHOR_PROVED / EXACT_MODULAR_CERTIFICATE / NOT_REVIEWED**. Frozen science: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Directly builds on R255B (rational characteristic scaling), R256 (13-adic periodic loss) and R257 (23-adic exceptional no-loss parameter).

## Theorem — exact common denominator at the simultaneous 13/23 exception

Retain the same seven-source positive rational auxiliary scalar observer and **all 63 labelled source masks**, with definitions `D_m`, `P_D`, `rho`, `W` and `h_(m,k)` exactly as in R257. Take

```
s = 866/2197
t = (1691*s-2615)/(2615*s-3539) = 389159/500963
E = lcm of reduced denominators of a_i,b_i = 1188664967880
T = E/299 = 3975468120
J = 3327364117
K = 36933000
```

Here `v_13(s)<=-2` and `v_23(t)<=-2`, so R255B predicts the simultaneous minimum-characteristic-scaling exception `E/T=13*23=299`. For **every integer k>=3**,

```
lcm_(0<=m<=62) den(h_(m,k)) = J*T^k/K
                             = 3327364117 * 3975468120^k / 36933000.
```

The right-hand side is an integer; there is **no loss at either p=13 or p=23 at any horizon k>=3**. The exact common-denominator bit length is `k log2(3975468120)+O(1) ≈ 31.888477605k+O(1)`.

## Proof

The shared monic source-mask characteristic polynomial is

`c_m(x)=prod_(i in D_m)(x-a_i)-sum_(i in D_m)b_i*prod_(j in D_m\{i})(x-a_j)`.

As in R254–R257, every `C_m(y)=T^d c_m(y/T)` has integral coefficients; the companion checker recomputes its 249 nonleading coefficients and gives a non-integral coefficient after replacing `T` by `T/p` for each prime p dividing T (`2,3,5,13,23,947`). It also computes `J=lcm_(m,i in D_m) den(W_popcount(m)rho_i)`. Its 249 directly propagated integer initial values `H_(m,k)=J*T^k*h_(m,k)`, for k=3,...,d_m+2, have gcd `K`.

Define `q_(m,k)=J*T^k*h_(m,k)/K`. The 249 starting values are integers, and each mask has the monic integral recurrence with polynomial `C_m`. Cayley–Hamilton proves `q_(m,k)` integral for every k>=3, hence each reduced denominator divides `J*T^k/K`.

For every possible prime divisor of `J*T^k/K`, the table supplies a mask with **no zero residues modulo p at any k>=3**. Type G has `C_m(y)=y^(d-1)(y-u)` modulo p, with u nonzero and all d starting residues nonzero. Type O is a complete nonzero periodic orbit with no transient.

| p | mask | type | unit u / full period | starting residues |
|---:|---:|:---:|---:|---|
| 2 | 3 | G | 1 | 1,1,1 |
| 3 | 17 | G | 2 | 2,1,2 |
| 5 | 2 | G | 1 | 3,4 |
| 7 | 2 | G | 4 | 6,3 |
| 11 | 48 | O | 3 | 1,1,9 |
| **13** | **9** | **G** | **7** | **5,9,11** |
| 17 | 0 | G | 2 | 13 |
| **23** | **42** | **G** | **3** | **10,7,21,17** |
| 67 | 0 | G | 30 | 60 |
| 947 | 32 | G | 914 | 231,900 |
| 3449 | 0 | G | 718 | 2531 |

For p=11, the full residue cycle of mask48 is exactly `(1,1,9)` of period 3; no residue is zero. For p=13, mask9's characteristic reduces to `y^3-7y^2`, with three nonzero initial residues. For p=23, mask42's characteristic reduces to `y^4-3y^3`, with four nonzero initial residues. Every p is therefore retained at its exact full denominator exponent by a labelled mask. The upper bound is sharp for all k>=3. QED.

## Exact execution and scope

The standalone standard-library checker `R258_simultaneous_13_23_certificate.py` verifies the 249 characteristic coefficients, 249 initial integral bases, minimality of T, ten geometric prime witnesses, one full three-state zero-free orbit, and independently propagates the original Fraction matrices at k=3,4,5,6,7,8,10,12,16. Local independent recalculation returned PASS; denominator bit lengths for those k were respectively 103,135,166,198,230,262,326,390,517. The project verification digest records exact input and the prime witnesses.

This is a proof within the positive rational auxiliary scalar model and retains all 63 source identifiers. A native signed/port BRC equivalent, formal CLAIM, independent mathematical review or Foundation admission is not asserted. P000 and the frozen scientific input remain unchanged.

## Research implication and next question

R256, R257 and R258 together show that exceptional **characteristic scaling** (`E/T` equal to 13, 23 or 299) does not determine whether the **actual reduced-output denominator** loses a corresponding prime. The answer depends on mod-p nonvanishing across all retained source masks. Derive an effective general rational-parameter criterion, then locate 23-adic examples with genuine denominator loss (if they exist). The separate continuous-real 270/403 double-Perron error threshold remains open.
