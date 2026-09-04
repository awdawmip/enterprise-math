# genus-9 strict cover 的 Hodge-character 分解、signature-6 Prym 的 CM 平方与显式 genus-2 signature-4 通道

Status: `FREE_RESEARCH / DERIVED_HODGE_CHARACTER_DECOMPOSITION / GEOMETRIC_PRYM_SPLITTING / MIXED_PRYM_OPEN / NOT_AXIOM / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`
Research unit: `EM-FREE-F6D046-R11-HODGE-CHARACTER-PRYM-SPLITTING`

## 0. 结果

对 R10 的曲线

\[
\mathcal X:\quad r^4=\frac{A(t)}{144},
\qquad q^2=\frac{D(t)}{24},
\]

其中 `A` 为 squarefree quartic、`D` 为与 `A` 互素的 squarefree quadratic，几何 deck group

\[
G=\langle a,b\mid a^4=b^2=1,ab=ba\rangle\simeq C_4\times C_2
\]

按

\[
a:r\mapsto ir,\qquad b:q\mapsto-q
\]

作用。

本轮直接枚举 `H^0(X,Omega^1)`，得到四个非零 character blocks，维数

\[
1,\quad2,\quad2,\quad4,
\]

总和 `9`。其几何含义是：

1. genus-1 common projective quotient `E_346`；
2. signature-4 Prym `P_4`，维数2；
3. signature-6 Prym `P_6`，维数2；
4. mixed Prym `P_46`，维数4。

更强地：

\[
\boxed{P_6\simeq_{\mathbf C} E_i^2}
\]

作为不带指定极化的复阿贝尔簇，其中

\[
E_i=\mathbf C/(\mathbf Z+i\mathbf Z),\qquad j(E_i)=1728.
\]

此外

\[
\boxed{P_4\sim J(H_4)},
\]

其中显式 genus-2 曲线可取

\[
\boxed{
H_4:\quad h^2=\frac{A(t)D(t)}{3456}.
}
\]

因此 genus-9 Jacobian 的分解可收紧为

\[
\boxed{
J(\mathcal X)\sim
E_{346}\times E_i^2\times J(H_4)\times P_{46},
}
\]

维数为

\[
9=1+2+2+4.
\]

其中 `P_46` 带 `Q(i)`-action 的 Hodge signature `(3,1)`；它是否进一步分裂，是当前最小未决算术问题。

---

## 1. 全纯微分基

考虑形式

\[
\omega_{j,\ell,m}=\frac{t^m\,dt}{r^j q^\ell},
\qquad
0\le j\le3,\quad0\le\ell\le1.
\]

在 `A=0` 的 index-4 分歧点，以 `r` 为局部参数，`dt` 含 `r^3dr`，所以 `j<=3` 保证全纯；在 `D=0` 的 index-2 分歧点，以 `q` 为局部参数，`dt` 含 `q dq`，所以 `ell<=1` 保证全纯。

在无穷远令 `u=1/t`。因 `r~c/u`、`q~c'/u`、`dt~-du/u^2`，有

\[
\omega_{j,\ell,m}\sim
u^{j+\ell-m-2}du.
\]

故全纯条件为

\[
0\le m\le j+\ell-2.
\]

得到九个微分：

\[
\frac{dt}{rq};
\]

\[
\frac{dt}{r^2};
\]

\[
\frac{dt}{r^2q},\quad\frac{t\,dt}{r^2q};
\]

\[
\frac{dt}{r^3},\quad\frac{t\,dt}{r^3};
\]

\[
\frac{dt}{r^3q},\quad\frac{t\,dt}{r^3q},\quad\frac{t^2dt}{r^3q}.
\]

对 `a,b` 的本征值为

\[
a^*\omega_{j,\ell,m}=i^{-j}\omega_{j,\ell,m},
\qquad
b^*\omega_{j,\ell,m}=(-1)^\ell\omega_{j,\ell,m}.
\]

于是 `H^{1,0}` 的非零块为

\[
(-i,-1):1,
\]

\[
(-1,+1):1,
\]

\[
(-1,-1):2,
\]

\[
(i,+1):2,
\]

\[
(i,-1):3.
\]

