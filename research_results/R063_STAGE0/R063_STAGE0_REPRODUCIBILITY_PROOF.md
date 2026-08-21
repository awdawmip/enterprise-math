# R063 Stage 0 — Reproducibility proof

Task: `RS-R063-STAGE0-PATH-VALUED-SQUARE-ROOT-2500-DISCOVERY`  
Taskbook source: `e7dd7af0b7f01168afd25e55d04900e841cc399e`  
Owner branch: `research/r063-stage0-path-valued-sqrt-2500`  
Researcher: `EM-R063S0-E7DD7A`

## Deterministic command

```text
python3 scripts/r063_stage0_validate_path_valued_sqrt_2500.py --out research_results/R063_STAGE0
```

The checker uses only Python exact integers, `isqrt`, integer factorization, Gaussian integer multiplication/norm, deterministic modular square-root/Cornacchia split-prime construction, exact binomial arithmetic, and deterministic combination rank/unrank.

## Phase barrier

`discover_from_scalar_root(N)` is called first. Its JSON-safe payload is materialized as `R063_STAGE0_DISCOVERY_PHASE_FROZEN.json` and hashed **before** `verify_against_norm_fiber` is called.

Frozen discovery SHA256: `6dd26e75436fb6740134590fc243b59ab9eb287cadbc46d417d5bbbb74022f0d`.

The brute function `brute_norm_fiber` is reachable only from the verification/regression code path and is not called by discovery.

## Anti-hardcode audit

Source scan pass: `True`.  
Nontrivial discovered-pair literal hits in checker source: `[]`.

## Exact replay checkpoints

- General square regression range: `1 <= r <= 512`.
- Combined C3/C4 regression mismatch count: `0`.
- Regression row SHA256: `51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae`.
- One-sector total path-cardinality certificate SHA256: `9d5e0d1b81bbc3b0cb1aa72bbf73b58fcdf4cf17555361f85d5e51b034439f19`.
- Replay summary core SHA256: `d922b6869c0abfd64981fa3b2714c0a8d16ab1889f049bd0f6dbe50fcbb7f14a`.

No explicit expansion of astronomical path fibers is performed. The checker stores coefficient-extraction formulas, exact binomial cardinalities, and deterministic rank/unrank samples instead.
