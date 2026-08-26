# Native Tri-sector P0/P1 → Arithmetic Bridge — Phase-A Return

Status: `PHASE_A_FROZEN / WEAKER_FOUNDATION_BRIDGE / PHASE_B_NOT_OPENED / FOUNDATION_UNCHANGED`

Date: `2026-08-26`

Researcher-ID: `EM-NTP1B-7C4A2F`

Task: `RS-NATIVE-TRISECTOR-P0P1-ARITHMETIC-BRIDGE`

Publication: `TP2-BD39D919E5642BECBE87`

Owner branch: `research/native-trisector-p0p1-arithmetic-bridge`

Owner base: `c5e6f8f97a545974638b0024a3fabb56c6dc64d8`

Frozen Phase-A authority snapshot for task dependencies: `f781c458b1dc4f3ec1c5cab9cdfc244ce11220f7`

## 1. Phase-A primary verdict

Freeze:

`PHASE_A_PRIMARY_VERDICT = WEAKER_FOUNDATION_BRIDGE`.

`PHASE_A_NATIVE_TRACE_GRADE_BRIDGE = DERIVED`.

`DISTINGUISHED_SINGLE_GLOBAL_CENTRAL_LANE = EXACT_DEFINABILITY_OBSTRUCTION`.

`ORDERED_MEMBER_OF_ODD_BALANCE_PAIR = EXACT_DEFINABILITY_OBSTRUCTION`.

`THEOREM_SIDE_COMPARISON = NOT_OPENED`.

`FOUNDATION_MUTATION = NONE`.

The current P0/P1 substrate does define a nontrivial, choice-free arithmetic bridge. It does **not** define a unique named global central lane or an orientation of the odd-shell central pair. The strongest Phase-A object is therefore an invariant/equivariant shell-and-balance structure, not a theorem-side singleton selector.

The surviving native bridge is generated entirely from:

1. nonnegative integer component counts;
2. P1 native component traces and their additive composition;
3. P0/P1 transition/event count;
4. the exact shuffle realization fiber of a trace;
5. the three-sector gluing already present in the native plane.

No theorem-side shell allocator, central-lane definition, breaker definition, breaker-capacity formula, hyperbola, Joukowski map, extremal-saturation formula or controlled-comparator formula is used.

## 2. Exact typed Phase-A input inventory

### P0 input actually used

- `N_0` and ordinary integer addition/equality/order/counting;
- finite cardinality;
- discrete transition/event count;
- finite quotient/equivalence reasoning already authorized by the component-trace definition.

### P1 input actually used

For every native sector `S_ij`:

- native line identity

  `T^(ij)_{a,b} = [X_i^a X_j^b]`,

  with `X_i X_j ~ X_j X_i`;

- trace composition

  `T^(ij)_{a,b} * T^(ij)_{c,d} = T^(ij)_{a+c,b+d}`;

- exact realization fiber

  `Realize_E(T^(ij)_{a,b})` = all single-cell shuffle trajectories having `a` occurrences of `X_i` and `b` occurrences of `X_j`;

- exact fiber cardinality

  `|Realize_E(T^(ij)_{a,b})| = binom(a+b,a)`;

- cyclic transport across the three sectors;
- shared physical axes are deduplicated when the sector charts are glued.

### Native plane input actually used

- exactly three positive native axes/rays;
- the induced three-sector atlas and its cyclic covariance;
- no distinguished positive axis or sector is added by this task.

### Explicitly **not** used as Phase-A premise

- `L_E`, radius/equidistance shells or any P2 rebuilt metric/length selector;
- Euclidean carrier length/angle/vector identities;
- arbitrary-point directed gauge formulas;
- theorem-side shell/lane/breaker/capacity definitions;
- theorem-side hyperbola/Joukowski/conic/finite-field formulas;
- the specialization `s=B=3`.

This last exclusion is load-bearing. The bridge below is a transition-trace bridge, not a metric-shell bridge.

## 3. Native transition grading

For each sector define the P0/P1 trace grade

`g(T^(ij)_{a,b}) := a+b`.

