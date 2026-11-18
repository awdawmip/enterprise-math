# EC49FDE addendum — original H2/H3 multiset-preserving reorders do not lower 112

**Date:** 2026-11-07. **Scientific baseline pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Changed late key:** `M'=(6,4,1)`; `L=(4,2,1)`. **Status:** AUTHOR_EXACT_FINITE_DP / UNREVIEWED / NOT_ADMITTED.

Previously [EC49FDE](README_EC49FDE.md) proved exact 112 when H2/H3's four literal words were fixed and H4–H9's twenty signatures were variable.

Now permit **each H2/H3 slot to take every permutation of its original operation multiset which preserves its nine-state endpoint signature**, while keeping H4–H9's complete changed-key pools. Direct enumeration gives:
- `2:16` multiset `{f,e}`: only `fe`; `2:32` `{g,e}`: only `ge`.
- `3:16` multiset `{f,e,g}`: `feg`, `fge`; `3:32` multiset `{g,e,f}`: `gef`, `gfe`.

This produces **22 freely selected labels**, while only the two H2 slots are fixed. The fixed native signed-prefix union has **12 edges**. The exact Trie incorporates **4,376 labelled words** and **26,705 nodes**. Using the same proven disjoint-label Trie recurrence as [SPARSE_PREFIX_TRIE_DP.cpp](../EC49FDD_FULL_H4_H9_20_SLOTS/SPARSE_PREFIX_TRIE_DP.cpp), a locally compiled `g++ -O3 -std=c++17` C++ implementation returned:

```json
{"trie_nodes":26705,"labels":22,"fixed_edges":12,
"new_edges_optimal":100,"total_exact_optimum":112,
"inspected_pairs":1091650576,"compatible_pairs":112832567,
"peak_states":4194304,"cap":150}
```

An independent cap-111 run found no full-label-mask state:
```json
{"trie_nodes":26705,"labels":22,"fixed_edges":12,
"new_edges_optimal":-1,"total_exact_optimum":-1,
"inspected_pairs":1091585040,"compatible_pairs":112831991,
"peak_states":4194048,"cap":111}
```

The existing 24-word 112-edge assignment attains the upper bound. The exhaustive label-mask dynamic program proves the matching lower bound, establishing **112 exactly even when original H2/H3 multisets may be reordered**.

**Exact reproduction:** From the frozen `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py`, generate H4,H5 pools using `L=(4,2,1)`, H6–H9 pools using `M'=(6,4,1)` with count laws stated in the EC49FDE README, and add the two H3 signature pools `{'3:16':['feg','fge'],'3:32':['gef','gfe']}`. Use the standard published `BUILD_EC49FCZ_TRIES.py` builder logic and `SPARSE_PREFIX_TRIE_DP.cpp` recurrence, with H2:16=`fe` and H2:32=`ge` fixed. Existing signed primitive expansion and nine-state observer are unchanged. The exactly executed trie data is retained in the local evidence bundle.

**Next:** Investigate a typed early-key change outside these original operation multisets or a new admissible operation word. The 93-edge mother question remains open; this addendum only covers the stated 22-variable finite language.