# Stage506-B — Exact exposure automaton for finite-horizon X6/BRC dynamic histories

Date: 2026-11-07. Classification: AUTHOR_PROOF / EXACT_FINITE_EXECUTED / UNREVIEWED.
Scientific parent: Stage505-B `awdawmip/enterprise-math@6bbb98d048bf885f2cb504955d2e48578c2874d8`, `PROOF_STAGE505B.md`.
Frozen science pins **unchanged** from parent: account `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral context separately read: GLOBAL_KNOWLEDGE main `f18362eb80e8623f16be0afddf480e044269b9b6`, Enterprise Math main `10635cfb1086d1c59ba7ca61a03a6f87c6744a5e`. P000 and observer-preservation contracts were applied; no changes proposed to protected world assumptions.

## Precise observer and operation language

Let A = {+E1,-E1,...,+E6,-E6}, with chart displacement v:A -> Z^6 taking the signed unit component. This chart is relative to a chosen cell; it is not a global origin. Let w be a finite direction word and
`F(w) = (|w|, D(w), E(w))`, `D=Σv(w_i)`, `E_ab=#{i: w_i=a, w_(i+1)=b}`.
E is the full 12×12 directed edge-count table. The first/last symbols of nonempty w are recovered exactly from D and E:
`v(first)=D-Σ_(a,b) E_ab v(b)`, `v(last)=D-Σ_(a,b) E_ab v(a)`.
Thus associative `F(u)⊙F(v)=F(uv)` uses component sums plus the directed boundary edge (last(u), first(v)). F(empty) is the identity. The executable stores the *derived* endpoints for convenient calculation.

Fix an initial length n, finite horizon h>=0, and finite end-offset set R ⊂ Z_>=0. At each step choose one of the following legal operations, with direction c∈A:
* POP: delete end-offset 0, legal for length >=1.
* DELETE2: delete end-offset 2 (third token from right), legal for length >=3.
* INSERT2(c): insert immediately before the last two tokens, legal for length >=2.
* SET_END(r,c), r∈R: replace token at end-offset r, legal for length > r.

The observer F and operation legality are visible at every prefix of every common legal sequence of at most h steps. Source labels are not queried by these operations. The proof tracks original-token identity only to construct a sufficient compressed state; newly inserted tokens remain explicit.

## Theorem 506.1 — Exact directly exposed original-token set

An original token starts at end-offset ρ=n−1−i. Define its position state (L,q), where L is the current word length and q the current end-offset, **while that original token survives**. Each operation has the following exact transitions:

| operation | legal length | original-token transition |
|---|---|---|
| POP | L>=1 | q=0: token erased; q>0: (L−1,q−1) |
| DELETE2 | L>=3 | q=2: token erased; q>2: (L−1,q−1); q<2: (L−1,q) |
| INSERT2(c) | L>=2 | q>=2: (L+1,q+1); q<2: (L+1,q) |
| SET_END(r,c) | L>r | (L,q) |

Call an original token **exposed** if, immediately before one operation within a legal length-≤h trace, it is at POP target q=0; DELETE2 target q=2; SET_END target q=r∈R; or INSERT2 adjacency q∈{1,2}. Let `X_(n,h,R)` be the set of its *initial* end-offsets.

**Theorem.** For every finite n,h,R, the forward DP over (L,q) and operation types in `REPRO_STAGE506B.py:exact_mask` returns exactly `X_(n,h,R)`. To compute it, it suffices to test the finite candidate set

`B = ([0,h+2] ∪ ⋃_(r∈R)[r−h,r+h]) ∩ [0,n−1]`.

The algorithm never enumerates direction words, and its candidate count is O(h(|R|+1)). For each candidate, it enumerates only the reachable (length,offset) states through h−1 earlier operations, filtering by each operation's current-length legality.

**Proof.** For a surviving original token each prior operation changes its end-offset by at most one in absolute value; hence an exposure at q=0,1,2, or r by step h implies the initial offset lies within h of that target. Therefore every exposed original belongs to B. The displayed transition table is obtained directly from the index effects of the four operations; direction choices never affect length, index, or legality. For each initial ρ, induction on the number j of preceding operations proves the DP contains precisely the position/length pairs reachable with that original token alive after j legal operations. The subsequent test at an eligible transition marks ρ precisely when its current q is a declared target or insertion neighbor. This proves soundness and completeness of X, including short-word legality and sequences that contain inserted tokens. QED.

## Theorem 506.2 — Observer-complete compressed execution with DELETE2

