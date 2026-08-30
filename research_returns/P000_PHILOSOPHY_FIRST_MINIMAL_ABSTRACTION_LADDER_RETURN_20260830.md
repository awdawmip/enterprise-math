# P000 Philosophy-First Q8 — Minimal Sufficient Abstraction Ladder

Task: `RS-P000-PHILOSOPHY-FIRST-MINIMAL-ABSTRACTION-LADDER`  
Publication: `TP2-28E97B509F00603F4053`  
Researcher: `EM-PHQ8-FFA922`  
Claim: `chatgpt-p000q8-20260830-1225-84c1d7`  
Execution branch: `research/p000-philosophy-minimal-abstraction-ladder-em-phq8-ffa922`  
Frozen P000 authority: `projects/enterprise-math/P000_REALITY_FOUNDATION.json` plus current Gen13 foundation.  
Terminal candidate: `MINIMAL_ABSTRACTION_GATES_EXACTLY_WITNESSED`

## 0. Result

The hard target

`P000_MINIMAL_SUFFICIENT_ABSTRACTION_LADDER_WITH_EXACT_UPGRADE_GATES`

is met at the current finite-model strength.

The main conclusion is deliberately **not** “use the highest categorical language.” The correct rule is:

> **A language level is sufficient for a question exactly when every answer asked by the question is constant on the fibers of the information-forgetting map into that language. Upgrade only when a finite lower-language fiber contains two states with different required answers, and the proposed higher language repairs that failure without erasing a P000-declared observable distinction.**

This turns “abstract only as far as the problem forces” into a finite falsifiable criterion.

The resulting operational ladder is

`SET -> GROUPOID -> PRESHEAF/DESCENT -> STACK`

but this is **not a literal chain of categorical inclusions**. `GROUPOID` adds morphism/equivalence information; `PRESHEAF/DESCENT` adds locality, base incidence, and restriction maps. When both are needed, the presheaf is groupoid-valued. `STACK` is justified only when isomorphism-valued descent data are intended to be effective global objects.

At current Q1-Q7 strength:

- Q2 and Q6 stay at **SET**.
- Q1, Q3, Q5, Q7 require **GROUPOID** for their canonicality/gauge/naturality content.
- Q4 requires **PRESHEAF/DESCENT** for its overlap-indexed cycle holonomy.
- Current strict-frame Q4 does **not** justify STACK.
- STACK becomes justified only in the explicitly different semantics where nontrivial twisting is promoted from “obstruction” to “legitimate global torsor/bundle data.”
- No current finite packet supplies a lower-language failure certificate requiring an infinity-groupoid upgrade; therefore such an upgrade is rejected by the stop-rule.

The deterministic checker returns:

`PASS P000_MINIMAL_ABSTRACTION_LADDER; checks=33; set_to_groupoid=object_set_same/pi0_2_vs_1/fixed0; triangle_C2=8_total/4_strict/4_obstructed; torsor_stack=2_gauge_classes_of_4; q_min=Q1:G,Q2:S,Q3:G,Q4:P,Q5:G,Q6:S,Q7:G; strict_frame_stack=REJECT; twisted_torsor_stack=ACCEPT; infinity_upgrade=REJECT`

---

## 1. Scope and non-promotion guards

This result is a **method theorem for choosing the language of current P000 finite-model questions**. It does not alter P000.

In particular:

1. the full Enterprise world remains the locked 6D discrete Cell space plus 1D relational time;
2. no carrier `S4`, `C2`, graph, cover nerve, coordinate frame, or finite extension used below is promoted to bare-P000 ontology;
3. Q1-Q7 return packets are used as finite evidence at their declared benchmark scopes; pending Driver review remains pending;
4. classical groupoid/descent/stack language is used as a lens only;
5. no novelty claim is made for standard facts about group actions, Čech cocycles, torsors, or stacks;
6. an abstraction level is not allowed to “solve” a P000 problem by quotienting away a distinction the task declares observable.

---

## 2. Tool-reuse gate

The taskbook requires reuse inspection before introducing a reusable mechanism. No new global mechanism is needed.

### T6 — composition-safe collapse: `REUSE_APPLIED`

Executable source inspected:

`src/enterprise_math/composition_safe_collapse.py`
blob `sha1:384d166f642fb65c53fc7f2431f43dc99880693a`

The exact reusable criterion is the existing finite fiber-constancy law:

