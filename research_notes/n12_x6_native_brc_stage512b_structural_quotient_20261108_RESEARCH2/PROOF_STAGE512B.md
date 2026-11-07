# Stage512-B — exact D_h structural-quotient transducer

Date: 2026-11-08 (Asia/Shanghai). Role: TASK_RESEARCH author-side continuation; mathematical review pending.

## Source scope and mother objective

**Frozen scientific inputs remain unchanged:** GK commit `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM commit `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, Source P000 V5 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Direct predecessor Stage511-B at `191cac081c8714098dafbc94fcaf56bc067d5c20`, preceded by Stage509-B `94f52374ed15a2a8cb41a7bf8b5aca163e8c1370`. The Stage511 theorem retains complete BRC F and opaque-gap provenance cap max(0,K−1).

Current **behavioral** normative snapshot was separately read: GK main `cc87ea534d8a14e1a74caaf1733d8628c5e9b865`, EM main `698f6bf033747ea7b2af46babb274b7a9f2689ac`; these are not new scientific pins. Native model: P000 six signed integer axis coordinates, signed twelve-axis direction alphabet and complete directed 12×12 adjacency observer, with separately typed history order. No traditional propagator or trigonometric arithmetic is used.

**Mother objective:** determine a finite-future lossless, source-sensitive BRC representation with efficient preprocessing. The current bounded subproblem is exactly computing the set D_h of original token identities which can be directly modified or removed by a legal action at some future operation step ≤h. The result here strengthens the Stage509/511 D_h *algorithm*, without changing its definition or the previously proved safe-gap compression theorem.

## 1. Objects and operations

Input: original identity-tag word `w=((a_i,p_i,i))_{i=0}^{n-1}`; `a_i∈{±E1,…,±E6}`, public source flag `p_i∈{O,P}`. Every INSERT2 adds a new P token. Legal operations:

* POP last; DELETE2 third from last; INSERT2(a) immediately before last two, for n≥2.
* SET_END(r,a), r in finite nonnegative set R, preserves source flag and identity.
* DELETE_KTH_PUBLIC(k), k in finite positive set S, removes k-th public token counting from the right.

Each SET or INSERT direction a is any signed native direction, but no operation tests a direction value to choose its target or decide its legality. An original identity is **directly touched** if an operation SETs or removes it, not merely if it appears at an insertion boundary. Let D_h be the union of these identities over legal prefixes of length <h and their next legal target action.

The complete BRC segment observation is
\[
F(w)=(|w|,D(w)\in\mathbb Z^6,E(w)\in\mathbb N^{12\times12},\mathrm{first}(w),\mathrm{last}(w)).
\]
For nonempty u,v, compose by adding length, displacement, all 144 directed edge counts, and one junction edge `last(u)→first(v)`. This is the predecessor F monoid used here for independently recomposed checks. The first/last fields are derivable from the exact signed-axis displacement and edge counts.

## 2. New structural quotient

Replace each surviving original token by its fixed distinct nonnegative original identity i; every inserted public token by a single sentinel `*` (in code `-1`). The original public flags are stored in an immutable tag lookup `p_i`; `*` has flag P. The quotient forgets all direction choices, SET value changes, and distinct insertion IDs; it still retains **order, multiplicity and original identity**.

Starting at `q_0=(0,1,…,n−1)`, breadth-first search the distinct quotient states using only structural state-changing moves POP, DELETE2, INSERT2(*) and DELETE_KTH_PUBLIC(k). SET has no state transition; at each reachable quotient pre-action state, simply mark the legal SET_END(r) original targets. Also mark original targets of each legal removal. Keep for every quotient state its **shortest** structural depth. Stop expanding at depth h−1; successors at depth h need not be scanned.

**Theorem 512.1 (exact quotient exposure).** For every input, every horizon h≥0 and finite R,S as above, the union of marked originals computed by this shortest-path structural quotient is **exactly** Stage509–511's D_h from the full identity/tag future operational tree with SET and all twelve direction choices.

**Proof.** Project a full intermediate word to the ordered original identities and inserted sentinels. All non-SET structural transitions commute with projection: legalities, end offsets and reverse-public ranks depend only on this projected ordered tag structure. All 12 INSERT directions project to the same fresh public sentinel. All SET actions project to an identity transition and preserve public flags, word length and original identities; thus deleting every SET from a legal full prefix gives a legal structural prefix with the *same* projected state, at no greater depth. The next action has the same position and provenance target, so any originally touched identity is marked by the quotient algorithm at a reachable depth <h.

