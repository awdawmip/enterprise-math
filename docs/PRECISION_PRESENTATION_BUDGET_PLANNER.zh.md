# Literal-Macro Presentation 的 Exact Budget Planner

状态：`RESEARCH BRIDGE / NONCANONICAL`

上一代给出了 forward map：

`macro depth d -> (stored rules, execution blocks)`。

本代反过来解决工程问题：给定 latency/depth budget 或 storage budget，在同一个 literal macro-table representation class 内选择真正 Pareto-efficient 的 exact presentation。

## 1. Forward laws

k 个 generator actions、macro depth d、declared word horizon h：

`S(k,d)=sum_(i=1)^d k^i`

条 stored literal transition macros，worst-case execution blocks 为：

`D(h,d)=ceil(h/d)`。

S 对 d 严格增加；D 对 d 单调不增但呈阶梯状。

## 2. Execution-depth budget -> 最少 storage

若最多允许 R 次 macro execution，则 exact condition 为：

`ceil(h/d)<=R`。

所以最小 feasible macro depth：

`d_min=max(1,ceil(h/R))`。

由于 S(k,d) 随 d 严格增加，该 d 同时给出满足 execution budget 的最小 stored rule count。

因此：

`B_rules_min(k,h,R)=S(k,ceil(h/R))`，

当 R>=h 时退化到 generator depth1。

## 3. Storage budget -> 最少 execution depth

给定 rule budget B，先求最大 affordable depth：

`d_max=max{d<=h:S(k,d)<=B}`。

它决定 best achievable runtime：

`R_min=ceil(h/d_max)`。

但 d_max 自己未必 Pareto-efficient，因为 D 可能在多个 d 上保持不变。

真正应该返回的是达到 R_min 的**最小** d：

`d_Pareto=ceil(h/R_min)`。

这样在 best runtime 下同时最小化 storage。

## 4. Sharp dominated-depth example

取 k=2,h=12,B=125。

预算可以负担 d=5：

`S(2,5)=62`。

但：

`D(12,5)=3`，

而 d=4 已经：

`D(12,4)=3`，

只需：

`S(2,4)=30`。

所以 d=5 被 d=4 storage-dominate。planner 正确返回 d=4、30 rules、3 rounds，而不是机械取最大 affordable d。

## 5. Horizon-only Pareto depth theorem

因为对任意 k>=1，S(k,d) 都随 d 严格增加，所以哪些 d 被支配只取决于 D(h,d)，与 k 无关。

完整 nondominated depth set 为：

`D_h={ceil(h/r): r=1,...,h}`。

k 只改变每个 depth 对应的 storage 高度，不改变哪些 depths 留在 Pareto frontier 上。

例如 h=12：

`D_h={1,2,3,4,6,12}`。

## 6. Frontier size 只有 O(sqrt(h))

因为：

`ceil(h/r)=floor((h-1)/r)+1`，

标准 distinct quotient 结构给出 O(sqrt(h)) 个不同 Pareto depths。

executable layer 使用一个简单 bound：

`|D_h| <= 2 floor(sqrt(h-1)) + 1`

（h>1）。

因此虽然候选 d 有 h 个，真正 nondominated 的 exact resource menu 远小于 h。

## 7. Dense scalar-storage budget

若 state dimension=b，一个 dense transition macro matrix 需要 b^2 个 scalars。

所以 scalar budget `B_s` 等价于 rule budget：

`floor(B_s/b^2)`。

同一个 inverse planner 随后给出 Pareto-optimal macro depth 与 execution count。

## 8. Same latency 下的 square storage law

达到 execution budget R 所需 macro depth 与 rule count 不依赖 state dimension，因此：

`B_scalar_min = b^2 S(k,ceil(h/R))`。

若 exact representation 从 dimension b 压成 r，则在**同样 latency target**下的 scalar storage 精确按：

`r^2/b^2`

缩放。

这把 state-representation axis 与 macro-depth axis 真正组合起来。

## 9. Same storage 下，state compression 可以购买 execution depth

固定 scalar budget，较小 state dimension 会让可负担的 rule count 增加，并可能跨过新的 macro-depth threshold。

例如 k=2,h=12,scalar budget=1000：

- dimension4：最多62 rules，Pareto plan 为 d=4、3 rounds、480 stored scalars；
- dimension2：最多250 rules，Pareto plan 为 d=6、2 rounds、504 stored scalars。

所以 exact state compression 能把同一个 memory ceiling 转换成更低 runtime depth。

## 10. Weighted-fan consequence

上一代 weighted fan 把 exact terminal-trace representation 从11个 discrete branching coordinates 改成2维 linear predictive coordinates。

对任意固定 literal-macro latency target，dense matrix storage 比例变成：

`2^2/11^2 = 4/121`。

这只适用于 terminal-linear task contract，不意味着2D representation 足以执行更强 branching interface。

## 11. Exact optimizer contract

executable layer 对 small k/h 与 frontier-adjacent budgets 做 brute-force 对照，锁住 planner 的 lexicographic Pareto 目标：

1. storage budget 下先最小化 execution blocks；
2. execution blocks 相同，再最小化 stored rules。

这样不会偷偷返回 dominated presentation。

## 12. Representation-class boundary

全部公式只对 literal contiguous-macro table class exact。

Binary-power macros、addition chains、algebraic normal forms、circuits、shared DAGs 会产生不同 frontier。下一代直接压力测试这个边界。

## Owner-local assets

- `presentation_budget_planner.py` / tests；
- `presentation_budget_frontier.py` / tests；
- `PRECISION_PRESENTATION_BUDGET_PLANNER.{en,zh}.md`。

## Prior art / status

Time-memory tradeoff、inverse resource planning 与 divisor-quotient frontier compression 都是标准既有数学/CS。项目价值是 exact inverse compiler 及其与 semantic state-representation cost 的组合。

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。