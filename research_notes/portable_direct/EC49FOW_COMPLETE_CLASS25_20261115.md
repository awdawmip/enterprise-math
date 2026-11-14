# EC49FOW — Complete class-25 native BRC equivalence and five-observer certificate

Date: 2026-11-15. Frozen science pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Raw frozen input SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e. Scientific context: EC49FOR, EC49FOS, EC49FOU, EC49FOV (draft PR #2437); no change to P000. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Exact finite domain

The frozen original corpus has 94 signed byte-prefix key families, 178850 words, 38169 seven-key configurations, 24 named labels (0..23), named roots 03,05,06,07, and 625 complete named legal-root signatures. C25 is **every** corpus configuration with the exact ordered 24-label legal-root signature of original configuration 25. The exhaustive corpus census gives |C25|=442. Optional labels are (5,7,11,13,15,17,19,21); there are 576 complete legal allocations, 292 reachable named root-subset coordinates per configuration.

For each K, root r and optional subset S, define D(K,r,S) as the exact integer native signed-byte Trie minimum-prefix-cover cost for all mandatory labels of r plus S. Let P(K) be the full ordered 292-vector of D values. For each complete named allocation rho, let T(K,rho)=sum_r D(K,r,S_r(rho)); let T(K) be the ordered 576-vector.

**Theorem (complete C25):** for all A,B in C25, T(A)=T(B) if and only if P(A)=P(B). All 442 configurations yield 344 equivalence classes under **each** vector. The same 98 unordered distinct pairs are equal under both; among 97461 unordered pairs there are 0 pairs with T(A)=T(B), P(A)≠P(B). The equality classes consist of 246 singletons and 98 doublets.

**Finite proof:** P equality implies T equality by the displayed sum. For the reverse implication, enumerate all 38169 configurations and group by the exact ordered signature. Enumerate all 442 members of C25. Build each root's byte Trie, computing minimum cover costs by exact integer min-plus union convolution over named-label masks and downward superset closure; export all 442×292=129064 cost coordinates. For each configuration independently enumerate all 576 legal assignments and sum those four root costs (254592 integer terminal evaluations). Compare the full P and T tuples, not hashes. Both partitions have the same 344 groups and 98 equal pairs. The supplied deterministic checker performs these exhaustive steps from the frozen raw text and full exact CSV. Independent Python byte-Trie recalculation matched all 292 coordinates for each of original configurations 25, 27676, 33162 (876 independent matches).

## Seven sufficient terminal observations

Let optional-label order be (5,7,11,13,15,17,19,21). Order legal root choices ascending and enumerate their Cartesian product in Python itertools.product order. Seven **zero-based** allocation indices

[390,477,547,107,137,110,182]

have the following root choices, in optional-label order:

- 390: (07,06,07,06,07,07,05,03)
- 477: (07,07,05,07,05,07,03,03)
- 547: (07,07,07,07,05,06,07,06)
- 107: (05,06,07,06,07,07,07,07)
- 137: (05,06,07,07,07,07,03,07)
- 110: (05,06,07,07,05,06,03,07)
- 182: (05,07,05,07,05,06,03,07)

These seven terminal costs distinguish all 344 different full terminal profiles. After greedy selection, exact numbers of still-colliding unordered profile pairs are 1253, 68, 12, 4, 2, 1, 0. Consequently for all A,B in C25, **equality of these seven terminal costs already forces P(A)=P(B)**. Seven is sufficient; minimality is an open optimization question.

## Evidence and verification

Original input SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e.
Full rooted-cost CSV SHA256: 5c13bd57d909c05ce3cc3e36cb101cc9dde025fb68c6f891f68718c9d5cc9a49.
Machine results SHA256: c1826586486064fbf6bec65453d35f8075831532e50d0e783aefbd3e205d08b8.
Seven-observer certificate SHA256: 1336e88c545392ce4170e710983de35787e92146c87b191fed2441ab02102cf1.

Reproduction bundle, independently stored as EC49FOW_COMPLETE_CLASS25_EVIDENCE_20261115.tar.xz, contains all frozen input bytes, root-profile CSV, C++17 generator, two Python exhaustive checks, results, logs and SHA256 manifest; archive SHA256 4672aff83b11f1540c6b2e10283059daa04ecc27e23a293fae501db5eeaf075c. The GitHub scripts in this branch record sufficient verification details; original corpus and the full CSV are included in the separately supplied portable evidence archive.

This is a class-complete finite result. The three nonzero native root-constant gauge pairs in EC49FOR belong to other named legal-root classes and remain valid.

**Next problems:** find a smaller separating set or a rigorous lower bound for the minimum; complete other legal-root classes (notably representatives 0 and 1, whose local exports remain partial); search for root-cost perturbations dependent on demand subsets that still cancel for all complete allocations.

Publication of this report is evidence preservation only; Activity, immutable Task/CLAIM, formal Result, Review and mathematical admission are separate control operations.

## Stronger exact certificate — five terminal observations (2026-11-15)

A second exact search reduced the sufficient fixed-observation set from seven to **five** complete root assignments. Optional label order remains (5,7,11,13,15,17,19,21). Five zero-based Python Cartesian-product indices are **[477,107,137,110,367]**, with root assignments respectively:

- 477: (07,07,05,07,05,07,03,03)
- 107: (05,06,07,06,07,07,07,07)
- 137: (05,06,07,07,07,07,03,07)
- 110: (05,06,07,07,05,06,03,07)
- 367: (07,06,07,06,05,06,07,06)

On all 344 distinct full 292-coordinate root profiles in C25, after each of the five observations the numbers of colliding unordered class pairs are exactly **[1340,99,29,13,0]**. Thus equality of these five integer terminal costs implies equality of all full root-cost coordinates for any two original configurations in C25. The independently executable check is experiments/EC49FOW_VERIFY_FIVE.py, which imports the frozen-data loader from experiments/EC49FOW_VERIFY_CLASS25.py. Five is sufficient; optimality/minimality remains open.

**Complete revised evidence bundle (V2):** EC49FOW_COMPLETE_CLASS25_EVIDENCE_V2_20261115.tar.xz, SHA256 **a815df445b747ef79de000499ec3eae484d157a4f0e867ed67f059c52d0de0b2**. Includes the pinned original input bytes, all 129064 exact root-cost CSV rows, full paper, C++17 source, both Python exact verifiers, five- and seven-observation certificates, logs, and checked manifest. Original V1 bundle remains separately available as historical evidence.