for a coarse map `q : X -> Q` and a required answer/observable `a : X -> A`, the answer descends through `q` iff `a` is constant on every `q`-fiber.

Q8 uses this as the mathematical definition of **question-relative sufficiency**.

### T7 — finite symmetry / group action: `REUSE_APPLIED`

Executable source inspected:

`src/enterprise_math/finite_symmetry.py`
blob `sha1:ae96a32cb6b6fdd974bd9f44fb28a1b643c9b8a2`

Its orbit, stabilizer, and global-fixed-point calculus is exactly the finite machinery needed for the `SET -> GROUPOID` gate and Q7 naturality certificates.

### T9 / holonomy family: `INSPECTED, NO NEW GLOBAL EXTENSION`

Executable source inspected:

`src/enterprise_math/precision_holonomy.py`
blob `sha1:b07b66e60cb887633691b8a3f7c2b2543dae41bb`

The module confirms the project’s existing discipline that path/coarsening defects must remain explicit exact states. Q8 does not extend that module: Q4 already supplies the task-specific finite overlap-graph holonomy theorem, so the Q8 checker keeps its `C2` cycle audit local to this task.

### Method disposition

`RESULT_ONLY / NO_NEW_GLOBAL_TOOL_FAMILY`

The new object is the **Q8 decision theorem and finite certificate**, not a general-purpose library.

---

## 3. Question-relative sufficiency

Let `Omega` be the frozen finite semantic packet relevant to a task: admissible models, presentations, local probes, lift choices, transition data, or other exact states permitted by that task.

Let

`Ans_Q : Omega -> A_Q`

collect **all answers the task actually asks for**, modulo the task’s declared equivalence.

Let `E_L : Omega -> C_L` be the information retained by language level `L`.

### Definition 3.1 — Q-sufficient level

`L` is **Q-sufficient** on the frozen packet iff there exists a map/functor

`Ansbar_Q : C_L -> A_Q`

such that

`Ans_Q = Ansbar_Q o E_L`

up to the task’s declared equivalence.

For a finite set-valued answer this is exactly T6 fiber constancy:

`E_L(x) = E_L(y)  =>  Ans_Q(x) = Ans_Q(y)`.

### Definition 3.2 — lower-language failure certificate

A failure certificate for `L` is a finite pair `x,y` such that

`E_L(x) = E_L(y)` but `Ans_Q(x) != Ans_Q(y)`,

or, for descent questions, an explicit compatible local datum whose effectivity status cannot be determined after `E_L` forgets the restriction/overlap structure.

### Definition 3.3 — higher-language repair theorem

A candidate level `L+` repairs the failure iff:

1. the witness is separated or correctly realized at `L+`;
2. the required answer factors through `E_{L+}`;
3. no P000-declared observable has been erased to obtain the repair.

This is stronger than “the higher language can describe the example.” It must recover the exact task answer.

---

## 4. Exact candidate levels in current P000 context

## 4.1 SET

For a **fixed declared model/presentation/probe scope**, retain:

- a finite set of candidates/states;
- literal equality;
- set maps such as observation, residue, or representability maps;
- predicates and fibers/images.

Typical form:

`F(M) in Set`.

SET does **not** retain:

- accepted model isomorphisms;
- gauge morphisms;
- automorphism action;
- locality/base incidence;
- restriction maps;
- effective gluing up to isomorphism.

SET is the default and must be retained unless a finite failure certificate forces escalation.

## 4.2 GROUPOID

Let `M` be the finite model groupoid:

- objects: admitted model/presentation instances;
- arrows: accepted invertible model isomorphisms, relabelings, or gauge maps.

A candidate family is a functor/action groupoid such as

`F : M -> Grpd`

or, in the simplest finite action case, `Gamma // G`.

The layer retains:

- object set;
- morphisms;
- connected components / orbit classes `pi_0`;
- isotropy / stabilizers;
- automorphism-fixed candidates;
- naturality under accepted equivalence.

It is required when the task answer depends on **how candidates transform**, not merely which candidates exist.

## 4.3 PRESHEAF / DESCENT

Let `B` be a finite base category/poset/overlap graph of:

- P000 slices;
- probe neighborhoods;
- refinement levels;
- declared local regions;
- overlaps.

A presheaf is

`F : B^op -> C`

where the fiber category `C` is the **lowest already-required fiber language**:

- `Set` when local objects have no relevant gauge;
- `Grpd` when Q3/Q7-type morphism data must also be retained.

The new information is not “more morphisms in the fiber”; it is:

- **where** local data live;
- restriction maps;
- overlap incidence;
- compatibility around compositions/cycles.

A descent datum is local objects plus overlap comparisons satisfying the declared cocycle rules.

This layer is required when unindexed local fibers can be identical while their restriction/overlap pattern changes the global answer.

## 4.4 STACK

For a declared cover `U_i -> U`, a groupoid-valued presheaf/prestack `F` has a descent groupoid

`Desc_F({U_i})`.

`F` is a 1-stack on the declared finite site when the comparison functor

`F(U) -> Desc_F({U_i})`

is an equivalence for every accepted cover.

The key new demand is **effectivity of gluing up to accepted isomorphism**, not merely storage of local restriction data.

A stack is not warranted merely because a cocycle or holonomy exists. It is warranted only when the task’s semantics says that the corresponding isomorphism-valued descent datum **is a legitimate global object**.

---

## 5. Exact finite upgrade witness A — SET fails, GROUPOID suffices

Take the same object set

`X = {0,1}`.

Construct two groupoids.

### A0 — discrete groupoid

Only identity arrows.

Then

`|pi_0| = 2`.

### A1 — `C2` swap action groupoid

`C2` swaps `0 <-> 1`.

Then

`|pi_0| = 1`

and the global fixed-point set is empty.

After forgetting arrows, both become the same SET `X`.

Therefore the SET forgetful map has a fiber containing two groupoids with different answers to:

- “how many equivalence classes?”;
- “does a natural singleton choice exist?”

So SET is not sufficient for these questions.

GROUPOID repairs exactly:

- `pi_0` records equivalence classes;
- isotropy records stabilizers;
- T7 fixed-point calculus decides natural single-valued choices.

### Direct Q1/Q3/Q7 relevance

This toy certificate mirrors the current finite returns:

- Q1: relabeling/conjugacy can flip label-level answers; section existence does not imply canonicality.
- Q3, `RR-49FC19221CA5D69B00E6`: the same section object layer can have different `pi_0` when the actual primitive-preserving morphisms differ.
- Q7, `RR-1ECF8B93CCAF6463224F`: natural selections are exactly automorphism-fixed candidates on component representatives; several symmetric candidate sets have fixed count zero.

**Gate verdict:** `SET -> GROUPOID = JUSTIFIED` for morphism/naturality-sensitive questions.

---

## 6. Exact finite upgrade witness B — unindexed GROUPOID fails, PRESHEAF/DESCENT suffices

Use a finite cover/overlap nerve equal to a triangle `C3` with no triple-overlap constraint, and transition group `C2 = {0,1}`.

There are three overlap edges and hence

`2^3 = 8`

edge transition assignments.

Every assignment is pairwise locally valid.

Define the cycle holonomy by XOR:

`h(e01,e12,e20) = e01 xor e12 xor e20`.

A strict globally synchronized frame exists iff

`h = 0`.

Exact enumeration:

- 4 assignments have `h=0` and globalize strictly;
- 4 assignments have `h=1` and are obstructed.

Equivalently, the strict-effective assignments are exactly the coboundaries of vertex `C2` potentials.

Now forget the base incidence and restriction map labels, retaining only “three local `C2` frame groupoids.” The even datum `(0,0,0)` and odd datum `(0,0,1)` have the same unindexed local groupoid signature, yet one globalizes and the other does not.

Thus a bare/unindexed groupoid description is not Q-sufficient for the global descent predicate.

The presheaf/descent layer repairs it by retaining:

- the three overlap locations;
- the transition attached to each overlap;
- the restriction/cocycle composition;
- the cycle holonomy.

### Direct Q4 relevance

Q4, `RR-1C8E7A4F2B9D6053E126`, already proved at its declared finite framed-overlap scope:

> strict global parallel-frame descent iff fundamental-cycle holonomy is trivial,

with the minimal triangle `C2` obstruction and the exact `8 = 4 + 4` split.

**Gate verdict:** `GROUPOID -> PRESHEAF/DESCENT = JUSTIFIED` for overlap-indexed local-to-global questions.

Important qualification: this does **not** mean every groupoid question must become a presheaf. Q3 and Q7 do not need locality merely because groupoids are useful there.

