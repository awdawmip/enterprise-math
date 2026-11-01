# R448｜signed BRC 的五次根增长窗口：无限参数局部 PF₃ 解析定理

**日期**：2026-11-01。**角色**：独立作者侧可移植推导（非正式 CLAIM，未独立审阅，NOT_ADMITTED）。**定位**：R446 的 Poisson 边缘极限与 R447 的固定宽度 24 精确证书之后的下一数学单元。仅研究 **signed BRC 辅助标量** Toeplitz 子式，保留原始带符号卷积；没有推导原生六维 X6 空间、三维切片、时间演化或物理观测的保真性，也不改动 P000/ACTIVE 世界观。

## 主定理：窗口宽度可随 r 无界增长

令 \(r\) 为正奇数，\(0\le h\le r\)，定义

\[
H(r,r-h)=\binom{2r-h}{2r-2h}[t^r](1-t)(1+t)^{2r-2h}(1+t^2)^h,
\qquad C_r=\frac1{r+1}\binom{2r}{r}>0.
\]

令 \(b_h=H(r,r-h)\)，对 \(h<0\) 取 \(b_h=0\)，并取 \(T^{(r)}_{ij}=b_{j-i}\)（\(i,j\ge0\)）。固定任意整数 \(L\ge1\)，若

\[
\boxed{r\ge652L^5\qquad(r\text{ 为奇数}),}
\]

则对于每个 \(m\in\{1,2,3\}\) 与每组 \(0\le j_1<\cdots<j_m\le L\)，有严格正性

\[
\boxed{\det\bigl[b_{j_v-i}\bigr]_{0\le i<m,\ 1\le v\le m}>0.}
\]

等价地，设 \(L(r)=\lfloor(r/652)^{1/5}\rfloor\)，对所有使 \(L(r)\ge1\) 的奇数 \(r\)，上述结论在 \(L=L(r)\) 时成立。特别是 **\(L(r)\to\infty\)**，这比 R446/447 的固定列宽结论多了一个显式的无限参数、增长窗口方向。依 R441 已使用的 Jacobi–Trudi / Littlewood–Richardson 非负展开，任意行列最小相对列跨度 \(j_{\max}-i_{\min}\le L\) 的至多三阶 Toeplitz 子式亦非负，容许结构零。

**限定**：这不证明整个半无限矩阵 \(T^{(r)}\) 满足 PF₃；\(L(r)=O(r^{1/5})\) 也不是 \(L\asymp r\) 的比例窗口。常数 652 为保守可验证界，不声明最优。即使使用经典 Schur 非负展开，以上带宽外的任意子式仍是开放问题。

## 引理 1：原始 signed 卷积的概率表达（精确恒等式）

记 \((x)_{\underline n}=x(x-1)\cdots(x-n+1)\)，\(\rho_h(r)=b_h/C_r\)。对 \(r\ge2h+2\) 原始卷积展开为

\[
H(r,r-h)=\binom{2r-h}{h}\sum_{q=0}^h\binom hq
\left[\binom{2r-2h}{r-2q}-\binom{2r-2h}{r-2q-1}\right].
\]

由 \(\binom nk-\binom n{k-1}=\binom nk\,(n-2k+1)/(n-k+1)\) 及 \(C_r=\binom{2r}r/(r+1)\)，得到

\[
\rho_h(r)= \frac{(r+1)(2r-h)_{\underline h}}{h!(2r)_{\underline{2h}}}
\sum_{q=0}^h\binom hq\,
\frac{(r)_{\underline{2q}}(r)_{\underline{2h-2q}}(4q-2h+1)}{r-2h+2q+1}.
\tag{1}
\]

该式带符号因子 \(4q-2h+1\)，不可把它当作正质量。对 \(h\ge1\) 定义以下 **正的有理数**（\(0\le q\le h\)）：

\[
F_{h,q}(r)=
\underbrace{\frac{r+1}{r-2h+2q+1}}_{A_q}
\underbrace{\frac{(2r-h)_{\underline h}}{(2r)^h}}_{B}
\underbrace{\frac{(r)_{\underline{2q}}(r)_{\underline{2h-2q}}}{r^{2h}}}_{M_q}
\underbrace{\frac{(2r)^{2h}}{(2r)_{\underline{2h}}}}_{D}.
\tag{2}
\]

