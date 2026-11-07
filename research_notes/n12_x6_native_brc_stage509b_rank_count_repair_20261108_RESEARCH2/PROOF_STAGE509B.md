# Stage509-B — Public-rank observer repair and minimal direct-target exposure

Date: 2026-11-08 (Asia/Shanghai)
Status: author-side exact counterexample, revised theorem with proof and finite exact verification; independent Driver review pending.

## Scientific identity and frozen input

Frozen Global Knowledge science: `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`.
Frozen Enterprise Math science: `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`.
P000 Git blob: `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`.
Predecessor Stage508: `6b169d6e858353bf253f1a28951ef6c3e8c71e44`.
Current *behavioral* snapshots verified independently: Global Knowledge `d23886ba43f09ba5bda6a7d239330642755d3550`, Enterprise Math `21f2de6927f4380141a512eac11191d097eda17e`.

The subject is a finite-word BRC joint-relation algebra, not a claim about native physical dynamics.

## Definitions and exact observer

An alphabet has the 12 signed native X6 directions `A={+E1,-E1,...,+E6,-E6}` with their six-dimensional signed integer unit-step vectors. A word is `w=((a_i,t_i))_(i=0,...,n-1)`, with `t_i∈{O,P}` denoting original/private or public source labels.

For any direction word define its complete joint-relation observer
`F(w)=(n,D(w),E(w))`,
where `D(w)=sum_i v(a_i)∈Z^6` and each of the 144 entries `E_(a,b)(w)` counts immediately consecutive pairs `a,b` in that exact direction order. No ordered relation coordinate is projected away.

The future grammar (any sequence of at most `h` legal operations) consists of `POP` (last token deletion), `DELETE2` (delete third from right), `INSERT2(c)` (insert a fresh `P` token immediately before the final two), `SET_END(r,c)` (update the direction but not source label at offset `r∈R` from the right), and `DELETE_KTH_PUBLIC(k)` (delete the `k∈S`-th public token counted from the right). Exact operation legality, output `F`, and source provenance are part of the declared observer/transition language. Here `R` is a finite subset of nonnegative integer end offsets, `S` is a finite subset of positive public ranks, and `h≥0`.

## Counterexample 509.1 — Stage508's gap-without-P-count abstraction fails

The preceding Stage508 Theorem 508.1 represented unexposed gaps by their `F` alone, tracking public labels only among explicitly retained original singleton tokens. Its proof used the false implication that whenever the `k`-th P is explicit, at least `k` P singletons must have been retained.

Fix `n=12,h=1,R={2,10,11},S={1,3}`, and distinct direction symbols `a_i=i` in the complete twelve-symbol native order. Compare:

- `x`: P at positions `{1,4,7}`; O elsewhere.
- `y`: P at positions `{1,7}`; O elsewhere.

The old Stage508 exposure set is exactly `{0,1,7,9,10,11}` for both. Every explicit direction and P/O tag is equal, and every nonempty hidden gap has the same `F` (the direction sequences are identical). Therefore **the two Stage508 compressed records are exactly identical**. However, the one-step operation `DELETE_KTH_PUBLIC(3)` is legal in `x` and illegal in `y` because `x` contains three P tokens and `y` only two. This is a strict one-step fiber-constancy counterexample against the old sufficiency statement. A raw-versus-Stage508-evaluator mismatch also occurs on `x` with `R={2,11}`, because it sees only two of the three P identities.

This requires a scoped correction to Stage508, not a silent rewrite of the immutable original.

## Theorem 509.2 — Corrected direct-target mask plus complete F and gap P counts

Using the *actual initial provenance tag skeleton*, enumerate the reachable legal identity-tag pre-action states of depths strictly less than `h`, considering all operations but not branching over different direction values. Track identities through deletion/insertion; inserted `P` tokens are always explicit and distinct from original identities.

Let `D_h(w)` be the set of original identity indices directly **deleted or direction-updated** by at least one legal operation from at least one such pre-action state: targets of POP, DELETE2, SET_END, DELETE_KTH_PUBLIC. Exclude purely adjacent INSERT2 neighbor identities from this definition.

Define `C_h(w)` as an ordered sequence of:
1. Full original direction and source tag `(a_i,t_i)` as a singleton for each original index in `D_h(w)`;
2. For every maximal remaining contiguous original run `g`, one indivisible summary
`G(g)=(F(directions(g)), #P(g))`, including the exact number of public-tagged tokens.

**Theorem.** For every `w,R,S,h` in the domain above, there exists an exact piecewise evaluator acting directly on `C_h(w)` that reproduces the legality and the complete `F` after each prefix of every legal future of length at most `h`. It never edits or splits an opaque `G` gap. Thus the fibers of `C_h` are future-safe for this fixed observer and grammar.

### Proof

The BRC relation summary `F` concatenates associatively. Displacement adds componentwise in `Z^6`; all 144 directed edge counts add, together with the unique junction edge between the last direction of the left nonempty piece and first direction of the right nonempty piece. The boundary directions are reconstructible from the declared `F`: for nonempty `w`, `D(w)−Σ_(a,b)E_(a,b)v(b)=v(first(w))`, and `D(w)−Σ_(a,b)E_(a,b)v(a)=v(last(w))`. The twelve signed unit vectors are distinct, so these differences uniquely identify the first and last directions. The implementation additionally caches both directions in its internal 5-tuple as a derived convenience, while the public observer remains `(n,D,E)`. P counts add under concatenation. Empty pieces contribute identity elements.

