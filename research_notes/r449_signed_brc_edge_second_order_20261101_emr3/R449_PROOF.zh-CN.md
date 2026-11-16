# R449｜signed BRC Poisson 边缘二阶修正与任意固定阶 Toeplitz 子式一阶公式

日期：2026-11-01。类别：作者侧独立 portable research；UNREVIEWED / NOT_ADMITTED。研究对象：R448 原始 signed BRC 辅助标量；不把带符号相消视为正质量，不作原生 X6 动力学保真转移。P000/ACTIVE 世界观未修改。

## 数学定理 A：全部固定 h 的二阶精确展开

令奇数 r→∞，固定非负整数 h，Catalan 数 C_r=binom(2r,r)/(r+1)，以及原始 signed 卷积

\[
H(r,r-h)=\binom{2r-h}{2r-2h}[t^r](1-t)(1+t)^{2r-2h}(1+t^2)^h.
\]

取 E_h(r)=h!H(r,r-h)/(C_r r^h)。那么

\[
\boxed{E_h(r)=1-\frac{h(3h+5)}{4r}+
\frac{h(h-1)(27h^2+89h+254)}{96r^2}+O_h(r^{-3}).}\tag{A}
\]

下标 h 在此固定，余项常数允许依赖 h；不声称窗口增长时的一致性。

证明：R448 已从原始有符号卷积建立 exact identity

\[
E_h(r)=\mathbb E[(4Q-2h+1)F_{h,Q}(r)],\quad Q\sim {\rm Binomial}(h,\tfrac12),
\]
\[
F_{h,q}(r)=\frac{r+1}{r-2h+2q+1}
\frac{(2r-h)_{\underline h}}{(2r)^h}
\frac{(r)_{\underline {2q}}(r)_{\underline {2h-2q}}}{r^{2h}}
\frac{(2r)^{2h}}{(2r)_{\underline {2h}}}.
\]

对固定 h,q，令 x=1/r。有限乘积对数展开给出
\[
\log F_{h,q}(1/x)=U(h,q)x+V(h,q)x^2+O_h(x^3),
\]
\[
U=-\frac{7h^2-16hq-11h+16q^2+8q}{4},
\]
\[
V=-\frac{62h^3-192h^2q-141h^2+192hq^2+288hq+103h-192q^2-96q}{48}.
\]

这些表达式来自 log(1+z)=z-z²/2+O(z³) 与有限和 Σk=n(n−1)/2、Σk²=n(n−1)(2n−1)/6。故 F=1+U/r+(V+U²/2)/r²+O_h(r−3)。对 W=4Q−2h+1，有 E[W]=1。利用精确矩恒等式

\[
\mathbb E[Q^k]=\sum_{\ell=0}^k
\left\{\begin{matrix}k\\\ell\end{matrix}\right\}
\frac{(h)_{\underline\ell}}{2^\ell}
\]

进行未定元 h 的多项式化简，逐项得到

\[
\mathbb E[WU]=-\tfrac14 h(3h+5),\quad
\mathbb E[W(V+U^2/2)]=
\tfrac1{96}h(h-1)(27h^2+89h+254).
\]

这两式是有限多项式恒等式，不是由有限 h 插值得出的猜想。h=0 时 E_0≡1，亦满足 (A)。证毕。

## 数学定理 B：任意固定阶 m 连续行子式的第一渐近修正

设 m≥1 固定，列组 0≤j_0<⋯<j_{m−1} 固定，且 b_k=H(r,r−k)，k<0 时 b_k=0。记
\[
\Delta(\mathbf j)=\prod_{v<w}(j_w-j_v)>0,
\quad
\Lambda_m(\mathbf j)=-3\sum_v j_v^2+(6m-11)\sum_vj_v+
m(m-1)(5-2m).
\]

则完整的原始 Toeplitz 连续行子式满足

\[
\boxed{
\det[b_{j_v-i}]_{0\le i,v<m}
=\frac{C_r^m r^{\sum_v j_v-m(m-1)/2}}{\prod_v j_v!}
\Delta(\mathbf j)
\left[1+\frac{\Lambda_m(\mathbf j)}{4r}
+O_{m,\mathbf j}(r^{-2})\right].}\tag{B}
\]

