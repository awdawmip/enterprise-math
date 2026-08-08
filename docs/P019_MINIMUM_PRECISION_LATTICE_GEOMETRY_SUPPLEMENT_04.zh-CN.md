# P019 补充 04 —— 纤维最小收缩、块标记径向球与严格跨维闭合

状态：`RESEARCH WIP / CORE IDENTITIES PROVED COMBINATORIALLY`  
范围：有限精度径向球、维度收缩、min-plus 合成、碰撞解释、带 block-size tag 的跨维边界递归  
纪律：全文只使用整数、有限最小值、有限差分和离散关系；不引入微积分或连续极限。

## 1. 上一补充留下的问题

Supplement 03 证明：`A_p` primitive graph ball 在固定 primitive direction 上挖出的 cut boundary 与同半径 `A_{p-1}` graph ball 存在严格双射。

但对平方径向能量

\[
E(x)=\sum_i x_i^2
\]

或等价的 `q=E/2`，若降维后仍强行与**无标记**的普通低维径向球比较，则该恒等式失败。

本补充说明失败原因并不是“径向球无法跨维统一”，而是：

> 合并坐标时，若把“一个低维坐标内部由多少个原始单位槽位组成”这一关系上下文擦掉，就丢失了径向能量所需的信息。

保留 block-size tag 后，径向球重新获得严格跨维闭合。

## 2. P019-X04 —— 单块的纤维最小平方能量

给定 `m>=1` 个整数槽位，约束

\[
a_1+\cdots+a_m=c.
\]

定义

\[
\psi_m(c)
:=
\min\left\{\sum_{i=1}^m a_i^2:\sum_i a_i=c\right\}.
\]

令

\[
|c|=mq+r,\qquad 0\le r<m.
\]

则平方和在各槽位尽可能均匀时达到最小值，故

\[
\boxed{
\psi_m(c)
=(m-r)q^2+r(q+1)^2.
}
\]

这是纯整数闭式。

特别地，

\[
\boxed{\psi_m(1)=1\quad\forall m\ge1.}
\]

所以“一个单位 `1` 在任意有限维槽位容量中仍然是 `1`”在这里成为严格的最小能量不变量，而不只是解释性口号。

当 `|c|<=m` 时，

\[
\psi_m(c)=|c|.
\]

只有当单位数超过可用槽位，必须发生叠放时，平方能量才高于单位计数。

## 3. 与 P011 collision spectrum 的直接连接

设 `n=|c|` 个单位被放入 `m` 个槽位，占用数为 `a_i>=0`。恒等式

\[
a_i^2=a_i+2\binom{a_i}{2}
\]

给出

\[
\sum_i a_i^2
=n+2\sum_i\binom{a_i}{2}.
\]

因此

\[
\boxed{
\psi_m(n)
=n+2J^{\min}_2(n,m),
}
\]

其中

\[
J^{\min}_2(n,m)
=
\min_{a_1+\cdots+a_m=n}
\sum_i\binom{a_i}{2}.
\]

所以平方径向能量可以读成：

> 单位总数 + 两倍不可避免的最小二元碰撞数。

这把 P019 径向能量与 P011 的 collision multiplicity 直接接起来。

## 4. P019-X05 —— 维度加法对应 min-plus 合成

对任意 `m,n>=1`，

\[
\boxed{
\psi_{m+n}(c)
=
\min_{a+b=c}\left(\psi_m(a)+\psi_n(b)\right).
}
\]

证明直接来自约束集合的重新分组：把 `m+n` 个槽位分成两组，第一组总和为 `a`，第二组总和为 `b=c-a`；先在两组内部各自取最小，再对所有组间分配取最小，与直接在全部 `m+n` 个槽位上取最小完全相同。

因此 block size 的加法在能量侧表现为 min-plus convolution：

\[
\boxed{
\psi_m\;\square\;\psi_n=\psi_{m+n}.
}
\]

结合律来自整数加法本身：

