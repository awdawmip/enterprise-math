# X6 to V39: a repeatable one-query code with one frame-phase bit

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_BRC_CHECK / NOT_FORMAL_INDEPENDENT_REVIEW.

This continuation uses the V39/R757 source-defined based macros and the preceding single-window relational code. It proves a repeatable network readout interface. It does not assert a primitive force-to-packet permission or a physical clock coupling.

## 1. The single-window code has a baseline that must be retained

Use the exact V39 convention

    h(path; next) = h(next) composed with h(path).

Let e=(0,1,2), a=(0,2,1), b=(1,0,2), g=(2,0,1), t=(2,1,0). R757's macros have h(A)=a, h(B)=b, C=B^-;A^- and h(C)=g. Every permutation of A,B,C returns to the common base and has zero final current and exactly one copy of A+,A-,B+,B-.

The previous one-window encoder chose ABC/ACB/BAC/BCA from the four adjacent-relation values. Its decoder assumed the block began at h=e. In a repeated stream, if a block begins at H, its queried frame is

    M = h(first two macros) composed with H.

The accumulated H cannot be silently replaced by e. For example, ACB ends at g. Repeating ACB then queries t composed with g instead of t; repeated application rotates through all three transpositions. The original absolute-frame table therefore is not, by itself, a repeatable fixed decoder.

This is an observer-baseline issue, not a failure of the original single-window theorem.

## 2. Exact repeatable code

For three consecutive named shell signs define

    q1=y0*y1, q2=y1*y2,
    d1=(1-q1)/2, d2=(1-q2)/2.

Initialize the network once with known h=e. Retain one frame-phase bit p in the sending controller, with invariant h=g^p and p in {0,1} at every completed block. The receiving decoder does not need p.

Choose the macro order using the following complete table:

| d1,d2 | Word when p=0 | Word when p=1 | Absolute frame after macro 2 | Next p |
|---|---|---|---|---|
| 0,0 | ABC | BAC | g^2=(1,2,0) | 0 |
| 0,1 | ACB | CAB | t=(2,1,0) | 1 |
| 1,0 | BCA | CBA | a=(0,2,1) | 0 |
| 1,1 | CAB | BCA | b=(1,0,2) | p |

**Theorem 1 (repeatable single-query code).** At the second completed macro, the queried absolute S3 frame has the displayed value independently of p. These four values are distinct, so a fixed decoder recovers (q1,q2). Completing macro 3 preserves h in {e,g} and updates p as shown. Every block has zero final current and the same four directed rings. By induction, this holds for an arbitrary finite or infinite sequence of completed input windows, without reset packets and without querying the next block's initial frame.

**Proof.** For initial p=0 the relevant two-macro transports of ABC,ACB,BCA,CAB are g^2,t,a,b. Their full transports are e,g,e,e. For p=1 the chosen words BAC,CAB,CBA,BCA have prefix transports g,b,t,a and final transports g^2,e,g^2,e. Right composition with the starting g gives respectively g^2,t,a,b at the query and e,g,e,g at completion. These are the table entries. The zero-current and directional-count statements hold word by word by the unchanged R757 macro expansions. Each completed block reestablishes the invariant required by the next. QED.

The boolean update may also be written

    p_next = d2 AND ((NOT d1) OR p).

There are still three source samples and one four-valued frame query per reported window. The four-valued query contains two binary units of outcome information. The one additional bit is **accumulated network-frame phase**, not the whole controller state and not a new source-sign calibration.

An initially known p=1 is also valid. An arbitrary unknown initial S3 frame is outside this initialization contract. A known network frame must not be confused with the absence of an external calibration of source rotation-edge signs.

## 3. One phase bit is minimal in the stated repeated-code interface

The lower-bound class is precise: each window is encoded by one ABC permutation; only the frame after macro 2 is queried; the receiving decoder is fixed and memoryless; the sender is a **stationary current-q encoder**, whose word choice depends only on the current two relation bits. It has no carried phase, additional frame query, reset loop, or external window counter/raw absolute sign used as hidden carried state. A first-window-versus-later-window flag is already carried information and is not a zero-memory exception. Source-sign reversal must leave the macro word unchanged. We count carried phase separately from the two current relation bits and the repeated within-window control mode.

**Theorem 2.** No zero-carried-phase encoder in this class can encode all four relations repeatedly. This remains impossible even when each source experiment has a constant relation in successive disjoint three-read windows, as happens for an exact X6 sequence with y_(n+3)=-y_n. The one-bit construction of Theorem 1 attains the minimum carried phase count.

