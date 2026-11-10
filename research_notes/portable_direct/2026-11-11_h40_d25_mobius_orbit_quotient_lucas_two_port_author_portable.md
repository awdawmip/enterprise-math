# D25/LIFT — Möbius orbit quotient: two-coordinate Lucas reconstruction of Clausen ports

2026-11-11. **AUTHOR-PROVED algebraic identity; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.** Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` OPEN. Canonical Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific input `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. Portable author evidence, no current native execution claim.

## Exact theorem (all primes p>5)

Write `p=6m+1+4ε`, where `ε=0` for p≡1 mod6 and `ε=1` for p≡5 mod6; m≥1. Define in F_p:

```text
K(X) = Σ[k=0..m] binom(m,k) binom(2m+ε,k) X^k
A = K(1/2); B=(1-6ε)K(1/2)+6K'(1/2)
D = F_p \ {0,-1,-2}; U(t)=(t+1)(t+2)^2/t
V_ε(t)=U(t)^m(t+2)^ε
w_ε(t)=[2-12ε-(3+10ε)t]/(t+2)
```

Use the **already established** two-branch moment laws `A=-2^{-(2m+ε)}Σ_D V_ε` and `B=-2^{-(2m+ε)}Σ_D V_ε w_ε` from [prior author proof](https://github.com/awdawmip/enterprise-math/blob/021b06753d070d2b69aa5f51a8eb5b73f805972e/research_notes/portable_direct/2026-11-11_h40_d25_both_branch_twisted_mobius_ports_author_portable.md).

For λ∈F_p\{-1}, let

```text
Δ=(λ+4)^2-8
ν=[1+Legendre(Δ,p)]/2, with Legendre(0,p)=0
C=(λ^3+10λ^2+27λ+20)/(λ+1)
α=(λ^2+6λ+7)/(λ+1)
L_0=2, L_1=C; J_0=0, J_1=1
L_{n+1}=C L_n-2L_{n-1}, J_{n+1}=C J_n-2J_{n-1}
L=L_m(C), H=αΔ J_m(C).
```

**Branch ε=0 (exact in F_p):**

```text
A = -2^(-2m) Σ_{λ≠-1} ν L
B = -2^(-2m) Σ_{λ≠-1} ν [(2λ+5)L-2H].
```

**Branch ε=1:** put `Q=[(λ+4)L+H]/2`, then

```text
A = -2^(-(2m+1)) Σ_{λ≠-1} ν Q
B = -2^(-(2m+1)) Σ_{λ≠-1} ν [16L-13Q].
```

These are universal identities for the stated primes, not finite-run extrapolations. At p=5 the earlier D-moment omits boundary terms; separately `A_5=1,B_5=0` by K_0=1.

## Complete algebraic proof

1. Under the previously established involution `T(t)=-2(t+1)/(t+2)`, set `t'=T(t)`, λ=t+t'. Straight algebra gives `λ=(t²-2)/(t+2)`, `tt'=-2(λ+1)`, so the fiber equation is `x²-λx-2(λ+1)=0`. Its discriminant is Δ. The excluded t=0,-1 are exactly the λ=-1 fiber; t=-2 is not a finite root. For each λ≠-1 there are two distinct, one double, or no F_p roots according as Legendre(Δ)=1,0,-1. Accordingly ν is 1,1/2,0, the exact weight for a *doubled* orbit sum.
2. Using the quadratic relation and `1/t=(t-λ)/[2(λ+1)]`, reduction of `U=(t+1)(t+2)²/t` gives `U(t)=αt+β`, where `β=(2λ²+10λ+10)/(λ+1)`. Consequently `U(t)-U(t')=α(t-t')`. Direct substitution also yields `U(t)U(t')=2`, `U(t)+U(t')=C`. These identities hold for double roots.
3. For roots y,y' of `Y²-CY+2`, the polynomial recurrences give `L_m=y^m+y'^m`, `y^m-y'^m=(y-y')J_m`. Therefore `(t-t')[U(t)^m-U(t')^m]=α(t-t')²J_m=H`, including Δ=0 by polynomial continuity.
4. For ε=0 the doubled local unweighted sum is L. Also `(t+2)(t'+2)=2` and `w_0(t)=-3+8/(t+2)=-3+4(t'+2)`. The doubled weighted sum is `-3L+4[(t'+2)U(t)^m+(t+2)U(t')^m]`. The bracket equals `(λ+4)L/2-H/2`, producing `(2λ+5)L-2H`.
5. For ε=1 the doubled local unweighted sum is `(t+2)U(t)^m+(t'+2)U(t')^m = [(λ+4)L+H]/2=Q`. Since `w_1(t)=-13+16/(t+2)`, the doubled weighted sum is `16L-13Q`.
6. Multiply local sums by ν and sum over λ≠-1; double roots count once, split roots twice, nonsplit roots zero. Finally apply the known original moment normalizations. QED.

## BRC typed-observer use and exact verification

The quotient preserves the two declared field observers `ΣV_ε` and `ΣV_εw_ε`, not all future pointwise operations. `H` is the necessary retained antisymmetric coordinate in the displayed reconstruction. At p=13, the aggregate Lucas sum `ΣνL=0` but `ΣνH=12`, while the weighted port B=6; discarding H changes the port. This is an exact information-loss witness.

An independent implementation computes original A/B from binomial integers, and the quotient from binary-exponentiated polynomial Lucas recurrences in `F_p[Y]/(Y²-CY+2)`. Fiber identities and fixed fibers are checked. All **364 primes 7≤p≤2500**, covering **419,710 original t**, passed. Counts ε=0:178; ε=1:186. Examples (p:A,B,ΣνL,ΣνH): `7:2,0,6,0`; `11:8,0,3,8`; `13:0,6,0,12`; `19:0,12,0,1`; `157:0,80,0,10`; `373:0,171,0,289`.

## Provenance and next exact action

The previous Möbius involution and two-branch moment representation are antecedents, not recredited. The new result is the **orbit quotient, cubic trace map C, Lucas observer pair and fixed-fiber aggregation**. The Legendre(-6/p) two-port selector remains a 3243-prime finite observation, not yet proved uniformly; the exact quotient isolates the Lucas cancellation problem. Next test a Cartier/eigenspace relation for the paired weighted Lucas sums, preserving the ε branch and the H coordinate.

Native original-class H0/B0 divided-power Frobenius, η/rank and κ versus Δ-R remain `NOT_RUN`; Source continuation still requires a current own issued session and winning CLAIM. UR V2 four-file original bundle also remains missing (historical 94,687 bytes; SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`). No repeat of finished UR mathematics.
