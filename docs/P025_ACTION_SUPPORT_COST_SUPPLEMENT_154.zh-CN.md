# P025 补充 154 —— Syntactic action count 与 semantic dependency support 可以线性分离

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-fairness-stage147`

## 1. Operation-support closure

Stage 153 已把 predecessor/downward closure 识别为 autonomous helper-action subsystem 的自然 support。对 declared action set

\[
Q\subseteq P_{gate},
\]

定义 semantic dependency support

\[
\boxed{
D(Q)=\downarrow Q.
}
\]

syntactically 列出的 raw actions 数为 `|Q|`；为了自洽解释这些 actions 所需的 support 大小则为 `|D(Q)|`。

## 2. Maximal actions 生成同一个 support

令 `Max(Q)` 表示 helper dependency order 下 `Q` 的 maximal elements。每个 nonmaximal action 都位于某个 maximal action 下方，因此

\[
\boxed{
\downarrow Q
=
\downarrow\operatorname{Max}(Q).
}
\]

所以 dependency footprint 自身有一个 exact antichain generator boundary。显式列出 ancestor actions，并不会扩大已经被 later action 强制出来的 support。

这是 ideal boundary compression 在 operation-language 一侧的对应物。

## 3. 一个 action 可以强迫很大的 support

考虑

\[
k=2^d
\]

个 raw antecedents 的 perfect balanced compiler。选择两个最高 pre-output helper gates 中的任意一个。它的 dependency subtree 包含 `k/2` 个 raw leaves，因此包含的 helper gates（含自身）精确为

\[
\boxed{\frac{k}{2}-1}.
\]

所以只包含这一个 helper 的 syntactic action language 满足

\[
\boxed{
|Q|=1,
\qquad
|D(Q)|=\frac{k}{2}-1.
}
\]

对 `k=4,8,16,32`，精确值为

\[
1,3,7,15.
\]

raw action count 始终是一，而 semantic support blowup 随问题规模线性增长。

## 4. 精确八元样本

八元 compiler 中，upper helper `h5` 依赖 first-layer helpers `h1,h2`。因此

\[
D(\{h_5\})=\{h_1,h_2,h_5\}.
\]

并且

\[
D(\{h_1,h_2,h_5\})
=
D(\{h_5\}).
\]

所以包含三个 labels 的 raw action list 可以压缩成一个 maximal support generator，但 autonomous semantic support 仍包含三个 helper states/actions。

## 5. 三种 operation-language 资源

action language 至少携带三个不同的 size notions：

1. **raw action count** `|Q|`；
2. **support-generator count** `|Max(Q)|`；
3. **dependency-support size** `|down(Q)|`。

若不加限定，不应把其中任一单独称作 `operation precision`。

## 6. 与 state precision 的关系

很小的 declared action family 可能要求很大的 state/relation footprint，才能让 action legality 与 transitions 自洽闭合。反过来，一个很大的 syntactic action list 也可能包含大量 support-redundant ancestor actions。

所以 future-language complexity 与 required state support 相互耦合，但并不相等。

## 7. 前人工作边界

transitive dependency closure 与 maximal-generator antichains 都属于经典 order theory。这里不主张 generic novelty。P025 提供 perfect-compiler exact family 以及 operation/state precision interpretation。
