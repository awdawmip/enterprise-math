# P023 —— Higher-Order Precision Incidence，补充 13

状态：`PROVED RESEARCH NOTE + NEGATIVE BOUNDARY`  
归属：A2 / P023，并采用 A4 witness-identity 解释  
依赖：P023-S12 pairwise incidence geometry  
纪律：finite hypergraphs、joint partitions 与 marginal/projection loss 都属于成熟组合数学。项目新增价值是精确 conditional-repair 接口，以及“不能从 pairwise shadows 重建 joint precision”的显式 no-go 边界。

## 1. Pairwise incidence 不是完整 joint state

对同一个有限非空状态集 `X` 上的 precision relations

\[
E_1,\ldots,E_m,
\]

定义 **realized precision incidence hypergraph**：

\[
\boxed{
\Gamma(E_1,\ldots,E_m)
=
\{(B_1,\ldots,B_m):
B_i\in X/E_i,
\ \bigcap_i B_i\ne\varnothing\}.
}
\]

当 `m=2` 时，它正是 S12 的 bipartite incidence graph。

当 `m>=3` 时，`Gamma` 的 pairwise projections 可能丢失真正的 higher-order witness identity。

## 2. P023-S13-T01 —— Hyperedges 就是 exact joint precision classes

状态：`PROVED`。

common refinement

\[
E_1\cap\cdots\cap E_m
\]

的每个 block 恰好对应 `Gamma` 中一个 realized tuple。因此

\[
\boxed{
\left|X/\bigcap_iE_i\right|
=
|\Gamma(E_1,\ldots,E_m)|.
}
\]

### 证明

common refinement 的 block 正是每个 supplied partition 各取一个 block 后形成的非空交集；不同 realized block-label tuples 给出互不相交的 common-refinement blocks。∎

完整 formal candidate count

\[
\prod_i|X/E_i|
\]

只是 complete multipartite tuple space；真正 joint task states 是 realized hyperedges。

## 3. Conditional extension degree

假设 tasks

\[
E_1,\ldots,E_m
\]

已经被保留。其 joint precision 为

\[
C_m=\bigcap_{i=1}^mE_i.
\]

现在新增 task `F`。

对一个 realized prefix tuple `tau`（等价地，一个 `C_m` block），定义

\[
\operatorname{Ext}_F(\tau)
=
\{D\in X/F:\tau\text{ 可以与 }D\text{ 扩展成一个 realized }(m+1)\text{-tuple}\}.
\]

其 extension degree 为

\[
e_F(\tau)=|\operatorname{Ext}_F(\tau)|.
\]

## 4. P023-S13-T02 —— Conditional repair 等于最大 extension degree

状态：`PROVED`。

在 context `C_m` 已知以后，再加入 task `F` 所需的 exact minimum alphabet 是

\[
\boxed{
\rho(F\mid C_m)
:=
R(C_m\to C_m\cap F)
=
\max_{\tau\in\Gamma(E_1,\ldots,E_m)}e_F(\tau).
}
\]

### 证明

一个 retained prefix tuple 就是一个 coarse `C_m` block。加入 `F` 后，该 block 内的 target subblocks 恰好由能扩展该 tuple 的不同 `F` blocks 构成。P023-S9 已证明 minimum shared alphabet 等于所有 current blocks 中 target subblock 数量的最大值。∎

因此 repair 本质上是**相对于已经 retained 的 context 的条件量**。

## 5. P023-S13-T03 —— Conditional repair spectrum

状态：`PROVED`。

定义

\[
\boxed{
\mathcal R_k(F\mid C_m)
=
\sum_{\tau}
\binom{e_F(\tau)}k.
}
\]

它正是 quotient projection

\[
X/(C_m\cap F)\to X/C_m
\]

的 S11 spectrum。

因此它能恢复完整 conditional local repair alphabet-size distribution，而不仅是 worst-case maximum。

## 6. P023-S13-T04 —— 已知 context 越多，conditional repair 不会增加

状态：`PROVED`。

若

\[
C'\subseteq C
\]

是更细的 known context，则对任意 added task `F`，