This is the number of component-transition letters in every representative of the trace. It is **not** asserted to be geometric/native line length.

By trace composition,

`g(T*T') = g(T)+g(T')`.

Hence `g` is an additive homomorphism from the P1 trace monoid to `(N_0,+)`.

For `n in N_0`, define the local transition shell

`Sigma_n^(ij) := { T^(ij)_{a,n-a} : 0 <= a <= n }`.

Then exactly

`|Sigma_n^(ij)| = n+1`.

This is a P0/P1 shell in the sense of **equal transition grade**. It is not an equidistance/radius shell and therefore does not import a P2 metric.

## 4. Exact global shell count from native three-sector gluing

For `n >= 1`, glue the three sector-local shells and deduplicate the physical positive-axis traces already identified by the native line definition.

Before gluing there are

`3(n+1)`

sector-local trace incidences.

Each of the three physical positive axes contributes one grade-`n` axis trace, and each such trace occurs in the two adjacent sector charts. Thus the sector-local count contains exactly three duplicate copies beyond the three physical axis traces.

Therefore the global grade-`n` trace shell has

`|Sigma_n^E| = 3(n+1)-3 = 3n`, for every `n >= 1`.

Freeze:

`GLOBAL_P0P1_TRANSITION_SHELL_CARDINALITY(n) = 3n FOR n>=1`.

The coefficient `3` here is **not** a derivation of native three-ness. It is the arithmetic consequence of the already-given three-sector input plus exact axis gluing.

No claim is made here for a special `n=0` global count, because the sector-local type-changing start incidences are distinct typed objects and are unnecessary for this bridge.

## 5. Axis-swap involution and the native balance object

Inside a fixed sector `S_ij`, relabel the two active component generators:

`tau_ij(T^(ij)_{a,b}) := T^(ij)_{b,a}`.

Because the defining commutation relation and trace composition are symmetric in the two active generators, `tau_ij` is an exact involutive automorphism of the local trace algebra and preserves grade and realization-fiber cardinality.

Its fixed set is

`Delta_ij := Fix(tau_ij) = { T^(ij)_{m,m} : m in N_0 }`.

This is not assumed as a geometric bisector or imported central lane. It is derived as the fixed locus of a native component-relabeling involution.

On a fixed shell:

- if `n=2m`, `Sigma_n^(ij)` contains exactly one fixed trace, `T^(ij)_{m,m}`;
- if `n=2m+1`, `Sigma_n^(ij)` contains no fixed trace.

Thus parity is detected internally by fixed-point existence:

`Fix(tau_ij | Sigma_n^(ij)) != empty  <=>  n is even`.

This gives a native **balance/fixed-point** notion without importing a theorem-side central-lane formula.

## 6. Realization multiplicity and the choice-free central set

Define the P0/P1 realization multiplicity

`kappa_n(a) := |Realize_E(T^(ij)_{a,n-a})| = binom(n,a)`.

This is a path-fiber cardinality. It is **not** identified with any theorem-side breaker capacity in Phase A.

For `0 <= a < n`,

`kappa_n(a+1)/kappa_n(a) = (n-a)/(a+1)`.

Therefore:

- `kappa_n` is strictly increasing while `a < (n-1)/2`;
- it is strictly decreasing after the center;
- for `n=2m`, the unique maximum occurs at `a=m`;
- for `n=2m+1`, the exactly two maxima occur at `a=m` and `a=m+1`.

Define the choice-free central set

`C_n^(ij) := Argmax_{T in Sigma_n^(ij)} |Realize_E(T)|`.

Then

`C_(2m)^(ij) = {T^(ij)_{m,m}}`,

and

`C_(2m+1)^(ij) = {T^(ij)_{m,m+1}, T^(ij)_{m+1,m}}`.

For even grade, the fixed trace and unique maximum coincide.

For odd grade, there is no fixed trace and the two maximizers form one unordered `tau_ij`-orbit.

The associated scalar envelope is

`K_n := max_a kappa_n(a) = binom(n, floor(n/2))`.

Again, `K_n` is only a native trace-fiber multiplicity readout at Phase A. No theorem-side semantic identification is made.

