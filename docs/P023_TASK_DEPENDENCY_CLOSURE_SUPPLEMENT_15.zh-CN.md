# P023 —— 零成本 task dependency closure，补充 15

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023，并连接 P018 scheduling 层  
依赖：P023-S13 conditional repair 与 P023-S14 exact task scheduling  
纪律：closure operator 与 functional dependency 都属于成熟数学。本补充的项目作用，是把 zero-repair task implication 确定为 finite precision 自然诱导的精确 closure，并用它压缩 scheduling state space。

## 1. Zero repair 就是一种 dependency

令有限 task family 为

\[
\mathcal T=\{E_1,\ldots,E_m\}
\]

定义在有限状态集 `X` 上。

对已经保留的 task subset

\[
S\subseteq\mathcal T,
\]

记当前 joint context 为

\[
C_S=\bigcap_{E\in S}E,
\]

空交取 universal one-block relation。

一个 task `F` 已经被 `S` 决定，当且仅当加入它不需要任何非平凡 repair：

\[
\boxed{
\rho(F\mid C_S)=1.
}
\]

由 P023-S12，这等价于

\[
C_S\subseteq F.
\]

所以 `F` 真的是当前 retained precision state 的一个确定函数。

## 2. Task dependency closure

定义

\[
\boxed{
\operatorname{cl}(S)
=
\{F\in\mathcal T:C_S\subseteq F\}.
}
\]

等价地，

\[
\boxed{
F\in\operatorname{cl}(S)
\iff
\rho(F\mid C_S)=1.
}
\]

它就是从当前 task set 出发，所有可以 zero repair 自动加入、且不会改变 joint partition 的 tasks 集合。

## 3. P023-S15-T01 —— Dependency closure 是 closure operator

状态：`PROVED`。

映射

\[
S\mapsto\operatorname{cl}(S)
\]

满足：

1. extensive：
   \[
   S\subseteq\operatorname{cl}(S);
   \]
2. monotone：
   \[
   S\subseteq T
   \Longrightarrow
   \operatorname{cl}(S)\subseteq\operatorname{cl}(T);
   \]
3. idempotent：
   \[
   \boxed{
   \operatorname{cl}(\operatorname{cl}(S))
   =
   \operatorname{cl}(S).
   }
   \]

### 证明

Extensivity 显然成立，因为 `C_S` 必然细化 `S` 中每个 task。

若 `S subseteq T`，则

\[
C_T\subseteq C_S.
\]

所以任何被 `C_S` 决定的 task，也必然被更细的 `C_T` 决定，从而得到 monotonicity。

对 idempotence，`cl(S)` 中每个 task 本来已经是 `C_S` 的函数；把这些已确定 tasks 再与 `C_S` 相交，不会继续细化 context。因此

\[
C_{\operatorname{cl}(S)}=C_S,
\]

于是再次 closure 也不会产生更多 tasks。∎

## 4. P023-S15-T02 —— Closure 不改变 represented precision state

状态：`PROVED`。

对任意 task set `S`，

\[
\boxed{
C_{\operatorname{cl}(S)}=C_S.
}
\]

因此 dependency closure 增加的是 task names，而不是 state distinctions。

这正是 zero-cost tasks 可以在 schedule 中自动补入、且不会改变后续 conditional repair factors 的精确原因。

## 5. Task bases

若

\[
\boxed{
\operatorname{cl}(S)=\mathcal T,
}
\]

则称 `S` 是一个 **task basis**。

由 T02，它等价于

\[
\boxed{
C_S=C_{\mathcal T}.
}
\]

所以 task basis 是任何已经能够生成完整声明 joint precision 的 coordinate subset。

一旦 basis 被保留，basis 外的 tasks 在数学上就是冗余坐标。

这只是 representation theorem，不表示这些 tasks 在实验测量上天然廉价。

## 6. P023-S15-T03 —— Higher-order dependencies 不必是 pairwise 的

状态：`PROVED`，由 S13 parity example 给出。

在 even-parity system 中，

\[
E_3\notin\operatorname{cl}(\{E_1\}),
\qquad
E_3\notin\operatorname{cl}(\{E_2\}),
\]

但

\[
\boxed{
E_3\in\operatorname{cl}(\{E_1,E_2\}).
}
\]

因此 dependency 一般不能只用 pairwise implication DAG 完整表示。

真正对象是 closure system / dependency hypergraph。

这与 S13 的结论一致：pairwise incidence geometry 不能决定 higher-order joint precision。

## 7. P023-S15-T04 —— 这个 closure system 一般不是 matroid

