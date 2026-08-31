# R062 Stage 0 — Deterministic Reproducibility Proof

Researcher-ID: `EM-R062-7C4A91`  
Checker: `scripts/r062_stage0_validate_brc_multipath_bridge.py`  
Taskbook source: `bde65a479108b8a906d287fb1728d004f25178af`  
Frozen Stage 1R reproducibility head: `653071b8e230d1e707e0544cab22ad2a408b92bd`

## 1. Invocation

```bash
python3 scripts/r062_stage0_validate_brc_multipath_bridge.py \
  --out research_results/R062_STAGE0
```

The checker uses exact integer arithmetic, finite combinatorics and SHA256 serialization only. No floating-point decision is present.

## 2. Independent frozen Stage 1R regeneration

The script regenerates the frozen native path data rather than reading R061 result JSON.

Recovered exactly:

- trace pairs through `a+b<=18`: `190`;
- formal linearizations: `524,287`;
- three-sector native paths: `1,572,861`;
- native replay SHA256: `359474ba6b53ffbb3c326cf331d55dd3ed098837451a46b0754926b7c642d702`;
- compressed trace SHA256 through `a+b<=256`: `aa0e3761f7446cf89e782c74b8020157b41713a37022daf44a2f8e95179e4ead`;
- structural mismatch: `0`;
- duplicate mask count: `0`.

Expected digests are comparison targets only after generation.

## 3. R062 bridge regeneration

From one generated witness source, for all `a+b<=12`, all three sectors and all seven translated starts, the checker simultaneously derives:

- concrete Path-BRC witness set;
- N-BRC terminal multiplicity;
- Boolean-BRC terminal support;
- trace fiber cardinality;
- typed terminal;
- relative translated prefix trajectory.

Replay totals:

- translated trace cases: `1,911`;
- concrete paths: `172,011`;
- center transitions: `1,892,394`;
- per-sector paths: `57,337`;
- per-start paths: `24,573`;
- witness replay SHA256: `175c7f0efa6e62497dde5abbb65d354ddfc17a557f37640ee30260815cd68726`;
- mismatch count: `0`.

## 4. Mandatory falsification gates

The same checker independently verifies:

- `(1,1)` commuting diamond: Path `2`, N `2`, Boolean `1`, trace class `1`;
- `(3,4)`: Path `35`, N `35`, Boolean `1`, trace class `1`;
- `(4,3)`: `35`;
- `(0,5)` and `(5,0)`: `1` each;
- `N=25` one-sector total: `72`;
- ordinary path-set cardinality is not globally additive, with minimal `A union A` counterexample;
- N-to-Boolean positivity map satisfies semiring support laws on the finite sanity window and is classified algebraically globally;
- unlabeled `(1,1)` support absorbs the reverse-third shortcut;
- component labels reject that shortcut without jump count;
- translated covariance;
- duplicate path detection.

`R062_STAGE0_MISMATCHES.json` preserves the smallest mismatch if any appears. Current result: `mismatch_count=0`.

## 5. Acceptance

All sixteen taskbook acceptance gates are true in `R062_STAGE0_REPLAY_SUMMARY.json`.

Final classification:

`BRC_IS_EXACT_BOOLEAN_SHADOW_OF_COMPONENT_TYPED_NATIVE_MULTIPATH_WITH_PATH_ENRICHMENT_RECOVERING_FULL_FIBER`.

This classification includes the independent negative boundary that unlabeled adjacency BRC is not a native-line-membership bridge.
