# P018 —— 有限精度证明演算：补充 12

状态：`ACTIVE RESEARCH NOTE`  
范围：无减法的 State Pair 层、difference coordinates、kernel/diagonal 演算，以及对底层逻辑的最小化  
依赖：P005、P008、P009、P010、P011、P018-T99—T109  
纪律：笛卡尔积、对角关系、kernel equivalence、pair dynamics 与函数复合都是基础成熟数学。本文不主张这些对象为新数学；研究重点是它们能否作为进取数论各条 precision/defect/irreversibility 路线的共同最低逻辑层。

## 1. T99—T109 留下的最小性问题

Supplement 11 定义

\[
\mathscr R_F(x,h)=F(x+h)-F(x).
\]

它把 State evolution 与 Difference evolution 接起来，并把 P010 历史合流重写成 zero-response relation。

但该表达仍依赖：

1. 状态拥有可做差的坐标；
2. 我们保留 base state `x`，因为同一个 `h` 在不同 base 上响应不同。

因此更底层的问题是：

> 在不预设减法、群完成甚至整数坐标的情况下，什么对象已经足够表达“两个状态如何一起演化、何时合流、路径差如何继续传播”？

答案是最朴素的 state pair。

---

## 2. P018-T110 —— 任意确定性映射都严格诱导 State Pair 演化

状态：`PROVED / ESTABLISHED PRODUCT CONSTRUCTION`

对任意状态集合 `X`，定义

\[
\boxed{
\operatorname{Pair}(X)=X\times X.
}
\]

对任意确定性映射

\[
F:X\to Y,
\]

定义

\[
\boxed{
\operatorname{Pair}(F)(x,y)
=(F(x),F(y)).
}
\]

则：

\[
\boxed{
\operatorname{Pair}(id_X)=id_{\operatorname{Pair}(X)},
}
\]

并且对

\[
X\xrightarrow{F}Y\xrightarrow{G}Z
\]

有

\[
\boxed{
\operatorname{Pair}(G\circ F)
=
\operatorname{Pair}(G)\circ\operatorname{Pair}(F).
}
\]

这是笛卡尔积映射的直接性质。∎

因此“同时跟踪两个状态”不需要额外代数公理；任意确定性 state evolution 自动给出严格 pair evolution。

---

## 3. P018-T111 —— 对角线是 deterministic evolution 的吸收子对象

状态：`PROVED`

定义 `X` 的对角线：

\[
\boxed{
\Delta_X
=\{(x,x):x\in X\}.
}
\]

对任意

\[
F:X\to Y,
\]

都有

\[
\boxed{
\operatorname{Pair}(F)(\Delta_X)
\subseteq
\Delta_Y.
}
\]

### 证明

若输入 pair 为 `(x,x)`，则

\[
\operatorname{Pair}(F)(x,x)
=(F(x),F(x))
\in\Delta_Y.
\]

∎

因此两个历史一旦变成同一状态，对所有后续确定性映射都继续位于 diagonal。

这已经在**完全不使用整数差值**的层面重现 P010 的“合流不可逆”。

---

## 4. P018-T112 —— kernel relation 就是被 Pair(F) 送入 diagonal 的状态对

状态：`PROVED / ESTABLISHED`

对

\[
F:X\to Y
\]

定义 kernel equivalence：

\[
\boxed{
x\sim_F y
\iff
F(x)=F(y).
}
\]

则

\[
\boxed{
(x,y)\in\sim_F
\iff
\operatorname{Pair}(F)(x,y)\in\Delta_Y.
}
\]

若再复合

\[
G:Y\to Z,
\]

则

\[
\boxed{
\sim_F\ \subseteq\ \sim_{G\circ F}.
}
\]

因为 `F(x)=F(y)` 必然推出 `G(F(x))=G(F(y))`。∎

所以 P010 的 kernel partition 单调粗化，在最底层只是：

> deterministic composition 只能让更多 pair 落到 diagonal，不能让已经落入 diagonal 的 pair 再离开。

---

## 5. P018-T113 —— 在 `N` 上，State Pair 与 `(base, signed difference)` 是无损等价坐标

状态：`PROVED`

令

\[
\mathcal E
=\{(a,h):a\in\mathbb N,
\ h\in\mathbb Z,
\ a+h\ge0\}.
\]

定义

\[
\boxed{
\Theta:\mathbb N\times\mathbb N\to\mathcal E,
\qquad
\Theta(a,b)=(a,b-a).
}
\]

其逆为

