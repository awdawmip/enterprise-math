# 图精度状态的正合序列桥

状态：`RESEARCH BRIDGE / NONCANONICAL`  
目的：用一个标准图链复形，同时解释隐藏的 contact-cycle history 与守恒的 ledger-component totals。

## 1. 同一个 boundary operator 的两种精度角色

对有限定向图 `G`，令

`C_1(G;Z)=Z^E`

为整数 edge/event lattice，

`C_0(G;Z)=Z^V`

为整数 vertex/state-compartment lattice。带符号 incidence / boundary map 为：

`partial = B : C_1 -> C_0`。

普通图没有 2-cell，因此存在标准正合序列：

`0 -> H_1(G;Z) -> C_1 --B--> C_0 -> H_0(G;Z) -> 0`。

若图有 `c` 个 connected components，cycle rank 为 `beta=E-V+c`，则：

`H_1(G;Z) ~= Z^beta`，

`H_0(G;Z) ~= Z^c`。

这一条序列在 Enterprise Math 中同时出现为两种不同的 precision mechanism。

## 2. edge history 通过 vertex 被观测：H1 就是隐藏历史

设整数 edge history / impulse vector 为 `j in C_1`，粗 body/vertex change 为：

`b=Bj`。

两个 edge histories 产生相同粗状态，当且仅当它们的差属于：

`ker_Z B = H_1(G;Z)`。

所以第一同调就是 edge->vertex observation 下的 free hidden-history fiber。

这正是 contact-network 中 cycle allocation ambiguity 的底层：

- forest -> `H_1=0`，delivered edge history 能由 incidence image 唯一识别；
- 一个 cycle -> 一维 free circulation history；
- 一般图 -> `beta` 个独立整数 cycle-history directions。

若 future witness 为 `Cj`，真正需要 repair 的只是 `C(H_1)`；coboundary witness 会杀掉 H1，并 telescope 成 vertex state。

## 3. vertex ledger 模掉内部 transfer：H0 就是不变量账本

现在把存储量放在 **vertices / compartments** 上。沿一条 transfer edge 搬运 whole quantum，对 vertex ledger 的改变就是 incidence matrix 的一个 column，也就是：

`im_Z B`

中的元素。

因此，在 group-completed internal-transfer language 下，两个 vertex ledgers 等价，当且仅当它们的差属于 `im B`。

quotient 为：

`C_0 / im B = H_0(G;Z)`。

所以第零同调就是 additive policy-invariant ledger state：每个 connected transfer component 保留一个 total。

这正是 applied / queued / expired transfer theorem 的抽象形式：

- transfer graph connected -> 只剩 total content 作为独立线性 invariant；
- 有 `c` 个 transfer components -> 有 `c` 个独立 component totals。

## 4. kernel 与 cokernel 不能混为一谈

同一个 incidence map 因而回答两个方向完全相反的 precision question：

```text
edge/event state --B--> vertex/body state
    hidden ambiguity = ker B = H1

vertex/ledger state modulo edge transfers
    invariant quotient = coker B = H0
```

第一条问：

> 哪些 fine edge histories 在投影到 vertices 后变得不可见？

第二条问：

> 哪些 vertex-ledger quantities 在所有允许的内部 redistribution 下仍然保留？

同一张图、同一个 boundary operator，但它们处在 boundary map 的两侧。

## 5. 为什么普通 graph homology 本身解释不了项目里出现的 torsion

对普通有限图，`H_1(G;Z)` 与 `H_0(G;Z)` 都是 free abelian。

因此这条 graph-chain exact sequence 能解释：

- free cycle ambiguity；
- free component totals；

但它**不能**直接解释项目里后来出现的有限 torsion。

有限 quantization / reachability torsion 是在进一步组成整数 lattice operator 后产生的，例如：

`K = B^T D B`

的 weighted contact coupling，或

`L = B B^T`

的 graph Laplacian / potential representation。

这些二阶整数算子即使底层 graph homology torsion-free，也可以拥有 nontrivial finite cokernel / critical group。

所以架构上必须分开：

- **来自 chain complex 的 free topology** —— H1 hidden cycles、H0 component totals；
- **来自 induced lattice operator 的 integer quantization obstruction** —— Gram/Laplacian cokernel torsion、Smith factors、critical-group denominators。

这就是图特化版本的项目规则：

`kernel / free homology -> ambiguity / history`；

`induced integer cokernel / torsion -> reachability / representation obstruction`。

## 6. future policy family

如果未来可能在多个 transfer graphs 之间切换，那么任何单独的 `H_0(G_i)` 都不一定是最小 current additive state。

正确的联合 future observation 是把所有 future component-total maps 堆起来。

它的 hidden ledger difference lattice 为：

`intersection_i im B_i`，

也就是 joint component-sum observation matrix 的 kernel。

这也解释了为什么 pairwise connectivity partitions 的 simple meet 只能作为 additive ledger 的安全 combinatorial upper bound：incidence images 的交可以包含平衡的 multi-compartment directions，而这些方向无法用“两个 compartment 是否始终同类”这种 pairwise 关系完整描述。

## 7. 状态 / prior art

Graph homology、incidence exact sequence、Laplacian 与 critical group 都是标准 prior mathematics。本文件不宣称这条正合序列是新数学。项目价值在 architecture：它把此前两条看似独立的 precision mechanism 识别成同一个 boundary operator 的 kernel 与 cokernel 两侧，同时把 finite torsion 正确定位到 induced integer operator，而不是 graph homology 本身。
