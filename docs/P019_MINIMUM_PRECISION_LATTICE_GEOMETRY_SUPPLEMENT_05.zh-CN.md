# P019 补充 05 —— 碰撞幂收缩族 `Psi_(m,s)`

状态：`RESEARCH WIP / FINITE IDENTITIES VERIFIED`  
范围：graph/radial 统一、隐藏维度容量、完整碰撞谱、跨维 cut-boundary 递归

## 1. 总族

对整数 `m>=1, s>=1, c in Z` 定义

\[
\Psi_{m,s}(c)
=
\min_{a_1+\cdots+a_m=c}
\sum_{i=1}^m |a_i|^s.
\]

若

\[
|c|=mq+r,
\qquad 0\le r<m,
\]

则平衡分配给出

\[
\boxed{
\Psi_{m,s}(c)
=(m-r)q^s+r(q+1)^s.
}
\]

并且

\[
\boxed{
\Psi_{m,s}(1)=1
\quad\forall m,s.
}
\]

这把“单位 1 不随维度和碰撞阶数改变”写成统一整数不变量。

## 2. `s=1` 与 `s=2`

当 `s=1`：

\[
\Psi_{m,1}(c)=|c|,
\]

完全与 `m` 无关。在零和状态上

\[
\sum_i|c_i|=2d_G(0,c),
\]

所以 primitive graph ball 是 `s=1` 成员，且收缩后 block-size tag 对数值不可见。

当 `s=2`：

\[
\Psi_{m,2}(c)=\psi_m(c),
\]

即 Supplement 04 的 tagged radial square-energy family。

因此 graph 与 radial 不再是两套不相关的模型，而是同一个 `Psi_(m,s)` family 的不同碰撞阶数。

## 3. 维度加法仍是 min-plus

固定任意 `s>=1`，都有

\[
\boxed{
\Psi_{m+n,s}(c)
=
\min_{a+b=c}
\left(\Psi_{m,s}(a)+\Psi_{n,s}(b)\right).
}
\]

所以

\[
\boxed{
\Psi_{m,s}\square\Psi_{n,s}
=\Psi_{m+n,s}.
}
\]

block sizes 的整数加法与 min-plus 合成严格对应。

## 4. 与完整 `J_k` collision spectrum 的连接

对非负占用数 `a`，幂可以在 falling-factorial / collision basis 中展开：

\[
a^s
=
\sum_{j=1}^s
S(s,j)\,j!\binom aj,
\]

其中 `S(s,j)` 为第二类 Stirling 数。

因此对一个 occupancy configuration：

\[
\sum_i a_i^s
=
\sum_{j=1}^s
S(s,j)\,j!
\sum_i\binom{a_i}{j}.
\]

右侧第二个求和正是 P011 类型的 `J_j` collision counts。

于是 `s` 不是一个任意连续指数，而可以解释为：该能量同时看到了最高到 `j=s` 阶的碰撞重数，并按固定整数系数组合它们。

例如：

\[
a^2=a+2\binom a2,
\]

\[
a^3=a+6\binom a2+6\binom a3.
\]

所以 `s=1` 只计单位；`s=2` 首次看见 pair collision；`s=3` 再加入 triple collision；更高 `s` 继续读出更高阶 multiplicity。

## 5. tagged collision-power balls

对 block partition

\[
\mathbf m=(m_1,\ldots,m_k)
\]

定义

\[
E^{(s)}_{\mathbf m}(c)
=
\sum_i\Psi_{m_i,s}(c_i),
\qquad
\sum_i c_i=0,
\]

以及

\[
B^{(s)}_{\mathbf m}(T)
=
\{c:E^{(s)}_{\mathbf m}(c)\le T\}.
\]

固定 transfer channel `j -> i`，把 blocks `i,j` 合并成 `m_i+m_j` 得到 `m'`。由于 `Psi_(m,s)` 离散凸，fiber threshold set 是整数区间；每个非空 fiber 沿指定方向恰有一个穿界出口。

因此对整个 family：

\[
\boxed{
|C^{(s)}_{\mathbf m,j\to i}(T)|
=
|B^{(s)}_{\mathbf m'}(T)|.
}
\]

该恒等式已对 `s=1,2,3,4`、多种 partitions 与有限 thresholds 做整数枚举回归，全部通过。

## 6. 当前统一图景

P019 当前得到一个三层整数结构：

\[
\boxed{
\text{unit }1
\to
\text{block capacity }m
\to
\text{collision sensitivity }s
}
\]

其中：

- `1` 始终保持 `1`；
- `m` 保存被收缩的维度槽位容量；
- `s` 控制读取到多高阶的 collision multiplicity；
- 维度合并是 block-size addition；
- 能量合并是 min-plus convolution；
- 挖球后的固定方向 cut boundary 严格递归成低一维 tagged ball。

因此“高维由低维简单运算得到”目前最强的候选形式不再是普通乘方或普通卷积，而是：

\[
\boxed{
\text{dimension addition}
\leftrightarrow
\text{tag addition}
\leftrightarrow
\text{min-plus contraction}.
}
\]

## 7. 下一步

1. Lean 形式化 `Psi_(m,s)` 的 balanced minimizer、min-plus law 与 cut-boundary theorem；
2. 检验完整 `J_k` spectrum 在不同 contraction tree 下是否具有更强不变量；
3. 研究 `s` 是否应只作为观察/工具阶数，而不能被误当成物理维度；
4. 检索 discrete convex analysis / infimal convolution / resource allocation prior art，并保持 novelty discipline；
5. 继续用挖球、缺口、边界和因果 marks 压力测试该 family 是否真的比固定 FCC/HCP 描述更稳健。
