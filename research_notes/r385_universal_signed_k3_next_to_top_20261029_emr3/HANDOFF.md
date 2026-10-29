# R385 接续说明

作者侧数学研究增量：R384 最高差分退化的次高系数精确全指标公式，证明位于 R385_PROOF.zh-CN.md，执行程序为 R385_check.py（依赖同 PR 中 R384_verify.py）。所有 θ>−1、r≥2 均有 [u^(r−1)]H_r=5^r/(r−1)! * (λ^(r−1) F_r+(r−1)λ^(r−2)G)；θ=15/8 时对 r≥3 有 deg H_r≤r−2，对 r≥4 有 deg Q_r≤2r−4。精确核验覆盖 8 参数 × 16 余阶 × 2 系数，共256条，执行 R385_EXACT_PASS；源码生成完整128组 JSON，附件证书包保存本次现成原始证据及运行日志。

来源 R384 Git commit 3cac53a3d4676e7ab0d54869d9537a971c8b091c；本轮固定 GLOBAL_KNOWLEDGE_V1 main@487467135ddd23b9886f382877e2836dd6ab4c1a、EM main@8e7fff08126ca1224c1f28a63d9f8e72e733a8c0。仅辅助带符号 BRC 组合模型；P000/ACTIVE 不变。研究 Gateway research_authority_granted=false、owner inventory CONTROL_QUOTA，未获取正式 owner/CLAIM/Source Result/Driver 许可；Research Activity REGISTER_PENDING，NOT_ADMITTED。

下一精确问题：证明或反驳 H_r(u) 的 all-r Sheffer 生成函数，进而检查 θ=15/8 半次数规律；或者独立完成第十六余阶33项有限 PF₂ 参数相图。此前全量 θ=15/8 半次数只是 r≤16 观察，不得视为已证。