令 \(Q\sim\mathrm{Binomial}(h,1/2)\)。对 (1) 提取 \(r^h/h!\) 并使用二项权重可得精确恒等式

\[
\boxed{\frac{h!}{r^h}\rho_h(r)=
\mathbb E\big[(4Q-2h+1)F_{h,Q}(r)\big].}\tag{3}
\]

在 \(F_{h,q}\equiv1\) 的 Poisson 参考模型中，\(\mathbb E(4Q-2h+1)=1\)。对 \(h=0\)，有 \(\rho_0=1\)。

## 引理 2：不丢弃 signed cancellation 的一致相对误差

当 \(h\ge1\)、\(r\ge8h^2\) 时，对所有 \(q=0,\ldots,h\)，有

\[
\boxed{1-3h^2/r\ \le F_{h,q}(r)\ \le 1+7h^2/r<2.}\tag{4}
\]

证明：\(A_q\ge1\) 且 \(A_q\le1+4h/r\)。由 \(\prod(1-x_i)\ge1-\sum x_i\)（\(0\le x_i\le1\)）得

\[
1-h^2/r\le B\le1,\qquad 1-2h^2/r\le M_q\le1.
\]

此外 \(1\le D\le (1-h^2/r)^{-1}\le1+2h^2/r\)。上界 \((1+4h/r)(1+2h^2/r)\le1+7h^2/r\)，使用 \(h\ge1\)、\(r\ge8h^2\)；下界由 \(A_qD\ge1\) 和 \(BM_q\ge1-3h^2/r\) 得到。

更重要的是，相邻 \(q\) 的比值 **完全消去公共因子**：

\[
\boxed{\frac{F_{h,q+1}}{F_{h,q}}
=\frac{(r-2q)(r-2q-1)}{(r-2h+2q+2)(r-2h+2q+3)}},\quad0\le q<h.
\tag{5}
\]

记右端分子为 \(x_1x_2\)、分母为 \(y_1y_2\)。\(|x_1-y_1|,|x_2-y_2|\le2h\)，\(x_2\le r\) 且 \(y_1,y_2\ge r/2\)。因此

\[
\left|F_{h,q+1}/F_{h,q}-1\right|\le12h/r,
\qquad |F_{h,q+1}-F_{h,q}|\le24h/r.
\tag{6}
\]

这是从 \(O(h^3/r)\) 的粗绝对值估计改进为 \(O(h^2/r)\) 的关键：\(F\) 的相邻变化可控。

精确的二项分布差分恒等式（令 \(Y\sim\mathrm{Binomial}(h-1,1/2)\)）为

\[
\mathbb E[(Q-h/2)f(Q)]
=\frac h4\,\mathbb E[f(Y+1)-f(Y)].
\tag{7}
\]

可直接把 \(Q\) 写为 \(h\) 个独立公平 Bernoulli 变量之和，对每个变量条件求期望证明 (7)。用 \(4Q-2h+1=1+4(Q-h/2)\) 将 (3) 化为

\[
\frac{h!}{r^h}\rho_h(r)
=\mathbb EF_{h,Q}+h\,\mathbb E[F_{h,Y+1}-F_{h,Y}].
\]

结合 (4)、(6) 得出完全显式、**对所有 \(0\le h\le L\) 一致** 的估计

\[
\boxed{\left|\frac{h!\,\rho_h(r)}{r^h}-1\right|
\le31h^2/r\le\varepsilon:=31L^2/r}\quad(r\ge8L^2).
\tag{8}
\]

这个步骤保留 signed 权重与协方差，不以各项绝对值替换原始相消。

## 引理 3：Vandermonde 行列式的定量稳定性

把连续行子式的第 \(i\) 行乘 \(r^i>0\)，第 \(v\) 列乘 \(j_v!r^{-j_v}>0\)，并除以 \(C_r>0\)。归一化矩阵为

\[
M_{i,v}=\begin{cases}
(j_v)_{\underline i}\,(1+\delta_{j_v-i}),&j_v\ge i,\\
0,&j_v<i,
\end{cases}
\qquad|\delta_h|\le\varepsilon.
\tag{9}
\]

