# Directly constructed words in the complete streaming instrument

Status: AUTHOR_ACTUAL_BOUNDED_INTEGRATION / SHARED_CONTEXT / NOT_ADMITTED.
Researcher `EM-DIRECT-C6438C`; activity `RA-CAAAC604CB513AEA8BBC1DFC`.

The two newly constructed phases from `../direct_word_compiler_general/`
have been admitted by the existing complete-word importer and executed in
the declared N15/a2/t4 and N21/a2/t4 full-circuit and streaming routes. Every
joint signed amplitude, terminal control bin and inverse recovery comparison
passed, including an N21 state with strictly positive retained residual mass.
Both routes use the same actual native words; no ideal QFT is executed.

## Imported words and exact error accounting

| Phase | Input artifact | Certified operator error | Canonical word length |
| --- | --- | ---: | ---: |
| m2 | Frozen `swap(0,1); neg(1)`, certified afresh | 0 | 2 indexed native letters |
| m3 | `M3_DELTA_EIGHTH.json.gz` | 1/8 | 8384 |
| m4 | `M4_DELTA_QUARTER.json.gz` | 1/4 | 8112 |

The m3/m4 artifact payloads are pinned by SHA256 before reading their phase
records. The integration calls `verify_phase_record` on each imported record,
then uses unchanged `program_from_compilation` for the complete t4 bank.
Its importer replays every phase record, including the exact quarter, and
the actual complete-word adapter replays all forward/inverse columns and
checks the full Gram matrix. Record word, target, bound, dimension, source,
and hash must agree. All 61 coordinates are retained.

The phase occurrence counts are 3, 2 and 1. Consequently

`E = 3*0 + 2*(1/8) + 1*(1/4) = 1/2 <= epsilon=1`.

The existing telescoping proof therefore supplies the single-terminal
operator/TV bound 1/2 for this bank. The combined bank is an explicitly
assembled collection of certified phase records with this nonuniform error
allocation; it is not relabelled as a previous uniform-allocation search
result. The records themselves preserve their original certificates.

The actual constructor arithmetic, normal vectors, four-square witnesses and
construction cursors remain in the two hash-bound source artifacts. This
integration freshly replays their phase certificates and actual complete
word columns; it does not claim to rerun the entire constructor search.
No legacy approximate seed bank is read to supply m3 or m4.

## Bounded execution result

`check_direct_word_integration.py` and `check_direct_word_n21.py` reuse the
frozen complete-case comparison routine. The full path prepares controls with
actual H4 and applies complete
sparse BRC modular tables, then runs the full inverse QFT with the imported
word bank. The streaming path enumerates all complete histories with that
same bank. The inverse full-circuit run recovers the original prepared state.

| Quantity | N15, a2, t4 | N21, a2, t4 |
| --- | ---: | ---: |
| Complete retained carrier | 61 modes | 61 modes |
| Complete leaf slots | 16, including 12 zero leaves | 16, all positive |
| Joint signed amplitude coordinate comparisons | 976, all equal | 5612, all equal |
| Inverse recovery coordinate comparisons | 976, all equal | 976, all equal |
| Complete control-bin comparison | All 16 equal; mass 1 | All 16 equal; mass 1 |
| Actual BRC core calls in this run | 435 | 244 |
| Calls to the old dense modular compiler | 0 | 0 |
| Original CF success mass at this declared width | 1/2 | 0 |
| Complete terminal residual mass | 0 | Strictly positive |

For N15 the control law is exactly 1/4 on k=0,4,8,12 and zero otherwise. Its
complete terminal state has zero residual mass in coordinates 2,...,60, so
that special input alone is not a nonzero-residual stress test. The second
N21 run closes this bounded coverage gap. Its exact terminal residual mass is

`2557830172007030474820891023747218698966287 / 11417981541647679048466287755595961091061972992 > 0`.

