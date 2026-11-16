# R5 — Fused exact dynamic programming for three scalar-count observations

Date: 2026-11-16. Scientific freeze: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
State: **AUTHOR_PROVED / TWO_EXACT_FINITE_WITNESSES / NOT_REVIEWED**.
Scope: the derived 954-indexed-event, one-dimensional integer radius-two center observer. This is a software/observer-level computation theorem, **not** a new native X6/BRC equivalence, formal Result, independent review, or computational complexity breakthrough.

## Question and preserved antecedents

The earlier three-scalar-query theorem gives eight effective closure bits `U={3,8,9,10,15,17,25,27}` and establishes that any exact three-count decoder must observe one A-private window (`K=214..221`), one B-private window (`K=223..291`), and one C-private window (`K=294..313`); exact fixed decoders include
`(214,223,294)`, `(214,290,294)`, `(214,291,294)`.

The preceding cost work proves that the last triple minimizes **raw exact count bit lengths pointwise**, while the original per-query sum-of-K metric has the Pareto points (731,319), (798,317), (799,305). That sum-of-K metric is an explicitly charged budget parameter, *not* by itself a measured CPU-operation cost.

Here the new resource is **one joint evaluation of multiple budgets against the same input closure configuration**, using a shared integer DP. The individual outputs remain three scalar observations. Batchability is an explicit API/operation assumption; in separate external experiments it need not hold.

## Theorem 1 — Exact shared-prefix evaluation

Fix any allowed closure configuration B and its indexed-event coordinate sequence `x_B`. Let `F_k(j)=(c_k(j),w_k(j))` give the minimum objective cost and exact number of attaining k-center sets whose final selected center has index j. Let `P_B(j)` be the predecessor list of admissible previous center index/edge cost, formed only from `x_B`, and let `s_B(j)` be the suffix cost when j is the last center. The existing min-plus/tie-count recurrence computes

`c_k(j)=min_{(i,v) in P_B(j)}(c_{k-1}(i)+v)`,

`w_k(j)=sum_{(i,v):c_{k-1}(i)+v=c_k(j)} w_{k-1}(i)`.

The final count `N_B(k)` is the sum of `w_k(j)` over terminal indices whose `c_k(j)+s_B(j)` equals the global minimum.

For any requested finite list `1<=k_1<...<k_q`, compute `F_1` once, then update through `F_{k_q}` **once**, extracting `N_B(k_i)` at the requested layers. This yields exactly the same `q` integer counts as independent executions, for *every* allowed B, by induction on k. The recurrence depends on B and k but not on the query history or which layers are requested. No independence between closure bits or mask enumeration is required for this theorem.

With the existing one-layer initialization, the number of complete DP layer transitions is exactly `k_q-1` for a joint sweep versus `sum_i(k_i-1)` for q independent sweeps. For a fixed B, predecessor construction and event preparation are performed once, not q times. In the given implementation the rolling DP retains two arrays of length 954 and predecessor arcs, plus q extracted counts; no storage of all intermediate DP layers is necessary.

This is an exact **operation-sharing identity** under the specified recurrence. It is not a universal lower bound on all possible algorithms or a claim of sublinear time in K.

## Theorem 2 — Batch computational frontier collapses for the known three-window decoder

All three established resource-Pareto triples end at `K_C=294`. They therefore require exactly the same joint DP transition sequence `F_1,...,F_294`, and differ only in which precomputed scalar values are read. Their exact layer counts are:

| Triple | Independent layer transitions | Joint layer transitions | Avoided repeated layers |
|---|---:|---:|---:|
| 214,223,294 | 728 | 293 | 435 |
| 214,290,294 | 795 | 293 | 502 |
| 214,291,294 | 796 | 293 | 503 |

Under the cost pair **(one shared DP sweep through largest requested K, raw total returned count bits)**, and excluding an independently assessed per-query K fee, `(214,291,294)` is pointwise weakly optimal among all valid deterministic exact three-scalar decoders, including adaptive choice of budgets.

Reason: the earlier support theorem forces one C-window query with K at least 294 on each successful path. The shared-prefix DP must reach at least that layer. Its counted transition work through layer 294 is an unavoidable prefix *for this particular DP implementation*. The earlier pointwise 612-comparison certificate proves that replacing the A, B, C reads by `214,291,294`, respectively, never increases the bit payload on the same closure mask, while preserving injectivity. A fixed decoder at these positions reaches precisely layer 294. Its computational layer count is no larger, and its raw bit payload is no larger, for every mask.

