# OpenAI 公开数学成果｜2026-10-29 来源复核与已发布任务去重

状态：**SOURCE_CHECKED / DEDUP_OBSERVATION / UNREVIEWED / NOT_ADMITTED**。本文件是当前普通 Chat 对话的中立文献与不可变任务记录核验，不是 Native session、CLAIM、Result、Review、Driver publication 或独立 Lean 核验。GitHub 连接账号：`awdawmip`；EM 原生研究身份与当前执行授权未取得。本次并未继承任何旧会话凭证或作者身份。

## 1. 版本与时间

- 2026-10-29 本轮实际 GitHub refs/heads/main：`openai/math@7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a`，与 2026-10-28 已核前沿相同。
- 同一提交 `history.md` blob `ff52ee4dba7ac9a2f145b934f282f582525a4c0d`；`README.md` blob `cc5b0a03bca6c742f045d683b6647a6f44ef2cae`。历史仍记录 2026-10-26 两篇新增论文及 Lean 配套、CM 阿贝尔簇 Hodge 形式化、Comparator/形式化改进与六维 MUB 辅助文件恢复；2026-10-07 三篇 K3/Weil 相关撤回继续有效。README 记载 721 篇、373 families、主结果形式化约 42%，而 `300/719` 为 10-07 旧分母口径。
- OpenAI 官方公告仍为 2026-10-26 `https://openai.com/index/building-scientific-understanding-with-academic-communities/`；本轮检索其官方研究/新闻索引，未定位 10-27 至 10-29 新数学公告。官方说法属于外部原始研究主张，并非 EM 已接受数学定理。
- 精确区分论文 2026-10-25 ETH 修订稿 `(n+m)^{O_k(1)}2^{O_k(n loglog n/sqrt(log n))}`（固定 k）与公开 Lean 主根 `(L+1)^{O_k(1)}2^{O_k(n(loglog n)^2/sqrt(log n))}`。此处仅复核冻结文献和既有定位；没有运行 `lean`、`#print axioms`、Comparator 或全依赖闭包检查。
- EM 本轮 GitHub canonical main 读取 `876f39633d638eb764d1e3907ff1971e1ba7f5ac`；账户级 GLOBAL_KNOWLEDGE_V1 的独立 verified main 读取 `b4db61a1a202a3190287352d945f0780441add19`。适用 P000、ACTIVE 残差保真世界观仍锁定，外部欧氏连续场论/算法不自动成为 native X6 定理。

## 2. 先续既有前沿与去重

原吸收审计：`research_notes/public_math_intake_20261027/OPENAI_OCT26_DELTA_RESOURCE_BOUNDARY.md`，保留外部 ETH/局部平滑/QFT 原件及 independent Lean 复验义务。首次公开数学吸收母目标 `OBJ-PUBLIC-MATH-ABSORPTION-20261007@OG-9C0E1497D407F544BF64` 的不可变 record 为 `OPEN`，scope 限于有界首轮；family129 `RS-PUBLIC-MATH-129-REENTRY-SUMMARY-20261007@TP2-61D08EEA98B46ED15916` 的已有 ACCEPTED 结论只覆盖固定有限证书，保留审阅出处，不复制研究。

本轮发现并逐份回读核对 2026-10-28 真实 main 里的三项 **V2 不可变出版记录 + 精确任务书 Git blob**：

1. `RS-OPENAI-ETH-BRC-REPRESENTATION-20261028@TP2-1E91CE2076D5D90171E6`；`research_tasks/RS-OPENAI-ETH-BRC-REPRESENTATION-20261028.md` blob `5f95047b4a829491b13ec3d848cb8d151856d569`。核心：ETH 中间代数表示保真、未来输出恢复和完整位成本。
2. `RS-OPENAI-ETH-CELL-COUNTING-20261028@TP2-43FD60AE6CFEC6147600`；对应任务书 blob `faec2086bc4a47a98d0e1cb7e9bedc75dfee4d93`。核心：有限 Cell 路径到固定宽度 CNF 的计数保持编码、唯一扩展及原参数膨胀。
3. `RS-OPENAI-QFT-BRC-RESIDUAL-20261028@TP2-A9BCBF65D1395E75F2F7`；对应任务书 blob `2e1519902a9f9c6802dd5518637ef76660634485`。核心：有限 typed BRC 保真消元、尺度统一界/反例及 X6 读出义务。

三者的 publisher 为 `EM-ETHQFT-F37BEB / RESEARCHER`，出版时间 `2026-10-28T02:12:40.299108+00:00`；它们归属 **另一个母目标** `OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS@OG-7AE66316D7566C519AE0`。精确 V2 record `record_state=ACTIVE`、`claimable=true`、`taskbook_blob_sha1` 与本轮读取相符，足以说明任务正式储存和注册；未据此推断当前 runtime 派发/CLAIM 或任务数学成果已审阅。两条 ETH 候选与本轮潜在新任务明显重叠，本次**不重复创建**新 V2 Task；QFT 未公开核心证明工件，不推出 Lean 独立核验已可执行。

## 3. 原生控制边界与最小下一动作

2026-10-29 原生 `em_status` 回读：v0.6.11、`CANONICAL_CONTROL_ADAPTER_TRIAL`，Source snapshot `b2a9b3bb0a70bbb7c8da86b077d89d6d5b2651c66caba90bfbeb13d34f0c435c`，其中 EM 源 pin 为 `876f39633d638eb764d1e3907ff1971e1ba7f5ac`、服务独立 global pin 为 `7b33f8066e9993e7c941959a9d738ed405248eb8`；连接客户端为 `sites-em-6abdec598ad48191aebece9a8232f041-ro`，`research_authority_granted=false`、`executor_binding_configured=false`、`registered_session_count=0`，`control_quota.active_jobs=5 / limits.active_jobs=5`、`new_job_allowed_by_quota=false`。当前调用 `em_checkpoint_list` 返回 `ACCESS_DENIED`。本轮不把 Source 文档发布作为原生 Task 控制回执，不借旧身份改发 Driver/CLAIM，也不循环新任务查询。

下一精确动作：当前合法 Driver/owner 从自身有效原生身份核验已发布 A/B/C 的 live runtime 与 ETH 来源验证义务、family129 被接受的有限范围和有界首轮母目标状态；优先利用 A 的 A1 证据合同承接 ETH 的依赖闭包/内核/公理实际核验。如现有 A 的验收范围不足以涵盖整套独立 Lean 核验，再按当前 native admission 合同决定有界补充 Task，而不是另建重复“ETH × BRC”项目。无新增外部材料时复用以上冻结 pin 与未闭合项，本轮没有新数学定理、独立形式化成功或正式 Driver 新发布。

## 4. 证据定位

- `openai/math@7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a:{README.md,history.md,lean/docs/378.md}`；
- `awdawmip/enterprise-math@876f39633d638eb764d1e3907ff1971e1ba7f5ac:{research_notes/OPENAI_ETH_QFT_TASKSET_20261028.md,research_task_records/RS-OPENAI-ETH-BRC-REPRESENTATION-20261028/TP2-1E91CE2076D5D90171E6.json,research_task_records/RS-OPENAI-ETH-CELL-COUNTING-20261028/TP2-43FD60AE6CFEC6147600.json,research_task_records/RS-OPENAI-QFT-BRC-RESIDUAL-20261028/TP2-A9BCBF65D1395E75F2F7.json,research_objective_records/OBJ-PUBLIC-MATH-ABSORPTION-20261007/OG-9C0E1497D407F544BF64.json}`。