因 Δ>0，对每个固定 m、固定列组存在依赖该列组的阈值，此后所有奇数 r 的此项子式严格正；这**并不**表示半无限矩阵在给定 r 下具有任意阶全矩阵 PF 性质。

证明：每行乘 r^i/C_r，每列乘 j_v!/r^{j_v}，形成
\[
M_{i,v}=(j_v)_{\underline i}E_{j_v-i}(r)
\]
（j_v<i 时两边均为零）。把 a(u)=−u(3u+5)/4，则
\[
M_{i,v}=(j_v)_{\underline i}+
r^{-1}(j_v)_{\underline i}a(j_v-i)+O_{m,\mathbf j}(r^{-2}).
\]
首项为首一阶乘多项式行构成的 Vandermonde 矩阵。关键精确恒等式
\[
(j)_{\underline i}a(j-i)=
a(j)(j)_{\underline i}
+\frac{3i}{2}(j)_{\underline {i+1}}
+\frac{i(3i+5)}4(j)_{\underline i}.
\]
一阶行列式展开中，第一、第三项分别贡献列缩放 Σa(j_v)、行缩放 Σ_i i(3i+5)/4；第二项对 i<m−1 重复已有下一行，仅 i=m−1 存活。因为
\[
\frac{\det[1,(j)_{\underline1},\ldots,(j)_{\underline{m-2}},(j)_{\underline m}]}
{\Delta(\mathbf j)}
=\sum_vj_v-\frac{m(m-1)}2,
\]
于是总一阶相对系数为
\[
\sum_v a(j_v)+\sum_{i=0}^{m-1}\frac{i(3i+5)}4+
\frac{3(m-1)}2\left(\sum_vj_v-\frac{m(m-1)}2\right)
=\frac{\Lambda_m(\mathbf j)}4.
\]
恢复正缩放得到 (B)。证毕。

特别地，对 m=3，相对一阶项等于
\[
-\frac{3(j_0^2+j_1^2+j_2^2)-7(j_0+j_1+j_2)+6}{4r}.
\]
这是 R448 粗误差尚未揭示的 Vandermonde 因子级别结构性相消，但仍不足以推断 j/r∈[0,α] 的一致 PF₃ 正性。

## 执行核验与界限

R449_VERIFY.py 以 SymPy 在未定元 h 上严格核对两个展开系数；独立用直接有理函数做 h=0…7 的 8 次 Laurent 系数核对；原始 signed 卷积与表达式精确核对 36 项；对 m=1…5、列组取自 {0,…,8} 的 381 项做行列式一阶证书交叉核对。全部实际完成，返回 R449_PASS；无浮点判号。计算证据 R449_EVIDENCE.json 与程序均保存在本研究目录。

已复用 R448 的原始 signed BRC 概率表示及 R441 的 Toeplitz 路径。最近学术背景：Konstanze Rietsch, Totally Positive Toeplitz Matrices: Classical and Modern, ICM 2026 invited lecture, DOI 10.1137/25M1806727，涉及 Edrei–Schoenberg 对全非负 Toeplitz 的经典分类；这一外部综述不等于本辅助模型已经满足 Edrei 条件。

固定输入：GLOBAL_KNOWLEDGE_V1 main@30ddf9f5a752c7e9d88d4569fffc6f61bddc3d1d，Enterprise Math main@9c7b0f5cdb347c8651e94463387cab95fb031273，接续 PR #1708 的 R448 commit@442b4d764eea38e400982ba9e282925d56feec78。原生 read-only DIRECTED_RESEARCH 的 authority_granted=false；Owner 查询 CONTROL_QUOTA。没有正式 CLAIM/Result/Driver Review；登记待处理，作者侧结论不等于接纳。

## 下一最小问题

对增长的 h 提供明确统一余项（例如在 r≥K h² 内证明 |E_h−1−a(h)/r−b(h)/r²|≤C h⁶/r³，如常数和量词确实成立），再利用除差、离散差分或 Schur 子式结构控制 det M / Δ 的**一致**剩余项，争取超过 R448 的 L=O(r^{1/5}) 窗口；保留尝试构造增长窗口外三阶负子式的反例路径。