Induct on the length of a legal operation prefix. Every original token that POP, DELETE2, SET_END, or the ranked public deletion might target at this pre-action prefix is by definition in `D_h(w)`, hence is an explicit singleton in the representation. An inserted token is explicit by construction. So positional deletions and SET touch a singleton, never a gap; operation legality is decided from total current length.

For `DELETE_KTH_PUBLIC(k)`, traverse all pieces right to left and subtract their exact public counts. This determines total-rank legality correctly even if some nonselected P source identities reside in hidden gaps. If the rank-selected target were inside a gap, it would be a directly accessed original identity in an enumerated legal pre-action state, hence would lie in `D_h(w)`—contradiction. The chosen token is explicit and can be deleted exactly; opaque counts and 144-edge internal statistics are unchanged.

For `INSERT2(c)`: if the state length is two, inserting before the final two occurs at its initial piece boundary. If the length is at least three, its left neighboring token is the third-from-last token. At precisely the same reachable pre-action identity/tag state, `DELETE2` is a legal alternative: it directly targets that neighbor. If original, the neighbor is therefore in `D_h(w)`; if inserted earlier, it is already explicit. Hence `INSERT2` inserts immediately after an explicit singleton, at an existing piece boundary, without splitting an opaque gap. Exact P counts and F readouts are updated through monoid concatenation.

The induction covers every legal future prefix. The evaluator preserves all legality and readouts. QED.

**Implementation nuance.** The abstract reachability computation must use real P-tag identities/positions to determine which ranked operation is legal. Retaining only counts on future compressed gaps is safe after `D_h` has been correctly computed, not an invitation to remove tags before building that set.

**Representation-specific minimality.** Within encodings that require all directly modified original identities to be explicit singleton pieces and do not permit editing or splitting opaque pieces, `D_h` is the exact minimal mandatory original-singleton set. This is not a lower bound on every possible lossless encoding, or a claim of minimum total bits. Each opaque run stores one additional integer `#P`, using `O(log(n+1))` bits.

## Corollary 509.3 — INSERT2-neighbor retention is redundant

Stage508's exposure set retained both original tokens adjacent to the prospective insertion position. Under the exact grammar above (which includes DELETE2), those adjacent “boundary only” reservations are unnecessary: `DELETE2` already puts every non-initial insertion's left neighbor in `D_h(w)`, so insertion cannot split an opaque gap.

Witness: `w=OOO` length three, `h=1,R={2},S={1,2}`. Stage508 retained all three original indices `{0,1,2}`; `D_h` retains only `{0,2}`, and the singleton at zero is sufficient to define the INSERT2 boundary. This is a one-direction reduction in explicit original singletons, not a claim that total bytes shrink for every short word. For the earlier Stage508 n=19/h=3/R={2,11}/S={1,3} example, both masks have 12 singletons; the corrected representation adds the essential gap P metadata.

## Exact computational checks

The self-contained Python standard-library program `REPRO_STAGE509B.py` compares every raw tagged-word operation prefix against the count-enriched compressed evaluator and the complete 6D/144-edge output, including negative legality. Its independently implemented identity-skeleton state enumeration and brute-force small-domain check test the exact direct-target masks.

Actual execution (see `STAGE509B_EXECUTED.json`):
- 1,839 initial roots;
- 48,844 exact future-prefix raw/compressed state pairs;
- 59,280 transitions compared;
- 3,455 abstract prefix states;
- 18,671 abstract transitions;
- 1,815 small brute-force minimum-mask cross-checks;
- 778 roots where `D_h` retains fewer original singletons than the Stage508 mask;
- the explicit n=12 two-history counterexample, the single-history evaluator failure, and the n=19 predecessor case.

All assertions passed. Root coverage: exhaustive 6-symbol words (three signed X6 directions cross two source tags) through length 4 for h=1 and through length 3 for h=2; twenty deterministic 12-direction histories of lengths 9/12/19/28 at h=2 or h=3; targeted sparse-P and mask witnesses. This is finite implementation corroboration for a separately proved general theorem.

No non-BRC scientific computation, classical trigonometric expansion, or native physical attribution was introduced. This stage neither states nor benchmarks a polynomial-time exact synthesis of `D_h`; that synthesis is open.

## Research status and next problem

This is an **author-side amendment**: Stage508's exact no-count sufficiency assertion is false by a witnessed rank-legality collision. The revised quotient and insertion simplification have a proof under the specified operations; independent Driver assessment and native project admission remain pending.

Stage510-B: design and prove a non-exponential or parameterized exact transformer computing `D_h(w)` under adaptive rank-P deletion, mixed positional operations and insertion, without enumerating all future identity/tag skeletons. Also determine a tight horizon/rank-dependent saturation threshold for opaque-gap P counts (or show that exact full counts remain necessary in some family), preserving future legality. The independent fully active 12-direction/144-relation Euler–BRC heterogeneous-edge exact rank/unrank cost comparison remains open.
