# Independent Readout Join 与 Compositional Interface Join

状态：`RESEARCH BRIDGE / NONCANONICAL`

两个 semantic capabilities 至少有两种不同的组合方式。仅仅同时保留两个 final coarse labels，比要求两个 operations 在同一个 shared quotient state space 上继续执行更弱。

这个区别精确解释了 semiring-product generation 中看似矛盾的两句话：product representation 对第一种 task 可能过精细，但对第二种 task 又恰好是 canonical coarsest repair。

## 1. 一个 K-valued relation interface

固定 finite state set、initial observation partition E_0、relation family 与 coefficient semiring K。

相对于 current partition E，action a 对每个 target E-class C 赋予 weight：

`(# raw a-successors in C) * 1_K`。

当同一 E-class 内的 sources 对每个 action、每个**当前 E-target class**拥有相同 K-weight vector 时，K-interface 才能在 E 上 descend。

反复按这些 vectors split，就得到 E_0 内唯一的 coarsest K-stable refinement。

它的 fixed-point sequence 与 recursive K-branching signature kernels 完全相同。

## 2. Independent readout join

假设两个 declared tasks 分别要求 coefficient interfaces K 与 L。

先各自计算 coarsest stable quotients：

`E_K`, `E_L`。

如果唯一要求只是：

> 从 current state representation 中，分别恢复 final K-label 与 final L-label，

那么 coarsest state partition 只是：

`J = E_K intersect E_L`，

即普通 joint refinement / kernel intersection。

这里**不**要求 K 或 L 的 transition interface 在 J 上继续 executable。

这是一种 **readout join**。

## 3. 为什么 readout join 会重新破坏 operation safety

Safe operation capability 对 raw state refinement 不是 monotone 的。

某个 operation 可能在 E_K 上 stable，是因为若干 target states 仍处于同一个 K-class。用 L 进一步 split 这些 targets 后，原先的 K-class 被拆开。两个 source states 过去向旧 class 发送相同 K-weight，但现在可能在新的 joint classes 之间分布不同。

因此，即便 K 在 E_K 上 safe，也可能在

`J=E_K intersect E_L`

上重新变 unsafe。

L 同理。

这正是 semantic-precision 路线中 generic safe-operation nonmonotonicity 在 multivalued weighted relation 内部的具体实例。

## 4. Shared compositional join

更强的 task 要求：

> 在一个 common quotient state space 上，K 与 L 两套 transition interfaces 都保持 directly executable，而且 later futures 能从同一个 coarse successor state 继续运行。

那么 partition 必须相对于它**自己的 target classes**同时对 K 与 L 的 coefficient weight vectors stable。

从 E_0 出发，同时按所有 K/L target-block weight vectors split 并迭代。

fixed point

`E_comp(K,L)`

就是同时支持两套 operations 的唯一 coarsest shared-state quotient。

即：

`E_comp(K,L) = Closure_(K,L)(E_0)`。

## 5. 精确的 two-stage decomposition

同一个 final quotient 也可以按三步得到：

1. 分别计算 E_K、E_L；
2. 取 readout join J；
3. 在 J 上再次按 joint K,L operation requirement 做 closure。

于是：

`E_comp(K,L) = Closure_(K,L)(J)`。

这把两种资源拆开：

- **static label join**：为了同时恢复两个 interface labels 需要的 state distinctions；
- **compositional closure**：由于另一套 capability 已经拆开 target classes，为了让两套 interfaces 在新 partition 上继续 safe 而额外需要的 distinctions。

## 6. Compositional closure debt

定义：

`debt_blocks`

为

`#blocks(E_comp) - #blocks(J)`。

同时记录从 J 开始直到 fixed point 的 strict refinement rounds。

它们不是 universal complexity measure，但精确量化一个 task-relative precision tax：

> 仅仅因为两个 capabilities 必须在同一个 successor state space 上继续组合执行，需要额外增加多少 state precision？

Debt=0 表示 independent readout join 已经对 full capability family operation-safe。

Debt>0 表示 cross-capability target refinement 重新激活了 hidden transition differences。

## 7. Product semiring theorem

对 semirings K 与 L，一个 current target block 在 product semiring 中的 weight 精确就是：

