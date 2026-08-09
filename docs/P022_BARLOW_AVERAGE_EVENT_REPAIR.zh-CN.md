# P022 — 微观平均事件修复是次线性的

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE MEAN / ANALYTIC ASYMPTOTIC / NOVELTY_UNVERIFIED`  
归属：`program/p022-geometry-v2`

## 核心结论

长度为 `N` 的双侧 Barlow 微观窗口含有 `2N` 个符号位。coordination-history 商只在两类事件处丢失标签：绝对通道离开零点时产生 orientation repair，等绝对通道分叉时产生 side-label repair。

若 `E` 为零点 excursion 方向修复数，`B` 为 diagonal split 数，则精确修复维数为

\[
r=E+B.
\]

最坏情形为 `N+1`，但对全部 `4^N` 个有序双侧微观窗口做等权平均，修复量只有平方根量级。

令

\[
m=\left\lfloor\frac{N-1}{2}\right\rfloor.
\]

单侧 orientation 平均为

\[
\boxed{
E_N^{(1)}=(2m+1)\frac{\binom{2m}{m}}{4^m}.
}
\]

双侧 diagonal-split 平均为

\[
\boxed{
D_N=
\sum_{t=1}^{N-1}
\frac{\binom{2t}{t}-\mathbf1_{2\mid t}\binom{t}{t/2}^2}{4^t}.
}
\]

因此总平均修复为

\[
\boxed{
\overline r_N=2E_N^{(1)}+D_N.
}
\]

进一步利用中心二项式渐近式得到

\[
\boxed{
\overline r_N
=2(1+\sqrt2)\sqrt{\frac N\pi}
-\frac{\log N}{\pi}
+O(1).
}
\]

故

\[
\boxed{\overline r_N=\Theta(\sqrt N),}
\qquad
\boxed{\frac{\overline r_N}{2N}\to0.}
\]

也就是说，尽管精确最坏修复仍然线性增长，等权微观平均下所需的附加精确修复只占原始两侧符号历史的渐近零比例。

负的 `-(log N)/pi` 修正来自两个通道同时回到零点时的重叠修正：该状态位于墙交点，但不构成非零 diagonal split。

## 边界

该结论描述的是**在已经保留 coordination history 的前提下**，恢复带标签微观 lift 所需的附加 repair；不能把它误说成整个系统总存储成本只有 `Theta(sqrt N)`。

此外，平均为 `Theta(sqrt N)` 不意味着修复量集中在某一个确定的平方根预算附近。现有 orientation 二阶矩定理已经证明其标准差同样是 `Theta(sqrt N)`；总 repair 的精确方差仍需控制 orientation 与 diagonal-split 两类墙事件之间的协方差。

## 几何解释

将两条 signed drift `S_t,T_t` 做整数变换

\[
U_t=(S_t+T_t)/2,
\qquad
V_t=(S_t-T_t)/2,
\]

可得到标准 `Z^2` cardinal walk。orientation repair 对应两条对角反射墙 `U=V`、`U=-V` 的墙局部时间，side-label repair 对应非零坐标轴 `U=0`、`V=0` 的离墙事件。因此上述平方根平均律是一个 `B_2/C_2` 四墙随机游走统计。

## 可执行资产

- `src/enterprise_math/p022_barlow_average_repair.py`
- `tests/test_p022_barlow_average_repair.py`

短 horizon 已与全部微观窗口直接枚举交叉核对。经典随机游走、中心二项式和调和和渐近均属于既有数学；这里的项目特化是它们与 Barlow 精确修复状态之间的对应。
