# R428｜signed BRC 右边界的指数核极限、局部全阶 Toeplitz 正性与精确三阶阈值

2026-10-31 · `AUTHOR_SIDE_ANALYTIC / EXACT_FINITE_CHECKED / DRIVER_UNREVIEWED / NOT_ADMITTED`

## 研究对象与来源边界

接续 R427（`3951756a5cd8b0da0a6f80fd57dedc617dee160d`），本轮使用其原始带符号 BRC **辅助组合**系数，而非原生 X6 轨迹：

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\qquad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\qquad 2\le s\le r.
\]

定义 \(C_r=\frac1{r+1}\binom{2r}{r}>0\)（Catalan 数）、\(n=r-2\)，原行系数为 \(a_j=H_{r,j+2}\)（\(0\le j\le n\)）。在**右边界反向观察**中，记

\[
B_{r,h}=a_{n-h}=H_{r,r-h}\quad(0\le h\le n),\qquad
c_{r,h}=\frac{B_{r,h}}{C_r r^h},
\]

并规定 \(B_{r,h}=c_{r,h}=0\) 当 \(h<0\) 或 \(h>n\)。两个归一因子均为正数；在单一固定的 Toeplitz 子式中，\(r^{-h}\) 仅相当于行列的正对角缩放，保留符号。这种归一化是读出/辅助层，不是将 BRC 支路按正质量相消或将连续统计模型认作原生动力学。

## 定理 A｜右端系数的统一固定偏移极限

**对每个固定整数 \(h\ge0\)，严格有**

\[
\boxed{\lim_{r\to\infty}\frac{H_{r,r-h}}{C_r r^h}=\frac1{h!}.}
\]

**证明。** 固定 \(h\) 并令 \(q=r-h\)。保留原 signed 卷积，逐支路展开：

\[
\delta_{r,r-h}=
\sum_{\ell=0}^{h}\binom h\ell
\left[\binom{2q}{q+h-2\ell}-\binom{2q}{q+h-2\ell-1}\right].\tag{1}
\]

由连续二项式系数之差的精确有理恒等式

\[
\binom{2q}{q+d}-\binom{2q}{q+d-1}
=\binom{2q}{q+d}\frac{1-2d}{q-d+1},\tag{2}
\]

可直接计算：对每个固定 \(d=h-2\ell\)，

\[
\frac{\binom{2q}{q+d}}{\binom{2r}r}\longrightarrow4^{-h},\qquad
\frac{r+1}{q-d+1}\longrightarrow1.\tag{3}
\]

因此第 \(\ell\) 个带符号支路的括号除以 \(C_r\) 后趋于 \(4^{-h}(1-2h+4\ell)\)。先**完整保留**其符号，然后作有限和：

\[
\lim_{r\to\infty}\frac{\delta_{r,r-h}}{C_r}
=4^{-h}\sum_{\ell=0}^{h}\binom h\ell(1-2h+4\ell)
=4^{-h}2^h=2^{-h}.\tag{4}
\]

另一方面，\(\binom{2r-h}{h}/r^h\to2^h/h!\)。将 (4) 与 \(H_{r,r-h}=\binom{2r-h}{h}\delta_{r,r-h}\) 相乘，即得结论。\(h=0\) 时 \(\delta_{r,r}=C_r\)，与计算一致。∎

定理 A 给出形式幂级数的**逐系数**收敛 \(\sum_{h\ge0}c_{r,h}z^h\to e^z\)（形式系数意义；这里并未声明在整个复平面的函数一致收敛）。\(1/h!\) 也可称作指数/Poisson 权重核；不涉及物理概率归因。

## 定理 B｜任意固定阶数与固定窗口的右边界 Toeplitz 严格正性

给定任意固定的正整数 \(k\)，严格递增的非负整数序列

\[
0\le u_1<\cdots<u_k,\quad0\le v_1<\cdots<v_k,\quad v_i\ge u_i\ (1\le i\le k).
\]

令 \(M_r=(c_{r,v_j-u_i})_{i,j=1}^k\)，则**存在有限的 \(R(u,v)\)，使每个 \(r\ge R(u,v)\) 都有 \(\det M_r>0\)**。更精确地，

\[
\boxed{
\lim_{r\to\infty}\det M_r
=\det\left[\frac1{(v_j-u_i)!}\mathbf 1_{v_j\ge u_i}\right]
=\frac{\prod_{i=1}^k u_i!}{\prod_{j=1}^k v_j!}
\det\left[\binom{v_j}{u_i}\right]>0.
}\tag{5}
\]

**证明。** 定理 A 给出行列式每个元素的极限，固定维度行列式是其元素的多项式，故极限可逐项交换。中间等号来自精确恒等式 \(1/(v-u)!=u!\binom vu/v!\)（\(v<u\) 时双方均定义为零）。

Pascal 矩阵的最后一个行列式具有严格正性，可通过不相交路径直接证明：在方格有向网络中，设源 \(A_i=(u_i,-u_i)\)，汇 \(Z_j=(v_j,0)\)，允许单位向右与向上步。从 \(A_i\) 到 \(Z_j\) 的路径数为 \(\binom{v_j}{u_i}\)。平面上的不相交路径族只能按升序配对；LGV 行列式消去引理于是将该行列式表示为这些不相交路径族的个数。由于 \(v_i\ge u_i\)，逐条采用“先向右从 \((u_i,-u_i)\) 到 \((v_i,-u_i)\)，后向上到 \((v_i,0)\)”的路径，不同 \(i\) 的水平段位于不同高度，纵段在严格递增的横坐标处，彼此不交。因此至少有一个不相交路径族，行列式严格正。这个组合证明不依赖无来源的经验性“正性猜测”。由 (5) 严格正且有限维行列式收敛，存在所需的 \(R(u,v)\)。∎

