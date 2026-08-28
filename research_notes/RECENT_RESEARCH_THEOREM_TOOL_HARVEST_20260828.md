# Recent Research Theorem / Tool Harvest — 2026-08-28

Status: `DRIVER_HARVEST / NO_NEW_MATHEMATICS / DEDUPLICATED_AGAINST_CURRENT_TOOLBOX`

Driver-ID: `EM-RSA-45F14F / CONTROL_PLANE`

Scope: recent 2026-08-27..2026-08-28 research with current-main accepted or already-harvested authority. Draft, awaiting-review, rejected, or superseded mathematical packages are not promoted here.

## 1. Executive harvest

The recent research yields **four mature theorem packages** and **two admitted reusable domain operators**.

No new top-level toolbox family is justified.

### Mature theorem packages

1. `PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_THEOREM_PACKAGE`
   - local factorial valuation wall;
   - activation-wall synchronization-ratio lemma;
   - dyadic first-hit dichotomy;
   - square-root two-seed fallback;
   - exact N-only promised-semiprime extractor;
   - explicit no-speedup boundary.

2. `P018_QUOTIENT_ROOT_ATLAS_TERNARY_CARRY_THEOREM`
   - exact high/low quotient-root atlas decomposition;
   - binary exact cardinality;
   - ternary threshold normal form;
   - Lean-checked theorem source.

3. `RSA_EXPONENT_COLLISION_CRT_COLLAPSE_THEOREM`
   - fixed-unit exponent kernel `ord_n(x) Z`;
   - exact 2-adic split iff local order depths differ;
   - exact random-unit failure probability;
   - global exponent-map kernel `lambda(n) Z` with classical order-to-factor boundary;
   - lcm subgroup aggregation and diagonal-graph obstruction.

4. `ENTERPRISE_BRC_INERT_MINUS_SECOND_ORDER_CLAUSEN_SWISHER_REDUCTION`
   - finite `S_p=W_p` identity;
   - two-scalar second-order conditions compressed to one `W_p` congruence;
   - exact modulo-`p^3` valuation truncation;
   - reduction to one finite Clausen–Swisher certificate `C_p`;
   - full inert-minus target remains open.

## 2. Admitted reusable tools

### A. `t1.nonly_valuation_wall_gcd_extractor`

Classification: `DOMAIN_OPERATOR` under `T1_SCALE_ENUMERATION_VALUATION`.

Reusable pattern:

`PUBLIC ACTIVATION WALL -> FIRST NONUNIT PROBE -> TOTAL-GCD SYNCHRONIZATION CERTIFICATE -> HIDDEN-RATIO BOUND -> PUBLIC SECOND-SCALE SPLIT`.

This is the most reusable mechanism in the recent factoring-adjacent work because the generic synchronization lemma survives replacement of the special factorial observable once a new exact activation law is separately proved.

Boundary: promised distinct odd semiprimes; current implementation is `Theta(p)` scale in the worst case and is not a factoring-speedup theorem.

### B. `domain.precision.quotient_root_atlas_carry`

Classification: `DOMAIN_OPERATOR` routed primarily through `T1_SCALE_ENUMERATION_VALUATION`, supported by `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA` and `T5_PRECISION_REFINEMENT`.

Reusable pattern:

`FULL DENOMINATOR SCAN -> HIGH INJECTIVE CHART + FORCED LOW INTERVAL + OPTIONAL HORIZON -> BINARY CARRY -> TERNARY COUNT CARRY`.

Boundary: finite positive-denominator quotient-root atlases only; no arbitrary floor-map, prime, factoring, or continuum generalization.

## 3. Results deliberately not promoted to tools

### RSA exponent-collision collapse

Classification: `RESULT_ONLY`.

Reason: the core global annihilating-exponent mechanism is classical order-to-factor mathematics, while the accepted local iff/probability/subgroup barrier is a clean theorem package but has not demonstrated cross-domain executable reuse sufficient for a new operator. Do not duplicate T6/T7/T8 machinery merely to rename the squaring chain.

### BRC inert-minus Clausen–Swisher reduction

Classification: `RESULT_ONLY`.

Reason: it is a sharp arithmetic compression inside an existing BRC / finite-hypergeometric interface. The reusable structural work is already covered by BRC and existing arithmetic machinery; the remaining `C_p` problem is theorem work, not tool construction.

## 4. Current toolbox deduplication map

The recent mechanisms route as follows:

