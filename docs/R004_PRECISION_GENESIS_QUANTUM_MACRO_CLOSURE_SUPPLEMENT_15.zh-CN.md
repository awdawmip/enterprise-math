# R004 精度起源——补充 15：activation-aware typed generator basis

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + P023/A3/A4_BOUNDARY`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_14.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 14 已经把任意大的 future syntax 压缩成“有限 typed generator basis + descent certificate”，但留下一个问题：究竟哪些 generators 真正必要？本补充对**carrier synthesis**给出精确有限答案，同时把它与**semantic reconstruction**分开，并证明何时 quotient-level algebraic reconstruction 可以让 generator 在不重新跑 carrier compiler 的情况下被安全删除。

set cover/hitting set、有限 semigroup 的最小 generating set、term generation、semiring generation 都是成熟先行数学。R004 当前只保留 activation-aware 的 typed Representation Compiler 放置、有限 reduction/counterexample 与 cross-domain bridge。

## 1. 两种不同的 basis

设完整 generator set 为 `G`，initial observation 为 `P_0`，完整 language 编译得到

`Q* = Compile_G(P_0)`。

### Carrier basis

若 `S subset G` 满足

`Compile_S(P_0)=Q*`，

则称 `S` 为 **carrier basis**。它只负责保留足以强迫同一个 safe carrier 的 distinctions。

### Semantic reconstruction basis

若 `S` 上 descended generators 可以通过声明的合法 reconstruction rules——operation term/composition、semiring polynomial、semantic factor map 或其他有明确 certificate 的 quotient-natural rule——重建所有未来要求的 descended generators，则称 `S` 为 **semantic reconstruction basis**。

carrier 相同不等于 semantics 相同。若两状态的 `P_0` 已经 discrete，一个未来要求的 swap operation 对 carrier 完全没有 refinement 作用，所以 empty set 可以是 carrier basis；但 swap 无法由 free identity term 重建，因此 semantic basis 仍必须保留它。

所以 compiler 必须返回 basis 的**类型与证书**，不能只返回一个最小 generator 数。

## 2. R004-COMP-T23——forbidden-world hitting-set theorem

定义全部 forbidden coarse worlds：

`U(P_0,Q*) = { P : Q* strict refine P and P refine P_0 }`。

对 generator `g` 和 candidate partition `P`，定义整数 kill bit：

`kappa_g(P)=1` 当且仅当 `g` 在 `P` 上不 stable，否则为 `0`。

因为 `Q*` 对完整 `G` stable，所以对任意 subset `S` 也 stable。因此 `S` 保持同一 target carrier，当且仅当不存在比 `Q*` 更粗的 `S`-stable refinement。

等价地：

`S 是 carrier basis`

当且仅当

`对每个 P in U(P_0,Q*), sum_(g in S) kappa_g(P) >= 1`。

所以 exact carrier-basis synthesis 是一个关于**forbidden partitions**的有限 hitting-set，而不是关于单独 state pairs 的问题。

证明：若某个 forbidden `P` 没被任何 selected generator 杀掉，则 `P` 对 `S` stable，故 `S` compiler 的最粗 stable refinement 不可能等于严格更细的 `Q*`。反之若每个 forbidden `P` 都被杀掉，则任何 refine `P_0` 且不比 `Q*` 更细的 `S`-stable partition 只能是 `Q*`；而 `Q*` 自己对 `S` stable，所以它就是最粗结果。

对 3-state 的所有 initial partitions、3 个 total unary generators 的所有测试族与全部 retained subsets 做独立穷举，共 **117,000** 个 subset/compiler cases；fresh subset compilation 与 hitting condition 全部一致。

## 3. R004-COMP-CE14——只检查 pairwise merge 不够

一个很诱人的 shortcut 是：只检查 final classes 是否能“单独合并一对”。这是错误的。

取

`P_0={{0,1,2},{3}}`

以及 unary operation

`f: 0->1, 1->2, 2->0, 3->3`。

再加入 splitter `h=(3,1,2,3)` 后，完整 `{f,h}` 会把 `P_0` 编译到 discrete partition。

现在只保留 `f`。

在 discrete target 与 `P_0` 之间，每一个只合并 `0,1,2` 中某一对的 3-block candidate 都**不是** `f`-stable。所以仅做 pairwise local test 会误判为“所有单对 merger 都已经被杀掉”。

但更粗的

`{{0,1,2},{3}}`

整体本身却是 `f`-stable，`f`-only compiler 会直接停在这里。

因此 local pair separation 不能识别 global minimal carrier。除非额外结构定理证明可以缩小 certificate，否则 forbidden-world universe 必须包含 multi-class mergers。

## 4. R004-COMP-T24——inclusion-minimal 与纯整数最优性证书

设 `S` 已经命中所有 forbidden worlds。

`S` inclusion-minimal 当且仅当：对每个 selected generator `g`，都存在一个 **private forbidden world** `P_g`，在 selected generators 中只有 `g` 能杀掉它。

若 `g` 没有 private world，那么删掉 `g` 后所有 forbidden worlds 仍被命中；反之 private world 会在删掉 `g` 时立即暴露。

进一步，若 `D subset U` 满足：任意 available generator 最多只能杀 `D` 中一个 world，则称 `D` 为 **generator-disjoint packing**。任何 carrier basis 至少需要 `|D|` 个 generators，因为 `D` 中每个 world 必须由不同 generator 杀掉。

所以若已有 carrier basis `S` 同时有 packing `D` 满足

`|S|=|D|`，

就得到完全整数化的 cardinality-optimal certificate。

补充 14 的 4-state ping-pong pair 对应 forbidden-world kill masks `1,1,1,2`；唯一 minimum carrier basis 为 `{f,g}`。取一个 `f`-private world 和一个 `g`-private world 就得到 size-2 generator-disjoint packing，因此无需任何 normalized weight 或 fractional dual variable 就能证明最优。

## 5. R004-COMP-CE15——contextual redundancy 不单调

不能只在 `P_0` 看一个 generator 是否“当前有作用”。

补充 14 的 4-state operation witness 中，`g` 单独不会改变 `P_0`，相对 empty language 看起来 carrier-redundant；但 `f` 一旦先改变 target geometry，`g` 马上变成 distinguishing，并成为最终 discrete carrier 所必需。

补充 13 的 3-state COUNT relation cascade 也有同样现象。

所以“把所有当前不产生 immediate refinement 的 generator 删除”是不 sound 的。hitting formulation 之所以 activation-aware，正是因为它在全部 forbidden coarse worlds 上评估 generator，包括只有其他 generator 先 refinement 后才会出现的 worlds。

## 6. R004-COMP-T25——quotient-natural reconstruction 推出 carrier redundancy

不过确实存在一大类 generator 可以不进入 hitting-set search 就安全删除。

设完整 `G` 编译得到 `Q*`，保留 `S subset G`。遗漏 generator `h` 在 `Q*` 上下降为 `h_bar`。

若存在 reconstruction rule `F`：

`h_bar = F((g_bar)_(g in S))`，

并且 `F` 对进一步 coarsening **natural**：只要某个更粗 quotient 对 retained generators 合法，那么“先应用 `F` 再 coarsen”与“先 coarsen retained generators 再应用 `F`”结果相同。

则 `h` 相对 `S` 必然 carrier-redundant。

证明：假设存在严格比 `Q*` 更粗的 partition `P` 对 `S` stable。它诱导 `Q*` 的进一步 quotient。coarsening-naturality 说明 reconstructed `h_bar` 对这个 quotient 也 compatible；由于 fine `h` 已对 `Q*` stable，于是 `h` 对 `P` 也 stable。若每个 omitted generator 都有这种 certificate，则任何 `S`-stable coarse world 同时也是 `G`-stable，这与 `Q*` 作为完整 language 的最粗 stable carrier 冲突。因此 `Compile_S(P_0)=Q*`。

这条 meta-rule 解释了：即使 reconstruction certificate 只有在 full carrier 编译完成后才发现，它仍然可以反过来用于删减 carrier synthesis generators。

## 7. R004-COMP-T26——total-operation specialization

对 total operations，普通 term evaluation 对 coarsening natural。

unary 情况下，只要所有 omitted quotient transformations 都落在 retained quotient transformations 与 identity 生成的 transformation monoid 中，retained subset 就自动保持同一个 carrier。

这比要求 fine-level generation 更强。一个 operation 可能在 fine world 完全不能由 retained operations 生成，却在 collapse 后变得可重建。

例：4 个 fine states，target partition 为 `{{0,1},{2,3}}`。within-block swap

`(0 1)(2 3)`

显然不是 fine identity；但它在 quotient 上下降后就是 identity。因此它可以由 quotient 的 free identity term 重建，对当前 task 同时 semantic-redundant 与 carrier-redundant。

对 3-state、3-operation families 共检查 **102,375** 个 retained-subset 情形。其中 **43,940** 个满足“全部 omitted quotient maps 属于 retained quotient transformation monoid”；这 43,940 个 subsets 全部编译出相同 target carrier。

## 8. R004-COMP-T27——semiring relation specialization

对 semiring-valued relation generators，Supplement 14 的 block-sum quotient homomorphism 保证 semiring polynomials 对 coarsening natural。

因此若 omitted relation 对 `Q*` stable，且它的 quotient matrix 落在 retained quotient matrices 生成的 semiring subalgebra 中，则该 omitted relation carrier-redundant。

证明同样通过 descent：任意对 retained matrices stable 的更粗 `P`，会在 `Q*` relation algebra 上诱导稳定 quotient；semiring polynomial reconstruction 在那里仍 stable，再利用 omitted fine relation 的 `Q*`-stability，即可推出它在 `P` 上 stable。

3-state Boolean MAY relations 上检查 **20,480** 个 two-generator / initial-partition cases。其中 **1,560** 个满足 omitted quotient relation 属于 retained Boolean relation semiring；这 1,560 个 retained languages 全部保持原最终 carrier。

COUNT -> MAY 这类 semantic factor map 更强：强 channel stable 在每个 partition 上都推出弱 channel stable，所以 dominated channel 可在 pre-compile 阶段就删除，并在输出时通过 factor map 重建。

## 9. R004-COMP-T28——carrier basis 可以严格小于 semantic basis

在上述 coarsening-natural reconstruction 范围内，任意 semantic reconstruction basis 自动也是 carrier basis。因此 derived minimum sizes 满足

`b_carrier <= b_semantic`。

可以严格不等。两状态 initial observation 若已经 discrete，一个 requested swap 对 carrier 不增加任何 distinction，所以 empty set 是 carrier basis；但 swap 不在 free identity transformation monoid 中，因此 reconstruction basis 必须保留 swap：

`b_carrier=0`, `b_semantic=1`。

这只是 derived cardinality 关系。补充 13 已经证明相同 class/basis count 不代表相同 typed information，所以 compiler 应输出实际 basis、recipes 和 certificates，而不是只输出数字。

## 10. Activation-aware basis compiler pipeline

当前 exact finite pipeline：

1. 用完整 declared typed generator set 编译 `Q*`；
2. 先做 context-independent dominance：semantic factor map、fine-level operation-term generation、fine-level semiring generation；
3. 在 `Q*` 上继续寻找 quotient-level coarsening-natural reconstruction certificates；
4. 从 carrier search 中删掉所有有 reconstruction certificate 的 generators；
5. 对剩余部分构造 forbidden coarse worlds 与整数 kill matrix；
6. 解 residual hitting-set，得到一个或全部 minimum carrier bases；
7. 输出 private forbidden-world witnesses，并在可得时给 generator-disjoint packing lower bound；
8. 另外选择 semantic reconstruction basis，并给所有 future generators 输出明确 quotient reconstruction recipes。

reference module 用 exact bit masks 与完整 finite set-partition enumeration，只是研究 reference，不声称大规模可扩展。Bell-number growth 本身就是下一 frontier 要找 structured forbidden-world certificate、而不是继续扩大 brute-force optimizer 的原因。

## 11. Prior art 边界

有限 semigroup / transformation semigroup 的 minimum generating set / rank 是成熟研究主题。generic hitting set/set cover、algebraic term generation、semiring generation 也都是标准问题。

R004 只主张更窄的 project-local package：task-relative carrier preservation 的 forbidden-partition reduction、activation-aware no-go、carrier/semantic basis 分离、coarsening-natural reconstruction criterion，以及它们在既有 typed future-language compiler 后面的组合位置。

历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 12. Validation 与下一 frontier

committed regressions 覆盖 4-state optimality certificate、contextual redundancy、pairwise-merge no-go、carrier/semantic strict gap 与 quotient-only operation reconstruction。

独立验证还包括：**117,000** 个 hitting-characterization cases；**102,375 / 43,940** 个 unary quotient-reconstruction audit；以及 **20,480 / 1,560** 个 Boolean-relation reconstruction audit。

这里不宣称 fresh full-repository CI 或 canonical-main 状态。

下一问题已经被压得很窄：

> 能否不枚举所有 forbidden coarse partitions，而从 typed algebra 自身导出更小的 **structural obstruction basis**，同时保持 exact？

pairwise-merge counterexample 已经证明任意 local pair tests 不够。因此任何 forbidden-world universe 的压缩，都必须有 theorem 说明它隐式覆盖了哪些 larger mergers。
