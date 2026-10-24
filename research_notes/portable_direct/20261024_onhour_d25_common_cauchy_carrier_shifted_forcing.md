# D25/LIFT — Source-fixed LOW/HIGH as residues and samples of one rational Cauchy carrier

2026-10-24 | TASK_RESEARCH | EXACT ALL-m ALGEBRA / EXECUTED FRACTION SELF-CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.

Mother: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Author ordinary-control lane `chatgpt-research-onhour-enterprise-math-20260923`, different from maintenance `chatgpt-hourly-enterprise-math-20260921` and separate research author `chatgpt-research-hourly-enterprise-math-20260923`.

**Inherited and not re-credited:** original LOW first jet and two HIGH sectors (`20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md`), genuine 1/3 HIGH jump (`20261024_onhour_d25_high_single_stream_one_third_jump_terminal.md`), fixed-rank LOW boundary (`20261024_onhour_d25_p211_fixed_endpoint_sharp_valuation_low_boundary.md`), terminal Green certificate (`20261024_onhour_d25_high_impulse_green_two_boundary_certificate.md`), and the other author's distinct finite-cutoff Laurent part (`20261024_hourly_d25_joint_cutoff_two_digit_finite_part.md`). Unlike those prior units, this proof identifies the common *rational Cauchy carrier* and exactly translates the actual LOW/HIGH forcing; no artificial m→m+1 cutoff is introduced.

## 1. One common carrier; different observers

For integer m>=1 and complex/rational z outside the indicated poles, set

```text
Q_m(z) = m! / [z(z+1)...(z+m)]
D_m    = 2^m m binom(2m,m) = 2^m (2m)!/[m!(m-1)!].
```

The genuine source-fixed original coefficients are

```text
b_(m,n) = (-1)^n binom(m,n) / 2^n,                   0<=n<=m,
a_(m,t) = 2^(m-t) (2m)! (t-1)! / [(m+t)!(m-1)!],   t>=1.
```

**Theorem A (all integer m>=1, exact rational).**

```text
b_(m,n) = 2^(-n) Res_{z=-n} Q_m(z),
a_(m,t) = D_m 2^(-t) Q_m(t),

Q_m(z)  = sum_{n=0}^m (-1)^n binom(m,n)/(z+n).
```

**Proof.** At z=-n the denominator product has derivative (-1)^n n!(m-n)!, so the residue is (-1)^n binom(m,n). At positive integer t the denominator product is (m+t)!/(t-1)!; substituting D_m gives precisely the original a_(m,t). The partial-fraction expression has those same poles and residues, and its difference from Q_m tends to zero at infinity, hence is identically zero.

The **same** rational shift equation

```text
(z+m+1) Q_m(z+1) = z Q_m(z)
```

gives the two exact established recurrences under their correct observers:

```text
b_(m,n)/b_(m,n-1) = -(m-n+1)/(2n),
a_(m,t+1)/a_(m,t) = t/[2(m+t+1)].
```

At negative integers take residues; at positive integers take evaluations. Neither operation can be silently substituted for the other, and the factors 2^(-index) are part of the source-fixed input.

## 2. The actual LOW/HIGH rational forcing differs by exactly 1/6

Keep the inherited source-fixed rational forcings

```text
k(z)     = (1-3z)(6z+3)/[(3z+1)(3z+2)]
kappa(t) = -2 + 4/(6t+1) + 2/(2t+1).
```

**Theorem B (exact identity, all rational admissible arguments).**

```text
k(z)      = -2 + (2/3)/(z+1/3) + 1/(z+2/3),
kappa(t)  = -2 + (2/3)/(t+1/6) + 1/(t+1/2)
          = k(t-1/6).
```

Proof is a direct common-denominator calculation, with both nonconstant coefficients retained. Thus LOW Cauchy poles {1/3,2/3} and HIGH poles {1/6,1/2} differ by the *same* -1/6 translation, not a fitted prime-specific map.

In particular, retaining the original HIGH double sector (with genuine t=m seam excluded and t=3m terminal excluded) gives the exact source coefficient representation

```text
Z_m^one = D_m [
    sum_{t=1}^{m-1} 2^(-t) Q_m(t) k(t-1/6)
  + (1/3) sum_{t=m+1}^{3m-1} 2^(-t) Q_m(t) k(t-1/6)
].

A_m = sum_{n=0}^m 2^(-n) Res_{z=-n} Q_m(z) k(n).
```

These equations reconstruct the genuine HIGH regular forcing and LOW first-digit coefficient. The 1/3 jump comes from n=2m in the *original* hypergeometric recurrence; it is not removed by a common analytic carrier. The t=3m / n=4m terminal likewise remains in the existing separately derived boundary correction.

The inherited **full fixed-rank finite obstruction**, for primes p=6m+1, is

```text
F_m == [A_m + (1-2m) B_m]/p + J_m^lo
       + B_m [ Z_m^one + 28/9 + H_m/3 + (2/9) H_(2m) ] (mod p),

B_m = (2m-1)!(2m)!/(4m)!.
```

