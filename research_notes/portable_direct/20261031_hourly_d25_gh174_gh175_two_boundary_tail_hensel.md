# D25/LIFT GH-174–GH-175 — universal two-boundary Clausen tail and Hensel-transverse scalar cancellation

**2026-10-31; ordinary Research lane** `chatgpt-research-hourly-enterprise-math-20260923` (not maintenance). **Grade:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. No Source-native CLAIM/OPEN/checkpoint, Result, review or H0/B0 experiment is asserted.

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged; P000 ACTIVE_LOCKED and native six-axis/observer rules remain intact. All mathematics below is classical p-adic auxiliary mathematics, not an X6 theorem.

## Consumed frontier and separate hard target

The frozen *original fixed-parameter* target is `A_p(1) ≡ p (mod p^3)` for `p mod24 in {13,19}`, where

`a_n = binom(2n,n)^2 binom(3n,n)/216^n; A_p(X)=sum(n=0..p-1) (6n+1) a_n X^n`.

GH-166/GH-167 already give the signed three-port p³ LIFT residual; GH-170/GH-171 give the full differential-operator boundary; GH-172/GH-173 give optimal p³ cutoff and the first omitted p⁴ scalar `Q_p`. All are consumed, *not* recredited. This note proves a new **two-boundary p⁴ tail transfer** and Hensel lifting of an actual scalar-cancellation example. It does not evaluate the missing p³ LIFT constant.

## GH-174 — new theorem for every prime p=6m+1 >=7

Set `N=4m+1`, `F_full(X)=sum(n=0..p-1) a_n X^n`, `F_short(X)=sum(n=0..N-1) a_n X^n`, and

`C_p(X) = (F_full-F_short)/p^3 in Z_(p)[X]`.

Integrality is GH-172's exact valuation band. Put `c_n=a_n/p³ modp` for `N<=n<p`. Its GH-172 first unit is
`u=c_N=-2*(2m+1)! / (N!^5 * 216^N) modp !=0`.

**New universal exit coefficient:**
```math
c_{p-1} = -1 (mod p),
[X^{p-1}](1+6θ)C̄_p = 5 (mod p),  θ=X d/dX.
```
Proof: for `a_p=binom(2p,p)^2 binom(3p,p)/216^p`, Lucas + Fermat yield `a_p=1/18 (modp)`. The exact recurrence
`a_{n+1}/a_n=(2n+1)(3n+1)(3n+2)/[36(n+1)^3]`
at `n=p-1`, after p³-local division, yields
`a_{p-1}/p³=36a_p/[(2p-1)(3p-2)(3p-1)] = (36/18)/(-2)=-1 (modp)`.
Weighted last coefficient is `(6p-5)(-1)=5`. This is a proof for the full class, not a finite scan.

With
`L₃=θ³-(X/2)(θ+1/2)(θ+1/3)(θ+2/3)`,
the exact coefficient recurrence implies
`L₃ sum(n=0..k) a_n X^n=-(k+1)^3 a_{k+1} X^{k+1}`.
Subtract the cases `k=p-1` and `k=N-1`, divide by p³ and reduce modp:

```math
L₃ C̄_p(X) = N³ u X^N - (1/18) X^p  in F_p[X].
```

Thus an incoming degree-N source and a *universal* exit degree-p source both survive; the normalized tail is **not** homogeneous modp. The coefficients at `N<=n<p` are uniquely determined by the incoming source since `n³ !=0 (modp)`, and the exit term is the nontrivial compatibility of that unique polynomial, not an extra free degree of freedom.