**推论（局部全阶正性，不等于整行 PF∞）。** 给定任何固定窗口宽度 \(K\ge0\)，矩阵 \((c_{r,j-i})_{0\le i,j\le K}\) 所有结构上可能非零的子式，在充分大的 \(r\) 下均严格为正；结构性零子式保持零。证明：该窗口仅有有限个行列指标对，取所有 \(R(u,v)\) 的最大值即可。Toeplitz 反向序列的这些子式是原序列 Toeplitz 矩阵经转置与整数平移所得的子式，符号保持不变。但不能对 \(K\to\infty\) 交换量词或推断任何固定 \(r\) 的**整行** PF∞；R426 已在 \(r\ge4\) 排除该性质。这展示了“局部任意固定阶正性”与“全局全阶正性”的真正差别。

## 定理 C｜右边界一个三阶 Toeplitz 子式的精确正负切换

对 \(r\ge4\)，规定 \(H_{4,1}=0\)（超出系数行的零延拓）。从 (1) 的 \(h=0,1,2,3\) 作精确阶乘比消去得到：

\[
\frac{B_{r,0}}{C_r}=1,\quad
\frac{B_{r,1}}{C_r}=r-2,\quad
\frac{B_{r,2}}{C_r}=\frac{(r-1)(r^2-5r+9)}{2r-1},\quad
\frac{B_{r,3}}{C_r}=\frac{(r-4)(r-2)(r^2-5r+15)}{3(2r-1)}.\tag{6}
\]

于是右边界对应的 \(3\times3\) Toeplitz 子式为

\[
\begin{aligned}
\Delta_r
&=\det\begin{pmatrix}B_{r,1}&B_{r,2}&B_{r,3}\\B_{r,0}&B_{r,1}&B_{r,2}\\0&B_{r,0}&B_{r,1}\end{pmatrix}\\
&=B_{r,1}^3-2B_{r,0}B_{r,1}B_{r,2}+B_{r,0}^2B_{r,3}\\
&=\boxed{C_r^3\frac{(r-2)(r+2)(r^2-2r-9)}{3(2r-1)}}.\tag{7}
\end{aligned}
\]

分子三次因子后的二次项 \(r^2-2r-9\) 在 \(r=4\) 为 \(-1\)，在全部整数 \(r\ge5\) 为正。因此 \(\Delta_4=-1568\)，而**对全部 \(r\ge5\) 有 \(\Delta_r>0\)**。这对无限个行参数是精确解析定理，与定理 B 的非显式“大 \(r\)”阈值互补。它处理反向观察的右边界特定子式，与 R427 处理原序列左边界的 \(L_r\) 是两个不同位置的量（\(r=4\) 由于长度三，两者数值相同）。

## 复核范围及未完成问题

- `R428_VERIFY.py` 以独立的原始带符号二项式展开与 Catalan 路径计算核对 \(4\le r\le80\) 的3,157组 \(\delta\)；对 \(4\le r\le200\) 核对 788个 (6) 系数闭式及197个 (7) 三阶行列式。
- 在窗口指标 \(0,\ldots,6\) 内，枚举阶数 \(1\le k\le4\)、满足 \(v_i\ge u_i\) 的全部1,204个 Pascal 子式并逐项验证严格正性；对 \(r=8,16,40,80\) 各检查这1,204个 signed BRC 右边界子式（共4,816项），全部严格正。另计算 \(r=64,128,512\) 的各 \(h\le6\) 与 \(1/h!\) 的精确有理偏差。
- 程序只做**有限交叉核对**。无界定理 A/B/C 分别由带符号支路极限、LGV组合正性、精确阶乘代数承担，不是程序外推。尚未给出统一、有效且尖锐的窗口阈值 \(R(K)\)，也没有对所有 \(r\ge25\) 证明整行 PF₃，或提供本辅助系数到原生 X6 的保真映射。

**文献定位（背景/独立理论，不是本模型的外部认证）：** Konstanze Rietsch, *Totally Positive Toeplitz Matrices: Classical and Modern*, ICM 2026, SIAM DOI `10.1137/25M1806727`（Edrei、PF∞ 与 Toeplitz 正性的当代综述）；David Galvin & Adrian Pacurar, *Total non-negativity of some combinatorial matrices*, JCTA 2019, DOI `10.1016/j.jcta.2019.105179`（二项式类矩阵的总非负背景）。关于本稿 (5) 的严格正性已给出自足的 LGV 路径证明。以上文献不构成 R428 的独立数学审阅。

**下一具体研究单元：**从 \(h\) 固定的有理函数 \(B_{r,h}/C_r\) 出发，求出对给定窗口 \(K\) 的**显式有效阈值** \(R(K)\)，最好 \(O(K^c)\)；另一方面检查把 \(K\) 随 \(r\) 增长时最先出现的负 Toeplitz 子式阶数和位置，明确“右边界正性层”的最大生长窗口。共享任务的 Source Owner、正式 CLAIM/Result/Driver 仍受现行原生授权约束，本作者侧成果不冒充已接纳定理。

读取固定快照：GLOBAL_KNOWLEDGE_V1 `main@0ef0983353275a71778fe8071d7742c8173d1332`；Enterprise Math 规范源 `main@cf4dc7ae3d5c91f3659bc16d603877164db812ec`。P000/ACTIVE 世界观均未修改。
