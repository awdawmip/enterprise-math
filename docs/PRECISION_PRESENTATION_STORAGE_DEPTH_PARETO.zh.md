# Exact Presentation 的 Storage / Execution-Depth Pareto

状态：`RESEARCH BRIDGE / NONCANONICAL`

一旦 future law 已被 exact 恢复，“到底要把多少 derived rules 预先存下来”就变成新的 precision resource 问题。预计算更多 transition rules 不会增加 semantic law，却可以减少 future execution depth。

本文在 literal macro-table representation class 内把这一 tradeoff 精确化，并与 readout / state / presentation 三层区分连接起来。

## 1. Generator presentation

固定一个 exact state representation，dimension 为 b，并有 k 个 named generator actions，其 exact transition matrices 为：

`B_a`。

最小 literal generator presentation 只存这 k 个 matrices。

长度 h 的 word

`w=a_1...a_h`

需要连续执行 h 次 generator applications。

storage 小，但 execution depth 随 word length 增长。

## 2. d-macro presentation

选择 macro depth `d>=1`。

预存所有长度1到d的 literal action words 对应的 exact transition matrix：

`B_w`。

这些 macros 不是新的 physical/world rules；每个都能由 generators exact composition 得到。

stored literal macro rules 数量为：

`S(k,d)=sum_(i=1)^d k^i`。

当 `k>1`：

`S(k,d)=k(k^d-1)/(k-1)`。

当 `k=1`：

`S(1,d)=d`。

## 3. Exact execution-depth law

任意长度 h 的 word 都可以切成连续 chunks，每个 chunk 长度至多 d。

因此只需：

`D(h,d)=ceil(h/d)`

次 stored macro transitions 即可完成 execution。

executable layer 使用 noncommuting matrices 验证该公式，所以不依赖 action commutativity。

## 4. Pareto endpoints

### Generator endpoint

`d=1`：

- stored rules = k；
- length-h word execution blocks = h。

### Full-horizon macro endpoint

`d=h`：

- stored rules = `sum_(i=1)^h k^i`；
- execution blocks =1。

对 `k>1`，这是用 exponential literal-table storage 换 linear execution depth。

两个 endpoint 都不 universally superior。

## 5. Nondominated macro depths

storage 随 d 严格增加，但 `ceil(h/d)` 只在某些 threshold 才下降。

若增加 d 却没有减少 worst-case execution blocks，那么新的 depth 在 literal macro-table class 中被更小 d 支配。

例如 `k=2`, `h=12`，nondominated macro depths 为：

`d = 1,2,3,4,6,12`。

对应：

`stored rules = 2,6,14,30,126,8190`，

`execution blocks = 12,6,4,3,2,1`。

这给出一个 concrete exact storage/depth frontier。

## 6. Semantic redundancy 与 execution value 必须分开

每个 macro matrix 对 exact generators 来说都 semantic redundant：

`B_w`

可以重新由 generator matrices 计算出来。

但若 execution depth / latency 是资源，stored macro 并不 operationally redundant。

这与 transitive rule table 的结构完全同类：某条 rule 不增加 closure law，却能减少 inference/execution rounds。

因此要分开：

- **semantic basis minimality**；
- **execution presentation efficiency**。

## 7. Reusable transition macro 与 terminal answer table 不同

对每个 word w，可以存两种对象：

### Transition macro

`B_w`。

它更新 state，并支持后续 arbitrary continuation。

### Terminal readout row

`C B_w`。

它能直接回答 w 的 terminal query，但本身不保留 arbitrary suffix execution 所需 successor state。

readout table 每个 word 可能存更少 scalars，但 contract 更弱。

这正是 readout vs executable-state distinction 在 presentation 层的对应。

## 8. Scalar storage model

若 state dimension 为 b，一个 literal transition matrix 有 `b^2` 个 scalar entries。

于是 d-macro transition table 存储：

`b^2 S(k,d)`

个 matrix scalars（尚未考虑 sparse/compressed encoding）。

若 current observation 有 c 个 output rows，full terminal readout table through horizon h 粗略存：

`c b S(k,h)`

个 scalars。

后者 per-word storage 可能更低，但 continuation 需要 reusable transition state 时不能替代前者。

这些是 representation-class counts，不是硬件 byte guarantee。

## 9. State dimension 与 macro depth 是正交两轴

上一代 linear-predictive result 可以把 b-state exact branching machine 压成 r-dimensional exact linear trace state。

若 macro transitions 存在 chosen state representation 中，同一个 macro-depth law 继续成立，而 matrix storage 随 state dimension 平方缩放：

`branching macro storage ~ b^2 S(k,d)`；

`linear predictive macro storage ~ r^2 S(k,d)`。

因此两种 optimization 可以组合：

1. 先减少 state representation dimension/type；
2. 再预存更长 macros 来减少 execution rounds。

二者不能混成一个参数。

## 10. 二维 presentation Pareto surface

一个 exact presentation 因此可以用类似

`(state representation, macro depth)`

的 coordinates 表示。

改变 state representation，会改变每条 stored rule 的 cost。

改变 macro depth，会改变 stored rule 数量和 runtime composition 数量。

同一个 future law 可以在这张 surface 上有很多 exact points，而 semantic truth 不变。

## 11. 与 local-code precision 的关系

第三条独立轴是：一开始用什么 local coefficient code 恢复 generator matrices。

所以完整 pipeline 可以在以下资源间 trade：

- local observation / coding range；
- state representation size/type；
- stored macro depth；
- runtime execution depth。

让 task 更快并不只有“增加 direct numeric precision”一种办法；还可以保留 structure 或预计算 derived transitions。

## 12. 与 Stage131 型 transitive rule table 的关系

当前 theorem 是 storing transitive closure rules 的 dynamic presentation analogue：

- small generator/basis table：stored law primitives 少，但需要 repeated execution；
- dense closure/macro table：存 derivable rules，减少 execution rounds。

不同 representation 的 exact numeric formula 会不同，但 resource principle 相同：

`semantic redundancy can buy execution-depth reduction`。

## 13. Representation-class boundary

本文**不是**对所有 possible program/circuit representations 的 global lower bound。

一个具体 action semigroup 还可能存在：

- algebraic relations；
- normal forms；
- repeated-squaring strategies；
- DAG/circuit sharing；
- sparse matrices；
- symmetry compression；
- specialized hardware execution。

这些都可能支配 literal table。

本文只拥有 declared literal macro-table class 内的 exact Pareto。

## 14. Foundation consequence

“minimal rule set”与“best exact presentation”是两个不同问题。

semantically minimal generator set 可能是 execution-poor presentation；当 depth/latency 本身是资源时，更 dense 的 exact presentation 反而更优。

因此 presentation precision 至少要按

`storage × execution depth × state representation × numeric range`

评价，而不能只看 rule count。

## Owner-local assets

- `src/enterprise_math/presentation_storage_depth_pareto.py`；
- `tests/test_presentation_storage_depth_pareto.py`；
- `docs/PRECISION_PRESENTATION_STORAGE_DEPTH_PARETO.{en,zh}.md`。

## Prior art / status

Memoization、transition monoid、macro action、time-memory tradeoff 与 precomputation 都是标准既有数学/CS。项目特有价值是 explicit presentation-precision resource routing，以及 semantic redundancy 与 operational efficiency 的分离。

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。