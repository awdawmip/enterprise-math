# R059D Stage AJ — C phase-delay theorem and resolver-robust algebraic circle constant

Researcher-ID: `EM-R059D-AJ-6D4A19`

Task-ID: `RS-R059D-STAGE-AJ-C-PHASE-DELAY-RESOLVER-ROBUST-ALGEBRAIC-CONSTANT`

## Primary disposition

`N_C_ONE_LAYER_PHASE_THEOREM_PROVED__RESOLVER_ROBUST_KAPPA_SQUARED_EQ_12`

## Result

Stage AJ proves the strongest requested form for the exact AD finite-sampling family, not merely for one tuned subdivision.

For every integer `s>=1` and every integer radius `r>=0`, let `C_s` be the inherited microtriangle-majority resolver and let `J_C_s(r)` be the boundary-excess count of its edge-supported dual-cell boundary.  Then

`J_C_s(r)=J_N(r)-chi_s(r)`

with

`chi_s(r) in {0,1}`.

The delay bit is exact:

`chi_s(r)=1 iff 2*K_s(r,M_N(r))<s^2`,

where `K_s` is the direct integer microcentroid count on the independently derived balanced C shell event triangle and `M_N=r+J_N`.  Exact half ties use the inherited AD `>=` rule and therefore have `chi=0`.

Consequently

`C_C_s(r)=6*(r+J_C_s(r))=C_N(r)-6*chi_s(r)`

and the sharp all-radius circumference difference is

`0 <= C_N(r)-C_C_s(r) <= 6`.

## Why the one-layer theorem is all-radius

Two symbolic lemmas close the argument.

First, C cannot run ahead of N.  If the N limiting shell centroid `c_m` is outside the radius, any C microcentroid inside the radius lies in the inward tangent halfspace at `c_m`.  An exact composition count proves that this halfspace contains strictly fewer than half of the AD microcentroids for every subdivision `s`.  The infinite part is an analytic bound for `s>=21`; `s<=20` is a finite exact certificate whose dependence on the even-shell index stabilizes after `k=13`.

Second, C cannot lag by two shells.  If N accepts shell `m`, every point of the complete preceding limiting triangle `T_(m-1)` lies inside the N centroid radius.  Therefore all `s^2` microcentroids of `T_(m-1)` are C-selected, for every s.

Thus

`M_C_s in {M_N,M_N-1}`

uniformly in `s` and `r`.

## Resolver-robust Enterprise circle constant

Stage AI proved

`kappa_E^2=12`, `kappa_E>0`,

and

`-2/r < C_N(r)/(2r)-kappa_E < 1/r`.

AJ subtracts the exact phase term `3*chi_s/r` and obtains

`-5/r < C_C_s(r)/(2r)-kappa_E < 1/r`.

Hence

`sup_(s>=1) |C_C_s(r)/(2r)-kappa_E| < 5/r -> 0`.

Therefore every finite-sampling C resolver shares the same algebraic Enterprise circle constant, and the convergence is uniform over the entire family.

For every fixed integer endpoint correction `epsilon`, whenever `2r+epsilon` is eventually positive,

`C_C_s(r)/(2r+epsilon) -> kappa_E`

uniformly in s.  The same holds on every fixed integer refinement subsequence `hr`.

## Precision and tie audit

AJ does not need, and does not claim, a subdivision `s0` after which all pointwise phase decisions become identical.  Sampling can change the local phase bit but cannot change the limit.

Exact-half ties occur and are resolved by the inherited rule.  Certified examples:

- `s=2,r=5,m=6`: `2/4`;
- `s=8,r=24,m=28`: `32/64`;
- `s=12,r=11,m=13`: `72/144`.

The 19 AF `s=1024` one-radius delay pairs through `r=512` are reproduced exactly after the theorem freeze.

## Deterministic validation

The pre-history checker run gives:

- `122985 / 122985 PASS`;
- digest `b8e19e6cac0189433293feda2bdb4be96ee5c89ccac491420e0ea817bea97ec2`;
- complete phase replay for `r=1..4096` at `s={1,2,3,4,5,8,12,16,32,64}`;
- checkpoints `8192,16384` at multiple s;
- all 19 historical `s=1024` delay/catch-up pairs;
- exact tie checks.

Finite replay is implementation evidence only.  The theorem is the all-radius tangent/whole-triangle proof.

## Semantic boundary

AJ proves resolver robustness of the Enterprise-native count-geometry constant.  It does not identify `kappa_E` with standard real `pi`, does not prove a theorem about Euclidean pi, and does not select N or C as the unique canonical resolver.

`STOP_FOR_DRIVER_REVIEW`
