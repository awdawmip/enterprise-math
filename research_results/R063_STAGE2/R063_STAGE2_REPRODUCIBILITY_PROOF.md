# R063 Stage 2 — Reproducibility Proof

Status: `CHECKER PASS / ZERO MISMATCH`

## 1. Frozen dependencies

- Taskbook: `74cacc89ec09a8af7dd7ff01c10f2baf082daf81`
- Stage 1 frozen owner head: `65f4e98cd707c634d805f2a9ec7c41f24ab06185`
- Stage 1 Driver acceptance: `fb2331b0602e74cae506ebac49c4582e7147479d`
- Researcher-ID: `EM-R063S2-52118B`

The Stage 2 checker does not contain an independent root-discovery implementation. By default it first looks for the frozen Stage 1 executable loader next to the Stage 2 script; if absent, it materializes the exact Stage 1 loader and checker parts from Git object `65f4e98...` using `git ls-tree` and `git show`, then executes that frozen code via `runpy`.

An explicit `--stage1-loader` path remains available for a separate frozen Stage 1 worktree.

## 2. Reproduction command

From an Enterprise Math clone containing the frozen Stage 1 commit object:

```bash
python scripts/r063_stage2_validate_multiplicative_provenance_algebra.py \
  --out research_results/R063_STAGE2 \
  --max-pair 128
```

Equivalent with a separate frozen Stage 1 worktree:

```bash
python scripts/r063_stage2_validate_multiplicative_provenance_algebra.py \
  --stage1-loader ../r063-stage1-general-path-norm-root/scripts/r063_stage1_validate_general_path_norm_root.py \
  --out research_results/R063_STAGE2 \
  --max-pair 128
```

## 3. Exact checker coverage

The accepted run records:

- mandatory base set `{1,2,5,13,17,25,65}`;
- `49` ordered base pairs with explicit provenance-pair enumeration;
- exact local `m_p` count checks over the exponent range needed through `128`;
- exhaustive ordered pair regression for every `1<=A,B<=128`, total `16,384` pairs;
- every one of the 16,384 compact pair rows is materialized in checker memory, including provenance summaries and full oriented trace-target index maps;
- publication stores the full-domain row SHA-256 plus 128 per-`A` block SHA-256 values so every ordered pair block is independently replay-checkable without a redundant 16,384-row source dump;
- the exact norm catalog is materialized in memory and frozen by a full SHA-256 plus 37 deterministic block hashes;
- deterministic sparse supported/unsupported pairs reaching `9,000,000,000,000`;
- large sparse path cardinalities represented exactly as symbolic `binom(n,k)` expressions instead of needlessly expanding enormous decimal integers;
- frozen Stage 1 generator/brute-verifier separation on replay anchors;
- mandatory `2 x 2` and `5 x 5` multiplicity discriminators;
- bounded executable checks of the oriented component product laws;
- ordinary general proofs in the theorem documents for the infinite statements.

## 4. Accepted hashes

At the final local Stage 2 generation:

- checker SHA-256: `4e7486776cae3d4107b4a18819b80f83e4b2aa1aff55564d25ad57f6de8707a9`
- semantic scope ledger SHA-256: `cfc98d4760887ab262ef8b4583c3c9c1c1d134cfa4fc23696d3f11fe8e73940a`
- provenance fiber certificate SHA-256: `e36633e99d4c54c7f1b0a5911569b8fcb97fb9e85e94ea2eae2fda6ed0711a7b`
- multiplicity separation certificate SHA-256: `8d698c52926da70b9302fac42e26d804507a947f28ad61885a64d4abd0f23de0`
- regression SHA-256: `af3a10d1ed5b29be7571600768d5c7f903f6f7958f639a1459c2ba918f68675e`
- mismatch file SHA-256: `ac888839dfba350877cf6a5d308707ad7e0883662f93fd867848e2ee3e75d1bb`

`R063_STAGE2_MISMATCHES.json` reports `mismatch_count=0`.

## 5. Connector-only execution disclosure

The current ChatGPT execution environment could not create a network Git clone because DNS resolution for GitHub was unavailable. The local theorem/checker run therefore supplied `--stage1-loader` using an execution-only adapter transcribed from the frozen Stage 1 factorization/Gaussian generator interface already read at the frozen head; this adapter is **not** a Stage 2 artifact and is not published.

The committed Stage 2 checker itself avoids that environmental workaround: its default path materializes and executes the exact frozen Stage 1 Git object. Driver replay in a normal repository clone therefore consumes the actual frozen dependency, not the execution-only adapter.

This environment limitation is tooling provenance, not mathematical evidence and not a research hard block.

## 6. Decision boundary

Finite replay validates implementation consistency and preserves counterexamples. The general provenance, quotient and no-go statements are proved separately in the Markdown theorem artifacts; no theorem is promoted solely from finite regression.

`CI_NOT_REQUIRED_FOR_RESEARCH` under the active L1/L2/L3 GitHub interaction policy.
