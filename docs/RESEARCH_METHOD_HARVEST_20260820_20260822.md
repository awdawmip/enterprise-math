# Research Method Harvest — current executable surface with priority window 2026-08-20..2026-08-22

Status: `DRIVER HARVEST COMPLETE / ROUTING UPDATE`
Date: `2026-08-22`
Driver-ID: `EM-DVR-ZX1UEJ`
Priority source window: `2026-08-20..2026-08-22`
Current source baseline at harvest start: `71f139ea52f59e3ed0f2895ae107b815d6dea8f6`
Machine inventory: `research_method_inventory.json`
Global router: `enterprise_toolbox_registry.json`

## 1. Scope and standard

The purpose is not to rename every theorem as a tool. The harvest asks which results already expose a reusable procedure, certificate, invariant, quotient compiler, finite transform or diagnostic likely to be reinvented in another route.

The audit used two complementary surfaces:

1. recent route/Driver-acceptance history, with priority on 20–22 August 2026;
2. the entire current executable Python surface under `src/enterprise_math`, searched at module/API level for general-purpose mechanisms left under historical route names.

Archive-only superseded prose is not promoted merely because it contains an algorithmic phrase. Exact owners remain authoritative, and `tools/enterprise_toolbox.py` scans all current executable modules dynamically so an uncurated current helper remains discoverable.

The harvest remains live during its integration window: a concurrently accepted research return is classified before final merge rather than being excluded merely because it landed after the initial baseline snapshot.

## 2. Main finding

The project did not primarily lack tools. It lacked **cross-route ownership and lookup discipline**.

Several mechanisms had already been implemented multiple ways or under route-local names:

- future-preserving quotient refinement;
- finite precision projection/detail/carry;
- relation collision/observable signatures;
- box/interval finite certificates;
- defect transport and loop/holonomy checks.

The new routing rule therefore prefers **family consolidation** over creating more names.

## 3. Harvested global families

### T5 — Integer Precision / Refinement Calculus

Existing owners:

- `src/enterprise_math/precision.py`;
- `src/enterprise_math/graded_precision.py`;
- related precision-system/proof modules.

Reusable core:

- exact coarse/fine projection and bounded detail;
- exact recomposition;
- nested refinement identity;
- addition carry / subtraction borrow;
- precision-chain decomposition;
- degree-aware transport and nonlinear projection defects.

Decision:

`HARVESTED_PREEXISTING_DERIVED_TOOL_FAMILY`.

Do not create a new tool merely because a later route calls the detail a residue, digit, hidden state or finite error.

### T6 — Operation-Safe Quotient / Predictive Refinement Calculus

Existing owners:

- `predictive_quotient.py`;
- `composition_safe_collapse.py`;
- `operation_quotient.py`;
- `partial_operation_quotient.py`;
- `safe_operation_algebra.py`.

These all implement parts of the same reusable question:

> Given declared observations/operations, what is the coarsest quotient/refinement that preserves the required behavior, and how do we certify failure of descent?

Decision:

`HARVESTED_PREEXISTING_DERIVED_TOOL_FAMILY`.

Future quotient/collapse work must check T6 before inventing another predictive-state equivalence.

### T7 — Finite Symmetry / Orbit / Equivariance Calculus

Recent trigger:

- R064 Phase A classified all component-only `S3`-equivariant maps and used orbit reduction;
- FQ009 uses orientation torsor/stabilizer structure;
- the fresh resolution-glue no-go uses the absence of an invariant target choice under relabeling.

The common method was not previously exposed as a shared callable. It is now toolized in:

`src/enterprise_math/finite_symmetry.py`.

Reusable operations:

- finite group-action validation;
- orbit partition;
- stabilizer;
- global fixed points;
- canonical-choice obstruction;
- exact equivariant-map counting/enumeration from orbit representatives.

Decision:

`HARVESTED_AND_TOOLIZED`.

R064's `11`-orbit result remains scoped to its declared pair-local reduct; the generic tool does not universalize that number.

