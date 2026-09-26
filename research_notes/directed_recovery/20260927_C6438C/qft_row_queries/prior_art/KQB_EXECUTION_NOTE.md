# Bounded professional literature query receipt

Status: MATCHED_RESULT_READBACK / ARCHIVE_PENDING, 2026-09-27 Asia/Shanghai.

At canonical Global Knowledge `f44ed5959c92e6e088c61c102951d1ab2c5e98d4`, the
professional catalog contained no matching CT/QFT/tensor-network literature
cache. The available `CAPABILITIES.json` permits arxiv/paper_search and
scholar/paper_search as metadata/abstract queries. No company source applies.

The first submission [Issue 2488](https://github.com/awdawmip/kimi-query-bridge/issues/2488)
was rejected before query execution with `INVALID_TURN_ID`; its readback is
retained in `KQB_2488_REJECTION_READBACK.json`. The same logical parent turn
was mapped to UUID `4ec7c225-8ee0-4565-9d9c-36957858ba21`, replacing the local
label `sep27-qft-goal-20260927T071454+0800`. The original conversation ID is
`01a079d7-5d03-7a21-abe9-f70606fee0ee`. The replacement contains the same two
jobs; no extra research query was added and the rejected issue was not edited.

The accepted batch is `092b236a-7d54-4ea7-aefb-5ca2279c732d`,
[Issue 2489](https://github.com/awdawmip/kimi-query-bridge/issues/2489).
Creation was observed at `2026-09-26T23:20:32Z`; intake at
`2026-09-26T23:20:38.682256+00:00`; completion at
`2026-09-26T23:20:47.888329+00:00`. Other paper-reading tool work occurred
between submission and the first readback, which returned the completed result.

The [intake receipt](https://github.com/awdawmip/kimi-query-bridge/issues/2489#issuecomment-5850846653)
and [result](https://github.com/awdawmip/kimi-query-bridge/issues/2489#issuecomment-5850847340)
agree on original request SHA256
`81e04961818220b8e621e2250caa03effbc10b261a8adffdd5c956e829b0213d`.
The separate normalized execution hash is
`c70c4760a503344096d0b8297c4f302bbbb5e260dd71a0daa3731404c7690d55`.
Both are preserved without conflating them. Full raw connector readback is
`KQB_2489_RAW_READBACK.json`; extracted result is `KQB_2489_RESULT.json`;
exact submitted request is `KQB_2489_REQUEST.json`.
The original request digest was also recomputed locally from the request
object using sorted keys, compact separators, Unicode UTF-8 and no NaN,
and matched the receipt. A final read of the issue body matched the saved
request object; `KQB_2489_ISSUE_READBACK.json` retains that source response.

Both child jobs report `PARTIAL`, `retrieval_verified=true`, eight records,
and `BOUNDED_SELECTION_LIMIT`. The envelope reports `FAILED`, despite the
two returned child payloads; that discrepancy is retained rather than
rewritten as success. Each source reports one confirmed provider query call,
zero unknown provider query calls, billable calls unknown, zero bridge Kimi
LLM calls, and unknown upstream internal LLM calls. This is two accepted
query tasks for the shared standard turn, not a claim of zero cost.

The Scholar payload supplied relevant QFT-MPO, QFT-MPS and Shor-MPS routing
records. The arXiv payload's eight records are largely topically unrelated;
they are not treated as relevant corroboration or evidence of no relevant
papers. The returned fields are metadata and supplied abstracts only.
Official primary PDFs were read separately for the scientific report.

All returned fields needed here were actually read from the result comment;
there is no full_result fragmentation manifest to follow. Root is responsible
for canonical raw/record/catalog archival and readback. Local preservation
alone is not `ARCHIVED_VERIFIED`. No new query is required for that archival.

Local publication material is now prepared in `canonical_archive/files/`:
two metadata/status raw extracts, two CONFLICT records and the catalog with
its original 26 entries retained and two additions. The canonical validator
from the declared base commit passed both new records and confirmed that a
same-query need does not silently requery either unfinished result. Seven-day
expiry is derived from each child's original observed_at, not ingestion.
`canonical_archive/ARCHIVE_MANIFEST.json` gives exact publication bytes,
hashes, base catalog blob and append entries. `base_snapshot/` and the
manifest are review aids, not additional GK publication files.

Global-Knowledge-Sync: main@f44ed5959c92e6e088c61c102951d1ab2c5e98d4.
