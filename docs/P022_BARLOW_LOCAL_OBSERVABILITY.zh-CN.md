# P022 — 两个连续 Coordination Shell 精确恢复当前隐藏 Drift 状态

状态：`ACTIVE RESEARCH NOTE / EXACT TWO-STEP OBSERVABILITY / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：Barlow coordination shell-energy 恒等式  
交叉价值：P018 kernel-time / predictive depth；P023/P024 history-sensitive quotient sufficiency

## 1. 从完整历史收缩到局部可观测深度

coordination history 已证明完整序列

\[
(S_0,S_1,\ldots,S_n)
\]

能恢复每个 radius 的无序 absolute drift pair

\[
P_q=\{|\delta_q|,|\delta_{-q}|\}.
\]

这里进一步问：只为恢复**当前** `P_n`，究竟需要多少最近 observation？

结论是统一最小深度恰好为 2。

## 2. 单个 shell 只给 quadratic energy

写

\[
P_n=\{a,b\},\qquad a,b\ge0.
\]

coordination 恒等式

\[
4S_n=42n^2+8-a^2-b^2
\]

说明单个 shell 等价于

\[
\boxed{Q_n=a^2+b^2.}
\]

radius 7 已有

\[
50=1^2+7^2=5^2+5^2,
\]

故单独 `S_7` 不足以恢复隐藏 pair。

## 3. 相邻 energy 的线性 shadow

从 `n-1` 到 `n`，每一侧 absolute drift 只会按 reflected ±1 规则变化。故

\[
Q_{n-1}-Q_n
=2+2(\epsilon a+\eta b)
\]

其中

\[
\epsilon,\eta\in\{-1,+1\}.
\]

定义

\[
\boxed{
L=\frac{Q_{n-1}-Q_n-2}{2},
}
\]

则

\[
\boxed{L=\pm a\pm b.}
\]

## 4. P022-LO01 — 两个连续 energy 唯一恢复当前无序 pair

已知

\[
Q=a^2+b^2,\qquad L=\pm a\pm b.
\]

### `L^2>Q`

差值满足 `(a-b)^2<=Q`，故此时必为

\[
|L|=a+b.
\]

于是

\[
2ab=L^2-Q.
\]

sum 与 product 唯一恢复 `{a,b}`。

### `L^2<Q`

和满足 `(a+b)^2>=Q`，故此时必为

\[
|L|=|a-b|.
\]

于是

\[
2ab=Q-L^2,
\qquad
(a+b)^2=2Q-L^2.
\]

再次唯一恢复两个整数根。

### `L^2=Q`

此时

\[
2ab=0,
\]

故一项为 0，另一项为 `sqrt(Q)`。

因此

\[
\boxed{(Q_{n-1},Q_n)\Longrightarrow\{a,b\}.}
\]

## 5. P022-LO02 — 两个连续 shell cardinalities 足够

radius 是查询上下文，每个 `S_q` 都精确恢复 `Q_q`，所以

\[
\boxed{
(S_{n-1},S_n)
\Longrightarrow
\{|\delta_n|,|\delta_{-n}|\}.
}
\]

将这个局部 decoder 对每个 `n` 独立应用，即可用宽度 2 的滑动窗口恢复整条无序 drift trajectory。

## 6. P022-LO03 — 统一状态 observability depth 恰好为 2

深度 1 在 radius 7 由 sum-of-two-squares collision 失败；深度 2 由 LO01 对全部合法状态成立。因此

\[
\boxed{d_{obs}=2.}
\]

这比“历史有帮助”更强：当前隐藏状态所需的历史长度是有限、统一而且最小的。

## 7. 与 future horizon 分离

`(S_{n-1},S_n)` 只足够恢复当前 extreme hidden pair `P_n`。

整个 radius-`n` geodesic statistic `T_n` 仍可能读取所有 heights `1,...,n` 的 drift。因此必须区分：

- **current-state observability depth**：2；
- **declared future functional 的 horizon**：可能一直延伸到 `n`。

局部状态可观测并不意味着全局 future query 只需局部历史。

## 8. 精度意义

同一个“memory”至少要拆成：

1. terminal observation；
2. 恢复当前 hidden state 所需的 local depth；
3. future functional 实际读取的总 horizon。

P022 在这里给出一个完全整数、有限的实例：

\[
1<d_{obs}=2\ll n
\]

仍可与长 horizon future query 共存。

## 9. 可执行验证

- `src/enterprise_math/p022_barlow_local_observability.py`；
- `tests/test_p022_barlow_local_observability.py`。

测试覆盖 radius 24 以内所有合法两通道 absolute transitions，并对长度 6 以内全部 microscopic two-sided windows 比较局部 decoder、直接 hidden trajectory 与早期递归 history decoder。