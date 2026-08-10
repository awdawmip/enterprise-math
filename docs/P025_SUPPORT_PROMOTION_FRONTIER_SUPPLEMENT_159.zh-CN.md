# P025 补充 159 —— State repair 与 action promotion 构成 Pareto frontier

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-state-support-stage155`

## 1. Support-growth layers

设 Stage156 的严格 predecessor-expansion layers 为

\[
Q^{(0)}\subsetneq Q^{(1)}\subsetneq\cdots\subsetneq Q^{(h)}=\downarrow Q,
\]

其中 `h` 是 Stage157 的 support horizon。

选择 promotion depth `t`：

- `Q^(t)` 中的 actions executable；
- `Q^(t)` 外 helpers 不属于该 subsystem 的 executable actions；
- 当 `t<h` 时，为了解释 `Q^(t)` actions，而让下一 hidden layer 保持 static，Stage155 需要 state support `Q^(t+1)`；
- 当 `t=h` 时 action family 已 predecessor-closed，因此 state 与 action support 相同。

所以定义

\[
A_t=Q^{(t)}
\]

以及

\[
R_t=
\begin{cases}
Q^{(t+1)},&t<h,\\
Q^{(h)},&t=h.
\end{cases}
\]

## 2. 三资源 cost vector

每个 promotion depth 的 structural cost 为

\[
\boxed{
C_t=
\left(
|A_t|,
|R_t|,
h-t
\right).
}
\]

三个坐标分别表示：

1. subsystem 中包含多少 executable helper actions；
2. 为解释这些 actions 需要保留多少 helper state coordinates；
3. 距离 fully autonomous closed action subsystem 还剩多少 predecessor-promotion rounds。

## 3. 每个 strict layer 都 nondominated

随着 `t` 增大：

- `|A_t|` 在 strict support-growth layer 上严格增加；
- `|R_t|` 单调不减，并通常增加；
- remaining horizon `h-t` 严格减少。

所以更深 promotion 只有通过支付更多 executable-action / state-support resources，才能购买更少 future closure obligation。

不存在一个点能在三个 minimization coordinates 上同时支配另一个点：

\[
\boxed{
\{C_0,\ldots,C_h\}
\text{ 构成 Pareto frontier}.}
\]

若没有 external workload/cost criterion，就不存在 scalar `best support level`。

## 4. Perfect binary exact frontiers

对一个最高 pre-output action：

### 八元 compiler

\[
\boxed{(1,3,1),\ (3,3,0).}
\]

### 十六元 compiler

\[
\boxed{(1,3,2),\ (3,7,1),\ (7,7,0).}
\]

### 三十二元 compiler

\[
\boxed{
(1,3,3),\ (3,7,2),\ (7,15,1),\ (15,15,0).
}
\]

第一个点保持极小 executable action language，但留下较多 closure obligation；最后一个点支付完整 autonomous dependency support，remaining horizon 为零。

## 5. Precision 解释

同一 dependency system 因而允许一整条合法 implementation/future contracts：

- **state-heavy / action-light** —— 保存 hidden prerequisite status，但不允许其 executable；
- **mixed** —— 部分 prerequisite layers executable，更深层保持 static state；
- **fully autonomous** —— 全部 dependency actions 纳入，support closed。

这不是同一个 operation language 的普通编码差异：它们声明了不同的 future freedom。

## 6. 与此前 Pareto 结果的关系

Stages94–95 研究 semantically equivalent coordinate charts 在 storage/update costs 下的不可比较；Stage159 不同：这里沿 frontier 改变的是 **future operation envelope 本身**，尽管 raw intent 都可以从同一个 top action 起源。

所以 action freedom 与 support precision 是耦合的 Pareto resources。

## 7. 前人工作边界

multiobjective/Pareto optimization 与 dependency-layer promotion 都属于经典对象。这里不主张 generic novelty。P025 提供 exact support-promotion specialization 与 future-relative precision interpretation。
