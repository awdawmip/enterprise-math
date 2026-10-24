# R277 研究接续｜清洁重置完整效果的精确支撑及边界系数

研究时间：2026-10-25，活动 ID RA-EMR3-20261025-0720-R277RESET。本地研究身份 EMR3-20261025-0720-LOCAL；原生 Source session、正式 CLAIM、独立 Driver 数学审查均未取得。

## 固定数学输入与已完成科学结果

来源 R276 作者侧定理（原始证据提交 ab39a2962c39f99c69fee8a04d555fd93f5697d7）。六条二进制正权 BRC 边、初态 q0/epsilon+1/k0，右复合 (epsilon,k)⋆(eta,b)=(eta epsilon,eta k+b)。clean 是未出现 00，P_n(epsilon,k) 保留所有原始有序词及正整数路径数。

新的无穷解析结论：对全部 n>=9，
supp P_n = {(epsilon,k): epsilon=+1 or -1; k=-n+2,-n+4,...,n-8}，总支撑 2(n-4)，n=9 最优。任何合格 k 两个 epsilon 符号都可达，并不蕴含路径计数相同。证明方法是原始来源的唯一首返分解为 W_(sigma,a)=x_sigma 1^(a-1)01，各个原子有序效果 (sigma,-a)、长度 a+2，sigma=- 时 a>=2；变换 t=epsilon k 后得到 t=−Σ E_i a_i。这是可逆精细化，不删除来源。

边界精确计数：r=1,2,3 正号 P_n(+,-n+2r)=C(n-2r-1,r-1), n>=3r；r=1,2 负号 P_n(-,-n+2r)=C(n-2r-2,r-1), n>=3r+1。首次非平凡补项 P_n(-,-n+6)=C(n-8,2)+1 (n>=10)，P_n(+,-n+8)=C(n-9,3)+1 (n>=12)。因此 Lambda_n>=ceil(a_n/[2(n-4)]) (n>=9)。

## 实际核验 / 证据位置

论文：R277_CLEAN_RESET_EXACT_SUPPORT_AUTHOR_PROOF.zh-CN.md，包含完整两个定理、必要性证明、每个格点显式原始来源构造、最优阈值、边缘计数证明。

执行程序：R277_verify_reset_support.py，标准库 Python，实际执行 PASS。原始二字来源词 n=0..15 共 65535 条；全六边 DFA n=0..200；独立首返 renewal DP n=0..75 对 5113 个非零效果系数一致；n=9..200 全支撑 38592 项；n=9..120 验证 13552 条明确构造见证；边缘计数 1340 项。机器结果：EXACT_EVIDENCE.json，整数大值均以十进制字符串保存。

有限证据仅核验原始边、首返分解和公式，不从实验深度外推无穷定理。未执行 enterprise_math 原版包、Lean、R193 原生端口或 P000 心跳世界六维 Cell 动力学。上述定理只适用于形式正权 BRC 辅助模型，不是 X6 物理定理，也不更改 P000 或 ACTIVE 世界观。

## 权限及下一精确科学问题

原生 em_control_tasks 返回 CONTROL_QUOTA；em_session_start 返回 STATIC_READONLY_SCOPE_DENIED, operation_sent=false。因此当前活跃 Owner 未权威核实、没有原生 CLAIM、正式 Result 或独立 Driver 接纳。GitHub 保存只是作者侧 Source 持久化，研究活动登记不授予 Task authority。

已存在且不重复：R274 对 clean q1 全效果支配；R275 对 clean q2 在 n>=12 的全效果支配；R276 对 dirty 的全效果支配存在无穷反例；R273 作者侧存在性证明：B_n=Lambda_n 对充分大 n 成立但尚无有效整数阈值 N。

**下一单元**：利用精确支撑及 near-edge 系数，研究 S_n=argmax_g P_n(g) 的内域峰值位置，只在至少一个 peak g 上证明 D_n^(0),(1),(2)(g)>=Lambda_n 对全部 n>=显式 N 成立；或找到严格反例，不能将 R276 已否定的 dirty 全效果支配当作目标。

方法复用：BRC ordered affine REUSE_APPLIED；R276 original transition semantics REUSE_EXECUTED（标准库整数复现）；unique first return is information-preserving decomposition. 本次不是已完成的 P000 原生物理验证。

固定读取：GLOBAL_KNOWLEDGE_V1 main@0b9f640eba076809bd952eb2b74de0bb401d1fdb / 原 P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc；Enterprise Math control main@8c3ff79a69c137d3fc4f8eb22ae63f8cb3c9d417。
