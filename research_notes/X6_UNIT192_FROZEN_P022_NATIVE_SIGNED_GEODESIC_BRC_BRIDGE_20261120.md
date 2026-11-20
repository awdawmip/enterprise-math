# X6 Unit192 — frozen P022 SC6 bridge: exact geodesic-layer BRC mass conservation

Date 2026-11-20. Parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Research lane `chatgpt-research-onhour-enterprise-math-20260923`; excluded maintenance lane `chatgpt-hourly-enterprise-math-20260921`.

**Status: AUTHOR_PROVED / EXACT_INTEGER_EXECUTED / GITHUB_SOURCE_EVIDENCE / UNREVIEWED / NOT_ADMITTED. Native semantic PROGRESS is separately pending.** Frozen science: `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Historical comparison/source: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

## Why this increment is different from Unit173

Unit173 already examined the true frozen `p022_geodesic_multiplicity` producer -> test consumer, distinguished A3 from signed-axis simple cubic, and independently checked 35 dimension/radius cases including SC6 through radius 4. **Those results are reused, not reproved as novel.** Unit192 contributes the additional **geodesic-interval BRC path-mass accounting interface**, source-specific missing six-coordinate interval testing, an unbounded interval-site versus BRC-weight discrimination, and a separate radius-6 shell exact test.

Actual historical Python source:
- `src/enterprise_math/p022_geodesic_multiplicity.py` frozen Git blob `46373050168d2430b6cb3952aa763f3081284632`: `sc_graph_radius` line 56, `sc_geodesic_path_count` line 87, `sc_geodesic_interval_profile` line 148, `sc_shell_total_geodesic_paths` line 206.
- True importing test `tests/test_p022_geodesic_multiplicity.py` frozen blob `ef3da1a789186867c538b604da1b642bf6039591`: SC endpoint recursive check line 116, interval profile check line 123, shell sum test line 130. Its loops cover dimensions 1, 2, 3 (intervals specifically dimension 3), not a complete six-axis interval regression.

P000 signed X6 primitive steps are `±e_i`, `i=1,...,6`, frozen in `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`; P000 `PERP_E` is its 120° native relation, not Euclidean 90°. The P022 simple-cubic graph serves here **only as a graph-isomorphic exact signed-axis step combinatorics implementation**; A3 root transfer moves `e_i-e_j` are different. Neither historical production module nor historical tests are claimed to import an X6 runtime adapter.

## Theorem: interval site counts versus ordered BRC mass

Let `z ∈ Z^6`, `n=Σ_i |z_i|`, and `B(z)=n!/Π_i |z_i|!` for P000 native shortest signed primitive paths. Let `Y_j(z)` be all integer intermediate endpoints satisfying `||y||_1=j` and `||z-y||_1=n-j`. Every coordinate lies between 0 and `z_i` with matching sign. The frozen P022 interval profile exactly gives

```text
I_j(z)=|Y_j(z)|=[t^j] Π_i (1+t+...+t^|z_i|).
```

For every `0 ≤ j ≤ n`, the **ordered-path split identity** is

```text
B(z) = Σ_{y∈Y_j(z)} B(y) · B(z−y).
```

Proof: split each shortest signed primitive word uniquely after event j. Its prefix and suffix are shortest paths to `y` and from `y` to `z`; conversely, concatenating any of the `B(y)B(z-y)` pairs gives a unique shortest path. The disjoint midpoint fibers partition all words. This is a complete proof for every signed integer displacement and every layer, and an exact preservation rule for using P022 interval readouts in native BRC research. The unweighted interval profile does *not* encode BRC multiplicities.

At `z=(2,1,1,0,0,0)`, `n=4`, production profile `I=(1,3,4,3,1)`; `B(z)=12`. At layer `j=2`, the four intermediate states have BRC split weights `2,4,4,2`, summing to 12. Recording 4 sites in place of 12 ordered paths would delete 8 path witnesses.

**Unbounded loss family**: `z_m=(m,m,0,0,0,0)`, layer `j=m`. Then `I_m(z_m)=m+1` whereas `Σ_{y∈Y_m}B(y)B(z_m−y)=C(2m,m)`; elementary binomial maximality yields `C(2m,m) ≥ 4^m/(2m+1)`. Consequently `B(z_m)/I_m(z_m) ≥ 4^m/((2m+1)(m+1)) → ∞`. Hence treating layer *site* count as ordered BRC path weight has no global finite distortion factor.

## Six-axis shell bridge and actual exact checks

For shortest-path shell radius n, independently of history count at arbitrary n ticks, the frozen SC shell formula specializes to

```text
T_6(n)=Σ_{k=1}^{min(6,n)} C(6,k) 2^k k! S(n,k),  n>0;   T_6(0)=1.
```

This counts all *geodesic* event words ending on the norm-one shell, not all `12^n` signed primitive words of unrestricted walks (e.g. n=2: 132 vs 144).

Source-equivalent computations were compared by three independent exact integer paths: signed endpoint multinomial, end-directed primitive recurrence, and Stirling shell polynomial. Interval counts were independently checked by monotone-midpoint enumeration against the P022 geometric coefficient product, while every layer's path mass was verified. These checks were **actually executed** in a V8 isolate using BigInt, not run via or imported from the historical Python package.

- 8,989 distinct six-axis signed shell endpoints for radii 0..6 checked by recurrence;
- 20,158 midpoint layer comparisons (20,153 covering *all* endpoints radius <=5, plus five repeated checks of the explicit example);
- 61,737 exact midpoint instances visited including explicit example;
- radius-6 shell: 5,336 endpoints and 856,212 shortest-path witnesses;
- shell mass radius 0..6: 1, 12, 132, 1,332, 12,372, 106,452, 856,212;
- ten exact binomial lower-bound family instances (m=1..10);
- zero discrepancies.

Reproducible source: `research_checks/X6_UNIT192_P022_SIGNED_BRC_BRIDGE_CHECK_20261120.js` and result certificate `research_checks/X6_UNIT192_P022_SIGNED_BRC_BRIDGE_RESULTS_20261120.json`. Original P022 production/test suite and original R063 six-file 17/17 + 512/512 benchmark were **not** rerun.

## Parent audit and remaining action

The verified genuine P022 producer/consumer source is typed as `KEEP/CORRECT_DERIVED_SC_GRAPH_BRC_INTERFACE`. Nothing in this audit locates LP011's alleged native signed argmax or LP019's alleged positive N-BRC subtraction; exact historic offending `commit:path:line` remains unresolved. Genuine frozen `src/enterprise_math/motion_history.py` is an **order-preserving 2D-body E001** consumer, importing `BodyMotion2D` and retaining `MotionHistory`; it is not a verified X6-native/A3 consumer. Parent should next identify an *actual* native X6 ordered-event consumer and typed interface (or bound the absent bridge) and continue exact LP011/LP019 source search, while preserving native Unit175–192 semantic linkage debt and older Units149–152. Source and independently executed checker evidence do not amount to Driver admission.