---

## 7. Sharp stackification criterion

The triangle example also separates two semantic regimes that must not be conflated.

Let vertex gauge transformations act on transition data by

`e_ij -> e_ij xor v_i xor v_j`.

Exact enumeration gives two gauge orbits, each of size 4, classified by cycle holonomy:

- trivial class `h=0`;
- twisted class `h=1`.

### Regime S — strict synchronized frame

The task asks for a single strict global parallel frame.

Then `h=1` is a **real negative answer**, not a missing global object.

Stackification would turn a task-relevant obstruction into an accepted object and therefore change the problem.

**Verdict:** `STACK_WARRANTED = FALSE`.

This is the current Q4 regime.

### Regime T — twisted `C2` torsor/bundle is an accepted global object

Suppose the semantics is explicitly changed: a nontrivial connection/torsor twisting is part of the global object, and objects are classified up to the declared gauge equivalence.

Then all 8 local transition assignments are valid descent data, and the two gauge orbits are the two global isomorphism classes.

The prestack of **globally trivialized frames** is not essentially surjective onto descent data: it sees only the 4 trivial-holonomy representatives. The stack of `C2` torsors repairs this by realizing both gauge classes.

**Verdict:** `STACK_WARRANTED = TRUE`.

### Criterion 7.1 — STACK_WARRANTED

For current finite P000 work, stackification is warranted only if all of the following pass:

1. **LOCALITY:** the question genuinely uses a declared cover/restriction system.
2. **LOWER FAILURE:** a finite groupoid-valued presheaf/prestack has an explicit descent datum not correctly handled at the lower level.
3. **ISO-SEMANTICS:** accepted global equivalence is isomorphism/gauge, not literal equality of chosen representatives.
4. **EFFECTIVITY INTENT:** the missing isomorphism-valued descent datum is declared to represent a legitimate global P000 object.
5. **REPAIR:** the proposed stack makes exactly those intended descent data effective.
6. **NON-ERASURE:** the repair does not quotient away a holonomy/residue/defect that the task declares observable.
7. **MINIMALITY:** no weaker enrichment of the lower level already suffices.

If any item fails, stackification is rejected.

This is the sharp boundary requested by Q8: **nontrivial holonomy does not imply stack; only intended effectivity up to isomorphism does.**

---

## 8. Q1-Q7 map to the lowest sufficient current level

The table maps the **exact completed/current finite theorem**, not every possible successor inspired by it.

| Packet | Exact current question/result | Lowest sufficient level | Why not lower? | Why not higher now? |
|---|---|---|---|---|
| Q1 / PR #883 / `RR-8C52E13D6C3202A25967` | language audit including presentation invariance and canonicality | **GROUPOID** | SET cannot express relabeling/gauge action or canonicality | no locality/descent is needed for the canonicality certificate itself |
| Q2 / PR #892 / `RR-5C9238DB872A93F13D37` | fixed-radius observation map is noninjective: `C8` vs `C4 ⊔ C4`; every fixed radius has a family obstruction | **SET** | nothing lower is needed: it is a fiber/noninjectivity theorem for a set-valued observation map | adaptive-radius/overlap successors may need PRESHEAF, but the completed Q2 theorem does not |
| Q3 / PR #893 / `RR-49FC19221CA5D69B00E6` | lift sections modulo actual primitive-preserving morphisms; `pi_0`, isotropy, empty/nonempty fiber | **GROUPOID** | same section set can have different component structure | restriction/local-cover structure is not part of the exact Q3 theorem |
| Q4 / PR #894 / `RR-1C8E7A4F2B9D6053E126` | local framed overlaps glue strictly iff cycle holonomy is trivial | **PRESHEAF/DESCENT** | unindexed local groupoids lose which transition lives on which overlap/cycle | strict-frame semantics treats nontrivial holonomy as obstruction, so STACK is not yet legitimate |
| Q5 / Draft PR #896 / `RR-3B032EC1AFB283195BE9` | residue ontology under lift/section changes; invariant orbit/profile vs presentation residue | **GROUPOID** | bare residue values do not retain lift-change/gauge orbit | current benchmark is global finite extension data, not local cover descent |
| Q6 / PR #895 / `RR-4B0C6E0CAEE305D5B844` | exact image/representability of fixed radius-one count profile; virtual `(0,3)` and noninjective `(0,8)` | **SET** | fixed image, fiber, and representability predicate are set-level | local restriction-compatible virtual profile successors may need PRESHEAF, but current theorem does not |
| Q7 / PR #897 / `RR-1ECF8B93CCAF6463224F` | natural choices are automorphism-fixed candidates | **GROUPOID** | SET existence/count cannot express automorphism-fixedness | no local restriction/gluing is required for the exact finite naturality theorem |

