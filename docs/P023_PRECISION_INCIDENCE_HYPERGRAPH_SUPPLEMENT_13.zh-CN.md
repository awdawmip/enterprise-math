# P023 —— 高阶 precision incidence hypergraph，补充 13

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023，并连接 A4 高阶关系边界  
依赖：P023-S9/S11/S12 与有限 joint partitions  
纪律：超图、多重交、条件 extension degree 都属于成熟组合结构。本补充的项目作用是确定高阶 precision 的精确对象，并给出 pairwise summary 的可复用 no-go theorem。

## 1. 为什么 pairwise precision geometry 不够

S12 对两个 task 给出完整 incidence graph 与精确 pairwise repair metric。

但对三个以上 tasks，所有两两 block intersections 并不必然决定哪些 block tuples 能够同时拥有共同 state。

因此一个 pairwise metric 可以完全正确，却仍然不足以表示 joint task precision。

## 2. Realized precision hypergraph

令

\[
E_1,\ldots,E_m
\]

是同一个有限状态集 `X` 上的 precision relations。

定义

\[
\boxed{
\Gamma(E_1,\ldots,E_m)
=
\{(B_1,\ldots,B_m):
B_i\in X/E_i,
\ \bigcap_i B_i\ne\varnothing\}.
}
\]

`Gamma` 的元素是实际实现的 block tuples，而不是完整 Cartesian product 中的所有形式 tuples。

## 3. P023-S13-T01 —— hyperedges 恰好就是 joint precision classes

状态：`PROVED`。

共同 refinement

\[
E_* = \bigcap_{i=1}^m E_i
\]

对每一个实际实现的 component-block tuple 恰好产生一个 block。因此

\[
\boxed{
|X/E_*|
=|
\Gamma(E_1,\ldots,E_m)
|.
}
\]

更强地，映射

\[
[x]_{E_*}
\mapsto
([x]_{E_1},\ldots,[x]_{E_m})
\]

在 joint quotient classes 与 realized hyperedges 之间给出双射。

所以 precision hypergraph 是有限 joint task quotient 的精确表示。

## 4. Formal-product defect

形式候选数为

\[
\prod_i |X/E_i|.
\]

定义

\[
\boxed{
U(E_1,\ldots,E_m)
=
\prod_i|X/E_i|
-
|\Gamma(E_1,\ldots,E_m)|.
}
\]

它精确统计没有任何 state 实现的形式 task-label tuples。

因此 P017 的 candidate-superset 警告直接推广到 multi-task precision：形式乘积也会制造不存在的 joint states。

## 5. P023-S13-T02 —— 完整 pairwise shadows 仍不能决定 joint quotient

状态：`PROVED BY EXPLICIT COUNTEREXAMPLE`。

取 8 个 states 和三个 binary precision tasks。

系统 A 只实现四个 even-parity triples：

\[
000,\ 011,\ 101,\ 110,
\]

每个 tuple 各出现两次。

系统 B 则实现全部 8 个 binary triples，每个恰好一次。

两个系统都满足：

- 每个单独 partition 都有两个大小为 4 的 blocks；
- 每个 pairwise incidence graph 都是完整 `2 x 2` 二部图；
- 每个 pairwise intersection cell 的大小都为 2；
- 每个 pairwise directed repair factor 都等于 2；
- 因而所有 pairwise S12 distances 完全一致。

但是 joint quotient sizes 分别为

\[
\boxed{
|X/(E_1\cap E_2\cap E_3)|=4
\quad\text{（系统 A）},
}
\]

和

\[
\boxed{
|X/(E_1\cap E_2\cap E_3)|=8
\quad\text{（系统 B）}.
}
\]

因此即使给出全部 weighted pairwise incidence shadows，也不能决定 three-task precision。

这构成一个硬 no-go boundary：任何试图只从 pairwise distances 或 pairwise overlap counts 重建 joint precision 的理论都不充分。

## 6. Conditional extension sets

假设 tasks `E_1,...,E_m` 已经被保留，现在加入新 task `F`。

对一个 realized prefix tuple

\[
\tau=(B_1,\ldots,B_m)
\in\Gamma(E_1,\ldots,E_m),
\]

定义

\[
\boxed{
\operatorname{Ext}_F(\tau)
=
\{C\in X/F:
B_1\cap\cdots\cap B_m\cap C\ne\varnothing\}.
}
\]

它就是在完整已知 context 固定后仍然可能出现的 `F` labels 集合。

