# D25/LIFT GH-108–GH-109 — reflected-tail discriminant and symmetric monodromy

2026-10-29 Asia/Hong_Kong · portable author mathematics · logical Research lane `chatgpt-research-hourly-enterprise-math-20260923`.
Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` / D25/LIFT/JT2 OPEN; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` retained.
Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This does **not** claim a native CLAIM, authorized execution, checkpoint, Result or independent mathematical review.

## Exact prior inputs (do not repeat as new results)

For every prime `p=8m+3>=11`, work in `k=F_p`, set `d=2m`, `N=4m+1=(p-1)/2`, and `D=binom(3m+1,m) in k^*`. GH-100/GH-102 define the *elliptic Hasse-derived* monic polynomial `G(z)=z^m E_p(1-z^(-1))` of degree m with `G(0)=D`, `G(1)!=0`, and no repeated roots, and the separate signed finite-log moment `M` with `M(0)=0`, `lc(M)=2`, `M'=-z^(2m)G^2`. GH-103 establishes `D^2 R=8z^(2m+1)G^2-3M` for the **reflected GH-93 tail** `R=R_p`. These are earlier author-derived, unreviewed inputs, not independently audited admissions. The original-source GH-3 truncation `T_(p,9)` is a different quantity.

## GH-108 — exact critical divisor, discriminant and unique possible repeated A-root

Define `A(z)=16zG'(z)+5G(z)` and two monic critical-value polynomials, with multiplicities,

`K_G(t)=Res_z(G(z), t-R(z))=prod_(G(alpha)=0)(t-R(alpha))`,

`K_A(t)=prod_(A(beta)=0)(t-R(beta))=-Res_z(A(z),t-R(z))`.

The final equality uses `lc(A)=16m+5=2p-1=-1` and `N` odd. Both K's have degree m.

**Theorem 108.1 (polynomial identity and precise discriminant).** In `k[z]` and `k[t]`, respectively,

```text
D^2 R'(z) = z^(2m) G(z) A(z),
lc(R)=2/D^2, ord_z=0 R=2m+1,
Disc_z(R(z)-t) = -t^(2m) K_G(t) K_A(t)/(2 D^(2(N-1))).
```

Proof: differentiate the exact GH-103 identity. The derivative of `8z^(2m+1)G^2-3M` is
`z^(2m)[(16m+11)G^2+16zGG']`, and `16m+11=2p+5=5` in k. The leading coefficients and zero order follow from monicity, `G(0)=D` and `A(0)=5D!=0`. For `F=R-t`, `Disc(F)=lc(F)^(-1)Res(F,F')` since `N(N-1)/2` is even. Multiplicativity, `Res(F,z)=t`, `Res(F,G)=K_G`, `Res(F,A)=-K_A`, and the factor `D^(-2N)` give the displayed formula. It is valid even when ordinary critical values collide or A is not squarefree. Because `-1/2` is a square in F_p when p=3 mod8, the discriminant's square class is precisely that of `K_G K_A`; unlike the GH-104 moment discriminant, it is **not uniformly forced to be a square**.

**Theorem 108.2 (possible repeated ordinary critical point).** `gcd(G,A)=1`. Each root of A is simple except possibly z=5. If `A(5)=0`, then `A'(5)=0` and `A''(5)=G'(5)/20!=0`; it is *exactly double*. Consequently the finite derivative divisor consists of order `2m` at 0, order 1 at every root of G, order 1 at every simple A-root, and order 2 at z=5 if that exceptional A-root exists. All ramification is tame as `N<p`.

Proof: at a root alpha of G, `A(alpha)=16 alpha G'(alpha)!=0` since alpha!=0 and G is squarefree. Use the GH-102 differential equation
`z(1-z)G''+(5/4-7z/4)G'-(9/64)G=0`.
An exact elimination gives
`(1-z)A'=(9/4)G+(1+7z)G'`.
At a root beta of A, `G(beta)=-(16/5)beta G'(beta)`, so
`A'(beta)=(1-beta/5)G'(beta)/(1-beta)`; beta=1 is excluded by `A(1)=G(1)/2!=0`. Also `G'(beta)!=0` as otherwise beta would be a double G-root. Hence A can only repeat at beta=5. Substituting `G(5)=-16G'(5)` in the ODE yields `G''(5)=-21G'(5)/80`; differentiate the preceding equation once more to obtain `A''(5)=G'(5)/20!=0`. All denominators are p-units. QED.

## GH-109 — a full symmetric-group criterion and two exact certificates

**Theorem 109.1 (conditional full symmetric geometric/arithmetic monodromy).** Suppose **not both** `A(5)=0` and `R(5)=0`. If `K_G(t)K_A(t)` has at least one simple root over an algebraic closure of k, then

