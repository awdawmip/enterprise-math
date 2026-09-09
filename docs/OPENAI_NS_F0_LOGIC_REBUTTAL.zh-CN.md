# 对 OpenAI Navier–Stokes 构造的逻辑反驳

## 为什么“先造目标、再用残差定义外力”不能回答无外力问题 \(f\equiv 0\)

状态：`研究笔记 / 逻辑审计 / 尚未独立复核`

日期：`2026-09-09`

冻结来源：`openai/NavierStokesAndEuler@8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`

进取数论研究路线：`UNFORCED / f ≡ 0 / AUTONOMOUS_SELF_STATE_INSTABILITY`

`AUTONOMOUS_SELF_STATE_INSTABILITY` 是研究方向标签，不是已经证明的定理。

## 核心结论

OpenAI 自己的仓库元数据已经明确：其 Navier–Stokes 结果讨论的是**带光滑外力**的有限时间爆破；Comparator 中的 (C) 选项也明确把外力 \(f\) 放在存在量词中。因此，对这一证明的批评必须把对象说准。

本文**不**声称 Lean 内核不可靠，也**不**声称仅凭下面这一条逻辑批评，就已经推翻 OpenAI 明确写出的强迫型 (C)/(D) 定理。若一个定理本身就允许把外力作为存在见证的一部分来选择，那么从候选场反向构造外力，原则上可以是该“强迫型定理”中的合法见证策略。

本文反驳的是另一种更强、也更容易被偷换的推论：

> 先规定一个带目标奇点的候选解，再把它不满足方程的部分定义成外力；随后证明该外力在选定奇点附近很小、无穷阶平坦，或者在 blow-up 缩放下消失——这些事实**不能**因此变成对无外力方程 \(f\equiv0\) 的证明、近似证明或内生不稳定性证据。

对无外力 Navier–Stokes 问题而言，这是一种目标泄漏。进取数论正式将其列入项目级**逻辑黑名单**，命名为：**目标泄漏式残差补全（target-imprinted residual completion）**。

## 1. 冻结版本的 OpenAI 源码实际证明什么

冻结版本的 `formalization.yaml` 明确写明：其 Navier–Stokes 部分针对三维不可压方程的**光滑外力有限时间爆破**，并覆盖正黏性下的 \(\mathbb R^3\) 与周期情形。列出的主结果是强迫型 breakdown alternatives (C) 与 (D)。

其中 (C) 的量词结构是

\[
\exists u_0\;\exists f\;\bigl(\text{初值满足条件}\bigr)\land
\bigl(\text{光滑外力满足条件}\bigr)\land
\neg\exists\text{ 全局光滑解}.
\]

这是一条“存在某个外力”的定理，不是

\[
f\equiv0.
\]

固定源码：

- [`formalization.yaml`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/formalization.yaml)
- [`ComparatorChallenges/NavierStokes.lean`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/ComparatorChallenges/NavierStokes.lean)
- [`NavierStokes/ComparatorSolution.lean`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/ComparatorSolution.lean)

任何不区分这两个量词目标的评价，本身也会失真。

## 2. 被列入黑名单的逻辑：先规定答案，再补残差

记

\[
\mathcal R(u,p)
:=
\partial_tu-\nu\Delta u+(u\cdot\nabla)u+\nabla p,
\]

同时附带散度为零约束。

真正的无外力目标是全局恒等式

\[
\mathcal R(u,p)\equiv0.
\tag{U}
\]

逻辑黑名单中的模式是：

1. 先指定或构造一个已经带有所需终点奇性的 \((u,p)\)；
2. 再定义
   \[
   f:=\mathcal R(u,p);
   \]
3. 证明这个 \(f\) 光滑、很小、衰减、在某个点无穷阶平坦，或者在某种 blow-up 缩放下趋于零；
4. 然后把第 3 步当作“奇性本来就是 \(f=0\) 自主演化产生的”证据。

对目标 (U) 而言，第 4 步无效。

最核心的逻辑差异只有一行：

\[
\left[
\mathcal R(u,p)=f,
\quad
D^\alpha f(T,x_*)=0\ \forall\alpha
\right]
\not\Rightarrow
\left[
\mathcal R(u,p)\equiv0
\right].
\tag{1}
\]

即使 \(f\) 在一个时空点的所有 jet 全部为零，也依然只是局部条件；而无外力要求的是整个时空域上的全局恒等式。

这不是数值精度问题，而是量词与目标对象发生了替换。

## 3. 奇点处无穷阶平坦，不等于外力为零

冻结 OpenAI 源码实际上做得比“光滑”更强：它要求选出的 residual 在奇点处具有 vanishing joint jets，最终外力在该点也继承零边界 jet。

这在数学上很强，但并不会改变式 (1)。

同一套 formal consequence 又证明最终外力在爆破时间之前的某个时空点**确实非零**。因此下面两句话完全可以同时成立：

\[
D^\alpha f(T,x_*)=0\quad\forall\alpha
\]

和

\[
f\not\equiv0.
\]

固定源码：