\[
\boxed{
\Theta^{-1}(a,h)=(a,a+h).
}
\]

因此

\[
\boxed{
\mathbb N\times\mathbb N
\cong
\{(a,h):h\in\mathcal D_a\}.
}
\]

在这个坐标变换下，T110 的 pair evolution

\[
(a,b)
\mapsto
(F(a),F(b))
\]

恰好变成 Supplement 11 的

\[
\boxed{
(a,h)
\mapsto
(F(a),\mathscr R_F(a,h)).
}
\]

因为 `b=a+h`。

所以 exact finite response 不是额外附加到底层的神秘运算；它是普通 state-pair evolution 在整数 difference coordinates 下的无损表达。

---

## 6. P018-C09 —— 单独保存 signed defect 会丢失后续传播所需信息

状态：`COUNTEREXAMPLE / DESIGN WARNING`

即使两个 pair 具有相同 signed difference，经过同一个非线性或粗化 operation 后，difference response 也可能不同。

### Quotient 反例

取

\[
Q_2(n)=n//2,
\qquad h=1.
\]

在 base `0`：

\[
\mathscr R_{Q_2}(0,1)
=Q_2(1)-Q_2(0)
=0.
\]

在 base `1`：

\[
\mathscr R_{Q_2}(1,1)
=Q_2(2)-Q_2(1)
=1.
\]

所以同一个 `h=1` 不能独立决定 transport。

### Collapse 反例

对平方 collapse：

\[
\mathscr R_{C_2}(1,1)
=C_2(2)-C_2(1)
=0,
\]

但

\[
\mathscr R_{C_2}(3,1)
=C_2(4)-C_2(3)
=3.
\]

因此：

\[
\boxed{
\text{defect value alone is not a complete state of difference dynamics.}
}
\]

必须至少保留 base + defect，或者等价地保留完整 state pair。

这给底层设计增加一个硬约束：不能把 holonomy 压缩成脱离 base state 的全局标量后再期待它独立演化。

---

## 7. P018-T114 —— parallel-path 2-cell 可以先定义成 endpoint pair，而不需要减法

状态：`PROVED / DEFINITIONAL MINIMIZATION`

令

\[
\gamma,\eta:X\to Y
\]

为两条 parallel deterministic paths。

对输入 `x`，定义最弱路径比较对象：

\[
\boxed{
\mathfrak C_{\gamma,\eta}(x)
=(\gamma(x),\eta(x))
\in Y\times Y.
}
\]

如果继续接共同后缀

\[
S:Y\to Z,
\]

则

\[
\boxed{
\mathfrak C_{S\gamma,S\eta}(x)
=
\operatorname{Pair}(S)
\bigl(\mathfrak C_{\gamma,\eta}(x)\bigr).
}
\]

这完全不需要 `Y` 具有加法、序或 group completion。

当

\[
Y=\mathbb N
\]

时，再通过 T113 的 `Theta` 坐标化，第二坐标就变成 T102 的 signed holonomy：

\[
\eta(x)-\gamma(x).
\]

所以可以把：

\[
\boxed{
\text{path pair / endpoint pair}
}
\]

视为比 signed holonomy 更原始的 2-cell 候选，而 signed holonomy 是有整数坐标时的压缩表示。

本文仍不宣布已经建立严格 2-category。

---

## 8. P018-T115 —— critical square 的最弱 defect 是 endpoint pair，数值 `Delta` 是其坐标

状态：`PROVED`

对 operation/projection square：

\[
X_e
\xrightarrow{F_e}
X_e
\]

与

\[
X_e
\xrightarrow{\pi}
X_d
\xrightarrow{F_d}
X_d,
\]

定义其 endpoint pair：

\[
\boxed{
\mathfrak C_F^{e:d}(x)
=
\bigl(
\pi(F_e(x)),
F_d(\pi(x))
\bigr).
}
\]

则 square 在 `x` 上交换当且仅当

\[
\boxed{
\mathfrak C_F^{e:d}(x)\in\Delta_{X_d}.
}
\]

当 `X_d=N` 时，T103 的 signed critical-square defect 恰好是该 pair 的 difference coordinate：

\[
\boxed{
\Delta_F^{e:d}(x)
=
\operatorname{second}(\mathfrak C)
-
\operatorname{first}(\mathfrak C).
}
\]

所以“square 是否交换”本身不需要 signed arithmetic；signed defect 只负责更高效地量化不交换的方向与大小。

---

