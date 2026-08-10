# P025 补充 151 —— 带标签的 enabled-action frontier 就是精确 runtime state

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-fairness-stage147`

## 1. 设置

设 `P_gate` 为 helper dependency poset，

\[
I\in J(P_{gate})
\]

为合法 asynchronous completed-helper ideal。

定义带标签的 enabled-action frontier

\[
\operatorname{En}(I)
=
\{h\notin I:\operatorname{Pred}(h)\subseteq I\}.
\]

Stage 146 已证明相同 ideal cardinality 可以拥有不同 enabled frontiers。更强的结论是：完整 labelled enabled frontier 精确决定 ideal。

## 2. Enabled frontier 是 complement 的极小 antichain

因为 `I` 是 ideal，它的 complement

\[
U=P_{gate}\setminus I
\]

是 upset。helper `h` enabled，当且仅当它属于 `U` 且 `U` 中已经没有任何 predecessor。因此

\[
\boxed{
\operatorname{En}(I)=\operatorname{Min}(U).
}
\]

enabled action set 自动是 antichain。

## 3. 精确重建

任意有限 upset 都由它的极小元素向上生成：

\[
U=\uparrow\operatorname{Min}(U).
\]

所以

\[
\boxed{
I
=
P_{gate}\setminus\uparrow\operatorname{En}(I).
}
\]

于是

\[
\boxed{
\operatorname{En}(I)=\operatorname{En}(J)
\iff
I=J.
}
\]

带标签 enabledness signature 在合法 ideals 上 injective，并保留全部 exact runtime progress state。

terminal ideal 的 enabled frontier 为空，它唯一对应 full ideal。

## 4. 双重 boundary charts

每个 ideal 因而有两种 exact antichain charts：

1. **completed boundary** —— 已完成 helpers 的 maximal elements `Max(I)`；
2. **enabled boundary** —— 未完成 helpers 的 minimal elements `Min(P_gate\I)`。

两者是同一 runtime state 的对偶表示。

两种 boundary 的最大可能大小都由

\[
\boxed{\operatorname{width}(P_{gate})}
\]

控制。对 balanced `k=2^d` compiler，该 width 为 `k/2`。

## 5. Sharpen Stage 146

若全部 labelled helper actions 都可见，则

\[
\boxed{
\text{enabled-action quotient}
=
\text{exact progress quotient}.
}
\]

所以 state-class ladder 可收紧为

\[
\boxed{
1
\quad\to\quad
m+1
\quad\to\quad
|J(P_{gate})|,
}
\]

分别对应 endpoint、remaining-work rank，以及完整 labelled action-legality / exact progress。

第三层仍有两个不同 coordinate charts：completed ideal/antichain 与 enabled frontier。

## 6. 与 legality-sensitive future quotient 的关系

这是现有 P023/Foundation “action enabledness 属于 future-observable structure” 的具体 specialization。在这里，当前全部 labelled actions 的 enabledness vector 已经分离所有合法 runtime states，不需要更深 action-word refinement 才能恢复 exact state identity。

这个强结论依赖于**全部 helper action labels 都被观察**。Stage 152 将研究 partial action visibility。

## 7. 前人工作边界

ideals、upset minimal boundaries 与 enabled-event frontiers 都属于经典 order/event-structure theory。这里不主张 generic novelty。P025 提供 exact specialization，并收紧 Stage146 中尚未确定的中间 quotient。
