# \(C_{46}\) canonical net 与完整自同构群证书

Status: `FREE_RESEARCH / EXACT_CANONICAL_NET_CERTIFICATE / THEOREM_ONLY_IF_VALIDATOR_PASSES / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research unit: `EM-FREE-F6D046-R20-C46-CANONICAL-NET-AUTOMORPHISM`

## 1. canonical complete intersection

取坐标

\[
[W:Z_0:Z_1:Z_2:Z_3]=[n:1:x:y:x^2].
\]

曲线由三个二次式给出：

\[
Q_1=Z_1^2-Z_0Z_3,
\]

\[
Q_2=Z_2^2-Z_1Z_3+6Z_0Z_3-36Z_0^2,
\]

\[
Q_3=W^2-Z_2Z_3+12Z_0Z_2.
\]

独立 validator 在五个 projective charts 上用 Jacobian rank/Groebner 检查该 \((2,2,2)\) complete intersection 光滑；通过时它就是 genus-5 canonical model。

## 2. quadrics net 判别式

对 \(aQ_1+bQ_2+cQ_3\) 的对称矩阵取行列式，除无关常数后得到

\[
c\cdot
\Bigl(
-a^3b+12a^2b^2-36ab^3+36b^4
+12c^2(a^2-3ab+3b^2)
\Bigr).
\]

判别 quintic 是直线 \(c=0\) 与一条不可约 nodal quartic 的并。quartic 在 \([0:0:1]\) 有唯一 node；其 normalization 是 genus-2 双覆盖

\[
d^2=
\frac{r^3-12r^2+36r-36}
     {12(r^2-3r+3)}.
\]

六个 hyperelliptic 分支点为：

- 三次式 \(r^3-12r^2+36r-36\) 的三个根；
- 二次式 \(r^2-3r+3\) 的两个根；
- \(\infty\)。

三次式平移后为 \(z^3-12z-20\)，判别式 \(-3888\)；其 splitting field 可表示为

\[
\mathbf Q(\alpha,\delta),
\qquad
\alpha^3=12\alpha+20,
\quad
\delta^2=-3.
\]

validator 在该六次域中枚举固定三个源点的全部

\[
6\cdot5\cdot4=120
\]

个可能像，逐一构造唯一 Möbius 变换并检查全部六点。只有该精确枚举得到 identity-only 时，才允许使用下面的自同构群结论。

## 3. 自同构群证书逻辑

若六分支点的 reduced \(\mathrm{PGL}_2\) 稳定子平凡，则 genus-2 normalization 的自同构只剩 hyperelliptic involution，因而 net 判别 quintic 的射影自同构群由

\[
c\longmapsto-c
\]

生成。

order-4 deck 生成元在 canonical 坐标上作用为

\[
\sigma:
[W:Z_0:Z_1:Z_2:Z_3]
\longmapsto
[iW:Z_0:Z_1:-Z_2:Z_3],
\]

并在 net 上实现 \(c\mapsto-c\)。

net 作用的核固定直线分量及其公共 vertex，故正规化 bielliptic involution。R17 已证明

\[
N_{\operatorname{Aut}(C_{46})}(\langle\sigma^2\rangle)=C_4,
\]

其中只有 \(\langle\sigma^2\rangle\) 在 net 上平凡。于是当 validator 的全部 exact checks 通过时，得到

\[
\boxed{\operatorname{Aut}_{\overline{\mathbf Q}}(C_{46})=\langle\sigma\rangle\simeq C_4.}
\]

## 4. 防误报边界

必须同时验证：

- canonical complete intersection 光滑；
- net determinant 分解精确；
- quartic component 不可约且只有指定 node；
- normalization 的六个 branch points 可分、互异；
- 120 个 Möbius 候选的 exact enumeration 只剩 identity；
- R17 normalizer dependency 未被削弱。

若任一项失败，本文件只保留为计算协议，不提升 full automorphism theorem。

分类：

`EXACT_CANONICAL_NET_CERTIFICATE / DERIVED_IF_PASSED / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.