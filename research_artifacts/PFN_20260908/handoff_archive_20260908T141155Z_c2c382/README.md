# PFN 未执行领取的事实归档

本目录只保存准备、领取、历史授权和释放证据；不包含新研究、CLAIM、Result 或数学认证。PFN 仍未开始数学。

原四份意向的不可变来源是 [fabe2a359cc5f2460a59d08abe462b1bb24c2593](https://github.com/awdawmip/enterprise-math/commit/fabe2a359cc5f2460a59d08abe462b1bb24c2593)。原 intent、source_binding、native_substrate_plan 和 ER 均保留原字节；精确路径及 pins 在 `archive_manifest.json`。本目录不重复发布这四个文件，也不把它们的准备状态改写成研究成果。

事实顺序：直接 CLI 准备在创建 ER 前被未初始化的既有 fork 检查拒绝；同一新 claim 经当前 canonical bootstrap 准备成功（8.067 秒）。Root 在消费完整全局 selector 结果之前领取 PFN；CLAIM [5585867751](https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-5585867751) 的服务端时间为 13:25:59Z，13:27:20Z 开始的 runtime 调用实际 PASS。数学尚未执行时，HANDOFF CONTINUATION [5585930654](https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-5585930654) 于 13:30:39Z 释放该领取。随后 canonical guard 明确拒绝：`DENIED_NO_WINNING_LIVE_CLAIM`，理由为 `registered execution requires a current winning live Issue #240 CLAIM`。

阅读入口：

- [交接清单](../handoff_manifest.json)：四份原始意向、事件和授权边界。
- [历史授权](../execution_authorization.json)：原始 PASS 回执，现不提供执行权限；根目录 runtime 原件与它逐字一致。
- [当前状态](../continuation_state.json)：`HANDOFF_READY`、`owner_claim={}`，本归档未修改它。
- `prepare/`：原失败/成功 invocation、stdout、stderr、receipt 和控制 helper 的精确字节副本。路径与时间保持当时值；helper 仅历史证据，不是今后的重新领取入口，不应重放。
- `events/`：两条 PFN server envelope 的精确原件副本。
- `dispatch/`：两次根调度回执的白名单提取件，保留原件 SHA/blob/bytes。它们不是原件的字节副本，也不是重新执行结果。仅保留另一被选任务的 ID/发布 ID/控制状态，不包含其数学正文、frontier 或 next_action。未复制 738/740 条评论全集。

当前 PFN 无有效 owner、无新证明/见证/null screen/回传/Result，既有 PFSSV 21-cell 没有重跑。再次进入 PFN 必须先由当时的 canonical dispatcher 选中，再建立新合法 owner、fresh claim/ER 和实际 runtime 授权；不得把已释放 claim/ER 或历史 PASS 作为当前许可。此交接不是父科研目标完成或数学否定结论。

`archive_manifest.json` 区分原样复制、已有同字节文件和有界提取。所有原始 TEMP 来源、原 publication.json 和已有七份仓库文件保持不变。下一次 GitHub 发布由 root 负责，本归档不声称未来 commit 已存在。

Global-Knowledge-Sync: main@f47b74b / GLOBAL_KNOWLEDGE_V1
