# 两个独立研究子单元：待规范发布的交接稿

Progress-Event-ID: `portfolio-publication-20260927-6f94c2`
Date: `2026-09-27`
Status: `NONEXECUTABLE_DRAFT / PENDING_CANONICAL_PUBLICATION`

## 用户委托与真实状态

当前用户原文：“把适合发布新任务的部分发布到状态机，原路线保持方向就好”。

本稿保存筛选后的问题、冻结来源、验收和去重信息。它不是任务发布记录，不是 CLAIM、Result、Working Truth 或 Driver 指令。不更改原路线、原任务、优先级、owner、依赖或定时配置。两个候选均没有正式 Task-ID / publication_id，不能从本文件领取。

```json
{
  "artifact_kind": "USER_DIRECTED_TASK_PUBLICATION_HANDOFF",
  "event_id": "portfolio-publication-20260927-6f94c2",
  "status": "NONEXECUTABLE_DRAFT_PENDING_CANONICAL_PUBLICATION",
  "formal_task_created": false,
  "canonical_publication_ids": [],
  "candidate_count": 2,
  "registered_session_id": null,
  "driver_authority_id": null,
  "live_queue_read_succeeded": false,
  "source_read_snapshot": "86022c1ee4de09a9c9055f4c6806a5d35459edfc",
  "source_head_seen_before_capture": "b782ba42244dd87f00d69d056691985c0b64a957",
  "global_read_snapshot": "60bd7d5591e518cef2c7df6098530c059b95690e",
  "existing_routes_changed": false,
  "logical_conversation_id": "chatgpt-research-portfolio-20260927-6f94c2",
  "blocking_error": "SOURCE_TREE_SIZE_LIMIT"
}
```

Native control 0.6.8 的 status 请求成功，但 session_start 与 tasks 两个实际请求均终止为 FAILED / SOURCE_TREE_SIZE_LIMIT。没有收到研究会话或 Driver authority；不能以 status 成功、用户授权或本稿存在替代规范发布检查。

- status：awdawmip/kimi-query-bridge Issue #2527，request_id `portfolio-20260927-6f94c2-status`。
- session_start：Issue #2528，request_id `portfolio-20260927-6f94c2-session`；终态评论 https://github.com/awdawmip/kimi-query-bridge/issues/2528#issuecomment-5854472549 ；request SHA-256 `fc676fe5055723407aea54c344658ce0b3ec074651472a4381fb87c4c9eaa11d`；receipt SHA-256 `d72d5dcf674cb1976a8ebac8a2a6b2ad5d4723ea5ec90fa545b1985a29a58f2f`。
- tasks：Issue #2529，request_id `portfolio-20260927-6f94c2-tasks`；终态评论 https://github.com/awdawmip/kimi-query-bridge/issues/2529#issuecomment-5854477896 ；request SHA-256 `83603f6c849128c32479b1d52f2877401487c6f30e4a1cc95af26d30adfaa274`；receipt SHA-256 `30fda37beadf240577666bb267a17ef341884ac8357c8746192f92c049f205d9`。

失败不等于任务队列为空。随后用原生 GitHub 读取固定 Source 的任务记录目录和相关任务正文进行有限去重；未读取全部任务正文，未证明全部当前 owner/claim 状态，也未执行发布 policy audit。按照 current_control_authority.json 与 RESEARCH_TASK_PUBLICATION_PROTOCOL.md，在无等效完整 preflight 时只落非可执行稿，不手写 ACTIVE/claimable 记录。

## 已完成去重与原路线保留

所有下面的原任务与路线保持原方向。本稿没有重新派单。

1. `RS-HBW-WEIGHTED-MULTILAYER-FAMILY-20260927` 已有不可变记录 `TP2-5579F1B38B4D8C3085AB`，固定 taskbook blob `0a6ca4debd4fd6972ee8559ddde544429b26542b`，母目标 `PO-HBW-WEIGHTED-REPAIR-20260927`；不重复发布“多层修复族”。记录和正文均已读。其同族 `RS-HBW-WEIGHTED-STABILIZER-IMAGE-KERNEL-20260927`、`RS-HBW-WL-WM-RECONCILE-20260927` 的记录目录已见，WL 发布入口也列有这两个后续方向；不替换或重复派发它们。
2. QFT 低精度/完整行查询、RP6 完整值共享、相邻位/楼板矩优化仍由原路线续接。此处候选 A 仅是可并行交付的全局误差认证子单元，不接管原查询器实现。若最新状态已包含同一交付物，直接把本稿作为原任务输入，不再新增。
3. 相邻非顶位的首次执行已经完成，不应重派。GLOBAL_KNOWLEDGE 的固定日志 `5d0666f3da748cdc7ff1c9b00cb154066567b551:journal/enterprise-math/2026-09-27/20260927T084355Z-qft-top-fast-c6438c.md` 记录：相邻版 37 个值、1152 个新付费有序对；生产算术 126950 对比较器 52700，六组均更贵；当时仅发布整理待完成。该信息在本轮用于防止重复科学执行，不冒充本轮重算或独立验收。后续短区间、重复表、混合核优化留原线。
4. LOW/Beta 到 B11 的横向导数修正保留原 D25 路线，不另立同题。此项依据本次对话用户指定的既有路线作保留决策，本轮未重新审查其全部数学证据，不升格结果状态。
5. 已读 `RTASK-RF-FINITE-BUDGET-STABILITY-20260927` 和 `RTASK-RF-ORDERED-PATH-RESIDUAL-20260927` 正文：分别研究五状态控制预算与端点条件矩。下面的首达阈值问题和 QFT 全局误差认证不应借其名称重复发布；正式发布前仍需完整语义去重。
6. `RS-SHOR-FAST-ROUGH-INTERVAL-GCD` 的记录已读，其目标是粗糙整数的区间素数积 GCD，不是本轮原生 QFT 近似行查询；不能仅因同属 Shor 而把候选 A 强绑到该母目标。

