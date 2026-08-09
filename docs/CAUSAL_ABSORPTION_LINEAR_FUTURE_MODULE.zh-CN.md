# 因果吞并 01 —— 从未来可区分性导出线性代数、深度几何与拓扑

状态：`CROSS-ROUTE RESEARCH WIP / EXACT INTEGER THEOREMS + EXECUTABLE REFERENCE`

归属说明：本文件在 A3 owner branch 上作为实验与证明来源。一般 future-compatible quotient 母理论仍归 A2/P023；若本文件结论去除 A3 背景后成立，应通过 Research Relay 上提，不在 A3 长期复制第二份母理论。

## 1. 纠偏目标

本阶段明确拒绝以下模式：

> 先承认传统线性空间、范数、拓扑为本体，再给它们附加一个 `precision` 标签。

这里反过来：

1. 原始对象只有显式整数状态；
2. 给出允许的未来操作；
3. 给出未来真正读取的整数观测；
4. 先问哪些状态差异在任意有限未来中仍可被区分；
5. 传统 `kernel / rank / observability / ultrametric / topology` 只在这套因果结构稳定后作为派生压缩语言出现。

因此传统工具不是 foundation，而是 **causal shadow / coordinate compression**。

## 2. 原始系统

状态：

\[
X=\mathbb Z^k.
\]

允许的有限操作族：

\[
\mathcal B=\{B_a\},
\qquad B_a\in\mathbb Z^{k\times k}.
\]

当前整数观测：

\[
W:\mathbb Z^k\to\mathbb Z^r.
\]

对操作词

\[
\omega=a_t\cdots a_1,
\]

记：

\[
B_\omega=B_{a_t}\cdots B_{a_1}.
\]

## 3. CA-01 —— 深度 `t` 的因果不可见 subgroup

定义：

\[
K_t
=
\left\{
\eta\in\mathbb Z^k:
WB_\omega\eta=0
\text{ 对所有 }|\omega|\le t
\right\}.
\]

于是：

\[
x\sim_t y
\iff
y-x\in K_t.
\]

解释不是“误差小于某个 epsilon”，而是：

> 在所有长度不超过 `t` 的允许未来实验中，`x` 与 `y` 给出完全相同的整数观测结果。

立即有：

\[
K_{t+1}\subseteq K_t.
\]

所以未来越长，可区分关系只会变细，不会重新把已经可区分状态合并。

## 4. CA-02 —— 未来观测拉回

令 `V_t` 为所有

\[
wB_\omega,
\qquad w\text{ 为 }W\text{ 的观测行},
\qquad |\omega|\le t
\]

在 `Q^k` 中生成的 row span。

则：

\[
\boxed{K_t=\mathbb Z^k\cap V_t^\perp.}
\]

因此传统的 row span / kernel 在这里不是原始定义，而是因果可区分性的一个精确计算压缩。

若 `V_{t+1}=V_t`，则 `V_t` 已在所有右作用 `v\mapsto vB_a` 下稳定，所以任意更长操作词都不会产生新的观测方向。

因此：

\[
\boxed{V_{t+1}=V_t\Longrightarrow K_{t+j}=K_t\quad\forall j\ge0.}
\]

## 5. CA-03 —— 无限整数状态上的有限稳定

每个 `K_t` 都是 `Z^k` 的 saturated subgroup：若 `n\eta in K_t` 且 `n!=0`，由全部观测为整数线性映射可得 `eta in K_t`。

若：

\[
K_{t+1}\subsetneq K_t,
\]

则两个 saturated subgroups 不可能具有相同 rank；否则它们拥有相同 rational span，而较小者 saturated 会迫使两者相等。

所以每次严格细化都使 invisible rank 至少下降 1。

于是：

\[
\boxed{
\text{严格 future-refinement 次数}\le k.
}
\]

这点很关键：

> 状态空间 `Z^k` 是无限的，但因果可区分 closure 仍在有限整数 rank 内稳定。

它不是靠截断状态盒子，也不是靠连续极限。

## 6. CA-04 —— 因果维数吞并传统 rank

稳定后记：

\[
K_*=\bigcap_{t\ge0}K_t.
\]

定义：

\[
\boxed{
\dim_{\rm causal}(X;\mathcal B,W)
=
\operatorname{rank}(\mathbb Z^k/K_*).
}
\]

等价地，它就是稳定 future-visible row span 的 rank。

解释：

> 因果维数 = 这组未来任务最终真正能够独立区分的整数自由度数。

所以 ambient coordinate 数 `k` 不再自动等于有效维数。

传统 `rank` 被重新定位为因果结构稳定以后的一种计数定理，而不是先验空间属性。

### 极端例子

若未来观测最终能恢复所有 `k` 个独立方向：

\[
\dim_{causal}=k.
\]

若无论未来怎样演化都只看得到一个总和：

\[
\dim_{causal}=1.
\]

这里没有先声明“精度是一维”；是一整套未来 operation language 自己把其余方向变成不可区分。

## 7. CA-05 —— 传统 observability matrix 的地位反转

传统做法可以把：

\[
W,\ WB,\ WB^2,\ldots
\]

纵向排列成某种 observability matrix。

在本体系里，这个矩阵不再是理论起点。

真正起点是：

\[
\boxed{
\text{所有允许未来是否能区分 }x,y?
}
\]

矩阵只是把未来拉回当前以后的一张有限坐标表。

因此：

\[
\boxed{
\text{observability rank}
=
\text{causal distinguishability rank}.
}
\]

这是“吞并”的第一例：传统线性系统工具保留其算法价值，但本体解释被 future distinguishability 取代。

