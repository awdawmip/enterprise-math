# Dependencies and restoration chain

This package contains the complete current-round source and evidence for `coherence_sampler` and `arithmetic_partition`. It is **not a standalone runtime archive**. Its existing executions use the historical modules and certified phase bank pinned below. This document adds source provenance; it does not report another scientific execution or independent admission.

All EM references below are immutable commits in `awdawmip/enterprise-math`. The Stage87 source is a separate Git-bundle snapshot, explicitly distinguished from an EM commit. `DEPENDENCY_MANIFEST.json` records exact paths, source SHA-256, Git blob IDs, selected gzip payload hashes, current entry-file hashes and import edges.

## Source layers

| Layer | Immutable commit | Manifest and restore subtree |
| --- | --- | --- |
| qft_approximation | `46fca6734fde9b1580b1b4160c454a43844451a9` | [PUBLICATION_MANIFEST.json](https://github.com/awdawmip/enterprise-math/blob/46fca6734fde9b1580b1b4160c454a43844451a9/research_notes/directed_recovery/20260927_C6438C/qft_approximation/PUBLICATION_MANIFEST.json); `sep27-qft-approx` |
| qft_row_queries | `951cc16cb09635fae9f93230d96030fdaa2035b3` | [PUBLICATION_MANIFEST.json](https://github.com/awdawmip/enterprise-math/blob/951cc16cb09635fae9f93230d96030fdaa2035b3/research_notes/directed_recovery/20260927_C6438C/qft_row_queries/PUBLICATION_MANIFEST.json); `sep27-qft-research` |
| optimization | `0e6380ff74d31b842ba0b54802c1f0595a7dd60d` | [OPTIMIZATION_MANIFEST.json](https://github.com/awdawmip/enterprise-math/blob/0e6380ff74d31b842ba0b54802c1f0595a7dd60d/research_notes/directed_recovery/20260926_C6438C/optimization/OPTIMIZATION_MANIFEST.json); `sep26-shor-general/optimization` |
| direct_word_bank | `9348fc6abdf45becbd12a8019d93f72d576b9fab` | [DIRECT_CLOSURE_MANIFEST.json](https://github.com/awdawmip/enterprise-math/blob/9348fc6abdf45becbd12a8019d93f72d576b9fab/research_notes/directed_recovery/20260926_C6438C/DIRECT_CLOSURE_MANIFEST.json); `sep26-shor-general` |
| compiled_word | `8d4e9c12f7492316b825e96423bc0ee36ccdee22` | [WORD_MANIFEST.json](https://github.com/awdawmip/enterprise-math/blob/8d4e9c12f7492316b825e96423bc0ee36ccdee22/research_notes/directed_recovery/20260926_C6438C/new_word_compiler/WORD_MANIFEST.json); `sep26-shor-general/new_word_compiler` |
| general_foundation | `1fb7ff99d205f9ca03772942be64f732553dcd86` | [MANIFEST.json](https://github.com/awdawmip/enterprise-math/blob/1fb7ff99d205f9ca03772942be64f732553dcd86/research_notes/directed_recovery/20260926_C6438C/MANIFEST.json); `sep26-shor-general` |
| terminal_foundation | `b6625778e869511d85a202a0839eb105a197659e` | [MANIFEST.json](https://github.com/awdawmip/enterprise-math/blob/b6625778e869511d85a202a0839eb105a197659e/research_notes/directed_recovery/20260926_0C08F0/MANIFEST.json); `sep26-shor-alternative` |

The manifest file hashes in the JSON were computed from the local historical publication manifests. All 25 selected historical source/data files were checked against their recorded hashes and Git blobs where supplied. Historical remote bytes were not downloaded again in this documentation step; the prior publication receipts remain the readback authority. The optimization receipt pins `0e6380ff74d31b842ba0b54802c1f0595a7dd60d`, including its corrected byte-preserving transport. The previous approximation and row-query receipts pin `46fca6734fde9b1580b1b4160c454a43844451a9` and `951cc16cb09635fae9f93230d96030fdaa2035b3` respectively.

## Actual entry points and phase bank

- `coherence_skip.py` imports `projected_rows.py` from qft_approximation and `single_walker.py` from qft_row_queries. These continue into the certified word observer, lazy streaming and native stage modules.
- `typed_quartic.py` imports the previous typed Jacobi certificate and the lazy typed arithmetic/GCD modules. Its checker also imports the old Gram bank loader and native norm/core interfaces.
- The checkers transitively import `check_direct_word_integration.py`, `check_compiled_streaming.py`, `general_driver.py`, `general_streaming.py`, `terminal_instrument.py`, the sparse foundation and typed integer prechecks. Importing a helper checker can therefore require its historical source dependencies even when its `main` function is not run.
- The current bounded sampler fixtures load `direct_word_integration/DIRECT_WORD_INTEGRATION_RESULTS.json.gz` at commit `9348fc6abdf45becbd12a8019d93f72d576b9fab`. `check_gram_sampler.load_bank` extracts `phase_compilation` and calls `bank_from_compilation(t=4, epsilon=1)`. The gzip SHA-256 is `ef981768a20a72a67bfd7d01284d1b946cfc95ded96552a07571c436964d1460`; its decompressed payload SHA-256 is `79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c`.
- The M3 delta-eighth and M4 delta-quarter archives are the construction provenance for that bank. They are listed to preserve the proof chain; the current loader consumes the archived complete compilation and does not rerun those constructors. Native `stage80/RESULTS.json` belongs to the older optional `load_frozen_bank` path and is not substituted for this actual t=4 bank.
- `check_matched_cost.py` also reads this round's `COHERENCE_SKIP_RESULTS.json.gz`, which is current package evidence rather than an external historical dependency.

## Native core and bundle

The complete native stage tree is restored from the Git bundle snapshot `0852cad130c1d877174d235687cf60c19f318c58`. The currently read checkout is clean, and seven selected native files were checked against the tracked Git blobs at that snapshot. The bundle is described by the immutable [general HANDOFF](https://github.com/awdawmip/enterprise-math/blob/1fb7ff99d205f9ca03772942be64f732553dcd86/research_notes/directed_recovery/20260926_C6438C/HANDOFF.md): Google Drive file ID `1ox9qTtXGbN0p6Zma29uXtBXM6FcOOXhV`, 61,398,315 bytes, SHA-256 `a0eb15a32c4db5a9fd0876f64a0ffd8dbedcd5eabb2a148c247a8886836e5a9c`. This external bundle must be available to restore the native tree; an EM-only download of this round is insufficient.

The vendor core is also independently pinned to the canonical EM [brc_weighted_recurrent.py](https://github.com/awdawmip/enterprise-math/blob/bc7babbb9e890f6d5a7094430a5fbdccf66c77ad/src/enterprise_math/brc_weighted_recurrent.py) at `bc7babbb9e890f6d5a7094430a5fbdccf66c77ad`, Git blob `4e6b3132580e3cd70a20a0d8bd4d28792b961afb`, SHA-256 `7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26`. `stage45.brc_loop_recheck.verify_vendor` guards that byte identity. The surrounding stage packages provide the typed observers, fixed phase words, arithmetic and readers; the core alone is not their replacement.

## Restore and verify

1. Restore the full native bundle at the specified snapshot, retaining every stage package and vendor file. Verify the bundle digest, checked-out commit and selected native hashes.
2. Restore the terminal foundation, general foundation, compiled-word package, direct-word bank and optimization package, then qft_row_queries and qft_approximation, from the immutable manifests in that order. Overlay only the named published subtrees; do not replace later source files with older copies. The JSON selects the authoritative source version for each actual imported file.
3. Recover required binary inputs byte-for-byte using each historical manifest's exact part/chunk order and hashes. Some archives are represented as binary parts or readable base64 chunks; reconstruct the original bytes before testing gzip and payload digests. There is no need to duplicate large prior Gram/walker experiment results into the current archive merely to document their provenance.
4. Preserve the sibling directory layout under a common `TEMP` directory: `sep26-shor-alternative`, `sep26-shor-general`, `sep27-qft-research`, `sep27-qft-approx`, and `sep27-qft-coherence`. Keep the native tree under `sep26-local-takeover/intake_brc/stage87-source`. Imports derived from `__file__` depend on this layout.
5. Set the source environment paths explicitly to the restored locations, especially when using a base other than the historical Windows defaults:

```text
BRC_STAGE87_SOURCE=<TEMP>/sep26-local-takeover/intake_brc/stage87-source
BRC_ZERO_ENDPOINT_SOURCE=<TEMP>/sep26-shor-alternative/adversarial/zero_endpoint_extension.py
BRC_STREAMING_PREVIOUS=<TEMP>/sep26-shor-alternative
```

6. Validate all selected source and bank hashes before invoking the existing current checkers. Preserve line endings and JSON bytes because certificates bind exact source hashes. The historical command used `D:/kimi-query-bridge/.venv/Scripts/python.exe -X utf8`; this documentation step does not certify a newly installed Python environment or newly restored execution.

The selected-file index makes the actual dependency path reviewable. Full historical manifests plus the complete native snapshot preserve the transitive source closure; the selected list is not a promise that those selected files alone suffice. No scientific code was imported or executed while creating these two dependency documents, and no frozen scientific source or raw evidence was changed.
