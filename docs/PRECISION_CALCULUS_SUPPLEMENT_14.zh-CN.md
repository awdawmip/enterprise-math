# P018 —— 有限精度证明演算：补充 14

状态：`ACTIVE RESEARCH NOTE`  
范围：有限合流时间、P020 stabilization kernel、eventual kernel、整数 ultrametric、P011 有限时间谱饱和  
依赖：P010、P011、P012、P018-T110—T128、P020  
前人工作边界：见 `docs/PRIOR_ART_P018_COALESCENCE.zh-CN.md`。hierarchy / dendrogram / coalescent 与 ultrametric 的一般联系属于成熟结构；本阶段只研究它们与进取数论 deterministic kernel/stabilization 的精确有限接口。

---

## 1. 从“是否最终合流”到“第几步合流”

对确定性 endomap

\[
F:X\to X,
\]

定义其第 `n` 次迭代为

\[
F^{[n]}.
\]

对状态对 `(x,y)`，若存在 `n` 使

\[
F^{[n]}(x)=F^{[n]}(y),
\]

则称二者 **eventually coalesce**。

首次合流时间定义为

\[
\boxed{
\tau_F(x,y)
=
\min\{n\in\mathbb N:F^{[n]}(x)=F^{[n]}(y)\}.
}
\]

若不存在这样的 `n`，记为 `∞`。

这一定义完全处于 State Pair / diagonal 层，不需要减法、距离或概率。

---

## 2. P018-T129 —— eventual coalescence 是等价关系

状态：`PROVED`

定义

\[
x\sim_\infty y
\iff
\exists n,\ F^{[n]}(x)=F^{[n]}(y).
\]

则 `~∞` 是等价关系。

- 自反：取 `n=0`；
- 对称：等号对称；
- 传递：若 `x,y` 在 `a` 步相等，`y,z` 在 `b` 步相等，则在

\[
N=\max(a,b)
\]

时，由“相等后共同 suffix 永远保持相等”，有

\[
F^{[N]}x=F^{[N]}y=F^{[N]}z.
\]

所以 `x~∞z`。∎

因此 deterministic dynamics 自己把状态空间分成 eventual-coalescence classes。

---

## 3. P018-T130 —— 首次合流时间在每个 coalescence class 上满足 ultrametric 不等式

状态：`PROVED / ESTABLISHED STRUCTURAL PATTERN`

在同一个 `~∞` 等价类中，`τ_F` 有：

\[
\tau_F(x,x)=0,
\]

\[
\tau_F(x,y)=\tau_F(y,x),
\]

且对任意 `x,y,z`：

\[
\boxed{
\tau_F(x,z)
\le
\max\bigl(\tau_F(x,y),\tau_F(y,z)\bigr).
}
\]

### 证明

令

\[
a=\tau_F(x,y),
\qquad
b=\tau_F(y,z),
\qquad
N=\max(a,b).
\]

在第 `a` 步以后 `x,y` 的轨道完全相同，在第 `b` 步以后 `y,z` 的轨道完全相同。因此第 `N` 步时三条轨道已经处于同一状态：

\[
F^{[N]}x=F^{[N]}y=F^{[N]}z.
\]

故 `x,z` 的首次合流不晚于 `N`。∎

所以在每个 eventual-coalescence class 上：

\[
\boxed{
\tau_F\text{ 是 }\mathbb N\text{-值 ultrametric。}
}
\]

这不构成一般 coalescent-ultrametric 结构的原创主张；一般联系属于前人工作。这里的新研究作用是：该 ultrametric 直接由 Enterprise Math 的 deterministic Pair/kernel dynamics 生成，不预设外部距离。

---

## 4. P018-T131 —— kernel chain 按共同时间单调扩大

状态：`PROVED`

定义

\[
K_n=\kerpair(F^{[n]}).
\]

若

\[
(x,y)\in K_n,
\]

则

\[
F^{[n]}x=F^{[n]}y.
\]

再共同施加一次 `F` 即得

\[
F^{[n+1]}x=F^{[n+1]}y.
\]

所以

\[
\boxed{
K_n\subseteq K_{n+1}.
}
\]

并且

\[
\boxed{
x\sim_\infty y
\iff
(x,y)\in\bigcup_{n\in\mathbb N}K_n.
}
\]

注意这里的“并”不表示我们需要无限极限计算：对每个属于该关系的具体 pair，都存在一个有限 witness `n`。

