# X6 / R063 Stage0 — Lossless polynomial-coefficient validation across 1,820 branches

**Date:** 2026-11-15. **Author:** EM-X6-FB6990, logical research lane chatgpt-research-onhour-enterprise-math-20260923. **Parent:** RS-X6-LEGACY-PLANE-RECONCILIATION, TP2-B4A441B23DA3159232C2. **Status:** AUTHOR-EXECUTED / EXACT FINITE EVIDENCE / UNREVIEWED / NOT_ADMITTED.

## Original source and new question

This unit continues the saved independent R063 512-row digest reconstruction (2026-11-15 21:00), the prior exact wrong-degree polynomial mutation witness (17:00), and the preexisting exact JSON transport-collision audit (07:00, source report at research_notes/X6_R063_STAGE0_JSON_EXACT_INTEGER_TRANSPORT_COLLISION_20261115_0700.md). It tests **semantic coefficient correctness against the actual frozen archived data**, rather than repeating root-set completeness or asserting that the 17 historical native gates were rerun.

Frozen branch: research/r063-stage0-path-valued-sqrt-2500. Loader blob b4e000a6377f2858ae434eb0eecd0c25c33e8592; part02.inc blob b543e185ec415b512c0ca0421616404cc12a19a7; native acceptance gates part04.inc blob a1834a4b39a9d528760e67220b5fe5f368c9e655.

Three actual source artifacts were read as raw UTF-8 through the connected GitHub path:

- research_results/R063_STAGE0/R063_STAGE0_PATH_CARDINALITY_CERTIFICATE.json — blob d4278d6c301587330252ff6683e87773d42cf4e2.
- research_results/R063_STAGE0/R063_STAGE0_COMPONENT_ROOT_FIBER.json — blob fcc8923cf99342650e321d65786cf605a9ac6a07.
- research_results/R063_STAGE0/R063_STAGE0_REPLAY_SUMMARY.json — blob f9d0598dbb410d892b5a03ec00b6baa8b7f1e7ad.

The original archive has 17 acceptance flags set to true. These flags were **read**, not independently re-executed.

## Exact mathematical law

Let u and v commute, and let Xi and Xj be distinct noncommuting native path letters. For nonnegative integers a,b and arbitrary n, the coefficient of u^a v^b in (uXi + vXj)^n is the sum of every **ordered** length-n word with a Xi letters and b Xj letters if n=a+b; otherwise it is identically zero by homogeneity. All distinct words have coefficient one, so the natural positive BRC multiplicity is binomial(a+b,a) in the matching-degree case. This is not signed amplitude cancellation. The word length a+b is not the scalar/native length r.

A strict semantic gate therefore parses the entire coefficient expression, checks its markers against the actual component pair, checks that outer degree equals a+b, and recomputes the exact integer cardinality with a separate combinatorial algorithm. A nonempty certificate hash or self-reported count does not verify this property.

## Direct source-archive observations

The tool-side source read preserved raw JSON integer lexemes before an exact BigInt calculation. All **six** archived N=2500 positive-chart formulas and their cross-artifact root-fiber records agreed with the independent binomial calculation; all **14** archived lexicographic rank/unrank samples were independently recomputed as exact integers and matched their positions, IDs and rank values. Six deliberately wrong-degree (+1) formula mutations were detected.

| Components (a,b) | Exact natural path count |
|---|---:|
| (0,50) | 1 |
| (14,48) | 29078984349975 |
| (30,40) | 55347740058143507128 |
| (40,30) | 55347740058143507128 |
| (48,14) | 29078984349975 |
| (50,0) | 1 |
| **Total** | **110695538274255714208** |

**Previously documented lossless-consumer boundary, independently reconfirmed here (not claimed as a novel finding):** ordinary JavaScript JSON.parse converts the two 55347740058143507128 integer lexemes to binary64 values whose exact integral value is 55347740058143506432, **696 lower per branch**. The archived total converts to binary64 integral value 110695538274255716352, **2,144 higher** than the true total. Independently summing individually rounded branches yields 110695538274255712816, **1,392 lower** than the true total. The two floating pathways disagree by **3,536**. A console's shorter rounded decimal rendering is not the exact integer held in the Float64 value. These errors arise in the **consumer's number representation**; the frozen archived JSON integers are correct.

## Actually executed new checker

A separate exact Python checker, committed at research_checks/X6_R063_STAGE0_POLYNOMIAL_LOSSLESS_1820_CHECK_20261115_2200.py, ran locally with exit code zero and output PASS_X6_R063_POLYNOMIAL_SEMANTIC_GATE_1820. Its committed Git blob is ebefa83cb1779cca669e478cfaee978f5bf55a60 and exactly matches the byte-executed local file (SHA256 b289bd2096416bee55e7fb8bfe87b2f29f463784a0e8c531c835cddd4e2f1ea4).

It uses exact isqrt to define the fixed positive chart's ordered component root population for **all r=1..512**. For all **1,820** root branches it recomputes the noncommuting-word coefficient cardinality by two integer routes (math.comb and Pascal recursion), obtaining **zero disagreements**; it also detects **3,640** independently constructed wrong-degree n±1 formula mutations. At r=50 it matches all six archival integer lexemes and their exact total. The full 512-radius certificate uses canonical decimal-string path counts, never JSON binary64. This is a *new semantic check* of the existing source family, not a repeat of the 512-row C2/C3/C4 hash construction.

The new research increment is the **complete 1,820-branch formal coefficient check, 3,640 detectable degree mutations, and source-archive cross-artifact verification of 14 rank samples**; the binary64 defect is reused prior evidence. The code tests the two-generator **positive sector chart**, not all signed native-X6 Cells or unproved triadic dynamics. An independent 512-case semantic check is not the missing **unchanged original loader + five pinned part files + 17 native gates + 512 same-object regression** execution.

## Connection to active research and next exact action

The authorized runner for issue [#2416](https://github.com/awdawmip/enterprise-math/issues/2416) still needs to execute the frozen original program with --N 2500 --regression-max-r 512, preserve discovery-before-brute phase separation, the 17 gates and raw artifact/hashes, and compare the original emission with the independent strict coefficient semantic oracle. Use arbitrary-precision integers / lossless JSON number tokens for all path counts. The support work has no confirmed active responsible executor; do not close the native obligation on this additional test.

Mother-task gaps remain: identify actual erroneous LP011 native signed-argmax caller, identify actual LP019 erroneous positive natural-path signed cancellation caller, close the 28-LP consumer dependency census, and receive independent Driver REQUEST_REVISION review. This is the **new author-side unit #41**; Native semantic association and formal Result have not been claimed here. Prior #39/#40 GitHub evidence remains intact.

Protected frozen P000 V5, current ACTIVE six-axis Heartbeat worldview and source provenance are unchanged. No maintenance-lane identity, scheduler, notification, CLAIM, reviewed Result or mathematical admission changes were made.
