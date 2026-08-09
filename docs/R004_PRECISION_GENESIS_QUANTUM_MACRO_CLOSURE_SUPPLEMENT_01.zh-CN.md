# R004 精度宇宙生成 —— 补充 01：精确缺陷分解、干预 no-go、层级几何与通用 adjunction

状态：`PROVED_WIP + EXECUTABLE_CHECKED + COUNTEREXAMPLE + PRIOR_ART + PHYSICAL_HYPOTHESIS`  
母文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE.zh-CN.md`  
Owner 分支：`research/r004-precision-genesis-closure-20260810`

本补充记录第一份 R004 报告之后得到的结果。不修改任何 numbered problem status，也不主张 `CANONICAL_MAIN`。

## 1. 历史碰撞谱增长的精确双机制分解

设 `n:X->N_0` 为当前 path-history multiplicities，`R subset X x Y` 为在 occupied support 上 serial 的有限 relation，并按 state-extensional 规则推进历史：

\[
n'(y)=\sum_{xRy}n(x).
\]

对每个 `k>=1` 定义

\[
W_k(n)=\sum_x {n(x)\choose k}.
\]

母报告已经证明 `W_k(n')>=W_k(n)`。现在可以进一步得到精确恒等式

\[
\boxed{W_k(n')-W_k(n)=B_k+C_k},
\]

其中

\[
B_k=\sum_x(\deg_R(x)-1){n(x)\choose k}
\]

以及

\[
C_k=\sum_y\left[
{\sum_{xRy}n(x)\choose k}
-\sum_{xRy}{n(x)\choose k}
\right].
\]

两项都是非负整数。`B_k` 是 **branch-copy growth**：已经共享同一当前终点的 k-history bundle 被复制到额外 successors；`C_k` 是 **cross-source growth**：来自不同当前终点的历史在同一 successor 上形成新的 k 重 coincidence。

因此 equality 条件也被完全拆开：只有两种机制同时为零时，`W_k` 才保持不变。特别是 `k=2` 时，只要一个已经发生历史碰撞的状态继续 branching，或者两个 occupied current states 出现共同 successor，`W_2` 就严格增长。

对 merge excess

\[
M(n)=\sum_x\max(n(x)-1,0),
\]

同样有

\[
\boxed{M(n')-M(n)=B_M+C_M},
\]

其中

\[
B_M=\sum_x(\deg_R(x)-1)\max(n(x)-1,0)
\]

以及

\[
C_M=\sum_y\max(p_y-1,0),
\]

`p_y` 是 incident 到 `y` 的 occupied current source states 数量。

这样不可逆量的增加被拆成两种不同的有限机制，而不是压成一个无法解释的 scalar。

## 2. 精确 path accounting 与 ambient capacity 仍然不同

定义

\[
H=\sum_x n(x),\qquad A=\#\{x:n(x)>0\},
\]

并令

\[
B=\sum_x n(x)(\deg_R(x)-1).
\]

则直接计数得到

\[
H'=H+B,
\]

又因为 `M=H-A`，得到

\[
\boxed{\Delta M=B-\Delta A}.
\]

这才是 toy dynamics 真正给出的 finite balance law。Ambient state capacity `|X_t|` 没有出现在恒等式里。因此 R004 目前仍没有定理把“宇宙可用状态容量增长”与“热力学熵产生”认定为同一个量或守恒交换量。

## 3. 更强的 generative-identifiability no-go：adaptive interventions 也不够

第一份报告已经证明 finite deterministic tower 与 finite-horizon rational stochastic process 都存在有限 latent / pre-sampled completion。现在该障碍可以推进到 finite adaptive interventions。

固定有限 horizon，把所有可能发生的有限 context 枚举出来。一个 context 可以包含时间、此前 observations，以及当前选择的 intervention。设每个 context `c` 都给出一个 finite rational response distribution `K_c`。

对每个 context 分别清分母，构造一个有限 uniform response table，使每个 outcome 出现恰好的 multiplicity。再把所有 context 的 local tables 做 Cartesian product。一个 product atom 会一次性给**所有可能 context**指定 deterministic response，包括实际 run 中永远不会访问的 context。

在初始时刻只需要抽取一个 product atom。之后 adaptive policy 可以根据之前看到的 response 选择下一 intervention；到达任何 realized context 时，只读取预先抽好的对应 coordinate，就会精确复现原来的 conditional/interventional response law。

因此在 finite classical rational scope 内：

\[
\boxed{
\text{finite adaptive intervention data}
\not\Rightarrow
\text{online ontic generation}
}
\]

除非再加入一个限制 admissible latent completions 的结构性条件。

所以缺失的东西已经不是“再加一个 intervention syntax”。候选限制必须具有独立内容，例如 locality、noncontextuality、causal independence、初始可用信息资源上界，或其他可以严格定义的条件。哪种限制既兼容 Enterprise Math 的有限 ontology，又具有独立物理依据，现在已经成为 Foundation-level 问题。

这一 representation mechanism 不是 R004 的新发明。Functional representation with independent auxiliary randomness 以及 structural-causal intervention semantics 都是成熟工具 [SRC-LI-ELGAMAL-2017-SFRL；SRC-PEARL-1995-CAUSAL-CALCULUS]。R004 的项目级新增意义在于用它们建立一个负面边界。

## 4. Refinement 自身可以诱导一种内禀 hierarchy geometry

母报告正确指出：distinguishability 增加不会自动强迫任意 adjacency relation。但 nested refinement 的确会自然产生一种几何。

设

\[
\lambda_0\mid\lambda_1\mid\cdots\mid\lambda_t
\]

是有限 divisibility chain，并给每个 current fine state 配置 compatible coarse-class sequence。要求这些 equivalence relations 嵌套，所有状态在 precision-one 层拥有同一个 root class，并且 final coordinate 能区分 current states。

对不同状态 `x,y`，令 `m(x,y)` 为它们仍然拥有相同 coarse class 的最细层级，并定义

\[
d_t(x,y)=\frac{\lambda_t}{\lambda_{m(x,y)}}.
\]

则 `d_t` 为整数，并满足

\[
d_t(x,z)\le\max(d_t(x,y),d_t(y,z)).
\]

所以 nested precision signatures 会自然诱导一个有限 **ultrametric**，不需要 Euclidean embedding，也不需要 primitive real-valued distance。

这是一个正面的 geometry-emergence 结果，但也同时给出警告：hierarchical geometry 并不自动等于 local macroscopic space。

### Shell-growth 假阳性

在 binary toy `(1,2,4,8)` 中，以 state 0 为中心，

\[
|B(1)|,|B(2)|,|B(4)|,|B(8)|=1,2,4,8.
\]

一个过于朴素的 growth-exponent 判据可能把它读成 line-like 的 `|B(r)|=r`。但若只连接 minimum-distance pairs，得到的图只是

`0--1`、`2--3`、`4--5`、`6--7`，

四个彼此断开的 sibling components。

因此

\[
\boxed{
\text{ball/shell growth alone}
\not\Rightarrow
\text{connected local or Euclidean-like geometry}
}.
\]

如果 R004 要真正生成宏观 locality，还需要 refinement hierarchy 之外的 cross-fiber relations。

## 5. Task-relative effective precision horizon

Hard physical `lambda_max` 依旧无法从有限 observed prefix 中识别。但现在已经可以定义一个不冒充“物理最小长度”的 exact operational endpoint。

固定最细 toy layer `X_L` 与该层上的 future signature `sigma`。对 `lambda|L`，当且仅当 `sigma` 在 projection `p_(L->lambda)` 的每一个 fiber 上恒定时，`lambda` 对该任务是 sufficient 的。定义

\[
\lambda_{\mathrm{eff}}(\sigma)
=
\min\{\lambda:\sigma\text{ factors through }p_{L\to\lambda}\}.
\]

该 minimum 总存在，因为 final identity layer 一定 sufficient。在 physical toy scale 8 上，不同 future languages 可以分别给出 `lambda_eff=1,2,4,8`。

这是 P018/P023 future-safe factorization 的直接 consumer，是 **task/process-relative effective maximum**，不是 universal physical minimum length。

## 6. P016 premodel：第一个不依赖完整 calibration 的排除区间

Finite environment-record premodel 预先声明

\[
V_{\mathrm{predicted}}=\eta V_{\mathrm{ordinary}},
\qquad 0\le V_{\mathrm{ordinary}}\le1.
\]

因此任何 realization 都必然满足

\[
V_{\mathrm{predicted}}\le\eta.
\]

Pedalino 等报告的 nanoparticle matter-wave experiment 在相应 high-mass regime 给出代表性 visibility `V=0.10 +/- 0.01` [SRC-PEDALINO-2026-NANOPARTICLE]。如果这里只把文章公开的数值区间按字面读作 `[0.09,0.11]`，那么当前 multiplicative premodel 对任何

\[
\boxed{\eta<0.09}
\]

都不可能达到该报告区间。

这只是 algebraic range exclusion，**不是** confidence-level statement、完整 likelihood analysis，也不是模型被支持。真正缺失的核心映射仍然是

`apparatus/environment variables -> finite record generator -> eta`。

只要这个 map 没有独立推导，`eta` 就仍然可能被事后调参，物理模型就仍过于自由。

## 7. Generic adjunction 确实存在，但没有物理诊断力

可选的 `1 -> universe -> 1` 黑洞路线已经在最弱 categorical 层面接受压力测试。

对任意有限 relation `R subset X x Y`，定义

\[
\exists_R(A)=\{y:\exists x\in A,\ xRy\}
\]

以及

\[
\forall_R(B)=\{x:R[x]\subseteq B\}.
\]

则标准 powerset Galois connection 为

\[
\boxed{
\exists_R(A)\subseteq B
\iff
A\subseteq\forall_R(B)
}.
\]

它根本不要求 functionality、seriality、cosmology、metric 或 causal horizon；任意 relation 都有。

所以，仅仅在 refinement correspondence 与 contraction/collapse correspondence 之间写出这种 generic adjunction，不会提供任何特殊证据证明 Big-Bang opening 与 black-hole contraction 是物理对偶。真正有意义的物理 duality 必须带有不是任意 relation 免费拥有的附加结构，并且仍然需要独立的 event-horizon / causal criterion。

## 8. 扩展后的 executable validation

重建后的 R004-local suite 现在共有 **43 个 tests**，在 `unittest` 与 `pytest` 下全部通过。

可执行层包含：

- 392 个非零 small serial-relation case 的 `W_k` monotonicity 检查；
- 735 个 small case 的 exact collision/merge defect decomposition，覆盖到 `k=4`；
- 7-versus-49 history-resurrection exhaustion；
- finite adaptive response-table completion；
- ultrametric geometry 与 nesting/root fail-closed guards；
- task-relative effective horizons；
- P016 premodel schema/claim guards；
- 所有 `2 x 2` finite relations 与所有 source/target subset pairs 形成的 256 个 adjunction instances。

六个 R004 `precision_*` modules 中没有 true-division operator，也没有 floating-point literal。

这些都只是 `EXECUTABLE_CHECKED` regression，不是 theorem certificate。本阶段也不主张 `LEAN_CHECKED`：当前 runtime 没有可用 Lean toolchain，所以没有为了完成形式上的清单而提交未经编译的 formalization。

## 9. 重新收紧后的研究前沿

得到以上结果后，R004 的主要未知量已经比任务开始时更清楚。

困难不再是“能不能画一个 finite refinement universe”——可以。也不再是“branching 与不可逆 history merge 能不能共存”——可以，而且有精确整数记账式。

真正决定 R004 能否越过世界观边界的问题已经变成：

> **什么具有独立依据的有限结构限制，能够禁止完整 latent/pre-sampled completion，同时又能产生 connected/local geometry，并给出预先固定的 P016 observable？**

如果没有这样的限制，“新的 distinguishability 被真正创造”仍然只是 interpretation。若能找到并证明这样的限制，precision opening 才可能从有限 hidden-variable re-description 进一步变成具有不可避免实验后果的理论结构。
