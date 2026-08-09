# P023 —— Incidence Repair 单调性，补充 10

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023，输入使用 A4 finite relation  
依赖：P023-S8 image separation、P023-S9 minimal repair cardinality、A4 admissible relations  
纪律：finite relations、quotient maps、degree 与 inclusion monotonicity 都属于成熟数学。项目作用是把它们固定成共同的 precision/admissibility 接口。

## 1. 设置

令

\[
R\subseteq I\times X
\]

为有限非空 incidence relation。可以把 `i in I` 看成 shell/factor/mode label，把 `x in X` 看成真正与该 label 关联的细状态。

再令

\[
g:X\to Y
\]

为保留的 observation。

任务只保留 `g(x)`，但仍要求恢复实际 label `i`。

## 2. Observed incidence relation

把 relation 沿保留 observation 推过去：

\[
\boxed{
\bar R_g
=
\{(i,y):\exists x,\ (i,x)\in R,\ g(x)=y\}.
}
\]

对每个保留 observation `y`，定义其 realized label set：

\[
L_{R,g}(y)
=
\{i:(i,y)\in\bar R_g\}
\]

以及局部 label multiplicity：

\[
m_{R,g}(y)=|L_{R,g}(y)|.
\]

定义最坏局部 burden：

\[
\boxed{
M(R,g)=\max_{y\in\operatorname{im}g}m_{R,g}(y),
}
\]

其中只考虑由 `R` 真正到达的 observation values。

## 3. P023-S10-T01 —— Incidence degree 等于最小 repair alphabet

状态：`PROVED`。

在 tagged state space `R` 上，把 coarse state 定义为

\[
(i,x)\mapsto g(x)
\]

并把 target state 定义为

\[
(i,x)\mapsto(g(x),i).
\]

则任何额外 repair coordinate 所需的精确最小 alphabet 为

\[
\boxed{
R_{\min}(R,g)=M(R,g).
}
\]

### 证明

保留值为 `y` 的一个 coarse fiber，恰好包含由

\[
L_{R,g}(y)
\]

索引的不同 target-label blocks。因此它的 split multiplicity 就是 `m_{R,g}(y)`。P023-S9-T03 已证明全局最小 repair alphabet 等于所有 coarse fibers 的最大局部 split multiplicity，所以正好得到 `M(R,g)`。∎

等价地，`M(R,g)` 是有限二部关系 `bar R_g` 在 observation 一侧的最大 degree。

## 4. P023-S10-T02 —— Relation enlargement 单调性

状态：`PROVED`。

若

\[
R\subseteq R',
\]

则对固定 observation `g`，

\[
\boxed{
M(R,g)\le M(R',g).
}
\]

### 证明

对每个 `y` 都有

\[
L_{R,g}(y)\subseteq L_{R',g}(y),
\]

所以每个局部 label multiplicity 只能增加或保持。再取最大值得证。∎

因此扩大 admissible state relation 只能增加或保持 shell/label repair burden。

## 5. P023-S10-T03 —— Observation coarsening 单调性

状态：`PROVED`。

若更粗的 retained observation `h:X->Z` 在 `R` 使用到的所有 states 上通过 `g` 因子化：

\[
\boxed{h=\phi\circ g},
\]

则

\[
\boxed{
M(R,g)\le M(R,h).
}
\]

### 证明

对每个 fine observation value `y`，在 `y` 上实现的每个 label，也一定在 coarse value `phi(y)` 上实现。因此

\[
L_{R,g}(y)
\subseteq
L_{R,h}(\phi(y)).
\]

合并 observation fibers 后，最大 label multiplicity 不可能下降。∎

所以 retained coordinate 越粗，在目标 label task 不变时，需要的额外 repair alphabet 不可能反而更小。

## 6. P023-S10-T04 —— 联合 precision/admissibility 单调性

状态：`PROVED`。

若

\[
R\subseteq R'
\]

且

\[
h=\phi\circ g,
\]

则

\[
\boxed{
M(R,g)\le M(R',h).
}
\]

由 T02 与 T03 直接得到。

这给出一个二维 order law：

\[
\boxed{
\text{更严格 realizability}
+
\text{更细 retained observation}
\Longrightarrow
\text{repair burden 不增}.
}
\]

反过来，relation enlargement 与 observation coarsening 都属于保守操作，它们可能制造额外 ambiguity。

## 7. P023-S10-T05 —— Image separation 是 alphabet-one 端点

状态：`PROVED`。

shell label 已经是 retained observation 的函数，当且仅当

\[
\boxed{M(R,g)=1.}
\]

### 证明

decoder 存在，当且仅当每个真正到达的 observation value 至多关联一个不同 label。每个 reached value 又至少有一个 label，所以这恰好等价于 observation-side 最大 degree 为 1。∎

因此 P023-S8 正是 S9/S10 定量 calculus 的 zero-extra-repair 端点。

## 8. Envelope 的单向逻辑

令 `R_actual subset R_envelope`。

由 T02：

\[
M(R_{actual},g)\le M(R_{envelope},g).
\]

因此：

- 如果 **envelope** 已经有 `M=1`，actual relation 一定也有 `M=1`；
- 如果 **actual relation** 有 `M>1`，envelope 一定也会显示 collision；
- 但 envelope 出现 `M>1` **不能**推出 actual collision。

这就是

\[
\boxed{
\text{over-approximation 可以证明 separation，
但不能证明 realized collision}.
}
\]

的精确逻辑形式。

## 9. P017 k=6：最小自我纠偏见证

在 `k=6` 的 lower-band `p=2,3` raw quotient windows 中，root observation 在 root 4 上产生 raw overlap，因此

\[
M(R_{window},R_2)=2.
\]

但冲突的 `p=3,q=16` 并不是 3-rough：`3*16=48` 的 least prime factor 是 2。施加真实 least-prime admissibility relation 后，

\[
\boxed{M(R_{shell},R_2)=1.}
\]

这正是推进 P017 L056 时暴露出的语义纠偏：即使是 exact interval envelope，仍然可能比真实 shell relation 更大。

## 10. Precision 解释

该定理把三个独立选择分开：

1. admissible relation `R` —— 哪些 tagged states 真正可以出现；
2. retained observation `g` —— 哪个状态坐标被保留下来；
3. target label task —— 哪些区别未来仍要求恢复。

repair burden 不是其中任何一个对象单独具有的内禀属性，而是

\[
\boxed{
M(R,g;\text{label task}).
}
\]

这就是 task-relative precision 的 relation-theoretic 形式。

## 11. 可执行规格

- `src/enterprise_math/incidence_repair.py`
- `tests/test_incidence_repair.py`

测试把 degree formula 与 generic P023-S9 minimal-repair compiler 交叉验证，固定两个单调轴的严格例子，把 S8 恢复为 alphabet-one case，并锁定 P017 `k=6` raw-envelope 与 realized-shell 的语义纠偏。

## 12. Ownership 边界

A4 负责 generic finite relation/composition/support structure；P023 负责 future-safe quotient 与 repair semantics。本补充是两者的 bridge：消费 A4-style relation，并计算 A2/P023 的 label-recovery precision burden。

这里不主张发明新的 generic relation algebra。
