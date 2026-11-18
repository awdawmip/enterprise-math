# Current observations for historical Activity summaries

Older Activity events may contain an `EM_REPRESENTED` summary and exact Source
pins, but no complete connector-observation sidecar. The loader preserves those
events as historical reports. It does not invent a past response or treat the
summary as a currently verified observation. Partial or malformed receipt fields
still fail validation; normal observations still require exact stored bytes.

The explicit `audit` operation reports unresolved legacy events as
`REOBSERVE_LEGACY_EM_SOURCES_AND_APPEND_CURRENT_REPAIR`. Re-read each exact
immutable repository/commit/path, check blob SHA1 and SHA256, and append a new
checkpoint using the existing `repairs_event_id` operation and actual complete
observation. A local `observation_id` records present provenance; it is neither
an invented historical tool call ID nor a signed server attestation. Keep old
event values, Activity ID, Researcher and original session unchanged.

This delivery applies that operation to Issue #2187, Activity
`RA-5E3FE1E761E4963EC461A892`: four historical events are retained and five exact
existing public Source files were actually read again. Four new current repair
events reference their original events. The five full observation sidecars are
new evidence; their time is not backdated. They do not rerun any mathematical
program or validate a theorem, Task, CLAIM, Result or Driver decision.

Publish the record and all its new sidecars together through Source CAS. Read
the immutable published record back, then run the explicit observation audit with that real
registration observation and the original session. The ordinary `guard` remains
the already-reviewed lightweight bookkeeping/session association check; it does
not demand connector envelopes or replay historical evidence. A source file's persistence,
an Activity guard result and formal execution authority remain separate facts.

The metadata overview exposes historical-summary events and recorded repairs;
only the explicit audit revalidates observations and resolves repair debt. Runtime
code packages must preserve their existing reviewed modules when picking up this
helper; updating this one helper does not authorize a whole-main executable swap.

No new or repeated tests are part of this change. The real-record migration,
Source byte/readback checks and guard acceptance are reported separately from
unperformed broad workflow or mathematical verification.

## Existing raw receipts and missing observations

A genuine existing sidecar may have a different JSON whitespace/key order from
the local writer. Validate its actual pinned bytes and all decoded source fields;
do not replace the stored SHA/path with a re-serialization's identity or rewrite
the old file. New receipts are still written canonically. Duplicate JSON keys,
non-JSON numeric constants and source/receipt/session/CAS drift are rejected.

For summary-only events, obtain a **current real full-file observation** for each
listed immutable source pin. Retain the complete actual managed response and
its real tool label, SHA-256, Git blob and immutable URL. Use a present local
`observation_id` when no call ID was exposed; never invent or backdate a past
response. Append a new event using the original Activity/session and exact
`repairs_event_id`, with the genuine observations covering that original event's
source pins. Publish the new sidecars and updated record atomically with fresh
Source CAS, then read the exact updated record back for `audit --registration-json`.
Reading an existing scientific file does not require rerunning its mathematics.

已有真实旁证可采用不同的 JSON 空白或键顺序。校验其原始字节摘要和全部来源字段，
不改写原文件，也不用重排后的摘要替换原路径身份；新文件仍按规范格式生成。
重复键、非 JSON 数值常量、来源或旁证篡改、会话不符和 CAS 冲突仍然拒绝。
仅有摘要的事件需要现在重新取得对应不可变来源的完整真实观察，保留实际工具返回，
不伪造旧调用或旧时间。沿原 Activity／会话追加明确关联旧事件的新修复事件，
以新鲜 CAS 一并发布记录和新旁证，再完整回读更新后的记录供显式审计。
这只修复记账证据，不重做数学、不创建 CLAIM，也不增加每轮科研启动检查。
