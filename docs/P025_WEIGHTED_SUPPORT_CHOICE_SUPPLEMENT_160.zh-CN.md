# P025 补充 160 —— 只有声明 workload cost 后，support level 才有“最优”

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-state-support-stage155`

## 1. 没有 canonical scalarization

Stage 159 给出 Pareto frontier

\[
C_t=(|A_t|,|R_t|,h-t),
\]

三个坐标分别是 executable-action count、static-state support size 与 remaining support-promotion horizon。

这三种资源没有 canonical 相加方式。只有 workload 先声明每种资源的代价，才可以选择一个 implementation level。

令

\[
\alpha>0,
\qquad
\beta>0,
\qquad
\gamma>0
\]

分别表示：

1. 一个 executable helper action 的单位成本；
2. 一个 retained helper state coordinate 的单位成本；
3. 一单位 remaining future support-closure obligation 的成本。

定义

\[
\boxed{
\mathcal C_t
=
\alpha|A_t|
+
\beta|R_t|
+
\gamma(h-t).
}
\]

这个 scalar cost 是 declared workload model，而不是 intrinsic precision invariant。

## 2. 精确 local promotion threshold

对相邻两个 frontier levels，

\[
\mathcal C_{t+1}-\mathcal C_t
=
\alpha\Delta A_t
+
\beta\Delta R_t
-
\gamma,
\]

其中

\[
\Delta A_t=|A_{t+1}|-|A_t|,
\qquad
\Delta R_t=|R_{t+1}|-|R_t|.
\]

所以多 promotion 一层会严格降低 workload cost，当且仅当

\[
\boxed{
\gamma
>
\alpha\Delta A_t+eta\Delta R_t.
}
\]

等号时精确 tie。

解释：只有“减少一层 future closure obligation”的 workload 价值，大于新增 executable-action 与 state-support 成本时，这层 operation freedom 才值得购买。

## 3. Perfect 32-way 样本

Stage159 frontier 为

\[
(1,3,3),
\quad
(3,7,2),
\quad
(7,15,1),
\quad
(15,15,0).
\]

取

\[
\alpha=4,
\qquad
\beta=1.
\]

相邻 promotion thresholds 精确为

\[
\boxed{12,24,32.}
\]

因为：

- 第一层新增 2 个 actions 与 4 个 state coordinates，成本 `8+4=12`；
- 第二层新增 4 个 actions 与 8 个 state coordinates，成本 `16+8=24`；
- 最后一层新增 8 个 actions，但 state support 已经提前支付，不再增加，成本 `32`。

精确 workload optima 包括

\[
\boxed{
\begin{array}{c|c}
\gamma & \text{optimal promotion depth}\\
\hline
5 & 0\\
15 & 1\\
26 & 2\\
40 & 3
\end{array}}
\]

而在

\[
\gamma=12
\]

时，depth 0 与 1 精确 tie。

所以这个 structural frontier 中每一个点，都确实能在某组 positive declared workload 下成为真正 optimum。

## 4. Structural theorem 与 policy decision

数学提供：

- exact Pareto frontier；
- exact marginal resource increments；
- 在 costs 已给定后的 exact switching inequalities。

数学**不提供** `alpha,beta,gamma` 的值；这些属于 declared task/runtime/environment。

因此

\[
\boxed{
\text{optimal precision level}
=
\text{structural frontier}
+
\text{declared workload valuation}.
}
\]

## 5. Precision 后果

这给出一个 concrete reason：不能把 `precision` 编成 globally ordered scalar。即使固定同一个 compiler 与 dependency graph，不同合法 workloads 也会选择不同 support layers。

future architecture 应当在 task 给出 valuation 以前保留 resource vector，而不是过早 collapse 成单一数值。

## 6. 前人工作边界

Pareto front 的 weighted scalarization 与 marginal-cost switching 都属于经典 optimization。这里不主张 generic novelty。P025 提供 exact support-promotion specialization，以及 mathematical structure 与 workload policy 的明确分离。
