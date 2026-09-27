# Actual bounded professional query and archive

Exactly one new standard Scholar/paper_search task was accepted. It used
conversation `01a079d7-5d03-7a21-abe9-f70606fee0ee`, actual turn
`f9a7ffbf-7ca9-4422-aa4d-62665da6257f`, batch
`22c9c4d3-ce6f-409f-af37-fafc27deced4`. The later suggested turn UUID
`51774a59-2dce-44a0-a717-1578dba01d93` was not submitted. There was no retry,
second batch, hidden parallel query or remaining pending handle.

The actual request is [Issue 2497](https://github.com/awdawmip/kimi-query-bridge/issues/2497).
It was created at 2026-09-27T02:23:11Z, accepted at
02:23:17.241380Z, and completed at 02:23:27.283333Z. An actual five-second
wait preceded the first result read; a later complete read at 02:28:01Z
also satisfies the older execution validator's thirty-second requirement.
The original issue body and client request SHA were matched exactly.

Child status is PARTIAL with eight returned metadata records, incomplete
coverage and unknown provider total. The bridge outer state is FAILED;
both are retained without promotion to COMPLETED or NO_HIT. Provider query
calls confirmed=1, unknown=0, bridge Kimi LLM calls=0. Billable calls and
upstream internal LLM calls are unknown, not zero.

KQB_CREATED.json, KQB_FIRST_READBACK.json, KQB_FINAL_READBACK.json,
KQB_ISSUE_READBACK.json and KQB_RESULT.json preserve actual connector output.
KQB_EXECUTION_RECEIPT.json passed the shipped canonical execution validator.
CACHE_GATE_VALIDATION.json reproduces the exact-identity miss across the
then-read 28-entry catalog; CACHE_DECISION.md separately accounts for the
later unrelated quartic PARTIAL record. Reading caches does not renew TTL.

The canonical extraction keeps all eight bibliographic records and actual
status/cost/request/intake fields, omitting abstract snippets and containing
no paper full text. Record state is CONFLICT, observed at
2026-09-27T02:23:20.926085Z and expiring seven days later. The same-query gate
returns CONFLICT_NEEDS_INSTRUCTION; this is not permission to reissue it.

Publication is **ARCHIVED_VERIFIED** at GK commit
`ed11167f4102d004e010643d74c00f0c658556a0`, parent
`8f6d4689295b1e383ba68fa6c68c82d5900c0ab9`. Fresh main and the current catalog
were read through the GitHub connector. One raw file, one record and the
catalog append were committed atomically with a nonforce update; all prior
29 entries including KQB2495 remain, giving 30. All three files were fetched
in full at the immutable commit and compared byte-for-byte and by Git blob
hash. canonical_archive/PUBLICATION_RECEIPT.json contains this actual full
readback evidence. ARCHIVE_MANIFEST.json preserves the earlier local staging
state; the publication receipt records its completion.

Record path:
`sources/professional/records/PQ-20260927-KQB2497-SCHOLAR-SHOR-DECISION-DIAGRAM.json`.
Raw path:
`sources/professional/raw/scholar/badebbe5db7176ce32e3ccd9a97d2d0a7f47aaa44a4cb67f030f75dc1eef23d0.json`.

The research note separately identifies which official primary texts were
read. Provider snippets are not presented as full-text verification or as
scientific validation. Full PDFs/text extractions in this local directory
are excluded from publication; only reading metadata and research notes
are proposed for the research package.
