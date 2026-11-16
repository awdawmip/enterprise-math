# R5 absolute-noise result — executed publication-byte verifier check

**2026-11-17 / frozen pin** `435e77af0d180eac32bd1f9c4c464bc4010b7551`.

The shorter published `VERIFY_R5_ABSOLUTE_NOISE.py` was independently reconstructed as local executable bytes. Local `git hash-object` returned `9f5d5e15a19269509e9f8be3f1b48be921e88d10`, **identical to the published GitHub blob**, so this exact source file was executed, in addition to the earlier longer verification driver.

Command using standard-library Python:

```bash
python VERIFY_R5_ABSOLUTE_NOISE.py /path/to/compact_stdout.json /path/to/EXACT_R5_ALL_101_BUDGETS.json > result.json
```

Result: `PASS_R5_ABSOLUTE_NOISE_FOUR_QUERIES_SHARP`; `pair_budget_integer_checks=3296640`; `absolute_noise_threshold=941475936774146084359372800000`. Source compact SHA256 `a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`. The executable verifies exact 101×256 Zeta reconstruction against the separately saved 25,856-entry count table before its pairwise computations. The fixed three-query optimization also checks all 552 first/middle pairs, 2,016 state pairs per pair, and the 20 late-budget four-state margins.

## Exact raw integer output widths

Using the same 101-budget exact coefficient data, bit length is Python `int.bit_length()`, summed over actual returned integers per full eight-bit closure mask. The following maxima cover all 256 masks:

| Budget vector | Sum K | Worst returned bits | Minimum returned bits |
|---|---:|---:|---:|
| (217,218,224,305) — sharp absolute-noise guarantee | 964 | 469 | 463 |
| (217,290,305) — best fixed 3-query absolute margin | 812 | 344 | 341 |
| (214,230,302) — sharp relative-noise guarantee | 746 | 411 | 404 |
| (214,285,302) — lower-width sharp relative-noise triple | 801 | 384 | 378 |

These are **exact raw data-width** counts for these specified query vectors, not universal encoding or bit-complexity optima. The four-query vector optimizes the worst-case absolute-error guarantee in the specified family; its 469-bit maximum is a measured cost of this feasible construction. Optimize the four-query resource frontier only if a new task requires it.

Original published result is `RESULTS_EXACT.json`. Earlier local full-verifier source checksum `b438a31fa6811e23f3c9303f6c2412e380109947fcda6ce5035f5824cc2b5826` differs from the shorter, now separately executed published verifier as explicitly documented. Mathematical status remains `AUTHOR_PROVED / EXACT_INTEGER_FINITE_CHECKED / NOT_REVIEWED`.