Those occupied residual coordinates are included in the full/streaming
comparison; none is removed or reset. The N21 script reads the already
certified bank from the pinned N15 artifact, then forces fresh complete
certificate and native-column replay through the same importer. In its JSON,
`imported_constructor_artifacts` preserves the original N15 provenance fields;
the N21 run's fresh verification is in `native_word_adapter_bindings`.
It performs
no new approximate phase search and preserves the N15 evidence separately.
The table's 679 total calls are new integration/replay calls; constructor
search receipts remain separately recorded in their source artifacts.

Every individual phase certificate covers arbitrary input in all 61
dimensions. The two complete-circuit comparisons concern the declared
prepared inputs, not an enumeration of every whole-circuit input basis vector.

The inherited comparison routine also performs one declared seeded software
sample and checks its probability against the exact actual terminal law.
That deterministic replay is not a randomness-frequency validation.

The standard t=2*ceil(log2 N) widths are 8 for N15 and 10 for N21. These checks
deliberately use t4 to keep integration bounded. Neither the reduced width
nor E=1/2 is presented as the standard factorization success budget. In fact,
the actual original CF success mass is zero for this N21/t4 fixture, and is
retained honestly in its full law. We do not subtract E from an ideal success
bound and claim a positive general CF lower bound. Single-terminal TV is not
whole-retry-transcript TV.

## Reproduction and retained evidence

The completed evidence can be read without rerunning it. For reproduction in
a separate working copy, the two executable checks are:

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -B -S 'D:/em/TEMP/sep26-shor-general/direct_word_integration/check_direct_word_integration.py'
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -B -S 'D:/em/TEMP/sep26-shor-general/direct_word_integration/check_direct_word_n21.py'
```

The fixed input artifacts and imported compiler/integration sources are
checked against the hashes declared in the script. On another authorized
checkout, preserve their relative layout and the recorded source bindings.
The final gzip retains complete phase records, complete native bindings,
sparse modular certificates, source and terminal states, every streaming
leaf, exact postprocessing, and this run's kernel-call receipts.

| Binding | SHA256 |
| --- | --- |
| N15 script | `c8dd1d00cbb66c540240877c3b45eecce154e86be265809768b4c60082eef7b7` |
| N21 script | `337aaf2e0eff7c24c743fe8b598e19b6bc4da175f87b63d36779d7de8b44a6fe` |
| Frozen compiler | `e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d` |
| General direct constructor | `830b2f0c0c206a53e2b349fe377976d369ebfb76d4dfc5aad494db88ab6e0c63` |
| m3 constructor payload | `0a712b1a918aa7326785605bdbc0e30453962c897286d9e293710f41318858d6` |
| m4 constructor payload | `1a4ca56447d32704376d4537da3e28550800ac4245093d6e303cef4b4918268c` |
| N15 uncompressed payload | `79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c` |
| N15 gzip bytes | `ef981768a20a72a67bfd7d01284d1b946cfc95ded96552a07571c436964d1460` |
| N21 uncompressed payload | `411dc398c1d9d80c275e4ad6bd88e7dbbc228398f7d8bbe1fef955de7c347ae0` |
| N21 gzip bytes | `7999527bc50274e6d4f0f77f6886e6f121be77697c3f2a8e7b3f7151fc41b00d` |

Read `DIRECT_WORD_INTEGRATION_SUMMARY.json` and `DIRECT_WORD_N21_SUMMARY.json`
for compact machine-readable results. The corresponding full artifacts are
`DIRECT_WORD_INTEGRATION_RESULTS.json.gz` and `DIRECT_WORD_N21_RESULTS.json.gz`.
These are bounded author executions under the inherited native-linear/quadratic
observer contract. No efficient classical factoring, physical measurement
derivation, ideal numerical propagation, or independent admission is claimed.
Old fixed-bank and published compiler artifacts are unchanged.

Global-Knowledge-Sync: main@8446003 / GLOBAL_KNOWLEDGE_V1
