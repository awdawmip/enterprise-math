# \(p=7\) 约化的 Honda–Tate 分解、绝对单纯曲面与几何端同态代数

Status: `FREE_RESEARCH / DERIVED HONDA–TATE THEOREM / CORRECTION-CLOSED / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units:

- `EM-FREE-F6D046-R37-P7-HONDA-TATE-DECOMPOSITION`
- `EM-FREE-F6D046-R38-P7-ABSOLUTELY-SIMPLE-SURFACE`
- `EM-FREE-F6D046-R39-P7-GEOMETRIC-ENDOMORPHISM-ALGEBRA`

## 1. 研究对象与勘误边界

设 \(P_{46}\) 为前序研究得到的四维 Prym。其 \(p=7\) Frobenius 多项式为

\[
f_7(X)=X^8+5X^6+245X^2+2401.
\]

它是偶多项式，因此前序的“不可约即绝对单纯”尝试在 \(m=2\) 处必然失败：若 \(\alpha\) 是根，则 \(-\alpha\) 也是根，且根比值为单位根 \(-1\)。这只说明 \(P_{46,7}\) 在某个有限扩域上不再单纯，并不单凭偶性给出精确分解。

本轮用完整 Honda–Tate 局部不变量关闭该问题。

## 2. 二次基变换多项式

精确恒等式为

\[
\boxed{f_7(X)=h(X^2)},
\qquad
h(Y)=Y^4+5Y^3+245Y+2401.
\]

在模 \(11\) 下，\(h\) 通过 Rabin 判据不可约，故 \(h\) 在 \(\mathbf Q[Y]\) 上不可约。

令 \(\alpha\) 为 \(h\) 的一个根并置

\[
F=\mathbf Q(\alpha).
\]

一个显式整数基为

\[
1,\quad
\alpha,\quad
\frac{\alpha^2+5\alpha}{7},\quad
\frac{\alpha^3+12\alpha^2+84\alpha+49}{98}.
\]

其迹 Gram 行列式给出

\[
\boxed{\operatorname{disc}(F)=4173336=2^3 3^3 139^2}.
\]

因此 \(7\) 在 \(F\) 中不分歧；幂基指数为 \(686\)。

## 3. \(7\)-进 Newton 多边形与局部域数据

\(h\) 的系数估值点为

\[
(0,4),(1,2),(2,+\infty),(3,0),(4,0).
\]

Newton 多边形有三段：

\[
(0,4)\to(1,2),\qquad
(1,2)\to(3,0),\qquad
(3,0)\to(4,0),
\]

对应根估值

\[
2,\quad1,1,\quad0.
\]

中间残余多项式为 \(T^2+1\)，在 \(\mathbf F_7\) 上不可约。因此 \(7\) 上方的三个素点数据为

\[
(e,f,v_{\mathfrak p}(\alpha))
=
(1,1,2),\quad(1,2,1),\quad(1,1,0).
\]

相应曲面 Newton 斜率为

\[
1,\frac12,\frac12,0,
\]

所以该曲面的 \(p\)-rank 为 \(1\)；四维 \(P_{46,7}\) 的斜率则各出现两次，\(p\)-rank 为 \(2\)。

## 4. Honda–Tate 局部不变量

在 \(\mathbf F_{49}\) 上，\(\alpha\) 是 weight-one Weil \(49\)-数。Honda–Tate 端同态除代数在 \(7\) 上方的局部不变量为

\[
[F_{\mathfrak p}:\mathbf Q_7]
\frac{v_{\mathfrak p}(\alpha)}{v_{\mathfrak p}(49)}
\pmod1.
\]

三处分别为

\[
1\cdot\frac22=1\equiv0,
\qquad
2\cdot\frac12=1\equiv0,
\qquad
1\cdot\frac02=0.
\]

所有有限处局部不变量均为零，故 Schur index 为 \(1\)，对应的 \(\mathbf F_{49}\)-单纯阿贝尔簇 \(B\) 是一条阿贝尔曲面，并满足

\[
\boxed{\operatorname{End}^0_{\mathbf F_{49}}(B)=F.}
\]

二次基变换把 \(P_{46,7}\) 的 Frobenius 特征多项式变为

\[
\prod_{j=1}^{8}(Y-\pi_j^2)=h(Y)^2.
\]

所以

\[
\boxed{
P_{46,7}\otimes_{\mathbf F_7}\mathbf F_{49}
\sim B^2.
}
\]

同时，\(f_7(X)=h(X^2)\) 结合 \(h\) 不可约及一个估值为奇数的素点，通过 Capell 型判据给出 \(f_7\) 在 \(\mathbf Q[X]\) 上不可约。因此 \(P_{46,7}/\mathbf F_7\) 本身仍然单纯。

## 5. \(B\) 的绝对单纯性

若 \(B\) 在某个有限扩域上失去单纯性，则 \(h\) 的两个不同根之比必为单位根。任意两根的合成域次数至多 \(16\)，故只需检查

\[
\varphi(m)\le16.
\]

由初等界可取 \(m\le512\)。实际候选阶共有 \(31\) 个，最大为 \(60\)。对每个候选 \(m\)，验证器构造

\[
h_m(Y)=\prod_j(Y-\alpha_j^m)
\]

并给出一个辅助素数，使 \(h_m\) 模该素数 squarefree。全部 \(31\) 项通过，因此不存在不同根的单位根比值。

故

\[
\boxed{B/\mathbf F_{49}\text{ 绝对单纯}.}
\]

并且在任意有限扩域上其有理端同态代数仍为 \(F\)。

## 6. 几何端同态代数

由

\[
P_{46,7,\mathbf F_{49}}\sim B^2
\]

以及 \(B\) 的绝对单纯性，得到

\[
\boxed{
\operatorname{End}^0_{\overline{\mathbf F}_7}(P_{46,7})
\simeq M_2(F).
}
\]

这严格解释了此前 \(m=2\) 证书失败：它不是偶然的算法退化，而是几何端同态代数从特征零的 \(\mathbf Q(i)\) 跃迁到特征七的矩阵代数 \(M_2(F)\)。

## 7. CM 域的实子域

令

\[
x=\alpha+\frac{49}{\alpha}.
\]

利用 \(h(\alpha)=0\) 可得

\[
\boxed{x^2+5x-98=0}.
\]

因此

\[
\boxed{F^+=\mathbf Q(\sqrt{417}).}
\]

并可写

\[
F=F^+\!\left(\sqrt{x^2-196}\right)
=F^+\!\left(\sqrt{-5x-98}\right),
\]

其中被开方元在 \(F^+\) 的两个实嵌入下均为负，故 \(F\) 是一个非双二次的四次 CM 域。四次 resolvent 分解为

\[
(Z-98)(Z^2+98Z+1225),
\]

与其非 Galois、二面体正规闭包结构一致。

## 8. 结论与边界

无条件结论为

\[
\boxed{
P_{46,7}/\mathbf F_7\text{ 单纯但不绝对单纯};
}
\]

\[
\boxed{
P_{46,7,\mathbf F_{49}}\sim B^2,
\quad
B\text{ 为绝对单纯阿贝尔曲面};
}
\]

\[
\boxed{
\operatorname{End}^0_{\overline{\mathbf F}_7}(P_{46,7})=M_2(F),

\operatorname{End}^0_{\mathbf F_{49}}(B)=F.
}
\]

本结果是有限域 Honda–Tate 与 CM 域算术的派生定理，不构成新公理，不进入 Foundation，也不改变 P000。

Classification:

`DERIVED_HONDA_TATE_DECOMPOSITION / P7_F49_IS_B_SQUARED / B_ABSOLUTELY_SIMPLE_SURFACE / GEOMETRIC_ENDOMORPHISM_ALGEBRA_M2_CM4 / CORRECTION_CLOSED / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.