---

## 5. 引入 P020 条件

现在设 `X` 为 well-founded partial order，且

\[
F:X\to X
\]

满足：

1. `F` 单调；
2. `F(x)≤x`。

P020 已证明每个 `x` 在有限步后到达 canonical greatest fixed point：

\[
S(x)=\operatorname{stabilize}_F(x),
\]

并给出一个有限 witness

\[
s(x)=\operatorname{stabilizationSteps}_F(x)
\]

使

\[
F^{[s(x)]}(x)=S(x),
\qquad
F(S(x))=S(x).
\]

---

## 6. P018-T132 —— P020 下，eventual coalescence 当且仅当 stabilization 相等

状态：`PROVED`

在上述 P020 条件下：

\[
\boxed{
x\sim_\infty y
\iff
S(x)=S(y).
}
\]

### `⇒`

设存在 `n` 使

\[
F^{[n]}x=F^{[n]}y.
\]

两条轨道从第 `n` 步开始完全相同。

又 P020 保证两条轨道各自在有限步到达并永久停留于 `S(x)`、`S(y)`。取一个同时不小于合流时刻和两边 stabilization steps 的有限时间，彼时两条轨道既已相同，又分别等于各自固定终点，因此

\[
S(x)=S(y).
\]

### `⇐`

若

\[
S(x)=S(y)=z,
\]

令

\[
N=\max(s(x),s(y)).
\]

由于 `z` 是 fixed point，两条轨道一旦分别在 `s(x),s(y)` 到达 `z`，后续一直保持 `z`。于是

\[
F^{[N]}x=z=F^{[N]}y.
\]

因此二者有限时间合流。∎

这给出非常直接的 kernel 结论：

\[
\boxed{
\kerpair(S)
=
\bigcup_{n\in\mathbb N}\kerpair(F^{[n]}).
}
\]

---

## 7. P018-T133 —— canonical finite coalescence bound

状态：`PROVED`

若 `S(x)=S(y)`，则

\[
\boxed{
\tau_F(x,y)
\le
\max(s(x),s(y)).
}
\]

这不是渐近界，而是直接来自 P020 finite witnesses 的有限整数上界。

因此 P020 不只回答“每条轨道最终稳定”，还给 Pair layer 一个 pair-specific merging bound。

---

## 8. P018-C11 —— 无限状态空间一般不存在统一全局合流时间上界

状态：`COUNTEREXAMPLE / DESIGN WARNING`

取

\[
F(n)=\max(n-1,0)
\]

作用于 `N`。

它单调、向下，并且每个状态都最终稳定到 `0`。

但状态 `n` 到固定点至少需要 `n` 步，所以对任意预先给定有限 `B`，取 `n>B` 即可得到 stabilization time 大于 `B`。

因此：

\[
\boxed{
\text{每个 pair 有有限 bound}
\not\Rightarrow
\text{整个无限状态空间存在统一有限 bound}.
}
\]

这阻止我们把 P020 的 pointwise finite stabilization 偷换成 uniform finite convergence。

---

## 9. P018-T134 —— 任意有限 observation set 都有有限 saturation time

状态：`PROVED`

取有限状态集合

\[
H\subseteq X.
\]

定义

\[
\boxed{
N_H=\max_{x\in H}s(x).
}
\]

则对每个 `x∈H`：

\[
F^{[N_H]}x=S(x).
\]

因此在 `H` 上：

\[
\boxed{
\kerpair(F^{[N_H]}|_H)
=
\kerpair(S|_H).
}
\]

并且对所有 `n≥N_H`，kernel partition 不再变化。

于是即使全局状态空间无限，每一个有限 observation set 的不可区分结构都在有限整数时间内完全饱和。

---

## 10. P018-T135 —— P011 collision spectrum 在有限 observation set 上有限时间饱和

状态：`DERIVED FROM P011 + T134`

P011 的 collision polynomial 与全部 `J_k` 只由有限映射的 fiber sizes 决定。

在有限 `H` 上，T134 已证明

\[
F^{[N_H]}|_H
\]

与

\[
S|_H
\]

诱导完全相同的 kernel partition / fibers。

因此：

\[
\boxed{
K_{F^{[N_H]}|_H}(t)
=
K_{S|_H}(t).
}
\]

而由 P011 的确定性后复合单调性，随 `n` 增加：

