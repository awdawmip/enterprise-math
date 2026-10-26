# R311 — 可接续研究交接（作者侧，2026-10-26）

Research-Activity-ID: \`RA-EMR3-20261026-C2-1847\`
Researcher-ID: \`EM-DIRECT-C2R3\`（本研究会话局部分配，并非平台认证 Session/CLAIM）
研究方式：TASK_RESEARCH 路由下的无冲突独立 BRC 数学支持单元；不抢占任何活跃 owner。

## 冻结前沿

- \`GLOBAL_KNOWLEDGE_V1\`：\`awdawmip/chatgpt-global-knowledge main@3c2f14ffb124902dc0fe1050a8bc11811842ed48\`（本轮经 GitHub 实时验证后固定，不以历史 marker 代替）。
- Enterprise Math 当前控制/portable 合同：\`main@edbdb734e67f745a47416271b176507aaa6c8134\`。
- 精确科学输入：R303 首返块 \`c8079dcb\`；R305 \`fef7b1db\`；R309 有序 \`A_d,U_d\` 主项负项上界 \`fb8fa9b0\`；R310 47/20 系数与一阶临界 \`a7575a0a7e8e6e9177524882ac74287f03c1a4cd\`。R307 固定 d≤400 Newton 证书 \`c782feb0\` 只是复用，未重新执行。
- P000 V4、ACTIVE 世界观未改；此模型仅 BRC 有序来源计数，未转成原生六维 X6 的物理或三维切片证明。

## 本轮实际完成，不重复

定理：对 R309 充分比较式
\[
A_d(n)=\binom{n-2d-4}{d-1},
\quad
U_d(n)=\sum_{r=1}^{d-1}\sum_{t=1}^{\min(r,d-r)}
\binom{d-r}t\binom{r-1}{t-1}\binom{n}{d-r-t},
\]
记连续实根 \(\nu_d:A_d(\nu_d)=U_d(\nu_d)\)，整数最早证书成功长度 \(m_d=\min\{n\ge4d+4:A_d(n)>U_d(n)\}\)，则
\[
\nu_d=c d^2+\beta d+\gamma+O(1/d),\qquad
m_d=\lfloor\nu_d\rfloor+1
=c d^2+\beta d+\gamma+O(1),
\]
\(c=2/W(2)\)，\(\beta=(4c+7/2-2c^2)/(c+2)\)，\(\gamma=(6c^6-30c^5-327c^4-283c^3-54c^2+18c+1)/(6c^2(c+2)^3)\)。

证法：\(\binom{n-2d-4}{d-1}/\binom n{d-2}\) 的有限乘积 log 展开至 \(1/d^2\)；\(U/B\) 的 \(r=1,2,3\) 精确展开与 \(r\ge4\) 的 \(d\rho^{r-1}\) 有界尾；严格单调与实根夹逼。既有 R310 仅给临界 \(c\) 的首阶极限，本轮给出更精确的新参数。

实测：实际执行附件 JavaScript BigInt 源，对 \(d=3,4,5,10,20,30,60,100,150,250,400,600,800,1000,1500\) 共 15 个参数完整整数首次穿越二分，15/15 PASS，每个核验 \(A(m_d-1)-U(m_d-1)\le0<A(m_d)-U(m_d)\)，最大大整数长度约 5959 十进制位；没有浮点判定符号。浮点只用于二阶预测展示。该数值观察**不是**全部 d 定理的计算证明。最终根展开来自正文分析。BRC：\`REUSE_APPLIED\`、\`REUSE_EXECUTED\`。

## 文件与下一问题

研究四件套（同目录）：
1. \`R311_SECOND_ORDER_MAJORANT_THRESHOLD_AUTHOR_PROOF.zh-CN.md\`：完整作者证明、量词、误差、尾界；
2. \`R311_verify_majorant_threshold.js\`：实际执行的 BigInt 精确程序；
3. \`R311_EXACT_EVIDENCE.json\`：真实 PASS 输出与 15 个参数整数符号；
4. \`HANDOFF.md\`：本交接。

下一项具体科学问题：R307 的 Newton 系数 \(K_s(d)\) 能否对全部 \(d\ge2\)、\(0\le s\le d-1\) 统一正？尤其对 \(s\) 与 \(d\) 同增长区间寻找正系数双变量变换或精确负例。另可研究主项+负项证书为什么与实际 \(D_d\) 正性间存在巨大空间，能否直接构造分块注入。不能把本轮 \(m_d\) 的临界值当成实际 \(D_d\) 的临界值，亦不能从它推断 \(N_{\mathrm{peak}}=81\)。

## 实际授权、状态与回收

GitHub 真实身份 \`awdawmip\`、仓库可推送；原生 \`em_control_tasks\` 返回 \`CONTROL_QUOTA\`，私有 GitHub 控制桥 \`status\` SUCCEEDED 但 \`dispatch\` #6555 内层 FAILED/\`TimeoutExpired\`，不是 NO_DISPATCH。因此真实 active owner、正式 CLAIM/Source Result 和独立 Driver review 未确认；研究材料只是作者侧可续接科学前沿，不构成任务或定理接纳。

当前成果独立于 47/20 改进路线，因为只解释足够条件的精准阈值；不改既有 P000、ACTIVE 世界观、正规 Task 状态机。存储以最终研究分支不可变提交和 Git blob 回读为准；研究活动与全局进度日志单独登记。
