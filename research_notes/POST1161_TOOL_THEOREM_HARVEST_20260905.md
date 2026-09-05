# Post-#1161 Tool + Theorem Harvest

Status: `FREE_RESEARCH_HARVEST / MAIN-BACKED-CANDIDATE / NOT FOUNDATION / NOT WORKING_TRUTH`
Date: `2026-09-05`
Researcher: `EM-FREE-G61R8`
Source synthesis: `research_notes/FREE_RESEARCH_POST1161_AGM_RETURN_MEMORY_SYNTHESIS_20260904.md`

## 1. Harvest verdict

The post-#1161 successor does **not** justify a new top-level toolbox family.

The reusable structure is a composition/extension of current families:

- `T0_BRC`: concrete two-witness multipath provenance and positive branch mass;
- `T6_OPERATION_SAFE_QUOTIENT`: observer-relative predictive quotient semantics;
- `T5_PRECISION_REFINEMENT`: cross-horizon precision projections and naturality;
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: orbit/stabilizer and equivariant-section obstruction;
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`: same-observation future-collision capacity lower bounds.

Freeze the reuse resolution:

`T0/recent.r062 = REUSE_APPLIED`.

`T6 predictive quotient = EXTEND_EXISTING_TOOL` because the new exact carrier is an unbounded one-counter process with a closed finite-horizon quotient tower and horizon-changing graded kernel, not one fixed finite state machine.

`T5 graded precision = COMPOSE_APPLIED`.

`T7 finite symmetry + equivariant_section = REUSE_APPLIED`; no new section tool is created.

`T4 fiber capacity = COMPOSE_APPLIED`; no new capacity family is created.

## 2. Extracted global subtool candidate

### `brc.binary_first_return_predictive_rg`

Executable:

`src/enterprise_math/brc_binary_first_return.py`

Tests:

`tests/test_brc_binary_first_return.py`

Reusable API:

- `first_balance_return_count(n)`;
- `first_return_mass(n)`;
- `signed_memory(a,b)`;
- `swap_memory(z)`;
- `unlabeled_memory(z)`;
- `first_hit_count(d,m)` / `first_hit_mass(d,m)`;
- `predictive_signature(d,h)`;
- `quotient_label(h,d)` / `quotient_states(h)`;
- `graded_kernel(h,state)`;
- `project_label(high,low,state)`;
- `counter_factorization_holds(h,d)`;
- `graded_naturality_holds(high,low,state)`;
- `first_return_polynomial(s,N)`;
- `renewal_coefficient_identity(n)`.

Core theorem interface:

\[
R_{2n}^{\rm first}=2C_{n-1},
\qquad
f_n=\frac{C_{n-1}}{2^{2n-1}},
\]

\[
F(2-F)=s^2,
\]

\[
\mathcal M_D=\mathbb Z^D/\mathbb Z\mathbf 1,
\qquad
\mathcal M_D/S_2\cong\mathbb N_0,
\]

\[
Q_h=\{0,1,\ldots,h,\mathrm{FAR}\},
\qquad |Q_h|=h+2,
\]

\[
q_{h-1}K=K_hq_h,
\]

and for `1<=k<=h`,

\[
\pi_{h-1,k-1}K_h=K_k\pi_{h,k}.
\]

Hard boundary:

This is N1 branch/path memory. The absolute quotient is adequate for unlabeled positive first-return mass but erases the sign of the branch majority. Do not reconstruct signed/amplitude information after positive recoalescence and do not call the memory an instantaneous native/G0 Cell coordinate without a separate native definability theorem.

## 3. Reused symmetry operator, not a new tool

### `symmetry.k4_diamond_orientation_bundle`

Use existing:

- `src/enterprise_math/finite_symmetry.py`;
- `src/enterprise_math/equivariant_section.py`.

Domain evidence:

`scripts/check_free_research_agm_s4_diamond_memory_bundle.py`.

The 24 ordered-witness states project equivariantly to 12 unordered K4/FCC diamonds. Each diamond stabilizer is `C2` and its nontrivial element swaps the two lifts. The existing T7 theorem therefore gives a local fixed-lift obstruction and hence zero global equivariant sections.

No new equivariant-section tool is needed.

## 4. AGM domain facade

### `agm.first_return_rg_certificate`

Executable facade:

`src/enterprise_math/agm_first_return_rg.py`

Tests:

`tests/test_agm_first_return_rg.py`

It exposes only domain-specific consequences of the generic binary-return tool:

- finite return mass `F_N(s)`;
- rational shape update `T_N(s)=F_N/(2-F_N)`;
- one-shell map `T_1=s^2/(4-s^2)`;
- finite geometric lower-channel approximation `H(1-F_N)/2`;
- quadratic-universality bounds;
- shape truncation error envelope;
- standard-orbit adaptive return depth;
- K4/S4 scalar state cost `24N+12`.

This facade does not own the binary-return theorem and does not identify the endogenous completion with classical `pi`.

## 5. Integer whole-trajectory / resource operators

Keep the already committed deterministic scripts as domain operators rather than forcing them into a new global family:

- `scripts/check_free_research_agm_two_index_interval_certificate.py`;
- `scripts/check_free_research_agm_return_depth_pareto.py`;
- `scripts/check_free_research_agm_five_step_lexicographic_pareto.py`.

They compose T5 precision semantics with the first-return domain facade.

Strongest fixed-compiler results:

- four outer steps cannot certify a 256-bit completion bracket;
- five outer steps are therefore minimal for that target;
- within the fixed `B=640`, five-step, `N_i>=1`, cost `sum(24N_i+12)` compiler:
  - width target optimum: `(50,18,8,3,1)`, total cost `1980`;
  - common 256-bit dyadic cell optimum: `(51,18,8,3,1)`, total cost `2004`.

These are finite domain certificates, not universal algorithmic complexity lower bounds.

## 6. Extracted theorem routing

Machine-readable ledger:

`research_notes/POST1161_BINARY_RETURN_THEOREM_LEDGER_20260905.json`.

It contains:

- `BFR-T01..T08`: reusable binary first-return / memory / predictive theorems;
- `BFR-S4-T01..T03`: K4/FCC S4 application theorems;
- `AGMR-T01..T06`: AGM-domain theorems/certificates;
- `BFR-N01..N04`, `AGMR-N01`: information-loss and promotion boundaries.

Do not add these IDs to the Foundation theorem ledger merely because they are main-backed. Foundation/Working-Truth admission remains a separate Driver/Steward action.

## 7. BRC observer audit

Population:

all two-witness path histories; do not filter histories by parity or apparent triviality before first-return classification.

Rich carrier before compression:

branch provenance + signed multiplicity difference.

Positive observer:

first-return shell count/mass by future length.

Safe scalar compression:

\[
z\mapsto |z|
\]

because the declared positive observer is invariant under witness swap.

Erased information:

which witness is currently the majority branch.

Future-operation lease:

all unlabeled first-hit/first-return mass operations through the declared horizon are safe on `Q_h`; branch-resolved labeled future operations are not safe on the absolute quotient.

## 8. Next admission boundary

The extracted code and research theorem interface are ready for reuse and independent audit. The next control-plane question is admission strength, not more AGM algebra:

`FREE_RESEARCH_HARVEST -> DRIVER/STEWARD AUDIT -> optional toolbox/Foundation promotion`.

Until that audit occurs:

`MAIN_BACKED_RESEARCH_RESULT != FOUNDATION_THEOREM`.

`EXECUTABLE_RESEARCH_SUBTOOL != CANONICAL_GLOBAL_TOOL`.
