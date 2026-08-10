# 精度状态诊断：Fiber、Image、Domain、Relation 与 Ledger

状态：`RESEARCH BRIDGE / NONCANONICAL`  
范围：从当前 P023 / P024 / E001 / A4 压力测试中提炼的 Foundation-facing 诊断框架  
目的：避免把数学上不同的失败，用错误的“加状态 / 提精度 / 换调度 / 选分支”方式修复。

## 1. 为什么需要这套诊断

近期 precision-first 研究反复出现一种表面相似的现象：粗接口下两个状态相同，但未来行为不同；或者一个整数目标无法实现；或者动作顺序改变结果；或者下一状态本身就是多值。

如果把这些都叫成“缺精度”“隐藏历史”“underresolved”或“非确定性”，会把不同数学问题混在一起。

目前已经稳定出现五个不同的失败位置：

1. **FIBER / 隐藏细节** —— 多个细状态落入同一个粗状态；
2. **IMAGE / COKERNEL 障碍** —— 请求的目标根本不在整数像 / 当前表示的可达集合中；
3. **DOMAIN / ACTION-LANGUAGE 缺陷** —— 更新公式存在，但动作带状态依赖的合法域，动作词顺序可能改变可执行性；
4. **RELATION / 多值后继** —— 世界 law 本身允许多个后继或多个 terminal outcome；
5. **LEDGER / TRANSFER 分配** —— 已量化或守恒的量分布在不同账本 compartment 中，policy move 只是在这些 compartment 之间转移。

这五类不是同一个现象的五种叫法，它们需要不同的修复。

**声明的 future language** 不属于第六类失败。它是外层选择器：决定每一类中的哪些差异未来还能被动作 / 观测重新读出来，因此哪些差异今天必须保留。

---

## 2. 诊断顺序

当一个粗状态或世界转移显得“不够”时，按以下顺序问。

### Q1 —— 声明的后继是不是单值？

如果不是，首先面对的是 **relation**，不是“某个尚未发现的确定性隐藏状态”。

不要通过最低编号 contact、最小范数、对称代表、优化器或 scheduler 偷偷选一个分支。除非未来可观测等价性证明所有分支都可交换，否则 selector 本身就是新增 world law。

### Q2 —— 所需目标是否在声明更新 / 表示映射的整数像中？

如果不在，这是 **image / cokernel 障碍**。

多存 history 不会把不可达目标变成可达。正确修复可能是：改目标、扩大操作语言、采用兼容的 refinement denominator，或者明确返回 UNDERRESOLVED / IMPOSSIBLE。

### Q3 —— 在可达且单值的粗行为下，是否仍有多个细状态落到同一个粗状态？

如果有，检查 **fiber**。

不要默认保存全部细状态。只保留 declared future language 真正读取的 repair。隐藏 fiber 可能是有限 remainder、有限 memory、free lattice、cycle history 等不同结构。

### Q4 —— 未来操作是否 partial / state-dependent？

如果是，**action domain / definedness** 必须进入 future signature。

代数上可交换的 total updates，不一定作为 guarded partial operations 可交换；一个静态可行的最终目标，也可能根本没有合法 causal action word。

### Q5 —— 已量化 / 守恒量是否分布在多个 compartment？

如果是，明确 **ledger 与 allowed transfer graph**。

applied、queued、expired、recovered、delayed、damaged 等 compartment 不能默认互换。先计算 transfer difference lattice / component totals，再决定能不能删除 compartment identity。

---

## 3. A 层 —— FIBER / 隐藏细节

粗映射 `q:X->Y` 产生 fiber：

`q^{-1}(y)`。

真正要问的不是“fiber 有多大”，而是：

> 同一个 fiber 内的哪些差异，未来动作 / 观测仍然能读取？

### 3.1 contact-local subquantum remainder

单个 contact：

`N=A*j+delta`, `0<=delta<A`。

当前 delivered impulse `j` 会丢掉有限 remainder fiber。命名 contact 的未来 raw additions 可以通过首次 carry 时间重新读出 `delta`。当所有 contact 都可独立寻址时，memoryless contact 的精确预测状态是 `(B j, delta)`，而不是完整 delivered allocation `j`。

这是 **有限 fiber / carry repair**。

### 3.2 TTL queue 年龄 histogram

年龄 bucket：

`q=(q_0,...,q_(D-1))`。

当前 total `Q=sum q_a` 丢掉年龄分布。TTL aging 每增加一个未来 tick，就把一个最老 bucket 从聚合池里揭示出来。

`h<=D-1` 时精确 key：

`(sum_(a=0)^(D-h-1) q_a, q_(D-h),...,q_(D-1))`。

到 horizon `D-1`，未来 total trace 通过整数差分就能完整恢复 age histogram，不需要除法。

这是 **有限 memory / 被动可观测 fiber**。

### 3.3 contact cycle history

对 incidence `B`，相同 body delta 的 contact histories 相差：

`ker_Z B = H_1(G;Z)`。

线性 witness `Cj` 能从 body state 恢复，当且仅当：

`ker_Z B subseteq ker_Z C`。

