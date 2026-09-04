# degree-29 最快公式的 level-2 / level-4 二次桥与代数系数伴随公式

Status: `FREE_RESEARCH / EXACT_QUADRATIC_TRANSPORT / DERIVED_NOT_AXIOM`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`

Author/program signature: `YUAN X / Enterprise Math`

## 1. 二次变换

记

\[
F_2(z)={}_3F_2\left(\frac12,\frac14,\frac34;1,1;z\right),
\qquad
F_4(w)={}_3F_2\left(\frac12,\frac12,\frac12;1,1;w\right).
\]

由 level 2 与 level 4 的标准二次变换，局部有

\[
\boxed{
F_2\left(-\frac{4w}{(1-w)^2}\right)
=\sqrt{1-w}\,F_4(w).
}
\]

设 `z=-4w/(1-w)^2`，则

\[
\Theta_z=\frac{1-w}{1+w}\Theta_w.
\]

这是前一阶段喷流变换矩阵的一个非平凡实例。

## 2. degree-29 奇异点的精确像

沿用最快公式的互补奇异点

\[
\alpha_0=\frac12-\frac{910\sqrt{29}}{9801},
\qquad
\beta_0=1-\alpha_0,
\qquad
z_0=4\alpha_0\beta_0=99^{-4}.
\]

取

\[
\boxed{w_0=-\frac{\alpha_0}{\beta_0}.}
\]

则

\[
1-w_0=\frac1{\beta_0},
\qquad
1+w_0=\frac{\beta_0-\alpha_0}{\beta_0},
\]

并且

\[
-\frac{4w_0}{(1-w_0)^2}=4\alpha_0\beta_0=z_0.
\]

Pell 恒等式进一步给出

\[
\beta_0-\alpha_0
=\frac{1820\sqrt{29}}{9801}
=\sqrt{1-z_0}.
\]

因此这个映射并非数值巧合，而是 degree-29 奇异点在 level 2 / level 4 二次桥下的精确对应。

## 3. 协向量传输

最快公式的 Wronskian 归一化形式是

\[
\frac{\sin(\pi/4)}{\pi}
=(A_2+B_2\Theta_z)F_2(z_0),
\]

其中

\[
A_2=\frac{2206}{9801},
\qquad
B_2=\frac{52780}{9801}.
\]

在 `w0` 处，规范因子和欧拉雅可比分别为

\[
g_0=\sqrt{1-w_0}=\frac1{\sqrt{\beta_0}},
\qquad
\kappa_0=\frac{1-w_0}{1+w_0}=\frac1{\beta_0-\alpha_0}.
\]

又有

\[
\frac{\Theta_wg}{g}\bigg|_{w_0}=\frac{\alpha_0}{2}.
\]

故喷流协向量按下式传输：

\[
\boxed{
A_4=\frac1{\sqrt{\beta_0}}
\left(A_2+\frac{B_2\alpha_0}{2(\beta_0-\alpha_0)}\right),
\qquad
B_4=\frac1{\sqrt{\beta_0}}
\frac{B_2}{\beta_0-\alpha_0}.
}
\]

于是

\[
\frac{\sqrt2}{2\pi}=(A_4+B_4\Theta_w)F_4(w_0).
\]

乘以 `sqrt(2)` 得到一个精确的 level-4 伴随公式：

\[
\boxed{
\frac1\pi=(\widehat A_4+\widehat B_4\Theta_w)
{}_3F_2\left(\frac12,\frac12,\frac12;1,1;w_0\right),
}
\]

其中

\[
\boxed{
\widehat A_4=\sqrt{\frac2{\beta_0}}
\left(\frac{2206}{9801}
+\frac{52780\alpha_0}{2\cdot9801(\beta_0-\alpha_0)}\right),
\qquad
\widehat B_4=\sqrt{\frac2{\beta_0}}
\frac{52780}{9801(\beta_0-\alpha_0)}.
}
\]

数值上

\[
w_0\approx-2.602550902759584\times10^{-9},
\]

\[
\widehat A_4\approx0.3183098887648975,
\qquad
\widehat B_4\approx7.615773115774127.
\]

## 4. 新信息

这给出了第一个显式的“同一守恒面积协向量跨 level 图册传输”实例：整数对 `(1103,26390)` 经过二次喷流矩阵后变为代数系数对 `(Ahat4,Bhat4)`，而标量 `1/pi` 保持不变。

它验证了此前的判断：

- `1103` 与 `26390` 是标准 level-2 图册中的坐标，不是绝对不变量；
- 真正可跨图册运输的是对偶喷流协向量；
- 系数的整数性不是几何不变量，而是特定模参数、坐标与归一化共同造成的算术现象。

## 5. 收敛比较

新图册的参数满足

\[
|w_0|\approx2.60255\times10^{-9},
\]

所以单看幂级数参数，名义收缩约为

\[
-\log_{10}|w_0|\approx8.5846
\]

位/项，比 `z0=99^-4` 的约 `7.9825` 位/项更小。这个比较只针对超几何参数；代数系数计算和基变换成本未计入，因而不应直接宣称它在实际算法中优于 Ramanujan 的整数公式。

## 6. 验证与分类

标准库高精度验证确认：

\[
(\widehat A_4+\widehat B_4\Theta_w)F_4(w_0)
=1/\pi
\]

达到 75 位以上一致。

该结果由已知二次超几何变换和前述喷流协变定理推出，分类为

`EXACT_QUADRATIC_TRANSPORT / DERIVED_NOT_AXIOM / PRIOR_ART_TRANSFORMATION_USED / NOT_FOUNDATION`。