This **does not** overturn the prior three-point frontier when `sum K` is itself charged as an independent resource, when three experimental trials cannot reuse a common DP state, or when per-query communication/online latency is material. It also does not price bit-level arithmetic, preprocessing, encoding, memory allocation, or external native observer acquisition as a complete wall-clock model.

## Exact executable checks (two masks, not exhaustive)

`VERIFY_R5_FUSED_DP.py` reconstructs the frozen 15-term source via all 32767 nonempty subsets, checks pool cardinalities 538/298/229, 954 integer-indexed events, coordinate extent 1065, 28 length-three cuts, and builds the original integer predecessor recursion. On masks zero and 255 of the eight effective bits, it evaluates all five K positions `214,223,290,291,294` in one fused sweep and in five separate runs; it asserts **exact equality of both minimum cost and integer optimal-family count** at every K.

It instruments:
- `attempted_transitions`: predecessor relaxation candidates with nonzero prior count, not elapsed time.
- `operand_bit_volume`: sum of `bit_length(w[i])` over these candidates, a count-multiplicity input-width proxy, not full bit complexity.
- `relax_or_tie_updates`: candidates improving or tying the minimum at a target.

All arithmetic is integer or exact rational reconstruction. Two verified masks are exemplars. The theorem's all-mask quantifier comes from the recurrence induction, not from exhaustively checking 2^28 masks.

| Eight-bit mask | Predecessor arcs | Fused candidates to K294 | Separate candidates (214/223/294) | Separate candidates (214/291/294) |
|---|---:|---:|---:|---:|
| 0 | 4,383 | 598,300 | 1,299,618 | 1,522,405 |
| 255 | 4,399 | 604,273 | 1,316,825 | 1,539,929 |

Thus the measured candidate reductions in these two witnesses are about 54.0% for the 731-budget plan and 60.7% for the 799-budget plan. For these witnesses the fused count-input bit-volume is respectively 99,391,071 and 100,055,653, versus 237,375,022 and 239,228,039 for independent execution of the 799 plan. The maximum observed raw payloads at mask 255 are 319, 317, 305 bits for the three plans; this reproduces the earlier worst-case triplet but does not reprove its global 256-mask optimality.

Command: `python VERIFY_R5_FUSED_DP.py > results.json`. Local result: `PASS_R5_FUSED_DP_EXACT`; the full local stdout JSON was 5,246 bytes, SHA256 `bcb04954a2ba3b675ae66bc92b900c2dea0216f86ded935b5b1d1838433082a2`. The committed `RESULTS_SUMMARY.json` retains the values plus source digests; the executable generates its own detailed JSON. Publication and source verification are separate from mathematical acceptance.

## Provenance and important limitations

- Frozen source for 954-event reconstruction: `435e77af0d180eac32bd1f9c4c464bc4010b7551`, retained, not rebased.
- Existing exact three-window classification: `research_notes/portable_direct/r5_minimum_scalar_queries_20261116/VERIFY_R5_ALL_TRIPLE_DECODERS.py` at `143ada28910f2b0e042d2d0ffcb066fee45d083e`.
- Existing bit-cost and adaptive proofs: `research_notes/portable_direct/r5_decoder_cost_20261116/RESEARCH.md` and `ADAPTIVE_PARETO_THEOREM.md` at `3581c1552a7194ffccd495aff7a387c7d89cba57`.
- This proof is derivative/auxiliary. Native X6 path, source, branch and future-operation residuals are retained rather than asserted redundant. No BRC speedup or native-state compression is claimed.
- This verifier's two-mask checks are not an independent implementation or independent mathematical review. Source code SHA and local stdout SHA identify observed files, not proof of authentic runtime execution on other clients.

## Next discriminating question

Develop a **bit-operation** cost frontier using exact big-integer addition and comparison input widths, terminal scans and source reconstruction, distinguishing (i) three truly independent query executions from (ii) a shared-batch computation. Then test whether any *single* change of the DP representation (such as compact predecessor indexing or layer specialization) lowers actual measured end-to-end cost without changing the count observer. A separate original frontier remains the exact max-new/min-old center-replacement distance on K214..291.
