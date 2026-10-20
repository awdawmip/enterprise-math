# 精度状态诊断：五个不同的失败位置

状态：`RESEARCH BRIDGE / NONCANONICAL`  
范围：从当前 P023 / P024 / E001 / A4 压力测试中提炼的 Foundation-facing 综合  
目的：避免把数学上不同的问题，用错误的“加状态 / 提精度 / 换调度 / 选分支”方式修复。

## 1. 核心分类

一个粗粒度离散世界可以在五个不同位置失效：

1. **FIBER / 隐藏细节** —— 多个细状态落在同一个粗状态中；
2. **IMAGE / COKERNEL** —— 请求的目标不在当前整数像 / 坐标表示可达范围内；
3. **DOMAIN / action language** —— 代数更新公式存在，但 state-dependent action 或 action word 不合法；
4. **RELATION / 多值后继** —— 声明的 world law 本身允许多个后继；
5. **LEDGER / transfer allocation** —— 已量化或守恒内容分布在明确的 compartment 中，policy operation 在这些 compartment 之间搬运。

这五类是不同的失败位置，不是“缺精度”的五种叫法，也不能用同一种修复。

**声明的 future language** 是外层选择器：决定这些层中哪些差异未来还能被重新读出来，因此今天必须保留哪些细节。

## 2. 诊断顺序

当一个粗状态或转移显得“不够”时，依次问：

1. 后继是 functional 还是 relation-valued？
2. 所需 target 是否在声明映射的整数 image 中？
3. 同一个 coarse fiber 内还藏了哪些差异，future language 能读到哪些？
4. 哪些 named operations 是 partial，哪些 words 真正 causally legal？
5. 已量化 / 守恒内容分布在哪些 ledger compartments，当前和未来允许哪些 transfer？

不要通过偷偷改变别的数学层来“修复”当前层：

- 多存 history 不会消掉 cokernel 障碍；
- 提高 denominator 不会替 relation 选出一个唯一分支；
- scheduler 不是“多值 response 本来就确定”的证明；
- 静态可行的 batch target 不是合法 guarded word 的证明；
- 总量守恒也不代表 compartment allocation 未来不可见。

## 3. FIBER —— 同一个粗状态内部藏了什么？

### 3.1 有限 carry fiber

单 contact：

`N=A*j+delta`, `0<=delta<A`。

当前 delivered integer `j` 会丢掉 subquantum remainder。未来命名 raw additions 通过首次 carry 时间重新读出 `delta`。在 memoryless local carry/body-output future language 下，精确 contact 预测状态是 `(B j,delta)`，而不是完整 delivered allocation。

### 3.2 有限 memory fiber

TTL whole-queue age histogram：

`q=(q_0,...,q_(D-1))`。

当前 total `Q=sum q_a` 丢掉年龄分布。纯 aging 每增加一个未来 tick，就揭示一个更老 bucket。`h<=D-1` 时精确 total-observation key 为：

`(sum_(a=0)^(D-h-1) q_a, q_(D-h),...,q_(D-1))`。

到 horizon `D-1`，完整 histogram 可以由未来 total trace 通过整数差分恢复，不需要除法。

### 3.3 free-lattice / homology fiber

contact incidence `B` 下，相同 body delta 的 histories 相差：

`ker_Z B = H_1(G;Z)`。

additive witness `Cj` 能从 body state 恢复，当且仅当：

`ker_Z B subseteq ker_Z C`。

hidden witness group：

`C(ker B) ~= ker B/(ker B intersect ker C)`。

若标量 witness 是整数 coboundary `c=B^T phi`，它会 telescope 成 body observable，不需要 cycle repair。

### 3.4 存在 fiber 不等于必须保留全部 hidden state

一个数学 fiber 可以真实存在，但 declared future language 也可能完全杀掉它。正确 repair 是 fiber 中真正 future-visible 的 quotient，而不是完整细状态。

## 4. IMAGE / COKERNEL —— 什么目标不可达或不可整数表示？

kernel 为 0 并不保证所有整数 target 都可达。

当前 contact 研究中已经出现：

- witness 唯一但仍有有限同余 cokernel 的 path/contact Gram；
- graph critical-group class 强迫 nontrivial potential/cycle representation denominator；
- two-sided action language 中永久 numerical-semigroup gap 与临时 finite-horizon packing underresolution 的分离。

