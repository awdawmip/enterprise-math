# P018 —— 有限精度证明演算：补充 03

状态：`ACTIVE RESEARCH NOTE`  
范围：factor precision 作为第二条精度轴；P018 与 P017 Legendre 压力测试的精确桥  
纪律：素数筛与最小素因子分层都是经典数学；这里研究的是它们在一般有限精度证明演算中的角色。

## 1. 精度不只等于数值尺度

P018 第一到第三阶段都使用正整数尺度因子作为 precision coordinate。

但这只是有限精度系统的一种实例。

证明过程还可以沿其他有限信息轴获得新信息。Legendre 压力测试本身就已经包含一条：

> 素因子究竟检查到了多远？

对正整数 `n` 和 factor cutoff `y`，定义 **factor-precision state**：

\[
D_y(n)
=
\{p\le y:p\text{ 为素数且 }p\mid n\}.
\]

它记录在 precision `y` 时已经可见的整除 witness。

## 2. P018-T29 —— factor-precision 投影相容性

状态：`PROVED`

若

\[
y\le z,
\]

则高 factor-precision 状态投影到低 precision，只需要忘掉高于 `y` 的 witness：

\[
\boxed{
\pi_{z\to y}(D_z(n))
=
D_z(n)\cap\{p:p\le y\}
=
D_y(n).
}
\]

因此对

\[
x\le y\le z,
\]

投影严格复合：

\[
\pi_{z\to x}
=
\pi_{y\to x}\circ\pi_{z\to y}.
\]

所以 factor cutoff 本身就是一条带相容忘却映射的有限 precision chain。

这里完全没有使用数值尺度因子。

## 3. P018-T30 —— 持久 factor certificate

状态：`PROVED`

在 factor precision `y` 上使用三种证明状态：

- `D_y(n)` 非空：`COMPOSITE`；
- `D_y(n)` 为空且尚未到达已证明完备的 horizon：`UNRESOLVED`；
- `D_y(n)` 为空且已经到达一个已证明有限完备 horizon：`PRIME`。

若某个因子 witness 已经在 precision `y` 出现，则所有更高 precision 都继续包含它：

\[
\boxed{
D_y(n)\ne\varnothing
\Longrightarrow
D_z(n)\ne\varnothing
\qquad(z\ge y).
}
\]

因此 COMPOSITE certificate 永久有效。

这正是 P018 第三阶段 proof-persistence 规则在另一条精度轴上的实例。

## 4. P018-T31 —— 平方盆地 factor horizon 给出有限 PRIME certificate

状态：`PROVED`

设

\[
k^2<n<(k+1)^2.
\]

P017 的 Root-Factor Horizon 已经给出

\[
n\text{ 为合数}
\iff
\exists p\le k,\ p\text{ 为素数且 }p\mid n.
\]

所以

\[
\boxed{
D_k(n)=\varnothing
\iff
n\text{ 为素数}.
}
\]

factor precision 不需要无限增加。在整个平方盆地上，有限 precision

\[
\boxed{y=k}
\]

已经对 primality 完备。

证明流程因此是：

\[
\text{UNRESOLVED}
\to
\text{COMPOSITE}
\]

一旦 witness 出现；或者如果一直没有 witness，则在有限终点 `k`：

\[
\text{UNRESOLVED}
\to
\text{PRIME}.
\]

这就是 P017 与 P018 的直接严格连接。

## 5. P018-T32 —— factor survivor 随精度单调减少

状态：`PROVED`

定义开放平方盆地中的 factor survivor：

\[
S_y(k)
=
\{n:k^2<n<(k+1)^2,\ D_y(n)=\varnothing\}.
\]

若

\[
y\le z,
\]

则

\[
\boxed{S_z(k)\subseteq S_y(k).}
\]

因此

\[
\boxed{|S_z(k)|\le|S_y(k)|.}
\]

在有限终点：

\[
\boxed{
S_k(k)
=
\{p:p\text{ 为素数},\ k^2<p<(k+1)^2\}.
}
\]

所以 P017 的素数计数获得 precision 解释：

\[
\boxed{
\Pi(k)=|S_k(k)|.
}
\]

Legendre 猜想恰好变成

\[
\boxed{|S_k(k)|\ge1\quad\text{对所有 }k\ge1.}
\]

P018 并没有证明这个不等式；它只是把 P017 的筛选动力学严格识别成有限 proof-precision process。

## 6. P018-T33 —— first-witness precision shell

状态：`PROVED`

对每个 `p<=k` 的素数，定义

\[
L_p(k)
=
\{n:k^2<n<(k+1)^2,\ \operatorname{spf}(n)=p\}.
\]

等价地，

\[
n\in L_p(k)
\]

当且仅当 `n` 在 `p` 以下没有素因子，并且 factor precision 第一次到达 `p` 时才变成 COMPOSITE。

所有 `L_p(k)` 两两不交。

平方盆地中的每个合数恰好属于一个 shell，因为它的最小素因子必不超过 `k`。

