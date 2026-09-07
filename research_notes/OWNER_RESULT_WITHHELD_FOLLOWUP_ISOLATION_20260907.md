# Exact Result-derived follow-up control isolation

This bounded change withdraws operational authority from five additional exact
`TASK_SET_PUBLISHED` packets whose source Reviews derive authority from frozen
Results in the independent Result control-authority quarantine. It preserves all
Result, Review, packet, publication, taskbook and Driver-disposition source bytes.
It does not amend mathematical conclusions, create a claim or replacement, or
grant working truth, Foundation authority, canonical promotion or a successor.

The intake checkpoint was
`2dd4c296f713f6bb3b2e509ba65104dc4a2a8ce0`. The exact manifest SHA-256 is
`30719e344b093760420ad20e833d2918c729b305f1fd83e1b98978b5602e4a63`.

## Source basis and complete packet sets

`research_driver_followup_fault_isolation.validated_quarantines` now recognizes
the explicit `RESULT_CONTROL_AUTHORITY` basis and calls
`research_result_authority_fault_isolation.validated_review_rows(root)` directly.
The source adapter validates the frozen Result, complete raw strict error set,
exact dependency bytes, and complete derived Review set. The new basis requires
an explicit `source_packet_ids` list even for a singleton. Existing packet,
publication, taskbook, active-head and complete-source checks remain in force.
An additional source is an unresolved authority change; it is not silently
accepted as a valid replacement source.

Exactly five rows were appended to the follow-up registry. The original ten rows
and outer registry fields retain their original text. Each new row has one
explicit source packet and one derived publication:

| Packet | Source Result | Exact derived publication |
| --- | --- | --- |
| DFU-B6A7EAFE760B531C3495 | RR-012E775840E54D36F41E | TP2-4E118647826FFB47BA2C |
| DFU-1337737608BDE3D7E622 | RR-1337737608BDE3D7E620 | TP2-3F7A91C4E82D105B6A38 |
| DFU-7D5F26937C1F108DCFB3 | RR-234ABD5082081CEBAB05 | TP2-875D6C62E617BCC7CE63 |
| DFU-83B1D6E4C9027A5F3148 | RR-4B7576B2FDCA2CCBAB37 | TP2-5D9C21A7B40E683F1C52 |
| DFU-060A48D8E81818A33864 | RR-5F80FBDB98CAA0E43177 | TP2-C74E704488CBF01A602D |

The manifest's other four packets retain their existing invalid-Review-audit
rows: `DFU-E79D7C72DF1A2D5137F5`, `DFU-07F2C626AB51FAADD478`,
`DFU-6D3A91B84E205FC713A9`, and `DFU-9D7E05C41A682BF330D7`. Their existing
shared-publication source set or strictly empty closure-only task sets are not
duplicated or reclassified.

The new Result adapter/module, its registry, and the public runtime activation
belong to the companion Result-authority unit. They must be integrated together
with this follow-up change. The old temporary Driver source union must continue
to exclude Result-only sources; a separate diagnostic union may compose the
independent causes explicitly. A missing or stale Result source fails closed.

## Observed preservation and authority withdrawal

The full-bootstrap before/after comparison verified 39 related packet, Review,
review-artifact, publication and taskbook files against both Git blob and SHA-256
pins. All were unchanged. The independent Result validator also validated its
12 exact Result rows and 11 derived Review rows.

All nine manifest packets are absent from the operational packet view. The
actual new packet-view delta is exactly the five appended packets. Of 193 task
definitions, exactly the five declared derived tasks changed to `BLOCKED` with
`publication_id=None`; the other 188 definitions are equal to the intake view.
Four current publications were newly removed. The fifth target was already
absent from the current-publication view, and is now explicitly blocked by its
follow-up source quarantine. Unrelated current publications are unchanged.
The registry now validates 15 packets and 12 distinct derived task publications.

## Validation and retained failure evidence

Tests use Python 3.12.14, actual `research_control_bootstrap.install(root)` before
test imports, and `scripts.run_unittest_shard.load_file_suite`. Temporary fixtures
copy one canonical source Result's exact dependency files and use the production
validators. They do not mock a validator or publication selector. The unrelated
semantic-integrity fixture also satisfies its real validator.

The first 12-test run exposed a genuine cross-basis composition defect:
`test_result_basis_cannot_be_disguised_as_driver_or_review_audit` did not raise
when a Result-only source was relabeled `DRIVER_REVIEW_AUTHORITY`. The companion
adapter had inserted Result-only sources into the temporary Driver union. Its
owner fixed that implementation; the refusal assertion was retained. A later
13-test run passed, but it preceded the final same-execution recovery boundary.

The first 55-test combined run then retained this exact error:
`same-execution recovery lacks validated replacement authority`. The newly
activated Result gate requires ordinary validated replacement authority when a
new Result reuses the withheld execution. The original same-execution fixture is
now an explicit refusal test. The positive sibling uses the same task and
publication with an independent canonical execution, claim and branch. Its
strict Result and Review audits pass, and its Result, Review, packet and READY
derived task remain operational. No production recovery condition was weakened.

The final stable-interface combined run passed **56 tests**, with zero failures,
errors or skips: 14 new Result-follow-up tests, 16 prior source-set tests, 17
Driver-follow-up tests, 2 immutable-baseline tests, 4 Driver fault-isolation tests,
and 3 review-write-authority tests. Total bootstrap and test time was 47.141
seconds. This verifies the bounded combination, not full CI or all reference
gates.

Local evidence directory:
`C:/Users/Administrator/AppData/Local/Temp/owner-result-followup-isolation-20260907-1vg6fmud/`.
Earlier logs were retained without overwriting:

| Evidence | SHA-256 |
| --- | --- |
| `run-udcxh43o/unittest.log` — first 12 tests, one cross-basis failure | a8ecb6a553c7e895daf987c2c4557995a101d080f2d35e7870442b3f6dc6806f |
| `run-7ex2wqa5/unittest.log` — interim 13 tests passed | ec70f60af243554dcf8b4094b6c8556055607d91c4e4b973efee62f34c19e53a |
| `run-dhfu951u/unittest.log` — 55 tests, one same-execution error | 433765e1235c357f8eff825a6261f6a47327988067dd930543b29d6f1db80da0 |
| `run-qcapsubn/unittest.log` — final 56 tests passed | 8f73e99348588ef9a40b4221cac08ac6dc718bd7332656f0edf50e34eac658c1 |
| `preservation_verification.json` | b03d8670fc071673193fcc7af73942a1f4fc70f02ac3b35f3f355d3eb7eba3bc |

Final implementation SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `control_plane/research_driver_followup_fault_isolation.py` | dba941c89797cc7a0a1730d05f774c203f77f00c3239b81e003498b3d993173d |
| `research_driver_followup_authority_quarantines.json` | f0f0c4fe139acc560603e5b6a22e794048dee98d132e69b27298138233319b45 |
| `tests/test_result_withheld_followup_isolation_20260907.py` | ebdae8d22ef78cd59f70acbc33fa74ece13ff46c47f0db1a6242b399a497a65e |

Only the follow-up module, follow-up registry, new test and this note belong to
this bounded unit. The unit made no Git commit or push; the owner controls the
combined integration and publication checkpoint.

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE

Global-Knowledge-Sync: main@ad23151 / GLOBAL_KNOWLEDGE_V1
