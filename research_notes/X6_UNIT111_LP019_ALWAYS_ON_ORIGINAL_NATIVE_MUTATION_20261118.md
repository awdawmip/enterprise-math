# X6 Unit111 — LP019 exact signed BRC: assertion elision in secondary math validation, new all-mode original-native repair

**2026-11-18.** Mother objective `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`, Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`.

**Status:** `AUTHOR-SOURCE-EXECUTED / EXACT-INTEGER / UNREVIEWED / NOT_ADMITTED`. P000 frozen V5 at `59538f585d037d09ef687b28715c4bc1a3f9fe03`; actual original six-axis signed BRC `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. This is not the frozen R063/Helly benchmark.

## Discriminating question and actual result

Unit109 proved actual original native `endpoint_multiplicity` calls survive Python optimization in the versioned LP019 program. Unit108 still retained 18 bare `assert` validations of the **two-axis positive word-count / signed net / thickness model**, in addition to the native six-axis API comparisons. They vanish under `python -O` and `-OO`.

Two exact controlled mutations to an otherwise pinned, temporary LP019 checker demonstrate a real false PASS:

1. Replace the output of `word_formula(s,n)` by zero while preserving its otherwise exact integer definition and all native BRC calls. Unit108 normal Python fails, but `-O` and `-OO` exit 0 with `status=PASS` and still report **10,364 true six-axis native DP endpoint comparisons**. With the same mutation, the new V3 checker rejects in all modes at `UNIT111_ALWAYS_ON_CHECK_10`.
2. Increase `hidden_histogram_count(s,n)` by two on otherwise admissible fibers, preserving the original returned zero on inadmissible fibers. Unit108 normal fails and both optimized modes falsely PASS; V3 rejects in all three modes at `UNIT111_ALWAYS_ON_CHECK_11`.

This is a substantive discrepancy: for two signed axes, a net displacement `(s_i,s_j)` after `n` steps has an exact count of labeled branch words given by
[
W_n(s)=\sum_{k=0}^{K} \frac{n!}{(s_i^+ +k)!(s_i^-+k)!(s_j^+ +K-k)!(s_j^-+K-k)!},
\quad K=\frac{n-|s_i|-|s_j|}{2},
]
when `n-|s_i|-|s_j|` is nonnegative even, otherwise zero. The native six-axis endpoint BRC API and this two-axis formula are different checked surfaces; a correct call to the former cannot prove correctness of an unexecuted check of the latter. The number of hidden cancellation histograms in the two-axis signed/length fiber is exactly `K+1`; the altered functions falsify those identities.

## Implemented and executed

Created **opt-in new source** `research_checks/X6_UNIT111_LP019_FULL_ALWAYS_ON_NATIVE_V3_20261118.py` with Git blob `541c78d4cb639934939635274f96fce8e6ef0e4c`: using AST-preserving logic, converted **all 18** original remaining `assert` predicates into unconditional `if not <predicate>: raise AssertionError` with stable check IDs. The unchanged original real-native Git blob guard and existing always-on native endpoint and return comparisons are retained. Unit108 original file, original native source and P000 source were not overwritten.

Executed unchanged original and repaired sources in a temporary matching repo tree against the *real* frozen native six-axis BRC module using CPython normal, `-O`, `-OO`; all six unmutated executions exited 0 with byte-identical JSON output SHA256 `eae53806d60ac8cfc6e757b004cce2f5f2ee3d989a318801226de45b8e5fcfac`. Exact evidence:

| Type | Actual executed checks |
| --- | ---: |
| Distinct four-part signed/thickness histograms | 625 |
| Two-axis signed endpoint formula comparisons | 2,925 |
| Six-axis original BRC DP endpoint comparisons | 10,364 |
| Real original native endpoint calls including odd parity/return helper | 10,368 |
| Original return-multiplicity calls | 3 |
| Native DP endpoints by lengths 0 through 6 | 1, 12, 73, 304, 985, 2,668, 6,321 |

Both mutation controls were executed in all three modes against the unchanged native module and correctly discriminated false positives. Their exits, exact original source pins and output digest are in the new JSON certificate `research_checks/X6_UNIT111_LP019_ALWAYS_ON_MUTATION_CERTIFICATE_20261118.json`.

**Scope:** exact finite signed X6 model, no new Foundation claims. Neither the historical erroneous LP019 **natural positive N-BRC subtraction caller** nor LP011 **wrong signed argmax caller** has yet been located at a demonstrably faulty frozen `file:line`. The real validation defects of Unit107–Unit111 are separately classified and must not be passed off as those unproved historic allegations.

## Subsequent mother-task research

LP011/LP019 genuine known validation defects have now been repaired in versioned, actual-original-BRC-integrated consumers; continue on the frozen history-to-current callsite crosswalk at actual `file:line`, distinguishing positive N-BRC, signed polynomials, observer quotient and native signed cells. Preserve the claim ledger's `UNRESOLVED_PROVENANCE` for the original alleged wrong callers, complete remaining 28-LP downstream dependencies, and send existing independent Driver `REQUEST_REVISION` material for review via the authenticated route. Original R063/Helly benchmark support Issue #2416 stays open and must be run by its actual authorized path; this Unit111 is not such an execution. All author evidence is `UNREVIEWED / NOT_ADMITTED`.