### T8 — Relation Observable / Spectrum Calculus

Existing owners:

- `relation_observable_signature.py`;
- `relational_spectrum.py`;
- `relation_observable_composition.py`;
- `relation_future_powerset.py`;
- `weighted_relation_field.py`;
- `relation_lattice.py`.

The shared mechanism distinguishes:

`RAW RELATION BRANCHING`

from

`OBSERVABLE NONDETERMINISM`

from

`QUOTIENT SAFETY`,

and supplies collision/overlap spectra and finite relation invariants.

Decision:

`HARVESTED_PREEXISTING_DERIVED_TOOL_FAMILY`.

This family sits upstream of T4 when a fiber/observation must first be constructed from relation-valued semantics.

### T9 — Holonomy / Cocycle / Gluing-Obstruction Calculus

Existing/recent owners:

- `precision_holonomy.py`;
- `precision_signed_holonomy.py`;
- `p023_borrow_cocycle.py`;
- `material_loop_identity.py`;
- R063 Stage 4 three-sector C4 globalization result.

Reusable pattern:

`LOCAL TRANSPORTS -> COMPOSE AROUND LOOP -> DEFECT/HOLONOMY -> STRICT GLUING VERDICT`.

R063 Stage 4 supplies a particularly clear recent instance: the local C4 process has unavoidable odd loop holonomy, so a strict global product cannot trivialize all charts; a torsor/groupoid or quotient survivor remains.

Decision:

`HARVESTED_PREEXISTING_PLUS_RECENT_DERIVED_TOOL_FAMILY`.

Nonzero holonomy does not by itself choose the repaired global object.

## 4. Existing families and specializations clarified by the harvest

### T2 absorbs old box Helly machinery

`box_collapse.py` already implemented integer-box Helly-2 and compact facet witnesses before the new abstract finite-certificate task. It is now explicitly a T2 specialization.

No future route should present “pairwise boxes imply global intersection” as a new Enterprise tool.

### T4 does not own quotient construction

T4 assumes a meaningful observation/fiber relation. If the quotient itself is being designed, T6 or T8 is normally the earlier tool.

Typical composition:

`T6/T8 -> declared quotient/fiber -> T4 capacity/compression`.

This prevents T4 from silently inventing the semantic observation it then counts.

### Prime Toolkit remains a domain facade

`prime_toolkit.py` plus `prime_method_inventory.json` already form a mature specialized tool library with provenance/status preservation.

It remains `D1_PRIME_TOOLKIT`, not a replacement for the global families. Prime routes should reuse global T1/T5/T6 methods where appropriate rather than copying them into new prime-specific machinery.

## 5. Priority-window route harvest

### R061 — native line program

Harvest classification:

- native line trace formula -> `DOMAIN_OPERATOR`;
- arbitrary-point directed gauge -> `DOMAIN_OPERATOR`;
- bidirectional segment spectrum -> `DOMAIN_OPERATOR`.

These are reusable current mathematical objects/operators, but not general cross-domain tool families. They are indexed so new line research can find them without promoting line ontology into generic tooling.

### R062 — BRC multipath bridge

Harvest classification:

`GLOBAL_SUBTOOL -> T0_BRC`.

The `PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC` bridge is a BRC projection/enrichment interface, not a separate new global family.

### R063 — path root and C4 process globalization

Harvest classification:

- path-valued root decomposition -> `DOMAIN_OPERATOR`, routed through path/fiber tools when reused;
- Stage-4 loop/gluing classification -> `GLOBAL_SUBTOOL -> T9`.

The route-independent phase-orbit quotient is a specific survivor of the C4 application; the reusable mechanism is the holonomy/gluing diagnostic, not the number `4` or the 12-state carrier.

### R064 — N0 component relation / event lift gap

Harvest classification:

`GLOBAL_SUBTOOL -> T7` for the finite `S3` equivariant-map/orbit method.

