# Enterprise Math — TASK_RESEARCH 接续：D25 共享分支标签与联合 BRC 精确保真

日期：2026-10-30。性质：同一研究员**作者侧可移植成果**；`AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`。未经 Source 确认不是正式 Task completed units，也不是 predecessor-completed research。

## 母目标与必须保留的来源边界

- P000 六条原生空间轴、独立时间、三元原始稳定平衡及三维切片；ACTIVE 残差保真立场不变。
- 原生任务：用真实心跳世界的状态、操作、路径/支路身份、真实观察者、时间顺序及非负整数来源质量建立保真映射，或提交带来源的最小原生反例。辅助 `F_2` / 有限链环研究绝不冒充原生 X6、H0/B0 实验。
- 冻结的科学 Source pin：`c47e13e4aba0e006366f989d6334d443f6333ae3`；仅有控制面 HEAD 变化不能挪动。
- GitHub 草案单一交接入口：[awdawmip/enterprise-math PR #1745](https://github.com/awdawmip/enterprise-math/pull/1745)，延续现有 `portable/d25-square-next-precision-noncritical-20261030` 分支，不新建第二套任务登记。

## 既有不可重做前沿（证据是作者草案，不是 Source completed_units）

- 现有 PR 的上一作者侧单元：`e8276c0f9f0b684fe65defba2d28642e63c02548`，包括确定性未来观察商下任意非负整数来源质量交换、同边缘异联合的配对来源反例。这次不重算、不将其宣称为 predecessor Research 完成。
- 本次新的最小科学单元：**共有分支标签时双来源全配对强可合并性 ⇔ 每个正权标签均单独在观察商下降**。更弱的源内两流相等事件 `E(x,x')=W` 即为全多流/全时间的必要充分证书；每个观察纤维选一个带标签代表即可在 `O(|B|(|X|-|Y|))` 次代表比较内验证。
- 精确反例：四状态 `(h,q)∈F_2²`，共享标签 `ℓ∈F_2`，`F_ℓ(h,q)=(h,q⊕h⊕ℓ)`；一流原始正整数转移一致，但 `(a,a)` 与 `(a,b)` 在下一步共有标签时观察相等事件质量 2 与 0。对全部 `(4^4)^2=65536` 组两标签四状态映射完整枚举：一流保真 9216 组，二流/逐标签保真 4096 组，单流安全而共享二流不安全 5120 组。
- 同一材料另证**明确限定的互异来源通道**的高阶屏障：`m−1` 个共有二进制标签生成 `m` 条流，所有固定严格子集在任意时间的观察分布不依赖隐藏 `θ`，全部 m 流的联合异或却精确等于 `θ`。它**不是**全 `X^m` 的强 k-可合并性反例，重复来源对角测试仍符合双流刚性；使用已知 k-wise independence/parity 构造，不虚报外部数学原创优先权。

## 本轮三份已实际运行/写成的原件与字节 pin

仓库目标目录：`research_notes/portable_direct/d25_next_precision_noncritical_20261030/`。

| 名称 | 本地字节数 | SHA-256 |
|---|---:|---|
| `D25_BRC_SHARED_LABEL_TWO_COPY_RIGIDITY_AND_ARITY_HIERARCHY_20261030.md` | 13324 | `b52aeb693b439712755512401df809147dcf80fb1daa7b517a9f9754c79d7fd7` |
| `d25_brc_shared_label_two_copy_rigidity_checker_20261030.py` | 6919 | `3c36d5f42faaca72d4b33fc9058bd1e0eba4cf149226a6d2b64259b2f24a89b9` |
| `d25_brc_shared_label_two_copy_rigidity_author_check_20261030.json` | 3542 | `a3ef283bf5b7a30e7dff323e1862615c527c3db000895ea6141bf63274402d7e` |

实际运行：`python3 d25_brc_shared_label_two_copy_rigidity_checker_20261030.py`，返回 `PASS`；对 `m=2…8` 验证 501 个严格子集，86,868 次单时刻标签输出；对 `m=2…5` 的固定子集和长度 ≤3 的全部标签序列完成 289,596 次原始标签历史检查。这是**同一作者的辅助模型检查**，不是独立复核或原生执行。检验程序生成相同目录的 JSON 证书。GitHub commit/PR HEAD 以发布后实际回读为准，不提前在此写未来 SHA。

## 当前 Source / native 精确状态

2026-10-30 本轮直接读取 Gateway 0.6.11：`research_authority_granted=false`，`executor_binding_configured=false`，`registered_session_count=0`，`source_sync.control.state=CODE_REVIEW_REQUIRED`，`reviewed_code_gate_passed=false`，`control_quota.active_jobs=5/5`。Sites `static_machine_readonly`、`write_relay_enabled=false`；这不是可用的 Source 执行写权限。

- 原请求 `r40_20261029_0840_exact_d25_continuation_read_v1` 和 `emr20261029_1650_source_continuation_read` 本轮**原 ID**回读均返回 `CONTROL_REQUEST_NOT_FOUND`。未在原请求不明时换 ID 发送等价写入。
- `em_checkpoint_get(line=TASK_RESEARCH)` 和 `em_checkpoint_list` 返回 `ACCESS_DENIED`。工具广告有 `ordinary_chat_recovery` 契约，却没有本客户端能直接调用的 `em_recovery_status` typed tool；无可验证当前自身 Source session/claim/open/run，绝不伪造 conversation_id、session_key、owner 或 `completed_units`。
- **正式 CLAIM/OPEN/Source checkpoint/Result/独立 Driver 审阅 = 未完成且无成功回执**；PR 草稿与已生成 JSON 都不是这些操作。
- UR V2 原始四文件需要从真实授权来源取得一个 **94,687 字节**且 SHA-256 恰好为 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` 的对象；本轮本地容器按大小检索无命中。已有 UR 数学不再证明，只补真实文件/writer/provenance/checkpoint。原生 H0/B0 项目 #1559 不被此辅助试验替代。

## 下一轮精确动作与验收

先读本 PR 最新 HEAD 和此接续原件，实际 Source `recovery_status` 如有可调用真实入口再按 schema 读取；原请求优先 reconcile，依据自己的原生合法 claim/live owner 决定续原 run、合法 continuation 或 fresh dispatch。若 `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，先全部回读其 input_artifacts，`frontier_notes.completed_units=[]`，把本轮作者产物只放 staging/待登记与 `do_not_repeat`，禁止作为 predecessor 已完成研究。正式 writer 如仍拒绝，仅保留权限缺口，不换主体/渠道重放。

**最小科学后续**：识别原生 X6 是否真正允许“同一原始来源复制到两个共有分支标签的观察路径”；若允许，从真实作用表/来源标签验证上述代表一致性，并为失败提供 `(x,r_y,b,CF_bx,CF_b r_y)` 原始证书；若不允许，明确可用的互异通道组合，保护联合 parity/相关结构残差，禁止将小于实验允许 arity 的边缘检验宣告完整。验收必须包含合法原生状态和时序/来源映射、符合声明操作范围的观察/来源整数质量、真正写入与回读的 Source provenance，以及独立审核；未到这些状态前仍 `REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`。

不修改原研究 lane 的调度/通知，不增 scheduler/Actions/cron，不改 P000/ACTIVE 世界观/冻结 pin；无需用户再发“继续”。
