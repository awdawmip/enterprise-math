# P023 —— 安全选择器稳定等价，补充 07

状态：`ACTIVE RESEARCH NOTE`  
范围：安全精度选择器词的稳定等价  
依赖：P023 Stage 2 安全精度内算子与 P020 有限稳定化  
纪律：单调/幂等算子的半群、共同不动点迭代等都属于成熟数学。本说明记录进取数论中的精确有限精度解释，以及与 P019 型坍缩词稳定等价的桥接。

## 1. 动机

Stage 2 对每个有限确定性运算族 `A` 给出安全精度选择器

\[
S_A(E)=\operatorname{Safe}_A(E),
\]

它返回输入精度关系 `E` 内最大的 `A`-compatible 等价关系。

每个 selector 都单调、向下且幂等。

一个自然问题是：能否把多个要求分别做一次 selector，然后就结束？Stage 2 已给出明确反例：单遍串行不仅可能依赖顺序，后处理 selector 甚至可能重新破坏先前运算的兼容性。

因此正确问题应当是动力学问题：

> 固定一个 selector word，然后反复执行**同一个完整词**，它的有限稳定值是什么？

## 2. 设置

令

\[
S_1,\ldots,S_m
\]

分别对应有限运算族

\[
A_1,\ldots,A_m.
\]

定义一个 selector word

\[
W=S_m\circ\cdots\circ S_1.
\]

每个 `S_i` 都是有限状态空间等价关系偏序上的单调向下映射。

记

\[
A_\cup=A_1\cup\cdots\cup A_m.
\]

## 3. P023-S3-T01 —— selector word 的不动点恰好是共同不动点

状态：`PROVED`。

对任意精度关系 `E`，

\[
\boxed{
W(E)=E
\iff
S_i(E)=E\text{ 对每个 }i.
}
\]

等价地，

\[
\boxed{
\operatorname{Fix}(W)
=
\bigcap_i\operatorname{Fix}(S_i)
=
\operatorname{Fix}(S_{A_\cup}).
}
\]

### 证明

因为每个 selector 都向下，

\[
W(E)
\subseteq
S_{m-1}\cdots S_1(E)
\subseteq\cdots\subseteq
S_1(E)
\subseteq E.
\]

若 `W(E)=E`，这条下降链的首尾相等。由偏序反对称性，每一个中间关系都必须等于 `E`。特别地 `S_1(E)=E`，再沿中间等式依次得到每个 `S_i(E)=E`。

反向显然：若所有 selector 都固定 `E`，它们的复合也固定 `E`。

最后，`S_i(E)=E` 恰好表示 `E` 支持 `A_i` 中全部运算；对所有 `i` 同时成立，就是支持运算要求的并集。∎

这里从“word 不动点推出各 selector 不动”只需要向下性，本身甚至不需要每个 selector 幂等；幂等性用于把各 selector 的不动点解释为对应运算兼容性。

## 4. P023-S3-T02 —— 反复 selector word 稳定到共同安全精度

状态：有限状态空间上 `PROVED`。

词 `W` 是单调向下映射，因为它由单调向下 selector 复合而成。等价关系偏序有限，因此 P020 有限稳定化可以直接使用。

对任意初始精度 `E_0`，有限次反复执行 `W` 会到达 `E_0` 下方最大的 `W`-不动关系。

结合 T01，

\[
\boxed{
\operatorname{stab}_W(E_0)
=
S_{A_\cup}(E_0).
}
\]

所以固定顺序地逐个强制安全要求，只要反复执行整个词，最终会到达与同时求 family closure 完全相同的最粗共同安全精度。

## 5. P023-S3-T03 —— 稳定结果与 selector 顺序无关

状态：有限状态空间上 `PROVED`。

取两个包含同一组运算要求的 selector word，可以顺序不同，也可以有任意重复。只要运算要求并集相同，根据 T01，它们具有相同不动点集合。P020 因而会从任意初始精度选出同一个最大不动点。

因此

\[
\boxed{
\operatorname{stab}_{W_1}(E)
=
\operatorname{stab}_{W_2}(E)
}
\]

只要 `W_1,W_2` 包含同一组 selector 要求。

瞬态 refinement 路线仍可能完全不同。Stage 2 的五状态反例中，`F→G` 与 `G→F` 第一遍结果不同，而且都未共同兼容；但分别继续重复同一顺序，第二遍都会到达相同的离散共同安全 partition。

所以：

\[
\boxed{
\text{单遍顺序有影响；稳定安全精度没有。}
}
\]

## 6. P023-S3-T04 —— 稳定等价半群退化为要求集合的并集结构

状态：有限 selector-family 层面 `PROVED`。

定义两个 selector word **稳定等价**：若它们在每个有限初始精度关系上的反复作用具有完全相同的稳定输入—输出映射。

根据 T02–T03，一个 word 的稳定类只取决于词中出现的运算要求并集。

在词拼接下，这些要求按集合并集组合：

\[
\boxed{
[W_A]\,[W_B]
\longmapsto
A\cup B.
}
\]

重复被吸收：

\[
A\cup A=A,
\]

顺序消失：

\[
A\cup B=B\cup A.
\]

因此有限安全 selector word 半群按稳定等价取商后，得到一个由有限运算要求集合索引的交换幂等 join 结构。

这与 P019 有明显结构平行：P019 中坍缩词瞬态顺序可以不同，但稳定等价由指数要求的 lcm 控制；这里稳定不变量不是 lcm，而是未来运算要求的集合并集。

## 7. 为什么这不与 Stage 2 no-go 矛盾

Stage 2 反驳的是一般捷径

\[
S_B(S_A(E))=S_{A\cup B}(E).
\]

Supplement 07 证明的是

\[
\boxed{
\operatorname{stab}_{S_B\circ S_A}(E)
=S_{A\cup B}(E).
}
\]

二者区别正是：一次瞬态 word application 与固定 word 的有限稳定化不是同一件事。

这也符合进取数论已有的纪律：瞬态不合流并不意味着稳定映射一定不同。

## 8. 可执行审计

`src/enterprise_math/p023_selector_semigroup.py` 实现：

- selector word 的一次作用；
- 固定词反复稳定；
- 运算要求并集的共同安全 selector；
- word 不动点/共同兼容性的审计。

`tests/test_p023_selector_semigroup.py` 包含：

- 五状态单遍顺序依赖反例；
- 两种重复顺序最终都到达共同安全精度；
- 三状态上所有确定性映射对、所有二值初始观察的穷举验证；
- 有限 partition 上 word 不动点/共同兼容性的检查；
- class-count 有限终止审计。

有限检查只用于审计实现。T01–T04 的依据是向下性、不动点刻画和 P020 有限稳定化。

## 9. 下一问题

selector-word 结果提示两个更高价值方向：

1. 把“不动点交集 / 稳定 word”定理抽象形式化到一般单调向下 endomap，使 P019 坍缩词与 P023 selector word 共用同一条可复用母定理；
2. 研究 Stage 2 得到的 `regular scale + localized bounded detail` 精度对象在不断增加运算要求时，能否保持高效、规范的有限表示，而不退化成数据库式任意索引。
