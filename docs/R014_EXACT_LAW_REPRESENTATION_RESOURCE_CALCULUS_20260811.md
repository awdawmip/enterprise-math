# R014 — Exact-Law Representation Resource Calculus: Consolidated Rooting Result

Status: `ROOTING_SUCCESS / METHODOLOGY_AND_TOOLING_ONLY / NO_NEW_FOUNDATION_RESOURCE_CALCULUS`

Researcher-ID: `EM-R014-7Q9K2A`  
Research-Task: `RS-R014-EXACT-LAW-REPRESENTATION-RESOURCE-CALCULUS`  
Research-Role: `RESEARCHER`  
Date: `2026-08-11`  
Base taskbook: `research_tasks/R014_EXACT_LAW_REPRESENTATION_RESOURCE_CALCULUS_20260811.md`  
Evidence policy: historical PRs `#454–#474` are evidence sources for this one mother question; no child taskbook or stacked child-PR is created.

## 0. Root answer

After exact semantic law/interface is frozen, the Stage131 closure presentations, A2/P023 future-word compilers, CRT factorizations, R004 storage/innovation schedules, and R005-A horizon/segment execution laws do **not** currently support a genuinely new Enterprise-specific foundation resource calculus.

The strongest reusable object that survives the prior-art kill gate is:

1. an exact semantic-fibre gate;
2. an explicit accounting regime;
3. an ordinary typed resource vector;
4. ordinary coordinatewise Pareto dominance inside one fibre/regime;
5. refusal to compare semantic or accounting mismatches;
6. an offline oracle enforcing those rules.

Formally, for an exact semantic contract `S` and accounting regime `A`, let

`Impl_A(S) = { I : I realizes S exactly and is costed under A }`.

For the mandatory operational projection used by the executable oracle,

`rho_A(I) = (storage, work, depth, channel, reconstruction)`.

Then the only justified generic order is the product/Pareto preorder

`I <=_(S,A) J`

iff every active coordinate of `rho_A(I)` is no larger than the corresponding coordinate of `rho_A(J)`.

Across different semantic fibres or accounting regimes there is **no resource dominance judgment**.

The global structure is therefore only the disjoint family

`P_A = disjoint_union_S Pareto(Impl_A(S), rho_A)`,

possibly further separated by accounting regime. Quotienting equal resource vectors yields the ordinary product partial order. No surviving evidence supplies an extra Enterprise-specific multiplication, residuation, conservation law, or representation-independent lower bound.

This is a successful negative rooting result, not a failed task.

## 1. What is Enterprise-specific and what is not

### 1.1 Methodology/tooling retained

The project-specific contribution is the **routing discipline**:

- semantic capability is frozen before resource optimization;
- exact semantic identity is committed by a stable identifier/digest;
- resource figures are tagged by one disclosed accounting regime;
- decoder/normalizer/reconstruction work is not silently free;
- `N/A`/`None` in an active coordinate is not treated as zero;
- incomparable points remain incomparable unless an explicit workload functional is introduced;
- a resource comparator rejects semantic-fibre mismatch before looking at costs.

This is useful and reusable engineering/research methodology.

### 1.2 Foundation claim rejected

R014 did not find either of the two things needed to promote a new foundation calculus:

**A. New cross-family composition law.**  
No Enterprise-native operation was found whose resource composition simultaneously explains Stage131 shortcutting, word compilation/normalization, CRT factorization, causal innovation timing, and segmented horizon execution while escaping standard circuit/automata/compiler/data-structure composition.

**B. Representation-independent multi-resource lower bound.**  
No lower bound survived changes of exact representation and accounting technology. In particular, the Stage131 materialization lower-bound route is broken by exact compact countermodels; compiler, CRT and segment results are class-relative; R004's innovation condition is semantic/information-theoretic rather than a universal implementation-resource lower bound.

## 2. Fixed-semantics representation/resource matrix

The table deliberately separates semantic carrier from implementation resources. “Native/materialized count” is representation-class specific; it is not interpreted as semantic precision.

