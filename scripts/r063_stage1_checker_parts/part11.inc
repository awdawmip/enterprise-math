Multiple factor-pair channels can collapse to the same component root.  This multiplicative derivation multiplicity is a provenance enrichment above the deduplicated native trace and is **not** native path multiplicity.

Small deterministic separation witness:

`{json.dumps(witness, sort_keys=True)}`.

No law identifying or multiplying algebraic derivation multiplicity with `binom(a+b,a)` is adopted.
"""

def markdown_repro(summary: Mapping[str, object]) -> str:
    return f"""# R063 Stage 1 — Reproducibility proof

Task: `{TASK_ID}`  
Taskbook source: `{TASKBOOK_SOURCE}`  
Owner branch: `{OWNER_BRANCH}`  
Researcher: `{RESEARCHER_ID}`

Deterministic command:

```text
python3 scripts/r063_stage1_validate_general_path_norm_root.py --out research_results/R063_STAGE1 --max-n {summary['general_regression']['N_range'][1]}
```

The checker uses exact integer arithmetic only.  Discovery runs from integer factorization and Gaussian prime splitting/exponent allocation.  Mandatory witness discovery is materialized and hashed before any brute verifier is called.  In the exhaustive regression each `N` is likewise discovered and frozen in memory before the independent target-equation verifier runs.

Exhaustive regression: `{summary['general_regression']['N_range']}`.  
Root-set mismatches: `{summary['general_regression']['rootset_mismatch_count']}`.  
Sparse suite max `N`: `{summary['sparse_suite']['max_N']}` with mismatches `{summary['sparse_suite']['mismatch_count']}`.  
Square Stage 0 regression pass: `{summary['square_scope_regression']['pass']}`.  
Mandatory discovery freeze SHA256: `{summary['mandatory_discovery_snapshot_sha256']}`.  
General regression rows SHA256: `{summary['general_regression']['rows_sha256']}`.  
Final mismatch count: `{summary['mismatch_count']}`.

Astronomical sparse-suite path counts are computed exactly as Python big integers and certified in compressed form by bit length plus SHA256 of the exact unsigned big-endian integer.  Mandatory and exhaustive-range path counts remain exact integers; no explicit path-word expansion is performed.
"""

def markdown_final(summary: Mapping[str, object]) -> str:
    return f"""# R063 Stage 1 — Final classification

Strongest supported classification:

`PATH_NORM_ROOT_OPERATOR_COMPLETE_EXACTLY_ON_SUM_OF_TWO_SQUARES_SUPPORT`

Equivalent integer-support statement:

`PATH_NORM_ROOT_FACTORIZATION_OPERATOR_COMPLETE_FOR_ALL_POSITIVE_INTEGER_N_WITH_INTEGER_COMPONENT_SUPPORT`

The operator is constructive from `N`, integer factorization, Gaussian prime splitting and exponent allocation.  It returns the complete ordered nonnegative component-root fiber when the sum-of-two-squares support criterion holds and the exact empty integer-addressed fiber otherwise.

Non-square native traces require no integer scalar square root.  A representable non-square `N` may have irrational native length `sqrt(N)` while retaining fully discrete integer-addressed trace/path fibers.

All acceptance gates: `{json.dumps(summary['acceptance_gates'], sort_keys=True)}`.

Stage 1 stops here for Driver review.  No R063 Stage 2 is opened.
"""

def build_outputs(outdir: Path, max_n: int, script_path: Path) -> Dict[str, object]:
    # DISCOVERY PHASE: mandatory witnesses are fully materialized and hashed first.
    discovery_obj = mandatory_discovery_object()
    discovery_sha = sha256_obj(discovery_obj)
