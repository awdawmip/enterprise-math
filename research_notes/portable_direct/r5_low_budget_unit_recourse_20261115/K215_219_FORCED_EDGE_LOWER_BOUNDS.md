# R5 — K=215–219: exact forced-edge witnesses for nonlocal optimizer recourse

Date: 2026-11-15. Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Status: **AUTHOR-CHECKED / EXACT FINITE WITNESSES / NOT_REVIEWED**.

## Object and exact quantified claim

Work exclusively in the **derived 954-event 1D integer, event-index-center radius-two observer**; keep original event indices under closing a length-3 gap to length 2. It is a typed observer of the Enterprise Math P000/HEARTBEAT_WORLD substrate, **not a claimed lossless native X6 reduction**. All 28 original closure variables, original task/science pins and richer BRC/X6 provenance remain unchanged.

For a closure mask B let `Opt_B(K)` be all indexed K-center sets attaining the minimum nearest-center total distance under radius-two coverage. The full-background directed recourse is

```
R_i(K) = max_{B subset I without i} max_{S in Opt_{B+{i}}(K)}
           min_{T in Opt_B(K)} |S \ T|.
```

Here we construct an actual `S` for **B=empty** in each of 20 `(i,K)` cases and compute its exact min over the **entire old optimum family**. Thus these are certified lower bounds for the full-background R, not upper bounds or identified worst-case maxima.

## New results (zero-based gap indices)

| K | J_old=J_new | R_3(K) ≥ | R_8(K) ≥ | R_9(K) ≥ | R_10(K) ≥ |
|---:|---:|---:|---:|---:|---:|
| 215 | 1059 | 3 | 6 | 6 | 4 |
| 216 | 1054 | 3 | 6 | 6 | 4 |
| 217 | 1049 | 3 | 5 | 5 | 4 |
| 218 | 1044 | 3 | 5 | 5 | 4 |
| 219 | 1039 | 3 | 5 | 5 | 4 |

The exact old/new optimum-cost formula throughout this five-budget window is **J(K)=2134−5K**. The associated gap start event indices are `cuts[3]=46`, `cuts[8]=110`, `cuts[9]=116`, `cuts[10]=123`. These are gap identities, not center coordinates.

These 20 results close the **witness-level gap between the already recorded K=214 lower bounds (3,7,7,4)** and the **already published K=220/221 forced-edge witnesses**. They remain valuable even when the upper extrema R are still unknown. In particular, under singleton closure of gap 8 or 9, an exact six-center replacement witness exists at budgets 215 and 216; a five-center replacement witness exists at 217–219.

## Proof / exact finite certificate

1. Reconstruct the pinned 15-term subset-sum input with the existing `frozen()` routine (exact `Fraction` arithmetic; 954 indexed events, 28 cut indices); obtain the old and singleton-closed edge DAGs from `graph()`. Every feasible K-center set is represented exactly once by its increasing index path; admissible edges encode radius-two coverage and exact integer intermediate distance costs.
2. Run exact integer shortest-path `paths_dp` on both coordinate sequences. In each listed budget and gap the optima agree, with `J(K)=2134−5K`. Enumerate all **newly admissible** center edges `u→v` that can occur on a new global optimal path at layer h, satisfying
   `C[h-1][u]+w(u,v)=C[h][v]` and `C[h][v]+D[K-1-h][v]=J(K)`.
   Such an edge occurs on a globally new-optimal path and is forbidden in the old graph; its inclusion certifies that the resulting path S is not old-feasible.
3. For each qualifying edge-layer state, generate 48 deterministic valid optimal prefix/suffix completions using the saved seed. The edge-layer state set is fully enumerated, but the completions are **sampled**, not exhaustive. Every selected witness has K unique sorted center indices, radius-two coverage in new coordinates and exact new optimal total J.
4. Given fixed S, compute the best old overlap across **every** old globally optimal K-center path, then use
   `rho_empty(S)=K-max_{T in Opt_empty(K)}|S∩T|`.
   The existing all-old-optimum restricted-cost DP is independently checked for the winning witness by a second **lexicographic (total cost, negative overlap)** DP on the old DAG, not restricted by the first algorithm's old-optimum prefix table. Both return the same exact old minimum total cost and overlap. This proves the displayed lower bound with the required nested quantifier order.
5. The exact witness material preserves 20 full center-index arrays, the forced edge/layer, old maximal overlap, minimum replacements and construction parameters. There are **1,680 sampled path checks**: 240 at gap 3, and 480 each at gaps 8, 9, 10. Every saved selected witness passed full 954-event coverage/cost and lexicographic old-family recourse checking.

## Reproduction and complete material

Original executable: `VERIFY_R5_K215_219_NEWLY_ADMISSIBLE_EDGE.py`, in this folder. Run next to the already saved `VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py` and `VERIFY_R5_K220_221_FORCED_EDGE.py`:

```bash
python VERIFY_R5_K215_219_NEWLY_ADMISSIBLE_EDGE.py > K215_219_REGENERATED_WITNESSES.json
```

It is standard-library Python. It asserts the new vectors against the table and independently checks all 20 winning-witness old optima by lexicographic dynamic programming. The author-side actual finite computations used equivalent implementations of the same frozen integer DAG and the same deterministic forced-edge path construction. The 20 selected center arrays and their exact old overlaps were additionally checked using the separate lexicographic implementation, returning `PASS_R5_K215_219_INDEPENDENT_LEX_CROSSCHECK`; the new consolidated source is preserved for a direct original-module rerun.

The complete **60,782-byte** independently checked JSON with all 20 arrays is saved losslessly as `EXACT_R5_K215_219_VERIFIED_WITNESSES.json.zlib.b64` (base64 of zlib level-9 compression). Original uncompressed JSON SHA-256:

`822206f22f15faf99128f746b9faeee6b561329d727f77a3aa9b4707784e6710`.

Decoding:

```python
import pathlib, base64, zlib, hashlib
p = pathlib.Path('EXACT_R5_K215_219_VERIFIED_WITNESSES.json.zlib.b64')
raw = zlib.decompress(base64.b64decode(''.join(p.read_text().split())))
assert hashlib.sha256(raw).hexdigest() == '822206f22f15faf99128f746b9faeee6b561329d727f77a3aa9b4707784e6710'
pathlib.Path('EXACT_R5_K215_219_VERIFIED_WITNESSES.json').write_bytes(raw)
```

The encoded artifact was verified against the locally computed Git blob SHA-1 `e51d7f679c4e6ee94387f0ba29b2452939553586`. Source, note and evidence require independent review and do not establish a formal Task/CLAIM/Result/Review, nor a current authorized Source Activity checkpoint.

## Next actual mathematical question

Compute **upper bounds or exact values** for the full `max_S min_T` at K=214–221, gaps 3/8/9/10 and every valid five-variable closure background. Changed-edge-constrained path generation can restrict the new-only family without losing any path; the remaining nontrivial piece is maximizing its exact distance to the old optimum language, rather than sampling completions. Preserve the interleaved maximum/minimum and any far-away necessary changes. The P000 joint-observer preservation constraint continues to govern further reductions.
