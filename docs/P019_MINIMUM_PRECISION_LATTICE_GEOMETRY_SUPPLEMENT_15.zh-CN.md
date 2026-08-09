# P019 补充 15 —— Capacity-Weighted Relation Field 与“一次降维丢一条内部关系”

状态：`RESEARCH WIP / EXACT INTEGER RELATION LAWS PROVED`

## 1. 动机

Supplement 14 给 unit slots 定义了 tree-independent pair field：

\[
d_{ij}=x_i-x_j.
\]

但 dimension contraction 以后，一个 coarse block 内已经包含多个原始 unit slots。此时若仍简单使用 `c_i-c_j`，会把不同 block capacities 混在一起。

正确的纯整数推广是：把“每单位 slot 的平均差异”做交叉乘法，而不是引入分数。

## 2. 定义 capacity-weighted relation field

对当前 partition 中的 blocks：

- capacity / hidden unit count：
  \[
  m_i\in\mathbb N_{>0};
  \]
- block total：
  \[
  c_i\in\mathbb Z.
  \]

定义：

\[
\boxed{
Z_{ij}=m_jc_i-m_ic_j.
}
\]

若所有 blocks 都是 unit：

\[
m_i=m_j=1,
\]

则

\[
\boxed{Z_{ij}=c_i-c_j=d_{ij}.}
\]

所以普通 pair-difference field 是 weighted field 的 unit-capacity 特例。

## 3. P019-X43 —— weighted antisymmetry 与三块闭合

显然：

\[
\boxed{Z_{ii}=0,}
\qquad
\boxed{Z_{ij}=-Z_{ji}.}
\]

对任意三 blocks `i,j,k`：

\[
\boxed{
m_kZ_{ij}+m_iZ_{jk}+m_jZ_{ki}=0.}
\]

证明直接展开：

\[
m_k(m_jc_i-m_ic_j)
+m_i(m_kc_j-m_jc_k)
+m_j(m_ic_k-m_kc_i)=0.
\]

这是 unit three-cycle law

\[
d_{ij}+d_{jk}+d_{ki}=0
\]

的 capacity-weighted 版本。

## 4. P019-X44 —— weighted field + capacities + grand total 唯一恢复 block totals

令总 capacity 与总量为

\[
M=\sum_i m_i,
\qquad
C=\sum_i c_i.
\]

对固定 `i`：

\[
\sum_jZ_{ij}
=
\sum_j(m_jc_i-m_ic_j)
=
Mc_i-m_iC.
\]

因此：

\[
\boxed{
Mc_i
=m_iC+\sum_jZ_{ij}.
}
\]

只要右侧能被 `M` 精确整除：

