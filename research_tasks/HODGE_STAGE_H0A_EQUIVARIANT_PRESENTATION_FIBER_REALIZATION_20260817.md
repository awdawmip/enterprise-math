# HODGE Stage H0A — Equivariant Presentation-Fiber Realization

Date: `2026-08-17`
Status: `ACTIVE / DRIVER-ISSUED TASKBOOK`
Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Task ID: `RS-HODGE-H0A-EQUIVARIANT-PRESENTATION-FIBER-REALIZATION`
identity_policy: `AUTO_RESOLVE_OR_ALLOCATE`
identity_lane: `HODGE-H0A-EQUIVARIANT-REALIZATION`
owner branch: `research/hodge-h0a-equivariant-presentation-fiber`
control branch: `research/hodge-special-control-plane`

## 0. Mission

H0 froze an honest negative qualification result:

`H0_PARTIAL_R1_ONLY_REDUNDANT_ENRICHMENT`

Frozen H0 owner head:

`b30bd1f662597f1819d7e96934bca2069036dcf4`

H0 established only that the audited **single-placement** Enterprise candidate families did not reach R2. It did **not** prove a universal no-go for Enterprise realizations.

The load-bearing correction for H0A is:

> Do not require an algebraic variety to choose one preferred Enterprise chart/origin/grid/precision placement. Replace the single-placement ansatz by an equivariant family of all admissible algebraically sourced Enterprise placements, together with exact transition/collapse/resolve data between presentations.

H0A asks whether this family contains an Enterprise-specific, presentation-independent invariant that survives quotienting by mere reparameterization and cannot factor through the classical/algebraic readout.

Hard target:

`ENTERPRISE_EQUIVARIANT_REALIZATION_REACHES_R2`

Do **not** start H1 cohomology unless this target is established.

A second R1 result is valid and must be frozen if obtained.

---

## 1. Frozen authority / inputs

Read only the smallest sufficient packet, then work.

Mandatory:

1. `AGENTS.md`
2. `docs/GITHUB_INTERACTION_BUDGET.md`
3. `research_common_surface.json`
4. `driver_handoffs/HODGE_SPECIAL_DRIVER_HANDOFF_20260817.md`
5. `driver_handoffs/HODGE_SPECIAL_DRIVER_PI_GEOMETRY_ADDENDUM_20260817.md`
6. `research_results/HODGE_H0_SEMANTIC_CHECKPOINT.md` at frozen head `b30bd1f662597f1819d7e96934bca2069036dcf4`
7. `research_results/HODGE_H0_REALIZATION_CANDIDATE_REGISTRY.json` at the same frozen head
8. `research_results/HODGE_H0_PRESENTATION_AUTOMORPHISM_GATE.json` at the same frozen head
9. `research_results/HODGE_H0_NONFACTORIZATION_WITNESS_REGISTRY.json` at the same frozen head
10. `native_semantics_admissibility.json`
11. `FOUNDATIONAL_LOGIC.md` / `foundational_logic.json` only as needed for native-vs-derived typing

H0 frozen result is read-only. Do not rewrite its disposition.

R059D Stage AD may be consulted only as a design precedent for **retaining resolve ambiguity instead of selecting a preferred resolve**. Its circle data, finite counts, or π content are not Hodge evidence and must not be imported as generator data.

---

## 2. Driver correction to the H0 search space

H0 correctly proved that a coordinate-anchored Enterprise placement on `P^1` cannot simply claim canonicity: `PGL_2(C)` moves any chosen finite anchor/chart/origin.

H0A must not fight this by searching for a magical fixed anchor.

Instead distinguish:

- **fixed invariance**: one placement is literally preserved by every automorphism;
- **equivariance/naturality**: automorphisms transport one admissible placement to another inside a canonically defined total family.

The second is sufficient in mathematics to define a natural object; a canonical object need not contain a preferred fixed point.

Therefore H0A must test the stronger and more appropriate possibility:

> the Enterprise realization is not one grid on `X`, but a presentation-equivariant family/fibration/groupoid of Enterprise carriers whose transition structure itself may contain the non-factorizing information.

