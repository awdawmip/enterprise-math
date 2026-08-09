# R004 精度宇宙生成 —— Supplement 02：局域性 obstruction、latent capacity、最小 bridge 与派生 record overlap

状态：`PROVED_WIP + EXECUTABLE_CHECKED + COUNTEREXAMPLE + PRIOR_ART + PHYSICAL_HYPOTHESIS`  
Parent：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_01.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

本补充继续攻击 Supplement 01 留下的最尖锐 frontier：

> 什么具有独立动机的有限结构限制，能够阻止完整 latent / pre-sampled completion，同时把 hierarchy geometry 推向 connected space，并把 P016 从自由 overlap 参数推向可派生 observable？

这里第一次对 latent-completion 问题得到**部分正面答案**，但答案依赖明确的 Bell-locality 假设。本补充不主张 `CANONICAL_MAIN`，不证明 cosmological genesis，也不证明无条件的 ontic randomness。

## 1. 第一个能真正阻止 complete local pre-sampling 的 operational obstruction

Supplement 01 已证明：若允许任意 counterfactual response table，则 finite deterministic tower、finite rational stochastic kernel，甚至 finite adaptive intervention policy 都存在有限 pre-sampled completion。

现在的新动作，是在看结果之前就对这些 response table 加入独立限制。

考虑两个空间分离的二元响应端。Alice 选择 setting `x in {0,1}`，Bob 选择 setting `y in {0,1}`。一个 deterministic **setting-local** latent table 写成

\[
\lambda=(A_0,A_1,B_0,B_1),
\qquad
A_x,B_y\in\{-1,+1\},
\]

其中 Alice 的值只依赖 `x` 与 latent seed，不依赖 Bob 的 setting；Bob 的值只依赖 `y` 与同一个 latent seed，不依赖 Alice 的 setting。

第二个限制是 **measurement-setting independence**：四组 setting pair 使用同一 latent-seed multiplicity / probability 分布。在 finite integer 实现里，每个 local table 只预先赋一个非负整数 weight `w_lambda`，setting pair 选择之后不能改变这组 weight。

这是实质 causal restriction，而不是 finiteness 自动推出的性质。

## 2. 有限 local table 的 exact integer CHSH theorem

对一个 deterministic local table，定义

\[
S_\lambda
=A_0B_0+A_0B_1+A_1B_0-A_1B_1.
\]

改写为

\[
S_\lambda
=A_0(B_0+B_1)+A_1(B_0-B_1).
\]

因为 `B_0,B_1` 都只能取 `+1` 或 `-1`，两个括号中恰有一个为零，另一个为 `+2` 或 `-2`。所以

\[
\boxed{S_\lambda\in\{-2,+2\}.}
\]

一共有十六个 deterministic local tables。R004 穷举全部十六个，得到八个 `-2`、八个 `+2`。

现在给每个 table 一个非负整数 multiplicity `w_lambda`，并令

\[
W=\sum_\lambda w_\lambda>0.
\]

四组 setting pair 共用同一组 multiplicities。定义四个 correlation numerators

\[
C_{xy}=\sum_\lambda w_\lambda A_x(\lambda)B_y(\lambda).
\]

则

\[
C_{00}+C_{01}+C_{10}-C_{11}
=\sum_\lambda w_\lambda S_\lambda,
\]

由普通整数三角不等式直接得到

\[
\boxed{
|C_{00}+C_{01}+C_{10}-C_{11}|\le2W.
}
\]

若除以公共正 weight `W`，就是通常的 CHSH bound `|S|<=2`。R004 的 executable primitive 保留交叉乘后的纯整数形式。

该定理属于 Bell/CHSH 成熟数学，不是 Enterprise Math 新发明 [SRC-BELL-1964-EPR; SRC-CHSH-1969]。R004 的新增点只是：把这个成熟 obstruction 精确用来堵自己前一阶段暴露出的 finite pre-sampled-completion loophole。

## 3. 一个完全有理、但落在 local completion class 之外的 quantum target

常见最大 CHSH 例子会写到 `sqrt(2)`。R004 不需要这种形式。

取平面 unit directions

\[
a_0=(1,0),
\qquad a_1=(0,1),
\]

以及勾股有理方向

\[
b_0=(3/5,4/5),
\qquad b_1=(3/5,-4/5).
\]

对 spin singlet，标准量子相关为

\[
E(a,b)=-a\cdot b.
\]

于是四个 exact correlations 为

\[
(E_{00},E_{01},E_{10},E_{11})
=
(-3/5,-3/5,-4/5,+4/5).
\]

按前述 CHSH 符号约定，

\[
S
=E_{00}+E_{01}+E_{10}-E_{11}
=-14/5,
\]

因此

\[
\boxed{|S|=14/5>2.}
\]

整个构造不需要 floating point，也不需要 irrational direction。

若二元 singlet marginals 无偏，则对应 joint probabilities

