# X6 R063 unit #49 — secondary attestor frozen loader-glob completeness

Date: 2026-11-16. Mother: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`. Lane: `chatgpt-research-onhour-enterprise-math-20260923`. Frozen P000 V5 and original R063 scientific input unchanged. Author-side source-level engineering finding; UNREVIEWED / NOT_ADMITTED. **The original six-file 17-gate / 512-case native benchmark has not been executed in this unit.**

## Reproduced source-set inconsistency

The exact original source `scripts/r063_stage0_validate_path_valued_sqrt_2500.py` at branch `research/r063-stage0-path-valued-sqrt-2500`, Git blob `b4e000a6377f2858ae434eb0eecd0c25c33e8592`, contains:

```python
_PARTS = sorted(_PART_DIR.glob("part*.inc"))
_SOURCE = "".join(p.read_text(encoding="utf-8") for p in _PARTS)
exec(compile(_SOURCE, str(_PARTS[0]), "exec"), globals(), globals())
```

Before the repair, **the independent secondary harness** `research_checks/X6_R063_PINNED_NATIVE_REPLAY_ACCEPTANCE_HARNESS_20261116.py` on main, old Git blob `d93add4c440fc453a16555d86d5e0aefc966d38b`, checked only the six expected source hashes. It did not compare the actual loader `part*.inc` expansion with the expected five-part manifest.

Consequently the six expected files may all match their frozen Git blobs while an untracked `part05.inc` or `part999.inc` is appended to the executable concatenation. This is an attestation completeness defect, not a claim that the historical accepted R063 program was altered.

An independent synthetic fixture used a loader with the same verified `glob/sorted/concat/exec` behavior and a temporary sixth `.inc`. The old six-file-only predicate remained true, the unpinned source actually executed, and the new exact manifest predicate rejected the fixture. The synthetic witness executed successfully in ordinary Python and with `-O`. This test did not execute or impersonate the native 512-case benchmark.

## Permanent source fix and test

On current main, secondary harness commit `db6d8f1dca48ad2560e428c18ae3f3123b040a17`, blob `234e0f00654ae5cdb5254f37fc9d63ea1b51cd30`, now validates, before running the original loader:

```python
parts_dir = repo / 'scripts/r063_stage0_checker_parts'
require(parts_dir.is_dir(), 'missing original checker part directory')
actual_parts = sorted(p.name for p in parts_dir.glob('part*.inc'))
expected_parts = [f'part{i:02}.inc' for i in range(5)]
require(actual_parts == expected_parts, ...)
```

The preceding hardened *primary* same-object wrapper already implemented this check; it was not modified. New dedicated regression test `research_checks/test_x6_r063_secondary_harness_glob_set_20261116.py`, final commit `097290e6a20699951f274708eb010d2e6468a415`, Git blob `a6a4c3ca5e1d088d92cb44b01df1b2267b1a7cc7`, constructs synthetic six-file exact pins and verifies that two extra-glob mutations fail and the restored exact set passes. Its syntax and equivalent small source-check test double were executed locally with Python and `-O`. Its import against the complete remote secondary harness remains a checkout-side regression to run with the actual authorized repository.

## Handoff / acceptance

Issue [#2416](https://github.com/awdawmip/enterprise-math/issues/2416) remains the bounded native execution support route. The actual runner must use the unchanged original six blobs, strict five-part manifest, `N=2500`, `r=1..512`, 17 original gates, 13 output artifacts, process exit, discovery SHA256 `6dd26e75436fb6740134590fc243b59ab9eb287cadbc46d417d5bbbb74022f0d`, and 512-row SHA256 `51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae`. No replacement implementation is accepted as that experiment.

The independent Driver REQUEST_REVISION, LP011 historic wrong singleton caller, LP019 historic wrong positive natural N-BRC cancellation caller, and 28-LP active-consumer closure remain distinct unresolved tasks. Do not infer those callers from correctly scoped current functions; keep their provenance status `UNRESOLVED_PROVENANCE`.

This unit changes one author-side execution attestor and adds one synthetic regression test. It does not change frozen source, claims, Result, P000, scheduler, or notification configuration.
