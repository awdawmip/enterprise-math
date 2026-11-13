# R114 — Reversible cut support and a minimal future-stable eligibility observer

Date 2026-11-13, author-side auxiliary S23 research. **Not a formal Task CLAIM or native six-dimensional Heartbeat theorem; independent review pending.**
Frozen science pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Prior exact result: R113 `research_notes/brc_s23_av_r113_persistent_allk_atom_rank_index_20261113/PROOF.md` at commit `83153fcc892747cd56e5a4766c48da5ede70e04d`. Retain R111 reversible cut support and R112 first-difference capacity.

## Definitions and retained observer

Let `U` be a finite set of **complete identities** `(t,b)` under a strict total rank. Sources with common time `t` have the same eligibility `M_t(θ)`, regardless of `b`; histories are subsets `F,G⊆U`. `Top_k(F,θ)` is the eligible descending identity tuple truncated to `k`.

For rational S23 directed-circle observations use `Y_t(θ)=x+(t-j)θ`, `A(θ)=aθ`, `B(θ)=cθ`, and let `M_t(θ)` mean `{Y_t(θ)}` lies on the directed **half-open** fractional arc `[{A(θ)},{B(θ)})`; coincident endpoints mean empty. This is an auxiliary finite Boolean/rank carrier; no positive-weight BRC cancellation or native 6D link/port is assumed.

On rational closed `I=[ℓ,r]`, let `K_t(I)` be the set of interior integer roots of the six affine functions `Y_t,A,B,Y_t-A,Y_t-B,B-A`, excluding constant functions with zero slope. Their finite union partitions `I` into singleton endpoints/cuts and open rational gaps where every retained eligibility predicate is constant.

## R114.1 — Reversible supported crossing cuts

Write `T(F,G)={t:(t,b)∈F∪G for some b}` and `n(q)=Σ_{t∈T(F,G)}1[q∈K_t]`. The effective cuts are `K={q:n(q)>0}`. A one-sided edit to complete identity `(s,b)` changes only time `s` in the support:

- If `s` is present on both sides of the edit, the entire cut index is unchanged.
- If `s` appears for the first time, `n'(q)=n(q)+1[q∈K_s]`.
- If its last identity disappears, `n'(q)=n(q)-1[q∈K_s]`.

If `r_+` distinct cuts newly appear and `r_-` disappear, the number of exact atoms changes by precisely `2(r_+-r_-)`, because an interior cut replaces one open gap with a left gap, a singleton and a right gap. Fixed endpoints remain singleton.

**Proof of certificate inheritance.** On refinement, each new atom is contained in one old atom. All old time predicates have the same eligibility at the new atom's rational representative as on the parent atom: any isolated crossing would have been an old cut. Thus all old mask bits and rank-index source states are inherited; only newly supported time bits must be computed. On coarsening after the last identity of `s` disappears, all retained time predicates agree on every old atom swallowed by the merged interval, since every remaining time's cuts remain supported. Any old representative yields the same retained mask. Recalculate rank capacity under edited `F,G` (R112/R113); older snapshots remain immutable. This is an exact semantic update rule, not a claim of logarithmic total execution time. Cut enumeration, arbitrary precision, rank updates and historical memory remain priced separately.

## R114.2 — Coarsest future-stable quotient

Fix a **potential future** universe `U`, not just currently active sources, and define the time eligibility signature
`σ_U(θ)=(M_t(θ))_{t∈T_U}`, where `T_U={t:(t,b)∈U}`.

Two parameters `θ,φ` are *future-equivalent* when, for every pair of possible histories `F,G⊆U` and every `k≥1`, the truth value of `Top_k(F,θ)=Top_k(G,θ)` equals that at `φ`.

**Theorem.** `θ~_Uφ` **if and only if** `σ_U(θ)=σ_U(φ)`.

*If*: every potential identity is eligible at one parameter exactly when eligible at the other; entire source lists and all Top-k tuples are identical across parameters. *Only if*: when some time `t` differs, choose `u=(t,b)∈U`, `F={u}`, `G=∅`, `k=1`; equality holds exactly where `u` is ineligible, distinguishing the two parameters.

Consequently eligibility-signature classes are the coarsest quotient preserving all allowed future source-edit comparisons *without hidden access* to omitted eligibility/parameter information. If `d` signatures occur, exactly `d` abstract classes are needed. Connected interval indexes may use more atoms because repeated signatures can occur in disjoint parameter intervals. An active-history cut quotient uses `T(F,G)` and is safe for that history; when a future source from a formerly absent time arrives, its missing cuts must be reconstructed or retained latently. These two observer scopes are different.

## R114.3 — Scalar-capacity information-loss witness

For a fixed pair `F,G`, R112's first-difference capacity `h(θ)` determines all current Top-k *equality predicates*. It is not an edit-stable state for arbitrary future changes.

Take abstract ranks `a ≻ x ≻ b ≻ c`. Initially `C=F∩G={c}`, `Δ=F△G={a,b}`. At atom `J0` the eligibility vector for `(a,x,b,c)` is `(1,1,0,1)`; at atom `J1` it is `(0,1,1,1)`. Both have capacity 0. Add `x` to *both* histories: at `J0` the first eligible difference `a` still outranks `x`, so capacity stays 0; at `J1` the first eligible difference is `b`, now shielded by eligible common `x`, so capacity rises to 1. Identical old scalar capacities therefore produce unequal post-edit capacities. Extra identity/eligibility structure or an authorized recomputation oracle is necessary; this is not a lower bound on all S23-specific representations.

## Exact program, evidence and scope

Program `check_r114.py.gz.b64` is lossless gzip+base64 encoding of standalone Python 3 source (decode `base64 -d ... | gzip -dc > check_r114.py`, run `python check_r114.py`). It uses only `fractions.Fraction`, no floating-point. Parameters: `I=[0,1]`, `t=-4,...,4`, branches `b=0,1,2`, `(j,x,a,c)=(0,1/4,0,1)`, deterministic seed `1142026`; exact singleton/open-gap atomization and strict half-open boundaries. It independently verifies complete source lists against inherited mask/capacity on all observed atoms.

Local execution: `R114_PASS 500 15226 851 116 25`. This records 500 historical branching edits, 15,226 atom checks, 851 new cut events, 116 removed cut events, 25 necessity witnesses across adjacent distinct signatures. Also: 176 same-time-support edits, 324 changed time support, 59,351 old eligibility bits inherited vs. 8,764 computed, 11,654 rational disagreement witnesses, 195 cross-k comparisons, and 22 immutable historical roots checked. For the nine-time potential universe there were 47 exact atoms, 25 distinct eligibility signatures and 21 adjacent equal-signature pairs. A separate exhaustive six-identity test over times `-1,0,1`, two branches each, verified all `2^6×2^6=4096` ordered history pairs across 45,056 atom checks and `k=1,...,7`. Exact counters are in `verification_r114.json`.

Mathematical theorems hold for the stated finite ranked-eligibility model. Tests are finite and exact but do not by themselves establish uniform time or bit complexity, a native physical Cell/Link/Port admission, or independent review. The code's current snapshot maps/tuples do not implement asymptotically optimal persistent AVL updates, and inherited-bit counts are not benchmark speedups.

**Next R115:** combine a real persistent ordered cut index with persistent rank trees; separate source-universe-stable signatures from history-specific scalar capacities, and measure exact cut generation, rational bit lengths, historical memory, witness recovery, and adversarial time reintroduction. Determine whether restricted S23 same-time structure admits a stricter compressed future-stable observer. Preserve frozen science input and native embedding obligation.
