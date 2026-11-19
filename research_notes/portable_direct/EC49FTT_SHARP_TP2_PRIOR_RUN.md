# EC49FTT — Actual validation and preservation record

Date: 2026-11-19 UTC. Scope: external smooth correlated price-prior postprocessing of the frozen BRC16943 author-optimum; no native 228-observer Bellman rerun.

## Executed exact arithmetic

Command on the local source file:

    python /mnt/data/EC49FTT/EC49FTT_SHARP_TP2_PRIOR_VERIFY.py

Actual process: exit code 0. Its standard-output JSON is published as EC49FTT_SHARP_TP2_PRIOR_CERT.json (1190 bytes, Git blob 238a5a95750016ca81ccff0393aad257795347b7). The source program was directly checked byte-for-byte against its remote Git blob 4b904c4fe6348995539029373e5cee245b4d31a4 (3576 bytes). These are concrete readbacks, not inferred from PR existence.

Assertions covered: exact 27/64 interval length; sharp threshold 171167905504400/63545784776721; rational coefficient decomposition against independent direct B0/A0; 64 strictly interior fractions; monotonicity of r0' at sampled points; four strictly positive TP2 determinants; exact top-atom reversal at lambda=3, p=2939/128<q=735/32. The universal result is proved symbolically in the accompanying note and the sample checks are diagnostics.

## Source / research-control separation

- Native frozen input: enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab, inherited from PR #2774 (AUTHOR_PROVED / NOT_REVIEWED).
- Direct external-prior parent: EC49FTS PR #2797@7dcff5e1e3713ac34f57484563ab6cdc57b9dd9a.
- Actual GitHub issue bridge read for RS-EC49AS: [Issue #7015](https://github.com/awdawmip/kimi-query-bridge/issues/7015#issuecomment-7002832746). Original request r4-ec49ftt-20261119-task-read-01 returned SUCCEEDED/NO_CANONICAL_PUBLICATION_DIRECTORY, observed 2026-11-19T07:34:53.680695+00:00 at Source 5a0b6ff2040cbbae5ca9b28ded3590658e11e893. That result is a pinned directory absence, not a complete active-owner projection. Existing formal CLAIM and execution authority were not established. This work was independently preserved under authorized GitHub rights without new native Task/Result/Review or Activity mutation.

Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED. Next scientific unit: vary the continuous TP2 kernel together with the clipping atom, or revisit native z<11/16 Bellman strategy phases using actual frozen original-index evidence.