## 8. CA-06 —— 整数因果 agreement depth

不把 `distance` 作为 primitive。

定义第一次可区分深度：

\[
s(x,y)
=
\min\{t:x\not\sim_t y\},
\]

若：

\[
x\sim_t y\quad\forall t,
\]

则记：

\[
s(x,y)=\infty.
\]

`s` 越大，表示两个状态必须等待更深的未来才能区分。

因为每个 `~_t` 都是等价关系，所以若：

\[
s(x,y)\ge m,
\qquad
s(y,z)\ge m,
\]

则：

\[
s(x,z)\ge m.
\]

故：

\[
\boxed{
s(x,z)\ge\min(s(x,y),s(y,z)).
}
\]

这是纯整数的 non-Archimedean similarity law。

若传统数学希望把它重新编码成某个 ultrametric，可以选择任意严格递减数值编码；但该实值 ultrametric 只是后生成表示，不是基础几何。

## 9. CA-07 —— 因果过滤层自动生成拓扑

对每个深度 `t` 和状态 `x` 定义：

\[
U_t(x)=[x]_{\sim_t}.
\]

由于：

\[
\sim_{t+1}\subseteq\sim_t,
\]

任意两个这类 equivalence classes 若相交，较细层的 class 必包含在较粗层 class 中。

所以：

\[
\mathcal B_{causal}
=
\{U_t(x):x\in X,t\ge0\}
\]

构成一套拓扑基。

而每个 `U_t(x)` 又是 clopen：其补集是同一 `t` 层其他 equivalence classes 的并。

因此传统 topological neighborhood 不需要先给定：

\[
\boxed{
\text{neighborhood}
=
\text{在某个有限未来深度仍不可区分的状态集合}.
}
\]

## 10. CA-08 —— T0 quotient 就是稳定未来等价 quotient

在上述 causal-depth topology 中，两个状态拥有完全相同的全部 basis neighborhoods，当且仅当：

\[
x\sim_t y\quad\forall t.
\]

也就是：

\[
y-x\in K_*.
\]

所以 topological indistinguishability 恰等于 stable future indistinguishability。

因此该拓扑的 Kolmogorov/T0 quotient 不是另一个额外操作，而正是：

\[
\boxed{
X/\sim_*.
}
\]

在线性整数情形，就是：

\[
\boxed{
\mathbb Z^k/K_*.
}
\]

这给“拓扑被因果理论吞掉”一个非常直接的意义：

> T0 分离不是额外公理；它等价于把所有永远无法被未来区分的状态先坍缩掉。

## 11. 与 P012 的关系：传统 metric 已有一个吞并先例

P012 已经做对了一件关键事情：

\[
d_G(x,y)
=
\text{primitive operation graph 上的最短整数步数}.
\]

也就是说，`L1` 并不是先验范数，而是在标准 unit-step operation family 下导出的 closed form。

本文件提出另一类因果几何：

- P012 `word/path cost` 问“从 `x` 实际走到 `y` 最少需要几步”；
- 本文件 `agreement depth` 问“需要多深的未来才能把 `x,y` 区分开”。

二者都是从 operation language 派生，而不是先接受传统 metric ontology。

它们当前是 `COMPOSABLE_INDEPENDENT`，不得未经证明强行合成一个距离。

## 12. 吞并标准

今后引入一个传统数学工具 `T`，至少通过以下测试之一才允许成为 core：

1. **Causal derivation**：`T` 可由 state + operations + future observations 精确推出；
2. **Shadow theorem**：`T` 是某个进取数论结构在特殊 regime 下的闭式表示；
3. **Compression only**：`T` 只提供算法/坐标压缩，不改变本体；
4. **Failure boundary**：若 `T` 需要额外连续完成、隐藏实值或外加精度公理，则只能作为外部 comparison tool。

目前：

- kernel/rank/observability：通过 1/2/3；
- ultrametric：通过 2/3，但 primitive 应保留 integer agreement depth；
- topology：通过 1/2；
- P012 graph metric / L1：通过 1/2/3；
- 一般 Euclidean norm：尚未被吞并，不应自动成为 core。

## 13. 可执行参考

新增：

- `src/enterprise_math/causal_future_module.py`；
- `tests/test_causal_future_module.py`。

参考实现覆盖：

- 多 operation future-visible row closure；
- exact integer rank；
- infinite `Z^k` 上有限 rank stabilization；
- future indistinguishability；
- first distinguishing depth；
- depth-equivalence transitivity 与 strong similarity law。

## 14. 前人工作纪律

传统 linear systems observability、automata future equivalence、ultrametric filtrations、zero-dimensional/clopen topologies 等都有成熟前人理论。

本项目不主张这些一般工具本身原创。

当前待检验的新研究主张是：

> **把 causal distinguishability 设为 primitive，并将传统 algebra / metric-like / topology tools 统一降级为同一 future filtration 的不同 shadows，能否形成比“传统数学 + precision annotation”更紧的 Enterprise Math core。**

正式 novelty claim 前继续做 lineage/prior-art 审计。

## 15. 下一步

1. 把 `dim_causal` 与 A3 relation rank / guard quotient free rank 比较，证明何时三者是同一个母量；
2. 尝试吞并传统 `basis`：定义为最小 future probe generator，而不是预先选择坐标基；
3. 尝试吞并传统 `norm`：把它重写成 translation-invariant causal word cost 的闭式，而不是先验长度；
4. 压力测试 topology：找出哪些传统拓扑性质无法由 finite future filtration 表达，明确吞并边界；
5. Relay 到 A2/P023 与 P012/A5，由各 owner 决定一般母定理与领域 corollary 的最终归属。
