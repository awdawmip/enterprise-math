# Causal Signature Coupling Defect —— 从独立签名失效生成耦合，而不是先验 interaction tensor

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE THEOREMS + EXECUTABLE REFERENCE`

## 1. 目标

独立 product 已有：

\[
\Sigma_{A\boxtimes B}=(\Sigma_A,\Sigma_B).
\]

本文件研究 product law 失败时，最少出现了什么新因果结构。

原则：不先引入 correlation、mutual information、interaction matrix、tensor 或 probability。先比较 joint future signature 与 marginal future signature 实际能区分什么。

## 2. Joint quotient 到 marginal quotient

令：

- `Q_A`、`Q_B`：只允许各自 subsystem future language 时的 signature classes；
- `Q_AB`：允许完整 joint future language 时的 signature classes。

joint class 忘掉 cross-future information 后，只剩一个边际 pair。令真实可达边际 pair 集为：

\[
R\subseteq Q_A\times Q_B.
\]

存在自然 forgetting map：

\[
\rho:Q_{AB}\to R.
\]

对每个 `r in R` 定义：

\[
\boxed{c(r)=|\rho^{-1}(r)|.}
\]

解释：边际看来完全相同的一个 coarse situation，在完整联合未来下实际有多少种不同 signature states。

## 3. CD-01 —— 两类耦合必须分开

定义 reachability defect：

\[
\boxed{M_{AB}=|Q_A||Q_B|-|R|.}
\]

它统计边际上分别存在、但在联合系统中不能同时出现的组合。

定义 signature split defect：

\[
\boxed{S_{AB}=|Q_{AB}|-|R|=\sum_{r\in R}(c(r)-1).}
\]

它统计已经可达的边际组合内部，被 joint future 进一步劈开的 signature classes。

因此当前有限定义中的严格独立判据是：

\[
\boxed{M_{AB}=0\quad\text{且}\quad S_{AB}=0.}
\]

二者不能相加后再遗忘类型。

### 反例：raw cardinality difference 会失真

设 `|Q_A|=|Q_B|=2`，理论 product 有 4 个 pair。

若仅 2 个 pair 可达，但每个可达 pair 内部又各 split 成 2 个 joint classes，则：

\[
|Q_{AB}|=4=|Q_A||Q_B|.
\]

所以 raw scalar `|Q_AB|-|Q_A||Q_B|=0`，但：

\[
\boxed{(M,S)=(2,2).}
\]

系统显然不是独立。该反例禁止把两种机制压成一个 cardinality scalar。

## 4. CD-02 —— coupling spectrum 就是 P011 collision spectrum

forgetting map `rho` 本身就是一次 many-to-one causal collapse。

定义：

\[
\boxed{C_k(A:B)=\sum_{r\in R}\binom{c(r)}k.}
\]

则：

\[
\boxed{C_k(A:B)=J_k(\rho).}
\]

因此：

- `C_1=|Q_AB|`；
- `C_2` 统计多少对 joint-signature classes 在 marginal future 下被认成同一个状态；
- `C_3` 同理；
- 完整 `C_k` 经 P011 已有整数二项反演精确恢复全部 `c(r)` 的 multiset。

所以 signature coupling 不需要再造新的统计谱：

\[
\boxed{\text{coupling spectrum}=\text{forget-cross-future collapse 的 P011 collision spectrum}.}
\]

## 5. CD-03 —— staged forgetting 的整数链式定律

任意有限 signature-forgetting 链：

\[
Q_2\xrightarrow{q_{21}}Q_1\xrightarrow{q_{10}}Q_0,
\]

令一阶 class-loss defect：

\[
D(q)=|\operatorname{dom}q|-|\operatorname{im}q|.
\]

若每一步的 domain 都正是上一层 reachable image，则：

\[
\boxed{D(q_{10}\circ q_{21})=D(q_{21})+D(q_{10}).}
\]

证明只是 telescoping cardinality：

\[
(|Q_2|-|Q_1|)+(|Q_1|-|Q_0|)=|Q_2|-|Q_0|.
\]

这给“分阶段忘掉 coupling information”一个纯整数账本。高阶 defect 不强行做假加法，而直接使用 P011 的 exact merge/collision increment 公式。

## 6. CD-04 —— pairwise zero 不推出 higher-order zero

三个二值 subsystem `A,B,C`，只允许偶 parity states：

\[
000,\ 011,\ 101,\ 110.
\]

任取两边，四种 pair combinations 都出现，因此所有 pairwise reachability defect 为 0；若 pair restriction 内也无额外 signature split，则所有 pairwise typed defects 都是 `(0,0)`。

但三体理论 product 有 8 个组合，实际只有 4 个：

\[
\boxed{(M_{ABC},S_{ABC})=(4,0).}
\]

所以这是不可由 pair coupling 表达的纯三体因果约束。

## 7. CD-05 —— causal independence complex

对一个 coherent subsystem family，收集所有满足 signature factorization 的非空 subsystem subsets：

\[
\mathcal I=\{S:\Sigma_S\text{ factorizes over its declared components}\}.
\]

若 restriction 语言一致，则 independence 向下封闭：一个更大的 subsystem 集若完全独立，其任意子集也独立。

因此 `I` 形成 abstract simplicial complex。

但 ontology 顺序是：

\[
\boxed{\text{signature factorization}\to\text{downward-closed independent subsets}\to\text{simplicial-complex shadow}.}
\]

不是先给一个 simplicial complex。

## 8. CD-06 —— irreducible coupling group = minimal nonface

若 `S` 自身不 factorize，但每个非空 proper subset 都 factorize，则称 `S` 为 irreducible causal coupling group。

在 independence complex 语言中，它恰好是 minimal nonface。

定义 coupling order：

\[
\boxed{\operatorname{ord}_{couple}=\min\{|S|:S\text{ 是 minimal factorization failure}\}.}
\]

于是：

- order 2 对应真正 pair coupling；
- order 3 可以在所有 pair interactions 都为零时出现；
- traditional interaction graph 只是保留 order-2 minimal nonfaces 的 shadow；
- hypergraph 是所有 minimal nonfaces 的传统组合表示。

## 9. 与 P011 / LEGO interaction 的关系

现在出现两层 interaction：

1. `lego_interaction_spectrum`：给定一个具体 response，哪些 unit 共存会产生不可约 extra effect；
2. 本文件：哪些 subsystem 的完整 future signature 无法从 proper-subsystem signatures 重建。

二者不是自动等价。当前应研究 bridge theorem：某个 local LEGO interaction 非零，在什么 operation/observation language 下必然制造 signature factorization failure；反向是否成立。

## 10. 线性 shadow，不提升为本体

若 integer-linear joint future language 包含所有 marginal probes，则 separate future-visible module 包含于 joint visible module。可以定义 rank shadow：

\[
\kappa_{free}=\operatorname{rank}(V_{joint})-\operatorname{rank}(V_{sep})\ge0.
\]

它只统计新增的 free independent distinctions。

但该 rank shadow不能检测所有有限 residue / reachability constraints，例如 parity 型高阶耦合。因此 linear rank 只能是 coupling defect 的特殊 shadow，不能重新升为 ontology。

## 11. 当前可执行资产

- `src/enterprise_math/causal_signature_coupling.py`
- `tests/test_causal_signature_coupling.py`
- `src/enterprise_math/causal_coupling_complex.py`
- `tests/test_causal_coupling_complex.py`

## 12. 下一步

1. 证明/反驳 LEGO local interaction 与 signature coupling minimal nonfaces 的双向 bridge；
2. 推导三系统及多系统 staged composition law；
3. 研究 dimension contraction 是否等于主动忘掉某类 coupling signature；
4. 研究 collision spectrum 是否能统一“不可逆坍缩”和“cross-future coupling”两种看似不同现象；
5. 暂不引入 tensor ontology；只有当 causal coupling 的组合规则逼出某种 multilinear shadow 时再吸收它。
