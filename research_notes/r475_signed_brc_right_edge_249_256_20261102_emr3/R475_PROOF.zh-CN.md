# R475｜signed BRC 辅助标量右缘 s=249–256：无限整数 k 正性证书

日期：2026-11-02。状态：AUTHOR_SIDE_EXACT / DRIVER_UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。本成果讨论 signed BRC 辅助标量 Toeplitz 矩阵；P000、ACTIVE 世界观、X6 原生动力学均未修改。

## 来源与命题

科学输入冻结于 R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f；冻结 R462 E/O/R 内核 Git blob 7c641c985b8c48ef3fb2ddcb2142e38ca0a4ccff，R468 精确整数运算内核 Git blob 9057a6c46814a06cea45bffc20fe6f44f370b0bb。本轮实际运行从已保存 R471 证据包取得源码并复核两个 Git blob；随后通过 GitHub 读取对应 blob。行为规范当前读取 GLOBAL_KNOWLEDGE_V1 main@e0e8ce5065badbb3d8842d5a7d436d579dadeabb、Enterprise Math main@e2b468654670e1456dcc96607a4090289687b80b；规范快照与科学冻结 commit 分离。

对正整数 k，r=2k+1，2≤s≤r，定义
\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s}.
\]
令 a_j=H(r,r-j)（0≤j≤r−2），越界均为0；令
\[
D_{2,j}=a_j^2-a_{j-1}a_{j+1},\quad
D_{3,j}=\det(a_{j+v-i})_{0\le i,v\le2}.
\]
**R475 精确整数多项式证书定理：** 对每个固定 s=249,…,256，全部整数 k≥k₀=⌊(s+2)/2⌋，取 j=r−s，有 D₂,j>0 与 D₃,j>0。

## 证明：有限多项式系数证书覆盖无限 k

取 u=k−k₀≥0，C_k=\binom{2k}{k}/(k+1)>0，F=(2s+4)!，按冻结 signed BRC E/O/R 恒等式构造
\[
Q_t(u)=F\,H(2k+1,t)/C_k\in\mathbb Z[u],\qquad t=s-2,\ldots,s+2.
\]
记 A=Q_s,B=Q_{s-1},C=Q_{s+1},D=Q_{s-2},E=Q_{s+2}，则
\[
P_2=A^2-BC,\quad P_3=A^3-2ABC+DC^2+B^2E-DAE.
\]
本轮对八个 s 全部展开 P₂、P₃，次数依次为 4s 和 6s；**16个多项式共20,216个整数系数全部严格正**。每个 s 又完整验证
\[
AP_3=P_2^2-(B^2-DA)(C^2-AE)
\]
这一 Desnanot–Jacobi 整式恒等式，共8次；在 k=k₀、k₀+1 和 t=s−2,…,s+2，完成80次原始 signed 卷积等式与80次正 Catalan 表达式交叉核验。所有符号使用 Python/GMP 任意精度整数，无浮点误差。精确系数流 SHA256、逐参数次数、数量见 R475_EVIDENCE.json；复现见 R475_CERTIFY.py 及冻结内核。
由于 u≥0 且所有 P₂/P₃ 系数严格正，
\[
D_{2,j}=(C_k/F)^2P_2(u)>0,\qquad D_{3,j}=(C_k/F)^3P_3(u)>0.
\]
因此每个固定 s 的证书覆盖无限多个合法 k，命题得证。

## 固定 r 独立整行整数核验与条件性 PF₃

对 r=273,275,277,279，取
\[
a_{r-s}=\binom{r+s}{2s}\sum_{0\le q\le \min(k,\lfloor(s-1)/2\rfloor)}\binom{s-1}{2q}4^q C_{k-q},\quad k=(r-1)/2.
\]
逐行对全部 j=0,…,r−2（含越界补零），精确得到 a_j>0、D₂,j>0、D₃,j>0。每类分别为1,100项，合计**3,300项正性检查**。再完成32项原始 signed 卷积、32项交替 Catalan 公式核对。两份不同整行源码的系数流 SHA256 完全一致，数值为 f71e9a60e63221f38f489dda8382b21dcb4d87b58039b17f61cb063650cbfd43；二/三阶交错流 SHA256 完全一致，数值为 9bad7abf24a40694968985006f81a21de7663c720911bc35e51b4ba8d18ce13a。见 R475_ROW_VERIFY.py、R475_INDEPENDENT_ROW.py 与本次机器证据。

沿用已发布 R447 左缘、R472 右缘、R441-A/R473/R474 作者侧矩阵充分判据，**条件性**将 signed BRC 辅助标量半无限 Toeplitz 矩阵的 PF₃ 拼接延至全部奇数 99≤r≤279。对新增四行，其局部正性已经独立整行整数核验；完整 PF₃ 推论的承重 Schur/LR 归约和前序拼接仍须独立数学审阅。signed 标量不直接推得原生 X6 观察保真。

## 实际复现、边界和下一问题

将 R475_CERTIFY.py、R475_ROW_VERIFY.py、R475_INDEPENDENT_ROW.py 与冻结的 R462_VERIFY_FROZEN_KERNEL.py、R468_EXACT_KERNEL.py 放在同目录；需要时编译 R468_GMP_ACCELERATOR.c 加速。按 s 分开运行 python R475_CERTIFY.py 249 249（替换为249至256的每个整数），以及 python R475_ROW_VERIFY.py、python R475_INDEPENDENT_ROW.py。八份单独 JSON、原始/汇总日志、验证脚本、SHA256 清单保存在本轮研究 ZIP 证据包；R475_EVIDENCE.json 保存核心复现摘要。

本轮 GitHub 实际认证用户 awdawmip、仓库 push=true。原生 em_session_start 返回 STATIC_READONLY_SCOPE_DENIED，operation_sent=false；活跃 Owner 查询返回 CONTROL_QUOTA，故没有正式 CLAIM/Result/Driver 接纳。下一研究单元：s=257–264 全系数正性与 r=281–287 整行证书；并审查 R441-A 的 skew dual Jacobi–Trudi / LR 索引归约，研究 s,k 同时无界时的统一 Turán 下界。
