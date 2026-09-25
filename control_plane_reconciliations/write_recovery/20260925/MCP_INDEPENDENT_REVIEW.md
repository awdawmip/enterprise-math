# MCP 0.6.7 独立代码审查

结论：冻结补丁没有未解决的 P1/P2 代码问题；允许进入 Root 的完整回归与部署验证。此结论不是生产研究权限、数学审阅或部署验收。Root 仍需以完整测试结果和实机只读回读确认上线结果。

审查基线为 `awdawmip/em-research-mcp@e2e9ca062c38df2da4c426f8794ce43ecd1ded62`，修复代理的 `mcp/DELIVERY_MANIFEST.json` 共 7 个文件。已独立逐文件计算字节长度、SHA256 与 Git blob SHA1，全部一致，记录见 `MCP_FROZEN_HASH_REVIEW.json`。本审查代理没有编辑 `mcp/work`，没有远端写入、部署、生产 session/claim 操作。

## 权限与不可变字节

`source_publication.py` 的精确复用仅进入 `DRIVER_AUTHORITY` 的 PLANNED 路径；已有 stage 检查仍限制真实生成的 Driver/session/DA 路径。复用同时检查已准备 Source 与 publication parent 对当前 main 的祖先关系，并核对返回 path、Git blob、size、完整内容字节。分叉历史、不同字节、错误 hash/path 仍拒绝。非 Driver 的 create-only 文件不获得覆盖或精确复用例外。

复用只创建本地读回证明，不写 Source、不再发布 AUTHORIZE 事件，返回值仍明确 `driver_authorized=false` 与 `execution_authorized=false`。`ControlJobs.driver_activate` 后续的当前 Source `driver_authorize` 保持不变，因此旧 AUTHORIZE 文件不能压过后来的 REVOKE 或继任。真实 native 测试还覆盖仍未关闭 session 的后续 REVOKE，然后验证再次 activate 明确失败且没有新 commit/comment。

## 未知结果、恢复与重复写

checkpoint/freeze 已有 Source 发布后，协调读取失败、可识别的授权读取传输失败、event journal I/O 与本地 upload receipt 登记失败均保留为原请求的 OUTCOME_UNKNOWN。Source 最终 VERIFIED journal 保存异常也保留此状态。原 ID reconcile 复用已落地 publication，并读取已认证、未编辑、内容完全匹配的原 event，不重新发布 Source 或已存在的 event。

实际 authority 拒绝、generation/owner/epoch 冲突、事件幂等冲突、重复认证 event、hash/path/字节错误仍保持明确拒绝。明确拒绝没有被包装成自动重新授权；没有重标历史 FAILED 任务或自动重放旧事件。

首次独立审查发现并实际复现了三处必须修复的遗漏：PREPARED、POSTING、VERIFIED event journal 保存失败会把已经发布 Source 的 job 终结为 FAILED，最后一类甚至已经存在远端 comment。证据是 `POST_DURABLE_JOURNAL_REPRO.json`。修复代理已补齐；独立复测结果见 `POST_DURABLE_JOURNAL_FIXED.json`：三个阶段均先得到 OUTCOME_UNKNOWN，关闭并重建 ControlJobs 后以原 ID reconcile 全部 SUCCEEDED；每案累计恰好 1 次 Source 更新、1 个 event。相关 Source 尾部 journal 和 SQL receipt 相邻窗口也已补齐并有提交测试。

## 测试覆盖与边界

审阅了 6 个 DA replay 用例、16 个 post-source 用例以及 1 个真实 Source/ordinary bridge Driver replay/revoke 用例；涵盖失败前后、完整/缺失回读、重启恢复、冲突与权限拒绝。修复代理最终报告 35 个不同聚焦用例（包含最终 post-source 16/16）与 native Driver 单项已通过，更新 manifest 后再次核对 7 个文件 hash 未变；本报告只独立执行并确认上述 3 个 journal 故障恢复用例。最终完整 Linux 回归与最终版本 native fixture 由 Root 验证，本审查不提前宣称通过。

不可消除的边界仍明确：如果 GitHub comment 的发送结果未知、后续也无法找到已认证 event，代码保留 UNKNOWN 而不盲目重发。平台明确批准/拒绝与缺少实际执行权限也不由这个补丁覆盖。恢复分类变得可接续，不代表所有平台故障都能自动放行。

Global-Knowledge-Sync: main@0606c46c / GLOBAL_KNOWLEDGE_V1
