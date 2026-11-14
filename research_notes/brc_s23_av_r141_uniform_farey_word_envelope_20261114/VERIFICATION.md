# R141 verification and provenance

Date: 2026-11-14 Asia/Shanghai. Status: exact finite computational checks; author-side analytical proof in PROOF.md remains NOT_REVIEWED.

## Full finite coverage executed in this research turn

An exact Python integer enumerator, adapted from R140's \`word_and_gap_records\`, generated all Farey-adjacent open-slope cells of order \(m\), their consecutive intercept gaps, and their binary words for **every** integer \(5\le m\le64\). For each word, it checked:

1. The existence of an order-\(m\) Farey-gap representation with one neighboring denominator \(q\le m-3\), except for the two words \(10^{m-2}1\) and \(01^{m-2}0\).
2. The complete minimum over the exact R139 gap-permanence cutoffs \(T_g=\max(2,bd-D_g+2)\).
3. Equality \(\max_w\min_g T_g=(m-2)^2+1\) and equality for both extremal words.

The executable reproducible version is \`check_r141.py\`, derived from R140's published exact checker. The in-turn run used unbounded Python integer calculations, not floating point.

**Result:** \`R141_FAREY_SUPPORT_PASS\`.
- Lengths: 60 (all \(m=5,\ldots,64\)).
- Distinct word records summed over lengths: **466,474**.
- Farey intercept gap records: **1,370,486**.
- Low-denominator exception words: **120**, precisely two at each length.
- Additional independent prefix-count rational-interval checks: **832** word records, all \(m=5,\ldots,12\), passing the exact reduced-denominator support criterion.

Selected rows:

| m | F_m | Exceptional words | U_rep |
|---:|---:|---:|---:|
| 5 | 24 | 2 | 10 |
| 6 | 36 | 2 | 17 |
| 7 | 54 | 2 | 26 |
| 10 | 136 | 2 | 65 |
| 20 | 944 | 2 | 325 |
| 40 | 6,980 | 2 | 1,445 |
| 64 | 27,834 | 2 | 3,845 |

The new **all-\(m\)** conclusion is supported by the Farey-denominator classification proof in PROOF.md, with the exact small case \(m=5\) checked exhaustively. The finite tests serve as regression evidence rather than an inference to infinity.

## Exact scientific and authority scope

Scientific source pin (unchanged): \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Related predecessor research: R137B (word-gap correspondence), R138 (D lower bound), R139 (per-gap cutoff), R140 (finite m=4..64 eventual saturation). The current R141 proof uses the precise predecessor statements, which remain author-side/not independently reviewed.

R141 concerns only the tied-phase external Sturmian S23 observer. There is no proof of equivalence to full signed native X6 trajectories or any claim to a current formal shared-task CLAIM/Result/Review.

Remaining work: prove or refute \(T(m)=(m-2)\lfloor(m-1)/2\rfloor+1\) for **all** \(m\ge5\), beyond the already exact finite range \(m\le64\). It will require a word-level modular covering argument, not just a permanent-gap cutoff.
