# Standalone Driver-authority gate uses canonical bootstrap

Mode: `CONTROL_PLANE_MAINTENANCE`
Base: `3f3cf31fdd9fc86505ad3e1e7a7f207f754cc6ce`
Global-Knowledge-Sync: main@990d7c1 / GLOBAL_KNOWLEDGE_V1

The actual reference workflow reached step 25 and failed with 17
`driver_authority_record_id does not pin active authority` errors. The frozen
source remained intact. The standalone checker installed only stale-binding and
review-audit isolation, omitting existing Driver-authority compatibility and the
canonical Result-dependency view.

One bounded diagnostic cycle separated the 17 records using their real source
bytes, authority event at `reviewed_at`, raw/normalized authority IDs and independent
source-comment pins. No review disposition or authority record was rewritten.

| Existing cause or compatibility | Records among the 17 | Effect |
| --- | ---: | --- |
| Byte-pinned historical raw authority ID with matching active event and source comment | 11 | Existing compatibility accepts the exact alias; 9 remain operational and 2 separately lose authority through exact Result dependencies. |
| Missing authority pins already in the exact Driver quarantine addendum | 5 | Existing quarantine removes these reviews from the operational view. |
| Review `DR-1337737608BDE3D7E621` derived from an independently withheld Result | 1 | Existing Result isolation removes operational review authority; it does not certify the review's Driver pin. |

The observed error counts were **17 -> 1 -> 0** after installing existing Driver
compatibility, then the complete existing bootstrap. Operational review counts
were **122 -> 117 -> 113**. Authority at the original review time, alias identity,
and source-comment identity are distinct checks. Current operational membership
does not rewrite or validate a missing historical pin.

The production change is confined to
`control_plane/check_driver_review_authority_fault_isolated.py`: it invokes the
existing canonical bootstrap before the existing strict isolation audit. The
contract check, `valid_records`, empty-authority-record rejection and final
`isolation.audit` are preserved. No validator, adapter, quarantine registry or
authority rule is relaxed or added.

In particular, valid Result `RR-00F7FFAA06553D90B4AC` remains operational. Its
missing-pin review `DR-98D79A8522754B43637A` stays in its pre-existing exact Driver
quarantine. A Result fault is not treated as proof that every related review has
invalid Driver provenance; those causes retain their separate validators.

## Validation

The unchanged workflow command
`python control_plane/check_driver_review_authority_fault_isolated.py` exited 0.
Python 3.12.14 then ran 22 related tests successfully in 123.194 seconds: 7 new gate
tests, 9 existing Driver-authority tests, 4 existing Driver-control isolation tests,
and 2 existing Result-binding tests.

Fresh processes test gate-first and bootstrap-first installation followed by
repeated installation. Their complete views match: 149 Results, 113 reviews,
100 packets, 149 current publications and 193 definitions. The packet comparison
preserves the full list, including historical entries without `packet_id`. These
counts describe this validation snapshot; they are not permanent repository-size
contracts.

After that 22-test run and its independent review, two assertions that fixed the
repository's total size were replaced with nonempty-view assertions: the new
gate-order test's five view counts and the earlier integrity/followup-order
test's definition count. Both tests still compare complete views across the two
fresh installation orders and repeated installation. The integrity/followup test
also retains its exact composed-cause checks; its two-source shared packet and
two-installation-order assertions remain unchanged. The first-order helper has
no additional repository-size assertion. Legitimate additions from other
research branches therefore do not invalidate these order checks merely by
increasing the repository size.

Only the two affected methods were rerun on this final test delta: **2 tests
passed in 188.083 seconds, exit 0**. The earlier 22-test and 53-test results remain
evidence for their original inputs; they were not rerun or relabeled as final
input runs. `run-growth-safe-order-methods.py` records both complete test names
and the loader invocation. `growth-safe-frozen-sha256.json` records the final four
owned files separately from the preserved earlier `frozen-sha256.json`.

Another fresh-process fixture first passes the real CLI using an exact copied
authority alias, then fails with the original strict error after an unregistered
review's source-comment pin is changed. Other negatives retain rejection of
authority source-byte drift, normalized-ID drift and quarantined review-byte
drift. No source validator is mocked. The known-quarantine fixture changes only
the checker's input root. Existing tests also cover revocation, backdating,
unauthorized server actors and edited authority events.

All 223 protected source/registry/validator files match their before-run SHA-256
values. The earlier Result-authority package's 10 files also match exact base
commit bytes. The first test attempt is retained: it exposed a test snapshot's
incorrect `packet_id` assumption and a misspelled old test-module name. Fixing the
test harness did not change production semantics or remove a boundary assertion.

Evidence directory: `TEMP/em-step25-cause-r4qvulbc`.

| Evidence | SHA-256 |
| --- | --- |
| `cause.json` (17 -> 1 -> 0 with exact review/authority pins) | `ec15cbc1e8ae7d98c13f690b1d4a2749f69891eae1786829e5c6fae27d2532c7` |
| `focused-first.log` | `0123c129f005944525dc05ca90ea8e67d6ab56f87d7f90aca0db740bc007f972` |
| `focused-final.log` | `696b5cfdf0c840e47a182c6fe954ab27daedd8adc5d0a9502557e729135f6f6c` |
| `step25-final.log` | `32f536a6a169376835f3ec1de2a2ead4845ee927f0904e538ea4d211b56c12a1` |
| `source-before.json` and `source-after.json` | `32f77927fa7f54a04c267c4a2fdd3e7be4fd5eb20fd81c16b7b452e422f90915` |
| `protected-result10.json` | `d0de82a987a94eb9d2acce0c5d737ca1c727054f86e7ca330a73ad7630beaf91` |
| `growth-safe-order-methods.log` (two affected methods only) | `cb4b12cae933905e5534a0ce96bca44a47e5092e40ac4c6b253ba64ffc08c3c9` |

`run-focused-tests-final.py` retains the exact bootstrap and module-loader command.
The original step-25 failure is in
`TEMP/em-ref22-3f3cf31-bte4eufg/25.stdout.log`, SHA-256
`88d9965f0393e09162e3063257c96702b2624e4b76bd4b5630e0e2055ae4584f`.
This is bounded step-25 repair evidence. It does not claim a new full reference
workflow or eight-shard quality run; original steps 26-34 remain for continuation.
