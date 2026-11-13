# R115 — Persistent signature-indexed Top-k certificate and event incidence

Date 2026-11-13. Enterprise Math Research1, author-side S23 auxiliary finite ranked Boolean model. Predecessor R114: `a5164fbc655dd09aa3fb681cca48d1f1003c5f78`, `research_notes/brc_s23_av_r114_future_stable_time_atoms_20261113/PROOF.md`. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This paper assumes no native six-dimensional Cell/Link/Port admission and no mathematical independent review.

## Definitions

Fix a finite universe `U` of complete ranked identities `(t,b)` with strict descending total rank. The time eligibility Boolean `M_t(θ)` is shared across branches with the same time, but identity, branch and membership provenance are never discarded. Histories `F,G ⊆ U` yield the descending tuple of eligible identities `Top_k(F,θ)`, truncated after `k`.

For the directed half-open fractional-arc S23 auxiliary observer, fix a rational closed interval `I`. Form a conservative exact atomization with singleton endpoints, singleton interior cuts, and open gaps at the integer intersections of the six affine phases `Y_t,A,B,Y_t-A,Y_t-B,B-A`. Each `M_t` is constant on every atom. Write their ordered sequence `J_0,...,J_(q-1)`.

For a *potential future* universe `U`, define the full eligibility signature `σ_U(θ)=(M_t(θ))_(t∈T_U)`, the set `S` of signatures attained by the raw atoms, and `d=|S|`. The future universe stays fixed throughout this theorem; a future source with an unindexed time is an R116 extension problem.

## R115.1 — Coarsest connected future-stable partition

At the edge between consecutive raw atoms define

`a_i=Σ_(t∈T_U) 1[M_t(J_i) ≠ M_t(J_(i+1))]`.

**Theorem.** The coarsest *connected* parameter partition that preserves the truth of every possible `Top_k(F,θ)=Top_k(G,θ)` for all `F,G ⊆ U` and all positive `k` consists exactly of maximal runs of identical full signatures. Its number of cells is

`N_conn = 1 + Σ_(i=0)^(q-2) 1[a_i>0]`.

*Proof.* If `a_i=0`, all source identities have the same eligibility on the two consecutive atoms, so all Top-k tuples and equality predicates agree; the atoms may be merged. If `a_i>0`, choose a changing time `t`, an identity `u=(t,b)∈U`, and histories `F={u},G=∅,k=1`. The equality predicate changes across that edge, so no connected valid cell can cross it. The maximal runs attain the lower bound, retaining the precise open/closed endpoint membership. Nonadjacent equal-signature runs may share an *abstract* state but cannot be represented as one connected interval. QED.

**Dynamic corollary.** For an active subset of times `A ⊆ T_U`, replace the sum by `a_i(A)`. Adding/removing time `t` changes precisely its Boolean transition edges by `±1`. An inverted index from time to actual toggle edges maintains the active observable connected partition, and ignores algebraic crossings that leave all eligibility bits unchanged. This describes the **Boolean observer** under fixed `U`, not physical or signed BRC cancellation.

## R115.2 — Two-level immutable signature/rank index

Let `n=|U|`. For a fixed signature `s`, mark each ranked source identity leaf:
- `common=1` if it is eligible and in `F∩G`;
- `diff=1` if it is eligible and in `F△G`;
- both zero otherwise.

The two counts are mutually exclusive at a leaf. A persistent balanced segment tree stores subtree common/diff counts. If no eligible diff exists, define `h_s=+∞`; otherwise descend to the highest-ranked eligible diff and accumulate eligible common counts in skipped earlier subtrees. This obtains `h_s` in `O(log(n+1))` node visits.

**Theorem.** Given the above finite ranked Boolean model, for all `k≥1` and `θ∈I`,

`Top_k(F,θ)=Top_k(G,θ) ⇔ k ≤ h_(σ_U(θ))`.

Indeed all earlier eligible identities are common, so every Top-k prefix up to their count agrees, and the next position contains a difference in exactly one history (or a different next eligible identity). This is the first-difference argument of R112 used at its exact scope.

Store for each distinct signature `s∈S` a rank-tree root and `h_s` in an immutable outer balanced segment tree. At each internal outer node store the minimum capacity and an attaining signature index. Then

