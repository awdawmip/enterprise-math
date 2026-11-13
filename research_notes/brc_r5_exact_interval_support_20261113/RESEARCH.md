# R5 — Exact interval theorem for radius-cover suffix supports

Date: 2026-11-13. Status: author-side proved combinatorial lemma with finite exact verification; not a formal Task Result/independent review.

## Source and scientific scope

Frozen scientific input: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. This note continues the radius-cover optimal center-ranking line from Draft PRs [#2273](https://github.com/awdawmip/enterprise-math/pull/2273) (blockwise min-plus/count suffix DP) and [#2279](https://github.com/awdawmip/enterprise-math/pull/2279) (safe support-band pruning). It strengthens their conservative statement that reachable supports *may* have holes: under the existing strictly increasing event-coordinate and **full radius-cover graph** hypotheses, holes are mathematically impossible.

This is about the auxiliary BRC R5 certificate-threshold checkpoint and prefix-query data carrier. It neither changes the original certificate corpus nor asserts native six-axis dynamics, P000 promotion or formal ownership.

## Exact theorem

Let `x[0]<x[1]<...<x[W]` be a strictly increasing real sequence (integer spacing is **not needed** for this stronger theorem), and let `R>=0`. Each chosen checkpoint `s` covers those boundary indices `b` with `|x[b]-x[s]|<=R`. Set

`U(p)=max{b : x[b]<=x[p]+R}` and
`L(q)=min{b : x[b]>=x[q]-R}`.

For `p<q`, write `p -> q` if every boundary between them is covered by checkpoint `p` or `q`. As established in #2279, this is equivalent to `L(q)<=U(p)+1`.

For each `q>=1`, define `ell(q)=min{p<q : p -> q}`. This minimum always exists because `q-1 -> q` (there are no intermediate boundary indices). Then:

1. **Consecutive predecessors:** `{p:p->q}=[ell(q),q-1]` as a set of indices.
2. **Monotone predecessor boundary:** `ell(q+1)>=ell(q)` for every `1<=q<W`.
3. **All suffix supports are intervals:** Let `S_t` consist of checkpoint indices that can begin a valid `t`-checkpoint suffix covering from their first index through `W`. Define `a_1=min{p:x[W]-x[p]<=R}`, `b_1=W`. As long as `S_{t-1}=[a,b]` and `b>=1`, its successor-preimage is
   `S_t=[ell(max(a,1)),b-1]`.
   If `S_{t-1}={0}` or empty, `S_t` is empty.
   Therefore every nonempty `S_t` is a **single contiguous integer-index interval**, with `b_t=W-t+1`, and its exact endpoints are available in O(1) time per layer once `ell` is built.

### Proof

For fixed q, `U(p)` is nondecreasing with p. Thus whenever `p->q`, each `p'` with `p<p'<q` also satisfies `U(p')+1>=L(q)`, proving consecutive predecessors. Since `L(q)` is nondecreasing with q and `U(p)` is nondecreasing with p, no p smaller than `ell(q)` can become valid for q+1; hence `ell(q+1)>=ell(q)`.

The finishing-center condition is precisely the suffix `S_1=[a_1,W]`. Suppose `S_{t-1}=[a,b]`. The possible first centers are the union, over integers `q in [max(a,1),b]`, of predecessor intervals `[ell(q),q-1]`. Each is nonempty. Consecutive intervals touch or overlap because the one for q ends at q-1 while the next begins no later than q (the edge q->q+1 is always legal). By monotonicity of ell, the union begins at `ell(max(a,1))`; its right endpoint is `b-1`. This proves the formula and interval claim by induction. Empty and singleton-zero boundary cases follow directly.

Note: the former auxiliary index-distance estimate `q-p<=2R+1` uses **integer** event coordinates; the new interval theorem does not. The predecessor boundary can be computed by a two-pointer scan of monotone U/L in O(W+1) comparisons. The entire list of reachable suffix bands is then computed in O(W+K) time with O(W) auxiliary words, without finding nonzero DP rows or assuming their observed shape.

The min-plus/count DP on these exact intervals retains the same optimal costs, tied-optimal counts and lexicographic rank/unrank as the original dense recurrence, because the bands are *exactly* its feasible continuation support. Any internal zero-count hole predicted by a proposed implementation is an implementation or changed-graph issue under these assumptions, rather than an admissible generic complication.

## Reproduced frozen R5 result

The standalone Python verifier reconstructs 953 distinct exact rational activation walls from the original 15-atom `WEIGHTS` and `K0` vectors using `fractions.Fraction`, obtaining 954 cumulative boundaries and 1,065 activations, with multiplicity histogram `{1:869,2:56,3:28}`. For `R=2`, `K=213`:

- Radius-cover edges: **4,383**.
- First two suffix supports: **[951,953]**, **[946,952]**.
- Final suffix support: **[1,741]**.
- Total nonzero row positions: **83,813**, matching PR #2279 exactly, versus 203,202 dense positions.
- The exact array E has SHA-256 `444bd2011f09921fe4e385c899f700e5910b230d421b445121165a9af45496c9` under compact JSON integer-array serialization.

The new verifier independently scans the full original R5 graph for **all 213 layers** and matches every predicted interval. It additionally exhausts all 4,372 small exact arrays of 0..6 increments from {1,2,3}, all radius choices 0..3 and all permitted K: **28,432** layer checks against both dense graph reachability and direct enumeration of **443,524** subsets for suffix coverage. All comparisons passed.

Source code: `VERIFY_R5_INTERVAL_SUPPORT.py`; machine-readable exact outcome: `EXACT_OUTPUT.json`. Finite exhaustive coverage is the declared small domain, while the general interval theorem follows from the proof above.

## Engineering consequence and next unfinished scientific unit

The previous safe implementation computed a support-band from the min/max nonzero entries of every DP layer and allowed potential internal holes. The proved formula supplies **exact endpoints before each row computation**, so interval-backed arrays can avoid per-row dictionary support scans, hole bookkeeping and needless dense initializations. This does not itself establish an end-to-end runtime benefit.

Next experiment: compare original frozen R5 min-plus/count 12-byte decoder using dense rows, prior support-pruned rows and direct interval-addressed contiguous arrays. Verify equality of `J=1070`, `T_opt=1338767625695954932334592000`, the original 213 centers and all original 2,747,520 boundary/prefix queries; measure independent-process cold construction, decode time, RSS and queries. Preserve the source pin and the actual owner/CLAIM boundary. Draft research is not a formal Result or review.
