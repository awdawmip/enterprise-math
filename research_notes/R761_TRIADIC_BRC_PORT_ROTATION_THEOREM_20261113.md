# R761 — Signed-port triadic BRC candidate, sharp S6 frame generation and exact observer lifts

Date: 2026-11-13 Asia/Shanghai. Mother Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Author: EM-X6-EF6D9D, Activity: RA-524B7D874F4A4A275BCC9734. Classification: new finite model with proved results and complete exact validation; **candidate** native event bridge, not admitted native physics/Source Result/Driver review.

## 1. Fixed foundations and exact sources

P000: 6 native spatial axes E1,...,E6 form a signed Cell torsor X6, with six pairwise native PERP_E relations at 120 degrees. The minimal nonzero primitive stable force population has exactly 3 quanta with TRIADIC_CLOSURE_E; a visible two-force equilibrium must receive a triadic lift. Native force incidence and update remain an open derived question; we never substitute classical Euclidean zero-vector summation for P000.

Current sources:
- definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md and definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md at frozen pin.
- research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md: a local PASS(a->b) increments an integer nonnegative count M[a,b] and gives Du=e_a-e_b, DOmega=E_ab-E_ba.
- research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md: based-loop (j,h) with h in S3; its future language is limited and separately typed.
- R757 PR #2194: three legal V39 macro-packets, not atomic forces. R759 PR #2222 and R760 PR #2225: separate auxiliary S7 rooted-word frame, not the S6 native axis-permutation skeleton.
The later V29/V39/R760 papers are comparison evidence, not a change of the frozen Task science.

## 2. Explicit signed-port branch event and proposed updates

Choose a Cell c in the affine Z^6 torsor as *local anchor*, a positive unit equal force quantum q=1, and 12 signed force-port labels P={(i,s):1<=i<=6, s in {-1,+1}}. A typed event T(c;[p1,p2,p3]) has 3 nonzero source branches each with a distinct native axis index. Its bracket is an ordered cyclic triple, considered modulo cyclic rotation but **not** reflection; signs and branches are distinct recorded data.

Define the candidate TRIADIC_CLOSURE_E predicate on this three-port family, and only on this family in this local model, to be true. Every event has 3 equal quanta on pairwise enterprise-orthogonal axes. This is a concrete sufficient *candidate* realization of the P000 canonical three-force configuration, without asserting that existing native code has admitted its scheduler.

The typed BRC carrier is the complete signed, branch-labeled cyclic port relation. The candidate event is atomic at its own scheduler level but is mapped as a batch of three existing V29 PASS occurrences:
 PASS(c;p1->p2), PASS(c;p2->p3), PASS(c;p3->p1).
Its positive-count increment is DM=E_(p1,p2)+E_(p2,p3)+E_(p3,p1), with no TRANSFER or negative count. The derived contrasts satisfy Du=(e_p1-e_p2)+(e_p2-e_p3)+(e_p3-e_p1)=0 and DOmega=DM-DM^T. Reflection transposes DM, changes DOmega to -DOmega, and does not change Du. Consequently the zero portwise contrast observer has a nontrivial branch fiber with different frame and Omega readouts. No signed cancellation is inferred from positive BRC mass; cancellation is checked in the derived signed contrast.

Write the three distinct axis indices (a,b,d) in the same order as their signed ports. Assign frame increment sigma_T=(a b d) in the already-founded axis-permutation S6 skeleton, fixing the three omitted axes, and update the local decorated frame by permutation composition. At the chosen anchor c, the associated action on relative Cell coordinates is x -> c+sigma_T(x-c). The map fixes the chosen Cell and preserves primitive signed adjacency and L_E^2=sum_i x_i^2. The signs/provenance are carried along with the source-labeled ports; they are not extra spatial coordinates. This is a proposed Cell/Port-to-V29/S6 bridge, NOT an automatic V39 based-loop S3 holonomy.

## 3. Theorem A: exact A6 generated frame group and sharp event depth

For the canonical local unit event population, the number of distinct typed events is

 C(6,3) * 2^3 * 2 = 20*8*2 = **320**.

The 2 orientations for each signed three-port set are inverse cycles. The number of distinct S6 increment permutations is 20*2 = **40** (all three-cycles). Their generated group is **A6**, of order **360**, and its complete shortest event word-length distribution is

 depth 0: 1 identity
 depth 1: 40 three-cycles
 depth 2: 229 states (144 five-cycles, 40 disjoint products of two three-cycles, 45 double transpositions)
 depth 3: 90 states (cycle type (4,2)).