\[
\boxed{
c_i=(m_iC+\sum_jZ_{ij})//M.}
\]

所以：

\[
\boxed{
(m_i),\ C,\ (Z_{ij})
}
\]

是当前 coarse block state 的一个 tree-independent relation representation。

capacity tags 不再是额外元数据；它们是定义 coarse relations 所必需的整数结构。

## 5. P019-X45 —— block merge 在 relation field 上只是“容量相加 + relation 相加”

合并 blocks `i,j` 成新 block `u`：

\[
\boxed{m_u=m_i+m_j,}
\]

\[
\boxed{c_u=c_i+c_j.}
\]

对任何未合并 block `k`：

\[
Z_{uk}
=m_k(c_i+c_j)-(m_i+m_j)c_k.
\]

分开：

\[
\boxed{
Z_{uk}
=Z_{ik}+Z_{jk}.
}
\]

未受影响 blocks 之间的关系保持不变。

因此 dimension contraction 在 canonical weighted relation field 上的 forward rule 极其简单：

> **容量相加，外部 relation rows 相加。**

不需要重新解高维几何。

## 6. P019-X46 —— 被删掉的 internal relation 恰好就是 contraction imbalance

合并 `i,j` 前的内部关系：

\[
\boxed{
Z_{ij}=m_jc_i-m_ic_j.
}
\]

这恰好就是 Supplements 09–13 使用的 imbalance tag：

\[
\boxed{z=Z_{ij}.}
\]

但 X45 表明，合并后所有外部 coarse relations 只依赖

\[
c_i+c_j,\qquad m_i+m_j,
\]

而不依赖 `Z_ij`。

所以一次 merge 会从 coarse relation field 中**真正删除**这一条 internal relation degree。

## 7. P019-X47 —— 一个被删掉的 `z` 足以精确反解两个 child totals

设 parent block capacity/total：

\[
M=m+n,
\qquad
c=a+b.
\]

internal relation：

\[
z=na-mb=Ma-mc.
\]

则：

\[
\boxed{
a=(mc+z)//M,}
\]

\[
\boxed{b=c-a.}
\]

合法性为：

\[
\boxed{M\mid(mc+z).}
\]

因此 coarse parent state + split capacities `(m,n)` + lost internal relation `z` 唯一恢复两个 child totals。

随后所有 child-to-external weighted relations 都可由 X43/X44 或定义直接恢复。

所以对于“当前 state 的一次 merge”：

\[
\boxed{
\text{lost internal relation }z
}
\]

是一个完整的 reverse fiber coordinate。

## 8. P019-X48 —— 一次 dimension contraction 精确减少一个 relation degree

当前有 `k` 个 blocks，固定 grand total `C`。

block totals 的自由整数度为：

\[
k-1.
\]

weighted relation field 与之等价，所以：

\[
\boxed{
dim_{relation}=k-1.}
\]

合并两个 blocks 后，block count 变成 `k-1`：

\[
\boxed{
dim_{relation}'=k-2.}
\]

因此：

\[
\boxed{
dim_{relation}-dim_{relation}'=1.}
\]

而 X46/X47 已经识别出被删掉的完整 scalar fiber coordinate：

\[
\boxed{Z_{ij}.}
\]

所以在这一 relation model 中：

> **一次离散降维 = 删除一条独立内部关系。**

这不是“坐标数量少了一个”的同义反复；删除的是一个可以精确参数化 merge fiber、并在保留时可反向恢复的整数 relation witness。

## 9. P019-X49 —— merge fiber 是 internal relation 的等差格

固定 coarse parent capacity/total `(M,c)` 与 split capacities `m,n`。

所有可能 child splits 用 `a\in Z` 参数化：

\[
b=c-a.
\]

对应 internal relation：

\[
z=Ma-mc.
\]

所以所有合法 `z` 满足同一个同余类：

\[
\boxed{
z\equiv-mc\pmod M.}
\]

并且相邻 child split `a->a+1` 时：

\[
\boxed{z\to z+M.}
\]

因此无能量约束的 merge fiber 是一个一维整数等差格。

若再加入 P019 collision-power ball / slack 约束，Supplement 07 的 left-total feasible interval

\[
a\in[L,U]
\]

严格变成：

\[
\boxed{
z\in
\{ML-mc,\ M(L+1)-mc,\ldots,MU-mc\}.}
\]

fiber multiplicity：

\[
\boxed{
U-L+1
=
\frac{z_{max}-z_{min}}{M}+1.
}
\]

所以 P011 fiber multiplicity、P019 interval witness 与 weighted relation field 是同一个结构的三种读法。

## 10. forward merge = relation collapse；保留 `z` = reversible completion

定义 forward merge 时若只保留：

- merged capacity；
- merged total；
- merged external weighted field；

则多个不同 `z` 的 fine states 会进入同一个 coarse state。

这是一个真正的 many-to-one relation collapse。

若同时保存 internal `z`，则该单步 merge 可反向恢复 child totals。

因此：

\[
\boxed{
\text{merge without }z
=
\text{relation collapse},
}
\]

\[
\boxed{
\text{merge with }z
=
\text{reversible completion candidate}.
}
\]

这与 P010/P011 的 history/fiber 语言直接对接。

是否自然本体真的保存 `z`，仍是 ontology/physical hypothesis；数学上只区分 forward coarse map 与其显式 witness completion。

## 11. 与 Contraction Atlas 的关系重新整理

现在 Contraction Atlas 不再需要被理解为“创造 `z`”。

真正顺序应是：

1. tree-independent weighted relation field `Z` 已存在；
2. binary contraction tree 选择一系列 nested block cuts；
3. 每个 internal node 读取对应 cut 的 `Z(A,B)` 作为局部 coordinate；
4. tree rotation 只是换一组 nested cuts；
5. local reassociation 是不同 cut-sum coordinates 之间的整数换基。

因此：

\[
\boxed{
\text{Contraction Atlas}
=
\text{weighted relation field 的 hierarchical cut charts}.
}
\]

这比把 tree 当本体更干净。

## 12. LEGO 解释

每个 block capacity `m_i` 可以解释为该 coarse LEGO block 内已合并的原始 unit-slot 数。

合并只执行：

\[
\boxed{m_i+m_j}
\]

和

\[
\boxed{c_i+c_j}. 
\]

对外关系自动线性相加。

因此 unit `1` 不需要在升降维时改变数值身份；维度变化发生在**关系自由度与 block capacity structure**上。

## 13. 与球形挖除的接口

对原始 unit blocks：

\[
m_i=1,
\]

weighted field 就是普通 pair-difference field。

挖 graph ball 后固定一个 primitive direction `i->j`，之前的坐标合并：

\[
(i,j)\to u
\]

现在可重新解释为：

- 删除内部 relation `Z_ij`；
- capacity `1+1=2`；
- 对外 relation rows 相加。

所以三维空腔“沿一个 primitive relation 降成二维”的双射，可以继续尝试完全用 weighted relation contraction 表述，而无需引用外部欧氏投影。

## 14. 实现与验证

新增：

- `src/enterprise_math/weighted_relation_field.py`
  - `weighted_relation_field`
  - `weighted_relation_field_is_closed`
  - `recover_totals_from_weighted_field`
  - `merge_weighted_relation_field`
  - `split_two_block_totals_from_internal_relation`
  - `weighted_relation_dimension`
- `tests/test_weighted_relation_field.py`

整数枚举验证：

- unit capacity 退化为普通 difference field；
- weighted three-block closure；
- field+capacities+grand total 的 exact recovery；
- forward merge external relation additivity；
- discarded internal relation 精确等于 `z`；
- `z` 的 reverse split；
- 每 merge 一次 relation dimension 减 1。

## 15. 下一步

1. 把 graph-ball directional contraction theorem X02/X03 直接改写成 weighted-field merge theorem；
2. 对 radial/collision-power tagged balls，把 fiber interval 改写成 internal `Z_ij` arithmetic progression；
3. 研究 weighted relation field 上是否存在 tree-independent future-safe quotient，可替代大量 historical contraction flags；
4. 把 P021 witness relation join 改写成“保留哪些 deleted internal relations 才足以未来复合”；
5. 研究多步 merge 后 lost `Z` 集合是否形成一个自然的 exact relation homology/provenance object，但不得无必要引入连续拓扑术语。