Groupoids, fibrations, stacks, descent, Čech constructions, pseudofunctors and moduli language are **prior-art formalisms**. Using them earns no Enterprise novelty by itself. Any Enterprise credit must come from the exact Enterprise carrier/transition/collapse/resolve structure placed inside that formalism.

---

## 3. Required construction schema

For each toy algebraic source `X`, define a declared algebraic presentation groupoid or the strongest exact finite surrogate:

`Pres(X)`.

Objects `p in Pres(X)` are permitted algebraic presentations of `X` (for example declared homogeneous/affine coordinate presentations or algebraically equivalent presentations used only as source data).

Morphisms `alpha : p -> q` are declared algebraic isomorphisms/presentation changes.

For each presentation `p`, attempt to construct an Enterprise carrier:

`E_p(X)`

from:

- the algebraic presentation data;
- current Enterprise coordinate/precision/collapse primitives;
- explicitly typed derived operational semantics.

Declare comparison/readout:

`U_p : E_p(X) -> C_p(X)`

where `C_p(X)` is the declared algebraic/classical comparison carrier. `U_p` is a checker bridge, not an Enterprise generator.

For each `alpha : p -> q`, construct the strongest exact admissible transition object:

`T_alpha : E_p(X) -> E_q(X)`

or, if deterministic transport is impossible without illicit re-quantization,

`T_alpha subseteq E_p(X) x E_q(X)`

as an exact relation/correspondence.

Do not force a function where the native semantics is genuinely multivalued.

The total candidate realization may be expressed as an equivariant family / Grothendieck-style total category / groupoid / fibration, but the formalism must be labeled prior art.

---

## 4. No-preferred-presentation gate

A candidate may not choose a privileged chart, origin, infinity point, factor ordering, Euclidean frame, or Enterprise grid orientation and then call it canonical.

Instead the total construction must satisfy one of:

1. all admissible presentations are included and source automorphisms act by exact transport; or
2. a proved cofinal/subpresentation family is used with an independence theorem; or
3. another exact natural-equivalence construction is supplied.

For `P^1`, inversion `z -> 1/z`, translation `z -> z+1`, and the automorphism `sigma([X:Y])=[Y:X]` must be explicit stress tests.

For `P^1 x P^1`, factor swap must be tested if product structure is claimed.

A merely chosen finite subset of presentations does not prove global canonicity; finite tests only certify the declared finite surrogate.

---

## 5. Transition/coherence gate

For exact presentation morphisms, test:

`T_id`

and

`T_(beta o alpha)` versus `T_beta o T_alpha`.

If they agree exactly in the declared category, record strict functoriality.

If they agree only up to declared equivalence, state the equivalence/coherence data explicitly.

If they disagree, define the exact residual/defect without interpreting it prematurely, for example:

`Delta_(beta,alpha) = T_(beta o alpha) triangle (T_beta o T_alpha)`

for finite relational carriers, or the appropriate exact typed analogue.

A nonzero `Delta` is **not automatically a discovery**. It may simply be quantization/re-placement inconsistency.

To count as Enterprise structure, a residual must pass all of:

- exact reproducibility;
- relabeling invariance/equivariance;
- independence from arbitrary tie-breaking;
- stability under algebraically equivalent presentation refinements or a proved transformation law;
- Enterprise-specific origin rather than a known algebraic invariant relabeled;
- theorem-relevant consumability by a later chain/cycle construction.

Otherwise classify it as:

`INCOHERENT_REQUANTIZATION_ARTIFACT`.

---

## 6. Closed-loop / automorphism transport test

Study presentation loops

`p0 -> p1 -> ... -> pn = p0`

including loops whose composite algebraic map is identity and loops representing nontrivial source automorphisms.

Possible observables include, but are not limited to:

- transition-fiber cardinality spectrum;
- branch/recoalescence ambiguity spectrum;
- conjugacy class of a transport relation;
- exact support residual after a loop;
- composition-defect spectrum;
- a choice-independent obstruction to strict descent.

Do not call any of these `holonomy`, `curvature`, `monodromy`, `cohomology`, or `Hodge` unless the corresponding mathematical structure is actually defined.

For an identity loop, an unexplained nonidentity result is a defect, not success.

