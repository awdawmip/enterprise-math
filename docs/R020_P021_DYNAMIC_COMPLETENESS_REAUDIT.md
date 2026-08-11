# R020 — P021 Witness/Cardinality Dynamic-Completeness Re-audit

Researcher-ID: `EM-R020-3C6821`  
Task: `RS-R020-P021-WITNESS-CARDINALITY-DYNAMIC-COMPLETENESS-REAUDIT`  
Frozen source snapshot: `main@05fc9b2b6056bed55446de88c73bca437690f502`  
Taskbook blob: `b3c756464ef37053561e77dd29367b5240f8c114`  
Historical P021 direction/witness source: PR #48 head `e8d176b30e7e52ca75b2ae9467066ea4f8f5af6c`  
Current P021 v3 owner: PR #213 head `0fd791a032469315d083ce815b117e440b953a98`  
Historical A3/A4 count/witness bridge consumed: PR #83 head `7d596b1a845ca5f878593940607ca6ed67210845`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`  
Status: `NOT_CANONICAL`

## Verdict

Primary return:

`P021_THEOREMS_STABLE / DYNAMIC_CARRIER_SCOPE_NARROWED / TOOL_AUDIT_COMPLETE / NOT_CANONICAL`

Completion return:

`P021_REAUDIT_COMPLETE / DYNAMIC_COMPRESSION_MATRIX_FROZEN / STATIC_ROWS_PRESERVED / COMPOSITION_ROWS_CLASSIFIED / NOT_CANONICAL`

No canonical P021 theorem was found false in its stated scope. The required change is interpretive, not mathematical:

> a correct one-step witness/cardinality/direction statistic is a reusable current state only when the declared future observable factors through that statistic, or an equivalent support/count congruence has been proved.

The historical P021 implementation already encodes the central negative boundary correctly: exact witness sets are the primitive transport data; `T_ij=card(W_ij)` is a cardinality shadow; ordinary multiplication of those shadows is not exact in general. Stage 12 is a local composed-count reduction, not an arbitrary finite-word closure theorem.

The complete 25-row frozen theorem/tool matrix is machine-readable in:

`experiments/r020_p021_theorem_tool_impact_matrix.json`.

The focused bounded evidence is in:

`experiments/r020_p021_dynamic_completeness_results.json`.

## 1. Declaration/tool inventory and source boundary

Current canonical `main` contains the P021 causal-boundary executable core, not the historical direction/witness-count transport layer. Current P021 v3 is a manifest-only owner continuation that explicitly retains direction-specific witness transport for future replay. No P021-specific witness/cardinality Lean module is imported by current `EnterpriseMath.lean`.

Audited historical P021 declarations:

- `directional_focusing.py`: exact incidence orbits, causal roles, target multiplicities, collision summaries, anisotropy diagnostics;
- `directed_expansion.py`: exact fine future support plus scalar/counting summaries;
- `direction_transport.py`: exact two-path witnesses, witness cardinalities, transport matrices/support, exact witness joins, uniform-fibre reduction, split/merge diagnostics;
- historical A3/A4 bridge specializations: coupling defect `Delta`, equitable count quotients, and nonnegative count-to-Boolean semantic shadows.

R015/R016 and R017/R018 are consumed as already-frozen generic support/composition gates; they are not re-proved or reclassified as P021 theorems.

## 2. Semantic type separation

The audit keeps the following objects type-distinct:

1. exact fine relation / witness structure;
2. deterministic observation/statistic;
3. quotient/cell identifier;
4. full compatible fine fibre;
5. Boolean reachable-result support;
6. witness/path multiplicity;
7. provenance / branch identity;
8. middle-incidence correlation;
9. task/future-signature refinement.

A static theorem is not false merely because its output is not a recursively executable carrier.

The information ladder relevant to P021 is strict:

`exact witness/provenance -> nonnegative path counts -> Boolean support`.

The converses fail.

## 3. Minimized middle-incidence counterexamples

### 3.1 Equal one-step cardinality and Boolean summaries, different composed support

Two fine middle states are sufficient and one is not.

System A:

- `R={(0,0)}`;
- `S={(0,0)}`;
- one-step counts `(1,1)`;
- exact composition `{(0,0)}`.

System B:

- `R={(0,0)}`;
- `S={(1,0)}`;
- the same one-step counts `(1,1)`;
- exact composition is empty.

