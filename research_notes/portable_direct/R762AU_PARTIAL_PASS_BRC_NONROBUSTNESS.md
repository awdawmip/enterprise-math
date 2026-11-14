# R762AU — V29 partial-PASS microsteps break the eventual V17/BRC selector

Date: 2026-11-15. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Researcher provenance: EM-X6-3050F6. Status: author proof and exact integer-BRC verification, NOT_REVIEWED. Frozen P000 scientific input: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This is a conditional V23/V25/V27 selector calculation with actual V29 count-update semantics, not a newly admitted force law.

## Problem and exact model

R762AT established a stable unique successor relation for completed triadic PASS macros when n>=15. We ask whether an active-frame selector can see the V29 ledger *between* the three constituent PASS events without changing its eventual successor relation.

The 20 active triads are all S subset {0,...,5}, |S|=3. Define the V23 four-field parity code c(S) using four perfect matchings:
(01)(23)(45), (02)(14)(35), (03)(15)(24), (04)(13)(25).
For a matching of three ordered pairs (a,b), c=0 unless S contains exactly one of each pair; otherwise c=(-1)^(number of selected second endpoints). Each triad has exactly nine neighbors T with |S intersect T|=2.

Use V29's *nonnegative cumulative* M,Rin,Rout: Rin=(0,0,0,10), Rout=(2,4,3,0). The completed macro executes PASS(0->1), PASS(1->2), PASS(2->0). After n complete macros and a subset e=(e0,e1,e2) of the next macro, n is any nonnegative integer and e_i in {0,1}. The only nonzero M entries are M01=n+e0, M12=n+e1, M20=n+e2. Mask m=e0+2e1+4e2 is from 0 to 7, covering all intermediate subsets under any of the six event orders.

V29's actual definitions I=M1+Rin, O=M^T1+Rout, u=I-O, Omega=M-M^T give

    u=(-2+e0-e2, -4+e1-e0, -3+e2-e1, 10),
    Omega=n Omega1+e0(E01-E10)+e1(E12-E21)+e2(E20-E02),

where Omega1 has +1 on (01),(12),(20), -1 on reverse edges, zero elsewhere. The conditional successor score is
    Phi(n,m;S,T)=u.c(T)+c(S)^T Omega c(T).
For any rational rho>1, the positive Weighted-BRC branch weight W_rho=rho^Phi has precisely the same maximizing neighbors as Phi. The signed differences are contrasts, not signed-amplitude cancellation.

## Theorem AU1 — exact stable relations for every microstep phase

Let F(n,m;S) be the *set* of maximizing neighbors, retaining ties. For each of the eight masks there is a least N_m such that the 20-state relation F(n,m;.) is constant for all integers n>=N_m. Exact exhaustive affine-coefficient certificates give:

| Mask (bits e2e1e0) | sharp N_m | permanently tied states | states with eventual successor set different from completed macro m=0 |
|---|---:|---:|---:|
| 0 (000) | 15 | 0 | 0 |
| 1 (001) | 16 | 1 | 1 |
| 2 (010) | 15 | 1 | 2 |
| 3 (011) | 15 | 2 | 2 |
| 4 (100) | 15 | 1 | 2 |
| 5 (101) | 16 | 2 | 2 |
| 6 (110) | 14 | 3 | 3 |
| 7 (111) | 14 | 0 | 0 |

For every n>=16 there are exactly seven distinct current successor relations among the eight phases. Only masks 0 and 7 are equal: mask 7 at n coincides with mask 0 at n+1 and both have the same stabilized map. Every other mask gives a distinct relation. Therefore the complete-macro deterministic R762AT successor map is not invariant under arbitrary partial-PASS observation, however many complete macros have already occurred.

## Theorem AU2 — an all-n one-event preference reversal

At source triad S=145, compare the two valid target triads 014 and 245:

| Phase | Phi(S,014) | Phi(S,245) |
|---|---:|---:|
| Mask 0 (completed macro) | 3 | 4 |
| Mask 2 (only PASS(1->2) in the next macro) | 4 | 3 |

These exact scores are *independent of n*. For all n>=15 the unique m=0 winner is 245, while for all n>=15 the unique m=2 winner is 014, checked against all nine neighbors. A single legal V29 PASS changes the preferred active-triad successor at arbitrarily large n. In addition, for m=1, S=013 retains the exact tie {012,034}; for m=6, S=023 retains the triple tie {012,035,234}. No tie may be silently replaced by lexical selection.

## Proof of AU1 for unbounded integer n

Every one of the 8*20*9=1440 scores has the exact affine form Phi(n,m;S,T)=a(S,T)*n+b_m(S,T), with integer a,b. For each mask and source triad, find the lexicographically greatest (A,B) among the nine pairs (a,b) and define L to be all candidates with pair (A,B). For each nonmember T, either da=A-a(T)>0, or da=0 and db=B-b(T)>0. When da>0, the champion beats T strictly exactly for integers
    n >= max(0, floor(-db/da)+1).