| Representation family | Semantic carrier | Exactness invariant | Native artifact count | Materialization bound / pressure | Working storage | Query / decision work | Eval depth / span | Channel / communication width | Reconstruction burden | Retained? | Gap / reason |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R014 identifier semantics / Stage131 override-set bridge | Canonical exact semantic contract plus stable semantic identifier; exact override/effect law | Same accepted state/input, DOMAIN/legality, future actions, observations/witness channels, continuation interface; same semantic ID | Compact semantic tuple / override representation under its declared model | Optional cached consequences can grow without changing the semantic fibre | Compact native state plus declared metadata | Direct vs iterative execution can shift online work | Representation dependent | Payload/override channels only as declared | Normalization/decoding must be counted | **YES — methodology guard** | Digest identifies the fibre; it does not itself prove a new complexity law |
| Stage131 Horn/CNF / closure / compile-state presentations | One fixed closure/executability relation | Same closure / reachable consequence law and same continuation contract | Hasse/adjacency, Horn/hyperedge, rooted-circuit, shortcut or compiled forms vary | Full transitive materialization can be large; selective/no materialization is exact in countermodels | Varies from compact generator/state descriptions to cached tables | Fewer cached consequences can require more inference/composition | Shortcut/materialization changes rounds | Usually not the controlling invariant; depends on exposed interface | Macro expansion / proof reconstruction can move cost | **YES — evidence family** | PR #467 kills a generic forced `Omega(n)` materialized-layer claim; no representation-independent lower bound survives |
| A2/P023 future-word compiler preserving `p,q,U,V,c` | Exact finite action semantics / future-operation law on the declared state | Exact preservation of state/effect behavior, including `p,q,U,V,c`; word normalizer must induce same transformation | Generators, literal word caches, right-generator automata, Cayley tables, formulaic normal forms | Literal cache through depth `d`: `sum_{i=1}^d k^i`; finite monoid tables `m*k` or `m^2`; formulaic presentations may collapse table cost | Can be tiny formula/state IDs or large tables | Preprocessing/normalization trades against online application work | Literal block cache gives `ceil(H/d)` rounds; associative/formulaic normalization can give logarithmic depth | Depends on state/effect encoding, not semantic precision | Word-to-effect normalization is mandatory and can erase apparent cache wins if replayed naively | **YES — evidence family** | PRs #471–#473 themselves classify block caching, monoids, Cayley tables, bitmask/semilattice work-depth as standard prior CS/algebra |
| R004 boxed-trace / storage-innovation schedule | Frozen predictable-span / observation law | Exact auxiliary information is nontrivial iff the target leaves the predictable span; equivalently nonzero innovation | Stored trace/auxiliary statistic versus runtime innovation events | Depends on causal timing and what can be predicted from prior information | Ex-ante transcript capacity can be exchanged with runtime innovation only under the frozen causal model | Runtime update/innovation processing | Timing/causality may require a typed temporal coordinate | Information arrival channel is model-specific | Reconstructing omitted predictable content is allowed only if the frozen model supplies it | **YES — test family** | `K_t != H_t` / innovation nonzero is an information/identifiability criterion, not a universal storage-work algebra |
| R005-A finite horizon / segment execution | Exact ultimately-periodic future output system and its finite-horizon quotient | Equality of exact horizon signatures; segment observation must expose the same contiguous future window | Minimal quotient classes `C_O(H)` plus segment-state/executor representation | Exact packet: `C_{O,B}(D)=C_O((D+1)B-1)` and `D_O*(B)=ceil((H_O*+1)/B)-1` | Depends on whether future signatures, quotient IDs or block executor state are materialized | Block processing versus state refinement | Sharp depth follows the displayed ceiling law | Block width `B` is an interface/resource parameter | Full-state reconstruction occurs once horizon reaches the distinguishing radius | **YES — test family** | Packet explicitly classifies the generic recursion as ordinary automata/Moore partition refinement and segment law as generic block-observation content; no common theorem with Stage131 beyond standard composition |
| CRT / modular sensor factorization | One fixed exact modular reflection/equality law, e.g. modulus product/lcm `L` | Pairwise-coprime factors encode the same exact residue law; scalar reconstruction required only if downstream contract demands it | One fused channel through grouped prime-factor channels | Generic Cayley-like materialization is irrelevant; factor packing is a partition/load-balancing choice | Ideal information fixed; rounded widths and metadata vary with grouping | Per-channel arithmetic can parallelize | Optional balanced CRT reconstruction depth `ceil(log2 g)` for `g` channels; zero for tuple-native consumers | Channel count trades against peak modulus/bit width | Conditional CRT recombination into scalar residue | **YES — evidence family** | PR #470 explicitly treats CRT, factor grouping, information-width bounds and load balancing as prior art; packing gaps are family-specific discrete optimization |

### Matrix-A conclusion

All six rows fit the same **methodological shell**:

`freeze semantics -> choose representation class/accounting -> obtain resource vector -> retain nondominated implementations`.

But their sharp formulas arise from different ordinary structures:

- reachability/shortcut geometry;
- semigroup/monoid/circuit presentation;
- causal predictability/innovation;
- deterministic automaton horizon refinement;
- block composition;
- integer factor packing / CRT reconstruction.

The common shell does not by itself supply a new algebra relating these formulas.

## 3. Prior-art / novelty attack matrix

