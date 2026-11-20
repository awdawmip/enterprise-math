# Stage471-B — Deterministic exact support, population and ranking for growing Q-POP windows (2026-11-06)

Status: AUTHOR_SIDE_MATHEMATICAL_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED. This note is an independently checkable continuation of Stage469-B and Stage470-B, not a formal Source Result.

## Scientific model and frozen input

Original ordered histories `P,Q` use `Sigma={A=+E1,B=+E2,C=+E3}` inside native six-dimensional X6, and begin with A. Lengths satisfy `4<=m=|P|<n=|Q|`. Initial complete observer `Phi` records both lengths, full signed six-axis displacement, each entire 12x12 ordered adjacency matrix, and exact position-match count `K`. Each original history pair contributes one positive integer BRC branch mass. Future language is Stage469-B's labeled tree: POP_P<=1, APPEND_P<=1, POP_Q<=h, APPEND_Q<=1, with all 12 signed native directions available for either APPEND; interleavings and popping appended letters are included.

Scientific pins inherited **without rebasing**: GLOBAL main `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM main `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 Blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. The Stage469 future-equivalence theorem is an author-side, presently unreviewed mathematical premise. Current normative rules were independently read from the canonical main entrypoints.

Set `t=max(1,n-h)` and assume `1<=t<=m-2` (a growing overlapping exposure window; in particular positive h). Stage469-B's repair `R469` then reduces exactly to the visible ordered repair word
```
V_t = (Q_t, (P_{t+1},Q_{t+1}),...,(P_m,Q_m),Q_{m+1},...,Q_n).
```
Indeed, Stage469's extra tags P_(m-1), Q_m and Q_(m+1) are already visible in this range. The tuple is compared in the displayed lexicographic order over A<B<C; paired symbols are ordered first by P, then Q.

## Theorem 471.1: deterministic positive BRC support

**Statement.** On *every feasible complete initial observer fiber* Phi in the domain above and for every `1<=t<=m-2`, exact populations `M(V_t)`, distinct future-equivalence class count `q_F = #{V_t:M(V_t)>0}`, and support-lexicographic rank/unrank are computable using a polynomial number of nonnegative integer operations in `m+n` for the fixed three-direction original alphabet, without enumerating the histories or emitting all repair words. The support algorithm is deterministic and works when `h` grows with `n`.

**Construction.** Let `E_P,E_Q` be the original 9-entry A/B/C ordered-adjacency vectors. Compute the exact positive integer prefix table `H_t(x,q,E_P^0,E_Q^0,k)`: number of pairs of length-t prefixes starting at A, ending in `P_t=x,Q_t=q`, with consumed directed edges `E_P^0,E_Q^0` and exactly `k` matches. This is the ordinary positive BRC pair-prefix recursion with fixed nine-plus-nine remaining-edge counters and the match counter.

For a prospective visible word `v=V_t`, let `q=Q_t`, `a=P_(t+1)`, `U_P` count P's **internal visible** edges `P_(t+1)->...->P_m`, `U_Q` count Q's visible edges `Q_t->...->Q_n`, and `k_v=sum_(j=t+1)^m [P_j=Q_j]`. Write `e_(x,a)` for a single P junction edge. Its exact original-history population is

```
 M(v) = sum_(x in Sigma, E_P^0,E_Q^0,k)
 H_t(x,q,E_P^0,E_Q^0,k)
 * [E_P^0 + e_(x,a) + U_P = E_P]
 * [E_Q^0 + U_Q = E_Q]
 * [k+k_v=K].
```

The quantity on the right is nonnegative and is determined **only by** the visible word's bounded-integer sufficient state `(q,a,U_P,U_Q,k_v)`, not by its full internal order. A left-to-right labeled suffix automaton starts from each `q` and emits one unique next P/Q pair at positions `t+1..m`, then one Q letter at positions `m+1..n`. It maintains `(position,q,lastP,lastQ,firstVisibleP,U_P,U_Q,k_v)`. A terminal state accepts iff `M(v)>0`, assigning terminal weight `M(v)`. Every different visible repair word is exactly one path. Merging equal states sums paths as *distinct labels* for Boolean support, while summing their terminal weights computes total raw population. A memoized child-support table supports lexicographic rank/unrank via deterministic branch counts; its terminal weight supplies class population.