critical class 阶为 `s` 时，同一个 physical delta 重复 `m` 次后的最小表示 denominator 为：

`s/gcd(s,m)`。

这是 representation/reachability 障碍，不是 hidden history。多存 history 修不好它。

## 5. DOMAIN —— 哪些操作实际上合法？

对 guarded contact score state `r`，单位动作 `i` 做 `K e_i` 更新，仅当：

`r_i<0`

时合法。

literal word 有 exact partial-affine normal form `(Delta,H)`；prefix requirement `H` 是 operation 本身的一部分。

因此：

- 代数上交换的 total updates，作为 guarded partial maps 可以不交换；
- material 层可以精确量化出 batch vector `J`，但可能根本不存在实现全部 `J` 的 guarded sequential word；
- Z-coupled、off-diagonal 非正时，只要 completion 存在，enabled-greedy completion 就结构性安全；
- definedness 自身可以在 present observation 常值时生成 predictive precision。

这是 action-domain 问题，不是 target-cokernel 问题。

## 6. RELATION —— 当世界本来就没有唯一下一状态

branching response 或 guarded terminal family 可以真正 relation-valued。

有限 relation `R` 与 target observation `O` 的正确一跳 signature：

`Sigma_(R,O)(x)={O(y):(x,y) in R}`。

empty set 就是明确的 undefined/no-target。

raw branching 与 observable nondeterminism 是不同问题。某个 multivalued raw relation 在某个 future language 下可以只有 singleton observed target set，但这不会把底层 world update 自动变成 functional。

单步 observable-deterministic 也不自动保证 composition-safe。后续 relation 可以重新读取被当前 observation 隐掉的 intermediate branch identity。安全 coarse composition 要求后续 powerset-valued signature 自身能通过当前 observation quotient 因子化。

reachable-support 语义下，A4 relation word 可以编译成 `P(X)` 上的 deterministic map；但这会丢 path multiplicity、branch identity、单独死亡的 branch。未来若读这些，就必须回到更丰富的 A4 witness 层。

## 7. LEDGER —— 守恒 / 已量化内容分配在哪里？

### 7.1 固定 transfer graph

把 ledger compartment 当顶点，允许的 whole-quantum transfer `u->v` 对 ledger 的改变量是：

`-d e_u + d e_v`。

redistribution lattice 就是 transfer graph 的整数 incidence image。标量线性 readout 对所有允许 transfer invariant，当且仅当它的权重在每个 connected component 上为常数。

因此固定一个 transfer graph 时，每个 connected component 恰好贡献一个独立线性 invariant，canonical coordinate 就是 component total。

对 `(P,Q,X)`：

- 只有 application `Q->P`：保留 `P+Q` 与 `X`；
- 只有 expiry `Q->X`：保留 `P` 与 `Q+X`；
- 两类 transfer 都允许：三格连通，只剩 `P+Q+X` 作为独立 fully policy-invariant 线性坐标。

### 7.2 多个未来 transfer graph：正确的 additive 母对象

第一版 WIP 曾把“所有未来 connectivity partitions 的 common refinement”当成最小 additive current state。这个命题**一般不成立**。

正确对象是 joint component-sum matrix。

对每个可能的未来 graph `G_i`，把每个 connected component `C` 的整数 indicator row `1_C` 堆起来：

`S : Z^V -> Z^m`。

两个 current additive ledgers 对所有声明的未来 component-total observations 完全不可区分，当且仅当：

`S(ell-ell')=0`。

等价地：

`ker_Z S = intersection_i im_Z D_i`，

其中 `D_i` 是对应 transfer graph 的 incidence matrix。

因此：

- hidden free rank = `|V|-rank_Q(S)`；
- 与完整 future signature 拥有同一 equality kernel 的最少独立标量线性坐标数 = `rank_Q(S)`；
- 全部 future component totals 可以包含线性冗余。

### 7.3 crossing-partition 反例

4 个 compartments，两种未来 partition：

`01|23`,
`02|13`。

pairwise connectivity-equivalence meet 是 4 个 singleton。但：

`d=(1,-1,-1,1)`

