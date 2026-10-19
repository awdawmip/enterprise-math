# signatures 3/4 经椭圆共同覆盖运输得到的两条 signature-6 伴随 1/pi 公式

Status: `FREE_RESEARCH / DERIVED_COMPANION_IDENTITIES / HIGH_PRECISION_VERIFIED / NOT_AXIOM / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`
Research unit: `EM-FREE-F6D046-R9-SIGNATURE6-COMPANION-INVERSE-PI`

## 0. 结论

R8 的椭圆共同底面使任何 signature `3` 或 `4` 的一阶 inverse-pi 协向量都能在同一个 `t` 基点上运输为 signature `6` 协向量。本轮将该运输应用于：

- signature `3`、degree `23`、参数 `-1/250000` 的公式；
- signature `4`、degree `29`、参数 `99^-4` 的 Ramanujan 公式。

所得两条 signature-6 公式均由 100 位以上数值计算验证。它们的参数不同，因为两个源公式在共同模曲线上对应不同 `j`-值和不同 `t` 基点。

## 1. 通用运输律

令

\[
A(t)=(t+6)(t^3+18t^2+84t+24),
\qquad
v^2=A(t),\quad v(0)=-12,
\]

\[
Z_6(t)=\frac{1728t(t+8)^3(t+9)^2}{A(t)^3},
\qquad
R_6(t)=-\frac{v}{12}.
\]

在共同喷流基 `S(t)=H(t)^2` 中，

\[
F_6(Z_6(t))=R_6(t)S(t),
\]

其中

\[
F_6(Z)={}_3F_2\!\left(\frac12,\frac16,\frac56;1,1;Z\right).
\]

设源 signature `s` 满足

\[
F_s(Z_s(t))=R_s(t)S(t),
\]

且在 `t=t_*` 有

\[
\frac1\pi=(a_s+b_s\Theta_{Z_s})F_s(Z_s).
\]

定义

\[
\kappa_s=\frac{Z_s}{tZ_s'},
\qquad
\delta_s=\Theta_t\log R_s,
\]

\[
\kappa_6=\frac{Z_6}{tZ_6'},
\qquad
\delta_6=\Theta_t\log R_6=\frac{tA'}{2A}.
\]

链式法则给出唯一的 signature-6 companion covector：

\[
\boxed{
b_6=\frac{R_s}{R_6}\,b_s\frac{\kappa_s}{\kappa_6},
}
\]

\[
\boxed{
a_6=\frac{R_s}{R_6}
\left[a_s+b_s\kappa_s(\delta_s-\delta_6)\right].
}
\]

于是

\[
\boxed{
\frac1\pi=(a_6+b_6\Theta_{Z_6})F_6(Z_6)
\quad\text{at }t=t_*.
}
\]

## 2. signature 3 source

取

\[
Z_3(t)=4\alpha_3(t)(1-\alpha_3(t)),
\qquad
\alpha_3(t)=\frac{t(t+9)^2}{(t+6)^3},
\]

\[
R_3(t)=\frac{(t+6)^2}{36},
\qquad
\delta_3=\frac{2t}{t+6}.
\]

`t_3` 是靠近零的实根

\[
Z_3(t_3)=-\frac1{250000}.
\]

源协向量为

\[
a_3=\frac{827}{1500\sqrt3},
\qquad
b_3=\frac{14151}{1500\sqrt3}.
\]

将这些量代入通用公式，得到完全由代数数 `t_3,v_3` 确定的 `(a_{6,3},b_{6,3},Z_{6,3})`。验证器选取与 `v(0)=-12` 连续的分支，并直接求和 `F_6` 及其 Euler derivative；所得值与 `1/pi` 的差小于 `10^-95`。

## 3. signature 4 source

取

\[
Z_4(t)=4\alpha_4(t)(1-\alpha_4(t)),
\qquad
\alpha_4(t)=\frac{t(t+8)^3}{(t^2+12t+24)^2},
\]

\[
R_4(t)=\frac{t^2+12t+24}{24},
\qquad
\delta_4=\frac{t(2t+12)}{t^2+12t+24}.
\]

`t_4` 是靠近零的正实根

\[
Z_4(t_4)=99^{-4}.
\]

源协向量为

\[
a_4=\frac{2206\sqrt2}{9801},
\qquad
b_4=\frac{52780\sqrt2}{9801}.
\]

代入通用公式得到 `(a_{6,4},b_{6,4},Z_{6,4})`；同样以直接 `{}_3F_2` 级数与 Euler derivative 验证，残差小于 `10^-95`。

## 4. 精确性与新颖性边界

这些系数虽然通常不是简单整数，但并非数值拟合。它们由：

1. 源公式的精确协向量；
2. 代数方程定义的 `t_*`；
3. 椭圆曲线方程 `v^2=A(t)`；
4. 明确的链式法则运输矩阵

唯一确定。

本结果说明同一个 inverse-pi 标量可在共同局部系统中产生不同 signature 的 companion identities。然而：

- 两个源基点不同；
- 不存在路径无关的全局平坦协向量；
- companion identity 不是独立模方程或新公理；
- 其证明依赖 R8 的标准 quadratic transformation 与 jet-covector transport。

公理门：`DERIVED_COMPANION_IDENTITY / NOT_NEW_AXIOM / NOT_FOUNDATION`。

工具复用：`T9 REUSE_APPLIED`；本轮只应用既有喷流/holonomy 运输，不建立新工具家族。
