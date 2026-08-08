# P019 —— 纠错补充 04：因果相位不能被有限精度幅度吞掉

状态：`ACTIVE CORRECTION / SUPERSEDING INTERPRETATION NOTE`  
修正对象：P019 第一阶段中把 `q_lambda=0` 的有限宽度区域直接称作“视界盆地”的过强物理解读  
数学公式状态：第一阶段关于 `q_lambda=0` 区间、宽度、projection 与 singleton threshold 的算术结论仍成立；被修正的是它们的**物理语义**。

## 1. 核心纠错

第一阶段定义了

\[
q_\lambda(n;h)
=
\left\lfloor\frac{\lambda|n-h|}{n}\right\rfloor.
\]

并证明

\[
H_\lambda(h)=\{n:q_\lambda(n;h)=0\}
\]

是一个有限整数区间。

这个集合确实存在，也确实随 precision 收缩。

但把它直接解释为“有限精度下事件视界本身变厚”是不充分的，因为绝对值已经删除了最重要的因果信息：

\[
\boxed{
\epsilon(n;h)=\operatorname{sgn}(n-h).
}
\]

对 `n<h`、`n=h`、`n>h`，即使 `q_lambda` 全部坍缩到 `0`，`epsilon` 仍分别是

\[
-1,\quad0,\quad+1.
\]

因此必须修正为：

> **`H_lambda(h)` 是零可分辨“幅度/钟速”盆地，不自动等于因果 horizon。精确 horizon 首先由 phase boundary 决定。**

## 2. P019-PM-T01 —— 正确的 finite-precision state 是 phase × magnitude，而不是带符号乘积

状态：`PROVED / DESIGN CORRECTION`

定义

\[
\boxed{
O_\lambda(n;h)
=
(\epsilon(n;h),q_\lambda(n;h)).
}
\]

必须保存 ordered pair，而不能只保存

\[
\epsilon q.
\]

因为当

\[
q=0
\]

时，乘积会把

\[
(-1,0),\quad(0,0),\quad(+1,0)
\]

全部压成同一个整数 `0`。

这与 P006 已经发现的“方向/符号与非负 magnitude 必须分离”完全一致。

因此 P019 的最小 typed state 应采用：

\[
\boxed{
\text{phase channel}
\times
\text{precision magnitude channel}.
}
\]

## 3. P019-PM-T02 —— Schwarzschild 精确 horizon 在任意 precision 下都是唯一零 phase vertex

状态：`PROVED`

由定义：

\[
\epsilon(n;h)=0
\iff
n=h.
\]

并且

\[
q_\lambda(h;h)=0.
\]

因此对任意正 `lambda`：

\[
\boxed{
O_\lambda(n;h)=(0,0)
\iff
n=h.
}
\]

所以**精确 phase boundary 不会因为有限 magnitude precision 而变成厚顶点集合。**

真正变厚的是：

\[
\boxed{
\{n:\text{magnitude channel}=0\}=H_\lambda(h).
}
\]

这个集合可同时包含：

- inner phase `(-1,0)`；
- exact horizon `(0,0)`；
- outer phase `(+1,0)`。

## 4. P019-PM-C01 —— Clock state `K=0` 不推出“位于 horizon”

状态：`COUNTEREXAMPLE TO STRONG CLOCK-HORIZON IDENTIFICATION`

平方 precision 下：

\[
K_\sigma(n;h)=R_2(q_{\sigma^2}(n;h)).
\]

因为 `q` 是非负整数：

\[
K_\sigma=0
\iff
q_{\sigma^2}=0.
\]

取

\[
\sigma=2,\qquad h=10.
\]

则

\[
K_2(9;10)=K_2(10;10)=K_2(11;10)=0.
\]

但 phase 分别为

\[
-1,\quad0,\quad+1.
\]

因此：

\[
\boxed{
K=0\not\Rightarrow\text{horizon phase}=0
}
\]

在 coarse precision 下明确成立。

第一阶段的 singleton threshold

\[
\lambda\ge h+1
\]

现在应重新解释为：

> **这是“零 magnitude/clock basin 收缩到唯一 phase boundary”的有限 completeness threshold， وليس“事件视界从厚变薄”的本体阈值。**

## 5. P019-PM-C02 —— 相同非零 clock state 也不能决定因果方向

状态：`COUNTEREXAMPLE`

取

\[
\sigma=2,\qquad h=3.
\]

则

\[
K_2(2;3)=1,
\qquad
K_2(4;3)=1.
\]

但

\[
\epsilon(2;3)=-1,
\qquad
\epsilon(4;3)=+1.
\]

所以即使 clock magnitude 非零：

\[
\boxed{
K\text{ alone does not determine causal phase.}
}
\]

这直接阻止我们把“时间流速值”当作完整的空间方向状态。

## 6. P019-PM-T03 —— Charged model 也必须保存 `sign(P)` 与 `g_lambda` 两条通道

状态：`PROVED`

RN 阶段定义

\[
g_\lambda(n;a,b)
=
\left\lfloor\frac{\lambda|P(n)|}{n^2}\right\rfloor.
\]

正确 typed observation 应是

\[
\boxed{
O^{RN}_\lambda(n)
=
(\operatorname{sgn}P(n),g_\lambda(n)).
}
\]