## 7. A native parity-defect readout

The previous section yields a choice-free binary defect:

`beta_n := 0` if `C_n^(ij)` is a singleton,

`beta_n := 1` if `C_n^(ij)` is a two-element orbit.

Equivalently,

`beta_n = n mod 2`.

This object can be read entirely from the fixed-point/maximizer structure of the P0/P1 trace shell. It is a derived balance obstruction, not a theorem-side breaker imported by name or formula.

Freeze the surviving weak bridge as

`B_P0P1(n) := (Sigma_n^E, {C_n^(ij)}_sectors, K_n, beta_n)`

with all sector objects taken equivariantly under axis relabeling rather than with a distinguished sector name.

## 8. Axis relabeling / presentation / gauge audit

### 8.1 Cyclic relabeling of the three native axes

Let

`rho: E_1 -> E_2 -> E_3 -> E_1`.

The exact native line definition already transports cyclically

`S_12 -> S_23 -> S_31 -> S_12`.

Under `rho`:

- grade is preserved;
- each `Sigma_n^(ij)` is sent to the corresponding sector shell;
- realization fibers are sent bijectively to realization fibers;
- `kappa_n`, `K_n` and `beta_n` are unchanged;
- `Delta_12 -> Delta_23 -> Delta_31 -> Delta_12`;
- the unordered family `{Delta_12,Delta_23,Delta_31}` is preserved.

Thus the **orbit/family** of three balance lanes is native-equivariant, while a named singleton lane is not invariant.

### 8.2 Active-axis swap within a sector presentation

Under the component-label swap `tau_ij`:

- `a+b` is invariant;
- the trace algebra is preserved;
- the realization fiber is carried bijectively to the swapped fiber;
- binomial cardinality is invariant;
- the even central singleton is fixed;
- the two odd central maximizers are exchanged.

Thus the odd central object is canonically an **unordered pair/orbit**, not an ordered side.

### 8.3 Word serialization gauge

The native line identity is already the quotient of words by adjacent component-preserving commutations. Therefore no bridge object above depends on one particular shuffle/serialization.

`kappa_n(a)` counts the whole realization fiber rather than selecting a representative word.

### 8.4 Carrier presentation

No Euclidean carrier vector relation, Euclidean angle, Euclidean distance, radius shell, hyperbola or conic structure enters the construction.

### 8.5 Sector-chart gluing

The only global identification used is the already-frozen deduplication of one physical positive-axis trace across its two adjacent sector charts. No new cross-sector metric or vector subtraction is introduced.

## 9. Exact paired-presentation definability obstructions

The obstruction is the standard automorphism test: a parameter-free object definable from the frozen native structure must be invariant, or canonically equivariant at its declared semantic type, under every admissible relabeling automorphism of that structure.

### Obstruction A — no distinguished singleton global balance lane

Take one native presentation `M` and the Foundation-equivalent cyclicly relabeled presentation `M^rho`.

They agree, up to the canonical relabeling isomorphism, on every P0/P1 observable used in this Phase A:

- integer and event-count structure;
- three-sector incidence structure;
- trace composition;
- grade;
- realization fibers and their cardinalities;
- axis gluing;
- all unlabeled orbit data.

But a proposed readout that selects the named lane `Delta_12` in `M` selects `Delta_23` after `rho`.

Since `rho` acts transitively on

`{Delta_12,Delta_23,Delta_31}`,

no member of this three-element orbit can be parameter-free selected from the frozen symmetric native data.

Freeze:

`SINGLE_GLOBAL_CENTRAL_LANE_SELECTOR_FROM_CURRENT_P0P1 = EXACT_DEFINABILITY_OBSTRUCTION`.

The strongest choice-free substitute is the three-element orbit/torsor of sector balance lanes.

### Obstruction B — no ordered side of the odd central pair

For `n=2m+1`, compare one sector presentation with its active-component-swapped presentation under `tau_ij`.

All frozen P0/P1 trace observables and realization multiplicities agree, but

`T^(ij)_{m,m+1} <-> T^(ij)_{m+1,m}`.

