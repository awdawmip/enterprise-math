# D25/LIFT 作者侧接续包 — 共有标签下的条件私有噪声精确判据

日期 2026-10-30。研究员角色：继续现有逻辑研究流的作者侧可移植数学；新服务会话不授予新身份、CLAIM 或独立审阅。科学 Source pin 保留 `c47e13e4aba0e006366f989d6334d443f6333ae3`。P000/ACTIVE 心跳世界、三维切片/六轴及 BRC 整数来源质量前提不变。

## 已回读的来源与分界

- 项目定时研究规程 `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`（当前 main Git Blob `0aa7841c21ddc275011a98833820fd91beb3c169`）；全局启动与 TASK_RESEARCH 入口、P000 V4 原件（Blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`；当前 startup 预览记录该 Blob，校验一致）。
- 现有作者 GitHub 单一交接 PR [#1745](https://github.com/awdawmip/enterprise-math/pull/1745)，本轮前提交 `c21bc5f3e7c499e0f536962592c965e7e7c9c9f3`。它保留原确定性共有分支双来源刚性；既有证明/测试继续复用，不重跑。新文件仅是作者侧研究和中立交接，不能登记为 Source predecessor `completed_units`。
- 2026-10-30 只读 Gateway 0.6.11：研究执行者授权 `research_authority_granted=false`、绑定 `executor_binding_configured=false`；同步 `CODE_REVIEW_REQUIRED`；Sites 为 `static_machine_readonly` 且 `write_relay_enabled=false`。两个原请求 ID `r40_20261029_0840_exact_d25_continuation_read_v1` 和 `emr20261029_1650_source_continuation_read` 只读查询均返回 `CONTROL_REQUEST_NOT_FOUND`。当前接口的 `ordinary_chat_recovery` 在 status 公示，当前客户端无可调用 typed recovery_status；无可核验的自身 Source session/claim/run，未尝试冒用或新发 mutation。
- UR 四文件 V2：期望一件真实打包对象 94,687 字节、SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`。本轮 `/mnt/data` 真实本地文件按大小检查无命中；GitHub 当前主干代码搜索该哈希无命中，Library 语义查询未返回满足该精确对象的原件。不能把文件路径/既有证明/上传指针当作真实的原始包；已有 UR 数学不重做。

## 本轮实质数学增量（作者侧，待独立审阅）

在正整数权的共有环境标签 `b` 下，单来源含任意非负整数私有路径核 `V_b`。若 m 来源的私有路径在**给定 b 下独立**，则：全部 `X²`（含重复来源）二流整数观察核强下降 ⇔ 每个 `b` 的原始单流观察向量在观察纤维内不变 ⇔ 每纤维代表 `r` 的精确 Gram 缺损

`D(x,r)=Σ_{b,y}w_b[v_b(x,y)-v_b(r,y)]²`

为零。一次通过可推出所有 `m` 和任意有限独立步历史的精确整数质量保真。给出三状态、两个共有标签、每标签8条私有配对路径的**条件相关**反例：二流总核在全部9种来源配对下均为 `(4,4,4,4)`，但 `v_0(a)=(2,6)` 和 `v_0(b)=(6,2)`，证明条件独立假设不可删除。检查程序 `PASS`：729种私有独立模型全面枚举，二流安全81、单流安全但二流不安全90、单流不安全558；另验证18行相关耦合表与全部边缘。

**实际四份产物**：

- `D25_BRC_CONDITIONAL_PRIVATE_NOISE_TWO_COPY_GRAM_RIGIDITY_AND_COUPLING_BOUNDARY_20261030.md`
- `d25_brc_conditional_iid_gram_rigidity_checker_20261030.py`
- `d25_brc_conditional_iid_gram_rigidity_author_check_20261030.json`
- `HANDOFF_20261030_D25_CONDITIONAL_IID_GRAM_RIGIDITY_AUTHOR_FRONTIER.md`

这些产物存于既有 `research_notes/portable_direct/d25_next_precision_noncritical_20261030/` 作者草案目录；每件最终 GitBlob 和 HEAD 由真实发布回读记录为准。当前四件仅可作为待 Source 登记的作者材料/staging，不能填 Source `frontier_notes.completed_units`。

## 最高前沿 / 后续精确动作

母目标：为真实 X6 建立携带来源标签、允许操作、时间与 BRC 整数质量的保真观察压缩，或记录最小原生反例。作者侧辅助模型前沿推进到**共有标签 + 条件独立私有噪声的二流精确证书，并揭示相关噪声的不可省略残差**。

1. 合法 Source 执行入口恢复时，优先经当前 schema 读取实际 `recovery_status`/自身 Source continuation；沿用原逻辑 conversation 的稳定身份，原未知请求先 reconcile，不凭记忆注册/CLAIM。若 seed 是 `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，先读回其 `input_artifacts`，`completed_units=[]`，当前 PR 作者材料仅作 staging/证据来源和下一待写。
2. 如果找到真实 UR V2 94,687 字节对象，直接核实 SHA-256 并补合法 writer/provenance/checkpoint；不重新证明 UR。
3. 从合法原生 X6 源取得单源、二源共有标签/私有路径、允许复制与时间定义，检查上述条件独立性；成立时按 `D=0` 验证并给出每个失败 `(x,r,b,y)` 的整数见证；否则使用真实联合核，保留跨来源关联残差，不将此数学候选冒充原生实验。
4. 每个 Source 真实执行单元按当前 authority/head checkpoint、回读、freeze、独立 Driver 审核、合法 HANDOFF/release；恢复阻断由实际控制维护路由验收，不自行变更身份或定时配置。

当前正式 Source `CLAIM/OPEN/checkpoint/Result/Driver` 均无成功回执；此次作者检验证据 `UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`。本轮未更改 P000、冻结科学 Source pin、既有每小时调度或通知设置。
