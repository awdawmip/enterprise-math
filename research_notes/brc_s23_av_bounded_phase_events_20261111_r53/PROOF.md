# R53 — Exact bounded-memory labelled phase events; semiconvergent-only obstruction

Status: author-side proof and exact finite execution, 2026-11-11. Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor: R52 Draft PR #2018 @ `032d035bd320af17022bc36023e36567d3bc14c6`.

## Defined mathematical object

Fix irrational `0<theta<1`, historical phase labels `z=0,...,m-1` at `p_z={z theta}`, history intervals `I_z` beginning at `p_z`, and ages `1<=r<=H`. Observation phase `x` assigns age `r` to the interval containing `{x-r theta}`. Keep the *complete* owner array `owner_x(r)`, the per-label age membership `M_x(z)`, and youngest-age readout `A_H(x)[z]=min M_x(z)` or empty. The object is an auxiliary irrational rotation; it is not asserted to implement native Heartbeat X6 dynamics.

### Theorem R53-B: exact indexed age-state sweep

Assume the exact descending circular order of cuts `p_s`, for `1<=s<=m+H-1`, and one correctly classified starting state. For each original historical label, maintain an ordered set of its member ages. Across a descending crossing of `p_s`, perform, for each `z` such that `1<=s-z<=H`, the move `r=s-z: z -> pred(z)`. Delete `r` from the source label and insert the *same indexed node* into the predecessor's ordered set. All subsequent source partitions, source identities and age vectors are exact, and the total live age-node count is always exactly `H`. With `m` root pointers, `H` indexed nodes and `H` owner entries, space is `O(H+m)` words, irrespective of the number of cuts traversed.

**Proof.** R52's incidence theorem states that the crossing sources are exactly the distinct pairs satisfying `z+r=s`. Thus every crossed source is removed from its prior set and inserted exactly once into the correct next set. Uncrossed source identities and memberships remain unchanged. This maintains the bijection between all `H` source ages and their single owner sets, inductively across every cut. The minimum age in each set equals its youngest-source readout, and empty sets are represented by null roots. There is one reusable node for each age, and no historical heap entries need be retained. QED.

The executable implementation uses one indexed treap node per age, arrays of child pointers, a random fixed 128-bit priority per age, `m` roots, and the original age-owner array. Deleting a node resets its child pointers; inserting reuses the same node, including when an age revisits a label. Exact structure checks detect duplicate/missing members, owner discrepancies, BST order and priority violations. For a fixed phase/crossing sequence independent of independently sampled treap priorities, expected insertion/deletion cost is `O(log H)` pointer operations; the fixed-seed reproducible run does not turn that expectation into a worst-case theorem. Worst-case treap height is `H`. Node and label indices take `O(log(H+m))` bits; a 128-bit priority is stored per age.

**Full algorithmic costs:** historical-phase sorting `O(m log m)` comparisons, requested cut generation (the independent verifier uses sort `O(K log K)` or heap top-d `O(K log d)`, `K=m+H-1`), initial age classification `O(H log m)`, treap initialization expected `O(H log H)`, `E` event moves expected `O(E log H)`, and `Omega(m)` for each fully emitted age vector. The precise arithmetic/precision, cut-order oracle and verification costs remain separately charged. R51 Floor Sum rank/select is an alternative cut oracle without changing this event theorem.

### R53-A: exact non-semiconvergent upper-phase witness

Let `theta=sqrt(2)-1`, `K=12`, and `eps_s=ceil(s theta)-s theta`. The seven smallest strictly increasing gaps have original indices:

```text
12, 7, 2, 9, 4, 11, 6
```

The first four errors are `17-12sqrt(2)`, `10-7sqrt(2)`, `3-2sqrt(2)`, `13-9sqrt(2)` respectively, strictly increasing. The continued fraction `[0;2,2,2,...]` has convergent denominators `1,2,5,12`; its intermediate semiconvergents through this range also include `3,7`, but **not 9**. Indeed the upper-gap record denominators on `1<=s<=12` are only `1,2,7,12`, and `eps_9>eps_7`. Therefore enumerating just upper semiconvergents or upper best-error records omits the **fourth-ranked** positive upper phase. The exact identity `eps_9=eps_7+eps_2` follows from `9=7+2` and these numerators, suggesting a next additive candidate route whose global completeness remains open.

### Exact finite evidence and certification

The full executed `VERIFY_R53.py` in the research handoff computes using standard-library integers and a common rational enclosure. For S23 the frozen envelope is `(262204504569236716045286,262204504569236716045287,10^24)`; the quadratic envelope is `(floor(10^30 sqrt(2))-10^30, floor(10^30 sqrt(2))+1-10^30, 10^30)`, formed using exact `isqrt` and strict square inequalities.

For every tested cell, an independently reconstructed owner map from modular phase comparisons matches the treap, while historical interval/cut ordering and **all** checked source memberships match *both* enclosure endpoints. Every live node/owner invariant and each youngest-age vector is checked. Six cases: 486 phase cells, 29,945 moves; S23 full 352-cell atlas has 28,672 moves, 290 complete vector changes, and 225 fixed live source nodes. The `H=99,993` experiment checks five rightmost cells, with 32 postinitialization moves and complete initial classification of all 99,993 ages. The 12-cut quadratic witness is exhaustively checked.

The remote compact reproducibility script implements the same indexed-node method for the main cases; the larger executed original script and the complete numerical JSON certificate are in the accompanying research bundle. Local diagnostics are not a controlled hardware benchmark.

### Native scope and next question

BRC applicability assessment: the selected computation is an external circle-rotation source-membership model, not a native BRC positive-weight arithmetic problem. Preserve source identity, original historical labels, multiplicity and future-observer-relevant membership. P000 remains locked. Native task CLAIM/Result/Review and independent mathematical review were not granted by these author-side computations.

R54: prove completeness for a top-k upper-phase candidate generator containing nonrecord sums (or exhibit an exact further obstruction), connect the fixed-node sweep to a declared finite S23 Farey-stage risk observer, and compare whole-program bit complexity including phase ordering, precision and output.
