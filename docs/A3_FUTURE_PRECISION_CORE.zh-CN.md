# A3 Future Precision Core —— Hidden Relation、Guard Quotient 与 Task-Derived Exact Precision

状态：`ACTIVE RESEARCH ORIENTATION / THEOREMS REMAIN WIP UNTIL CLEAN INTEGRATION`

## 1. 目的

本文件是 `research/core/relation-quotient` 的当前恢复入口之一。

历史 `P019_MINIMUM_PRECISION_LATTICE_GEOMETRY_*` 与 A3 supplements 继续保留证明、反例和发现 provenance；但 A3 future-precision 主线不应再通过顺序阅读全部历史文档恢复。

当前最小工作骨架是：

\[
\boxed{
(m,c,Z),\quad A,\quad K_A,\quad W,\quad L_A=W(K_A),\quad \mathcal Q_A=\mathbb Z^r/L_A.
}
\]

其中：

- `(m,c,Z)`：capacity-weighted relation state；
- `A`：partition aggregation；
- `K_A=ker_Z A`：被 coarse state 隐藏的 relation/motion lattice；
- `W`：future guard / linear predicate map；
- `L_A=W(K_A)`：当前 future language 真正能读取的 hidden guard variation；
- `Q_A=Z^r/L_A`：coarse predicate-information quotient。

## 2. A3 relation state

weighted relation：

\[
Z_{ij}=m_jc_i-m_ic_j,
\qquad Z=cm^T-mc^T.
\]

partition quotient：

\[
(m,c,Z)\mapsto(Am,Ac,AZA^T).
\]

state fiber 与 coarse-invisible additive motion 是同一个：

\[
\boxed{K_A=\ker_{\mathbb Z}A.}
\]

relation dimension loss：

\[
\operatorname{rank}K_A=k-\ell.
\]

## 3. Future language 只看 kernel 的像

给 `r` 个 integer linear guards，矩阵：

\[
W:\mathbb Z^k\to\mathbb Z^r.
\]

同一个 coarse fiber 中 score 的全部 hidden variation：

\[
\boxed{L_A=W(K_A).}
\]

因此 future predicate precision 的关键复杂度参数不是 fine dimension 或 guard count 本身，而是：

\[
\boxed{d=\operatorname{rank}L_A.}
\]

基本端点：

- `d=0`：guards 全部 descend；
- `d=1`：arithmetic line，已有 exact switch / residue / minimum precision solver；
- `d=2`：integer halfplane lattice，已有 exact reachability / hidden-subgroup / minimum precision solver；
- fixed `d`：reduce 到 `d` integer variables，general feasibility 可调用成熟 fixed-dimension ILP。

## 4. Guard quotient module

coarse predicate state 的 tree/representative-independent object：

\[
\boxed{\mathcal Q_A=\mathbb Z^r/L_A.}
\]

若 hidden rank为 `d`，则：

\[
\mathcal Q_A
\cong
\mathbb Z^{r-d}
\oplus
\text{finite torsion}.
\]

finite torsion由 hidden generator matrix 的 Smith invariant factors 给出。

refinement `R≼P` 时：

\[
L_R\subseteq L_P
\]

并有 exact sequence：

\[
\boxed{
0\to L_P/L_R
\to\mathcal Q_R
\to\mathcal Q_P
\to0.
}
\]

所以 refinement 新暴露的 predicate detail 恰是 `L_P/L_R`。

## 5. Canonical hidden-subgroup refinement

取 parent hidden lattice 的 exact basis：

\[
H:\mathbb Z^d\cong L_P.
\]

在每个 parent block 内给 fine coordinate 分配 hidden label：

\[
W_i-W_a=H\lambda_i,
\qquad \lambda_i\in\mathbb Z^d.
\]

任取 subgroup：

\[
M\le\mathbb Z^d.
\]

按：

\[
\lambda_i-\lambda_j\in M
\]

分组，得到 canonical coset partition `R_M`。

核心 theorem：

> `R_M` 是唯一最粗使 child hidden image contained in `H(M)` 的 refinement；若某 arbitrary refinement 的 exact child image 本来就是 `H(M)`，则 `R_M` 也恰有该 image，并且不更细。

因此 minimum precision 搜索可从 raw set partitions 改为 finite label-generated hidden subgroup family。

## 6. Reachable behavior，而不是 syntactic branches

固定 coarse fiber `y`，reachable branch patterns：

\[
R_y.
\]

固定 declared coarse effect map `E`。

branch identity 可安全擦除当且仅当：

\[
\boxed{E|_{R_y}\text{ 为常值}.}
\]

定义 state-local effect ambiguity：

\[
\boxed{a_E(y)=|E(R_y)|.}
\]

- `a_E=1`：当前 state 对该 effect language exact；
- `a_E>1`：当前 partition不足。

不可达 branch 的不同代码/历史不制造 precision obligation。

## 7. Rank-one / rank-two complete state-local solvers

### rank one

hidden image：

\[
\mathbb Z h.
\]

fine coordinates 有 hidden integer labels `lambda_i`。

modulus `q` 的 canonical refinement 按：

\[
\lambda_i\bmod q
\]

分组。

有限 visibility bound后所有 labels 完全分离，因此只需有限枚举 canonical modulus partitions。

已证明 solver 给出**全部 partition refinements 中**的 minimum task-exact relation-rank cost与完整 minimum frontier。

minimum frontier 可以是 antichain，不必唯一。

### rank two

fine coordinates 有 labels：

\[
\lambda_i\in\mathbb Z^2.
\]

