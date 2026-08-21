# R063 Stage 1 — Reproducibility proof

Task: `RS-R063-STAGE1-GENERAL-NON-SQUARE-PATH-NORM-ROOT-DISCOVERY`  
Taskbook source: `6a3c104f5e3a46125ccec6d591de6b824cf8dae9`  
Owner branch: `research/r063-stage1-general-path-norm-root`  
Researcher: `EM-R063S1-6A3C10`

Deterministic command:

```text
python3 scripts/r063_stage1_validate_general_path_norm_root.py --out research_results/R063_STAGE1 --max-n 100000
```

The checker uses exact integer arithmetic only.  Discovery runs from integer factorization and Gaussian prime splitting/exponent allocation.  Mandatory witness discovery is materialized and hashed before any brute verifier is called.  In the exhaustive regression each `N` is likewise discovered and frozen in memory before the independent target-equation verifier runs.

Exhaustive regression: `[1, 100000]`.  
Root-set mismatches: `0`.  
Sparse suite max `N`: `1000000000` with mismatches `0`.  
Square Stage 0 regression pass: `True`.  
Mandatory discovery freeze SHA256: `941169ca05595ea2282c1771358a62d0384f1c625e8dd64d2cefcfe9ca404ed3`.  
General regression rows SHA256: `2a5855190e94eaa56e5ad6c730d523b075100a939e53116e2afbab6c49cb1bb2`.  
Final mismatch count: `0`.

Astronomical sparse-suite path counts are computed exactly as Python big integers and certified in compressed form by bit length plus SHA256 of the exact unsigned big-endian integer.  Mandatory and exhaustive-range path counts remain exact integers; no explicit path-word expansion is performed.
