# P018 —— 有限精度证明演算：补充 15

状态：`ACTIVE RESEARCH NOTE`  
范围：kernel 新增事件、逐步 collision polynomial 增量、高阶历史首次合流计数、有限时间 telescoping  
依赖：P010、P011、P018-T129—T136  
纪律：二项式系数、生成函数与集合划分粗化属于成熟组合数学。本阶段研究的是它们如何精确连接 Pair/kernel 的逐时间事件与 P011 全部整数碰撞谱，不主张这些基础组合恒等式为原创。

---

## 1. Pair 层为什么还不够

Supplement 14 已经把 deterministic time 写成单调 kernel chain：

\[
K_0\subseteq K_1\subseteq K_2\subseteq\cdots,
\qquad
K_n=\kerpair(F^{[n]}).
\]

新增的二元 pair

\[
K_{n+1}\setminus K_n
\]

精确告诉我们“哪些历史对在第 `n+1` 步第一次变得不可区分”。

但 P011 的 collision polynomial

\[
K_F(t)=\sum_y\big((1+t)^{m_F(y)}-1\big)
\]

同时记录全部 `k` 元历史子集，而不只是二元 pair。

因此本阶段的问题是：

> 能否从一次 kernel partition 的确定性粗化，直接计算这一时刻新增的全部高阶 collision spectrum？

答案是肯定的，而且完全是有限整数公式。

---

## 2. 单个新 fiber 的旧块分解

设第 `n+1` 步的一个新 fiber `A` 由第 `n` 步的若干旧 fibers 合并而成：

\[
A=A_1\sqcup\cdots\sqcup A_r,
\qquad
|A_i|=m_i,
\]

总大小为

\[
M=\sum_{i=1}^r m_i.
\]

旧 partition 中，这些块对 collision polynomial 的贡献为

\[
\sum_{i=1}^r\big((1+t)^{m_i}-1\big).
\]

新 partition 中，合并后的贡献为

\[
(1+t)^M-1.
\]

---

## 3. P018-T137 —— 单个 fiber merge 的精确时间增量

状态：`PROVED / EXECUTABLE`

定义该合并在这一时刻新产生的 collision polynomial：

\[
\boxed{
\Delta_A(t)
=
(1+t)^M-1
-
\sum_{i=1}^r\big((1+t)^{m_i}-1\big).
}
\]

其 `t^k` 系数为

\[
\boxed{
[t^k]\Delta_A(t)
=
\binom{M}{k}
-
\sum_{i=1}^r\binom{m_i}{k}.
}
\]

### 组合解释

`C(M,k)` 统计新 fiber `A` 内全部 `k` 元历史子集。

其中已经在旧时刻发生 collision 的，是完全落在某个单独旧 fiber `A_i` 内的子集，总数为

\[
\sum_i\binom{m_i}{k}.
\]

因此差值恰好统计：

> 在第 `n+1` 步第一次被同一个新 fiber 包含、并且跨越至少两个旧 fibers 的 `k` 元历史子集。

所以 P011 的谱增量不只是“最终 fiber 大小之差”，而可以逐时间步解释为**新发生的高阶不可区分事件数**。

---

## 4. P018-T138 —— 二阶系数就是当步新进入 kernel 的历史对数

状态：`PROVED / EXECUTABLE`

取 `k=2`：

\[
[t^2]\Delta_A(t)
=
\binom{M}{2}
-
\sum_i\binom{m_i}{2}.
\]

由基本恒等式：

\[
\boxed{
[t^2]\Delta_A(t)
=
\sum_{1\le i<j\le r}m_i m_j.
}
\]

右侧正是从不同旧 fibers 各取一个历史的 unordered pairs 数。

这些 pair 在第 `n` 步仍不在 kernel 中，在第 `n+1` 步第一次进入同一新 fiber，因此：

\[
\boxed{
[t^2]\Delta_A(t)
=
\#\{\text{当步新进入 diagonal/kernel 的历史对}\}.
}
\]

这第一次把 Supplement 12 的 Pair/kernel 底层与 P011 二阶 collision observable 做成精确逐事件同一对象，而不是概念类比。

---

## 5. P018-T139 —— 一般 `k` 阶系数是高阶 kernel-event 的直接推广

状态：`PROVED STRUCTURAL INTERPRETATION`

对任意 `k≥2`，

\[
[t^k]\Delta_A(t)
\]

统计的不是 pair，而是第 `n+1` 步第一次被新 partition 视为单一 collision class 的 `k` 元历史子集。

因此可以定义时间分辨的高阶事件计数：

\[
\boxed{
E_{n+1,k}
:=J_k(F^{[n+1]})-J_k(F^{[n]}).
}
\]

则

\[
E_{n+1,k}\ge0,
\]

且它由所有新 fibers 的上述 binomial differences 求和得到。

Pair/kernel 是 `k=2` 的最弱关系底座，而 P011 的全部 `J_k` 是同一 partition-coarsening 过程的高阶组合提升。

---

## 6. P018-T140 —— 整个时间步的 polynomial 增量是所有新 fibers 增量之和

状态：`PROVED / EXECUTABLE`

设第 `n+1` 步的新 fibers 为 `B`，每个 `B` 都是若干旧 fibers 的并。

定义

\[
\Delta_{n+1}(t)
:=
K_{F^{[n+1]}}(t)-K_{F^{[n]}}(t).
\]

则严格有

\[
\boxed{
\Delta_{n+1}(t)
=
\sum_B\Delta_B(t).
}
\]

且

\[
\boxed{
\Delta_{n+1}(t)\in\mathbb N[t].
}
\]

所以 P011 coefficientwise monotonicity 可以被强化为：

