# P005 —— Projective precision completion 与 realization 边界，补充 01

状态：`PROVED RESEARCH NOTE`  
归属：A0 / P005 scale-refinement foundation，并桥接 P023 task precision  
依赖：P005 compatible finite refinement、P023 finite task quotients、P017 L077 split-profile 例子  
纪律：inverse limit、product topology、density、compactness 与 countability 都属于标准数学。本补充的项目贡献，是把 finite precision 的 realization 边界显式写成可复用定理。

## 1. Compatible finite refinement 背后缺失的问题

P005 已经允许兼容的 finite refinements，而不预设唯一 hidden fine state。

当存在可数多个兼容 precision coordinates 时，会自然出现一个更强问题：

> 如果每个有限坐标集合都被全部实现，是否意味着每个兼容的无限 coordinate profile 都对应某个 actual state？

答案是否定的。

有限 surjectivity 精确给出的只是 actual image 在 projective completion 中的**稠密性**。要得到全局 realization，还需要额外 global closure principle。

## 2. Finite product system

令 coordinate index set 为 countably infinite：

\[
I=\{1,2,3,\ldots\},
\]

每个 coordinate alphabet `A_i` 都有限且非空。

对有限

\[
F\subset I,
\]

定义

\[
Q_F=\prod_{i\in F}A_i.
\]

若 `F subseteq G`，令

\[
\pi_{G,F}:Q_G\to Q_F
\]

删除 `F` 外坐标。

这些 projection 满足 identity 与 path independence：

\[
\pi_{H,F}=\pi_{G,F}\circ\pi_{H,G}.
\]

其 inverse limit 自然同构于

\[
\boxed{
Q_\infty
=\varprojlim_FQ_F
\cong
\prod_{i\in I}A_i.
}
\]

## 3. Actual state image

令 `X` 为 actual state space，并令

\[
\Phi:X\to Q_\infty
\]

记录全部声明 coordinates。

记

\[
A=\Phi(X)
\subseteq Q_\infty
\]

为真正实现的 profiles。

对每个有限 coordinate set `F`，finite precision shadow 为

\[
\Phi_F=\pi_F\circ\Phi:X\to Q_F.
\]

## 4. P005-S1-T01 —— 所有有限 shadow 全实现等价于 density

状态：`PROVED`。

以下两条等价：

1. 对每个有限 `F`，finite projection `Phi_F` 都满射；
2. actual image `A` 在 `Q_infty` 的 product topology 中稠密。

### 证明

product topology 的 basic open cylinder 只固定有限多个 coordinates，设其索引为 `F`，并指定一个 pattern `a in Q_F`。

若所有 finite projections 都满射，则存在 actual state 实现该 pattern，所以每个非空 cylinder 都与 `A` 相交，因此 `A` 稠密。

反过来若 `A` 稠密，则每个 finite pattern 对应的 cylinder 都与 `A` 相交，于是每个 `Q_F` 中所有 patterns 都被 actual state 实现。∎

所以

\[
\boxed{
\text{all finite shadows surjective}
\iff
\text{actual image dense in completion}.
}
\]

结论只是 dense，不是 equality。

## 5. P005-S1-T02 —— Countable finite-support 反例

状态：`PROVED`。

取 binary alphabets

\[
A_i=\{0,1\}
\]

并令 `X` 为所有 finite-support binary sequences：