---

# 候选 A：原生 QFT 近似查询的低成本全局误差证书

候选标识（仅本稿内）：`QFT-MASS-CERTIFICATE`。
关系：原低精度行查询路线的并行证书子单元；不是重开 Shor 主线。正式 parent_objective_id、lineage 和 parent_task_id 必须从届时当前任务源绑定，本稿不猜造。

## Mother question

在不预先给出模乘阶/因子的前提下，怎样低成本地认证一个既定、轨迹一致的完整行近似器的总误差，使“只保留可辨认信息”落实为最终输出分布的界，而不把指数遍历藏进证书计算？

## Frozen inputs and scope

固定 `awdawmip/enterprise-math@86022c1ee4de09a9c9055f4c6806a5d35459edfc`：

- `research_notes/directed_recovery/20260927_C6438C/qft_row_queries/README.md`，blob `c60da0b31a4024ecedc8aad8bb43d1333f0d2d38`。
- 同目录 `point_queries/MASS_WEIGHTED_APPROXIMATION_BOUND.md`，blob `32b746b30b9a0602715e44c662cae5c5a15044a0`。
- `definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json`，blob `de980f972de840c55d2535dbf4e40be7e03659ed`。

精确行 v_h(w) 与近似行 u_h(w) 都保留完整原生坐标/残差。u 必须是公共 (h,w) 和独立固定种子的函数，不得依赖当前 latent 私有路径；重复查询一致。使用原单 walker 提议和两臂读出，不改换成未经对应的传播器。允许一个明确受限的输入族及近似器，但必须声明其构造、零回答回退和失败事件。

原作者候选界为 E_h=sum_w||v_h(w)-u_h(w)||^2。对坏历史集合 B_i 的精确质量上界 beta_i，以及好集合误差总和的认证上界 epsilon_i，目标使用：

    TV <= min(1, sum_i (beta_i + sqrt(epsilon_i))).

此界是源中的 AUTHOR_SYMBOLIC / SHARED_CONTEXT / NOT_ADMITTED 候选，需核对其假设；不是高效认证器已经存在的证明。精确阶查询归约不是一般近似算法不可能性定理。原生采样逼近、理想 Shor 分布逼近和因数恢复成功率是不同层，不能合并宣称。

## Hard target and required outputs

交付一个明确的证书格式、构造/合成规则与验证器，输入给定的近似器及其公开分区/截断规则，输出 beta_i、epsilon_i 的有理或有向界；健全性须覆盖所有声明历史，而不是一条所抽轨迹。先在含非零反馈的明确小族上使用原 BRC/完整行接口给出可重算对照，再为一个非退化参数族证明证书构造或验证成本界。

至少交付一项新的判别：证书在某个无限受限族上确实避免完整历史×工作标签遍历，并给出总资源节省；或对冻结的证书载体构造反例/成本障碍，明确指出欠缺哪一项联合信息。单独再次推导上述总变差界不算新交付。

成本逐项包含：近似器/分区初建、完整值及标签关联保存、证书生成、验证、整数位数、失败概率、误差舍入和每次查询。零历史可作诊断，但不能凭其压缩率声称典型或高质量历史可压缩；不得事后挑选成功样本。

## Research value to preserve

把原线已得到的全局误差契约变成可付费、可复核的部件。原查询器研究仍可独立推进，消费本子单元提供的证书或障碍；本任务不预设正质量可以有符号抵消，不强制所有历史常驻，也不要求一个笼统的通用多项式 Shor 结果。

## Success, kill, and return criteria

成功：完整健全性论证、声明范围内的精确对照与总成本界；或冻结载体上的明确否定证书。仅有经验误差小、单行便宜、免费阶/因子输入、私有轨迹依赖或把认证开销漏账均不通过。若最新原任务已经覆盖同一认证交付物，不发布新任务，只归并此输入；不得以改名绕过去重。返回时区分符号证明、实际执行和独立审查。