> 每个时间步的非负整数增量都有明确的“这一时刻新形成的高阶历史 collision”解释。

---

## 7. P018-T141 —— 时间增量严格 telescoping

状态：`PROVED / EXECUTABLE`

对任意有限时间 `N`：

\[
\boxed{
K_{F^{[N]}}(t)-K_{id}(t)
=
\sum_{n=0}^{N-1}\Delta_{n+1}(t).
}
\]

更一般地，对 `a<b`：

\[
\boxed{
K_{F^{[b]}}(t)-K_{F^{[a]}}(t)
=
\sum_{n=a}^{b-1}\Delta_{n+1}(t).
}
\]

这只是有限 telescoping，因此不需要极限或级数收敛。

结合 Supplement 14 的 finite saturation，在有限 observation set `H` 上取

\[
N_H=\max_{x\in H}s(x),
\]

得到：

\[
\boxed{
K_{S|_H}(t)-K_{id_H}(t)
=
\sum_{n=0}^{N_H-1}\Delta_{n+1,H}(t).
}
\]

因此最终 irreversibility spectrum 可以被精确拆成有限个逐时刻新增 collision events。

---

## 8. P018-T142 —— Pair time 与 P011 spectrum time 是同一 partition filtration 的不同阶观察量

状态：`PROVED SYNTHESIS`

现在可以把 P010/P011/P018 的关系写得更准确：

\[
\boxed{
K_0\subseteq K_1\subseteq\cdots
}
\]

是底层 kernel-pair filtration。

- `K_{n+1}\setminus K_n`：这一时刻新增的二元不可区分关系；
- `[t^2]\Delta_{n+1}`：新增 unordered pair collision 的数量；
- `[t^k]\Delta_{n+1}`：新增 `k` 元 collision 子集数量；
- `\Delta_{n+1}(t)`：把这一时刻所有阶的不可逆事件打包成一个整数多项式。

因此：

\[
\boxed{
\text{Pair/kernel filtration}
\longrightarrow
\text{time-resolved collision spectrum}
}
\]

不是额外假设，而是同一 finite partition coarsening 的组合提升。

---

## 9. 一个重要边界：多项式仍不是完整带标签历史

即使知道每一步全部 `\Delta_n(t)`，也未必能恢复究竟是哪几个具体历史发生合流；多项式记录 fiber sizes 与高阶计数，不保留全部标签信息。

所以必须区分：

1. **kernel relation / partition**：带标签的不可区分结构；
2. **collision polynomial**：对 fiber-size multiplicity 的高阶整数统计；
3. **逐步增量 polynomial**：每一时刻新增统计。

P011 已证明 collision polynomial 对 fiber-size multiset 完备，但并不对带标签 partition 完备。本阶段保持这个边界不变。

---

## 10. 可执行验证

新增：

- `src/enterprise_math/collision_increment.py`
- `tests/test_collision_increment.py`

压力测试包括：

1. 两 fiber merge 的二阶系数恢复 P011 的 `ab`；
2. 多 fiber merge 的二阶系数等于所有 cross-fiber pair 数 `Σ_{i<j}m_im_j`；
3. old polynomial + exact increment = new polynomial；
4. 多个新 fibers 的 step increment 等于整个 partition polynomial 差；
5. 没有实际 merge 时增量全零；
6. 所有增量系数非负；
7. 多时间步增量严格 telescoping 到最终 spectrum。

---

## 11. 对底层逻辑的进一步反哺

到 T142 为止，不可逆性层可以被组织为：

\[
\boxed{
\text{State Pair}
\to
\text{kernel filtration}
\to
\text{first coalescence time }\tau
\to
\text{time-resolved higher collision events}
\to
\text{finite stabilization spectrum}.
}
\]

这里没有一步需要先引入概率熵。

因此 P011 的 polynomial/spectrum 不再像一个后加的统计量；它可以被看成 Pair/kernel filtration 的高阶整数影像。

这支持一个更稳定的底层分工：

- Pair/kernel 保存**谁与谁**不可区分；
- `τ` 保存**什么时候**第一次不可区分；
- `J_k` / collision polynomial 保存**每一阶有多少组**历史变得不可区分。

三者分别对应 identity、time、multiplicity，不应互相替代。

---

## 12. 下一步

### P018-Q109 —— 是否存在完整的带标签高阶 kernel complex？

寻找比 collision polynomial 更强、但仍保持有限整数结构的对象，直接保存每个 `k` 元历史集合首次进入同一 fiber 的时间。

### P018-Q110 —— `τ` 与逐步二阶增量的精确分布

对有限 `H`，研究

\[
N_n=\#\{\{x,y\}:\tau_F(x,y)=n\}
\]

与 `[t^2]\Delta_n(t)` 的严格等价，并推广到 `k` 元首次共同合流时间。

### P018-Q111 —— 与 P017 certificate 的接口

研究 P017 的 global certificate 是否也能按“局部信息逐步汇聚但最终全局成立”的 filtration/collision 语言重新表达，前提是不削弱现有 prime-gap 路线。

---

## 13. 当前结论

Pair/kernel 层已经足以生成 P011 的完整时间分辨整数谱：

\[
\boxed{
[t^k]\Delta_{n+1}(t)
=
J_k(F^{[n+1]})-J_k(F^{[n]}),
}
\]

其中 `k=2` 精确等于这一时刻新进入 kernel 的 unordered history pairs 数。

在有限 observation set 上，这些非负 polynomial increments 经过有限步严格 telescoping 到 stabilization collision polynomial。

因此“不可逆性”现在有了一个完全有限的三重表达：

\[
\boxed{
\text{kernel：谁合流；}
\qquad
\tau：何时合流；
\qquad
\Delta K(t)：每阶有多少合流。}
\]
