# Exact Weighted Trace 的 Minimal Linear Predictive State

状态：`RESEARCH BRIDGE / NONCANONICAL`

Discrete quotient 不是唯一可能的 exact state representation。一旦 declared future language 被限制为 linear terminal weighted traces，已经恢复出的 exact weighted branching machine 往往还能进一步压成更低维的 rational predictive state。

这不是继续 split/merge partition，而是**改变 representation type**。

## 1. Exact weighted branching machine

假设已经得到一个 finite exact weighted quotient，共有 b 个 discrete quotient states、integer action matrices

`B_a in Z^(b x b)`，

以及 current observation rows

`C in Z^(c_0 x b)`。

对 literal word w，terminal weighted outputs 是：

`C B_w`。

全部 infinite trace language 因此由 rational row space 控制：

`W = span_Q { C B_w : all words w }`。

## 2. Finite invariant row-space closure

从 C 的 rows 出发，不断加入它们右乘每个 action matrix 后的 rows。

若某一步 rational rank 不再增长，则当前 row space 已对全部 actions invariant，任何 longer word 都不会增加新的 trace direction。

在 b 个 quotient states、initial observation rank 为 c_0 时，strict rank growth 最多发生：

`b-c_0`

次。

令

`r=dim_Q W`。

从生成出的 integer word rows 中选一个 integer row basis：

`R in Z^(r x b)`。

## 3. Induced predictive actions

因为 W action-invariant，对每个 action a 都存在唯一 rational matrix：

`T_a in Q^(r x r)`

使

`R B_a = T_a R`。

current observation rows 也属于 W，所以存在 rational decoder：

`H in Q^(c_0 x r)`

满足

`C = H R`。

对 discrete quotient source j，定义 predictive state：

`s_j = R e_j in Q^r`。

则

`s -> T_a s`

就是 exact predictive update，而

`output = H s`

就是 exact current output。

## 4. Exact word theorem

对任意 source j 与任意 word w：

`R B_w e_j = T_w R e_j`，

因此：

`C B_w e_j = H T_w s_j`。

所以 r-dimensional predictive machine 精确再现所有 terminal weighted word traces。

owner helper 同时验证 predictive-state intertwining 与 emitted observation equality，而不是只比较 final partition。

## 5. 在线性 predictive representation 中的最小性

设另一个 linear state map

`S:Q^b -> Q^d`

也足以表示同一完整 terminal trace language，即每个 row `C B_w` 都 factor through S。

那么所有 `C B_w` 都属于 S 的 row span，因此：

`W subseteq rowspan(S)`，

从而：

`r=dim W <= rank(S) <= d`。

所以 r 是 declared trace language 在 Q 上任何**线性** predictive representation 的最小可能维数。

这是一个真正的 minimal-state theorem，但只在明确声明的 linear representation class 内成立。

## 6. Linear quotient 不是 set partition

映射

`R:Q^b -> Q^r`

实际上把整个 vector state space quotient by unobservable linear subspace：

`N = intersection_w ker(C B_w)`。

它的 kernel 是 vector subspace，不只是“把若干 discrete basis states 合并”的 equivalence relation。

两个 raw states trace-equivalent，当且仅当它们的 basis vectors 得到相同 predictive vector；但 linear quotient 还能紧凑表示任意 superpositions / weighted distributions。

这就是为什么 linear predictive dimension 可以远小于 trace-distinct discrete source class 数量。

## 7. Sharp weighted-fan dimension witness

取十个 source states `x_1,...,x_10` 和一个 terminal state z，present observation 全部相同。

唯一 action 有 weighted edges：

`x_i -> z`，weight=i，

z 没有 outgoing edge。

exact weighted branching 第一轮就得到11个不同 states，因为 local weights 分别是 `1,...,10,0`。

terminal traces 也区分全部11个 sources：

- empty word 给出共同 current observation；
- 一步 action 给出 `1,...,10,0`。

