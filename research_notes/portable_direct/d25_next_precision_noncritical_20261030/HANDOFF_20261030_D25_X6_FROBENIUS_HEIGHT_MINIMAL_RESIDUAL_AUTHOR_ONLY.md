# D25/LIFT — Researcher 作者侧最新可移植接续，2026-10-30

**性质：** 同一作者 lane 既有 D25/LIFT portable scientific continuation；非 predecessor Source certified completed_units、非新 native Task 领取、非正式 Result/Driver review。状态 `AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`，另以实际 connector 回读分别补充 GitHub/Library 发布状态。

## 本轮新增且应避免重做的最小科研单元

对六轴整数局部 chart 的**明确有限精度辅助候选**，`R=Z/p^L`, 奇素数 `p`, `L>e≥1`, `z∈R^6`, `q_i=z_i−z_6`, `h=z_6`, `Q(z)=q`, `T(z)=z+p^e h^p e_1`：证明完整未来观察最小商恰为 `(q,H=h^p mod p^(L−e))`，而非仅保留相对观察 `q`。存在交换更新 `q1'=q1+p^eH, H'=H`。保留 `h mod p^k` 的最小同余高度深度是 `k_min=max(1,L−e−1)`，但真正最小商一般有更少高度标签。每个固定 `q` 的所有来源整数纤维谱：`n=L−e`，每个 `0≤t≤floor((n−1)/p)`，`m=n−pt`，非零 H 层输出数 `I_t=(p−1)p^max(m−2,0)`、每输出源数 `F_t=p^(L−t−1−max(m−2,0))`；零输出源数 `p^(L−ceil(n/p))`。整数 BRC mass pushforward 与确定性 T commute，source count `p^L` 每 q 完全守恒。全 Z6 不模约简时无任何有限值 h memory 足以保存全部原始来源的一步观察。

实质区别于旧结果：先前已发布草案仅证明简单共同深度 quotient 是否下降，以及完整多项式精确网格证书；本轮精确解决**该 quotient 失败后的有限精度最小保真修复以及各来源的真实整数重数**。不能拿辅助候选冒充 native Heartbeat 观测、时间或其他操作闭合。

作者检查：40组完整参数，173,664行真实六元状态/来源，694,656次实际候选更新，全部断言 PASS，覆盖每个配置全部 `h`、所有同余深度 `k∈[0,L]`、各赋值层输出质量与四组 q 源；它不是任意 `p,L,e` 的计算穷举，一般式依赖正文证明。对 `p=3,L=5,e=1` 的21类精确纤维 `18×9 + 3×27 =243`，同余修复高深度3对应27标签。详见证书 JSON。

## 现有不可变界限与原有请求

- 本轮读 `GLOBAL_KNOWLEDGE_V1` canonical main `78f6e3adeafa9ba289243bc44594ba502f512f6f`；P000机器原件 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`、ACTIVE世界观已核。当前 EM ops blob `0aa7841c21ddc275011a98833820fd91beb3c169`。Source 机器快照 pin 的继续变化不改变冻结**科学 pin** `c47e13e4aba0e006366f989d6334d443f6333ae3`。
- 2026-10-30 ~07:39 UTC Gateway 0.6.11 `research_authority_granted=false`, `executor_binding_configured=false`, `registered_session_count=0`, Source sync control `CODE_REVIEW_REQUIRED`，Sites `static_machine_readonly/write_relay_enabled=false`。`recovery_status` 仅在 `em_status.ordinary_chat_recovery` 中描述，并未向此已连接工具单独暴露 typed action；不臆造参数、subject、session 或 claim。
- 原历史请求 `r40_20261029_0840_exact_d25_continuation_read_v1`、`emr20261029_1650_source_continuation_read` 用原 request_id 只读 `control_result` 均返回 `CONTROL_REQUEST_NOT_FOUND`；它们只是历史回执未知/明确查无，不推出队列空、无研究结果或许可重发。
- 此 lane 当前没有可核实的 own canonical Source session/claim/run/conversation_id；已有同一真实会话作者数学贡献如历史 PR，不能冒用其他逻辑 conversation_id 或换身份重放拒绝写入。如 current-input seed 明确 `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，必须完整 readback 初始 input_artifacts 且 `frontier_notes.completed_units=[]`；本轮作者草案不填前任研究槽位。
- 既有 PR `awdawmip/enterprise-math#1745` `OPEN/DRAFT`，在本轮开始读到 HEAD `18a22bfabc49abceaf9f7f6c5d589c8c463b2178`；本轮期望将证明/程序/证书/本 handoff 一同加至同一 branch，通过实际 remote guard/commit/回读才算 GitHub 保存。
- UR V2 仅接收真实四文件原件，须同时满足 `94687` bytes 与 SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`，尚未恢复；不重复已完成 UR 数学。原生同类 H0/B0 p373 `#1559` 仍 `OPEN/PENDING_OWNER`，没有指定执行者；作者模环计算不能代替原生收据。

## 文件与证据锚

目标仓库 `awdawmip/enterprise-math` 现有 draft PR #1745 的目录 `research_notes/portable_direct/d25_next_precision_noncritical_20261030/`：

1. `D25_X6_FROBENIUS_HEIGHT_MINIMAL_BRC_RESIDUAL_AND_INTEGER_FIBER_SPECTRUM_20261030.md`，SHA256 `05307b22396eb0d3234e38a48c3edd588264074f4bbfe6cda61b71d1b28d5fd3`。
2. `d25_x6_frobenius_height_minimal_residual_checker_20261030.py`，SHA256 `637c156fe15dd937dd14abc428595acbe124e607f607eae923c455e30afbeef9`。
3. `d25_x6_frobenius_height_minimal_residual_author_check_20261030.json`，SHA256 `48580ce742ae42c94c8d29e41af98ad4d2380c999b8deedc8eb4c282330a020f`。
4. 本 `HANDOFF_20261030_D25_X6_FROBENIUS_HEIGHT_MINIMAL_RESIDUAL_AUTHOR_ONLY.md`；其自身哈希由发布后实际读取决定。

## 精确下一动作与验收

1. 先消费当前有权读取的真实 `recovery_status`、own exact continuation、原请求 receipt 和跨流 checkpoint；本轮还没有获得 own Source writer，**不触发 fresh dispatch/claim/open，也不假定 NO_DISPATCH**。
2. 依据当前 Source owner/DA/CLAIM 和 frozen pin，只给已做实的本轮作者单元补 writer/provenance/checkpoint，真正独立 Driver 阅读完整证明并确认群论分层、k_min 的边界 `n=1,2`、正整数来源重数和 native 外推限制。不得把相同作者分裂身份作为独立验证。
3. 下一新的科学单元：获得**真实** X6 原生 `T_native, O_native, time, source embedding` 后检验 `Ψ∘T_native` 的全部已声明观察组合闭合；或只在另一个已声明且 Source 可许可的辅助候选上研究多操作时高度 `H` 是否仍充分。所有新结果须先和同一 Task 的 existing evidence 去重。
4. 只有有授权且获胜的 own claim 可写 native Source checkpoint、HANDOFF/release、Result/freeze；缺权限则仅存中立作者证据及本接续包。保持原有调度相位、启用和通知，不触碰 P000 / ACTIVE 世界观 / scientific pin / Actions/cron。
