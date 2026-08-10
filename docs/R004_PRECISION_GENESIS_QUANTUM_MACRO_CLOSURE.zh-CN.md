# R004 —— 精度宇宙生成、量子—宏观分界与理论闭环

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PHYSICAL_PREMODEL`  
源基线：`main@0d6b751e0d16ba0049369e912e1730e3383f0f58`  
Owner 分支：`research/r004-precision-genesis-closure-20260810`  
纪律：下文严格分开数学结论、可执行检查、既有数学/物理先行工作和物理假说。

## 1. 一句话结论

“精度生成宇宙”可以被压成一套完全有限、精确、可反例攻击的数学研究纲领，但目前还不是物理宇宙学。第一阶段最强的新结构是一个**与分叉兼容的历史碰撞谱单调定理**：只要 refinement 是 state-extensional 的有限 serial correspondence，可用路径/未来分辨能力可以增加，而已经合并的历史绝不会因此恢复；与此同时，一组 no-go 结果说明，refinement 本身不能判定“新的自由度是否真正被创造”、不能自动产生 geometry、不能决定物理 `lambda_max`，也不能单独强迫一个涉及环境容量的熵守恒律。

## 2. Ownership 与 canonical 依赖

R004 不重新制造母理论。

| Surface | R004 中的用途 | Owner / canonical 归属 |
| --- | --- | --- |
| 正整数尺度、整除顺序 | 精度标签与 compatible forgetting | A0 / P005 |
| typed scale state | 防止擦除类型后制造假动力学 | P009 |
| deterministic history merge / collision spectrum | deterministic 退化与碰撞解释 | A1 / P010 / P011 |
| observation / future-safe quotient | task-relative distinguishability | A2 / P018 / P023 |
| coarse-to-fine multivalued support | refinement correspondence | A4 |
| primitive adjacency、graph metric、shell/ball | 涌现几何 observable | A5 / P012 / P022 |
| 定量物理 kill test | 物理入口 | P016 |

R004 只拥有**精度宇宙学的组合层**：把上述既有 surface 组装成有限宇宙模型，证明跨 surface 后真正新增的结论，找出必然失败的接口，并给出进入 P016 前必须补充的物理承诺。

## 3. 精确定义

### D1 —— 有限精度链

定义有限尺度链

\[
1=\lambda_0\mid\lambda_1\mid\cdots\mid\lambda_T=\lambda_{\max},
\]

每一层有有限物理状态集合 `X_lambda`，对 `lambda | mu` 有 surjective forgetting map

\[
p_{\mu\to\lambda}:X_\mu\to X_\lambda.
\]

`lambda=1` 的含义是**最粗的物理可区分性**，而不是最小长度。

### D2 —— Precision-one physical pregeometry

不预设连续空间时，最强而干净的定义是：

1. 物理 quotient `Q_1` 只有一个 class；
2. 凡被称为“物理 geometry”的结构，必须直接定义在 `Q_1` 上，或明确 factor through `Q_1`；
3. 不允许把一个不可观测 carrier 上的 primitive relation 偷偷升级成物理 geometry。

在这一语义下，`lambda=1` 不存在非平凡物理距离、方向、邻接、shell 或 causal separation。

### D3 —— Relational refinement

对 `lambda | mu`，refinement 使用有限 serial correspondence

\[
J_{\lambda\to\mu}\subseteq X_\lambda\times X_\mu,
\]

而不是伪造唯一 inverse function。若要求与 projection 相容，则

\[
(x,y)\in J_{\lambda\to\mu}\Longrightarrow p_{\mu\to\lambda}(y)=x.
\]

Serial 指每一个当前被占据的状态至少有一个 admissible successor。

### D4 —— State-extensional evolution

设 `H_t` 为到达 `X_t` 的路径历史集合。如果所有拥有相同当前物理终点的历史都得到完全相同的 successor support，则演化称为 **state-extensional**。等价地说，history-indexed successor relation 必须 factor through 当前 state map。

这是“不准未来 refinement 偷读已经丢失的历史身份”的精确定义。

### D5 —— 历史重数

定义

\[
n_t(x)=\#\{h\in H_t:\operatorname{end}(h)=x\}.
\]

对 serial state-extensional relation `R_t subset X_t x X_(t+1)`，每一条当前历史沿所有 admissible edge 延伸：

\[
n_{t+1}(y)=\sum_{x\,R_t\,y}n_t(x).
\]

这是有限路径分叉，不是量子振幅。

### D6 —— 历史碰撞/路径谱

对整数 `k>=1` 定义

\[
W_k(n)=\sum_x {n(x)\choose k}.
\]

`W_1` 是被表示的路径历史总数；`W_2` 是当前共享同一终点的不同历史无序对数量；高阶 `W_k` 记录同一终点上的 `k` 重历史合并。

另定义

\[
H(n)=\sum_x n(x),\qquad
A(n)=\#\{x:n(x)>0\},\qquad
M(n)=H(n)-A(n).
\]

`A` 表示被占据终点的可区分数量，`M` 是 merge excess：在每个占据终点保留一个代表以后，多出来的历史重数。

## 4. R004-T01 —— 与 relational branching 兼容的碰撞谱单调性

状态：`PROVED_WIP`；另有 exhaustive finite regression。

**定理。** 设 `X,Y` 有限，`n:X->N_0`，`R subset X x Y` 在 `n` 的 support 上 serial。定义

\[
n'(y)=\sum_{xRy}n(x).
\]

则对每个整数 `k>=1`，都有

\[
\boxed{W_k(n')\ge W_k(n)}.
\]

并且

\[
\boxed{M(n')\ge M(n)}.
\]

### 证明

对每个 occupied `x` 选择一个 successor `f(x)` 满足 `x R f(x)`；有限性和 seriality 已足够。对每个 `y` 定义

\[
m(y)=\sum_{f(x)=y}n(x).
\]

所有被选择的 edge 都属于 `R`，所以 `n'(y)>=m(y)`。对固定 `k`，函数 `a -> binom(a,k)` 在非负整数上单调。由 Vandermonde identity 又有

