# EC49FNP: complete eight-class single-key stability spectrum in a frozen native-BRC finite subfamily

Status: author-side exact finite postprocessing, NOT_REVIEWED; 2026-11-13. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Source: EC49FNN [PR #2298](https://github.com/awdawmip/enterprise-math/pull/2298) (exact indices 32000–32999). EC49FNO [PR #2301](https://github.com/awdawmip/enterprise-math/pull/2301) already covers 33000–38168; this independent result does not rescan that solved tail.

## The finite proposition

Fix the original nine-state lawful-word BRC grammar, 94 full cache keys, 24 label demands, and original **ordered signed native-X6 prefix** identity, preserving branch and source-word provenance. The source optimizer's `C_i` is the minimum number of distinct nonempty native prefixes covering the 24 labels; `m_i` is the count of optimal admissible root-demand allocations; `g_i` is the strictly positive difference between the second **distinct** root-allocation cost and `C_i`.

Let `V={32000,...,32999}`, and let `K_i` be the associated seven *complete* cache keys. Two **distinct** vertices are adjacent when one key is replaced: `|K_i\\K_j|=|K_j\\K_i|=1`. For such an edge, define its three-bit equality signature `(1[C_i=C_j],1[m_i=m_j],1[g_i=g_j])`.

**Theorem (finite, exhaustive):** This 1000-vertex graph has exactly **27,942** undirected edges, and all eight logically possible signatures occur:

| Signature C,m,g | Count |
|---|---:|
| 000 | 3,613 |
| 001 | 4,700 |
| 010 | 2,287 |
| 011 | 3,862 |
| 100 | 501 |
| 101 | 830 |
| 110 | 575 |
| 111 | 11,574 |
| **Sum** | **27,942** |

Thus the preservation of any two of `C,m,g` does **not** imply preservation of the third for this finite original BRC configuration family. This is a counterexample to any *unconditional* two-to-three preservation law on one-key replacements; local sufficient inequalities remain worth seeking.

Witnesses within the certified graph:

* Cost and gap preserved but multiplicity changes: 32273→32354 (key 38→42), `(176,2,1)→(176,12,1)`.
* Cost and multiplicity preserved but gap changes: 32280→32505 (key 39→50), `(135,1,4)→(135,1,1)`.
* Multiplicity and gap preserved but cost changes: 32807→32813 (key 61→77), `(125,1,1)→(204,1,1)`.

## Reproducible exact evidence

The independent input `EDGE_VECTOR_EC49FNP.u8x11.xz.b64` contains **all 1000** contiguous records (indices implied by 32000+row number). Base64 decode then XZ decompress into exactly 11,000 bytes. Each consecutive 11-byte record consists of `7 complete cache-key indices, C, m, g, available-first-root-count`, each uint8. Decoded raw SHA256: `4d6540181b8c25a324aa701f551602ed53156be46b70170f1c104230c6443e9b`. The values were generated from the original EC49FNN C++ integer output, with its original frozen seven-key index list, and checked row-by-row against the earlier EC49FNN exact certificate.

`VERIFY_EC49FNP.py` first checks the exact byte length, SHA256, index count, uniqueness of seven-key sets, positivity of `m,g`, and then independently enumerates edges by (A) comparing all 499,500 unordered vertex pairs, and (B) inverting the six-key subsets. Two distinct seven-sets that differ in exactly one element share precisely one six-key subset, so the second enumeration generates every edge exactly once. Both must yield the same 27,942 edges and eight signature counts. Every operation is exact integer/set arithmetic; no floating point or endpoint-only path collapse.

**Boundary:** This is a complete finite combinatorial postprocessing proof *given the archived exact native-BRC optimizer rows*, not an independent rerun of the BRC prefix DP for all 1000 cases. The underlying EC49FNN C++ solver, original legal-word source, representative independently checked optimizers, and original logs remain in the EC49FNN evidence package. PR publication is not CLAIM, Result, Driver review, or P000/Foundation admission.

## Next research unit

Derive root-cost perturbation inequalities that suffice to preserve `C,m,g` across a one-key replacement, then test the inequalities across the observed 111/101/110/011 signature classes without recomputing every admissible root assignment.
