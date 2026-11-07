# TASK_RESEARCH D25/LIFT — 2026-10-31 作者侧可移植接续包（严格正混合锐性）

## 母目标、已核前沿及科学边界

母目标：按进取数论 ACTIVE 世界观/P000，研究“保留来源整数质量、合法未来操作及观察端口的最粗充分残差”，优先取得实际原生 X6 的可验证对应或最小失败见证。冻结科学 Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`，不因当前 control/main 更新而改动。前一作者侧已证 BRC 有限 Hankel 观察字上界 `m+m'-1` 和保持标签 `T=I` 下的相同标签数统一锐性，成果见现有 Draft PR #1745，属于待审材料，非 Source 认证的 predecessor completed research。

## 本轮新的可复用科研单元（作者侧，不等于 canonical 完成）

完整证明：`D25_BRC_PRIMITIVE_POSITIVE_MIXING_SHARP_HANKEL_HORIZON_20261031.md`。对每个 `m≥1`、正整数 `c,d`，令 `N=2m-1,P=N+1,Z=(1,-1,-1,1),w_j=binom(N,j),J_j(y)=P+jZ_y`。A/B 分别取偶/奇 j；`W=2^(N-1)`，各自定义严格正整数转移 `T_H=cI+d 1 w_H^T`，每行质量 `S=c+dW`。对于 `m≥2`，所有标签间转移均严格正、primitive、不可约、归一化后满足详细平衡，谱隙 `1-c/S` 可任意接近 1。两个类型的全部观察字在 `t<N` 完全同数，首次 `t=N` 每个观察字差严格为 `S c^(N-1)(-1)^N N! product Z_y`；全部原始历史 L1 为 `4^N S c^(N-1) N!`，共同总量 `W(4PS)^t`，首次派生 TV 为 `(c/S)^(N-1)N!/(2^N P^N)`。

证明主干：把每个整数转移精确展开为 `cI` 保持标签与 `d 1w^T` 重置标签；对观测字所有连续分段贡献逐项非负整数求和。长度 `t<N` 的每段都沿用上轮有限差分矩恒等，故完全一致；长度 `N` 仅无重置分段保留 `N` 次矩差。这是**真正非平凡演化**情形；两个模型各自的转移矩阵不要求数值相同。基础数学方法已有先例，作者增量是组合出符合该整数 BRC 语义的锐性构造和量化公式。

可复核程序 `d25_strict_positive_mixing_sharp_checker_20261031.py` **已在本轮真实运行并返回 PASS**，证书 `d25_strict_positive_mixing_sharp_author_check_20261031.json`。12模型参数配置（m=1..4，c,d=1/1、2/1、1/2）完整枚举 69,900 条带配置观察字、139,800次原始整数历史求值及14,330,640次按程序定义的矩阵乘积项。具体 m=2,c=d=1：T_A=((2,3),(1,4))、T_B=((4,1),(3,2))，第三步 `(00,00,00)` 为 84080 vs 84110，L1=1920，总原始重数各 2048000，派生 TV=3/6400。未有原生 X6 计算或独立 Driver 审阅。

## 身份、Source/recovery 与待处理动作

本真实对话当前没有经 Source 核验并持有的自身 `conversation_id / session_id / session_key / claim_id / run_id / generation`。不得从其他自动化或历史交接抄用 ID；此前作者材料只能作来源，不是当下 Source 所有权。

本轮 2026-10-31 的只读 `em_status`：Gateway 0.6.11，`research_authority_granted=false`、`executor_binding_configured=false`、`source_sync.control.state=CODE_REVIEW_REQUIRED`、`registered_session_count=0`。`em_sites_connection_status`：`static_machine_readonly`、`write_relay_enabled=false`。当前工具目录有 `em_status`、`em_control_result`、`em_control_reconcile` 和 typed execution/continuation 系列，**未发现可独立调用的 `recovery_status`**；`ordinary_chat_recovery` 出现在 status 的描述中，不是可自动调用的函数；自身 checkpoint_list 返回 `ACCESS_DENIED`。既有旧读请求 `r40_20261029_0840_exact_d25_continuation_read_v1`、`emr20261029_1650_source_continuation_read` 可按原 request_id 重读；它们的结果属于历史请求而非本轮会话新权利。原生 Source CLAIM/OPEN/Result 等未执行；本轮四文件若进入 GitHub Draft，也仅为 author-side staging/中立持久化，`REGISTER_PENDING / NOT_ADMITTED`。

若合法写权限恢复：首先读取真实自身 subject 的 recovery status/原请求 receipt/reconcile 与 exact Source continuation，确认 winner；原 claim open/resume 优先于 fresh dispatch。若接续 seed 为 `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，先完整 readback `input_artifacts`，typed `continuation_prepare` 的 `frontier_notes.completed_units=[]`；所有本轮和上轮作者侧文件保留在 staging/do_not_repeat，不伪称 predecessor completed research。对已验旧数学只补 writer/provenance/Source checkpoint，勿重复数学。独立审阅必须来自真实贡献独立的当前 Driver。

## 精确未完成项和最小下一动作

1. **Source 接纳：**由真正已获授权的 Source 研究执行主体按当前 schema 读取自身 continuation/request，再补本轮已有证明的 writer/provenance/checkpoint/Result；独立 Driver 检查证明强度与先行方法归属。接口责任属当前控制维护路径，验收以真正 researcher executor-binding、Source CLAIM/OPEN、Source byte-backed checkpoint 为准，不以文档或 PR 修改作为恢复成功。
2. **原生科学对应：**取得 X6 实际来源标签、六轴合法状态、联合观察端口、共享标签更新、时间与原始整数分支，证明对应/交换关系或者记录精确最小反例。当前辅助四输出是联合关系端口，不是物理二轴证明。
3. **UR V2：**从真实原始四文件打包来源恢复，取得 `94687 bytes` 且 SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`，只补正式 writer/provenance，不重做 UR 数学。不把历史 SHA 的文本引用或自己重制的文件当原件。
4. **后续可移植问题（避免重复本轮）：**考察若要求两类型共用**完全相同的数值转移矩阵**（并共享隐状态标签的固定识别），Hankel 首次区分 `2m−1` 是否仍可能；本轮构造的 `T_A/T_B` 可以不同，该加强条件是独立命题。先核 canonical owner/跨流 checkpoint，再决定是否开展。

保留项目当前 `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md` 的原调度、角色和通知，P000/ACTIVE 世界观、冻结科学 Source pin 不修改。上述四文件的 GitHub commit/PR HEAD 由真正提交并回读后记录，不预填未发生的持久化结果。