但完整 trace row space 只由两条 rows 张成：

`(1,1,...,1)`

与

`(1,2,...,10,0)`。

所以：

`b=11`，

而

`r=2`。

11 个 exact source states 在一个二维 predictive space 中变成 `(1,i)` 型不同 vectors。

这精确证明：discrete state-class count 与 algebraic state dimension 是两个不同 precision resources。

## 8. Count-correlation witness

在此前 exact-count branch-correlation world 中：

- exact weighted branching 有6个 discrete behavioural classes；
- p/q 在 branching level 必须分离，因为 successor future-count grouping 不同；
- terminal count traces 却合并 p/q；
- invariant trace row space 的 rational rank 只有4。

于是同一个 world 同时出现：

`branching discrete state size = 6`

与

`linear terminal predictive dimension = 4`。

这是 continuation debt 在线性表示层的对应物：较弱 future semantics 允许不同且更小的 state type。

## 9. 与 trace-equivalence partition 的关系

每个 quotient basis state j 得到 predictive vector `R e_j`。

这些 vectors 相等，当且仅当对应 sources 的所有 terminal linear traces 相等，因为 R 张成完整 future observation row space。

因此 ordinary terminal trace-equivalence partition 可以作为 predictive-state map 的 equality fibers 恢复。

但保留 vector 本身是一种更强的 representation technology：它还能对 weighted distributions 做 exact linear evolution。

## 10. 与 bounded local-law reflection 的组合

上一代已经证明：small finite local code 可以恢复 exact integer weighted quotient machine。

这些 exact action matrices 一旦恢复，linear predictive compiler 后续只消费：

- exact quotient matrices `B_a`；
- quotient observation rows C。

不再需要原始 raw relation。

branch 会把 mod3-reflected primitive weighted machine 与直接 exact matrices 交叉比较，得到完全相同的 row-space closure、predictive action matrices 与 observation decoder。

因此完整 pipeline 是：

`bounded local code`

`-> exact local reflection`

`-> exact weighted branching machine`

`-> minimal linear predictive trace state`。

## 11. 三种不同 state 概念已经显式分离

### Branching / compositional state

保留足够 structure，使 weighted relation interface 本身能在 successor state classes 上执行。

### Terminal answer partition

只保留“哪些 discrete source states 给出相同完整 terminal answers”。

### Linear predictive state

一个最小维线性 representation，可以继续 evolution 并生成完整 terminal trace language。

三者满足不同 future-language contract，不能用一个 scalar “precision level” 排序完毕。

## 12. Representation tradeoff

从 b 个 discrete branching states 改成 r 个 linear coordinates 可以减少 structural dimension，但会把信息转移到 exact coordinate values 与 rational transition matrices 中。

weighted fan 把这个 tradeoff 做得很 sharp：任意多 distinct source values 都可以塞进二维 coordinates，因为其中一个 coordinate 承担不断变化的 integer weight。

因此：

`fewer state dimensions`

并不推出

`less numeric range`。

这与此前“更丰富 compositional structure 可以降低直接 arithmetic modulus”正好形成对偶。State dimension、coefficient range、branching correlation 与 execution interface 是不同资源。

## 13. Prior-art boundary

Weighted automata minimization、observability subspace、linear realization、Krylov space 与 Hankel-rank 型 state compression 都是标准既有数学/CS。这里不主张 generic novelty。

Enterprise Math 在本 Draft 中得到的 precision routing 是：

> **exact local dynamics 一旦恢复，最小 future state 取决于 declared representation class 与 future language；trace-only linear semantics 可以需要比任何 discrete branching quotient 更低维的 state type。**

## Owner-local assets

- `src/enterprise_math/linear_predictive_state.py`；
- `tests/test_linear_predictive_state.py`；
- `docs/PRECISION_LINEAR_PREDICTIVE_STATE.{en,zh}.md`。

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。