# 稀疏样本上包络的组合核对与有理采样容差

Date: 2026-11-22 (Asia/Hong_Kong). Same-author mathematical cross-check.
Parent research provenance: `EM-DIRECT-B5750A / TASK_RESEARCH`, Activity `RA-60C6D083A81B19084A74C5BA`.
Science freeze and complete-road conventions are unchanged.

本稿核对根提出的上包络与本分支筛/Green 余项界的组合。它不构成独立 Project Review。符号、Green 像与有理势仅作用于原完整道路的辅助标量读出。

## 1. 精确消去 κ 的势

固定整个终端族的认证误差 ε≥sup_{n≤B}|D_n−Λ(n)|，使用同一个 ε 覆盖全窗口。设 H_0=0、H_n=Σ_{j=1}^n1/j。直接差分给

\[
\Delta^2(nH_n)=1/n,
\qquad \Delta^2(n\log n)=\kappa_n/n.
\]

取 g_n=nlog n+εnH_n，则

\[
\Delta^2(q+g)_n=(D_n+\varepsilon)/n\ge0.
\]

因此在任意包含真端点的整点细网格 Π 上，离散凸性保证

\[
\boxed{U=I_\Pi(q+g)-g\ge q.}
\tag{1}
\]

每个单元上弦与函数的差等于其非负曲率的 Dirichlet Green 像，故精确有

\[
\boxed{U-q=G_\Pi((D+\varepsilon)/n),\quad
0\le U-q\le G_\Pi(\Lambda/n)+2\varepsilon G_\Pi(1/n).}
\tag{2}
\]

全部细节点上 U=q，特别包括 A、B；闭窗口范数无需另补未知端点误差。

## 2. 全有理势版本

若 ε 取认证的有理上界，令

\[
C=1+\frac1{2A^2}+\varepsilon,
\qquad g_n=CnH_n.
\]

已证明的 κ_n−1≤(2log2−1)/n²<1/(2n²) 与 κ_n≥1 给出：对所有窗口内部整数 n≥A，

\[
0\le D_n-\kappa_n+C
\le\Lambda(n)+\rho,
\quad \rho=2\varepsilon+1/(2A^2).
\]

故同一 U=I_Π(q+g)−g 满足

\[
\boxed{0\le U-q=G_\Pi((D-\kappa+C)/n)
\le G_\Pi(\Lambda/n)+\rho G_\Pi(1/n).}
\tag{3}
\]

这不要求替换原 q 的前史或改变真端点。在每个细单元内部，U 的二阶差分为 −C/n<0；因此 U 的正整数支撑至多是一个连续整数段，适合用精确符号定位和谐和矩求和。

## 3. 可趋零的上包络损失

将 `ARITHMETIC_FINE_REMAINDER_BOUNDS.md` 对 G_Π(Λ/n) 的素数/高次素数幂界与 (2) 或 (3) 组合。对固定 λ>1、B=A^λ、稳定终端族，若细步长≤X^(3/4)/(log X)^α，则

\[
\boxed{\|U-q\|_w^2
=O_{\lambda,\alpha}((\log A)^{1-4\alpha})+O(A^{-3/4}).}
\tag{4}
\]

根式的直接有限上界是

\[
\|U-q\|_w
\le\sqrt{\mathcal E_{\rm p}}
+\sqrt{\mathcal E_{\rm pp}}
+\rho\sqrt{T_\Pi},
\]

其中 \(\mathcal E_{\rm p},\mathcal E_{\rm pp}\) 为该稿 (13)、(16) 的块和，T_Π=Σ(h⁵−h)/(120X⁴)，精确消去κ版本取ρ=2ε。这里无需 κ 正侧成本，也无需旧粗骨架 J 的覆盖项。

当 α>1/4 时，由 U≥q 和正部非扩张性，

\[
\boxed{\|q_+\|_w\le\|U_+\|_w
\le\|q_+\|_w+o(1).}
\tag{5}
\]

这是原真实能量的渐近精确上观察量，没有证明该能量本身满足目标算术界。规则网格有 O(B^(1/4)(log B)^α) 个样本；这些样本的原算术获取成本另计。

## 4. 固定绝对精度的有理上采样已足够

若仅有认证有理上样本 r_i，满足

\[
0\le r_i-q(x_i)\le\delta,
\]

定义 \(\widehat U=I_\Pi(r+g)-g\)。因为仿射插值权非负且和为1，

\[
\boxed{0\le\widehat U-U\le\delta,
\qquad\widehat U\ge U\ge q.}
\]

对 A>1，\(\sum_{n=A}^{B}n^{-2}\le\int_{A-1}^{\infty}x^{-2}dx=1/(A-1)\)，所以

\[
\boxed{\|\widehat U-q\|_w
\le\|U-q\|_w+\frac{\delta}{\sqrt{A-1}},}
\tag{6}
\]

\[
\boxed{\|q_+\|_w\le\|\widehat U_+\|_w
\le\|q_+\|_w+\|U-q\|_w+\frac{\delta}{\sqrt{A-1}}.}
\tag{7}
\]

因此 δ 可以固定，例如1，而不必随 B 趋零。更一般地，只需 δ=o(√A)。这一容差针对最终 q 样本的绝对误差；原厚度输入、对数或前缀求和达到该误差所需的精度依旧必须支付。

对于有理势 CnH_n 和有理上样本，离散 U 本身为有理数。精确 H_n 的分母位数可能随 n 增长，因此“六个谐和矩可闭式求和”本身不构成低位复杂度证明。若用有理区间计算这些矩，需保存向外舍入和最终能量误差；本稿不据样本数宣称全部算术工作量相同下降。