\[
\boxed{
\rho(F\mid C')
\le
\rho(F\mid C).
}
\]

### 证明

每个 `C'` block 都包含在唯一 `C` block 中，因此它能接触的 `F` blocks 只能是 parent `C` block 所接触 `F` blocks 的子集。extension degree 不可能更大，取最大值得证。∎

所以得到一个纯 finite-partition 的 operational law：

\[
\boxed{
\text{more exact context}
\Longrightarrow
\text{no larger additional repair requirement}.
}
\]

这里不需要 probability 或 entropy。

## 7. P023-S13-T05 —— Pairwise weighted incidence 不能决定 triple precision

状态：`PROVED BY EXPLICIT COUNTEREXAMPLE`。

在同一个 eight-state set 上构造两个 triple-partition systems。

### System A —— duplicated even parity

realized triples 为

\[
000,011,101,110,
\]

每个由两个 raw states 实现。

### System B —— full binary cube

全部 8 个 triples

\[
000,001,010,011,100,101,110,111
\]

各实现一次。

两个系统中：

- 每个单独 binary partition 的 block sizes 都是 `4+4`；
- 任意 pair 都实现四种 pair-label combinations；
- 每个 pairwise intersection cell 的 cardinality 都精确等于 `2`。

所以**所有 pairwise weighted incidence tables 完全一致**。

但 joint precision 不同：

\[
\boxed{
|X/(E_1\cap E_2\cap E_3)|
=4
\quad\text{in System A},
}
\]

而

\[
\boxed{
|X/(E_1\cap E_2\cap E_3)|
=8
\quad\text{in System B}.
}
\]

因此 pairwise incidence graphs 与 pairwise intersection cardinalities 都不能决定 triple common refinement。

## 8. P023-S13-T06 —— Pairwise repair geometry 不能决定 conditional repair

状态：`PROVED BY THE SAME COUNTEREXAMPLE`。

两个系统中，对任意 `i!=j` 都有

\[
\boxed{
\rho(E_i,E_j)=2.
}
\]

因此所有 pairwise directed repair factors、integer depths 与 symmetric S12 distances 都相同。

但保留 `E_1,E_2` 后：

### System A

even parity 已精确决定第三个 label：

\[
\boxed{
\rho(E_3\mid E_1\cap E_2)=1.
}
\]

### System B

每个 `(E_1,E_2)` pair 下两个 third labels 都仍可能：

\[
\boxed{
\rho(E_3\mid E_1\cap E_2)=2.
}
\]

所以 pairwise precision geometry 不能恢复 higher-order conditional task cost。

这正是 A4 witness-identity boundary 的 precision 版本：pairwise shadows 可以保留全部 marginal counts，却仍丢失把多个 relations 绑在一起的 witness identity。

## 9. Hypergraph 视角下的 task redundancy

新增 task `F` 在已知 context `C` 下冗余，当且仅当

\[
\boxed{
\rho(F\mid C)=1.
}
\]

等价地，每个 realized `C` hyperedge 只能唯一延伸到一个 `F` block。

这比 pairwise label recovery 更强：一个 task 可以相对每个单独已有 task 都不冗余，但在多个 tasks 联合保留以后变成完全冗余；even-parity example 正是如此。

## 10. Sequential task addition

对有序 task family

\[
E_1,E_2,\ldots,E_m,
\]

令

\[
C_j=\bigcap_{i=1}^jE_i.
\]

第 `j+1` 步的 exact local repair factor 为

\[
\rho(E_{j+1}\mid C_j).
\]

final joint class count 满足 exact recurrence：

\[
|X/C_{j+1}|
=
\sum_{B\in X/C_j}
\#\{E_{j+1}\text{ blocks meeting }B\},
\]

从而得到界

\[
\boxed{
|X/C_m|
\le
|X/E_1|
\prod_{j=2}^m
\rho(E_j\mid C_{j-1}).
}
\]

这个乘法上界可以严格，因为每一步的 worst extension degree 不必发生在同一条 branch 上。

这直接连接到 P018 adaptive query/precision scheduling。

## 11. 研究工具规则

面对 `m>=3` 的 task family：

1. pairwise incidence graphs 仍然适合局部成本与上界；
2. 没有定理时，不得只凭 pairwise data 重建 joint state；
3. 应编译 realized tuple hypergraph，或保存一个能够精确恢复它的 sufficient representation；
4. added-task repair 必须相对于**当前 joint context**计算，不能只看 pairwise cost。

## 12. 可执行规格

- `src/enterprise_math/precision_incidence_hypergraph.py`
- `tests/test_precision_incidence_hypergraph.py`

回归固定 eight-state even-parity/full-cube counterexample：所有 weighted pairwise incidence tables 相同，但 triple class counts 不同，conditional repair 分别为 `1` 与 `2`。

## 13. Foundation 边界

S12 给出合法的 pairwise metric geometry；S13 证明这种 metric 不是 multi-task precision system 的 complete invariant。higher-order context 位于 realized hyperedges / witness identity 中；只要 task language 能查询这些信息，就必须另外表示。
