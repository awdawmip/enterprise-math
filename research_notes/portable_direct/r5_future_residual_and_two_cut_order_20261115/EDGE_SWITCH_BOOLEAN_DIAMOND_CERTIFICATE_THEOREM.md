# R5 — Exact edge-switch certificate for two-cut optimizer diamonds

**Date:** 2026-11-15. **Evidence:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.  
**Lineage:** frozen source science `435e77af0d180eac32bd1f9c4c464bc4010b7551`, author-side R5 Draft PR #2427. This is a result about **finite labeled optimizer path languages**; when applied to the R5 954-event integer-line model it remains an auxiliary derived observer, not native X6 geometry.

## Theorem — exact local graph criterion

Let `G0,Ga,Gb,Gab` be finite directed acyclic graphs using a **common labeled vertex universe**, common single source `s` and sink `t`. Every graph is trimmed to its accepting source–sink paths, and accepting paths are injectively identified with labeled optimizers. Assume

```
L(G0) ⊆ L(Ga) ∩ L(Gb) ⊆ L(Ga) ∪ L(Gb) ⊆ L(Gab).
```

For clarity, adjoining source→first-rank and last-rank→sink edges makes path start/end membership explicit. Write `E0,Ea,Eb,Eab` for the resulting sets of identically labeled edges. The path-family residuals are `P=(La∩Lb)\\L0` and `Q=Lab\\(La∪Lb)`.

**Intersection criterion.** Form the graph with edge set `Ea∩Eb`, then trim it again to edges lying on some `s→t` path. Let the retained edge set be `Eint_trim`. Then

```
P = empty  iff  Eint_trim ⊆ E0.
```

**Joint-only criterion.** Classify every edge of `Gab` into (i) A-and-B, (ii) A-exclusive `Ea\\Eb`, (iii) B-exclusive `Eb\\Ea`, or (iv) **neutral**, outside `Ea∪Eb`. Then

```
Q = empty  iff
  (Eab \ (Ea∪Eb) = empty)
  AND
  (no s→t path of Gab contains both an A-exclusive edge
   and a B-exclusive edge, in either order).
```

Consequently the Boolean optimizer diamond holds if and only if **both** criteria pass. The joint criterion has two genuinely distinct failure mechanisms: a newly admitted edge, or a mixed-color path composed exclusively of already singly admitted edges.

### Proof

Common labeled path acceptance means that a path is accepted by both `Ga,Gb` exactly when each of its edges lies in `Ea∩Eb` (including source and sink arcs). Trimming the intersection removes edges unrelated to such paths. If a retained edge is not old, some accepted intersection path contains it and cannot be old. Conversely if all retained edges are old, each intersection path is a valid old path. Since `L0⊆La∩Lb`, this proves the P criterion.

If an `Eab` edge is neutral, graph trimming supplies a joint accepting path through it; that path belongs to neither single-cut graph, proving nonempty Q. In the absence of neutral edges every joint path consists only of edges in A or B. It belongs to both if all edges are common; belongs only to A if it has A-exclusive but no B-exclusive edge; belongs only to B in the symmetric case. It belongs to neither **exactly if** it contains edges of both exclusive colors. This proves the Q criterion.

A forward reachability search from `s` and a backward search from `t` implement `Eint_trim`. A 4-state finite automaton propagated along the joint DAG, with bits “seen A-exclusive” and “seen B-exclusive”, tests mixed-color reachability. With hash-set edge membership, the certificate has `O(|V|+|E0|+|Ea|+|Eb|+|Eab|)` primitive operations and bounded 4-fold state width. Large integer path counts are not needed for the **yes/no** result. This is not a bit-complexity claim about constructing the optimal DAGs from the original geometry.

## Exact tests and new structural observation

The executable `VERIFY_R5_EDGE_SWITCH_CERTIFICATE.py` imports the existing frozen `VERIFY_R5_JOINT_CLOSURE_OFFLINE.py` generator and the new `VERIFY_R5_FIVE_TYPE_CARRIER.py` count verifier. It checks both graph criteria against the direct five-type signature counts, without enumerating the enormous R5 optimizer families.

**Frozen 954-event model:** all **64** configurations (K=214..221, eight effective backgrounds with cuts 8 and 9 initially open) give `P=Q=empty`. More strongly, in **all 64 cases both exclusive edge colors actually occur**, but **no jointly optimal path switches between their colors**, and no joint edge falls outside their union. This explains the earlier Boolean diamond as a *path compatibility* property, not the mistaken assertion that one of the cuts adds nothing. Across the 64 checks, the largest joint optimizer DAG contains 2,183 edges including synthetic boundary arcs. Direct five-type path counts and this graph-level yes/no certificate agree in all cases.

**Geometric small counterexamples:** the previously saved 4-event example fails the intersection criterion, while its joint criterion passes; the 5-, 6-, and 8-event examples have joint-only optimizers and **neutral joint edges**. The 8-event scalar cancellation example also fails the intersection criterion. The precise small inputs and prior exhaustive enumeration are preserved in `TWO_CUT_RESIDUALS_THEOREM_AND_GEOMETRIC_COUNTEREXAMPLES.md`.

**Independent graph-only switching witness:** Let the old language be `{(2,4,8)}`; let `La=old∪{(0,3,6)}`, `Lb=old∪{(1,3,7)}`, and let `Lab` additionally contain `(0,3,7),(1,3,6)`. Take the rank-labeled graphs induced by these paths. Every joint edge belongs to `Ea∪Eb` — **there are zero neutral edges** — yet the two crossed paths each combine an exclusive edge of each color. Thus `P=empty`, `|Q|=2`, and the mixed-color criterion detects the failure. This is a synthetic labeled DAG example and **not** asserted to be realizable as a radius-two geometric contraction configuration.

These tests distinguish edge-level signature preservation from simple scalar path count cancellation. The Boolean diamond's native transfer to an X6 slice remains unclaimed.

## Reproducibility and limits

Run `python VERIFY_R5_EDGE_SWITCH_CERTIFICATE.py` in the committed folder, with its two adjacent dependency scripts unchanged. It emits `PASS_EXACT_R5_EDGE_SWITCH_CERTIFICATE`. The local output contains 64 full edge-certificate rows plus the abstract switching witness, 19,982 UTF-8 bytes, SHA-256 `05a1bdab8e35031f7015ebbe7a93e672b8bd0f2bc92fd173e240a4eae5144a97`. An independent longer implementation separately reproduced all 64 graph counts and all four small geometric cases.

Critical assumptions: the graphs must be path-trimmed and share exact edge labels, the start/end edges must be included, and no different source–sink paths may be interpreted as the same center-set optimizer without proven quotient injectivity. An auxiliary graph extracted from a coarse observer without these properties does not justify this certificate.

**Next question:** derive *geometric* constraints (gap-support separation, bounded influence intervals, rank-consistent subgraphs) that force the two edge criteria, instead of merely checking them after optimizer-DAG construction; construct a radius-two indexed-center counterexample where Q arises **only** through mixed singly admitted edges (no neutral edge), or prove that this specific geometric model forbids such a phenomenon.
