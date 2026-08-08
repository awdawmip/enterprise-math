# P018 —— 有限精度证明演算：补充 05

状态：`ACTIVE RESEARCH NOTE`  
范围：predicate-specific conflict multiplicity、自适应多精度轴选择、有限整数 decision-cost 优化  
依赖：P018 第一到第五阶段  
纪律：decision tree 与 dynamic programming 都是成熟思想；P018 只研究它们在有限 precision observation 上的使用，不把一般算法据为原创。

## 1. 信息更多，不等于证明推进更多

第五阶段定义了 ambiguity multiplicity：

\[
A_\lambda(x)=|[x]_\lambda|,
\]

即当前 precision observation 后仍与 terminal state `x` 相容的状态数。

但证明通常只针对一个 predicate：

\[
P:X\to\{\mathrm{true},\mathrm{false}\}.
\]

一次 refinement 可能删掉很多与 `x` 在 `P` 上同真值的 terminal state，却一个都没有删掉真正可能推翻命题的状态。

所以 adaptive proof precision 需要一个 predicate-specific quantity。

定义 **predicate conflict fiber**：

\[
K_{\lambda,P}(x)
=
\{y\in[x]_\lambda:P(y)\ne P(x)\}
\]

以及 **conflict multiplicity**：

\[
\boxed{
C_{\lambda,P}(x)=|K_{\lambda,P}(x)|.
}
\]

它精确计算：当前仍相容、但对目标命题持相反真值的 terminal state 还有多少个。

## 2. P018-T45 —— Predicate certificate 当且仅当 conflict multiplicity 为零

状态：`PROVED`

对任意有限 precision observation：

\[
\boxed{
C_{\lambda,P}(x)=0
\iff
P\text{ 在 }[x]_\lambda\text{ 上常值}.
}
\]

因此

\[
\boxed{
C_{\lambda,P}(x)=0
\iff
\text{P018 predicate certificate 已为 TRUE 或 FALSE}.
}
\]

证明：conflict 为零，意味着 fiber 内不存在真值与 `P(x)` 相反的状态，所以整个 fiber 都与 `x` 同真值；反向显然。∎

因此 conflict multiplicity 是剩余**证明阻碍**的精确整数计数，而不只是剩余 state ambiguity。

## 3. P018-T46 —— Conflict multiplicity 随 refinement 单调不增

状态：`PROVED`

若 `mu` refine `lambda`，则

\[
[x]_\mu\subseteq[x]_\lambda.
\]

两边与 opposite-truth class 取交得到

\[
K_{\mu,P}(x)
\subseteq
K_{\lambda,P}(x).
\]

所以

\[
\boxed{
C_{\mu,P}(x)
\le
C_{\lambda,P}(x).
}
\]

一旦该量降到零，T45 与第五阶段的 certificate persistence 保证它以后永久保持为零。

## 4. P018-T47 —— 严格 conflict reduction 的充要条件

状态：`PROVED`

当 `mu` 比 `lambda` 更细时，下列条件等价：

1. `C_(mu,P)(x) < C_(lambda,P)(x)`；
2. fine fiber 至少移除了一个 opposite-truth terminal state；
3. 存在 `y` 满足

\[
O_\lambda(y)=O_\lambda(x),
\qquad
P(y)\ne P(x),
\]

但

\[
O_\mu(y)\ne O_\mu(x).
\]

所以对 `x` 来说，一次 refinement 真正具有 proof information，当且仅当它分开了当前相容的一个**反真值 witness**。

这比第五阶段的 ambiguity-drop 条件更严格；后者把所有相容状态的分离都算成信息。

## 5. P018-T48 —— Ambiguity gain 与 proof gain 可以相反

状态：`PROVED BY EXPLICIT COUNTEREXAMPLE`。

令

\[
X=\{x,t_1,t_2,t_3,f\},
\]

predicate 在 `x,t1,t2,t3` 上为 true，只在 `f` 上为 false。

从完全粗的 observation 开始，此时 `x` 的 fiber 含全部五个状态。

考虑两种 refinement。

### Refinement A —— 对证明有用

把 `f` 与四个 true state 分开。

对 `x`：

- ambiguity 从 `5` 降到 `4`，gain=`1`；
- conflict 从 `1` 降到 `0`，gain=`1`；
- predicate 已完全决定。

### Refinement B —— 对 ambiguity 很有用，对证明没用

把 `t1,t2,t3` 分到其他 fiber，但仍让 `x` 与 `f` 留在一起。

对 `x`：

- ambiguity 从 `5` 降到 `2`，gain=`3`；
- conflict 仍为 `1`，gain=`0`；
- predicate 仍是 UNRESOLVED。

所以

\[
\boxed{
\text{更大的 ambiguity reduction}
\not\Rightarrow
\text{更大的 proof progress}.
}
\]

