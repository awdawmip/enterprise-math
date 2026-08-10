# R004 精度起源——补充 25：temporal primitive-instruction retirement

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + RESOURCE-POLICY SPECIALIZATION`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_24.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 24 已计算 staged program 每个位置的 weakest live certificate quotient。本补充把 obstruction-cut 视角作用到随时间携带的 primitive instruction set。

新的关键区分是 operational：一个早期已经删除的 primitive instruction，以后还能不能重新 acquisition？这个能力会改变 minimization problem，所以必须属于 typed future language，不能作为未声明的实现假设。

## 1. Future suffix 变弱会扩大 adequate-set family

固定一个 primitive generator catalog G。在 program point i 定义

`Phi_i(S)=1`

表示 retained generator set S 足以执行剩余 suffix。

若 j 晚于 i，且使用同一 catalog semantics，则能执行更长 suffix 的集合必然能执行 tail：

`Phi_i(S)=1 => Phi_j(S)=1`。

令 `C_i,C_j` 为两个 predicate 的 inclusion-minimal deletion-cut clutters。

则每个 later cut 都包含某个 earlier cut：

`forall H_j in C_j, exists H_i in C_i with H_i subseteq H_j`。

证明：later bad deletion set 对更强的 earlier requirement 也必然 bad；earlier bad family 向上闭，因此其中包含一个 earlier minimal bad subset。

所以 future requirement 变弱时，obstruction cuts 只会向 generator subset lattice 外侧移动。

## 2. Minimum instruction count 只能不增

任何 hitting every earlier cut 的 retained set 也会 hit every later cut：对每个 later H_j 选其中的 earlier H_i，击中 H_i 就必然击中 H_j。

因此

`tau(C_j)<=tau(C_i)`。

随着 future requirements 消失，剩余 suffix 所需的 minimum primitive instruction 数不会增加。

但这只是 cardinality law，不表示 later minimum basis 一定是 earlier minimum basis 的 subset。

## 3. Local minimum bases 一般不 nested

取 generators `{a,b,c}`。

Early clutter：

`C_0={{a},{b}}`。

唯一 minimum basis 是

`{a,b}`。

Later clutter：

`C_1={{a,c},{b,c}}`。

唯一 minimum basis 反而是

`{c}`。

future 确实变弱：每个 later cut 都包含一个 earlier singleton cut；minimum cardinality 从 2 降到 1。但

`{c} not subseteq {a,b}`。

所以一个 stagewise optimizer 若永久删除所有 currently redundant generators，可能直接摧毁未来最优 basis。

generator 可以 **currently redundant but globally valuable**。

## 4. Reacquisition allowed 与 no reacquisition

### Global primitive library

若已删除 instruction 可以按零/声明成本重新 load，则各 stage 可独立优化，每个位置都能从头挑当前 minimum basis。

### Carried instruction set

若没有显式 acquisition operation 就不能出现新 primitive，则 retained sets 必须 nested：

`S_(i+1) subseteq S_i`。

这会把 local basis minimization 变成 temporal optimization。

补充 23 的 no-upward-lift rule 使这个区别成为 semantic，而不是 cosmetic：reacquire instruction 是真正的 future capability，存在就必须声明。

## 5. Temporal cut-cover formulation

定义 binary variables

`x_(g,i) in {0,1}`

表示 generator g 在 stage i 仍被保留。

no reacquisition：

`x_(g,i+1)<=x_(g,i)`。

每个 stage 的 adequacy 给出 cut constraints：

`sum_(g in H)x_(g,i)>=1`，对每个 `H in C_i`。

给定非负 holding costs `w_(g,i)`，最小化

`sum_(i,g) w_(g,i)x_(g,i)`。

等价地，每个 primitive instruction 选择一个 retirement time `tau_g`，在该时刻之前一直存在。

这是纯整数 formulation。generic hitting-set / dynamic-programming complexity 属于先行数学；R004 这里只把它用作 compiled instruction cuts 的 resource semantics。

## 6. Anticipatory redundancy example

使用上述三-generator clutters。让 later clutter 持续 h 个 stages，并取 unit holding cost。

Myopic early minimum：

- stage 0 只保 `{a,b}`；
- c 已经永久删除且禁止 reacquisition，所以以后每个 stage 也只能继续保 `{a,b}`。

总成本：

`2+2h`。

Anticipatory schedule：

- stage 0 暂时多保一个当前冗余的 c，即 `{a,b,c}`；
- early requirement 消失后，退休 a,b，只保 `{c}`。

总成本：

`3+h`。

当 `h>=2` 时 anticipatory redundancy 严格更优。

因此“删除每一个 currently redundant primitive”不是合法的 temporal optimization rule。

## 7. Exhaustive cut-clutter pressure test

枚举四 generators 上全部 antichain cut clutters，排除不可能的 empty deletion cut。在所有 **7,413** 对满足 future-weakening bad-family inclusion 的 ordered clutter pairs 中：

- 每个 later minimal cut 都包含一个 earlier minimal cut；
- minimum transversal cardinality 从不增加；
- 但有 **346** 对不存在任何 later cardinality-minimum transversal 被任何 earlier cardinality-minimum transversal 包含。

因此 nonnested-basis phenomenon 在四 generators 上已经很常见，不是手工挑选的 anomaly。

## 8. Architecture consequence

primitive instruction minimization 至少有两个不同模式：

1. **static library optimization**：允许 reacquisition，各 suffix 独立优化；
2. **persistent-machine optimization**：禁止 reacquisition，必须全局选择 nested retirement schedule。

compiler 不能静默选择其中之一。若允许 `ACQUIRE(generator)`，它本身就是 future operation language 的一部分。

这再次体现项目总规则：

> future capabilities 决定正确的 representation problem。

## 9. Next frontier

下一步要把 algebraic cut backends 真正用于 temporal problem：Arithmetic Cut、Module Cut、Structural Target family 是否能直接从 dependency geometry 计算 retirement schedule，而不先展开 generic hypergraph cuts？特别是 matroid basis exchange 暗示“先临时增加再删除”与 strict no-reacquisition 会有 sharp 区别，而 p-adic target cuts 可能携带 extension-depth costs，而不是 unit instruction counts。
