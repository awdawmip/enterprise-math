# P019 补充 12 —— Contraction Atlas 与局部整数 Tree Rotation

状态：`RESEARCH WIP / EXACT LOCAL TRANSFORMS PROVED`

## 1. 问题

Supplement 11 给出：

`ordered contraction tree + root total + internal imbalance tags z`

可以无损表示当前 fine integer state。

但如果不同 contraction trees 都能表示同一个 fine state，则 tree 仍可能只是一个坐标选择，而不是状态本体。

本补充构造不同二叉树之间的局部整数坐标变换。

## 2. 三块局部旋转

取连续三个 blocks `A,B,C`：

- sizes `m,n,k`；
- totals `a,b,c`。

在 parenthesization

\[
((A,B),C)
\]

上定义

\[
\boxed{
u=na-mb}
\]

和

\[
\boxed{
v=k(a+b)-(m+n)c.}
\]

旋转到

\[
(A,(B,C))
\]

后，定义

\[
\boxed{
u'=kb-nc}
\]

和

\[
\boxed{
v'=(n+k)a-m(b+c).}
\]

## 3. P019-X29 —— 局部 reassociation 只作用于 imbalance tags

上述四个整数满足：

\[
\boxed{
(m+n)u'=nv-ku
}
\]

以及

\[
\boxed{
(m+n)v'=(m+n+k)u+mv.
}
\]

### 证明

直接代入 `u,v`：

\[
nv-ku
=nk(a+b)-n(m+n)c-kn a+km b
=(m+n)(kb-nc).
\]

第二式同理展开：

\[
(m+n+k)(na-mb)+m[k(a+b)-(m+n)c]
=(m+n)[(n+k)a-m(b+c)].
\]

得证。∎

因此不需要恢复叶子 states，也不需要重新枚举 fiber，就能完成局部 tree rotation。

合法 relation state 自动满足两个 numerator 被 `m+n` 整除。

## 4. P019-X30 —— 逆变换同样是整数局部式

反方向从 `A,(B,C)` 回到 `((A,B),C)`：

\[
\boxed{
(n+k)u=nv'-mu'
}
\]

\[
\boxed{
(n+k)v=(m+n+k)u'+kv'.
}
\]

所以 local rotation 在合法 imbalance lattice 上可逆。

这不是在整个 `Z^2` 上任意做有理线性变换；合法 tags 自带对应整除约束。

## 5. 单位三槽例子

当

\[
m=n=k=1,
\]

有

\[
u=x-y,
\qquad
v=x+y-2z.
\]

旋转后：

\[
u'=y-z,
\qquad
v'=2x-y-z.
\]

X29 化成：

\[
\boxed{2u'=v-u}
\]

\[
\boxed{2v'=v+3u.}
\]

合法三元整数 state 自动保证右侧为偶数。

## 6. P019-X31 —— tree rotation 保持 pair-dispersion quadratic content

令

\[
N=m+n+k.
\]

X29 可推出 fraction-free invariant：

\[
\boxed{
(n+k)
\bigl(kN u^2+mn v^2\bigr)
=
(m+n)
\bigl(mN {u'}^2+nk {v'}^2\bigr).
}
\]

单位三槽退化为：

\[
\boxed{
3u^2+v^2
=
3{u'}^2+{v'}^2.
}
\]

而由 Supplement 11：

\[
3u^2+v^2=2P(x,y,z).
\]

所以局部 reassociation 改变 relation coordinates，但不改变它们编码的 pair dispersion。

## 7. P019-X32 —— Contraction Atlas

固定一组 labeled leaves 与 root total。

对每棵 rooted ordered binary tree `T`，把每个 internal node 的 imbalance 组成坐标 tuple：

\[
z_T.
\]

Supplement 11 已证明：

\[
(T,z_T,root\ total)
\]

唯一确定 fine leaf state。

X29/X30 给相邻 tree rotations 之间的 exact local coordinate transition。

因此可以把：

- binary trees 视为离散 charts；
- legal imbalance lattices 视为 chart coordinate domains；
- reassociation formulas 视为 transition maps。

当前把这一工具候选称为：

\[
\boxed{\textbf{Contraction Atlas}}
\]

这里的 “atlas” 只是离散坐标图语言，不引入连续流形。

## 8. rotation coherence

任意 local rotation 都是从同一个 block totals 代数消元得到。

因此若一串合法 rotations 从 tree `T` 走到 tree `T'`，所得最终 tags 必然等于直接从同一个 fine leaf state 在 `T'` 上计算的 tags。

所以：

> 在合法 imbalance states 上，tree-transition 的结果只依赖起点 fine state 与终点 tree，不依赖中间 rotation path。

特别地，任何 rotation loop 返回原 tree 时，所有 legal tags 返回原值。

这是当前 contraction-coordinate 的 coherence 性质。

完整的 associahedron/categorical coherence 属于成熟数学邻域；P019 不对一般 tree-rotation coherence 机制作原创声明。

## 9. tree 是否可以删除？

需要严格按 Supplement 08 的 future language 判断。

### 当前状态型问题

若 future query 只依赖当前 fine leaf state 或 tree-invariant relation observables（例如 `P,q`），则不同 `(T,z_T)` 若通过合法 rotations 表示同一 leaf state，可以安全视为同一个 relation state 的不同坐标表示。

这时 tree shape 不应被当作额外本体信息。

### 历史型问题

若 future query 包含：

- 实际哪两个 blocks 先合并；
- 哪一步 receiver/donor selection 真正发生；
- causal/history provenance；

则 rotation quotient 会删除真实历史，不 future-safe。

所以：

\[
\boxed{
\text{representation tree}
\neq
\text{historical contraction trace}
}
\]

必须分开。

## 10. 与 P021 的接口

P021 已证明：direction transport 的 exact witness relation 与 cardinality shadow 不能混同。

Contraction Atlas 给出同类分层：

- `tree+z`：一种 exact current-state witness coordinate；
- rotation class：tree-independent current relation state；
- historical oriented flag：真实 process witness。

是否从 historical flag 降到 rotation class，必须由 future-safe quotient 证明，而不能自动进行。

## 11. 实现与验证

`src/enterprise_math/pair_dispersion.py` 新增：

- `reassociate_imbalances`；
- `reassociation_quadratic_identity`。

`tests/test_pair_dispersion.py` 对：

- `m,n,k=1..3`；
- 多个正负 block totals

逐项验证：

- X29 local transport；
- X31 quadratic invariant；
- 单位三槽 closed example。

## 12. 进一步含义

这一步给“乐高”模型增加了一个重要性质：

> 同一组 LEGO units 可以先以不同层级顺序组合；只要我们讨论的是最终关系 state 而不是实际历史，组合树的差异可以通过局部整数换基运输，而不需要引入连续旋转坐标。

因此“维度/关系结构”不必绑定某一棵固定分解树。

## 13. 下一步

1. 实现一般 tree 数据结构与 rotation path，直接验证四块 pentagon coherence；
2. 研究 legal imbalance lattice 的最小同余约束；
3. 判断 rotation equivalence class 是否能直接用更小的 tree-independent integer invariants 表示；
4. 寻找 `P` 之外足以重建完整 relation state 的 invariant family；
5. 把 Contraction Atlas 与 P012 automorphism charts、P021 witness transport、P018 precision detail 进一步统一。
