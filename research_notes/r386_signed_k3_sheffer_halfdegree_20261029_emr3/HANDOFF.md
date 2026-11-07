# R386｜可直接继续的研究交接

日期：2026-10-29；角色：本次自动研究对话的作者侧便携研究（EMR3，未取得原生 session/CLAIM/Owner 批准），状态：`UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING`。

## 科学前沿（精确、不可重做）

阅读 `R386_PROOF.zh-CN.md`。从 R346 原始保号十二支路 K/J→B→D 递推证明全余阶公式 `sum_{r>=0} H_r(u;theta) s^r = A_theta(s) B_theta(s)^u`，其中 A、B 由 `G_theta(x,s)=1-K_theta(x,2s/x)` 的唯一形式根 X_theta(s) 给定；当 `theta=15/8` 时，对全部整数 r>=0 证明 `deg H_r=floor(r/2)`，对全部 r>=1 证明 `deg Q_r=r` 及 `c_r=(-1)^r binom(r,floor(r/2))*180^r`，j>r 时 c_j=0。所有奇数 r>=1 提供严格非 PF2 的负 Newton 系数反例。量词结论来自留数法，不能归因于有限计算。

## 固定输入与验证

全局固定知识读取 `awdawmip/chatgpt-global-knowledge main@314ff1ecb8d348f87f9d97f51570d65256705595`，EM 规范 `awdawmip/enterprise-math main@b519a46c64db7b40581b618e67a3467cc40a542f`；原始代码依赖 `research_notes/r384_universal_signed_k3_catalan_top_20261029_emr3/R384_verify.py`；源研究 R385 `46090af49a7bad8389fb387af8d18f4fd6b0ff80`。参数 `[−1/2,0,1/2,1,15/8]`，r=0..16，u=2..5，340项有理 Sheffer 等式；theta*=15/8 r=1..16 另外64项次数及尾系数断言，`R386_EXACT_PASS`。`R386_EVIDENCE.json` 包含全部逐阶结果、`R386_SUMMARY.json` 包含 SHA256。复现：`python R386_verify.py`，须从同一仓库的兄弟 R384 目录找到 `R384_verify.py`。

## 下一可执行科学问题

推导 theta*=15/8 时 Q_{2k} 的次高项及 Newton c_{2k−1}^{(2k)} 精确符号，判断是否对所有偶数 k>=1 出现 PF₂ 负系数或负 Turán。保留奇数 r 已证反例族并以它作为新判据的起点，不重复逐阶恢复 R384/R385。

## 接纳与后续流程

当前 Enterprise Math 原生服务返回 `research_authority_granted=false`、`CODE_REVIEW_REQUIRED`、活跃控制 job 5/5。不可推断活跃 owner 为本人，也不能以作者侧文献提交替代正式 Source CLAIM、Review 或 Foundation 推广。当前 GitHub PR 仅持久化可消费原件；正式登记和独立审查依现行协议由获授权真实身份完成。不要修改 P000/ACTIVE 世界观，不将 x,s,u 形式变量解释为六维原生空间量。

## 交接给下一执行者的完整任务

“使用 R386 的不可变数学证明、原始 K/J→B→D 递推及 R386_verify.py 的精确证据，从 theta*=15/8 的 A*(s),B*(s) 出发，求所有偶数 r=2k 的 c_{r−1} 或某个可统一证明负性的 Turán 缺陷。提供适用于无限 k 的代数证明，或明确指出最小反例和阻断条件。复用 R384/R385/R386 成果，不重新报告有限扫描即为无限证明；保留有符号支路 provenance。将新证明、确切有限检查范围及下一独立未解义务保存到本 PR 分支；原生接纳仍需实时 Source 授权和独立 Driver。”
