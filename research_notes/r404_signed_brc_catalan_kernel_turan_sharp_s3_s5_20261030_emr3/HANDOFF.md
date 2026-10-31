# R404 作者侧精确研究 HANDOFF

研究身份：Researcher-ID: EM-R404-3C89B8 / TASK_RESEARCH。GitHub 实际连接身份 awdawmip。本交付是研究原件保全，不替代 Source Native CLAIM、Result、独立 Review、Owner 接纳。

科学前沿：由 R402 全余阶 Laurent 展开及 R403 Turán 首项恒等式，建立新的全余阶 Catalan 非负核公式 R404.1；进一步证明所有 r≥4、3≤s≤min(5,r−1) 的 D_(r,s)>0，故 T_(r+s) 在 a=30−16θ=0 处恰消失 4s 阶。与 R403 s=1、2 合并，前五条退化阶数对全部适用余阶已取等号。

本轮新增且已完成的证据：R404_PROOF.zh-CN.md 有完整有限代数证明与六个显式有理恒等式。verify_r404.py.gz.b64 是实际执行标准库源码；R404_EVIDENCE.json.gz.b64 是原始机器证据。R404_EVIDENCE_INDEX.md 给出无损恢复与 SHA256 检查。执行返回 R404_EXACT_PASS，严格范围 r≤512；有限验证不代表无限命题的证明，数学证明来自显式恒等式及正系数代换。

不可重做的已验证前沿：R402 Catalan 最高系数、R403 s=1/2 严格符号及 r≤240 有限扫描均已有原件，不重复作为本轮新发现。不修改 P000、ACTIVE 世界观，不将带符号辅助模型接入未经证明的原生 X6/三维切片动力学。

冻结读入：GLOBAL_KNOWLEDGE_V1 main@b8632f1fb3f57d217415c7580f24bc79db6dce0c；Enterprise Math main@2fdba2f4e10aea0c41c4178535edcdf69bc92fbf；R403 PR HEAD@dabf55feaa5bf9f72abff704a307a76f1e5dd139。正式 Source Owner 未核验，原生服务 v0.6.11 research_authority_granted=false，executor_binding_configured=false，quota 5/5，CODE_REVIEW_REQUIRED。故状态 AUTHOR_SIDE_PROOF / EXACT_PASS / DRIVER_UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING。

最小未解决问题：对全部 r≥7、6≤s<r 是否 D_(r,s)>0？尝试从 Catalan 正核取得统一 Turán/比值不等式，必要时构造 exact integer 反例；如无证明，改为逐个固定 s 的符号多项式证书，不重复固定 r 的 PF₂ 参数分类。审阅应特别核对 R402 形式外根分离、R403 的首项关系、R404.1 的 Laurent 系数索引及 R404.3/4 代数化简。
