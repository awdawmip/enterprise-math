# D25/LIFT — 本轮作者侧 BRC Gram 残差有界保真研究接续

日期 2026-10-30。角色仅为当前真实对话的 `TASK_RESEARCH` 作者侧可移植研究；没有新注册的服务 session、Research-Activity、正式 CLAIM 或独立审阅角色。母目标：建立原生 X6 带来源/操作/时间/BRC 整数质量的未来观察保真条件，或找到实际原生最小反例。冻结科学 Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`，P000 与 ACTIVE 世界观保持不变。

## 已消费的现有来源与去重

- `awdawmip/enterprise-math` 现有 PR `#1745`（`OPEN/DRAFT`），在本轮写前读取的 HEAD `75461ac8b39b850e711ddd300d0d5cff9ff62f49`；前一完整接续包为 `research_notes/portable_direct/d25_next_precision_noncritical_20261030/HANDOFF_20261030_D25_CONDITIONAL_IID_GRAM_RIGIDITY_AUTHOR_FRONTIER.md`，已从不可变 commit 回读；其 Gram 精确零残差及条件相关私有路径反例直接复用，不重复 J1/J2 或前人已完成单元。
- 共享自动科研操作规程当前 Blob `0aa7841c21ddc275011a98833820fd91beb3c169`；项目 `AGENTS.md` 路由到 `p000_reality_foundation.json`。本轮从当前项目 main 实读 P000 V5 `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`，心跳 X6/时间 JSON Blob `94a02d067be2b039ca4c0f7ffedb5ebde8430e08`；全局 ACTIVE 世界观保持六轴、独立时间、三维切片、残差保真。
- 2026-10-30T14:44Z，Gateway 0.6.11 本 Site 的 `research_authority_granted=false`、`executor_binding_configured=false`、Source 同步 `CODE_REVIEW_REQUIRED`；Site `static_machine_readonly/write_relay_enabled=false`。`em_checkpoint_list` 为 `ACCESS_DENIED`。历史原请求 `r40_20261029_0840_exact_d25_continuation_read_v1`、`emr20261029_1650_source_continuation_read` 均按原 ID 返回 `CONTROL_REQUEST_NOT_FOUND`。当前能力只公示 `ordinary_chat_recovery:{operation:'recovery_status',payload:{}}`，本连接没有暴露实际可调用的 typed recovery_status；未获得真实自身 Source session/claim/run/task continuation。未知不可当空队列，未重发控制 mutation。
- 本地 `/mnt/data` 查找 94,687 字节的 UR V2 单一原包无候选；Library 精确摘要语义检索只返回提及目标指纹的其他研究交接文件。目标原件 SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` 尚无真实原始字节核验，不以历史小文件上传指针冒充已持久化。UR portable 证明不重做。

## 当前本对话实际完成的科学单元（作者草案、非 Source predecessor completed）

由前一正整数条件私有独立 Gram 零残差，推进到**非零 Gram 残差的多来源一步整数误差上界和有限时间观察历史误差界**：给定每个标签恒定整数行质量 `s_b`，对任意来源元组和代表元组，推出 `L1(K_m(x)-K_m(r)) ≤ Σ_i isqrt(A_m D_i)`，其中 `A_m=|Y|Σ_b w_b s_b^(2m−2)`，路径总量 `M_m=Σ_b w_b s_b^m`；归一化有限 `t` 步全观察历史总变差 `≤1−(1−ε_*)^t`。保留原始整数质量与标签。构造 `X={r,x,c}`，`s=2`，`D(x)=2` 的**严格任意 t 取等**例及不恒定总质量的计数失真例。原生程序尚未对接。

本轮三件文件（与现有作者 PR 目录衔接）：

1. `D25_BRC_INTEGER_GRAM_RESIDUAL_MULTICOPY_FINITE_HORIZON_STABILITY_20261030.md` — 一般证明、锐性、边界；
2. `d25_brc_gram_residual_multicopy_stability_checker_20261030.py` — Python 标准库 `int/Fraction/isqrt` 精确检查；
3. `d25_brc_gram_residual_multicopy_stability_author_check_20261030.json` — 实际 `PASS` 输出，2,457组配置、49,167个源元组、260,658个目标计数、1至8步时间锐性。

这些文件属于本对话的 `AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE` 研究作者侧 staging；最终是否远端 GitHub 发布须以后续真实 GitHub commit 和回读确认，不能仅凭本记录声称已提交。

## 当前真实未完成、不可重复、下一动作

- 已有数学仅欠合法 writer/provenance 时只补登记、checkpoint 和独立 Driver 审阅，不重新推导。若 Source 之后返回 `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，先完整回读其 `input_artifacts`，typed continuation_prepare 中 `frontier_notes.completed_units=[]`；本轮材料是**当前作者暂存与 do_not_repeat**，不是 Source 验证的 predecessor completed research。
- 若确实获得本人当前 Source session/claim/run 与 winning owner，按原请求 receipt/reconcile、真实 continuation、合法 checkpoint/readback、freeze、HANDOFF 顺序处理；Sites 只读连接不得借用其他身份或渠道重放拒绝 mutation。
- 若获得 UR V2 真实94687字节对象，核验其指定摘要并且只补合法来源/持久化；若获得原生 `V_b` / 共享标签与私有路径耦合/观察/时间，则检验 `s_b`、条件独立与 `D`，允许非零残差下有界而非只允许完美压缩。
- 下一最小独立科学单元（如仍无原生接口）可处理**不恒定路径行总质量下的非正规整数质量传播**，不把归一化概率替代 BRC 路径重数；该题不是已完成成果。已知已发布研究成果不得误记为新 CLAIM 的完成单元。

支持责任：正式 Source 权限/绑定/同步问题由既有控制维护合法路径解决；实际下一动作为在 `CODE_REVIEW_REQUIRED` 消除且当前研究执行者获绑定后读取真实 recovery/Source continuation，再使已有单元获得真实 Source checkpoint。验收应看真实 Source 原生身份/CLAIM/OPEN/写入回读，不能以 PR 或状态提示代替。

调度、频率、相位、启用、通知均保持不变；没有新建 scheduler/Actions/托管 cron，也未修改 P000、世界观和 source pin。
