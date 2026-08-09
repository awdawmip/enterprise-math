# P019 补充 16 —— Partition Relation Quotient 与统一方向挖球定理

状态：`RESEARCH WIP / EXACT FINITE INTEGER THEOREMS PROVED`

## 1. 目标

前面的路线曾经历一个假冲突：

- graph ball 的方向挖除可严格降成普通低一维球；
- radial ball 若擦掉 capacity tag，则简单低维公式失败。

Supplements 04–15 已逐步表明，问题不在 radial 几何，而在**粗化时删除了 block capacity / relation context**。

本补充把整个结果压成一个统一 partition-relation 定理。

## 2. partition quotient 的 tree-free 定义

已有 current weighted relation state：

\[
(m_i,c_i,Z_{ij}),
\qquad
Z_{ij}=m_jc_i-m_ic_j.
\]

取当前 block index set 的任意 partition：

\[
\Pi=\{A_1,\ldots,A_k\}.
\]

定义 coarse capacity 与 coarse total：

\[
\boxed{
M_\alpha=\sum_{i\in A_\alpha}m_i,
}
\]

\[
\boxed{
C_\alpha=\sum_{i\in A_\alpha}c_i.
}
\]

定义 coarse relation：

\[
\boxed{
Z^{\Pi}_{\alpha\beta}
=
\sum_{i\in A_\alpha}
\sum_{j\in A_\beta}Z_{ij}.
}
\]

直接展开可得：

\[
\boxed{
Z^{\Pi}_{\alpha\beta}
=M_\beta C_\alpha-M_\alpha C_\beta.
}
\]

所以 arbitrary partition quotient 自动仍属于同一个 weighted relation family。

## 3. P019-X50 —— partition coarsening 严格复合

若

\[
\Pi\preceq\Sigma
\]

表示 `Sigma` 比 `Pi` 更粗，则可先：

\[
Z\to Z^{\Pi}
\]

再：

\[
Z^{\Pi}\to (Z^{\Pi})^{\Sigma/\Pi}.
\]

由于 relation quotient 只是有限双重求和：

\[
\boxed{
(Z^{\Pi})^{\Sigma/\Pi}=Z^{\Sigma}.
}
\]

因此：

\[
\boxed{
\text{先粗化再粗化}
=
\text{直接粗化到最终 partition}.
}
\]

binary contraction tree 只是把同一个 partition quotient 分解成一串 two-block merges 的执行方案。

coarse current relation state 不依赖这条执行树。

## 4. P019-X51 —— dimension 是 partition block count 减 1

固定 grand total。

partition `Pi` 有 `k` 个 coarse blocks，则：

\[
\boxed{
dim_{relation}(\Pi)=k-1.}
\]

一次 binary merge 是 partition 中两个 blocks 合并：

\[
k\to k-1,
\]

所以：

\[
\boxed{
dim\to dim-1.}
\]

从 `N` 个 singleton units 完全粗化到一个 block，恰做 `N-1` 次独立 relation elimination。

这与 `A_p` 的 `N=p+1` 给出：

\[
\boxed{p=N-1.}
\]

## 5. P019-X52 —— merge fiber 是 coarse quotient 的 kernel direction

只看两个待合并 blocks：

- capacities `m,n`；
- parent total `c=a+b`；
- `M=m+n`。

在保持 coarse parent state 不变时，所有 fine lifts：

\[
(a,b)=(a,c-a),
\qquad a\in\mathbb Z.
\]

相邻 lifts：

\[
(a,b)\to(a+1,b-1).
\]

这是一个 primitive internal redistribution direction。

对应 internal weighted relation：

\[
z=na-mb=Ma-mc.
\]

因此一次 primitive fiber move：

\[
\boxed{z\to z+M.}
\]

而所有 merged external relations

\[
Z_{uk}=Z_{ik}+Z_{jk}
\]

保持不变。

所以 merge fiber 真正就是 coarse quotient 看不见的一条一维整数 relation line。

## 6. tagged collision-power ball

对 block capacities

\[
\mathbf m=(m_1,\ldots,m_k)
\]

与 totals `c_i`，定义：

\[
\boxed{
E_{\mathbf m}^{(s)}(c)
=
\sum_i\Psi_{m_i,s}(c_i),
}
\]