### The deliberately important non-uniformity

The minimum map is:

`Q1:G, Q2:S, Q3:G, Q4:P, Q5:G, Q6:S, Q7:G`.

That non-uniformity is a success criterion, not an inconvenience. A rule that mapped all seven packets to STACK would fail Q8.

---

## 9. Gen13 map by question signature

Gen13 itself is not assigned one universal categorical level. Its subquestions split.

### SET is enough for

- fixed-model existence of a section/lift;
- finite enumeration of candidate sections;
- a fixed presentation’s raw residue values;
- image/fiber predicates of a fixed observation map;
- exact carrier-relative relation checks.

### GROUPOID is required for

- section/lift classification modulo permitted gauge;
- presentation/model invariance;
- residue orbits under lift change;
- kernel/action information that survives accepted equivalence;
- “canonical / natural / distinguished / preferred” claims.

### PRESHEAF/DESCENT is required for

- slice-indexed or region-indexed local data;
- refinement/restriction consistency;
- overlap transition data;
- local-to-Full-Cell gluing questions;
- cycle/holonomy obstructions whose location in the cover matters.

### STACK is required only conditionally

Only after P000 semantics explicitly accepts locally trivial but globally twisted objects up to gauge/isomorphism as legitimate global objects.

Current strict-frame Q4 does not yet cross this gate.

---

## 10. Upgrade-without-benefit certificates

Q8 requires at least one case where escalation is useless and the correct action is to return to a lower level. There are three.

### 10.1 Q2: stay at SET

The exact theorem is simply that a finite observation map has a nontrivial fiber:

`Obs_r(C_(2m)) = Obs_r(2 C_m)`

for the declared fixed-radius family.

No morphism, cover, or stack datum is required to prove noninjectivity. Recasting the theorem as a stack statement adds verification burden and no task answer.

### 10.2 Q6: stay at SET

The theorem

`representable(t,p) iff t mod 3 = 0 and (p=0 or p>=4)`

at the frozen profile scope is an exact image-membership statement.

SET plus an explicit `REPRESENTABLE` predicate is sufficient.

### 10.3 No current infinity upgrade

All current Q1-Q7 witnesses use:

- finite sets;
- finite groups and action groupoids;
- ordinary invertible 1-morphisms;
- finite restriction maps;
- 1-cocycle / cycle equations.

No current task observable refers to a nontrivial 2-morphism, `pi_n` for `n>=2`, or higher coherence class. Therefore no lower-language failure certificate exists for an infinity-groupoid escalation.

This is a **current finite-strength stop result**, not a ban on future higher structure.

---

## 11. Reasoning cost versus structural payoff

| Level | Extra data retained | Typical exact finite audit | Relative verification burden | Structural payoff |
|---|---|---|---|---|
| SET | elements, equality, maps, fibers/images | enumerate states; T6 fiber constancy | **1 / low** | exact existence, image, noninjectivity, representability |
| GROUPOID | invertible arrows, action, orbit, isotropy | T7 orbit/stabilizer/fixed-point audit | **2 / low-moderate** | removes arbitrary-presentation/canonicality errors |
| PRESHEAF/DESCENT | base incidence, restrictions, overlap transitions | edge/restriction checks + fundamental-cycle holonomy | **3 / moderate** | makes local-to-global obstruction visible |
| STACK | effective descent up to isomorphism | descent groupoid + gauge orbit/effectivity enumeration | **4 / high** | admits legitimate twisted global objects without choosing trivializations |
| higher/∞ language | higher cells/coherences | would require explicit higher witness and checker | **5 / unjustified now** | **0 current incremental payoff** because no Q1-Q7 higher observable exists |

The numerical burden is only an ordinal comparison inside Q8, not a performance benchmark.

---

## 12. `ABSTRACTION_UPGRADE_GATE`

For a proposed upgrade `L -> H`, the Driver should require the following certificate tuple:

`G = (FAIL, REPAIR, MINIMAL, INVARIANT, SEMANTIC, AUDITABLE)`.

