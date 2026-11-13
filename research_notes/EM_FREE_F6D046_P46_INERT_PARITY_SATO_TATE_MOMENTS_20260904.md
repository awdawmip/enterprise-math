# \(P_{46}\) 的惰性素数偶多项式定理与 Sato--Tate 矩

Status: `FREE_RESEARCH / DERIVED ARITHMETIC-COMPONENT CONSEQUENCE / EXACT MOMENT FORMULA / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units:

- `EM-FREE-F6D046-R34-P46-INERT-FROBENIUS-PARITY`
- `EM-FREE-F6D046-R35-P46-ODD-DEGREE-POINT-COUNT-EQUALITY`
- `EM-FREE-F6D046-R36-P46-SATO-TATE-TRACE-MOMENTS`

## 1. 输入与结果

沿用

\[
K_e(P_{46})=\mathbf Q(i),
\qquad
\operatorname{ST}_{\mathbf Q}(P_{46})
\simeq U(4)\rtimes C_2,
\]

其中非平凡分量按复共轭作用于 \(i\)-端同态。

本轮得到一个对所有好素数的精确分量判据：

\[
\boxed{
p\equiv3\pmod4
\Longrightarrow
f_p(X)=f_p(-X).
}
\]

因此每个惰性好素数的 Frobenius 多项式都是偶多项式，所有奇次 Frobenius 幂迹为零，而且

\[
\boxed{
\#C_{46}(\mathbf F_{p^{2m+1}})
=
\#E(\mathbf F_{p^{2m+1}})
\quad(m\ge0).
}
\]

进一步，R15 所用的单位根比值绝对单纯证书在每个惰性素数都必于阶二失败；若该约化同时 ordinary 且 simple，则可进一步推出它不是绝对单纯。对非 ordinary 约化，偶性本身不作这一结论。

在群论的 Haar 预测层，normalized trace 的 Sato--Tate 测度含有质量恰为 \(1/2\) 的零原子；其全部偶矩有闭式分拆公式。

## 2. Frobenius 与 \(I\) 的反交换

令 \(I\in\operatorname{End}_{\overline{\mathbf Q}}(P_{46})\) 是 \(i\) 的作用，满足

\[
I^2=-1.
\]

对不除 \(6\) 的好素数 \(p\)，若

\[
p\equiv3\pmod4,
\]

则 \(p\) 在 \(K=\mathbf Q(i)\) 中惰性，算术 Frobenius 在

\[
\operatorname{Gal}(K/\mathbf Q)\simeq C_2
\]

中的像为复共轭。因此在 Tate 模上

\[
F_p I F_p^{-1}=-I,
\]

即

\[
F_pI=-IF_p.
\]

在含有 \(i\) 的系数域上分解

\[
V_\ell=V_i\oplus V_{-i}.
\]

反交换关系说明

\[
F_p(V_i)=V_{-i},
\qquad
F_p(V_{-i})=V_i.
\]

所以相对于该分解，

\[
F_p=
\begin{pmatrix}
0&A\\B&0
\end{pmatrix}.
\]

## 3. 偶 Frobenius 多项式

由块矩阵公式，

\[
\det(X-F_p)
=
\det(X^2-AB).
\]

因此

\[
\boxed{f_p(X)=f_p(-X).}
\]

等价地，若 \(\alpha\) 是 Frobenius 本征值，则 \(-\alpha\) 也是同重数本征值。于是所有奇次幂迹都消失：

\[
\boxed{
\operatorname{Tr}(F_p^{2m+1}\mid V_\ell)=0
\quad(m\ge0).
}
\]

## 4. 奇次扩域点数恒等式

由 Jacobian/Prym 分解

\[
J(C_{46})\sim E\times P_{46},
\]

局部 \(L\)-多项式满足

\[
L(P_{46,p},T)
=
\frac{L(C_{46,p},T)}{L(E_p,T)}.
\]

因此对每个 \(n\ge1\)，

\[
s_n(P_{46,p})
=
\#E(\mathbf F_{p^n})
-
\#C_{46}(\mathbf F_{p^n}).
\]

代入奇次迹消失即得

\[
\boxed{
\#C_{46}(\mathbf F_{p^{2m+1}})
=
\#E(\mathbf F_{p^{2m+1}}).
}
\]

这给出一个无需构造点之间显式双射的全体奇次扩域点数恒等式。

## 5. 惰性素数上的绝对单纯证书阻碍

特征不为二时，\(\alpha\ne-\alpha\)，但

\[
\alpha^2=(-\alpha)^2.
\]

所以在 \(\mathbf F_{p^2}\) 上，Frobenius 本征值发生成对碰撞；其 powered characteristic polynomial 是一个四次多项式的平方。由此可以无条件推出：R15 所采用的“不同 Frobenius 根之比不是单位根”的绝对单纯**充分证书**，在每个惰性好素数都必于 \(m=2\) 失败：

\[
\boxed{
p\equiv3\pmod4
\Longrightarrow
\text{R15 root-ratio certificate fails at }m=2.
}
\]

这里必须保留 Honda--Tate 边界：powered polynomial 出现平方，并不在所有 Newton 类型下自动推出原约化在代数闭包上非单纯；超奇异椭圆曲线已经表明“扩域后特征多项式有重因子”不能脱离端同态除代数指数直接使用。若惰性约化同时是 ordinary 且在基域上 simple，则标准 ordinary simple 判据才进一步给出非绝对单纯。对非 ordinary 约化，需要单独计算 Honda--Tate division index。

这精确解释了 \(p=7\) 的已验证现象：

\[
f_7(X)=X^8+5X^6+245X^2+2401
\]

是偶多项式，根比值 \(-1\) 在 \(m=2\) 处立即击穿 R15 证书。它说明为何 \(p=7\) 不能承担此前的绝对单纯证书，而不单独决定 \(P_{46,7}\) 的真实 Honda--Tate 分解。后续采用 split primes \(17,29\)，是为了得到可闭合的 ordinary 绝对单纯与端同态场证书。

## 6. split 与 inert 分量

除去有限多个坏素数后，component map 正是

\[
\operatorname{Frob}_p
\longmapsto
\left(\frac{-1}{p}\right)
\in C_2.
\]

因此：

\[
p\equiv1\pmod4
\Longleftrightarrow
\operatorname{Frob}_p\in\operatorname{ST}^\circ,
\]

\[
p\equiv3\pmod4
\Longleftrightarrow
\operatorname{Frob}_p\in
\operatorname{ST}\setminus\operatorname{ST}^\circ.
\]

两类素数各有自然密度 \(1/2\)。所以 normalized trace 为零的好素数集合无条件包含一个密度 \(1/2\) 的子集。这里不排除少量或稀疏的 split primes 也偶然具有零迹。

## 7. 紧群上 trace 的分量公式

在标准紧模型中，恒等分量为

\[
\iota(U)=
\begin{pmatrix}
U&0\\0&\bar U
\end{pmatrix},
\qquad U\in U(4).
\]

其八维实辛表示的 trace 是

\[
T(U)=\operatorname{Tr}(U)+\overline{\operatorname{Tr}(U)}
=2\operatorname{Re}\operatorname{Tr}(U).
\]

非平凡分量写成

\[
\iota(U)J
=
\begin{pmatrix}
0&U\\-\bar U&0
\end{pmatrix},
\]

故

\[
\boxed{T(\iota(U)J)=0.}
\]

更强地，令

\[
D=\operatorname{diag}(I_4,-I_4).
\]

则

\[
D\iota(U)JD^{-1}=-\iota(U)J,
\]

所以非平凡分量的每个元素都与其负数共轭，特征多项式必为偶多项式。这正是上一节算术反交换定理的紧群版本。

## 8. Haar trace 测度

完整紧群只有两个等体积分量，所以 Haar trace 推前测度为

\[
\boxed{
\mu_T
=
\frac12\mu_{2\operatorname{Re}\operatorname{Tr}U(4)}
+
\frac12\delta_0.
}
\]

这是一项群论测度恒等式，不以解析 Sato--Tate 等分布为前提。若未来证明该阿贝尔簇的 analytic Sato--Tate conjecture，则素数 trace 的经验分布将收敛到这项测度。

## 9. 全部矩公式

令 \(U\) 按 Haar 测度分布于 \(U(4)\)，并写

\[
Z=\operatorname{Tr}(U).
\]

中心旋转不变性说明在

\[
(Z+\bar Z)^{2k}
\]

的展开中，只有 \(Z^k\bar Z^k\) 项积分不为零。因此

\[
\mathbf E_{U(4)}[T^{2k}]
=
\binom{2k}{k}
\mathbf E_{U(4)}[|\operatorname{Tr}U|^{2k}].
\]

Schur--Weyl 对偶给出

\[
\mathbf E_{U(4)}[|\operatorname{Tr}U|^{2k}]
=
\sum_{\substack{\lambda\vdash k\\\ell(\lambda)\le4}}
(f^\lambda)^2,
\]

其中 \(f^\lambda\) 是形状 \(\lambda\) 的标准 Young tableaux 数，由 hook-length 公式计算。

完整 Sato--Tate 群的非平凡分量 trace 恒为零，所以对 \(k\ge1\)：

\[
\boxed{
M_{2k}
=
\frac12\binom{2k}{k}
\sum_{\substack{\lambda\vdash k\\\ell(\lambda)\le4}}
(f^\lambda)^2,
}
\]

而

\[
M_{2k+1}=0,
\qquad M_0=1.
\]

当 \(1\le k\le4\) 时，所有 \(S_k\) 分拆都至多四行，所以平方和为 \(k!\)。于是

\[
\boxed{
M_{2k}=\frac12\frac{(2k)!}{k!}
\quad(1\le k\le4).
}
\]

前八个非平凡偶矩为

\[
\begin{array}{c|rrrrrrrr}
2k&2&4&6&8&10&12&14&16\\ \hline
M_{2k}&1&6&60&840&14994&320628&7862712&214439940.
\end{array}
\]

继续为

\[
M_{18}=6364552480,
\qquad
M_{20}=202371376064.
\]

## 10. 与现有计算的回归

- \(p=7\equiv3\pmod4\)：已有 Frobenius 多项式完全为偶多项式，符合非平凡分量；
- \(p=17,29\equiv1\pmod4\)：Frobenius 多项式具有非零奇次系数，允许且符合恒等分量；
- \(p=7\) 在 \(m=2\) 处失败，而 \(p=17,29\) 通过完整单位根比值排除，正与惰性／分裂结构一致。

## 11. 边界与分类

本结果没有证明 analytic equidistribution。它证明的是：

1. 所有惰性好素数的精确 Frobenius parity；
2. 所有奇次扩域的精确点数恒等式；
3. 惰性约化上 R15 单位根比值充分证书必于 \(m=2\) 失败，并明确区分 ordinary 与非 ordinary 的 Honda--Tate 边界；
4. 已确定紧群的 Haar trace 测度及矩。

分类：

`DERIVED_INERT_FROBENIUS_PARITY / ODD_DEGREE_POINT_COUNT_IDENTITY / INERT_ROOT_RATIO_CERTIFICATE_OBSTRUCTION / SATO_TATE_HAAR_MOMENTS / NOT_ANALYTIC_EQUIDISTRIBUTION / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`。
