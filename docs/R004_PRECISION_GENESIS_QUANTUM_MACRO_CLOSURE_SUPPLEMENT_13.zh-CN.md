# R004 精度起源——补充 13：typed relation compiler 与语义激活级联

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + CORRECTED_BY_SUPPLEMENT_14 + P023/A4_BOUNDARY`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_12.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 12 已证明 future kernel 只是 equality IR；仅凭 kernel 一般不能恢复 quotient 上的 typed semantics。本补充把 relation/witness stabilization 做成有限可执行 compiler。补充 14 随后纠正了本文件第一版中一处过强对照：**raw meet 只在固定同一个 operation family、改变 observations 时有保证，并不能推广到任意不同 operation languages。** 不同 operation families 也会 cross-activate，需要共同 fixed point。

下列 relation 结果本身不受该纠正影响。

## 1. Typed relation channel

设 `X` 是有限 carrier，`P` 是当前 partition。typed relation channel `c` 包含交换幺半群 `(M_c,op_c,0_c)` 与 edge/witness values `w_c(x,y)`。

对 source state `x` 和当前 target block `B`：

`Sigma_(c,P)(x,B)=op_(y in B) w_c(x,y)`。

若同一 source block 内 states 对所有 declared channels、所有当前 target blocks 的 aggregate vectors 完全相同，则 `P` typed-relation stable。

常见 instances：

- MAY：`(Bool,OR,False)`；
- witness COUNT：`(N_0,+,0)`；
- witness LABEL-SET：有限集合并集；
- 同时保留多语义时取 monoid product。

generic weighted/monoid partition refinement 属于 prior art；R004 只把它作为 typed future-language specialization。

## 2. R004-COMP-T11——唯一最粗 stable refinement

从 initial observation `P_0` 出发，每轮按**当前 target blocks**上的完整 typed relation signature 拆 source blocks。

每次 strict round 至少增加一个 block，因此最多经过

`|X|-|P_0|`

次 strict rounds 即终止。

终态 `P_*` 是 `P_0` 的唯一最粗 typed-relation-stable refinement。

证明：若 `Q` 是任意 stable refinement 且 `Q` refine `P_n`，则每个 `P_n` block 都是若干 `Q` blocks 的并。逐 `Q` block aggregate 相等通过交换幺半群聚合后，逐 `P_n` block aggregate 仍相等，因此 `Q` refine `P_(n+1)`。归纳得到 `Q` refine `P_*`。

## 3. R004-COMP-T12——semantic factor-map monotonicity

若 channel semantics `M,N` 之间存在 monoid homomorphism `phi:M->N`，且 `N` edge data 是逐 edge 应用 `phi` 得到，则每个 `M`-stable partition 都 `N`-stable：

`Compiler_M(P_0)` refine `Compiler_N(P_0)`。

典型例子：

- COUNT -> MAY：`n -> (n>0)`；
- LABEL-SET -> MAY：`S -> (S nonempty)`。

因此 typed precision 应按 structural information order 组织，而不是只靠 scalar class count。

## 4. R004-COMP-CE10——相同 class count 不等于相同 typed precision

取 `X={x,y,z,a,b}`，witnesses：

- `x->a` label `p`；
- `x->b` label `q`；
- `y->a` label `p`；
- `y->b` label `p`；
- `z->a` label `p`；
- `a,b` 无 outgoing witness。

从 universal observation 编译：

- MAY：`{{x,y,z},{a,b}}`，2 classes；
- COUNT：`{{x,y},{z},{a,b}}`，3 classes；
- LABEL-SET：`{{x},{y,z},{a,b}}`，3 classes；
- COUNT+LABEL-SET：`{{x},{y},{z},{a,b}}`，4 classes。

COUNT 与 LABEL-SET 都是 3 classes，却对应不可比较 partitions。class count 只是 derived complexity statistic。

## 5. R004-COMP-T13——修正后的固定-operation-family observation meet law

固定同一个 total finitary algebra `A`。记 `C_A(P)` 为 contained in observation `P` 的最大 `A`-congruence。

则：

`C_A(P meet_raw Q)=C_A(P) meet_raw C_A(Q)`。

原因是两边的 closed kernels 都是**同一个 algebra** 的 congruences，而同一 algebra 的 congruences 对 intersection 封闭。

本补充第一版容易被读成“不同 operation languages 也可各编译一次后 raw meet”。该推广是错误的。补充 14 给出 4-state counterexample 与任意长度 two-operation ping-pong family。正确规则是：

- 固定 operation family + 不同 observations：上述 raw-meet theorem 成立；
- 不同 operation families：除非另有 commutation certificate，否则必须求 common fixed point。

## 6. R004-COMP-CE11——relation task 会被新 target geometry 激活

取 `X={0,1,2}`，initial universal partition，两个 channels 都用 COUNT。

Channel `A`：只有 `0->1`。

Channel `B`：cycle `0->1,1->2,2->0`。

分别编译：

- `A` -> `{{0},{1,2}}`；
- `B` -> universal partition。

raw common refinement 仍为 `{{0},{1,2}}`，但 joint language 下不 stable。`A` 一旦把 target `{0}` 暴露，`B` 就能区分 `1,2`，最终到 discrete partition。

这证明一个 typed requirement 可以通过改变 quotient geometry 激活另一个 requirement。

## 7. R004-COMP-CE12——单个 fixed relation channel 内部也会 raw-meet failure

5 states 上取 graph：

- `0->2,3`；
- `1->2,3`；
- `2->0,1`；
- `3->0,1`；
- `4->0,1`。

COUNT semantics 下：

`P={{0,2,4},{1,3}}`，

`Q={{0,3,4},{1,2}}`

都 stable。但 raw common refinement

`{{0,4},{1},{2},{3}}`

不 stable，必须继续 split 到 discrete partition。

对所有 `n<=4` loopless directed simple graphs 的穷举没有发现同类 same-channel failure，因此该 5-state witness 在此 bounded class 中最小。

## 8. R004-COMP-T14——stable common refinement = stabilization(raw meet)

对固定 typed relation language `W`，记 `Stab_W(P)` 为 `P` 的唯一最粗 stable refinement。

`Stab_W` refinement-extensive、monotone、idempotent。对已经 stable 的 `P,Q`，其 stable common refinement 为：

`Stab_W(P meet_raw Q)`。

5-state witness 证明最后的 stabilization 一般不能删掉。

balanced-equivalence / weighted-network theory 中已有紧邻 prior art；R004 只将其作为 compiler control rule。

## 9. 修正后的 compiler architecture

当前结论绝不是“operation 一遍、relation fixed point”。正确结构是：

1. 每个 typed semantic family 都给当前 partition 一个 closure/stabilization obligation；
2. raw one-pass 只有在存在该 fixed family 的显式 theorem 时才可用，例如固定 algebra 的 congruence meet law；
3. 不同 semantic families——包括两个不同 total operation languages——都可能 cross-activate，默认应求 least common fixed point；
4. quotient-relative relation aggregation 还有更强现象：同一个 fixed channel 的两个 stable partitions，raw intersection 仍可能不 stable。

补充 14 实现新的 mixed fixed-point dispatcher，并加入 legality / semiring descent certificates。

## 10. 本代保留验证

独立穷举：

- COUNT relation compiler/oracle，`n<=4` 全 loopless directed simple graphs + 全 initial partitions：**61,769** cases，0 mismatch；
- MAY 同 family：**61,769** cases，0 mismatch；
- COUNT result refine MAY result：同 **61,769** cases，0 violation；
- `n<=4` 共 **4,165** loopless directed simple graphs：无 same-channel COUNT raw-meet failure；
- 5-state witness：raw meet 失败且 stabilization 到 discrete partition。

补充 14 增加 operation 侧纠正与 mixed validation matrix。

## 11. Ownership 与 prior art

weighted/monoid transition systems、weighted bisimulation、balanced/equitable partitions、coalgebraic partition refinement、balanced-equivalence lattices、algebra congruence lattices 都是 prior mathematics。

R004 只保留 typed Enterprise Math placement、factor-order/counterexample package 与 cross-owner reduction；generic mother ownership 继续属于 P023/A3/A4，historical novelty 仍为 `NOVELTY_UNVERIFIED`。
