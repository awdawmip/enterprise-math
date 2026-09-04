# \(P_{46}\) 的显式 Prym 线丛模型与 \(\mathbf Q(i)\)-Hodge signature \((3,1)\)

Status: `FREE_RESEARCH / DERIVED_EXPLICIT_PRYM_MODEL / HODGE_SIGNATURE_EXPLAINED / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research unit: `EM-FREE-F6D046-R18-P46-LINE-BUNDLE-HODGE-MODEL`

## 1. 从 quartic 商到 Weierstrass 商

令

\[
u=t+6,\qquad x=-\frac{12}{u},\qquad y=\frac{6v}{u^2}.
\]

则

\[
E:\quad y^2=x^3-6x^2+36.
\]

原二重覆盖

\[
m^2=-\frac1{288}vD(t),\qquad D(t)=u^2-12
\]

满足

\[
-\frac1{288}vD(t)=\frac{y(x^2-12)}{x^4}.
\]

令 \(n=mx^2\)，得到等价函数域模型

\[
\boxed{
C_{46}:\quad
\begin{cases}
y^2=x^3-6x^2+36,\\
n^2=y(x^2-12).
\end{cases}}
\]

设 \(h=y(x^2-12)\)。在 \(E\) 上，\(y=0\) 给出三个有限二阶点，\(x^2=12\) 给出四个点；\(h\) 在无穷远原点 \(O\) 有七阶极点。因此相应分支除子为

\[
B=E[2]\sqcup S_D,
\]

其中无穷远 \(O\) 由奇极点贡献，并且

\[
B\sim8O.
\]

所以二重覆盖的线丛可取

\[
\boxed{L=\mathcal O_E(4O),\qquad L^{\otimes2}\simeq\mathcal O_E(B).}
\]

## 2. Prym 全纯形式的显式四维模型

对 branched double cover \(\pi:C_{46}\to E\)，有

\[
\pi_*\omega_{C_{46}}\simeq\omega_E\oplus(\omega_E\otimes L).
\]

由于 \(\omega_E\simeq\mathcal O_E\)，deck involution \(\sigma^2\) 的反不变全纯形式空间为

\[
H^{1,0}(P_{46})\simeq H^0(E,L)=H^0(E,\mathcal O_E(4O)).
\]

在模型 \(y^2=x^3-6x^2+36\) 上，

\[
\operatorname{ord}_O(x)=-2,\qquad \operatorname{ord}_O(y)=-3.
\]

Riemann--Roch 给出 \(\ell(4O)=4\)，并有显式基底

\[
\boxed{H^0(E,\mathcal O_E(4O))=\langle1,x,y,x^2\rangle.}
\]

这同时重新验证 \(\dim P_{46}=4\)。

## 3. order-4 deck 作用与 \((3,1)\) signature

order-4 生成元可写为

\[
\sigma:(v,m)\longmapsto(-v,im).
\]

在 Weierstrass 商上它下降为

\[
[-1]:(x,y)\longmapsto(x,-y),
\]

而

\[
\sigma^2:(v,m)\longmapsto(v,-m)
\]

是 \(C_{46}\to E\) 的二重 deck involution。

在 \(H^0(E,L)\) 上，\([-1]^*\) 的偶、奇子空间为

\[
H^0(E,L)^+=\langle1,x,x^2\rangle,
\qquad
H^0(E,L)^-=\langle y\rangle.
\]

任取与 \(\sigma^2=-1\) 相容的 \(L\)-linearization，\(\sigma\) 在这两个子空间上的本征值为 \(i,-i\)（整体可因把 \(\sigma\) 换成 \(\sigma^{-1}\) 而互换）。故

\[
\boxed{
\dim H^{1,0}(P_{46})_i=3,
\qquad
\dim H^{1,0}(P_{46})_{-i}=1
}
\]

或反向标记。

因此此前的 imaginary-quadratic action Hodge signature

\[
\boxed{(3,1)}
\]

由线丛截面的奇偶分解直接实现。

## 4. 极化型与模空间含义

对属 \(1\) 基底、八点分歧的二重覆盖，Prym 的诱导极化型为

\[
\boxed{(1,1,1,2)}.
\]

所以 \(P_{46}\) 是一个带 \(\mathbf Z[i]\)-作用、Hodge signature \((3,1)\) 和非主极化 \((1,1,1,2)\) 的阿贝尔四维对象。

signature \((3,1)\) 对应的 unitary period domain 具有复维

\[
3\cdot1=3.
\]

这说明仅凭 \(\mathbf Q(i)\)-作用与 signature 不会强制 CM 或 product decomposition；额外 endomorphism 必须由 Frobenius 场交、Hodge locus 或显式 correspondence 另行证明。

## 5. 对当前分裂问题的作用

本模型把未决问题精确改写为

\[
\operatorname{End}^0_{\bar{\mathbf Q}}(P_{46})\supseteq\mathbf Q(i)
\]

是否严格。

- 若绝对单纯性证书通过，则 \(P_{46}\) 没有 product decomposition；
- 仍需进一步区分 \(\operatorname{End}^0(P_{46})=\mathbf Q(i)\) 与更大的 CM/除代数；
- R16/R17 已排除由现有 branch/deck normalizer 直接产生的额外自同构；
- 因而下一有区分力的对象不是新的局部坐标，而是两个 split good primes 的 Frobenius centralizer/intersection。

分类：

`DERIVED_EXPLICIT_PRYM_MODEL / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.