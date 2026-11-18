# X6 Unit119 — sharp 3-divisibility theorem for R063 square-radius pair-chart versus full signed-X6 min-zero observer

**Date:** 2026-11-18. **Parent:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. **Status:** `AUTHOR-PROVED / EXACT-INTEGER-EXECUTED / UNREVIEWED / NOT_ADMITTED`. Native R063 C3/C4 benchmark not rerun.

## Immutable inputs and typing

Frozen P000 V5: `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Historical R063 source: `fd2bcff10ca6e147348b6c1236027fc0d2877df3:experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py`, blob `643b2bac659a445891dcb5588b647972977104e0`. Its `groots_square`/positive path multiplicity are lines 136–149. The current typed consumer `research_checks/X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py` blob `db46dde5a962b93b65775bf2b4d8f52d5e3f83b9` imports those functions at line 40, and constructs signed native pairs with explicit start/axes/signs at lines 45–65. This unit does not modify either source.

Work in the chosen-anchor *internal signed-displacement* chart `Z^6`, not in final public six-nonnegative-field addresses and not an asserted two-dimensional native plane. Define
- `G(z)=sum_i z_i²` (the P000 Enterprise component quadratic readout);
- `rho(z)=z-min_i(z_i)*(1,1,1,1,1,1)` (the derived min-zero **six-axis relative observer**, distinct from R063's `residue(point,m)` modulo-sector observable);
- `S_r={z in Z^6: G(z)=r², |supp(z)|<=2}`, the signed native endpoint union of R063's fixed ordered positive two-component root charts, including axis and polarity labels;
- `F_r={z in Z^6:G(z)=r²}`, the full signed native square-norm endpoint shell;
- `B_min(z)=(sum_i |z_i|)! / product_i |z_i|!`, the natural nonnegative shortest signed-step N-BRC path mass.

## Theorem A — exact, all positive integer radii

For every integer `r>=1`:

1. `rho` restricted to `S_r` is injective.
2. For each `x in S_r`, there exists a **distinct** `y in F_r` with `rho(x)=rho(y)` **if and only if `3 divides r`**.
3. When `3 divides r`, each `x in S_r` has exactly one such `y`, all such `y` have support at least four, and the full `rho` fiber inside `F_r` has precisely two endpoints. When `3 does not divide r`, each `x in S_r` has singleton full-shell fiber.
4. Let `h(r)=#{(a,b) in Z_nonnegative²:a²+b²=r²}` count ordered positive R063 roots. Then the number of distinct signed pair endpoints with a full-shell observer alias is exactly
   `A(r) = (60*h(r)-108) * 1_{3 divides r}`.
   The prefactor `60*h(r)-108` is also `|S_r|`.

**Proof of (1).** If `x,x' in S_r` have the same `rho`, then `x'-x=k*(1,...,1)` for some integer `k`. Their supports together cover at most four axes, so at least two coordinates are zero in both. Thus `k=0` and `x=x'`.

**Proof of (2) and (3).** Fix `x in S_r`. Equality of `rho` forces `y=x+k*1_6` with integer `k`. Equality of `G` gives
`0=G(y)-G(x)=2*k*sum_i(x_i)+6*k²=2*k*(sum_i(x_i)+3*k)`.
Thus for a distinct `y`, the only candidate is `k=-(sum_i x_i)/3`, necessarily a nonzero integer.

Write the at most two nonzero signed coordinates of `x` as `±a,±b` with `a²+b²=r²`. If `3` does not divide `r`, reduction modulo 3 shows exactly one of `a,b` is nonzero mod 3; hence `sum_i x_i` is not divisible by 3. This rules out nonzero integral `k`.

If `3` divides `r`, then `a²+b²=0 mod 3` forces both `a,b` divisible by 3. Therefore the proposed `k` is integral. It cannot vanish: `±a±b=0` with both `a,b` nonzero would imply `a=b` and `r²=2a²`, impossible for positive integers; if an axis component is zero, the signed sum is nonzero because `r>0`. The resulting `y` preserves the quadratic norm and relative observer, and at least four axes that were zero in `x` become `k!=0`. This establishes support at least four. The quadratic equation has at most two solutions for `k`, so the full fiber is exactly `{x,y}`.

**Proof of (4).** The two axial ordered roots `(r,0)`, `(0,r)` in every chart all deduplicate to precisely `2*6=12` signed native axial endpoints. Every nonaxial ordered root `(a,b)` is distinct under coordinate ordering and sign when `r>0` (an integer nonzero solution to `a=b` and `2a²=r²` does not exist); each yields `binom(6,2)*4=60` unique signed two-axis endpoints. Thus `|S_r|=12+60*(h(r)-2)=60*h(r)-108`. Combine with (2), (3). QED.

## Theorem B — infinite exact natural BRC counterexamples, first one at r=3

