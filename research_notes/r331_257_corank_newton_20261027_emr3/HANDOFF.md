# R331 — 接续包：BRC Newton 257 条无界正性带

研究母目标：正权有序六边 BRC 辅助组合模型的全部 Newton 差分阵列正性；P000、ACTIVE 世界观、原生 X6 空间与三维切片均不改变。继承 R330 immutable 7c73f56263c3f0515aa28e55ced2d4c703b8e086 及 R327 8332494a0aea16df27beb9828edfb41b3f234e09。账户知识冻结 main@1115410aa5e5d94c4b5ff10c5df77379ca1f5825。

本轮完成的作者侧数学单元：证明 D_{r+u,u}=5^u H_r(u)，H_r 次数<=r（继承 R330 母函数公式）；从未截断的 K/J 12项整数递推精确计算 H_r(0..r)，形成 c_{r,i}=Δ^iH_r(0)，对 r=0..256、i=0..r 共33153项全部严格正，得全部 u>=0 的无界正性和所有差分阶次正性。r=18..256 为新增239条。运行脚本 R331_VERIFY.py、证据 R331_EXACT_EVIDENCE.json、完整推导 R331_257_CORANK_NEWTON_AUTHOR_PROOF.zh-CN.md 均与本 PR 同分支。运行 SHA256 81c190fa50e22dc8479cb337a374706ae300a877fc9c74aa7a9033c49d96cf09。三角域内 s≤768 全296065项正，保留域外124191个负系数。与原 R330 有理符号母函数独立交叉至 r=18；不宣称更高 r 已第二路符号展开。

下一研究执行提示：阅读上述三份文件以及 R330 公式 (★)。优先构造 r=257 的全部258项 Δ^i H_257(0) 正性证书；请采用流式或按需 B_s 系数/差分重算，避免无故重复已验证的 r≤256 全部区间。对新 r 进行独立的 D_{q,q-r} 有穷整数抽查。任何 c_{r,i}≤0 必须分别检验：仅插值充分正锥失效、实际 D<0、原 B_s 三角域负项三者是否成立。尝试对 r~alpha q 建立统一的符号归纳或准确阈值。保留原始来源、完全计算覆盖、算术语义、所有未完成项；完成后通过有条件 GitHub 发布及原生允许路径核对。

注意：r=384 的探索曾在计算进行至 r284 后因执行时限终止，没有可复用的完整 r384 证书，不得报告其 PASS。当前 GitHub actor awdawmip admin/push，原生 em_status 0.6.11；em_control_tasks 因 CONTROL_QUOTA 未能核对活跃 Owner。先前 em_session_start 的 STATIC_READONLY_SCOPE_DENIED 未在本轮重试；无正式 CLAIM、Result、independent Driver 接纳。Research-Activity 尚待规范原生检查；不能从作者侧 PR 冒充 canonical Task/Source 发布。

验收：真实新定理或精准反例、可重算代码和整数/有理机器证据、GitHub 不可变提交与回读；不回退为逐个旧 r 重算。