\[
P(A=a,B=b\mid x,y)
=\frac{1+abE_{xy}}4
\]

全部都是 `1/20` 的整数倍。因此 R004 可以把 target 直接写成 exact twenty-atom count tables。`E=-3/5` 时，按 `(--,-+,+-,++)` 排列的 counts 是 `(2,8,8,2)`；`E=-4/5` 时是 `(1,9,9,1)`；`E=+4/5` 时是 `(9,1,1,9)`。

因此，一个完全 finite + rational 的 observable target 已经足以落在 setting-local、setting-independent pre-sampled class 之外。

## 4. 这对“生成”到底说明了什么，又没有说明什么

这是 R004 generative-identifiability 问题第一次得到部分正面答案：

\[
\boxed{
\text{locality + setting independence + pre-sampling}
\Longrightarrow |S|\le2,
}
\]

而 exact finite rational target 有 `|S|=14/5`。

所以**这一受限的 latent-completion class 在 operational 上可以与 target 区分**。

但结论绝不能越界。它没有排除：

- nonlocal hidden-variable completion；
- latent state 与未来 measurement settings 统计相关的模型；
- superdeterministic 或其他 measurement-dependence construction；
- 拒绝被检验 singlet correlation law 的其他物理模型；
- 关于 outcome 在什么时候成为 ontically real 的任意形而上结论。

Hensen 等人的 Bell test 在其实验中关闭了 locality 与 detection loophole [SRC-HENSEN-2015-BELL]；Bell-certified randomness 也已有成熟 device-independent 文献 [SRC-PIRONIO-2010-BELL-RANDOMNESS]。R004 把它们当作压力测试使用，不把一次 Bell violation 夸成对整个 precision-genesis ontology 的无条件证明。

R004 剩下的问题现在进一步变窄：

> Enterprise Math 能否从自己的 finite causal / geometry layer **推导或独立论证** locality 与 setting independence，而不是为了继承 Bell theorem 临时插入它们？

## 5. 第二种 obstruction：有限初始 latent capacity

Locality 不是唯一可能的限制。另一条候选路线，是给初始 latent carrier 一个硬的有限资源上界。

设某个 declared future language 有 `m` 个 step，每步有 `r>=1` 种可能 response。完整 response strings 数量就是

\[
\boxed{r^m.}
\]

设一个 deterministic pre-sampled seed state 只能选择一条完整 response string。如果 target future law 具有 **full support**——所有 `r^m` 条 string 都必须有正概率——那么 seed-to-string map 必须是 surjective。因此

\[
\boxed{|U|\ge r^m.}
\]

这个下界不需要 logarithm，也不要求 probability 必须 rational；它只是有限 surjectivity counting。

而且 bound 是 sharp 的：取 `r^m` 个 seed states，每条 response string 一个 seed state，就达到这个 state-count 下界；在目标概率可以由这些 seed weights 表示时再赋相应正 weight 即可。

如果初始 seed capacity 是有限整数 `K`，那么能够 complete pre-sample 的最大 full-support horizon，就是满足

\[
r^m\le K
\]

的最大整数 `m`。

Executable layer 通过有限整数乘法求这个值，不引入 `log_r K`。

### Precision-one corollary

如果 R004 的强 pregeometry 语义真正要求：precision one 只有一个完整 physical state，而且**不存在额外 hidden carrier**，那么 `K=1`。此时哪怕只有一个 genuinely two-outcome、full-support 的未来 step，deterministic complete pre-sampling 也需要 `K>=2`，因此无法被塞进该初始 ontology。

这仍没有说明第二个 outcome 究竟通过什么物理机制产生；它只说明：一旦“一状态 + 无隐藏载体”被认真当成 ontology，all-at-once deterministic latent encoding 就已经不可用。

## 6. 最小 cross-fiber bridges：connectedness 的 exact cost

Supplement 01 已证明 nested refinement 自然产生 ultrametric，但不保证 connected local space。

现在把 nested precision classes 看成一棵有限 rooted refinement tree。对每个 parent class `v`，记

\[
c(v)=v\text{ 的 immediate child classes 数量}.
\]

加入**由真实 leaves 见证的 edges**。一条 edge 只有在两个 leaf endpoints 落在 `v` 的不同 immediate children 时，才算作 `v` 的 bridge。

要让 `v` 的 child quotient graph 连通，至少需要

\[
c(v)-1
\]

条这样的 bridge witnesses。

Nestedness 保证任意 leaf edge 都有唯一 first-divergence parent，所以同一条 edge 不可能同时替两个不同 parents 支付 cross-child connectivity cost。因此任何 bridge certificate 至少需要

\[
\sum_v(c(v)-1)
\]

条 leaf edges。

在 one root 且 final classes 都是 singleton 的情形，refinement-tree 计数精确望远镜化：

\[
\boxed{
\sum_v(c(v)-1)=|X|-1.
}
\]