For every positive integer `m`, put `r=3m` and
`x=(-3m,0,0,0,0,0)`, `y=(-2m,m,m,m,m,m)`.
Then `x in S_r`, `y in F_r\S_r`, `G(x)=G(y)=9m²` and `rho(x)=rho(y)=(0,3m,3m,3m,3m,3m)`, but
`B_min(x)=1`, `B_min(y)=(7m)! / ((2m)!*(m!)^5)>1`.

At the first square radius `r=3`, the exact witness is `x=(-3,0,0,0,0,0)`, `y=(-2,1,1,1,1,1)` with `G=9`, common `rho=(0,3,3,3,3,3)`, and **N-BRC counts `1` and `2520`**. The earlier `G=25` (`r=5`) specific absence of aliases is a valid instance of Theorem A, rather than a general no-collision phenomenon.

## Exactly executed integer census

The self-contained independent source `research_checks/X6_UNIT119_R063_SQUARE_RADIUS_NATIVE_RHO_ALIAS_CHECK_20261118.py` was executed under CPython default, `-O`, `-OO`, with **byte-identical result JSON** in all modes. All mathematical checks use explicit always-on conditions rather than `assert`.

Finite domain: every integer radius `r=1,...,128`, all ordered nonnegative R063 Gaussian-square roots for each radius, all 15 pairs of 6 axes, all 4 sign choices per ordered root; deduplicate each radius's signed native pair endpoints and explicitly construct any candidate nonzero-depth full-shell alias.

- `398` total ordered positive roots across the 128 radii;
- `23,880` labelled chart cases;
- `7,080` labelled alias cases;
- `2,544` distinct signed-native pair endpoints having a full-shell alias, summed by radius;
- `42` radii divisible by 3;
- `r=3: 12/12` native pair endpoints with alias; `r=5: 0/132`; `r=50: 0/252`.

Exact executed checker Git blob `3acce8850f889e6e97aa076260156896459d8252`, local source SHA256 `9cb0730145a1411d441895c32109e783b4915f3bb63716c3536a5ff758d75d33`, committed at `6449e35f03518ec185d92bea983919508af3208f`. The integer certificate is `research_checks/X6_UNIT119_R063_SQUARE_RADIUS_NATIVE_RHO_ALIAS_RESULTS_20261118.json`, blob `ab09cdf883ba1816095e278c8694a632f7f501ef`, SHA256 `861fb6479df259b51361775aca2373a0b3d882056623e75279dce47949704abe`, committed at `ec949ac3ce00e18387dfa87fe6d2719885636521`. Git blob equality was independently checked after remote publication, making published checker bytes identical to the tested local script.

The exhaustive finite test corroborates the two universal theorems; the preceding proofs establish the all-`r` statements without extrapolating from 128 experiments.

## Consumer repair and mother-task implications

The currently inspected LP028 signed chart consumer genuinely preserves signed axes, polarity, starts and native BRC during its *native embed* at source lines 45–94. That makes its individual chart count a correctly typed native computation. A **subsequent consumer** that collapses such a signed native endpoint to `rho` for arbitrary full-shell reuse must retain common depth or an adequate future-operation probe. Theorem A gives the exact domain: for a fixed positive integer square radius not divisible by 3, `rho` is injective on `S_r` and has no full-shell alias touching `S_r`; for radius divisible by 3, even fixing `G=r²` leaves a two-element relative-observer fiber for every pair-chart endpoint, with a demonstrable natural BRC distinction in the axial family.

This is a **source-grounded downstream type-compatibility criterion**. The nine-file LP028 current `research_checks` source census in Unit117 did not find actual misuse of the original `residue/first_collision` modulo-sector functions; this Unit119 tests a separate `rho=can6` relative-observer transfer, not those old functions. Historical LP011 wrong-native-argmax and LP019 positive-path-cancellation original call sites remain `UNRESOLVED_PROVENANCE`, and 28-LP complete current consumer graph is still pending independent Driver `REQUEST_REVISION`.

Existing Unit118 versioned `X6_UNIT118_LP028_PINNED_ALWAYS_ON_NATIVE_REPLAY_20261118.py` has a saved implementation but no confirmed complete actual three-mode pinned native integration. Do not mark its integration PASS or execute a substitute for the fixed R063 C3/C4 512-case benchmark. Original R063 author-side 512/512 result is evidenced in [Issue #2416](https://github.com/awdawmip/enterprise-math/issues/2416); independent authorized review/admission remains outstanding.

**Next scientific action:** inspect the exact consuming call edges that transfer LP028 signed endpoint counts into relative/min-zero `rho` or future native step operations, preserving the six coordinates and provenance. If a verified unsafe caller is found, tie a typed correction to `source commit:path:line`; otherwise report bounded negative caller evidence. Continue independent Driver/R063 review handoff without declaring admission.

**Source and authority:** author contribution for same Research lane `chatgpt-research-onhour-enterprise-math-20260923`, task `RS-X6-LEGACY-PLANE-RECONCILIATION`; this GitHub author evidence is not automatically a Native semantic PROGRESS, independent review or formal Result.
