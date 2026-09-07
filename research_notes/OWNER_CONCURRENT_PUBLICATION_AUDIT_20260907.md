# Owner 并发发布审计 — 2026-09-07

状态：`BOUNDED_AUDIT / NO_BLOCKING_DEFECT_FOUND_IN_THIS_PUBLICATION`。本报告为 ANCHOR_EXPOSED 内部控制面帮助，不是正式任务、评审、Researcher-ID 或 promotion 授权。只审本次 source checkpoint、既有隔离合同与 journal 写入边界；不巡检 scheduler、CI 或其他 owner。

## 1. 结论与可核验证据

本次发布没有发现 stale whole-tree 覆盖。成立的关键是 **远端父树与已验证本地基树相同**，然后只增加冻结的 owned delta；`nonforce` 本身不能替代这个条件。

本地对象独立核验结果：

| 用途 | 本地 commit | 对应远端 commit 对象 | 共同 tree |
|---|---|---|---|
| 上一已验证 checkpoint | `ac4fa6368614285ab73c1b0f67eb1292f187389e` | `fc2de5e4ab360731b6f1a5d1290e19459fb5c85a` | `5a219ff24dc7be47a7facc19bed063ccea91a1f4` |
| 本次冻结 checkpoint | `c87631636434690d235410cfd788c52f32220af2` | `22ab4335325573657d9df33a3e02a7de5355b324` | `5b373ad350eac53386d6064fb459021a6f320323` |

`22ab433…` 的唯一父是 `fc2de5…`。本地 `c876316…` 的父是 `5f9c8f89ba4983e767fea3f78879117de330a6c5`。同树而不同历史保留为两个真实来源，不能把本地 SHA 写成远端 branch HEAD，也不能据 tree 相等推断两提交存在祖先关系。

实际执行的只读核验：两组 `git diff --quiet` 均退出 `0`；`git merge-base --is-ancestor fc2de5… 22ab433…` 退出 `0`；`git diff ac4fa636… c876316…` 与远端两对象的 tree delta 相同。差集为 **52 个路径：51 新增、1 修改**，全部位于 `research_notes/`、`experiments/`；唯一修改文件是 `OWNER_RESEARCH_PROGRAM_20260907.md`。本次 delta 不含 `src/`、`tools/`、`control_plane/` 或控制策略文件。

root 提供的执行顺序是：第一次 `ls-remote == fc2de5…`；`fetch --no-write-fetch-head --no-tags <url> fc2de5…`；断言父树为上述 `5a219ff…`；`commit-tree <finaltree> -p fc2de5…`；第二次 `ls-remote == fc2de5…`；nonforce push；回读 HEAD 为 `22ab433…`。这是一段 **inline Python/命令流程，不是已保存的发布 helper**。本审计独立确认上述 Git 对象、父子关系和树差；网络调用顺序与回读成功是 root 的执行证据，本助手没有重新发起远端遥测，也没有据此宣称远端此后未移动。

## 2. 直接复用的并发合同

| 情形 | 必须保持的条件与动作 |
|---|---|
| 冻结后、写前 remote HEAD 未动 | 固定 source commit/tree、已验证 base tree、确切 owned delta、expected remote parent；证明目标 tree 在该 parent 上只改变本次授权路径，然后写入其 descendant。 |
| HEAD 已动但包含等价 checkpoint | 按 `ARTIFACT_PUBLICATION_LIVENESS` 消费或对账，只发布真正缺失的 delta；不机械重复发布。 |
| 不同文件并发修改 | 在新父树上应用本次精确 delta，保留其他文件的新 bytes。不能只换 commit parent 而继续使用旧整树；路径不重叠仍须检查实际 tree delta。 |
| 同文件并发修改 | 重新读取该文件的新 bytes；语义合并并重跑受影响验证，或明确 defer。旧 blob 与新 blob 不同即不能 blind overwrite；文本自动合并也不等于语义通过。 |
| 写前/写中发生新的 HEAD 移动 | 预检查发现变化即停止本次 candidate；nonforce 拒绝则重新检查这一个 owner 分支，重算或 defer。禁止 force/reset、换父后直接重试旧 tree。 |
| 同树异历史 | 记录本地 source SHA、远端发布 SHA、两 tree、旧远端 parent 和 path delta；保留双方历史，不为美化 commit ancestry 改写它们。 |
| 传输异常或响应丢失 | 状态是 `UNKNOWN/PUBLISH_PENDING`，不能当作成功，也不能直接假定没有副作用。读取确切 ref/路径和 bytes/hash；已落地则消费该结果，未落地才进行有界重试。 |
| 发布完成 | 验证实际 remote commit/tree 或确切文件 bytes，与冻结 payload 对照后结束发布子流程，继续父研究目标。成功返回、commit 对象已创建、仅 journal 落地均不能单独代替 source 持久化证据。 |

精确边界：Git nonforce 的保证是禁止通常的 non-fast-forward ref 替换，不是“某提交不会删除文件”，也不是任意异常 ref rewind 情形下的严格 old-OID CAS。正常并发作者只增加 descendant 时，以固定旧 HEAD 为父的 candidate 会在另一作者先推进后被拒绝；若必须要求严格 expected-old-OID 相等，应使用现有支持该语义的接口，不能把 nonforce 命名为更强的保证。

