# Stage510-B — K-saturated provenance count for exact finite-future X6 BRC observation

**Date:** 2026-11-08 Asia/Shanghai. **Research status:** author-side proved lemma and exact computational evidence, independent review pending.

**Scientific freeze:** GK `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Parent Stage509-B is commit `94f52374ed15a2a8cb41a7bf8b5aca163e8c1370`, `PROOF_STAGE509B.md` and `NEXT_STAGE510B.md` under `research_notes/n12_x6_native_brc_stage509b_rank_count_repair_20261108_RESEARCH2/`. Current *behavioral* reads were separate: GK main `385416a332a82b012c2b564d4af7cc13ea2434c0`, EM main `c337181b4963c27aa8c5225d5b8e8858eae5fb8b`.

## Domain, observer, operation language

Let `A={+E1,-E1,...,+E6,-E6}` be 12 signed unit directions, with source tag `t∈{O,P}`. A history is a finite tagged word `w=((a_i,t_i))`. Its declared BRC joint-relation observation is `F(w)=(n,D∈Z^6,E∈N^144)`, where `D=Σ_i v(a_i)` and `E_(a,b)` counts adjacent **ordered** direction pairs. All 144 coordinates remain present.

Fix future horizon `h≥0`, finite end-offset SET set `R⊆N_0`, and nonempty allowed public-rank delete set `S⊆N_+` with `K=max(S)≥1`. Permitted operations are POP, DELETE2 (delete third-from-right), INSERT2(c) (insert fresh P-tagged direction before final two), SET_END(r,c), and DELETE_KTH_PUBLIC(k) for k∈S. The observer demands each operation's legality and full F after each future prefix of length ≤h. It **does not expose an exact total P-count query**.

Compute Stage509's exact `D_h(w)` from the **full initial identity/P-tag skeleton**: every original token that *can* be directly deleted or SET at a pre-action state reachable in <h legal operations is in D_h. Keep each such original token explicitly. Keep every maximal remaining consecutive interval g in an opaque BRC gap, with F(g) and public tag count p(g). Inserted tokens are explicit. The exact preprocessing of D_h remains an open algorithmic target.

## Lemma 510.1 — Saturated rank routing

For K≥1 let `c_K(p)=min(K,p)`. Given any ordered piece counts p_1,...,p_m∈N, every ranked query k≤K has the same legality, selected piece, and residual rank *within that piece*, whether the rank router reads exact p_i or c_K(p_i).

**Proof.** Read pieces right-to-left with residual r initially k≤K. At piece i, if p_i<r then p_i<K so c_K(p_i)=p_i; both routers subtract the same amount. Otherwise p_i≥r: either p_i<K and the values agree, or p_i≥K≥r and the capped count is K≥r. Both routers select the same piece at the same residual. Thus failure to find a target also agrees. QED.

The cap map is a homomorphism `c_K(a+b)=min(K,c_K(a)+c_K(b))` into saturated addition. **Do not subtract from a capped aggregate.** Retain per-piece metadata: no opaque gap is ever edited, and explicit P singletons are updated individually.

## Theorem 510.2 — Replace exact hidden P count by min(K,p)

For every original w, h, R and S above, compute the *true* exact D_h(w), then represent each untouched original interval g by `G_K(g)=(F(g),min(K,#P(g)))` rather than `G(g)=(F(g),#P(g))`. Keep the explicit original direction/tag tokens in D_h(w). This state admits an exact piecewise evaluator of legality and full F after **every** legal future of length ≤h without splitting an opaque gap.

**Proof.** Full F composes associatively. For nonempty x,y, n and D add; E adds with the directed junction edge from last(x) to first(y). Those endpoints are themselves reconstructible from F:
`v(first(x)) = D(x)-Σ_(a,b) E_(a,b)(x)v(b)`,
`v(last(x)) = D(x)-Σ_(a,b) E_(a,b)(x)v(a)`.
Each of the twelve unit vectors is distinct. Empty interval has the monoid identity.

Induct over actual operation-prefix depth t≤h. Direct original targets of POP, DELETE2, SET_END and ranked P deletion belong by definition to D_h(w) in every reachable pre-action state of depth t<h, so they are explicit singletons; inserted tokens are explicit by construction. Legality of positional operations is decided by exact piece lengths. Any noninitial INSERT2 boundary has the third-from-right token to its left: at that same pre-action state, the alternative DELETE2 can target that token, proving that left boundary is explicit; at length two the insertion occurs at the beginning. Insertion never splits an opaque interval.

For a ranked P deletion with k∈S, Lemma 510.1 gives exactly the same legal/illegal decision, target piece and residual within that piece as the exact-count evaluator. If selected P belonged to an opaque interval, it would have been a direct-target original identity in D_h(w), contradiction. The selected P is explicit and can be deleted. Untouched intervals retain F and their saturated counts; singleton tags and ordered F junctions update exactly. The induction completes the claim. QED.

**Bit corollary.** For an opaque interval of length g, full P count needs at most `ceil(log2(g+1))` bits, while the saturated count needs `ceil(log2(min(K,g)+1))` bits. This is a precise metadata reduction, not a claim about total memory on all histories. The six integer coordinates and all 144 directed edges are untouched.

## Proposition 510.3 — K is sharp for *generic piece rank routing*

If a universal per-piece cap `min(T,p)` must preserve all k=1,...,K ranked piece lookups for unrestricted lists of nonnegative piece counts, then T≥K. For T<K take two pieces, left count 1 and right count T vs T+1. These have equal capped right-count T. Rank k=T+1 chooses the left piece in the first and the right in the second. Lemma 510.1 proves sufficiency of T=K. This lower bound is for generic routing, not automatically for the narrower D_h-safe-gap class.

## Exact checks

Executed locally using `REPRO_STAGE510B.py` in the accompanying restored evidence bundle (see `STAGE510B_EXECUTED.json` for the actual counters): 9,331 count vectors, 195,951 rank queries, 335,916 saturated-monoid checks, 1,593 history roots, 54,436 raw/compressed future nodes, and 56,283 transitions. All assertions passed; exact integers and 144 directed relation coordinates are used. Roots include exhaustive tagged six-symbol words to length four, deterministic 12-direction histories, and a length-80 witness with h=2, R={2,3}, S={1,3}, five exposed originals and one opaque interval of length 75. Histories with hidden P counts 50 and 40 produce the *same* cap-3 state yet remain future-equivalent in tested depth. General statements above are supported by proofs, not extrapolated from these finite tests.

**Next:** compute D_h without complete identity/tag future-skeleton enumeration, and test whether D_h-safe gaps admit a smaller cap than generic rank routing. The 12-direction/all-144-active heterogeneous Euler–BRC exact rank/unrank cost comparison is a separate open unit. This is author research, not an authenticated Result, Driver Review or Foundation promotion.
