# \(X_0(6)\) 最小共同覆盖、中心符号 holonomy 与跨 signature \(1/\pi\) 协向量

Status: `FREE_RESEARCH / DERIVED_COMMON_COVER / EXACT_CENTRAL_HOLONOMY_OBSTRUCTION / PRIOR_ART_COMPATIBLE / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`

Research unit: `EM-FREE-F6D046-R3-X0-6-COMMON-COVER-HOLONOMY`

Blindness status: `ANCHOR_EXPOSED / PHASE-B CONTINUATION`

Author/program signature: `YUAN X / Enterprise Math`

## 0. 本轮闭合结论

前一研究单元已经证明：

- signature \(4\)、\(a=\tfrac14\) 与 signature \(3\)、\(a=\tfrac13\) 的裸一阶喷流都落在同一个 \(B\neq0\) 轨道；
- 保留各自 Gauss 周期方程后，二者不能由任一方向的直接二次拉回连接；
- 尚未闭合的问题是：是否存在第三个局部系统作为共同覆盖，并在其上比较两条 \(1/\pi\) 协向量。

本轮给出完整答案。

1. **最小项目化共同覆盖存在。**  
   signature \(4\) 周期系统对应 \(X_0(2)\)，signature \(3\) 周期系统对应 \(X_0(3)\)。二者的标准最小 congruence 共同覆盖是
   \[
   X_0(2)\xleftarrow[\deg 4]{}X_0(6)\xrightarrow[\deg 3]{}X_0(3).
   \]
   覆盖双次数 \((4,3)\) 由 orbifold Euler 特征强制为最小正整数解。

2. **两个项目化周期系统在 \(X_0(6)\) 上相同，但线性周期系统并不直接相同。**  
   二者都约化到同一个四尖点 Picard–Fuchs 方程 \(L_6h=0\)，但 signature \(4\) 一侧额外带有
   \[
   \sqrt{D(t)},\qquad D(t)=t^2+12t+24
   \]
   的二次符号局部系统。围绕 \(D\) 的任一根解析延拓，乘子变为 \(-1\)。

3. **严格线性等价需要再取一个二次覆盖。**  
   在
   \[
   \widetilde X:\quad s^2=D(t)
   \]
   上该符号 character 被消去。此二次覆盖仍为 genus \(0\)，并给出显式有理参数；由此得到覆盖双次数 \((8,6)\) 的严格线性化 span。这里的“最小”是指在已确定的 \(X_0(6)\) congruence span 上消去该非平凡二次 character 所需的最小附加次数。

4. **Clausen 平方精确消去中心符号。**  
   两个 \({}_3F_2\) 系统在 \(X_0(6)\) 上已经由一个有理函数作 meromorphic gauge 等价：
   \[
   \widehat F_4(t)=
   \frac{3D(t)}{2(t+6)^2}\widehat F_3(t).
   \]
   这是因为 symmetric square 将 \(-1\) 中心 holonomy 平方为 \(+1\)。

5. **两条具体 Ramanujan 公式被拉回到同一个 \(H(t)^2\) 系统，但位于不同基点。**  
   两个基点的 \(j\)-值一正一负，故不可能是共同覆盖上的同一点。它们的 \(1/\pi\) 协向量可分别显式写成共同喷流基
   \[
   \bigl(H(t)^2,\Theta_tH(t)^2\bigr)
   \]
   上的行向量，并经 110 位数值检查同时给出 \(1/\pi\)。

6. **不存在非零的全局平坦协向量。**  
   \(\Gamma_0(6)\) 中两个非共线抛物元已经把 rank \(2\) 及其 symmetric square 的共同固定协向量空间压为零。因此，跨不同基点的完整局部系统协向量比较必然依赖路径；Clausen 平方只消掉中心 \(\mathbf Z/2\) twist，并没有消掉 \(\Gamma_0(6)\) 的非平凡 monodromy。

因此，本轮的精确分类是：

\[
\boxed{
\begin{array}{c|c}
\text{层级}&\text{跨 signature 关系}\\ \hline
\text{项目化 rank-2 周期系统}&X_0(6)\text{ 上相同}\\
\text{线性 rank-2 周期系统}&\mathbf Z/2\text{ character twist}\\
\text{二次线性化覆盖 }s^2=D&\text{严格 gauge 相同}\\
\text{rank-3 Clausen / }{}_3F_2&X_0(6)\text{ 上有理 gauge 相同}\\
\text{两条具体 }1/\pi\text{ 协向量}&\text{共同系统、不同基点、无路径无关全局同一化}
\end{array}
}
\]

