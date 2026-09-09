# R005 双发布头参考审查（内部控制用途，2026-09-09）

审查者：EM-DVR-A4187A。本任务由 Owner 委派为有界控制参考；本人当前 DA 的 source reason 是 RB 常驻路线委派，不能据此宣称取得新的 R005 Driver 权威。下述两阶段均由同一审查者在共享上下文中完成，披露为 `SHARED_CONTROL_CONTEXT_DISCLOSED`，不是两名独立研究员或干净上下文盲审。阶段一逐头提取其自身合同，不因另一头存在而排除它；阶段二才作交叉比较。未执行数学、scanner、全库审计、claim 或正式 review/selection 事务。

固定观察快照为 `562df4628f1896bd0faca3706efbacdb78f189d0`。两阶段共同引用同一七源清单，见 [source_pins.json](../research_artifacts/CONTROL_R005_PUBLICATION_FORK_REFERENCE_20260909/source_pins.json)；本地参考输入摘要为 `0c2d809e0ca345a268ec003db1dc0c4b59b05a1a2ccaa9303e40c8f84d40dcfe`。这不是 canonical parallel synthesis 的 ID 或已通过其 validator 的证明。

## 合同边界

三个实读合同 C1–C3 区分不可变研究证据与单值运行选择：

- 两头必须保留，不以时间较新、同一发布者或同 TaskID 推定合流，更不能删改旧对象来消除分叉。
- 两次逻辑不同的参考审查应绑定同一完整证据集；共享审查者必须披露。真正的严格独立性只能由任务声明，不能由“两段”推得。
- 现有允许路径包括 KEEP_PARALLEL、MERGE_TO_NEW_GENERATION、typed split 和显式 operational reselection；非选中头不是被否定的研究。
- C3 要求显式选择前有两段参考及 synthesis，完整保留所有 active unsuperseded heads。本文只是可供授权流程引用的参考材料，没有创建这些正式记录。
- C1/C3 状态为 ACTIVE_CANONICAL_CANDIDATE，C2 为 ACTIVE_PROPOSED_CONTROL_PLANE。本文报告其文字合同；实际当前 consumer、合法 authority、完整记录集和写入前 CAS 仍由 Owner 核验，不能把本文当成运行入口已接受本次选择。

## 第一阶段 A：旧头自身合同

**P_OLD：TP2-ADD82532ACD19FC01D53**，2026-09-03T03:01:57Z，generation 1，supersedes null。书为 `research_tasks/R005A_DEFICIT_SHADOW_EXECUTABLE_BINDING_CORRECTION_20260903.md`，TP2 pin 与实读 blob 均为 `5b186a65ee10eaf4e650a272a50a7dc91089c6c3`。

| 项目 | 独立提取 |
|---|---|
| 父路线 | `OBJ-R005-PRIME-ALGORITHM-LAB`；origin 与 lineage 都是 MAINTENANCE |
| 硬目标 | `R005_DEFICIT_SHADOW_EXECUTABLE_BINDING_CORRECTED_AND_BYTE_REVALIDATED` |
| 固定源与边界 | 数学内容冻结于 `f9e2a611b45631c43effce36b7300c6f9a56b77b`；保留 DSI1/2/3、q=78553 常数、已认证端点 `k<=2822453183433` 及精确 916-gap 外部目录义务，不收集该完整目录、不推进 seam frontier |
| 修复对象 | 书中指称 scanner 的 `metada` typo 与错误 coverage f-string，以及不能绑定最终源码字节的 transcript/manifest；本文未重新验证这些代码缺陷 |
| 正向检验 | `completeness_attestation=true` 的 synthetic fixture 必须真正到达完整 `validate_catalog_for_seam`，包括 `max_gap_bound_end` 和 coverage diagnostic |
| 明确负向检验 | 声明的 max-gap-bound coverage 结束过早时必须拒绝 |
| 输出证据 | 最终 scanner 与 regression 的 `python3 -m py_compile`、focused suite；新 transcript 记录命令、exit status、确切路径；manifest 记录每个变更文件最终 byte count 与 SHA-256 |
| 终局 | 只保留 `NO_MATH_DELTA_EXECUTABLE_BINDING_REPAIRED` 或 `MATH_DELTA_FOUND_REQUIRES_DRIVER_REVIEW`；任何 DSI 定理、常数、端点、目录义务或搜索语义变化必须停交 Driver |
| 运行绑定 | owner 为 `research/r005a-deficit-shadow-executable-binding-correction`；identity lane `R005A-FIX`，书中 lease 360 分钟，Task publication 的 claimable=true 不是实际 winning claim 证明 |

旧书还明确引用原 return 与 PR1140 blocking review 5097275954。该出处作为此书的声明被保留，未在本轮打开原数学、PR review 或执行包。书中“旧执行已放弃”也不是本轮核验出的现时 owner 状态。正文要求 correction return，未写新 Result 的具体 ID；这不构成对通用 canonical Result 流程的豁免。

阶段一旧头结论：可辨识的独立修复合同，源/书 pin 对得上，正负检验及停止边界具体。保留进入第二阶段；没有据此接受其底层数学或证明工作已经完成。

## 第一阶段 B：新头自身合同

**P_NEW：TP2-2C524413EC9774383AF1**，2026-09-09T06:06:00Z，generation 1，supersedes null。书为 `research_tasks/R005_DEFICIT_SHADOW_EXECUTABLE_BINDING_CORRECTION_20260909.md`，TP2 pin 与实读 blob 均为 `80f3d289824a4310d50e6763e3940c7574d5e7c2`。