## 9. P018-T116 —— P005、collapse basin 与 P010 history merge 统一为 kernel-pair 问题

状态：`PROVED STRUCTURAL UNIFICATION`

以下结构都可以统一写成“哪些 state pairs 被某个 map 送入 diagonal”。

### Precision projection

对 coarse projection

\[
Q_m:\mathbb N\to\mathbb N,
\]

其 kernel pair 为

\[
\boxed{
(x,y):Q_m(x)=Q_m(y).
}
\]

这正是同一 coarse fiber 中的状态对。

### Collapse basin

对

\[
C_p:\mathbb N\to\mathbb N,
\]

其 kernel pair 为

\[
\boxed{
(x,y):R_p(x)=R_p(y),
}
\]

即同一完全幂盆地中的状态对。

### Deterministic time

对累计演化

\[
\mathcal F_t,
\]

其 kernel pair 为

\[
\boxed{
(x,y):\mathcal F_t(x)=\mathcal F_t(y),
}
\]

即 P010 的历史合流关系。

三者的物理语义不同，但底层关系结构共享：

\[
\boxed{
\text{many-to-one map}
\longleftrightarrow
\text{nontrivial kernel pair}
\longleftrightarrow
\text{off-diagonal pairs sent to diagonal}.
}
\]

这比直接把三者称为同一个“熵”或同一种“坍缩”更弱，也更严格。

---

## 10. P018-T117 —— P010 multiplicity 是 kernel pair 的单基点 fiber cardinality

状态：`PROVED`

对累计演化 `F_t` 与状态 `x`，P010 定义

\[
[x]_t
=\{y:F_t(y)=F_t(x)\}.
\]

在 pair language 中，它正好是 kernel relation 在第一个坐标固定为 `x` 时的 fiber：

\[
\boxed{
[x]_t
=
\{y:(x,y)\in\kerpair(F_t)\}.
}
\]

因此当有限时：

\[
\boxed{
M_t(x)
=|[x]_t|
=\left|
\{y:(x,y)\in\kerpair(F_t)\}
\right|.
}
\]

T107 的 zero-response 计数与这里完全一致，只是经过 T113 从 pair coordinates 换成 difference coordinates。

所以 P010 的不可逆性 multiplicity 可以在**完全不使用减法**的底层定义，然后在整数坐标下再转成 zero-response count。

---

## 11. P018-T118 —— kernel relation 在确定性复合下单调扩大

状态：`PROVED`

设

\[
X\xrightarrow{F}Y\xrightarrow{G}Z.
\]

则

\[
\boxed{
\kerpair(F)
\subseteq
\kerpair(G\circ F).
}
\]

进一步，沿序列

\[
F_t=T_{t-1}\circ\cdots\circ T_0
\]

有

\[
\boxed{
\kerpair(F_t)
\subseteq
\kerpair(F_{t+1}).
}
\]

这就是 P010 等价类只能保持或合并的 pair-level 版本。

其重要性在于：该定理只需要“函数复合”，不需要自然数、序、加法、距离或概率。

因此如果我们寻找进取数论关于**确定性不可逆性**的最底层逻辑，这个 kernel-pair 单调性比任何具体的整数 entropy 公式都更原始。

---

## 12. 对 P011 的入口：先在 kernel pair 上定义谱，再决定是否需要 difference coordinates

P011 已经研究：

- fiber multiplicity；
- collision polynomial；
- multiplicity spectrum；
- 与 entropy 的比较。

T117—T118 提示一个更基础的组织顺序：

1. 先把累计映射的 kernel pair / equivalence classes 作为原始组合对象；
2. 在这些 finite fibers 上定义整数谱；
3. 只有需要方向、局部边界或 operation response 时，才切换到 `(base,h)` difference coordinates；
4. 对数 entropy 继续只作为外部派生比较。

这可以减少把某个坐标选择误认为不可逆性本体的风险。

---

## 13. 对底层逻辑的进一步最小化

状态：`RESEARCH SYNTHESIS / NOT FROZEN`

Supplement 11 的候选底层为：

\[
\text{typed finite State}
+
\text{state-dependent Difference fibers}
+
\text{exact response}.
\]

本阶段说明还可以再分层：

### Layer -1 —— Pair / kernel logic

只要求：

- typed state sets/objects；
- deterministic maps；
- parallel state pairs；
- diagonal；
- kernel pair；
- pair evolution under functions。

这一层已经足够表达：

- 合流；
- 不可重新分开；
- many-to-one；
- path endpoints 是否相同；
- P010 multiplicity 的集合论底座。