这不是新公理。它是经典混合 signature 模对应、Picard–Fuchs 拉回、局部指数和 holonomy 的派生闭合。

---

## 1. 两个周期系统

记

\[
U_4(x)={}_2F_1\!\left(\frac14,\frac34;1;x\right),
\qquad
U_3(y)={}_2F_1\!\left(\frac13,\frac23;1;y\right).
\]

它们满足

\[
x(1-x)u''+(1-2x)u'-\frac{3}{16}u=0,
\]

\[
y(1-y)v''+(1-2y)v'-\frac{2}{9}v=0.
\]

局部指数差分别为

\[
(0,0,\tfrac12),
\qquad
(0,0,\tfrac13),
\]

故项目化 monodromy orbifold 分别具有型

\[
(\infty,\infty,2),\qquad(\infty,\infty,3).
\]

经典模解释把它们分别放在 \(X_0(2)\) 与 \(X_0(3)\) 上。

---

## 2. 最小项目化共同覆盖

### 2.1 Euler 特征强制的最小双次数

两个 orbifold 的 Euler 特征是

\[
\chi_4
=
2-2-\left(1-\frac12\right)
=-\frac12,
\]

\[
\chi_3
=
2-2-\left(1-\frac13\right)
=-\frac23.
\]

若连通 orbifold \(Y\) 同时以次数 \(d_4,d_3\) 覆盖二者，则

\[
\chi(Y)=d_4\chi_4=d_3\chi_3.
\]

因此

\[
-\frac{d_4}{2}=-\frac{2d_3}{3},
\qquad
3d_4=4d_3.
\]

最小正整数解为

\[
\boxed{(d_4,d_3)=(4,3).}
\]

另一方面，

\[
\Gamma_0(2)\cap\Gamma_0(3)=\Gamma_0(6),
\]

且标准指数为

\[
[\Gamma_0(2):\Gamma_0(6)]=4,
\qquad
[\Gamma_0(3):\Gamma_0(6)]=3.
\]

所以 \(X_0(6)\) 达到该下界。

这里的 \((4,3)\) 是两侧代数覆盖的双次数；在“同一个 \(\tau\)”的混合模变换术语中，它对应 degree \(1\) 的 signature-\(4\)/signature-\(3\) 变换，二者不可混淆。

### 2.2 显式 \(X_0(6)\) 参数

取 \(t=t_6\)。定义

\[
\boxed{
\alpha_4(t)
=
\frac{t(t+8)^3}{(t^2+12t+24)^2},
}
\]

\[
\boxed{
\alpha_3(t)
=
\frac{t(t+9)^2}{(t+6)^3}.
}
\]

于是

\[
1-\alpha_4(t)
=
\frac{64(t+9)}{(t^2+12t+24)^2},
\]

\[
1-\alpha_3(t)
=
\frac{27(t+8)}{(t+6)^3}.
\]

第一张映射次数为 \(4\)，第二张映射次数为 \(3\)。

它们的 ramification passport 为

\[
\alpha_4:
\quad
0:(1,3),\quad
1:(1,3),\quad
\infty:(2,2),
\]

\[
\alpha_3:
\quad
0:(1,2),\quad
1:(1,2),\quad
\infty:(3).
\]

因此 \(X_0(6)\) 的四个 cusp 可取

\[
t=0,-8,-9,\infty,
\]

而 signature \(4\) 的 order-\(2\) 项目化椭圆点被两个二重分歧点消去，signature \(3\) 的 order-\(3\) 项目化椭圆点被 \(t=-6\) 的三重分歧消去。

### 2.3 共同 \(j\)-映射及混合模方程

两种 signature 的 \(j\)-函数分别写成

\[
j_4(x)=
\frac{64(1+3x)^3}{x(1-x)^2},
\]

\[
j_3(y)=
\frac{27(1+8y)^3}{y(1-y)^3}.
\]

直接代入得到

\[
\boxed{
j_4(\alpha_4(t))
=
j_3(\alpha_3(t))
=
\frac{(t+6)^3(t^3+18t^2+84t+24)^3}
{t(t+8)^3(t+9)^2}.
}
\]

消去 \(t\) 后，混合 signature 模关系可紧写为