因此“每次都选最能缩小 state fiber 的 precision step”不是正确的一般 adaptive proof rule。

## 6. P018-T49 —— Product precision 不会增加 predicate conflict

状态：`PROVED`

对 precision observations `O_1,...,O_m`，定义 joint observation：

\[
O_\times(x)
=
(O_1(x),\ldots,O_m(x)).
\]

它的 fiber 为

\[
[x]_\times
=
\bigcap_i[x]_i.
\]

所以 joint conflict fiber 包含于每一条单轴 conflict fiber：

\[
K_{\times,P}(x)
\subseteq
K_{i,P}(x).
\]

因此

\[
\boxed{
C_{\times,P}(x)
\le
\min_i C_{i,P}(x).
}
\]

所以组合不同 precision axis 不会让 predicate 变得更难决定。

## 7. P018-T50 —— Joint predicate completeness 判据

状态：`PROVED`

一族有限 observations 对 `P` **jointly predicate-complete**，当且仅当每个 joint observation fiber 都完全落在 `P` 的一个 truth class 内。

等价地，不存在真值相反的 `x,y`，却同时满足

\[
O_i(x)=O_i(y)
\]

对**所有**可用 observation `i` 成立。

再等价地：

\[
\boxed{
C_{\times,P}(x)=0
\quad\text{对所有 }x\in X.
}
\]

这就是：现有 precision axes 究竟是否包含足够信息来决定目标 predicate 的精确有限判据。

它可以在 joint observation 并不 state-injective 的情况下成立。

## 8. 整数 observation cost

给每个可用 observation `i` 指定正整数 cost：

\[
c_i\in\mathbb N_{>0}.
\]

cost 可以表示计算量、实验分辨率、需要检查的素因子数、内存、能量预算，或者其他任意有限项目资源。

P018 不要求把它转换为概率、对数或实值 utility。

## 9. P018-T51 —— 固定 target state 的最优 precision path：Bellman recurrence

状态：`PROVED FINITE RECURRENCE`。

固定实际 terminal state `x`，并设当前 compatible block `B` 包含 `x`。

设 `R` 为尚未使用的有限 observation 集合。

定义

\[
V_x(B,R)
\]

为使 `P` 在包含 `x` 的 compatible block 上变为常值所需的最小剩余整数 cost。

若 `P` 已经在 `B` 上常值：

\[
\boxed{V_x(B,R)=0.}
\]

否则，选择 observation `i` 后会观测到 `O_i(x)`，于是 compatible block 缩为

\[
B_i(x)
=
\{y\in B:O_i(y)=O_i(x)\}.
\]

因此

\[
\boxed{
V_x(B,R)
=
\min_{i\in R,\ B_i(x)\subsetneq B}
\left(
 c_i+V_x(B_i(x),R\setminus\{i\})
\right),
}
\]

若任何有限 sequence 都无法决定 predicate，则值未定义。

证明：任何 adaptive path 都有第一步 observation；取完第一步以后，对固定 terminal state 来说，只剩对应 observation value 的有限 sub-block。扣除第一步 cost 后，问题重新变成同类型的更小有限优化问题。对 `|R|` 做有限归纳即可。∎

所以在小型系统中，最佳 proof precision path 可以被**精确求解**。

## 10. P018-T52 —— 最优 worst-case 有限 decision tree

状态：`PROVED FINITE RECURRENCE`。

若实际 terminal state 事先未知，一个 observation 可能产生多个 possible child blocks。

对当前 block `B`，定义

\[
V(B,R)
\]

为对 `B` 中所有 terminal state 都决定 `P` 所需的最小**最坏情况**剩余整数 cost。

若 `P` 在 `B` 上常值，则

\[
V(B,R)=0.
\]

否则 observation `i` 把 `B` 分成非空 observation blocks

\[
\mathcal P_i(B).
\]

于是

\[
\boxed{
V(B,R)
=
\min_{i\in R}
\left[
 c_i+
 \max_{C\in\mathcal P_i(B)}
 V(C,R\setminus\{i\})
\right].
}
\]

不劈开 `B` 的无用 observation 可以忽略；若某个 child 永远无法决定，则该候选路径成本视为未定义/无穷。

这是一个完全不需要概率分布的 minimax decision tree，所有量都是有限整数。

## 11. P018-T53 —— Joint completeness 当且仅当存在有限 decision tree；并有 sum-cost 上界

状态：`PROVED`

设所有 observation cost 都是正整数。

若 joint observation 对 predicate 完备，那么顺序执行**全部** observation 最终一定能决定 `P`。因此有限 decision tree 一定存在，并且

\[
\boxed{
V(X,R)
\le
\sum_{i\in R}c_i.
}
\]

反过来，如果 joint observation 不 predicate-complete，那么必存在一对真值相反的 `x,y`，却共享所有 observation value。只使用这些 observations 的任何 decision tree 都永远无法把它们分开，所以不可能存在完整有限 decision tree。