| Attack family | Primary prior-art anchor | Collision with R014 candidate | R014 disposition |
|---|---|---|---|
| Time-space / memory-I/O tradeoff | Hong & Kung, *I/O Complexity: The Red-Blue Pebble Game*, STOC 1981, DOI `10.1145/800076.802486` | Precomputation/materialization versus memory traffic/work is already model-relative complexity theory | Generic storage/work tradeoff **not novel** |
| Circuit size/depth/work | R. P. Brent, *The Parallel Evaluation of General Arithmetic Expressions*, JACM 21 (1974), 201–206 | Work/depth and bounded-processor simulation already separate total operations from parallel span | Generic work/depth coordinate **not novel** |
| Automata / monoid presentation | M. P. Schützenberger, *On Finite Monoids Having Only Trivial Subgroups*, Information and Control 8(2) (1965), 190–194, DOI `10.1016/S0019-9958(65)90108-7`; classical finite transformation-monoid theory | Exact future-word effects, right-generator automata, Cayley multiplication and formulaic semigroup presentations are standard algebraic automata objects | Future-word algebra/presentation layer **not novel** |
| Compiler / partial evaluation | Yoshihiko Futamura, *Partial Evaluation of Computation Process, An Approach to a Compiler-Compiler*, Computer Software 21(5) (2004), 343–351, DOI `10.11309/jssst.21.343` (publication of the classic partial-evaluation/compiler idea) | Moving work from online interpretation to specialization/precomputation is exactly the compiler/partial-evaluation axis | Generic compile-vs-run Pareto **not novel** |
| Succinct data structures / preprocessing-query | M. Pătraşcu & E. D. Demaine, *Logarithmic Lower Bounds in the Cell-Probe Model*, SIAM J. Comput. 35(4) (2006), 932–963, DOI `10.1137/S0097539705447256` | Storage/update/query tradeoffs and class-relative lower bounds already require a declared machine/model | Generic preprocessing/query lower-bound language **not novel** |
| TC-spanners / shortcutting | A. Bhattacharyya, E. Grigorescu, K. Jung, S. Raskhodnikova & D. P. Woodruff, *Transitive-Closure Spanners*, SIAM J. Comput., DOI `10.1137/110826655` | A TC-spanner is defined to preserve the same transitive closure while adding shortcut structure to reduce diameter | Stage131 exact-closure storage/depth tradeoff has a **direct prior-art analogue** |
| Communication / channel width | A. C.-C. Yao, *Some Complexity Questions Related to Distributive Computing (Preliminary Report)*, STOC 1979 | Channel/communication is already an independent complexity resource once a protocol model is declared | Generic channel-width coordinate **not novel** |
| Multiobjective / Pareto optimization | C. H. Papadimitriou & M. Yannakakis, *On the Approximability of Trade-offs and Optimal Access of Web Sources*, FOCS 2000, 86–92, DOI `10.1109/SFCS.2000.892068` | Nondominated resource vectors and refusal to totalize without a utility function are standard multiobjective optimization | Pareto frontier itself **not novel** |

### Kill-gate result

Every generic component of the proposed calculus is already standard once stripped of Enterprise semantic naming:

- product-order resources;
- explicit machine/accounting model;
- preprocessing versus online work;
- state/table/formula presentation complexity;
- work versus depth;
- shortcut storage versus path/round depth;
- communication width;
- nondominated multiobjective optimization.

The project-native piece is the semantic/fibre routing guard, not a new resource mathematics.

## 4. Cross-family novelty tests

| Candidate foundation statement | Evidence / attack | Survives as new foundation? |
|---|---|---|
| “Exact implementations of one law admit a common resource order.” | This reduces immediately to a product/Pareto preorder after coordinate/model declaration. | **NO** |
| “Semantic identity plus resources forms a new Enterprise calculus.” | Semantic identity is a guard/index; it does not change the ordinary product order inside each fibre. | **NO — methodology only** |
| “A five-coordinate vector `(storage,work,depth,channel,reconstruction)` is universal.” | Different families require additional typed coordinates such as coefficient width, preprocessing, law storage, causality/timing; projections are workload/model dependent. | **NO** |
| “Materialization obeys a representation-independent lower bound.” | Stage131 exact compact/no-materialization countermodels invalidate the attempted generic linear lower bound. | **NO** |
| “Block/horizon ceilings imply one common composition theorem.” | R005-A's `ceil((H*+1)/B)-1`, future-word `ceil(H/d)`, and TC-spanner diameter reductions arise from different standard composition models. Shared ceiling syntax is insufficient. | **NO** |
| “Monoid/effect cardinality controls exact presentation cost.” | #472/#473 show generic `m^2` tables can collapse to compact formulaic bitmask/semilattice presentation with runtime circuit work. | **NO** |
| “CRT factorization contributes a new cross-resource conservation law.” | Same information can be packaged into standard coprime channels; width/channel/reconstruction and discrete factor packing are classical implementation/packing effects. | **NO** |
| “R004 innovation supplies the missing common resource.” | Innovation detects unpredictable information under a causal sigma-field/span; it is not interchangeable with generic cache/materialization cost without adding a causal model. | **NO** |
| “Stable semantic IDs are operationally valuable.” | They prevent comparing semantically different implementations and make evidence reproducible. | **YES — methodology/tooling** |
| “An offline comparator can enforce semantic/accounting discipline.” | Deterministic oracle below implements exactly that policy. | **YES — tooling** |

