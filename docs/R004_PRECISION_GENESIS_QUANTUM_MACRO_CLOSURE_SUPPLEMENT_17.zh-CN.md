# R004 精度起源——补充 17：typed adequacy cuts 与 primitive instruction sets

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_REDUCTION + P023/A3/A4_INTERFACE`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_16.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 16 已经解决 carrier 一侧：minimal Carrier Bases 是 carrier-cut clutter 的 minimal transversals。但补充 15 已经证明，仅保持同一个 quotient carrier 比保持用户未来真正需要的 semantics 更弱。本补充把两个 obligation 统一成一个 typed adequacy clutter。

## 1. Semantic reconstruction closure

固定完整 compiled carrier：

`Q* = Compile_G(P0)`。

对 retained generators `S subseteq G`，记

`Rec_Q*(S)`

为这些 retained generators 在 `Q*` 上的 descended objects 所生成的、已声明合法的 quotient-level reconstruction closure。

不同 typed semantics 的 reconstruction algebra 不同：

- total operations：term / transformation-monoid closure；
- semiring-valued relations：在声明的有限 addition / composition 下的 semiring polynomial closure；
- semantic factor maps：较弱 channel 可由声明的 homomorphism 重建；
- 更丰富 A3/A4 witnesses：只能使用对应 owner 已经明确证明的 reconstruction interface。

不能仅从 carrier equality 自动猜出 generic semantic closure。

令 `Req` 为任务明确要求未来仍然可执行/可恢复的 descended objects family。

定义 semantic adequacy：

`Psi_sem(S)=1 iff Req subseteq Rec_Q*(S)`。

它对 retained-generator inclusion 单调。

## 2. Carrier adequacy 与 semantic adequacy 不同

Carrier adequacy 仍然是

`Psi_car(S)=1 iff Compile_S(P0)=Q*`。

补充 15 的 discrete-observation swap 例子已经证明二者一般不一致：若 `P0=Q*` 本来就是 discrete，一个非平凡 swap 可以完全不影响 carrier，但若未来明确要求执行这个 swap，且空 instruction set 无法重建它，那么它仍然 semantic-essential。

因此 compiler 必须保留两种 certificate：

- world-generation certificate（`Psi_car`）；
- future-reconstruction certificate（`Psi_sem`）。

## 3. R004-COMP-T28——typed adequacy predicate

定义 joint adequacy：

`Psi(S)=Psi_car(S) AND Psi_sem(S)`。

它是 `2^G` 上的单调 Boolean function。

retained set `S` 当且仅当 `Psi(S)=1` 时是一个 **adequate primitive instruction set**。

这把 semantic actions 与 primitive instructions 的区别正式化：

- 完整 requested future language 是 semantic action surface；
- 若 `S` 在生成同一 safe carrier 的同时，其 quotient algebra 又能重建这个 action surface，则 `S` 是 primitive instruction set。

## 4. R004-COMP-T29——semantic cuts

定义 minimal semantic deletion cuts：

`C_sem = Min_subseteq {H subseteq G : Psi_sem(G\H)=0}`。

每个 semantic cut 都有有限 failure certificate：在 `G\H` 上，至少有一个 required descended object `r in Req` 不属于 `Rec_Q*(G\H)`；而 minimality 表示恢复 cut 中任意一个被删 generator 后，完整 semantic adequacy 都恢复。

semantic cuts 与 carrier cuts 不同，它们不必对应一个更粗 state partition。carrier 完全可以仍是 `Q*`，但某个未来明确要求的 operation/relation table 已经不可重建。

## 5. R004-COMP-T30——joint cut decomposition

令 `C_car` 为补充 16 的 minimal carrier-cut clutter。

由于 joint failure 是析取：

`NOT Psi = (NOT Psi_car) OR (NOT Psi_sem)`，

而两个 failure family 都对 deletion 向上封闭，所以 minimal joint deletion cuts 精确满足：

`C_joint = Min_subseteq ( C_car union C_sem )`。

因此两种 failure family 可以直接合成，不需要第三种 obstruction type。被更小 cut 支配的 edges 自动消失。

joint cut certificate 是 typed 的：

- carrier cut -> canonical forbidden-world partition `P_H`，且 exact kill set = `H`；
- semantic cut -> 一个明确 required descended object，在 retained quotient algebra 中不可重建；
- 若同一个 deletion 同时破坏 carrier 与 semantics，任一 certificate 都可证明 inadequacy，而 minimal-union reduction 只保留 inclusion-minimal cut edges。

## 6. R004-COMP-T31——primitive instruction sets = transversals

retained set `S` jointly adequate，当且仅当它与 `C_joint` 每条 edge 都相交。

因此 inclusion-minimal adequate primitive instruction sets 为：

`B_primitive = Tr(C_joint)`。

把两边都 reduction 到 inclusion-minimal clutter 后，标准 blocker duality 再给：

`C_joint = Tr(B_primitive)`。

这是成熟 hypergraph duality。R004 当前真正新增的是 compiler adequacy predicate 的 typed decomposition：carrier failure certificate + semantic reconstruction failure certificate。

## 7. 一个 exact 三 operation 例子

取 exact states `{0,1,2}`，初始 observation：

`P0={{0,2},{1}}`。

三个 unary operations：

`g0=(0,0,0)`，

`g1=(0,0,1)`，

`g2=(0,0,2)`。

完整 language 编译得到 discrete carrier `Q*`。

Carrier cuts：

`C_car={{g1}}`。

所以唯一 minimal Carrier Basis 是 `{g1}`。

但是在最终 discrete quotient 上，若要求三个 descended operation tables 都必须可通过 composition（identity 免费）重建，则 `g0=g1^2` 可以重建，而 `g2` 不能由 `g1` 单独生成。

Semantic cuts：

`C_sem={{g1},{g2}}`。

于是

`C_joint={{g1},{g2}}`，

唯一 minimal adequate primitive instruction set 为

`{g1,g2}`。

这个例子精确区分：“什么生成了这个世界”与“为了复现要求的未来 algebra，还必须保留什么”。

## 8. 先做 reconstruction pruning，再做 obstruction dualization

补充 15 已证明：若 quotient-level reconstruction certificate 与继续 coarsening 相容，则可推出 carrier redundancy。新的 cut formulation 给出直接算法：

1. 先编译完整 `Q*`；
2. 在 `Q*` 上做 sound algebraic reconstruction pruning（operation terms、semiring relation polynomials、semantic factor maps，或 owner-certified richer reconstruction）；
3. 在剩余 candidates 上建立 `C_car`；
4. 对 explicit requested action surface 建立 `C_sem`；
5. reduction：`C_joint=Min(C_car union C_sem)`；
6. 只在这个 reduced generator clutter 上枚举/求 minimal transversals。

这可以在 combinatorial dualization 前显著缩小 generator universe。

## 9. Exact validation

对所有三个互异的 3-state total unary operations，以及所有 initial partitions，共 **14,625** 个 full instances 做了完整检查。

每个 instance 都：

- 用三个 operations 编译完整 `Q*`；
- 对所有 retained subsets 重新从 fine-state compiler 计算 carrier adequacy；
- 在最终 `Q*` 上独立用 descended retained quotient operations 的 transformation-monoid closure 计算 semantic adequacy，并要求 full descended generator tables 全部可重建；
- 分别枚举 `C_car`、`C_sem` 与直接 joint minimal cuts；
- 检查 direct joint cuts = `Min(C_car union C_sem)`；
- 检查 minimal jointly adequate retained subsets = `C_joint` 的 minimal transversals。

全部 **14,625** instances 通过，0 violation。

结合补充 16 的 **552,960** 个 mixed carrier-cut validations，当前有限 reduction package 有强 exact evidence；仍不主张 full-repository CI 或 canonical-main status。

## 10. Prior-art 边界

minimal hitting sets、hypergraph transversals、blocker/dual hypergraphs 与 monotone Boolean dualization 都是成熟数学。有限 transformation semigroup 的 minimal generating sets/rank 等 algebraic generation 问题也属于先行工作，并已在补充 15 映射。

R004 不把这些 generic problems 宣称为新发明。

项目级结果是 typed compiler factorization：

`typed future language -> final safe carrier + quotient reconstruction algebra -> carrier cuts + semantic cuts -> joint adequacy clutter -> primitive instruction sets`。

这套 Enterprise Math architecture 与 finite certificates 的历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 11. 架构后果

Representation Compiler 现在已经有两个方向。

Forward：

`typed semantic actions -> finite generators -> least common safe carrier -> descended quotient algebra`。

Reverse/minimizing：

`final carrier + required quotient semantics -> obstruction cuts -> minimal primitive instruction sets`。

所以 compiler 可以回答两个不同问题：

1. 哪些 exact-state distinctions 是 future language 真正要求保留的？
2. 哪些 future-language generators 对生成并重建这个世界是独立必要的？

这就是 semantic-action vs primitive-instruction-set distinction 的精确 finite form。generic quotient/operation semantics 的母层仍归 P023；更丰富 relation/witness semantics 归 A3/A4；R004 只负责 cross-surface finite reductions、counterexamples 与 certificates。

## 12. 下一 frontier

generic obstruction problem 已经不再是“枚举所有 forbidden state partitions”，而是 generator bits 上的 monotone dualization。

下一步真正属于项目的问题是：利用 typed algebra 自身进一步压缩 `C_joint`。也就是找出哪些 classes 中，carrier/semantic cut edges 可以直接由 support、rank、prime axes、relation kernels、guard-image lattices 等 algebraic invariants 推出，而不需要调用 compiler 枚举全部 `2^|G|` retained subsets。
