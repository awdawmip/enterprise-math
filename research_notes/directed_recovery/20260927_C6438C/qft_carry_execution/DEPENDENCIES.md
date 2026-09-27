# Immutable source and restoration chain

The current package adds the two-carry executor, typed complete alias
discovery, bounded checks and whole-period aggregation work. It uses the
existing complete native phase bank and execution chain; it is not a
standalone runtime distribution.

The authoritative historical dependency index is
[DEPENDENCY_MANIFEST.json](https://github.com/awdawmip/enterprise-math/blob/6370e937d3cea8b957ac2d66d0bd6a42f385f9ee/research_notes/directed_recovery/20260927_C6438C/qft_coherence/DEPENDENCY_MANIFEST.json),
SHA-256 `247b58caf177a9b12117898e6966128bce04a56c62a2ae8343c44e0a05808016`.
Its companion
[DEPENDENCIES.md](https://github.com/awdawmip/enterprise-math/blob/6370e937d3cea8b957ac2d66d0bd6a42f385f9ee/research_notes/directed_recovery/20260927_C6438C/qft_coherence/DEPENDENCIES.md)
describes the full transitive restoration, exact binary reconstruction,
native source bundle and configurable source paths. Current scientific
payloads additionally pin the actual imported sources before/after their
runs. The historical index is referenced, not represented as a new execution.

Key immutable layers in `awdawmip/enterprise-math`:

- Two-carry proof: commit `469b16d9c7db1993c1d793fb2601fd3b1669a88b`,
  `research_notes/directed_recovery/20260927_C6438C/qft_dyadic_carry/`.
  `DYADIC_CARRY_CORRELATION.md` SHA-256
  `70b35a57ee0ffe628b2090f0ddeb0a7bce7eb076a03b627ca10ba8e1f815f3d1`.
- Gram, streaming, lazy modular arithmetic and exact carrier codec:
  `0e6380ff74d31b842ba0b54802c1f0595a7dd60d`,
  `research_notes/directed_recovery/20260926_C6438C/optimization/`.
  Gram source SHA-256
  `468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9`.
- Complete compiled phase bank: `9348fc6abdf45becbd12a8019d93f72d576b9fab`,
  `research_notes/directed_recovery/20260926_C6438C/direct_word_integration/DIRECT_WORD_INTEGRATION_RESULTS.json.gz`.
  Gzip SHA-256 `ef981768a20a72a67bfd7d01284d1b946cfc95ded96552a07571c436964d1460`;
  payload SHA-256 `79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c`.
- Compiled words: `8d4e9c12f7492316b825e96423bc0ee36ccdee22`;
  general foundation: `1fb7ff99d205f9ca03772942be64f732553dcd86`;
  terminal foundation: `b6625778e869511d85a202a0839eb105a197659e`.

The actual native stage tree comes from the separate Git bundle snapshot
`0852cad130c1d877174d235687cf60c19f318c58`, not an EM commit. Its Drive file
ID is `1ox9qTtXGbN0p6Zma29uXtBXM6FcOOXhV`, 61,398,315 bytes, SHA-256
`a0eb15a32c4db5a9fd0876f64a0ffd8dbedcd5eabb2a148c247a8886836e5a9c`.
The vendor core is also pinned at EM `bc7babbb9e890f6d5a7094430a5fbdccf66c77ad`,
`src/enterprise_math/brc_weighted_recurrent.py`, SHA-256
`7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26`.

Existing execution restoration keeps `sep27-qft-carry-execution` adjacent
to `sep26-shor-general` and the other historical directories described in
the linked chain. This layout records how the saved checker resolves its
imports; it does not make that operating system or local path a prerequisite
for further mathematical research. Read the proof/evidence and continue
derivations on any available platform. New executions should retain their
own actual source correspondence and complete evidence.