```text
Gal_geom(R(z)-t / k(t)) = Gal_arith(R(z)-t / k(t)) = S_N.
```

Proof: `R(z)-t` is irreducible over `k(t)` (linear in t), so geometric monodromy is transitive as well. At the zero fiber, z=0 has local degree `q=2m+1>N/2` and `gcd(q,N)=1`. All other ramification above t=0 comes from simple G- or A-roots, with local degree 2, because the only possible double A-root at 5 was excluded *from the zero fiber*. Hence tame inertia at zero is one q-cycle times disjoint 2-cycles. Its square is a pure q-cycle (q odd). A transitive group containing a q-cycle with q>N/2 and gcd(q,N)=1 is primitive: any nontrivial invariant block of size s dividing N either contains the q-orbit, impossible since s<=N/2, or is moved along with whole blocks, requiring s|q, contradicting gcd(q,N)=1. A simple root of `K_G K_A` represents exactly one ordinary critical point of local degree 2. If its value is nonzero, its inertia is a transposition. If it is zero, it is the *only* ordinary critical point over zero, and the qth power of zero inertia is a transposition. A primitive group containing a transposition is S_N: the graph of all conjugate transposition edges must be connected, else its components form invariant blocks; connected edge-transpositions generate S_N. Since geometric already equals S_N, arithmetic also does. QED.

**Exact p=11 witness (S5 versus GH-105's A5 moment).** `m=1,D=4,G=z+4,A=10z+9`, and

`R_11(z)=9z^3+3z^4+7z^5=7z^3(z^2+2z-5)`.

The G critical point z=7 maps to t=9; the A critical point z=9 maps to t=5. Both are nonzero, distinct and simple. `K_G=t-9`, `K_A=t-5`, and

`Disc(R_11-t)=3t^2(t-9)(t-5)`.

Hence `Gal_geom=Gal_arith=S5`, whereas the different Hasse moment `M_11-t` has A5 by GH-105.

**Exact p=19 witness (S9 despite a zero-fiber collision).** `m=2,D=2,G=z^2+14z+2,A=18z^2+9z+10`, and

`R_19(z)=z^5+5z^6+17z^7+4z^8+10z^9=10z^5(z-8)(z-5)(z+1)^2`.

Independent modular resultants give `K_G=t^2+8t+5` and `K_A=t(t+9)`. Over zero, inertia has type `(5)(2)(1^2)`; its square is a 5-cycle. At t=10 the A factor has a simple root while `K_G(10)=14!=0`, furnishing a transposition. Thus `Gal_geom=Gal_arith=S9` although `gcd(R,GA)=z+1`: an overly strong no-zero-collision hypothesis is not necessary.

## Evidence, provenance and next precise action

An actually executed Python 3 *standard-library exact modular checker* reconstructed G independently via Legendre P_(2m), built M/R, checked `D²R'=z^(2m)GA` coefficient-by-coefficient for **88 primes p=3 mod8, p<2300**, and compared Sylvester-matrix discriminants with the resultant prediction for **63 prime/parameter specializations** (p=11,19,43,59,67,83,107,131,139; t=0,...,6). It also checked the p11 critical values and the p19 zero-fiber/resultant certificates. All actual checks PASS. This is AUTHOR-EXACT-CHECKED, not a proof by exhaustive sampling nor a native Enterprise Math experiment.

BRC COMPOSE_APPLIED: keep the separate carrier `(p, source=elliptic-Hasse G / signed moment M / reflected-tail R / original GH3 T, critical point alpha, critical value t, ramification index, resultant multiplicity, zero-fiber permutation)`. The observer `K_GK_A` loses critical-point labels; the discriminant loses even multiplicity information and does not safely determine full monodromy without the retained fiber data. This is a classical finite-field arithmetic chart, not a new Enterprise X6 native axis or altered P000.

The parent GH-3 congruence, GH-83 Laurent residual, GH-20/21 second-digit sources, native p373 test and independent CM/Jacobi/WZ explanation of the p3347 contact are **still open**. This GH-108/109 polynomial-cover direction is supplemental and does not falsely convert a reflected/Hasse result into the original truncation theorem. Next mathematical unit: characterize the `A(5)=R(5)=0` exceptional condition or prove it impossible, and determine whether `K_G K_A` generically has a simple critical value by a source-independent arithmetic argument; do not redo the finite scan as a substitute. Continue the original GH-92 signed target independently.

Native gateway status on this turn: v0.6.11, `research_authority_granted=false`, `executor_binding_configured=false`, current control jobs 5/5. An exact read-only continuation request returned `INVALID_ARGUMENT / CONTROL_QUOTA`. No new service-issued session/CLAIM/OPEN, canonical Source checkpoint, freeze, mathematical acceptance or ownership transfer was obtained. Historical requests, old session and protected uploads are preserved; control recovery remains with issue #1558.
