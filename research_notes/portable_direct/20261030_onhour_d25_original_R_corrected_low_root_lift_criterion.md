# D25 / SECOND-DIGIT-LIFT — exact original-R-corrected low-degree Gauss root criterion

2026-10-30 Asia/Hong_Kong · **AUTHOR-SIDE / PROVED SOURCE-FAITHFUL EQUIVALENCE / EXECUTED 166-PRIME EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING**.

This is a new **direct original-LIFT continuation** of the immediately preceding root cutoff transport `20261030_onhour_d25_gauss_cutoff_hensel_root_source_transport.md`, not another independent auxiliary theorem or a native H0/B0 experimental substitute. Research lane `chatgpt-research-onhour-enterprise-math-20260923` only; maintenance `chatgpt-hourly-enterprise-math-20260921` is separate. Original D25 task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` **unchanged**; P000 ACTIVE_LOCKED / ACTIVE worldview retained.

## Exact input (at original proof strength)

For every target prime `p=6m+1 ≡13,19 mod24`, let `a_n=binom(2n,n)^2 binom(3n,n)/216^n`, `A_p=sum_(n<p)(6n+1)a_n` and `c_n=(1/6)_n(1/3)_n/(n!)^2`. Define

```text
G_full(z) = sum_(0<=n<p) c_n z^n;
G_low(z)  = sum_(0<=n<=2m) c_n z^n;    # degree 2m, NOT P_m itself
z0=1/2; g=G_full'(z0)=G_low'(z0) (mod p^2), g != 0 (mod p);
zeta_full,zeta_low = unique Hensel roots congruent to z0 (mod p);
d_full=(z0-zeta_full)/p; d_low=(z0-zeta_low)/p;
F_p=(G_full(z0)-G_low(z0))/p^2 (mod p).
```

All p-divisions occur in `Z_(p)`. The source-frozen **signed** reflected scalar `R_p` is NOT replaced by a new fit. Its original definition (2026-10-26 exact port proof, commit `2d7bdfd7821d3afac8eaefb4b88bfedca8ff46be`) is

```text
B_i = c_i * 2^(-i),
C_1 = 1/10,
C_(a+1) = C_a * 36a^2/[(6a+5)(3a+2)] (mod p),
R_p = 2 sum_(i=1)^m B_i sum_(a=1)^i (1+6(i-a))*C_a (mod p).
```

The 2026-10-30 previously author-proved Gauss–Hensel theorem provides the **original observer equivalence**, under consumed CM0/simple zero and accepted first-digit UR,

```text
A_p ≡ p (mod p^3)  <=>  d_full ≡ d* (mod p^2),
t = g^(-2) (mod p^2),
d* = t/6 + p*(R_p*t/6 - t^2/54) (mod p^2).           (1)
```

Its signed residual transport is `(A_p-p)/p^2 ≡ 6g^2 (d_full-d*)/p (mod p)`; the left is the **original** `Delta_p-R_p` with its exact sign and Source cutoff. No unconditional LIFT vanishing is imported.

## New theorem: full original LIFT is equivalent to an explicit degree-2m root target

From the prior separate source-labeled factorial tail and the new proved low/full root transport,

```text
d_full = d_low + p*F_p/g (mod p^2).                        (2)
```

Substitution into (1) proves the **full-prime exact equivalence for both target classes**:

```text
A_p ≡ p (mod p^3)
   <=>
