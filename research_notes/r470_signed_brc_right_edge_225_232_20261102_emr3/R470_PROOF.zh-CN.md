# R470｜signed BRC 辅助标量模型右缘 s=225–232：无限 k 精确正性与 PF₃ 条件拼接

日期：2026-11-02。性质：作者侧整数/符号计算证明；正式独立审阅及原生任务接纳尚待完成。

## 规范与冻结来源

现行行为规范在已验证的 GLOBAL_KNOWLEDGE_V1 main@c3c9c172fe5ca17dc1695081052f3a650e1882c4 和 Enterprise Math main@85b54b1fbceb232e2ab8f4067215b9299966064d 下读取。加载 P000、ACTIVE 世界观、current-normative-context 入口所指适用规则、portable research 和 BRC 约束。科研计算沿用冻结 R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f`，其 E/O/R 数学源码 Git blob 7c641c985b8c48ef3fb2ddcb2142e38ca0a4ccff，R468 精确乘法源码 Git blob 9057a6c46814a06cea45bffc20fe6f44f370b0bb。两份本地实际执行源码已通过 Git blob 哈希与所述发布版本核对。

研究对象仅为 signed BRC 辅助标量模型；数学定义保留签名信息与来源，不对原生 X6 动力学或物理残差作推断。P000、ACTIVE 世界观保持不变。

## 定义与本轮命题

令 k≥1 为整数、r=2k+1 为奇数、2≤s≤r，定义

\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},
\qquad C_k=\frac1{k+1}\binom{2k}{k}>0.
\]

对固定 r 置 a_j=H(r,r-j)（0≤j≤r−2），其余位置 a_j=0；并令

\[
D_{2,j}=a_j^2-a_{j-1}a_{j+1},\qquad
D_{3,j}=\det(a_{j+v-i})_{0\le i,v\le2}.
\]

**定理 R470（八个独立的全 k 参数族）**：逐个固定整数 s=225,…,232；对于所有整数 k≥k₀=⌊(s+2)/2⌋，记 r=2k+1、j=r−s，则 D₂,j>0 且 D₃,j>0。

## 整数多项式严格正系数证书

固定上述 s，令 u=k−k₀≥0、F=(2s+4)!。借助冻结 R462 E/O/R 精确恒等式，构造 t=s−2,…,s+2 的整数多项式

\[
Q_t(u)=F\,H(2k+1,t)/C_k\in\mathbb Z[u].
\]

记 A=Q_s、B=Q_(s−1)、C=Q_(s+1)、D=Q_(s−2)、E=Q_(s+2)；直接展开相邻子式：

\[
P_2=A^2-BC,\qquad
P_3=A^3-2ABC+DC^2+B^2E-DAE.
\]

因 C_k,F 严格正且系数恒等式精确成立，

\[
D_{2,j}=(C_k/F)^2P_2(u),\qquad
D_{3,j}=(C_k/F)^3P_3(u).
\]

针对每一个 s，实际使用任意精度整数算术，完整生成、逐项检查 deg P₂=4s、deg P₃=6s，且 **P₂ 与 P₃ 的所有系数严格为正整数**。每个 s 覆盖 (4s+1)+(6s+1)=10s+2 个系数；八参数累计 **18,296 个严格正系数**。完整多项式恒等式

\[
A P_3=P_2^2-(B^2-DA)(C^2-AE)
\]

对八个 s 分别精确检查通过；另在每个 s 的 k=k₀、k₀+1，以及 t=s−2,…,s+2 上，完成 80 项原始 signed BRC 卷积与 80 项 Catalan 公式交叉核验。

对任意 P(u)=∑p_i u^i 且每项 p_i>0，有 P(u)≥p₀>0（u≥0）。结合上述精确比例关系，定理对八个指定 s 各自的所有合法 k 均成立。全系数数据的确定性 SHA256 编码在冻结 R462 的 s_certificate() 中给出；八份独立哈希、次数和检查结果位于 R470_EVIDENCE.json 及逐参数证据文件。此为有限完整整数计算支持的无穷 k 参数证明。

## 新增整行 r=249、251、253、255

独立采用正 Catalan 恒等式构造每个固定 r 的完整系数行：

\[
a_{r-s}=\binom{r+s}{2s}
\sum_{q=0}^{\min((r-1)/2,\lfloor(s-1)/2\rfloor)}
\binom{s-1}{2q}4^q C_{(r-1)/2-q},\quad 2\le s\le r.
\]

两份不同程序独立检验全部 j=0,…,r−2，零填充边界一并纳入；每类 a_j、D₂,j、D₃,j 各有 248+250+252+254=1,004 个严格正值，总计 **3,012 项精确整数正性**，均通过。另对每行 8 个 s 检查原始 signed 卷积和交替 Catalan 表达式，分别 32 项、32 项。两份程序的系数流和子式流 SHA256 逐一相同，见两份 R470_ROW 证据文件。该整行核验独立于上述全系数证书方法。

## 条件性 PF₃ 拼接与承重依赖

原有作者侧右缘证书覆盖 2≤s≤224；本轮延伸至 232。既有左缘证书覆盖 j≤22。故当奇数 r≤255 时，j≥23 导致 s=r−j≤232，左、右缘覆盖全部相关位置。

在 R447 左缘、R450 局部相邻二/三阶子式正性推导半无限 Toeplitz PF₃ 的充分判据和此前拼接引理均成立的前提下，推出 **T^(r)∈PF₃，r=99,101,…,255**。较 R469 新增 r=249、251、253、255；四个新增 r 的整行相邻子式正性还有本轮独立整数证据。上述拼接依赖旧承重引理，独立审查尚未完成；固定 s 的全 k 子式正性具有本轮完整整式证书。

## 复现与后续问题

完整源码、汇总和逐参数机器证据置于当前目录，依赖同仓库已发布的 R468 目录内 R468_EXACT_KERNEL.py 和冻结 R462_VERIFY_FROZEN_KERNEL.py：

- 逐一运行 python R470_CERTIFY.py 225，…，python R470_CERTIFY.py 232；
- 运行 python R470_ROW_VERIFY.py、python R470_INDEPENDENT_ROW.py；
- 如不使用 GMP 动态加速库，R468_EXACT_KERNEL.py 可回退 Python 任意精度整数，数学输出不变。

真实权限：GitHub 连接身份 awdawmip 具备项目仓库写入权限；原生 em_session_start 返回 STATIC_READONLY_SCOPE_DENIED (operation_sent=false)，em_control_tasks 返回 CONTROL_QUOTA。活跃 Owner 尚无法核实，无新 CLAIM/Result/Driver 接纳。

下一问题：检查 s=233–240 的全系数证书，拟检验至 r=263；优先独立审查 R450 局部充分判据，并寻找 s 与 k 同时无界时的 Turán 正性统一证明。若下一组出现非正系数，须检查真实合法整数子式，分清系数法边界与实际反例。