- valuation walls / threshold activation / local divisibility -> `T1_SCALE_ENUMERATION_VALUATION`;
- quotient-root collision horizon / carry compression -> `T1 + T4 + T5`;
- finite symmetry, orbit, stabilizer and double-coset candidates -> `T7_FINITE_SYMMETRY_EQUIVARIANCE`;
- multivalued compressed composition candidates -> `T8_RELATION_OBSERVABLE_SPECTRUM` and `T0_BRC`;
- groupoid / transport coherence candidates -> `T9_HOLONOMY_COCOYCLE_GLUING` when route dependence is present;
- RSA collision theorem -> theorem layer only at current evidence strength;
- finite Clausen–Swisher bridge -> theorem layer only at current evidence strength.

Therefore the current harvest verdict is:

`NEW_GLOBAL_TOOL_FAMILY = NONE`.

## 5. Pending recent candidates — do not promote yet

The following recent research contains potentially reusable structure but lacks final Driver acceptance at the harvest cutoff or was explicitly returned for revision.

### A3 shell tomography / radial defect

Candidate structure:

- double-coset radial defects;
- set-valued double-coset support multiplication;
- pair-groupoid deterministic lift;
- weighted orbital structure constants.

Current posture: **candidate only**. The first H4 package was rejected/revised; the corrected fixed-stabilizer package must receive terminal review before theorem/tool admission. Likely dedup route is `T7 + T8`, with groupoid transport under existing relation/holonomy machinery rather than a new global family.

### SHOR FAST_ROUGH_INTERVAL_GCD

Candidate theorem structure:

- legal `B^2`-rough `d<=B^6` has at most two prime factors;
- squarefree prefix-gcd encodes exact factor-prefix information;
- FAST interval-GCD is exponent-equivalent to factoring the legal rough-semiprime class;
- remaining coarse-locator primitive.

Current posture: unresolved exact frontier / awaiting review. Do not toolize until the accepted boundary is fixed.

### PCF6 Prime-Fusion N-blind realization

Candidate theorem structure:

- channel selector `c=-tr(T)` becomes a nontrivial CRT idempotent;
- exact corrected mixed carrier realization is equivalent at that layer to factor splitting;
- fixed H-independent determinant probes reduce to resultants.

Current posture: awaiting review. This looks theorem-facing and likely `RESULT_ONLY` unless a reusable selector/certificate interface survives audit.

### NollM Eisenstein rotation atlas

Candidate structure:

- exact Eisenstein rotation/commensurability atlas;
- affine-side normalization;
- bounded path-jet residue.

Current posture: awaiting review. Existing `T3/T5/T7/T9` coverage is already strong; default assumption should be composition, not a new family.

### Native trisector P0/P1/N2 bridges

Candidate structure:

- shell cardinality and cumulative growth;
- parity defect scalar;
- torsor-valued center/orientation obstruction;
- N2 scalar/set/relation admission.

Current posture: awaiting review / Foundation gate. Keep theorem semantics separate from pointwise canonical-label claims.

## 6. Harvested source nodes

Already present before this transaction:

- `research_notes/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_THEOREM_PACKAGE_20260828.md`;
- `research_method_inventory_addenda/20260828_nonly_valuation_wall_gcd_extractor.json`;
- `research_notes/P018_QUOTIENT_ROOT_ATLAS_TERNARY_CARRY_DRIVER_ACCEPTED_THEOREM_NODE_20260828.md`;
- `research_notes/P018_QUOTIENT_ROOT_ATLAS_TERNARY_CARRY_THEOREM_TOOL_HARVEST_20260828.md`;
- `research_method_inventory_addenda/20260828_p018_quotient_root_atlas_carry_harvest.json`.

Added by this transaction:

- `research_notes/RSA_EXPONENT_COLLISION_CRT_COLLAPSE_DRIVER_ACCEPTED_THEOREM_NODE_20260828.md`;
- `research_notes/ENTERPRISE_BRC_INERT_MINUS_SECOND_ORDER_CLAUSEN_SWISHER_DRIVER_ACCEPTED_REDUCTION_NODE_20260828.md`;
- this current recent-harvest index.

## 7. Final extraction posture

Formal tool admissions from the recent window:

- `t1.nonly_valuation_wall_gcd_extractor`;
- `domain.precision.quotient_root_atlas_carry`.

Formal theorem/reduction nodes from the recent window:

- N-only valuation-wall synchronization / GCD extraction package;
- P018 quotient-root atlas / ternary carry theorem;
- RSA exponent-collision / 2-adic CRT collapse theorem;
- BRC inert-minus finite Clausen–Swisher exact reduction.

Pending candidate pool remains non-authoritative until its own review gates close.

`NEW_THEOREM != NEW_TOOL` remains the controlling rule.