\[
K_{F^{[n]}|_H}(t)
\preceq_{\rm coeff}
K_{F^{[n+1]}|_H}(t).
\]

所以整个整数 collision spectrum 在有限时间 `N_H` 后严格停止变化。

这给出一个不需要 Shannon entropy、不需要连续极限的 finite-time irreversibility saturation theorem。

---

## 11. P018-T136 —— stabilization fibers 同时是 coalescence-ultrametric components

状态：`PROVED SYNTHESIS`

由 T132：

\[
S(x)=S(y)
\iff
\tau_F(x,y)<\infty.
\]

因此 `stabilize` 的每个 fiber

\[
S^{-1}(z)
\]

恰好是一个 eventual-coalescence class。

由 T130，`τ_F` 在该 fiber 上是整数值 ultrametric。

所以 P020 的 canonical fixed points 同时给出：

1. dynamics 的 stable normal forms；
2. P010 eventual kernel 的等价类标签；
3. 每个 basin 上一套由 first-merger time 生成的 ultrametric geometry。

这是一条很强的 P012 反哺路线：某些几何结构可以从 deterministic irreversibility 的 pair history 中**派生**，而不是作为连续背景先验。

但这不取代 P012 primitive-step graph metric。两种 metric 来源不同：

- P012 graph metric 测量 primitive-step 路径长度；
- `τ_F` 测量共同动力学下首次失去可区分性的时间。

未来必须研究二者何时相关、何时完全独立，不能直接等同。

---

## 12. 当前对“时间”的新分层

P010 的时间箭头原先主要由 kernel partition 单调粗化表达。

现在可以进一步分成：

\[
\boxed{
\text{State Pair}
\to
\text{kernel chain }K_0\subseteq K_1\subseteq\cdots
\to
\text{first diagonal-entry time }\tau
\to
\text{stabilization fiber}
\to
\text{finite collision-spectrum saturation}.
}
\]

这里的时间完全是离散整数事件序，不需要连续参数。

---

## 13. 可执行压力测试

新增：

- `src/enterprise_math/coalescence_time.py`
- `tests/test_coalescence_time.py`

测试包括：

1. decrement dynamics 的显式 stabilization steps；
2. same stabilized state `iff` finite coalescence 的有限穷举；
3. kernel chain 单调；
4. finite observation kernel 在最大 stabilization time 上精确饱和；
5. 无限 `N` 上不存在统一 saturation bound 的回归；
6. coalescence time 的 ultrametric inequality 穷举。

---

## 14. 下一步

### P018-Q105 —— coalescence ultrametric 与 P012 graph metric 的关系

寻找明确的等价条件、上下界和反例。默认二者是不同 metric，不做未经证明的统一。

### P018-Q106 —— grid cancellation 与 coalescence time

研究 Supplement 13 的 local defect cancellation 是否改变 outer coalescence time，以及是否存在整数 certificate 分离“局部抵消”和“真正 local flatness”。

### P018-Q107 —— finite-history collision polynomial 的时间增量公式

P011 已有单次 fiber merge 的 polynomial 增量。现在研究每一时间步

\[
K_{n+1}(t)-K_n(t)
\]

能否直接由当步新进入 diagonal 的 pair/higher-order tuples 计算，并最终求和到 stabilization spectrum。

### P018-Q108 —— nondeterministic dynamics

当前 ultrametric 证明关键依赖：pair 一旦进入 diagonal，在共同 deterministic suffix 下永不分开。若未来引入 relations/spans，必须重新审查该性质，而不能机械沿用。

---

## 15. 当前结论

P020 与 Pair/kernel 层结合后，得到一个完全有限的闭环：

\[
\boxed{
S(x)=S(y)
\iff
\tau_F(x,y)<\infty,
\qquad
\tau_F(x,y)
\le
\max(s(x),s(y)).
}
\]

并且每个 stabilization fiber 上

\[
\boxed{
\tau_F(x,z)
\le
\max(\tau_F(x,y),\tau_F(y,z)).
}
\]

所以 canonical stabilization basin 自带一个由首次合流时间生成的整数 ultrametric；任意有限 observation set 的 kernel 与 P011 collision spectrum 都在有限时间内精确饱和。

这使“时间—不可逆性—几何”第一次在进取数论内部通过同一个有限 Pair/kernel 机制严格接通，而不是依赖连续极限或外部概率模型。
