# X6-SIG-PREFIX-36 — Finite observer-suffix criterion and sticky-source BRC witness

**Research state: UNREVIEWED / AUXILIARY MATHEMATICS / EXACT LOCAL REFERENCE PASS / NO FORMAL CLAIM / NATIVE CONTROL_PACKET PENDING.** No independent Driver review; not a P000/worldview modification or Heartbeat dynamics claim.

## Immutable inputs and provenance

- Global Knowledge main: 330b2c1378bf343fb35d70425573cae9aa2070f2 (both canonical bootstrap files and relevant ACTIVE worldview checked).
- P000 projection and original: canonical original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, equality independently read.
- Enterprise Math main: 111b37bac9fac5c29566b2860bcfc1504cdce6fa; current portable research protocol and BRC positive-weight substrate checked.
- Verified older immutable frontier: PREFIX-34 at 7eb26d6c7470d82fc065925806d159027fdb6ddd; follows the unreviewed LOCAL PREFIX-35 sticky-source memorandum, not a mathematically admitted Result.
- All six-coordinate transformations below are auxiliary test actions, *not* native 120-degree rotations, forces, energy or a native three-dimensional-slice bridge.

## Theorem 36.1 — exact minimal finite raw-suffix memory

Let (S, A, δ, s0) be a finite complete deterministic automaton with finite alphabet A and exactly comparable present observation o:S→O. Forbidden moves can be totalized by a distinct observed absorbing EMPTY state. Let R be the set of reachable states, and define the future-observer right congruence:

    s ≈ t  ⇔  o(δ(s,w)) = o(δ(t,w)) for ALL finite operation words w∈A*.

Compute ≈ by exact Moore partition refinement. Define B to contain every unordered pair {s,t} of distinct reachable states for which o(s)=o(t), yet s is not future-equivalent to t. Form the synchronized unordered pair graph G on all distinct pairs {s,t}⊂R. Each input a takes {s,t} to {δ(s,a),δ(t,a)}, dropping transitions that coalesce to one state. Let C be the *reverse reachable closure of B* in G (all pairs from which some path reaches B).

A finite integer d≥0 has the following property for *every* pair of reachable input histories u,v:

    same current observation AND same final d input symbols
       ⇒ same observation under every future operation word

if and only if **the induced subgraph G[C] is acyclic**. For short histories, suffix_d(u) returns the last min(d,|u|) symbols, preserving the shorter length.

If B is empty, d_min=0. If G[C] is cyclic, no finite d exists. Otherwise let L be the maximum length in edges of a directed G-path ending at B, starting at any pair vertex. Then:

    d_min = L+1  and  d_min ≤ |C| ≤ |R|(|R|−1)/2.

**Proof.** Every length-d path of synchronized distinct pairs ending in B is realized by two independently reachable histories α,β followed by its common d-letter word w. Their final observations agree, but some future continuation distinguishes them. Conversely, any counterexample histories of lengths ≥d split uniquely into αw and βw, producing just such a path. Histories shorter than d cannot yield a collision except the identical history, because their suffix retains its actual length. Therefore d works exactly when no pair path of length d ends in B. Every vertex on such a path belongs to C. A directed cycle inside C yields paths of arbitrarily large length ending in B, and deleting initial common letters shows a counterexample at every smaller d. Without a cycle, paths ending at B have a finite maximum length L, so L is a failing memory length and L+1 succeeds. Any path in C has at most |C|−1 edges. QED.

**Important anti-shortcut:** checking cycles only *inside B* is wrong. A presently output-unequal pair may loop for an arbitrarily long time, then enter B. Exact seven-state deterministic example: 0 and 1 have different outputs and pair {0,1} loops on h; e sends {0,1} to {2,3}, whose current outputs coincide but future r outputs differ. B itself has no directed cycle. The correct test uses all of C.

