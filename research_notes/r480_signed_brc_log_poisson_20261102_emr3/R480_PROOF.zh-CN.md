# R480 — signed BRC 左缘 Poisson 极限的定量对数增长窗口

日期：2026-11-02。作者侧解析证明及精确分数验证；状态 AUTHOR_SIDE_ANALYTIC / DRIVER_UNREVIEWED / NOT_ADMITTED。科学输入继续固定于 R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f，直接复用 R479@752ed68bd6404267d036761cc412846969f1ec21 的 signed BRC/Catalan 精确变换。只研究有符号 BRC 来源的辅助标量读出，不改变 P000、ACTIVE 世界观或原生 X6 结论。

## 对象

对奇数 r≥9，整数 0≤j≤r−2，记 Catalan 数 C_n=binom(2n,n)/(n+1)，以及 R479 精确恒等式

\[
a_{r,j}=H(r,r-j)=\binom{2r-j}{j}\sum_{q=0}^j\binom jq(-2)^q C_{r-q},\qquad b_{r,j}=\frac{a_{r,j}}{C_r r^j}.
\]

越界的 a、b 置零。令
\[
D_{m,j}^{(r)}=\det(a_{r,j+v-i})_{0\le i,v<m}.
\]

## 定理 1：精确系数误差界

若 1≤L≤r/4，且 0≤t≤L，定义
\[
\alpha_{r,L}=\frac3{2(r-L)-1},\qquad
\eta_{r,L}=\frac{3L^2-L}{4r}+(3+\alpha_{r,L})^L-3^L.
\]
则
\[
\boxed{\left|t!\frac{a_{r,t}}{C_r r^t}-1\right|\le\eta_{r,L}.}\tag{1}
\]

证明：Catalan 相邻比值给出精确乘积
\[
\frac{C_{r-q}}{C_r}=4^{-q}G_{r,q},\quad
G_{r,q}=\prod_{h=0}^{q-1}\left(1+\frac3{2(r-h)-1}\right),
\quad 1\le G_{r,q}\le(1+\alpha_{r,L})^q.
\]
令 S_{r,j}=\sum_q\binom jq(-2)^q C_{r-q}/C_r。因为 \sum_q\binom jq(-1/2)^q=2^{-j}，由三角不等式和二项式定理，
\[
|2^jS_{r,j}-1|\le (3+\alpha_{r,L})^j-3^j.
\]
另有
\[
T_{r,j}=\frac{j!}{(2r)^j}\binom{2r-j}{j}
=\prod_{h=0}^{j-1}\left(1-\frac{j+h}{2r}\right),
\quad 0\le1-T_{r,j}\le\frac{3j^2-j}{4r}.
\]
由 j!b_{r,j}=T_{r,j}(2^jS_{r,j})、0≤T≤1，得到 (1)。j=0 时精确相等。

## 定理 2：全部有限参数的相邻子式判据

设 m≥1、0≤j≤L−m+1，记
\[
\Pi_m=\prod_{i=0}^{m-1}i!,\quad M_m=\frac{m(m-1)}2,\quad
\mathcal E_{r,L,m}=\frac{m!(L+m)^{M_m}}{\Pi_m}[(1+\eta_{r,L})^m-1].
\]
若 \(\mathcal E_{r,L,m}<1\)，则
\[
\boxed{D_{m,j}^{(r)}>0,}\qquad
\frac{D_{m,j}^{(r)}}{(C_rr^j)^m}
\ge(1-\mathcal E_{r,L,m})\prod_{i=0}^{m-1}\frac{i!}{(j+i)!}>0.\tag{2}
\]

