# D25 SECOND-DIGIT-LIFT — exact identification of the frozen R_p with the finite Clausen boundary

Date: 2026-11-07 (Asia/Hong_Kong). Author-side portable mathematical research for `chatgpt-research-onhour-enterprise-math-20260923`; excludes CONTROL_PLANE_MAINTENANCE. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, immutable publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Status: AUTHOR-SIDE ALGEBRA PROVED / FINITE VERIFIED / UNREVIEWED / NOT_ADMITTED. P000 remains unchanged.

## Frozen source, not a guessed definition

The accepted-parent return `research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md` (§§2,6,11) binds the exact second-digit scalar `Delta_p=(G_p h-1)/p` and cites the immutable predecessor `a722292873eba2449f0959fad7b766a12741ff47`. At that commit, `scripts/check_enterprise_brc_half_coupling_inert_plus_terminating_jacobi_jet_certificate.py` (blob `81c26f7a270392541ad24415da5ce0741fef5068`) defines the independent `reflected_Cs` and `reflected_R` formula actually used to check JT2. We read that exact source rather than defining R := Delta.

For a prime p=6m+1>3 set
```
u_k=(1/6)_k(1/3)_k/(k!)^2,  B_k=u_k*2^(-k),  0<=k<p
g=sum(B_k),  h=sum((12k+1)B_k),  G_p=g/p
a_n=(2n)!(3n)!/(216^n(n!)^5), W_p=sum_{n=0}^{p-1}(6n+1)a_n.
C_1=1/10, C_{ell+1}/C_ell=36 ell^2/((6ell+5)(3ell+2)), 1<=ell<m.
R_p=2 sum_{i=1}^m B_i sum_{ell=1}^i (6(i-ell)+1)C_ell  [mod p].
```
All rational expressions are in Z_(p). In particular, denominators in the displayed recurrences are p-units.

## Theorem A: exact independent-observer identification (ALL p=6m+1>3)

The earlier finite Clausen proof introduced high-index coefficients `H_1=1/10`,
`H_{ell+1}/H_ell=18 ell^2/((6ell+5)(3ell+2))`, with
`H_ell = u_{p-ell}/p^2 (mod p)` and boundary
```
K_p = sum_{1<=ell<=i<=m} (6(i-ell)+1) u_i H_ell 2^{-(i-ell)}  [mod p].
```
The exact rational recurrence relation `C_ell=2^{ell-1}H_ell` holds by equal initial data and ratios. Since `B_i=u_i 2^{-i}`, termwise
```
  2 B_i C_ell
= 2 u_i 2^{-i} 2^{ell-1}H_ell
= u_i H_ell 2^{-(i-ell)}.
```
Summing with the original signed weight `6(i-ell)+1` gives

**R_p = K_p (mod p)**,

with an identity of rational lifts if K uses the rational recurrence H rather than only its reduction. The mapping preserves the independent frozen R source, low-index i, reflected high-index p-ell, the ordered pair and its signed weight. It was absent from the previous author-side Gauss/Clausen notes, which explicitly left this identification unverified.

## Theorem B: exact single-scalar equivalent of frozen LIFT

The formal Clausen square gives a finite polynomial identity
```
 W_p = g*h - T_p,
 T_p=sum_{0<=i,j<p; i+j>=p}(6(i+j)+1)u_i u_j 2^{-(i+j)}.
```
Using the *existing* coefficient valuations `v_p(u_k)=0,1,2` on `[0,m],[m+1,2m],[2m+1,p-1]`, only ordered low/high pairs with `1<=ell<=i<=m` survive modulo p^3, giving `T_p/p^2=K_p (mod p)` by the earlier proved Clausen tail lemma. Theorem A therefore yields for EVERY p=6m+1>3:

**W_p = g h - p^2 R_p (mod p^3).**

For p≡13,19 mod24, consume the accepted CM0 and UR/JT0: `g in p Z_(p)` and `G_p h=1 (mod p)`. Hence all divisions below exist in Z_(p) and

**(W_p-p)/p^2 = Delta_p - R_p (mod p).**

Consequently frozen `LIFT: Delta_p=R_p (mod p)` is *exactly* equivalent, under accepted UR, to the ONE-SUM residual
```
sum_{n=0}^{p-1}(6n+1)(2n)!(3n)!/[216^n(n!)^5] = p (mod p^3).
```
This equivalence removes separate evaluation of Phi_xx, derivative/Frobenius and the reflected R port at the **final** check while retaining their original provenance in the proof. It does not assume the single-sum congruence itself.

## Exact computation and discrimination

Companion `d25_frozen_R_clausen_bridge_20261107.py` computes B and a by *different* modular recurrences modulo p^3; R from the immutable reflected_Cs recursion; K independently from the high-end 18-recursion and an ordered prefix sum (plus a separate explicit double sum for p<=373). Actual local Python standard-library execution:

- all 330 primes p<5000 with p≡1 mod6: R=K and `g*h-W=p^2 R (mod p^3)`, 0 failures;
- the 166 target primes among these: `Delta-R=(W-p)/p^2 (mod p)`, 0 failures;
- p=19: R=K=Delta=12, W mod p^3 =19;
- p=373: R=K=Delta=196, W mod p^3 =373.

These finite checks validate the observer mapping and sign conventions; the general equalities above follow from exact recurrences and the reused Clausen proof, not from extrapolating these checks.

## Continuation / authorization boundary

Task publication `TP2-B6F4FC938FF94941C1B7` remains open: the all-target W_p third-digit supercongruence (equivalently LIFT) still requires a proof or an exact refutation. The next discriminating unit is a WZ/creative-microscoping or CM Gauss-jet identity on the *single* original216 signed sum modulo p^3; preserve the already proved R/K source map rather than revisiting first-digit D8/Pfaff or rebuilding three-band harmonic carriers. A candidate identity must be tested at p=19 and p=373 and prove uniform behavior for both target classes.

Native Source original target_request_id: `onhour11-20261106-1400-exact-research-lane-continuation`, UNKNOWN. 2026-11-07 Site reports `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`; original receipt and checkpoint reads return `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`. Session/CLAIM/run not verified; register pending / sync debt. A Site-bound backend client, approved version and secure user-entered credential remain operator prerequisites to read/reconcile exact continuation. Do not send a new claim or adopt maintenance identity. Native p=373 H0/B0, divided-power, Frobenius/κ and independent reproduction under issue #1559 remain OPEN / NOT_EXECUTED / PENDING_OWNER; this is an author-side mathematical bridge, not the native benchmark or a canonical Source Result.