## 5. Minimal dominance oracle

Owner-local executable:

`src/enterprise_math/exact_resource_pareto.py`

Required coordinates:

`[storage, work, depth, channel, reconstruction]`.

### Comparator contract

1. `semantic_fibre` equality is checked **before** any resource comparison.
2. `accounting_regime` equality is also mandatory.
3. Default comparison is weak coordinatewise Pareto.
4. Strict dominance requires at least one strict coordinate improvement and no active regression.
5. A cross-coordinate tradeoff is `INCOMPARABLE`.
6. Equal active resource vectors are `RESOURCE_EQUIVALENT`; this does not assert representation identity.
7. `None` on an active coordinate raises `UndefinedResource`.
8. Weights are **not** a weighted-sum scalarizer:
   - positive weights are common coordinate rescalings;
   - zero disables that coordinate;
   - negative/nonfinite weights fail;
   - all-zero weights fail.
9. A user who wants a scalar ranking must supply a separate workload/cost functional outside this foundation-neutral comparator.

The module exposes the machine-readable verdict:

`ROOTING_SUCCESS / METHODOLOGY_AND_TOOLING_ONLY / NO_NEW_FOUNDATION_RESOURCE_CALCULUS`.

## 6. Deterministic verification

Test file:

`tests/test_exact_resource_pareto.py`

Offline command:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_exact_resource_pareto.py' -v
```

Local R014 execution result:

`13 tests passed / 0 failed`.

Fixtures cover:

- canonical semantic digest under key reordering;
- semantic-law change produces a different digest;
- semantic mismatch fails;
- accounting mismatch fails;
- same-fibre strict Pareto passes;
- storage/work tradeoff remains incomparable;
- resource-equivalent encodings are not collapsed into identity;
- active `None` fails;
- explicit zero-weight disabling works;
- positive weights do not scalarize a tradeoff;
- all-zero weights fail;
- dominated points are removed from the frontier;
- root routing verdict is machine-readable.

No repository-wide CI or `EXECUTABLE_CHECKED` claim is made by this research package.

## 7. Evidence consolidation

This package consumes, but does not extend, the stacked research lineage.

Key evidence checkpoints include:

- `#454–#474`: Stage131 / A2-P023 / Foundation-facing representation-resource chain as a whole;
- `#467`: counterexample pressure against a forced generic materialization lower bound;
- `#470`: exact CRT factorization/resource Pareto;
- `#471`: literal future-word cache storage/execution-depth Pareto;
- `#472`: finite semantic word-normalizer / transformation-monoid presentation tradeoff;
- `#473`: formulaic word algebra versus tabulated semantic monoid;
- `#474`: explicit semantic-precision versus representation-resource two-level architecture;
- `#449`: frozen R004 storage/innovation schedule;
- R005-A External Prime Capability Packet v3 at source commit `6991a5d875a3c74d447869cb987a08e661b3d97e`, especially finite-horizon quotient refinement and exact segmented composition.

No child taskbook is created. No claim in this package promotes those draft chains to canonical Foundation.

## 8. Routing table

| Route | Decision | Reason |
|---|---|---|
| `NEW_ENTERPRISE_SPECIFIC_EXACT_RESOURCE_CALCULUS` | **REJECT** | No new cross-family composition law or representation-independent lower bound survives prior art/countermodels |
| `METHODOLOGY_AND_TOOLING_ONLY` | **ACCEPT** | Semantic-fibre gate + accounting guard + explicit typed Pareto comparator are useful project-native research infrastructure |
| `ORDINARY_IMPLEMENTATION_PARETO_ONLY` | **ACCEPT / ROOTED** | Inside a frozen exact semantic fibre, surviving resource structure is ordinary model-relative implementation Pareto |

Final routing token:

`ROOTING_SUCCESS / METHODOLOGY_AND_TOOLING_ONLY / NO_NEW_FOUNDATION_RESOURCE_CALCULUS`

## 9. Stop condition

The taskbook stop condition is met.

Further child generations would only elaborate standard resource coordinates or representation classes unless new evidence supplies one of:

1. a cross-family Enterprise-specific resource composition law not reducible to known circuit/automata/compiler/data-structure/Pareto machinery; or
2. a representation-independent exact multi-resource lower bound that survives all exact encodings and a declared broad technology class.

Absent such evidence, R014 should remain rooted as methodology/tooling rather than be expanded into another stacked PR lineage.