因此 \(M\) 的行列式与原来的子式同号。其参考矩阵 \(V_{i,v}=(j_v)_{\underline i}\) 由首项系数为 1 的阶乘多项式组成，故

\[
\det V=\prod_{v<w}(j_w-j_v)
\begin{cases}
=1,&m=1,\\
\ge1,&m=2,\\
\ge2,&m=3.
\end{cases}
\tag{10}
\]

对 \(\varepsilon\le1\)，按 Leibniz 展开逐项比较，因 \(0\le(j_v)_{\underline i}\le L^i\) 得

\[
|\det M-\det V|\le m!L^{m(m-1)/2}[(1+\varepsilon)^m-1].
\]

分别为

\[
\begin{array}{c|c}
m&|\det M-\det V|\text{ 的上界}\\\hline
1&\varepsilon=31L^2/r\\
2&6L\varepsilon=186L^3/r\\
3&42L^3\varepsilon=1302L^5/r.
\end{array}\tag{11}
\]

当 \(r\ge652L^5\)、\(L\ge1\) 时，自动满足 \(r\ge8L^2\)、\(\varepsilon<1\)。一阶误差小于 1；二阶误差 \(\le186/(652L^2)<1\)；三阶误差 \(\le1302/652<2\)。由 (10) 每个 \(\det M\) 严格为正。证明完成。注意三阶下界 **2** 而不是 1 是阈值常数 652 的来源。

## 运行核验与来源

`R448_VERIFY.py` 使用 `fractions.Fraction`、`math.comb` 的任意精度整数有理运算，实际运行返回 `R448_PASS`。它独立按原始 signed 二项卷积核对 30 个 \((r,h)\) 输入；对 \(L=1,\ldots,8\) 各取奇数 \(r=652L^5+1\)，核对 156 次 \(F\) 界、120 次相邻比值/差分界，及 374 个一至三阶归一化子式和严格误差上界。**这些是有限抽样的实现交叉检查，不能替代上面的全称解析证明**；详细数量及输入见 `R448_EVIDENCE.json`。无浮点数判号。

BRC 路径：`REUSE_APPLIED`，原始 signed 12-branch 辅助标量定义来自 R446/R447；使用原始符号卷积、Catalan 正比例、R441 的 Schur–LR 归约，不以正质量取代有符号相消。数学外部依据：Marc A. A. van Leeuwen, *Schur Functions and Alternating Sums*, Electronic Journal of Combinatorics 11(2), A5 (2006), DOI [10.37236/1897](https://doi.org/10.37236/1897)，包含 Jacobi–Trudi 与 Littlewood–Richardson 规则。内部实际基础：`R446_PROOF.zh-CN.md`、`R447_PROOF.zh-CN.md` 和 `R441_PROOF.zh-CN.md`（现有 Draft PR #1708）。

**本轮读取的固定来源**：GLOBAL_KNOWLEDGE_V1 `main@b33cf2f18b4fbfd428312f384310cb2601c68a79`；Enterprise Math 规范源 `main@ce7279d4cafc8d7ddb4a65d75c33e8c40849428c`；直接研究接续 PR #1708 原 HEAD `adb2f26bee7e47f36991879f1b975a0fc7fbf3bc`。P000/ACTIVE 世界观未修改。原生 Source control_tasks 读取得到 `CONTROL_QUOTA`，session_start 得到 `STATIC_READONLY_SCOPE_DENIED / operation_sent=false`，故目前仅为 **AUTHOR_SIDE_ANALYTIC / CHECKED_EXAMPLES / REGISTER_PENDING / DRIVER_UNREVIEWED / NOT_ADMITTED**；不声称合法 CLAIM、Result 或正式 Owner 已确认。

## 下一最小未解单元

本轮将固定宽度扩展为 \(L\ll r^{1/5}\) 的明确增长窗口，但未得到 \(j/r\in[0,\alpha]\) 的一致 PF₃。下一步优先通过 **二阶离散差分/行列式专属结构** 替换 (11) 中对每个排列单项式的绝对误差，把五次根提升到更高增长幂；若仍达不到比例窗口，构造随 \(r\) 增长的三阶边界负证作为反例测试。对于完整半无限 PF₃ 的数学结论，仍须覆盖所有列窗口和相应非连续子式，任何新证书都应保存其全量量词和边界。
