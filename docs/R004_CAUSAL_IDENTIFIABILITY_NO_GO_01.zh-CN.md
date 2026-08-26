# R004 / FQ-20260810-007 — 有限反事实完备化 No-Go 01

状态：`L4 CANONICAL CANDIDATE / EXECUTABLE_CROSSCHECKED / NOT_LEAN_CHECKED`

研究来源：Draft PR #389，冻结 head `735a8bd94af2723153203776b1949f7f5d0ab296`。

Foundation 独立验证：Issue #164 steward comment `5242406428`。

本补充仅记录已经通过 steward 验证的负核心。后续得到的 operational-fiber、certificate、rank 与 bounded-capacity 深化属于独立 Foundation maintenance，不在本 L4 payload 中偷渡升级。

## 1. 结论与适用范围

对每一个固定的有限时域，只要允许不受限制的隐藏状态扩张，就可以把下列任一有限过程编译成预先存在的确定性 counterfactual masters：

- 有限 action-indexed relation/support 过程；或
- 有限的、**total rational** 的 action-indexed stochastic 过程。

这些 masters 在声明的有限时域内与原过程具有完全相同的可见操作行为。

对于 total rational kernels，还存在一个与未来 policy 无关的 rational master measure；它不仅精确复现每一个 literal action-word law，也精确复现任意由可见历史决定下一步 action 的确定性 adaptive policy 在该时域内产生的完整 visible-history law。

因此，有限 branching、有限 rational randomness、多值 support 以及确定性 adaptive intervention syntax，**本身都不能证明**分支是在 intervention 时才 ontically online 生成。

这是一个有限操作语言下的 identifiability no-go，而不是隐藏变量本体论，也没有采用任何新的物理公理。

## 2. 继承的 Foundation 边界

本结论不重新占有相邻理论。

- FQ-004 继续区分 exact state equality、present observational equality 与 declared-future-safe equality。
- FQ-006 继续负责 legality-sensitive deterministic partial-operation quotient；disabledness 不能静默当作 identity。
- A4 继续负责 multivalued relation/support semantics 与 witness 信息。
- R004/FQ-007 只研究：上述有限 operational semantics 能否区分 online generation 与 unrestricted latent counterfactual completion。

这里不假设 Bell locality、measurement independence、量子力学、连续体定律、宇宙学或任何物理 hidden-variable ontology。

## 3. R004-CI-T01 — 有限 relation-support completion

设 `X` 为有限状态集，`A` 为有限声明 action 集，并对每个 action 给定有限关系 `R_a subseteq X x X`。

以可见状态 `x` 为根、深度为 `H` 的确定性 counterfactual master，会在每个 contingent node 上对每一个声明 action 预存：

- 当该 action 没有 successor 时的显式 disabledness；或
- 一个选定 successor 以及完整 child master。

master family 通过对所有 action-indexed branch choices 递归取 Cartesian product 构造。

对每个满足 `|w| <= H` 的 literal action word `w`，都有

`raw_support(x,w) = { target(m,w) : m is a compiled master and target(m,w) is defined }`。

证明对 word length 归纳。首个 action 上，compiled branch choices 恰好遍历 raw relation successors；对后缀应用归纳假设并取并集，就得到普通 relational composition。若首 action disabled，则两边都得到空 support。

因此，有限的可见 multivalued support 可以由一族 ex-ante deterministic contingent masters 完全复现，而不改变 raw A4 wordwise support language。

## 4. R004-CI-T02 — 一个 policy-independent rational master measure

现在假设每个 action 都是在有限状态集上的 **total rational stochastic kernel** `K_a(y|x)`。

在每个 master node，并且对每个 counterfactual action `a` 独立地：

1. 以精确权重 `K_a(y|x)` 采样一个 successor `y`；
2. 从以 `y` 为根的递归分布中采样一个 child master；
3. 对所有 action-indexed branches 取 product。

由此在任何未来 action word 或 policy 尚未确定之前，就得到定义在有限 deterministic masters 上的一个 rational probability measure `mu_(x,H)`。

对每个满足 `|w| <= H` 的 literal word `w`，把 `mu_(x,H)` 通过 master 对 `w` 的确定性执行映射 push forward，恰好得到普通 kernel law `delta_x K_w`。

未使用的 counterfactual branches 被边缘化为总质量一；被选中的 branch 则具有正确的 kernel marginal。对 word length 归纳即可完成证明。

## 5. R004-CI-T03 — 确定性 adaptive policy 使用同一个 master measure

令下一步 action 是当前为止完整可见历史的任意确定性函数。

T02 中同一个 ex-ante measure `mu_(x,H)`，无需预先知道未来会使用哪个 policy，就能精确复现原 kernels 在该 policy 下直到 horizon `H` 的完整 visible-history law。