反过来，在每个 parent 的 child quotient 上各选一棵 spanning tree，并由真实 leaf edge 见证，就能精确实现这么多 edges。由 leaves 向上归纳，最终 leaf graph 连通。因此

\[
\boxed{
\text{minimum immediate-child bridge certificate size}=|X|-1.
}
\]

得到的 leaf graph 是一棵 spanning tree，因此也是全局 connectivity 意义下 edge-minimal 的。

这属于成熟 finite tree / graph mathematics 在 R004 refinement hierarchy 上的 specialization，不主张它是新 graph theorem。

## 7. Minimum connectivity 仍不能决定 macroscopic geometry

Exact connectivity cost 补上了一块缺口，但马上暴露下一块缺口。

在八个 leaves、scale `(1,2,4,8)` 的 binary hierarchy 上，minimum bridge count 是 7。R004 在**同一个 hierarchy**上构造两套不同的七边 certificate：

1. first-representative witness tree，graph diameter 为 `5`；
2. ordered boundary-witness tree，恰好得到 path `0-1-2-3-4-5-6-7`，diameter 为 `7`。

两者都用 exact minimum `|X|-1=7` 条 edges，并且都连通每一个 immediate child quotient。

所以

\[
\boxed{
\text{hierarchy + minimum connectedness}
\not\Rightarrow
\text{unique macroscopic geometry}.
}
\]

下一层 geometry variable 必须约束**哪些** cross-fiber witnesses 在物理上 admissible，例如 translation symmetry、bounded degree、homogeneous local neighborhoods、causal accessibility 或其他 exact finite condition，而不能只数 bridge 有多少条。

## 8. P016 continuation：从 finite record generator 派生 eta

第一版 R004 P016 premodel 把 environment-record overlap `eta` 当作预先声明参数。本补充在一个明确 toy subfamily 里去掉这个自由度。

令 finite environment state 为

\[
e\in\{0,1,\ldots,d-1\},
\]

其中 `d` 是正整数 resolution。定义 system state `x` 产生的 record：

\[
R_d(x,e)=\left\lfloor\frac{e+x}{d}\right\rfloor,
\]

实际实现使用 integer division。

比较两个 alternatives `x=0` 与 `x=delta`，其中 `delta>=0`。在 declared environment cell 内始终有 `R_d(0,e)=0`，两条 record 相等当且仅当

\[
e+\delta<d.
\]

因此 exact agreement count 为

\[
\max(d-\delta,0),
\]

若 toy environment cell 取 uniform，则

\[
\boxed{
\eta(d,\delta)=\frac{\max(d-\delta,0)}d.
}
\]

Executable formula 已在大量 bounded integer cases 上与逐状态 record enumeration 独立交叉核对。

如果继续采用

\[
V_{\mathrm{predicted}}=\eta V_{\mathrm{ordinary}},
\qquad 0\le V_{\mathrm{ordinary}}\le1,
\]

那么 Pedalino 报告的代表性 lower numerical endpoint `0.09` [SRC-PEDALINO-2026-NANOPARTICLE] 在 `eta<0.09` 时不可达到。在这个 derived subfamily 中条件精确等价为

\[
\boxed{100\delta>91d.}
\]

这是一个纯整数 cross-product inequality。它仍然只是 algebraic range exclusion，不是 confidence-level 结果。

决定性的 missing physical map 现在已经缩小成：

`real apparatus/environment -> integer record resolution d and alternative separation delta`。

在这个映射被独立 calibration 之前，`R004-THRESHOLD-RECORD-PREMODEL-V1` 仍然只是 `PHYSICAL_HYPOTHESIS`。

## 9. 修正后的 closure picture

R004 的 frontier 现在不再是一个混在一起的问题。

### Generative identifiability

任意 finite pre-sampling 可以穿过 deterministic refinement、rational randomness 与 adaptive interventions；但加入某些独立可检验限制后，它会真正失败。Bell locality + measurement-setting independence 是一个已证明的例子；hard finite initial seed-capacity bound 则是另一种纯 combinatorial resource restriction。

### Geometry

Nested refinement 给出 hierarchy / ultrametric。完整 immediate-child bridge certificate 以 exact minimum `|X|-1` 条 leaf edges 增加 connectedness；但 witness 如何选择仍会改变宏观 graph geometry。

### P016

Overlap variable 可以由具体 finite record map 派生，而不是事后自由拟合。未解决的工作已从 `eta` 的代数自由度转成 apparatus calibration。

三条线现在共同指向一个更强的 target：

> 用同一条 finite causal dynamics 同时派生 locality / resource bound、admissible cross-fiber bridges 与 record-generation parameters，然后让它面对不可避免的 joint predictions。

这会比继续添加互不相干的 toy mechanism 强一个层级，因为同一个 primitive law 必须同时穿过 Bell/locality boundary、geometry reconstruction 和 P016 falsification。