Substituting the preceding *exact* Q_m expressions into this equality is a **single-source-kernel representation of the unchanged original finite obstruction**. It retains the existing complete first jet, both seam/terminal contributions through the inherited finite residual, and the original p-divided LOW normalization. This is a proven change of representation, **not** a proof of F_m=0 for all primes and not native benchmark evidence.

## 3. Harmonic jets and a rank-mixture identity

Put H_r^(s) = sum_(j=1)^r 1/j^s and rho_n=(-1)^n binom(m,n). At z=-n+epsilon,

```text
Q_m(z) = (rho_n/epsilon) [
  1 + epsilon L_(m,n)
  + (epsilon^2/2)( L_(m,n)^2 + H_n^(2) + H_(m-n)^(2) )
  + O(epsilon^3) ],

L_(m,n) = H_n - H_(m-n).
```

**Proof:** factor (z+n)=epsilon, expand each remaining rational factor (j-n+epsilon)^(-1); its first logarithmic coefficient is -sum_(j!=n)1/(j-n) = H_n-H_(m-n), its second is (H_n^(2)+H_(m-n)^(2))/2. All displayed coefficients are rational, with *no* artificially introduced complex log(2) or p-adic logarithm. These ordinary jets do not purport to replace the source's complete fractional-parameter LOW jet J_m^lo.

For q rational and z>0 define the exact finite Cauchy/Beta polynomial

```text
C_m(z;q) = sum_{n=0}^m (-q)^n binom(m,n)/(z+n)
         = integral_0^1 u^(z-1) (1-q*u)^m du.
```

The integral is finite polynomial integration, not a numerical approximation. Then C_m(z;1)=Q_m(z). The polynomial identity (1-u/2)^m = 2^(-m)(1+(1-u))^m proves

```text
C_m(z;1/2) = 2^(-m) sum_{j=0}^m binom(m,j) Q_j(z),
Q_j(z) = j!/(z)_(j+1).
```

Consequently the inherited LOW Cauchy ports I_a(m)=sum b_(m,n)/(3n+a), a=1,2, have the **new exact complete-Beta rank-mixture interface**

```text
I_a(m) = [1/(3*2^m)] sum_{j=0}^m binom(m,j) j!/(a/3)_(j+1).
```

This scalar identity is all-m exact, but replacing signed LOW summands by a positive rank mixture is *only* valid for this declared scalar Cauchy readout: it cannot erase the original LOW first-jet operations or the two HIGH provenance branches. This is the BRC observer boundary.

## 4. Exact verification, attribution, unfinished work

An independently written Python standard-library Fraction checker evaluated source-fixed factorial b/a coefficients, the rational partial-fraction identity, residue/finite-part and epsilon^1 harmonic coefficients via direct product expansions, translated forcing, genuine two-sector HIGH sums and both q=1/2 LOW Cauchy ports, for m=1,2,...,10 and m=35 (p=211). **All checks passed**. Selected exact modular witnesses (p; A_m, Z_m^one, I_1, I_2) are 13:(6,2,11,10), 19:(13,6,11,5), 37:(34,3,0,31), 211:(162,124,80,81). The algebraic proofs, not finite tests, establish the all-m statements. The user-visible local exact checker was `d25_common_cauchy_carrier_check.py`; no original native/X6 benchmark was executed.

**BRC COMPOSE_APPLIED.** Carrier: exact Q_m rational state with *labeled* negative residues, positive samples, signed LOW coefficient branches, original HIGH weights and genuine seam/terminal. Observers: residues vs point evaluations vs ordinary pole jets vs scalar Cauchy mixture vs the original mod-p obstruction. No positive-mass BRC rule was imposed on signed cancellations; no native spatial transfer is inferred.

**Still open and not newly admitted:** prove the original F_m=0 for all target primes or exhibit an original-target falsifier, perform same-class CM/divided-power representative, semilinear map direction and ordinary omega+6 nabla_lambda omega normalization comparison, execute the unchanged native benchmark. This work is **UNREVIEWED / NOT_ADMITTED**, not a native Source checkpoint, Researcher CLAIM/open/run, independent review, Result or frozen proof.

**Next exact mathematical action:** use the source-matched rational Q_m shift relation and the *real* 1/6 forcing translation to seek a terminating residue/sample WZ identity connecting the LOW first-jet functional (not merely A_m) to both weighted positive HIGH sectors. Boundary constraints: explicit n=2m / t=m 1/3 splice and original n=4m / t=3m terminal, all at fixed m and p. Test any proposed operator against the unchanged complete F_m before discussing universal lifting. The q=1/2 rank mixture supplies an exact contiguous candidate but is not itself such a certificate.

At this run's read-only backend: Gateway 0.6.11, Sites research_authority_granted=false and executor_binding_configured=false. Existing exact ordinary-control #6186 reports local ACTIVE projection but source_authority_verified=false, no claim/run, neutral staging only; #6187 was PREREQUISITE_NOT_SUCCEEDED and #6188 FAILED TimeoutExpired. The existing recovery path is EM issue #1539, distinct from the #1501 generic resolver cleanup. No old request was retried, no Researcher identity was borrowed or faked, no formal checkpoint/result or scheduler/notification mutation was performed. This GitHub author research note is neutral evidence persistence, not Source role admission.