证明：取 (1) 的 e_t=t!b_{r,t}−1。在 \det(b_{r,j+v-i}) 各列提取 (j+v)! 的倒数，剩余矩阵为
\[
A_{iv}=(j+v)_{\underline i}(1+e_{j+v-i}),
\]
负下标项按降阶阶乘的零值处理。未扰动矩阵 A⁰_{iv}=(j+v)_{\underline i} 的行列式为 \(\Pi_m\)，因为降阶阶乘是首一多项式基，列参数 j,j+1,…,j+m−1 的 Vandermonde 行列式等于 \(\prod i!\)。每个未扰动排列乘积的绝对值至多 (L+m)^{M_m}；各乘积受 |e_t|≤η 扰动的绝对差至多此界乘 [(1+η)^m−1]。逐一相加 m! 项，得到
\[
|\det A-\Pi_m|\le m!(L+m)^{M_m}[(1+\eta)^m-1]=\Pi_m\mathcal E.
\]
系数分解 a_{r,t}=C_rr^t b_{r,t} 使行列式归一化因子恰为 (C_rr^j)^m，证毕。

## 推论 3：随 r 无界增长的对数左缘正性带

对每个固定整数 m≥1 和实数 0<c<1，存在 R(c,m)，使全部奇数 r≥R(c,m) 及
\[
0\le j\le\lfloor c\log_3r\rfloor-m+1
\]
满足 D_{m,j}^{(r)}>0。任意固定有限阶数集合亦可取同一充分大的 R。

证明：取 L=floor(c log₃r)。有 3^L≤r^c、L=O(log r)、α=O(1/r)，并且
\[
(3+\alpha)^L-3^L\le3^L\frac{L\alpha}{3}(1+\alpha/3)^L.
\]
所以 η=O((log r)^2/r+(log r)r^{c−1})，固定 m 时 \(\mathcal E=O(\eta(\log r)^{M_m})=o(1)\)。由定理 2 得证。这加强了 R479 的固定左缘位置结论：位置 j 自身也无界增长。

## 推论 4：显式统一阈值与精确证书

设 L=25，对全部奇数
\[
\boxed{r\ge 10^{24}+1=1000000000000000000000001}
\]
及 m=1,2,3,4，0≤j≤26−m，严格有 D_{m,j}^{(r)}>0。以 Python 任意精度整数和 Fraction 在 r₀=10²⁴+1 计算，四个 m 全部精确满足 \(\mathcal E_{r_0,25,m}<1/16\)。固定 L 时 \(\eta_{r,L}\) 对 r 单调下降，故阈值对全部更大 r 有效。阈值为保守充分界。

## 补充：固定 j 的一阶渐近修正

对每个固定 j≥0，展开 T 与 G 的有限乘积可得
\[
\boxed{\frac{j!a_{r,j}}{C_rr^j}=1-\frac{3j^2+5j}{4r}+O_j(r^{-2}).}
\]
这里 G_{r,q}=1+3q/(2r)+O_j(r^{-2})，且 \(\sum_q\binom jq(-1/2)^qq=-j2^{-j}\)。本式可供后续构造更宽窗口的精确误差证书使用。

## 验证及下一问题

同目录 R480_VERIFY.py 用纯整数/Fraction 在阈值 r₀ 精确判定四个严格有理数不等式，对奇数 r=9,11,…,101 的 309 项系数、954 项正规化行列式误差界逐项检查，并对20项参数同原始 signed 卷积比较。结果见 R480_EVIDENCE.json。无穷参数结论由上面的解析推导支持，属于作者侧证明，独立审查待办。

BRC 复用决议 REUSE_APPLIED：保留 R479 在 frozen R462 来源下的 signed BRC/Catalan 读出及相应支路类型；没有把辅助标量的 Toeplitz 符号性质提升为原生 X6 动力学。R479 右缘移动位置的四阶负子式仍然成立，本轮展示的是同时可成立的增长左缘正性窗口。

下一最小研究问题：减少基于三角不等式的 3^L 放大，建立 j=o(r^θ) 的系数误差和三阶曲率下界；另检验固定右缘 s≥4 的四阶负子式阈值。研究母目标继续保持。
