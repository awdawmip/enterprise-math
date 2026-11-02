# D25: exact ordered-pair Cauchy source and third-digit moment closure

Date: 2026-11-02. Research lane provenance: `chatgpt-research-hourly-enterprise-math-20260923` (not an assertion of native owner authorization). Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3`. State: AUTHOR-DERIVED / ALGEBRAICALLY PROVED / EXACT INTEGER CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Predecessor U3/U4: `research_notes/portable_direct/20261102_hourly_r11_d25_cauchy_character_binomial_harmonic_lift.md`.

## V1: exact ordered-pair cancellation

For any prime `p=6r+1>=7` and `1<=s<=m<=2r`, define in the p-local rationals

```
a_m=(1/2)_m(1/3)_m(2/3)_m/(m!)^3,
b_s=(1/2)_s/(2^s s!),  u_s=-1/(4s b_s),
T_m=(-1)^m 2^(-m) C(3r,m) C(2r,m) C(4r,m),
v_s=(-1)^(s+1) 2^s/[4s C(3r,s)].
```

Let the *typed multiset* of factor weights be

```
B(m,s)={1/[2(3r-j)]:s<=j<m}
      +{1/[3(2r-j)]:0<=j<m}
      +{2/[3(4r-j)]:0<=j<m}.
```

**Exact rational identity:**

```
a_m*2^(-m)*u_s = T_m*v_s * PROD_{w in B(m,s)} (1-p*w).      (V1)
```

**Proof.** Substitute the exact parameter shifts `1/2=-3r+p/2`, `1/3=-2r+p/3`, `2/3=-4r+2p/3` in the three Pochhammer products. The `1/2`-band of `a_m` carries factors for `0<=j<m`, while the reciprocal `1/b_s` carries the inverse factors for `0<=j<s`. Because `s<=m`, the first `s` factors cancel *exactly*. The remaining two bands are unchanged; the terminating binomial baselines multiply to `T_m*v_s`. All denominators are p-units on these ranges. Therefore for every `q>=1`

```
a_m*2^(-m)*u_s = T_m*v_s *
  SUM_{k=0}^{q-1} (-p)^k e_k(B(m,s))   (mod p^q),
```

where `e_k` are the elementary symmetric polynomials (`e_0=1`). This all-precision statement preserves each original ordered `(m,s)` and its three factor-family origins.

## V2: exact four-prefix-moment reconstruction at p^3

Define

```
alpha_m = SUM_{0<=j<m} [1/(2(3r-j))+1/(3(2r-j))+2/(3(4r-j))],
sigma_m = SUM_{0<=j<m} [1/(4(3r-j)^2)+1/(9(2r-j)^2)+4/(9(4r-j)^2)],
beta_s  = SUM_{0<=j<s} 1/(2(3r-j)),
tau_s   = SUM_{0<=j<s} 1/(4(3r-j)^2).
V_m=SUM_{s=1}^m v_s, E_m=SUM_{s=1}^m v_s*beta_s,
F_m=SUM_{s=1}^m v_s*beta_s^2, G_m=SUM_{s=1}^m v_s*tau_s.
```

The original weighted Cauchy endpoint is `H_p=SUM_{m=1}^{2r}(6m+1)*a_m*2^(-m)*SUM_{s=1}^m u_s`. Then for all stated primes:

```
H_p = Hbin_p + p*Hharm_p + p^2*Hquad_p             (mod p^3),
Hbin_p  = SUM_m (6m+1)T_m V_m                        (mod p^3),
Hharm_p = SUM_m (6m+1)T_m(E_m-alpha_m V_m)         (mod p^2),
Hquad_p = (1/2) SUM_m (6m+1)T_m[
              (alpha_m^2-sigma_m)V_m - 2alpha_m E_m + F_m + G_m
          ]                                           (mod p).
```

**Proof.** V1 has first and second power sums `alpha_m-beta_s` and `sigma_m-tau_s`. Apply the elementary symmetric relation
`prod(1-pw)=1-p*sum(w)+p^2*((sum w)^2-sum(w^2))/2 (mod p^3)`, multiply by `(6m+1)T_mv_s`, sum over `1<=s<=m<=2r`, and collect the four displayed prefix moments. All divisions are p-adic units. No CM0 or unproved character identity is required. This strictly extends previous U4 from `p^2` to `p^3`, without recrediting U4. For this *declared linear observer and precision*, the four prefix sums and two m-level power sums suffice; universal observer minimality and arbitrary future s-dependent operations are not asserted. The computation is O(p) modular operations and O(1) running moments for fixed precision, apart from optional inverse precomputation.

## Exact checks and BRC witness

An independently constructed original hypergeometric recurrence and terminating-binomial recurrence were compared with the V2 moments **pointwise at every m** for all 611 primes `7<=p<=10000, p%6=1`. V1 was additionally checked at every individual `(m,s)` for p=7,13,19,31,37,43,373, totaling **8022 ordered pairs** at `p^3` precision. A rational `fractions.Fraction` source check independently verified selected exact pairs at p=7,13,19. All passed. The old C1 character pattern repeated its 611-prime finite check, but remains a conjecture and is not newly proved here.

At p=373 (`p^2=139129`, `p^3=51895117`):

```
Hbin mod p^3=16064358; Hharm mod p^2=22812;
Hquad mod p=317; Horiginal mod p^3=16782010.
(16064358+373*22812+139129*317)%51895117=16782010.
```

The previously finite-supported character prediction `C1=3*((2/p)-1)=-6` has second digit 232 and **new third digit 120**, since `(16782010+6-373*232)/139129=120`. Dropping the quadratic port changes the original p^3 observer by `139129*317 (mod 51895117)`. This is an exact observer-specific information-loss certificate for the signed `(1+6 theta)` Cauchy endpoint; the first-digit character result is still only finite-supported.

## Current unresolved work and control separation

The universal identity `Hbin_p=3*((2/p)-1) (mod p)` for all primes p=6r+1 is open. Next scientific unit: a terminating finite-field creative-telescoping or contiguous certificate using `6m+1=6(m-r) (mod p)`, or a genuine prime counterexample; then combine the proven source-preserving ports with the signed D25 parent goal `Delta_p-R_p=0 (mod p)` on p=13,19 (mod24). Existing CM0/R_p and the distinct onhour lane's CM quotient-deformation work are not recredited. Native p373 H0/B0 remains separately assigned.

At 2026-11-02 the native gateway 0.6.11 reported `UPSTREAM_CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, `executor_binding_configured=false`. Historical recovery Issue #6637 showed an old active service session `MCP-06f7ad61a8d841d9ba1ba1ef4d088d94`, no native claim/run or pending mutation, and two neutral preserved staging dispositions; continuation #6638 failed the named code-review gate. This author-side note is not a Source `completed_units` record, native checkpoint, Result, or independent review. P000, ACTIVE worldview, frozen scientific inputs, schedule and notifications unchanged.

Execution evidence: integer-only script `d25_cauchy_allorder_pair_lift_20261102.py` (local SHA256 `faa87f00a73ae15dd69b2c39bc8bb8b4beae50f6e020bbb4c45beae5e21f8ebe`), actual 611-prime log SHA256 `f4041df9bfd1f101542c4b07e0091042408ca0f54dd856afce7894bbf123e5c5`. The complete script and log are part of the associated local portable research package; until uploaded/read back on this repository these checks are cited as author-side executed evidence rather than Git-hosted checks.
