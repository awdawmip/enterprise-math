# R762AT — V29 cumulative triadic-passage ledger stabilizes an odd V17 holonomy selector

Date: 2026-11-15. Researcher provenance: EM-X6-3050F6. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Current science input frozen at enterprise-math@`a72226e2430ffa4786321ac86e7f0c599d5f0389`. Status: AUTHOR PROOF + EXACT BRC CHECK, NOT_REVIEWED.

## Scientific question and exact model

R762AS established a sharp frame-covariant token requirement under an explicit frame-to-port bridge. The next question is closer to V29's *actual* count-ledger law: does repeated, genuine nonnegative V29 PASS deposition preserve the V27 deterministic active-triad odd-holonomy mechanism, or does accumulated skew circulation alter it?

Use **the published V23/V25/V27 four-field conditional selector**, not a new native force law. An active triad S is a 3-subset of {0,...,5}; its four-field code c(S) is the V23 perfect-matching parity code:
```
{{0,1},{2,3},{4,5}}, {{0,2},{1,4},{3,5}},
{{0,3},{1,5},{2,4}}, {{0,4},{1,3},{2,5}}.
```
For matching pairs (a_i,b_i), c=0 unless exactly one endpoint of every pair is in S; otherwise c=(-1)^(number of second endpoints in S). The 20 codes are distinct.

Fix the typed four-port V29 Cell ledger, with nonnegative M[a,b], Rin[a], Rout[a]. Use the actual V29 rules I=M1+Rin, O=M^T1+Rout, u=I-O, Omega=M-M^T. Initialize Rin=(0,0,0,10), Rout=(2,4,3,0), M=0. One **three-PASS macro** deposits the ordered occurrences PASS(0->1), PASS(1->2), PASS(2->0); after n macros, M_n[0,1]=M_n[1,2]=M_n[2,0]=n, all other entries zero. This is a declared event schedule; V29 itself does not impose an event-selection law or token inventory gate.

Consequently u=(-2,-4,-3,10) for every n, while Omega_n=n Omega_1 with
```
Omega_1 = [[0,1,-1,0],[-1,0,1,0],[1,-1,0,0],[0,0,0,0]].
```
For S~T sharing exactly two axes, set Phi_n(S,T)=u·c(T)+c(S)^T Omega_n c(T). This is exactly the V25/V27 conditional edge-score family. Under the existing positive Weighted-BRC interface, branch weight is W_rho(S->T)=rho^Phi_n(S,T) with any fixed rational rho>1. Rank comparison is exactly exponent comparison; the checker also compares positive rational weights at rho=2 with arbitrary-precision BigInt, without floating approximation. The signed contrast is kept separately; no positive mass is used as a signed force.

## Theorem AT1 — exact repair of the PF-10/V29 ledger witness

The V27 displayed signed contrast u and single 3-cycle M are compatible with V29, but V27's illustrative values I=(0,0,0,10), O=(2,4,3,0) cannot be a joint PF-10 window count with that M: the first three rows of M each contain an internal passage, whereas their displayed I counts are zero. For each n>=0 the **unique componentwise minimal** pair of nonnegative I,O compatible with the fixed M_n and u is
```
I_n=(n,n,n,10),  O_n=(n+2,n+4,n+3,0).
```
Indeed M_n 1=M_n^T 1=(n,n,n,0), so u=Rin-Rout; componentwise minimal nonnegative solutions are Rin=max(u,0), Rout=max(-u,0). Every other admissible solution adds the same nonnegative slack to both residual counts in each coordinate. This repairs the old count-bookkeeping witness while preserving exactly the original u, Omega_1, branch scores, and V27 n=1 six-cycle. It is a source-compatible **repair**, not a rejection of V27's existing odd-holonomy calculation.

## Theorem AT2 — a sharp finite threshold for eventual deterministic odd transport

Let F_n(S) be the unique maximizing neighbor of Phi_n when one exists. **For every integer n>=15**, all 20 states have a unique maximizing neighbor, and the entire successor map F_n is independent of n. It has exactly one recurrent orbit,
```
012 -> 123 -> 234 -> 034 -> 035 -> 025 -> 012,
```
whose V17 shared-axis frame transport is (2,1,0), i.e., the transposition of slots 0 and 2, of odd parity. Every other triad enters this orbit in at most **three** successor steps; 145 needs exactly three. The uniform threshold 15 is sharp: at n=14 the state 014 has tied maximizing neighbors 013 and 145.

**Proof beyond finite n-search.** Every candidate edge score is an affine integer function b(S,T)+n a(S,T), with b=u·c(T) and a=c(S)^T Omega_1 c(T). Calculate the maximizer F_15 by the 20 explicit V23 codes. Among its 160 winner-versus-other-neighbor pairs, each score difference at n=15 is at least 1, while its coefficient of n is nonnegative: slope 0 occurs 52 times, slope 1 occurs 54 times, slope 2 occurs 54 times. Thus for all n>=15 each strict comparison remains strict, proving the **infinite** tail without extrapolating from numeric samples. The provided deterministic 20-state map has only the stated six-cycle; its V17 slot transport and the three-step maximum transient are established by complete enumeration over 20 states. At n=14, the displayed tie proves sharpness. QED.

If the protocol performs one full three-PASS macro per active-triad update, then n advances by one, so every trajectory which continues beyond n=15 follows the fixed successor graph thereafter, reaching the odd six-cycle within three more active-triad updates. Branch decisions for n=2,3,4,5,12,13,14 must remain explicitly branched (see exact tie certificate), rather than forcing a lexical tie-break or treating the cumulative ledger as a timeless snapshot.

## Evidence and boundary

The self-contained Node verifier exhausts all 20 V23 codes and their 9 neighbors (180 directed scores), 160 affine winner-versus-competitor inequalities, every tie in n=0..15, 20-vertex functional graph and based-slot holonomy, and 11,520 independent exact positive BRC weight comparisons at rho=2. It directly verifies the corrected PF-10 counts. The JSON is direct checker output. This is an exact finite-enumeration-backed algebraic proof of a statement for **every n>=15**, via nonnegative affine slopes; the finite check by itself is not used to justify an unbounded claim.

The conditional V23/V25 deterministic score rule is additional to P000. The V29 ledger deposition is an actual defined event operation, but the fixed choice of three PASS events, autonomous scheduler, mapping of four typed source fields to actual Cell ports, and admissible signed-force `TRIADIC_CLOSURE_E` event still require a native bridge. The six X6 spatial axes, three-dimensional slice, native PERP_E 120-degree relation and exact Cell/Link/source provenance are unchanged. V39 based-loop observer has not been separately evaluated.

Sources: canonical main `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md` (blob 6849ebd3fc776fb7da3b46627376490aba3dad99); `X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md` (blob 42b810a8f82c504833027da17884cc4fb2943e5b); `X6_ATOMIC_TRIADIC_PASSAGE_DRIVES_ODD_HOLONOMY_V27_20260906.md` (blob c5a02e6727dfc1f70ae4594c3ee807d1760c0be9); `experiments/x6_dynamic_law_holonomy_v24_20260906/check_channel_circulation_bridge.py` (current source), and R762AS proof @91040b54ae619dac9cc97a8e36187b67d8f4fdd3.

Next discriminating problem: couple the **same** incremented PF-10 Cell ledger to an admitted signed-force TRIADIC_CLOSURE_E Cell/Link/Port event and test whether its scheduler actually makes this three-PASS macro legal; then add the native V17 source-port frame action and V39 based-loop readout. The exact n>=15 eventual-cycle result is ready as a reference case, not native-law admission.