\[
(\psi_a\square\psi_b)\square\psi_c
=
\psi_a\square(\psi_b\square\psi_c)
=
\psi_{a+b+c}.
\]

所以组合顺序不改变最终维度收缩结果。

## 5. 带 block-size tag 的收缩径向能量

令

\[
\mathbf m=(m_1,\ldots,m_k),\qquad m_i\ge1,
\]

表示当前 `k` 个可见坐标块分别由多少个原始槽位合并而来。

对

\[
c=(c_1,\ldots,c_k),\qquad \sum_i c_i=0,
\]

定义

\[
\boxed{
E_{\mathbf m}(c)
=
\sum_{i=1}^k\psi_{m_i}(c_i).
}
\]

原始 `A_p` 平方能量对应

\[
\mathbf m=(1,1,\ldots,1)
\]

共 `p+1` 个块，因为 `\psi_1(c)=c^2`。

定义带标记径向球

\[
B_{\mathbf m}(T)
=
\{c:\sum_i c_i=0,\ E_{\mathbf m}(c)\le T\}.
\]

`m_i` 不是额外连续参数，而是一个整数 relation-context tag：它记录该可见坐标内部还承载多少原始单位槽位。

## 6. P019-X06 —— 收缩算子在该族中严格闭合

若把第 `i,j` 两个块合并，令

\[
c_*=c_i+c_j,
\qquad
m_*=m_i+m_j,
\]

则在所有满足固定 `c_*` 的高维 fiber 上，原能量的最小值为

\[
\min_{a+b=c_*}
\left(\psi_{m_i}(a)+\psi_{m_j}(b)\right)
=
\psi_{m_i+m_j}(c_*).
\]

所以 fiber-minimum contraction

\[
(\pi_*E)(y)
:=
\min_{\pi(x)=y}E(x)
\]

把 `E_m` 精确送入同一个家族：

\[
\boxed{
E_{(\ldots,m_i,m_j,\ldots)}
\xrightarrow{\text{merge }i,j}
E_{(\ldots,m_i+m_j,\ldots)}.
}
\]

这给径向结构一个严格的整数“重整化”规则：维度被压缩后并未消失，而被编码进 block sizes。

## 7. 一步搬运的闭式能量变化

`psi_m` 的前向有限差分为

\[
\boxed{
\psi_m(c+1)-\psi_m(c)
=2\left\lfloor\frac{c}{m}\right\rfloor+1.
}
\]

因此若从块 `j` 搬一个单位到块 `i`：

\[
c_i\mapsto c_i+1,
\qquad
c_j\mapsto c_j-1,
\]

则

\[
\boxed{
\Delta E
=2\left(
\left\lfloor\frac{c_i}{m_i}\right\rfloor
-
\left\lfloor\frac{c_j-1}{m_j}\right\rfloor
\right).
}
\]

当所有 `m_i=1` 时退化为

\[
\Delta E=2(c_i-c_j+1),
\]

即原始平方能量沿 primitive root 的变化式。

## 8. P019-X07 —— 径向 cut boundary 的严格跨维恒等式恢复

固定一个有向 transfer `j -> i`。对每个合并后的低维状态 `y`，保持其余块和 `c_i+c_j` 不变，在该 fiber 上用一个整数 `a=c_i` 参数化。

fiber energy

\[
F_y(a)
=
\psi_{m_i}(a)
+
\psi_{m_j}(c_*-a)
+
R_y
\]

是离散凸函数，因为 `psi_m` 的一阶差分单调不减。

因此其阈值下集合

\[
\{a:F_y(a)\le T\}
\]

若非空，必为一个有限整数区间。沿有向 transfer `a -> a+1`，每个非空 fiber 恰有**一条**边从该区间右端穿出阈值球。

而该 fiber 非空当且仅当

\[
\min_aF_y(a)\le T.
\]

由 X05，

\[
\min_aF_y(a)
=
\psi_{m_i+m_j}(c_*)+R_y,
\]

恰好就是合并后的 tagged energy。

因此得到严格双射：

