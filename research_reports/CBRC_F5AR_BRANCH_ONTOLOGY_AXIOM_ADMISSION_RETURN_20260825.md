# CBRC F5AR — Independent Branch Ontology / Axiom Admission Return

Status: `RAW_FREEZE_COMPLETE / CHECKPOINT_A_READY`
Date: `2026-08-25`
Researcher-ID: `EM-CBRCF5AR-7E8B04`
Task-ID: `RS-CBRC-F5AR-INDEPENDENT-BRANCH-ONTOLOGY-AXIOM-ADMISSION-REPLICATION`
Owner branch: `research/cbrc-f5ar-independent-branch-ontology-axiom-admission`

Primary verdict:

`F5AR_ADMIT_RESTRICTED_ELEMENTARY_RULE_ONLY`

Hard target:

`BRANCH_TO_OLD_SUPPORT_FAITHFULNESS_AXIOM_ADMISSION_STATUS_INDEPENDENTLY_CLASSIFIED`

## 0. Frozen source boundary

Mathematical premises used before this raw freeze are exactly:

1. `research_inputs/CBRC_F5A_BRANCH_ONTOLOGY_AXIOM_ADMISSION_PACKET_20260825.md@b904a86aa24ed35564956181a7c1309074a782ea`;
2. `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md@6ec0d73a19e28ec586c59a97d24f5798c9119771`;
3. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@b631242db84c5bd3640e6dc554b19a1d04d464f3`;
4. `driver_reviews/CBRC_F5R_INDEPENDENT_FORGETFUL_BRANCH_SEMANTICS_DRIVER_REVIEW_20260825.md@6e40f56745c405042ad2216d1f62b110312ffb83` only as the accepted semantic boundary.

No missing F5A verdict is reconstructed.

## 1. Typed universe used for the classification

Let `W` be the set of concrete Path-formal witness occurrences. A witness in `W` retains word, prefix trajectory, placement and terminal. The canonical forgetful tower remains

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

The admission problem is about an additional pre-erasure enrichment layer, not about changing the canonical witness fiber.

For the axiom audit, use these separate sorts/predicates:

- `C`: enriched coefficient states;
- `pi : C -> Z e`: old signed-coordinate retraction;
- `B_active`: currently retained marked branch records before marker erasure;
- `coeff(b) in C`: coefficient state carried by branch record `b`;
- `RefOld(b,w)`: branch `b` is explicitly declared to refine old concrete witness occurrence `w`;
- `Parent(b',b)`: `b'` is an immediate refinement child of active branch `b`;
- `Desc(b,w)`: transitive refinement descent from original old witness `w`;
- `SuppOld(b) subset W`: explicit old-witness support metadata when such data are present.

Typing convention used throughout:

`b in B_active => coeff(b) != 0`.

This is a branch-activity convention, not a support-faithfulness axiom. Pure kernel coefficient states may exist in `C` without being members of `B_active`.

After marker erasure/recoalescence, the resulting aggregate is not automatically a member of `B_active`. This type exit is essential for signed-cancellation compatibility.

## 2. Exact formulations

Write `p(b)` for the integer old coefficient defined by `pi(coeff(b)) = p(b)e`.

### A0 — elementary projection nondegeneracy

For every authorized elementary two-branch refinement of one embedded old occurrence `w`,

`RefOld(b1,w) and RefOld(b2,w)`

implies

`p(b1) != 0 and p(b2) != 0`.

Domain: elementary two-child old-occurrence split only.

No witness-support metadata is required.

### A1 — typed branch-to-old-support faithfulness

For every active branch record `b` and old witness `w`,

`RefOld(b,w)`

implies both

`SuppOld(b) != empty`

and

`p(b) != 0`.

The quantifier is over branch records actually typed by `RefOld`. It does not itself assert that every transitive descendant keeps that type.

### A2 — descendant-family faithfulness

For every original old witness `w`, let `Front(w)` be the currently retained descendant frontier attached to that original witness. Then

`sum_{b in Front(w)} p(b) != 0`.

Individual descendants may have zero projection.

This rule requires a descendant-family partition even when direct old-link markers are no longer present.

### A3 — global support-reflecting retraction

For every enriched coefficient state `z in C`,

`z != 0 => pi(z) != 0`.

This quantifies over all enriched states, including states not typed as active branches.

### A4 — arbitrary-depth leafwise refinement faithfulness

For every original old witness `w`, every finite authorized refinement tree rooted at `w`, and every active retained leaf `b` in that tree,

`p(b) != 0`.

Because any internal node can be a leaf at an earlier finite stage, the schema is equivalently: every reachable active branch node at every finite depth has nonzero old projection.

## 3. Strict implication lattice among A0–A4

The exact candidate implications are:

`A1 => A0`.

`A3 => A4 => A0`.

No other implication between distinct members of `{A0,A1,A2,A3,A4}` holds from the frozen semantics.

Thus the candidate Hasse picture is:

```text
A1          A3
 |           |
 |          A4
 |           |
 +---------->A0

A2 is incomparable with A0, A1, A3 and A4.
```

The arrow from `A1` to `A0` uses only that elementary children are explicitly `RefOld`-typed.

The arrow `A3 => A4` uses `B_active => coeff(b) != 0`.

### 3.1 Failed converses and exact countermodels

The countermodel packet materializes all witnesses. The minimal structural witnesses are:

- `A0 !=> A4`: one binary depth-2 comb, 5 branch-tree nodes total. Root splits to `(1,1)`; one child then splits to `(1,0)`. A0 sees only the first split and passes; A4 fails at depth 2.
- `A1 !=> A4`: same 5-node model. The first-generation children are `RefOld`-typed and faithful; the zero-projection grandchild is only `Parent`-typed because no hereditary old-link law exists.
- `A4 !=> A1`: one root plus two faithful depth-1 branches is enough; give one branch nonzero projection but no `SuppOld` data.
- `A4 !=> A3`: one root plus two faithful active branches, together with one off-branch pure-kernel state `k != 0`, `pi(k)=0`.
- `A1 !=> A3`: same off-branch kernel construction.
- `A3 !=> A1`: all coefficient states have nonzero old projection, but one directly old-linked branch lacks explicit old-witness support metadata.
- `A0 !=> A2`: two elementary branch projections `(1,-1)` are individually nonzero but have zero family sum.
- `A2 !=> A0`: F5R kernel witness pattern `(1,0)` has nonzero family total but one zero-projection active child.
- The same two 3-node models show that A2 is incomparable with A1, A3 and A4.

## 4. Strictly intermediate rules discovered

### 4.1 Projection-only typed old-link faithfulness `A1pi`

Define

`A1pi: RefOld(b,w) => p(b) != 0`.

Then

`A1 => A1pi => A0`

and

`A3 => A1pi => A0`.

Both converses fail:

- `A1pi !=> A1` by omitting support metadata while retaining nonzero projection;
- `A1pi !=> A3` by allowing an off-branch pure-kernel state.

`A1pi` is the exact projection clause of A1 stripped of the ontology-costly witness-support field.

### 4.2 Finite-depth hierarchy `D_d`

For every integer `d>=1`, define

`D_d := every active descendant branch of depth <= d has nonzero old projection`.

Then

`D_1 = A0`

for binary elementary old-occurrence refinement, and

`A4 = forall d>=1, D_d`.

For every `d>=1`,

`D_{d+1} => D_d`

strictly.

Smallest binary-comb witness to `D_d !=> D_{d+1}` has `2d+3` total tree nodes: all projections through depth `d` are nonzero and exactly one child first becomes zero at depth `d+1`.

Therefore there is an infinite strict finite-depth ladder between A0 and the all-depth schema A4. No finite-depth validation can prove A4.

### 4.3 Hereditary refinement transport `H`

`H` is not itself a projection axiom. It is the missing ontology/composition rule:

If `b'` is a retained child of `b` and `b` belongs to the refinement genealogy of old witness `w`, then `b'` inherits the same old-root genealogy in a serialization- and marker-independent way.

Equivalently, there is a root map

`rho : B_active -> W`

preserved by authorized refinement:

`Parent(b',b) => rho(b') = rho(b)`.

If `A1pi` is required uniformly on every active record carrying `rho`, then induction gives A4.

Without `H`, A1 does not imply A4.

### 4.4 Total old-coordinate conservation `Csum`

For every split parent `b` with children `b_i`,

`sum_i p(b_i) = p(b)`.

With a nonzero root coefficient and a preserved descendant-family partition, `Csum` implies A2.

It does not imply A0 or A4: `(1,0)` is conserving for root coefficient `1`.

A0/A4 do not imply `Csum`: `(1,1)` closes the zero-child loophole but does not conserve root coefficient `1`.

Thus conservation is orthogonal to per-branch faithfulness.

## 5. Canonical BRC consistency

### 5.1 Concrete Path-formal branching and N augmentation

A0, A1, A4 and A1pi act only on the extra enriched active-branch layer. They do not alter:

- Path-formal words;
- prefix trajectories;
- placements;
- typed terminals;
- shuffle fibers;
- N augmentation;
- Boolean support.

The canonical `(1,1)` commuting diamond remains exactly two distinct witnesses,

`XiXj` and `XjXi`,

with one common typed terminal and one common trace class.

No candidate requires identifying a marked coefficient slot with a concrete path witness.

### 5.2 Exact conservative extension model

For any old signed coefficient `n != 0`, take an enrichment carrier containing pairs `(n,k)` with an arbitrary kernel tag `k`.

On an active branch split use old projections

`n -> (2n,-n)`.

Then:

- both children have nonzero old projection;
- the old total is conserved: `2n + (-n) = n`;
- the rule can be repeated at every depth;
- kernel tags may be carried on either faithful child;
- pure-kernel states `(0,k)` may still exist off `B_active`.

Thus A0 is consistent with total conservation, and the hereditary version is consistent with A4.

Adding support metadata `SuppOld(child)={w}` yields an A1-compatible extension whenever a direct `RefOld` declaration is present.

This extension leaves the canonical Path/N/Boolean layers unchanged.

### 5.3 Signed cancellation and recoalescence

Take two individually faithful pre-erasure branches with projections `+a` and `-a`.

Both satisfy A0/A1/A4/A1pi locally.

After same-terminal recoalescence and marker erasure their old aggregate may be exactly zero.

This is compatible because the recoalesced aggregate is not automatically re-declared an active retained branch.

Therefore:

`PRE_ERASURE_BRANCH_FAITHFULNESS != POST_RECOALESCENCE_AGGREGATE_NONZERO`.

A3 also permits exact cancellation when the aggregate is the zero state, but A3 additionally forbids nonzero pure-kernel aggregates and all other nonzero kernel states.

A2 is not cancellation-neutral. If the cancelling branches lie in one still-retained descendant family, A2 forbids their zero family sum. It is compatible only after adding a narrower family/conservation convention that excludes that situation, so it is not suitable as the generic cancellation-compatible faithfulness rule.

### 5.4 Same-terminal recoalescence and marker erasure

Branch markers distinguish active pre-erasure records. Recoalescence may sum coefficients. Marker erasure terminates the domain of the branch-faithfulness predicate.

If one instead insists that a zero recoalesced aggregate remain typed as an active retained branch, A0/A1/A4-style faithfulness and exact signed cancellation become inconsistent.

Hence the type-exit rule at recoalescence is a necessary compatibility boundary.

### 5.5 Translation and relabeling

A0/A1pi/A4 depend only on authorized refinement type and `p(b)!=0`, not on spatial origin, marker spelling or branch ordering.

They are invariant under:

- translation of the typed native skeleton;
- permutation/relabeling of branch markers;
- serialization order of independent refinements.

Support metadata in A1 is invariant only if it is transported as witness identity/provenance rather than reconstructed from marker names after erasure.

## 6. Composition and arbitrary refinement closure

### Theorem 6.1 — A0 alone does not imply A4

The depth-2 5-node comb is an exact countermodel.

The first split has projections `(1,1)`, so A0 holds.

Refine the first child into `(1,0)`. The zero grandchild violates A4.

No canonical source makes the second split another direct old-occurrence split, so A0 has no premise there.

### Theorem 6.2 — exact necessary and sufficient projection closure

Fix the class of finite refinement trees generated solely by authorized active-branch splits.

The following are equivalent as projection properties:

1. every reachable active branch node has nonzero old projection;
2. every active leaf in every finite refinement tree has nonzero old projection;
3. the local hereditary schema holds: whenever a reachable active parent has nonzero old projection, every retained child of every authorized split has nonzero old projection.

Proof:

- `(1)=>(2)` is immediate.
- `(2)=>(3)`: take any reachable parent and extend its history by exactly one split. The children are leaves of that finite extended tree, so each is nonzero.
- `(3)=>(1)`: induction on depth from the nonzero old root.

This is the exact closure content of A4.

### Corollary 6.3 — ontology needed to derive A4 from typed A1

A1 applies only where `RefOld` is declared. To reuse its projection clause at arbitrary depth, the system must add either:

- a persistent root-witness map `rho` inherited by every child; or
- an equivalent functorial branch-to-parent genealogy making every reachable child eligible for the same local rule.

Without such data, A1 does not propagate.

Thus arbitrary-depth closure is not obtained for free from the present branch ontology.

### Regrouping / contraction / expansion

- Structural contraction back to an already existing faithful ancestor preserves the rule.
- Expansion by a hereditary faithful split preserves the rule.
- Pure reassociation/reordering of branch records preserves the rule.
- Arithmetic recoalescence that sums branches is different from structural contraction. It may yield old aggregate zero and therefore must exit the active-branch type if signed cancellation is to remain legal.
- Marker renaming and serialization order do not matter if genealogy is structural rather than name-based.

Deliverable:

`F5AR_REFINEMENT_COMPOSITION_CLOSURE_CLASSIFIED`.

## 7. Minimal F4-loophole closing rule

The F4 elementary loophole is exactly an authorized active two-child old-occurrence split with old-projection pattern

`(nonzero, zero)`

up to branch relabeling.

Consider the class of marker-relabeling-invariant rules whose observable elementary data are the two old projections.

A rule closes the loophole iff it excludes every elementary pair with either coordinate equal to zero.

The weakest such predicate is exactly

`p1 != 0 and p2 != 0`.

That is A0.

Proof of minimality:

If a strictly weaker marker-symmetric predicate does not imply A0, it admits an elementary pair with some zero coordinate. Relabel the two branch markers if necessary. The admitted pair then has form `(n,0)` with `n!=0` whenever the old total/support condition keeps at least one old component alive. Hence the F4 kernel-branch loophole survives.

Concrete weaker rules that fail:

- both enriched outputs are nonzero;
- at least one old projection is nonzero;
- nonempty family old support;
- A2 family-total nonzero;
- total old-coordinate conservation;
- concrete-witness support without nonzero signed projection.

A0 still permits:

- nonzero kernel tags attached to old-supported active branches `(n,k)` with `n!=0`;
- pure-kernel states `(0,k)` outside the active-branch type;
- later exact signed cancellation after marker erasure.

### A3 is unnecessarily strong

The conservative extension above satisfies A0 and, with hereditary reuse, A4. It also contains a nonzero off-branch pure-kernel state `(0,k)`.

A3 rejects that model solely because `pi(0,k)=0`.

Therefore A3 removes states that are irrelevant to the elementary loophole and is strictly stronger than required.

Deliverable:

`F5AR_MINIMAL_LOOPHOLE_CLOSING_RULE_CLASSIFIED`.

## 8. Conservativity and ontology cost

### A0

Base-theory effect: none on existing Boolean/N/Path-formal theorems.

Concrete path witnesses forbidden: none.

Path counts / typed terminals changed: no.

Enriched-model effect: restricts which two output states may be declared active branches of one elementary old occurrence.

New data: no additional support set is needed beyond the already typed elementary event.

Noncanonical choice: none if the event typing is fixed.

Future coefficient obligation: elementary old-refining branch outputs must project nontrivially.

Ontology cost: low.

### A1

Base-theory effect: none if added only to the enrichment layer.

Concrete path witnesses forbidden: none.

New data: yes, explicit nonempty `SuppOld` for every `RefOld` branch.

Noncanonical choice risk: real after regrouping/recoalescence unless provenance is retained rather than reconstructed.

Future coefficient obligation: every directly old-linked active branch must have nonzero projection and witness support.

Ontology cost: medium/high.

### A2

Base-theory effect: none at the raw Path/N/Boolean level, but it constrains enrichment/refinement histories.

New data: persistent descendant-family partition by original witness.

Noncanonical choice risk: high under regrouping and same-terminal merging.

Cancellation: not neutral for same-family signed cancellation.

F4 loophole: not closed.

Ontology cost: high relative to utility for this gate.

### A3

New metadata: little.

Carrier restriction: maximal among candidates; every nonzero kernel state is forbidden.

Existing canonical path counts and terminals: unchanged.

Enriched-model conservativity: fails for the accepted F5R kernel witness and for otherwise harmless pure-kernel extensions.

Future coefficient obligation: every future enrichment must have zero kernel.

Ontology cost: algebraically/global rather than metadata-heavy, and unnecessarily high.

### A4

Base-theory effect: none if refinement genealogy is extra structure.

New data/structure: arbitrary-depth refinement genealogy or an equivalent hereditary local schema.

Noncanonical choice risk: low if the tree is retained structurally; high if genealogy must be reconstructed after erasure.

F4 loophole: closed.

Future coefficient obligation: every active descendant leaf at every finite depth must project nontrivially.

Ontology cost: medium/high.

### Exact conservativity statement

A0 is conservative over the existing canonical Boolean/N/Path-formal BRC theory in the model-extension sense:

For every canonical concrete path-witness structure, one can add an enrichment/branch layer satisfying A0 without changing any object, relation, path count, augmentation value, Boolean support or typed terminal in the base structure.

A0 is not conservative over the class of all previously allowed enriched models, because it deliberately removes the F5R kernel-active-branch model. That is the intended new-axiom effect.

The same base-theory conservativity is available for A1/A4 via the explicit extension model, but with additional ontology.

Deliverable:

`F5AR_CONSERVATIVITY_AND_ONTOLOGY_COST_CLASSIFIED`.

## 9. Mandatory ablation conclusions

| Ablation | Loophole closure | Conservativity / ontology effect | Signed cancellation | Interpretation |
|---|---|---|---|---|
| remove active-branch type restriction | still closes if global nonzero projection is imposed | degenerates toward A3 and kills harmless off-branch kernel states | exact zero cancellation still possible, but nonzero kernel residue forbidden | overstrong |
| remove concrete-witness support data | unchanged for projection-only A0/A4 | cheaper and more conservative | preserved | support metadata is not needed for F4 closure |
| remove nonzero signed old projection | fails | support-only branch ontology permits kernel-only active branch | preserved but loophole reopens | fatal |
| remove leafwise closure | elementary F4 closure remains | cheaper | preserved | A0 remains, A4 lost |
| remove descendant-family closure | elementary/leafwise projection closure unchanged | cheaper | improves neutrality to same-family cancellation | A2 not needed |
| remove total old-coordinate conservation | A0/A4 unchanged | broader model class | more flexible | conservation orthogonal to zero-child exclusion |
| remove signed-cancellation compatibility | loophole may still close | permits overstrong family/nonzero-aggregate rules | lost | unacceptable for canonical signed completion |
| remove translation/relabeling covariance | may close only chosen labels/locations | noncanonical | depends on names/order | unacceptable |
| remove composition/refinement functoriality | elementary closure only | cheaper | preserved | A0 no longer propagates to A4 |

## 10. Admission verdict

The weakest exact marker-symmetric rule that closes the actual F4 elementary pure-enrichment loophole is A0.

A1 adds witness-support ontology that is not needed for that closure.

A4 adds arbitrary-depth genealogy/closure that is not derivable from A0 or A1 without new hereditary refinement structure.

A2 does not close the loophole.

A3 closes it but is globally overstrong because it forbids pure-kernel states outside the active-branch type.

Therefore the independent admission verdict is:

`F5AR_ADMIT_RESTRICTED_ELEMENTARY_RULE_ONLY`.

Admitted content:

> An authorized elementary two-branch refinement of one embedded old concrete occurrence may declare both outputs active retained old-refining branches only if each output has nonzero old signed projection.

Non-admitted extensions:

- no automatic witness-support field is mandated;
- no arbitrary-depth A4 theorem is claimed without hereditary branch genealogy;
- no descendant-family nonzero aggregate is required;
- no global kernel elimination is imposed;
- no Foundation-wide promotion is made by this task.

This rule is a narrow ontology gate on what may be called an active elementary old-refining branch. It is not derived from prior BRC semantics; it is admitted because it is the exact minimal typed exclusion, is base-theory conservative, is composition-neutral when kept elementary, is translation/relabeling invariant, preserves off-type enrichment, and preserves post-erasure signed cancellation.

## 11. Conditional consequence required by the taskbook

Because the admitted restricted rule forces both elementary old projections nonzero, the already accepted conditional consequence may be stated, without using it as a selector:

`GLOBAL_ZERO_SEPARATION + ADMITTED_BRANCH_FAITHFULNESS => torsion_free_rank(C) >= 2`.

Status:

`CONDITIONAL_THEOREM_ONLY`.

No rank-two carrier is constructed or classified here.

## 12. Deliverable labels

`F5AR_BRANCH_FAITHFULNESS_AXIOM_LATTICE_CLASSIFIED`.

`F5AR_CANONICAL_BRC_CONSISTENCY_CLASSIFIED`.

`F5AR_REFINEMENT_COMPOSITION_CLOSURE_CLASSIFIED`.

`F5AR_MINIMAL_LOOPHOLE_CLOSING_RULE_CLASSIFIED`.

`F5AR_CONSERVATIVITY_AND_ONTOLOGY_COST_CLASSIFIED`.

`BRANCH_TO_OLD_SUPPORT_FAITHFULNESS_AXIOM_ADMISSION_STATUS_INDEPENDENTLY_CLASSIFIED`.

Primary verdict:

`F5AR_ADMIT_RESTRICTED_ELEMENTARY_RULE_ONLY`.

Stop boundary remains: no F6, no rank-two construction, no downstream coherent-wave comparison, no Foundation promotion.
