# R284FW — Parameter-uniform second-edge obstruction for the eleven R284FV frontier families

Date: 2026-11-23 (Asia/Shanghai).
Role: informed portable TASK_RESEARCH, unshared mathematics.
Status: AUTHOR_PROVED_CONDITIONAL_FAMILY_LEMMA / EXACT_SMALL_CERTIFICATE / NOT_INDEPENDENTLY_REVIEWED.
Parent: R284FV and the frozen R284CO scientific lineage. This is a binary four-phase observer-model result, not an alteration of P000, Heartbeat X6 or project worldview.

## Exact statement

Let q>=2 be an integer, u=1, A=2q+5, B=2q+3. As in R284FV, normalize the phase-0 codeword to zero and count the seven nonconstant column types by their phase-(1,2,3) bits, with indices 1,...,7. In particular p=5 has phase sequence (0,1,0,1), while p=6 has (0,0,1,1).

Consider the following **eleven explicitly specified families** of seven-type histograms (x1,...,x7), with n=4q+8 for F0, and n=4q+9 for F1--F10:

    F0  (0,0,0,0,A,B,0)
    F1  (0,0,0,0,A,B,1)
    F2  (0,0,0,0,A,B+1,0)
    F3  (0,0,0,0,A+1,B,0)
    F4  (0,0,0,1,A-1,B,1)
    F5  (0,0,0,1,A,B,0)
    F6  (0,0,1,0,A-1,B,1)
    F7  (0,0,1,0,A,B,0)
    F8  (0,1,0,0,A-1,B,1)
    F9  (0,1,0,0,A,B,0)
    F10 (1,0,0,0,A,B,0)

**Theorem (uniform prefix obstruction for these families).**
For every q>=2 and every ordering of bit-write attempts on the non-atomic phase-1 to phase-2 publication edge, at least one prefix admits a physical read within Hamming distance <=1 of a valid stable phase-0 or phase-3 read, under legal per-edge omission histories and at most q omitted attempts. In particular, none of F0--F10 can satisfy the full no-third-phase-observation protocol.

This proves an all-q statement **for the eleven families**, not an all-q classification of every possible histogram. R284FV established by exhaustive enumeration that these families exhaust the relevant first-edge survivors for q=7,...,10; its finite classification has not yet been replaced by a uniform analytic stable-cut classification. Consequently the unrestricted conjecture n_min(q,1)=4q+10 for every q>=2 is NOT claimed as newly proved here.

## Small-prefix barriers

Let a and b be counts of attempted updates of p=5 and p=6 along the 1->2 edge. F8--F10 have one further update of p=2 or p=1; denote its attempted count c in {0,1}. The following barriers must be intersected on every monotone integer count path from the zero prefix to all attempted updates.

| Families | Forbidden count prefixes (for each c=0 or 1 when present) | Number of concrete barrier nodes |
|---|---|---:|
| F0, F4--F7 | (a,b)=(3,0), or (a,1) with 0<=a<=2 | 4 per family |
| F1, F3 | (a,b)=(4,0), or (a,1) with 0<=a<=3 | 5 per family |
| F2 | (a,b)=(3,0),(3,1), or (a,2) with 0<=a<=2 | 5 |
| F8--F10 | c=0 or 1, and (a,b)=(3,0), or (a,1) with 0<=a<=2 | 8 per family |

Total: 59 concrete forbidden prefix states, distributed over eleven families. The barrier property is elementary: a path either raises b to the stated threshold before a reaches its threshold, or reaches the a threshold while b is still below its threshold. An optional single c-update cannot evade these barriers because both c=0 and c=1 are covered.

## Exact base check at q=2