---

# 候选 B：心跳世界首达观察的安全降精度与首次分歧边界

候选标识（仅本稿内）：`HBW-FIRST-HIT-PRECISION-GAP`。
关系：对 WL 已有“强证书失败但指定观察未变”见证作独立的参数化研究，不重复多层 transporter/稳定子任务，不另建大而泛的残差理论。
母目标候选：既有 `PO-HBW-WEIGHTED-REPAIR-20260927`；正式 publisher 仍须核对当前目标/依赖绑定。

## Mother question

在指定初态、允许操作和首达读出下，普遍作用证书开始失效的阈值，与实际首达分布首次不同的阈值，相差多少？能否给出不先验证全部安全输入格的、可计算的观察保真判据？

## Frozen inputs and scope

固定 `awdawmip/enterprise-math@9fcdbe1ad147a125464ae35fcf1dff493cec505d`：

- `research_notes/heartbeat_weighted_lift_20260927_AD0416/README.md`，blob `0d783a37e6a3389dbcae42692569e5824a7cf27f`。
- 同目录 `RESEARCH_NOTE.md`，blob `866a5bdc458f58414e028bff33f2bd6c91f826e0`，尤其 HBW-WL-005/006。
- 完整依赖包按上述 README 的 PUBLICATION/Drive 校验链获取；WL snapshot 不是 WM 主干模块的可互换副本。

原生六轴为二维块重复三次。取 U=diag(2,1)、V=diag(1,2)、E_k=I+2^k E_12，k>=1。基线在活动端口 U、V 各质量1/4，停止质量1/2；扰动为 U、UE_k 各1/8，V为1/4，停止1/2；停止后恒等。初态严格复用原 WL 证据中声明的初态，并将其完整原生表示写入新交付物，不能私自换成方便的初态。原始 ports、weight、multiplicity、action、translation 及观察限制保留。

精度阈值 R 与时间拍 t 分离。目标是完整首达时间分布/其生成函数，不仅某一时刻样本或最终命中概率。科学接口优先复用原 `compile_carry_peak -> PeakChain -> ControlMassQuotient/finite_recurrent_mass_analysis` 与正质量 star；不把修复数计为概率。

已知 k=1 的作者源见证：R=3 的指定可达观察链完全一致；R=4 首次在 t=8 分歧，基线 56/131072、扰动57/131072。本稿引用而未重跑，不宣称独立认可。

## Hard target and required outputs

对至少一个非平凡 k 参数族，定义并刻画：普遍作用证书的首次失效阈值、从声明初态出发的完整首达分布首次变化阈值，以及变化阈值下最小分歧时间。给出足以支持参数族的证明、显式上/下界或参数化反例；不能把 k=1 数值直接外推。

交付声明观察/初态/时域的精确保真证书，并至少有一例出现“普遍证书失效而观察证书仍成立”；对实际分歧输出最短见证及精确有理质量差。有限有理链的标准等价检查或生成函数相等只是验证基线，新增价值须来自此原生族的边界定理、较弱充分条件或严格资源改进。报告可达状态构造、最小化、验证和整数位数成本；预算不足用 UNKNOWN，不用未发现差异冒充等价。

## Research value to preserve

区分“当前看不见”与“在声明未来语言下始终无关”，避免一端无证删除残差、另一端为目标观察不需要的普遍证书过度付费。这是正质量 BRC 观察问题；不把它与 QFT 有符号振幅当同一代数。

## Success, kill, and return criteria

成功为明确参数族的观察保真范围及边界证书，或证明拟议降精度必失败的参数化反例。只重跑 R=3/4、把最终命中概率相等当完整首达律相等、把 m 与 t 混同、忽略不可达/UNKNOWN 质量，均不通过。若 WL/WM 对照发现所需观察接口不兼容，保留分别分型的结果并返回确切缺口，不覆盖任一模块。若最新现有任务已覆盖这一交付物，归并而不新发。

---

## 规范发布恢复点

这不是要求改变控制面或部署。当前有权限的 publisher 应先读取最新规范和上述终态回执，处理/避开实际 Source 树读取上限所需的受支持路径，核实本次失败未产生会话/任务。不得借用 EM-DIRECT-AD0416、EM-DIRECT-C6438C 等原作者身份，也不得将失败会话伪装为 ACTIVE。

然后针对两个候选分别重新核对当前任务正文、有效 publication、活动 owner 和最新成果。已有同一任务即消费输入；真正独立时绑定实际母目标与 lineage，完成五段非空任务正文、实际 policy audit PASS、source-backed publisher、精确 taskbook blob、所有 origin/successor gate 与原子发布检查，最后在同一可见提交发布 taskbook+V2 记录并回读。缺任一条件仍保持 NONEXECUTABLE_DRAFT。

不得顺手调整原主线、依赖、优先级、owner、定时任务；不得重跑已完成的相邻位首次实验。本轮没有新增科学执行、独立审稿或正式接纳结论。