It can become admissible information only if H0A proves that it defines a coherent equivalence-class invariant of the Enterprise family rather than a failure of implementation/presentation consistency.

---

## 7. Exact R2 non-factorization gate after quotienting presentation metadata

H0A passes only if it produces an exact witness **after removing mere presentation labels**.

Required certificate:

1. define the total equivariant Enterprise candidate `E^eq(X)`;
2. define the declared comparison/forgetful map `U^eq_X`;
3. quotient or otherwise neutralize pure presentation-name/chart-label information;
4. exhibit two admissible Enterprise states/classes `e1 != e2` with
   `U^eq_X(e1) = U^eq_X(e2)`;
5. define an Enterprise-specific observable/operation/constraint `A_E` with
   `A_E(e1) != A_E(e2)`;
6. prove `A_E` does not factor through `U^eq_X` on the declared carrier;
7. prove the distinction survives the relevant source-presentation equivalence/automorphism action;
8. state exactly how a future H1 chain/cycle construction could consume the distinction.

If the only surviving data is:

- which chart was used;
- which arbitrary grid offset was used;
- a torsor of choices with no theorem-relevant invariant;
- generic relation metadata already determined by the algebraic source;
- a known local-ring/jet/valuation/tropical invariant;

then the correct result remains R1 or prior-art control.

---

## 8. Enterprise-specific origin gate

H0 already identified genuine nontrivial prior-art controls: formal neighborhoods, jets, local algebra, ramification multiplicity, tropical/non-Archimedean realizations.

H0A must continue to use them as controls only.

A candidate does not become Enterprise-specific merely because it is represented in Enterprise coordinates.

For every surviving observable record:

- exact Enterprise primitive(s) that generate it;
- exact algebraic source data consumed;
- whether the same invariant already exists before Enterprise realization;
- whether the Enterprise construction only computes/re-encodes that prior invariant;
- strongest novelty status.

If a known invariant is merely recovered, record:

`PRIOR_ART_RECOVERY / NO_ENTERPRISE_R2_CREDIT`.

---

## 9. Toy registry

Minimum exact registry:

1. point;
2. `P^1_C` with at least presentations `z`, `1/z`, `z+1`;
3. `P^1_C x P^1_C` with factor swap;
4. one nontrivial algebraic morphism `P^1 -> P^1`;
5. identity and nontrivial automorphism loops;
6. at least one finite exact precision/collapse carrier where all transition relations can be exhaustively inspected.

Use exact symbolic/integer/rational/algebraic arithmetic wherever possible.

No floating Euclidean distance/angle, no classical circle, no classical π, no numerical Hodge targets.

Finite computation proves only the finite declared carrier unless accompanied by theorem.

---

## 10. Required negative and positive controls

Negative controls:

- arbitrary chart coloring transported equivariantly;
- arbitrary grid offset family;
- all-presentations family whose quotient contains no extra theorem-relevant invariant;
- deliberately inconsistent re-quantization producing fake composition defect.

These must not pass R2.

Positive prior-art controls:

- intrinsic formal-neighborhood/jet tower;
- one valuation/tropical or other established nontrivial realization mechanism if useful.

These should show what a genuine nontrivial realization looks like while receiving zero Enterprise novelty credit.

---

## 11. H0A classification

Freeze exactly one strongest disposition:

### `H0A_R1_EQUIVARIANT_FAMILY_STILL_REDUNDANT`

The all-presentations/equivariant construction is coherent but every theorem-relevant invariant factors through classical/algebraic data or pure presentation metadata.

Consequence: H1 remains inadmissible. The next search must move away from presentation-derived Enterprise carriers entirely.

### `H0A_REJECT_INCOHERENT_TRANSITION_ARTIFACT`

Apparent non-factorization comes only from re-quantization/tie-breaking/composition inconsistency and fails coherence/choice-independence.

Consequence: H1 remains inadmissible.

### `H0A_R2_EQUIVARIANT_ENTERPRISE_REALIZATION_FOUND`

An exact Enterprise-specific non-factorization witness survives presentation quotient/equivariance and all hard gates.

Consequence: Driver may accept H0 as qualified and issue H1.

### `H0A_R3_HODGE_RELEVANT_EQUIVARIANT_REALIZATION_CANDIDATE`

