# Enterprise Math Concept Lineage Matrix

Status: `PROPOSED / ACTIVE AUDIT`  
Snapshot date: `2026-08-09`  
Purpose: identify when independently named research routes are mathematically the same, one strictly generalizes another, one is a specialization/application, or two similarly named objects are actually independent.

This document is an architecture/audit map. It does not renumber canonical theorems or promote WIP results into `FOUNDATIONS`.

## 1. Relationship labels

Use these labels before consolidating routes:

- `SAME_MOTHER`: the two statements encode the same mathematical theorem after an explicit change of notation/coordinates/horizon encoding. Maintain one reusable mother statement and keep source-specific corollaries/provenance.
- `STRICT_GENERALIZATION`: the target removes assumptions, enlarges the operation language, or covers strictly more objects while retaining the source statement as a theorem-level specialization.
- `SPECIALIZATION`: a domain-specific instance of a more general theorem. Keep it when it carries useful arithmetic, geometric, physical, or executable content.
- `GENERATOR`: one structure constructs examples/inputs for another, but is not itself the same theory.
- `COMPOSABLE_INDEPENDENT`: distinct mathematical objects that can be connected by a declared map or theorem but must not be merged by vocabulary alone.
- `CONFLICT / NEGATIVE_BOUNDARY`: one route proves a tempting stronger identification or monotonicity false. Preserve the counterexample as an architectural boundary.
- `NAME_COLLISION_ONLY`: historical naming overlap without mathematical ownership.

A route is not consolidated merely because the same words occur in both branches.

## 2. Precision / quotient / future-compatibility lineage

| Source result | Target/general home | Relationship | Audit conclusion |
|---|---|---|---|
| P018 T151–T152/T159: observation kernel is dynamically closed iff the fine endomap descends to autonomous coarse dynamics | P023 T01: fiber constancy iff a chosen future observable factors through a quotient | `SPECIALIZATION` | P018 is the precision/semiconjugacy specialization with `q=O` and future observable `O∘F`. P023 owns the general factorization gate; P018 keeps precision-time semantics, semiconjugacy, defects, and observational interpretation. |
| P018 T160–T168: finite unary predictive refinement by future observation signatures | P023 T03–T07: finite deterministic future-compatible quotient refinement | `SAME_MOTHER` | The recursions and theorem package coincide in the finite unary case: monotone refinement, `N-c0` stabilization, depth/horizon semantics, compatible stable quotient, and coarsest compatible refinement. Do not maintain two independently growing general unary theorem families. |
| P018 T160–T168 / P023 T03–T07 | P023 T10–T14 finite operation-family closure | `STRICT_GENERALIZATION` | P023 replaces one endomap by a finite named family and replaces one future trajectory by all operation words. P018 C17 had explicitly left this multi-operation case open. |
| P023 T02 coarsest one-step repair `(q,h)` | P018 predictive closure | `COMPOSABLE_INDEPENDENT` | T02 solves a one-observable repair problem; predictive closure solves autonomous all-future closure. One-step repair can be an ingredient in iterative closure but is not identical to it. |
| P023 T15–T16 boundary-bit repair for `Q_r` under `D_d` | P007/P018 quotient/remainder/carry geometry | `SPECIALIZATION + NEW MINIMALITY QUESTION` | The arithmetic coordinates come from existing quotient/remainder geometry, while P023 proves that the future task may require only one canonical bit rather than the full remainder. Keep the exact arithmetic theorem in P023 and cross-reference its P007/P018 coordinate source. |
| P021 witness-identity failure of cardinality transport | P023 quotient-safety rule | `MOTIVATING SPECIALIZATION` | P021 gives an application-level counterexample showing counts can be composition-incomplete. P023 abstracts the legal-collapse criterion. P021 keeps direction/causal objects; generic factorization belongs to A2/P023. |
| A3 operation/observation-aware minimum exact relation precision | P018/P023 future-compatible quotient | `SPECIALIZATION / BRIDGE CANDIDATE` | A3 computes task-derived exact precision inside a structured linear partition/relation-state model. It should eventually be proved as an A2 instance, not declared a second general future-compatibility theory. Exact bridge hypotheses still need formal statement. |

### Consolidation decision

For the general finite unary theorem, the reusable mother statement should be maintained once. During migration, keep both historical theorem numbers for provenance, but new general extensions should go through P023/A2. P018 should cite the mother theorem and add only precision-specific consequences (kernel/time bifiltration, defect/response, carry/extension data, merger geometry, arithmetic examples).

## 3. P017 pressure-test results lifted into reusable precision mathematics

