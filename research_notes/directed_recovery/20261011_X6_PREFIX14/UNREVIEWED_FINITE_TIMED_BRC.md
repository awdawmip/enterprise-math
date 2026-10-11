# X6-SIG-PREFIX-14 — timed BRC finite quotient (UNREVIEWED DRAFT)

Status: `LOCAL_EXACT_REFERENCE_PASS / NATIVE_IMPORT_PENDING / SOURCE_ADMISSION_PENDING`.
Source pins: global knowledge `46de0b0d4865d9e7410df30d96b07ee4167d1fbe`; Enterprise Math `d679a01c5e15c1ec24544e0e226013839053a47e`. This is a branch-level research draft, **not** a canonical claim, checkpoint, approved Result or physical theorem.

## Declared model
Let S be a finite **nonspatial** control type set, times t=0,...,H, public readouts o_t:S->O_t. Packet P in G_t has native `start=t`, **positive integer** `duration=d(P)` with t+d(P)<=H and exact typed BRC histograms H^P_{s,u} of (positive rational branch weight, six-axis rational affine effect, positive integer multiplicity). Alternative combines like effects with positive counts. Sequential composition is convolution with action order (w,A)*(v,B)=(wv,B∘A), not signed cancellation. Readouts are allowed at packet boundaries; no mid-packet hidden-state access.

## Theorem: duration-aware coarsest exact-step partition
At time H put pi_H=[o_H]. At each earlier t, for every P in G_t and every class C of pi_{t+d(P)}, let
  R^P_{t,s}(C) = sum_{u in C} H^P_{s,u}
where sum is exact BRC alternative of complete (weight,Affine6,count) keys. Define
  pi_t(s) = [o_t(s), ((P.name,d(P), (R^P_{t,s}(C))_{C in S/pi_{t+d(P)}}))_{P in G_t}].
Then pi_t is the unique coarsest time-varying partition preserving both current readout and exact effect-histogram output to every **retained destination control class** for every allowed packet, with all legal future packet concatenations on the finite time DAG. Proof: d>=1 gives strictly later target times. Reverse induction establishes soundness using exact histogram distributivity and affine composition associativity. Any other safe partition sigma_t must have identical o_t and exact outgoing rows to each sigma_{t+d} class; since every later sigma_{t+d} refines pi_{t+d}, summing rows proves sigma_t refines pi_t. The conclusion is for this strong interface, NOT arbitrary minimal late scalar observation, provenance-free aggregation, physical heartbeat duration, or complete path-history encoding.

## Exact counterexample to ignoring duration
S={0,1,2}; t=0,1,2; o_0=o_1=(0,0,0), o_2=(0,0,1). Sole action at t=0 is a duration=2 deterministic positive-unit-weight packet 0->0,1->2,2->2. True pi_0=(0,1,1) distinguishes sources 0 and 1 by the t=2 observation; the incorrect duration-one-only recursion without that packet gives (0,0,0).

## Exact noncommuting Affine6 witness
Let A=I_6+E_{12}, B=I_6+E_{21}, so BA≠AB. A first packet (duration1) from control0->control1 has atoms (2/3,A,count2), (3/2,B,count3). Then a packet (duration2, start1) from control1->control0 has (7/5,B,count4). Their exact composition has only
  (14/15,B∘A,count8), (21/10,B²,count12).
Checking wrong second packet start=0,2,4 gives three time-port mismatches, not legal composition.

## Zero-duration boundary
The real `ControlPacket.identity` has duration0. A nontrivial zero-duration action makes the time graph cyclic and needs same-time fixed-point treatment. Strong obstruction: the one-control-state duration0 self-loop with positive weight 2 and identity Affine6 yields distinct atoms (2^k,I6) for all k>=0. Aggregating all finite same-time histories in a single **finite-support** EffectHistogram is impossible. No cancellation or precision trick removes this. Distinguish bounded zero-time words, unbounded finite-word behavioral equivalence, and the generally non-finite histogram union.

## Exact checks
`check_prefix14_typed_dag.py` (local handoff) executed with Python exact Fraction, no floats: 35 seeded models / 175 available packet options, 238 exhaustive safe partition candidates checked, 716 independent complete observable trace equality pair checks, noncommuting six-axis effect multiplication, three deliberate time-port rejections, and 13 exact loop-powers all passed. A separate `check_prefix14_native_control_port.py` is prepared but the current runtime lacks the `enterprise_math` package (`ModuleNotFoundError`); **do not claim native execution**.

## Source/prior-art boundary
`src/enterprise_math/brc_control_port.py` already defines `refine_control_partition` for time-homogeneous permanent control quotients; PREFIX-13 handled duration1 finite windows. This draft only extends the declared finite-time interface to duration jumps and noncommuting Affine6 checks. Weighted automaton bisimulation / partition refinement is pre-existing mathematics (P. Bhaduri, LMCS 19(1), 2023, DOI 10.46298/lmcs-19(1:4)2023; S. Lombardy and J. Sakarovitch, arXiv:2112.09387).

## Authentication and next
The private Enterprise Math Sites credential is static read-only (`em:access/source:read/control:read`, `research_authority_granted=false`). Attempted `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED; operation_sent=false`. No X6 Claim, runtime, native checkpoint, independent Driver or mathematical admission was obtained. Next: independently re-run true-module `ControlPacket` regressions, then PREFIX-15 studies same-time zero-duration weighted bisimulation vs infinite aggregate branch histories and the exact admissibility of bounded loops. Preserve X6 native six-axis P000 and all earlier source/history distinctions.
