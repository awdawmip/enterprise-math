# Immutable dependencies and reconstruction

This package extends the frozen carry execution package at Enterprise Math commit `8e2f54ce5581636b9169845a54f018c25d00b165`, prefix `research_notes/directed_recovery/20260927_C6438C/qft_carry_execution/`.

Its [DEPENDENCIES.md](https://github.com/awdawmip/enterprise-math/blob/8e2f54ce5581636b9169845a54f018c25d00b165/research_notes/directed_recovery/20260927_C6438C/qft_carry_execution/DEPENDENCIES.md) links the complete transitive source chain, native bundle and exact binary reconstruction. Its [PUBLICATION_MANIFEST.json](https://github.com/awdawmip/enterprise-math/blob/8e2f54ce5581636b9169845a54f018c25d00b165/research_notes/directed_recovery/20260927_C6438C/qft_carry_execution/PUBLICATION_MANIFEST.json) binds the frozen implementation and evidence. The corresponding verified Drive bundle is file `1YzDgpP0Ns5Vk0m6Olx12aPPR4-uNguAI`, 3,883,772 bytes, SHA-256 `8a24a1d8fe83a89dd300d25e8b7d10de07c82eab6cc7fcca79cb527342fb0ae7`.

Direct source bindings:

- carry_executor.py: `f017b1fb1516e8faa97afd39d663e4eda6d21cad95f65bb2ccf5a79d7ff3b810`.
- Previous period_aggregator.py: `6f2c855bec09f7cf7fc4853b55ea41f94a195ba3d3b783d18921e9a3b6465f0c`. The new adapter reuses its full contraction core and replaces the O(R) certification boundary; it additionally reduces the routing bit modulo q before typed subtraction, including q=1.
- Lazy modular arithmetic: `08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4`.
- Gram sampler: `468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9`.
- Actual bank payload: `79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c`.

The historical authoritative dependency index is [DEPENDENCY_MANIFEST.json](https://github.com/awdawmip/enterprise-math/blob/6370e937d3cea8b957ac2d66d0bd6a42f385f9ee/research_notes/directed_recovery/20260927_C6438C/qft_coherence/DEPENDENCY_MANIFEST.json), SHA-256 `247b58caf177a9b12117898e6966128bce04a56c62a2ae8343c44e0a05808016`.

Existing checker imports use adjacent directories sep27-qft-oddpart, sep27-qft-carry-execution and sep26-shor-general, plus the pinned stage tree described by the historical index. This records a reproducible saved execution layout, not an environment prerequisite for further research. Pure proofs and full-evidence review can proceed in any conversation; another execution layout must preserve or explicitly rebind the actual sources.

Full new raw gzip evidence is reconstructed by readable_evidence/build_readable_evidence.py --restore after verifying INDEX.json and all chunk hashes. The Drive delivery bundle carries both those text chunks and the exact original gzip bytes. It is a complete mirror of this new unit, not a new distribution of every historical runtime or third-party paper.
