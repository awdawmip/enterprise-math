# 未来语言闭包作为半模：整数、Boolean 与商精度

状态：`RESEARCH BRIDGE / NONCANONICAL`

本文从整数 future-observability 与 A4 relation-support 两条研究线中抽取一套共同代数骨架。它是一份架构说明，不主张所有世界 law 都是线性的，也不主张某一种系数体系天然更“真实”。

## 1. 共同闭包公式

固定有限的 named state coordinates 和一个系数半环 `R`。

令 total action 由矩阵 `A_a` 作用在列状态上，声明的线性 observation 由行 `C` 给出。一个 action word `w` 产生 future rows

`C A_w`。

定义

`L_h = span_R { C A_w : |w| <= h }`。

由分配律得到精确递推

`L_(h+1) = L_h + sum_a L_h A_a`。

这就是共同的 future-closure 对象。

不同系数代数决定 `span`、加法和“可重构”究竟意味着什么；递推骨架本身不依赖这些具体解释。

## 2. 与半环无关的 plateau 证书

只要该半环/半模 setting 中上述表达有定义，若某一步满足

`L_(h+1)=L_h`，

则对每一个声明 action 都有

`L_h A_a subseteq L_h`。

因此所有更长 word 也都保持在同一闭包里，得到

`L_(h+t)=L_h`

对所有 `t>=0` 成立。

所以：**一次精确相等的闭包步就是永久停止证书。**

但这不表示任意半环都必然在某个有界 horizon 达到 plateau。有限稳定还需要对应系数体系自己的代数条件。

## 3. 整数特化：`R = Z`

对于整数 actions 与 observations，`L_h` 是 `Z^n` 中的嵌入子模。

`Z^n` 是 Noetherian，所以递增的 row-module chain 最终稳定。当前 executable bridge 还给出了更细结构：

1. 有理 rank 先增长，直到第一次 rational plateau；
2. rational span 稳定后，整数 row lattice 仍可能在同一个 saturated rational span 中继续扩大；
3. 每一次严格的同-span 扩大，saturation index 都必须降为真因子；
4. 若 rational stabilization 发生在 `h_Q`，当时 index 为 `I`，则最终整数闭包最迟在

   `h_Q + Omega(I)`

   达到。

Hermite normal form 可以直接保存嵌入 row lattice，而无需枚举 literal words。Smith / determinantal divisors 则描述抽象整数精度类型：

`(hidden free rank ; Smith invariant factors)`。

但它们并不决定 named world coordinates 中的精度落点。

## 4. Boolean 特化：`R = B = ({0,1}, OR, AND)`

对有限 relation `R_a`，取 Boolean 矩阵

`A_a[target,source]=1 iff source R_a target`。

一个 target observation class 是 indicator row。此时 `C A_w` 正好表示：哪些 initial states 经过 word `w` 后至少有一个 branch 能到达该 observed class。

这里 `span_B` 就是有限 OR/join closure。环境中的 Boolean rows 总共只有 `2^n` 个，因此 chain 稳定的原因很直接：整个 Boolean semimodule 是有限的。

一个有限 join-semilattice 的 join-irreducibles 构成其 canonical 最小 join-generating set。由于 relation preimage 对 OR 可分配，只传播这些 generators 就足够。

于是得到 A4 forward powerset compiler 的精确反向对偶：

- forward support：Boolean column state `v -> A_a v`；
- backward future predicate：Boolean row `c -> c A_a`。

literal relation words 只需要保留为 oracle，不再是主执行路径。

## 5. 状态区分完成，不代表 reconstructive closure 已完成

future state partition 与完整 reconstructive semimodule 是两个不同的精度层。

### 整数情形

state kernel 已经为零时，仍可能存在非单位 Smith factors。后续 future observations 不再增加 state identity，但会继续改善整数坐标重构能力。

### Boolean 情形

一个三状态 relation 例子在 horizon 1 已经把 raw states 全部分开，但 Boolean row semimodule 在 horizon 2 仍新增一个 support predicate。state partition 完全不变，而 OR-可重构的 support 信息继续增长。

