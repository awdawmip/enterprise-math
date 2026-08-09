# Causal Signature Core —— 从 LEGO 状态、因果操作与未来签名生成数学结构

状态：`ACTIVE CROSS-ROUTE RESEARCH ORIENTATION / NOT YET CANONICAL FOUNDATION`

本文件是对“传统数学 + precision annotation”路线的进一步纠偏与收敛。

它不创建新 canonical problem 编号，也不修改《我眼中的世界.md》。

## 1. 三个原始层

当前候选 core 只保留三类 primitive。

### 1.1 LEGO state / composition

状态由离散 unit 与其关系组成。

在可独立组合的 regime 中有：

\[
x\oplus y.
\]

`1` 是 unit count，本身不随维度改变。

### 1.2 Causal operation language

允许有限操作词：

\[
\omega=T_n\circ\cdots\circ T_1.
\]

理论不默认所有数学变换都允许；只有声明的 causal operations 才产生未来。

### 1.3 Observation language

给定真正允许读取的离散/整数 observations：

\[
o:X\to V_o.
\]

不同 future task 可以有不同 observation language。

## 2. CS-01 —— future signature

对状态 `x` 定义完整未来签名：

\[
\boxed{
\Sigma(x)(\omega,o)
:=
o(\omega(x)).
}
\]

这里：

- `omega` 带 operation identity；
- `o` 带 observation identity；
- 输出保持原始离散/整数值。

所以 `Sigma(x)` 不是一个 real embedding，而是一张因果实验结果表。

## 3. CS-02 —— 理论层状态等价

对 declared future language：

\[
\boxed{
x\equiv_\Sigma y
\iff
\Sigma(x)=\Sigma(y).}
\]

也就是说：

> 如果任何允许的有限未来实验都无法区分两个状态，那么在当前理论层它们应当被坍缩为同一个状态。

这不是“测量误差下近似相等”，而是 operation-language-relative exact indistinguishability。

## 4. CS-03 —— collapse 在 precision 之前

定义 causal collapse：

\[
C_\Sigma:X\to X/{\equiv_\Sigma}.
\]

于是顺序是：

\[
\boxed{
\text{future indistinguishability}
\to
\text{collapse}
\to
\text{remaining structure}.
}
\]

所谓 precision 只能在最后描述：

> 当前 quotient 还保留了多少 future distinction。

因此 precision 是 collapse 的结果/诊断，不是 foundation 输入。

## 5. CS-04 —— finite-depth signature

如果 future words 有离散长度，定义：

\[
\Sigma_t(x)
=
\Sigma(x)|_{|\omega|\le t}.
\]

相应：

\[
x\equiv_t y
\iff
\Sigma_t(x)=\Sigma_t(y).
\]

有：

\[
\equiv_{t+1}\subseteq\equiv_t.
\]

所以 causal distinguishability 自然形成 finite-depth filtration。

这条 filtration 是 topology / agreement depth / future precision 的共同母对象。

## 6. Traditional quotient 被吞并

传统 quotient 语言只在 `equiv_Sigma` 产生以后才出现。

primitive 不是：

> 我们选择一个 equivalence relation。

而是：

> 未来 operation/observation language 实际能不能区分这两个状态？

因此 P023/A2 的 future-compatible quotient 应逐渐重写成：

\[
\boxed{
\text{causal signature equality}
\to
\text{quotient representation}.
}
\]

quotient 是表示，future indistinguishability 才是因。

## 7. Traditional linear algebra 被吞并

若 LEGO composition 是 free integer addition，且 causal operations preserve composition：

\[
T(x\oplus y)=T(x)\oplus T(y),
\]

则 operation 由 unit images：

\[
T(e_i)
\]

完全决定，integer matrix 只是 unit-effect table。

对 future signature 再取 integer-linear observation special case，得到：

- kernel = signature-invisible motion；
- rank = signature-visible independent freedom count；
- basis = minimal future probe generator；
- observability matrix = future probes 的 coordinate table。

所以 linear algebra 是：

\[
\boxed{
\text{LEGO composition}
+\text{causal signature}
\text{ 的特殊 shadow}.
}
\]

## 8. Traditional topology / ultrametric 被吞并

finite-depth equivalence classes：

\[
U_t(x)=[x]_{\equiv_t}
\]

形成 clopen basis。

第一次 future signature 分叉深度：

\[
s(x,y)=\min\{t:x\not\equiv_t y\}
\]

满足：

\[
\boxed{s(x,z)\ge\min(s(x,y),s(y,z)).}
\]

所以：