状态：`PROVED BY EXPLICIT COUNTEREXAMPLE`。

使用 S14 的五状态 greedy counterexample：

\[
A=(0,0,0,0,1),
\]

\[
B=(0,0,0,1,0),
\]

\[
C=(0,0,1,2,3).
\]

`C` 能决定 `A` 与 `B`，所以

\[
A\in\operatorname{cl}(\{C\})
\setminus\operatorname{cl}(\varnothing).
\]

但 `A` 不能决定 `C`：

\[
C\notin\operatorname{cl}(\{A\}).
\]

这违反 matroid closure 的 exchange implication：

\[
x\in\operatorname{cl}(S\cup\{y\})\setminus\operatorname{cl}(S)
\Longrightarrow
y\in\operatorname{cl}(S\cup\{x\}).
\]

因此 generic precision dependency closure 不是 matroid closure。

所以不能通过引入 matroid exchange 来为 universal greedy acquisition theorem 辩护。

## 8. P023-S15-T05 —— Exact scheduler 可以按 dependency closure 商掉状态空间

状态：`PROVED`。

S14 的 subset DP 表面上最多有

\[
2^m
\]

个 raw task-subset states。

但如果两个 subsets 有相同 closure，由 T02，它们诱导完全相同的 context partition，因此对所有 remaining tasks 都具有相同 conditional repair costs。

于是 DP states 可以规范地替换成 closure fixed points：

\[
\boxed{
\mathfrak C
=
\{S\subseteq\mathcal T:\operatorname{cl}(S)=S\}.
}
\]

并且

\[
|\mathfrak C|\le2^m.
\]

这个不等式可以严格成立，且 dependency 很强时可以大幅缩小状态空间。

每一步 positive-cost transition 都可以改写为：

1. 从当前 closed set 外选择一个 task；
2. 支付它当前的 conditional repair depth；
3. 立刻对新增集合做 closure，把所有新确定 tasks 免费加入。

得到的 optimum 与原始 subset DP 完全相同。

## 9. 五状态例子：一个 generator 闭合整个 task family

在同一个 S14 例子中，

\[
\boxed{
\operatorname{cl}(\{C\})=\{A,B,C\}.
}
\]

所以 `C` 单独就是一个 task basis。

相反，

\[
\operatorname{cl}(\{A,B\})=\{A,B\};
\]

两个看起来便宜的 binary tasks 并不能决定 four-way task。

因此 optimal schedule 只有一个 positive-cost generator：

\[
\boxed{C}
\]

binary cost 为 `2`；之后 `A,B` 都通过 closure 零成本补入。

这正是 S14 greedy failure 的结构性解释。

## 10. P017 解释

L065 给出两个具体 two-task closure states。

`k=11` 时，root precision 决定 least-prime precision：

\[
\boxed{
P\in\operatorname{cl}(\{R\}).
}
\]

因此 `{R}` 已经是 `{P,R}` 的 task basis。

而 `k=1737` 时，两个 task 互不决定，因为

\[
\rho(P,R)=2,
\qquad
\rho(R,P)=8.
\]

所以该 two-task family 的任何 basis 都仍然必须真正保留两个 coordinates。

closure language 因而精确捕捉了 L065 order reversal 背后的 basin-dependent 结构原因。

## 11. 研究工具规则

在运行昂贵的 multi-task scheduler 前：

1. 先计算当前 context 的 zero-repair dependency closure；
2. 从 positive-cost candidate set 删除 closure 中所有 tasks；
3. 按 closure equality 商掉 DP states；
4. 存在小 task basis 时优先识别；
5. 不假设 pairwise dependencies 已经完整；
6. 不假设 closure 是 matroid，也不在无单独 theorem 时使用 greedy basis construction。

这属于 exact state reduction，不是 heuristic pruning。

## 12. 可执行规范

- `src/enterprise_math/precision_dependency_closure.py`
- `tests/test_precision_dependency_closure.py`

测试验证 closure axioms，固定 S14 family 上的 nonmatroid exchange failure，把 `{C}` 识别为唯一 minimal basis，并将 closure-state DP 与完整 subset DP 做精确对照。

## 13. 前人工作与新颖性纪律

Closure operators、functional dependencies、implication closure 与 attribute-closure 风格推理都是成熟数学与数据库理论。Enterprise Math 不主张发明这些结构。

本项目新增的统一接口是精确识别

\[
\boxed{
F\in\operatorname{cl}(S)
\iff
\rho(F\mid C_S)=1,
}
\]

从而把 zero-repair precision dependence 变成由现有 P023 incidence calculus 自然诱导的 closure operation。