Retain, in their initial order, the direction and any source label of exactly those original tokens whose initial end-offset belongs to X; replace every maximal contiguous intervening run of original tokens by its complete F summary and its length. Call this ordered piece state `K_X(w)`. A new INSERT2 token is always retained explicitly.

**Theorem.** If two initial tagged direction words x,y of equal length satisfy `K_X(x)=K_X(y)`, then every sequence of at most h operations from the declared language has identical legality and identical observed F at every prefix. Moreover there is an exact, executable update on compressed pieces without inspecting the interior of any summary gap.

**Proof.** By Theorem 506.1, each original token subsequently targeted by POP, DELETE2 or SET is explicitly retained at time zero. The pair of original neighbors surrounding an INSERT2 boundary, when present, are also retained at time zero. Inserted tokens remain explicit by construction. Thus every permitted operation edits, removes or inserts a singleton token, at a boundary between complete pieces, without splitting an opaque gap. Each unchanged gap retains its original F; the associative exact BRC product yields the current F from all pieces, including boundaries of gaps and freshly modified tokens. Legality depends only on total length and the selected offset, which the pieces retain. Induction on the common operation history proves both words have equal updated piece states and F at every prefix. QED.

The construction is a scoped **sufficient** quotient for these observers and operations; X is exact for the above *direct-exposure criterion*, not asserted to be an information-theoretically minimum encoding under every possible representation.

## Size and strictly smaller adaptive certificate

Let c=|X|. The representation uses c singleton directions and at most c+1 full F summaries, each with 1 length + 6 signed displacement +144 edge counters and derived endpoint symbols. Fixed alphabet bit cost: `O((c+1)log(n+h+1)+c)`; finite-horizon construction of the original summaries requires a scan of n tokens. Exact exposure enumeration uses the candidate B and a finite set of (L,q) states; its cost depends on h and |R| and integer lengths, rather than an n-wide direction enumeration.

For n=1,000,000, h=4, R={2,100000}, the safe broad halo B contains **16** original tokens. The exact DP returns exactly these **13** initial offsets:
`[0,1,2,3,4,5,99997,99998,99999,100000,100001,100002,100003]`.
This is a symbolic index/legality computation for a million-token word, **not** a million-token execution/throughput benchmark. A further safe compression collision: x=`AABA A^15`, y=`ABAA A^15` (length 19) have distinct original directions but identical F summaries in the hidden prefix, identical retained singleton tokens, and equal `K_X` for h=3, R={2,5}. Hence their observed future trees through depth 3 agree exactly.

## Independent finite computational check

`REPRO_STAGE506B.py` is pure Python 3 standard library, exact signed six-component integer arithmetic and all 144 ordered edge counts. It implements (i) exact_mask DP, (ii) independent raw-word edit and F recalculation, (iii) piece-state edits with illegal access assertions, (iv) all-prefix operation-tree comparisons.

Executed `STAGE506B_EXECUTED.json` reports:
- 364 raw histories over three directions, lengths 0..5, complete depth-2 operation trees with R={2,4}, all three insertion/replacement directions;
- 65 deterministic-seeded histories over all 12 native directions, lengths 0..34, complete depth-3 trees with R={2,5}, two operation directions;
- two nonidentical 19-token histories that collide under the compressed state, checked through depth 3;
- total **431** test roots, **73,765** visited nodes and **78,364** tested transitions (including illegal-transition checks); all assertions PASS.

Proof strength: Theorem 506.1 follows by a complete position-state induction, Theorem 506.2 follows by a piece-preservation induction. Finite checks independently test implementation behavior on exactly the declared domains. No native CLAIM/Result/Driver mathematical acceptance is claimed.

## Stage507-B live next question

Extend the automaton to *rank-based provenance deletion*, where DELETE_LAST_PUBLIC or DELETE_KTH_PUBLIC changes the target based on hidden public-label counts, while retaining a compact exact guard on original reachable public ranks. Compare a signed-interval/label-count DP with the position-only X certificate and seek the smallest concrete counterexample to removing labels from an opaque gap. Separately complete the pending 144-active-edge heterogeneous Euler–BRC rank/unrank same-inventory bit-cost/time/RSS benchmark.

Current operational observation: GitHub authenticated as awdawmip with repository write permission. Native Enterprise Math `em_status` and `em_control_tasks` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, subreason `UPSTREAM_STATUS_TOOL_ERROR`, `STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`; active canonical Owner, CLAIM and Result could not be verified. Research is author-side evidence, not independent Driver review.
