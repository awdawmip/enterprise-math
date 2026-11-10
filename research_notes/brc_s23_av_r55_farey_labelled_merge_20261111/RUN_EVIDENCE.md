# R55 exact computation — executed evidence

Scientific frozen commit: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
R54 predecessor immutable head: `e83b08d5cf956ba19634c838c07816715b372ad5`.

Actual local Python 3 exact-integer execution (original executable versions kept in R55 research bundle):

```
PASS_R55_CIRCULAR_MERGE_SMALL 594
PASS_R55_STATES {61: 2, 225: 76} endpoint_source_classifications 900 endpoint_phase_generator_steps 1030
PASS_R55_INDEPENDENT_STAGE_ORACLE 156
PASS_R55_298_RISK_RUNS {'stages': 78, 'events': 9697, 'affine_runs': 298, 'bytes': 15356, 'sha256': '2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6', 'last_affine': [-4017401528447, 15321634290944]}
```

Published independent compact executable rerun:
```
PASS_R55_FULL 78 Farey stages 298 affine runs 9697 events 156 independent stage-oracle checks 15356 TSV bytes 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6
```

R55 15,356-byte TSV is bytewise identical to the frozen R46 TSV and a freshly rerun independent R49 source compiler, with same SHA-256. Two distinct endpoint rational parameters each pass all 78 stage owner-vector comparisons. The 594 exact rational small tests exercise negative source time and overlap of source and historical phase indices.

Matched cut-oracle operation counts, same 82-bit midpoint rational and exact integers:

| K | requested k | R54 Farey comparisons | R54 index updates | R51 Floor Sum calls | R51 Euclidean iterations | R53 heap exact residue evaluations |
|--:|--:|--:|--:|--:|--:|--:|
| 352 | 12 | 36 | 12 | 1271 | 22481 | 352 |
| 352 | 352 | 36 | 352 | 35507 | 637819 | 352 |
| 100000 | 12 | 133 | 12 | 1552 | 32389 | 100000 |
| 1000000 | 12 | 180 | 12 | 1672 | 37956 | 1000000 |

The three-run host medians and exact-operand peak bit lengths are in local `R55_COST_CERTIFICATE.json`; measurements are implementation-/host-specific. Cut-only benchmarks do not include precision construction, labelled source-state assembly, full Farey stage generation, and output serialization. When only frozen S23 end-to-end source vector construction is needed, R49's 778 source inspections across two endpoints are still fewer than R55's 1,030 cut successor operations plus 900 tags. The R55 integration therefore supplies a constructive, independent and reusable route rather than a claimed universal end-to-end speedup.

GitHub's source `VERIFY_R55_PUBLISHED.py` is exactly the standalone program actually executed and read back; its Git blob SHA-1 is `cd5062c9ca6aea313c744b697768f6016435e1f8`. The separate extended executable, JSON certificates, TSV, independent reference and run logs remain in the linked user-facing research archive, not all in this PR.

Status: AUTHOR_DERIVATION + FINITE_EXACT_CHECKS; independent mathematical review and formal Source Result not claimed.
