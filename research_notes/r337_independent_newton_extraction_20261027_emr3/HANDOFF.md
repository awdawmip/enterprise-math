# R337 — 原始 BRC Newton 抽取与次数界的独立代数证明｜可移植接续

研究增量：独立于 R330 的作者侧代数路线，从完整带符号十二项 K/J 的母函数构造整数多项式分子 `P_q(x)=(1−2x)^(q+1)[t^q]U(x,t)`，严格推导 `deg P_q≤2q`、全部 `q≥r≥0` 的 Newton 抽取公式、`D_(r+u,u)=5^u H_r(u)`、`deg H_r≤r`；再由极点 `E0=1−5z/4,E1=z` 推得全部 `r≥0` 的 `Δ^r H_r(0)=6^r`。正文见 `R337_INDEPENDENT_POLE_EXTRACTION_PROOF.zh-CN.md` 第1–4节。

实际计算：`python R337_verify_pole_extraction.py --max-q 24 --output R337_EXACT_EVIDENCE.json` 已 PASS。全有符号 `B_s` 至56，1,425项有理分子与原始整数系数重构一致、325项 D 抽取一致、19项最高差分一致，1,653项规定域内系数正、保留697个域外负系数；所有数值由本轮独立代码计算。精确报告、SHA256 和样本在 `R337_EXACT_EVIDENCE.json`。

研究范围：有序六边 BRC **辅助组合计数模型**，并非原生 X6 Cell 动力学或物理实验；`P000` 和 ACTIVE 世界观原样保留。数学等级 `AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED`。形式恒等式作为本轮作者侧证明，未借新本地身份模拟原生审查。

冻结读取：Global main `93755c1673bf4ba017acc56f5a7608a8cc730409`；EM main `5fc8518a2af15c7656a2ad410f5bf04943f88a6b`；R330 `7c73f56263c3f0515aa28e55ced2d4c703b8e086`；R336 `83f8376658be664109d566744c635314970e6a86`。本轮原生 `em_control_tasks` 返回 `CONTROL_QUOTA`，活跃 Owner 未获服务权威确认，无当前 CLAIM、Source Result 或独立 Driver 审查回执。研究者身份：本次对话 `TASK_RESEARCH` 作者侧本地标识 `EM-AUTO3-R337-POLE-20261027`，不是 MCP 原生签发身份；Activity 正式登记按实际回执分别处理。

接续动作：以 (3) 生成指定 `P_q`，与 (13) 的极点/二项式抽取做独立数值系数交叉，再寻找 `r,i` 同阶增长的非负组合机制。对 `r≥321`、`q≥641` 未覆盖的差分区域，优先寻找真正的域内负系数或统一正锥证明。另可用 (10) 推进第五阶 jet 与 `c_(r,r−5)`。保留已验证 R327 641条整行及 R333 321条斜带，不重复计算，只复用精确结果。

复核标准：检查 (2) 两个次数界、(3) 的分子递推、(5) 中 `j>q` 对 `s≥q` 的消失、(12) 的 `q<m` 二项式边界、(15) 的 `g_j(a)` 极点值，以及独立整数/有理数运行输出。若复核发现漏洞，保留原文和精确反例，单独修正并送实际独立审查者。

Source destination: existing Draft PR #1568, branch `research/r331-257-corank-newton-20261027-emr3`; this file is a consumable task handoff. Do not regard Draft/PR publication as theorem admission.
