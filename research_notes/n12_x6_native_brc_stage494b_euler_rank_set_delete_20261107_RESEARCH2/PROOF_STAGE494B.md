# Stage494-B — Full 144-edge Euler–BRC lexicographic ranking and sequential SET→DELETE residual

Status: **AUTHOR-SIDE EXACT PROOF / EXECUTED INTEGER VERIFICATION / UNREVIEWED / NOT ADMITTED**. Parent Stage493-B: commit `87f5e2ed008d81446deae35400a367696a75c429`, PR #1736. Immutable scientific pins: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current normative context: global main `f1ad7ad5b25d136814b3e9e7e5bdd45db051d01c`, EM main `1122007eefdcbd2052347af04d09bc0a846875ba` at 2026-11-07 UTC ~01:13. Preserve original history identities (positive multiplicity-one BRC branches) and directed X6 relation counts.

## Theorem 494.1 (closed-form exact population for any directed Euler word)

Let `D` be the 12 signed native X6 step letters, one for each `+E_i` or `-E_i`, not an additional spatial dimension. Let `M=(m_{ij})` be a nonnegative integer matrix of counts of *ordered consecutive direction pairs*. A history `w_0,...,w_n` of length `n+1` realizes `M` when the consecutive ordered pairs occur with multiplicities `m_{ij}`, where `n=sum m_{ij}`. Fix the first letter `s` and final letter `t`; count different **value words**, each with unit raw branch population.

Write `o_v=sum_w m_{vw}`, `i_v=sum_w m_{wv}` and `V_+=\{v:o_v+i_v>0\}\cup\{s,t\}`. For nonempty M, the required Euler imbalance is `o_v-i_v=1[v=s]-1[v=t]`; if this fails, the population is zero. Let `tau_t(M)` be the number of directed spanning arborescences toward t of the multigraph restricted to `V_+`, computed by deleting t's row and column from the outgoing directed Laplacian `L_{vw}=1[v=w] sum_{z≠v} m_{vz} - 1[v≠w] m_{vw}` and taking its determinant. Self-loops do not enter L. If a nonterminal vertex has zero outdegree or `tau_t=0`, the population is zero. Otherwise

```text
N(M;s,t) = tau_t(M) * o_t! * product_{v in V_+ minus {t}} (o_v-1)! / product_{v,w} m_vw!.
```

For the empty edge inventory, `N=1[s=t]`.

**Proof.** Label temporarily each of the `m_vw` parallel arcs. In any complete Euler trail ending at t, at each `v≠t` the final outgoing arc forms, jointly, one directed arborescence toward t (otherwise the last-exit arcs contain a directed cycle that the trail could never leave). Conversely any such arborescence, an arbitrary order of all outgoing arcs from t, and an arbitrary order of all outgoing arcs at each nonterminal v with the prescribed tree arc last determine exactly one Euler trail by repeatedly taking the next unused local arc: if the procedure prematurely stops, a vertex with unused arcs on the traversed component would contradict the tree-last-exit property. Thus the count of labeled trails is `tau_t o_t! ∏_{v≠t}(o_v-1)!`. Every value word arises from exactly `∏m_vw!` labelings of its parallel arcs, giving the displayed exact integer quotient. The Laplacian minor counts the directed rooted trees by the directed matrix-tree theorem, including parallel arcs but excluding loops.

**Corollary: all native X6 ordered edge types active.** Take all `12²=144` ordered pairs exactly once and start/end at A. The off-diagonal graph is a complete bidirected 12-vertex graph, so `tau_A=12^(12-2)`. Therefore

`N=12^10 * 12! * (11!)^11`.

Executed exact count: `12158005148129205525344033033623852119586471620751100464227382815205544467365888000000000000000000000000` (104 decimal digits; 343 bits). Each word has 145 direction symbols and all 144 directed edges once.

## Theorem 494.2 (exact rank / unrank without enumerating N histories)

At any prefix ending at v, delete the already used directed edges from M and let the required terminal letter remain t. Test next letters `x` in native alphabetical order; for each available edge `v→x`, its entire lexicographic block has `N(M-e_vx;x,t)` completions, as computed by Theorem 494.1. Subtract blocks from a zero-based input rank until entering its block; append x and continue. The inverse adds the blocks for all smaller letters before each actual next letter. Induction on the number of remaining edges proves that these two algorithms are mutual inverses for all valid ranks and all Euler value-words. No enumeration of the 104-digit population is required.

For `n` remaining edges and `d` supported letters, each rank step tries at most d candidates and each count uses one at-most-`(d-1)×(d-1)` exact integer determinant plus factorials, multiplicities and degree checks. This gives at most `nd` count-oracle calls (and an `O(nd^4)` arithmetic-operation bound with cached factorials and cubic Bareiss determinants). Inputs require `d²` nonnegative edge counts and two endpoints; output recovery emits `n+1` letters. Rank integers have `O(n log(nd))` bits in this regime. There is no claim of sublinear output complexity.

## Lemma 494.3 (two internal edits do not add independently)

Consider an ordered substring `a b c d`. SET original b to public z, then DELETE its immediately following original c; final substring is `a z d`. Denote an edge count by `[xy]`. With `δ_SET` and `δ_DELETE` each calculated independently against the original string:

```text
Δ_joint = -[ab]-[bc]-[cd]+[az]+[zd]
δ_SET  = -[ab]-[bc]+[az]+[zc]
δ_DEL  = -[bc]-[cd]+[bd]
I      = Δ_joint - δ_SET - δ_DEL = [bc]+[zd]-[zc]-[bd].
```

This identity holds for coinciding and distinct symbols among all twelve signed native directions. For `a=A,b=A,c=B,d=A,z=C`, the nonzero interaction is `[AB]+[CA]-[CB]-[AA]`. The same signed edge-residual representation applies to adjacent paths; discarding it loses the exact joint observer. Deleting the *just SET* center has the same **terminal** word as deleting that center directly, but an observer reading after the intermediate SET can still distinguish the traces; a terminal-only identification requires that changed observation scope.

## Executed verification (2026-11-07)

Runnable Python standard-library source: `REPRO_STAGE494B.py`. Actual stdout: `REPRO_STAGE494B_EXECUTED_STDOUT.txt`. It independently enumerated **4,663** binary directed-edge inventories/endpoints with 1,692 valid Euler paths in total, checking each population and full lexicographic rank/unrank against raw path enumeration. Another **320** ternary-inventory endpoint cases checked parallel-edge multiplicities against raw enumeration. It checked **20,736 = 12^4** sequential SET→DELETE identities and found **17,424** nonzero interactions with fixed a=A. For the complete 144-edge graph, it executed **9 rank/unrank roundtrips** at boundary, midpoint and pseudorandom 343-bit ranks and checked that every recovered 145-symbol word uses every ordered pair exactly once. All assertions passed in one standard-library run (wall time approximately 1.074 s for the local invocation). The exact count, not all 10^103 words, was computed.

BRC representation: the directed signed X6 step history is a positive, provenance-distinct branch carrier with exact integer edge observer and *value-word* class population; this is a mathematical combinatorial certificate, not a measured physical evolution, phase cancellation or newly accepted native dynamics. The original P000 assumptions remain untouched.

## Open step

Stage495-B: construct a composable transported local-state criterion for two dynamic internal edits amid INSERT/DELETE/POP/APPEND, test whether initial two triple values suffice and search for shortest strict counterexample; benchmark full 12-direction rank/unrank with nonuniform sparse and dense *multiplicity* inventories, including input bit cost, determinant growth and repeated-query caching. Native CLAiM/Result and independent Driver review remain pending.