| Source result | Target/general home | Relationship | Audit conclusion |
|---|---|---|---|
| P017 cofactor-window raw width = whole quotient blocks plus one boundary carry | P018 quotient response / carry pattern | `SAME_MOTHER` | The cofactor residue-hit formula and quotient-response carry are the same finite boundary phenomenon in different coordinates. Keep one general response statement; P017 keeps the square-basin cofactor specialization. |
| P017 square-basin floor-division / quotient-root transport first discovered with prime-oriented motivation | P018 general quotient/root two-basin theorem | `STRICT_GENERALIZATION` | The prime assumption was removable. General theorem belongs to P018; P017 keeps the lower-band least-factor consequence. |
| P017 different local names for cofactor residue hit, quotient-response carry bit, and common-center unique hit | canonical P017 high-band hit machinery | `SAME_MOTHER` | These have already been consolidated in P017. Future work should not resurrect them as independent routes unless a new invariant distinguishes them. |
| P017 generic sieve-density heuristics | canonical P017 deterministic resource/correlation route | `CONFLICT / NEGATIVE_BOUNDARY` | Independent-density intuition telescopes or fails to supply the required deterministic control. Preserve it as a forbidden shortcut, not as an active parallel proof route. |

### P017 architectural rule

P017 remains a domain pressure test, not a warehouse for every structure it exposes. Remove a prime/square-basin assumption whenever the proof allows it, lift the resulting mother theorem upward, and keep only genuinely square-basin/least-factor/resource constraints local to P017.

## 4. Functional irreversibility and relational spectra

| Source result | Target/general home | Relationship | Audit conclusion |
|---|---|---|---|
| P011 collision spectrum `J_k(F)` for total deterministic maps | A4 witness spectrum `W_k(R)` and group/event spectrum `G_k(R)` | `EXACT SPECIALIZATION` | If `R` is the graph of a total function `F`, then `W_k=G_k=J_k(F)`. P011 remains canonical for functional fibers; A4 handles multivalued correspondences. |
| P011 monotonicity under deterministic postcomposition | A4 `G_k` under deterministic target postcomposition | `STRICT GENERALIZATION WITH BOUNDARY` | `G_k` retains the monotonic group/event property, while `W_k` need not. Do not transfer every P011 monotonicity statement to witness multiplicity. |
| P011 fiber partition | general A4 support relation | `SPECIALIZATION` | A function graph partitions sources by unique target; a multivalued relation generally yields overlapping target supports and need not induce an equivalence relation. |
| Pairwise common-target graph | A4 higher-order common-target hyperstructure / `G_k` | `CONFLICT / NEGATIVE_BOUNDARY` | Pairwise intersection data cannot in general reconstruct triple or higher common targets. Preserve this as a prohibition against replacing higher-order support structure by a simple graph without proof. |

## 5. Two distinct “relation” cores

The most important negative consolidation result of this audit is that A3 and A4 are **not the same object**.

| A3 — partition relation-state algebra | A4 — admissible support/correspondence algebra |
|---|---|
| Structured integer field `Z_ij=m_j c_i-m_i c_j` with capacities/totals | Arbitrary-but-admissible finite binary relation `R⊆X×Z` |
| Represents exact present block-total state up to declared constraints | Represents which target states are allowed for each source |
| Partition quotient has matrix law `Z'=AZA^T` | Composition is ordinary relation composition |
| Kernel `K_A={η:Aη=0}` describes invisible additive motion/state fiber | Common-target relation is `R_r ; converse(R_s)` |
| Rank/quantum/refinement forest quantify structured state precision | `W_k/G_k` quantify witness and common-target multiplicity |

Relationship: `COMPOSABLE_INDEPENDENT`.

The current shared word “relation” is a terminology collision, not an equivalence theorem.

### Open A3/A4 bridge questions

1. Given a geometry or operation family, when is an A4 support relation derivable from an A3 structured state?
2. When does an A4 common-target query factor through an A3 partition quotient?
3. What A3 internal relation coordinates are sufficient/necessary for a chosen A4 query language?
4. Does a natural functor/forgetful map exist in a restricted admissible class, or are the two structures fundamentally incomparable outside applications?

No architectural merge is allowed until at least one precise bridge theorem is proved.

## 6. Geometry lineage

