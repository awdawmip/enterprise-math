# Exact audit containment for one directly superseded Result

Status: `CONTROL_PLANE_ONLY / LOCAL_VALIDATION_PASS / MAIN_ADMISSION_PENDING`

The immutable Result `RR-68BA014D54542DA7221C` belongs to task
`RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE`, publication
`TP2-D425335E9566A3F6A54C`. Its same-task Gen2 publication
`TP2-75A6C3F81E2D094B67CF` directly supersedes that Gen1 publication.

This change appends one row to the existing superseded-publication audit
registry. It uses the existing validator without changing the Result API,
replacement edges, dispatch, Driver disposition, theorem status, or source
records. Both preceding registry rows retain their exact text bytes.

The exact Result Git blob is `sha1:c6d4806e9b5d353b54fbc42048aabd3279f7adc3`.
Its pure strict audit reports exactly these three errors:

- `invalid method_harvest`
- `invalid independence_status`
- `invalid source_exposure_status`

Only those complete, exact-path errors are contained. An additional error
remains a failure; disappearance of any registered error makes the row stale.
This historical containment does not establish current operational authority
for an explicitly queried old generation or resolve any mathematical result.

Validation on the integration checkout based on main
`6d152bcb244b61ab1602f1e564ebd7f037a04302`:

- Existing validator accepts all three registered rows.
- The pure per-Result audit produces exactly the three registered errors.
- Eleven Result, execution, publication, and manifest source files remain
  byte-identical to that main snapshot.
- Six regression tests pass after the complete canonical bootstrap. They cover
  actual direct lineage, additional and missing errors, immutable byte drift,
  other-task/indirect/nonincreasing successors, and Result identity mismatch.

Reproduce the focused regression with:

```console
python -m unittest tests.test_superseded_result_audit_boundary_20260907
```

The complete reference gate remains pending the separate invalid-review and
invalid-Result authority repairs. This unit is neither a blanket error waiver
nor a claim that step 24 or the full quality matrix has passed.

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@ad23151 / GLOBAL_KNOWLEDGE_V1
