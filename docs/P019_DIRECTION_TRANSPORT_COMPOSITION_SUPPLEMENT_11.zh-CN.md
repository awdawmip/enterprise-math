# P019 补充 11 —— Transport matrix 只是 witness relation 的基数投影

状态：`TESTING / 有限反例与 witness 精确复合已建立`

## 1. 问题

补充 10 定义了方向运输矩阵

\[
T_{ij}=|W_{ij}|,
\]

其中 \(W_{ij}\) 是从时间 \(t\) 的方向类 \(D_i^{(t)}\) 到时间 \(t+1\) 的方向类 \(D_j^{(t+1)}\) 之间所有可拼接 primitive incidence pairs 的集合。

一个自然猜想是：多步方向运输可以直接用普通整数矩阵乘法复合。

这个猜想一般是错的。

## 2. 最小过计数反例

取三层连续 incidence：

\[
a\to x\to p\to r,
\qquad
b\to y\to q\to s.
\]

把每一层的两条 incidence 都放入同一个 direction class。

第一层到第二层恰好有两个 two-path witnesses：

\[
(a\to x,\ x\to p),
\qquad
(b\to y,\ y\to q),
\]

故 \(T_{01}=2\)。

第二层到第三层同样有两个 witnesses：

\[
(x\to p,\ p\to r),
\qquad
(y\to q,\ q\to s),
\]

故 \(T_{12}=2\)。

若直接做矩阵乘法，会得到

\[
T_{01}T_{12}=4.
\]

但真实三步链只有两条：

\[
a\to x\to p\to r,
\qquad
b\to y\to q\to s.
\]

另外两项是伪组合：它们把一条 two-path witness 与另一条不共享同一 middle incidence 的 continuation 错误相乘。

所以一般有

\[
\boxed{
|W_{01}|\,|W_{12}|
\neq
|W_{01}\Join W_{12}|.
}
\]

## 3. 丢失了什么信息？

\(|W_{ij}|\) 只记住“有多少个可拼接 pair”，却忘记了**究竟是哪一条 primitive middle incidence 支撑这次拼接**。

精确复合必须在同一个真实 middle incidence 上做 join：

\[
(e_0,e_1)\Join(e_1,e_2)
=
(e_0,e_1,e_2).
\]

因此，在当前层级上真正 composition-complete 的对象是 witness sets \(W_{ij}\)，而不是它们的基数。

整数矩阵 \(T\) 只是 witness relation 的 cardinality projection / decategorification。

## 4. 精确 witness 复合

设两段连续 witness relations 为

\[
W^{(t,t+1)}_{ij}
\subseteq
D_i^{(t)}\times D_j^{(t+1)},
\]

\[
W^{(t+1,t+2)}_{jk}
\subseteq
D_j^{(t+1)}\times D_k^{(t+2)}.
\]

则精确复合应定义为 fibered join：

\[
\boxed{
W^{(t,t+2)}_{ik}
=
\{(e_0,e_1,e_2):(e_0,e_1)\in W^{(t,t+1)}_{ij},
(e_1,e_2)\in W^{(t+1,t+2)}_{jk}\}.
}
\]

中间 primitive incidence \(e_1\) 必须完全相同。

这个结构仍然是有限、无坐标、integer-compatible 的，不需要概率或连续插值。

## 5. 与 P010 / P011 的统一结构

这个 no-go 与进取数论前面已经出现过的结构高度一致：

- P010：多个历史合并到同一当前状态后，粗粒度当前状态不能恢复具体 predecessor history；
- P011：低阶 collision totals 不能恢复完整 multiplicity spectrum；
- P019 Stage 11：transport cardinalities 不能恢复究竟是哪一条 middle incidence 支撑多步 continuation。

三者共同说明：**聚合可以保留统计，但会丢 witness identity；后续若要精确复合，就必须保留相关 fiber / witness structure。**

## 6. 对 P019 核心的影响

方向动力学层更合适的表示应是

\[
\boxed{
\text{direction classes}
\xrightarrow{\text{witness relation }W}
\text{direction classes}
\xrightarrow{|\cdot|}
T.
}
\]

矩阵 \(T\) 仍然有价值：它可以用于 support、split/merge 判断以及有限计数；但它不应被当成 primitive composition law。

## 7. 对 shear-like 比较的含义

如果只保留静态 direction partition 加上整数 transport-count matrix，就无法一般性地精确描述多步方向形变动力学。

因此得到更强的 no-go：

> **静态方向类 + transport 基数矩阵，单独不足以定义精确的多步方向形变演化。**

未来若要继续和 shear-like dynamics 比较，只能：

1. 保留 witness-complete transport；或者
2. 找到一个受限结构区间，并证明在该区间里 cardinality matrix 已经 composition-complete。

## 8. 下一门槛

下一步应该寻找这种“矩阵足够”的精确条件，而不是继续增加统计量。

候选 sufficient conditions 包括：middle incidence continuation 是确定的，或者每个非零 transport cell 的 witness fiber pattern 满足足够强的均匀性。

目标是刻画何时

\[
|W\Join W'|
\]

可以仅由 cardinality data 推出。如果不存在足够宽的自然条件，就把 witness transport 保留为 primitive，把 matrix transport 固定为派生投影。

## 9. 范围纪律

本文不主张 category theory 新颖性，也不声称得到物理 connection 或量子 path amplitude。`witness relation`、`join`、`cardinality shadow` 都只按有限组合意义使用。
