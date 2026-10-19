# \(B/\mathbf F_{49}\) 的显式 genus-2 Jacobian 与 \(P_{46,7}\) 的 Weil-restriction 实现

Status: `FREE_RESEARCH / DERIVED EXPLICIT CURVE THEOREM / PRINCIPAL POLARIZATION EXHIBITED / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units:

- `EM-FREE-F6D046-R40-B-EXPLICIT-GENUS2-JACOBIAN`
- `EM-FREE-F6D046-R41-B-PRINCIPAL-POLARIZATION`
- `EM-FREE-F6D046-R42-P7-WEIL-RESTRICTION-REALIZATION`

## 1. 输入

R37--R39 已得到

\[
P_{46,7}\otimes_{\mathbf F_7}\mathbf F_{49}\sim B^2,
\]

其中 \(B/\mathbf F_{49}\) 是绝对单纯阿贝尔曲面，Frobenius 多项式为

\[
h(T)=T^4+5T^3+245T+2401.
\]

其几何端同态域是四次 CM 域

\[
F=\mathbf Q(\alpha),\qquad h(\alpha)=0.
\]

本轮目标是给出 \(B\) 同源类中的显式曲线代表，并把整个 \(p=7\) 四维约化写成一个定义在 \(\mathbf F_7\) 上的显式 Weil restriction 同源类。

## 2. 显式 genus-2 曲线

取

\[
\mathbf F_{49}=\mathbf F_7(u),\qquad u^2=-1.
\]

定义

\[
\boxed{
C:\quad y^2=
 x^5+(5+6u)x^4+(1+3u)x^3+3ux^2+4x+(2+4u).
}
\]

右端五次多项式与其导数的最大公因子为 \(1\)，故 \(C\) 是光滑 genus-2 曲线，且奇次数模型具有一个 \(\mathbf F_{49}\)-有理无穷远点。

验证器在两个彼此独立的有限域模型中直接计数：

\[
\boxed{\#C(\mathbf F_{49})=55,}
\]

\[
\boxed{\#C(\mathbf F_{49^2})=2377.}
\]

第二次计数不使用第一次数值的递推，而在

\[
\mathbf F_{2401}=\mathbf F_7(w)/(w^4+w^3+1)
\]

中直接枚举，并以

\[
u=1+4w^2+w^3,
\qquad u^2=-1
\]

嵌入 \(\mathbf F_{49}\)。每个点数又分别由 Euler 判别和平方表两种算法重算。

## 3. Weil 多项式恢复

令 \(q=49\)，并记 Frobenius 根的幂和为 \(s_r\)。由点数公式

\[
s_1=q+1-\#C(\mathbf F_q)=-5,
\]

\[
s_2=q^2+1-\#C(\mathbf F_{q^2})=25.
\]

Newton 恒等式给出

\[
e_2=\frac{s_1^2-s_2}{2}=0.
\]

故 \(J(C)\) 的 Frobenius 多项式为

\[
\begin{aligned}
P_C(T)
&=T^4-s_1T^3+e_2T^2-qs_1T+q^2\\
&=T^4+5T^3+245T+2401\\
&=h(T).
\end{aligned}
\]

因此由有限域 Tate 同源定理，

\[
\boxed{J(C)\sim_{\mathbf F_{49}} B.}
\]

因为 R38 已证明该同源类绝对单纯，所以 \(J(C)\) 也是绝对单纯的 genus-2 Jacobian。

此外

\[
\#J(C)(\mathbf F_{49})=P_C(1)=2652=2^2\cdot3\cdot13\cdot17.
\]

## 4. 主极化的显式实现

Jacobian 的 theta 除子给出定义在 \(\mathbf F_{49}\) 上的典范主极化：

\[
\lambda_C:J(C)\xrightarrow{\sim}J(C)^\vee.
\]

所以这不只是“同源类原则上可主极化”，而是给出了一个具体的主极化代表：

\[
\boxed{(B,\lambda_B)\ \text{可取为}\ (J(C),\lambda_C).}
\]

对一般阿贝尔曲面同源类，Howe--Maisner--Nart--Ritzenthaler 的判据说明，若 Weil 多项式写成

\[
T^4+aT^3+bT^2+aqT+q^2,
\]

则不含主极化代表的唯一情形要求 \(a^2-b=q\)、\(b<0\) 及附加素因子条件。这里 \((a,b,q)=(5,0,49)\)，首先就有 \(25\ne49\)；显式曲线已给出更强的构造性证明。

## 5. Hasse--Witt 型

写

\[
f_C(x)^3=\sum_k c_kx^k.
\]

在基 \(dx/y, xdx/y\) 下取 Hasse--Witt 矩阵

\[
H=(c_{7i-j})_{1\le i,j\le2}.
\]

以 \(a+7b\) 编码 \(a+bu\)，验证器得到

\[
H=
\begin{pmatrix}
41&25\\
5&39
\end{pmatrix}
=
\begin{pmatrix}
6+5u&4+3u\\
5&4+5u
\end{pmatrix}.
\]

有

\[
\det H=0,
\qquad H\ne0.
\]

并且 Frobenius-twisted stable product \(H^{(7)}H\) 仍为非零秩一矩阵。因此

\[
\boxed{f\text{-rank}(J(C))=1,\qquad a(J(C))=1.}
\]

这与 R37 的 Newton 斜率

\[
0,\frac12,\frac12,1
\]

完全一致。

## 6. Weil restriction 实现四维约化

令

\[
A=\operatorname{Res}_{\mathbf F_{49}/\mathbf F_7}J(C).
\]

其 \(\mathbf F_7\)-Frobenius 在诱导 Tate 模上平方为 \(J(C)\) 的 \(\mathbf F_{49}\)-Frobenius，因此

\[
\operatorname{charpoly}(\operatorname{Frob}_7|A)
=h(T^2).
\]

即

\[
\begin{aligned}
h(T^2)
&=T^8+5T^6+245T^2+2401\\
&=f_7(T).
\end{aligned}
\]

这正是 \(P_{46,7}\) 的 Frobenius 多项式，所以再次由 Tate 同源定理：

\[
\boxed{
P_{46,7}\sim_{\mathbf F_7}
\operatorname{Res}_{\mathbf F_{49}/\mathbf F_7}J(C).
}
\]

该实现同时解释：

\[
A_{\mathbf F_{49}}
\simeq J(C)\times J(C)^{(7)}
\sim B^2,
\]

以及

\[
\#P_{46,7}(\mathbf F_7)=f_7(1)=2652
=\#J(C)(\mathbf F_{49}).
\]

Weil restriction 把同构 \(\lambda_C\) 送为

\[
\operatorname{Res}(\lambda_C):A\xrightarrow{\sim}A^\vee,
\]

故 \(P_{46,7}\) 的 \(\mathbf F_7\)-同源类含有主极化代表。这里必须区分：原 Prym 的自然极化型仍是 \((1,1,1,2)\)；本结论是该有限域同源类中另有一个通过 Weil restriction 构造的主极化代表。

## 7. 非下降边界

\(B\) 不可能在 \(\mathbf F_7\) 上下降到一个阿贝尔曲面同源类。否则存在 degree-4 Weil 多项式 \(g(T)\in\mathbf Z[T]\)，使其二次基变换为 \(h\)，进而

\[
g(T)g(-T)=h(T^2)=f_7(T),
\]

这会使已在 R37 中证明不可约的 \(f_7\) 在 \(\mathbf Q[T]\) 中分解，矛盾。

所以 Weil restriction 不是一个隐藏的二维 \(\mathbf F_7\)-下降，而是真正的二次诱导四维同源类。

## 8. 分类

本轮结果属于：

`DERIVED_EXPLICIT_GENUS2_MODEL / B_ISOGENOUS_TO_JACOBIAN / PRINCIPAL_POLARIZATION_EXHIBITED / P7_WEIL_RESTRICTION_REALIZATION / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

父候选仍为 `REJECT_AS_NEW_AXIOM`。本轮不修改 P000，不把有限域实现提升为六维本体公理。
