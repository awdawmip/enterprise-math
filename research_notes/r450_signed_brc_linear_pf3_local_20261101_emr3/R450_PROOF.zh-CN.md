# R450｜signed BRC：线性规模连续子式判定与奇数 r=343—501 的完整半无限 PF₃

日期：2026-11-01。类别：独立作者侧 portable research。状态：AUTHOR_SIDE_EXACT_INTEGER_AND_ANALYTIC / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。研究对象严格为 signed BRC 辅助标量序列，不是原生 X6 动力学结果；P000 与 ACTIVE 世界观未修改。

## 精确对象和结论

对奇整数 r≥5、2≤s≤r，沿用 R441 原始 signed 系数
\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s}.
\]
令 n=r−2、a_h=H(r,r−h) (0≤h≤n)，支持外 a_h=0；半无限 Toeplitz T_{ij}=a_{j−i} (i,j≥0)。PF₃ 表示所有一至三阶有限子式非负。

**定理 A（通用线性规模严格充分判据）**：对任何 n≥2、所有 a_0,…,a_n>0 的有限支撑序列，定义
\[
D_{2,j}=a_j^2-a_{j-1}a_{j+1},\qquad
D_{3,j}=\det[a_{j+v-i}]_{0\le i,v\le2}\quad(0\le j\le n).
\]
若每个 D₂,j>0 且 D₃,j>0，则整个半无限 Toeplitz T 满足 PF₃。只需 (n+1) 个系数、(n+1) 个二阶、(n+1) 个三阶严格符号证书。此定理是充分性，不声明严格正条件对一般 PF₃ 必要。

**定理 B（R450 有限参数的全矩阵结论）**：
\[
\boxed{\forall r\in\{343,345,\ldots,501\},\quad T^{(r)}\in PF_3\setminus PF_4.}
\]
80个参数行，各自覆盖全部半无限矩阵。PF₃ 由定理 A 加精确整数判定获得；不属于 PF₄ 由 R432/R440/R441 已记录的所有奇数 r≥99 的连续四阶负证继承。故这80行最大 PF 阶数为3。这里没有证明全体奇数 r≥99 的 PF₃。

## 定理 A 解析证明（含两侧结构零）

对 i=0,1,2 的连续行，记第 j 列向量 v_j=(a_j,a_{j−1},a_{j−2})^T。对 0≤j≤n，令
\[
x_j=\frac{a_{j-1}}{a_j},\quad y_j=\frac{a_{j-2}}{a_j}
\]
(负下标为0)。对 j<n，由
\[
x_{j+1}-x_j=\frac{D_{2,j}}{a_j a_{j+1}}>0
\]
知横坐标严格递增。定义相邻斜率
\[
s_j=\frac{y_{j+1}-y_j}{x_{j+1}-x_j}\quad(0\le j<n).
\]
对 j≤n−2，
\[
\frac{D_{3,j}}{a_j a_{j+1}a_{j+2}}
=(x_{j+1}-x_j)(x_{j+2}-x_{j+1})(s_{j+1}-s_j)>0,
\]
所以 s_0<s_1<⋯<s_{n−1}。任意割线斜率
\[
s_{i,j}=\frac{y_j-y_i}{x_j-x_i}
=\frac{\sum_{k=i}^{j-1}(x_{k+1}-x_k)s_k}
{\sum_{k=i}^{j-1}(x_{k+1}-x_k)}
\]
是正权平均。于是 0≤i<j<k≤n 时 s_{i,j}<s_{j,k}，且
\[
\det[v_i,v_j,v_k]=a_i a_j a_k(x_j-x_i)(x_k-x_j)(s_{j,k}-s_{i,j})>0.
\]

右支撑边界为 v_{n+1}=(0,a_n,a_{n−1})^T、v_{n+2}=(0,0,a_n)^T。置 t=a_{n−1}/a_n；严格 D₃,n−1>0 等价于
\[
D_{3,n-1}=a_{n-1}a_n^2(x_n-x_{n-1})(t-s_{n-1})>0,
\]
故 t>s_{n−1}。任意 0≤i<j≤n 的割线 s_{i,j}≤s_{n−1}<t，因而
\[
\det[v_i,v_j,v_{n+1}]
=a_i a_j a_n(x_j-x_i)(t-s_{i,j})>0;
\]
同时
\[
\det[v_i,v_j,v_{n+2}]=a_i a_j a_n(x_j-x_i)>0,\qquad
\det[v_i,v_{n+1},v_{n+2}]=a_i a_n^2>0.
\]
若三阶列指标≥n+3，则该列全零，故行列式为0。