其中共轭 character 对应的两个 Hodge multiplicities 合并成有理/实阿贝尔因子：

- `(i,+1)` 与 `(-i,+1)` 给维数 `2` 的 `P_6`，multiplicity `(2,0)`；
- `(i,-1)` 与 `(-i,-1)` 给维数 `4` 的 `P_46`，multiplicity `(3,1)`。

---

## 2. signature-6 Prym 为什么分裂为 E_i^2

在 `P_6` 的切空间上，order-4 automorphism `a` 以同一个复嵌入标量作用；等价地，其 cotangent CM type 为 `(2,0)`。积分同调 lattice `H_1(P_6,Z)` 因 `a^2+1=0` 成为 torsion-free rank-2 `Z[i]`-module。

`Z[i]` 是 PID，所以该 lattice 是自由的：

\[
H_1(P_6,Z)\simeq Z[i]^2.
\]

选择一个 `Z[i]` 基，并以复线性变换送到标准基，即得到复环面同构

\[
P_6\simeq
(\mathbf C/Z[i])^2=E_i^2.
\]

该陈述不说 Prym 极化是两个 product principal polarizations；R10 的 double-cover Prym 极化仍可能在 `E_i^2` 上对应非对角 Hermitian form。

相应地，signature-6 中间曲线 `C_6:r^4=A/144` 满足

\[
\boxed{
J(C_6)\sim E_{346}\times E_i^2.
}
\]

---

## 3. signature-4 Prym 的 genus-2 模型

令

\[
h=r^2q.
\]

则

\[
h^2=r^4q^2=\frac{A(t)D(t)}{144\cdot24}
=\frac{A(t)D(t)}{3456}.
\]

因为 `AD` 是 squarefree sextic，`H_4` 是 genus2。其全纯微分

\[
\frac{dt}{h},\qquad\frac{t\,dt}{h}
\]

拉回后正是

\[
\frac{dt}{r^2q},\qquad\frac{t\,dt}{r^2q},
\]

即 character `(-1,-1)` 的二维块。由相应 V4 quotient relation，

\[
P_4\sim J(H_4).
\]

这把 signature-4 线性 holonomy channel 从抽象 Prym 变成可直接计算 Igusa invariants、reduction 和 endomorphisms 的 genus-2 曲线。

---

## 4. mixed Prym 是真正剩余核心

`P_46` 来自 characters `(i,-1)` 与 `(-i,-1)`，在 `H^{1,0}` 上 multiplicities 为 `(3,1)`。它具有 `Q(i)` action，但与 `(2,0)` 情形不同，lattice/complex-type 论证不强迫其成为 CM 椭圆曲线的幂。

等价的中间曲线为

\[
C_{46}:m^2=-\frac{vD(t)}{288},
\]

或在归一化意义下

\[
m^4\propto A(t)D(t)^2,
\]

其 genus 为5，而 `P_46=Prym(C_46/E_346)` 维数4、极化类型不在本轮中擅自简化。

当前严格前沿是：判定 `P_46` 在 `\overline Q` 上是否简单，或是否分解为两个 abelian surfaces / genus-2 Jacobians；若分解，确定其与 signature-4 genus-2 factor `J(H_4)` 的同源关系。

---

## 5. 对 inverse-pi 几何的意义

Wronskian和Clausen数据只能看到偶次 representation blocks，无法区分 `P_6` 的 Gaussian CM lift 与 mixed `(3,1)` lift。R11 表明“丢失的符号数据”并非无结构噪声：它在 Jacobian 中落入具有明确 CM/Hodge 类型的 Prym 因子。

但这仍然是模周期局部系统的派生结构，不是 P000 六维空间本身的因子分解。

## 6. 审计

工具复用：`T7 COMPOSE_APPLIED`、`T9 REUSE_APPLIED`。本轮使用标准 abelian-cover character decomposition、Prym 和 V4 quotient machinery；`NO_NEW_TOOL_FAMILY`。

公理门：`DERIVED_HODGE_CHARACTER_DECOMPOSITION / GEOMETRIC_PRYM_SPLITTING / NOT_NEW_AXIOM / NOT_FOUNDATION`。
