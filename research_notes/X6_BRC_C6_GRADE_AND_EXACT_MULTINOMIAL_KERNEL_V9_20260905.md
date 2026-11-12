# X6 × BRC：C6 端点 grade、三轴 holonomy 的 parity shadow 与精确 multinomial kernel

Status: `DERIVED_RELATIVE_BRC_EXACT / HISTORICAL_POSITIVE_FULL_RETURN_RETYPED / CURRENT_NATIVE_SIGNED_P000_V5`
Date: `2026-09-05`
Current type reconciliation: `2026-11-13` under frozen signed-X6 P000 V5 (`59538f585d037d09ef687b28715c4bc1a3f9fe03`).

**Current reading rule.** The C6 grade and multinomial kernel below are exact for the **derived relative endpoint** `G6_D=Z^6/Z1` and positive-only path words. The current native Cell endpoint lies in full signed `Z^6`, retaining common depth. A six-positive-axis word with one step per axis ends at the genuine native displacement `D=(1,1,1,1,1,1)`; its relative endpoint is zero, its native norm squared is 6, and it does *not* return to its starting native Cell. The old positive "full return" wording in §5 is superseded as native, but the coefficient 720 is correct as **relative-observer return multiplicity**. Exact native signed returns count paths using both ± axes and are computed by the separate `signed_brc.py` native endpoint kernel.
Depends on: `X6_NATIVE_COORDINATE_COMPLETION_V7_20260905.md`.

## 1. Canonical C6 grade

For the derived coordinate group

`G6_D=Z^6/Z(1,...,1)`,

define

`rho([z]) = sum_i z_i mod 6`.

This is well-defined: replacing z by `z+k*(1,...,1)` changes the sum by `6k`.

Every positive native-axis generator has grade `1 mod 6`; every reversed axis generator has grade `-1 mod 6`.

Therefore `rho` is exactly the endpoint residue of signed axis-event count in the commutative coordinate trace observer.

The all-six positive-axis word has grade 0 and is a **relative-observer** diagonal loop in `G6_D`; it is an open path of displacement `D` in the current native signed Cell torsor.

## 2. Three-axis triangle holonomy has grade 3

For any 3-of-6 slice S,

`H_S=sum_{i in S} e_i`

has

`rho(H_S)=3 mod 6`.

Its complementary slice has

`H_{S^c}=-H_S`

but also grade `3 mod 6` because `-3 == 3 mod 6`.

Thus every local 3-axis positive triangle that is closed in the slice observation carries the same half-period class in the global C6 grade.

The order-two character

`chi_2([z])=(-1)^(sum_i z_i)`

is the unique parity character obtained from `rho` by the quotient `Z/6 -> Z/2`.

Hence

`chi_2(H_S)=-1`

for every native 3-axis triangle holonomy.

For the current K4/FCC subatlas, this provides a natural finite signed readout compatible with the previously derived all-negative chart transition connection. This is a character/readout compatibility only; it is not a physical phase claim.

## 3. Positive-path endpoint support

Consider only positive axis events and let a concrete path of length m use axis i exactly `n_i>=0` times.

Its endpoint in the min-zero coordinate section is

`a=can6(n_1,...,n_6)`.

Hence every count vector producing a fixed endpoint a is of the form

`n=a+k*(1,...,1)`

for a unique integer `k>=0`.

Since `sum_i n_i=m`,

`k=(m-|a|_1)/6`.

Therefore a min-zero endpoint `a in A6_D` is reachable by a positive path of length m iff

1. `m>=|a|_1`;
2. `m-|a|_1` is divisible by 6.

Equivalently

`rho(a)=m mod 6`.

## 4. Exact N-BRC endpoint multiplicity

When the support condition holds, the axis occurrence counts are forced:

`n_i=a_i+k`.

The number of distinct labeled axis words is exactly the multinomial coefficient

`N_m(a)=m! / product_i (a_i+k)!`.

Otherwise `N_m(a)=0`.

No `6^m` enumeration is required.

This is an exact **relative-coordinate endpoint multiplicity observer** on positive-only words. A native Cell-endpoint multiplicity requires the raw six-component signed displacement (and the actual step alphabet); Path-formal BRC still distinguishes every word and may retain richer placement/provenance.

## 5. Positive-only relative-observer return count (not native Cell return)

The relative/min-zero observer zero endpoint `a=0` is reachable at positive length m iff

`m=6k`.

Then each of the six axes occurs exactly k times, so

`Return_relative,6k = (6k)!/(k!)^6`.

**Native endpoint distinction:** all these positive-only words end at nonzero native displacement `kD` for `k>0`, so native *positive-only* return count is zero for every positive length. In contrast, for the full signed native alphabet `{±e_i}`, `signed_brc.return_multiplicity(6)=19,920`; this is a different path family and a different endpoint predicate.

For `m` not divisible by 6, the positive path cannot return to the **relative zero observer** either.

Examples:

- m=6: `Return_relative,6 = 6! = 720` (native endpoint `D`, squared norm 6);
- m=12: `Return_relative,12 = 12!/(2!)^6 = 7,484,400` (native endpoint `2D`, squared norm 24).

By contrast, a selected 3-axis slice already sees a three-step local triangle as returned. The difference is precisely the hidden `H_S` translation in the omitted coordinates.

## 6. Exact positive rational weighted kernel

Assign each positive native axis an exact positive rational branch weight `w_i`.

For a fixed reachable endpoint a at length m, every word has the same multiplicative branch weight

`product_i w_i^(a_i+k)`

because its six occurrence counts are fixed.

Hence the total Weighted-BRC endpoint mass is

`W_m(a)= [m! / product_i (a_i+k)!] * product_i w_i^(a_i+k)`.

This remains exact positive rational arithmetic when all `w_i` are positive rationals.

Prime-valuation data can be retained before optional logarithmic readout, consistent with the global Weighted-BRC substrate.

## 7. Rotation covariance

For `sigma in S6`, let `sigma a` permute endpoint components and `sigma w` permute weights in the same way.

Then

`N_m(sigma a)=N_m(a)`

and

`W_m(sigma a; sigma w)=W_m(a;w)`.

The C6 grade is also S6 invariant because total component sum is permutation invariant.

## 8. Relation to old over-quotient C2 kernel

A superseded shared-axis-endpoint-identified model produced a fundamental `Z/2` companion and exact sheet balance. The type audit showed that model over-identified chart-local Cell transitions.

The derived six-coordinate quotient has no such fundamental torsion: `G6_D` is torsion-free of ordinary rank 5, while current native signed Cell coordinates form `Z^6`. What survives canonically is the **finite C6 grade quotient** of endpoint traces, whose order-two parity character sends every 3-axis hidden holonomy to `-1`.

Thus the old C2 pattern is better regarded as a coarse signed shadow/diagnostic, not full Cell identity.

## 9. BRC observer discipline

Recommended hierarchy:

`PATH-FORMAL / WEIGHTED BRANCH OCCURRENCES`

`-> SIX-AXIS OCCURRENCE HISTOGRAM / PRIME VALUATIONS`

`-> DERIVED RELATIVE COORDINATE ENDPOINT A6_D`

`-> SELECTED 3-AXIS SLICE ADDRESS`

`-> BOOLEAN SUPPORT`.

Do not move downward before proving the intended future observer factors through that quotient.
