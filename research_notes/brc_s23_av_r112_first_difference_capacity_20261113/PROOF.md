# R112 — First-difference capacity and rank-tail pruning for exact all-k equivalence

Date: 2026-11-13 (Asia/Shanghai). Scope: auxiliary rational directed-circle S23, continuing R111. Status: author-side mathematical derivation and finite exact computational validation; independent review pending.

Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. No native Heartbeat-X6 embedding is asserted. Relevant earlier source: R111 `research_notes/brc_s23_av_r111_reversible_cut_support_20261113/PROOF.md` at `821b74c7c3b0c79e79418a0a826860f50b31a224`.

## Model

Let `(U, ≻)` be a totally ordered collection of **complete, distinct source identities**, with each active source possessing an eligibility predicate `M_u(θ)` on a parameter domain `I`. For finite versions `F,G⊆U`, `Top_k(F,θ)` is the descending ordered tuple of the first `k` eligible source identities (or all eligible identities when fewer than `k` exist), for integer `k≥1`. Sources must retain identity, including branch label; equal observed membership does not merge identities. Define `C=F∩G` and `Δ=F△G`. In S23, `u=(t,b)` and `u≻v` means descending lexicographic order. Membership depends on `t` but not `b`:

`M_t(θ)` iff `{x+(t-j)θ}` lies in the positively directed **half-open** fractional-circle arc from `{aθ}` to `{cθ}`, with equal endpoints yielding the empty arc. Here `j,a,c∈ℤ`, `x∈ℚ`, and `I=[L,U]` is a nondegenerate closed rational interval.

## R112.1 — First-difference position theorem (pointwise, exact and sharp)

For fixed `θ`, let `Δ_θ={u∈Δ : M_u(θ)}`. If `Δ_θ` is empty, define `h(θ)=+∞`. Otherwise let `d(θ)=max_≻ Δ_θ`, the *highest-ranked eligible differing identity*, and set

`h(θ)=#{v∈C : v≻d(θ), M_v(θ)}`.

Then for **every** positive integer `k`:

`Top_k(F,θ)=Top_k(G,θ) ⇔ k≤h(θ)`.

If `h(θ)<∞`, the first differing position of the two fully ordered eligible lists is exactly `h(θ)+1` (one-indexed), even if one list ends there. Both lists have the same prefix consisting of all eligible common identities above `d(θ)`.

**Proof.** All identities strictly higher than `d(θ)` which are eligible must belong to both versions, by the maximality of `d(θ)` within the eligible symmetric difference. Their common descending sequence has length `h(θ)`. At the next position, the version containing `d(θ)` lists it, while the other version cannot list it; the other version either stops or lists a lower-ranked identity. Thus the first difference is precisely after the shared prefix. If no differing identity is eligible, the full lists coincide. This establishes both directions for every `k` simultaneously. ∎

## R112.2 — Whole-interval all-k capacity and exact witness

Define the equivalence capacity

`K*(I)=min_{θ∈I} h(θ)`, with minimum of only `+∞` values defined as `+∞`.

Then for all integers `k≥1`,

`(∀θ∈I, Top_k(F,θ)=Top_k(G,θ)) ⇔ k≤K*(I)`.

For finite capacity `K*(I)=m`, any point `θ*` attaining the minimum is an **exact disagreement witness for every `k>m`**, while equality is certified for all `1≤k≤m`. No separate enumeration for each `k` is required.

**Proof.** Apply R112.1 pointwise and commute the integer threshold condition with the universal quantifier: `∀θ (k≤h(θ))` iff `k≤min h`. A minimizing point has first divergent index `m+1`, so it witnesses failure for all larger `k`. The S23 interval minimizer exists among finitely many exact atoms described next. ∎

## R112.3 — Rank-tail pruning and sufficient cut set

When `Δ` is nonempty, let `d_min=min_≻ Δ`, i.e. the **lowest-ranked** differing identity, and define the relevant source set

`R=Δ ∪ {v∈C : v≻d_min}`.

When `Δ=∅`, put `R=∅`. For any parameter `θ`, `h(θ)` depends only on the membership predicates of the sources in `R`. Consequently every common source `v⪯d_min` may be excluded from the interval certificate without altering `K*(I)` or any difference witness. For each time `t` occurring in `R`, generate exactly the six affine crossing sets used in R111:

`aθ, cθ, (a-c)θ, x+(t-j)θ, x+(t-j-a)θ, x+(t-j-c)θ ∈ ℤ`.

Let `T_R(I)` be the union of their distinct *interior* rational solutions, with zero-slope forms contributing no cuts. The singletons of `T_R(I)∪{L,U}` and the open gaps between adjacent cuts partition `I` into exactly `2|T_R|+3` atoms. On each open gap, all eligibility predicates of `R` are constant; endpoints are checked separately. Evaluating `h` at each singleton and one exact rational midpoint per gap therefore yields **the exact `K*(I)`** and (when finite) a rational minimizing witness.

**Proof.** For any eligible differing `d`, its eligible higher common sources belong to `R` because `d≽d_min`. Hence both the maximum eligible difference and its common prefix count use only `R`. Each S23 membership predicate changes only at one of its six affine integer-crossing sets; no such crossing occurs inside an open gap of the proposed partition. Half-open endpoint behavior is determined exactly at the singleton, and all gap midpoints are rational. R112.1 and R112.2 then apply. ∎

### Exact relevance-index update under branching edits

For each historical version pair, let `S_R={time(u):u∈R}` and maintain immutable support counts

`n_R(q)=Σ_{t∈S_R} 1[q∈K_t(I)]`.

Upon a single-sided identity toggle, recompute the *relevant time set* `S_R'` from the updated identity sets. The exact transition is

`n_R'(q)=n_R(q)+Σ_{t∈S_R'\S_R}1[q∈K_t(I)]−Σ_{t∈S_R\S_R'}1[q∈K_t(I)]`.

In an AVL support-index representation, key updates cost `O(Σ_{t∈S_R△S_R'} |K_t(I)| log(N+Σ|K_t|+1))` rational key comparisons/structural node allocations, apart from computing `R` and the crossing streams, arbitrary-precision bit costs, and certificate evaluation. If relevant times do not change, the support-index root can be reused. The lowest-difference boundary can move after an edit, so multiple relevant times may enter/exit: a one-sided identity toggle is **not** in general a one-time-only update. The formula is exact for arbitrary history forks and allows reversible coalescence as in R111.

## Computation, evidence and limitations

Program: `check_r112.py.gz.b64` is a gzip-compressed UTF-8 Python file encoded as base64; decode with `base64 -d ... | gzip -d > check_r112.py`, then run `python check_r112.py`. It uses exact `fractions.Fraction` arithmetic, a fixed S23 observation `(j,x,a,c)=(0,1/4,0,1)`, `I=[0,1]`, and three deterministic random seeds `11201,11202,11203`.

The program performs 360 historical forked identity toggles over time values `-5..5` and branches `0..3`, verifies the incremental relevance counter against full recalculation at every edit, and compares all-k capacity with independent direct Top-k sorting at all selected cut singleton and midpoint representatives. It also checks the direct first-difference index and restores exact rational witnesses for all non-equivalent `k` in the tested finite range. The returned JSON is `verification_r112.json`, reporting 22,532 exact atom representatives, 5,619 all-k certificate checks, 22,532 first-divergence checks, 5,556 tight witnesses, 300 unchanged relevance-time roots and 60 changed relevance-time supports; all assertions pass.

A sparse constructed family has one high-ranked difference `(0,0)` and 30 lower-ranked common times. The full support of all time sources has **448** distinct interior crossings; the relevance-filtered support needs **1**. Identical versions have no relevant cuts regardless of how many common source crossings exist. These are exact structural reductions in required cut enumeration, not measured CPU gains. Dense random instances may have little or no pruning. The general claims rest on the proofs; random tests validate implementation only. This auxiliary directed-circle model is not identified with native six-dimensional Heartbeat dynamics.

## R113 research frontier

Develop a persistent all-k capacity segment tree with rank-tail filtered time supports, and integrate changes of `d_min` without scanning the entire common identity set when branch edits are local. Test cases where the lowest difference oscillates across a long rank prefix and quantify real runtime, memory, big-integer bit cost, proof/witness recovery cost and alternative explicit-materialization baselines. Study how guard-interval dominance certificates allow pruning additional high-rank crossings while preserving the first-difference position.
