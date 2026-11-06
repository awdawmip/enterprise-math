# EC49FCF — 150 additional exact four-slot rigidity cases (2026-11-06)

**Status:** author-side finite proof and computation; independent Driver admission pending.
**Scientific input pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`
**Frozen source model:** `5b10f1c296cb8826d4b69f6fd83dba89d765df1c` (`VERIFY_EC49FBY.py`).
**Predecessor:** EC49FCE, 370 early1+late3 cases (Git commit `ef7fc1ac4b75689bd61e53b7769b905bfd41139f`).
**Research line:** EC49FBU witness, fixed 24 slots, frozen H2/H3 paths, nine-state observer, signed native X6 primitive paths, positive BRC cache keys L=(4,2,1) at H4/H5 and M=(7,3,2) at H6–H9.

## Exact result

Let (W) denote the fixed 24-path witness with 158 distinct nonempty signed-X6 primitive prefixes. For any selected set (S) of four observation-signature slots, replace paths in (S) by any observer-valid paths with exactly the original length and full cache key, leaving the other paths unchanged. Let (C_S) be the number of distinct prefixes of all 24 paths.

**Theorem:** For all 150 slot sets in the following families, (min C_S=158).

| Four-slot family | Slot sets | Raw path quartets | Final strict-improvement union checks | Min |
|---|---:|---:|---:|---:|
| early1 + H7+H7+H8, last 30 (of 240) | 30 | 911,191,680,000 | 449,286 | 158 |
| early1 + H7+H9+H9 | 40 | 1,365,590,016,000 | 112,992 | 158 |
| early1 + H8+H8+H8 | 40 | 11,522,165,760,000 | 7,576 | 158 |
| early1 + H8+H9+H9 | 40 | 5,462,360,064,000 | 32,444 | 158 |
| **Total** | **150** | **19,261,307,520,000** | **602,298** | **158** |

The first family follows the exact ordering of `(early slot, two lexicographically ordered H7 slots, H8 slot)`, skipping indices 0..209 already checked in EC49FCE. The four families are mutually disjoint and disjoint from those 370 previously verified slots.

**Proof/algorithm:** Let (P(w)) be the set of all nonempty ordered, signed native-X6 primitive prefixes of legal word (w), retaining its full primitive-step order. For four selected slots (S), put (F=igcup_{t
otin S}P(W_t)). Each legal replacement (v) at slot (s) has residual (R_s(v)=P(v)setminus F). Its total four-slot cost is exactly

[
 |F|+left|igcup_{sin S}R_s(v_s)ight|.
]

Set (d=158-|F|). A residual whose size is at least (d) cannot occur in a strict improvement. A partial union of two or three residuals with size at least (d) likewise cannot be extended to improve the witness, by monotonicity of union. Equal residual sets are interchangeable **only for this cost function and fixed observer/scope**; their source words remain in the original legal candidate generation. This is an exhaustive, integer-exact branch-and-bound decision procedure for cost below 158. Every listed slot family retains the original legal witness of cost 158, so excluding cost below 158 proves equality.

`VERIFY_EC49FCF_150.py` re-generates all legal candidates from the frozen nine-state DFA, with the original H4–H9 signatures and keys, evaluates all 150 combinations and writes `EC49FCF_150_CERTIFICATE.json`. The compressed full per-group certificate is stored as `EC49FCF_150_CERTIFICATE.json.gz`. `INDEPENDENT_CHECK_EC49FCF.py` computes signed step prefixes as literal integer tuples instead of indexed bitsets, cross-checking four actual slot sets; all four minimum costs and fourth-check counts matched.

### Reproduce

From this directory: `python VERIFY_EC49FCF_150.py`, then `python INDEPENDENT_CHECK_EC49FCF.py`. `frozen_model.py` is a retained copy of the verified `VERIFY_EC49FBY.py` at the exact pinned scientific commit.

### Frontier / next

Previous four-slot coverage: 4,015/4,845. After 150 disjoint additions: **4,165/4,845**. Remaining 680 early1+late3 quartets: 120 early1+H8+H8+H9, 240 early1+H7+H8+H8, 320 early1+H7+H8+H9. These require faster exact pair-union/dynamic pruning; the current result does not resolve them. Five-path exchanges, other BRC cache keys and the 93-edge mother objective remain open.

### Evidence and admission

The named finite computation, signed tuple cross-check, full 150-group certificate and the executable program were actually run together on 2026-11-06. The model is a combinatorial cost calculation on frozen legal paths, not a claimed physical native-dynamics calibration. Research author-side evidence is publishable without current CLAIM; formal Source Result and independent Driver review require their own native authority.
