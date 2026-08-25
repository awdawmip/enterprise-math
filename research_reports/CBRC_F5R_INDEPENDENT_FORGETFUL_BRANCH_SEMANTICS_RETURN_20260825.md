# CBRC F5R — Independent Forgetful-Branch Semantic Replication Return

Status: `CHECKPOINT_A_DRAFT / RAW_MATHEMATICAL_FREEZE_PENDING`
Researcher-ID: `EM-CBRC-F5R-8120F1`
Task: `RS-CBRC-F5R-INDEPENDENT-FORGETFUL-BRANCH-SEMANTIC-REPLICATION`
Owner branch: `research/cbrc-f5r-independent-forgetful-branch-semantics`
Taskbook source: `3015cee704b6864c955bf577637383dd8c3dfd19`

## Source firewall

Mathematics in this draft uses only:

1. `research_inputs/CBRC_F5_BLIND_FORGETFUL_BRANCH_SEMANTICS_PACKET_20260823.md@a107c133e11597623bbe79ef37397fc8ba5c13f7`;
2. `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md@6ec0d73a19e28ec586c59a97d24f5798c9119771`;
3. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@b631242db84c5bd3640e6dc554b19a1d04d464f3`.

No downstream coherent-wave, R063/R064/R065/FQ, rank-two carrier, complex/quadratic carrier, phase group, norm, inner product, square law, or external wave/quantum semantics is used.

## Provisional primary verdict

`F5R_NEW_AXIOM_REQUIRED`.

The candidate

`FORGETFUL_BRANCH_NONDEGENERACY : pi(x) != 0 and pi(y) != 0`

is compatible with the allowed semantics but is not forced by them. A retained marked slot and a concrete Path-formal witness are different types. The allowed sources do not supply a canonical total map from marked slots to concrete Path-formal basis witnesses with nonzero old coefficients.

## Q1 — exact type boundary

### Theorem F5R-TYPE-1

The allowed sources canonically distinguish:

1. a concrete Path-formal witness `[p]`, identified by generator word, prefix trajectory, typed placement and terminal;
2. the formal coefficient multiplying `[p]` in a finite formal `N`-sum;
3. a marked slot in a bookkeeping pair `C ⊕ C`;
4. an enriched coefficient state `x in C` occupying such a slot;
5. the additive forgetful retraction `pi : C -> Z e`;
6. later marker erasure / same-terminal recoalescence.

A marked slot is not, merely by being retained and nonzero in `C`, a concrete Path-formal witness. The bridge gives a concrete basis of path witnesses before coefficient enrichment, while the blind packet introduces marked coefficient slots later and does not identify each slot with a concrete basis witness.

Freeze:

`F5R_PATH_WITNESS_VS_MARKED_SLOT_SEMANTIC_BOUNDARY_CLASSIFIED`.

## Q2 — derivability / independence

### S-A — basis-refinement semantics

If one adds the rule that every retained marked branch refines at least one concrete Path-formal basis witness carrying a nonzero old signed occurrence coefficient, then per-branch nondegeneracy is immediate: each branch has nonzero old projection by the added branch-to-witness rule.

This rule is not present in the allowed sources; it is a strict strengthening.

### S-B — carrier-state semantics

The allowed sources permit the weaker reading that a retained branch is a nonzero enriched state in a typed marked slot. Nonzero in `C` does not imply nonzero under a retraction with nontrivial kernel.

Exact countermodel: let

`C = Z × (Z/2)`

as an additive bookkeeping carrier, embed `e=(1,0)`, and define

`pi(n,t)=n e`.

On `C ⊕ C`, define the reversible additive map

`M_B((n,t),(m,s)) = ((n,t),(m, s + n mod 2))`.

It is an involution. For the elementary input

`((1,0),(0,0))`

it gives

`x=(1,0)`, `y=(0,1)`.

Thus `x != 0`, `y != 0`, `pi(x)=e`, `pi(y)=0`. Total old projection is preserved because the integer coordinates remain `n,m`. Old Boolean support of the total occurrence is preserved. The second marker stores exact reversible enrichment information while carrying no old occurrence coordinate.

Therefore `FORGETFUL_BRANCH_NONDEGENERACY` fails in an exact model satisfying retraction, nonzero enriched outputs, reversibility and total old-coordinate conservation.

### S-C — total-only semantics

The same countermodel satisfies the total-only rule

`pi(x)+pi(y)=e`

while one individual projection vanishes. Therefore total recovery does not imply per-branch recovery.

Freeze:

`F5R_FORGETFUL_BRANCH_NONDEGENERACY_DERIVABILITY_CLASSIFIED`.

## Q3 — load-bearing implication audit

| Condition | Per-branch nonzero follows? | Reason |
|---|---|---|
| Path-formal provenance retention | No, unless strengthened to branch-to-concrete-witness correspondence for every slot | Provenance can remain on the genuinely old-supported branch while a kernel-only marked branch stores enrichment |
| conservative embedding/retraction | No | `pi(e)=e` does not make `pi` injective |
| no-resurrection | No | a `pi=0` branch creates no new old support and is therefore compatible with no-resurrection |
| marker refinement consistency | No | marker identity distinguishes slots; it does not constrain the kernel of `pi` |
| reversibility before marker erasure | No | `M_B` above is an involution |
| typed locality | No | type correctness does not imply projection injectivity |
| total old signed coefficient preservation | No | it implies only `pi(x)+pi(y)=e`; `M_B` has `(e,0)` projections |
| old Boolean support preservation | No | one old-supported branch is enough to preserve the old support |

The only tested principle that directly yields the candidate is the stronger S-A bridge axiom: every retained marked branch must refine concrete old Path-formal support with nonzero old coefficient.

Freeze:

`F5R_BRANCH_SURVIVAL_LOAD_BEARING_AXIOMS_CLASSIFIED`.

## Q4 — strongest derived substitute

There are two exact scopes.

### Source-only scope

From the abstract laws stated for the marked split, the unconditional branch result is only

`x != 0 in C` and `y != 0 in C`.

No nontrivial per-branch theorem about `pi(x)` and `pi(y)` follows from retraction alone.

### Conserving old-coordinate scope

If the separately tested conservation condition

`pi(x)+pi(y)=e`

is imposed, then

`pi(x) != 0 or pi(y) != 0`.

Proof: if both projections were zero their sum would be zero, contradicting `e != 0` in the old signed occurrence coordinate.

This is maximal among natural branch-count strengthening in this scope: `M_B` satisfies conservation but has exactly one zero branch projection, while a reversible conserving model with free-coordinate matrix

`[[2,1],[-1,0]]`

maps `(e,0)` to old projections `(2e,-e)`, showing that the same scope also permits both projections nonzero.

Hence conservation determines neither `both nonzero` nor `exactly one nonzero`; it forces only `at least one nonzero`.

Freeze:

`F5R_MAXIMAL_DERIVED_FORGETFUL_BRANCH_CONDITION_CLASSIFIED`.

## Q5 — rank consequence

The accepted F4 boundary says that a successful torsion-free-rank-one model has a signed-permutation free quotient block, whose first column cannot have two nonzero old-coordinate projections.

Because F5R does not derive two nonzero branch projections from native semantics, no unconditional rank lift follows.

If the new S-A / per-branch nondegeneracy axiom is added, then and only then the F4 boundary gives

`torsion_free_rank(C) >= 2`.

Status:

`CONDITIONAL_ON_NEW_AXIOM`.

The weaker conserving consequence

`pi(x) != 0 or pi(y) != 0`

does not kill the F4 torsion loophole: a signed-permutation first column is compatible with exactly one nonzero old-coordinate projection and one nonzero pure-enrichment/torsion branch.

Freeze:

`F5R_CONDITIONAL_RANK_CONSEQUENCE_CLASSIFIED`.

## Checkpoint-A theorem set

The theorem statements above are stable enough for deterministic model checking and ablation. Final polish, source/target-leak audit, checker digest, manifest, artifact hashes and owner-head freeze remain pending.