因此架构上应区分：

`STATE-EQUALITY PRECISION`

与

`COEFFICIENT-SEMIMODULE RECONSTRUCTION PRECISION`。

后者一般更强。

## 6. 系数同态产生精度商

设 `phi:R->S` 是半环同态，并对 actions / observations 逐项应用 `phi`。那么每个 S-valued future signature 都是对应 R-valued signature 经 `phi` 的像。

因此 R-signature 相等必然推出 S-signature 相等。沿系数同态下降，只可能保持或合并 future distinctions。

### 路径数量 -> 路径 support

对非负 path-count 语义，

`phi:N->B`, `phi(n)=1[n>0]`

是半环同态。

自然数矩阵乘法保留与一个 action word 一致的 witness path 数量；Boolean 乘法只保留是否至少存在一条路径。

所以 exact path-count precision 必然细于 reachable-support precision。

sharp witness：一个 source 有两条 relation branches 进入同一个 observed class，而另一个 source 只有一条。Boolean support 都只回答“reachable”，但 count language 在一步后给出 `2` 与 `1`。

做 equality 分析时，可以把这些非负 count rows 嵌入其 `Z`-module envelope。出现负系数只是分析/重构工具，不表示物理 path count 可以为负。

### 精确整数 -> 模精度

环商

`Z -> Z/MZ`

是另一个系数同态。因此 exact integer future equality 必然细于 modulo-M equality。这与 scheduler/history ambiguity 在模观测下被 quotient 掉是同一种机制。

## 7. Boolean predicate laws 精确定位 DOMAIN 与 RELATION

对 raw relation `R` 定义 existential backward predicate transformer

`T_R(P)={x : exists y in P, xRy}`。

任意 relation 都保 bottom 与 union。

两个更强的代数律分别诊断两个不同 failure layer：

`T_R(X)=X`

当且仅当每个 source 至少有一个 successor —— **DOMAIN / totality**。

`T_R(P intersect Q)=T_R(P) intersect T_R(Q)` 对所有 `P,Q`

当且仅当每个 source 至多有一个 successor —— **RELATION / functionality**。

因此：

- partial deterministic action：保 meet，但 top 有缺陷；
- total branching relation：保 top，但 meet 有缺陷；
- total deterministic function：同时保 top 与 meet，是 predicate 上真正的 Boolean-algebra homomorphism。

这样，partial definedness 与 multivalued branching 被放进了同一张系数层表格，但并没有被混为同一个概念。

## 8. 半环精度仍然不等于 literal operation capability

一个更小的 action family 可以产生完全相同的 state kernel 或 coefficient semimodule，但这只证明 observation precision 层面的冗余。

它不表示被删掉的 named action 仍然可执行，也不保留 literal word provenance、guard、cost、timing 或 actuator meaning。这些属于更强的 DOMAIN/capability semantics。

同样，Boolean support 会忘记路径数量；自然数 count 会把不同 literal paths 合并为同一个数量。若 future language 读取更丰富的 witness identity，就必须使用更丰富的 coefficient/object space。

## 9. 架构总结

共同 compiler 模式是：

`declared actions + declared observations`

`-> coefficient-semimodule future closure L_h`

`-> state equality kernel + reconstructive coefficient state`。

但是 termination/refinement mechanism 必须按系数体系分别证明：

- `Z`：rational rank + lattice saturation / Smith purification；
- `B`：finite join-semilattice growth / join-irreducibles；
- 其他半环：需要自己的 finite-generation / termination theorem。

不能仅凭共享递推式，就推断一个通用的有限 horizon theorem。

本文使用的 semiring/module、Boolean matrix、automata、Smith/Hermite、predicate transformer 与 path-count 事实都是标准既有数学/计算机科学。进取数论的项目价值在于 precision-first routing：先声明 future question 要看的 coefficient semantics，再只保留该问题能够重新激活的闭包信息。