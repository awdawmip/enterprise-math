# X6 signed original S6 rotation regression after Boolean-axis repair

Research status: AUTHOR-EXECUTED_ORIGINAL_REGRESSION / EXACT INTEGER / NOT_REVIEWED / NOT_ADMITTED.
Parent Task: RS-X6-LEGACY-PLANE-RECONCILIATION, publication TP2-B4A441B23DA3159232C2.
Foundation: frozen P000 V5, original scientific baseline 59538f585d037d09ef687b28715c4bc1a3f9fe03. Historical comparison fd2bcff10ca6e147348b6c1236027fc0d2877df3.

## The original source, not a substitute checker

Original script executed as-is in Python from a repository-shaped local directory:

  experiments/x6_signed_native_spatial_v16_20260905/check_x6_signed.py

with direct imports from the original matching file x6_signed.py. A sibling signed_brc.py was also present without changing the checker's source or assertions. Each local file was reconstructed from the authorized GitHub connector's complete current-main content and checked against the source Git blob SHA1:

- check_x6_signed.py: blob 83c5ed026c41360696019f2a1d92d3db41910295, 6128 bytes, SHA256 258cdc9ec68eeca2c0ecfaeec3b10ad4af1bbe7019b4efd7edb2751fe1cbafcf.
- x6_signed.py: blob 405d9bc752bbf45582f2d0a6d9f91bff9cc5f89e, 6308 bytes, SHA256 3ff8e757a2752267b450c587ccc978b3c531abc6ff33f4babf2b3c49ab9b8d56.
- signed_brc.py (sibling, not imported by this checker): blob 300a96e3dc24bf6fff73743037a0347a8bc83176, 2852 bytes, SHA256 6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4.

Actual command from the original script's directory: python check_x6_signed.py.
Actual exit status: 0. Captured unmodified stdout:

```text
PASS_X6_SIGNED_NATIVE_SPATIAL_V16
checks= 56510
full_translation_group=Z^6
primitive_signed_neighbours=12
joint_positive_slice_kernel=Z*(1,1,1,1,1,1)
relative_observer=Z^6/Z*1
full_diagonal_norm_squared=6
length6_balanced_positive_paths_to_diagonal=720
full_positive_return_nontrivial=false
```

This is specifically the post-S6-rotate Boolean-axis guard source revision, not the earlier 56502-check pre-rotate original regression. Assertions cover invalid Boolean axis permutation rejection, signed primitive neighbors, all S6 axis permutations, source-relative observer and BRC-related counts. Native direction and axis-index exact type checks remain in the current actual module. This is a successful original check under Python's default assertion-enabled mode, not a formal admission of the broader 28-LP reconciliation.

## Next exact unfinished original regression

The distinct original coordinate-completion checker remains PENDING_EXECUTION in this author certificate:

- experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py Git blob d562df4cedf3aa54fd3ca5db5ee0d17ff873a752.
- Its original direct dependencies include x6_coordinate.py blob 9738543aace13f8a72af577e9ad8964c5fd40de8, x6_signed.py blob 405d9bc752bbf45582f2d0a6d9f91bff9cc5f89e, signed_brc.py blob 300a96e3dc24bf6fff73743037a0347a8bc83176, and six_axis.py blob 2a16d04bd6c5e6d50e0fdd20e455f854b71bdcf4.
- Recover exact full current sources and execute the original script unmodified; record actual stdout, count, exit code, exact Git blobs, and any errors. Do not treat the earlier 58999-check version as post-S6 execution.

## Link to parent objective and source state

The earlier source audit of eight frozen BRC programs and semiring support conditions is published at research_notes/X6_LP011_LP019_FROZEN_BRC_SEMIRING_SOURCE_BOUNDARY_20261113.md (commit b16492e4be64852cbaadc6f4da548cb129deaf7d); original Research Activity checkpoint #16 is saved at a8e75c7ba3012cb4b59d3ffb4b67897a8b48bb27. The frozen LP011 wrong native argmax and LP019 wrong positive-N-BRC signed-cancellation callers remain UNRESOLVED_PROVENANCE.

Same original Research lane: chatgpt-research-onhour-enterprise-math-20260923; Researcher EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034. Fresh exact task read request onhour-20261113-2359-x6-task-read-guard-v2 succeeded: state HANDOFF_READY, dispatch NEEDS_DISPATCH, claim_id null, execution_authorized false. No new native CLAIM, semantic PROGRESS or independent review is inferred from this GitHub author's execution certificate.

The remaining mother objective is exact historical wrong-caller provenance and all 28 LP dependencies, with an independent Driver REQUEST_REVISION. Original frozen science pins, prior completed native G25 and PathSqrt results, and prior owner contributions remain unchanged.
