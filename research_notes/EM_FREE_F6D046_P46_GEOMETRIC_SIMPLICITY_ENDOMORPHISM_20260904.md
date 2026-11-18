# \(P_{46}\) 的几何单纯性与几何端同态代数

Status: `FREE_RESEARCH / CORRECTION-AWARE DERIVED THEOREM / EXACT FINITE CERTIFICATE / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units:

- `EM-FREE-F6D046-R22-P46-CORRECTED-ABSOLUTE-SIMPLICITY`
- `EM-FREE-F6D046-R23-P46-ASYMMETRIC-ENDOMORPHISM-INTERSECTION`

## 1. 结论

令

\[
E:\ v^2=A(t),\qquad
A(t)=t^4+24t^3+192t^2+528t+144,
\]

并令

\[
C_{46}:\ m^2=-\frac1{288}vD(t),\qquad
D(t)=t^2+12t+24.
\]

记

\[
P_{46}=\operatorname{Prym}(C_{46}/E),\qquad \dim P_{46}=4.
\]

在 R18 已建立的 order-\(4\) deck 作用下，

\[
K=\mathbf Q(i)\subseteq
\operatorname{End}^0_{\overline{\mathbf Q}}(P_{46}).
\]

本轮得到两个经独立有限证书支持的派生定理：

\[
\boxed{P_{46}/\overline{\mathbf Q}\ \text{几何单纯}},
\]

以及

\[
\boxed{
\operatorname{End}^0_{\overline{\mathbf Q}}(P_{46})
=\mathbf Q(i).
}
\]

由于 order-\(4\) deck 作用已经给出
\(\mathbf Z[i]\subseteq\operatorname{End}_{\overline{\mathbf Q}}(P_{46})\)，
而 \(\mathbf Z[i]\) 是 \(\mathbf Q(i)\) 的极大整数环，进一步有

\[
\boxed{
\operatorname{End}_{\overline{\mathbf Q}}(P_{46})
=\mathbf Z[i].
}
\]

这里同时排除了此前尚未关闭的所有额外几何端同态场、非交换几何端同态代数和更大的积分端同态阶。

## 2. 必要勘误：\(p=7\) 不能证明绝对单纯

R14 的 \(p=7\) Frobenius 多项式为

\[
f_7(X)=X^8+5X^6+245X^2+2401.
\]

它是偶多项式：

\[
f_7(-X)=f_7(X),
\qquad
f_7(0)\ne0.
\]

因此任一根 \(\alpha\) 都与不同根 \(-\alpha\) 同时出现，且

\[
\frac{-\alpha}{\alpha}=-1
\]

是二阶单位根。等价地，\(\alpha^2=(-\alpha)^2\)，所以在二次扩域后共轭 Frobenius 根发生碰撞。

故：

\[
\boxed{
p=7\text{ 约化虽在 }\mathbf F_7\text{ 上单纯，
但不是绝对单纯。}
}
\]

R15 若以 \(p=7\) 为输入，其有限证书在首项 \(m=2\) 即失败。该失败不是数值误差，而是精确结构性反例。

## 3. 新的两个 split good primes

曲线模型满足

\[
\operatorname{disc}(A)=-2^{16}3^5,\qquad
\operatorname{disc}(D)=2^4 3,\qquad
\operatorname{Res}(A,D)=-2^8 3^3.
\]

所以 \(17,29\) 都是模型的 good primes；并且

\[
17\equiv29\equiv1\pmod4,
\]

故 \(i\) 在两个剩余域中均可选定。

### 3.1 \(p=17\)

对 \(n=1,2,3,4\) 的精确点数为

\[
\begin{array}{c|rrrr}
n&1&2&3&4\\ \hline
\#E(\mathbf F_{17^n})&14&308&5054&83776\\
\#C_{46}(\mathbf F_{17^n})&26&260&4946&84552\\
s_n(P_{46})&-12&48&108&-776
\end{array}
\]

Newton 恒等式与权一函数方程给出

\[
\begin{aligned}
f_{17}(X)=\;&X^8+12X^7+48X^6-36X^5-814X^4\\
&-612X^3+13872X^2+58956X+83521.
\end{aligned}
\]

中间系数 \(-814\not\equiv0\pmod{17}\)，故约化 ordinary。

### 3.2 \(p=29\)

精确点数为

\[
\begin{array}{c|rrrr}
n&1&2&3&4\\ \hline
\#E(\mathbf F_{29^n})&30&900&24390&705600\\
\#C_{46}(\mathbf F_{29^n})&34&884&24898&708168\\
s_n(P_{46})&-4&16&-508&-2568
\end{array}
\]

相应地，

\[
\begin{aligned}
f_{29}(X)=\;&X^8+4X^7+148X^5+1298X^4\\
&+4292X^3+97556X+707281.
\end{aligned}
\]

中间系数 \(1298\not\equiv0\pmod{29}\)，故该约化也 ordinary。

## 4. 两个多项式在 \(\mathbf Q\) 上不可约

在 \(K=\mathbf Q(i)\) 上有精确分解

\[
f_{17}=g_{17}\overline{g}_{17},
\]

其中

\[
\begin{aligned}
g_{17}(X)=\;&X^4+(6+2i)X^3+(4+16i)X^2\\
&+(-74+78i)X-255+136i,
\end{aligned}
\]

以及

\[
f_{29}=g_{29}\overline{g}_{29},
\]

其中

\[
\begin{aligned}
g_{29}(X)=\;&X^4+(2+6i)X^3+(-20-8i)X^2\\
&+(162-86i)X+609+580i.
\end{aligned}
\]

有限 Rabin 证书给出：

- \(g_{17}\bmod(5,i-2)\) 是 \(\mathbf F_5\) 上不可约四次式；
- \(g_{29}\bmod(101,i-10)\) 是 \(\mathbf F_{101}\) 上不可约四次式。

故二者在 \(K[X]\) 上不可约。

再写 \(g=g_0+ig_1\)。两个实例均满足

\[
\gcd(g_0,g_1)=1\quad\text{于 }\mathbf Q[X].
\]

若 \(\alpha\) 是 \(g\) 的根，则 \(g_1(\alpha)\ne0\)，从而

\[
i=-\frac{g_0(\alpha)}{g_1(\alpha)}
\in\mathbf Q(\alpha).
\]

于是

\[
[\mathbf Q(\alpha):\mathbf Q]
=
[K(\alpha):K][K:\mathbf Q]
=4\cdot2=8.
\]

因此 \(f_{17}\) 与 \(f_{29}\) 都在 \(\mathbf Q[X]\) 上不可约。

## 5. 完整单位根比值排除

设 \(f_p\) 的八个根为 \(\alpha_1,\ldots,\alpha_8\)。若

\[
\alpha_i/\alpha_j=\zeta_m
\]

为单位根，则

\[
\varphi(m)\le
[\mathbf Q(\alpha_i,\alpha_j):\mathbf Q]\le64.
\]

由

\[
\varphi(m)\ge\sqrt{m/2}
\]

可取有限上界 \(m\le8192\)。实际候选集合

\[
\mathcal M=
\{2\le m\le8192:\varphi(m)\le64\}
\]

恰有 \(126\) 个元素，最大值为 \(240\)。

对每个 \(m\in\mathcal M\)，验证器计算

\[
f_{p,m}(Y)=\prod_{j=1}^8(Y-\alpha_j^m)
\]

的模辅助素数版本，并给出一个 \(\ell\ne p\)，使

\[
\gcd(f_{p,m}\bmod\ell,\,
\partial_Y f_{p,m}\bmod\ell)=1.
\]

这证明八个 \(\alpha_j^m\) 在特征零中两两不同。

结果：

\[
\boxed{
p=17:\ 126/126\text{ 个阶全部排除},
}
\]

\[
\boxed{
p=29:\ 126/126\text{ 个阶全部排除}.
}
\]

辅助素数分布为：

\[
p=17:\quad
\ell=11\ (49),\quad
19\ (76),\quad
31\ (1);
\]

\[
p=29:\quad
\ell=11\ (106),\quad
13\ (2),\quad
17\ (13),\quad
19\ (4),\quad
31\ (1).
\]

完整 \(252\) 条 powered-polynomial 与 squarefree gcd 证书保存在验证输出中。

由普通单纯有限域阿贝尔簇的绝对单纯判据，两个约化都在代数闭包上绝对单纯。特别地，\(p=17\) 的好约化已经足以推出：

\[
\boxed{
P_{46}/\overline{\mathbf Q}\text{ 几何单纯}.
}
\]

因为特征零几何端同态向好约化的几何端同态代数单射；若特征零中存在非平凡 isogeny 分解，其有理幂等元会在绝对单纯约化中产生非平凡幂等元，矛盾。

## 6. 端同态场：一个非对称双素数证书

记

\[
D=
\operatorname{End}^0_{\overline{\mathbf Q}}(P_{46}).
\]

在 \(p=17,29\) 的普通绝对单纯约化中，几何端同态代数均为对应 Frobenius CM 场。故在选择 \(i\) 的剩余嵌入后，

\[
K\subseteq D\subseteq F_{17},
\qquad
K\subseteq D\subseteq F_{29},
\]

其中

\[
F_p=K[X]/(g_p),
\qquad [F_p:K]=4.
\]

### 6.1 \(F_{29}/K\) 没有非平凡中间域

\(g_{29}\) 的 cubic resolvent 为

\[
\begin{aligned}
R_{29}(Y)=\;&Y^3+(20+8i)Y^2\\
&+(-1596-1520i)Y-15600-34080i.
\end{aligned}
\]

其模 \((17,i-4)\) 约化为不可约三次式。故 \(g_{29}\) 与其 cubic resolvent 都在 \(K\) 上不可约，quartic Galois closure 群为 \(A_4\) 或 \(S_4\) 型；根稳定子为极大子群。因此

\[
K\subseteq L\subseteq F_{29}
\quad\Longrightarrow\quad
L=K\ \text{或}\ L=F_{29}.
\]

注意这里不需要对 \(F_{17}\) 作同样假设；这修正并强化了 R19 原协议。

### 6.2 排除 \(F_{17}\simeq_KF_{29}\)

在 Gaussian 素理想

\[
\mathfrak l=(37,i-6)
\]

处，四种 \(i/\!-i\) 配对全部 squarefree，并且分裂型统一为

\[
g_{17}^{\pm}:\ [2,2],
\qquad
g_{29}^{\pm}:\ [1,3].
\]

所以四种可能配对

\[
(g_{17},g_{29}),\quad
(g_{17},\bar g_{29}),\quad
(\bar g_{17},g_{29}),\quad
(\bar g_{17},\bar g_{29})
\]

均不可能定义同构的 \(K\)-四次域。

现在若 \(D\supsetneq K\)，由 \(D\subseteq F_{29}\) 及无中间域性，只能有

\[
D=F_{29}.
\]

但 \(D\hookrightarrow F_{17}\)，且二者在 \(K\) 上次数同为 \(4\)，这会强制

\[
F_{29}\simeq_KF_{17},
\]

与上述四配对分裂型证书矛盾。因此

\[
\boxed{D=K=\mathbf Q(i).}
\]


## 7. 已有条件定理的自动解除

R17 已无条件证明

\[
N_{\operatorname{Aut}(C_{46})}
(\langle\sigma^2\rangle)
=
\langle\sigma\rangle\simeq C_4,
\]

并证明任何不在该 normalizer 中的额外曲线自同构都会产生一个不同的 bielliptic involution，从而产生第二个椭圆商。

现在 \(P_{46}\) 已被证明几何单纯，所以

\[
J(C_{46})\sim E\times P_{46}
\]

中的椭圆 isotypic 因子只有 \(E\) 一个，且

\[
\operatorname{Hom}(E,P_{46})
=
\operatorname{Hom}(P_{46},E)=0.
\]

任意 bielliptic involution 的 \(+1\) 上同调空间都只能是该唯一椭圆因子；其 \(-1\) 空间也只能是 \(P_{46}\)。因此所有 bielliptic involution 在 \(H^1(C_{46})\) 上作用相同。属数至少二的曲线自同构在 \(H^1\) 上作用忠实，故该 involution 唯一。

于是 R17 的条件结论现在被解除为无条件派生定理：

\[
\boxed{
\operatorname{Aut}_{\overline{\mathbf Q}}(C_{46})
=
\langle\sigma\rangle
\simeq C_4.
}
\]

因此 R20 的 canonical-net \(120\) 个 Möbius 候选枚举不再是完整自同构群定理的必要前提；它仍可作为独立交叉验证协议保留，但在验证器尚未完成时不得被反向当作本结论的证据。

另一方面，

\[
\operatorname{Aut}_{\mathrm{gp},\overline{\mathbf Q}}(P_{46})
=
\operatorname{End}_{\overline{\mathbf Q}}(P_{46})^\times
=
\mathbf Z[i]^\times
=
\{\pm1,\pm i\}
\simeq C_4.
\]

## 8. 与既有研究工具的关系

本轮没有建立新的通用工具族。

- R13 的精确有限域点数方法：`REUSE_EXECUTED`，扩展到 \(p=17,29\)；
- R15 的有限单位根阶协议：`REUSE_APPLIED`，并由 \(p=7\) 失败见证完成 correction-aware 重启；
- 有限证书结构：与 `T2_BLOCK_FINITE_CERTIFICATE` 相容，但本结果保持为专用 arithmetic validator；
- 既有 holonomy/cocycle 结论：保留其边界，不用有限域端同态证书替代局部系统 holonomy。

Method harvest：

\[
\texttt{DOMAIN\_CERTIFICATE / RESULT\_ONLY / NO\_NEW\_GLOBAL\_TOOL}.
\]

## 9. 公理与 P000 边界

这些结论来自：

- 精确有限域点数；
- Newton 恒等式；
- Frobenius 根单位根比值排除；
- ordinary Honda–Tate/Tate 端同态理论；
- 好约化 specialization；
- \(K\)-四次域的有限分裂型证书。

所以分类为

\[
\texttt{DERIVED\_GEOMETRIC\_THEOREM},
\]

\[
\texttt{GEOMETRICALLY\_SIMPLE},
\]

\[
\texttt{GEOMETRIC\_ENDOMORPHISM\_ALGEBRA\_QI},
\]

并同时为

\[
\texttt{NOT\_NEW\_AXIOM / NOT\_FOUNDATION / P000\_UNCHANGED}.
\]

该结果不修改、证明、反驳或替换 P000。
