# R020 — P021 Witness/Cardinality Dynamic-Completeness Re-audit

Researcher-ID: `EM-R020-3C6821`  
Task: `RS-R020-P021-WITNESS-CARDINALITY-DYNAMIC-COMPLETENESS-REAUDIT`  
Taskbook snapshot: `main@05fc9b2b6056bed55446de88c73bca437690f502`, taskbook blob `b3c756464ef37053561e77dd29367b5240f8c114`  
Historical P021 direction/witness source: PR #48 head `e8d176b30e7e52ca75b2ae9467066ea4f8f5af6c`  
Current P021 v3 owner: PR #213 head `0fd791a032469315d083ce815b117e440b953a98` (manifest-only owner generation)  
Historical A3/A4 count/witness bridge consumed: PR #83 head `7d596b1a845ca5f878593940607ca6ed67210845`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`  
Status: `NOT_CANONICAL`

## Return verdict

Primary:

`P021_THEOREMS_STABLE / DYNAMIC_CARRIER_SCOPE_NARROWED / TOOL_AUDIT_COMPLETE / NOT_CANONICAL`

Completion:

`P021_REAUDIT_COMPLETE / DYNAMIC_COMPRESSION_MATRIX_FROZEN / STATIC_ROWS_PRESERVED / COMPOSITION_ROWS_CLASSIFIED / NOT_CANONICAL`

No canonical P021 theorem was found false in its stated scope. The audit instead freezes a stricter type boundary:

> a correct P021 witness/cardinality/direction summary is a reusable current state only when the declared future observable descends through that summary (or an equivalent exact support/count congruence is proved).

The historical P021 direction-transport implementation already states the central distinction correctly: the primitive is the exact witness relation `W_ij`; `T_ij=|W_ij|` is a cardinality shadow, and ordinary multiplication of the shadows is not exact in general. Stage 12 is a local composed-count reduction, not an arbitrary finite-word closure theorem.

## 1. Canonical/source-surface inventory boundary

Current canonical `main` contains the P021 causal-boundary Python core, not the historical direction/witness-count transport layer. The current P021 v3 owner is a manifest-only continuation that explicitly retains direction-specific witness transport for future replay. The historical direction/witness declarations therefore remain provenance/owner-replay inputs rather than current canonical Lean theorems.

No P021-specific witness/cardinality Lean declaration is imported by current `EnterpriseMath.lean`. R016/R018 Lean results are consumed as generic upstream support/composition gates, not reclassified as P021 declarations.

Relevant owner declarations audited:

- `directional_focusing.py`: exact incidence orbits, target multiplicities, direction-channel collision summaries, anisotropy diagnostics.
- `directed_expansion.py`: exact fine future support plus scalar/counting summaries.
- `direction_transport.py`: exact two-path witnesses, witness cardinalities, transport matrices/support, exact witness joins, uniform-fibre cross-multiplication, split/merge diagnostics.
- historical A3/A4 bridge specializations: coupling defect `Delta`, equitable count quotients, nonnegative count-to-Boolean semantic shadows.

## 2. Static statistic versus reusable current state

The audit uses the following semantic types:

1. **Fine witness state**: exact incidences / exact witness relation / exact fine support.
2. **Static observation**: a deterministic function of the fine object, such as a count, spectrum, anisotropy scalar, row/column marginal, or a current composed count.
3. **Cell/quotient label**: `q(x)`.
4. **Full compatible fibre**: `q^-1(q(x))`, interpreted as a set of possible fine states, not as the original point.
5. **Boolean support state**: exact set-valued reachable support.
6. **N-count state**: nonnegative path/witness-count vector or matrix whose algebra is ordinary addition/multiplication.
7. **Witness/provenance state**: identity-bearing paths/incidences, strictly richer than counts.
8. **Future-signature refinement**: the coarsest (or any sufficient) refinement that factors all declared future observables.

A static theorem is not false merely because its output is not in classes 5–8.

## 3. Middle-incidence boundary: minimized counterexamples

### 3.1 Same one-step cardinalities, different composed Boolean support — 2 states, minimal

Take exact middle identity space `X={0,1}` and collapse it to one coarse cell. Compare:

