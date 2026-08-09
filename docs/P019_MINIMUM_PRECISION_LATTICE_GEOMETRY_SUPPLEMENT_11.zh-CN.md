# P019 补充 11 —— Pair Dispersion 与 Imbalance-Tree 精确重建

状态：`RESEARCH WIP / EXACT INTEGER IDENTITIES PROVED`

## 1. 动机

Supplement 09 把平方层的一次 split 压缩成：

- parent total `c`；
- block sizes `m,n`；
- cross-multiplied imbalance `z=na-mb`。

其中 `z` 可以精确恢复 child totals。

本补充进一步证明：`z^2` 不是任意编码，它恰好是两个 blocks 合并时新增的 pairwise integer dispersion 项。

这使平方径向量获得一个不依赖连续角度/长度原语的关系解释。

## 2. 定义 pair dispersion

对整数 tuple

\[
x=(x_1,\ldots,x_N)
\]

定义

\[
\boxed{
P(x)=\sum_{1\le i<j\le N}(x_i-x_j)^2.
}
\]

这是完全由整数状态之间的两两差构成的关系量。

## 3. P019-X24 —— pair-dispersion 基本恒等式

对任意整数 tuple：

\[
\boxed{
P(x)
=N\sum_i x_i^2
-\left(\sum_i x_i\right)^2.
}
\]

### 证明

展开：

\[
\sum_{i<j}(x_i-x_j)^2
=\sum_{i<j}(x_i^2+x_j^2-2x_ix_j).
\]

每个 `x_i^2` 出现 `N-1` 次，并利用

\[
\left(\sum_i x_i\right)^2
=\sum_i x_i^2+2\sum_{i<j}x_ix_j
\]

即可。∎

全程没有平方根、角度或极限。

## 4. P019-X25 —— fraction-free block merge law

把 tuple 分成左右 blocks：

- left size `m`，total `a`；
- right size `n`，total `b`；
- `M=m+n`；
- parent total `c=a+b`。

定义 imbalance：

\[
\boxed{z=na-mb.}
\]

记三者 pair dispersion 为 `P_L,P_R,P_M`。

则有严格整数递推：

\[
\boxed{
mnP_M
=
nMP_L
+mMP_R
+z^2.
}
\]

### 证明

由 X24：

\[
P_L=m\sum_{L}x_i^2-a^2,
\qquad
P_R=n\sum_{R}x_i^2-b^2.
\]

代入 parent：

\[
mnP_M
=nM(P_L+a^2)
+mM(P_R+b^2)
-mn(a+b)^2.
\]

剩余 quadratic 项满足

\[
nMa^2+mMb^2-mn(a+b)^2=(na-mb)^2=z^2.
\]

得证。∎

这条式子完全 fraction-free。

## 5. `z^2` 的结构意义

X25 表明，在给定两个 child blocks 内部 dispersion 后，把二者接成一个更大 block 时新增的跨块结构恰由

\[
\boxed{z^2}
\]

控制。

若

\[
na=mb,
\]

即两个 blocks 的 total 与 block size 完全成比例，则

\[
z=0,
\]

没有新增 proportional-imbalance 项。

因此 `z` 同时具有：

1. split reconstruction coordinate；
2. proportional allocation defect；
3. pair-dispersion merge witness

三重意义。

## 6. P019-X26 —— `A_p` 的 `q` 可写成纯 pair relation

对 `A_p` 状态，坐标数

\[
N=p+1
\]

且

\[
\sum_i x_i=0.
\]

所以 X24 化为

\[
P(x)=N\sum_i x_i^2.
\]

而 P019 原径向整数二次量为

\[
q(x)=\frac12\sum_i x_i^2.
\]

因此严格有

\[
\boxed{
P(x)=2Nq(x).
}
\]

反过来，`P(x)` 在 `A_p` 整数域上必被 `2N` 整除：

\[
\boxed{
q(x)=P(x)//(2N).
}
\]

这里 `//` 是精确整除，不是隐藏实数除法。

所以 `q` 可以等价理解为：

> `A_p` 全部 slot-pairs 的整数差平方总和经过一个严格可整除尺度投影后的状态。

这不会自动证明物理空间采用该 `q`，但消除了“必须先把 q 解释成连续欧氏范数”的必要性。