精确 hidden witness group：

`C(ker B) ~= ker B / (ker B intersect ker C)`。

这是 **free lattice / homology fiber**。

### 3.4 Fiber repair 是任务相对的

数学上存在 fiber，不等于必须保存 repair。

例如：

- 纯 local carry + body-output future language 看不到 cycle allocation，因此即使图有环，`(B j,delta)` 仍然精确；
- 标量 cycle witness 若是整数 coboundary `c=B^T phi`，会 telescope 成 body observable，不需要 cycle repair；
- 模 `M` 的 future observation 可以把无限 scalar hidden subgroup `gZ` 压成 `M/gcd(M,g)` 个有限 phase。

因此：

**存在 hidden fiber != 必须保留全部 hidden state。**

---

## 4. B 层 —— IMAGE / COKERNEL 障碍

一个映射可以完全没有 hidden ambiguity，但仍然不是每个整数目标都能到达。

这不是 fiber 问题。

### 4.1 path/contact target 同余障碍

uniform path contact Gram 中：

`ker K=0`

但

`coker(K) ~= Z/nZ`。

所以 witness 可以唯一，但整数 target 仍可能不可达。nullity 为 0 不会自动消掉 torsion。

### 4.2 graph critical-group denominator

对 body delta `b=Bj` 与 Laplacian `L=B B^T`，若把整数 edge history 精确分解成 potential/cut + cycle，有时必须引入 denominator。

最小 denominator 就是 `[b]` 在

`im_Z(B) / im_Z(L)`

中的阶。

对 cycle `C_n` 的单 edge impulse，最小 denominator 精确等于 `n`。

这是 **表示 / 可达性障碍**，不是隐藏 history。

### 4.3 重复相位

critical class 阶为 `s` 时，同一个 physical delta 重复 `m` 次后的最小 denominator：

`s_m=s/gcd(s,m)`。

普通整数 `m` 下可以非单调，但沿真正 divisibility refinement 单调下降。

### 4.4 诊断规则

如果失败发生在 image / cokernel：

- 多存 history 没用；
- 换 relation branch 只有在改变 target 时才可能有用；
- 提 denominator 只有与 torsion/order 兼容的 refinement 才能修复表示障碍；
- 必须区分永久 arithmetic impossibility 与有限 horizon / packing underresolution。

---

## 5. C 层 —— DOMAIN / action-language 缺陷

更新公式可以代数上完全存在，但世界操作可能只在部分状态上合法。

### 5.1 guarded contact actions

contact score `r`、coupling `K`，单位动作 `i`：

`r -> r + K e_i`

仅当

`r_i<0`

时合法。

任意 action word 可压成 exact partial affine profile `(Delta,H)`，其中 `H` 记录各 contact 的最大 prefix requirement。

因此：

`代数更新相等 != causal operation 相等`。

### 5.2 batched target 与 causal realizability

material 层可以精确量化出 delivered vector `J`。batched network application 永远是 `KJ` 的加法更新。

guarded sequential world 还必须问：是否存在 count vector 为 `J` 的合法单位动作词？

q=1 的正耦合三叶 star 中，batch `J=(1,1,1)` 完全合法，但不存在能消费全部三单位的 guarded sequential word。

这是 **domain / word-language failure**，不是 arithmetic image failure。

### 5.3 Z-coupled greedy 结构

若所有 off-diagonal coupling 非正，则任何当前 enabled 的 remaining action 都可以被交换到一个合法 completion 的词首。因此：只要存在 completion，任意 enabled-greedy scheduler 都不会卡死。

这是一条 domain theorem；它不意味着完整 guarded operation algebra 全局交换。

### 5.4 partial-action precision genesis

definedness 自身可以在当前 observation 完全常值时生成 predictive precision。因此 current precision 必须相对于 future action domains 计算，而不能只看 present value observation。

---

## 6. D 层 —— RELATION / 多值后继

有时并不存在“等待被找到的唯一细后继”。世界 law 本身就是 relation。

### 6.1 static response relation

branching contact network 可以存在多个互不可比的 minimum-total responses。保留完整 first feasible layer 与“挑一个代表”是不同操作。

### 6.2 scheduler terminal relation

prequantized target `J` 在 guarded consume-until-stuck 语义下，可能有多个 terminal applied-count vector `n`。

于是 exact queue `Q'=J-n` 只要 terminal count 不唯一，就天然是 relation-valued。

### 6.3 relation 的 observable determinism

有限 relation `R` 与 target observation `O`：

`Sigma_(R,O)(x)={O(y):(x,y) in R}`。

raw relation branching 可以被 declared observation 隐掉，但这不会把底层 A4 relation 自动变成 deterministic state update。

source quotient 安全，当且仅当 `Sigma_(R,O)` 在 quotient fiber 上完全相同，包括 empty/no-target outcome。

### 6.4 composition 警告

单步 observable-deterministic 不自动保证组合后仍 deterministic。后续 relation 可能重新读取被当前 observation 隐掉的 intermediate branch identity。

安全 coarse composition 要求后续 powerset-valued signature 自身能通过当前 observation quotient 因子化。

