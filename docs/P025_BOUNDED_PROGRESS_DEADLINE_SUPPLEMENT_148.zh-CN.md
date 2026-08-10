# P025 补充 148 —— Bounded progress 给出精确 completion deadline

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-fairness-stage147`

## 1. Quantitative scheduler contract

Stage 147 已区分 unrestricted scheduling 与定性的 weak fairness。若要得到有限 deadline，还需要显式更强的 quantitative contract。

对正整数 `B`，定义 **B-progress contract**：

> 只要 helper process 尚未 terminal，每连续 `B` 个 scheduler steps 内至少发生一次实际 helper firing。

其他 scheduler steps 可以 stutter。每次 helper firing 精确完成一个此前未完成的 helper。

这里故意使用清楚定义的 progress contract，而不是把所有标准 bounded-fairness 术语强行统一重命名。

## 2. 精确上界

设 ideal `I` 处仍未完成的 helper 数为

\[
r(I)=m-|I|,
\]

其中 `m` 是 helper 总数。

每至多 `B` 个 scheduler steps 至少完成一个 helper，所以经过至多

\[
Br(I)
\]

步后全部 remaining helpers 都已经 firing：

\[
\boxed{T_{max}(I;B)\le B\,r(I).}
\]

## 3. Sharpness

考虑如下 scheduler：只要 process 非 terminal，

1. 先 stutter `B-1` 步；
2. 第 `B` 步只触发一个 enabled helper；
3. 重复。

Stage 147 已保证每个 nonterminal ideal 至少存在一个 enabled helper。因此该 schedule 始终合法，并且每完成一个 helper 精确消耗 `B` 个 scheduler steps。

于是

\[
\boxed{T_{max}(I;B)=B\,(m-|I|).}
\]

这是 declared B-progress contract 下精确的 worst-case completion time。

## 4. State quotient 与 value precision

固定 `B` 后，deadline 只依赖 ideal cardinality。因此 deadline future 精确只有

\[
\boxed{m+1}
\]

个 state classes，与 Stage 146 的 remaining-helper-work future 完全相同。

改变 `B` 会改变数值保证，却**不会**细化 state partition：

\[
I\sim J
\iff
|I|=|J|.
\]

所以 liveness-contract strength 可以改变 **future value precision**，而不改变 **state precision**。

## 5. Qualitative 与 quantitative liveness

Stage 147 的 weak fairness 保证 eventual completion，但不给统一有限 time bound：持续 enabled action 在最终 firing 以前仍允许任意长的有限 delay。

B-progress contract 正好加入缺失的 quantitative resource，把 eventuality 升级成 sharp deadline。

因此

\[
\boxed{
\text{weak fairness}\Rightarrow\text{eventual completion},
\qquad
B\text{-progress}\Rightarrow\text{finite exact worst-case deadline}.
}
\]

## 6. 架构后果

scheduler contract 至少具有两条 precision 轴：

1. **qualitative liveness** —— 是否保证完成；
2. **quantitative progress** —— 保证多快完成。

两个 contracts 可以诱导同一个 state quotient，却返回不同强度的 quantitative guarantees。

## 7. 前人工作边界

bounded progress assumptions 与 worst-case progress-time bounds 都属于经典 scheduling/verification 思想。这里不主张 generic novelty。P025 提供 exact finite specialization 与 state/value precision separation。