- topology = future-signature filtration 的 neighborhood shadow；
- ultrametric = integer agreement depth 的可选数值重编码。

## 9. Traditional metric / norm 的位置

另一类几何来自 operation cost：

\[
\ell(x\to y)
=
\text{使 }x\text{ 演化到 }y\text{ 的最短 causal program cost}.
\]

P012 graph metric 是这一方向的现有 special case。

所以进取数论至少有两类不同的 derived geometry：

1. **transport geometry**：实际走过去要多少 primitive operations；
2. **distinguishability geometry**：要多深未来才能区分。

不得因为传统数学习惯就把二者强制塞进同一个 norm。

## 10. Traditional measure / probability 被部分吞并

对 finite collapse signature class：

\[
[y]=C_\Sigma^{-1}(y),
\]

其 coarse weight 先定义为：

\[
\boxed{m(y)=|[y]|.}
\]

即该 coarse signature 吞掉多少 fine unit histories。

finite event weight：

\[
\mu(A)=\sum_{y\in A}m(y).
\]

传统 probability 只有在额外采用 uniform sampling semantics 后，才把：

\[
(\mu(A),N)
\]

渲染成比值。

所以 finite counting measure 是 signature-fiber multiplicity 的 shadow；general probability 尚未被吞并。

## 11. Traditional nonlinearity / Taylor 被部分吞并

若 operation 不 preserve LEGO composition，先研究具体 unit coexistence interaction：

\[
I(A)
=
\sum_{B\subseteq A}
(-1)^{|A|-|B|}T(B).
\]

这是 exact finite interaction，不是 Taylor approximation。

对 indistinguishable repeated units，fiber-local response：

\[
\phi(n)
=
\sum_k a_k\binom nk.
\]

整个 collapse response：

\[
\boxed{
\sum_y\phi(m_y)
=
\sum_k a_kJ_k.
}
\]

因此 P011 `J_k` 是 symmetric repeated-unit nonlinear response 的 interaction carrier。

传统 polynomial moments / collision probabilities / entropy scalars 由此降为后坐标或后渲染。

## 12. CS-05 —— traditional-tool absorption criterion

传统结构 `T` 若要进入 core，必须证明存在：

\[
\boxed{
\text{causal signature object }S
\quad\text{使}\quad
T=\text{Shadow}(S)
}
\]

其中 Shadow 至少满足：

1. 不改变哪些 future distinctions 实际存在；
2. 不偷偷增加 hidden continuum state；
3. 不要求未声明的 causal operation；
4. 可以从 signature/collapse 结构精确恢复，或明确只是 lossy rendering。

否则 `T` 只能是外部工具。

## 13. 当前 status table

### 已有第一阶段 causal derivation

- quotient / congruence；
- finite integer linear kernel/rank/observability；
- causal probe basis；
- finite-depth clopen topology；
- non-Archimedean agreement depth；
- P012 graph/word metric special case；
- finite counting measure；
- exact count-ratio probability shadow；
- LEGO interaction spectrum；
- P011 collision-interaction basis。

### 尚未吞并

- arbitrary real vector spaces；
- Euclidean inner product as primitive；
- general norm；
- manifolds；
- calculus as foundation；
- Hilbert/Banach completion；
- arbitrary probability measure；
- continuous stochastic processes；
- Lebesgue measure；
- quantum amplitudes。

## 14. 研究边界

Causal Signature Core 当前只是项目级 research orientation，不声称这些传统工具的一般数学是原创。

很多局部工具属于成熟领域：automata equivalence、linear observability、Möbius/binomial inversion、counting measure、graph metric、ultrametric filtration 等。

真正要验证的是整体方向：

> **是否能让越来越多传统数学结构变成同一个 finite causal signature calculus 的不同 shadows，从而停止“传统数学本体 + precision 标签”的路线。**

## 15. 当前可执行资产

- `causal_future_module.py`
- `causal_probe_basis.py`
- `lego_additive_operation.py`
- `causal_count_measure.py`
- `lego_interaction_spectrum.py`
- `collision_interaction_basis.py`

及其对应 tests。

## 16. 下一阶段唯一主攻

暂时不再横向增加 traditional invariant。

下一阶段优先研究：

\[
\boxed{
\text{signature composition law}
}
\]

即：

1. 两个 causal subsystems 拼接后，future signature 如何由子系统 signature 生成；
2. collapse 后 signature 是否仍可组合，而无需恢复 fine state；
3. 什么条件下 transport geometry、interaction spectrum、counting weight 都能通过同一个 signature quotient 下沉；
4. 找出第一个不能被 signature core 吞并的传统工具，明确理论边界。
