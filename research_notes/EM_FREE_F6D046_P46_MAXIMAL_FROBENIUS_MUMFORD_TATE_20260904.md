# \(P_{46}\) 的最大 Frobenius 环面、全幺正单值群与 Hodge–Tate 闭合

Status: `FREE_RESEARCH / DERIVED ARITHMETIC-HODGE THEOREM / MUMFORD-TATE CLOSED / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units:

- `EM-FREE-F6D046-R25-P46-MAXIMAL-FROBENIUS-TORUS`
- `EM-FREE-F6D046-R26-P46-MUMFORD-TATE-GU31`
- `EM-FREE-F6D046-R27-P46-HODGE-TATE-DIVISOR-GENERATION`

## 1. 输入与结论

沿用已经独立验证的对象

\[
P_{46}=\operatorname{Prym}(C_{46}/E),\qquad \dim P_{46}=4,
\]

以及 R18、R22、R23 的结论：

\[
\operatorname{End}_{\overline{\mathbf Q}}(P_{46})=\mathbf Z[i],
\qquad
\operatorname{End}^0_{\overline{\mathbf Q}}(P_{46})=K:=\mathbf Q(i),
\]

\[
\dim H^{1,0}(P_{46})_i=3,
\qquad
\dim H^{1,0}(P_{46})_{-i}=1,
\]

且 \(P_{46}\) 在 \(\overline{\mathbf Q}\) 上单纯。

令 \(V=H^1(P_{46},\mathbf Q)\)，并固定一个极化。由 Rosati 对合在 \(K\) 上诱导复共轭，\(V\) 上得到一个 signature \((3,1)\) 的 \(K/\mathbf Q\)-Hermitian 形式 \(h\)。定义 rational Lefschetz group

\[
L=\operatorname{Cent}_{\operatorname{GSp}(V)}(K)
   =\operatorname{GU}_K(V,h).
\]

本轮证明：

\[
\boxed{\dim T_{29}=5,}
\]

其中 \(T_{29}\) 是 \(p=29\) Frobenius 元生成的连通代数环面；这是 \(L\) 中可能的最大维数。

进一步，若 \(G_\ell^\circ\) 表示 \(\ell\)-adic Galois 像的连通 Zariski 闭包，则

\[
\boxed{G_\ell^\circ=L_{\mathbf Q_\ell}\quad\text{对每个素数 }\ell.}
\]

因而 Mumford–Tate 猜想在本对象上成立，并且

\[
\boxed{\operatorname{MT}(P_{46})=L=\operatorname{GU}_K(V,h).}
\]

相应 Hodge group 为

\[
\boxed{\operatorname{Hg}(P_{46})=\operatorname{U}_K(V,h),}
\]

其实导出群为 \(\operatorname{SU}_K(V,h)\)，实 signature 为 \(\operatorname{SU}(3,1)\)。

最后，所有有限幂 \(P_{46}^n\) 的 Hodge 类均由除子类生成；所有 \(\ell\)-adic Tate 类也由除子类生成。因此 Hodge 猜想和 Tate 猜想对 \(P_{46}\) 的所有自积成立。

## 2. \(p=29\) 的 Gaussian 四次因子

R23 已给出

\[
\begin{aligned}
f_{29}(X)=\;&X^8+4X^7+148X^5+1298X^4\\
&+4292X^3+97556X+707281.
\end{aligned}
\]

在 \(K=\mathbf Q(i)\) 上，

\[
f_{29}=g\bar g,
\]

其中

\[
\boxed{
\begin{aligned}
g(X)=\;&X^4+(2+6i)X^3+(-20-8i)X^2\\
&+(162-86i)X+(609+580i).
\end{aligned}}
\]

记其根为 \(\beta_1,\ldots,\beta_4\)，并令

\[
d=\prod_{j=1}^4\beta_j=609+580i.
\]

有精确恒等式

\[
d\bar d=609^2+580^2=29^4.
\]

而且 reciprocal pairing 为

\[
\boxed{
\bar g(X)=\frac{X^4}{d}g\!\left(\frac{29}{X}\right).
}
\]

所以 \(f_{29}\) 的八个根恰为

\[
\beta_1,\ldots,\beta_4,
\frac{29}{\beta_1},\ldots,\frac{29}{\beta_4}.
\]

## 3. \(g\) 的 Galois 群是 \(S_4\)

R23 已用 prime ideal \((101,i-10)\) 的 Rabin 证书证明 \(g\) 在 \(K[X]\) 上不可约。

其 cubic resolvent 为

\[
\boxed{
\begin{aligned}
R_g(Y)=\;&Y^3+(20+8i)Y^2\\
&+(-1596-1520i)Y-15600-34080i.
\end{aligned}}
\]

R23 又给出 \((17,i-4)\) 处的不可约三次 Rabin 证书。因此 quartic Galois 群只能是 \(A_4\) 或 \(S_4\)。

直接计算判别式：

\[
\Delta_g=-26583701760+30788326400i.
\]

在 Gaussian prime ideal

\[
(13,i-5)
\]

处，

\[
\Delta_g\equiv8\pmod{13}.
\]

而

\[
8^6\equiv-1\pmod{13},
\]

故 \(8\) 是 \(\mathbf F_{13}\) 中的非平方。若 \(\Delta_g\) 在 \(K\) 中为平方，它在这个非分歧且非零的剩余类中也必须为平方，矛盾。因此

\[
\boxed{\Delta_g\notin K^{\times2}}
\]

并得到

\[
\boxed{\operatorname{Gal}(g/K)\simeq S_4.}
\]

## 4. 归一化 Frobenius 角的乘法独立性

定义

\[
\delta_j=\frac{\beta_j^2}{29},
\qquad j=1,\ldots,4.
\]

每个 \(\delta_j\) 的所有复绝对值均为 \(1\)。考虑模挠乘法关系格

\[
\mathcal R=
\left\{
(n_1,\ldots,n_4)\in\mathbf Z^4:
\prod_{j=1}^4\delta_j^{n_j}
\text{ 是单位根}
\right\}.
\]

由于 \(\operatorname{Gal}(g/K)=S_4\) 任意置换 \(\beta_j\)，\(\mathcal R\otimes\mathbf Q\) 是置换表示 \(\mathbf Q^4\) 的 \(S_4\)-子模。该表示分解为

\[
\mathbf Q^4=\mathbf Q\mathbf 1\oplus V_{\mathrm{std}},
\]

其中

\[
\mathbf1=(1,1,1,1),
\qquad
V_{\mathrm{std}}=\left\{(x_j):\sum x_j=0\right\}
\]

且 \(V_{\mathrm{std}}\) 在 \(\mathbf Q\) 上不可约。因此只有四种可能：

\[
0,
\quad
\mathbf Q\mathbf1,
\quad
V_{\mathrm{std}},
\quad
\mathbf Q^4.
\]

### 4.1 排除标准子模

若 \(V_{\mathrm{std}}\subseteq\mathcal R\otimes\mathbf Q\)，则对任意 \(j\ne k\)，存在 \(N>0\) 使

\[
N(e_j-e_k)\in\mathcal R.
\]

于是

\[
\left(\frac{\delta_j}{\delta_k}\right)^N
=
\left(\frac{\beta_j}{\beta_k}\right)^{2N}
\]

是单位根，从而 \(\beta_j/\beta_k\) 是单位根。这与 R23 已通过全部 \(126\) 个可能阶逐项排除的证书矛盾。

故 \(\mathcal R\otimes\mathbf Q\) 不含 \(V_{\mathrm{std}}\)。

### 4.2 排除平凡子模

有

\[
\prod_{j=1}^4\delta_j
=
\frac{d^2}{29^4}
=
\left(\frac{609+580i}{841}\right)^2.
\]

令

\[
u=\frac{609+580i}{841}\in\mathbf Q(i).
\]

虽然 \(u\bar u=1\)，但 \(\mathbf Q(i)\) 中的单位根仅为

\[
\{1,-1,i,-i\},
\]

而 \(u\) 不等于其中任何一个。因此 \(u\) 不是单位根，\(u^2\) 也不是单位根。

故 \(\mathbf Q\mathbf1\) 也不能包含于 \(\mathcal R\otimes\mathbf Q\)。

综上，

\[
\boxed{\mathcal R=0.}
\]

也就是说，四个归一化角 \(\delta_1,\ldots,\delta_4\) 在模挠意义下乘法独立：

\[
\boxed{\operatorname{angle\ rank}(P_{46,29})=4.}
\]

这是四维阿贝尔簇所允许的最大 angle rank。

## 5. Frobenius 环面维数为 \(5\)

设 \(\Gamma\) 是由 \(29,\beta_1,\ldots,\beta_4\) 在 \(\overline{\mathbf Q}^{\times=\) 中生成的群，模去挠元。

若

\[
29^a\prod_{j=1}^4\beta_j^{b_j}
\]

为单位根，则取任一复绝对值给出

\[
2a+\sum_{j=1}^4b_j=0.
\]

将关系平方并使用 \(\beta_j^2=29\delta_j\)，得到

\[
\prod_{j=1}^4\delta_j^{b_j}
\]

为单位根。由 \(\mathcal R=0\)，所有 \(b_j=0\)，进而 \(a=0\)。因此

\[
\operatorname{rank}\Gamma=5.
\]

半单 Frobenius 元的连通 Zariski 闭包维数正是其本征值乘法群的无挠秩，所以

\[
\boxed{\dim T_{29}=5.}
\]

另一方面，对四维 \(K\)-Hermitian 空间，

\[
L_{\overline{\mathbf Q}}
\simeq
\operatorname{GL}_4\times\mathbf G_m,
\]

其中 \((g,\mu)\) 在共轭分量上按

\[
\mu(g^{-1})^{\mathsf t}
\]

作用。因此

\[
\operatorname{rank}L=4+1=5.
\]

故 \(T_{29}\) 是 \(L\) 中的最大环面。

## 6. 一个四维最大秩子群引理

### 引理

设 \(k\) 是特征零代数闭域，\(H\subseteq\operatorname{GL}(W)\) 是连通 reductive 子群，\(\dim W=4\)。若

1. \(\operatorname{rank}H=4\)；
2. \(\operatorname{End}_H(W)=k\)，

则

\[
\boxed{H=\operatorname{GL}(W).}
\]

### 证明

由第二条和完全可约性，\(W\) 是 \(H\) 的不可约表示。Schur 引理说明连通中心 \(Z(H)^\circ\) 只能通过标量作用，故其有效维数至多为 \(1\)。于是

\[
\operatorname{rank}H^{\mathrm{der}}\ge3.
\]

能在四维空间上忠实不可约作用的半单 Lie 类型只有：

- \(A_1\)：四维对称三次表示，rank \(1\)；
- \(A_1\times A_1\)：\(2\otimes2\)，rank \(2\)；
- \(C_2\)：标准四维表示，rank \(2\)；
- \(A_3\)：标准或对偶四维表示，rank \(3\)。

半单 rank 至少 \(3\) 因而只可能是 \(A_3\)，其像包含 \(\operatorname{SL}(W)\)。总 rank 为 \(4\) 又迫使存在一维标量中心，所以 \(H\) 同时包含 \(\operatorname{SL}(W)\) 与全部标量，故 \(H=\operatorname{GL}(W)\)。证毕。

## 7. \(\ell\)-adic 单值群等于完整幺正 similitude 群

先取 \(\ell=5\)。由于 \(5\) 在 \(K=\mathbf Q(i)\) 中分裂，

\[
V_5=W\oplus W^{\vee},
\qquad
L_{\mathbf Q_5}\simeq
\operatorname{GL}(W)\times\mathbf G_m.
\]

把基域作有限扩张，使所有几何端同态均定义且 \(5\)-adic 单值群连通；这不改变其连通分量。Faltings 的半单性与 endomorphism theorem 给出

\[
\operatorname{End}_{G_5^\circ}(V_5)
=K\otimes\mathbf Q_5.
\]

所以投影到 \(W\) 的表示具有标量 commutant，因而绝对不可约。

在基域扩张后的任一 \(29\) 上方好素点，Frobenius 本征值只是上述本征值的同一正整数次幂；乘法秩仍为 \(5\)。因此

\[
\operatorname{rank}G_5^\circ\ge5.
\]

而

\[
G_5^\circ\subseteq L_{\mathbf Q_5},
\qquad
\operatorname{rank}L=5,
\]

故 rank 恰为 \(5\)。

在代数闭包上，设 \(H\) 是 \(G_5^\circ\) 到 \(\operatorname{GL}(W)\) 的像。投影核位于额外的 \(\mathbf G_m\) 中，rank 至多 \(1\)，所以

\[
\operatorname{rank}H=4.
\]

其 commutant 为标量，应用上一引理得

\[
H=\operatorname{GL}(W).
\]

投影核因总引 rank 为 \(5\) 而是一维，故等于整个额外 \(\mathbf G_m\)。于是

\[
\boxed{G_5^\circ=L_{\mathbf Q_5}.}
\]

完全相同的 \(p=29\) Frobenius 环面论证适用于每个 \(\ell\ne29\)，所以

\[
G_\ell^\circ=L_{\mathbf Q_\ell}
\qquad(\ell\ne29).
\]

对于 \(\ell=29\)，使用 Larsen–Pink 对来自阿贝尔簇的严格相容半单系统之 algebraic monodromy rank 的 \(\ell\)-独立性：

\[
\operatorname{rank}G_{29}^\circ
=
\operatorname{rank}G_5^\circ
=5.
\]

再应用同一 commutant 与四维子群引理，得到

\[
G_{29}^\circ=L_{\mathbf Q_{29}}.
\]

因此最终为

\[
\boxed{
G_\ell^\circ
=
\operatorname{GU}_K(V,h)_{\mathbf Q_\ell}
\quad\text{对所有 }\ell.
}
\]

## 8. Mumford–Tate 群

极化和 \(K\)-端同态都是 Hodge tensors，故

\[
\operatorname{MT}(P_{46})\subseteq L.
\]

Deligne 关于阿贝尔簇 Hodge cycles 为 absolute Hodge cycles 的定理给出已知方向

\[
G_\ell^\circ
\subseteq
\operatorname{MT}(P_{46})_{\mathbf Q_\ell}.
\]

取 \(\ell=5\)，结合上一节的等式：

\[
L_{\mathbf Q_5}
=G_5^\circ
\subseteq
\operatorname{MT}(P_{46})_{\mathbf Q_5}
\subseteq
L_{\mathbf Q_5}.
\]

所以

\[
\boxed{
\operatorname{MT}(P_{46})=L=
\operatorname{GU}_K(V,h).
}
\]

并且所有 \(\ell\) 上都有

\[
G_\ell^\circ=
\operatorname{MT}(P_{46})_{\mathbf Q_\ell}.
\]

这正是该对象的 Mumford–Tate 猜想。

## 9. 所有自积上的 Hodge 类由除子生成

Hodge group 是 Mumford–Tate 群在 weight similitude 上的连通核。因此

\[
\operatorname{Hg}(P_{46})
=
\operatorname{U}_K(V,h).
\]

在 \(\mathbf C\) 上，

\[
V_{\mathbf C}=W\oplus W^\vee,
\qquad
\operatorname{Hg}(P_{46})_{\mathbf C}
\simeq\operatorname{GL}(W).
\]

\(\operatorname{GL}(W)\) 的第一不变量定理说明，任意由若干份 \(W\) 与 \(W^\vee\) 构成的 tensor algebra 中，不变量由基本收缩

\[
W\otimes W^\vee\longrightarrow\mathbf C
\]

生成。限制到

\[
H^*(P_{46}^n,\mathbf Q)
=
\bigwedge{}^*H^1(P_{46}^n,\mathbf Q)
\]

后，这些收缩正是极化与 \(K\)-endomorphism 所产生的 degree-\(2\) Hodge 类，也就是自积上的除子类。

故对每个 \(n\ge1\)：

\[
\boxed{
\operatorname{Hdg}^*(P_{46}^n)
\text{ 由除子类生成}.}
\]

特别地，Hodge 猜想对所有 \(P_{46}^n\) 成立。

这也解释为什么 signature \((3,1)\) 不产生 Weil-type 的异常中间维 Hodge 类：

\[
\bigwedge_K^4H^1
\]

的 Hodge 类型为 \((3,1)\oplus(1,3)\)，而且在
\(\operatorname{GL}(W)\) 中按 determinant character 变换，不是不变量。

## 10. Tate 类

由所有 \(\ell\) 上的

\[
G_\ell^\circ=L_{\mathbf Q_\ell}
\]

以及同一个 \(\operatorname{GL}_4\) 不变量论证，任一有限扩域后出现的 \(\ell\)-adic Tate 类也由 degree-\(2\) Tate 类生成。Faltings 的 isogeny theorem 识别这些 degree-\(2\) 类为极化和 endomorphism 对应的代数除子类。

因此：

\[
\boxed{
\text{Tate 猜想对所有 }P_{46}^n
\text{ 和所有 }\ell\text{ 成立}.}
\]

## 11. Sato–Tate 连通分量

这里必须区分两个不同的“最大紧子群”操作。Hodge group 的实点为

\[
\operatorname{Hg}(P_{46})(\mathbf R)=U(3,1),
\]

其最大紧子群 \(U(3)\times U(1)\) 描述 Hermitian 对称域的实微分几何；它**不是** Sato–Tate 连通分量。

Sato–Tate 连通分量按定义取代数 Hodge group 复点

\[
\operatorname{Hg}(P_{46})(\mathbf C)
\simeq GL_4(\mathbf C)
\]

的最大紧子群。因此正确结论是

\[
\boxed{
\operatorname{ST}(P_{46})^\circ
\simeq U(4).
}
\]

signature \((3,1)\) 决定实 Hodge 域和 PEL 模空间，但代数群复化后成为 \(GL_4\)，所以不会把 Sato–Tate 紧群切成 \(U(3)\times U(1)\)。

这里仅确定连通分量。由于 \(i\)-endomorphism 在 \(\mathbf Q(i)\) 上定义，完整 component group 还需要单独核验 arithmetic descent；本文件不把它自动写成 \(C_2\)。

## 12. 方法复用与边界

本轮复用：

- R23 的 \(p=29\) 完整 root-ratio certificate：`REUSE_APPLIED`；
- R23 的 \(K\)-quartic 与 resolvent Rabin 证书：`REUSE_APPLIED`；
- R18 的 \(K\)-action 与 signature \((3,1)\)：`REUSE_APPLIED`；
- 有限对称／轨道分解思想：与 `T7_FINITE_SYMMETRY_EQUIVARIANCE` 相容，但这里不建立新工具；
- Frobenius relation lattice 属 arithmetic domain certificate，而非新的全局工具族。

Method harvest：

`DERIVED_THEOREM / DOMAIN_CERTIFICATE / NO_NEW_GLOBAL_TOOL`。

本结果没有：

- 改动 P000；
- 把 Prym 模型提升为基础公理；
- 从单个数值 period matrix 猜测 Mumford–Tate 群；
- 把未完成的 canonical-net 枚举当作证据；
- 声称完整 Sato–Tate component group 已确定。

分类：

\[
\texttt{DERIVED\_FROBENIUS\_TORUS\_THEOREM},
\]

\[
\texttt{MAXIMAL\_ANGLE\_RANK},
\]

\[
\texttt{MUMFORD\_TATE\_GROUP\_GU31},
\]

\[
\texttt{MUMFORD\_TATE\_CONJECTURE\_ALL\_ELL},
\]

\[
\texttt{HODGE\_AND\_TATE\_ALL\_POWERS},
\]

以及

\[
\texttt{NOT\_NEW\_AXIOM / NOT\_FOUNDATION / P000\_UNCHANGED}.
\]

## 13. 参考基础

- P. Deligne, *Hodge cycles on abelian varieties*, in **Hodge Cycles, Motives, and Shimura Varieties**, LNM 900 (1982): 阿贝尔簇 Hodge cycles 的 absolute-Hodge 性。
- G. Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, Invent. Math. 73 (1983): \(\ell\)-adic 半单性与 endomorphism centralizer。
- M. Larsen and R. Pink, *On \(\ell\)-independence of algebraic monodromy groups in compatible systems of representations*, Invent. Math. 107 (1992), 603–636: rank 的 \(\ell\)-独立性。
- E. Howe and H. Zhu, *On the existence of absolutely simple abelian varieties of a given dimension over an arbitrary field*, J. Number Theory 92 (2002): ordinary simple reduction 的绝对单纯判据框架。
