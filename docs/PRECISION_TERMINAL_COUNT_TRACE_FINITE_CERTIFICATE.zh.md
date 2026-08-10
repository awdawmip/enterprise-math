# Infinite Terminal Path-Count Trace 的有限 Certificate

状态：`RESEARCH BRIDGE / NONCANONICAL`

Exact natural terminal path-count traces 会随着长 word 持续增长，但对一个固定 finite-state relation system，完整 infinite trace language 仍然存在有限 exact certificate。

这个 certificate 使用两类资源：

1. 由 rational observability closure 给出的 finite word-depth bound；
2. 在该 depth 以前足够反射全部 count values 的 finite coefficient modulus。

这与 exact count-branching state 明显不同：branching state 的 coefficient cutoff 只依赖 one-step outdegree，不需要追随 accumulated trace range 增长。

## 1. Terminal path count 的 linear form

固定 n 个 states 的顺序，把每个 relation action a 写成整数 adjacency matrix：

`A_a[target,source]=1[source R_a target]`。

对每个 current observation class，令 C 含有对应 indicator row。

Literal word w 的 terminal observation path-count rows 就是：

`C A_w`

（若 matrix composition 与文字 word 顺序相反，只是记号 convention，不影响全部 words 的集合）。

因此完整 terminal count language 是 initial basis-state vector 上的一族 integer linear observations。

## 2. Rational row-space closure

定义：

`W_h = span_Q { C A_w : |w|<=h }`。

则：

`W_(h+1)=W_h + sum_a W_h A_a`。

如果某一层满足：

`dim W_(h+1)=dim W_h`，

那么 `W_h` 已对全部 action matrices right-invariant，之后任何更长 word 都不能增加 row space。

所以一次 equal-rank step 就是 permanent rational stop certificate。

## 3. Universal finite word-depth bound

Observation-class indicator rows 线性独立。若 current observation 有 `c_0` 个 classes，则：

`dim W_0=c_0`。

在 stabilization 以前，每个 strict horizon 至少让 rational rank 增加1，而 ambient state dimension 只有 n。

因此：

`h_* <= n-c_0`。

所以任意 infinite exact terminal trace distinction，都已经存在一个长度不超过 `n-c_0` 的 witness word。

这是 multi-relation weighted automaton 的 finite-dimensional observability closure。

## 4. Horizon bound 可以 sharp

取 n-state deterministic countdown chain，最后一个 state 是 absorbing terminal。

Current observation 只区分：

- terminal；
- nonterminal。

因此 `c_0=2`。

每多看一层 future action，就精确多揭示一个 distance-to-terminal layer。Rational row ranks 依次为：

`2,3,4,...,n`，

所以 stabilization 恰好发生在：

`h_*=n-2=n-c_0`。

因此 finite-depth theorem 并不是一个毫无约束力的 dimension upper bound。

## 5. Final row basis 决定 infinite exact trace partition

Row space stabilized 后，取任意一组 rationally independent integer rows 作为 basis。

两个 source states x,y 对**所有 literal words**拥有完全相同 exact natural terminal traces，当且仅当每一个 basis row 在 x/y 两个坐标上的值都相同。

因此 infinite exact trace partition 可以直接由一个 finite final row basis 编译。

Executable branch 会把这个 partition 与 certified horizon 内的 literal exact path-count traces 直接交叉验证。

## 6. Actual closure horizon 上的 finite arithmetic certificate

令 Delta 为 maximum raw one-step outdegree。

长度 k 的 word 从一个 source 出发最多有：

`Delta^k`

条 raw paths。

所以到 actual closure horizon `h_*` 为止，需要读取的所有 terminal observation counts 都落在：

`[0,max(1,Delta^h_*)]`。

任选：

`M > max(1,Delta^h_*)`，

mod-M 在这些 exact count values 上 injective。

因此：

`h_* 以内的 mod-M terminal traces`

与

`全部 infinite exact natural terminal traces`

诱导完全相同的 state partition。

这就是 infinite trace language 的 finite exact certificate。

## 7. 只用 state-count 数据的 universal certificate

若不先计算 actual closure horizon，可以直接使用：

`h_* <= n-c_0`。

于是 safe uniform modulus 可以取：

`M > max(1,Delta^(n-c_0))`。

配合 word depth `n-c_0`，它对给定 finite state count、observation class count 与 outdegree bound 的全部 relation systems，都能 certify infinite exact terminal count equivalence。

这是 worst-case theorem bound，不一定是某个固定 world 的 realized minimum。

## 8. Realized minimum modulus 可以更小

对一个固定 world，即使某些 individual path-count coefficients modulo M 发生 collision，也可能仍然得到正确 exact state partition。

真正有害的只有那些会把 exact trace 必须区分的 states 合并掉的 collisions。

因为 theorem modulus 保证有效，所以 branch 可以从 modulus2 开始有限搜索，返回第一个使 `h_*` 内 terminal trace partition 与 infinite exact partition 相同的 modulus。

因此需要区分：

- coefficient-value reflection bound；
- realized state-precision modulus。

后者可以严格更小。

## 9. 固定 branching-versus-trace witness 再解释

之前 Delta=2 的 acyclic world 具有：

- exact count-branching cutoff：mod3；
- exact terminal trace rational row-space stabilization：`h_*=2`；
- safe terminal coefficient cutoff：mod5。

Exact terminal counts 用：

`a^2: 4 versus 1`

拆开 p/q。

mod3 把4与1合并，因此即使 mod3 branching state 已经 exact，mod3 terminal traces 仍然错误。

mod5 能反射这两个 count values，并在 horizon2 恢复完整 infinite exact terminal trace partition。

所以同一个 fixed world 里可以同时有：

`branching state exact at M=3`，

而

`direct terminal trace certificate uses M=5`。

## 10. Structural memory 可以替代 arithmetic range

Branching state 递归保存：哪些 successor behavioural types 出现，以及每种 type 有多少 one-step successors。

它的 local coefficients 永远不超过 Delta。

Terminal trace 则把这种 structure 擦掉，并沿 future steps 累积 path multiplicity。在 finite-dimensional row space closure 以前，coefficient values 可以达到 `Delta^h`。

所以 recursive structural state 可以用更有组织的 memory structure 换取更小的 arithmetic range。

这不是 generic compression slogan，而是两个 declared interfaces 上的 exact theorem。

## 11. 与 N-semimodule non-Noetherian boundary 的关系

此前 unipotent path-count example 已经说明：literal natural-count 的**positive reconstructive semimodule** 可能永远持续出现新 generators。

这不与当前 finite state-equivalence theorem 矛盾。

Rational row-space closure 只问：完整 count language 最终能区分哪些 initial states。

Positive N-semimodule 则问：所有 future count rows 是否能由一个 finite basis 通过 nonnegative integer combinations 重构。

因此至少要分开三件事：

- finite exact state-equivalence trace certificate；
- finite rational / integer-linear envelope；
- finite positive-semimodule reconstructive basis。

第一项可以 finite，而第三项仍然 infinite。

## 12. Prior-art boundary

Weighted automata equivalence、rational invariant subspace、observability matrix 与 path-count bounds 都是标准既有数学 / CS。A4 保留 relation / witness ownership；P023/A2 保留 future-signature precision ownership。

这里的项目价值是 exact resource theorem：

> **固定 finite relation system 的 infinite exact terminal path-count state partition 拥有 finite depth × finite modulus certificate；但所需 arithmetic range 可能随 trace depth 增长，而 branching-state exactness 只需要 one-step outdegree precision。**