在两种 partition 的每个 component 上总和都为 0，所以 `S d=0`。

因此“保存 4 个 singleton totals”安全但过精细；joint observation rank 只有 3。

connectivity meet 仍然有两个精确用途：

- 判断两个**单个 unit placement** 是否在所有未来 graph 中 pairwise indistinguishable；
- 提供一个安全的 combinatorial block-total upper bound。

它不是 additive minimality theorem。

### 7.4 future totals 已 injective，仍可能有整数坐标 torsion

即使 `ker S=0`，还可能有第二个问题。

4 个 compartments 的三种 pair partition：

`01|23`, `02|13`, `03|12`。

联合 future component totals 已唯一确定完整 ledger，`rank_Q(S)=4`、hidden rank 0；但 component-indicator row lattice 的 saturation index 是 2。

所以 hidden-state ambiguity 已消失，但 future-total 坐标系仍不是 unimodular。

这是 LEDGER 内部再次出现的 IMAGE/COKERNEL 型坐标障碍：五类是“问题进入架构的位置”，并不意味着一个层内部不能再同时出现 kernel 与 torsion。

### 7.5 今天的 component totals 是否能扛住未来 policy change？

current graph 的 component totals 能重建所有 future component totals，当且仅当未来没有 graph 会把某个 current connected component 拆开。

未来合并是安全的；未来拆分会重新激活今天已经删除的细节。

这个 current-safety 判据，与“多个未来 policy 联合后的全局最小 additive signature”是两个不同问题。

## 8. 防混淆映射

| 症状 | 首先诊断为 | 不要这样“修” |
|---|---|---|
| 同 delivered integer、下一 carry 时间不同 | FIBER | 只提 denominator |
| 同 body delta、cycle damage history 不同 | FIBER | 宣称 target 不可达 |
| rational witness 唯一、integer target 无解 | IMAGE/COKERNEL | 多存 history |
| batch target 精确、没有合法 guarded word | DOMAIN | 把 batch feasibility 当 causal realizability |
| 多个 admissible terminal outcome | RELATION | 偷偷选 representative |
| 同 quantized total 分布在 applied/queued/expired | LEDGER | 不分析 transfer/future 就删 compartment identity |
| queue total 相同、TTL age histogram 不同 | FIBER + future DOMAIN/LEDGER | 假设 current total 永远够用 |
| critical denominator >1 | IMAGE/COKERNEL | 把它叫 hidden cycle history |
| raw relation 分叉、observed target set singleton | RELATION + future observation | 宣称底层 law 已 functional |
| 多个未来 transfer policies | LEDGER + joint linear observation | 把 connectivity-meet block totals 当 additive minimum |

## 9. 架构规则

precision-first state compiler 至少要分开这些问题：

```text
STATE/FIBER
    current coarse fiber 内还藏什么？
    哪些差异会被 future language 重新激活？

TARGET/IMAGE
    target 是否可达 / 可整数表示？
    是永久 arithmetic obstruction，还是 finite-horizon underresolution？

ACTION/DOMAIN
    哪些 action 当前定义？
    哪些 action words 真正 causally realizable？

SUCCESSOR/RELATION
    next-state law 是 functional 还是 relation-valued？
    哪些 branch difference 在 declared observation 下仍可见？

LEDGER/TRANSFER
    已量化 / 守恒内容分配在哪里？
    当前与未来允许哪些 transfer？
    joint future observation kernel 是什么？
```

统一外层规则：

> **只保留 declared future operation / observation language 能重新激活的差异；绝不能通过偷偷改变另一个数学层来“修复”当前层的问题。**

## 10. 证据状态

本文件是 noncanonical synthesis。它消费 finite material impulse lineage、guarded P024、contact homology/critical precision、causal material queue/history、A4/P023 relation-observable、TTL age/loss，以及修正后的 material-ledger future-policy lattice 等 canonical + Draft evidence。

所使用的 quotient/kernel/cokernel、finite relation、subset construction、numerical semigroup、graph homology/cohomology、critical group、queue、graph incidence 与 integer lattice 都是标准 prior mathematics。项目价值在于 architecture separation：这些结构出现在不同失败位置，构造 finite-precision world state 时不能混为一谈。
