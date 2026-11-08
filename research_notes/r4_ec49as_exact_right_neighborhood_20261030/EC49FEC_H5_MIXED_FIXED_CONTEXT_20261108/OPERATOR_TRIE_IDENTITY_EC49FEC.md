# EC49FEC — Exact weighted operator-Trie identity for native signed-X6 prefix cost

Date 2026-11-08. Author-side exact combinatorial theorem; science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This identity concerns the **literal six-operation frozen model**, independent of H2–H9 quotas and BRC key selection; Source-native admission remains pending.

## Model and theorem

The original operation-to-signed-primitive map is

```
a=(-1,-1)
c=(+1,+2,-1,-2)
d=(+2,+1,-2,-1)
e=(+3,+1,+1,-3)
f=(+1,-1)
g=(+2,-2)
```

These are integer identifiers for signed native axis steps in the fixed X6 primitive coordinate chart, not Euclidean vectors. For a finite set `W` of literal operator words, let `T_op(W)` be its rooted operator-prefix Trie. For every operator-prefix node `v`, let `Ch(v)` denote the set of symbols labelling its outgoing edges; set `ell(s)=len(native(s))`. Define `D_fc(W)` as the number of operator-prefix nodes having both `f` and `c` as outgoing children, and `D_gd(W)` likewise for `g` and `d`.

**Theorem (exact, all finite word sets).**

```
NativeTrieEdgeCount(W)
 = sum_{v in T_op(W)} sum_{s in Ch(v)} ell(s)
   - D_fc(W) - D_gd(W).
```

Thus the native cost is exactly a weighted operator-Trie cost with only **two local one-edge overlap corrections**, at every operator-prefix node. No additional global correction, path-length scaling, or approximation is needed.

**Proof.** The six primitive codewords form a **prefix-free** code. Each has a distinct first primitive step, except the pairs `{c,f}` (both start +1) and `{d,g}` (both start +2). At their second primitive step, each of these two pairs differs: c follows +1 with +2, whereas f follows +1 with -1; d follows +2 with +1, whereas g follows +2 with -2. The codeword e starts +3 and a starts -1. Consequently the only overlaps between distinct codeword prefix sets are exactly one edge each for `{c,f}` and `{d,g}`. Prefix-free unique decoding makes each operator-prefix node correspond to a unique boundary vertex in the signed-native primitive Trie; completing a codeword unambiguously determines its operator prefix. Charge each primitive edge to the unique operator boundary at which the codeword segment containing it starts. Distinct boundary vertices charge disjoint sets of primitive edges, while two child symbols leaving the *same* boundary can share their first primitive edge. Hence each operator-prefix node contributes the sum of its children's primitive code lengths, minus one for each of the two possible shared first-step pairs. Summing gives the claimed exact equality. QED.

A useful equivalent recursive formulation: at each node, add `2*(number of outgoing symbols among a,f,g)+4*(number among c,d,e)`, then subtract indicators `[c and f both present]` and `[d and g both present]`. This directly supports a smaller exact integer/branch-and-bound prefix-sharing objective at the operator level. Completeness still depends on the actual admissible-word enumeration.

## Executed verification and worked exact example

An independent local standard-library Python implementation compared the theorem's operator-Trie objective with the literal union of **all signed-native primitive prefixes** for **29 complete 24-word systems**: 24 exact H5 fixed-context certificates and five separate joint-search witnesses.

Result: **29/29 exact equalities**, minimum constructive system cost **109**. For the explicit 109-edge system recorded in `README_EC49FEC.md`, operator-Trie data are:

```
operator-prefix nodes = 29
sum of raw weighted outgoing operator edge lengths = 116
nodes with both f and c children = 5
nodes with both g and d children = 2
exact native prefix count = 116 - 5 - 2 = 109
```

This identity is a general theorem within the frozen typed six-operation model. The 29 cases are an independent implementation cross-check, not the scope of the theorem.

## Next executable work

Use this identity to build a joint exact weighted operator-prefix integer model over the 108 quota-feasible A×B×C key triples, the early H2/H3 word choices, and H5's twelve mixing-eligible cases. In particular, avoid rebuilding the full signed-native prefix inventory at every candidate search; retain literal BRC key, endpoint and rank constraints as originally required. Test whether the extra mixture flexibility reduces the **complete** H2–H9 cost once all other words may vary.

The mother target remains ≤93 edges with five full BRC keys, and the best known verified complete system remains 94 edges. No formal Source-native CLAIM, Result or independent Driver review was available in this session because `em_status` and `em_control_tasks` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`.
