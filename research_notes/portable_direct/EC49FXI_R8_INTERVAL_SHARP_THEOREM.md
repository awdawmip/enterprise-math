# EC49FXI — Exact r=8 consecutive-phase two-channel observer theorem

Date: 2026-11-23 (Asia/Shanghai). Frozen scientific pin **BRC16943**, unchanged. Immediate predecessor EC49FXH (PR #2979, proof at `e267dbb78e33365e1303f5039fc9797ae7ff0412:research_notes/portable_direct/EC49FXH_R7_INTERVAL_SHARP_THEOREM.md`), and inherited exact auxiliary sensor reduction EC49FWT–FXG.

## Theorem

In the same 110-periodic P10/one-hole auxiliary Farey–CRT observer with known reference, complete separately indexed reflection spectra, two separately counted Boolean bits per physical activation, and relative phase d in D_k={0,...,k-1} for 1<=k<=55, require fixed-sample channel-bit Hamming distance at least 8. Then the exact minimum number of physical activation sites is:

    N_fixed(D_k;8) = 23 (k=1,2); 24 (k=3,4); 25 (k=5,...,55).

Distance 8 permits correction of three unknown channel-bit errors and one additional known channel-bit erasure simultaneously. Whole two-bit activation errors are a different metric.

## Lower bound: integer multiplicity alone closes all k

Use the exact inherited criterion F_S(d,i,j)>=8 for all d in D_k, mod5 color i and missing mod11 column j, where

    F_S(d,i,j) = sum_{t in S} (1_{t%5=i, t%11!=j} + 1_{(d-t)%5=i, (d-t)%11!=j}).

Let m_i=number of activated sites of residue i modulo5. Before deleting column j, the row has n=m_i+m_(d-i). Summing the deleted contributions over the eleven j gives n; when the required distance is 8, n is positive and at least one column deletes >=1, so n>=9. Summing five rows i at any fixed d gives 2|S|>=45 and |S|>=23.

If k>=3, the self-reflection phases d=0,1,2 respectively force m_0,m_3,m_1>=5 because n=2m_i>=9. In the d=1, i=2 row, m_2+m_4>=9. Hence |S|=m_0+m_1+m_3+(m_2+m_4)>=24.

If k>=5, the five phases d=0,1,2,3,4 include self-reflection d=2i mod5 for each color i. Every m_i>=5; hence |S|>=25.

## Explicit optimal activation sets

- For k=1,2, select S_23={3,4,...,25} (23 physical sites).
- For k=3,4, select S_24={3,4,...,26} (24 physical sites).
- For k=5,...,55, select S_25={0,1,...,24} (25 physical sites).

For S_25, every mod5 color occurs exactly five times in five distinct mod11 columns. Each of the two channels in every CRT row loses at most one bit under deletion, so F>=10-2=8 for all d,i,j.

For the four small phase rows, direct modular enumeration yields the following *exact minima over the eleven missing columns*, with columns listed for i=0,...,4:

| Activations | d=0 | d=1 | d=2 | d=3 |
|---|---|---|---|---|
| S_23 | (9,8,8,8,8) | (8,8,8,9,8) | — | — |
| S_24 | (9,9,8,8,9) | (9,9,8,9,8) | (8,9,8,9,9) | (9,8,8,9,9) |

These tables are verified directly using only integer mod5/mod11 comparisons in the attached standalone code. They prove F>=8 in every small permitted row, closing the upper bound. Combining the matching lower and upper bounds proves the theorem.

## Source / verification / status

The program enumerates all 55 consecutive phase sets, 5 colors and 11 missing columns per phase: 84,700 exact inequalities, all passed. It emits all 55 site sets, the minimum row distances and the small-case tables. Scientific status **AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**. Reuse the frozen predecessor reduction; this auxiliary sensor theorem does not establish genuine same-anchor Farey reachability, X6 dynamical adequacy, or an independent Review.

The original six-axis P000/ACTIVE ontology, joint-relation/composite observation directions, signed provenance, height, anchor, CRT/carry and causal residual remain typed and untouched. No new formal Task CLAIM/Result is asserted.

**Next:** derive fixed activation-symbol distance for corruption/erasure of an entire two-bit hardware activation, and then compare reachable relative phase sets in native same-anchor Farey dynamics with auxiliary D_k.