**Proof.** Without carried phase, each relation chooses a fixed word W. Repeating this same relation queries

    h(prefix_2(W)) composed with h(W)^n, n=0,1,2,... .

All final transports are in C3={e,g,g^2}. If h(W) is nonidentity, its powers are all C3, so its query orbit is the entire even or odd coset of C3 in S3, according to its prefix parity. At most one relation can use an entire coset, and every other relation must use query values in the other coset. A second nonidentity word would either collide in the first coset or occupy the whole other coset, leaving no value for a third or fourth relation. Thus at most one chosen word has nonidentity final transport.

The only identity-final words are ABC,BCA,CAB, whose query frames are respectively g^2,a,b. If no nonidentity word is used, these give at most three distinct relations. If one nonidentity word is used, its whole coset meets either g^2 (the even coset) or both a,b (the odd coset); therefore the remaining three relations cannot all use the three identity-final words without a collision. Four relations are impossible. QED.

This does not rule out moving phase memory to a stateful receiver, querying additional frames, using reset packets, changing the block language, or using a different observation channel. The minimality claim is exactly for the stated one-query repeated interface.

## 4. A finite online controller and its actual timing contract

For the new table, defer macro execution until all three samples of a window have arrived. In particular the two rows beginning at p=0 and d1=1 require BCA versus CAB, whose first macros differ. Launching a first macro from d1 alone would assume unavailable information in this table.

An implementation has the following logical stages:

1. Acquire the named sample y0 at source index n, retaining its sign.
2. Acquire y1 at n+1; retain d1 and y1 (two source bits).
3. Acquire y2 at n+2; replace that register by d1,d2, choose the table word using p.
4. Dispatch and await completion of the first based macro.
5. Dispatch and await completion of the second based macro; query its absolute frame once and emit the decoded pair for this named window.
6. Dispatch and await completion of the last macro; commit the displayed p_next and acknowledge window completion.

The controller holds at most two source-dependent bits plus one persistent network-phase bit. The selected program can be generated from those registers and the macro position; it need not be stored as a separate uncounted input-dependent word. Window/macro position, completion handshake and sample identity are explicitly separate control/provenance data. A separate acquisition buffer holding a raw pending window uses its three sign values plus names/event indices; it is not free storage included in the controller's three-bit count. The Path/BRC evidence retains full named signed sample leaves and ordered directed-ring paths; a small observer/controller state is not a claim that the whole physical evidence uses three bits.

With a producer that retains a pending window until the receiver acknowledges it, and with each dispatched macro eventually completing, the protocol is lossless and live on the declared accepted windows. Arrival delays and macro completion delays merely insert waits in the same causal event order. The decoder and completed BRC projection do not depend on those delays. Consecutive **source event indices** n,n+1,n+2 must still be checked; consecutive delivery times alone do not prove this.

The contract permits a finite held window or a paced producer. It does not establish that the physical X6 source can be halted. If the native source evolves autonomously, the acquisition layer must either retain the consecutive samples, select explicitly declared windows, or satisfy a separate rate/buffer bound. Flow control on delivery alone cannot recover samples that were never captured.

The repeated code also assumes its blocks are serialized on the declared network port, with no unaccounted external loop inserted. An additional known loop can be handled in the full V39 (j,h) port, but may leave the two-phase invariant of this particular encoder. Concurrent shared-network scheduling or re-entry from an arbitrary S3 frame requires a separately specified bridge.

### Finite buffering obstruction without pacing

**Theorem 3.** An arbitrary-rate source, arbitrarily delayed network completion, finite total pending-window storage and a requirement to report every source window exactly once are incompatible.

**Proof.** Hold the network without completion while the source generates N windows of one fixed relation. Even though their relation values agree, their named occurrences and required output multiplicities differ. If the complete pending-work state has K possibilities, two different counts among 0,...,K reach the same state. Resume the same subsequent network completions and give no new source input. The identical state then produces the same number of reports for the two different required counts, so one execution fails. A queue/history whose size grows with N escapes this argument by providing unbounded storage; it is not a finite-buffer implementation. QED.

For arbitrary relation-valued windows, keeping all ordered pending values requires at least 4^N distinguishable queues at a fixed backlog N. For exact feedback dynamics the values may be predictable from the initial source state, but exact named occurrence count still requires N+1 distinguishable backlog states through backlog N. Predictability does not remove multiplicity when every window is a required report. A latest-relation-only interface has a different observer and can discard superseded windows only under that separately declared scope.

