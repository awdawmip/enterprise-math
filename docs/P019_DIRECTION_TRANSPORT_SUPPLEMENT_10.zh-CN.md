# P019 补充 10 —— 方向运输一般是关系，而不是映射

状态：`TESTING / 有限组合核心已证明`

## 1. 动机

Stage 8 把内禀方向类定义为带标记截面自同构群对 outgoing primitive incidences 的轨道；Stage 9 进一步证明，causal phase role 是比这些 direction orbit 更粗的结构分区。

下一步问题是动态的：若

\[
A_{t+1}=F(A_t),
\]

那么时间 \(t\) 的某个方向类，是否能够不依赖任意选择地对应到时间 \(t+1\) 的某个方向类？

如果方向类本身无法规范运输，那么静态 anisotropy 量就不能直接升级成 shear-like 动力学。

## 2. 规范可拼接矩阵

设

\[
D_1^{(t)},\ldots,D_r^{(t)}
\]

是从 \(A_t\) 指向 \(A_{t+1}\) 的内禀方向类；

\[
D_1^{(t+1)},\ldots,D_s^{(t+1)}
\]

是从 \(A_{t+1}\) 指向 \(A_{t+2}\) 的方向类。

定义

\[
\boxed{
T_{ij}
=
\#\{((u,v),(v,w)):(u,v)\in D_i^{(t)},\ (v,w)\in D_j^{(t+1)}\}.
}
\]

即 \(T_{ij}\) 统计通过共同中间截面能够拼成 primitive 两步因果路径的数量。

它完全由 directed incidence structure 和现有 direction partitions 决定，只使用整数计数，不引入欧氏方向、角度、概率或分数归一化。

## 3. 运输支撑

判断“方向身份能否延续”只需要矩阵支撑

\[
S_{ij}=1[T_{ij}>0].
\]

一个当前方向类的某一行可能：

- 没有任何后继：该分辨率下 direction death；
- 只连接一个后继类：局部函数式延续；
- 连接多个后继类：direction split。

反过来，一个下一时刻的方向类可能没有前驱、只有一个前驱，或有多个前驱，分别对应 birth、唯一前驱和 merge。

## 4. 规范一一运输判据

只根据可拼接关系能够得到规范一一方向身份，当且仅当支撑矩阵是置换矩阵：

1. 当前与下一时刻方向类数量相同；
2. 每一行恰有一个非零支撑项；
3. 每一列恰有一个非零支撑项。

此时存在唯一匹配

\[
\pi:\{1,\ldots,r\}\to\{1,\ldots,r\}
\]

满足

\[
T_{i,\pi(i)}>0.
\]

其中正整数权重 \(T_{i,\pi(i)}\) 不必等于 1；它表示两步路径 multiplicity，而不是方向类身份本身。

## 5. 一般方向身份的 no-go

一般情况下，支撑矩阵并不是置换矩阵。

一个方向类可以分裂成多个下一方向类；多个当前方向类也可以合并为一个下一方向类；在当前结构分辨率下还可以出现方向类的 birth/death。

因此：

\[
\boxed{
\text{内禀方向的演化规范地是一个关系，而一般不是函数。}
}
\]

所以，如果在任意时间步之间强行持续标记 `direction 1`、`direction 2` 等固定身份，就引入了 primitive causal structure 本身没有给出的额外选择。

这是对朴素 dynamic shear 类比的一条结构性 no-go。

## 6. 对 anisotropy 演化的含义

Stage 8 的静态量

\[
A_C
=
\sum_{i<j}(E_jC_i-E_iC_j)^2
\]

在每个截面上都可以独立定义。

但

\[
A_C(t+1)-A_C(t)
\]

只表示一个总体标量发生了变化，并不能自动解释成具体方向形变被运输后的变化。

只有在 transport support 给出唯一一一匹配的时间步，componentwise direction evolution 才是规范的；一旦发生 split / merge / birth / death，若要逐方向比较，就必须再加入额外结构。

因此 P019 目前不把静态 \(A_C\)，也不把它简单的时间差，认定为物理 shear。

## 7. 更稳健的结构链

当前层级成为

\[
\text{phase/boundary}
\to
\text{causal roles}
\to
\text{direction orbits}
\to
\text{transport relation }T
\to
\text{仅在置换支撑时间步存在一一方向身份}.
\]

也就是说，我们允许“方向身份本身”随因果结构发生分裂和合并，而不是预设一个永远固定的切空间基底。

## 8. 下一门槛

下一步不再增加静态标量，而是研究：是否存在可以穿过任意 transport relation、无需选定一一 matching 也能规范传播的较弱结构。

优先检查现有数据：

- transport support 上的总 incidence flow；
- causal role 的保持与转换；
- 在 transport-connected components 上聚合的 collision spectrum。

如果这些对象可以跨多步精确复合，我们将得到真正的 relational dynamics；如果不能，就保留 no-go，不强造连接。

## 9. 范围纪律

本文的 `transport` 只表示 primitive causal incidences 的可拼接关系，不声称得到离散 Levi-Civita connection、parallel transport、tangent bundle、geodesic deviation、Raychaudhuri equation 或物理 shear tensor。