\[
\boxed{
64(1+3x)^3y(1-y)^3
=
27(1+8y)^3x(1-x)^2.
}
\]

该关系对 \(x=\alpha_4(t)\)、\(y=\alpha_3(t)\) 恒等成立。

---

## 3. 两个拉回方程约化为同一 \(L_6\)

置

\[
D(t)=t^2+12t+24.
\]

定义拉回周期

\[
u_4(t)=U_4(\alpha_4(t)),
\qquad
u_3(t)=U_3(\alpha_3(t)).
\]

### 3.1 signature \(3\) 拉回

直接链式拉回得到

\[
u_3''
+
\frac{t^3+18t^2+132t+432}
{t(t+6)(t+8)(t+9)}u_3'
-
\frac{24}{t(t+6)^2(t+8)}u_3
=0.
\]

令

\[
u_3(t)=\frac{t+6}{6}H(t).
\]

则 \(H\) 满足

\[
\boxed{
L_6H
=
H''
+
\left(
\frac1t+\frac1{t+8}+\frac1{t+9}
\right)H'
+
\frac{t+6}{t(t+8)(t+9)}H
=0.
}
\]

在 \(t=0\) 的全纯支上，

\[
H(0)=1.
\]

### 3.2 signature \(4\) 拉回

直接拉回得到

\[
u_4''
+
\frac{t^4+24t^3+204t^2+816t+1728}
{t(t+8)(t+9)D(t)}u_4'
-
\frac{108(t+8)}
{t(t+9)D(t)^2}u_4
=0.
\]

令

\[
u_4(t)=\sqrt{\frac{D(t)}{24}}\,\widetilde H(t).
\]

以