After both middle states are collapsed to one cell, both one-step Boolean matrices are `[true]`, but Boolean product predicts a path in System B that does not exist.

The lost datum is exactly the shared-middle witness identity/intersection.

Profile form:

- `m=2`;
- `l=(1,0)`;
- System A `r=(1,0)` gives `N=1`;
- System B `r=(0,1)` gives `N=0`;
- both have `L=R=1`.

### 3.2 Equal one-step counts and identical exact Boolean composition, different path multiplicity

Three states are minimal in the searched simple-relation class.

Common:

`R={(0,0),(0,1)}`.

System A:

`S={(0,0),(1,0)}` gives exact composed support `{(0,0)}` with two middle paths.

System B:

`S={(0,0),(2,0)}` gives the same exact composed support `{(0,0)}` with one middle path.

Both have one-step counts `(2,2)`. Thus even exact fine Boolean support is not path-count complete.

### 3.3 Historical Stage-11 overcount remains correct

The historical two-chain P021 fixture has adjacent witness counts `2` and `2`. Raw multiplication gives `4`, while exact three-edge chains are `2`. This is the intended negative oracle, not a tool defect.

## 4. Dynamic-completeness hierarchy

Let `q:X->Q`.

### 4.1 Deterministic functional descent

For `f:X->X`:

`FUNCTIONAL_SAFE(q,f)` iff there exists a unique induced `f_bar:q(X)->q(X)` satisfying

`q(f(x))=f_bar(q(x))`,

iff

`q(x)=q(y) => q(f(x))=q(f(y))`,

iff

`ker(q) subseteq ker(q o f)`.

For a finite operation family, require this generatorwise.

### 4.2 One-step coarse Boolean successor-support exactness

For relation `R`, define

`sig_R^q(x)={q(y): x R y}`.

A cell identifier is an exact one-step Boolean state iff `sig_R^q` factors through `q`, equivalently iff it is constant on every `q`-fibre.

By contrast, existentially lifting the whole fibre produces an exact MAY summary of that whole fibre, not automatically a pointwise or recursively executable state.

### 4.3 Arbitrary finite-word Boolean support

For a finite generator family, generatorwise successor-support constancy is sufficient for exact repeated coarse execution for every finite word. If one-letter generator observations themselves belong to the declared future language, the same condition is also necessary.

This is the P021 specialization of the already-frozen R017/R018 strong completeness boundary.

For a fixed terminal observable and declared word set `U`, a weaker static criterion is enough. Define the final-support future signature

`Sigma_U(x)=(Support_o(R_w,x))_{w in U}`.

Exact answers for that fixed language are equivalent to factorization of `Sigma_U` through `q`. This does not imply a closed transition on `Q`.

### 4.4 Future-language growth forces refinement

Independent bounded search found a four-state minimum, in the declared deterministic one-generator/binary-observable class, where a quotient is exact through horizon 1 but fails at horizon 2:

- `q=(0,0,1,2)`;
- `f=(0,2,3,0)`;
- observable `o=(0,0,0,1)`.

The merged states `0,1` agree on current and one-step observations but disagree two steps later. No such example appeared for `n<=3` in that search class.

### 4.5 One-step full-fibre saturation does not imply repeated saturation exactness

Independent reconstruction of the R021 search produced:

- `n=1`: 1 trial, 0 failures;
- `n=2`: 20 trials, 0 failures;
- `n=3`: 837 trials, 84 failures;
- total: 858 trials, 84 failures.

First fixture:

- `q=(0,0,1)`;
- `f=(0,2,0)`;
- start coarse fibre `0`.

One-step coarse image is `{0,1}`; exact two-step coarse image is `{0}`; repeated full-fibre saturation returns `{0,1}`.

This is the 3-state minimum in the quotient-saturation search class. It must not be confused with a different pointwise deterministic-descent minimality question.

### 4.6 Nonnegative path-count exactness

Let a fine transition be a nonnegative integer matrix `M`. For each fine source `x`, define the target-cell count signature

`kappa_M(x)[B]=sum_{y in B} M[x,y]`.

A quotient count row is well-defined exactly when this signature is constant inside every source cell. This is standard equitability/lumpability.

If every generator is equitable for the same partition, quotient count matrices multiply exactly for every finite word. This is the strong dynamically reusable count carrier.

