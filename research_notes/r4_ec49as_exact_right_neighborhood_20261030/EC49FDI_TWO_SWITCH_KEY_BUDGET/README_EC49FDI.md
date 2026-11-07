# EC49FDI — Exact two-switch full-BRC-key budget frontier, 112 → 96 → 92

Date: 2026-11-07. Classification: AUTHOR_EXACT_FINITE / EXECUTED / UNREVIEWED / NOT_ADMITTED.
Scientific source pin: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Frozen original model source: EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py (Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859).
Predecessor: EC49FDH at ab431005adceba79a62a6954b93e658a8c6faffe.
Canonical source rules and P000 remain unchanged.

## Mother-target audit: the 92-edge witness uses seven full keys

The original H2–H9 signed-X6 seven-operation mother target (see EC49FAM/README_EC49FAM.md and EC49FAW/README_EC49FAW.md) requires **five distinct complete positive BRC cache keys globally**, one full key per horizon, rank nine per horizon, and at most six permitted nine-history observation signatures. The full key counts actual positive signed primitive occurrences on all six axes; every ordered native path, observation label and provenance is retained.

The EC49FDH 92-edge witness uses the fixed four H2/H3 words "fe, ge, feg, gef", with three distinct keys (2,1,1),(3,0,1),(3,1,1), each with trailing (0,0,0). The later horizons use:
H4/H5=(4,2,1), H6=(5,3,1), H7/H9=(6,4,1), H8=(6,5,1).
Therefore its exactly 92 nonempty signed native-prefix edges consume **seven** distinct full keys. It solves the published extended seven-key finite model, while the original five-key mother 93-edge objective is still open. This is a direct path/key audit, not a revision of the numerical 92-edge check.

## Complete binary-switch theorem

Fix H2/H3 original four paths; they contribute exactly 16 distinct nonempty signed primitive prefixes. Use full keys A=(4,2,1), B=(6,4,1), C=(5,3,1), D=(6,5,1), with three trailing zero coordinates. Require H4/H5=A, H7/H9=B, H6 chosen from {B,C}, H8 chosen from {B,D}. Each horizon has its fixed key, all original signature labels, the frozen nine-state DFA, and **the entire legal ordered operation-word candidate language**. Minimize the number of literal nonempty ordered signed-X6 primitive prefixes over the complete 24-label selection.

| H6 | H8 | Total distinct full keys | Exact min edges | Legal candidate words | Trie nodes | Inspected DP pairs |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| B | B | 5 | **112** | 4372 | 26705 | 21972032 |
| C | B | 6 | **96** | 4492 | 25605 | 25909100 |
| B | D | 6 | **106** | 5492 | 31159 | 21984948 |
| C | D | 7 | **92** | 5612 | 30059 | 25815852 |

Thus, within this declared four-case family, the exact optima under at most 5, 6 and 7 distinct complete keys are **112, 96, 92** respectively. In particular, switching H6 alone reduces 112 to 96; then also switching H8 reduces 96 to 92. Total independently executed Python Trie DP state-pair checks: 95,681,932. The existing C++ solver and this independent Python implementation agree in every case. These key-budget observations are structural constraints on this family; the prior author five-key 94-edge mother witness lies outside the four-case family.

## Explicit 96-edge / six-key signed-native construction

All 24 original observation labels are provided, in each horizon's label order:

    H2: fe ge
    H3: feg gef
    H4: gefd fegd fegc gefc
    H5: feggf gefgf
    H6: gefdfg fegdfg feggfc gefgfc
    H7: gefdfgd fegdfgd feggfcc gefgfcc
    H8: gefdfggf fegdfggf feggfcfg gefgfcfg
    H9: feggffggf gefgffggf

The exact verifier independently checks original nine-state observation signatures, horizon lengths, full six-coordinate positive primitive key, complete candidate-language membership and literal signed-native expansion. The union of all nonempty signed-native primitive prefixes contains exactly 96 elements. The SHA256 of its sorted newline-terminated UTF-8 lines is:
dd8c0a68979ee66fc83970d351bea1d65608d00fa46ebbaaa3fb7ec0b9310f69.

For the H6=C,H8=B case, the complete Trie DP finds exactly 80 payable prefixes in addition to the 16 fixed early prefixes. The witness attains 16+80=96.

## Exhaustiveness / reproducibility

For a full cache key (x,y,z), horizon h and original operations a,c,d,e,f,g, legal multiplicities obey:
n_a=z−1; n_e=z; n_c+n_d=x+y−h−1; n_f=h+1−y−2z; n_g=h+1−x.
Enumerate all nonnegative multisets, all orderings and nine-state DFA transitions. For each of the 20 H4–H9 label requirements, include every legal candidate. Expand every operation into the original signed six-axis primitive sequence, build a primitive prefix Trie, and charge each previously unseen primitive prefix once. A min-plus dynamic program at every Trie node tracks precise disjoint subsets of labels supplied by selected words and adds child subtrees while charging one prefix edge for every nonempty child. Bottom-up induction shows the complete recurrence considers each legal one-word-per-label assignment and counts shared prefixes exactly. The frozen H2/H3 prefix set has zero incremental cost, then add 16 at the root. The complete root label mask is 2^20−1. No heuristic sampling or beam cap is used.

Programs: "VERIFY_EC49FDI.py" (independent Python Trie DP and signed-prefix witness checker) and the existing EC49FDG "DP_EC49FDG.cpp" (C++ full-language exact Trie solver). Captured result: "EXACT_REPORT_EC49FDI.json". All four full Python runs and 96-witness checks were executed before publication.

## Next precise unit EC49FDJ

Preserve **five distinct full positive keys**, rank nine per horizon, original 24 labels, at most six observer signatures, frozen primitive expansion and literal prefix cost. Use EC49FAW's 124 rank-feasible two-new-key schedules and the known author-side **94-edge five-key mother witness** as the comparison frontier. Investigate whether any exact five-key schedule admits a 93-edge or smaller signed-prefix cover. Either provide a fully legal <=93 witness or certify the minimum for a declared complete schedule family. Explore independently a key-lifespan lower bound from EC49FAM. The evidence for the four-case family above is reusable but does not close the five-key parent.

## Provenance and authority

Actual connected GitHub actor: awdawmip (admin). Native Enterprise Math request returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. Formal active owner, CLAIM, Source Result and independent Driver verdict were not verified. This is an author-side research certificate, preserving P000 and ACTIVE worldview without changing either.