| Source result | Target/general home | Relationship | Audit conclusion |
|---|---|---|---|
| P012 primitive adjacency and integer graph metric | P022 lattice/root-lattice geometry | `GENERATOR / SPECIALIZATION` | P022 may choose specific lattices and derive balls, shells, radial observations and carry, while P012 remains the metric-foundation baseline. |
| P012 finite graph balls / geometry-generated supports | A4 admissible support relations | `GENERATOR` | Geometry can generate an admissible correspondence family. This does not make A4 part of primitive geometry. |
| Historical P022 branch weighted relation-state machinery | A3 | `STRICT GENERALIZATION OUT OF GEOMETRY` | Once the formulas no longer use lattice/metric hypotheses, the mother statements belong to A3; P022 retains geometric instantiations. |
| P022 radial/quadratic/distance observations | A3 observation-aware relation precision | `SPECIALIZATION / CONSUMER` | Geometry supplies concrete observation rows/queries; A3 may determine the minimum exact partition precision for those queries. |
| E001 square-body/Chebyshev supports | P012/A4 | `APPLICATION` | E001 is one executable geometry-generated admissible-support system, not a new primitive geometry. |

## 7. Stabilization / kernel lineage

| Source result | Target/general home | Relationship | Audit conclusion |
|---|---|---|---|
| P010 strict history merge | P018 pair/kernel filtration | `SPECIALIZATION / REUSE` | P018 exposes kernel/pair as a lower substrate and adds precision-time semantics; P010 remains the canonical deterministic-history merge problem. |
| P011 collision polynomial/spectrum | P018 time-resolved collision increments | `STRICT TEMPORAL REFINEMENT` | P018 decomposes the same finite partition evolution by when merges occur; it should cite P011 rather than rename the final spectrum. |
| P019 collapse-word stabilization | P020 well-founded stabilization | `SPECIALIZATION` | P020 supplies the general monotone reductive well-founded theorem; P019 retains the exact lcm collapse-word consequences and semilattice quotient. |
| historical `P019_*` geometry/relation files | canonical P019 | `NAME_COLLISION_ONLY` | No theorem ownership follows from the old filename. Canonical P019 is collapse-word stabilization. Historical geometry/relation work migrates to P022/A3 as appropriate. |

## 8. P021 physical-facing lineage

| Source result | Target/general home | Relationship | Audit conclusion |
|---|---|---|---|
| Direction orbit, causal role, focusing/horizon constructions | P021 | `APPLICATION-SPECIFIC` | These remain P021 and must not be promoted into general quotient theory merely because they use witness transport. |
| Witness relation vs count-matrix insufficiency | A2/P023 | `MOTIVATING SPECIALIZATION` | The negative result exposes a general information-sufficiency issue; P023 owns the abstract quotient gate. |
| Physical horizon/time interpretation | P016 falsification contract | `DOWNSTREAM HYPOTHESIS` | Mathematical many-to-one/focusing results do not by themselves establish physical black holes, time ontology, curvature, or GR replacement. |

## 9. E001 lineage after the split

| E001 asset | Long-term owner | Relationship |
|---|---|---|
| collision engine, broad phase, adaptive schedule, exact oracle, benchmark | E001 | `APPLICATION / EXECUTABLE TEST` |
| finite observation/refinement logic | P018/A2 | `REUSE` |
| admissible support relations, common-target composition, split-completeness | A4 | `LIFTED GENERAL MATHEMATICS` |
| `W_k/G_k` relation spectra | A4 with explicit P011 degeneration | `LIFTED GENERAL MATHEMATICS` |
| CPU/performance measurements | E001 only | `ENGINEERING EVIDENCE`, never mathematical theorem |

The split prevents E001 from growing a second precision calculus or hiding reusable relation mathematics inside a benchmark branch.

## 10. Immediate deduplication actions

1. Treat P018 T160–T168 and P023 T03–T07 as one unary mother theorem family in future documentation. Preserve both historical theorem numbers, but stop adding parallel general extensions.
2. Continue multi-operation closure under P023 T10–T14/A2; P018 adds only precision-specific corollaries.
3. Keep P023 one-step/minimal repair as a distinct subline; do not collapse it into predictive closure.
4. Keep A3 and A4 separate until bridge theorems exist.
5. When P022 is replayed, lift every lattice-independent weighted relation theorem to A3 before integrating the geometry-specific remainder.
6. When E001 is replayed, import A4 mathematics rather than duplicating it in engineering modules.
7. P017 continues the established policy: coordinate-equivalent routes are one route; generic results move upward.

## 11. Provenance rule

Consolidation never erases discovery history.

For every lifted theorem, record:

- original branch and commit where the structure was first exposed;
- original problem/application motivation;
- final reusable theorem home;
- surviving specialized corollary;
- whether the relationship is exact equivalence, strict generalization, or merely an application.

The repository should become easier to reason about without making the actual history of discovery harder to reconstruct.