\[
\boxed{
\text{directed cut edges of }B_{\mathbf m}(T)
\text{ in channel }j\to i
\;\longleftrightarrow\;
B_{\mathbf m'}(T),
}
\]

其中 `m'` 是把 `m_i,m_j` 替换为 `m_i+m_j` 的分拆。

故

\[
\boxed{
|C_{\mathbf m,j\to i}(T)|
=
|B_{\mathbf m'}(T)|.
}
\]

这恢复了 radial cavity 的严格跨维递归。

上一补充看到的“radial ball 不满足 `E_p=p(p+1)V_{p-1}`”现在应更精确地解释为：**如果收缩后错误地删除 block-size tag，公式失败；保留 tag 后，固定方向的 cut boundary 仍严格等于一个低一维 tagged ball。**

## 9. graph 与 radial 的统一解释

现在两类球可放入同一个框架：

### graph cost

primitive graph cost 在坐标合并下的 fiber-minimum 仍是同一形式，所以 block-size tag 对它不可见。

因此 graph ball 是收缩算子的一个**同形固定族**：

\[
B_p^G(r)\to B_{p-1}^G(r).
\]

### radial square energy

平方能量在收缩后进入 `psi_m` family，block-size tag 不可删除：

\[
(1,1,\ldots,1)
\to
(2,1,\ldots,1)
\to
(3,1,\ldots)
\text{ or }(2,2,1,\ldots)
\to\cdots.
\]

无论按什么结合顺序合并，只要最终 block partition 相同，X05 保证结果相同。

所以二者不是“一个能降维，一个不能”，而是：

- graph geometry：收缩后 context-free；
- radial geometry：收缩后 context-sensitive，但在 tagged family 内严格闭合。

这正好支持 P019 已形成的原型：

`relative state = integer distance + precision tag + relation context`。

## 10. 维度与信息保存

设原始 `A_p` 有 `p+1` 个 unit slots。任意收缩后 block sizes 满足

\[
\sum_i m_i=p+1.
\]

因此：

- 当前显式关系维数由可见块数 `k` 给出 `k-1`；
- 已被收缩隐藏的内部容量保留在 `m_i`；
- 原始总槽位数从 `sum m_i` 完整可恢复。

这说明维度收缩不必等于信息抹除。只要 block-size tag 不被擦掉，低维状态仍携带其高维来源容量。

最终全部合并时只有一个块 `m_1=p+1`，零和约束强制 `c_1=0`，球退化为单点，但原始槽位容量仍由 tag `p+1` 保存。

## 11. 当前最重要的解释

本补充把“乐高”直觉推进成以下纯整数结构：

\[
\boxed{
\text{unit slots add}
\Longleftrightarrow
\text{block sizes add}
\Longleftrightarrow
\text{fiber energies min-plus compose}
}
\]

而 `psi_m(1)=1` 保证最小单位本身不因维度变化而改变。

同时

\[
\psi_m(n)=n+2J_2^{\min}(n,m)
\]

说明所谓径向平方代价并不需要先解释成连续长度平方；它也可以完全离散地解释为“单位计数 + 不可避免碰撞”。

## 12. 状态纪律与下一步

当前已证明/回归的是有限整数恒等式和组合双射。尚未证明自然空间采用这一 family，也尚未把 `psi_m` 解释为物理能量、引力或时空曲率。

下一步优先：

1. 把 X04-X07 形式化为 Lean，尤其是 balanced minimizer、min-plus associativity 与 cut-fiber unique-exit theorem；
2. 将 `block_sizes` 升格为 typed relation-context，而不是裸 tuple；
3. 研究不同 contraction tree 在相同最终 partition 下是否不仅能量相同，连 incidence / collision spectrum 也同构；
4. 研究 `J_k` 而非仅 `J_2` 是否给出更高阶 `psi` family；
5. 对 graph fixed family 与 radial tagged family 构造统一的 fiber-minimum functor 语言；
6. 检索 infimal projection、discrete convex analysis、min-plus convolution、root-lattice contraction 等前人工作，novelty 暂保持未验证。