Independent bounded check: all 96 equitable `3x3` binary matrices for partition `{0,1}|{2}` were paired in all 9,216 ordered ways; every product remained equitable and every quotient product was exact.

This is prior mathematics. Enterprise Math only needs the P021 specialization/typing consequence.

## 5. Uniform-fibre Stage-12 re-audit

For middle incidences `e_1,...,e_m`, predecessor/successor multiplicities `l_i,r_i`, define

`L=sum_i l_i`, `R=sum_i r_i`, `N=sum_i l_i*r_i`,

and

`Delta=m*N-L*R`.

Then

`Delta=sum_{i<j}(l_i-l_j)(r_i-r_j)`.

The historical Stage-12 theorem is correct:

- uniform `l` implies `Delta=0`;
- uniform `r` implies `Delta=0`;
- therefore one-sided uniformity implies `m*N=L*R`.

However, this proves only the current matched count. It does not prove that `(m,L,R)` is a closed carrier for another future join.

Uniformity is sufficient, not necessary. Example:

- `l=(0,0,1)`;
- `r=(0,2,1)`;
- both nonuniform;
- `m=3`, `L=1`, `R=3`, `N=1`, `Delta=0`.

Focused enumeration over lengths `1..4` and entries `0..3` checked 69,904 profile pairs:

- zero failures of the pair-difference identity for `Delta`;
- zero failures of `one side uniform => Delta=0`;
- 5,712 both-nonuniform pairs still had `Delta=0`.

Thus `Delta=0` is the sharper local criterion for the normalized current-count formula. Arbitrary-word count closure needs the stronger generatorwise equitability condition.

## 6. Boolean versus arithmetic matrix semantics

### Fine matrices

For exact fine Boolean adjacency matrices, Boolean matrix multiplication exactly represents relational composition.

For exact fine nonnegative path-count matrices, ordinary arithmetic multiplication exactly counts paths.

Positive support is a semiring homomorphism:

`supp(A*B)=supp(A) BooleanCompose supp(B)`.

Independent check: all 6,561 ordered pairs of `2x2` nonnegative matrices with entries `0..2` satisfied this identity.

### P021 cardinality shadows

P021 `T_ij=card(W_ij)` is not automatically either a Boolean quotient transition matrix or an N-semiring transition matrix. It aggregates witness pairs over a coarse direction class and forgets which exact middle incidence makes the next join possible.

For one middle class:

`N=sum_i l_i*r_i`.

Raw marginal multiplication gives

`L*R = N + sum_{i != j} l_i*r_j`.

Therefore raw arithmetic multiplication is exact only when every off-diagonal cross term vanishes. Stage-12 uniformity instead yields the normalized relation `m*N=L*R`; it is not ordinary count-matrix multiplication.

For coarse Boolean product, a fixed source-cell/middle-cell/target-cell triple is exact precisely when the set of exact middle states reached from the left intersects the set of exact middle states that can continue to the right whenever both sets are nonempty. For a reusable operation family, consume the stronger R018 support-congruence condition.

A set-valued support must never be silently treated as a count matrix: Boolean product records endpoint existence, arithmetic product records numbers of middle paths. Booleanizing a valid count matrix is safe only when multiplicity is no longer observable.

## 7. Uniformity kill pressure: negative and positive sides

Weak one-step cardinality uniformity is not composition-stable.

A 3-state minimum in the searched simple-relation class has every source with two `R` successors and one `S` successor, but composite support sizes `(1,2,2)`.

This does not contradict the positive regime above. If "uniformity" means full target-cell row-count equitability, then equitability is closed under multiplication and the quotient count algebra is composition-safe.

Therefore no blanket statement that "uniform fibres lose uniformity under composition" is justified. The correct distinction is:

`weak one-step marginal/cardinality uniformity` versus `generatorwise equitability/count congruence`.

## 8. Executable audit

No `TOOL_ASSUMPTION_MISMATCH` was found.

- `direction_transport_matrix` explicitly calls itself a cardinality shadow.
- `naive_matrix_product_entry` explicitly exists to expose the overcount no-go.
- `uniform_fiber_cross_multiplication_holds` rejects cases where neither side is uniform; it does not infer a false general law.
- `compose_two_path_witnesses` explicitly requires equality of the exact middle incidence.
- `transport_support` computes immediate zero/nonzero support only.
- `canonical_one_to_one_transport` is an adjacent support-permutation criterion, not a multi-step witness theorem.
- scalar collision/anisotropy tools are correct static statistics.
- `future_section` and `expansion_trajectory` are positive controls because they retain the exact fine Boolean support under the fixed relation.

