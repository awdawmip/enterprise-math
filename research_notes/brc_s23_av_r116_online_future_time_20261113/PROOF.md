# R116: Online addition of unseen time buckets to a future-stable Top-k certificate

Date: 2026-11-13. Author-side Enterprise Math Research1 finite ranked Boolean auxiliary model.
Predecessor: R115-SIG at `70bdc1abf3ce2ffa8d9ba7501181bcfb53846d77` (research_notes/brc_s23_av_r115_signature_rank_20261113/PROOF.md). Retained frozen scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. R116 supplies new auxiliary mathematics; no modification of the frozen inputs.

## Model

Let `I` be a compact rational parameter interval. Let `U` be a finite potential universe of *complete* identities `u=(t,b)` with a strict total ranking. Each time `t` has a Boolean eligibility predicate `M_t(theta)`, shared across branches with that time. For histories `F,G ⊆ U`, `Top_k(F,theta)` is the descending tuple of eligible complete identities, truncated after `k≥1`. Complete branch identity, histories, multiplicity when relevant, and provenance are retained before any quotient. This is a precisely scoped auxiliary ranked Boolean observer; it is not native X6 Cell/Link/Port authorization or a signed BRC amplitude model.

For a finite potential time set `T`, define `sigma_T(theta)=(M_t(theta))_(t in T)`, `S_T={sigma_T(theta):theta in I}`, `d=|S_T|`. Disconnected sets of parameters may share an abstract signature; a connected atom partition has different semantics.

## R116.1 — Exact new-time fiber-refinement theorem

Introduce one previously unseen time `tau∉T`. For each attained old signature `s`, let
`D_s={theta in I:sigma_T(theta)=s}`;
`B_s={M_tau(theta):theta in D_s}`, a nonempty subset of `{0,1}`.

**Theorem:**
`S_(T∪{tau})={(s,b):s∈S_T, b∈B_s}` (coordinate inserted at canonical time position).
Writing `r=# {s:B_s={0,1}}`, one has **`d'=d+r`**, and therefore `d≤d'≤2d`.

**Proof.** Restrict a new signature to old coordinates. This yields an attained `s`, with the new bit necessarily in `B_s`. Conversely, for each `(s,b)` on the right, the definition of `B_s` supplies an actual parameter attaining that full signature. Every `B_s` has size one or two; summation gives `d'=d+r`. No connectedness or monotonicity of eligibility fibers is required. QED.

## R116.2 — Exact persistent root inheritance and conditional insertion

Initially fix `F,G⊆U` containing no identity at the new time `tau`. Let `R_s` be R115's immutable rank-keyed balanced-tree root for the eligible common (`F∩G`) and difference (`F△G`) identities under old signature `s`, with first-difference capacity `h_s` from R112.

**Theorem:** Every refined state `(s,b)` can point to the **same exact immutable `R_s`**, and its capacity equals `h_s`.

**Proof.** Every old identity retains exactly its old eligibility bit and the histories are unchanged. Thus the ranked eligible tuples and common/difference counts are identical for any parameter in either refined child, so the old root and capacity are reusable without recalculation. QED.

Now add one previously absent complete identity `u=(tau,beta)` to `F` only. In any new state `(s,0)`, `u` is ineligible, so its old root remains valid without edits. In every attained `(s,1)`, apply exactly one persistent rank-*key* insertion/leaf update to represent `u` as a difference leaf, retaining other leaves. Its rank position can be anywhere. All earlier historical roots remain valid. Using the exact R112 first-difference invariant, for every `k≥1` and parameter within this state:
`Top_k(F∪{u},theta)=Top_k(G,theta) iff (h_(s,b)=∞ or k≤h_(s,b))`.
A rational representative of a state with finite minimal `h` witnesses failure at `k=h+1`.

**Conditional structural cost.** Given already discovered attained signatures and a persistent balanced search tree keyed by complete identities with insertion and aggregate query costing `O(log(n+2))` node visits, write `n=|U|`, `d_1=# {(s,1) attained}`. New rank-tree allocation is `O(d_1 log(n+2))`; explicit rebuilding of an outer signature index costs `O(d')`, with at most `O(d_1 log(d'+1))` extra outer aggregate path updates. Old roots are shared by reference. These counts exclude the cost of finding `B_s`, generating/sorting cuts, exact rational bit operations, parameter lookup, representation of membership histories and witness recovery. A fixed positional array must be reindexed or replaced by a rank-key structure when new identities enter. The supplied Python checker validates invariants with sets; it does not implement or benchmark an AVL tree.

## R116.3 — Unbounded gap between explicit atoms and signatures

For integer `N≥1`, on `I=[0,1]` define
`M_N(theta)=1[{N theta+1/4}∈[0,1/2))`, where `{x}=x-floor(x)`.
There are exactly `2N` interior eligibility-changing rational cuts: `N` half-integer crossings and `N` integer crossings of the affine phase. Singleton endpoints/cuts plus open gaps produce `4N+3` exact raw atoms. With empty old `T`, old `d=1`, new `d'=2` for every `N`. Thus the explicit atom expansion requires `Ω(N)` cells even though the abstract signature index has just two states. Binary input length of `N` is `Θ(log N)`.

For `N=101`, the independent exact checker obtains **407 raw atoms, 2 attained signatures**. A symbolic eligibility predicate can answer *pointwise* rational queries without storing all cuts; an exact support/witness oracle for full-interval queries is a separate costed problem.

## Exact reproducibility

`check_r116.py` uses Python 3 standard library `Fraction` and a fixed seed, with eligibility `M_t(theta)=1[{t theta+1/4}∈[0,1/2))`. The local auxiliary test, distinct from full six-phase S23, covers negative and positive times, exact rational cut endpoints and gap midpoints, arbitrary history forks, old-capacity inheritance, one-sided addition, direct ranked tuple checks for all k, and exact finite-capacity difference witnesses. A four-identity universe is exhaustively checked over every ordered pair of history subsets and all exact atoms.

Output: `R116_PASS`; 6 fresh time buckets `[-3,1,7,-9,13,23]`; **15,912** random pair/atom direct checks; **15,912** unchanged-history inheritance checks; **7,632** zero-eligibility preserved-capacity checks; **8,280** exact difference witnesses; **9,984** exhaustive pair/atom checks; **41** split signature fibers. Max raw atoms in the incremental suite **199**, max signatures **42**. High-frequency `N=101`: **407** atoms versus **2** signatures. Full machine-readable data are in `verification_r116.json`. Script SHA256: `b36dedf52b98473a59f6e0fcb3dc4c6a08e4aeb86ff025f1804561b2d4157324`. Run `python3 check_r116.py`.

## Actual scope and forward question

This proves abstract finite-model identities and a constructive high-frequency family, with exact finite tests of the stated checker. The historical S23 frozen scientific inputs are unchanged, and the complete original S23 six-affine-phase predicate needs its own exact connection before using these test counts as an S23 benchmark. This is an author-side auxiliary result, not a canonical task CLAIM, independent review, native Cell/Link/Port theorem or Foundation promotion.

**R117 question:** Construct and compare an exact feasibility oracle for `D_s∩{M_tau=b}` that supplies rational witnesses without expanding every high-frequency phase cut, including nonconnected old fibers. Measure full bit operations, memory and witness recovery against eager atomization while preserving branch provenance and immutable historical roots.