`(K-weight, L-weight)`。

所以同一个 current partition 上：

一轮 simultaneous K,L refinement

精确等于

一轮 `(K x L)` refinement。

归纳以后，完整 fixed-point sequences 也相同：

`E_comp(K,L) = E_(K x L)`。

因此 direct product semiring 是**coupled shared-state operation interface** 的 canonical coarsest coefficient representation。

这与 parent generation 的 product-overprecision witness 不矛盾，因为 parent 比较的是更弱的 independent-readout task。

## 8. Sharp Boolean + parity debt witness

使用 parent 的 eight-state coefficient-correlation fixture。

分别看：

- Boolean-support branching 得到 stable quotient E_B；
- mod2 parity branching 得到 stable quotient E_2；
- 两者各自都保持 source states p/q 等价。

普通 readout join J 也继续合并 p/q。

但 J 已经把若干 target states 按另一套 coefficient view 拆得更细。到了 J 上：

- p/q 在新的 target blocks 之间分配 Boolean support 的方式不同；
- parity weight 的分布方式也不同。

所以 J 已经不再对 required operations stable。

再做一轮 compositional repair 才把 p/q 拆开。

这个 fixture 中：

`debt_blocks=1`，

而 post-join closure 恰好需要1轮 strict refinement。

## 9. Morphism-ordered interfaces 的 debt 为0

若有 semiring homomorphism：

`phi:K->L`，

使 L 成为 K 的 coefficient quotient，那么在任何**同一个 partition**上，K-weight vectors 相等必然推出其 L-images 相等。

因此 K-stability 已经自动保证 L-stability。

于是：

- K-stable quotient refine L-stable quotient；
- independent readout join 就是 K quotient；
- 再加入 L capability 不会要求更多 shared-state refinement；
- compositional debt 精确为0。

Concrete examples：

`N -> Boolean`，

`N -> Z/MZ`。

所以 coefficient 上真正 richer 的 interface 可以无额外 interaction tax 地吸收自己的 morphic quotients。

## 10. 一个 dominating interface 可以吸收多项 capabilities

若 capability family 同时包含 exact N-count branching、Boolean support 与 mod-M count，那么 N 同时 homomorphically map 到后两者。

shared compositional join 因而直接等于 N-count stable quotient。

不需要因为同时声明 support / modular count 就额外保留新的 product correlation。

实际 compiler rule 可以写成：

> 在计算 shared-state join 前，先删除那些已经被某个 declared dominating coefficient interface factor 的 interfaces。

## 11. Semantic join 取决于 interface semantics

下面两句话没有矛盾：

`product can be overprecision`

以及

`product is the coarsest shared-state join`。

因为 task 发生了变化。

### Independent readout semantics

只要求分别得到两个 completed answers。

Minimal state kernel = 两个 answer kernels 的 intersection。

### Coupled compositional semantics

要求两套 transition structures 都在同一个 recursively reusable coarse successor state 上继续工作。

Minimal state = joint operation-congruence closure，也就是 product-semiring branching fixed point。

所以只说“join”是不完整的；必须说明 joined capabilities 的 futures 是否允许 cross-composition。

## 12. Architecture consequence

一个 representation 可以作为 static readout 已经 sufficient，却作为 compositional state 仍然 insufficient。

这个 pattern 在 Enterprise Math 中反复出现：

- scalar potential 能回答 current query，却不是 Markov continuation state；
- independently sufficient quotient labels 在 target partitions 被共同 refine 后可能重新失去 operation safety；
- product state 对 static task 可能 overretain correlation，但对 shared dynamic continuation 又可能正好成为必要 repair。

因此 state minimality 永远不能脱离 declared continuation interface。

## 13. Prior-art boundary

Congruence closure、weighted bisimulation、product semiring 与 partition refinement 都是标准既有数学 / CS。A4 保留 relation / witness ownership；P023/A2 保留 future-signature 与 semantic-precision ownership。

这里的项目价值是精确 routing principle：

> **independent output join 与 compositional state join 是不同 precision problems；二者之间的 gap 是由 cross-capability continuation 产生、可以精确计量的 closure debt。**