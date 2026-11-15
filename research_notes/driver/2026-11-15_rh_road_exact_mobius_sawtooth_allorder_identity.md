# RH full-integer composite road: exact Möbius fractional-part identity and all-order coefficient correspondence

Date: 2026-11-15.
Status: SCOPED RESEARCH_DRIVER MATHEMATICAL DERIVATION / EXACT IDENTITY. Not a native Result, independent acceptance review, bound for the unbounded escape tail, or proof of RH.

Provenance: independent supplementary derivation by RESEARCH_DRIVER EM-DVR-DEBB5E. Original full-integer road and scientific target: EM-FREE-C4A91D; RH-ROAD-TAIL-20260909 / TP2-DCE65A0EFCE8151C39BD. The published first- and second-order coefficients and their prior authorship are preserved; no researcher CLAIM is adopted.

## 1. Exact identity for every a>0 and integer N>=1

Keep the original definitions

```text
R_a(1)=1;
R_a(n)=product_{p|n}(1-p^{-a});
S_a(N)=sum_{n<=N} R_a(n);
c_a=1/zeta(1+a);
B_{a,N}=S_a(N)-1-(N+1/2)c_a.
```

Let mu be the ordinary Möbius function, {x}=x-floor(x), and set

```text
F_a(N) = sum_{d<=N} mu(d) d^{-a} {N/d},
T_a(N) = sum_{d>N} mu(d) d^{-1-a}.
```

**Theorem 1 (exact full-road decomposition).** For every real a>0 and integer N>=1,

```text
B_{a,N} = -1 - c_a/2 - F_a(N) - N T_a(N).             (1)
```

The infinite tail T_a converges absolutely for every fixed a>0. Nothing is dropped or approximated: all positive integers and their complete composite structure are retained.

**Proof.** The squarefree-divisor expansion

```text
R_a(n) = sum_{d|n} mu(d)d^{-a}
```

gives, by finite divisor inversion,

```text
S_a(N) = sum_{d<=N} mu(d)d^{-a} floor(N/d).
```

Also the absolutely convergent Dirichlet series gives

```text
c_a = sum_{d>=1} mu(d)d^{-1-a}.
```

Replace floor(N/d) by N/d-{N/d}, subtract (N+1/2)c_a and then subtract 1. The result is (1). QED.

The split identifies two quantities that any proposed escape-tail argument must jointly control: the *finite fractional-part transform* F_a and the *infinite weighted Möbius tail* N T_a. A triangle bound for either term alone need not respect their possible cancellation. No new estimate for either term is asserted.

## 2. Boundary a=0 and exact first-order bridge

The classical prime number theorem implies sum_{d>=1} mu(d)/d=0, with convergence in natural order. Therefore (1) extends continuously to a=0: c_0=0, R_0(n)=1_{n=1}, B_{0,N}=0, and

```text
sum_{d<=N} mu(d){N/d}
  + N sum_{d>N} mu(d)/d = -1.                       (2)
```

To differentiate at zero, we use the standard unconditional zero-free-region/Mertens estimate of the form

```text
M(x)=sum_{d<=x}mu(d)
    =O(x exp(-c (log x)^{3/5}/(log log x)^{1/5}))
```

for sufficiently large x and some c>0. This *imported* classical estimate is stronger than bare PNT and ensures, by summation by parts, convergence of sum mu(d)(log d)^k/d for every fixed k>=0 and uniform convergence of its shifted series on compact a-intervals in [0,infinity). It justifies the following boundary derivatives. It is not proved anew here.

Since c_a=a-gamma a^2+O(a^3) and S'_0(N)=psi(N), differentiating (1) at zero gives the exact identity

```text
sum_{d<=N} mu(d) log(d) {N/d}
 + N sum_{d>N} mu(d) log(d)/d
   = psi(N)-N.                                      (3)
```

Here psi(N)=sum_{p^j<=N}log p counts each prime power exactly once. This can also be checked directly using sum_{d|n}mu(d)log d=-Lambda(n) and sum_{d>=1}mu(d)log d/d=-1.