At q=2, A=9 and B=7. For each of the 59 nodes, enumerate all possible missed attempted writes at that prefix, subject to total misses <=2. For each resulting successful-write count vector use R284FT's exact integral prefix-flow oracle (reproduced in the existing R284FV_prefix_count_lattice.py) for i=1, target=2, and j in {0,3}. The minimum distance from a legal actual prefix state to the set of legal stable phase-j states is <=2 for at least one such missed-write assignment and j. Therefore the two radius-1 read balls intersect, and a phase-j output is forced at that physical observation. This is already a prohibited third-phase output.

This is a fixed finite verification, independent of any q-large enumeration. A companion checker enumerates all 59 witnesses and verifies a count-lattice cut, importing the existing exact-flow implementation rather than replacing its mathematical oracle. Executing the checker at q=2,3,7,13 returned:
- 11 families, 59 forbidden prefix nodes, and 47 non-barrier-reachable nodes, with every assertion passing in each run.
- These later q checks are regression evidence; the all-q quantifier rests on the lifting lemma below.

Reproduce from research_notes/portable_direct:

    python3 R284FW_uniform_prefix_barrier.py

## Lifting lemma: from q to q+1 without increasing third-phase distance

Fix one of the eleven families, a forbidden attempted prefix (a,b,c), and a witness pair consisting of a legal actual phase-1 prefix word and a legal stable phase-j word for j=0 or j=3, at a particular q>=2. Increase q by one. The new histogram adds exactly two columns of type p5 and two of type p6. Keep the original prefix attempts, their outcomes, and both original physical states unchanged on existing columns; perform no prefix attempts on the four added columns.

**Case j=0.** Phase 1 and phase 0 disagree only on type p5 among the two expanding groups. On one new p5 column, make the phase-1 stable value 0 by omitting the 0->1 update on edge 0, and leave phase-0 value 0 correct. On the other new p5 column, retain phase-1 value 1 correctly, and make the phase-0 value 1 by omitting the 1->0 update on edge 3. Thus the new p5 columns agree across the witness pair. Set both added p6 columns to their correct common value 0. No individual history edge has acquired more than one additional omission.

**Case j=3.** Phase 1 and phase 3 disagree only on type p6 among the expanding groups. On one new p6 column, make the phase-1 value 1 by omitting the 1->0 update on edge 3, matching the correct phase-3 value 1. On the other, leave phase-1 value 0 correct and make phase-3 value 0 by omitting the 0->1 update on edge 1, again matching. Set both added p5 columns to their correct common value 1. Again at most one new omission is assigned to any edge of either history.

All omissions are allowed by the reset-free multi-generation model; witness histories on the two sides may be chosen independently. The new observation pair has exactly the same Hamming distance as before, and every edge's omission count remains <=q+1. The two read flips are unchanged. Iterating extends every q=2 barrier witness to all integers q>=2, with its attempted prefix counts unchanged. The 59 finite barriers therefore obstruct every publication order for all q>=2.

The proof intentionally preserves omission provenance by original edge; combining four independent edge budgets into a single ordinary Hamming ball would not justify this lift. No native X6 geometric identity or BRC arithmetic interface is invoked by this auxiliary binary observer lemma.

## Validity, existing evidence, and next step

- Base oracle: R284FT exact integral-flow prefix-distance theorem; R284FV_prefix_count_lattice.py at the current pinned research lineage.
- Parent finite classification: R284FV_Q7_Q10_U1_GLOBAL_SHARP_CAPACITIES_20261123.md. This work does not re-run or expand the historical 120-million-histogram scan.
- Checker: research_notes/portable_direct/R284FW_uniform_prefix_barrier.py (self-contained family/barrier logic, reusing prior flow).
- Author-level proof and exact checks; formal Result and independent mathematical Review remain separate and absent.
- Remaining principal obligation: prove *uniformly in q* that the complete distance+six-stable-cut+first-edge survivor histograms for n=4q+8, 4q+9 reduce to F0--F10 for all q sufficiently large, or identify a new histogram outside this list. Only after that classification is established may this lemma be combined with the existing 4q+8 lower bound and 4q+10 Gray construction to claim the unrestricted theorem.
