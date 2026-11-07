# Stage513-B — Rank-one-assisted sharp provenance cap for source-sensitive X6-BRC gaps

Date: 2026-11-08. TASK_RESEARCH author-side proof; independent review pending. This is not a native Result.

## Inputs and observer

Frozen scientific inputs: GK bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Predecessor Stage512-B commit 4657873f539da8f64efa2ca4454f4eb70f2a51d6, whose exact structural-quotient D_h algorithm is used without changing science pins.

Each original history token carries one of twelve signed native X6 directions, an immutable original identity and a source tag P/O. The complete BRC observation F is history length, six signed displacement coordinates, all 144 directed native adjacency counters, first and last direction. The F concatenation law adds counters and the single last-to-first junction relation. Allowed actions are POP, DELETE2 (third from end), INSERT2(a) (new public source just before last two), SET_END(r,a) at r in fixed finite R, and DELETE_KTH_PUBLIC(k), k in nonempty finite S. Target legality is independent of direction values. The horizon is h operations. The exact D_h set contains original identities that could be directly SET or removed within the horizon. All originals in D_h and all new insertions remain explicit; maximal original runs outside it are opaque gaps g, each retaining F(g). Total exact P count is not a direct observer.

## Theorem 513.1 — improved source-rank cap

Suppose S contains 1 and K=max(S), where K>=1. For every h>=0 and finite R, preserving every opaque gap's capped source count

    c(g)=min(T,p(g)),    T=max(0,K-2)

together with the complete F(g) and D_h explicit tokens is sufficient to update the representation and exactly reproduce legality and the complete F observation at every step of every sequence of length at most h. Here p(g) is the actual public-token count in g. This strictly improves the universal Stage511 cap K-1 whenever K>=2.

**Proof.** Stage511's D_h-safe gap property guarantees that at any legal reachable pre-action state of depth t<h, no operation targets an original inside a hidden gap. INSERT2 does not split such a gap: when n>=3 its left neighbour is the DELETE2-targeted third-from-last, exposed if original; for n=2 the insertion is at the start. Hidden counts therefore stay constant unless adjacent gaps merge, where exact F joins and saturated source counts compose by min(T,p+q)=min(T,min(T,p)+min(T,q)).

For K=1 the known zero cap suffices. Suppose K>=2. Consider any hidden gap g with p(g)>T, equivalently p(g)>=K-1. Let m be the true number of public tokens strictly to its right at the reachable pre-action state. If m=0, the legal source deletion of rank 1 would delete the rightmost public original inside g: a contradiction. If 1<=m<K, the legal deletion of rank K has residual rank K-m in {1,...,K-1}, no more than p(g), and would delete a hidden original: again a contradiction. Consequently p(g)>T forces m>=K. Every allowed rank k<=K has already been satisfied strictly to the right; no ranked query visits g.

In particular, among gaps with p>T, the rightmost one has only exact-count (p<=T) gaps to its right. Its m>=K is therefore also correctly represented by the truncated counters. A rank query stops before this gap; the same argument progresses to all earlier truncated gaps. All gaps a query visits retain their exact counts, so legality and selected exposed target agree with the full word. POP, DELETE2 and SET_END act on D_h-exposed originals or new explicit tokens. After each action the associative BRC monoid returns exact F, and the same premise holds for the next reachable state. Induction on the action sequence proves the theorem. QED.

Per-gap count bit budget becomes ceil(log2(min(g_length,max(0,K-2))+1)); this is metadata only, not a reduction of the full X6 F or the preprocessing complexity of D_h.

## Theorem 513.2 — sharpness of uniform threshold

For every K>=3 there are two histories at h=1, S={1,K}, with the same D_1 explicit-mask and identical F on every opaque gap, whose uniform cap K-3 encodings coincide although rank-K deletion has different six-dimensional displacement. Thus K-2 is the smallest sufficient nonnegative **uniform** cap for this declared D_h-safe-gap codec. For K=1 or K=2, zero is already minimal.

**Construction and proof.** Let g=max(4,K), n=2+g+5. Both direction histories consist of prefix (+E1,+E2), followed by g repeats of +E3, followed by five tail directions (which may use the remaining native axes). Both prefix sources are public. The middle +E3 run has K-3 public tags in history a and K-2 in history b; all remaining middle tags are private. The final tail direction is public; the other four tails are private. Choose R={n-1,n-2}, h=1, S={1,K}. Both prefix originals are explicit under SET_END. The trailing public token is explicit under POP/rank1. DELETE2 targets a tail token. Rank K removes the first prefix public direction in a and the second prefix public direction in b; no middle original is targeted. Hence both D_1 masks agree and omit all middle originals, all opaque F are equal, and cap K-3 maps the two middle public populations to the same value. But removing +E1 rather than +E2 changes the six-displacement and directed adjacency observation. Therefore cap K-3 loses a future observable distinction. QED.

Concrete K=3, n=11: cap0 conflates the middle counts 0 and1, but rank3 yields exact displacement (1,2,4,1,1,1) versus (2,1,4,1,1,1) in the executable test.

## Reproducible finite execution

File REPRO_STAGE513B.py uses Python standard library exact integers and the complete 12-direction/144-edge BRC F. It builds structural-quotient D_h and an explicit-token/opaque-gap state with saturated counts; a separate full-word transition is applied at every tested action and compared to the compressed state and F. Tests: all O/P patterns for n=2..6, h=1,2, K=2,3,4, plus deterministic n=7,9,12, h=3, K=2,3,4; 852 roots, 20,879 pre-action states, 241,742 transitions, 4,220 preprocessing-state scans. All assertions pass. Five strict lower-cap counterexamples for K=3..7 also pass. Raw evidence in STAGE513B_EXECUTED.json. Finite tests verify the stated implementation/input scope; the general theorem and sharpness rest on their separate arguments.

This result covers a bounded horizon, the exact stated operation language and D_h computed from original source positions. It does not claim minimum memory for arbitrary codes, unbounded edit equivalence, a platform-authenticated CLAIM, independent Driver review, or Foundation promotion. GitHub authenticated user awdawmip has admin permission; Enterprise Math native status and task list both returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE with operation_sent=false, so active native Owner is unconfirmed.

## Next: Stage514-B

Compute per-gap reachable residual-rank profiles for general S, h and R and seek stronger scoped cap or a counterexample, ideally without enumerating every Stage512 skeleton. Verify identical full-F observer futures and account for preprocessing. Retain the independent all-12-direction, all-144-active-relation heterogeneous Euler-BRC exact rank/unrank cost comparison as unfinished.