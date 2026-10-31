# R425 signed BRC full Turán sign classification — next continuation

母目标：研究 signed BRC 辅助组合的 jet 与原生 X6 保真。当前仅为作者侧可移植研究；不声称正式 Task/CLAIM/Result/Review/数学接纳。

**已完成**：定义 δ_{r,q}=[t^r](1−t)(1+t)^{2q}(1+t²)^{r−q}, H_{r,q}=binom(r+q,2q)δ_{r,q}, D_{r,s}=H²−H_{s−1}H_{s+1}。对全部整数 r≥2,1≤s<r：D<0 当且仅当 s=1 且 r 偶数，或 (r,s)=(3,2),(5,2)；D 均不为零。新解析闭式解决 s=1,2 无限边界，s≥3 依赖已发表、未独审的作者侧 R404/R407–R418/R424 精确证书/傅里叶解析证明。R403 的 4s jet 非退化仅为其传递恒等式成立下的条件推论。

**验证完成**：标准库执行 R425_VERIFY.py，返回 R425_EXACT_PASS 12 2484 10296 74 2047。涵盖12点+次数11的严格多项式恒等式证书、2484项 signed 卷积与 Catalan 核重构、10296项有限 Turán 检查（74负例）、2047项边界闭式复核。无限 s≥3 不从网格外推。R425_PROOF.zh-CN.md 详列全称分区及依赖；R425_EVIDENCE_SUMMARY.json 给完整计数与边界；同脚本可重新生成完整 R425_EVIDENCE.json。完整本地原始 JSON 及逐文件 SHA256 在对话中的 R425 ZIP 包。

**本轮固定来源**：GLOBAL_KNOWLEDGE_V1 main bb5d22a791f3b28aa6998efcb53f4f1b9683a12a；Enterprise Math canonical main 75b88a101f96112098c70438babbf626a1940da8；上游 Draft PR #1708 原始 R424 head 94ae64f9f7351509b21cefe20fec98e9c935aa1b。GitHub 用户 awdawmip。原生 DIRECTED_RESEARCH authority_granted=false，em_control_tasks CONTROL_QUOTA，Owner 未权威确认，正式 CLAIM/Result、独立审阅未完成。P000、ACTIVE worldview 未改。

**下一最小数学问题**：逐行独立审计 R424 负半弧 Beta 上界，并尝试从单一傅里叶解析关系把统一充分条件 s≥50 降为 s≥3，解除 R404—R418 逐带系数证书依赖；另研究 signed BRC → 原生 X6 的 typed 观察者/后续操作保真界面。保留所有签名分支身份和 provenance，不从标量正性假定原生正质量。
