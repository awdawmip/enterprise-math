# R721 — Sharp 18-arc threshold for the five-axis rooted-repair CNB (S_3) carrier

Date: 2026-11-11 (Asia/Shanghai). Research line: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Scope: **exact finite computer-assisted theorem** in the directed V17 triad-permission model; independent author-side research. Review: `UNREVIEWED`.

## Exact model and theorem

Keep the six-axis X6/P000 ontology fixed. This theorem selects five *accessible* axis labels `0,1,2,3,4` within it and studies the ten 3-axis sets `V=binom({0,1,2,3,4},3)`. Let `D` contain all 60 directed Johnson-neighbor arcs `u>v` where `|u ∩ v|=2`. Root at `S=012`.

For each `a∈S`, put `X_a=(S\\{a})∪{3}`, `Y_a=(S\\{a})∪{4}`. Require the nine *specific* directed repair arcs

```
R={ S>X_a, X_a>Y_a, Y_a>S : a in 012 }.
```

A BRC branch is a rooted, labeled, positive-count closed directed walk `T_0=S,T_1,...,T_m=S` in `E⊆D`, obeying cyclic non-backtracking `T_{i-1}≠T_{i+1}` (indices modulo `m`, including the seam). Starting with ordered V17 frame `012`, a step replaces the unique outgoing axis in its own slot by the unique incoming axis, yielding holonomy `h∈S_3`. Write `H_m(E)` for the support of the final ordered frames of all these walks.

**Theorem R721.** Over *all* directed permission graphs `E` in this precise 5-axis carrier that contain the above nine repair arcs,

```
min{|E| : R subset E subset D and H_m(E)=S3 for every integer m>=4} = 18.
```

The bound is sharp. In particular, the 18-arc network of R719q is an **arc-count optimum among all 51 permitted optional directed-arc choices under this mandatory repair-triangle certificate**, not merely inclusion-minimal inside its original list.

## Proof: finite reduction and exact exhaustive certificate

**1. Infinite-to-finite reduction.** By R719q-A, the nine rooted repair arcs let one append a 3-step *identity* triangle to any cyclic non-backtracking rooted closed walk. Choose its omitted root axis different from the at most two axes omitted by the first and last root neighbors. This preserves seam legality and V17 holonomy; appending is injective. Thus `H_m(E)=S3` for all `m>=4` iff the six frames are all reached at the three lengths `m=4,5,6`. Necessity is immediate; sufficiency follows by the `+3` construction and residue classes modulo 3.

**2. Exhaustive witness generation.** Enumerate the 10 combinations of three among five axes and the 60 ordered Johnson arcs. For each of the 18 pairs `(m,h)∈{4,5,6}×S3`, recursively traverse every length-`m` path from `012`, excluding `next=previous-previous`. At depth `m`, retain the path iff the last state is `012`, the last pre-root state differs from the first neighbor, and its slot-frame equals `h`. The recursion traverses **every** legal finite rooted path because each possible next arc is considered and the only discarded branches violate the declared condition. Record for each path only its subset of the **51 optional arcs** used. Duplicate masks may be merged because the proposition is existential support, while original positive BRC branch counts are separately retained.

Full-graph path counts by length, in frame order `012,021,102,120,201,210`:

| m | 012 | 021 | 102 | 120 | 201 | 210 |
|---|---:|---:|---:|---:|---:|---:|
| 4 | 12 | 16 | 16 | 6 | 6 | 16 |
| 5 | 60 | 40 | 40 | 66 | 66 | 40 |
| 6 | 270 | 248 | 248 | 324 | 324 | 248 |

**3. Decision equivalence.** A selected optional-arc mask `A` supports target `(m,h)` iff some recorded witness mask `w` satisfies `w&A=w`. This is exactly equivalent to an admissible path being present: every witness already includes all required arcs in `R`; the optional mask records exactly the other needed arcs. There are no unrecorded arc constraints in this declared combinatorial model.

**4. Exhaustive lower bound.** The standard-library script `R721_MIN_ARC_EXACT_VERIFY.py` searches the exact finite decision problem using a complete recursive certificate. Start with `A=∅`. For any unsatisfied target, branch over **all** witness masks `w` for that target whose union with `A` contains at most eight optional arcs. Recurse with `A←A∪w`. Reject a branch if an unsatisfied target has no feasible witness; succeed only if all 18 targets are supported. Choosing the currently shortest feasible target list merely reorders a complete branching search. Memoizing a selected mask is sound because remaining support depends only on this mask. If an actual feasible solution `A*⊆D\\R` of size at most eight existed, an induction along the recursion could always choose a witness `w⊆A*`; therefore a successful branch would exist. Exhaustion found **no** such branch after **319 distinct visited masks**. This proves that at least nine optional arcs are necessary, hence `|E|>=9+9=18`.

**5. Constructive upper bound.** The explicit R719q graph has exactly 18 distinct arcs, contains all nine repair arcs, and yields the following strictly positive V17 histograms:

| m | 012 | 021 | 102 | 120 | 201 | 210 |
|---|---:|---:|---:|---:|---:|---:|
| 4 | 1 | 2 | 2 | 1 | 1 | 2 |
| 5 | 2 | 1 | 1 | 2 | 2 | 1 |
| 6 | 11 | 2 | 5 | 2 | 2 | 5 |

An independent local JavaScript enumeration also recomputed these six-bin histograms. By step 1, this 18-arc graph supports all six permutations at every length `m>=4`. Combined with step 4, the minimum is exactly **18**.

## Verification and type/observer scope

Primary executable: `R721_MIN_ARC_EXACT_VERIFY.py` (Python standard library, deterministic exact integer/bitset operations). Exact output: `R721_MIN_ARC_EXACT_RESULTS.json`, status `R721_18_ARCS_SHARP_EXACT_PASS`. A second local Node.js enumerator independently reproduced the 319-state lower-bound search and the full R719q histograms. The finite-search proof above specifies why the exhaustive program tests the stated proposition; tests or solver status alone are not substituted for that justification.

The retained carrier is the set of labeled, ordered positive BRC histories with V17 slot transport. The support projection is used **only** for the existential reachability criterion; it is not claimed to preserve multiplicity or provenance under other future observers. The optional-arc mask is an exact certificate for this one declared support interface.

This is a mathematical sharp threshold for a **specified sufficient-certificate family**. The physical/native V29 Link/Port scheduler and inventory may impose additional event permissions and dependencies not encoded in `E`; they remain the next correspondence problem.

## Provenance and continuation

- Parent task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; frozen scientific Source pin `a72226e2430ffa4786321ac86e7f0c599d5f0389` (P000 V5 loaded at this pin).
- Current normative context: Source `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, current account math policy and current `research_priorities/research_method.json`; behavior rules and frozen science have separate scopes.
- Immediate mathematical predecessor: R719q, immutable project commit `421b6ae328fa5ee9509b7b43c0fdd6e3ca46d85a`, `2026-11-11_R719q_sparse_directed_CNB_six_state_certificate.md`; Draft PR #2086.
- Next: determine whether any directed admissible graphs *without* this fixed 9-arc repair gadget can achieve six-state reachability at every length using fewer than 18 arcs; also map the 18-arc candidate into actual native Link/Port/inventory/time rules and inspect permitted-future V39 observational fibers.

Status: `FINITE_COMPUTER_ASSISTED_PROOF_WITH_REPRODUCIBLE_EXHAUSTIVE_CHECK`; independent project review / native admission pending.