System A:
- `R={(0,0)}`
- `S={(0,0)}`
- `|R|=|S|=1`
- `S o R={(0,0)}`

System B:
- `R={(0,0)}`
- `S={(1,0)}`
- `|R|=|S|=1`
- `S o R=empty`

Thus both one-step coarse cardinality matrices are `[1]`, and both one-step Boolean support matrices are `[true]`, but the exact composed support differs. The forgotten datum is exactly the equality/intersection of the middle witness identity.

Exhaustive search over all simple relations on one state finds no such failure; two states are minimal in the declared one-coarse-cell search class.

Profile form:

- `m=2`
- `l=(1,0)`
- System A `r=(1,0)`: `N=1`
- System B `r=(0,1)`: `N=0`
- both have `L=R=1`.

### 3.2 Same one-step counts and identical exact fine composed support, different path multiplicity — 3 states, minimal

On `X={0,1,2}`:

Common:
- `R={(0,0),(0,1)}`.

System A:
- `S={(0,0),(1,0)}`
- exact composed relation `{(0,0)}`
- two exact middle paths.

System B:
- `S={(0,0),(2,0)}`
- exact composed relation `{(0,0)}`
- one exact middle path.

Both have `|R|=|S|=2` and the same exact Boolean composed relation, yet path multiplicity is `2` versus `1`. Exhaustive search found no such same-count/same-exact-support multiplicity separation on `n<=2`; `n=3` is minimal for simple relations in this search class.

This proves that even **fine Boolean support** is not count-complete.

### 3.3 P021 Stage-11 overcount remains valid

The historical P021 fixture has two independent chains. Adjacent witness cardinalities are `2` and `2`, while the exact three-edge path count is `2`; ordinary integer multiplication gives `4`. This is not a bug in the tool: `naive_matrix_product_entry` exists specifically as the negative oracle.

## 4. Support versus multiplicity versus provenance

For nonnegative path-count semantics there is a strict information ladder:

`exact witness/provenance -> N path counts -> Boolean support`.

The implications are semantic projections:

- witness identities can be counted;
- nonzero counts can be Booleanized;
- the converses fail.

The 3-state example above separates Boolean support from path counts. Count-to-provenance failure is even more basic: two identity-labelled path families can have the same numeric counts while an identity-sensitive future accepts one family and rejects the other.

R015/R016 branch deferral is therefore applicable only **after** the current state has already been established as exact Boolean result-support under a union-preserving relational future. It cannot repair a P021 cardinality shadow that has already lost middle-incidence correlation, and it cannot erase multiplicity/provenance that the declared future still reads.

## 5. Exact dynamic-completeness criteria

Let `q:X->Q`.

### 5.1 Deterministic functional descent

For a deterministic transition `f:X->X`:

`FUNCTIONAL_SAFE(q,f)`

iff there exists a unique induced `fbar:q(X)->q(X)` with

`q(f(x)) = fbar(q(x))`

iff

`q(x)=q(y) => q(f(x))=q(f(y))`

iff

`ker(q) subset ker(q o f)`.

For a finite operation family, require this generatorwise.

### 5.2 One-step coarse Boolean successor-support exactness

For a relation `R`, define

`sig_R^q(x) = { q(y) : x R y }`.

Then a coarse cell is an exact one-step Boolean current state iff `sig_R^q` factors through `q`:

`q(x)=q(x') => sig_R^q(x)=sig_R^q(x')`.

This is the relation-valued analogue of deterministic descent. A mere existential full-fibre quotient

`Rhat(a)= union_{x in q^-1(a)} sig_R^q(x)`

is always an exact MAY summary of the entire fibre, but it need not be a pointwise or repeatedly executable state.

### 5.3 Finite-word Boolean composition safety

For a generator family `{R_a}`, generatorwise one-step support constancy is sufficient for exact repeated coarse execution for every finite word and every fine support. Conversely, if the coarse transition language contains the one-letter generators and is required to reproduce singleton/fibre coarse support by repeated execution, the one-step constancy condition is necessary.

This is the P021 specialization of the R017/R018 strong saturation/completeness boundary; it is consumed, not re-proved as a new mother theorem.

