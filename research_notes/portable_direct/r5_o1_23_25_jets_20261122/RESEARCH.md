# R5 — First-residual jets restore primitive 23/25 period factors at precision O_m(N)

Date: 2026-11-22 (Asia/Shanghai). Status: **AUTHOR_EXACT_DERIVATION / TWO_ALGORITHMS_CROSSCHECKED / NOT_REVIEWED**. Frozen scientific input: `awdawmip/enterprise-math@990c8855b9e47b3eae12c9e93567b7c9e4bb7b65`; preceding true-event correction `@75d986aa23b68a7ecf9b29dc1006f0e322b35a15`. This is a result for the specified **scalar cost observer**, not a native X6 transfer or a modification of P000.

## Theorem (new)

Let the prices be the 101 consecutive integers 214,...,314. For the five original failure supports
`S0={214,...,218}`, `S1={214,216,217,218,219,220,221}`, `S2={215,216,217,218,219,220,221}`, `S3={223,...,290}`, and `S4={296,...,312}`, count price-multiplicity vectors of cost N that satisfy **at least one** of the separate event inequalities `sum_{p in Si} a_p < m`. Write `F_m(q)=R_m(q)/prod_{p=214}^{314}(1-q^p)`, and let `D=q d/dq`. Let `M_m(O_m(N^a))` be the least coefficient period after discarding an error O_m(N^a), for each fixed positive integer m.

For each primitive dth root `zeta_d`, d=23 or 25, the exact pole order of F_m at that root is:

| d | pole order four iff | pole order three iff |
|---|---|---|
| 23 | m mod 46 is not 0,42,43,44,45 | m mod 46 is 0,42,43,44,45 |
| 25 | m mod 50 is not 0,46,47,48,49 | m mod 50 is 0,46,47,48,49 |

Consequently, **for every fixed m>=1**, both factors are necessary at precision O_m(N):

```text
23 | M_m(O_m(N))
25 | M_m(O_m(N))
575 | M_m(O_m(N)).
```

In particular, m=46 removes both fourth-order poles at these roots, but **both third-order poles survive**. The inherited, not independently reviewed, all-m O_m(N^3) theorem would further give `26,771,144,400 | M_m(O_m(N))` for all m. The unconditional new assertion here is the 575 divisibility and the root-order classification.

## Proof: coupled three-event threshold kernel

Let `A_m(q)` denote the exact inclusion-exclusion numerator of the union of the first three events, preserving all three original loads
`L0=x+y+u`, `L1=x+j+u`, `L2=y+j+u`; here `x=a_214`, `y=a_215`, `u=a_216+a_217+a_218` and `j=a_219+a_220+a_221`. Use exactly the seven nonempty event masks, each with **simultaneous** inequalities, not a maximum-over-the-support shortcut.

At roots of order d in {23,25}, all terms involving S3 in the full 31-mask inclusion-exclusion have at least three zero factors in their product numerator (S3 contains three multiples of each d). Thus they vanish through first q-derivative. Write `B_m=C4 P4,m` for the single S4 event. Since S4 is disjoint from S0,S1,S2, every non-S3 term factors, and at `q=zeta_d`:

```text
R_m(zeta_d) = A_m(zeta_d)
D R_m(zeta_d) = D A_m(zeta_d) + D B_m(zeta_d) * (1-A_m(zeta_d)),
```

because `B_m(zeta_d)=0` (S4 contains precisely one d-divisible price).

The exact threshold generating function `G_A(q,t)=sum_{m>=1}A_m(q)t^(m-1)` is
`U(q,t)/(1-t) * sum_{I subset {0,1,2}, I nonempty}(-1)^(|I|+1) C_I(q) B_I(q,t)`, where `U=prod_{p=216}^{218}(1-q^p t)^(-1)` and `B_I` is the exact **maximum of selected base loads** kernel; its explicit seven rational expressions and tie-disjoint cone partition are in the frozen predecessor RESEARCH.md. This formula is also independently implemented in the present verification by obtaining each exact B_I coefficient from `max(x+y,x+j,y+j)` with only the selected loads.

## Root-of-unity rationality and the derivative recurrence

For d=23, the linear-factor exponents modulo d occurring in the seven rational terms use the distinct residues 0,7,...,15,19,...,22 in each denominator product; quadratic triple-intersection factors have exponents `a+b+w_i = 4,5,6` modulo d. Their roots do not collide with the linear roots in those terms. For d=25, the linear residues are drawn from 0,4,8,...,11,14,...,21 with no within-term repetition; quadratic exponents are 23,24,0. The sole possible collision is for `a+b+w=650` (the w=221 component) at t=1. The combined triple-cone numerator there is `1-q^650*t^3`; its ratio with `(1-t)(1-q^650*t^2)` has a simple pole at t=1 when q=zeta_25, and its q-derivative has at most a double pole because

