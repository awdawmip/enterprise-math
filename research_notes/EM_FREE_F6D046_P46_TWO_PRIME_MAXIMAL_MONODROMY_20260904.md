# \(P_{46}\) 的双素数最大 Frobenius 环面与全 \(\ell\) 直接单值闭合

Status: `FREE_RESEARCH / DIRECT TWO-PRIME MONODROMY CERTIFICATE / SUPERSEDES L-INDEPENDENCE STEP / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units:

- `EM-FREE-F6D046-R25B-P17-MAXIMAL-FROBENIUS-TORUS`
- `EM-FREE-F6D046-R26B-TWO-PRIME-ALL-ELL-MONODROMY`

## 1. 目的与强化

R25 已用 \(p=29\) 的 \(S_4\)-四次 Frobenius 因子证明

\[
\dim T_{29}=5,
\]

并据此得到 \(\ell\ne29\) 时的完整连通单值群。原写法对 \(\ell=29\) 使用 Larsen--Pink 的 rank \(\ell\)-独立性。

本文件给出第二个完全显式的最大环面证书：

\[
\boxed{\dim T_{17}=5.}
\]

因此可以直接选择

\[
q(\ell)=
\begin{cases}
29,&\ell\ne29,\\
17,&\ell=29,
\end{cases}
\]

并在每个 \(\ell\) 上使用一个与 \(\ell\) 不同的 good Frobenius prime。于是

\[
\boxed{
G_\ell^\circ=\operatorname{GU}_{\mathbf Q(i)}(V,h)_{\mathbf Q_\ell}
\quad\text{对每个 }\ell
}
\]

由两个显式有限证书直接推出，不再依赖 rank 的 \(\ell\)-独立性。

这不否定 Larsen--Pink 定理；只是在本对象上把它从必要证明依赖降为外部一致性检查。

## 2. \(p=17\) 的 Frobenius 数据

R22 已精确重算

\[
\begin{aligned}
f_{17}(X)=\;&X^8+12X^7+48X^6-36X^5-814X^4\\
&-612X^3+13872X^2+58956X+83521.
\end{aligned}
\]

在 \(K=\mathbf Q(i)\) 上，

\[
f_{17}=g_{17}\bar g_{17},
\]

其中

\[
\boxed{
\begin{aligned}
g_{17}(X)=\;&X^4+(6+2i)X^3+(4+16i)X^2\\
&+(-74+78i)X-255+136i.
\end{aligned}}
\]

R22 的 Rabin 证书表明 \(g_{17}\bmod(5,i-2)\) 是不可约四次式，故 \(g_{17}\) 在 \(K[X]\) 上不可约。

其 cubic resolvent 精确分解为

\[
\begin{aligned}
R_{17}(Y)
={}&(Y+4+16i)\\
&\cdot\bigl(Y^2+(-8-32i)Y-60+32i\bigr).
\end{aligned}
\]

二次因子的判别式为

\[
-720+384i.
\]

在 Gaussian prime ideal \((5,i-2)\) 处，它约化为 \(3\in\mathbf F_5\)，是非平方。故二次因子在 \(K\) 上不可约。

因此 \(g_{17}\) 的传递 Galois 群是

\[
\boxed{C_4\ \text{或}\ D_4.}
\]

对本轮的关系格判定不需要进一步区分这两个群。

## 3. \(C_4/D_4\) 置换模的三个不可约分量

把四个根按 Galois 群保持的方形/四循环结构标记为

\[
\beta_1,\beta_2,\beta_3,\beta_4.
\]

定义

\[
\delta_j=\frac{\beta_j^2}{17}.
\]

模挠乘法关系格

\[
\mathcal R_{17}
=
\left\{n\in\mathbf Z^4:
\prod_j\delta_j^{n_j}\text{ 是单位根}
\right\}
\]

的有理化是 \(C_4/D_4\)-置换模 \(\mathbf Q^4\) 的子模。

无论群是 \(C_4\) 还是 \(D_4\)，都有无重分解

\[
\mathbf Q^4
=
\mathbf Q\mathbf1
\oplus
\mathbf Q\varepsilon
\oplus
W_2,
\]

其中

\[
\mathbf1=(1,1,1,1),
\qquad
\varepsilon=(1,-1,1,-1),
\]

而

\[
W_2=\langle(1,0,-1,0),(0,1,0,-1)\rangle_{\mathbf Q}
\]

是二维不可约旋转分量。因此只需逐块排除。

## 4. 排除二维分量 \(W_2\)

若 \(W_2\subseteq\mathcal R_{17}\otimes\mathbf Q\)，则存在正整数 \(N\) 使

\[
N(1,0,-1,0)\in\mathcal R_{17}.
\]

于是

\[
\left(\frac{\delta_1}{\delta_3}\right)^N
=
\left(\frac{\beta_1}{\beta_3}\right)^{2N}
\]

为单位根，故 \(\beta_1/\beta_3\) 本身为单位根。

这与 R22 在 \(p=17\) 上对全部

\[
\{2\le m\le8192:\varphi(m)\le64\}
\]

共 \(126\) 个可能阶的逐项 squarefree-powered-polynomial 证书矛盾。因此

\[
W_2\not\subseteq\mathcal R_{17}\otimes\mathbf Q.
\]

## 5. 排除分块符号分量 \(\mathbf Q\varepsilon\)

resolvent 的 \(K\)-有理根

\[
S=-4-16i
\]

对应 Galois 保持的二二分块。令两个块内根乘积为 \(r,s\)，则

\[
r+s=S,
\qquad
rs=d,
\qquad
d=-255+136i.
\]

符号向量 \(\varepsilon\) 对应的归一化乘积比为

\[
\frac{\delta_1\delta_3}{\delta_2\delta_4}
=
\left(\frac r s\right)^2.
\]

根标记变化只会取逆。令 \(z=r/s\)。由 \(r+s=S,rs=d\) 得

\[
z+z^{-1}
=
\frac{r^2+s^2}{rs}
=
\frac{S^2-2d}{d}
=
-\frac{18}{17}.
\]

若 \(z\) 是单位根，则 \(z+z^{-1}\) 是代数整数；但它是非整数有理数 \(-18/17\)，矛盾。因此 \(z\) 不是单位根，\(z^2\) 也不是单位根。故

\[
\mathbf Q\varepsilon
\not\subseteq
\mathcal R_{17}\otimes\mathbf Q.
\]

## 6. 排除平凡分量

有

\[
\prod_{j=1}^4\delta_j
=
\left(\frac d{17^2}\right)^2,
\qquad
d=-255+136i,
\]

并且

\[
d\bar d=255^2+136^2=17^4.
\]

令

\[
u_{17}=\frac{-255+136i}{289}\in\mathbf Q(i).
\]

虽然 \(u_{17}\bar u_{17}=1\)，但 \(u_{17}\) 不属于

\[
\mu(\mathbf Q(i))=\{\pm1,\pm i\}.
\]

故它不是单位根，\(u_{17}^2\) 也不是单位根。因此

\[
\mathbf Q\mathbf1
\not\subseteq
\mathcal R_{17}\otimes\mathbf Q.
\]

## 7. 最大 angle rank 与最大 Frobenius 环面

三个不可约分量均被排除，所以

\[
\boxed{\mathcal R_{17}=0.}
\]

从而

\[
\boxed{
\operatorname{angle\ rank}(P_{46,17})=4.
}
\]

与 R25 对 \(p=29\) 的结论相同，加入 weight generator \(17\) 后，本征值乘法群的无挠秩为

\[
1+4=5.
\]

因此

\[
\boxed{\dim T_{17}=5.}
\]

这等于

\[
\operatorname{rank}
\operatorname{GU}_{K}(V,h)=5,
\]

所以 \(T_{17}\) 也是 Lefschetz group 中的最大环面。

## 8. 对每个 \(\ell\) 的直接证明

令

\[
L=\operatorname{GU}_{K}(V,h),
\qquad
G_\ell^\circ\subseteq L_{\mathbf Q_\ell}
\]

为连通 \(\ell\)-adic 单值群。

对给定 \(\ell\)：

- 若 \(\ell\ne29\)，取 \(p=29\)；
- 若 \(\ell=29\)，取 \(p=17\)。

所选 \(p\ne\ell\)，故对应 good Frobenius 元是 \(\ell\)-adic 表示中的半单元素。把基域作有限扩张以定义全部几何端同态并使单值群连通时，Frobenius 只被替换为一个正整数次幂；其连通 Zariski 环面仍为原最大环面。

所以对每个 \(\ell\)，

\[
\operatorname{rank}G_\ell^\circ=5.
\]

Faltings endomorphism theorem 给出

\[
\operatorname{End}_{G_\ell^\circ}(V_\ell)
=K\otimes\mathbf Q_\ell.
\]

在代数闭包上

\[
L\simeq GL_4\times G_m,
\qquad
V=W\oplus W^\vee.
\]

因此 \(G_\ell^\circ\) 在 \(W\) 上的像有标量 commutant。投影核至多一维，而总 rank 为五，故该像是 rank 四的连通 reductive 子群。R25 的四维最大秩子群引理给出该像为 \(GL_4\)；投影核同时必须是整个 \(G_m\)。于是

\[
\boxed{
G_\ell^\circ=L_{\mathbf Q_\ell}
\quad\text{对所有 }\ell.
}
\]

这直接重证 R26 的 all-\(\ell\) 结论，并使后续

\[
\operatorname{MT}(P_{46})=L,
\]

所有自积上的 Hodge/Tate 结论，以及完整 Sato--Tate 分量计算，不再依赖 Larsen--Pink。

## 9. 更正与边界

本文件是证明依赖的强化，而非对 R25/R26 定理结论的否定：

\[
\texttt{R25/R26 CONCLUSIONS PRESERVED};
\]

\[
\texttt{LARSEN--PINK DEPENDENCY REMOVED BY TWO-PRIME DIRECT COVER}.
\]

本文件不：

- 声称 \(p=17\) 的 quartic Galois 群必须是 \(C_4\) 或 \(D_4\) 中的某一个具体群；
- 用单个 pairwise ratio 检查替代三个不可约分量的完整排除；
- 证明解析 Sato--Tate 等分布；
- 改动 P000 或公理门分类。

分类：

`DERIVED_TWO_PRIME_MAXIMAL_TORUS_CERTIFICATE / ALL_ELL_DIRECT_MONODROMY / PROOF_DEPENDENCY_STRENGTHENING / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`。