For a **fixed terminal observable** and a declared word set `U`, a weaker static criterion is available. Define the future-support signature

`Sigma_U(x) = (Support_o(R_w,x))_{w in U}`.

Then exact final-answer compression for `U` is equivalent to factorization of `Sigma_U` through `q`:

`ker(q) subset ker(Sigma_U)`.

This says nothing by itself about a closed transition on `Q`.

### 5.4 Future-language growth is a real refinement axis

A bounded exhaustive deterministic example shows a summary can be exact for one declared horizon and fail at the next:

- four states;
- `q=(0,0,1,2)`;
- `f=(0,2,3,0)`;
- binary observable `o=(0,0,0,1)`.

The merged states `0,1` agree on `o` and `o o f` but disagree on `o o f^2`. Exhaustive search found no such deterministic one-generator/binary-observable horizon-1 versus horizon-2 separation on `n<=3`; `n=4` is minimal in that declared search class.

Thus future-signature completeness is explicitly language/horizon relative.

### 5.5 Full-fibre one-step exactness does not imply repeated saturation exactness

Independent reconstruction of the R021 quotient-composition search gives:

- `n=1`: 1 trial, 0 failures;
- `n=2`: 20 trials, 0 failures;
- `n=3`: 837 trials, 84 failures;
- total through `n=3`: 858 trials, 84 failures.

First independently found fixture:

- `q=(0,0,1)`;
- `f=(0,2,0)`;
- start fibre label `0`.

One-step coarse image is `{0,1}`. Exact two-step coarse image is `{0}`, while repeated full-fibre quotient saturation returns `{0,1}`.

This is a different minimality statement from pointwise deterministic descent and must not be conflated with it.

### 5.6 N-semiring path-count exactness

Let each generator be a nonnegative integer transition matrix `M_a` on fine states. For each fine source `x`, define its block-count signature

`kappa_a(x)[B] = sum_{y in B} M_a[x,y]`.

A quotient count row is well-defined iff `kappa_a` is constant inside every source `q`-cell. This is exactly the standard **equitable partition / lumpability** condition for nonnegative count matrices.

If every generator is equitable with respect to the same partition, quotient matrices multiply exactly for every finite word:

`Q(M_1 ... M_k) = Q(M_1) ... Q(M_k)`.

This is the strong dynamically reusable count carrier. It is prior mathematics; P021 only consumes it as the correct closure regime.

Independent bounded check: for all 96 equitable 3x3 `0/1` matrices for partition `{0,1}|{2}`, all 9,216 ordered matrix pairs remained equitable under product and satisfied exact quotient multiplication.

## 6. Uniform-fibre Stage 12 re-audit

For a middle direction class with exact incidences `e_1,...,e_m`, predecessor/successor profiles `l_i,r_i`, marginals

`L=sum l_i`, `R=sum r_i`

and exact current matched count

`N=sum l_i r_i`,

define

`Delta = mN - LR`.

Then

`Delta = sum_{i<j} (l_i-l_j)(r_i-r_j)`.

The historical Stage-12 theorem is correct:

- if `l` is uniform, `Delta=0`;
- if `r` is uniform, `Delta=0`;
- therefore `mN=LR`.

But the theorem is precisely a **local current composed-count reduction**. It does not prove that `L,R,m` form a closed current-state carrier for an additional future join.

Uniformity is sufficient, not necessary. Example:

- `l=(0,0,1)`;
- `r=(0,2,1)`;
- both profiles nonuniform;
- `m=3, L=1, R=3, N=1`;
- `Delta=0`, hence `mN=LR`.

Focused enumeration for profile lengths `1..4`, entries `0..3` checked 69,904 profile pairs:
- zero failures of the `Delta` pair-difference identity;
- zero failures of `uniform on one side => Delta=0`;
- 5,712 both-nonuniform pairs with `Delta=0` (288 for `m=3`, 5,424 for `m=4`).

Therefore the sharp local condition for the normalized marginal formula is `Delta=0`; one-sided uniformity is a clean sufficient subcase. Dynamic arbitrary-word count closure requires a stronger invariant such as equitability of the whole generator family.

## 7. Matrix semantics: Boolean and natural-number products

### 7.1 Exact fine-state matrices