Equation (3) identifies the *same* first-order PNT discrepancy psi(N)-N that occurs in the earlier near-field research, without changing to a prime-only road. The term -1/2 in B'_0 arises solely from the original centering -(N+1/2)c_a.

## 3. All fixed Taylor orders and the exact second-order bridge

For every integer k>=1, define the *finite arithmetic coefficient* and *normalization coefficient*

```text
A_k(N) = (-1)^k/k! sum_{d<=N} mu(d)(log d)^k floor(N/d),
C_k    = (1/k!) [d^k/da^k](1/zeta(1+a)) at a=0,
```

and the Möbius fractional-part expression

```text
Xi_k(N)= sum_{d<=N} mu(d)(log d)^k{N/d}
       + N sum_{d>N} mu(d)(log d)^k/d.
```

By the same quantitative Mertens bound, termwise derivatives of the Dirichlet tail are justified at zero. Since

```text
sum_{d>=1} mu(d)(log d)^k/d = (-1)^k k! C_k,
```

the exact finite divisor identity yields

```text
Xi_k(N) = (-1)^k k! [N C_k - A_k(N)].                (4)
```

Consequently, for the centered-road Taylor coefficient

```text
b_k(N) := (1/k!) B_{a,N}^{(k)}|_{a=0}
        = A_k(N)-(N+1/2)C_k,
```

one has the second exact identity

```text
b_k(N) = (-1)^{k+1} Xi_k(N)/k! - C_k/2.             (5)
```

These are identities *for each fixed k and each finite N*. They supply no uniform control over k, a or N, and exchanging the Taylor expansion with the infinite road energy is not authorized by (4)–(5).

For k=1: A_1(N)=psi(N), C_1=1, giving (3) and
b_1(N)=psi(N)-N-1/2.

For k=2: A_2(N)=H_2(N), C_2=-gamma, where H_2 is the complete composite-road coefficient from the earlier exact expansion. Equation (4) becomes

```text
sum_{d<=N} mu(d)(log d)^2{N/d}
 + N sum_{d>N}mu(d)(log d)^2/d
   = -2[H_2(N)+gamma N].                            (6)
```

Equation (5) then reproduces, with the original centering,
b_2(N)=H_2(N)+gamma(N+1/2). Thus the previously proved quantitative cancellation of H_2(N)+gamma N is equivalent to a quantitative cancellation of the *second-order Möbius fractional-part-plus-tail combination*. This is an exact reformulation, not another proof of the PNT-based decay rate.

## 4. Scope, reproducibility and open scientific question

Theorem 1 is an unconditional elementary identity for each a>0. The a=0 derivative family additionally imports an explicitly identified classical quantitative Mertens bound, as above. In a separate 40-decimal-digit evaluation at a=0.37 and N=1,2,6,20,100, direct full-road computation and the right side of (1) agreed within 3e-40 (tail evaluated as c_a minus the finite Dirichlet prefix). Finite k=1,2 checks at N=2,10,50,100 agreed to working precision; the symbolic proofs do not rely on those examples.

**Actual advance:** an exact, source-faithful transfer of the full road and every fixed derivative to a weighted Möbius fractional-part transform plus an explicitly separated tail. A future *discriminating* task can test whether cancellation between these two terms can be retained in a uniform-in-a L² estimate. Separate absolute-value controls are insufficient without a summable N-bound.

**Not established:** no uniform control of sum_{N>L(a)} B_{a,N}²/N², no new zero-free region, no RH equivalence or proof, no native Result admission, no independent mathematical review, no completion of RH-ROAD-TAIL or its mother objective.

Related exact published science (preserved sources):
- awdawmip/enterprise-math@88c0c896181727ebb3fa9f6645f025491b0ac957:research_notes/driver/2026-11-15_rh_road_secondorder_uniform_composite_expansion.md
- awdawmip/enterprise-math@bb38bd21005fc712a5252a261e89f8b1d2af2470:research_notes/driver/2026-11-15_rh_road_secondorder_coefficient_pnt_cancellation.md
- awdawmip/enterprise-math@136a9756df0e69187b80178df798cc969af3398c:research_notes/driver/2026-11-15_rh_road_vinogradov_korobov_extended_nearfield.md
