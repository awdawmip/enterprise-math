# 因果吞并 03 —— 线性不是先验向量空间公理，而是 LEGO 组合保持律

状态：`CROSS-ROUTE RESEARCH WIP / EXACT FREE-INTEGER GENERATOR THEOREM + EXECUTABLE REFERENCE`

## 1. 为什么还要再往前一层

若我们直接从：

\[
X=\mathbb Z^k,
\qquad T(x)=Bx
\]

开始，再把 `rank/kernel` 解释成因果对象，仍然可能只是传统线性代数换了本体叙事。

真正的吞并要求连 matrix 都变成派生物。

## 2. LEGO primitive

先只承认 `k` 类 unit slots：

\[
e_1,\ldots,e_k.
\]

一个状态表示每类 unit 有多少个。

unsigned 层：

\[
\mathbb N^k.
\]

signed completion 后：

\[
\mathbb Z^k.
\]

这里的加法首先解释为 LEGO composition：

\[
x\oplus y=x+y.
\]

不是先验向量加法。

## 3. CL-01 —— composition-preserving causal operation

定义一个操作 `T` 满足：

\[
\boxed{
T(0)=0,
\qquad
T(x\oplus y)=T(x)\oplus T(y).
}
\]

解释：

> 如果两个 LEGO state 彼此独立地拼在一起，那么操作整体作用的结果，应等于分别作用后再拼起来。

这是一条 causal/compositional rule，而不是“线性空间公理”。

## 4. CL-02 —— unit images 完全决定操作

每个状态都可由 unit generators 重复组合得到。

在 signed integer state 中：

\[
x=\sum_i x_i e_i.
\]

composition preservation 强制：

\[
\boxed{
T(x)=\sum_i x_iT(e_i).
}
\]

因此，整个操作只需知道：

\[
T(e_1),\ldots,T(e_k).
\]

这就是**unit effect table**。

## 5. CL-03 —— integer matrix 是 unit effect table 的坐标排版

把每个 `T(e_i)` 放成一列：

\[
B=
\begin{bmatrix}
|&&|\\
T(e_1)&\cdots&T(e_k)\\
|&&|
\end{bmatrix}.
\]

立即得到：

\[
\boxed{T(x)=Bx.}
\]

所以 matrix 的理论地位被反转：

旧顺序：

\[
\text{vector space}
\to
\text{linear map}
\to
\text{matrix}.
\]

进取数论顺序：

\[
\boxed{
\text{unit LEGO blocks}
\to
\text{composition law}
\to
\text{operation respects composition}
\to
\text{unit effects}
\to
\text{integer matrix as table}.
}
\]

## 6. CL-04 —— unsigned 与 signed matrix 的因果意义

如果 state 只允许：

\[
\mathbb N^k,
\]

并且 operation 不产生负 unit counts，则每个：

\[
T(e_i)\in\mathbb N^m.
\]

所以 matrix entries 自动是 nonnegative integers。

只有在引入 signed-state completion 后，才自然允许：

\[
B\in\mathbb Z^{m\times k}.
\]

因此“matrix coefficient 可以为负”不是代数习惯，而是 signed LEGO ontology 已经允许 cancellation 的结果。

## 7. CL-05 —— nonlinear 的重新定义

传统定义常把“非线性”理解为“不满足向量空间线性公式”。

这里更底层的判据是：

\[
\boxed{
T(x\oplus y)\neq T(x)\oplus T(y).
}
\]

也就是说：

> 非线性首先意味着操作会读取/改变 blocks 之间的组合关系，而不能由各 unit 的独立 causal effect 相加得到。

这比“出现平方项、乘积项”更本体化。

例如碰撞、阈值、capacity saturation、conditional branch 都天然可能违反 composition preservation。

所以未来研究 nonlinear dynamics 时，不必从 polynomial degree 出发，而应先问：

> 哪一类 LEGO interaction 使 independent-unit superposition 失效？

## 8. CL-06 —— 与 causal future module 的连接

只有当 operation 通过 composition-preserving test 后，才把其 unit effect table 编译成 integer matrix，交给：

`causal_future_module.py`

计算：

- future-visible directions；
- causal invisible subgroup；
- causal dimension；
- causal probe basis。

所以线性代数整条链可以写成：

\[
\boxed{
\text{LEGO composition}
\to
\text{additive causal operation}
\to
\text{matrix shadow}
\to
\text{future distinguishability}
\to
\text{rank/kernel shadow}.
}
\]

这比“先给 matrix，再加 precision”向前推进了一层。

## 9. “1 不随维度改变”在这里的作用

每个 generator：

\[
e_i
\]

不是一个“带维度的数 1”。

它只是一个 unit block。

操作只声明这个 unit block 会产生哪些 unit outputs：

\[
T(e_i).
\]

无论系统有多少 slots，unit count 仍然是整数 `1`。

所谓高维 matrix 只是同时列出更多 unit-slot causal effects。

所以：

\[
\boxed{
\text{维度增加改变 relation slots，
不改变 unit value 1。}
}
\]

## 10. 吞并结论

在这个 regime 中：

- vector addition → LEGO composition 的坐标写法；
- linear map → composition-preserving causal operation；
- matrix → unit effects table；
- column → one unit type 的 causal image；
- rank/kernel → 再由 future distinguishability 产生。

因此线性代数不再作为前置 ontology，只保留为一个**被两层因果结构夹住的高效计算语言**。

## 11. 边界

这并没有吞并所有 linear algebra。

尚未自动得到：

- arbitrary scalar field；
- real/complex vector spaces；
- inner product；
- eigenvalue 的物理意义；
- spectral theorem；
- infinite-dimensional functional analysis。

当前只吞并了：

\[
\boxed{
\text{free finite integer additive operations}
\leftrightarrow
\text{integer matrices}.
}
\]

其他传统结构必须继续给出自己的 causal derivation。

## 12. 可执行参考

新增：

- `src/enterprise_math/lego_additive_operation.py`；
- `tests/test_lego_additive_operation.py`。

实现从 unit images 编译 matrix，并反向恢复 unit images；回归验证 operation 对大量 signed integer states 精确满足 LEGO composition preservation。

## 13. 下一步

1. 研究 interaction term：最小什么额外 relation state 足以描述 composition preservation 的失败；
2. 检查 P010/P011 collision 是否能成为第一个“nonlinear = unit interactions”完整模型；
3. 将 causal probe basis 进一步降到 unit-level experiment generator；
4. 研究 eigenvalue 是否可以被因果吞并为 repeated operation 对某种 integer relation pattern 的周期/scale law，而不是先接受复数谱；
5. 不提前引入 field extension。
