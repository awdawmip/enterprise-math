# R004 精度起源——补充 14：混合 typed fixed-point dispatcher 与 generator descent

状态：`PROVED_WIP + EXECUTABLE_CHECKED + CORRECTION + PRIOR_ART_SPECIALIZATION + P023/A3/A4_BOUNDARY`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_13.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 13 正确建立了 quotient-relative relation stabilization、semantic factor order 和 relation activation cascade，但其中关于 total operation 的对照表述过强。真正成立的 raw-meet 结论只适用于**固定同一个 operation family、只改变 observations**。不同 operation families 之间也会互相激活，而且可以要求任意长的交替 repair。本补充据此修正边界，并把原来的 operation/relation 二分升级成一个统一 mixed typed fixed-point 接口。

## 1. R004-COMP-CORR-01——固定 algebra 的 meet law，而不是所有 operation 的 meet law

固定有限 carrier `X` 上同一个 total finitary algebra `A`。对 observation partition `P`，记 `C_A(P)` 为 refine `P` 的最粗 `A`-congruence。

则任意 `P,Q` 都满足：

`C_A(P meet_raw Q) = C_A(P) meet_raw C_A(Q)`。

原因是 `C_A(P)` 与 `C_A(Q)` 都是**同一个 algebra** 的 congruence，所以交集仍是 congruence；反向则由“最大 compatible congruence”的定义直接得到。

对 `|X|=2,3,4` 的所有 unary operation 和 partition pairs 共 **58,291** 个 case 做了独立有限检查，0 violation。

这条 theorem 不能推广成“不同 operation languages 分别编译后 raw meet 就结束”。

## 2. R004-COMP-CE13——不同 total operations 会 cross-activate

取 `X={0,1,2,3}`：

`f=(0,0,0,1)`，`g=(0,0,3,0)`，

初始 partition：

`P_0={{0,2,3},{1}}`。

单独编译 `f`：

`P_f={{0,2},{1},{3}}`。

单独编译 `g`：保持 `P_0` 不变。因此二者 raw common refinement 仍为 `P_f`。

但 `P_f` 对 `g` 已不 stable：`0,2` 仍同块，而 `g(0)=0`、`g(2)=3` 已落入不同 target blocks。所以 joint compiler 还必须再拆，最终得到 discrete partition。

穷举 `|X|<=3` 的所有 unary-total-operation pair 与 initial partition，共 **3,677** cases，没有发现这种 failure；因此在该 bounded class 中 4 states 为最小尺寸。

## 3. R004-COMP-T15——任意长度的 operation ping-pong

上述 4-state witness 不是偶然。

任意 `n>=3`，令

`X_n={0,1,...,n-1}`，

`P_0={{0},{1,...,n-1}}`。

定义：

`f(0)=g(0)=0`；

当正整数 `k` 为奇数时 `f(k)=k-1`，否则 `f(k)=k`；

当正整数 `k` 为偶数时 `g(k)=k-1`，否则 `g(k)=k`。

从 `P_0` 出发，先做 `f` closure 会只拆出 state `1`；随后 `g` closure 拆出 `2`；下一次 `f` 拆出 `3`；继续交替。

第 `t` 次 strict activation 后：

`{{0},{1},...,{t},{t+1,...,n-1}}`。

所以达到 discrete partition 恰需

`n-2 = |X|-|P_0|`

次严格 cross-language refinement。

因此不存在与 state size 无关的“两遍够了”“每种 operation 编译一次够了”规则。共同 fixed point / worklist 是数学必要条件，而且 block-count termination bound 是 sharp 的。

## 4. R004-COMP-T16——统一 mixed typed signature

一般 finitary operation 到 unary elementary contexts 的 generic compiler 已由 A2/P023 持有；R004 只消费这些 unary contexts，不复制母定理。

对当前 partition `P`，mixed typed language 可以包含：

1. total unary contexts `f:X->X`；
2. partial unary contexts `g:D_g subset X -> X`，其中 enabledness 本身属于 future semantics；
3. 使用交换幺半群 block aggregation 的 quotient-relative relation channels。

定义：

`S_P(x) = ([x]_P, ([f(x)]_P)_f, (tag_g(x))_g, (Sigma_(c,P)(x,B))_(c,B in P))`。

其中 partial tag 为：

- undefined 时 `disabled`；
- defined 时 `(enabled,[g(x)]_P)`。

一次 mixed refinement 就是：

`P^+ = ker S_P`。

