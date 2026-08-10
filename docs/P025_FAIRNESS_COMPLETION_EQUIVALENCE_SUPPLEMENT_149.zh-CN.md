# P025 补充 149 —— 有限单调 helper run 中 weak fairness 与 completion 等价

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-fairness-stage147`

## 1. 范围

本补充严格限制在 Stages 144–148 的有限 one-shot helper process：

- 合法 states 是有限 dependency poset 的 ideals；
- completed helpers 永远不会重新变 incomplete；
- 每个 helper 最多 firing 一次；
- helper 一旦 enabled，就会持续 enabled 直到 firing；
- 使用标准 infinite-run fairness 语言时，把 terminal execution 用 terminal stutter 无限延长。

下面的结论不是 arbitrary transition systems 上的 generic theorem。

## 2. Completion 推出 weak fairness

若一条 execution 最终完成全部 helpers，那么每个 helper 都在某个有限时刻 firing。

特别地，任何从某时刻开始持续 enabled 的 helper 最终都会 firing。

所以每条 completing execution 都 weakly fair：

\[
\boxed{\text{completion}\Rightarrow\text{weak fairness}.}
\]

## 3. Weak fairness 推出 completion

取一条 weakly fair execution，若当前 ideal 非 terminal，则 complement 中存在一个极小 helper；它的全部 predecessors 已经完成，所以它 enabled。由于 completed helpers 与 prerequisites 单调保持，它会持续 enabled 直到 firing。

weak fairness 强制它最终 firing。未完成 helper 的有限数量减少一。归纳即可得到全部 helpers eventual completion。

所以

\[
\boxed{\text{weak fairness}\Rightarrow\text{completion}.}
\]

## 4. 精确 execution-class equality

合并两个方向：

\[
\boxed{
\{\text{weakly fair executions}\}
=
\{\text{eventually completing executions}\}.
}
\]

因此在这个特殊单调 process 中，weak fairness 既不是比 completion 更细的额外 hidden trace refinement，也不是一个较弱 surrogate；它精确选择 completing executions。

## 5. 对 future precision 的意义

Stage 147 已证明加入 weak fairness 会把 MUST-completion 从“所有 nonterminal states 为假”翻转成“全部 states 为真”。Stage 149 更精确地解释：fairness restriction 实际就是把 admissible execution family 限制为 completing runs。

因此 liveness assumptions 可以被视为 **future-path domain** 的组成部分，与 Stage 138/142 的 hidden-state legality domain 对应。

## 6. 边界

该等价依赖 finiteness、monotone one-shot actions 以及 enabledness persistence。存在 reset、reversible actions、recurring events，或者 enabledness 会在 firing 前消失的系统中，不应直接推广。

## 7. 前人工作边界

weak fairness 与 finite progress arguments 都属于标准 concurrency theory。这里不主张 generic novelty。P025 只提供当前 precision testbed 内的 exact scoped identification。
