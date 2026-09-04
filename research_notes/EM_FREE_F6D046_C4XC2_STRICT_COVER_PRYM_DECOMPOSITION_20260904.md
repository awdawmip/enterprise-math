# signatures 3/4/6 严格共同覆盖的 C4×C2 压缩、分歧 passport 与 Prym 分解

Status: `FREE_RESEARCH / DERIVED_EXPLICIT_GALOIS_COVER / PRYM_DECOMPOSITION / NOT_AXIOM / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`
Research unit: `EM-FREE-F6D046-R10-C4XC2-STRICT-COVER-PRYM`

## 0. 结论

R8 的两级 signature-6 扩张

\[
v^2=A(t),\qquad r^2=-\frac{v}{12}
\]

可压缩为单个 cyclic quartic 方程

\[
\boxed{r^4=\frac{A(t)}{144}},
\qquad
A(t)=t^4+24t^3+192t^2+528t+144.
\]

signature `4/3` character 由

\[
\boxed{q^2=\frac{D(t)}{24}},
\qquad D(t)=t^2+12t+24
\]

消去。故 signatures `3/4/6` 的 strict common cover 可写成

\[
\boxed{
\mathcal X:\quad
r^4=\frac{A(t)}{144},
\qquad
q^2=\frac{D(t)}{24}.
}
\]

在代数闭包上，deck group 为

\[
\boxed{G\simeq C_4\times C_2},
\]

由 `a:r↦ir` 与 `b:q↦-q` 生成。其次数为 `8`、紧化 genus 为 `9`。

该表达不仅重算 genus，还揭示：signature 6 的 projective base-change 与 linear center choice 并非两个互不相干的二次层，而是同一个 order-4 Kummer channel 的平方与四次根两级。

## 1. 分歧 passport

`A` 与 `D` squarefree 且互素。

- 在 `A=0` 的四点，quartic cover `r^4=A/144` 有 inertia `C4`；
- 在 `D=0` 的两点，quadratic cover `q^2=D/24` 有 inertia `C2`；
- 无穷远处 `ord_infinity(A)=-4`、`ord_infinity(D)=-2`，均被相应根次数整除，所以无额外分歧；
- 两组有限分歧不交。

对 `|G|=8` 的 Galois cover，Riemann--Hurwitz 为

\[
2g(\mathcal X)-2
=8(-2)
+4\cdot8\left(1-\frac14\right)
+2\cdot8\left(1-\frac12\right)
=-16+24+8=16.
\]

因此

\[
\boxed{g(\mathcal X)=9.}
\]

这与 R8 从 genus-1 椭圆底面上的 `(Z/2)^2` cover 得到的结果一致。

## 2. 与 R8 椭圆底面的关系

定义

\[
v=-12r^2.
\]

则 `v^2=A(t)`。子群

\[
H=\langle a^2,b\rangle\simeq C_2\times C_2
\]

固定 `t,v`，故

\[
\mathcal X/H=E_{346}:v^2=A(t).
\]

因此：

- `a mod H` 是 `E_{346}->P1_t` 的 projective involution；
- `a^2` 是 signature-6 linear character；
- `b` 是 signature-4 linear character。

这把 `projective base-change` 与 `linear H1 characters` 放在同一个有限 deck group 中，但二者仍属于不同 quotient 层级。

## 3. 三个 V4 中间 double covers

把 `\mathcal X->E_{346}` 看成 deck group `H=<a^2,b>≈V4` 的 cover。三个 index-2 quotient 分别是：

### 3.1 signature-6 channel

\[
C_6:\quad r^2=-\frac{v}{12}.
\]

它在 `v=0` 的四点分支，因此

\[
g(C_6)=2g(E)-1+\frac42=3.
\]

等价地，`C_6` 是 plane/superelliptic quartic `r^4=A/144`。

### 3.2 signature-4 channel

\[
C_4:\quad q^2=\frac{D(t)}{24}
\]

连同 `v^2=A(t)`。在 `D=0` 的四个 `E`-点分支，也有

\[
g(C_4)=3.
\]

### 3.3 mixed channel

令 `m=rq`，则

\[
C_{46}:\quad m^2=-\frac{vD(t)}{288}.
\]

其 branch set 是前两组四点的并，共八点，故

\[
g(C_{46})=2\cdot1-1+\frac82=5.
\]

于是 genus 关系为

\[
\boxed{
g(\mathcal X)=g(C_6)+g(C_4)+g(C_{46})-2g(E)=3+3+5-2=9.}
\]

## 4. Jacobian / Prym isogeny decomposition

标准 `V4`-cover Jacobian relation给出（在适当底域上、至 isogeny）：

\[
\boxed{
J(\mathcal X)\times J(E)^2
\sim
J(C_6)\times J(C_4)\times J(C_{46}).
}
\]

等价地，维数可分成

\[
9=1+2+2+4,
\]

对应

\[
J(E),\quad
\operatorname{Prym}(C_6/E),\quad
\operatorname{Prym}(C_4/E),\quad
\operatorname{Prym}(C_{46}/E).
\]

这给出三个不同的 holonomy 通道：signature-6、signature-4 与 mixed interaction。该 isogeny 不主张主极化直接分裂，也不自动给出各 Prym 的进一步简单因子分解。

## 5. 偶次 readout 的群论位置

Clausen/symmetric square 对 `a^2` 与 `b` 的中心 signs 都不敏感；但 order-4 生成元 `a` 的 projective involution仍控制 `v` 的符号及 signature-6 coordinate sheet。因此：

\[
\text{EVEN TENSOR KILLS }H\text{-CHARACTERS}
\quad\text{但不等于}
\quad
\mathcal X/P1\text{ 的整个 }C_4\times C_2\text{ deck data 消失。}
\]

## 6. 审计

本结果由 R8 方程的 Kummer 压缩、Galois 分歧与标准 V4 Jacobian relation 派生。它不是新公理，也不是新的通用工具家族。

工具复用：`T9 REUSE_APPLIED`、`T7 COMPOSE_APPLIED`。公理门：`DERIVED_EXPLICIT_GALOIS_COVER / PRYM_DECOMPOSITION / NOT_NEW_AXIOM / NOT_FOUNDATION`。