因为 signature 显式包含当前 class `[x]_P`，所以只会继续 refine，不会合并已存在 distinctions。

## 5. R004-COMP-T17——唯一最粗 mixed fixed point

从 initial observation partition `P_0` 迭代：

`P_(r+1)=ker S_(P_r)`。

每个 strict step 至少多一个 block，因此最多经过

`|X|-|P_0|`

次 strict steps 即终止。

终态 `P_*` 恰是同时满足所有 declared typed obligations 的**唯一最粗 refinement**。

证明核心：若 `Q` 是任意 jointly stable refinement，且归纳已知 `Q` refine `P_r`，则：

- total operation 在 `Q` 中 output class 相同，因而在更粗的 `P_r` 中也相同；
- partial operation 在 `Q` 中 enabledness 一致，且 enabled output 也 `Q`-equivalent；
- 每个 `P_r` target block 都是若干 `Q` blocks 的并，交换幺半群上逐 `Q` block aggregate 的相等可以继续合并成逐 `P_r` block 的相等。

所以 `Q` refine `P_(r+1)`。归纳后 `Q` refine `P_*`，证明 `P_*` 最粗。

generic fixed-point / partition-refinement 数学属于 prior art；项目价值在 typed P023/A3/A4 接口及有限 specializations。

## 6. R004-COMP-T18——模块化 closure/worklist theorem

若每个 typed sublanguage `L_i` 提供自己的最粗 stable-refinement closure `C_i`，则这些 `C_i` 都满足 refinement-extensive、monotone、idempotent。

任何 fair worklist 反复执行

`P <- C_i(P)`

并在出现 strict refinement 后重新激活其他可能受影响 semantic domains，最终都会到达同一个 least common fixed point，与 fair scheduling 顺序无关。

原因是 partition 只能严格 refine 有限次；fair schedule 终止时所有 `C_i` 都固定结果。另一方面，任何共同 fixed point 通过 monotonicity 都始终位于所有 intermediate partitions 之上，因此终态就是最粗共同 fixed point。

在 3-state 全 family 中，同时放入一个 total unary operation、一个 partial unary operation 和一个 COUNT relation channel，对 **552,960** 个 cases 检查六种 cyclic domain orders，全部与 simultaneous compiler 一致。

这允许 dispatcher 复用 P023/A3/A4 owner compilers，而不需要造一个 monolithic replacement engine。

## 7. R004-COMP-T19——partial legality totalization

对 partial unary operation `g`，加入独立 `bottom` state：

`g_hat(x)=bottom` 当 `g(x)` undefined；否则 `g_hat(x)=g(x)`；并令 `g_hat(bottom)=bottom`。

把 `bottom` 永远放在自己的 coarse class。

则 `P` 上“同一 fiber 内 definedness 一致 + defined output class 一致”，恰等价于 lifted partition 对 `g_hat` 的 ordinary compatibility。

所以 legality 在 quotient compatibility 层不是另一个神秘 precision primitive，而是一个 tagged deterministic output。

这里只把 one-point totalization 当 compatibility device；不宣称任意 partial algebra 的全部 algebraic identities 都被这种 extension 保留。

3-state 所有 **320** 个 partial-unary/partition cases 已穷举验证。

## 8. R004-COMP-T20——stable semiring relations 构成子 semiring

若 relation weights 落在 semiring `K` 中。对 partition `P`，若矩阵 `R` 满足：

对任意 source block `A`、target block `B`，

`sum_(y in B) R(x,y)`

只依赖 `A=[x]_P`，则称 `R` 为 `P`-stable，并定义 quotient matrix `R_bar`。

所有 `P`-stable matrices 包含 `0,I`，对 `+` 与 matrix multiplication 封闭，并且

`R -> R_bar`

是 semiring homomorphism：

`overline(R+S)=R_bar+S_bar`，

`overline(RS)=R_bar S_bar`。

乘法证明只需把中间 state 按当前 blocks 分组：

`sum_(z in C) (RS)(x,z)`

`= sum_B (sum_(y in B)R(x,y)) S_bar(B,C)`

`= sum_B R_bar(A,B) S_bar(B,C)`。

所以未来如果声明 sequential relation composition，compiler 只需稳定 relation **generators**，不用把每个 finite path expression 都展开进 state synthesis。

3-state `N_0` path-count matrices 共 **4,964** 个 stable pair 做了 product closure / quotient multiplication 精确核对，全部成立。