**Proof.** Any full history pair uniquely splits into its first t steps and its visible suffix, and the sole P edge crossing the split is `(P_t,P_(t+1))`; Q's suffix explicitly starts at `Q_t`, so it shares no missing Q junction. The three displayed equalities are necessary for original adjacency and K to match Phi. Conversely, joining any prefix counted by `H_t` to a visible suffix satisfying all three equalities reconstructs precisely one valid full pair; fixed first A and directed-edge counts determine both signed six-axis endpoints through `N_z=[z=A]+sum_y E_(y,z)`. Thus the formula counts each full history exactly once. Distinct visible words are unique paths of the deterministic suffix automaton. The Boolean terminal condition depends only on its state, so memoized backward support recursion counts each feasible *word* once, independently of how many hidden prefixes realize it. Its lexicographically ordered child counts yield mutually inverse zero-based rank/unrank. Under the stated Stage469 future-equivalence theorem, equality of these repair words is exactly full labeled-future equivalence.

There are at most `(n+1)^18(m+1)` edge/match profiles, `O(n)` position choices and constant many alphabet/boundary choices, both for H and the suffix automaton. A conservative fixed-alphabet bound is `O(n^20)` memoized states and `O(n^20)` constant-branch integer additions/comparisons (n >= m). Each population and rank is at most `3^(m+n-2)`, hence has `O(m+n)` bits; the conservative bit cost is `O(n^21)` using linear-time addition of such integers, excluding input/output parsing and assuming explicit lengths. Ranking/unranking an already-computed support table requires `O(n)` child examinations and emits an `O(n)`-symbol word. This is a polynomial in the **explicit history lengths**, not a strongly polynomial claim in the binary bit-length of compressed numeric length inputs.

## Executed exact checks

`STAGE471B.py` exhaustively groups true full original observers and raw repair-word classes on eight small cases `(m,n,t)=(4,5,1),(4,5,2),(4,6,1),(4,6,2),(5,6,1),(5,6,2),(5,6,3),(6,7,4)`. It selects the 540 highest-multiplicity feasible fibers (deterministically), checks 2,212 class populations, and verifies each exact zero-based rank and inverse. The execution visited 1,836 aggregate prefix and 37,574 suffix states across those fiber runs. Maximum sampled class mass was 4. All assertions passed. A distinct nontrivial full fiber `m=6,n=7,t=4,K=3` with P edges `AA=3,AB=1,BA=1`, Q edges `AA=2,AB=1,AC=1,BA=1,CA=1` has 14 classes and 30 full histories, with class-mass histogram `{1:6,2:4,4:4}`; the algorithm reproduces these figures.

For the Stage470 full fiber `m=35,n=56,K=18` with P=A^35, and Q directed edges `AA=3,AB=BA=14,AC=CA=12`, set `t=8` (`h=48`). The exact deterministic computation gives
```
q_F = 4,618,757,880
|F| = 11,154,643,500
prefix states = 21
suffix memo states = 8,221
terminal profiles = 107
```
Five full-length lexicographic rank/unrank probes (ranks 0,1,2,100,1000) passed; their per-class masses are 4, and SHA256 hashes of the exact emitted keys are in the executed evidence. No large-fiber history or repair-key enumeration was used. Positive mass is independently conserved by the Stage470 combinatorial count of 11,154,643,500. The Stage469 future-equivalence theorem and its all-12-direction finite checks are inherited, rather than re-executed by this support-count run.

## Reuse, limitations and next unit

BRC resolution: **EXTEND_EXISTING_TOOL** — extends Stage470's positive integer edge-count transfer by a hidden-prefix compatibility table and a deterministic visible-word support automaton. No Boolean quotient erases source multiplicity: support is a separate projection from `M(v)`. The exact 19-counter initial observer remains intact. This establishes growing-window polynomial support/rank for `t<=m-2`; `t=m-1,m,m+1,...` introduce isolated hidden repair tags and need their own closure. The separate Stage471 request to increase P budgets to two POP/two APPEND remains open. These are the next constructive units, not impossibility claims.

Author-side proof, executed source and evidence are preserved in this directory; formal Source Result, current canonical Task CLAIM and independent Driver review were not established by the calculations.
