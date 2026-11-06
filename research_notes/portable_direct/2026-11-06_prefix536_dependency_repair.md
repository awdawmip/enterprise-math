# PREFIX-536 dependency compatibility repair

2026-11-06. Software maintenance and finite executable regression.

## Failure and change

At source commit `96ffdf1472ee4c44fce84c678f433029ff7c0d0c`, the benchmark failed at its first import-contract assertion. It expected `delta_coefficients`, `evaluate_roots`, `TARGET` and `sign`, whereas the published PREFIX-535 dependency exports `denominator`, `evaluate`, `T` and `sig`. This is the reproducibility gap recorded in the [PREFIX-537 report](2026-11-06_prefix537_symbolic_brc_gate_48root.md).

The repair adapts only the benchmark loader to these existing names. It also checks the existing `results=[]` definition/test separator before executing the definition prefix, so a missing separator fails before executing the dependency's test main. Algorithms, constants, recurrence, benchmark sizes and assertions are unchanged. PREFIX-535 and the original PREFIX-536 execution JSON remain unchanged, as do the PREFIX-537/538 materials and frozen science pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## Executed checks

The unmodified source failed with exit 1 and `AssertionError`. The repaired script completed with exit 0 and `ALL_CHECKS_PASS` on CPython 3.12.14, Linux x86_64. [The separate maintenance run record](PREFIX536_DEPENDENCY_REPAIR_RUN_20261106.json) preserves the failure, actual new stdout, complete measured result and source identities.

- Both existing denominator-modulus checks passed.
- The existing single-root exact consistency checks passed at lengths 0, 1, 2, 7, 23, 24, 35 and 60; the independent raw-path check passed through length 7.
- Existing all-48-root consistency checks passed at lengths 0, 7, 23 and 40.
- All three methods were measured with the existing five repetitions, then exactly cross-compared through N=64, 256 and 1024 for one root and N=64 and 256 for all 48 roots. Memory-measurement reruns also passed output equality assertions.
- Focused loader checks passed: Python syntax, absence of the dependency's test output, and an intentionally missing separator raising before dependency execution.

New median timings in milliseconds (controller / linear / parity): one root N=1024, 57.431 / 48.733 / 3.490; all 48 roots N=256, 449.705 / 29.719 / 20.081. These are this maintenance environment's measurements. The original author's measurements retain their historical provenance.

## Reproduce

Copy `PREFIX535_rooted_parity_certificate.py` and `PREFIX536_benchmark_certificate.py` from this commit into a fresh temporary directory, then run `python PREFIX536_benchmark_certificate.py` there with assertions enabled. The script writes `PREFIX536_EXACT_EXECUTION.json` beside itself; using a temporary directory preserves the repository's historical result file.

This run validates the existing finite integer checks and executable benchmark. Mathematical proof review and native Result admission were not performed. Repository-wide unit tests, bilingual/reference checkers and the unchanged PREFIX-537/538 certificates were not run for this loader-only change.