If `B_R` and `B_S` are **fine Boolean adjacency matrices**, then standard Boolean matrix multiplication exactly represents relational composition:

`B_(S o R) = B_R (*)_Bool B_S`.

If `M_R` and `M_S` are **fine nonnegative count-transition matrices**, ordinary arithmetic multiplication exactly counts two-step paths:

`M_(paths) = M_R M_S`.

Positive support is a semiring shadow:

`supp(M_R M_S) = supp(M_R) (*)_Bool supp(M_S)`.

Independent check: all 6,561 ordered pairs of 2x2 nonnegative matrices with entries `0..2` satisfied this identity.

### 7.2 P021 cardinality-shadow matrices are not automatically either of those objects

P021 `T_ij=|W_ij|` is an aggregate count of two-path witnesses between direction classes. Multiplying `T` values pairs witnesses that merely share a **coarse direction class**, not necessarily the same exact middle incidence.

For one middle class:

`N = sum_i l_i r_i`.

Raw arithmetic marginal product is

`LR = N + sum_{i != j} l_i r_j`.

Because all terms are nonnegative, the raw product `LR` equals the exact `N` iff every off-diagonal cross term vanishes. In a nondegenerate positive case, this essentially forces all left/right mass onto the same single exact middle incidence. This is much stronger than Stage-12 uniformity.

Under `Delta=0`, the correct aggregate recovery is instead

`mN=LR`,

or equivalently `N=LR/m` when exact division is justified. This is a fibre-size-normalized contraction, not ordinary integer matrix multiplication.

### 7.3 Coarse Boolean product can also fail

Let coarse Boolean support use only whether an aggregate cell contains at least one witness. In the 2-state example both one-step matrices are `[true]`, so Boolean product predicts `[true]`; exact fine composition is empty in System B.

For a fixed source-cell `A`, middle cell `B`, and target-cell `C`, define:
- `Y_R(A,B)` = exact middle states in `B` reached by some `R` edge from `A`;
- `Y_S(B,C)` = exact middle states in `B` that have some `S` continuation into `C`.

The coarse Boolean product is exact for that triple iff

`Y_R(A,B) != empty and Y_S(B,C) != empty => Y_R(A,B) intersect Y_S(B,C) != empty`.

This pairwise join-consistency condition is the exact fixed-pair boundary. For a reusable operation family, use the stronger generatorwise support-congruence condition consumed from R018.

### 7.4 Set-valued support is not a count matrix

For a simple relation, arithmetic multiplication of its `0/1` adjacency matrix counts the number of middle paths, while Boolean multiplication only records existence. Two middle paths to the same endpoint yield arithmetic entry `2` and Boolean entry `true`.

Conversely, Booleanizing a valid count matrix is legitimate only when the declared observable is support. It irreversibly discards path multiplicity. A downstream count-sensitive computation cannot recover the lost `2` from `true`.

## 8. Uniform one-step fibres kill test

The phrase "uniform fibre" is overloaded. Two distinct claims must be separated.

### Weak cardinality uniformity can fail under composition

There is a minimal 3-state simple-relation example in which every fine source has the same one-step **number of distinct successors** in both `R` and `S`, but the composite successor-support cardinality becomes nonuniform:

`R`:
- `0 -> {0,2}`
- `1 -> {0,1}`
- `2 -> {0,1}`

so every row has support size `2`.

`S`:
- `0 -> 0`
- `1 -> 1`
- `2 -> 0`

so every row has support size `1`.

Then:
- `0 -> {0}`
- `1 -> {0,1}`
- `2 -> {0,1}`

under `S o R`, giving composite support sizes `(1,2,2)`.

Exhaustive search found no such example on `n<=2`.

### Equitability does not fail this way

If "uniformity" means the stronger count-congruence condition that every state in a source cell has the same target-cell row-count signature, that is equitability. It is closed under multiplication and is exactly the positive dynamic regime described above.

Therefore the kill pressure does **not** justify a blanket claim that all uniformity is non-compositional.

## 9. Executable semantic-assumption audit

No `TOOL_ASSUMPTION_MISMATCH` was found in the audited P021 tools.

Key findings:

- `direction_transport_matrix` explicitly calls itself a cardinality shadow.
- `naive_matrix_product_entry` explicitly exists to expose the no-go.
- `uniform_fiber_cross_multiplication_holds` rejects instances in which neither side is uniform; it does not silently infer exactness.
- `compose_two_path_witnesses` explicitly checks equality of the exact middle incidence.
- `transport_support` computes immediate zero/nonzero support only.
- `canonical_one_to_one_transport` is an adjacent-step support-permutation test; it does not claim multi-step witness reachability.
- scalar collision/anisotropy tools are correct static statistics.
- `future_section` / `expansion_trajectory` are positive controls: they retain exact fine Boolean support and therefore are recursively executable under the fixed fine relation.
- there is no P021-specific witness/cardinality Lean module on the current root import surface.

Standalone focused oracle:
- Python `py_compile`: PASS.
- bounded exact search suite: PASS; results frozen in `r020_p021_dynamic_completeness_results.json`.
- repository CI was not queried or used.

## 10. P023 terminology routing

Recommended typed consumption:

### `FUNCTIONAL_SAFE`

Use only for deterministic descent:

`q(x)=q(y) => q(f(x))=q(f(y))`.

### `FINE_SUPPORT_SAFE`

Use when the retained current carrier is the exact fine set-valued support (or a lossless code for it) and the future is result-only relational/union-preserving. This is the R015/R016 branch-deferral domain. It does not imply count/provenance safety.

### `CELL_ONE_STEP_EXACT`

Define this strongly enough to be reusable for one coarse step:

the coarse successor-support signature is constant on every `q`-fibre.

Do not use the same term for mere existential full-fibre MAY lifting, which is weaker.

### `COMPOSITION_SAFE[semantic target, future language]`

Make the semantic target explicit.

- Boolean support: generatorwise support congruence / R018 strong completeness.
- N path counts: generatorwise equitability of count transitions.
- witness/provenance: identity-bearing future signatures must descend; numeric counts are insufficient if identities remain readable.

A naked unparameterized `COMPOSITION_SAFE` risks collapsing distinct semirings/observables.

## 11. Downstream routing

### P010 / P011

`NO_NEW_MOTHER_TASK_REQUIRED`

Their canonical theorem truth is unchanged. Fibre cardinalities, collision totals, and spectra remain correct static statistics. The only boundary is interpretive: those statistics are not automatically next-step states. A new mother research task would be artificial unless a canonical P010/P011 statement actually claims recursive closure.

### P018 precision-object typing

`NO_FOUNDATIONAL_RETYPE_REQUIRED`

The R019 frozen distinction among cell labels, full fine fibres, set-valued supports, and future-refined point carriers remains adequate. P021 adds an orthogonal observable tag that should stay explicit at interfaces:

- `BOOL_SUPPORT`;
- `N_PATH_COUNT`;
- `WITNESS_PROVENANCE`.

Do not fold all three into a generic "support" object.

### R014 resource/Pareto accounting

Resource comparisons must be indexed by the same semantic target:

`(future language, observable/carrier, required closure horizon)`.

A small P021 `T` matrix is not a cheaper equivalent implementation of exact witness transport for a multi-step count/provenance task if it is semantically insufficient. If a repair is required, charge:
- middle-incidence/correlation metadata;
- fibre-size/equitability certificates where used;
- refinement/future-signature state;
- decoder/reconstruction cost.

Only after semantic-fibre equality is established should storage/work/branch-width Pareto comparison begin.

### A3/A4 support bridge

Canonical A3->A4 is a Boolean/support bridge. Keep it that way.

Do not infer that a P021 cardinality shadow is an N-semiring compositional state merely because positive support of a **valid** count matrix commutes with multiplication. If count semantics is needed, use a separately typed nonnegative count carrier and an equitability/count-congruence proof. Signed A3 quantities with cancellation are outside the positive-support homomorphism.

No new A3/A4 mother theorem is required by this audit.

## 12. Prior-art/rooting

The following are prior mathematics and are not Enterprise Math novelty claims:

