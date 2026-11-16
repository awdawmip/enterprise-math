# R641｜V26/V27 原生主动三元组的非交换路径记忆与最小有限状态
Date: 2026-11-08. Status: AUTHOR_SIDE_EXACT_THEOREM / EXACT_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.

## Source, frozen inputs, and typed domain

Direct original program: `awdawmip/enterprise-math@b62110008321d9147212cb89f2627ff613c2550d:experiments/x6_dynamic_law_holonomy_v24_20260906/check_channel_circulation_bridge.py` (blob `5618dae00632f9f796d3f5a6a692c248ea699131`). Its `TRIADS`, `NEIGH`, `transport_slots`, `holonomy` define the precise finite operator studied here. Its V26 paper `research_notes/X6_CHANNEL_NONRECIPROCITY_CIRCULATION_BRIDGE_V26_20260906.md` (blob `a8252050cc03f6930bb86251094d899c04743b60`) supplies the internal PF10 four-port signed edge score. Predecessor R640: Git `d57da3c84cb9add0d563d2c22dfd9a0d503f1ad9`. Frozen signed-K scientific input R462 remains `18783e01e3646c72b7aab3b16d3f565e83e6446f`; the present exact group-theoretic result does not evaluate K coefficients. P000/ACTIVE unchanged.

All labels below are the SIX native X6 axis labels used to index finite active triads, **not** a claim that the active-triad graph is the full six-dimensional Cell space or that PF10 internal port labels equal spatial axes. The model is the source-defined twenty vertices `V={S⊂{0,...,5}:|S|=3}`, with one allowed directed step `S→T` iff `|S∩T|=2`. The three inherited slots are distinct elements `{0,1,2}`. A state `(S,σ)` assigns one slot bijectively to each member of S. Each edge preserves slots on S∩T and transfers the departing member's slot to the arriving member. Source's `transport_slots` implements this operation. No PF10 count time-update is postulated.

## Theorem 1: exact counting-histogram collision for noncommutative holonomy

Fix `S0=(0,1,2)` with initial slot map `0→0,1→1,2→2`. The following are legal three-edge closed walks (parentheses denote the active triad, NOT spatial Cell addresses):

```
A: (012) → (013) → (023) → (012)
B: (012) → (013) → (123) → (012)
```

The source step rule gives `Hol(A)=(0,2,1)`, `Hol(B)=(2,1,0)` in the slots ordered by (0,1,2). For the concatenations `AB` and `BA`, direct exact transport gives

```
Hol(AB)=(1,2,0)
Hol(BA)=(2,0,1)
```

These are different elements of S3. Yet the FULL directed-transition histogram `h_γ(S,T)=#{k:(S_k,S_{k+1})=(S,T)}` is identical for AB and BA: its entries are sums of the very same two closed-loop edge multisets, independent of their concatenation order. Both walks have length six and share base and endpoint. Consequently **no deterministic readout factoring solely through the complete unordered directed-triad-edge histogram** recovers exact ordered slot holonomy for every legal history. This is an exact counterexample even for a much finer histogram than a mere scalar transition count.

This theorem is scoped to the V26/V27 source **active-triad path** language. PF10 four-port `I,O,M` are independently typed internal counts. A future PF10-to-triad-edge event map must be explicitly established before asserting the two walks have equal PF10 counts.

## Theorem 2: 120 states are necessary and sufficient for (triad, full slot map)

For fixed initial S0, define `Q={(S,σ):S∈V,σ:S→{0,1,2} bijective}`. Thus `|Q|=20·3!=120`. The source transport defines a deterministic state update `δ((S,σ),T)=(T,σ')` for every T adjacent to S; the resulting state records both the current active triad and the complete ordered-slot identity. Hence Q is sufficient for all finite legal histories, and its terminal state gives the exact source slot map (and closed-loop S3 holonomy).

All 120 states are reachable from the fixed initial state: source-admissible three-edge closed walks at S0 give each of the three slot transpositions (see Theorem 3 and checker). Two different transpositions generate all S3. For any target T, J(6,3) is connected (replace one nonshared label per step), so choose a fixed S0→T path. Prefix that path by each of the six distinct base-loop permutations; transporting a bijection preserves distinctness, hence six slot states are reachable at T. For an observer required to output **both** current T and its full σ, all 120 reachable outputs differ. Any deterministic state summary permitting exact current output needs at least 120 distinguishable values. Q realizes that lower bound.

This minimality is an observer-target theorem, not a claim that a full PF10/X6 physical state has only 120 states.

## Theorem 3: exact smaller quotients for narrower observers

If the declared output is (current triad, parity of its slot permutation relative to sorted target labels), the edge carries a fixed permutation of ordered positions `f_{S,T}`, independent of σ; `σ'_T=σ_S∘f_{S,T}`. Therefore `sign(σ'_T)=sign(σ_S)·sign(f_{S,T})`. The induced 40-state update on `(S,sign σ)` is closed and deterministic; all 40 current outputs are reachable, so 40 is optimal **for that output**. For the current triad alone, the 20-state quotient is sufficient and necessary. For closed loops at S0, the exact full S3 holonomy output has six possible values; parity alone has two.

In particular, frozen V26 edge score `Φ(S,T)=uᵀc(T)+c(S)ᵀΩc(T)`, with fixed u,Ω and code c, requires only (S,u,Ω) for the next-score computation; full slot memory is additionally required if exact V17 S3 transport/holonomy is requested. Its positive Weighted-BRC weights `ρ^{Φ}` remain positive; signed Φ and noncommutative holonomy are separately typed observables.

## Exact finite certificate

A Python-standard-library independent checker reconstructs all 20 vertices and 180 directed adjacent edges, validates source-style slot transport on all 120×9=1080 reachable transitions, checks the two six-edge witnesses and their complete directed histogram, and exhaustively checks the 36 simple oriented three-step base loops. There are 18 identity loops and 18 nontrivial loops (six for each of three transpositions); among 630 unordered pairs of these loops, 108 are noncommuting under path concatenation. The six closed-loop holonomies, 120 full open states and 40 parity states are all enumerated. The 40-state quotient's 360 transition rows are verified well-defined. Marker `R641_X6_ORDERED_HOLONOMY_120_STATE_EXACT_PASS`.

## Next exact bridge

Locate an actually admitted PF10 event-history/step-update law and a typed map from its four source ports to active-triad transition events. Test if the current PF10 snapshots carry the ordered loop information or require a distinct S3 accumulator. A proposed minimal nonperturbative overlay for full path transport is the six-valued slot permutation over each current triad (or only its parity for parity-limited observers); the mathematical update above is exact on the source-defined triad graph. Check source, branch, path and event-time behavior against the actual update before native physical claims. An independent Driver proof review and formal Source CLAIM are still separate.
