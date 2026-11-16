# R608 作者侧研究交接 · 2026-11-07

前沿：冻结 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f，接续 R607@68cf8d90d9d7647411c7eb001e734530a14d08ca。研究者身份与正式 Owner/CLAIM 未核实；原生 em_status/em_control_tasks 均 BACKEND_IDENTITY_OR_VERSION_MISMATCH(operation_sent=false)。保留作者侧数学证据，DRIVER_UNREVIEWED/NOT_ADMITTED。

本轮完成 R607 二阶观察 Q=(d,A) 与整数 Magnus 观察 M_2 的**精确等价定理**：C_i=d_i；C_ii=d_i(d_i−1)/2；C_ij=(d_i d_j+A_ij)/2，C_ji=(d_i d_j−A_ij)/2。两者互相重构，保真范围为路径拼接后读取二阶观察。

严格反例：八步 p=`abABAbaB`，q=p^−1=`bABabaBA`；长度均8，d=A=0，M_2=1，但 M_3(p)−M_3(q)=2(X_1²X_2−2X_1X_2X_1+X_2X_1²)，任意共同前后缀保持该差。构造 W_3=p，W_{n+1}=aW_n A W_n^-1，所有 n≥3 满足 M_{n−1}(W_n)=1、M_n(W_n)=1+ad_{X_1}^{n−1}(X_2)≠1；任意有限阶都可被更高阶联合观察区分。纯整数形式观察，不代表物理动力学或原生 BRC 支路已映射。

证据：R608_PROOF.zh-CN.md 完整论证；R608_VERIFY.py 标准库整数穷举22,621个长度≤4的十二字母路径、169组上下文、n=3..6 构造；R608_EVIDENCE.txt 终止标记 `R608_EXACT_MAGNUS_HIERARCHY_PASS`。完整科学输入仍以 R462 原始 K/J→B→D 为准。

下一最小问题：从 R462 冻结支路中提取原生状态、允许的更新与可复核的原生步标签映射（带符号/相位/来源）；验证两条形式路径是否出自同标量 H 的真实合法状态。若实际未来只要求二阶 Q，则已有 Q 足够；若含三阶联合读出，则须选择相应保真层。额外独立路线：BRC 全谱能量 V_k 的尾项控制。
