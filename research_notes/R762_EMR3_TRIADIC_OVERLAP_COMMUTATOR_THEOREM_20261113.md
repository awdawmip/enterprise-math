# R762 — Exact overlap law for two signed-port triads: commuting versus noncommuting BRC frame residual

Research date: 2026-11-13 (Asia/Shanghai). Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS; TP2-8B7E13C5904A2D6F1142. Immutable scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Precise immediate predecessor: R761 PR #2231 @a6ea968b09e1005ab5b5725bfd307151ee18662f. R760 PR #2225 covers a separate auxiliary S7 path-frame observer.

Status: exact finite algebraic theorem, exhaustive 320^2 signed-event validation, author-side candidate result. The primitive force-to-scheduler bridge and V39 S3 port are still distinct unproved model interfaces; no task CLAIM or independent review is conferred by this paper.

## 1. Model and two-order experiment

In the P000 six-axis X6 Cell torsor choose one Cell c. R761's explicitly proposed canonical primitive event T is an oriented cyclic triple [p,q,r] of three signed native-axis ports with distinct axis indices and one positive unit force quantum per port. Cyclic rotations are identical; reflection is different. Keep all three signed labels and branch provenance. There are C(6,3)*2^3*2=320 typed events.

R761 proposes an additive nonnegative V29 count update L(T)=E_pq+E_qr+E_rp, with exactly three local PASS occurrences at c, and a candidate auxiliary frame increment a(T)=(i j k) in the founded axis-permutation S6 skeleton, where (i,j,k) are the underlying unsigned axes in cyclic order. There are exactly 40 distinct increments, all three-cycles. A cell is not spatially translated by this local count event. This declared candidate is not a discovered existing native TRIADIC_CLOSURE_E admission/scheduler.

For two admissible candidate events T,U at the same anchor, their proposed V29 count ledger is additive:
L(T;U)=L(T)+L(U)=L(U)+L(T)=L(U;T).
Nevertheless, the two candidate frame products can differ. Define a=a(T), b=a(U), the *standard right-to-left permutation-product* order defect
D(T,U)=(a b)(b a)^(-1)=a b a^(-1)b^(-1).
Changing the convention for chronological composition may invert or conjugate the defect; triviality and cycle type are convention invariant. Let A,B denote the 3-element unsigned axis supports and k=|A intersect B|.

## 2. Exact overlap-commutator theorem

For every ordered pair of the 320 signed candidate events:

| overlap k | defect D cycle type | frame products equal? |
| --- | --- | --- |
| 0 | identity | yes |
| 1 | one nonidentity 3-cycle | no |
| 2 | product of two disjoint transpositions | no |
| 3 | identity | yes |

This is an if-and-only-if criterion: two candidate event frames commute precisely when their axis supports are disjoint or identical. The 12 signed port directions still matter to the complete BRC provenance and V29 counts, even though the S6 commutator cycle type depends only on unsigned support overlap.

**Proof.** For k=0 the cycles are disjoint. For k=3 both a and b belong to the same order-three cyclic subgroup on their common support. For k=1 or k=2, simultaneously conjugate by a permutation of the six axis labels so that a=(0 1 2). For k=1 we may take b=(0 3 4) or its inverse; for k=2, b=(0 1 3) or its inverse. There are two possible orientations for a and two for b. Evaluating the four group commutators in each of these representative families gives a nontrivial three-cycle for k=1, and a product of two disjoint transpositions for k=2. Conjugation preserves cycle type. The finite representative check covers all possible support pairings and both event orientations. The port signs do not enter the definition of a or b. Thus the table holds for every pair. QED.

Example, with a=(0 1 2): if b=(0 3 4), D=(0 1 3); if b=(0 1 3), D=(0 1)(2 3). In both examples the two event schedules have the same full nonnegative directed PASS histogram but distinct final candidate frame.

## 3. Exhaustive multiplicity, image size, and reconstruction scope

There are 20 unsigned three-axis supports. For a fixed support A, the number of choices of the other support B with overlap k=0,1,2,3 is 1,9,9,1, by C(3,k)*C(3,3-k). Each support pair has four oriented cycle pairs. Therefore the 40^2=1600 ordered oriented increment pairs have overlap counts (80,720,720,80). Each increment corresponds to exactly eight independent signed-port choices, so each frame-pair occurs with multiplicity 8^2=64 among the 320^2=102400 signed-event pairs.

| overlap k | signed ordered event pairs | exact D image | multiplicity of each distinct D |
| --- | ---: | ---: | ---: |
| 0 | 5,120 | identity (1) | 5,120 |
| 1 | 46,080 | all forty 3-cycles | 1,152 |
| 2 | 46,080 | all forty-five double transpositions | 1,024 |
| 3 | 5,120 | identity (1) | 5,120 |
| total | 102,400 | 86 distinct elements total | — |

For k=1, existence of a nontrivial 3-cycle witness and invariance of the full pair population under simultaneous S6 conjugation show that all 40 three-cycles occur equally often. For k=2 the same argument yields all 45 double transpositions equally often. Their multiplicities follow by dividing 720 oriented pairs by 40/45 and multiplying by 64 source-sign lifts. No floating approximation is used. Under an *additional optional* uniform sampling of the 102400 ordered source pairs, identity, three-cycle, and double-transposition probabilities are respectively 1/10, 9/20, 9/20.

**Observer theorem (strict scope).** For the specific observer "conjugacy class of the reordering defect of exactly two R761 candidate events", the scalar overlap k is exactly sufficient. It can be coarsened to the three labels k in {0,3}, k=1, k=2 without changing that observer. For the *exact rooted S6 defect*, k alone is insufficient: when k=1 there are 40 possible values and when k=2 there are 45. Full signed branch/port identity is retained for any later provenance-sensitive or V29 occurrence observer. This is a horizon-typed BRC quotient, not permission for broader source collapse.

## 4. Reproduction

Run the companion Python 3 standard-library source R762_TRIADIC_OVERLAP_VERIFY.py. It enumerates each of the 320 signed source events, all 102400 ordered event pairs, exact cycle types and directed PASS ledger additivity, independently regenerates the 40^2 unsigned orientation-pair table, and asserts exact class sizes and uniform defect-image multiplicities. R762_TRIADIC_OVERLAP_EVIDENCE.json stores the exact deterministic outcome and scope. The algebraic proof and exhaustive finite verification apply to the declared model, with no physical time evolution, V39 holonomy or external trigonometric computation.

## 5. Research frontier

The result supplies a discriminating swap experiment for a future genuine native Cell/Link/Port triad scheduler: if the scheduler preserves the three-PASS batch and realizes the declared S6 three-cycle, two same-Cell triads overlapping in exactly one or two axes have an observable order residual despite identical final directed PASS counts. First establish an actually Source-admitted P000 force event, whether its update is this candidate's batch, and its genuine relation to V29 and V39. A different admitted update must be tested on its own terms. Keep immutable frozen science and the distinct R757 V39 S3, R760 S7, and R761 S6 frame carriers separate.