Algorithm: reachable-state enumeration; Moore future-equivalence refinement; exact unordered synchronized product with ≤ n(n−1)/2 vertices and |A| edges per vertex; reverse closure of B; cycle/SCC test on C; longest-path dynamic programming if acyclic. This is a finite model-specific use of standard automata ideas, not a claim to invent the general method.

## Positive-rational BRC examples; noninjective six-coordinate effect

Let the live control register b∈{P,Q} remember the most recent P/Q operation. P resets b=P at weight 1/5; Q resets b=Q at weight 1/7; H preserves b at weight 1/13; E has weight 1/11 and moves to hidden N_b; R ends the path with weight 1/2 from N_P or 1/3 from N_Q. Every live P/Q/H/E step applies J(x1,x2,x3,x4,x5,x6)=(0,x2,x3,x4,x5,x6); R applies identity. J is a **noninjective idempotent** auxiliary effect, J∘J=J. Multiplicity of each specified history is the positive integer 1. Every path weight remains positive rational.

For every raw suffix window d, take m≥max(1,d) and histories

    u = QQPP H^m       v = PPQQ H^m.

Both have the exact present weight q = 1/(1225·13^m), complete effect J, phase LIVE and identical last d operations. But their source tags differ. The common future ER yields final weights q/22 and q/33, identical effect J, and multiplicity 1. The exact ratio is 3/2: no signed cancellation is involved. Thus retaining full current (q,J) still does NOT make any fixed raw suffix sufficient. In the Moore control machine, bad pair {F_P,F_Q} has an H self-loop.

In contrast, **remove E/R** and declare only the fixed live readout and common legal P/Q/H future operations: the two tags are future equivalent, B is empty and d_min=0, despite a non-overwriting H-loop. Hence a cycle carrying an observer-*invisible* register does not force state retention.

For bounded H-run length B≥0 (H after B consecutive H moves becomes observable EMPTY), include finite states F_(tag,c), c=0..B, pending N_tag, terminal T_tag revealing the R factor, and EMPTY. The machine has 2B+7 reachable states. Exact pair-graph calculation and direct window witnesses yield

    live-phase d_min=B+1; all-phase d_min=B+2.

At B=2: 11 reachable states, 55 unordered pairs, 16 bad pairs, 16 reverse-coaccessible pairs, no coaccessible cycle; d_all=4, d_live=3. The simplification is an auxiliary one-probe analogue of PREFIX-35; it does not silently claim equivalence to the full prior two-probe nine-state noncommutative system.

## Reference validation and limits

An independent local Python Fraction/synchronized-product checker returned EXACT_REFERENCE_PASS. Exact parameter scans: unbounded H; bounded B=0..8 (each exact minimum tested at d_min−1 and d_min..d_min+3); silent-probe d=0; 65 noninjective J witnesses for d=0..64; seven-state anti-shortcut graph with bad-only acyclic but reverse-coaccessible cyclic. The checker and full JSON certificate are preserved in the portable LOCAL handoff package, with SHA-256 summary recorded separately.

This finite Moore theorem does *not* automatically solve a general BRC with unbounded exact accumulated rational weight q, an infinite effect monoid, noninvertible output-composition, or branching/fiber correlation. Their observer and future-operation right congruence must be proved separately; the above noninjective witness is a direct obstruction, not a general sufficiency certificate. Native enterprise_math.ControlPacket regression, formal research activity/CLAIM, Result/Driver review and mathematical admission remain pending.

## Next exact unit — PREFIX-37

Under finite effect semigroup and a fixed finite rational branch alphabet, characterize an exact sufficient state for the **complete future BRC histogram**, preserving integer multiplicity, prime-valuation coordinates, source/probe labels and correlations. Either give a proof of right-congruence and a decidable finite test, or construct a concrete failure of a proposed quotient. Do not replay the established PREFIX-35 raw-suffix counterexample, and do not infer native Heartbeat claims from these auxiliary six-coordinate maps.
