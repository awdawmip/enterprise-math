# Implementation corrections

The first author contract-test run failed before benchmarking because mixed NumPy advanced indexing moved the vector axis in the Hermitian check (shapes (3,32,32) versus (32,3,32)). Replaced the check with explicit np.take(axis=...) operations. No threshold, case, or tolerance changed. Failed run produced no successful test report.

The original 64-cubed batch hit the local 45-second tool execution boundary after two complete five-repeat cases had been printed. Those two raw cases were recovered without rerun. The incomplete third case has no reported result. The runner was extended to save each completed case and resume from printed complete rows; mathematical code, tolerances, fixed cases and trial count did not change. The pre-checkpoint runner is preserved verbatim.