| 项目 | 独立提取 |
|---|---|
| 父路线 | `OBJ-R005-PRIME-ALGORITHM-LAB-RELAY-20260909`；origin 是 DIRECT_USER_DIRECTION，lineage 是 MAINTENANCE |
| 硬目标 | `R005_DEFICIT_SHADOW_EXECUTABLE_BINDING_CORRECTED_AND_REVALIDATED` |
| 固定源与边界 | source_refs 指向同一 `f9e2a611...` 的结构文档和 scanner；冻结 DSI1/2/3、q=78553 常数、gap-start band `[1291005053866735,1294364244470160]`、端点 `k<=2822453183433`；不获取完整 916-gap 目录、不声称 q78553 closure |
| 修复与正向检验 | 重现并修复 `metada` 与 coverage diagnostic；返回 fail-closed scanner，真实 `completeness_attestation=true` 回归应覆盖 coverage/max-gap/positive scanner 逻辑 |
| 负向检验的文字边界 | 要求 fail-closed，但未像旧书那样单独明定“max-gap-bound 结束过早”的拒绝反例；不能把“exercises coverage”自动记录成这个负例已覆盖 |
| 输出证据 | final-byte syntax/focused regression evidence、再生 transcript/manifest hashes；**显式要求一个新的 immutable correction Result**，绑定最终 source revision 和不变数学边界 |
| 终局 | 残余交付缺陷返回 `REVISION_REQUIRED`；DSI 语义改变返回 `MATHEMATICAL_SCOPE_DRIFT`；corrected package frozen 后停止，seam closure 属另一任务 |
| 运行绑定 | owner 为 `taskbook/unassigned`；identity lane `R005FIX1`，lease 360 分钟；RA-PR1140-P8H4Q2-20260909 是引用的来源/跟踪记录，不是 claim 或旧 session 延续证明 |

新头正文没有重新给出旧书所有诊断/命令/逐文件 byte-count 细项。它可以是同一修复意图的简写，但本次参考不能自行补出未写明的测试、终局标签或旧 owner/Result 绑定。保留进入第二阶段；没有判定它因较新而优先或因并列而无效。

## 第二阶段：交叉对照与对抗性控制复核

两头 **核心修复目标兼容，但执行与治理合同不是可静默互换的逐项等价文本**。适宜关系是 `COMPATIBLE_COMPLEMENTARY`，同时披露父路线等治理字段的 `DIFFERENT_SCOPE`；不作无条件 EQUIVALENT 或最新覆盖旧版的结论。

共同部分是同一 f9e2a611 scanner/证据链的无数学增量修复，冻结的 DSI、q78553 band/endpoint 与目录阻塞边界没有冲突。差别至少包括：

1. 旧书显式的拒绝反例、命令/exit/路径和 byte-count 义务，新书不得因简写而被当成已完整继承或可以删除。
2. 新书显式新 immutable Result 的证据绑定，应在实际收口保留；不能以旧书只写 return 为理由规避 canonical freeze，也不能把“要求新 Result”误报为已经存在/通过。
3. 两个硬目标字符串和失败/终局标签不同；任何统一标签都需要明确映射，不能改写原书/TP2/历史 return 或假定已有下游 Result 可重绑。
4. parent objective、origin kind、owner、identity lane 以及 policy digest 不同。新 RELAY 路线治理责任是真实需保留的要求，不能在将新头选为 nonoperational 后默默丢失；旧 owner 支路也不能仅因 `taskbook/unassigned` 而释放。
5. 两个 TP2 都是 generation 1、无 supersedes；同 TaskID 与同 publisher EM-DVR-P8H4Q2 不能合成替代关系。必须分别保留其 book blob、source refs 和任何已存在的 claim/ER/Result/review 关联。本轮没有检索或验证这些执行对象，不能声称它们为空。

合流时应取能同时满足两份文本的证据要求：完整 true-attestation 正路径 + 明确过早 coverage 拒绝，最终字节 compile/回归及真实 argv/exit/path，逐变更文件 size/SHA-256，与最终源一致的新 correction Result，NO_MATH_DELTA 边界和数学漂移停止机制。保留原 f9e2a611 结构来源、旧有限端点和外部 catalogue 义务。若统一成新任务书合同，按既有机制生成新的不可变合成 generation 并显式记录来源/父路线衔接；不要在两份原件上打补丁。是否另做 typed split 是 Owner 的路线决定，本文不创建新任务。

## 能否指定 operational head

**合同允许在完整的两段参考、授权 synthesis/selection 和当前运行边界核验之后显式选择；本文自身不能合法指定。** 需要由实际有权的 Owner/Driver 使用当前既有入口，精确保留两个头于 retained parallel set，绑定同一完整 evidence set，核对是否有有效 claim/ER/Result 等既有派生权限，以及写入时最新 target/CAS。未经这些步骤，两头歧义不得通过自动“最新赢”、直接改 canonical_publication_id、删除新记录或宽泛忽略 fork 获得授权。

在未发现现有 owner/Result 冲突、且 Owner 选择沿用原执行合同的条件下，旧头可作为保留较明确正负检验与原 lineage 的 **运行候选**；这是条件性参考，不是本次 selection。新 RELAY 的治理责任仍需显式连接保留。选择新头或新合成 generation 也须保存旧书额外要求和旧引用关系，不能把选择当作质量排名、数学否定或关闭另一条路线。

此参考支持利用已有机制隔离单值运行歧义，保留全局其他任务继续推进；不声称已经解除了实际 CI 阻塞、授予了新 R005 authority、创建了正式两-pass/synthesis 记录或完成了数学审阅。

Driver-ID: EM-DVR-A4187A / CONTROL_PLANE
Global-Knowledge-Sync: main@5f14819 / GLOBAL_KNOWLEDGE_V1