## 9. R004-COMP-T21——MAY path lifting 与有限 reachability

Boolean semiring 就是 MAY/reachability specialization。

当 relation generators 已 block-MAY stable 时，每个 finite composition 都精确下降。尤其 stable intermediate relation 消除了 coarse world 的 fake witness stitching：同一个 intermediate block 的任意 representative 都具有相同 outgoing block-support word，因此 coarse path 可以逐 block lift 成真实 fine path。

若没有 stability，2 states 已有最小 fake stitching：把两个 states 放在同一 coarse block，令 `R` 只有 `0->0`，`S` 只有 `1->1`。粗世界看见 `R` 非空、`S` 非空，于是错误拼出 composition path；fine `R;S` 实际为空。

3-state 独立验证：

- 满足 downstream MAY stability 的 two-step cases：**8,960**，0 failure；
- three-step stable downstream generators：**361,472**，0 failure；
- stable Boolean single-relation reflexive-transitive reachability：**140**，0 failure。

所以 finite Boolean world 中，一步 relation stabilization 可以为任意有限 path horizon 提供统一 descent certificate。

## 10. R004-COMP-T22——有限 typed generator basis

当前 compiler 可以把**carrier synthesis** 与**future syntax closure**分开。

若声明一个 finite typed generator basis：

- total operation generators compatible，则所有普通 algebraic terms 自动下降；
- partial-operation generators 的 definedness/value compatible，则 generated partial terms 可归纳下降；
- semiring relation generators stable，则这些 matrices 生成的所有有限 semiring polynomials 都通过 quotient homomorphism 精确下降。

因此，如果一个未来语言由有限 typed basis 代数生成，就不必逐条枚举无限多 future expressions。

目前最强 Representation Compiler contract 可以写成：

`Exact Carrier + Typed Generator Basis + Initial Observation`

`-> least common safe fixed point`

`-> descended generator tables / quotient matrices`

`-> requested future syntax 的 algebraic closure certificates`。

## 11. Validation

独立研究穷举（与 committed direct regression 分开）覆盖 3-state 所有：

- 一个 total unary operation；
- 一个 partial unary operation；
- 一个 loopless binary relation；
- 每个 initial partition。

COUNT、MAY、MUST 三种 relation aggregation 各有 **552,960** cases，全部与 full stable-partition oracle 一致。

另外：固定-operation observation meet **58,291** cases；小尺寸不同-operation raw-meet search **3,677**；partial totalization **320**；semiring product **4,964**；two-step MAY path **8,960**；three-step MAY path **361,472**；Boolean reachability **140**，均无反例。

候选 `precision_mixed_typed_dispatcher.py` 的 7 个 direct `unittest` 在当前 private Python 环境通过。这里不宣称 fresh full-repository CI 或 canonical-main 状态。

## 12. Prior art 与 ownership 边界

以下都是成熟数学：generic fixed-point iteration、congruence closure、partial-algebra congruence、equitable/balanced partitions、weighted/semiring transition systems、weighted bisimulation、quotient matrices、coalgebraic partition refinement，以及 transition types 的 modular combination。

现有 coalgebraic partition-refinement 工作已经覆盖 weighted systems 和多种 system type 的 modular composition，所以 R004 不能把 generic mixed partition refinement 当成新发明。

R004 当前 project-local 新增只保留：

1. 用 explicit different-operation activation family 修正此前过强的 operation/relation 二分；
2. 把 P023/A3/A4 obligations 接入一个 finite typed-signature fixed point，但不夺取 mother ownership；
3. 把 legality、relation composition 变成显式 typed descent certificates；
4. 区分 finite generator compilation 与 potentially infinite future syntax；
5. 在这一套 finite compiler 中保持 integer/fractionless internal representation。

历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 13. 下一前沿

下一问题已经不是“再造一个 refinement engine”，而是**minimal typed generator synthesis**：

> 给定一个很大的 future language，哪些 operation contexts、legality probes、relation channels、witness semantics 的有限子集，恰好足以生成同一个 safe carrier 与 descended future algebra？

semantic factor maps 已经可以删掉部分 dominated channels，例如 COUNT 或 LABEL-SET 可推出 MAY；但完整 minimal-basis compiler 还必须识别 algebraic generation 与 cross-domain redundancy，同时不能把 generator selection 本身做成比原 future language 更难的黑箱问题。

该问题应继续回到 P023/A3/A4 interface；R004 负责提供有限 theorem、no-go 与 executable reduction。
