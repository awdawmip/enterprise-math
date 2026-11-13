# R5: exact support-pruned min-plus/count suffix dynamic programming

Date: 2026-11-13. Status: author-side proof and exact finite verification; **not** a formal Source Result/Review or accepted native task return.

## Provenance and research question

Frozen scientific source: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Original R5 certificate input: 15 labeled integer atoms; 954 strictly increasing cumulative event boundaries with 1,065 total events; 953 distinct exact rational activation walls. The 213-center radius-2 mean-optimal class, optimal cost `1070`, cardinality `1338767625695954932334592000`, original rank `417027933051277583800994379`, and 12-byte rank encoding are preserved from PRs #2268 and #2273. This increment changes *only* the memory representation and row evaluation domain of the existing exact suffix DP.

## Theorem: exact recursive support pruning

Let `x[0]<...<x[W]` be **strictly increasing integers**, let `R>=0` and `K>=1`, and let `p->q` (`p<q`) be an edge precisely if every intervening query boundary is within event distance `R` of center `p` or center `q`. Define the right and left coverage bounds:

`U_R(p)=max{b:x[b]<=x[p]+R}` and `L_R(q)=min{b:x[b]>=x[q]-R}`.

Then `p->q` iff `L_R(q)<=U_R(p)+1`. Since the event coordinates increase by **at least 1 per boundary**, `p->q` implies `q-p<=2R+1`: if there are more than `2R` intermediate boundaries, neither endpoint's radius-R cover can account for all of them.

Let `S_1={p:x[W]-x[p]<=R}`. For `t>=2` define
`S_t={p: exists q in S_(t-1) with p->q}`.
These are **exactly** the indices with at least one legal t-center suffix terminating in the permitted final coverage region. If `S_(t-1)` is nonempty and `a=min S_(t-1)`, `b=max S_(t-1)`, then

`S_t subseteq [max(0,a-(2R+1)), b-1]`.

For an empty previous support, the new support is empty. Therefore the min-plus/count suffix recurrence may inspect only this candidate interval, delete leading/trailing states of zero continuation count, and represent all other states as `(infinity,0)` without changing *any* finite optimal cost, tie multiplicity, admissible root, global center count, rank, or unrank. Internal holes, if present, remain explicitly zero-count; **contiguity is not assumed for the theorem**.

Proof: the base support consists precisely of allowed final centers. A t-center suffix must first choose one outgoing legal edge to a valid (t-1)-suffix, and conversely any such edge followed by a valid suffix is legal. Thus induction establishes the support formula. The edge displacement bound restricts all possible predecessors to the displayed interval. Because each recurrence discards zero-count descendants, restricting to that interval cannot alter any minimizing candidate or sum of tied minimum counts. Induction then gives equality with the dense recurrence at every t and p. Lexicographic ranking/unranking only consult these pairs, hence is also unchanged.

Using a vector band from its first to last nonzero continuation state (retaining any internal holes), at most `sum_t (max(S_t)-min(S_t)+1)` cost/count entries are stored in all full rows. A streaming recurrence requires only the old and new bands. Blockwise recomputation can use the same bands at each anchor and temporary row; worst-case bounds remain the previous dense bounds, while the actual saved work is instance-dependent. No general 58.75% saving is claimed.

## Exact pinned R5 result

Rebuilt the original 15-atom rational thresholds using `fractions.Fraction`. Obtained the exact activation histogram `{1:869, 2:56, 3:28}`, 954 boundaries, 1065 events and 4383 legal radius-2 edges. Compared each of the `213*954=203202` dense state positions (cost and tie count) against support-pruned rows; all match. For this **specific original R5 fixture**, all nonzero supports are contiguous, and the sum of retained row lengths is **83813**, 58.7539% fewer row *cells* than dense storage. This is a statement about DP representation cells, not the memory of the whole application.

Both methods recover `J=1070`, `T_opt=1338767625695954932334592000`, the existing 213 original centers and their exact rank `417027933051277583800994379`. Additional independent small-input checking exhausts 2184 (integer-coordinate vector, radius, K) instances, compares dense and pruned row dictionaries and crosschecks the optimal cost and multiplicity by direct enumeration of all K-subsets. No floating arithmetic is used in the mathematical oracle.

The attached `VERIFY_R5_SUPPORT_BANDS_COMPACT.py` is the **executed** portable proof checker. The resource results below were separately measured with the full local `VERIFY_R5_SUPPORT_BANDS.py` implementation, archived in the task's local run output; its resource setup is not a part of the compact checker. See `EXACT_OUTPUT.json` for the actual measured values and limitations.

| Cold independent CPython process | Dense full rows | Pruned full rows | Dense B=12 | Pruned B=12 |
|---|---:|---:|---:|---:|
| Retained full-table row cells | 203202 | 83813 | 203202 logical | 83813 logical |
| Max simultaneously held band cells | 204156 | 84554 | 28620 | 15160 |
| One run: DP build + 12-byte rank unrank, seconds | 0.267 | 0.207 | 0.505 | 0.303 |
| Peak traced Python allocations for this DP phase | 8304508 B | 6346056 B | 1545604 B | 1329456 B |

The timing row above is indicative only; no interleaved repeated-process statistical conclusion is made. The five-stage pipeline rebuilt original exact rational walls, radius graph, the historical 12-byte rank decode and the 954-byte direct lookup. The four variants produced identical decoded-center and directory SHA-256. Cold-run process RSS was noisy and mostly dominated by interpreter/fixture overhead; this is not an application RSS savings claim.

## Scope and next open question

This is an exact **auxiliary R5 certificate-checkpoint algorithm** result under the unchanged frozen pin, not a proof of native spatial/geometric dynamics or revised P000. It does not run the original 28-coordinate certificate legal-word bitmap/prefix-query pipeline, so 2,747,520 original full prefix comparisons, original mixed rational query throughput, complete application peak RSS and a multi-machine cost crossover remain open. The actual TASK owner/CLAIM and Source reviewer state must be separately validated; an author-side Draft PR does not confer them.

Next: integrate original wavelet/bitmap query construction with the same four-row schemes and 12/17/33/35/56-byte center codecs; measure identical process-level cold workloads with separate construction/queries and identify the real total-cost crossover. Do not repin the mathematical source.