因此

\[
\boxed{
\text{存在有限 decision tree}
\iff
\text{joint observation predicate-complete}.
}
\]

这是第五阶段 predicate completeness 的 adaptive 版本。

## 12. P018-T54 —— 最大 one-step conflict gain 不保证 total cost 最优

状态：`PROVED BY EXPLICIT COUNTEREXAMPLE`。

设

\[
X=\{x,f_1,f_2,f_3\},
\]

predicate 只在 `x` 上为 true。

可用 observation：

- `A`：一步直接把 `x` 与三个 false state 全部分开，cost=`5`；
- `B`：先移除 `f1,f2`，仍留下 `x,f3`，cost=`1`；
- `C`：移除 `f3`，并与 `B` 组合后完成证明，cost=`1`。

从完全粗的状态开始，`A` 的 immediate conflict reduction 最大：一步删掉全部三个 opposite-truth state。

但 adaptive path `B` 再 `C` 的总 cost 只有

\[
1+1=2<5.
\]

所以

\[
\boxed{
\text{最大 one-step conflict gain}
\not\Rightarrow
\text{最小 total proof cost}.
}
\]

同一例子中，最优 worst-case finite decision tree 的 cost 也是 `2`，而 greedy direct observation 的 cost 为 `5`。

因此 Stage 6 必须使用 T51–T52 的 Bellman recurrence，而不能宣称存在普遍正确的 greedy rule。

## 13. 现在 adaptive precision 有三个不同优化目标

### State ambiguity

降低

\[
A_\lambda(x).
\]

适合目标是识别 terminal state 本身的场景。

### Predicate conflict

降低

\[
C_{\lambda,P}(x).
\]

适合目标只是证明一个 predicate 的场景。

### Total decision cost

最小化

\[
V_x(B,R)
\quad\text{或}\quad
V(B,R)
\]

适合不同 precision operation 有不同整数成本、且可以自适应选择时。

这三个目标未必选择同一个下一步 precision。

这正是“精度本身参与数学”的一个重要推论：**证明过程可以选择下一步该提高哪一种精度。**

## 14. 与 scale precision / factor precision 的关系

### Scale precision

候选 refinement 可以继续劈开 unresolved numerical fiber。对 order/threshold predicate，conflict multiplicity 只计算那些仍可能跨过 decision boundary 的 subcell states。

### Factor precision

候选 factor cutoff 会排除那些因新出现 divisor witness 而与当前 survivor 不相容的 terminal state。对 primality，conflict multiplicity 追踪的是“到当前 factor horizon 仍伪装成 prime 的 composite survivor”。

### Product precision

scale 与 factor observation 可以作为 decision tree 中两种独立 action。其 joint fiber 是交集，所以 Bellman recurrence 可以比较：下一步提高哪条 precision axis 更值得。

这是 P018 第一次形式化“**改变精度的种类**”，而不只是提高同一种 precision 的数值。

## 15. 前人边界

finite decision tree、minimax recurrence 与 dynamic programming 都是成熟计算机科学/优化思想。P018 不声称 Bellman principle 或 decision-tree optimization 是新发明。

当前要检验的是：当 action 被具体替换成 Enterprise Math 已建立的 finite precision observations 后，它们能否形成有用的数学证明演算：

\[
\boxed{
\text{precision fiber}
+
\text{predicate conflict}
+
\text{persistent certificate}
+
\text{multi-axis observation}
+
\text{integer precision cost}
+
\text{exact finite optimal proof path}.
}
\]

整个构造不需要概率、entropy score 或无限精度完成。

这一组合的历史创新状态仍为 `NOVELTY_UNVERIFIED`。

## 16. 第六阶段状态

- P018-T45 conflict-zero certificate criterion：`PROVED`
- P018-T46 conflict monotonicity：`PROVED`
- P018-T47 strict conflict-reduction criterion：`PROVED`
- P018-T48 ambiguity gain != proof gain counterexample：`PROVED`
- P018-T49 product conflict bound：`PROVED`
- P018-T50 joint predicate-completeness criterion：`PROVED`
- P018-T51 optimal target-state precision recurrence：`PROVED`
- P018-T52 optimal worst-case decision-tree recurrence：`PROVED`
- P018-T53 completeness / finite-tree equivalence and cost bound：`PROVED`
- P018-T54 greedy nonoptimality counterexample：`PROVED`
- large-system complexity 与 approximation algorithm：`OPEN`
- adaptive P017 proof path（scale + factor + shell observations）：`NEXT`
- physically weighted precision cost：`OPEN / PHYSICAL MODEL REQUIRED`

可执行检查位于 `src/enterprise_math/adaptive_precision.py` 与 `tests/test_adaptive_precision.py`。