## 7. P019-X27 —— ordered contraction tree + imbalance tags 精确重建叶子状态

考虑一个 rooted ordered binary contraction tree：

- 每个 leaf 是一个原始 unit slot；
- 每个 internal node 的左右 child sizes 为 `m,n`；
- parent total 为 `c`；
- internal node 存一个 signed imbalance `z`。

由 Supplement 09：

\[
z=(m+n)a-mc.
\]

若合法性条件

\[
m+n\mid(mc+z)
\]

成立，则 child totals 唯一：

\[
\boxed{
a=(mc+z)//(m+n),
\qquad b=c-a.}
\]

从 root total 开始递归，所有 leaves 的整数 totals 都被唯一恢复。

因此：

\[
\boxed{
\text{ordered contraction tree}
+
\text{one signed }z\text{ per internal node}
+
\text{root total}
}
\]

是当前 fine integer state 的一个 lossless hierarchical encoding。

它不必保存每个 internal node 的大 child totals。

## 8. 与完整 oriented contraction history 的区别

Supplement 07 的完整 oriented contraction flag 还记录：

- 独立 merges 发生的时间先后；
- 每一步 receiver/donor selection history。

ordered tree + `z` tags 只保留最终层级分解与当前 fine state 所需的信息，可能忘记互不嵌套 merges 的实际时间顺序。

所以：

- 若 future query 只依赖**当前 fine integer state**，tree+z 是充分编码之一；
- 若 future query 要求**真实 contraction process history**，该压缩未必 future-safe。

这正是 Supplement 08 future-composition quotient 的任务依赖性。

## 9. P019-X28 —— pair dispersion 可由 imbalance tree 递归恢复

所有 leaf block 都只有一个数，因此

\[
P_{leaf}=0.
\]

每个 internal node 使用 X25：

\[
mnP_M
=
nMP_L+mMP_R+z^2.
\]

所以给定 tree、block sizes 和全部 `z`，可自底向上恢复每个 node 的 pair dispersion。

特别地，若 root 是 `A_p` 零和状态，则最终

\[
P_{root}=2Nq.
\]

因此 radial quadratic state `q` 可以从一棵纯整数关系收缩树的局部 imbalance witnesses 恢复。

这把：

`relation contraction`

与

`radial quadratic observation`

进一步接到同一整数结构中。

## 10. 和“挖球”的关系

挖球研究最初区分：

- graph/relation boundary；
- radial/collision-power boundary。

现在平方层得到新的连接：

- block merge / dimensional contraction 由 tree 表示；
- directional split 由 `z` 表示；
- `z^2` 同时是 pair-dispersion 的局部 merge term；
- 全局 `q` 是整个 pair dispersion 的严格整数投影。

所以 radial 信息并非附着在 relation geometry 外面的独立实数层；至少在当前 `A_p` 工作模型中，它可以由 pair relations 与 contraction imbalance 完整重建。

## 11. 实现与验证

新增：

- `src/enterprise_math/pair_dispersion.py`
  - `pair_dispersion`
  - `pair_dispersion_identity`
  - `merge_pair_dispersion_identity`
  - `zero_sum_quadratic_separation`
- `tests/test_pair_dispersion.py`

有限枚举直接验证：

- X24；
- X25；
- `A_p` 零和情况下 `P=2Nq`。

## 12. 研究纪律

pairwise-square dispersion、variance decomposition、hierarchical contrast decomposition 均可能有成熟前人工作邻居。

本补充当前只把 X24–X28 作为 P019 内部直接整数推导与工具连接，不作原创优先性声明。合并前必须继续 prior-art 映射。

也不把 `P`、`z^2` 自动解释为物理能量、曲率或引力。

## 13. 下一步

1. 找出整棵 tree 上 `z` 的最小合法性/一致性条件，使任意 tag set 可判定是否对应一个整数 fine state；
2. 研究不同 trees 表示同一个 fine state 时，`z` systems 之间是否存在局部整数变换；
3. 若存在局部变换，尝试建立与 tree 无关的 canonical relation coordinates；
4. 把 pair-dispersion merge law 接入 Supplement 08 future-safe quotient，判断什么时候 tree shape 本身也可以消去；
5. 检查 `z` 的局部变换是否与 P021 witness join / intrinsic direction transport 存在统一关系。