最小反例说明树检查为何不可省：基树有 `a=0,b=0`；另一作者提交 `a=0,b=1` 为新父 P；本作者把旧树改成 `a=1,b=0` 后直接 `commit-tree -p P`。该提交是 P 的快进 descendant，却把别人的 `b=1` 改回 `0`。本次发布通过 `tree(fc2de5)=tree(ac4fa636)` 的 guard 排除了该情形。

## 3. Journal 与控制隔离

root 本次 journal 来源是 `awdawmip/chatgpt-global-knowledge` 的 main commit `2d82b9087ae383f3791ff57f97142f4cf45fe9a8`，唯一新增路径：

`journal/enterprise-math/2026-09-07/20260907T151213+0800-owner-01e1d9-native-certificates.md`。

root 报告使用 Contents API create，未携带覆盖已有文件的 `sha` 参数，并已回读 bytes 相等。本助手未独立重取这一远端对象，明确保留该证据边界。

在本次 canonical lease 的 `PROGRESS_JOURNAL_PROTOCOL.md` 下，journal 是 **新增唯一不可变事件文件**，不是多人向同一个文件尾部追加。不同事件路径可独立创建，由服务在 current main 上串行落地，不能上传一棵旧 main tree。路径碰撞或并发写失败后换新的 event ID/path 重试；不读取旧事件后覆盖或拼接它。若仅响应丢失，先查确切原路径以识别已完成写入；事件重复可作 provenance，但不必因不确定传输制造重复。

这个 journal fast path 明确豁免一般 curated 写入前的 full-main refresh/dedup；不能把它误判为本轮遗漏 `-BeforeWrite`。curated canonical 记录更新仍需当前 parent/blob SHA、重读受影响记录、语义合并和冲突重试。新 journal 不夹带生成索引、路由表或 curated 记录改写。

研究 source 在 `D:/em/owner-20260907`、branch `research/em-owner-20260907`；控制改动只在独立 `D:/em/owner-control-20260907`、branch `maintenance/em-owner-control-20260907`。root 提供控制 PR 为 `#1363` 且本轮未动；本审计没有读取其活动状态或更改它。

`RESEARCH_OWNER_ISOLATION` 允许研究 owner 落后 main，只消费必要的明确依赖；不能为更新而全树同步 main。source checkpoint / Draft PR / journal 只提供进展与来源，均不授予正式 task、claim、Working Truth、Foundation 或数学 canonical promotion。真正 promotion 按 L4 从当时最新 main 只 replay owner payload，保留 source 历史；控制维护遵守 `NO_NEW_MATHEMATICS`、path/semantic overlap 审计、回归、fresh main 与 expected-head merge。控制维护 lane 可与数学研究并行，不可借 source 发布成功自动执行 merge 或扩大数学权限。

## 4. 已有接口与有限审查范围

- `control_plane/immutable_write_transaction.py` 的 `preflight`、`PlannedFile`、`commit(..., postcheck=...)` 提供本地不可变新文件的 exclusive create、postcheck 与未变字节回滚；其文件头明确说不是远端 Git authority。不能把它当成整组文件原子可见或远端 CAS helper。本审计只核对接口职责，没有扩成该模块的全并发故障注入。
- `tools/research_task_records.py` 是**正式 task publication**入口，必须 exact taskbook blob、当前 preflight、精确 supersedes、不可变 record 与冲突安全写入；source 笔记发布不能冒充该事务。此处核对的是 canonical 协议，不声称重新审查该 writer 的全部实现。
- 本次 source 发布没有持久 helper 可修；未发现需要新建发布框架或修改控制代码的阻断缺陷。后续继续复用本节合同中的已验证 inline 路径，特别保留 base-tree guard 与确切 path delta。

审计读取的项目协议固定于本地 `c87631636434690d235410cfd788c52f32220af2`；真实读取字节 SHA256：

| 文件 | SHA256 |
|---|---|
| `docs/RESEARCH_OWNER_ISOLATION.zh-CN.md` | `bd2edfba6681c58d30e326df8d9112f6a3bb073d5634e0a226e076bec426bf02` |
| `docs/ARTIFACT_PUBLICATION_LIVENESS.md` | `fc6231df371922040a686de101cb8a9c768c91b9ca4c96ecb277e3374c7c0358` |
| `docs/GOVERNANCE_MAINTENANCE_LIVENESS.md` | `78cf6b8ec75997f453bc41df8de1dbd80d926de7d960440cdab16699c986a2a0` |
| `docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md` | `8f97a36c3e9f1868e46c413e89e04fa8ba96af59b4093676b121697c1779d76e` |
| `control_plane/immutable_write_transaction.py` | `3378b18055ab41616bff9ab7839e43b8e56e332d9b680b98f0534a7c25072ac3` |

全局写入结论以 `4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563` 的 `CODEX_SYNC_PROTOCOL.md`、`OPERATING_MANUAL.md`、尤其窄覆盖 `PROGRESS_JOURNAL_PROTOCOL.md` 为准；未把不匹配 canonical SHA 的本地 KB 工作树当成现行政策。唯一产出为本报告；未修改源模块、控制代码、远端 ref 或 journal，未发 Issue/comment，未领取正式任务。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