Hence no current-strength parameter-free native rule can select one member as a distinguished left/right side while remaining invariant under component relabeling.

Freeze:

`ORDERED_ODD_CENTRAL_SIDE_FROM_CURRENT_P0P1 = EXACT_DEFINABILITY_OBSTRUCTION`.

The unordered pair is definable and survives.

### Scope of the obstruction

These paired-presentation certificates **do not** kill the weaker bridge. They kill only stronger readouts that demand a singleton sector choice or an orientation of the odd pair.

The weak object

`(global transition shell, balance-lane orbit, unordered odd central pair, realization-multiplicity envelope, parity defect)`

is invariant/equivariant at exactly the semantic strength claimed.

No paired-model obstruction was found against this weaker object because its definitions are preserved by the audited relabelings by construction and exact algebra.

## 10. Complete audit of every `3`

### `3` as frozen Foundation input

- exactly three positive native axes;
- exactly three native sectors generated by those axes.

This is the only load-bearing source of native three-ness in Phase A.

### `3` as presentation/index notation

- axis labels `1,2,3`;
- the cyclic relabeling orbit has three named sector presentations.

The labels are not an arithmetic derivation.

### `3` as derived arithmetic consequence

For `n>=1`:

`|Sigma_n^E|=3n`.

Also the global balance-lane orbit has cardinality `3`.

Both are consequences of the primitive three-sector input. Neither explains or re-derives why the native Foundation has three axes.

### `3` explicitly not used

- no premise `s=3`;
- no premise `B=3`;
- no premise `s=B=3`;
- no theorem-side uniqueness/selectivity result involving `3`;
- no use of `R_CELL=1/sqrt(3)` in the bridge;
- no theorem-side arithmetic chain.

Freeze dependency direction:

`NATIVE_THREE_SECTOR_INPUT -> P0P1_TRACE_BRIDGE -> DERIVED 3n / THREE-LANE-ORBIT`.

Not:

`THEOREM_SIDE_3 -> NATIVE_THREE_SECTOR_FOUNDATION`.

## 11. Anti-circularity and target-leakage audit

`TARGET_LEAKAGE = NONE_FOUND_IN_PHASE_A`.

The bridge was obtained before opening the theorem-side research package.

No target-side formula was copied into a native premise.

The words shell / central / capacity are used here only after independent P0/P1 definitions have been given:

- shell = equal transition-grade class;
- central set = fixed-point/maximizer structure of the trace involution and realization multiplicity;
- capacity-like scalar = exact cardinality of a native realization fiber.

No semantic identity to theorem-side objects is asserted in Phase A.

## 12. Minimality / weakest additional structure for stronger selectors

### To obtain one distinguished global balance lane

The weakest evident addition is one marked element of the three-lane orbit, equivalently a marked native sector/axis-pair or another parameter that breaks the cyclic `C3` transitivity.

Ontology cost: one three-way torsor choice.

This additional mark is not present in current Foundation and is not added by this task.

### To orient an odd central pair

The weakest evident addition is an orientation/order of the two active component directions, equivalently one binary choice that breaks `tau_ij`.

Ontology cost: one `C2` orientation choice for the relevant sector, or a coherent global orientation law if the choice must glue across sectors.

This additional orientation is not present in current Foundation and is not added by this task.

### No additional law needed for the weak bridge

No extra law is required for:

- additive transition grading;
- local/global grade shells;
- the balance-lane orbit;
- the unordered odd central pair;
- realization multiplicity `binom(n,a)`;
- the maximal multiplicity envelope `K_n`;
- parity defect `beta_n`.

## 13. Why this is `WEAKER_FOUNDATION_BRIDGE`, not the full task verdict yet

Phase A proves a genuinely native P0/P1 arithmetic bridge at a weaker, invariant semantic type than a named theorem-side lane/breaker architecture.

Whether this weaker bridge is sufficient to recover any exact theorem-side shell/lane/breaker/capacity role is deliberately **not** decided here, because the task requires the native freeze to precede theorem-side comparison.

Therefore Phase A freezes:

`PHASE_A_NATIVE_BRIDGE_THEOREM = PROVED_AT_P0P1_DERIVED_STRENGTH`.

`PHASE_A_STRONG_SINGLETON_SELECTOR = EXACTLY_OBSTRUCTED`.

`PHASE_A_THEOREM_SUFFICIENCY = UNTESTED_BY_DESIGN`.

`HARD_TARGET_FULL_TASK_STATUS = PENDING_PHASE_B_COMPARISON`.

## 14. Finite-certificate/checker status

`FINITE_CHECKER_REQUIRED = false`.

The Phase-A conclusions are symbolic consequences of the exact trace definitions and explicit automorphism actions. No bounded search is used as evidence for a global definability claim.

## 15. Evidence boundary

Permitted/frozen authorities actually used:

- `PROJECT_DEFINITION.md@f781c458b1dc4f3ec1c5cab9cdfc244ce11220f7`;
- `FOUNDATIONAL_LOGIC.md@f781c458b1dc4f3ec1c5cab9cdfc244ce11220f7`;
- `definitions/00_CURRENT_NATIVE_FOUNDATION.md@f781c458b1dc4f3ec1c5cab9cdfc244ce11220f7`;
- `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md@f781c458b1dc4f3ec1c5cab9cdfc244ce11220f7`;
- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@f781c458b1dc4f3ec1c5cab9cdfc244ce11220f7`;
- `native_semantics_admissibility.json@f781c458b1dc4f3ec1c5cab9cdfc244ce11220f7`;
- the Foundation-review gap statement in `driver_reviews/NATIVE_TRISECTOR_COUPLED_CLOSURE_FOUNDATION_CANONICALIZATION_DRIVER_DISPOSITION_20260826.md@f781c458b1dc4f3ec1c5cab9cdfc244ce11220f7`.

The admitted theorem node and theorem-side supporting package were **not opened for Phase A**.

## 16. Exact Phase-A freeze

Freeze the following together:

`PHASE_A_PRIMARY_VERDICT = WEAKER_FOUNDATION_BRIDGE`.

`P0P1_TRACE_GRADE = a+b`.

`LOCAL_TRACE_SHELL_CARDINALITY = n+1`.

`GLOBAL_TRACE_SHELL_CARDINALITY = 3n FOR n>=1`.

`EVEN_SHELL_BALANCE_FIXED_SET = SINGLETON`.

`ODD_SHELL_BALANCE_FIXED_SET = EMPTY`.

`EVEN_REALIZATION_MAXIMIZER_SET = SINGLETON`.

`ODD_REALIZATION_MAXIMIZER_SET = UNORDERED_TWO_ORBIT`.

`TRACE_FIBER_MULTIPLICITY = binom(n,a)`.

`TRACE_FIBER_MAX_ENVELOPE = binom(n,floor(n/2))`.

`BALANCE_PARITY_DEFECT = n mod 2`.

`GLOBAL_BALANCE_LANE_ORBIT = THREE_ELEMENT_EQUIVARIANT_ORBIT`.

`DISTINGUISHED_SINGLE_GLOBAL_BALANCE_LANE = EXACT_DEFINABILITY_OBSTRUCTION`.

`DISTINGUISHED_ORDERED_ODD_SIDE = EXACT_DEFINABILITY_OBSTRUCTION`.

`S_EQUALS_B_EQUALS_3_NOT_USED = true`.

`THEOREM_SIDE_PACKAGE_OPENED = false`.

`FOUNDATION_MUTATION = NONE`.

## 17. Next permitted action

Only after this Phase-A freeze may Phase B open the admitted theorem-side node/supporting package and compare, object by object, whether:

- the transition-grade shell maps to the theorem shell role;
- the three-lane orbit or local fixed/maximizer set is sufficient in place of a named central lane;
- the odd parity-defect / unordered pair maps to any breaker role;
- the trace-fiber multiplicity or its maximum maps to any capacity role;
- stronger target-side objects require precisely the `C3` selector and/or `C2` orientation additions isolated above.

No such comparison is part of this Phase-A return.