Thus the sharp maximal minimum number of atomic candidate events to produce any generated frame is **3**. No odd S6 rotation can be produced in this model. For one fixed 3-axis support, the subgroup is C3, order 3.

Proof. All 40 increments are three-cycles and hence even. Each possible three-cycle has a signed-port realization; three-cycles generate A6, yielding the exact group equality. The 40 nonidentity increments give precisely depth 1. Two 3-cycles multiply to the indicated nonidentity classes or identity according to their support intersections; in particular no product of two 3-cycles has type (4,2). The 360-element finite group is exhausted by exact BFS of all generators and inverses; enumeration confirms that all remaining 90 even permutations have type (4,2), are reached in 3, and none in 2. This is a fully exhaustive finite certificate, independently reproducible from the companion standard-library Python checker. For fixed support, the two orientations are inverse generators of the same C3.

## 4. Theorem B: exact two-visible-port triadic lift, minimal repair

Define an observer that reports the *unordered* pair of two signed force ports of distinct axes, their unit quantum, and an apparent equilibrium flag inherited from the completed full triadic event. The observer hides the third force and the cyclic orientation. There are C(6,2)*2^2 = **60** different signed-pair observations. For every one:

- exactly 4 possible hidden axis indices, 2 hidden signs and 2 cyclic orientations, i.e. **16 exact typed event lifts**;
- exactly 8 distinct S6 frame increments, each represented by 2 different hidden-sign full events;
- therefore **4 fixed additional bits** are necessary and sufficient to reconstruct the full signed event (within the declared canonical source population), and **3 fixed bits** to reconstruct its S6 frame increment alone.

Proof. The visible two axes and their signs are fixed. The hidden axis may be any of the remaining four; its signed direction may be chosen independently in two ways; reflection chooses either oriented cycle. These choices are distinct source-typed events. The frame sees the hidden index and orientation but not its sign, hence fibers of size exactly 2. The binary bit bounds follow from 16 and 8 equipossible coding alternatives in the worst-case, not from entropy or a prior on events. This lifts an apparent two-force equilibrium to a P000-compatible triple in this **declared candidate observer**; it does not declare a primitive two-force stable configuration.

## 5. Theorem C: exact S6 equivariance

For any pi in S6 relabel each signed force port (i,s) to (pi(i),s), leaving its source branch identity intact. Then the candidate event predicate is preserved; for its frame increment,

 sigma_(pi T) = pi sigma_T pi^(-1).

The three positive directed V29 PASS edges are relabeled by precisely the same permutation. Thus the event incidence, source-order branch carrier, zero Du, signed Omega relation and frame update commute with the known S6 axis-permutation rotation skeleton.

Proof. Pi is a bijection of the six axes, preserving distinctness, signed direction and PERP_E. Cyclic port edges map one-to-one. Conjugation of a cycle sends (a b d) to (pi(a) pi(b) pi(d)). These identities hold for all pi and event T; the checker enumerates all 720*320 = **230400** exact cases.

## 6. Finite validation and precise scope

The exact integer/permutation checker R761_TRIADIC_BRC_PORT_ROTATION_VERIFY.py exhausts all 320 events and checks their signed-port provenance and 3 positive directed PASS counts, 160 orientation reflections, 40 increments, the 360-state A6 group/shortest-depth BFS, 60 observer fibers each of 16 events and 8 frame values, 20 fixed support C3 closures, and 230400 rotation-equivariance pairs. Output R761_TRIADIC_BRC_PORT_ROTATION_EVIDENCE.json records deterministic PASS status, counts and model restrictions.

Only finite source-labelled combinatorics and typed exact BRC incidences were computed. No pi, trigonometry, matrix exponential, Padé/Taylor, floating physical residual attribution, or native dynamics solver was invoked. Observer compression is certified only for the two explicitly declared reconstruction targets. More extensive provenance or future-event queries continue to require their branch data.

## 7. Remaining mother-task interface

The decisive next test is a native, actually admitted P000 force Cell/Link/Port incidence event and scheduler: does it authorize this three-port cyclic batch as one force update, and does its permitted frame effect equal the defined S6 three-cycle? If there is a clash, locate the *first exact* type/admissibility/observer failure and preserve the valid candidate theorem. A separate source-preserving map into V29 PASS/TRANSFER and based-loop V39 S3 can then be studied without identifying S6, S3 and R760 auxiliary S7 by fiat.

The task also needs multi-Cell interactions, larger force-population triadic decompositions, nonuniqueness and BRC source retention. Frozen P000/ACTIVE world and scientific pin are unchanged. Shared mother task has another LEASED owner in the actual native continuation read; this is an independent author-side paper with no new CLAIM, no formal Source Result and no Driver admission.
