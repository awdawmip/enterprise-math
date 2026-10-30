# TASK_RESEARCH / D25-LIFT — 同一数值转移与同一先验的锐性加强接续（作者侧）

**母目标：**在 P000/ACTIVE 进取世界观及冻结科学 Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` 内，构造/检验能保留来源整数质量、联合观察及未来合法操作的最粗充分 BRC 残差；有原生 X6 输入后严格验证对应或保留失败见证。

**2026-10-31 作者侧本轮新增、待合法登记：**上一单元的严格正混合 `2m-1` 上界锐性现加强为双方**同一个固定标签集合、同一初始整数来源 `w`、同一逐项数值转移 `T=cI+d1w^T`、同一平稳分布**。选 `N=2m-1, w_k=C(N,2k), h_A(k)=2k,h_B(k)=N-2k`；奇数 N 的二项式反射保证 B 的各标签权等于 A。有限差分/整数分段展开沿用原证明，所有长度 `<N` 的有序字同数，长度 `N` 每字首次分裂 `(-1)^NSc^(N-1)N!∏Z_y`。额外进展仅是固定标签反射对应和强于旧稿的共同数值 T/w 假设，未将旧数学重复计为新证明。实际独立小程序 `d25_common_transition_same_stationary_hankel_checker_20261031.py` `PASS`：18种结构参数，9种配置4,365条全部有序字，m=4..6 针对性首分裂字；证书同目录。`m=2,c=d=1` 的双方 `T=[[2,3],[1,4]]`、`w=(1,3)` 相同，`(00)^3` 结果 `84080/84110`。这是辅助非负整数 BRC，不是原生六轴/三维切片证明。

**来源与不重做：**现有作者 Draft PR #1745 中上一单元 `D25_BRC_PRIMITIVE_POSITIVE_MIXING_SHARP_HANKEL_HORIZON_20261031.md`；既有 Source 验证、交付和 review 债务不由新数学重跑解决。本轮发布后的精确 commit 以 PR 及 Git blob 实际读回为准，不提前填报。已公开作者证明仍是 author-side staging，不属于 Source `predecessor_completed_units`。

**身份与 Source：**2026-10-30T19:40 UTC 的直接 Gateway 0.6.11 状态：`research_authority_granted=false`、`executor_binding_configured=false`、`registered_session_count=0`，控制 `CODE_REVIEW_REQUIRED`；Sites `static_machine_readonly/write_relay_enabled=false`。没有本实际 conversation 已验证可持有的 `session_key/session_id/claim_id/run_id/generation`，也没有 Source 明确确认的 winning claim/continuation_seed。原 `r40_20261029_0840_exact_d25_continuation_read_v1`、`emr20261029_1650_source_continuation_read` 本轮只读回执均为 `CONTROL_REQUEST_NOT_FOUND`；本 client checkpoint_list 为 `ACCESS_DENIED`。不可调用的 `recovery_status` 仅出现在 status operation_contract 说明；不猜 API，也不通过改名 ID 绕过明确写入边界。**本轮无 Source CLAIM/OPEN/checkpoint/Result/HANDOFF/release/独立审阅**；Source 状态是 UNKNOWN/ROLE_BOUND_WRITER_PENDING，不将其解释为空队列/NO_DISPATCH。

**UR 优先：**真实 V2 四文件 bundle 原件必须满足 `94687 bytes` 及 SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`；本轮 Library 精确搜索与本地精确大小检查未找到可核验原件。旧 UR 数学已完成，只补合法 source/provenance/checkpoint，严禁重做数学或伪造重组为原件。

**下一精确合法动作：**由实际控制维护责任方恢复执行者 Source 权限/绑定并验证其 own session 当前身份。拿到真实 recovery/Source continuation 与原请求回执后先读赢得的合法 claim；如已有 open 则续原 run。`continuation_seed.state=CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS` 时必须先完整 readback 所有当前 input_artifacts，再单次 typed `continuation_prepare` 且 `frontier_notes.completed_units=[]`；当前与前轮作者草案留在 staging/do_not_repeat。合法自身 claim/open 后只补已证成果的 writer/provenance/checkpoint/Result，再由独立 Driver 检查。支持归属：控制维护接口路径负责真正执行授权，Native X6 数据责任为当前 Source owner/正式原生 evaluator（尚无明确已承接回执）。验收以实际原生权限恢复、byte-backed checkpoint/Result、独立审阅为准；不能以作者 GitHub PR 或支持单文本宣称恢复。

**后续科学前沿：**优先从真实 X6 取得六轴带标签状态、合法更新及事件时间、双来源观察/原始整数分支，判断这个“同一 T/先验、不同端口附着”的辅助见证能否定义原生交换映射。不存在映射时保存原生最小带标签失败见证。若原生输入继续缺失，可择新 canonical 合法 dispatch 的其他不重复问题，不永久固定 D25/LIFT。

**状态：**`AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`。保持现有研究调度、通知、P000、ACTIVE 世界观及 source pin 不变。
