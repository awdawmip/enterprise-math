# R5 — Eleven states are necessary and sufficient without transition coherence

Date: 2026-11-16. Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551. Continuation of research_notes/portable_direct/r5_two_control_coherent_cube_20261116/R5_TWO_CONTROL_CUBE_COVER_THEOREM.md at scientific commit edcceb086854d269acf0f7e288da54ddb7393d25. Research class: author-side auxiliary, exact integer/source-labelled repair model; review NOT_REVIEWED. Not a P000/X6-native state-collapse claim, nor a formal Task/CLAIM/Result/Review.

## Exact question and result

Let k=6, raw snapshot u in {0,...,63}, and q(u)=sum over i mod 6 of u_i*u_(i+1), with bits read in cyclic order. An output is a canonical genuine-source library L(r), centre r in {0,...,63}. It serves raw u within slack s=2 precisely when

    G(r,u) := ((u & ~r)==0) AND (0 <= q(r)-q(u) <= 2).

Only named raw actions Set_0(0/1), Set_1(0/1) are allowed; they replace the specified bit and leave all other bits fixed. A deterministic Moore controller has a finite set Q, an arbitrary total transition f_l:Q->Q for each of these four operations, an output r(q) at each internal state, and a total initialization choosing at least one internal state for every raw snapshot. Output correctness is required after every finite operation word. No internal idempotence, commutation, or reset absorption is assumed.

**Theorem.** Assuming the inherited genuine-source canonicalization lemma (a typed library serving a set of obligations can be replaced by an equal-or-better canonical L(r)), the unrestricted optimum is

    N_dyn(k=6, J={0,1}, s=2) = 11.

Thus arbitrary internally noncommuting updates do not improve upon the explicit eleven-state coherent construction in this instance.

## General lower-bound method

For any finite raw state set X, source-feasibility sets G_r, actions U_l:X->X and a proposed m-state Moore controller, static correctness implies that the m output labels cover X by their G_r sets. Enumerate all size-m output-centre covers after replacing a dominated centre with a nondominated one. A centre is dominated if its entire G_r is contained in another G_r'; replacement preserves every output obligation under every future action.

For a fixed output-centre tuple (r_0,...,r_(m-1)), define forced raw snapshots F_j initially as those u for which G_(r_j) is the **only** selected output covering u. Every correct initialization must place u in state j. For each operation l, any target of f_l(j) must cover every U_l(u) for u in F_j. Intersecting these necessary candidate target sets may yield (a) no target, ruling out the tuple; or (b) a unique target, which forces all updated snapshots into the target's F set. Iterating these implications is sound and terminates in finitely many additions. When targets remain nonunique, enumerate every target choice; this includes *all* deterministic transition tables compatible with the forced implications.

For each concrete transition table f, calculate the greatest output-correct forward-stable relation by the descending exact-bitset iteration

    B_j^(0)   = G_(r_j),
    B_j^(h+1) = B_j^(h) ∩ INTERSECT_l U_l^(-1)(B_(f_l(j))^(h)).

Any set of raw snapshots genuinely associated with controller state j in a correct execution is a postfixed relation and therefore lies in every B_j^(h). Accordingly, a necessary condition for total initialization is UNION_j B_j^(infinity) = X. The descending sequence stabilizes in at most m*|X| strict element removals. This is a complete finite negative certificate for each enumerated centre tuple and transition table, with no assumption about coherence or action order.

## Exact exhaustive certificate for k=6

The verifier computes all 64 genuine-source G_r as 64-bit integers. They are distinct; exactly 22 are nondominated. Exact set-cover search finds minimum static centre count **10** and **116** distinct ten-centre covers among those 22. Since any ten-state controller must use ten distinct effective source labels (otherwise fewer than ten centres would statically cover all raw snapshots), its output tuple reduces to one of those 116 cases.

Unique-initialization propagation rejects 111 cases by an impossible deterministic transition. Exactly five cases survive this necessary propagation. Their undetermined transition edges each have two allowed targets; their full exhaustive counts are **4, 4, 128, 128, 64**, totaling **328** complete transition tables. The stable-relation fixed point gives maximum initialized-raw coverage respectively **52, 52, 44, 44, 36** out of 64. Thus no ten-state arbitrary deterministic controller can initialize all snapshots while preserving correctness for every finite action sequence.

The published eleven-state witness from the preceding coherent-cover theorem is independently rechecked by the verifier: its seven disjoint components have state counts (4,1,1,2,1,1,1) and cover all 16 fixed tails for all four control-bit assignments. Its explicit correct commuting/reset-absorbing transitions are a subset of the unrestricted allowable controllers, establishing the matching upper bound.

## Reproduction and evidence

Run VERIFY_R5_K6_UNRESTRICTED_NO_TEN.py using Python standard library. It rebuilds the source masks, enumerates all static ten-centre covers, performs exact forced-transition closure, enumerates all remaining tables, computes their greatest stable belief relations, and checks the eleven-state witness. Its JSON stdout is retained as EXACT_R5_K6_UNRESTRICTED_NO_TEN_EVIDENCE.json. Expected status: PASS_R5_K6_UNRESTRICTED_TEN_STATE_NO_GO. In a separate independent local crosscheck, direct enumeration of all binomial(22,10)=646646 nondominated ten-centre tuples reproduces the count 116; no separate program is claimed for that crosscheck.

Status: AUTHOR_PROVED / EXACT_FINITE_EXHAUSTIVE / NOT_REVIEWED. Exact raw domain size 64, four operations and frozen science pin given above. This settles the auxiliary genuine-source canonical ring conditional on its inherited typed-library canonicalization theorem. The result does not require a general multi-coordinate collapse theorem.

Next: extract a minimal raw-snapshot and transition-implication obstruction, then test whether internally noncommuting updates ever strictly reduce state count in other k, J, or slack regimes. The general two-coordinate collapse theorem remains open.
