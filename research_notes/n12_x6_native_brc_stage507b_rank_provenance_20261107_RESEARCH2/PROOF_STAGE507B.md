# Stage507-B — Rank-aware X6/BRC provenance compression without hidden P-counts

Date 2026-11-07. AUTHOR_PROOF / EXACT_FINITE_EXECUTED / UNREVIEWED. Frozen science: Stage506-B `awdawmip/enterprise-math@3af4c24fbadb66c80a796fc19dcc7868c534c688`; account pin `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math pin `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current normative rules read separately. This is not a native Result or independent Driver review.

## Native carrier, declared observer and operations

Take the 12 signed primitive X6 directions `A={+E1,-E1,...,+E6,-E6}`, understood as increments in a chart relative to a selected native cell. A finite tagged history is `w=((a_i,t_i))`, with `t_i∈{O,P}` original/public. The full BRC direction observer is `F(w)=(n,D,E)`, where `D=Σv(a_i)∈Z6` and `E_ab=#{i:a_i=a,a_(i+1)=b}` for *all 144* directed pairs. Operation legality and the observer at every prefix of length ≤h are visible; full O/P tags are not directly visible except through the ranked-delete operation.

`F` is an associative exact concatenation monoid. For a nonempty word, `v(first)=D-Σ_ab E_ab v(b)` and `v(last)=D-Σ_ab E_ab v(a)`, so the first and last directions can be uniquely recovered because native signed-unit vectors are injective. In `F(u)⊙F(v)`, sum n and D and E and add the junction edge (last(u), first(v)) when both are nonempty.

Fix a horizon h≥1, a finite end-offset set `R⊂Z_>=0`, a nonempty finite public-rank set `S⊂Z_>=1`, `K=max(S)`. Permitted operations: POP (last token), DELETE2 (third from right), INSERT2(c) (new P before last two tokens), SET_END(r,c) for r∈R (change direction, *preserve* tag), and DELETE_KTH_PUBLIC(k) for k∈S (remove kth P from right). Each operation has its natural length/rank legality predicate. INSERT2 requires n≥2, DELETE2 requires n≥3.

## Theorem 507.1 — Complete finite-future compression with no hidden P counts

Define the initial end-offset halo
`B=([0,h+2] ∪ ⋃_(r∈R)[r-h,r+h]) ∩ [0,n-1]`.
Set `M=K+h-1`. Encode *explicit* direction+tag singletons for (a) every initial token whose end-offset lies in B, and (b) the rightmost min(M,total initial P) initial P tokens. Replace every maximal remaining contiguous run by its complete `F` summary. Keep pieces in order. **Do not store hidden P counts, locations or labels in the opaque gap summaries.** Denote the encoding `C_(h,R,S)(w)`.

**For all tagged X6 histories x,y of arbitrary finite length, equal C states imply identical legality and complete F observer after every prefix of every permitted operation string of length ≤h. Every such operation admits an exact compressed-state transition without splitting any opaque gap.**

Proof. For any surviving original token, each prior POP, DELETE2, INSERT2 or ranked P deletion changes its end-offset by at most one; SET changes no positions. Immediately before one of ≤h operations, the difference between current and initial offset is at most h−1. A POP, DELETE2, SET or INSERT2 target/neighbor is at offset 0,2,r∈R or 1/2 respectively. Hence every original token touched or neighboring an insertion boundary lies within B; newly inserted P tokens remain explicit by construction. These operations never split a hidden gap.

Now let p be any **unretained original P** token. At least M original P tokens initially lay to its right, all explicitly retained. In t≤h−1 prior operations, at most t of those M can be removed. SET preserves tags and new P insertions only add potential P tokens, never remove these survivors. Thus at least `M-t ≥ K` surviving *explicit* public tokens still lie to p's right immediately before any ranked deletion. As every permitted k≤K, p cannot be selected. Consequently every DELETE_KTH_PUBLIC target is an explicit singleton, and its legality is decided by the current explicit P count: if any hidden P exists there are already ≥K explicit P survivors on its right; if none exists, the explicit count is the total count. This proves that **not even per-gap public counts are needed** for the finite future.

Each legal operation therefore edits/removes/inserts an explicit singleton only, leaving each opaque summary intact. Adjacent pieces can be concatenated using the associative complete F product, which exactly recovers junction adjacency relations even after removals. Induction on the operation length proves exact legality and observer preservation at every prefix. QED.

With c retained original singletons,
`c≤min(n,(h+3)+(2h+1)|R|+(K+h-1))`.
At most c+1 opaque gaps, each storing n, six signed displacements and 144 directed edge counters, yield `O((c+1) log(n+h+1)+c)` bits for the fixed 12-letter alphabet. The initial representation can be built by one scan. This is a *sufficient* quotient under the stated operation language, not an unrestricted minimum encoding theorem.

## Theorem 507.2 — Sharp rightmost-P retention budget in this representation class

For every K,h≥1 with POP and DELETE_KTH_PUBLIC(K), the `M=K+h-1` rightmost-original-P budget is worst-case sharp for this class of “rightmost-P singleton list + opaque F gaps”, even if the gaps additionally record their P counts.

Take an arbitrarily long tagged direction word `(+E2,+E1,...,+E1)`. Ensure original positions 0 and 1 are outside B. Both histories mark the trailing M−1 `+E1` tokens public. In x only position 0 is additionally P; in y only position 1 is additionally P. They have identical direction words, F, retained rightmost M−1 public singletons, positional halo and hidden-gap P counts. But after `POP^(h-1)`, the trailing P group contains K−1 tokens; `DELETE_KTH_PUBLIC(K)` deletes `+E2` in x and `+E1` in y, producing different D and E on operation h. Budget M retains the otherwise hidden distinguishing P token. QED.

This proves sharpness **within the declared truncation scheme**, not a universal information-theoretic lower bound on every possible future-response algebra.

## Executed finite evidence and source

The archived `REPRO_STAGE507B.py` independently implements raw tagged histories, exact six-axis signed integer and 144 directed edge F readout, explicit singleton/opaque-gap concatenation, five operation types, rank deletion and all-prefix operation-tree assertions. Standard-library Python, no float or random seed. Actual run `STAGE507B_EXECUTED.json`:

- 32,714 initial roots; 558,135 prefix states; 623,309 tested operation transitions; all assertions PASS.
- Exhaustive for the 6-symbol tagged alphabet derived from the three native signed directions `+E1,-E1,+E2`: all lengths ≤5 at h=1, and ≤4 at h=2; S={1}, {1,2}, {1,3}, R={2} or {2,4}.
- 54 deterministic tagged 12-direction inputs, lengths 1..18, h=3, R={2,5}, the same three S choices.
- One nonidentical hidden-tag collision at h=3 for which the new C states coincide; 16 sharpness witnesses for all K,h in {1,2,3,4}, with the h-step POP/ranked-delete sequence.

Finite checks test exact implementation on those domains; the general result is supported by the two induction arguments above.

BRC reuse: **COMPOSE_APPLIED** to Stage506 exact F-piece algebra and initial position-exposure halo. Stage506's count-only provenance counterexample is repaired by retaining the bounded rightmost-P identities; the new proof also removes the earlier proposed per-gap P-count requirement.

## Next exact unresolved unit

Construct a smaller exact *joint position/public-rank reachability* automaton for a specific S,R,h, including dynamically inserted public tokens and legality of short histories. Seek one strict saved-singleton reduction with an exact proof or a minimum counterexample. Separately, the heterogeneous all-144-active-edge Euler–BRC rank/unrank bit-cost, wall-time and peak RSS experiment is still outstanding.
