# R455｜signed BRC 右边缘 s=141—150 的无限参数 PF₃ 精确符号证书

日期：2026-11-01。类型：AUTHOR_SIDE_EXACT_SYMBOLIC，UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。母目标：Enterprise Math / 进取数论。执行者为本次 ChatGPT 研究对话，GitHub写入身份为 awdawmip；未取得原生服务 researcher/session/CLAIM 身份。本文件为已授权可移植数学研究交接，不是正式状态机 Result。

## 1. 不可变输入与问题

本轮核验 GLOBAL_KNOWLEDGE_V1 主干快照 \`0535430c6666f6bc032014cb0ca309e3c1ea632c\`，Enterprise Math 主干快照 \`c81693f40e81c1d640d4dd0caa54a680a93bce0a\`。P000 与 ACTIVE 世界观按原样继承。已有作者侧证明及可执行算法：R454 \`5ee2a81ccea8af95a92cae0bcbe008c04d1083f0\`，R447 \`adb2f26bee7e47f36991879f1b975a0fc7fbf3bc\`，R450 \`6d79677bda1fbce91c8b5f5af70dc830a33bd9dd\`，R452 \`8e2d954a18eb8e3e27790d92cb9052c9107d691e\`，R453 \`147f35867e406429d0c8727d6aa09c094d9a7854\`。

对奇数 \`r=2k+1\`、\`2≤s≤r\` 研究原始带符号 BRC 辅助标量

\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s}.
\]

记 \`a_s=H(2k+1,s)\`，支撑外为零，\(\Delta_s=a_s^2-a_{s-1}a_{s+1}\) 及

\[
\Theta_s=a_s^3-2a_{s-1}a_sa_{s+1}+a_{s-2}a_{s+1}^2
+a_{s-1}^2a_{s+2}-a_{s-2}a_sa_{s+2}.
\]

该标量辅助模型仍保留原始 signed 路径的精确卷积定义；正 Catalan 重排只是其**代数恒等式**，不把带符号支路误读为正质量。

## 2. R455 主定理与证书

**定理。** 对每个整数 \(\boxed{141\le s\le150}\) 和每个整数
\(k\ge k_0(s)=\lfloor(s+2)/2\rfloor\)，严格有

\[
\boxed{\Delta_s>0,\qquad\Theta_s>0.}
\]

**计算机辅助严格证明。** 复用 R452—R454 的精确恒等式。设 \(C_k=\binom{2k}{k}/(k+1)\)，\(B_t(k)=H(2k+1,t)/C_k\)，\(m=\lfloor(t-1)/2\rfloor\)，则

\[
(2t)!B_t(k)=E_t(k)O_t(k)R_t(k),
\]
\[
E_t(k)=\prod_{j=0}^{t-1}2(k+1-\lfloor t/2\rfloor+j),\quad
O_t(k)=\prod_{j=0}^{\lfloor t/2\rfloor}(2k+2j+1),
\]
\[
R_t(k)=\sum_{q=0}^{m}\binom{t-1}{2q}2^q
\prod_{h=q}^{m-1}(2k-2h-1)
\prod_{d=0}^{q-1}(k+1-d).
\]

所有空乘积取1。固定 \(s\)，令 \(u=k-k_0\ge0\)、\(F=(2(s+2))!\)，对 \(t=s-2,\ldots,s+2\) 设 \(Q_t(u)=F\,B_t(k_0+u)\in\mathbb Z[u]\)。写 \(A=Q_s,B=Q_{s-1},C=Q_{s+1},D=Q_{s-2},E=Q_{s+2}\)，则

\[
P_2=A^2-BC,\qquad
P_3=A^3-2ABC+DC^2+B^2E-DAE,
\]
\[
\Delta_s=C_k^2P_2(u)/F^2,\qquad
\Theta_s=C_k^3P_3(u)/F^3.
\]

本轮实际执行的 \`R455_VERIFY.py\` 只使用精确整数多项式加乘，按升幂展开完整检查 \(s=141,\ldots,150\) 的二十个多项式。每个 \(s\) 都严格有

\[
\deg P_2=4s,\quad \deg P_3=6s,\quad
\forall j,\ \operatorname{coeff}_{u^j}P_2>0,\ 
\operatorname{coeff}_{u^j}P_3>0.
\]

全部 **14,570 个整数系数严格大于零**，覆盖的系数数目
\(\sum_{s=141}^{150}[(4s+1)+(6s+1)]=14,570\)。由于 \(u\ge0\)、\(F>0\)、\(C_k>0\)，两个子式严格为正。此处是**固定十个 s、每个 s 的所有无限多个整数 k** 的确定性多项式系数证书，不是有限 k 取样。证毕。

每一行另检查精确的 Desnanot–Jacobi 多项式恒等式

\[
A\,P_3=P_2^2-(B^2-DA)(C^2-AE).
\]

十行均通过。对每个 s 的 \(k=k_0,k_0+1\)、每个 \(t=s-2,\ldots,s+2\)，计算原始 signed 二项卷积及独立 Catalan 正和，共100组精确整数等式核验；在 \(k=k_0\) 时还核对 \(Q_t(0)C_k=FH(2k+1,t)\)。这是代码与输入公式的交叉核验，有限点不承担无限参数判号的证明义务。

各 s 的完整有符号大整数多项式由源码确定性重建；\`R455_EVIDENCE.json\` 包含每行总系数数目、最高次数、精确字节编码散列和执行回执。散列是复验指纹，本身不取代正性检验。所有计算用 Python 任意精度整数、整数阶乘和二项式系数；没有浮点或舍入误差。曾有一个分片执行达到单次工具运行时限，只有打印完成并重新纳入最终证书的 s 行被计入本报告；后续完整分片及十行合并均已完成。

## 3. 两端拼接推论

R452、R453、R454 的独立作者侧证书覆盖 \(2\le s\le140\)。与本轮相结合，对**所有奇数 \(r\ge153\)**，右端 \(s=2,\ldots,150\) 共149个位置的 \(\Delta_s,\Theta_s\) 均严格正。此处还可逐个适用更小 r 的合法 s，判断条件总是 \(k\ge\lfloor(s+2)/2\rfloor\)。

R447 证明对所有奇数 \(r\ge99\)，\(\{0,\ldots,24\}\) 列中的连续行一至三阶 Toeplitz 子式严格正，从而对 \(a_j=H(r,r-j)\) 的相邻二、三阶判据覆盖 \(0\le j\le22\)。对任何奇数 \(99\le r\le173\)，其余合法 \(23\le j\le r-2\) 置 \(s=r-j\)，就有 \(2\le s\le150\)，且 \(k=(r-1)/2\ge\lfloor(s+2)/2\rfloor\)。因此由右端证书覆盖所有余下位置。系数 \(a_j>0\) 来自精确 Catalan 正和表达式。

引用 R450 的有限正序列 Toeplitz PF₃ 局部充分判据，得到

\[
\boxed{\forall r\in\{99,101,\ldots,173\},\quad T^{(r)}\in PF_3.}
\]

与 R454 原先拼接到 \(r=163\) 相比，本轮将**纯符号两端拼接论证**推进至 \(r=165,167,169,171,173\)。这些 r 已有 R450 的逐行完整整数证据，因此不宣称发现此前未知的 PF₃ 参数值；新增的是统一参数证书覆盖范围与另一条证明路径。

## 4. 适用边界、权限和接续

对象是 signed BRC 辅助标量 Toeplitz 矩阵；本轮不声称已获得对所有奇数 \(r\ge99\) 的整个半无限 PF₃ 定理，也没有构建通往原生 X6/进取坐标动力学的保真嵌入。P000、ACTIVE 世界观及独立数学准入均维持原版本。

GitHub 仓库写入身份 \`awdawmip\`，本轮原生定向研究上下文 \`authority_granted=false\`；一次活跃任务/owner 只读查询返回 \`CONTROL_QUOTA\`，因而当前正式 owner 未经核实。提交属于 \`AUTHOR_SIDE_EXACT_SYMBOLIC / REGISTER_PENDING / DRIVER_UNREVIEWED / NOT_ADMITTED\`，不作为 CLAIM、正式 Result 或独立数学审阅。

**下一最小研究单元**：从 \(s=151\) 继续完整系数证书，定位首个非正系数；若出现非正，则以实际整数 \(k\) 的二阶/三阶子式判断是证书局限还是负例。同时探索对全部 \(s\ge2\) 适用的 Turán 正性分解，避免无界逐行枚举。将证明、源码、完整正性检查输出和接续约束一起保存在本 PR 的可移植资料中。
