# EC49FNQ — Exact triple-stable exchange plateaus in the frozen native-BRC seven-cache family

Date: 2026-11-13. Status: **author-side exact finite postprocessing, NOT_REVIEWED**; no formal CLAIM, Result, independent Driver review or P000/Foundation admission. This is an independent continuation of [EC49FNP PR #2303](https://github.com/awdawmip/enterprise-math/pull/2303), based on its immutable 1000-row source vector at commit `98cd8ce66ba27609359d9182e94376f0e81a1600`. Scientific pin **`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`** is unchanged.

## Exact proposition

Fix the original nine-state BRC lawful-word grammar, 94 complete cache keys, 24 demand labels and **ordered signed native-X6 microstep-prefix** cost. For the 1,000 configurations indexed `32000..32999`, let `K_i` be the original 7-key set and define `v_i=(C_i,m_i,g_i)`: the exact native-prefix optimum, number of distinct optimal admissible root-demand assignments, and positive gap to the second *distinct* root-assignment cost.

An edge `i--j` is a replacement of exactly one whole cache key (`|K_i\K_j|=|K_j\K_i|=1`). Call it **triple-stable** precisely when `v_i=v_j`. This is a graph on *whole-key assignments*, not on endpoint-only coordinates or collapsed native prefixes.

**Finite theorem (exhaustive on these frozen 1000 configurations):**

1. The full one-key exchange graph contains **27,942** undirected edges, of which **11,574** are triple-stable. Its triple-stable spanning subgraph has **244** connected components: **155** isolated vertices and **845** nonisolated vertices. The largest stable component contains **87** vertices, all with `v=(138,1,1)`. The three largest components have sizes **87**, **85** and **67**.
2. The **maximum shortest-path length inside any triple-stable connected component is exactly 4**. Thus any two configurations in the *same* stable component can be joined by at most four successive native-cache-key substitutions that each preserve all three observables. This is a finite graph property, not a general perturbation theorem.
3. There exist **three-key-disjoint exchange endpoints** connected by an *optimal-length* triple-stable path of three edges. Precisely:
   
   | Index | Seven complete cache keys | `(C,m,g)` |
   | --- | --- | --- |
   | 32291 | 0, 4, 5, 11, 37, 39, 57 | (154,1,1) |
   | 32296 | 0, 4, 5, 11, 37, 39, 62 | (154,1,1) |
   | 32773 | 0, 4, 5, 11, 38, 39, 62 | (154,1,1) |
   | 32916 | 0, 4, 5, 11, 38, 52, 62 | (154,1,1) |

   The endpoints' extra 3-key sets `{37,39,57}` and `{38,52,62}` are disjoint, so *any* one-key path requires at least three changes; the displayed triple-stable path meets this lower bound. Exactly **four** triple-stable components have at least one such pair; exactly **95** vertices have a three-key-disjoint stable-reachable partner.
4. Identical observables are **not** enough to guarantee a stable exchange path inside this selected finite graph: there are **18,609** unordered distinct vertex pairs with equal `(C,m,g)`; **16,558** share a stable component and **2,051** do not. Connectivity is thus strictly stronger than equality of these compressed observables.

The component size distribution `size -> number` is:

```text
1:155 2:53 3:10 4:2 5:1 6:3 7:1 8:2 9:1 14:1 16:1
18:1 24:1 30:1 34:1 36:3 38:1 40:1 42:1 43:1 67:1 85:1 87:1
```

## Proof and independently crosschecked finite evidence

The published `EDGE_VECTOR_EC49FNP.u8x11.xz.b64` is byte-identical to the immutable [EC49FNP source](https://github.com/awdawmip/enterprise-math/blob/98cd8ce66ba27609359d9182e94376f0e81a1600/research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FNP_EDGE_SPECTRUM_32000_32999_20261113/EDGE_VECTOR_EC49FNP.u8x11.xz.b64). Base64 then XZ yields exactly **11,000** bytes, 1000 consecutive 11-byte unsigned-integer rows `(seven cache-key indices,C,m,g,first-root-count)`, with exact decoded SHA256:

```text
4d6540181b8c25a324aa701f551602ed53156be46b70170f1c104230c6443e9b
```

The byte stream also independently reconstructs from the original complete EC49FNN evidence bundle (`cases.json` and `EXACT_CERTIFICATE_EC49FNN.json`), and its SHA256 matches the previously published FNP checksum. The original EC49FNN verifier was rerun against the unchanged evidence bundle and passed: all 1000 recorded exact optimizer rows, four segment FINISHED logs, input/source hashes, and four original lawful-word witness sets.

`VERIFY_EC49FNQ.py` verifies the following using only integer/set graph operations, standard-library Python and the immutable copied 11,000-byte vector:

- Two independent enumerators yield **identical** 27,942 undirected edges: exhaustive 499,500 vertex comparisons and inverse six-key-subset indexing.
- All eight equality-signature edge frequencies agree with EC49FNP: `000:3613, 001:4700, 010:2287, 011:3862, 100:501, 101:830, 110:575, 111:11574`.
- BFS components agree *as sets* with an independent union-find construction; component histogram and full shortest-path exhaustions establish the claimed counts and diameter.
- The four exhibited adjacent key sets and signed-prefix optimization triples are checked row by row. The lower bound of three moves is exact because a one-key exchange can remove at most one of the initial three differing keys.
- Every same-signature unordered pair and every component containing three-key-disjoint endpoints are enumerated, yielding the exact pair/vertex figures above.

The general graph lemma behind the exhibited path is simple: if `K,K'` are 7-element sets, an edge replaces one complete key, and every path between them has length at least `|K\K'|`. Along a triple-stable path the equality `(C,m,g)` propagates by transitivity. The *existence, maximal diameter, and size* of stable paths here are finite certified findings, not deduced from the lemma alone.

## Scope, provenance, and unresolved research

This establishes a **finite derived graph theorem conditioned on the archived 1000 exact native-BRC optimizer rows**. It does not re-solve all 1000 native trie/subset-DP instances, independently certify every original native operation word, or promote a graph-level compressed signature to full root-function equivalence. Nor does it generalize to all 38,169 radius-three configurations or the unrestricted 7-key mother problem. In particular, `v_i=v_j` does not assert equality of all root set functions.

A next substantive question: find **root-cost-function perturbation inequalities** guaranteeing the entire `(C,m,g)` triple across a one-key replacement *without* first evaluating the replacement's complete assignment distribution. Test on the stable three-key path above and on FNP's 101/110/011 counterexample classes, retaining the exact original native-prefix semantics.

No credentials or account-private policy text are included. The research artifact is published for preservation; formal Task publication/owner/CLAIM/Result and independent review remain separate.