Conversely, lift every structural path of length s<h to a legal full path by choosing any native direction on INSERT2. Its state projection is the prescribed quotient state. A marked original is then targeted by its corresponding legal operation (POP, DELETE2, SET_END or public-ranked deletion), and is thus in full D_h. Replacing identical inserted IDs by sentinels is safe for this claim because no operation reads their private IDs; distinct copies persist as separate positions and retain public multiplicity. For a quotient state reachable at several depths, the earliest arrival dominates all later arrivals: it preserves at least as many remaining operations, so processing that state once at the smallest depth is complete. Thus the sets agree. QED.

**Algorithmic bound.** Let U be the number of distinct quotient states scanned, and m=n+h the maximum word length. With hashable O(m)-size states and an O(m) reverse-public scan, the direct implementation takes O(U((|S|+1)m+|R|)) time plus hashing overhead and O(U m+n) memory. It still has potentially exponential U in h, but removes direction branching, SET stutters and redundant insert-ID distinctions and reaches the exact answer without enumerating complete edit trees.

**Corollary 512.2.** Apply the exact quotient D_h as the Stage511 explicit mask; retain the pre-established complete F for every hidden interval and per-gap provenance count capped at max(0,max(S)−1). The Stage511 theorem yields the identical finite-future legality and full observation guarantee. The observer has all 144 directed X6 relations throughout.

## 3. Exact executed evidence

Executable source: `REPRO_STAGE512B_COMPACT.py`. Raw output: `STAGE512B_COMPACT_EXECUTED.json` (both present in this directory). Python standard library, exact integers and discrete tags. Direct comparison against a faithful, readable Stage509-style identity/tag layered reference across 390 input/parameter families: **390 identical D_h masks**. All 394 recompositions of the full six signed coordinate displacement and 144 directed adjacency counters matched their full words; all assertions PASS.

The input families cover every O/P tag sequence for n=2,…,6, additional n=7/8 deterministic tag patterns, h∈{1,2,3}, R selected from {0,2,n−1}, S={1,2} or {1,3}. Source signatures and SET/INSERT directions are erased **only for D_h reachability**; complete F is tested using twelve native signed directions.

Measured five in-process repetitions of each variant using tracemalloc; resulting median milliseconds and maximal traced Python heap peak within repetitions:

| Case, exact tags and parameters in source | Legacy states | Quotient states | Legacy median ms | Quotient median ms | Legacy/quotient peak bytes |
|---|---:|---:|---:|---:|---:|
| n=19,h=3,R={2,11},S={1,3} | 26 | 19 | 0.3637 | 0.1433 | 20152 / 9104 |
| n=28,h=2,R={2,12},S={1,2} | 6 | 5 | 0.1061 | 0.0758 | 7864 / 8616 |
| n=28,h=5,R={2,12},S={1,3} | 263 | 119 | 4.8354 | 1.7789 | 213840 / 116256 |
| n=100,h=5,R={2,61},S={1,3} | 516 | 253 | 13.2346 | 5.3120 | 1222048 / 674176 |

The n=19 reproduction uses original P positions {0,3,6,12,15,18} and returns the independently previously published Stage508 mask `{3,5,6,7,8,9,12,14,15,16,17,18}` (12 originals). The n=28 input uses P={0,20,24,26,27}, mask `{14,15,16,24,25,26,27}` (7 originals). The two larger cases use explicit tags and R,S specified in executable source. Timings depend on the interpreter, heap tracer, execution order and representation. This comparison combines quotienting with a more compact integer/sentinel state encoding; the state-count reduction is the structural result. Stage511's full future losslessness remains supported by its own proof; this program directly checks exposure equality and initial complete-F recomposition.

A second, unarchived local exploratory checker also compared against literal full twelve-direction action trees at n=6,h=2; n=19,h=3; n=28,h=2, and all assertions passed. As only the compact executable source and its output are persisted here, these supplementary observations are not used as independently archived certificates.

## 4. Next independent units

1. Derive a symbolic or interval/rank automaton eliminating enumeration of structurally distinct histories as well, with a strict same-input mask and cost comparison against the quotient algorithm; or find a counterexample to an attempted simplification.
2. For S={1,3}, test whether the Stage511 uniform provenance cap 2 may be reduced to 1 at h≥2 over a specified R, then prove a scoped lemma or preserve an exact counterexample.
3. Independently implement the all-twelve-native-direction / 144-active directed relation heterogeneous repeated-edge Euler–BRC rank **and** unrank measurement with actual big-integer and preprocessing costs.

## 5. Publication and review boundary

This is author-side mathematical derivation and local exact evidence. GitHub credential identity is `awdawmip` with admin permission; native session, task list and status calls returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false` at 2026-11-08 ~03:14 Asia/Shanghai; Site gateway reported `CONFIGURED_NOT_LIVE_VERIFIED`. No current native Owner/CLAIM, Native Result, Driver review or Foundation promotion is asserted. The branch preserves the research checkpoint for later authorized intake without altering a current task owner.