给定一段已经发生的 visible history，policy 选择一个 action。这个 action 对应的 child branch 早已按当前可见状态下正确的 kernel conditional law 被采样；未使用的 action branches 继续被边缘化。对 history depth 归纳即可得到完整历史分布相等。

因此，deterministic visible-history adaptivity 本身也不能逃离有限 counterfactual pre-sampling。

## 6. R004-CI-C01 — closure 蕴含 non-identifiability

若一个 admissible finite operational model class 对“加入相应 hidden counterfactual master、同时保持声明 visible projection 不变”的操作闭合，那么在上述 relation/support 与 total-rational-kernel 类中，每一个目标有限时域行为都存在一个 admissible ex-ante completion，且具有完全相同的声明有限时域操作行为。

因此，仅使用该声明有限时域语言可表达的任何实验，都不能区分 online generation 与 ex-ante completion。

经过 steward 验证的逻辑方向是：

`closure under the relevant latent master extension -> non-identifiability`。

所以，**要逃离这个必然 no-go，破坏相应 closure 是必要条件**。

但单纯 nonclosure **不是充分条件**。一个模型类可能排除了某些 master extensions，却仍允许另一个与目标具有相同声明操作行为的 presampled representative。任何更强的正 identifiability theorem，都还需要一个独立合理的 admissibility restriction，使所有相关 observationally equivalent presampled completions 被排除，或者给出等价的 separating-observable theorem。

因此，本补充不会把 latent-extension nonclosure 称为 iff 意义下的 identifiability criterion。

## 7. 候选 primitive 的结论

已经验证的 no-go 给出如下窄结论。

- **Intervention-local response ownership：** 如果所有局部 counterfactual response subtrees 都可以 ex ante 隐藏共存，则仅有 local ownership 不够。
- **State-extensional visible accessibility：** 如果 hidden master coordinates 可以继续细化 retained visible state，则仅有可见 state-extensional access 不够。
- **Bounded latent capacity：** 它可能真正形成 obstruction，因为 capacity bound 自身禁止了原本合法的 completion；它是额外 resource/ontic assumption，而不是有限 operational syntax 的推论。
- **Composition/factorization locality：** 只有当 factorization 或 independence rule 实质性禁止某些 joint counterfactual masters 时才可能形成 obstruction；真正提供额外 causal content 的正是该 restriction 本身。

Bell-locality + measurement independence 是既有文献中 substantive restriction 的一个例子，而不是这里采用的 Foundation axiom。

本 no-go 不选择唯一的 weakest physical axiom。

## 8. 可执行证据

冻结 executable payload：

- `src/enterprise_math/r004_causal_identifiability_completion.py`；
- `tests/test_r004_causal_identifiability_completion.py`。

研究 checkpoint 已交叉验证：

1. 两状态 carrier 上全部 `16 x 16` relation pairs、两个 source states、直到 horizon two——**512/512** source-family cases 对每个 word 都满足 raw-support = master-support；
2. 精确 disabled-word preservation；
3. 一个 hidden-branch support witness；
4. 一个两状态、两 action 的 exact rational kernel family，直到 horizon three；同一个 policy-independent master measure 复现全部 literal word laws；
5. 同一个 master measure 精确复现一个非平凡 visible-history-dependent deterministic policy；
6. stochastic checks 使用 `fractions.Fraction`，不依赖浮点近似。

这些有限交叉检查支持递归证明，但不替代证明本身。

## 9. 既有研究与 novelty 边界

不对 complete contingent plans、mixed/behavior strategy representation、finite product coupling、channel randomization 或 auxiliary randomness 的 functional representation 主张一般性新颖性。

研究 sidecar 记录 Kuhn (1953) 作为 contingent-plan/extensive-game 的 prior-art calibration，并记录 Li–El Gamal (2017) 作为 functional-representation calibration。

Enterprise Math 在这里更窄的贡献，是把这些标准 completion 思路接入 FQ-004/FQ-006/A4 ownership，并在明确的 relation/support 与 total-rational-kernel 假设下证明 project-native T01–T03 finite no-go。

## 10. 本补充没有证明什么

本补充没有证明所有可想象的 causal primitive 都不可能。一个 primitive 完全可能自身就带有 substantive admissibility restrictions，从而排除相应 hidden completion。

它没有证明每个 finite-horizon completion 都能粘成一个固定有限 latent carrier 适用于所有 horizon；completion size 可以随 horizon 增长。

它没有选择任何 physical locality、capacity、common-cause 或 factorization axiom。

它也没有把后续 Foundation 推导出的 operational-fiber、certificate、rank 或 compactness 结果偷升格为本 L4 payload 中的 T01–T03。

本 slice 的 canonical Foundation-facing 结论严格只有这个负结论：**只要相应 latent counterfactual completion 仍被允许，纯有限 operational branching/randomization/adaptivity 就不足以建立 generative identifiability。**