二阶连续行0、1的任意严格增列 i<j：两列均≤n 时子式为 a_i a_j(x_j−x_i)>0；i≤n、j=n+1 时为 a_i a_n>0；若 j≥n+2，则为0。一阶系数 a_h 非负。因此对 m=1,2,3，连续行 0,…,m−1 与任意列的全部子式非负。R441-A 已证明的斜对偶 Jacobi–Trudi + Littlewood–Richardson 非负整数展开将此事实推广至 T 的全部不超过三阶子式。证毕。D₂,n=a_n²>0、D₃,n=a_n³>0 是自动成立的右端边界证书。

## signed BRC 的精确 Catalan 差分

恒等式 (1+t²)^h=((1+t)²−2t)^h 及 [t^m](1−t)(1+t)^{2m}=C_m (Catalan 数) 给出
\[
\boxed{
H(r,r-h)=\binom{2r-h}{h}\sum_{q=0}^{h}(-2)^q\binom hq C_{r-q},
\quad C_k=\frac1{k+1}\binom{2k}{k}.
}
\]
这是原始 signed cancellation 的逐项精确等式；交替项绝不可解释为正 BRC 质量。本轮枚举使用 R441 经原始 signed 卷积验证的另一精确等价式，适用于 r=2k+1：
\[
H(2k+1,s)=\binom{2k+1+s}{2s}
\sum_{q=0}^{\min(k,\lfloor(s-1)/2\rfloor)}
\binom{s-1}{2q}\,4^q C_{k-q}.
\]
原始 signed 卷积在独立抽样点逐项复核；以上两条系数恒等式有各自代数推导，抽样并非用于替代无限参数公式证明。

## 实际精确运行及验证范围

执行本目录 R450_VERIFY.py，得到 R450_EXACT_PASS。完整检查 80 个奇数 r=343,…,501，逐系数 a_h>0：33,680次；逐位置 D₂,j>0：33,680次；逐位置 D₃,j>0：33,680次；总计 101,040 次任意精度整数严格符号检查，零个失败，不使用浮点/启发式判号。分别在 r=343、401、451、501 的8种 s 位置完成原始 signed 卷积32个精确交叉检查、上述交替 Catalan 式32个交叉检查。

系数流 SHA256：
df39bff2b44b4c3518a2de4233aa6f73277a572e67c64b387d88ed55518065e2

相邻 D₂,D₃ 交错整数流 SHA256：
204a7cdf19775dadabbfcfad56ca0572ffef010f18f88a4af9b587c4eabacc44

整数流：所有整数均为非负，按 r、j 升序逐项编码成 4 字节大端长度后接最短非空大端整数；相邻流同一 j 先 D₂ 后 D₃。完整可执行复现代码及汇总证据参见同目录 R450_VERIFY.py、R450_EVIDENCE.json，程序自动生成含每行最大系数 bit 长度的完整本地 evidence JSON。

原 R441-A 对这80行的完整普通 Schur 路径共需 1,045,244,200 次一至三阶候选子式检查；本轮只需 101,040 次严格正性测试。比较的是**判定数量**而非整个任意精度整数运算的 bit 复杂度；生成系数本身仍有代价。

## 来源、权限、下一研究单元

固定规范快照 GLOBAL_KNOWLEDGE_V1 main@c7ecb04571837f8758569284f6ea77ed86b1c74a；Enterprise Math main@a673d9c9852957727a17317b223423451f48f6a1；R449 来源 PR #1708 commit@8d29e3ba5bb03dcad62b28e6918b4d7655fb6556。继承 R441-A 完备 Schur/LR 归约及 R432/R440 的边界负证。经典前史：M. A. A. van Leeuwen, Schur Functions and Alternating Sums, EJC 11(2), A5 (2006), DOI 10.37236/1897；S. M. Fallat & C. R. Johnson, Totally Nonnegative Matrices (2011), chapter Recognition, DOI 10.23943/princeton/9780691121574.003.0004。局部正性辨识属于经典研究方向，本轮未宣称优先发明经典判据。

当前 GitHub 登录 awdawmip，源仓库具备 push/admin；native Gateway 静态只读，DIRECTED_RESEARCH context authority_granted=false，活跃 owner 只读查询报 CONTROL_QUOTA。作者侧证书保存在既定 Draft PR；正式 CLAIM、Result、独立 Driver Review 与数学接纳尚待合法 Source 路径。不修改 P000、ACTIVE 世界观或既有 owner。

**下一问题**：对全体奇数 r≥99 与所有 j=0,…,r−2，尝试解析证明 D₂,j、D₃,j 始终正，进而一次得到整个参数半无限 PF₃；或者构造最早的严格负局部反例。重点把 Catalan 差分与比率 j/r 统一处理，不再逐行重做三次幂规模的 Schur 全枚举。