# Stage489-B — 一次固定位置内部编辑的完整未来观察修复

Date: 2026-11-07 Asia/Shanghai. Parent: Stage488-B commit d1ab98c4d91b0fbc404bd262d6e4d3070dfc4594; PR #1736. Scientific pins unchanged: GK bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. This is author-side proof, not Driver-admitted.

## Object and theorem

Let D={A,...,L} denote the 12 signed primitive directions of the six-axis X6 native space; A..F are positive, G..L negative. An original ordered history pair (P,Q) is observed through both lengths, both signed six-component total displacements, all 144 ordered-edge counts of each word, and K(P,Q), the number of coordinatewise equal letters in the overlapping prefix. Every POP removes the final letter (while length remains ≥1) and APPEND(x) appends the publicly specified direction x∈D. Each word has finite POP/APPEND budgets. Each operation is immediately observed. The same labeled operation sequence is tested on both candidate histories. Let ~0 be equality of every lawful observation trace of these base operations. Its definition does NOT assume the unreviewed Stage486-B formula.

Add at most ONE guarded Q_SET(j,z), replacing Q's existing letter at fixed absolute, one-based position j with z∈D. Its position is never rebased after POP. It does not change length or consume other operator budgets. It may interleave in any order with POP/APPEND. Original 1<j<|Q| and j>|P| are assumed; P is initially common on the compared pair and P's operations are publicly specified. Let ~1 be future equivalence for this enlarged language.

**Theorem 489.1 (exact and minimal one-shot edit lift):**

(P,Q1) ~1 (P,Q2) if and only if (P,Q1) ~0 (P,Q2) and

 (Q1[j−1], Q1[j], Q1[j+1]) = (Q2[j−1], Q2[j], Q2[j+1]).

All triple indices above are one-based.

**Necessity.** The enlarged language includes the no-SET paths, so ~1 implies ~0. For a triple (a,b,c), one immediate SET to z produces Δ-displacement v(z)−v(b) and Δ-directed-edges

δ_z(a,b,c) = −[a→b]−[b→c]+[a→z]+[z→c].

If b differs, native signed-unit v is injective, hence even the displacement response separates the cases. If b is identical but a or c differs, choose z outside {a,a′,b,c,c′}; 12 directions guarantee such a z. Edges with an endpoint z are disjoint from the removed original edges, and reveal a and c individually. Immediate Q_SET is legal at the original interior position j. Hence distinct triples are distinguishable.

**Sufficiency.** Couple equal labeled POP/APPEND/SET traces. Prior to SET, equal observations follow from ~0. When SET happens, either the original letter at j has survived, in which case its left neighbor and present symbol come from the common triple, and the right neighbor is the original common j+1 or a publicly APPENDed symbol; or that letter was already POPped, in which case position j and any subsequently appended neighbors are public, while a surviving original predecessor j−1 is supplied by the triple. The local displacement/edge and K corrections therefore match. Subsequently the edit differs from the counterfactual unedited trajectory at at most the single fixed index j, while it survives. The predecessor remains the common original j−1 (or a public append), and any successor is the original common j+1 or a public append. So all later observation corrections match as well; when POP removes position j, the correction vanishes. The two unedited reference trajectories agree at every step by ~0. This proves ~1.

The theorem works for arbitrary finite budgets and *all* lawful interleavings in the stated operation grammar. It is independent of whether the Stage486 proposed base repair key R_h is ultimately admitted; substituting R_h for ~0 remains conditional on a separate correctness proof. If editing within P's original extent, moving-relative indices, or multiple edits are introduced, those are separate mathematical questions.

**BRC realization.** Inside a fixed complete-initial-observer fiber, partition base classes by typed triples. Boolean support counts surviving (base,triple) keys. Positive original-history counts M(base,triple) obey Σ_triple M(base,triple)=M(base). This preserves branch provenance and raw multiplicity and uses no amplitude cancellation.

## Executed finite checks

The accompanying original standard-library experiment used P=T=ABGABA, W=GH, Q=TWAHA, u=6, 4096 H-words over ABGH and all 144 observed directed edge coordinates, with full native six-component Δ. It found 1202 initial-observer fibers. H=AAAABA and H=AAABAA share the initial observer, one-symbol H suffix, and local triple AAA at j=10. Exhaustive paired exploration of all legitimate interleavings with each of P_POP,P_APPEND,Q_POP,Q_APPEND,Q_SET budget 1 and every APPEND/SET value in the 12 signed directions visited **8788 states** without observation divergence. For H=AB versus H=BA at u=2, Q_SET(10,A) immediately distinguishes the histories despite identical initial observations and the original h=0 key. All 64 triples over ABGH had distinct 12-direction response profiles. Lexicographic ranks/unranks agreed for 12 three-symbol suffix repair keys in one finite fiber. Exact execution results and larger local source are recorded in Stage489-B run artifacts (not included in this compact proof text).

## Real all-144 active-edge population and cost scope

A deterministic Euler tour of the complete 12-vertex directed graph including self-loops once gives a length-145 signed-direction word with **all 144 directed pair types active**. The exact positive integer number of Euler trails starting and ending at A on these unit pair-counts is, by BEST plus the directed matrix-tree theorem,

N = 12^10 * 12! * (11!)^11,

which is a **343-bit, 104-decimal-digit** integer. The same closed formula was checked by independent exact memoized edge-subtraction Euler recurrences for d=2 (2 words, 10 memo states) and d=3 (72 words, 146 memo states). No all-144-edge dynamic rank/unrank run is claimed.

Four actual prefix inputs with s=5,20,60,144 active pairs compare (1) dense 144-tuple, (2) active-pair tuple, and (3) depth-two keyed dictionary/trie. Full dense observation construction from a word costs O(n+144); conversion to sorted sparse slots costs O(144+s), residual tuple copying costs O(s) vs O(144), and a trie shallow-copy costs O(d+row-width) in an abstract machine with constant expected dictionary access. Exact integer bit complexity is separate. Five-repeat microbenchmarks measured complete preprocessing (15 builds/repeat), independent 2500-edge-decrement transitions, and Python tracemalloc peaks; these are representation timings, NOT full DP timings. At s=5, recorded median 2500-transition seconds: dense .005755, sparse .001780, keyed .002823; full preprocess of 15 builds: dense .000672, sparse .000811. At s=144, transition seconds: .004505/.004453/.002824, preprocess: .001710/.002403/.002429. Runtime-specific totals and their scope are in executed artifacts; no universal speedup or polynomial bound at s=144 is claimed.

## Next

Stage490-B tests two fixed-index SET operations, especially neighboring indices, under interleaved POP/APPEND, and extends exact Euler memoization/rank/unrank on bounded signed edge support with complete cost accounting.
