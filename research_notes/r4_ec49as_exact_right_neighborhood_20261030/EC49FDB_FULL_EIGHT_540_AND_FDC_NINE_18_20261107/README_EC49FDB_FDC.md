# EC49FDB / EC49FDC — complete eight-slot extension and first nine-slot exact results

Date: 2026-11-07 (Asia/Shanghai). Scientific input frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: **AUTHOR_FINITE_EXACT_PROOF / EXECUTED / UNREVIEWED / NOT_ADMITTED**. Source predecessor: `d4031834992fc84d1d0ccf505bce02281f51d5a0`, EC49FDA, PR #1730.

## Exact object

Fix 24 original designated slots, nine-state observer and literal *ordered signed primitive-step prefixes*. Cache keys remain `L=(4,2,1), M=(7,3,2)`. For any legal word `w`, `P(w)` is the set of its distinct nonempty literal signed native-step prefixes. For selected slot set `S`, every slot outside `S` retains its original word, and each slot in `S` chooses exactly one legal word from its **entire** frozen multiset-and-observer signature language. The objective is `C(S)=min |union of P(w_i) over 24 slots|`. The original legal witness has 158 edges.

For `r,s,t in {1,2,4,8}` define
- `A(r,s,t)={4:r,5:16,6:s,7:t,8:2,8:4,9:16}`.
- `B(r,s,t)={4:r,5:32,6:s,7:t,8:1,8:8,9:32}`.

**Theorem EC49FDB (768 eight-slot cases).** For either A/B, all r/s/t, and one additional distinct `6:q` (q != s) *or* `7:u` (u != t), with q,u from the same four signatures, the exact global finite minimum is **158**. Prior EC49FDA established 228 cases with `r=1` or `(s,t)=(1,1)`. This round exhaustively solved the complementary **540 cases** with `r in {2,4,8}` and `(s,t)!=(1,1)`. These 228+540 are disjoint and cover `2*4^3*6=768` instances.

**Theorem EC49FDC (18 nine-slot cases).** In A/B with `r=2,s=t=1`, additionally vary **both** a distinct `6:q` and a distinct `7:u`, with `q,u in {2,4,8}`. All `2*3*3=18` nine-slot instances have exact finite minimum **158**.

## Proof kernel (full legal candidate languages)

For fixed `S`, let `F` be the literal signed-prefix union of the unchanged original words. Build a trie of *all* legal candidate signed primitive strings at each selected label. Incoming trie edge `e` has cost `c(e)=0` if its complete prefix is in F and 1 otherwise. A terminal bitmask records all variable labels whose legal word terminates at that node; shared edges retain each label's identity.

For each node v and label-mask M define `D_v(M)` as the minimum new-edge count within the strict subtree below v realizing exactly labels M. Initially at v, any subset T of terminal labels at v is available with cost zero; all other masks have infinite cost. For each child u combine disjoint masks A and B using

`D_new(A union B) = min(D_new(A union B), D_old(A)+D_u(B)+c(u)*[B nonempty])`.

Each child subtree has disjoint strict prefixes from the other children. Its incoming edge is paid exactly once if at least one assigned variable uses it; terminal choices at v pay no further edges. Induction on trie height gives the exact optimum `C(S)=|F|+D_root(all selected labels)`. Every candidate word is inserted (no fixed sublanguage truncation), all costs are integers, and the original 158-edge witness supplies the matching upper bound. The complete full-language solver is the existing C++17 `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/EXACT_PREFIX_TRIE_DP.cpp`, source Git blob `dfe7a3b596f615a26b88d48beee931459d2357eb`. The frozen generator `frozen_model.py` is Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`; the trie builder is Git blob `4c74b4ee243c939494d9f7eedb3f61255e16f91f`.

## Executed evidence and replay

* **540 newly computed full-language exact eight-slot cases:** all optima 158, fixed-prefix count 108–126, max trie nodes 59,174, total **196,555,855,176 actual trie DP subset transitions**. Full per-case compact row table with all 540 keys, fixed-edge counts, trie sizes and transition totals: `EC49FDB_540_ROW_TABLE.json.gz.b64` (gzip-compressed UTF-8 JSON, base64 transport), decoded JSON SHA-256 `d69c6ce8efda1e41b5401b22e0bc93ccf6b3bdcfe88f30990f42127b7a26d40f`. All optimum values are the declared 158; the count/pool fields not stored in the compact table are reproducible from pinned generator. Author's full 540-row JSON SHA-256: `8e69d5ff79fd4f5bd8ac93d3f7afa0333666bd6218a574d6e188313734180461`.
* **18 newly computed full-language nine-slot cases:** all optima 158. Complete 18 rows: `EC49FDC_18_NINE_SLOT.json.gz.b64`, decoded JSON SHA-256 `ad45efb837fee1d3c80e05baa0b027e916d31e7e798d9b3743625c1c2499b3a1`.
* An independent direct literal signed-prefix set enumerator examined **118,098 restricted candidate tuples** (three legal words at each of eight selected slots, 18 spread cases), and all restricted minima were 158. This audit checks literal prefix semantics on that *restricted sublanguage*; the full-language minima come from the exact trie recurrence.
* The 540-case archive, row coverage, case order and SHA-256 were checked locally; 4 full-language cases were freshly recomputed with fixed-prefix counts, trie size, transition counts and optimum matching the published row table. All 18 nine-slot cases were freshly solved on the full candidate languages. The executed local Python driver also retains the unabridged 540 rows.

Reproduce eight-slot certificate: `python REPLAY_EC49FDB_COMPACT.py --check`; optional full-language rerun: `python REPLAY_EC49FDB_COMPACT.py --recompute --limit 4` (or omit limit). Required sibling EC49FCZ frozen generator, trie builder, solver are already versioned in the same PR branch. For the nine-slot instances, use `python RUN_EC49FDC_NINE.py`, which writes its own complete exact report.

The above are **finite neighborhood theorems for the specified typed observer and cache keys**. The full nine-window 93-edge mother target and admissible changes in BRC keys remain open. P000, joint-observer constraints and ACTIVE worldview are unchanged.

## Control status / next unit

Connected GitHub login: `awdawmip`; repository push permission verified. Native Enterprise Math gateway responded `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`; Site reports `research_authority_granted=false`. Live owner/CLAIM and authenticated native Result/independent Driver review remain unconfirmed. GitHub publication preserves author-side mathematics and does not assert native admission.

Next EC49FDD: expand nine-slot cases beyond these 18 (distinct H6 and H7 extras at other r,s,t), seek an explicit 157-or-less witness, or open a tenth variable / admissible BRC-key rearrangement. Preserve complete signed prefix semantics and save any strict witness words and union.
