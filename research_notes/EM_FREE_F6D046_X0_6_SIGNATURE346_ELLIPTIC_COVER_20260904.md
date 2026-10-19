# X0(6) 上 signatures 3/4/6 的显式 genus-1 项目化共同覆盖、中心 characters 与 genus-9 严格线性化

Status: `FREE_RESEARCH / DERIVED_EXPLICIT_ELLIPTIC_COMMON_COVER / EXACT_LINEARIZATION / CORRECTED_SIGNATURE6_MARKING / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`
Research unit: `EM-FREE-F6D046-R8-X0-6-SIGNATURE346-ELLIPTIC-COVER`
Blindness status: `ANCHOR_EXPOSED / PHASE-B CONTINUATION`

## 0. 闭合结论

R3 已把 signatures 4 与 3 的 Gauss 周期系统共同放在 `X0(6)` 上。令

\[
P(t)=t^3+18t^2+84t+24,
\qquad
A(t)=(t+6)P(t),
\]

\[
D_6(t)=t(t+8)^3(t+9)^2,
\]

则共同 `j`-映射为

\[
 j_6(t)=\frac{A(t)^3}{D_6(t)}.
\]

本轮发现并精确验证 sextic

\[
Q(t)=t^6+36t^5+504t^4+3384t^3+10584t^2+11232t-1728
\]

满足

\[
\boxed{A(t)^3-Q(t)^2=1728D_6(t).}
\]

因此

\[
1-\frac{1728}{j_6(t)}=\frac{Q(t)^2}{A(t)^3}.
\]

signature 6 所需 quadratic projective base-change 由显式曲线

\[
\boxed{E_{346}:\quad v^2=A(t)}
\]

实现。`A` 是 squarefree quartic，故紧化的 `E_{346}` 是 genus `1`。选择 `v(0)=-12` 的局部分支，并令

\[
s=\frac{Q(t)}{v^3},
\qquad
w=\frac{1-s}{2},
\]

则

\[
\boxed{4w(1-w)=\frac{1728}{j_6(t)}.}
\]

所以 `E_{346}` 是标准 `j`-marking 下 signatures `3,4,6` 的显式最小 projective common cover。

在该椭圆底面上仍有两个独立 quadratic linear characters：

1. signature `4/3` 的 character，由 `sqrt(D(t))` 给出，其中 `D(t)=t^2+12t+24`；其 pullback branch set 有四点；
2. signature `6/3` 的 character，由 `sqrt(-v/12)` 给出；其 branch set 是 `v=0` 的四个 ramification points。

两组分支点不交，characters 独立。因此最小 strict rank-2 common cover 是

\[
\boxed{
 v^2=A(t),\qquad q^2=\frac{D(t)}{24},\qquad r^2=-\frac{v}{12}.
}
\]

它在 `E_{346}` 上次数 `4`，在 `X0(6)` 上总次数 `8`；紧化 genus 为

\[
\boxed{g=9.}
\]

这给出了之前“genus 9”数字的正确、无条件位置：它属于 signatures `3/4/6` 在 `X0(6)` 上的严格线性共同覆盖，而不是未经 projective base-change 的四-signature `X0(12)` 模型。

---

## 1. 三个 period carriers 的共同方程

记

\[
U_3(y)={}_2F_1\!\left(\frac13,\frac23;1;y\right),
\]

\[
U_4(x)={}_2F_1\!\left(\frac14,\frac34;1;x\right),
\]

\[
U_6(w)={}_2F_1\!\left(\frac16,\frac56;1;w\right).
\]

R3 的 `X0(6)` 参数为

\[
 y=\alpha_3(t)=\frac{t(t+9)^2}{(t+6)^3},
\qquad
 x=\alpha_4(t)=\frac{t(t+8)^3}{D(t)^2}.
\]

共同二阶 Picard--Fuchs 方程为

\[
L_6H=H''+
\left(\frac1t+\frac1{t+8}+\frac1{t+9}\right)H'
+\frac{t+6}{t(t+8)(t+9)}H=0,
\]

在 `t=0` 取 `H(0)=1` 的全纯支。已有

\[
\boxed{U_3(\alpha_3(t))=\frac{t+6}{6}H(t),}
\]

\[
\boxed{U_4(\alpha_4(t))=\sqrt{\frac{D(t)}{24}}\,H(t).}
\]

signature 6 使用标准二次变换

\[
{}_2F_1\!\left(\frac16,\frac56;1;w\right)
=
{}_2F_1\!\left(\frac1{12},\frac5{12};1;4w(1-w)\right).
\]

而 signature 3 与 universal period 的关系是

\[
U_6(w)=(1+8y)^{1/4}U_3(y),
\qquad
4w(1-w)=\frac{1728}{j_3(y)}.
\]

直接计算

\[
1+8\alpha_3(t)
=
\frac{9P(t)}{(t+6)^3}
=
\frac{9v^2}{(t+6)^4}.
\]

在 `v(0)=-12`、`w(0)=0` 的归一化分支上，

\[
\sqrt{1+8\alpha_3(t)}=-\frac{3v}{(t+6)^2}.
\]

所以