R2 plus an exact, non-target-leaking chain/cycle consumption interface is already visible.

This still does **not** prove Hodge and does not authorize skipping H1/H2/H3/H4/H5.

---

## 12. H1 entry firewall

Do not construct a full chain/cochain complex in H0A.

Only if R2/R3 passes, freeze an H1 entry contract specifying:

- Enterprise chain generator source;
- boundary incidence source;
- orientation/relabeling rule;
- proof obligation `partial_E^2 = 0`;
- cochain/coboundary source;
- comparison map;
- choice/precision dependencies;
- why the construction is not singular/cellular/Čech chains merely relabeled.

No automatic H1 start.

---

## 13. Target-leakage / Hodge firewall

Forbidden generators:

- classical Hodge decomposition;
- Hodge numbers;
- classical algebraic-cycle answers;
- harmonic forms/Kähler metric;
- singular/cellular/Čech cohomology as an Enterprise generator;
- classical equidistant circle;
- standard real π;
- a prior-art stack/sheaf/tropical object renamed Enterprise;
- known ramification/multiplicity/jet data counted as Enterprise novelty.

External Hodge theory remains benchmark/type discipline only.

The target remains the rational Hodge conjecture; no weaker discrete statement may be called Hodge.

---

## 14. Required artifacts

At minimum produce:

1. `research_results/HODGE_H0A_PRESENTATION_GROUPOID_SPEC.json`
2. `research_results/HODGE_H0A_EQUIVARIANT_ENTERPRISE_CARRIER_REGISTRY.json`
3. `research_results/HODGE_H0A_TRANSITION_RELATION_REGISTRY.json`
4. `research_results/HODGE_H0A_COHERENCE_COMPOSITION_LEDGER.json`
5. `research_results/HODGE_H0A_LOOP_TRANSPORT_REGISTRY.json`
6. `research_results/HODGE_H0A_PRESENTATION_QUOTIENT_NONFACTORIZATION.json`
7. `research_results/HODGE_H0A_PRIOR_ART_NOVELTY_LEDGER.json`
8. `research_results/HODGE_H0A_TARGET_LEAKAGE_LEDGER.json`
9. `research_results/HODGE_H0A_H1_ENTRY_CONTRACT.json`
10. `research_results/HODGE_H0A_CLASSIFICATION.json`
11. `research_results/HODGE_H0A_SEMANTIC_CHECKPOINT.md`
12. one deterministic checker + checker output
13. manifest with SHA-256 digests

A checker PASS means protocol/artifact consistency only; it must not be worded as if H0A mathematical R2 passed unless the classification actually says so.

---

## 15. Completion estimates and advancement vector

Before H0A:

- Enterprise coordinate foundation for current plane semantics: `~95%`
- Hodge conceptual route: `~14%`
- Enterprise realization qualification: `~45%` (H0 negative boundary mapped)
- Enterprise cohomology: `0%`
- native Hodge-type structure: `0%`
- algebraic lifting theorem: `0%`
- unknown Hodge attack readiness: `0%`

If H0A reaches R2:

- Hodge conceptual route: `~22%`
- Enterprise realization qualification: `~80%`
- H1 readiness: `QUALIFIED`

If H0A remains R1:

- Hodge conceptual route still advances through a stronger no-go boundary;
- Enterprise realization qualification becomes `~65% negative-map coverage`;
- H1 remains `NOT_ADMISSIBLE`;
- next route must seek an Enterprise structure generated from algebraic relations themselves rather than presentation/placement families.

Advancement vector:

`realization-test +30 / presentation-equivariance +25 / nonfactorization +25 / prior-art-separation +10 / H1-readiness +10 / unknown-hodge +0`

---

## 16. Research discipline

- Preserve H0 as frozen negative evidence.
- No refit-by-vocabulary: changing `grid` to `groupoid` is not success.
- No ad hoc operator added solely to create non-factorization.
- No classical Hodge target leakage.
- No finite enumeration promoted to universal theorem.
- No deletion of failed routes.
- Source repo remains remote-silent between semantic checkpoints.
- No routine CI/workflow status reads.
- Publish one coherent semantic checkpoint at completion.

Final return target:

`EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