The standalone R020 oracle compiles under Python and reproduces the bounded results frozen in the JSON evidence file. Repository CI/workflows were not queried because this is research-state evidence, not an integration gate.

## 9. P023 terminology routing

Recommended consumption:

### `FUNCTIONAL_SAFE`

Use only for deterministic functional descent through `q`.

### `FINE_SUPPORT_SAFE`

Use when the current carrier is exact fine set-valued support, or a lossless code for it, and future semantics are result-only relational/union-preserving. This is where R015/R016 branch deferral applies. It says nothing about multiplicity/provenance.

### `CELL_ONE_STEP_EXACT`

Use for fibrewise constancy of the coarse successor-support signature. Do not use the same term for mere existential full-fibre MAY lifting.

### `COMPOSITION_SAFE[semantic target, future language]`

Parameterize the term.

- Boolean support: generatorwise support congruence / R018 strong completeness.
- N-path counts: generatorwise equitability of count transitions.
- witness/provenance: identity-bearing future signatures must factor through the retained carrier.

A naked unparameterized `COMPOSITION_SAFE` risks mixing different semirings and observables.

## 10. Downstream routing

### P010/P011

`NO_NEW_MOTHER_TASK_REQUIRED`

Canonical theorem truth is unchanged. Fibre cardinalities, collision totals and collision spectra remain correct static statistics. The only correction is that they are not automatically next-step states.

### P018

`NO_FOUNDATIONAL_RETYPE_REQUIRED`

The frozen distinction among cell labels, full fine fibres, set-valued supports and future-refined point carriers remains sufficient. Keep an orthogonal observable tag where needed:

- `BOOL_SUPPORT`;
- `N_PATH_COUNT`;
- `WITNESS_PROVENANCE`.

Do not collapse them into one generic support type.

### R014 resource/Pareto accounting

Compare costs only inside the same semantic fibre:

`(future language, observable/carrier, required closure horizon)`.

A small cardinality shadow is not a cheaper equivalent of witness transport if it cannot answer the same future. Charge correlation metadata, fibre/equitability certificates, refinement/future-signature state and decoder/reconstruction when those are required.

### A3/A4

Keep the canonical A3-to-A4 bridge typed as Boolean support. Do not infer that a P021 cardinality shadow is an N-semiring current state merely because positive support of a valid nonnegative count matrix commutes with multiplication. Signed/cancellation-sensitive A3 quantities are outside that homomorphism.

No new A3/A4 mother theorem is required.

## 11. Prior art/rooting

The following are prior mathematics, not new Enterprise Math mother theorems:

- relation composition and relational direct image;
- Boolean semiring matrix semantics;
- nonnegative path-count matrix semantics;
- quotient factorization/congruence;
- equitable partitions/lumpability;
- bisimulation and behavioural/future equivalence;
- sufficient statistics/future signatures;
- automata/Myhill-Nerode-style distinguishability;
- coalgebraic quotient ideas.

The Enterprise-specific residue frozen here is only the declaration-level classification of which P021 witness/direction/cardinality reductions retain which observables under the declared future language.

## 12. Frozen decision summary

- canonical P021 theorem break: **NO**;
- static theorem preservation: **YES**;
- dynamic carrier scope narrowed: **YES**;
- tool assumption mismatch: **NONE FOUND**;
- P010/P011 new mother task: **NO_NEW_MOTHER_TASK_REQUIRED**;
- P023 terminology: typed as above;
- P018 foundational retype: **NO**;
- A3/A4 new mother theorem: **NO**;
- descendant task created: **NO**;
- canonical semantics modified: **NO**;
- CI/workflow queried: **NO**.

Final:

`P021_THEOREMS_STABLE / DYNAMIC_CARRIER_SCOPE_NARROWED / TOOL_AUDIT_COMPLETE / NOT_CANONICAL`

and

`P021_REAUDIT_COMPLETE / DYNAMIC_COMPRESSION_MATRIX_FROZEN / STATIC_ROWS_PRESERVED / COMPOSITION_ROWS_CLASSIFIED / NOT_CANONICAL`