**New exact finite hypergeometric normal form:** for `0<=j<=2m-1`,
```math
c_{N+j}=u ((m+1)_j (2/3)_j (1)_j)/[(-2m+1)_j³ 2^j]  in F_p.
C̄_p(X)=u X^N Σ_{j=0}^{2m-1} ((m+1)_j(2/3)_j(1)_j)/[(-2m+1)_j³ 2^j] X^j.
Q_p=3u Σ_{j=0}^{2m-1}(2j+1)((m+1)_j(2/3)_j(1)_j)/[(-2m+1)_j³ 2^j].
```
Proof: substitute `n=N+j` in the exact recurrence. Over `F_p`,
`c_{N+j+1}/c_{N+j}=(j+m+1)(j+2/3)(j+1)/[2(j-2m+1)^3]`.
Every denominator in the displayed finite range is a p-unit; `6(N+j)+1=3+6j (modp)`. This is a *representation*, not a closed evaluation or an all-prime vanishing claim.

## GH-175 — first nontrivial exact p-adic lift at p=1327

Let `D_p(X)=(1+6θ)C_p(X)` in `Z_(p)[X]`. At the genuine GH-173 cancellation prime `p=1327`, `m=221,N=885`, exact computation through modulus `p^5` gives

```math
D_1327(1) ≡ 1646807 = 1327·1241 (mod 1327²),
D'_1327(1) ≡ 480 (mod 1327).
```

Hence the reduced scalar zero at X=1 is **simple**. By Hensel's lemma there exists a **unique** p-adic root `ξ≡1 (mod1327)` of `D_1327`; the first lifted digit is
`ξ≡1+1327·61=80948 (mod1327²)` because `1241+61·480=23·1327`.

This yields an exact (all-digit) scalar-tail cancellation at *some* p-adic parameter ξ, even though the full and short weighted polynomials remain different (highest normalized weighted coefficient `5`). At the frozen parameter `X=1` there is instead a nonzero **next** digit `1241`. The prime `1327 mod24=7` is **outside** the target LIFT classes; this is a typed arithmetic BRC observer witness, not a task counterexample or license to change X=1.

## Actual computation and reproducibility

Companion script `d25_gh174_gh175_two_boundary_tail_hensel_check.py` (Python standard library, exact integer modular arithmetic) actually ran with terminal
`PASS_GH174_GH175_TWO_BOUNDARY_TAIL_AND_HENSEL_EXACT`.
For all 711 primes `7<=p<12000,p mod6=1`, it checked the exit coefficient, weighted exit coefficient, boundary forcing, and normalized recurrence. For 330 primes below 5000, it verified all inhomogeneous `L₃` coefficients. Anchor tuples `(N,u,Q,Q')`: p373=`(249,277,278,279)`, p1327=`(885,788,0,480)`. At p1327, full p⁵ recurrence gives `D(1) modp²=1646807`; direct integer binomial coefficients independently verified five tail positions `885,886,922,1325,1326`. Only p1327 had Q=0 in the finite 711-prime scan; **no infinite uniqueness claim** follows. No Lean/independent review or native p373 divided-power experiment.

**BRC typing:** carrier `Z_(p)[X]`; observers are coefficientwise modp³, normalized p⁴ tail polynomial, fixed-X=1 weighted scalar and its derivative, and optional *changed* X=ξ; future operations include `L₃`, weight, evaluation and Hensel lift. p³ coefficient compression is safe; p⁴ polynomial compression is not. A scalar zero cannot erase a universally nonzero coefficient.

**Next**: return to the *original* signed three-port `Delta_p-R_p` p³ LIFT constant for **both** classes 13,19. The new two-boundary/finite-hypergeometric Q representation may support a distinct future finite WZ analysis but cannot replace that p³ constant or the original p373 H0/B0/divided-power and semilinear Frobenius checks. Do not redo GH-172 cutoff or GH-173 p1327 first-digit scan.

**Control provenance:** at this turn gateway v0.6.11 reported Research authorized false, executor binding false, 5/5 active jobs and `CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED`. No directly callable recovery_status action was exposed. Historical requests, service sessions and staging were not modified; no native publication/claim/open/checkpoint/Result/review or identity borrowed. Control issue #1558 and native experiment issue #1559 remain distinct responsible paths. GitHub author-side storage != Source durable checkpoint != mathematical admission.