因此

\[
\boxed{
I_k
=
\left(
\mathop{\bigsqcup}_{p\le k}L_p(k)
\right)
\sqcup
S_k(k),
}
\]

其中 `I_k` 为开放平方盆地。

这是一个 **first-witness precision-shell decomposition**。

与 P017 原始 inclusion-exclusion 路线中的带符号 Möbius shell 不同，这里的 shell 非负而且互不重叠，因为每个合数只分配给它的第一个证明 witness。

但这并没有消灭困难的数论：精确计算 `L_p(k)` 本身就必须排除所有更小素因子。因此 parity difficulty 被重新组织，而不是凭空消失。

## 7. P018-T34 —— 精确 P017/P018 bridge identity

状态：`PROVED`

开放平方盆地恰有

\[
2k
\]

个状态。

由 T33：

\[
2k
=
\sum_{p\le k}|L_p(k)|
+
|S_k(k)|.
\]

再由 T32：

\[
|S_k(k)|=\Pi(k).
\]

所以

\[
\boxed{
\Pi(k)
=
2k-\sum_{p\le k}|L_p(k)|.
}
\]

P017 另一方面已经证明带符号 carry 恒等式：

\[
\Pi(k)
=
2+
\sum_{d\mid P_k}\mu(d)\kappa_d(k).
\]

因此两种 precision 描述满足精确桥：

\[
\boxed{
2+
\sum_{d\mid P_k}\mu(d)\kappa_d(k)
=
2k-\sum_{p\le k}|L_p(k)|.
}
\]

这个等式不证明 Legendre。它说明：

- 原 P017 一侧通过带符号 overlap cancellation 计算最终 survivor 数；
- P018 factor-precision 一侧通过互不重叠的 first-witness exit shell 计算同一个 survivor 数。

这是第一条严格说明“非平凡 P017 对象确实属于 P018 precision dynamics”的结果，而不再只是类比。

## 8. 现在至少有两条不同精度轴

P018 已经拥有两个数学上不同的 precision coordinate。

### Scale precision

通过整除关系提高整数尺度因子。投影是 Euclidean quotient，每个 fiber 带有有界数值 detail。

### Factor precision

通过提高已检查素因子 horizon 精化证明状态。投影是忘记高 cutoff witness，新 detail 是新显现的整除 witness 集合。

它们共同的抽象结构并不是某个具体 remainder 公式，而是：

\[
\boxed{
\text{有限 precision level}
+
\text{相容 forgetting map}
+
\text{嵌套 fiber/信息}
+
\text{持久 certificate}.
}
\]

这强烈说明 P018 下一阶段应该建立**抽象 finite precision system**，而不是继续堆尺度专用恒等式。

## 9. 精度方向与时间方向

这里还出现了与 T012 的结构性反向关系。

### 时间演化

在确定性多对一前向动力学中，历史纤维只会合并，所以 merged-history multiplicity 单调不减。

### 精度精化

在相容 refinement 中，与当前粗观测相容的细状态集合只会缩小，所以 ambiguity multiplicity 单调不增。

目前还不能把它宣称为范畴意义上的 time/precision duality，但单调方向确实严格相反：

\[
\boxed{
\text{time：可区分历史发生合并},
\qquad
\text{precision：相容可能性发生分离}.
}
\]

抽象 precision-system 形式化现在可以直接检验这种反向关系是否具有更深的序理论意义。

## 10. 前人边界

Eratosthenes 类筛法、trial division、最小素因子分类以及逐步提高 factor cutoff 都是经典数学。P017 也已经登记了筛法/动力学前人工作，包括连续平方区间中的 sieve survival 思路。

所以 P018 不声称 factor sieve 或 first-prime-factor partition 是新发明。

当前真正要检验的项目组合是**跨精度轴的统一**：

- scale refinement 与 factor refinement 都是有限 precision system；
- 两者都支持永久 coarse proof certificate；
- P017 的最终 prime survivor count 成为 factor-precision proof process 的终态；
- P017 带符号 carry identity 与互不重叠 first-witness precision-shell identity，是同一 terminal survivor count 的两种精确分解。

这一组合的历史创新状态仍为 `NOVELTY_UNVERIFIED`。

## 11. 第四阶段状态

- P018-T29 factor-precision projection compatibility：`PROVED`
- P018-T30 persistent factor certificates：`PROVED`
- P018-T31 square-basin terminal factor horizon：`PROVED`
- P018-T32 survivor monotonicity + terminal-prime identity：`PROVED`
- P018-T33 disjoint first-witness factor shells：`PROVED`
- P018-T34 exact P017/P018 bridge identity：`PROVED`
- abstract finite precision-system axioms：`NEXT`
- scale precision × factor precision product：`OPEN`
- time/precision order duality：`OPEN`
- Legendre 猜想：`OPEN / NOT PROVED HERE`

可执行检查位于 `src/enterprise_math/factor_precision.py` 与 `tests/test_factor_precision.py`。