- [`NavierStokes/MixedCandidateWitness.lean`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/MixedCandidateWitness.lean)
- [`NavierStokes/MixedPeriodicAssembly.lean`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/MixedPeriodicAssembly.lean)
- [`NavierStokes/CandidateConsequences.lean`](https://github.com/openai/NavierStokesAndEuler/blob/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538/NavierStokes/CandidateConsequences.lean)

因此必须冻结：

`FLAT_AT_SINGULAR_POINT != ZERO_FORCE`。

## 4. blow-up 缩放后外力趋零，不等于原始轨道无外力

即使围绕 \((T,x_*)\) 做抛物缩放后，rescaled force 在每个固定紧集上趋于零，也最多说明某个**局部切向极限方程**可能是无外力的。

它不说明原始轨道从一开始就是由 \(f\equiv0\) 产生的。

原始演化可以在更早的时间、或者别的空间区域受到非零外力。Navier–Stokes 的压力与 Leray 投影具有非局部性，奇点尺度上的速度保留的是整个全局强迫轨道的历史，而不是只看最后一个局部 jet。

因此：

`ZOOM_LIMIT_UNFORCED != ORIGINAL_TRAJECTORY_UNFORCED`。

局部渐近不能替换全局动力学前提。

## 5. Lean 能证明什么，不能替你决定什么

证明助手回答的是一个严格类型化的问题：

> 在已经编码的定义和前提下，这个结论能否被推出？

如果被编码的 theorem 是强迫型 (C)/(D)，一个正确的 Lean proof 当然只证明那个强迫型 theorem。Lean 内核不会自动替研究者判断：另一个非形式化目标是不是才是真正想解决的问题。

因此：

`FORMAL_VERIFICATION != SEMANTIC_TARGET_EQUIVALENCE`。

一个再漂亮的 proof term，也不能把

\[
\exists f\neq0\text{，且 theorem 允许选择它}
\]

变成

\[
f\equiv0.
\]

这不是对形式化证明的贬低，恰恰说明：**形式正确性越强，越需要先审计 formal statement 是否就是目标本身。**

## 6. 为什么这种残差补全在我们的 \(f=0\) 路线中属于循环

进取数论现在把无外力路线冻结为：

\[
\boxed{f\equiv0\text{ 从第一条前提一直保持到最终结论}.}
\]

因此，以下研究路径在本项目中被禁止：

\[
\text{先规定想要的奇点轮廓}
\longrightarrow
\text{再定义残差外力}
\longrightarrow
\text{证明外力局部很小/平坦}
\longrightarrow
\text{声称得到内生不稳定性}.
\]

在真正解出自主 PDE 之前，终点目标已经参与了 witness 的设计；剩余不匹配部分又被外力补掉。对于 \(f=0\) 定理，这叫目标泄漏式残差补全，不叫自主不稳定性推导。

我们的路线反过来：

\[
\boxed{
\text{先固定 }f\equiv0
\;\longrightarrow\;
\text{只允许方程本身产生演化}
\;\longrightarrow\;
\text{再问状态能否自己失稳}.
}
\]

我们把这个研究方向称为：**自态自主不稳定（autonomous self-state instability）**。

它比“安排一个带外力的轨道在终点奇异”严格得多。

## 7. 自主路线中的 BRC 要求

在 \(f=0\) 路线中，所有分支来源必须在压缩之前保留。尤其是 helicity 符号、shell/band 身份、迭代代际以及复相位，不能在真正的消去问题解决之前被提前做绝对值、平方或总量化。

正权总量不能代替 signed cancellation theorem：

`POSITIVE_WEIGHTED_BRC != SIGNED_OR_PHASE_CANCELLATION`。

因此真正的结构目标不是先指定奇点，再去修 residual；而是直接在自主网络内部证明：

- 要么存在能在 \(f=0\) 下穿过黏性耗散的内生不稳定机制；
- 要么存在足够强的 coercive/cancellation 结构，证明这种失稳不可能发生。

两种结果都是真结果；任何一种都不能靠把缺失项重新包装成外力来制造。

## 8. 本文反驳的准确边界

本文建立的是一个语义与逻辑边界，不是对 OpenAI 仓库每一条 lemma 的内部反例。

本文**直接反驳**下面这种推论：

> “既然工程化外力在选定奇点处无穷阶平坦，或者在 blow-up 缩放后消失，那么这个构造已经回答了无外力 Navier–Stokes。”

本文**没有仅凭这一条批评就推翻**其明示的强迫型 (C)/(D) theorem，因为这些 theorem 本来就允许存在量词中的非零外力。

如果要继续直接推翻强迫型 C/D 本身，就必须找到另一个真正的内部缺陷，例如：错误的分析 lemma、source theorem 与 Comparator statement 不一致、非法的极限交换、错误的 extension/gluing、或者不被允许的依赖。

这个边界必须写清楚。进取数论不能用一种目标偷换去反对另一种目标偷换。

## 9. 项目逻辑冻结

进取数论现在对相关研究启用以下规则：

- `FORCING_IDENTICALLY_ZERO_FROM_PREMISE_TO_CONCLUSION`：无外力 Navier–Stokes 路线必须从头到尾保持 \(f\equiv0\)；
- `FLAT_AT_SINGULAR_POINT != ZERO_FORCE`；
- `ZOOM_LIMIT_UNFORCED != ORIGINAL_TRAJECTORY_UNFORCED`；
- `FORMAL_VERIFICATION != SEMANTIC_TARGET_EQUIVALENCE`；
- `TARGET_IMPRINTED_RESIDUAL_COMPLETION -> LOGIC_BLACKLIST`；
- `AUTONOMOUS_SELF_STATE_INSTABILITY -> RESEARCH_DIRECTION_NOT_THEOREM`。

通用黑名单规则维护在 [`LOGIC_BLACKLIST.zh-CN.md`](LOGIC_BLACKLIST.zh-CN.md)。
