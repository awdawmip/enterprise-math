# Quartic-Jacobi source query: partial result and verified archival

Status: `ARCHIVED_VERIFIED` describes provenance storage, not relevance, complete literature coverage or mathematical admission.

The current protocol and exact source-cache schema were read before submission. The live catalog had 28 entries, including both earlier QFT searches; none matched the quartic Jacobi / Bach-Sandlund subject, and the dedicated-query Issue search found no pending request for it. The same conversation and standard-mode turn as Issue 2489 was reused. That earlier batch used two jobs; this batch submitted exactly one final job, with no details query, retry under a new ID or extra provider call.

Actual request: `arxiv/paper_search`, query `"quartic" "Jacobi" "Bach" "Sandlund"`, `n=3`. [Issue 2495](https://github.com/awdawmip/kimi-query-bridge/issues/2495) was accepted and [its result](https://github.com/awdawmip/kimi-query-bridge/issues/2495#issuecomment-5851481295) was read back with matching request ID, original-request digest, conversation/turn identity, child query and provider IDs. One provider call is confirmed, zero calls are unknown, and bridge model calls are zero. Provider-internal model work and billing remain unknown.

The actual outer status is `FAILED`; the child is `PARTIAL` with three returned records. They concern nonlinear Schrodinger equations, toric-code metrology and spline smoothing; none is the targeted Bach-Sandlund paper. Therefore this is neither a successful targeted literature hit nor `NO_HIT`, and it does not establish absence of relevant papers. `QUARTIC_QUERY_RESULT_METADATA.json` preserves all three bibliographic records, statuses and counts while omitting abstracts and transport envelopes. No paper full text was obtained through the provider.

The mathematical source was separately read through the public official [arXiv 1807.07719v1 paper](https://arxiv.org/pdf/1807.07719), section 7, pages 13–14. Its primary convention and two supplements match the implemented recursion; this public-original reading is distinct from the unsuccessful targeted provider selection. The related code/proof reading was shared-context author cross-checking, not independent admission or a new numerical propagation.

The source record, metadata/status extraction, catalog addition and unique progress journal were published atomically to `awdawmip/chatgpt-global-knowledge` in commit **`35da005f357501045d4462d9eda78fe6f7346c11`**, parent `06788df022dbd11720132b4ed0882ce8e41b3b8a`. Actual head and catalog dependencies were checked; the non-forced update preserved all 28 previous entries. All four files were then read back at the canonical commit with exact text and Git-blob equality to the locally hashed files.

| Canonical artifact | SHA-256 |
|---|---|
| `sources/professional/raw/arxiv/31b4332014ef5027d5472f0817c4eecacdf186b0111d1b465540495ec81dfcc9.json` | `31b4332014ef5027d5472f0817c4eecacdf186b0111d1b465540495ec81dfcc9` |
| `sources/professional/records/PQ-20260927-KQB2495-ARXIV-QUARTIC-JACOBI-BACH-SANDLUND.json` | `53b95b195de2d7cfee83c06e83a49d4391a0de67ce1823536f56385304a85800` |
| `sources/professional/catalog.json` | `cd3ec4cd448282b0c8e6e1ce6a4f94a831cc216a9515e73ea484e0ee6d13cc90` |
| `journal/enterprise-math/2026-09-27/20260927T010352Z-kqb2495-quartic-metadata-partial.md` | `dd9aefeae0af9c842d7cee9999a5e15f65d2f13629b09d0a3e471d6ddc8080cc` |

The canonical cache validator passed for the new record; its state is `CONFLICT`, raw completeness `PARTIAL`. Original observation remains **2026-09-27T01:03:56.595264+00:00** and seven-day expiry remains **2026-10-04T01:03:56.595264+00:00**. A same-query decision correctly returns `CONFLICT_NEEDS_INSTRUCTION`, `provider_query=false`: archival does not refresh the clock or authorize silent requery. Existing 28 catalog entries were retained unchanged as JSON values; this isolated transaction did not edit scientific code, EM Source ownership or research-activity state.

Only this scope note, `QUARTIC_QUERY_RESULT_METADATA.json` and `ARCHIVED_VERIFIED.json` are intended for the EM research package. The larger catalog snapshots, original transport envelopes and local archive preparation files remain local provenance material and must not be mistaken for new research outputs.

Global-Knowledge-Sync: main@35da005f / GLOBAL_KNOWLEDGE_V1