\[
X
=
\{x\in\{0,1\}^{\mathbb N}:\#\{i:x_i=1\}<\infty\}.
\]

则：

1. `X` 可数；
2. 任意 finite binary pattern 都能由某个 finite-support sequence 实现；
3. 因此 `X` 在 full Boolean product 中稠密；
4. 但
   \[
   \{0,1\}^{\mathbb N}
   \]
   不可数，所以 `X` 是严格真子集。

因此

\[
\boxed{
\text{每个有限 precision level 全实现}
\not\Rightarrow
\text{每个 inverse-limit point 都实现}.
}
\]

这就是 P017 L077 split-profile 现象的抽象母版本。

## 6. P005-S1-T03 —— Closed-image realization theorem

状态：`PROVED`。

假设所有 finite shadows 满射，并且 actual image

\[
A\subseteq Q_\infty
\]

在 product topology 中 closed。

T01 已给出 `A` dense。一个同时 dense 与 closed 的 subset 只能等于整个空间。因此

\[
\boxed{
A=Q_\infty.
}
\]

所以 **closedness 正是 finite shadow data 所缺少的一个充分 global realization principle**。

在 finite-shadow-surjective 的前提下，它同时也是必要的：若 `A=Q_infty`，当然 closed。

因此

\[
\boxed{
\text{finite shadow surjectivity}
+
\text{closed actual image}
\iff
\text{full completion realization}.
}
\]

## 7. P005-S1-T04 —— Compact-source 推论

状态：`PROVED / STANDARD TOPOLOGY`。

若 `X` 是 compact topological state space，每个 coordinate alphabet 是 finite discrete，并且

\[
\Phi:X\to Q_\infty
\]

连续，则 product `Q_infty` 为 Hausdorff，compact image `Phi(X)` 因而 closed。

若所有 finite shadows 又满射，则由 T03

\[
\boxed{
\Phi(X)=Q_\infty.
}
\]

所以 compactness + continuity 是一条 concrete route，使 finite realizability 真正推出 projective realization。

它是 finite-support 反例的正向边界。

## 8. P005-S1-T05 —— 有限 precision data 无法区分 dense proper image 与 full completion

状态：`PROVED`。

令 `A` 是 `Q_infty` 的任意 dense proper subset。

对每个 finite coordinate set `F`，都有

\[
\pi_F(A)=Q_F.
\]

所以任何只依赖有限多个 coordinate values 的 statement，在允许 global state space 为 `A` 或为 full completion `Q_infty` 时，看到的 finite possibilities 完全相同。

但两个 global state spaces 不同。

因此

\[
\boxed{
\text{finite observational completeness}
\not\Rightarrow
\text{global ontological equality}.
}
\]

这是一条数学 indistinguishability statement，不是关于自然界的经验主张。

## 9. P005-S1-T06 —— Free finite-shadow model 没有 finite basis

在 finite-support Boolean 反例里，把所有 coordinate tasks 都作为 task language。

任何有限 coordinate set 都不能决定某个遗漏 coordinate：固定 finitely many bits 后，仍可以让某个遗漏 bit 取 0 或 1，同时保持 finite support。

因此对每个 finite task subset `S`，

\[
\boxed{
\operatorname{cl}(S)=S.
}
\]

整个 infinite task language 没有 finite basis。

所以“每个 finite precision level 都 finitely generated”并不推出整个 projective task language finitely generated。

## 10. Finite-intersection-property 版本

对一个 formal completion profile

\[
a=(a_i)_{i\in I},
\]

对每个有限 `F subset I` 定义 actual-state constraint set

\[
\boxed{
X_F(a)
=
\{x\in X:\Phi_i(x)=a_i\text{ for all }i\in F\}.
}
\]

所有 finite shadows 满射意味着：对每个有限 `F`，

\[
X_F(a)\ne\varnothing.
\]

而且

\[
X_{F_1}(a)\cap\cdots\cap X_{F_m}(a)
=
X_{F_1\cup\cdots\cup F_m}(a),
\]

所以这些 constraint sets 具有 finite intersection property。

但 profile `a` 真由某个 actual state 实现，要求

\[
\boxed{
\bigcap_{F\subset I\atop F\text{ finite}}X_F(a)
e\varnothing.
}
\]

finite-support counterexample 表明，finite intersection property 本身并不保证全局 intersection 非空。

如果 `X` compact 且各 coordinate fibers closed，则 compactness 恰好把 FIP 提升成非空 total intersection。这与 T03/T04 是同一 realization principle 的 constraint-set 版本。

因此 missing completion point 可以精确理解为：

\[
\boxed{
\text{每个 finite constraint subsystem 都有 actual witness，}
\text{但不存在一个同时满足全部 constraints 的 global witness}.}
\]

## 11. 与 P017 L077 的关系

P017 提供了这套结构的真实算术特化。

其 all-prime split profile

\[
I(k)=(I_p(k))_p
\]

对每个 actual basin `k` 都 finite support；由 L074/L076，每个 finite prime projection 都是 full Boolean cube；actual image 可数、dense，却严格小于 infinite Boolean completion。

所以 P017 不是 T02 的类比，而是 P005 projective-realization boundary 的真正 number-theoretic specialization。

## 12. 与 P023 future-safe precision 的关系

P023 研究声明 finite future language 需要保留哪些 distinctions。

P005-S1 说明：即使**每一个** finite language 都有 fully populated exact quotient，形式上把所有 finite languages 取极限得到的 infinite completed task state，仍可能含有 actual state 从未产生的 ideal profiles。

因此

\[
\boxed{
\text{all finite task quotients}
\longrightarrow
\text{infinite completed task state}
}
\]

是额外数学 construction，不是 finite future compatibility 自动给出的 theorem。

要证明 completion realization，必须另给 closedness / compactness 一类 global hypothesis。

## 13. 基础后果

Enterprise Math 现在可以严格区分三件事：

1. **finite compatibility** —— projections commute，每个 finite quotient 精确；
2. **finite realizability** —— 每个 finite quotient state 都由某个 actual state 产生；
3. **completion realizability** —— 每个兼容 infinite profile 都由某个 actual state 产生。

前两条不推出第三条。

所以一个理论可以一致地使用任意多兼容 finite precision levels，而不把 completed infinite object 自动放进 primitive ontology。

这不是禁止 completion；而是要求在没有 global realization theorem 前，把 completion points 标成 **formal / ideal**。

## 14. 可执行规范

- `src/enterprise_math/projective_precision_completion.py`
- `tests/test_projective_precision_completion.py`

可执行模型用 canonical finite-support profile 实现每个 tested finite binary coordinate set 上的所有 patterns。countability、density、properness 与 closed-image theorem 是本文的数学证明，而不是 finite computation claim。

## 15. 前人工作与新颖性纪律

Inverse limits、product topology、cylinder sets、dense subsets、compact-image closedness，以及 Boolean product 中 finite-support dense subset，都属于 established mathematics。

项目新增的是显式 realization taxonomy：

\[
\boxed{
\text{finite compatibility}
\to
\text{finite realizability}
\to
\text{completion realizability},
}
\]

并指出其中缺失的 closedness principle，以及 P017 的算术特化。
