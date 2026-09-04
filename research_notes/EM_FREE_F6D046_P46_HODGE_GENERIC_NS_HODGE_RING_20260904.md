# \(P_{46}\) 的 Hodge-generic 性、Néron--Severi 秩与自积 Hodge 环

Status: `FREE_RESEARCH / DERIVED PEL-AND-INVARIANT-THEORY CONSEQUENCE / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units:

- `EM-FREE-F6D046-R31-P46-HODGE-GENERIC-PEL-POINT`
- `EM-FREE-F6D046-R32-P46-NS-RANK-ALL-POWERS`
- `EM-FREE-F6D046-R33-P46-EXPLICIT-HODGE-NUMBERS-ALL-POWERS`

## 1. 输入与主结论

沿用已闭合结论

\[
\operatorname{End}^0_{\overline{\mathbf Q}}(P_{46})=K=\mathbf Q(i),
\]

\[
\operatorname{MT}(P_{46})=\operatorname{GU}_K(V,h),
\qquad
\operatorname{Hg}(P_{46})=\operatorname{U}_K(V,h),
\]

其中 \(h\) 的 signature 为 \((3,1)\)，且所有自积的 Hodge 类由除子类生成。

本轮得到：

1. \(P_{46}\) 是 signature \((3,1)\) 的 \(\mathbf Z[i]\)-PEL 三维 Shimura 家族中的 Hodge-generic 点；
2. 对每个 \(n\ge1\)，
   \[
   \boxed{\rho(P_{46}^n)=n^2;}
   \]
3. \(P_{46}^n\) 的余维 \(r\) Hodge 类维数为
   \[
   \boxed{
   h_{n,r}
   =
   \sum_{\substack{\lambda\vdash r\\
                    \ell(\lambda)\le4\\
                    \lambda_1\le n}}
   \left(\dim S_{\lambda'}\mathbf C^n\right)^2.
   }
   \]

该公式给出完整的 Hodge-class Hilbert 向量，且与 Poincaré 对偶严格对称：

\[
h_{n,r}=h_{n,4n-r}.
\]

## 2. PEL 家族维数与 Hodge-generic 性

考虑带有下列数据的极化阿贝尔四维簇：

- \(\mathbf Z[i]\)-作用；
- Rosati 对合在 \(\mathbf Q(i)\) 上为复共轭；
- \(H^{1,0}\) 的两个复嵌入重数为 \((3,1)\)；
- 与 \(P_{46}\) 相同的离散极化／level 分量。

对应 Hermitian 对称域为

\[
U(3,1)/(U(3)\times U(1)),
\]

其复维数为

\[
3\cdot1=3.
\]

因此该 PEL 模空间的每个相关连通分量是三维。

generic PEL Hodge group 是完整的

\[
\operatorname{U}_K(V,h),
\]

而 R26 已证明 \(P_{46}\) 的 Hodge group 正好达到这一群。故它没有额外 Hodge tensor 迫使 Mumford--Tate 群落入 proper \(\mathbf Q\)-子群：

\[
\boxed{
P_{46}\text{ 是该 PEL 分量中的 Hodge-generic 点}.
}
\]

精确含义是：其点不落在由额外 Hodge tensors 定义的 proper special Shimura 子簇中。这不声称它在 Zariski 拓扑中是“通用点”，也不排除它落在非 special 的普通代数子簇中。

特别地，\(P_{46}\) 不是 CM 点；其 Mumford--Tate 群非交换，且其几何端同态代数只有二次域 \(\mathbf Q(i)\)，而非四维 CM 阿贝尔簇所需的八次 CM 代数。

## 3. \(P_{46}\) 的 Picard 数为 \(1\)

固定一个极化 \(\lambda\)。经典 Rosati 对应给出

\[
\operatorname{NS}(P_{46})_{\mathbf Q}
\simeq
\operatorname{End}^0(P_{46})^{\dagger=1},
\]

其中 \(\dagger\) 是 \(\lambda\)-Rosati 对合。

在 \(K=\mathbf Q(i)\) 上，正 Rosati 对合只能是复共轭。因此

\[
K^{\dagger=1}=\mathbf Q.
\]

所以

\[
\boxed{
\operatorname{NS}(P_{46})_{\mathbf Q}\simeq\mathbf Q,
\qquad
\rho(P_{46})=1.
}
\]

积分 Néron--Severi 群无挠且秩一，故抽象同构于 \(\mathbf Z\)。本文件不把已有 type \((1,1,1,2)\) 的 Prym 极化自动认定为该格的 primitive generator；这需要额外的积分指数核验。

## 4. 所有自积的 Néron--Severi 秩

对 \(A=P_{46}\)，有

\[
\operatorname{End}^0(A^n)=M_n(K).
\]

选择 product polarization 后，Rosati 对合在适当基下为 conjugate transpose：

\[
M\longmapsto\bar M^{\mathsf t}.
\]

于是

\[
\operatorname{NS}(A^n)_{\mathbf Q}
\simeq
\operatorname{Herm}_n(K)
=
\{M\in M_n(K):M=\bar M^{\mathsf t}\}.
\]

其 \(\mathbf Q\)-维数为

\[
 n+2\binom n2=n^2.
\]

故

\[
\boxed{\rho(P_{46}^n)=n^2.}
\]

更具体地：

- \(n\) 个对角方向来自各因子的极化类；
- 每对不同因子贡献一个 \(K\)-二维的图／Poincaré 交叉方向；
- 合计为 \(n^2\)。

在实系数下

\[
\operatorname{NS}(A^n)_{\mathbf R}
\simeq
\operatorname{Herm}_n(\mathbf C),
\]

且 ample cone 对应正定 Hermitian 矩阵锥。积分 NS 格是相应 Hermitian 整数格的一个有限指数版本；极化 type 会影响该积分指数，但不影响秩和实锥。

## 5. Hodge 类维数的分拆公式

令

\[
W\simeq\mathbf C^4,
\qquad
U\simeq\mathbf C^n.
\]

由

\[
\operatorname{Hg}(P_{46})_{\mathbf C}\simeq GL(W)
\]

以及 \(H^1(A)_{\mathbf C}=W\oplus W^\vee\)，有

\[
H^1(A^n)_{\mathbf C}
=
(W\otimes U)\oplus(W^\vee\otimes U).
\]

中心标量迫使 degree \(2r\) 的不变量恰好从两个直和项各取 \(r\) 次，因此

\[
\operatorname{Hdg}^r(A^n)_{\mathbf C}
\simeq
\left[
\bigwedge^r(W\otimes U)
\otimes
\bigwedge^r(W^\vee\otimes U)
\right]^{GL(W)}.
\]

外幂 Cauchy 公式给出

\[
\bigwedge^r(W\otimes U)
\simeq
\bigoplus_{\substack{\lambda\vdash r\\
\ell(\lambda)\le4\\
\lambda_1\le n}}
S_\lambda W\otimes S_{\lambda'}U.
\]

对偶项具有对应的 \((S_\lambda W)^\vee\)，而 Schur 引理说明只有相同 \(\lambda\) 配对留下一个 \(GL(W)\)-不变量。因此

\[
\operatorname{Hdg}^r(A^n)_{\mathbf C}
\simeq
\bigoplus_{\substack{\lambda\vdash r\\
\ell(\lambda)\le4\\
\lambda_1\le n}}
S_{\lambda'}U\otimes(S_{\lambda'}U)^\vee.
\]

取维数即得

\[
\boxed{
 h_{n,r}
 =
 \sum_{\substack{\lambda\vdash r\\
                  \ell(\lambda)\le4\\
                  \lambda_1\le n}}
 \left(\dim S_{\lambda'}\mathbf C^n\right)^2.
}
\]

其中每个 Schur 模维数由 hook-content/Weyl 公式精确计算。

## 6. 前五个自积的完整 Hodge-class 向量

按余维 \(r=0,1,\ldots,4n\) 排列，得到：

### \(n=1\)

\[
(1,1,1,1,1).
\]

### \(n=2\)

\[
(1,4,10,20,35,20,10,4,1).
\]

### \(n=3\)

\[
(1,9,45,165,495,846,994,846,495,165,45,9,1).
\]

### \(n=4\)

\[
\begin{aligned}
(&1,16,136,816,3876,12368,27608,44912,53382,\\
&44912,27608,12368,3876,816,136,16,1).
\end{aligned}
\]

### \(n=5\)

\[
\begin{aligned}
(&1,25,325,2925,20475,102879,373275,1005075,2035800,\\
&3093100,3550756,3093100,2035800,1005075,373275,102879,\\
&20475,2925,325,25,1).
\end{aligned}
\]

所有向量均满足：

\[
h_{n,0}=h_{n,4n}=1,
\qquad
h_{n,1}=h_{n,4n-1}=n^2,
\]

以及 Poincaré 对偶对称。

## 7. “由除子生成”的定量化

R27 已证明 Hodge 环由余维一类生成。本轮公式进一步给出生成后每个余维实际剩余的线性维数。

因此有一个自然满射

\[
\operatorname{Sym}^*\bigl(\operatorname{NS}(A^n)_{\mathbf Q}\bigr)
\longtwoheadrightarrow
\operatorname{Hdg}^*(A^n),
\]

其中生成空间维数为 \(n^2\)，而目标余维 \(r\) 的维数正是 \(h_{n,r}\)。

例如 \(n=2\) 时有四个除子方向，低余维维数为

\[
1,4,10,20,35,
\]

直到中维正好与四变量次数 \(r\) 齐次多项式维数

\[
\binom{r+3}{3}
\]

一致；高余维的关系由总复维数八和 Poincaré 对偶强制出现。

对一般 \(n\)，分拆条件 \(\ell(\lambda)\le4\) 精确记录了 \(W\) 的 rank 四边界；超过该边界的 Schur 分量就是除子生成代数中的表示论关系来源。

## 8. 边界与分类

本结果没有：

- 把 Hodge-generic 误写成 Zariski generic；
- 声称 \(P_{46}\) 不在任何普通代数子簇中；
- 从 Picard rank 一直接推出特定 Prym 极化是 primitive；
- 忽略 polarization type 对积分 NS 格的影响；
- 把 Hodge-class 维数公式提升为 P000 或 Foundation 原语。

方法复用：

- R26/R27 的完整 Hodge group 与 divisor-generation：`REUSE_APPLIED`；
- classical Rosati--Néron--Severi correspondence：`REUSE_APPLIED_EXTERNAL_THEOREM`；
- \(GL_4\) first invariant theorem 和外幂 Cauchy identity：`REUSE_APPLIED_EXTERNAL_METHOD`；
- 分拆／Schur 维数枚举：专用验证器，`DOMAIN_CERTIFICATE / NO_NEW_GLOBAL_TOOL`。

分类：

`DERIVED_HODGE_GENERIC_THEOREM / NS_RANK_N_SQUARED / EXPLICIT_HODGE_CLASS_HILBERT_FUNCTION / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`。