### Gate 1 — FAIL

Produce a finite lower-language fiber witness:

`E_L(x)=E_L(y)` but `Ans_Q(x)!=Ans_Q(y)`,

or an explicit descent datum whose global status cannot be recovered after the lower forgetting.

No witness => no upgrade.

### Gate 2 — REPAIR

Prove/check that the higher representation makes the required answer factor:

`Ans_Q = Ansbar_Q o E_H`.

Description alone is insufficient.

### Gate 3 — MINIMAL

Test weaker repairs first:

- add an explicit predicate;
- retain the missing action;
- retain an orbit rather than choose a representative;
- retain restriction maps;
- retain the actual holonomy/defect state.

If one suffices, stop there.

### Gate 4 — INVARIANT

The higher repair must respect all P000-declared equivalences and preserve all load-bearing observables.

### Gate 5 — SEMANTIC

New objects introduced by completion/stackification must be objects the task actually intends to count as global reality, not artifacts added only to make a theorem true.

### Gate 6 — AUDITABLE

There must be an exact finite checker or an explicit proof obligation at the new layer.

### Decision rule

`UPGRADE(L,H,Q) = TRUE`

iff all six gates pass.

Otherwise:

`STOP_AT(L)`.

For `PRESHEAF -> STACK`, Criterion 7.1 is an additional mandatory subgate.

For any future proposed `STACK -> infinity` escalation, add:

`HIGHER_WITNESS`: two states identical after 1-truncation but separated by a task-relevant higher-coherence observable.

No `HIGHER_WITNESS` => reject the escalation.

---

## 13. Formal minimality theorem for the current packet

Let the candidate language levels be ordered operationally by the extra information they retain for a specific question.

For each current Q1-Q7 packet, let `L_Q` be the level in Section 8.

The finite certificates establish:

1. `Q2` and `Q6`: the required answers already factor through SET encodings.
2. `Q1`, `Q3`, `Q5`, `Q7`: SET forgetting loses required automorphism/gauge/naturality information; GROUPOID repairs it.
3. `Q4`: forgetting cover incidence/restrictions loses the strict-globalization predicate; PRESHEAF/DESCENT repairs it by the cycle-holonomy criterion.
4. current Q4 strict-frame semantics fails the semantic/effectivity gate for STACK.
5. the torsor variant passes the stack gate and supplies a finite witness that STACK is a real, non-vocabulary-only level when the semantics actually changes.
6. no current packet passes a higher-coherence gate.

Therefore no single highest language is minimal across the current P000 packet, while the decision rule selects a unique lowest sufficient level for each frozen question signature.

This is precisely the taskbook-valid terminal:

`MINIMAL_ABSTRACTION_GATES_EXACTLY_WITNESSED`.

---

## 14. Remaining residue / limits

1. Q8 classifies the current finite question signatures; it does not prove that all future P000 questions stop at 1-stacks.
2. A future Full-Cell local ontology may introduce genuine higher coherence. If so, the required evidence is a new `HIGHER_WITNESS`, not analogy.
3. Stackification is semantics-sensitive. The same odd `C2` holonomy is:
   - an obstruction for “strict global parallel frame”;
   - a legitimate nontrivial torsor class for “global object up to gauge.”
   These are different problems and must not be silently exchanged.
4. The linear label `SET -> GROUPOID -> PRESHEAF -> STACK` is an operational driver ladder. Mathematically, locality and morphism depth are partly orthogonal axes; Q8 resolves this by letting the presheaf fiber category remain the lowest already-required one.
5. Q1-Q7 packets cited above may still await Driver review; Q8 consumes their finite certificates as research evidence and does not canonically promote them.

---

## 15. Recommended Driver action

Freeze the following publication rule for future P000 taskbooks:

> Before introducing a higher abstraction layer, state the exact question answer, exhibit a finite lower-language fiber failure, prove the proposed higher language repairs that failure, test all weaker enrichments, and verify that the repair preserves P000 observables. For stackification additionally prove that the missing isomorphism-valued descent datum is intended to be a legitimate global object. Otherwise stop at the lower layer.

Recommended machine-readable gate name:

`ABSTRACTION_UPGRADE_GATE_V1`

Recommended hard guard:

`NO_LOWER_LANGUAGE_FAILURE_CERTIFICATE => NO_ABSTRACTION_ESCALATION`