- relation composition and relational direct image;
- Boolean adjacency matrices and Boolean semiring multiplication;
- nonnegative path-count matrices and ordinary semiring multiplication;
- quotient factorization / congruence;
- equitable partitions / lumpability;
- bisimulation and future behavioural equivalence;
- sufficient statistics / future signatures;
- automata/Myhill–Nerode-style distinguishability;
- coalgebraic/behavioural quotient ideas.

Enterprise-specific residue frozen here is narrower:

> which historical P021 direction/witness/cardinality outputs retain which declared observable, and which may legally be reused after a further composition.

## 13. Frozen theorem/tool impact matrix

| artifact_theorem | fine_object | compressed_object | preserved_observable | static_exact | one_step_support_exact | composition_exact | multiplicity_exact | semantic_status | counterexample_or_required_hypothesis | required_action | downstream_owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| canonical main P021 causal-boundary core (control row) | finite directed graph + integer expansion/phase data | boundary/phase observations | declared causal-boundary observables only | YES | N/A to witness/cardinality audit | N/A | N/A | SEMANTICALLY_STABLE | Not a direction/cardinality carrier; canonical main contains no P021 witness-count composition theorem. | No change. | P021 |
| directional_focusing.incidence_orbits / phase_marked_direction_roles | exact outgoing primitive incidences + marked-section automorphisms | orbit partition, retaining exact edge members | intrinsic direction classes / causal-role refinement | YES | N/A | ONLY when exact incidence members are retained and later joined | YES for retained members | SEMANTICALLY_STABLE | No lossy cardinality collapse in the orbit output itself. | Keep exact incidence membership distinct from orbit counts. | P021 |
| directional_focusing.channel_multiplicities / directional_channel_data[multiplicities] | one direction channel as exact edge set | target vertex -> incoming-incidence count vector | one-step target support and target multiplicity | YES | YES | CONDITIONAL: reusable for N-path propagation only with exact target identities and a valid next-step count transition | YES at current target-state vector level; provenance NO | THEOREM_STABLE / INTERPRETATION_CHANGED | Dropping target identities to totals/spectra loses middle incidence. | Type as fine-state count vector, not as generic direction summary. | P021 / A4 |
| directional_focusing.directional_channel_data scalar fields / collision spectrum | one exact direction channel | incidence count, target count, collision excess, spectrum | static one-section collision statistics | YES | NO from scalars alone | NO | PARTIAL statistic only | SEMANTICALLY_STABLE | Equal scalar/collision summaries can have different middle incidence. | Do not reuse scalar/spectrum as next state absent a future-signature proof. | P021 / P011 |
| directional_focusing.cross_channel_pair_collision / pair_collision_channel_decomposition | multiple exact direction channels | within/cross pair-collision counts | static J2 decomposition | YES | NO | NO | Only declared pair-collision statistic | SEMANTICALLY_STABLE | Static combinatorial identity; no recursive-state claim. | Preserve as static statistic. | P021 / P011 |
| directional_focusing.collision_rate_anisotropy_numerator | direction channels with incidence/collision counts | single integer anisotropy numerator | current-section fraction-free anisotropy witness | YES | NO | NO | NO | SEMANTICALLY_STABLE | Supplement 10 already says raw time difference is not direction transport. | Keep static; never promote scalar to transport state. | P021 |
| directed_expansion.future_section / expansion_trajectory | current exact vertex support under fixed directed graph | exact set-valued fine support (not merely a cell label) | Boolean reachable fine support | YES | YES | YES for repeated relational direct image on the same fine carrier | NO | SEMANTICALLY_STABLE | R015/R016 applies only to this Boolean support semantics, not to path counts/provenance. | Use as positive-control FINE_SUPPORT_SAFE carrier. | P021 / P023 |
| directed_expansion.section_expansion / branching_collision_decomposition / local_collision_spectrum | current section and one-step incidence relation | integer scalar/statistic | one-step expansion/collision quantities | YES | NO | NO | Only the declared statistic | SEMANTICALLY_STABLE | Correct static formulas do not imply recursive executability. | No theorem change; tag as static observation. | P021 / P010 / P011 |
| direction_transport.composable_two_path_witnesses | two exact direction channels as edge sets | full TwoPathWitness set with exact shared vertex/incidences | exact two-edge witness identity | YES | YES | YES when exact middle witness identity is retained | YES | SEMANTICALLY_STABLE | Exact witness join is the retained primitive. | Keep as exact witness structure. | P021 |
| direction_transport.composable_two_path_count | TwoPathWitness set | integer cardinality | current two-path count; immediate existence via >0 | YES | YES for the current pair | NO | CURRENT STEP ONLY | THEOREM_STABLE / INTERPRETATION_CHANGED | 2-state middle-incidence counterexample; Stage 11 2×2 overcount. | Forbid use as a recursive current state. | P021 / P023 |
| direction_transport.direction_transport_witnesses | successive direction partitions with exact edge members | matrix of exact witness sets W_ij | full current two-path incidence relation by direction classes | YES | YES | YES under exact fibre join on same middle incidence; fixed Python API demonstrates one further join | YES | SEMANTICALLY_STABLE | Must not replace W_ij by W_ij before an identity-insensitive proof. | Retain W as general P021 primitive. | P021 |
| direction_transport.direction_transport_matrix T_ij=W_ij | exact witness matrix W_ij | nonnegative integer cardinality matrix | one-step witness count per direction-class pair; zero/nonzero support | YES | YES | NO blanket law | CURRENT ADJACENT STEP ONLY | THEOREM_STABLE / INTERPRETATION_CHANGED | Equal cardinality matrices can have different composed support; ordinary arithmetic product can overcount. | Type as CARDINALITY_SHADOW, not current state. | P021 / P023 / R014 |
| direction_transport.compose_two_path_witnesses | two exact TwoPathWitness relations | exact ThreePathWitness set | exact shared-middle incidence and path provenance through three edges | YES | YES | YES for exact join | YES | SEMANTICALLY_STABLE | Equality of middle primitive incidence is essential. | Keep exact-join semantics; generalized arbitrary-length join is standard prior relation/path mathematics. | P021 / A4 |
| direction_transport.exact_three_path_count | three exact direction channels | integer current three-edge chain count | current path multiplicity for the given triple | YES | YES for this triple via N>0 | NO as a subsequent current state | CURRENT TRIPLE ONLY | SEMANTICALLY_STABLE | Same N can end on different exact incidences and diverge under a fourth step. | Keep as static/current composed-count readout. | P021 |
| direction_transport.predecessor_witness_profile / successor_witness_profile | exact left/middle/right incidence channels | per-exact-middle-incidence count vectors l_i,r_i | middle-incidence correlation sufficient for current N=sum l_i r_i | YES | YES for current join when both profiles retained | NOT a closed arbitrary-word carrier by themselves | YES for current N | SEMANTICALLY_STABLE | Future joins may read endpoint incidence distribution beyond current dot product. | Keep vectors keyed to exact middle identity if used. | P021 / A4 |
| direction_transport.uniform_fiber_cross_multiplication_holds (Stage 12) | middle profiles l,r of size m | m,L=sum l,R=sum r plus uniformity hypothesis | current exact three-edge count through identity mN=LR | YES under stated hypothesis | YES for this current triple | NO arbitrary finite-word closure | YES for this current triple | THEOREM_STABLE / INTERPRETATION_CHANGED | Uniform on either side => Delta=0; converse false. Local Delta=0 is weaker than equitability. | Freeze wording as LOCAL COMPOSED-COUNT REDUCTION, not COMPOSITION_SAFE carrier. | P021 / P023 |
| direction_transport.transport_support | one-step cardinality matrix T | Boolean zero/nonzero matrix | immediate direction-class composability | YES | YES | NO on coarse classes in general | NO | THEOREM_STABLE / INTERPRETATION_CHANGED | 2-state one-cell example: Boolean product predicts a path while exact fine composition is empty. | Do not invoke R015 until this support itself has been shown composition-safe. | P021 / P023 |
| direction_transport.transport_branching_profile / transport_merging_profile | Boolean transport support | row/column support degrees | static split/merge degree marginals | YES | NO (marginal only) | NO | NO | SEMANTICALLY_STABLE | Different support patterns can share row/column degrees. | Keep as static diagnostic. | P021 |
| direction_transport.canonical_one_to_one_transport | one-step transport support matrix | permutation matching or None | adjacent-step class identity from composability | YES | YES under permutation-support criterion | NO guarantee of exact multi-step fine witness reachability | NO | THEOREM_STABLE / INTERPRETATION_CHANGED | A 1x1 positive support is a permutation support yet two successive cells can use disjoint exact middle witnesses. | Keep criterion scoped to adjacent class matching. | P021 |
| direction_transport.transport_obstruction | one-step transport support | split/merge/birth/death/cardinality-mismatch label | adjacent structural obstruction category | YES | NO (classification only) | NO | NO | SEMANTICALLY_STABLE | No dynamic-state claim. | No change. | P021 |
| direction_transport.naive_matrix_product_entry | two adjacent aggregate counts | ordinary integer product L*R | none claimed; negative diagnostic | YES as arithmetic expression, NOT as exact path count | N/A | NO | NO | SEMANTICALLY_STABLE | Stage 11: 2*2=4 vs exact N=2. | Retain as explicit no-go oracle. | P021 |
| historical A3/A4 bridge witness_coupling_defect: Delta=mN-LR | middle incidence profiles l,r | m,L,R,Delta (or N) | one fixed current matched count N | YES | YES for that fixed count/support | NO recursive witness identity | CURRENT COMPOSITE ONLY | SEMANTICALLY_STABLE | Delta=0 iff normalized cardinality formula is exact; both profiles can be nonuniform. | Consume as one-step repair specialization, not a P021 mother theorem. | A3/A4 bridge / P023 |
| historical A3/A4 bridge equitable_count_quotient | nonnegative fine count-transition matrices + fixed partition | per-source-cell quotient count matrix | target-cell path counts for arbitrary finite words | YES under equitability | YES | YES for a generatorwise equitable family | YES (path counts), provenance NO | CONDITIONALIZED | Target-cell row sums must be constant within every source cell; standard equitability/lumpability. | Use as the strong dynamic count regime; root as prior mathematics. | A4 / P023; P021 consumes |
| historical A3/A4 bridge semantic_shadows.support_product_commutes | valid nonnegative integer path-count matrices | positive Boolean support | existence/reachable support | YES | YES | YES when the input matrices are already valid compositional N-semiring carriers | NO after shadow | CONDITIONALIZED | Nonnegative counts; does not legalize a P021 aggregate cardinality shadow that was never a valid transition matrix. | Keep semiring typing explicit; reject signed/cancellation analogy. | A4 / P023 |
| interpretive misuse: reuse P021 T/cardinality/direction marginals as next current state | exact witness/incidence relation | T, support degrees, collision/direction marginals only | varies; only static/current-step summaries | YES where declared | SOMETIMES | NO without additional congruence/equitability/future-signature hypothesis | NO beyond current counted quantity | COUNTEREXAMPLE_RISK | 2-state middle-incidence support failure; 3-state same-support/different-path-count; 3-state saturation failure. | Add semantic type boundary in any future replay; do not rewrite stable theorem statements. | P021 / P023 / P018 / R014 |

## 14. Final Driver routing

- Canonical theorem break: **NO**.
- Static theorem preservation: **YES**.
- Dynamic carrier interpretation narrowed: **YES**.
- Tool mismatch: **NONE FOUND**.
- P010/P011 new mother task: **NO_NEW_MOTHER_TASK_REQUIRED**.
- P023: consume the four typed terms above; parameterize composition safety by semantic target.
- P018: no foundational retype; preserve count/provenance tags orthogonally.
- R014: resource comparison only within equal semantic fibres.
- A3/A4: keep Boolean support bridge distinct from N-count/equitability bridge.
- New descendant task created: **NO**.
- Canonical semantics modified: **NO**.
- CI/workflow queried: **NO**.

Final:

`P021_THEOREMS_STABLE / DYNAMIC_CARRIER_SCOPE_NARROWED / TOOL_AUDIT_COMPLETE / NOT_CANONICAL`

and

`P021_REAUDIT_COMPLETE / DYNAMIC_COMPRESSION_MATRIX_FROZEN / STATIC_ROWS_PRESERVED / COMPOSITION_ROWS_CLASSIFIED / NOT_CANONICAL`