所有 partition-realizable hidden subgroups正是 finite label differences 的 distinct subgroup closures。

对每个 subgroup构造 canonical coset partition，再用 rank0/1/2 exact reachability checker。

4-coordinate Bell-partition oracle同时验证：

- subgroup search space 完整；
- minimum frontier完整。

## 8. Task precision 可以严格低于 predicate visibility

已经有 rank-one 与 rank-two exact examples：

### rank one

\[
\boxed{\Delta d_{task}=1<2=\Delta d_{guard-visible}.}
\]

### rank two

\[
\boxed{\Delta d_{task}=1<3=\Delta d_{guard-visible}.}
\]

原因不是近似，而是 refinement 只需让 effect-distinguishing branch 不可达；不必把所有 predicate scores 完全显式化。

## 9. State-local、finite workload、global all-state 三层

必须区分：

\[
\boxed{
\text{state-local minimum}
\neq
\text{finite-workload minimum}
\neq
\text{global all-state minimum}.
}

finite workload 要求同一个 refinement 对多个 base-score cosets 都 safe。

已有 strict examples：多个 state 各自最低 cost `1`，共同 coarse program 需要 cost `2`。

对 finite scalar band `|w^Tc+b|<=R`，whole-domain theorem更强：若该 task在 `Z^k` 上 nonconstant，则 global exact partition **必须让 scalar observable itself descend**。state-local residue shortcut不能替代 global visibility。

## 10. Hidden finite-band theorem

scalar hidden fiber：

\[
z_0+q\mathbb Z.
\]

定义 least absolute residue：

\[
\rho_q(z_0)=\min_{t\in Z}|z_0+qt|.
\]

对 finite band：

\[
|z|\le R,
\]

若 `q>0`：

- `rho_q(z_0)>R`：整个 fiber exact False；
- `rho_q(z_0)<=R`：同一 fiber 同时 True/False；
- hidden nonzero fiber 不可能 uniformly True。

所以 finite residue certificate 可以在 relation仍 hidden 时安全证明“不支持”。

A3→A4 radius support是该 theorem 的 downstream specialization。

## 11. Two-guard typed quotient state

若两个 guards 的 hidden image rank为 1：

\[
L=Zh,
\qquad h=d p,\ p\text{ primitive},
\]

则：

\[
\boxed{
\mathbb Z^2/L
\cong
\mathbb Z\oplus\mathbb Z/d\mathbb Z.
}
\]

用 unimodular transform 可显式得到：

- one free integer `phi`；
- one torsion residue `tau mod d`。

二者是 hidden score coset 的 complete invariant，并可直接由 coarse block totals 符号计算。

support guards `R-z,R+z` 中 free invariant固定为 `±2R`，真正变化只剩有限 hidden residue。

## 12. Typed precision certificate，不做单标量

当前 partition precision至少包含：

### relation state

- relation rank；
- relation quantum；
- relation translation period。

### future predicate

- hidden guard rank；
- guard quotient free rank；
- Smith invariant factors；
- torsion factors/order。

refinement 中：

\[
0\le d_P-d_R\le\Delta d_{relation}.
\]

但可以：

\[
d_P=d_R
\]

同时增加 finite torsion detail，例如 rank-one mod-2 refinement。

所以：

\[
\boxed{
\text{precision 不能只用 dimension/rank 一个数表示}.}
\]

## 13. Branch ownership

A3 owner branch：

`research/core/relation-quotient`。

一般 future-compatible / behavioral quotient 母理论：A2/P023。

A4 support correspondence 与 A3 仅通过已证明 bridge组合。

P022 持有真实 lattice/ball/geometry 结果。

跨路线一般 theorem、strict generalization、bridge、negative boundary必须进入 Research Relay #82；不要通过重复 whole-branch merge同步。

## 14. 当前实现路由

主要模块：

- `weighted_relation_field.py`；
- `relation_precision_profile.py`；
- `linear_relation_quotient.py`；
- `linear_observation_quotient.py`；
- `piecewise_relation_quotient.py`；
- `guard_image_lattice.py`；
- `rank_two_guard_reachability.py`；
- `guard_pattern_complexity.py`；
- `guard_branch_erasure.py`；
- `rank_one_guard_modulus.py`；
- `rank_one_task_precision.py`；
- `rank_two_guard_refinement.py`；
- `rank_two_task_precision.py`；
- `guard_workload_precision.py`；
- `hidden_band_predicate.py`；
- `two_guard_coset.py`；
- `guard_quotient_module.py`；
- `future_precision_certificate.py`。

完整 repo CI 尚未在当前执行环境运行；本分支有 executable unit tests、Bell-partition oracles 与独立整数压力检查，但 promotion 仍需 clean integration branch + canonical CI。

## 15. 当前唯一主问题

下一阶段不再扩散新 primitive。主问题是：

\[
\boxed{
\text{给定 future operation / predicate / effect language，
如何从 }(m,c,Z)\text{ 自动生成最小 exact typed precision state？}
}
\]

近期子问题按优先级：

1. global symbolic multi-guard coarse program：在 quotient module `Q_A` 上直接编译 branch effects；
2. finite-workload frontier 的 dominance/antichain pruning；
3. general hidden rank `d` 使用 production HNF/SNF + fixed-dimension ILP，而不是 A3 自造 optimizer；
4. A3→A4 support 与 P021 witness future language 的真实压力测试；
5. 与 P018/P023 建 theorem-level bridge，让 adaptive precision 直接消费 A3 typed certificates。
