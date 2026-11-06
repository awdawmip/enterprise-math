# Validation-count clarification (2026-11-07)

The executed original VERIFY.py prints `assertions= 7013`. In that version the variable `checks` is a **weighted progress counter**, not the number of Python `assert` statements executed. Its value is 6,709 immediately before the `mpmath` section and 7,013 after the 70-digit numeric diagnostics (304 additional counter units). The exact `Fraction` identities and range checks all passed, and the high-precision checks also passed.

The first PROOF.md edition and the initial PR progress comment used the phrase "7,013 exact assertions"; interpret this as 7,013 *mixed counted test units*, not 7,013 exact-rational assertions. The mathematical theorem rests on the analytic proof; the finite checker supports the declared tested instances and numerical constant only.

Readback of the executed VERIFY.py and RUN_EVIDENCE.txt is unchanged and matches their local Git blobs. This clarification corrects evidence labeling without altering the frozen scientific pin or the source code that actually ran.