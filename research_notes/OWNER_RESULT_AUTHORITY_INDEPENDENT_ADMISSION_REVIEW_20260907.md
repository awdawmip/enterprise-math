# Independent admission review of exact Result authority isolation

Status: **PASS for the frozen bounded combination; no blocking findings.**

This is an independent implementation review of the ten paths in the Result
authority unit, performed against the local integration tree at
`2dd4c296f713f6bb3b2e509ba65104dc4a2a8ce0` plus the frozen, uncommitted control
delta. The four Result-derived follow-up paths were written by this reviewer in
an earlier bounded unit. They received combination and preservation checks here;
this note does not present those four paths as independently reviewed original
work. No implementation, registry, mathematical source, test or existing note was
changed during this review. The only repository addition is this note.

The ten-path author manifest is
`TEMP/owner-result-authority-isolation-20260907/frozen-sha256.json`, SHA-256
`65764cfcaf110fb40559e4bf5842dbfbd26e5fd6b0f0150212526429af6791ac`.
All ten hashes matched. All fourteen input paths matched again after the actual
tests and public-view comparison. The combined input-hash manifest is preserved
in the independent evidence directory below.

## Implementation findings

The public Result facade validates ordinary replacement edges and removes their
predecessors before invoking Result authority isolation. The actual replacement
`RR-BFB7190B3C8D391C6E9D -> RR-AE11E20304C60C349CBD` remains present, and BFB
remains absent from the operational Result map after AE11 is withheld.
Same-execution recovery requires the ordinary validated replacement chain; an
independent execution on the same publication is not treated as that replacement.

The registry validator requires canonical Result/publication/execution paths,
one exact raw-store occurrence per registered Result, complete dependency and
derived-Review sets, exact source bytes, exact strict errors, and false authority
flags. Historical legacy diagnostics remain distinct from raw strict errors.
The three legacy execution IDs remain absent from the canonical execution map.
The ContextVar snapshot is scoped to one reduction and rechecks input inventories
and bytes on exit. It does not create a durable authorization cache.

The final Review adapter uses a marker on the current function. A later bootstrap
facade replacement therefore triggers recomposition instead of retaining a stale
module marker. The fresh-interpreter regression installs Result isolation before
full bootstrap, repeats bootstrap, and verifies that the held Results and their
Reviews remain absent. The public diagnostic cause union may retain overlapping
causes explicitly; the temporary legacy Driver union excludes Result-only causes.
The explicit Result follow-up basis cannot be relabeled Driver or Review-audit
authority.

Dispatch preserves authenticated pre-freeze CLAIM evidence while blocking new
control events that would restore the held generation. Ordinary execution,
canonical claim binding and stale adoption consult the current exact generation.
Lane execution and adoption consult the lane's own immutable publication. A
cohort containing only held-generation lanes stays blocked. The mixed-cohort test
actually authorizes an independent retained publication lane through
`tools.research_runtime_guard.authorize_execution`; the held lane remains refused.
These are real guard calls with production validators, not mocked acceptance.

## Independent execution evidence

Python 3.12.14 ran full bootstrap before importing the suites through the actual
`scripts.run_unittest_shard.load_file_suite` loader. The frozen final combination
passed **65 tests**, zero failures, errors or skips, in 74.688 seconds including
bootstrap:

- exact invalid Result authority: 19;
- Result-derived follow-up combination: 14;
- frozen pure Result audit completeness: 10;
- ordinary Result replacements: 7;
- cohort dispatch overlay: 4;
- runtime lane authority: 6;
- runtime claim authority: 5.

The original step24 command
`python control_plane/check_result_review_binding_fault_isolated.py` independently
returned exit code 0. Its counts were binding Reviews 1, invalid Reviews 25,
superseded Result audit rows 3, and withheld Result authority rows 12.

The separate public-view comparison used the exact same public APIs as the fixed
2dd baseline, including the Review-keyed `research_driver_followup.packet_map`.
It did not drop legacy packets merely because they lack `packet_id`.

| Public view | Fixed 2dd | Reviewed combination | Exact removals |
| --- | ---: | ---: | ---: |
| Result map | 161 | 149 | 12 |
| Review map | 117 | 113 | 4 |
| Packet map | 105 | 100 | 5 |
| Current publications | 153 | 149 | 4 |
| Task definitions | 193 | 193 | 0 |

There were no added or changed surviving Result, Review, packet or current
publication rows. Exactly five declared derived-task definitions changed to
`BLOCKED` with `publication_id=None`; the other 188 definitions were equal to
the fixed baseline. The fifth target publication was already noncurrent.

All **114 distinct source paths** matched their registered Git-blob and SHA-256
pins and the immutable 2dd source bytes. Of these, 104 had hashes in the public
baseline. Ten already-isolated historical sources were intentionally absent from
that public baseline's source inventory, so their bytes were independently read
from local `git show 2dd4c296:<exact-path>` and compared. No remote access was used.
The twelve rows account for 32 raw strict errors.

The clean same-publication Result `RR-00F7FFAA06553D90B4AC` passes the strict
Result audit and is actually selected by the public `task_result_state` as
`AWAITING_DRIVER_REVIEW`, with `terminal=false`. This preserves its legitimate
review route without manufacturing a Driver disposition or terminal completion.

## Reproducible evidence and limits

Independent evidence directory:
`C:/Users/Administrator/AppData/Local/Temp/owner-independent-result-admission-20260907-alnnnsbh/`.

| Evidence | SHA-256 |
| --- | --- |
| `input_hashes.json` — all fourteen frozen inputs | 408c2d674ea205f893555aaf3504012a306e053a8d1adeacd79880ffb4ee67fd |
| `unittest-65.log` | 6f07d8466f2d4c245623cdb4acd52af94a1f90d1cb6001a49b50f29cbbcd1cf7 |
| `step24-cli.log` | 030fbba700a0ec65c29015d26075b7b09f3d27603d02f741e0d03d4e648aefb5 |
| `independent-public-delta.json` — exact identities and 114 pins | 1dd39dfa4b00494033909ad34d370c2c0dbf3e83632d293c5af8b9c6c08fdaef |
| `public-views.json` — complete observed public rows | fa279d865bb637e311662960953537f2dfd5bb35f87642b4a7c27bb717e6dc9b |

The fixed baseline file is
`TEMP/owner-control-step24-2dd4c29-20260907T141855Z/public-runtime-baseline-2dd4c29.json`,
SHA-256 `8b6a53cdabce6dea91624a4bf621d5caa8a043c3b67b7bb6c9bf1ab8f34de991`.

This admits only the exact frozen control combination to the owner's next
integration decision. It is not a formal Driver review, mathematical promotion,
claim, full reference-gate pass, eight-shard CI pass, remote merge or deployment.
No commit or push was performed by this reviewer.

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE

Global-Knowledge-Sync: main@ad23151 / GLOBAL_KNOWLEDGE_V1