```text
partial_Q [(1-Q*t^3)/((1-t)*(1-Q*t^2))]
       = t^2/(1-Q*t^2)^2,   Q=q^650.
```

All remaining factors are nonzero at that collision. The rational expressions and their derivatives are proper as functions of t. Thus, with `T=2d`, in the cyclotomic field:

```text
G_A(zeta_d,t) = P_d(t)/(1-t^T),       deg P_d < T,
D_q G_A(zeta_d,t) = H_d(t)/(1-t^T)^2, deg H_d < 2T.
```

Here `D_q` differentiates in q before evaluating at `zeta_d`. Hence `A_{m+T}(zeta_d)=A_m(zeta_d)` for all m. One exact full T-phase computation determines the only root-zero phases (last five in each period), reproducing the predecessor's independent direct-event checks. Write `c_m=D A_m(zeta_d)`. The second rational identity says that, **if** the exact cyclotomic vector equality `c_{r+T}=2c_r` holds for a phase r in 1,...,T, then

```text
c_{r+kT}=(k+1)*c_r    for every k>=0.
```

The exact-integer jet computation checks this *entire degree-(phi(d)-1) cyclotomic vector equality* for all five exceptional phases of both orders, not just one coordinate.

## S4 contribution at the exceptional phases

For d=23 the single d-divisible S4 price is p0=299, and for d=25 it is p0=300. The 17 prices in S4 have 17 distinct residues modulo d, including zero. The product over the complementary `d-17` residues, denoted `Q(t)`, satisfies

```text
sum_{n>=0} h_n(zeta_d^296,...,zeta_d^312) t^n
    = Q(t)/(1-t^d),  deg Q=d-17.
```

At `m=r+kT` with r among the last five of T=2d, the truncated sum `P4,m=sum_{n<m}h_n` contains exactly `2(k+1)` complete nonzero coefficient blocks of Q, so `P4,m(zeta_d)=2(k+1)Q(1)`. Also
`D C4(zeta_d)=-p0 * prod_{p in S4,p!=p0}(1-zeta_d^p)`. Multiplying the latter product by Q(1) gives `prod_{s=1}^{d-1}(1-zeta_d^s)=d`. Therefore,

```text
D B_{r+kT}(zeta_d) = -2(k+1)*p0*d.
```

At the exceptional phases `A_m(zeta_d)=0`, so

```text
D R_{r+kT}(zeta_d) = (k+1)*(c_r - 2*p0*d).             (*)
```

The quantity subtracted is a scalar integer; it changes only the coefficient of q^0 in the cyclic representation.

## Small exact nonzero certificate

Reduce cyclic coefficient vectors modulo the primitive cyclotomic polynomial: for d=23 use `v_i-v_22` (0<=i<=21); for d=25 use `v_i-v_{(i mod 5)+20}` (0<=i<=19). The following **index-1** coefficient of `c_r` is unaffected by the scalar `2*p0*d` in (*).

| d | exceptional r in [1,T] | index-1 coordinates, in increasing r |
|---|---|---|
| 23 | 42,43,44,45,46 | -28589, -4209, 47219, -66815, 33787 |
| 25 | 46,47,48,49,50 | -1090275, 1015225, -493900, 26000, 97675 |

Every one is a nonzero exact integer. Therefore (*) is nonzero for all k>=0, giving an **exact order-three pole** at every exceptional phase. All other phases have nonzero A_m(zeta_d), giving order four. A primitive-root pole of order three contributes a degree-two quasipolynomial Fourier term and forces d into the coefficient period at precision O_m(N).

## Verification, reproducibility, boundary

`VERIFY_JETS.py` recomputes the two exact-period jet sequences with Python arbitrary-size integers and exact cyclic convolution. It checks the primitive-root zero phases, the complete cyclotomic derivative relation `c_{r+T}=2c_r`, the ten independent index-1 witnesses, and the d=23 and d=25 m=46 derivative vectors by a **second implementation enumerating the original selected load inequalities directly**. `CERTIFICATE.json` stores the ten witnesses and direct-check rows. No floating point and no finite-sample-to-infinity extrapolation is used: the infinite step is the proper rational denominator analysis above.

The first-order jet is the lowest residual preserved after the value observer vanishes at an exceptional root. It is a precise typed refinement of the scalar generating-function observer; no claim is made that its numerical coordinates are native X6 Cell coordinates. Mathematical review remains `NOT_REVIEWED`; this is not a formal shared task Result, review or Working Truth.

Next: study d=23/25 next higher jets at O_m(1) and determine whether a smaller set of full-root coefficient invariants can replace the ten-vector certificate. Verify the inherited all-threshold O_m(N^3) theorem independently before any conditional global period statement is promoted.
