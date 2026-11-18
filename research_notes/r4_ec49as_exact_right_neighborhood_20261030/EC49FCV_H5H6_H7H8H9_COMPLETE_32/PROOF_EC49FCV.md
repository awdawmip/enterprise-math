# EC49FCV — exact 32-group H5:16/H6:1 mixed-late five-path exchange

Date: 2026-11-07 Asia/Shanghai. Status: AUTHOR_FINITE_EXACT_PROOF / DUAL_REPRESENTATION_EXECUTED / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Reused `frozen_model.py` Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`; reused bitset program `VERIFY_EC49FCS_EARLY2_H7H8H9.py` Git blob `6403b576ea415646d80aa8971d75a7facc20af85`. Both are in the existing `EC49FCS_EARLY_H4_H5_LATE_H7_H8_H9_256/` directory of this research branch. Parent: EC49FCU commit `1e0218058619e446498908d29a71944e0960d700`.

## Finite theorem

Preserve the original 24 witness slots, frozen nine-state observer, literal ordered signed native-step prefixes, and BRC multiset cache keys L=(4,2,1) at H2–H5 and M=(7,3,2) at H6–H9. Replace simultaneously slots `5:16`, `6:1`, one slot from each `7:{1,2,4,8}`, `8:{1,2,4,8}`, and `9:{16,32}`, holding the remaining 19 witness words fixed. For **all 4×4×2=32 selections**, the minimum among all legal replacement words is **exactly 158 distinct nonempty signed primitive-step prefixes**. These are global group indices **992–1023** in `combinations(early,2)` followed by `product(s7,s8,s9)` as defined by the frozen model.

## Proof and exact computational coverage

Let P(w) be every nonempty literal ordered signed primitive prefix of legal word w, and F the union of prefixes from the unchanged 19 words. The candidate generator exhaustively permutes the specified length-h operator multiset subject to the pinned trap-avoiding nine-state automaton and terminal signature. Put R_i(w)=P(w)\\F, c=158-|F|. A strict improvement exists exactly when a five-way choice has `|R_1∪...∪R_5|<c`. The unchanged witness gives the feasible 158-edge upper bound.

Filter candidate residuals of cardinality >=c; such a residual cannot occur in an improving union. Keep only inclusion-minimal residual sets in each candidate pool and intermediate union state. This is exact because A⊆B implies A∪T⊆B∪T for every future completion T. For remaining pool j let I_j be the intersection of every option in that pool; every completion contains I_j. Therefore a partial union U can be discarded if `|U∪(⋃_{j>i}I_j)|>=c`. The last-stage strict-improvement antichain is empty for **all 32**. None of these operations can remove an improving solution; hence the optimal value equals the original 158.

Actually executed the unchanged integer-bitset checker in completed, disjoint batches: indices `992`, `993`, `994`, `995–999`, `1000–1023`. The published checker also independently ran its original literal mode on 992 and 1000–1023. Separately executed this directory's new `VERIFY_EC49FCV_LITERAL_SUFFIX.py` for all 32 with `frozenset[str]` signed-prefix labels (no integer bit positions), its own minimal-antichain routine, and the proved mandatory-suffix bound. Exact results agreed **32/32** on selected slots, |F|, strict cap, all option and stage antichain counts, total union checks, and the absence of a better construction. This cross-check is independent at the representation level; both representations intentionally share the original frozen candidate generator.

The lossless `EC49FCV_ALL32_EXACT.json.gz.b64` includes every original row and both representations. Base64-decode then gzip-decompress into UTF-8 JSON; SHA256 of decoded JSON is `4aeb5acf7701a0fe773b0f71175197393cccd0cde5fa5d7a75d78c67ecc619be`. Totals: 32/32 exact optimum 158; **1,930,268** executed stage-union checks in each of the bitset and literal checkers; maximum intermediate antichain **84**; **30,725,775,360,000** unpruned Cartesian combinations (a mathematical count, NOT actual attempts). All exact integer/set operations, without floating approximation.

Reproduce using the prior published `EC49FCS` frozen-model directory as the working directory:

```bash
python VERIFY_EC49FCS_EARLY2_H7H8H9.py --start 992 --stop 1000 --literal 0 --output bitset_part1.json
python VERIFY_EC49FCS_EARLY2_H7H8H9.py --start 1000 --stop 1024 --literal 0 --output bitset_part2.json
PYTHONPATH=. python ../EC49FCV_H5H6_H7H8H9_COMPLETE_32/VERIFY_EC49FCV_LITERAL_SUFFIX.py $(seq 992 1023)
```

The first bitset command above is only a reproduction recipe; actual runs were completed as smaller bounded batches as stated. Compare output rows with the published lossless certificate.

## Scope and governance

This is a finite signed-native auxiliary BRC observer-language result at fixed keys and pinned 24-slot observer. It does not establish variable-cache-key rigidity, all five-path neighborhoods, six-path rigidity or the nine-window 93-edge mother target. Author-reported five-path cases: 8,220 preceding, +32 disjoint = **8,252**. In the early-two/one-each-late mixed family: 288 preceding +32 = **320/1,440**, leaving **1,120** without these author-side certificates.

The native service status call failed with `BACKEND_IDENTITY_OR_VERSION_MISMATCH` and `operation_sent=false`; the site-local check reported `backend_connected=false`. Current owner / native Researcher session / CLAIM / Source Result were not confirmed. GitHub author-side publication is distinct from formal task/Driver admission. P000 and ACTIVE worldview were read, not modified. Next research unit: `NEXT_EC49FCW.md`.