并取 fixed-total ball：

\[
\boxed{
B_{\mathbf m}^{(s)}(T)
=
\{c:\sum_i c_i=C,\ E_{\mathbf m}^{(s)}(c)\le T\}.
}
\]

对于 `A_p` 使用 `C=0`。

## 7. P019-X53 —— 统一 directional excavation bijection

固定 donor block `j` 与 receiver block `i`。

定义 directional cut boundary：

\[
C_{\mathbf m,j\to i}^{(s)}(T)
=
\{c\in B_{\mathbf m}^{(s)}(T):
 c+e_i-e_j\notin B_{\mathbf m}^{(s)}(T)\}.
\]

把 `i,j` 合并成 parent block，capacity：

\[
m_i+m_j,
\]

得到 merged capacity tuple `m'`。

投影：

\[
\pi_{ij}(c)
=
(c_i+c_j,\text{所有其他 totals}).
\]

则：

\[
\boxed{
\pi_{ij}:
C_{\mathbf m,j\to i}^{(s)}(T)
\overset{\sim}{\longrightarrow}
B_{\mathbf m'}^{(s)}(T)
}
\]

是集合级双射。

### 证明

固定任意 coarse state `y` 于右侧。

其 `i,j` fiber 的 parent total 记为 `c`，其他 blocks 的 energy 为 `E_other`。

coarse minimum energy：

\[
E_{other}+\Psi_{m_i+m_j,s}(c).
\]

因为 `y` 在 coarse ball 内：

\[
\omega
=T-E_{other}-\Psi_{m_i+m_j,s}(c)
\ge0.
\]

fine split 令 receiver total 为 `a`，fiber energy：

\[
f(a)
=
\Psi_{m_i,s}(a)
+
\Psi_{m_j,s}(c-a).
\]

Supplement 07 已证明 `f` 离散凸，feasible split set 恰为整数 interval：

\[
[L,U].
\]

方向 `j->i` 对应 `a->a+1`。

所以该 fiber 中唯一满足“当前在 ball 内、下一步穿出”的 state 正是：

\[
\boxed{a=U.}
\]

每个 coarse state 恰有一个 directional boundary lift，且每个 directional boundary state 投影到唯一 coarse state。故为双射。∎

这一定理对所有整数 `s>=1` 使用同一证明。

## 8. graph 与 radial 的旧冲突被消除

### `s=1`

\[
\Psi_{m,1}(c)=|c|
\]

与 capacity `m` 完全无关。

所以 merge 后即使 parent capacity 变成 `m_i+m_j`，ball membership 看不到这个 tag。

因此 X53 在 unit `A_p` graph geometry 中自动退化成：

\[
\boxed{
\text{p-dimensional directional graph boundary}
\cong
\text{ordinary (p-1)-dimensional graph ball}.
}
\]

这就是 Supplement 03 的 X02。

### `s=2`

\[
\Psi_{m,2}(c)
\]

依赖 capacity。

所以同一个 X53 给出：

\[
\boxed{
\text{radial directional boundary}
\cong
\text{capacity-tagged lower-dimensional radial ball}.
}
\]

此前 radial simple formula 的失败，仅仅是把 merged capacity tag 擦掉后拿它去比较 untagged lower ball。

因此 graph/radial 不再是两套 incompatible contractions。

它们是：

\[
\boxed{
\text{同一个 weighted relation contraction}
+
\text{不同 observation order }s.
}
\]

## 9. P019-X54 —— unit symmetric case 的总方向边界

从 `N` 个 unit blocks 开始：

\[
\mathbf m=(1,\ldots,1).
\]

有

\[
N(N-1)
\]

个有向 primitive transfer directions `j->i`。

由于 unit state 在 slot permutation 下对称，每个方向的 merged capacity pattern 都同构于：

\[
(2,1,\ldots,1).
\]

所以总有向 cut-edge 数：

\[
\boxed{
E_{N,s}(T)
=N(N-1)
\left|
B_{(2,1,\ldots,1)}^{(s)}(T)
\right|.
}
\]

当 `s=1` 时 capacity 2 隐身，于是：

\[
\boxed{
E_{N,1}(T)
=N(N-1)|B_{N-1}^{(1)}(T)|.
}
\]

对 `A_p`，`N=p+1`，恢复：

\[
\boxed{
E_p(r)=p(p+1)V_{p-1}(r)
}
\]

（阈值与 graph radius 按 `E^(1)=2d_G` 对应）。

所以早期 graph-ball 公式现在成为 X53 的 `s=1` 特例，而不是孤立巧合。

## 10. internal `Z_ij` fiber 与 boundary root

在固定 coarse state 的 fiber 中：

\[
z=Ma-mc.
\]

因为 `a` 的 feasible set 是 `[L,U]`，所以 internal relation 的 feasible set是：

\[
\boxed{
\{ML-mc,\ M(L+1)-mc,\ldots,MU-mc\}.
}
\]

方向 boundary 就是最大 internal relation：

\[
\boxed{z_{max}=MU-mc.}
\]

反方向是 `z_min`。

因此 Supplement 09 的 fiber root 也可以完全解释为：

> **在 coarse quotient 的 kernel relation line 上，找不超过当前 energy slack 的最大合法 internal relation state。**

这与 P008 integer-root/adjoint 骨架直接一致。

## 11. 与 P018 partition precision 的接口

P018 已经把有限 precision 理解为 partition/coarse-fiber 结构。

weighted relation quotient 给出一个具体几何实例：

- partition block = coarse finite-resolution unit；
- capacity = block 中保留的 original unit count；
- weighted field = coarse blocks 之间仍可见的 relation；
- internal deleted `Z` = 被此次 coarse observation 擦掉的 relation detail；
- refinement = 重新暴露某些 internal relations。

所以 dimension contraction 与 precision coarsening 在这里开始共享同一个 partition language。

## 12. 与 P010/P011/P021 的接口

- P010：merge 是 many-to-one，history fiber 可扩大；
- P011：有限 energy 下 internal relation fiber multiplicity 可由 interval 长度精确计算；
- P021：多步 future composition 前，不能把需要 join 的 exact witness 只剩 cardinality；
- P019：被删除的 internal `Z` 给出 relation-level witness coordinate。

因此下一步可以把“future-safe trace”改写成：

> 在一串 partition coarsenings 后，哪些 deleted internal `Z` relations 对允许的未来操作仍可观测/可组合？

## 13. 实现与验证

`src/enterprise_math/weighted_relation_field.py` 新增 arbitrary partition quotient：

- `coarsen_weighted_relation_field`。

并把 binary merge 改为 partition quotient 的 two-block 特例。

`tests/test_weighted_relation_field.py` 增加：

- arbitrary partition aggregation 与直接 capacities/totals 计算一致；
- nested coarsening 与 direct final coarsening 完全一致。

此前 collision-power boundary tests 已对 `s=1..4`、多个 partitions 与 thresholds 验证 X53 的 cut-count 影子；当前文档给出集合级 interval-endpoint 证明。

## 14. 当前统一图景

现在 dimensional excavation 可以压成：

\[
\boxed{
\text{unit LEGO states}
\to
\text{pair relation field}
\to
\text{capacity-weighted partition quotient}
\to
\text{delete one internal }Z\text{ per binary merge}
}
\]

与此同时：

\[
\boxed{
\text{collision order }s
\to
\Psi_{m,s}
\to
\text{同一个 directional-boundary quotient theorem}.
}
\]

所以“高维是否能用低维简单运算统一”在当前工作模型中已有一个非常具体的正答案：

> **所有有限维 relation contraction 都由同一个二元 block merge 生成；所有 collision-power ball 的方向表面都由同一个 fiber-endpoint lift 降一维。**

## 15. 下一步

1. 把 X53 形式化成 Lean 的 finite-fiber order-adjoint/bijection；
2. 直接在 weighted relation field 上实现 boundary lift，不再依赖显式 fine coordinate enumeration；
3. 将 P018 的 abstract partition refinement 与 weighted relation quotient 做正式接口；
4. 把 future-safe quotient 施加到 deleted internal `Z` witness families；
5. 研究是否存在“只保留最少 deleted relations 仍保证指定未来 geometry/dynamics exact”的 canonical relation memory。
