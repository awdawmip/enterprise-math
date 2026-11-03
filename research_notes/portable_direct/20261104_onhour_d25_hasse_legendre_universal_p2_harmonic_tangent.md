# D25: universal Hasse-to-Legendre p² harmonic correction (original CM d=3 family)

Date: 2026-11-04 (+08). **Status: AUTHOR-DERIVED / SCOPED EXACT ALGEBRA / FINITE INTEGER CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is author-side portable research, not a native Source checkpoint, authenticated CLAIM/run or a H0/B0 benchmark.

**Task**: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance `chatgpt-hourly-enterprise-math-20260921`).

## Exact object and new theorem

The frozen objective is `Delta_p = R_p (mod p)` for primes `p=13,19 (mod24)`, equivalent under the already-proved finite Clausen bridge to the original weighted 216 relation `W_(p−1) = p (mod p³)`. The accepted first digit and original four-source F4 reduction remain as published in `20261103_onhour_d25_complete_low_middle_h2_four_source_lift.md`. **The global second-digit signed cancellation is still open**.

Let `p=6r+1>=7` be any prime, `n=2r`. Use the ordinary external classical elliptic model `E_3(t): y²+xy+(t/27)y=x³`, with `f_t(x)=4x³+(x+t/27)²`. Its *literal* Hasse-polynomial lift and the literal classical Legendre lift are

```
A_p(t)=[x^(p−1)]f_t(x)^((p−1)/2)
      =sum_(m=0)^(2r) alpha_m t^m,
alpha_m=binom(3r,m) binom(6r−2m,m)(4/27)^m;
L_p(t)=P_(2r)(1−2t)=sum_(m=0)^(2r) lambda_m t^m,
lambda_m=(−1)^m binom(2r,m)binom(2r+m,m).
h_m=(1/3)_m(2/3)_m/(m!)²;
d_m=H_m/6−2*sum_(j=0)^(m−1)1/(3j+2), H_m=sum_(i=1)^m1/i.
```

All denominators are `p`-units for `0<=m<=2r`; all calculations are in `Z_(p)[t]` before reduction. The **new, all-prime, coefficientwise theorem** is

```
A_p(t) − L_p(t) = p * sum_(m=1)^(2r) h_m d_m t^m  (mod p²).
```

## Proof (original finite binomial coefficients, no native Frobenius assumptions)

Because `−2r=(1−p)/3` and `2r+1=(p+2)/3`, the Legendre coefficients satisfy the **exact rational product law**

```
lambda_m=h_m*product_(j=0)^(m−1)(1−p/(3j+1))(1+p/(3j+2)).
```

Using `3r=(p−1)/2` and `6r=p−1` directly in the Hasse binomial coefficient, two groups of negative factors cancel. The remaining p-free factor is `(3m)!/[27^m(m!)³]=h_m`, giving the second **exact** law

```
alpha_m=h_m*product_(j=0)^(m−1)(1−p/(2j+1))
           *product_(j=2m+1)^(3m)(1−p/j).
```

Both laws hold at `m=0` with empty products. The factors are units because `3m<=6r=p−1`. After first-order multiplication modulo `p²`, the quotient `(alpha_m−lambda_m)/(p h_m)` is the finite harmonic sum

```
e_m=−sum_(j=0)^(m−1)1/(2j+1)
    −sum_(j=2m+1)^(3m)1/j
    +sum_(j=0)^(m−1)1/(3j+1)
    −sum_(j=0)^(m−1)1/(3j+2)   (mod p).
```

An exact consecutive-index comparison gives `e_0=0` and

```
e_(m+1)−e_m=1/(2m+2)−1/(3m+3)−2/(3m+2)
            =1/[6(m+1)]−2/(3m+2).
```

This is exactly the increment of `d_m`, with the same zero initial value. Hence `e_m=d_m` and the displayed coefficient congruence follows for every `0<=m<=2r`. QED.

## Source-labelled 373 certificate and direct frozen-Gauss comparison

In the *declared* classical CM ring `R_2=(Z/139129Z)[t]/(t²−t+1/8)`, at `p=373`, `r=62`:

```
A_373(t)=112273+35808t=373(301+96t)             (mod 139129);
L_373(t)=17158=373*46                             (mod 139129);
(A_373−L_373)/373=255+96t                          (mod 373).
```

The independently generated harmonic RHS is **exactly** `255+96t`. The coefficient `96` of the quadratic branch is nonzero in `F_373`; replacing the full observer by a scalar mod-p Hasse/Legendre identification would erase second-digit information.

Reuse the prior exact Legendre-to-frozen-Gauss correction (not a new claim here): `G_62(1/2)/373=340`, `L_373/373=46`, `(L_373−G_62(1/2))/373=79` modulo 373. Thus the **new direct ordinary Hasse-to-frozen-Gauss observation** in the named quadratic ring is

```
(A_373(t)−G_62(1/2))/373 = 334+96t (mod 373).
```

The original H0/B0 divided-power `[X]U`, its rank, semilinear Frobenius direction/basis `eta`, signed Green/Hesse observer and `kappa` remain different **native experiment** objects. The above external Hasse polynomial is not a native computation.

## Executed finite certificate and BRC/continuation

An independent Python standard-library checker generated `alpha_m` from original binomial expressions, `lambda_m` from Legendre binomials, and `h_md_m` via

```
h_(m+1)/h_m=(3m+1)(3m+2)/[9(m+1)²];
d_(m+1)−d_m=1/[6(m+1)]−2/(3m+2).
```

It passed **46,052 coefficient tests on all 148 primes `7<=p<=2000, p=1 mod6`**. Separate literal polynomial evaluations in the quadratic ring passed at `p=7,13,19,37,43,373`. On all 77 target primes `p<=2000, p=13,19 mod24`, the harmonic correction's odd `t` coefficient was nonzero (finite observation; no universal nonvanishing theorem claimed). Full checker and JSON results are separately retained in this run's evidence bundle.

**BRC COMPOSE_APPLIED**: carrier retains original index, p-valuation, classical quadratic parameter/lift, source provenance and signed odd branch; observer is Hasse vs Legendre vs frozen Gauss, future operations include p-division and direct F4 low/middle/high source comparison. This is a classical external comparison, not a new native X6 coordinate identification. P000/ACTIVE Heartbeat World remains unchanged.

**Next exact mathematical action:** compose this second-digit lift repair with the *existing* F4-glued four-source `D+C−2chi(M1+epsilon M0)+chi H/9`; derive a finite signed Green/WZ adjoint with actual edge residues at `2r,3r,4r`, test `13,19,373`, then seek the all-target-prime cancellation proof. Do not reprove D24/finite Clausen/R bridge/first Hensel and middle/high duals.

**Native evidence pending:** GitHub support issue `#1559` OPEN/no named executor as read 2026-11-04; exact p373 original H0/B0 `[X]U mod139129`, module rank, real semilinear Frobenius, `eta`, signed observer, `kappa` and independent replay not run. Research client as of this run `research_authority_granted=false`, `write_relay_enabled=false`, active control quota `5/5`, `checkpoint_list=ACCESS_DENIED`; historical dispatch request `research-onhour-20261031-0205-dispatch-r15` gateway read returned `CONTROL_REQUEST_NOT_FOUND` (earlier GitHub receipt: `FAILED/UPSTREAM_CODE_REVIEW_REQUIRED`). No own native session/claim/run/Source checkpoint or formal Result was asserted. Historical request was not replayed; no maintenance-lane identity was used.