因为 magnitude channel 使用绝对值，它不可能自行恢复正/负 causal phase。

取

\[
a=5,\quad b=5,\quad\lambda=5.
\]

可找到 `g_lambda=0` 的状态同时属于负相和正相。

因此 RN 中同样有：

\[
\boxed{
\text{zero magnitude}
\ne
\text{zero phase}.
}
\]

若 `P(n)=0`，则 pair 一定是 `(0,0)`；而 nonsquare discriminant 的 horizon boundary 可以完全位于 crossing edges 上，没有任何 `(0,0)` primal vertex。

## 7. P019-PM-T04 —— “时间变慢导致空间收敛”目前不能作为已推出的因果定理

状态：`NO-GO / UNDERDETERMINATION RESULT`

即使固定同一个 clock label `K=k`，只要没有额外公理把 `K` 与 directed future incidences 连接起来，就可以构造具有同样当前截面大小的有限 causal graphs，使：

\[
\Xi>0,
\qquad
\Xi=0,
\qquad
\Xi<0.
\]

例如取当前截面

\[
A=\{x_1,x_2\}.
\]

统一赋予同一个 clock label `k`：

- 若两点总共到达 4 个不同 future vertices，则 `Xi=+2`；
- 若到达 2 个不同 future vertices，则 `Xi=0`；
- 若两点合流到同一个 future vertex，则 `Xi=-1`。

clock label 完全相同，但 expansion sign 三种都能出现。

所以在当前公理下：

\[
\boxed{
\text{clock slowdown}
\not\Longrightarrow
\text{causal-space contraction}
}
\]

不是因为该想法已经被物理否定，而是因为**数学结构还缺少 coupling law**。

## 8. 当前更稳健的解释：共同底层来源，而非已证明的单向因果

Schwarzschild 阶段中：

- phase 来自 `sign(n-h)`；
- magnitude 来自 `q_lambda(n;h)`；
- clock state 来自 `R_2(q)`。

它们共享同一个底层 radial residual `n-h`，但经过不同 projection。

RN 阶段更清楚：

- causal phase = `sign P(n)`；
- precision magnitude = quotient of `|P(n)|`；
- horizon boundary = zero vertices + sign-crossing edges。

因此当前更强健的研究起点应写成：

\[
\boxed{
\text{one underlying causal residual}
\longrightarrow
\begin{cases}
\text{phase/direction},\\
\text{finite clock/rate magnitude},\\
\text{boundary structure}.
\end{cases}
}
\]

而不是提前写成

\[
\text{time slows}\to\text{space contracts}.
\]

单向因果关系只有在未来找到非任意的 clock→incidence coupling 后才有资格恢复。

## 9. 这次纠错反而保留了用户最初直觉中最有价值的部分

被否定的是过强版本：

> “clock value 本身决定空间收敛。”

目前仍然活着、而且结构更清楚的是：

> **时间速率、因果方向和空间截面收敛可能是同一底层离散因果结构的不同 projection。**

接下来真正要找的是：是否存在一个自然、局部、可证伪的规则，把 phase/magnitude state 映射到 Supplement 03 的

\[
B(A),C(A),\Xi(A).
\]

如果找不到，就应保留 common-cause 解释并放弃强单向因果解释。

## 10. 对之前 P019 术语的正式替换

从本补充开始：

- 原“zero horizon basin”建议改称 **zero-magnitude basin / 零幅度盆地**；
- 原“horizon becomes a unique shell at terminal precision”改称 **zero-magnitude basin becomes phase-complete at terminal precision**；
- `q_lambda=0` 不单独作为 horizon 定义；
- horizon/boundary 使用 Supplement 02 的

\[
\partial_\xi G=(V_0,E_{\pm});
\]

- magnitude observation 永远不得偷偷替代 phase channel。

原来的整数区间、width、projection、clock-shell 计算仍然有效，只是解释对象改成 finite-resolution magnitude/rate structure。

## 11. 本阶段 ledger

- `P019-PM-T01`：phase × magnitude typed state is required —— `PROVED / DESIGN CORRECTION`
- `P019-PM-T02`：Schwarzschild exact zero-phase vertex is unique at every precision —— `PROVED`
- `P019-PM-C01`：clock `K=0` can contain inner/horizon/outer phases —— `COUNTEREXAMPLE`
- `P019-PM-C02`：same nonzero clock state can occur at opposite causal phases —— `COUNTEREXAMPLE`
- `P019-PM-T03`：charged observation also requires phase/magnitude separation —— `PROVED`
- `P019-PM-T04`：clock label alone does not imply expansion sign without a coupling law —— `UNDERDETERMINATION / NO-GO`

Executable checks：

- `src/enterprise_math/phase_magnitude.py`
- `tests/test_phase_magnitude.py`

## 12. 下一步

下一阶段不再继续增加坐标公式，而只攻一个问题：

\[
\boxed{
(\text{phase},\text{clock magnitude})
\stackrel{?}{\longrightarrow}
\text{directed incidence constraints}
\longrightarrow
B,C,\Xi.
}
\]

候选规则必须满足：

1. 局部；
2. 整数；
3. typed scale compatible；
4. 不把 observer-coordinate effect 冒充 invariant law；
5. Schwarzschild/RN specializations 正确；
6. 能被反例推翻，而不是为得到黑洞答案倒推规则。
