# PREFIX-984 — Four-phase signed-source cycles: an eight-step threshold and exact census

Date: 2026-11-21 Asia/Shanghai
Status: AUTHOR_CONSTRUCTIVE_PROOF / EXACT_INTEGER_CENSUS_p3_p7 / NOT_REVIEWED
Predecessor: PREFIX-983 (three-phase uniform dichotomy)
Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json

## Model and question

This is the auxiliary signed-source bit-flip observer, not a native X6, Heartbeat or physical-residual computation. Fix p>=3, odd input x in [0,2^p), and nonzero residual c. A named source (i,j,s) has 0<=i<p, 1<=j<p, s=+1 or -1, c=2^i-s*2^j. It is legal exactly if bit_j(x)=(1-s)/2. Its move flips bit j, then advances the phase of a fixed ordered four-residual word w=(a,b,c,d). Source multiplicity/sign and move order must be retained when interpreting actual paths. A four/eight-step return means the same integer input and phase after respectively one/two full words.

PREFIX-983 proved a six-step criterion in the three-phase case. The one-period analogy for four phases is false.

## Theorem 984.1 — Two periods can be necessary (all p>=6)

For every integer p>=6, w=(6,24,6,-3) has an eight-step, phase-aligned closed named-source path, but has no four-step, phase-aligned closed path starting from any odd input.

Proof: From the exact source equation, the allowed nonzero ports and bit requirements in the four phases are:
- residual 6 (phases 0 and 2): port 1 accepts either bit; port 2 accepts bit 1 only;
- residual 24 (phase 1): port 3 accepts either bit; port 4 accepts bit 1 only;
- residual -3 (phase 3): port 2 accepts bit 0 only.

In any four consecutive moves beginning at phase 0, the phase-1 move flips one of ports 3 and 4. No other phase flips either port. Hence parity makes integer return impossible for any initial state.

For existence, take odd x=5 and choose ports (2,3,1,2,2,3,1,2). The exact states are
(5,1,9,11,15,11,3,1,5).
Their actual signed named sources (i,j,s) in order are
(1,2,-1), (5,3,+1), (3,1,+1), (0,2,+1),
(1,2,-1), (4,3,-1), (2,1,-1), (0,2,+1).
Substitution in c=2^i-s*2^j checks every equality; each bit at the time of use satisfies the sign requirement. The last integer equals the first, and the phase returns to 0. Repeating gives an infinite path. More generally every odd x with bit_2(x)=1 admits the same port sequence, giving 2^(p-2) such initial states. QED.

The mechanism is genuinely joint: the phase-1 port 3 changes signed source from (5,3,+1) to (4,3,-1) across the two periods. Boolean port availability alone erases this provenance.

## Theorem 984.2 — Exact finite census

An exact all-state census over every ordered four-tuple of nonzero residuals gives:

| bit width p | distinct nonzero residuals | ordered words | words with directed cycles | cyclic without 4-step return | cyclic without 8-step return | longest finite path from phase 0 |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 9 | 6,561 | 960 | 0 | 0 | 4 |
| 4 | 16 | 65,536 | 9,957 | 0 | 0 | 11 |
| 5 | 26 | 456,976 | 54,654 | 0 | 0 | 15 |
| 6 | 39 | 2,313,441 | 209,213 | 1,868 | 0 | 18 |
| 7 | 55 | 9,150,625 | 627,234 | 10,992 | 0 | 18 |

Therefore p=6 is the smallest width at which a four-phase word may have infinite paths but no four-step return. All cyclic words examined at p<=7 have an eight-step return. The longest finite path of 18 steps is attained at phase 0 for w=(6,24,8,40) when p=6 or 7.

Finite checking method: generate all c via their original (i,j,s) equation, collect port requirements as bitmasks 1/2/3, form every state (phase, odd input) and all legal directed edges. Kahn topological elimination detects acyclicity; path-length dynamic programming gives the exact longest finite path. For cyclic graphs, exact 4/8-step reachability from each phase-zero state tests the corresponding closed walks. All words, all odd inputs and all phases are covered for each p=3..7; integer arithmetic and bit operations only. A separate Python reachability/topological implementation matched p=3,4,5 counts. This is author-provided reproducible finite evidence, not an independent Review.

Evidence:
- Source program: research_notes/portable_direct/PREFIX984_R6_FOUR_PHASE_EXACT.cpp at 9ca9ca8b8fa1d4b9ca44ffee7ee790fd1c1b0357
- Exact integer results: research_notes/portable_direct/PREFIX984_R6_EXACT_RESULTS.json at a62cfcc6403efc9c8f7e89c9028ee4cd2753420e
- Reproduce: g++ -std=c++17 -O3 PREFIX984_R6_FOUR_PHASE_EXACT.cpp -o prefix984; run prefix984 p for p=3,4,5,6,7.
- Predecessor manuscript: research_notes/portable_direct/2026-11-21_r6_prefix983_uniform_three_nonzero_dichotomy.md, observed blob ced9a23b0fb4b4e3c48ef6e65d867acf35da216e.
- Historical research provenance: EM-DIRECT-FBEA5D, Activity RA-3FB2D033BE6048D8712FF056. Source publication here is not CLAIM, formal PROGRESS, Result, Review or a new Activity-CAS event.

## Questions open after this result

1. For arbitrary width p>=3, is the existence of an infinite path equivalent to an eight-step closed path in a four-stage nonzero-residual word?
2. Is the uniform finite path length at most 18 in every bit width, and is 18 sharp? The present census proves that statement only for p=6,7.
3. Establish an actual typed BRC-to-X6 update/observer correspondence that preserves named signed sources, joint path order and future operations before native attribution.

The mother problem B_fix,odd(32) in {19,20} remains open; the protected P000 and ACTIVE worldview are unchanged.
