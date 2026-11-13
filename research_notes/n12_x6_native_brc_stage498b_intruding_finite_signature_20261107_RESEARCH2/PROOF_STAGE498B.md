# Stage498-B — Exact finite-horizon BRC quotient under intruding public edits
Date: 2026-11-07. Author-side proof and exact executed evidence; independent Driver review pending.

## Source/authority
Frozen scientific pins unchanged: GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, original P000 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Direct parent Stage497-B `4412de8efd435bec516f20cb660803a918754e5a`; its NEXT_TASK_PACKET_498B.md sets the question. Current behavioral snapshots separately read: GLOBAL main `2b07a7f65f1b2f428b5d35297836f7a6ae3aaad3e`, EM main `d0ecaba59bff8c711bc7739654ce8b980b9b4d3e`. Enterprise Math native gateway status/task read returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. This write is branch-side author evidence, not a native CLAIM/Result.

## Typed model
The full native signed-X6 direction alphabet has 12 distinct symbols A..L for +/-e1..+/-e6 in a chart of SIX spatial axes. An ordered token word w has D(w)=sum v(w_i) in Z^6 and all 144 directed adjacency counts E_ab(w). Let F(w)=(D,E). The executable experiment restricts value directions to {A,B,C}; all 144 directed pair coordinates remain present. Full population consists of ordered words with source labels O (original) and P (publicly inserted). Initial words carry only O tags. Provenance labels are nonspatial metadata; the F observer does not read them directly.

The five fixed partial commands on current (w,p), n=|w|, are: POP final token; SET_END_MINUS_2_C changes zero-based index n-3 to C if n>=3 (source tag retained); INSERT_BEFORE_LAST2_C inserts C tagged P before index n-2 if 2<=n<8; DELETE_END_MINUS_1 removes index n-2 if n>=2; DELETE_LAST_PUBLIC removes rightmost P-tagged token if one exists. The observed trace records F after EVERY prefix, plus action legality. These operations can target original opaque intervals; Stage497's no-intrusion guard need not hold.

## Theorem 498.1 (unique coarsest exact horizon-h observer quotient)
Let S be any state set with finite fixed action alphabet A of deterministic partial transitions T_a and exact observer F:S->O. Define S_0(x)=F(x) and S_(h+1)(x)=(F(x),(L_a(x))_{a in A}), where L_a(x)=ILLEGAL if T_a(x) is undefined and otherwise L_a(x)=S_h(T_a(x)). Define x ~_h y if the same public action traces of length <=h are legal in both and all F observations at every trace prefix agree. For each integer h>=0,

**x ~_h y iff S_h(x)=S_h(y).**

Therefore the partition by S_h is the unique coarsest exact observer-preserving partition for this operation language and horizon, up to renaming of classes. This minimality counts equivalence classes, not a minimum-bit universal encoding or a fast algorithm.

*Proof.* At h=0 only the empty trace exists, so ~_0 is equality of F. Inductively, equality of (h+1)-signatures supplies equal current F, equal legality of every first action a and equal h-signatures for every legal successor. Applying the h-induction hypothesis to each successor yields equal F along every prefix of all traces length <=h+1. Conversely equality of all such traces forces equality of current F and first-action legality; each pair of legal successors agrees for all traces of length <=h, so has equal h-signature. Collecting them yields equality of S_(h+1). Any compressed representation preserving the declared trace responses must distinguish states outside the same ~_h class, so its fibers refine S_h classes. The quotient by S_h itself is exact. QED.

The finite certificate is executable by memoized enumeration of reachable (state,depth) and exact interning of observations and ordered successor tuples. For a fixed finite initial population N and horizon h, the pre-dedup action exploration is <= N * sum_{j=0}^h |A|^j; no complexity speedup is inferred. The program interning compares exact JSON strings of integer arrays; strings, rather than hash codes, are the equality keys.

## Theorem 498.2 (exact provenance obstruction)
The states (A,O) and (A,P) have identical F. Yet DELETE_LAST_PUBLIC is illegal on the former and legal on the latter, so they are separated at h=1. Thus if future commands can select by provenance, token-F equality alone is not enough to erase provenance. A different grammar that never reads provenance has a different quotient. QED.

## Complete finite experiment
Enumerate all initially O-labeled ordered words of lengths n=4,5,6,7 over {A,B,C}. The table gives number of distinct exact S_h classes for horizons h=0..4:

| n | Population | h0 | h1 | h2 | h3 | h4 |
|---:|---:|---:|---:|---:|---:|---:|
|4|81|75|81|81|81|81|
|5|243|186|243|243|243|243|
|6|729|414|711|729|729|729|
|7|2187|840|1908|2133|2187|2187|

In the n=6 population, 18 two-element S_1 classes remain and are split by h=2. For n=7, 54 two-element S_2 classes remain; all split by h=3. The largest initial F fiber for n=7 contains 12 distinct histories. The full observer has six signed displacement coordinates and 144 directed pair counters. All counts are exact, not sampling estimates.

For initial pairs with all O tags, the EXACT shortest separating traces are:
- AABA vs ABAA: first at h=1 via POP, yielding AAB vs ABA.
- CACCAA vs CCACAA: equal through h=1, first at h=2 via POP then SET_END_MINUS_2_C, yielding CACCA vs CCCCA.
- CACCAAA vs CCACAAA: equal through h=2, first at h=3 via POP,POP,SET_END_MINUS_2_C, yielding CACCA vs CCCCA.

Lower bounds follow from equality of the complete recursively evaluated S_h signatures, hence cover ALL allowed traces; upper bounds are the displayed legal traces giving unequal F. A separate, direct full-action-tree recursion checks all same-F initial pairs for n<=6 at h<=2, giving 1602 pair-horizon comparisons with complete agreement. The executable program also asserts all witness horizons and the provenance legality split; output file records ALL_ASSERTIONS_PASSED.

## BRC result and scope
Distinct ordered histories remain BRC branches; F fibers collect branches with exact multiplicities, and S_h retains precisely the future-visible structural residual under the declared grammar. Even when an edit enters the original protected interval, a nontrivial safe quotient can remain at finite h (n=6 h=1 and n=7 h=1,2). The exact quotient is more flexible than the Stage497 no-intrusion sufficient condition. The complete proof applies to any deterministic finite-action observer system; the numerical certificate is confined to this explicitly defined subalphabet, provenance tags, action set, length cap and horizon. No physical heartbeat law or native rotation propagator is asserted.

## Reproduction and next unit
Run `node REPRO_STAGE498B.js > REPRO_STAGE498B_EXECUTED.json`; Node builtins only. Exact raw output saved beside this proof. Next study a compositional cut-interface K_h for long intervals that can be computed without full word enumeration, and separately measure full bit/wall/memory cost for heterogeneous Euler-BRC ranking on 144 active edges.