## 5. Completed relation and future-safe network state

The fixed decoder is memoryless only for the current relation. Unlike the preceding one-window code, the current relation alone does not always determine the accumulated final h: input q=(-1,-1) preserves the incoming phase.

For the unrestricted repeated-window interface, the reachable joint completed records are exactly

    ((+,+),0), ((+,-),1), ((-,+),0), ((-,-),0), ((-,-),1).

All five are reachable from initial e: the last one arises by first sending (+,-), then (-,-). The current relation query distinguishes different q, while V39's direct h query distinguishes the two (-,-) records. Conversely (q,p) determines the current relation and (j=0,h=g^p); by V39's composition theorem it determines every later declared L_JH observation under the same appended loop history. Thus **five classes are necessary and sufficient** for the joint current-relation-plus-V39-future observer at balanced boundaries, requiring three bits of fixed-length storage. Source/path-order queries retain their underlying Path/BRC carrier.

This is separate from the two-bit current relation result and the sender's one carried phase bit. Correlated state coordinates must not be added as though independent.

## 6. Relation to the continued X6 source machine

For the ingress-feedback source, the parallel source proof gives y_(n+3)=-y_n. Successive disjoint three-read windows therefore have the same (q1,q2); sliding one-event windows update by

    (q1,q2) -> (q2,-q1*q2).

The repeatable V39 table works for both these sequences and for arbitrary explicitly supplied relation windows. For ingress feedback, reconstruct the initial-window relation by

    r_(j-1)=q1, r_(j-2)=-q1*q2, r_j=q2.

For a fixed generator the conversion is instead (q1,q2,-q1*q2). The encoder only transmits the pair; the proven source law determines which conversion applies. Window offsets remain part of the source interface.

For a **single fixed feedback source**, initialized with network h=e, and consistently using either disjoint consecutive three-read windows or one-event sliding windows, the fifth joint state ((-,-),1) is unreachable. Indeed q=(-,-) is a fixed source orbit and never reached from the other three relations; it starts at p=0 and preserves that phase. For all other relations the table resets p, so at every completed window

    p=1 if and only if q=(+,-).

The joint completed relation/network record then has exactly four classes. Its network phase is derivable from the retained relation, and the current source predictable-state register may already contain it. No unconditional extra bit may be added to a source-state minimum. The one-carried-phase lower bound in section 3 concerns a word selector with no carried information; retaining the previous source/relation state is itself such information. Changes of source orbit, arbitrary window delivery or arbitrary initial network phase restore the broader interface and its five classes.

The full source predictable-state theorem belongs to the parallel source note. This bridge neither needs nor claims to regenerate physical source measurements from its network frame. Its new result is the exact repeatable packet code and the explicit sequencing/buffering contract.

## 7. Source pins and verification

- V39: `enterprise-math@ef720decf4a35a276e509964250571a55421b9f8:research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md`, blob `8151d0b6a4b65225b93d858bbc8a5d7037bf9cef`.
- R757: `enterprise-math@ed0b15b4ba948a21150969478d8a6941db76b11f:research_notes/R757_V39_BOWTIE_NATIVE_THREE_PACKET_CLOSURE_20261113.md`, blob `29db8d67e2dcd7ed76fd358219d04a7fcc1418d3`; historical authorship/status remain unchanged.
- Predecessor research package, parent-verified publication `enterprise-math@5806c80973d881009a755e8b5c922dab758a1032`: `research_notes/portable_direct/20261119_x6_native_relational_feedback/V39_RELATIONAL_PACKET_COMPRESSION.md`; this note corrects no single-window claim and makes its repeated-window baseline explicit.
- Applicable native and observer contracts: parent-verified P000/Heartbeat, BRC-only method, residual fidelity and Joint Relation Observer Preservation at the frozen comparison snapshot.

`check_v39_stream_bridge.py` verifies every entry, sign reversal, consecutive named sample indices, exact directed paths, single-query decoding, end-phase closure, all pairs of successive relation windows, and all 6^4 fixed stateless encoders against the constant-input obstruction. It also exercises both disjoint and sliding windows of every anti-periodic three-sign source. These are exact finite path checks; the arbitrary-stream and arbitrary-delay claims follow from the proofs above.

This contribution creates no identity, Activity, CLAIM, native admission or independent Review. Publication and the current portable author attribution are handled by the parent research session.