The component-complement theorem itself remains an R064 result. The shared tool is the symmetry/orbit/equivariance calculus used to classify such laws.

### FQ008 — transverse scalar independence

Harvest classification:

`GLOBAL_SUBTOOL -> T1` for the mixed finite-difference separability diagnostic.

The Foundation question's semantic status is not changed by this indexing. Tool routing does not make the proposed Foundation interface canonical.

### FQ009 — orientation torsor

Harvest classification:

`GLOBAL_SUBTOOL -> T7` for orbit/stabilizer/torsor analysis.

Again, indexing a method does not promote its Foundation conclusion.

### CBRC F0 — signed recoalescence forward derivation

This result was accepted concurrently during the harvest window at Driver review commit:

`d4c7dd11287b313360be9e53a5bad5dfd7f1b502`.

Harvest classification:

- conservative signed group completion of the nonnegative typed Path-formal occurrence monoid -> `GLOBAL_SUBTOOL -> T0_BRC`;
- sign-valued elementary-diamond / gauge diagnostic for the accepted minimal signed carrier -> `GLOBAL_SUBTOOL -> T9`;
- scalar-readout underdetermination -> `RESULT_ONLY`;
- the minimal-carrier integer-linear branch-mixing no-go is retained as a scope boundary on the T9 entry, not generalized to richer carriers.

The group-completion and finite gauge mathematics are standard/general. Tool value is the exact typed Enterprise interface and reuse boundary; no generic novelty claim is made.

The subsequently issued CBRC F1 is an explicit blind-forward task. Under the new invocation policy its current-tool catalog remains hidden until the taskbook's raw F1 packet freeze, then post-freeze tool dedup is mandatory before method-novelty claims.

### LSR-N2

Harvest classification:

`CANDIDATE_NOT_TOOL -> T4 owner already exists`.

The maximal line-safe kernel/cardinality proposal remains under its independent-replication gate. Generic kernel/fiber machinery is already available, so creating a separate LSR tool family would duplicate T4/T6 and risk candidate laundering.

### resolution-glue symmetry no-go

Harvest classification:

`GLOBAL_SUBTOOL -> T7` as a canonical-choice obstruction pattern.

The exact project no-go remains parked; the generic method is simply the finite group-action fixed-point test.

### 22-August discrete-geometry tool-discovery quartet

Driver classifications are preserved:

- valuation/Ehrhart/Brion mechanism -> T1;
- Helly/Radon certificate mechanism -> T2;
- oriented graphic circuit mechanism -> T3;
- geometry-of-numbers fiber layer -> T4 with novelty downgrade.

## 6. Current-source older-method harvest

The executable scan also exposed mature generic machinery that predated the priority window:

- `safe_operation_algebra` / quotient congruence -> T6;
- finite predictive partition compilers -> T6;
- precision carry/detail/graded transport -> T5;
- relation future signatures and spectra -> T8;
- precision/cocycle loop defects -> T9;
- integer box Helly certificates -> T2;
- Prime Toolkit -> D1 domain facade.

These are now first-class lookup targets even though their original research routes are older.

## 7. What was deliberately not converted into tools

The harvest rejects automatic toolification of:

- one-off theorem values;
- Foundation candidates still under audit/replication;
- historical carrier presentations superseded by current semantics;
- domain definitions whose reuse does not cross problem families;
- implementation artifacts with no mathematical input/output contract;
- a renamed special case of an already registered tool.

This is necessary to keep the toolbox smaller than the research archive.

## 8. Future-proof closure

This harvest is not intended to be repeated manually after every burst of work.

The new universal policy requires every accepted future research return to receive a method-harvest classification. When routing value changes, the Driver/Steward updates the shared inventory immediately.

At task start, the lookup flows in the opposite direction:

`problem -> tool family -> harvested method -> current executable source`.

Thus the project now has both halves of the loop:

`RESEARCH -> TOOL HARVEST`

and

`NEW RESEARCH -> TOOL REUSE GATE`.