\[
{a+b\choose k}\ge {a\choose k}+{b\choose k}.
\]

因此按被选择的 target 对 source 分组，得到

\[
\sum_y {n'(y)\choose k}
\ge
\sum_y {m(y)\choose k}
\ge
\sum_x {n(x)\choose k}.
\]

对 merge excess，令 `g(0)=0`，`g(a)=a-1`（`a>0`）。`g` 同样在非负整数上单调且 superadditive，重复上述分组论证即得 `M(n')>=M(n)`。∎

### 含义

refinement relation 可以把一个当前状态打开成多个未来终点；但只要它只依赖“当前已经合并后的物理状态”，每一个新 branch 都继承相同的历史重数。因此：

> **新的未来 alternatives 可以产生，而已经丢失的 history identity 不会被 refinement 恢复。**

该定理同时消费 A1 的 collision 语言和 A4 的 correspondence 语义；应通过 Relay 回流给相关 mother owner，而不是在 R004 内另建一套碰撞母理论。

## 5. 精确 branching / merge balance

对 serial relation 定义 branching increment

\[
B_t=\sum_x n_t(x)(\deg_R(x)-1).
\]

直接计数得到

\[
\boxed{H_{t+1}=H_t+B_t.}
\]

又因为 `M=H-A`，存在精确有限恒等式

\[
\boxed{
M_{t+1}-M_t
=B_t-(A_{t+1}-A_t).
}
\]

结合 R004-T01，得到

\[
A_{t+1}-A_t\le B_t.
\]

这是 R004 对“两个相反单调方向能否共存并形成 balance law”的第一条精确回答：relational branching 新增的路径 alternatives，一部分表现为新的 occupied distinguishable endpoints，剩余部分进入终点历史重数/merge excess。整个结构只用有限整数计数。

**重要边界：** ambient capacity

\[
C_t=|X_t|
\]

不在上述恒等式中。未被占据的可用状态可以任意增加。因此这不是“容量与熵之间”的守恒律，而只是实际 path process 的精确记账式。

## 6. R004-C01 —— 从 precision-one 固定初始 cohort 定义时间箭头是空的

状态：`COUNTEREXAMPLE / DEFINITION CORRECTION`。

如果 precision-one pregeometry 真正只有一个物理状态和一条物理历史，那么“固定 Big-Bang 初始 cohort 的 history equivalence class 数”一开始就是 `1`。若再要求它随时间单调下降，它永远无法产生非平凡时间箭头。

因此历史对象不能只取 Big Bang 的 singleton 初始 history。必须把随后 refinement/branching **新生成的 path histories** 纳入。D5/D6 的 multiplicity 定义正是对此的修正。

## 7. R004-C02 —— history-indexed refinement 会复活已丢失历史

状态：`COUNTEREXAMPLE`。

假设两条历史现在共享同一个状态，于是 `n(x)=2`、`W_2=1`。如果允许一个非法的 history-indexed update 读取这两条历史的身份，再分别送往 `y_0,y_1`，新 multiplicity 就变成 `(1,1)`，于是 `W_2=0`。

因此 no-resurrection 在 refinement 能读取 hidden history identity 时立即失败。这不是技术细节，而是本体论边界。

toy exhaustive search 对“两条已合并历史 + 三个未来状态”得到：

- state-extensional 非空 successor supports 共 `7` 种，history resurrection 为 `0`；
- history-indexed support pairs 共 `49` 种，其中 `42` 种重新区分两条历史。

## 8. R004-T02 —— 有限 latent-master representation no-go

状态：`PROVED_WIP / PRIOR_ART-BASED IMPOSSIBILITY BOUNDARY`。

任意有限 deterministic projection tower 都可以被表示成一个有限 compatible-path space 的不同 views。最简单的 surjective chain 甚至可以直接用最细层作为 master carrier；更一般地，可取各层笛卡尔积中所有 compatible tuples 的有限集合。

所以单看一个有限 refinement tower 的 extensional 数据，无法区分：

- A. fine alternatives 从一开始就作为有限 latent state 存在；
- B. refinement 真正创造了新的物理 alternatives；
- C. coarse state 只含 relational potential，interaction 后 alternatives 才 actualize。

这**没有**恢复连续体；latent master 可以仍然是有限集合。它证明的是更强的识别性边界：

> **有限 refinement 结构本身不足以决定“ontic creation”。**

因此，“Big Bang = precision opening”要超过换一种说法，必须增加某种 generative commitment，并且该 commitment 必须产生 projection tower 之外的 operational consequence。

## 9. R004-T03 —— 加入有限有理随机分叉仍不能证明现场生成

状态：`PROVED_WIP / PRIOR_ART-BASED IMPOSSIBILITY BOUNDARY`。

有限 rational probabilities 也不能解决上一节的问题。对任何 finite-horizon、path probability 全为有理数的过程，取所有 path probability 的公分母 `D`，把概率 `a/D` 的 path 替换成 `a` 个 equiprobable seed atoms，即得到一个完全有限的 latent seed space，精确复现整个联合分布。

所以，仅仅把 refinement 写成 stochastic/branching 过程，并不能 operationally 区分“现在生成”和“事先有限预采样”。要打破这种等价，R004 需要额外的 causal/intervention structure，而不是只需要 randomness。

可执行 helper 对一阶构件进行 exact integer 检查，例如

\[
(1/2,1/3,1/6)\leftrightarrow D=6,\ (3,2,1).
\]

## 10. Geometry emergence：能证明什么，不能证明什么

### R004-T04 —— singleton physical quotient 排除非平凡 quotient geometry

状态：`PROVED_WIP`，是 elementary graph theory / P012 的直接 specialization。

如果物理 geometry 被定义为**物理 quotient `Q_lambda` 上**的 simple graph，那么 `|Q_lambda|=1` 时不存在非平凡 edge，所有 intrinsic distance 都退化为零。

### R004-C03 —— 一个 observable class 并不排除 hidden geometry

状态：`COUNTEREXAMPLE + EXECUTABLE_CHECKED`。

取三个 hidden carrier points，但 observation map 将三点全部送入一个物理 class。三点 labelled simple graph 一共有 `2^3=8` 个，其中 `7` 个非空，`4` 个 connected。因此

\[
|Q_1|=1\not\Rightarrow\text{“hidden carrier 不可能具有 graph”}.
\]

要坚持强 pregeometry，必须采用 **quotient physicality**：不可观测 carrier 上的 primitive geometry 不计作物理 geometry。

### R004-C04 —— distinguishability 增加不会自动产生 geometry

即使每一层 `|Q_lambda|>=2`，仍可令 adjacency 全为空。状态数可以一直增长而 geometry 永远不出现。所以

\[
\lambda_{\rm geom}
=
\min\{\lambda:G_\lambda\text{ 满足指定 geometry predicate}\}
\]

只有在另给 relation-generation law 后才有数学内容。

## 11. Finite toy universe

状态：`EXECUTABLE_CHECKED`；不主张物理真实性。

reference model 取

\[
\lambda\in\{1,2,4,8\},\qquad X_\lambda=\{0,\ldots,\lambda-1\},
\]

并使用 exact block forgetting

\[
p_{\mu\to\lambda}(y)=y//(\mu/\lambda),
\]

其中比例始终为整数。Refinement 是该 projection 的 inverse-image correspondence。

模型在 `lambda<4` 时不声明任何 adjacency；从 `lambda=4` 起显式生成 finite cycle graph，因此 `lambda_geom=4` 来源于 relation law，而非由 cardinality 偷渡。模型可计算 exact graph distance、shell、ball 和 geodesic multiplicity。

最小 history sequence 为：

1. 一个 state/history；
2. precision opening `0 -> {0,1}`，得到 multiplicity `(1,1)`；
3. many-to-one collapse `{0,1} -> 0`，得到 multiplicity `(2)`；
4. 再次 refinement `0 -> {0,1}`，得到 `(2,2)`，而不是 `(1,1)`。

对应 `W_1,W_2`：

\[
(1,0)\to(2,0)\to(2,1)\to(4,2).
\]

这就是 R004 所需的最小闭环机制：

> **可用路径/精度 alternatives 可以继续打开，而历史碰撞不可逆性仍保持单调。**

穷举回归进一步检查了两当前状态、三未来状态、multiplicity `0,1,2`、所有非空 serial successor supports 组成的 `392` 个非零情形；`k=1,2,3` 的 `W_k` 没有找到下降反例。该结果只是 regression；证明由 R004-T01 给出。

## 12. Ambient capacity 与“熵守恒律”的 no-go

状态：`PROVED_WIP IMPOSSIBILITY BOUNDARY`。

仅有

\[
C_t\uparrow,\qquad\text{某固定 history cohort 的 recoverability}\downarrow
\]

不足以强迫任何 universal conservation law。给定任意有限非降正整数序列 `C_t` 和任意非升正整数序列 `A_t<=C_t`，都可以构造有限状态集合 `|X_t|=C_t` 与 compatible many-to-one cohort maps，使 image class 数恰好等于 `A_t`。

所以不能从双单调性推出

\[
C_t+A_t=\text{constant}
\]

或某个固定的“容量增长—历史损失兑换率”。要得到这样的 law，必须再加入 resource、measure 或局域动力学耦合假设。

不需要额外假设就精确成立的，是第 5 节的 path accounting：`H'=H+B` 与 `Delta M=B-Delta A`。

## 13. Maximum finite precision

状态：`COUNTEREXAMPLE / PHYSICAL_HYPOTHESIS BOUNDARY`。

一个有限可观测 prefix 无法判断 precision tower 是否真的在那里终止。两个模型可以在所有已经测试的层完全一致，其中一个在 `lambda=T` 停止，另一个继续存在更细的有限层。

因此手工写入 hard `lambda_max` 并不等于推导出最小物理尺度。R004 必须区分：

- **hard maximum**：人为规定的有限 endpoint；
- **emergent maximum**：动力学使继续 refinement 不可达；
- **typed maximum**：不同物理量纲具有不同 endpoint；
- **process-effective maximum**：给定 future language 无法 operationally 使用更细信息。

Planck length、Planck time 与 action/`hbar` 只能进入不同的 typed calibration，不能粗暴合成一个无量纲统一步长。

## 14. 连续世界如何重新出现

状态：`PRIOR_ART / EXECUTABLE_CHECKED EXAMPLE`。

完全有限、exact rational dynamics 可以逼近 smooth laws，这一方向没有原则性数学障碍。例如对 `[0,1]` 上 `f(x)=x^2` 的 rational grid，有限 left sum 精确为

\[
S_n=\frac{(n-1)(2n-1)}{6n^2},
\]

并有

\[
\frac13-S_n=\frac{3n-1}{6n^2}\le\frac1{2n}.
\]

scaled forward difference 精确为

\[
n\left[f\left(\frac{k+1}{n}\right)-f\left(\frac{k}{n}\right)\right]
=\frac{2k+1}{n},
\]

相对于 `2k/n` 的误差恰为 `1/n`。

这是成熟 numerical analysis，而不是进取数论的新定理。真正的下一步不是证明“有限和能逼近积分”，而是从 Enterprise Math 自己的离散 transition family **导出某个特定宏观方程及明确误差界**，不能先把连续方程当作底层真理再反向离散化。

## 15. Quantum—classical boundary：第一阶段留下了什么

### 15.1 固定质量/尺寸阈值应淘汰

“超过一个原子大小 / 超过 N 个原子 / 超过某固定质量就自动经典化”不是可用模型。2026 年 sodium nanoparticle matter-wave experiment 已在超过 7,000 个原子、超过 170,000 Da 的对象上观测到干涉 [SRC-PEDALINO-2026-NANOPARTICLE]。这直接给 naive size-only variant 施加压力；但它当然不会直接检验一个尚未给出定量 visibility law 的 Enterprise Math 模型。

### 15.2 Finite environment-record premodel

对两个 alternatives 和有限 environment microstate set，定义 record maps `r_0,r_1`，并取 exact rational overlap

\[
\eta=\frac{\#\{e:r_0(e)=r_1(e)\}}{|E|}.
\]

同样大小的系统，仅因 interaction/history/environment 不同，就可有 `eta=1`、`1/2`、`0`。这说明有限模型完全可以拥有 task/environment-relative 的 classicalization-like parameter；其结构更接近 decoherence / environment-as-witness / quantum Darwinism 先行工作 [SRC-OLLIVIER-POULIN-ZUREK-2005]，而不是固定尺寸 cutoff。

但 `eta` **不是量子力学推导**。这里没有 Hilbert-space phase、Born rule 或 unitary dynamics。

### 15.3 进入 P016 的条件

一个 R004 physical realization 只有在事先声明

\[
\theta,\text{apparatus/environment data}
\longmapsto
(r_0,r_1,\ldots)
\longmapsto
V_{\rm predicted}
\]

或其他可直接测量 observable 的映射后，才能真正进入 P016。如果 record maps 可以看完数据后再自由挑选，模型就是不可证伪的。对于 matter-wave interference，第一入口应是 P016-F3；具体 dynamics 若不可避免地产生能量、reversal deficit、symmetry breaking 或不合法 quantum channel，还会触发 F4/F6/F8/F9。

## 16. Prior-art / novelty map

整个 synthesis 的历史新颖性继续是 `NOVELTY_UNVERIFIED`。

- `PRIOR_ART`：divisibility/projective systems、inverse/path-space representation、有限有理概率 sample space、graph metrics、causal sets、finite-information quantities、partition refinement/bisimulation、decoherence/environment-as-witness、objective-collapse falsification、Riemann sums/finite differences、coarse-graining/renormalization。
- `PROJECT-SPECIFIC COMBINATION`：把 P005 scale、A4 relational refinement、A1 history collision、P023 future language、P012/P022 geometry、P016 falsification 放进一个统一 finite ontology。
- `PROVED_WIP CROSS-SURFACE RESULT`：R004-T01 —— serial state-extensional relational branching 下的 collision spectrum / merge-excess 单调性，以及 exact branching/occupied/merge balance。
- `PROVED_WIP NO-GO`：有限 deterministic 或 rational stochastic refinement 数据不能识别 ontic creation；singleton observation 不代表 hidden carrier 无 geometry；capacity monotonicity 不决定 universal entropy law 或 hard `lambda_max`。
- `PHYSICAL_HYPOTHESIS`：precision opening 作为 cosmological genesis；environment/future-language regime 作为 quantum—classical 候选模型的一部分；typed physical endpoint。

Loop quantum cosmology 已经提供另一条完全不同的非经典宇宙起点路线：经典 Big-Bang singularity 可被 quantum geometry bounce 替代 [SRC-ASH-PAW-SINGH-2006-LQC]。所以 R004 不能仅凭“把 classical singularity 换成非经典有限结构”宣称新颖。

## 17. 经过 no-go 定理后，“Big Bang = precision opening”还剩下什么

这句话目前在数学上成立的最弱版本是：

> 可以在不预设连续 background space 的情况下，从一个物理 quotient class 定义到多个 class 的有限演化。

要升级为**新的物理模型**，opening law 必须进一步固定某种不可避免 observable，并且该 observable 不能被一个有限 latent-master completion 在同一 intervention 结构下完全复现。R004-T02/T03 说明 deterministic refinement 与 finite rational branching 本身都过不了这一门槛。

因此下一阶段真正的关键对象不是更华丽的“宇宙分裂图”，而是 **generative intervention law**：它必须规定“哪些 future interaction 只能依赖当前 actualized relational data”，并产生某个不能通过预采样有限 hidden seed 在不改变 intervention 规则的条件下复制的 operational restriction。

## 18. 可选黑洞闭环

状态：`CONJECTURAL / DEFERRED`。

“one/few classes -> many classes”和“many future classes -> one/few classes”目前只是 cardinality motion 方向相反，不构成 categorical duality。除非给出 objects、morphisms、两个 functors 以及 unit/counit，或另一个明确 Galois structure，否则不能使用 adjunction 语言。

普通 collapse fibers、zero-magnitude basins、clock slowdown 或 causal focusing 也都不能直接称为 event horizon。因此本阶段不升级“1 -> universe -> 1”图景。

## 19. Foundation backflow 与 Research Relay

### 应回流 Research Relay #82

最成熟的 reusable payload 是 R004-T01 与 no-resurrection boundary：

- source：R004 owner branch/commit；
- status：`PROVED_WIP + EXECUTABLE_CHECKED`；
- weakest assumptions：有限状态集合、非负整数 path multiplicities、serial state-extensional relation；
- relation class：对 A1 collision spectrum 与 A4 correspondence 为 `COMPOSABLE_INDEPENDENT / BRIDGE`；
- downstream action：A1 检查是否作为 relational extension of collision spectrum；A4 检查是否可表述成 serial support 上的 history-multiplicity pushforward；P018/P023 将其作为 no-hidden-history refinement invariant 消费。

Finite latent-master no-go 也应以 `NEGATIVE_BOUNDARY` 回流，防止其他路线把“出现 refinement structure”直接解释成“ontic creation 已证明”。

### 成熟 Foundation Feedback Packet

候选基础问题：

> 在保持 P018/P023 的 actual state / observation / future-safe layering，并保持 A4 correspondence owner 边界的前提下，什么最弱有限 causal/intervention structure 能使 state-extensional relational refinement **不再 operationally 等价于有限 latent-master / pre-sampled path model**？

这个问题不能覆盖 FQ-004 已经建立的 state/observation/future-safe 分层，也不能复制 FQ-006 的 partial-operation machinery。它只问一个额外层：需要什么结构，才能把“新的 distinguishability 真正生成”从解释变成可检验 theorem。

## 20. 下一阶段拆分

1. **R004-A / A1↔A4 bridge**：分类 R004-T01 的 equality/strictness 条件，研究完整 `W_k` 单调性是否有干净的 relation/hypergraph formulation，并避免重复 P011。
2. **R004-B / generative no-go**：形式化 finite latent-master 与 rational-seed representation theorem，再寻找打破 observational equivalence 的最弱 intervention/causal assumptions。
3. **R004-C / geometry**：要求 relation-generation law 同时 local 且 projection-compatible；研究 connectedness、shell growth、dimension-like observable、direction/causal structure 在哪个最小尺度开始被**强迫出现**而不是手工指定。
4. **R004-D / P016 physical model**：选择一个预先固定的 finite environment-record dynamics，把 apparatus variables 映射到其参数，并推出 unavoidable matter-wave visibility residual；必要时直接用当前干涉数据杀掉模型。
5. **R004-E / continuum**：从 toy transition family 推导一个宏观方程与显式 finite error bound；不得把目标连续方程作为微观输入。
6. **R004-F / typed endpoint**：寻找 process-dependent / dimension-dependent `lambda_max` 的结构来源；手写 hard cutoff 只保留为 baseline countermodel。

## 21. 当前判决

“首尾相连”的世界观现在**只在数学架构层面进入了理论**。我们已经有一个完全有限的精确机制：

\[
\text{precision/path opening}
+
\text{state-extensional many-to-one merge}
\Longrightarrow
\text{new alternatives without history resurrection},
\]

并得到单调整数 collision spectrum 与 exact branching/merge accounting law。

距离物理理论仍缺少的东西也已经被精确定义：

- 一个 operationally non-latent 的 generative law；
- 一个不是人为指定的 geometry-generation law；
- 一个有结构来源的 finite physical endpoint；
- 一个预先声明、可以进入 P016 kill test 的 observable map。

在这些空缺被填上以前，`precision-one -> universe -> quantum/classical -> minimum scale` 是一套数学上严肃的研究纲领与 physical premodel，而不是已经验证的宇宙学。