d_low ≡ t/6 + p*( R_p*t/6 - t^2/54 - F_p/g ) (mod p^2). (3)
```

Every factor on the right is explicitly given by the **degree-2m original Gauss polynomial** and two separate original source ports `R_p` (signed Clausen reflection) and `F_p` (valuation-two high-index Gauss tail). Because `G_full'-G_low'` is divisible by `p²`, the `g` and `t` in (3) may be computed from `G_low` modulo `p²`. Thus the original second-digit LIFT is reduced, with **no source erasure**, from a degree-(p−1) Hensel zero to a degree-2m Hensel zero plus two explicit finite sums.

The signed observer itself has a **strict residue-transport identity**:

```text
Delta_p - R_p ≡ 6g^2*((d_low-d*)/p) + 6g*F_p (mod p).  (4)
```

Here `d_low-d*` is divisible by `p` by the existing first-digit result. The term `6gF_p` is not generally zero; it is the exact correction for changing the observer's root carrier, **not** permission to identify an arbitrary truncated observable with `Delta` or to delete the original frozen `R_p`.

**Proof:** (2) is the earlier second-digit cutoff transport. Combine (2) with the previously proved full-root equivalence (1); subtract the same `d*` and use the already proved signed full-root transport to obtain (3) and (4). All inverses use p-units; quantifiers and sign are unchanged. This is an exact logical equivalence, not a proof of either side's universal truth.

## Executed original-source check

The exact Python script `d25_low_root_lift_original_R_guard_20261030.py` was run over **all 166 primes `13<=p<5000` with `p≡13,19 mod24`**, with terminal `PASS_D25_ORIGINAL_R_SOURCE_CORRECTED_LOW_ROOT_LIFT`. It *independently* computed the original weighted 216 `A_p` via integer-binomial factorial-ratio recurrence modulo `p³`, the original signed `R_p` via its own `C_a` recurrence/double sum (reordered into prefix sums), two Gauss Hensel roots, the independent `F_p` factorial formula, and both sides of (3)–(4). All 166 source-typed comparisons passed; in this finite range the original `A_p≡p mod p³` passed. These data do not establish the universal last assertion.

Representative `(p,R,F,d_low,d*_low,d_full,d*,naive_low_residual,corrected_residual)` modulo the indicated p-local powers:

```text
( 13,  0,   8,    115,    115,    50,    50,   4, 0)
( 19, 12,  10,    194,    194,   289,   289,  13, 0)
( 37, 11,   8,   1213,   1213,   991,   991,  27, 0)
( 43, 15,   7,   1724,   1724,   391,   391,  40, 0)
(157, 82,   0,   7434,   7434,  7434,  7434,   0, 0)
(211,119, 130,   5320,   5320, 25787, 25787, 101, 0)
(373,196, 252, 118340, 118340, 19122, 19122, 176, 0)
```

At `p=373`, the naive truncated-root error is **176**, and the required high-tail signed correction is **197**; `176+197=373 ≡0`. At `p=13`, the analogous pair is `4+9=13`. If the high-tail source is **silently deleted**, the low-root shortcut produces a wrong original residual at 165 of the 166 checked primes. The exceptional `p=157` with `F_p=0` is an actual exact finite exception, not an all-prime classification. This refutes the shortcut **at fixed primes**, while the exact corrected reduction (3) remains a proved all-prime equivalence conditioned on the consumed original CM0/UR source.

## Frontier and Source boundary

The minimal remaining **math** action is to derive the predicted second digit of `d_low` *uniformly*, using the explicitly indexed low-rank p-adic deformation with the **separately retained** signed `R_p` and tail `F_p`. Equation (3) does not itself provide that proof. Previous other-lane GH-161/GH-162 marked three-isogeny reflected stationarity is a distinct source observer and is not silently identified with the frozen original `R_p`.

The highest-priority **native** experiment remains #1559 OPEN/PENDING_OWNER: original class fixed `p=373` H0/B0 divided-power `[X]U mod 139129`, actual Frobenius/eta, module rank, signed odd Green/Hesse and `kappa`, plus independent execution/replication. No execution, formal Source CLAIM/checkpoint, Result or admission is implied by this portable proof and checker. Current Site `research_authority_granted=false`, `write_relay_enabled=false`, upstream source `CODE_REVIEW_REQUIRED`, `executor_binding_configured=false`; preserve the old correct-lane request IDs and the neutral staging archive rather than retrying a denied mutation. Keep Source scientific pin, true Research lane and existing scheduler unchanged.
