# R465｜signed BRC 辅助标量：s=185–192 无限参数正性与 r=215 条件性 PF₃ 拼接

研究日期：2026-11-02。作者侧精确整数／符号研究；尚待独立 Driver 审查和正式任务登记。

## 来源与对象

当前规范快照：GLOBAL_KNOWLEDGE_V1 main@6fe5152374ea27cc2a7247434dfcbd5495c25d8a；Enterprise Math main@9a1ea3ab71469ff6a4f645852d1be9f33b09fdc9。科学冻结输入继承 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f；接续已核实 R464@d22650f431aa516feba34f32516fe0e89eb0f597。P000、ACTIVE 世界观未修改。GitHub 认证身份 awdawmip，原生身份启动因 STATIC_READONLY_SCOPE_DENIED 拒绝，owner 清单 CONTROL_QUOTA；故本材料不表示正式 CLAIM/Result/Review。

固定奇数 r=2k+1，2≤s≤r，定义
$$H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s}.$$
置 $a_j=H(r,r-j)$（$0\le j\le r-2$），越界补零。定义
$$D_{2,j}=a_j^2-a_{j-1}a_{j+1},\qquad D_{3,j}=\det(a_{j+v-i})_{i,v=0}^{2}.$$

## R465-A：八个新的无限参数正性证书

**精确计算机辅助命题。** 对每个整数 $185\le s\le192$，及每个整数 $k\ge\lfloor(s+2)/2\rfloor$，令 $r=2k+1,j=r-s$，则
$$D_{2,j}>0,\qquad D_{3,j}>0.$$

证明沿用冻结 R452/R463 的精确 E/O/R 分解。设 $C_k=\binom{2k}{k}/(k+1)$，$B_t(k)=H(2k+1,t)/C_k$。冻结的恒等式为
$$(2t)!\,B_t(k)=E_t O_t R_t,$$
其中
$$E_t=\prod_{v=0}^{t-1}2(k+1-\lfloor t/2\rfloor+v),\quad O_t=\prod_{v=0}^{\lfloor t/2\rfloor}(2k+2v+1),$$
$$R_t=\sum_{q=0}^{\lfloor(t-1)/2\rfloor}\binom{t-1}{2q}2^q
\prod_{v=q}^{\lfloor(t-1)/2\rfloor-1}(2k-2v-1)
\prod_{d=0}^{q-1}(k+1-d).$$
对固定 s，置 $k_0=\lfloor(s+2)/2\rfloor$、$u=k-k_0\ge0$、$F=(2s+4)!$，定义 $Q_t(u)=F B_t(k_0+u)\in\mathbb Z[u]$（$t=s-2,\dots,s+2$）。令 $A=Q_s,B=Q_{s-1},C=Q_{s+1},D=Q_{s-2},E=Q_{s+2}$，则
$$P_2=A^2-BC,\qquad P_3=A^3-2ABC+DC^2+B^2E-DAE.$$
从而 $D_{2,j}=C_k^2P_2/F^2$、$D_{3,j}=C_k^3P_3/F^3$。本轮对每个 s 完整构造 $P_2$ 的 $4s+1$ 项和 $P_3$ 的 $6s+1$ 项整数系数，所有系数均严格正。由 $u\ge0,F>0,C_k>0$，命题成立；对固定 s 的合法 k 为无限集。

所有八个 s 分别完成整多项式 Desnanot–Jacobi 恒等式检查
$$A P_3=P_2^2-(B^2-DA)(C^2-AE),$$
并在 $k=k_0,k_0+1$ 的五个相邻 t 对原始 signed 卷积和正 Catalan 表达式各核对 10 项／s。统计：16 个多项式、15,096 个严格正系数、8 项完整多项式恒等式、80 项 signed raw 和 80 项 Catalan 交叉等式。s=185..192 的完整系数流 SHA256 见 R465_EVIDENCE.json。计算采用 Python 任意精度整数，所有判号均无浮点误差。两个跨 s 批处理在输出部分完整成功记录后中断；所有八个 s 的单独证书记录现已齐全，不将被中断的批处理视为成功。

## R465-B：条件性半无限 PF₃ 拼接

依已发布作者侧 R447 的左边缘 $0\le j\le22$、此前 R452–R464 的 $2\le s\le184$ 右边缘与 R465-A 的 $s\le192$，对奇数 $99\le r\le215$，当 $j\ge23$ 时有 $s=r-j\le192$，两端覆盖全部合法 j。调用先前 R450 的局部充分判据（该判据及依赖尚待独立审查），得到条件性结论
$$T^{(r)}\in PF_3\quad(r=99,101,\ldots,215).$$
本轮新增 $r=209,211,213,215$。独立按 Catalan 整数式复算这四个 r，各 844 个正系数／二阶相邻子式／三阶相邻子式，共 2532 项严格正整数判号；另对 32 项原始 signed 卷积和 32 项交替 Catalan 式交叉核验。R465_ROW_VERIFY.py 为本轮实际执行源码，R465_ROW_EVIDENCE 摘要收入 R465_EVIDENCE.json。该整行结果的半无限 PF₃ 推论仍依赖 R450。

## 复现、边界及下一问题

无限参数证书可复用已发布 R464_REPRODUCE.py 的整数 Kronecker 乘法与 R463 E/O/R 核心，在完整仓库检出下运行 R465_VERIFY.py；同一数学内核的冻结 R462 版本已在本轮实际计算并通过 s=175 的 R463 证书 SHA256 回归。整行验证运行 python R465_ROW_VERIFY.py。两种计算均仅用整数；材料包括完整输入、证书摘要、验证源码与校验哈希。

结论限于 signed BRC 辅助标量模型；从 R447/R450 作者侧判据到全 PF₃ 为条件性拼接，亦不直接证明原生 X6 动力学。下一研究单元为 $s=193,\ldots,200$ 的可区分系数/负例测试，以及探索 $s,k$ 同时无界时不依赖逐个 s 枚举的统一 Turán 下界；若出现非正多项式系数，应先在合法整数 k 验证实际行列式符号，区分证书失败与数学反例。