### Layer 0 —— Numeric difference coordinates

当 state object 具有可用的 cancellative/additive coordinates 时，才把

\[
(a,b)
\]

压缩成

\[
(a,h=b-a).
\]

这时得到 signed response、carry/borrow、holonomy magnitude 与 finite chain law。

### Layer 1+ —— Precision/order/operation enrichment

再叠加 P008 order adjunction、P005 precision atlas、operation defect/obstruction、P017 certificate 等结构。

所以 pair/kernel 并不取代 integer-first ontology；它只是说明：**不可逆性和路径比较的逻辑骨架，比整数算术本身还可以更弱。**

---

## 14. 为什么这有助于“保持所有路线”

如果两条研究路线最终输出的是两个不同表示对象，不应立刻强迫它们共享同一个 signed coordinate。

可以先比较它们是否定义了同一个：

- state pair；
- kernel relation；
- diagonal-hit event；
- partition of states。

若这些最弱结构已经一致，那么数值 defect 不同可能只是坐标差异。

若连 kernel pair / endpoint pair 都不同，才说明两条路线对底层状态结构给出了真正不同的预测。

因此路线比较可以形成层级：

\[
\boxed{
\text{pair/kernel}
\to
\text{difference coordinate}
\to
\text{defect transformation law}
\to
\text{higher certificate/invariant}.
}
\]

越往左越弱、越不依赖表示；越往右信息越丰富但假设也越多。

---

## 15. 可执行压力测试

新增：

- `src/enterprise_math/state_pair.py`
- `tests/test_state_pair.py`

优先验证：

1. T110 Pair(id) 与 Pair(G∘F)；
2. T111 diagonal 吸收；
3. T112 kernel relation = diagonal preimage；
4. T113 pair ↔ base/difference 坐标互逆；
5. C09 同 defect 不同 base 的 response 反例；
6. T114 common-suffix pair propagation；
7. T116 quotient/collapse/time kernel-pair 特例；
8. T118 kernel monotonicity under composition。

---

## 16. 下一阶段开放问题

### P018-Q100 —— Pair/kernel 是否就是最弱的 irreversibility substrate？

寻找一个确定性 many-to-one 结构，不能被 kernel pair 描述其“合流不可逆性”。若找不到，再讨论是否把该层正式提升为 P010/P011 的共同基础。

### P018-Q101 —— relation 而非 function 的演化

自然底层未来可能需要 nondeterministic transition。此时 ordinary function kernel 不够。研究 relation/span/correspondence 下 diagonal 与 pair evolution 应怎样改写。

### P018-Q102 —— 2x2 critical-grid interchange 应在哪一层证明？

优先尝试在 endpoint-path-pair 层证明 strict pasting/coherence；只有在需要量化时才映射到 signed defect coordinates。这样可避免 state-dependent response 让数值 2-cell 的组合看起来人为复杂。

### P018-Q103 —— kernel partition 与 precision atlas 的兼容

mixed-radix chart change 不改变 underlying total detail。证明合法 chart transition 是否也严格保持相关 kernel pairs / ambiguity partitions。

### P018-Q104 —— Pair layer 与 P012 几何

几何最原始对象可能是“哪些 pair 可由 primitive steps 连接以及最少几步”，而不是先假设一个数值距离。研究 P012 graph metric 是否可被看成 pair layer 上的最短 path observable。

---

## 17. 当前结论

本阶段把 Supplement 11 的 State/Difference 二层结构再向下分解了一次：

\[
\boxed{
\text{State Pair}
\quad\text{比}\quad
\text{signed Difference}
\quad\text{更原始。}
}
\]

对任意确定性映射，只需要

\[
\boxed{
(x,y)\mapsto(F(x),F(y))
}
\]

就已经能表达合流、diagonal、kernel 与 P010 的不可逆性单调性。

在自然数坐标中，

\[
(a,b)
\leftrightarrow
(a,b-a)
\]

才进一步产生 exact finite response；这说明 signed defect 是 pair evolution 的高效坐标，不是底层必须先验拥有的对象。

因此当前最弱的底层候选继续收敛为：

\[
\boxed{
\text{typed finite State}
+\text{Pair/kernel logic}
+\text{optional numeric Difference coordinates}
+\text{precision/order/operation enrichments}.
}
\]

这一步尤其重要，因为它同时做到两件事：**继续保留 integer-first 数学本体，又把不可逆性所需的逻辑公理降到比整数更弱的层级。**