\[
\boxed{
U_6(w(t))=\sqrt{-\frac{v}{12}}\,H(t).
}
\]

该平方根正是 signature `6/3` 的线性 character；它不能在 `E_{346}` 上由单值 meromorphic gauge 消去。

---

## 2. Clausen squares 已在较低层统一

令 `S(t)=H(t)^2`。Clausen 恒等式给出相应 rank-3 carriers：

\[
F_3(Z_3(t))=\frac{(t+6)^2}{36}S(t),
\qquad Z_3=4\alpha_3(1-\alpha_3),
\]

\[
F_4(Z_4(t))=\frac{D(t)}{24}S(t),
\qquad Z_4=4\alpha_4(1-\alpha_4),
\]

\[
F_6(Z_6(t))=-\frac{v}{12}S(t),
\qquad Z_6=4w(1-w)=\frac{1728}{j_6(t)}.
\]

因此 signatures `3/4` 的 Clausen systems 已在 `X0(6)` 上有理 gauge 等价；signature `6` 的 Clausen system在 projective double cover `E_{346}` 上也只差 meromorphic factor `-v/12`。中心 signs 在 symmetric square 中消失，但 projective base-change `v^2=A` 本身不能被“偶次张量”替代。

---

## 3. 椭圆曲线不变量

展开

\[
A(t)=t^4+24t^3+192t^2+528t+144.
\]

其 binary-quartic invariants 为

\[
I=12ae-3bd+c^2=576,
\]

\[
J=72ace+9bcd-27ad^2-27b^2e-2c^3=-34560.
\]

并且

\[
4I^3-J^2=-2^{16}3^8\neq0.
\]

故 `E_{346}` 光滑。其 Jacobian 可取

\[
Y^2=X^3-27IX-27J,
\]

经 `X=36x, Y=216y` 缩放为

\[
\boxed{y^2=x^3-12x+20.}
\]

相应

\[
\boxed{j(E_{346})=-3072,}
\qquad
\Delta=-2^8 3^5.
\]

因为原 quartic 有有理点 `(t,v)=(0,-12)`，它与其 Jacobian 在 `\mathbf Q` 上同构；本轮只使用该同构类型，不依赖某一特定 birational 坐标公式。

---

## 4. character 独立性与 genus 计算

`D=t^2+12t+24` 与 `A` 互素。于是：

- `q^2=D/24` 在 `E_{346}` 上于 `D=0` 的四个点分支；
- `r^2=-v/12` 在 `v=0` 的四个点分支；
- 两个 branch sets 不交。

围绕两类分支点的小环分别检测 `(chi_D,lambda_6)=(-1,+1)` 与 `(+1,-1)`，故联合 character image 为 `(\mathbf Z/2)^2`。任何同时平凡化二者的连通 cover 次数至少 `4`，joint kernel cover 达到下界。

底面 `E_{346}` genus 为 `1`，共有八个 inertia-order-2 branch points。Riemann--Hurwitz：

\[
2g(\widetilde E)-2
=4(2\cdot1-2)+8\cdot4\left(1-\frac12\right)
=16.
\]

故

\[
\boxed{g(\widetilde E)=9.}
\]

---

## 5. 三层结构与最小性边界

必须区分：

1. `X0(6)`：signatures `3/4` 的 projective common base；
2. `E_{346}:v^2=A`：加入 signature `6` 所需的最小标准-`j` projective base-change；
3. `q^2=D/24, r^2=-v/12`：消去两个 linear characters 的 strict common cover。

最小性限于：保留标准 `j`-marking；signature 6 经 `4w(1-w)=1728/j` 接入；比较完整 rank-2 linear local systems；covers 连通并允许 algebraic branching。改变 marking、使用非标准 correspondence 或只比较单点函数芽，不受本结论约束。

---

## 6. 对 Wronskian / 1-pi 解释的影响

Wronskian 位于 `\wedge^2` determinant line，quadratic characters 以平方作用，所以 `chi_D` 与 `lambda_6` 都不可见。这解释了为什么 signatures `3/4/6` 可以共享归一化辛面积机制，同时 period vectors 仍需 genus-9 strict cover 才能共同线性化。

因此：

\[
\boxed{
\text{COMMON WRONSKIAN / CLAUSEN DATA}
\not\Rightarrow
\text{COMMON LINEAR PERIOD TRIVIALIZATION}.
}
\]

---

## 7. P000 与公理门

本结果只构造 rank-2/rank-3 模周期局部系统的显式共同覆盖，不决定 P000 六维补空间、完整旋转群或切片耦合。椭圆曲线的 genus 也不是 Enterprise 空间维数。

工具复用：

- `T9_HOLONOMY_COCOYCLE_GLUING`: `REUSE_APPLIED`；
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: `COMPOSE_APPLIED`；
- 新工具：`NO_NEW_TOOL_FAMILY / RESULT_ONLY`。

公理门：

`DERIVED_EXPLICIT_ELLIPTIC_COMMON_COVER / EXACT_LINEARIZATION / PRIOR_ART_TRANSFORMATION_SPECIALIZATION / NOT_NEW_AXIOM / NOT_FOUNDATION`。