`K*(I)=min_(s∈S) h_s`

is available from the outer root in `O(1)` further node visits, and `k≤K*(I)` is the necessary and sufficient condition for full-interval equality. When `K*` is finite, an exact rational representative of a raw atom realizing the reported signature is a difference witness for every `k>K*`.

For a one-sided addition/deletion of complete identity `u=(t,b)`, only signatures with `s(t)=1` change their corresponding rank leaf. Let `d_t=|{s∈S:s(t)=1}|`. Path-copying the affected rank and outer paths needs

`O(d_t (log(n+1)+log(d+1)))`

new tree nodes and unit-cost tree operations **after** global signature/cut preprocessing and assuming a persistent source-membership representation. All older history roots remain unchanged and may fork arbitrarily. If `d_t=0`, the outer root is reused. An absent time returning later within the same potential universe needs no new signature preprocessing.

**Cost accounting.** The bound counts the two trees. Preprocessing must still enumerate/sort all needed exact rational cuts, evaluate source eligibilities on atoms, and index their signatures. Exact rational arithmetic incurs input-dependent bit operations; lookup of an arbitrary rational parameter needs a predecessor search in the raw cuts or direct signature evaluation. The Python checker uses copied `frozenset` histories and therefore spends an additional `O(n)` membership-copy cost per edit; its tree allocation counters do not measure this. The permanent set of rational representatives and signature index also consumes storage. There is no claim of a general polynomial-in-input-bitlength atomization bound or benchmark speedup.

## R115.3 — Reversal, branch provenance and retention

Reversing a one-sided membership edit restores `F,G`, every `h_s` and all Top-k equality predicates. Path-copying alone does **not** guarantee the exact old root object is recovered by pointer identity without hash-consing. Older roots themselves remain valid immutable snapshots. Removing the last active identity at time `t` and later reintroducing one can reuse the full potential-universe signature scheme; the source identity, branch and order remain explicit.

## Exact checker, output and scope

The lossless `check_r115.py.gz.b64` decodes to standalone Python 3 `check_r115.py`:

`base64 -d check_r115.py.gz.b64 | gzip -dc > check_r115.py`
`python check_r115.py`

It uses only `fractions.Fraction`, immutable dataclass nodes and exact Boolean comparisons. Fixed parameters: `I=[0,1]`, times `-4,...,4`, branches `0,1,2`, `(j,x,a,b)=(0,1/4,0,1)`, random seed `1152026`. The directed circle arc is half-open, with empty coincident endpoints. Both singleton cuts and open rational gaps are tested.

Actual local output: `R115_PASS 22 47 25 26 511 527 43945 525`.

There are 22 distinct internal algebraic cuts and 47 exact raw atoms, compressed to 25 distinct future eligibility signatures or 26 maximal **connected** runs. Of the 46 adjacent edges, 25 have nonzero eligibility transition incidence, leaving 21 redundant edges for this observer. A total of 50 per-time toggles are present across these edges.

The executable checks 510 randomized one-sided history edits (126 historical forks), retains 511 main historical roots, audits 527 full versions (including past snapshots), performs 43,945 direct Top-k comparisons, and validates 525 exact rational difference witnesses. A separate exhaustive 4-identity check evaluates all `2^4 × 2^4=256` ordered pairs and `k=1,...,5` for each of the 25 observed signatures. The add/remove/re-add case is also checked.

Actual counters (including initial node construction): 6,286 changed per-signature rank roots, 36,584 new rank nodes, 35,509 new outer map nodes; 8,789 raw-atom checks; maximum rational representative numerator/denominator bit length 8. The script SHA256 is `c23a6589c496ddd60d0125b80adf0ce7fc9de9e2af1cac8a653c56595c62ab92`. Full counters are in `verification_r115.json`.

**Next R116:** expand `U` with formerly unavailable times. Test online persistent signature refinement, old-rank-root inheritance, exact rational bit complexity, wildcard/dormant time bits, and adversarial add/delete/reintroduction; compare with full rebuilding without losing identity provenance.

Status: author-side proof and exact finite checks, outside canonical Task CLAIM/Result and independent review. Existing R114 scientific pin remains frozen.