### 6.5 powerset compiler 边界

A4 support dynamics 可以编译成 `P(X)` 上的 deterministic map，用于 reachable-support 语义。但它会丢 witness multiplicity、path identity、单独死亡的 branch。未来若读取这些，powerset support 就过粗。

---

## 7. E 层 —— LEDGER / transfer 分配

一个守恒或已量化总量可以完全已知，但它分配在哪些 compartment 仍可能 future-relevant。

### 7.1 applied / queued / expired

whole-contact material quanta：

`H=P+Q+X`。

policy move：

- application：`Q->P`；
- expiry：`Q->X`。

标量 readout `uP+vQ+wX`：

- scheduler/application invariant iff `u=v`；
- expiry invariant iff `v=w`；
- 两者都 invariant iff `u=v=w`。

这解释了 applied / live committed / ever-quantized history 的确定性为什么不同。

### 7.2 一般 transfer graph

任意 compartments 与 allowed transfer edges 下，标量线性 observable 对所有允许 transfer invariant，当且仅当权重在 transfer graph 每个 connected component 上为常数。

因此：

`独立线性 transfer invariants 的 rank = transfer connected components 数量`。

canonical coordinate 就是各 component total。

### 7.3 future policy meet

如果未来 transfer graph 可能改变，仅按今天 graph 的 component total 压缩不一定安全。

两个 compartment 只有在**每一种声明的未来 transfer graph 中都属于同一个 connected component**，今天才可以安全合并。

最小 current additive state 是所有未来 connectivity partitions 的 common refinement / meet 各 block 的总量。

未来合并是安全的；未来拆分会重新激活细节，因此要求今天就保留。

---

## 8. 跨层防混淆表

| 症状 | 正确层 | 应避免的错误修复 |
|---|---|---|
| 同 coarse state，但下一次 carry 时间不同 | FIBER | 只提 denominator 却不保留 future-visible remainder |
| 同 body delta，但 cycle damage history 不同 | FIBER | 宣称 target 不可达 |
| Q 上 witness 唯一，但整数 target 无解 | IMAGE/COKERNEL | 多存 history |
| batch vector 精确，但没有合法 guarded word | DOMAIN | 把 batch feasibility 当 causal realizability |
| 多个 admissible terminal outcome | RELATION | 偷偷选 scheduler / representative |
| 同一 quantized total 分布在 applied/queued/expired | LEDGER | 不检查 transfer/future invariance 就合并 compartment |
| TTL queue 当前总量相同但年龄不同 | FIBER + future DOMAIN/LEDGER | 假设当前 scalar total 永远够用 |
| critical-group denominator > 1 | IMAGE/COKERNEL | 把它叫 hidden cycle history |
| raw relation 分叉但所有 branch 当前 observed target 相同 | RELATION + future observation | 宣称底层 relation 已单值化 |

---

## 9. 统一诊断输出

未来 precision/state compiler 在可能时不应只返回一个笼统的 `UNDERRESOLVED`。应至少分别报告：

```text
STATE/FIBER:
    当前 coarse fiber 内还存在什么差异？
    哪些差异能被 declared future language 重新读取？

TARGET/IMAGE:
    所需 target 是否在当前整数 image / representation 中？
    若不在，是永久 arithmetic torsion/gap，还是有限 horizon underresolution？

ACTION/DOMAIN:
    哪些 named operations 当前定义？
    哪些 words causally realizable？
    顺序是否改变 legality？

SUCCESSOR/RELATION:
    下一状态 law 是 functional 还是 relation-valued？
    哪些 branch difference 在 declared observation 下仍然可见？

LEDGER/TRANSFER:
    已量化 / 守恒内容现在分配在哪里？
    当前及未来允许哪些 transfer？
    因而哪些 component total 才是 future-safe？
```

统一外层规则始终是：

> **只保留 declared future operation / observation language 能重新激活的区别；绝不能通过偷偷修改另一个数学层来“修复”当前层的问题。**

---

## 10. 当前证据映射

本文件是当前 canonical + Draft research 的架构综合，不是 canonical Foundation theorem。相关研究面包括：

- #194 lineage 的 canonical finite material impulse / remainder telescope；
- P024 guarded-action / two-sided action-language 工作，包括 #310 / #315；
- contact guarded / homology / critical-precision Draft #342；
- contact-local predictive reservoir Draft #357；
- causal whole-quantum material tick Draft #360；
- history / scheduler ambiguity Draft #365；
- generic A4/P023 relation-observable Draft #368；
- finite TTL queue-age Draft #370；
- TTL loss / operation-order / history Draft #371；
- material-ledger transfer / future-policy precision Draft #372。

所使用的 prior mathematics 包括 quotient/fiber/kernel/cokernel、finite relation、automata/subset construction、numerical semigroup、graph homology/cohomology、critical group、finite queue、graph connectivity 与 integer conservation ledger。

这里不宣称这些标准对象本身都是新数学。项目价值在于 precision-first 架构：这些标准结构出现在**不同失败位置**，构造离散世界状态时绝不能混为一谈。
