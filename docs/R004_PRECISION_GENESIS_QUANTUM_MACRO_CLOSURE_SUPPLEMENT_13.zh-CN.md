# R004 精度起源——补充 13：typed relation compiler 与语义激活级联

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + P023/A4_BOUNDARY`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_12.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 12 已经证明：future kernel 只是 equality IR；仅凭 kernel，一般不能恢复 quotient 上应当保留的 typed semantics。本补充把下一层 relation/witness future language 做成有限可执行 compiler。

这里不是重新发明一般 bisimulation。weighted bisimulation、balanced/equitable partition、coalgebraic partition refinement、monoid-weighted network 及其稳定 partition lattice 都是成熟先行数学。R004 当前真正固定的是一条项目级边界：

> total-operation congruence 可以直接按 kernel 交集组合；而相对于当前 quotient 做 target-block aggregation 的 relation/witness semantics，在合并两个分别已经编译的任务后，可能必须重新发生 stabilization cascade。

因此 compiler 必须知道什么时候“取交”就结束，什么时候还要重新 repair。

## 1. Typed relation channel

设 `X` 是有限状态集，`P` 是当前 partition。

一个 typed relation channel `c` 包含：

- 一个声明的交换幺半群 `(M_c, op_c, 0_c)`；
- edge/witness value `w_c(x,y) in M_c`。

对 source state `x` 和当前 target block `B in P`，定义 block aggregate

`Sigma_(c,P)(x,B) = op_{y in B} w_c(x,y)`。

把所有 channel、所有当前 target blocks 的 aggregate 拼起来，就是 `x` 在 `P` 上的完整 typed relation signature。

若同一 source block 中的 states 具有完全相同 signature，则称 `P` 对该 typed relation language **stable**。

Executable reference 把结合律、交换律、单位元律作为调用方声明的语义前提；代码本身只验证有限 carrier / partition 契约以及 aggregate 可哈希性。

## 2. R004-COMP-T10——常见有限 relation semantics 都是 monoid instance

### MAY support

使用 Boolean monoid `(Bool, OR, False)`。当且仅当存在 relation edge `(x,y)` 时令 `w(x,y)=True`。于是 `Sigma(x,B)` 只回答：“`x` 是否至少能到达 `B` 中一个 target”。

### Witness multiplicity

使用 `(N_0, +, 0)`，其中 `w(x,y)` 等于 `x` 到 `y` 的 declared witness 数。此时 `Sigma(x,B)` 是进入 target block 的精确 witness multiplicity。

### Witness label/class set

使用有限集合并集 `(P_f(L), union, emptyset)`。此时 `Sigma(x,B)` 是所有进入该 target block 的 witness label/class 集合。

若 future 同时需要多种语义，可以使用 monoid product；reference implementation 等价地允许多个 channels，并连接它们的 signatures。

## 3. R004-COMP-T11——唯一最粗 stable refinement

从初始 observation partition `P_0` 出发，每一步按照**当前 target blocks**上的完整 typed relation signature，继续拆分当前 source blocks：

`P_0 >= P_1 >= P_2 >= ...`

这里 `>=` 表示“更粗”。

每次 strict round 至少增加一个 class，所以有限 carrier 上最多经过 `|X|-|P_0|` 次 strict rounds 即停止。终态 `P_*` 是 stable。

更强的是：`P_*` 是 `P_0` 的**唯一最粗 stable refinement**。

证明。取任意 stable refinement `Q`。归纳假设 `Q` refine `P_n`。每个 `P_n` target block 都是若干 `Q` blocks 的并。因为 `Q` stable，同一 `Q` block 中的 states 对每个 `Q` target block aggregate 相同；交换幺半群的聚合允许把这些相等式继续合并到 `P_n` blocks，所以这些 states 在 `P_n` 上 signature 也相同。因此 `Q` refine `P_(n+1)`。归纳到终态即得任意 stable refinement 都 refine `P_*`。

这属于成熟 balanced/weighted partition-refinement 数学的有限 specialization，不作为一般 refinement 新定理宣称。

## 4. R004-COMP-T12——semantic factor-map monotonicity

若两个 channel semantics 分别取值于交换幺半群 `M,N`，并存在 monoid homomorphism `phi:M->N`，而 `N`-valued edge data 正好是逐 edge 对 `M` data 应用 `phi` 得到，则每一个 `M`-stable partition 都必然 `N`-stable：

`phi(op_M values)=op_N phi(values)`。

因此 `Compiler_M(P_0)` refine `Compiler_N(P_0)`。

这给 typed future languages 提供了一个 information order，而不需要把所有语义压成一个 scalar precision。

两个重要 exact factor maps：

- witness count `n -> (n>0)`，从 `(+ ,0)` 到 `(OR,False)`，所以 COUNT 必然 refine MAY；
- witness label-set `S -> (S nonempty)`，从 union 到 OR，所以 LABEL-SET 必然 refine MAY。

## 5. R004-COMP-CE10——相同 class count 不等于相同 relation precision

取 `X={x,y,z,a,b}`，初始 observation 为 universal partition。声明 witnesses：

- `x -> a` label `p`；
- `x -> b` label `q`；
- `y -> a` label `p`；
- `y -> b` label `p`；
- `z -> a` label `p`；
- `a,b` 没有 outgoing witnesses。

编译结果：

- MAY：`{{x,y,z},{a,b}}`，2 classes。
- COUNT：`{{x,y},{z},{a,b}}`，3 classes。
- LABEL-SET：`{{x},{y,z},{a,b}}`，3 classes。
- COUNT + LABEL-SET：`{{x},{y},{z},{a,b}}`，4 classes。

所以 COUNT 和 LABEL-SET 虽然都是 3 classes，却是不可比较的 partitions。

因此即便 class count 已经被做成 task-relative，`safe class 数` 仍不是 typed relation precision 的完整坐标。正确结构是 `semantic factor map -> safe-partition refinement`。class count 只能是 derived complexity statistic。

## 6. R004-COMP-T13——total-operation task 满足 raw meet law

对 total finitary algebra，operation-compatible equivalence relations 就是 congruences，而 congruences 对任意交封闭。

因此同一个 total-operation language 下，两个 observation/task packages 分别编译得到最大 compatible congruences `Theta_1,Theta_2` 时，联合 observation package 的结果就是 `Theta_joint = Theta_1 intersect Theta_2`。

所以 total-operation task 在已经分别编译之后，其 equality kernels 可以直接做 raw common refinement，不需要额外发生 congruence repair cascade。

这是普通 congruence-lattice 数学，母层属于 A2/P023；R004 只把它作为 typed compiler boundary 的对照半边。

## 7. R004-COMP-CE11——一个 relation task 可以被另一个 task 暴露的新 target geometry 激活

quotient-relative relation aggregation 不满足上述 raw meet law。

取 3 states `{0,1,2}`，初始为 universal partition。两个 channels 都使用 witness-count semantics。

Channel `A` 只有一个 witness：`0 -> 1`。

Channel `B` 是 directed 3-cycle：`0 -> 1`, `1 -> 2`, `2 -> 0`。

分别编译：

- `A` 得 `P_A={{0},{1,2}}`；
- `B` 得 universal partition `P_B={{0,1,2}}`，因为在唯一 target block 中，每个 state 都恰有一个 `B` witness。

raw common refinement 仍是 `P_A meet_raw P_B={{0},{1,2}}`。

但它对 joint language 已不 stable。`A` 一旦把 target `{0}` 与 `{1,2}` 分开，`B` 就开始可区分：state `1` 的 B witness 落入 `{1,2}`；state `2` 的 B witness 落入 `{0}`。

所以联合 compiler 必须再 repair 一轮，最终成为 discrete partition：`1 class -> 2 classes -> 3 classes`。

即 `Compiler_(A+B)(P_0) != Compiler_A(P_0) meet_raw Compiler_B(P_0)`。

在已穷举的 loopless directed simple two-channel system 类中，这是最小例子：1、2 states 都不存在这种 cascade。

关键不是“relation 天生更复杂”，而是这里的 relation semantics 是**相对于当前 quotient**定义的：输出是进入当前 quotient target blocks 的 aggregate。target blocks 一旦被其他语义继续拆开，原来不可见的 relation difference 就可能变成可见。

## 8. R004-COMP-CE12——单个 relation channel 内部也会 raw-meet failure

同一个固定 relation channel 的 stable partitions 之间也可能出现这种现象。

取 5 states `{0,1,2,3,4}`，simple directed graph：

- `0 -> 2,3`；
- `1 -> 2,3`；
- `2 -> 0,1`；
- `3 -> 0,1`；
- `4 -> 0,1`。

在 witness-count semantics 下，`P={{0,2,4},{1,3}}` 和 `Q={{0,3,4},{1,2}}` 都 stable：对各自两块，每个 state 的 count vector 都是 `(1,1)`。

但 raw common refinement `P meet_raw Q={{0,4},{1},{2},{3}}` 不 stable。state `0` 指向 singleton targets `{2},{3}`，state `4` 则指向 `{0,4}` 与 `{1}`。

再 stabilization 一轮会拆开 `{0,4}`，得到 discrete partition。

对所有 `n<=4` 的 loopless directed simple graphs 做穷举，没有发现任何一对 count-stable partitions 的 raw common refinement 失稳。因此该 5-state witness 在这个 bounded class 中是最小的。

## 9. R004-COMP-T14——stable meet = stabilization(raw meet)

记 `Stab_W(P)` 为固定 typed relation language `W` 下，`P` 的唯一最粗 stable refinement。

则 `Stab_W(P)` refine `P`；`Stab_W` idempotent；若 `P` refine `Q`，则 `Stab_W(P)` refine `Stab_W(Q)`。

所以对已经 stable 的 `P,Q`，stable-partition lattice 中的 meet 为 `P meet_W Q = Stab_W(P meet_raw Q)`。

5-state example 证明最后这个 `Stab_W` 一般不能删掉。

balanced-equivalence / weighted-network theory 中已经存在 stable lattice 先行结构；R004 这里只把它作为 compiler control rule。

## 10. 对 Representation Compiler 架构的直接后果

Supplement 12 的接口是 `Exact Carrier + Typed Future Language -> Minimal Safe Carrier + Descended Typed Semantics`。

现在进一步得到 dispatch 规则。

### Total-operation semantics

elementary contexts 是 fine carrier 上固定的 functions。compatible kernels 构成对 intersection 封闭的 congruence family。因此直接复用 A2/P023 operation-congruence engine；已经分别编译的 task kernels 可以 raw meet。

### Quotient-relative relation/witness semantics

一个 source state 的 observable 不是固定的一串 exact target identities，而是对**当前 quotient target blocks**做 aggregate。

所以 compiler 必须跑 fixed point：`current target geometry -> source signatures -> refined target geometry -> new source signatures -> ...`。

多个独立 relation channels 应当通过 product signatures 同时编译；等价地，也可以反复 stabilization 到共同 fixed point。不能“每个 channel 单独跑一次，然后取交一次”就结束。

这就是 R004 compiler 中第一条 exact **semantic activation cascade**：一个 typed requirement 可以通过改变 quotient target geometry，让另一个此前不区分 state 的 requirement 变成区分 state。

## 11. Ownership 与 prior-art 边界

以下属于成熟数学，不是 Enterprise Math novelty：weighted / monoid-valued labelled transition systems 与 weighted bisimulation；balanced/equitable network partitions；generic coalgebraic partition refinement；coarsest invariant refinement algorithms；balanced equivalence relations 的 complete lattice；total algebra 的 congruence lattice。

对应 source IDs 记录在 `sources_r004_typed_relation_compiler.json`。

R004 当前 WIP 新增更窄：

1. 在既有 future-language compiler 中把 relation semantics 明确类型化为 MAY、witness COUNT、witness LABEL-SET 及其 products；
2. 用 monoid factor map 作为一个 semantic quotient 必然 refine 另一个的 exact sufficient certificate；
3. 给出同 class count 但 COUNT/LABEL-SET partitions 不可比较的例子，证明 scalar class count 不是完整 relation-precision coordinate；
4. 区分 total-operation composition（congruence raw meet）与 quotient-relative relation aggregation（stabilize raw meet）；
5. 给出 3-state two-channel semantic-activation cascade 与 5-state same-channel raw-meet failure，并做 bounded minimality checks；
6. 把 generic mother mathematics 回流 P023/A4，不建立重复基础层。

这套 Enterprise Math package 的历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 12. Validation

Committed regressions 覆盖 typed-order 与 cascade examples。

另有独立穷举：

- `n<=4` 的所有 loopless directed simple graphs、所有 initial partitions，COUNT semantics：**61,769** 个 compiler/oracle cases，0 mismatch；
- 同一 family 的 MAY semantics：**61,769** cases，0 mismatch；
- 同一 **61,769** cases 上 COUNT result refine MAY result：0 violation；
- `n<=4` 共 **4,165** 个 loopless directed simple graphs：未发现 same-channel count-stable raw-meet failure；
- 上述 5-state graph：raw meet 确认失败，stabilization 得 discrete partition。

oracle 独立枚举所有满足 stability contract 的 set partitions，再选唯一最粗 stable refinement，并未调用 iterative compiler 自证。

新模块的 5 个 direct `unittest` regressions 在当前 private Python environment 全部通过。这里不主张 fresh full-repository CI、Lean proof 或 canonical-main status。

## 13. 下一 frontier

下一问题不再是“relation partition 怎么 refine”。generic refinement 已是先行数学。

真正的项目问题是：

> 给定同时含 operation、quotient-relative relation、witness identity class、MAY/MUST requirement、甚至 partial legality 的 **typed future language**，compiler 能否自动构造最弱的 semantic-domain product，把各部分路由到正确 stabilization engine，并输出显式 descent certificates，证明声明的每一种 future composition 在 compiled carrier 上都仍合法？

这属于 P023/A3/A4 interface。R004 继续提供 finite reduction theorem 与 counterexample，不夺取 mother abstraction。
