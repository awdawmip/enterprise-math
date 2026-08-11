# Prefix Semantic Ladder 的 Information Decomposition

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Terminal / discovery / timing quotients 删除的是不同 semantic distinctions。对 uniform literal-word workload，exact quotient fibers 可以把这条 hierarchy 变成 exact Shannon-information decomposition。

对长度 H、k 个 generator labels 的 word：

`literal provenance -> full timing -> discovery order -> terminal set`。

Total literal information 精确分解成 terminal-state information，加三项 quotient increment：first-discovery order、discovery timing 与 stutter action provenance。

## 1. Uniform literal workload

令 W 在 `k^H` 个 exact length-H literal words 上 uniform。

则：

`H(W)=H log2 k`。

对任意 deterministic quotient Q，给定 semantic class q 后，literal words 在该 fiber 内仍然 uniform。因此：

`H(W)=H(Q)+E[log2 |fiber(Q)|]`。

这个 identity 把 exact fiber formulas 直接变成 semantic information budgets。

## 2. Entropy ladder

记：

- `H_T`：terminal-set entropy；
- `H_D`：discovery-order entropy；
- `H_P`：full prefix-timing entropy；
- `H_L`：literal-word entropy。

由于每一层都是上一层的 deterministic quotient：

`H_T <= H_D <= H_P <= H_L`。

Branch 从 exact quotient fibers 独立计算每一项，并在 bounded parameter grids 上验证完整 chain rule。

## 3. Terminal-set entropy

Terminal support size=s 时：

- terminal classes 数：`C(k,s)`；
- 每个 class literal fiber：`s! S(H,s)`。

所以每个此类 terminal class probability：

`s! S(H,s)/k^H`。

对 s 求 Shannon sum 得 exact `H_T`。

## 4. Discovery-order entropy

Discovery length=s 时：

- order classes 数：`P(k,s)`；
- 每个 class literal fiber：`S(H,s)`。

所以每个 order class probability：

`S(H,s)/k^H`。

由此得到 exact `H_D`。

## 5. Exact first-discovery order information

条件在实际使用 exactly S=s 个 distinct generators。

一个 terminal set 下面恰有 `s!` 个 discovery orders，而且每个 order 的 literal fiber 都同样是 `S(H,s)`。

所以恢复 first-appearance order 所增加的 conditional information 精确是：

`log2(s!)` bits。

对随机 distinct-generator count S 取平均：

`H_D-H_T=E[log2(S!)]`。

Branch 独立计算右侧并与 direct entropy gap 对照。

## 6. Duration information

固定一个 s-generator discovery order。

Positive duration composition：

`r=(r_1,...,r_s)`

的 literal fiber 是：

`f(r)=product_i i^(r_i-1)`。

该 discovery order 总 literal fiber 是 `S(H,s)`，所以 induced duration probability：

`P(r|S=s,order)=f(r)/S(H,s)`。

这个 duration distribution 的 conditional Shannon entropy，正是 order 已知以后恢复 discovery **何时发生**所增加的信息。

对 S 平均：

`H_P-H_D=E[H(duration|S)]`。

Branch 用 positive compositions 精确枚举该 distribution 并验证 entropy identity。

## 7. Stutter-action provenance information

在一个 full-timing class r 内，剩余 literal ambiguity 是：每个 semantic stutter 实际执行了哪个 already-seen generator。

该 class 有 `f(r)` 个 literal words，所以 conditional provenance entropy 是：

`log2 f(r)`。

对 timing classes 平均：

`H_L-H_P=E[log2 f(r)]`。

这正是 full prefix-state timing 仍然没有观察到的 action-label information。

## 8. Complete exact decomposition

组合三层 quotient increment：

`H_L`

`=H_T`

`+E[log2(S!)]`

`+E[H(duration|S)]`

`+E[log2 f(r)]`。

换句话说：

`literal action information`

`=terminal-set information`

`+first-discovery order information`

`+discovery-time information`

`+stutter-action provenance information`。

Executable report 从独立 formulas 计算全部 terms 后，以 tight floating tolerance assert 整个 chain。

## 9. Sharp k=2,H=2 witness

四个 equiprobable literal words：

`aa,ab,ba,bb`。

Literal entropy=2 bits。

Terminal semantics classes：

`{a}`, `{b}`, `{a,b}`

probabilities 分别 `1/4,1/4,1/2`，所以：

`H_T=1.5` bits。

Discovery order 会区分 `ab` 与 `ba`，因此：

`H_D=2` bits。

H=2 时没有额外 duration / stutter ambiguity，所以：

`H_P=H_L=2`。

整个0.5-bit terminal/discovery gap 精确等于：

`E[log2(S!)]=1/2`。

## 10. H 增大后 duration 与 provenance 分别变成正资源

k=2,H=3 时，可以有 same discovery order 但 different discovery times，也可以有 different literal stutter actions 共享同一 timing trace。

所以：

`H_P-H_D`

与

`H_L-H_P`

都会严格为正。

这给出 timing information 与 action provenance 是两个独立 semantic resources 的最小例子。

## 11. Conditional entropy 等于 quotient ambiguity

对每一层 semantic quotient Q：

`H(W|Q)=H_L-H(Q)`

精确等于 induced semantic workload 下 literal fiber size 的 expected logarithm。

所以 semantic quotient 同时可以理解成：

- state-space partition；
- declared workload 下的 exact expected ambiguity / information-loss channel。

第二种解释需要 workload distribution；quotient structure 自己不会自动给概率。

## 12. Semantic cardinality 与 semantic entropy 是不同资源

一个 layer 可以数学上允许很多 semantic classes，但实际 workload 可能高度集中在少数 classes。

因此：

`log2(number of classes)`

只是 worst-case index-size bound，不等于 workload 下的 Shannon information。

下一条 asymptotic generation 会用 long random words 压这个边界。

## 13. Stage131 consequence

Representation design 现在至少可以区分：

- worst-case semantic state count；
- workload 下 information-theoretic minimum average code length；
- representation 下仍保留的 exact quotient ambiguity；
- runtime decode / materialization cost。

Semantic quotient 对 class count 与 expected information 的压缩比例可以完全不同。

这对 semantic layer 确定后的 cache compression 与 workload-aware coding 尤其重要。

## Owner-local assets

- `src/enterprise_math/prefix_semantic_information_decomposition.py`；
- `tests/test_prefix_semantic_information_decomposition.py`；
- 本双语 theorem note。

## Prior-art / status

Shannon entropy、deterministic quotient chain rule、Stirling occupancy distribution 与 conditional entropy 都是标准既有 information theory / combinatorics。P023/A2 保留 future-signature / precision ownership。本文只拥有 prefix semantic-information decomposition specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