\[
\frac{r'}r=\frac{D'}{2D},
\qquad
\frac{r''}r=\frac{D''}{2D}-\frac{(D')^2}{4D^2}
\]

作精确 gauge 变换，得到 \(\widetilde H\) 满足完全相同的 \(L_6\widetilde H=0\)。

在 \(t=0\) 选择平方根使 \(\sqrt{D(0)/24}=1\)，并取全纯归一化支，则

\[
\widetilde H(0)=H(0)=1.
\]

由同一二阶方程的局部唯一性，

\[
\boxed{
u_3(t)=\frac{t+6}{6}H(t),
}
\]

\[
\boxed{
u_4(t)=\sqrt{\frac{D(t)}{24}}\,H(t).
}
\]

因此

\[
\boxed{
\frac{u_4(t)}{u_3(t)}
=
\sqrt{\frac{3D(t)}{2(t+6)^2}}.
}
\]

这给出了 \(X_0(6)\) 上的显式 mixed-signature period multiplier。

---

## 4. 项目化相同不等于线性相同：中心 \(\mathbf Z/2\) holonomy

### 4.1 signature \(4\) 一侧的两个符号点

\(D\) 的根为

\[
r_\pm=-6\pm2\sqrt3.
\]

它们是 \(\alpha_4(t)=\infty\) 的两个二重分歧点。原 signature \(4\) 方程在 \(\infty\) 的指数为

\[
\left\{\frac14,\frac34\right\}.
\]

二重拉回后，局部指数变为

\[
\left\{\frac12,\frac32\right\}.
\]

故两个局部本征值都为 \(-1\)：项目化 monodromy 已经变成恒等，但线性 monodromy 是

\[
\boxed{-I.}
\]

这正是乘子 \(\sqrt{D(t)}\) 围绕任一 \(r_\pm\) 变号的原因。

相对地，signature \(3\) 的椭圆点在 \(t=-6\) 处作三重拉回，指数

\[
\left\{\frac13,\frac23\right\}
\longmapsto
\{1,2\},
\]

线性 monodromy 已经为 \(+I\)，且该点在除去有理因子 \(t+6\) 后成为普通点。

### 4.2 局部系统陈述

设 \(\mathscr L_4,\mathscr L_3\) 为两个 rank-\(2\) 周期局部系统，\(\mathscr L_6\) 为 \(L_6\) 的局部系统。令 \(\chi_D\) 是由 \(\sqrt D\) 定义的 rank-\(1\) 二次 character，则

\[
\boxed{
\alpha_4^*\mathscr L_4
\simeq
\chi_D\otimes\mathscr L_6,
}
\]

\[
\boxed{
\alpha_3^*\mathscr L_3
\simeq
\mathscr L_6.
}
\]

其 projectivization 满足

\[
\mathbf P(\chi_D\otimes\mathscr L_6)
=
\mathbf P(\mathscr L_6),
\]

所以项目化共同覆盖是 \(X_0(6)\)，但线性共同对象仍差一个不可由单值有理函数消去的中心符号。

### 4.3 严格线性化二次覆盖

取

\[
\boxed{
\widetilde X:\quad s^2=t^2+12t+24.
}
\]

该二次 character 的 kernel cover 正是 \(\widetilde X\)。由于只在两个简单点分歧，Riemann–Hurwitz 给出 genus \(0\)。

取有理参数 \(u\)：

\[
\boxed{
t=
-\frac{2(u^2+2u-5)}{(u-1)(u+1)},
}
\]

\[
\boxed{
s=
-\frac{2(u^2-4u+1)}{(u-1)(u+1)}.
}
\]

可直接验证 \(s^2=D(t)\)。两侧映射变为

\[
\boxed{
\widetilde\alpha_4(u)
=
-\frac{(u^2+2u-5)(3u^2-2u+1)^3}
{(u^2-4u+1)^4},
}
\]

\[
\boxed{
\widetilde\alpha_3(u)
=
-\frac{(u^2+2u-5)(7u^2-4u+1)^2}
{32(u^2-u+1)^3}.
}
\]

其次数分别为 \(8\) 与 \(6\)。

在此覆盖上，

\[
\boxed{
\frac{u_4}{u_3}
=
-\frac{\sqrt6}{4}
\frac{u^2-4u+1}{u^2-u+1},
}
\]

已经是单值有理函数乘一个常数。由于 \(\chi_D\) 是非平凡 order-\(2\) character，任何**经由该 \(X_0(6)\) span** 严格消去它的连通覆盖都必须至少再有次数 \(2\)；上述 \((8,6)\) 构造达到该下界。

---

## 5. Clausen 平方：中心 twist 的偶次消失

记

\[
F_a(z)
=
{}_3F_2\!\left(\frac12,a,1-a;1,1;z\right).
\]

Clausen 恒等式给出

\[
F_a(4x(1-x))
=
{}_2F_1(a,1-a;1;x)^2
\]

（在 \(x=0\) 邻域取标准全纯支）。

定义

\[
Z_4(t)=4\alpha_4(t)(1-\alpha_4(t))
=
\frac{256t(t+8)^3(t+9)}{D(t)^4},
\]

\[
Z_3(t)=4\alpha_3(t)(1-\alpha_3(t))
=
\frac{108t(t+8)(t+9)^2}{(t+6)^6}.
\]

令

\[
S(t)=H(t)^2.
\]

则

\[
\boxed{
F_{1/4}(Z_4(t))
=
\frac{D(t)}{24}S(t),
}
\]

\[
\boxed{
F_{1/3}(Z_3(t))
=
\frac{(t+6)^2}{36}S(t).
}
\]

因此

\[
\boxed{
F_{1/4}(Z_4(t))
=
R(t)F_{1/3}(Z_3(t)),
\qquad
R(t)=\frac{3D(t)}{2(t+6)^2}.
}
\]

这是 \(X_0(6)\) 上的单值有理 meromorphic gauge。其 first-jet 矩阵为

\[
\boxed{
T_R(t)=
\begin{pmatrix}
R(t)&0\\
\Theta_tR(t)&R(t)
\end{pmatrix}.
}
\]

### 偶奇 symmetric-power 定理

更一般地，若

\[
\mathscr L'=\chi\otimes\mathscr L,
\qquad
\chi^2=1,
\]

则

\[
\operatorname{Sym}^m\mathscr L'
\simeq
\chi^m\otimes\operatorname{Sym}^m\mathscr L.
\]

故

\[
\boxed{
\operatorname{Sym}^{2k}\mathscr L'
\simeq
\operatorname{Sym}^{2k}\mathscr L,
}
\]

而

\[
\boxed{
\operatorname{Sym}^{2k+1}\mathscr L'
\simeq
\chi\otimes\operatorname{Sym}^{2k+1}\mathscr L.
}
\]

Ramanujan 的 \({}_3F_2\) 层是 rank-\(2\) 周期的 symmetric square，因而无法看见 \(\chi_D\)。这说明：

\[
\boxed{
\text{平方可保留数值恒等式，却会不可逆地抹去中心符号 holonomy。}
}
\]

---

## 6. 两条 \(1/\pi\) 协向量拉回共同 \(S=H^2\) 系统

### 6.1 原始协向量

signature \(4\) 的 Wronskian 归一化为

\[
\frac{\sin(\pi/4)}{\pi}
=
\left(
\frac{2206}{9801}
+
\frac{52780}{9801}\Theta_{Z_4}
\right)F_{1/4}(Z_4).
\]

signature \(3\) 的 Wronskian 归一化为

\[
\frac{\sin(\pi/3)}{\pi}
=
\left(
\frac{827}{3000}
+
\frac{14151}{3000}\Theta_{Z_3}
\right)F_{1/3}(Z_3).
\]

### 6.2 通用拉回公式

若

\[
F(Z(t))=q(t)S(t),
\qquad
\kappa(t)=\frac{Z(t)}{tZ'(t)},
\]

则

\[
\Theta_Z=\kappa(t)\Theta_t
\]

并且

\[
\boxed{
(A+B\Theta_Z)(qS)
=
\bigl(Aq+B\kappa\Theta_tq\bigr)S
+
B\kappa q\,\Theta_tS.
}
\]

因此共同喷流基 \((S,\Theta_tS)\) 上的协向量是

\[
\boxed{
C(t)=
\left(
Aq+B\kappa\Theta_tq,\;
B\kappa q
\right).
}
\]

本题中

\[
q_4(t)=\frac{D(t)}{24},
\qquad
q_3(t)=\frac{(t+6)^2}{36},
\]

\[
\boxed{
\kappa_4(t)
=
-\frac{(t+8)(t+9)D(t)}
{3(t^2+8t-8)(t^2+16t+72)},
}
\]

\[
\boxed{
\kappa_3(t)
=
-\frac{(t+6)(t+8)(t+9)}
{2(t+12)(t^2+6t-18)}.
}
\]

且

\[
\Theta_tq_4=\frac{t(t+6)}{12},
\qquad
\Theta_tq_3=\frac{t(t+6)}{18}.
\]

要得到 \(1/\pi\) 归一化，只需分别把 Wronskian 行向量乘以

\[
\sqrt2,\qquad\frac2{\sqrt3}.
\]

### 6.3 两个算术基点

signature \(4\) 的 Ramanujan 点满足

\[
\alpha_4(t_4^*)
=
\frac12-\frac{910\sqrt{29}}{9801},
\]

signature \(3\) 的点满足

\[
\alpha_3(t_3^*)
=
\frac12-\frac{53\sqrt{89}}{1000}.
\]

取靠近 \(t=0\) 的根：

\[
\boxed{
t_4^*
\approx
2.92786976334236543105849079522\times10^{-9},
}
\]

\[
\boxed{
t_3^*
\approx
-2.66666202470228072032889840979\times10^{-6}.
}
\]

它们也分别是以下有理整系数方程的近零根：

\[
99^4\cdot256t(t+8)^3(t+9)-D(t)^4=0,
\]

\[
250000\cdot108t(t+8)(t+9)^2+(t+6)^6=0.
\]

### 6.4 共同系统中的数值行向量

将 \(1/\pi\) 协向量写成

\[
D_r(t)=\bigl(D_{r,0}(t),D_{r,1}(t)\bigr)
\]

作用于

\[
\binom{S(t)}{\Theta_tS(t)},
\]

则在两个算术点：

\[
\boxed{
D_4(t_4^*)
\approx
(0.318309890055450954954747829690,\;
7.61577311112871190628056559049),
}
\]

\[
\boxed{
D_3(t_3^*)
\approx
(0.318307323957320547160891526922,\;
5.44670811671826477983919362751).
}
\]

同时

\[
S(t_4^*)
\approx0.999999999512021706308041440838,
\]

\[
\Theta_tS(t_4^*)
\approx-4.87978293493522879890\times10^{-10},
\]

以及

\[
S(t_3^*)
\approx1.00000044444383539225117786361,
\]

\[
\Theta_tS(t_3^*)
\approx4.44444000000846210416\times10^{-7}.
\]

两次配对均给出

\[
\boxed{
D_r(t_r^*)
\binom{S(t_r^*)}{\Theta_tS(t_r^*)}
=
\frac1\pi
}
\]

至超过 \(90\) 位。

---

## 7. 两个具体基点不重合

若两个给定 Ramanujan 点是 \(X_0(6)\) 上同一点的两侧像，则它们必须具有相同 \(j\)-值。

但直接计算：

\[
j_4\!\left(
\frac12-\frac{910\sqrt{29}}{9801}
\right)
\approx
2.4591258496000008\times10^{10}>0,
\]

\[
j_3\!\left(
\frac12-\frac{53\sqrt{89}}{1000}
\right)
\approx
-2.699929800726296\times10^7<0.
\]

故

\[
\boxed{
j_4(\alpha_4^*)\ne j_3(\alpha_3^*).
}
\]

所以共同覆盖并没有把两条既定公式变成“同一点的两个坐标表达”；它只把它们放进了同一个可运输的局部系统族。两个协向量仍位于不同 fiber。

---

## 8. 全局平坦协向量的严格 no-go

### 8.1 rank \(2\)

在标准 period basis 中，\(\Gamma_0(6)\) 含有两个抛物元

\[
T=
\begin{pmatrix}
1&1\\0&1
\end{pmatrix},
\qquad
U=
\begin{pmatrix}
1&0\\-6&1
\end{pmatrix}.
\]

若行向量 \(\lambda=(a,b)\) 同时满足

\[
\lambda T=\lambda,
\qquad
\lambda U=\lambda,
\]

第一式给出 \(a=0\)，第二式继而给出 \(b=0\)。因此

\[
\boxed{
(\mathscr L_6^\vee)^{\Gamma_0(6)}=0.
}
\]

### 8.2 symmetric square

在基 \((x^2,xy,y^2)\) 中，

\[
\operatorname{Sym}^2(T)
=
\begin{pmatrix}
1&2&1\\
0&1&1\\
0&0&1
\end{pmatrix},
\]

\[
\operatorname{Sym}^2(U)
=
\begin{pmatrix}
1&0&0\\
-6&1&0\\
36&-12&1
\end{pmatrix}.
\]

设 \(\Lambda=(p,q,r)\) 同时被二者固定。第一式强制

\[
p=q=0,
\]

第二式再强制

\[
r=0.
\]

故

\[
\boxed{
\left(\operatorname{Sym}^2\mathscr L_6^\vee\right)^{\Gamma_0(6)}
=0.
}
\]

这给出两个层次的区别：

- distinguished holomorphic section \(H^2\) 可以在选定支上解析延拓并用于数值恒等式；
- 但完整 rank-\(3\) 局部系统不存在非零全局水平协向量，因而不同基点 fiber 之间不存在路径无关的协向量同一化。

绕不同路径运输时，差异由 \(\Gamma_0(6)\) monodromy 给出。中心 \(\chi_D\) 只是其中在 rank-\(2\) 两种 signature 比较中额外出现、又被平方消掉的一层。

---

## 9. 对 P000 六维切片粘合的精确影响

本轮不修改 P000，也不声称 rank-\(2\) 模曲线就是六维空间本身。得到的是对切片数据类型的进一步约束。

### 9.1 至少需要四层数据

一个可用于 P000 多切片拼接的 Ramanujan 周期对象至少应区分：

\[
\boxed{
\text{PROJECTIVE PERIOD SYSTEM}
}
\]

\[
\boxed{
+\ \text{LINEAR LIFT / CENTRAL CHARACTER}
}
\]

\[
\boxed{
+\ \text{SYMMETRIC-POWER OBSERVABLE}
}
\]

\[
\boxed{
+\ \text{BASEPOINT AND PATH/HOLONOMY DATA}.
}
\]

仅保留 \({}_3F_2\) 数值和一阶系数会看不见 \(\chi_D\)；仅保留项目化系统也看不见 \(-I\) 中心 monodromy；仅给定同一个共同覆盖仍不能把不同基点的协向量规范地认作同一个。

### 9.2 与全局 branch typing 的相容性

本题提供了一个精确实例：

\[
\text{signed/phase carrier}
\longrightarrow
\text{symmetric square}
\longrightarrow
\text{sign-erased observable}.
\]

因此：

\[
\boxed{
\text{相同的正值／平方读出}
\not\Rightarrow
\text{相同的带符号线性来源}.
}
\]

这与项目的全局类型纪律相容：signed/amplitude 信息不能从正的、平方化的或 Boolean 读出中反推回来。

---

## 10. 公理门、先行工作与方法审计

### 10.1 公理门

本轮分类：

\[
\boxed{
\texttt{DERIVED\_COMMON\_COVER}
}
\]

\[
\boxed{
\texttt{EXACT\_CENTRAL\_HOLONOMY\_OBSTRUCTION}
}
\]

\[
\boxed{
\texttt{NOT\_NEW\_AXIOM / NOT\_FOUNDATION}.
}
\]

父候选继续保持：

\[
\texttt{REJECT\_AS\_NEW\_AXIOM}.
\]

理由：

- \(X_0(6)\) 的覆盖映射与混合 signature 模变换属于经典模曲线框架；
- 共同 Picard–Fuchs 方程来自直接拉回与 gauge 约化；
- \(\mathbf Z/2\) twist 来自局部指数和平方根解析延拓；
- symmetric-power 偶奇律是张量函子的直接结论；
- 固定协向量 no-go 是显式 monodromy 线性代数。

### 10.2 先行文献边界

Robert S. Maier 的 *On Rationally Parametrized Modular Equations* 系统说明：

- signature \(4,3,2\) 分别与 \(X_0(2),X_0(3),X_0(4)\) 对应；
- 混合 signature 模方程来自这些群的有限指数交；
- \(X_0(6)\) 到 \(X_0(2),X_0(3)\) 的 Hauptmodul 映射是有理的；
- \(h_6\) 满足本文使用的四奇点 Picard–Fuchs 方程。

因此本文不把共同覆盖或 mixed modular transformation 本身作为新颖性主张。保留价值是把它们与前两轮的“喷流协向量—方程刚化—holonomy”框架精确接合，并显式分离：

\[
\text{projective equality},
\quad
\text{linear sign twist},
\quad
\text{symmetric-square erasure},
\quad
\text{basepoint transport obstruction}.
\]

### 10.3 Enterprise tool reuse

覆盖审计命中：

- `T9_HOLONOMY_COCOYCLE_GLUING`;
- `holonomy.precision_defect_transport`;
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`.

复用决议：

- `T9`: `REUSE_APPLIED`。使用 loop holonomy、strict-globalization no-go 和 fixed-vector obstruction；严格遵守“非零 holonomy 只诊断严格平凡化失败，不自动给出唯一修复对象”的边界。
- `T7`: `REUSE_APPLIED`。使用共同固定子空间计算；未从缺失固定点推出额外几何结构。
- 新验证脚本：`RESULT_ONLY`，不是新的通用工具家族。

---

## 11. 验证

无第三方依赖验证器：

```bash
python scripts/verify_em_free_f6d046_x0_6_common_cover.py
```

检查覆盖：

1. 两个 \(\alpha\)-映射及补值的精确因式分解；
2. 覆盖次数 \(4,3\)；
3. 两侧 \(j\)-映射完全相等；
4. 混合模方程；
5. \(Z_4,Z_3\) 与 Euler-Jacobian \(\kappa_4,\kappa_3\)；
6. 两个 Gauss 方程的精确拉回；
7. 两侧 gauge 后都严格等于 \(L_6\)；
8. rational squared-period gauge；
9. 二次严格线性化 cover 及其 \(8,6\) 显式映射；
10. orbifold Euler 特征最小双次数；
11. rank-\(2\) 与 symmetric-square 固定协向量空间为零；
12. 两个算术基点、共同系统行向量及 \(1/\pi\) 高精度评价。

结果：

\[
\boxed{\texttt{all\_passed=true},\qquad 37/37.}
\]

---

## 12. 下一前沿

本轮已经闭合“共同覆盖是否存在、两侧是相等还是 gauge、是否出现 holonomy”的全部三分支：

\[
\boxed{
\text{项目化共同覆盖存在}
\;+\;
\text{线性层有非平凡 }\mathbf Z/2\text{ twist}
\;+\;
\text{平方层有理 gauge 相同}
\;+\;
\text{不同基点运输仍有 }\Gamma_0(6)\text{ holonomy}.
}
\]

下一最小研究单元是：

\[
\boxed{
\text{在 signatures }2,3,4\text{ 的共同 }X_0(12)\text{ atlas 上，}
}
\]

构造所有两两中心 characters 的 Čech \(1\)-cocycle，检验其是否：

1. 在三重交叠上满足严格 cocycle 条件；
2. 可由单个 rank-\(1\) twist 同时平凡化；
3. 在偶 symmetric powers 中统一消失、在奇 powers 中形成非平凡 parity obstruction；
4. 能否作为 P000 六维切片粘合中“线性 lift 数据不可由平方读出恢复”的最小离散标签。

该后继仍属于 derived local-system research，不预设也不承诺产生新公理。