## 7. P023-S13-T03 —— 条件 repair factor 等于最大 hyperedge extension degree

状态：`PROVED`。

当前 context partition 为

\[
C=E_1\cap\cdots\cap E_m.
\]

加入 `F` 时，每个 context block 会按它实际碰到的不同 `F` blocks 继续分裂。因此精确最小 repair alphabet 为

\[
\boxed{
\rho(F\mid E_1,\ldots,E_m)
=
\max_{\tau}
|\operatorname{Ext}_F(\tau)|.
}
\]

这正是把 P023-S9 应用于当前 joint context partition。

当 `m=1` 时，它退化成 S12 二部 incidence graph 的最大左度数。

## 8. P023-S13-T04 —— 已知 context 越多，同一 task 的 repair 不会增加

状态：`PROVED`。

若 context `C'` 比 `C` 更细，则每个 `C'` block 都包含在一个旧 `C` block 中。因此 finer context block 内仍可能出现的 `F` labels 必然是原集合的子集。

于是

\[
\boxed{
\rho(F\mid C')
\le
\rho(F\mid C).
}
\]

这是纯有限 partition theorem：加入更精确的已知 context，只能降低或保持同一个新增 task 的最坏额外 repair alphabet。

这里不需要概率或 entropy。

## 9. Parity 例子：高阶 context 可以让一个 task 完全冗余

在 T02 的系统 A 中，第三个 bit 由前两个 bit 唯一确定，因为在 realized state set 上

\[
E_3=E_1\oplus E_2.
\]

因此

\[
\rho(E_3\mid E_1)=2,
\]

但

\[
\boxed{
\rho(E_3\mid E_1,E_2)=1.
}
\]

一旦保留两个 tasks，第三个 task 不再需要任何非平凡 repair state。

而系统 B 实现全部 8 个 triples，所以

\[
\rho(E_3\mid E_1,E_2)=2.
\]

两个系统的全部 pairwise 信息相同，条件 repair 结构却不同。

## 10. P023-S13-T05 —— 条件高阶 repair spectrum

对每个 realized context tuple `tau`，记

\[
e_\tau=|\operatorname{Ext}_F(\tau)|.
\]

定义

\[
\boxed{
\mathcal R_k(F\mid C)
=
\sum_\tau\binom{e_\tau}{k}.
}
\]

这就是 quotient projection

\[
X/(C\cap F)\to X/C
\]

的 S11 repair spectrum。

因此 hypergraph 不仅决定最坏 conditional repair factor，也决定新增 task 的完整 local repair-size distribution 与高阶 repair ambiguity。

## 11. 与 A4 的关系

A4 已经证明/强调 pairwise support shadows 可能丢失 higher-order witness identity。

S13 是它在 precision-partition 侧的对应版本：

\[
\boxed{
\text{pairwise block incidence}
\not\Rightarrow
\text{joint realized incidence}.
}
\]

这不是偶然类比；两者本质上都在研究一个高阶有限 relation 被投影成低阶 shadows 后丢失什么。

因此未来 A2/A4 bridge 中，只要声明任务能够查询 higher-order tuple，就必须把 realized higher-order incidence 当作一等对象。

## 12. 研究工具规则

面对三个以上 precision axes：

1. pairwise graphs 可以作为 diagnostics 与 geometry；
2. 除非有单独 theorem 证明 pairwise completeness，否则它们不是充分 joint state；
3. 构造 realized tuple hypergraph 或等价的紧凑表示；
4. 从当前 realized context 的 extension degrees 计算 conditional repair；
5. 然后才继续压缩 higher-order state。

这样可以防止 pairwise shadow 被静默升级成完整 future-compatible quotient。

## 13. 可执行规范

- `src/enterprise_math/precision_incidence_hypergraph.py`
- `tests/test_precision_incidence_hypergraph.py`

回归固定 even-parity 与 full-cube 反例，包括所有 weighted pairwise incidence shadows 完全相同而三阶 joint quotient 不同；同时验证 conditional-repair monotonicity 与 higher-order repair spectrum。

## 14. 基础边界

incidence hypergraph 是声明的有限 tasks 的精确数学表示，并不意味着所有可能物理 observable 都必须被同时保留。

它的基础作用更窄且可证伪：

> 当 future language 确实要求多个 task coordinates 联合可用时，安全 precision 必须尊重它们的**实际高阶 incidence**，而不能只保留 pairwise shadows。