When da=0, it beats T for all n. Take the maximum of these thresholds over all 20 states and nonmember candidates. The verifier computes the eight stated values N_m, confirms all L remain exactly the maximizer sets at n=N_m, and exhibits a differing set at n=N_m-1, proving sharpness. It also exhausts all 28 mask pairs to establish that only (0,7) share an eventual successor relation. The finite enumeration is a *complete affine-coefficient certificate* for all integer n above the thresholds, not a finite-horizon extrapolation.

## Observation, sources and next scientific question

The count ledger is additive, but active-triad update after each dependent event can read its intermediate state. Consequently, an autonomous scheduler must establish when a triadic macro is atomic versus sequential and what observer it exposes. Under the current-only 20-state successor observer, the eight phases give seven eventual classes; this is not yet a future-operation-safe quotient for arbitrary subsequent PASS histories. Retain event order, source-port identity and branch multiplicity until a full observer/future-operation proof permits compression.

The result advances the specific P000 task's force-closure/scheduler dependency: obtain one P000-admitted signed-force TRIADIC_CLOSURE_E Cell/Link/Port event and decide whether its three PASS channels are an atomic barrier, independent events, or sequential steps. Then establish the actual V17 frame-to-port action and V39 based-loop observer. No new P000 axiom, native rate, physical calibration, or theorem promotion is asserted.

Sources:
- Frozen scientific input: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389; taskbook research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md.
- V29 research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md (Git blob 6849ebd3fc776fb7da3b46627376490aba3dad99).
- V17 research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md (Git blob 42b810a8f82c504833027da17884cc4fb2943e5b).
- V27 research_notes/X6_ATOMIC_TRIADIC_PASSAGE_DRIVES_ODD_HOLONOMY_V27_20260906.md (Git blob c5a02e6727dfc1f70ae4594c3ee807d1760c0be9).
- R762AT immutable author proof: enterprise-math@892e804f8843f7b23bcfc383bd711e599b577819.

Verification: run Node.js standard-library file R762AU_MICROSTEP_BRC_VERIFY.js, which computes a full JSON certificate. Exact integer score semantics; 20 triads, nine neighbors each, all eight phase masks, all integer n by affine proof. The author checker passed locally on 2026-11-15. Independent review remains open.


## Theorem AU3 — the odd six-cycle survives every partial PASS phase, and is a global eventual attractor

There is a much stronger invariant inside the phase-sensitive successor relation. Define the ordered six-state orbit

    012 -> 123 -> 234 -> 034 -> 035 -> 025 -> 012.

For **every mask m=0,...,7** and **every integer n>=2**, each of these six source states has exactly its displayed next state as a *unique* maximizing neighbor. This uniform lower threshold 2 is sharp: at n=1, for instance, mask 1 and source 123 have a tie between 012 and 234 (while the displayed successor is 234).

Moreover, for any integer n>=16, form the union G of all eight mask-specific successor relations. Its unique directed cycle/recurrent strongly connected component is exactly the six-state odd-holonomy orbit above; its induced subgraph on the other 14 states is a directed acyclic graph. Every directed path from an exterior state enters that six-cycle in **at most three moves**, and this bound is sharp. One three-move witness is

    145 -> 245 -> 024 -> 234.

Consequently, even if the selector reads the V29 count ledger at arbitrary intermediate phases and the phase mask changes adversarially between active-triad decisions, **as long as n stays >=16**, all successor choices enter the same odd V17 orbit within three decisions and then follow it uniquely. This holds for a sequential schedule with nondecreasing completed-macro count n, because all eight successor relations have stabilized by n=16. It does not require globally deterministic transient behavior.

**Proof.** For each of the 6 cyclic states, each of 8 masks and all 8 competing neighbors, take the exact difference of its designated successor's affine score and the competitor's. Its coefficient of n is nonnegative; zero-slope differences are strictly positive. Taking the same exact strict affine threshold maximum as in AU1 gives precisely 2, with a tie witness at 1. For the union graph, enumerating the 20*8 current successor sets at n=16 produces 27 directed edges. All six recurrent vertices have only their designated cycle edge, while the other 14 admit no directed cycles and all directed paths have at most two edges wholly outside the cycle; the next edge enters it. The executable checker performs both exact certificates, including a no-exterior-cycle recursion and the three-move witness. The V17 holonomy of this preserved cycle is the already established transposition (2,1,0), hence odd, under the published shared-axis replacement transport law.

This yields a useful separation: partial V29 ledger updates permanently alter the *transient* branching relation (AU1/AU2), yet they preserve the *recurrent* odd frame transport over the stated range (AU3). For the actual native program, the outstanding task is to establish the permitted Cell/Link/Port event and whether the V17 internal-frame update consumes this same phase-dependent selector; the theorem is exact under the declared conditional event language.
