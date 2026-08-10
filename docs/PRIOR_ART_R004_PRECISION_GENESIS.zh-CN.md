# R004 精度宇宙生成 —— Prior art 与 novelty 边界

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

R004 是对成熟数学/物理工具的一次项目级组合研究。不能因为使用有限状态、离散时空、coarse graining、relational refinement、decoherence 或非经典宇宙起点，就直接宣称这些概念由进取数论首创。

## 已有结构邻域

Enterprise Math 现有 source corpus 已经记录：对物理无限精度实数的 finite-information 批判（`SRC-GISIN-2018`、`SRC-DEL-SANTO-GISIN-2019`）；causal-set local finiteness（`SRC-CAUSALSET-1987`）；可与非平凡 symmetry 并存的 discrete spacetime（`SRC-SNYDER-1947`）；logical irreversibility 与 reversible completion（`SRC-LANDAUER-1961`、`SRC-BENNETT-1973`）；从 projection/coarse-graining 得到宏观不可逆描述的路线（`SRC-ZWANZIG-1961`、`SRC-MORI-1965`）；finite graph metric（`SRC-MATHLIB-SIMPLEGRAPH-METRIC`）；以及 matter-wave / objective-collapse falsification方法（`SRC-FEIN-2019-25KDA`、`SRC-TOROS-BASSI-2018-INTERFEROMETRY`）。

Partition refinement、quotient congruence、behavioral equivalence/bisimulation、finite path space、finite rational probability space、Riemann sums、finite differences、graph shell growth、tree connectivity、projective/inverse-system language 也都是成熟数学。R004 使用这些工具，但不把它们当作新发明。

R004 后续加强的 generative-identifiability no-go 也有直接先行工作邻域。Li 与 El Gamal 的 Strong Functional Representation Lemma 把 stochastic output 表示为 input 与独立 auxiliary randomness 的函数 [SRC-LI-ELGAMAL-2017-SFRL]；Pearl 的 causal calculus 从 nonparametric structural equations 出发正式定义 intervention semantics [SRC-PEARL-1995-CAUSAL-CALCULUS]。R004 的有限 denominator-clearing seed table 与 adaptive counterfactual response table 只是这些成熟 representation / structural-causal 思想的更简单 finite-rational specialization/用途。其项目级作用是一个**负面结果**：仅仅增加 finite randomness 或 finite intervention syntax，并不能让“online ontic generation”变成可识别事实。

## Bell 局域性对 pre-sampled completion 的边界

Bell 1964 年的定理给出了 locality-constrained hidden-variable completion 与全部量子预测之间的不兼容性 [SRC-BELL-1964-EPR]。Clauser、Horne、Shimony 与 Holt 随后给出了可实验实现的四设置不等式，即今天使用的 CHSH 边界 [SRC-CHSH-1969]。因此 R004 **不**把 local-response-table inequality 当作自己的发明。

R004 只把这一成熟定理族用于一个更窄的项目问题：什么额外限制能够真正让 finite pre-sampled completion 失败？在二元四设置情形，一个 deterministic setting-local response table `(A_0,A_1,B_0,B_1)` 的 CHSH 值必为 `+2` 或 `-2`；任何 setting-independent 的非负整数 multiplicity 混合都满足交叉乘后的有限不等式 `|N_CHSH|<=2W`。R004 给出一组只用勾股有理方向构造的 exact rational singlet target，其相关为 `(-3/5,-3/5,-4/5,+4/5)`，因此 `|S|=14/5>2`。这里的整数化 specialization 属于 R004；locality obstruction 本身属于 Bell/CHSH 先行工作。

Hensen 等人报告了在其实验中同时关闭 locality 与 detection loophole 的 Bell test [SRC-HENSEN-2015-BELL]。这是对 local-realist completion 的外部实验 benchmark，不是对所有 latent model 的排除。R004 明确保留剩余边界：completion 仍可选择放弃 locality，或放弃 measurement-setting independence。

Pironio 等人的工作表明，在 device-independent assumptions 下，Bell-inequality violation 可以用于认证 randomness [SRC-PIRONIO-2010-BELL-RANDOMNESS]。这与 R004 尝试把“new distinguishability”变成 operational statement 高度相邻；但 R004 不把这类结果改写成“Bell violation 无条件证明所有 outcome 都是在现场本体生成”的形而上结论。

在保留 local deterministic response functions 的同时放松 measurement independence，本身也已有成熟研究。Hall 已经构造并量化了 measurement-dependent 的 local deterministic singlet models [SRC-HALL-2010-MEASUREMENT-INDEPENDENCE]。因此 R004 不主张这种一般 tradeoff 路线由本项目发明。R004 当前更窄的 WIP 结果只固定自己的归一化 `M=max_{s,t} TV(mu_s,mu_t)` 和自己的 rational four-setting target，证明 `|S|<=2+6M`，再给出一个 denominator-60 的显式 local witness 达到 `M=2/15`；sharp `2/15` 只属于这一 declared finite target 与该 normalization。

## R004 新增的 primary physical pressure tests

Pedalino 等人在 2026 年 Nature 正式发表的实验，对超过 7,000 个原子、超过 170,000 Da 的 sodium nanoparticles 展示 matter-wave interference [SRC-PEDALINO-2026-NANOPARTICLE]。因此“质量/尺寸/原子数本身就是普适 quantum-to-classical cutoff”的朴素版本不能继续作为候选机制。该实验并不直接检验 Enterprise Math；R004 仍须先给出进入 P016 的参数—visibility 映射。

Loop quantum cosmology 早已提供另一条路线：在其特定模型中，经典 Big-Bang singularity 被 quantum-geometry dynamics 与 big bounce 替代 [SRC-ASH-PAW-SINGH-2006-LQC]。因此 R004 不能仅凭“用非经典/离散结构代替经典奇点”主张新颖性。

Environment-as-witness / quantum-Darwinism 研究已经讨论环境记录与 redundancy 如何参与有效 classical objectivity 的形成 [SRC-OLLIVIER-POULIN-ZUREK-2005]。R004 的 exact finite record-overlap 变量只是 structural premodel / contrast，绝不是对 decoherence、Born rule、pointer states 或 quantum Darwinism 的推导。

## R004 正在检验的项目级新增结构

R004 的项目级组合是

`integer precision scale -> relational refinement -> path-history multiplicity -> many-to-one collision -> future-safe observation -> intrinsic hierarchy/graph geometry -> P016 kill test`，

并在 WIP 层证明：对有限 serial **state-extensional** correspondence，若每条历史沿所有 admissible successors 推进，则所有 binomial history-collision spectra `W_k=sum_x binom(n_x,k)` 以及 merge excess 都不会下降。R004 进一步把每个 `Delta W_k` 精确拆成两个非负部分：branch-copy growth 与 cross-source collision growth。

证明使用成熟的 Vandermonde / binomial superadditivity。当前并没有完成“历史上从未出现过同样表述”的 priority search，因此该 cross-surface theorem 的历史 novelty 必须继续标记 `NOVELTY_UNVERIFIED`。

R004 同时得到若干 negative boundaries：有限 deterministic tower 与 finite rational stochastic process 都存在有限 latent-master / pre-sampled representation；对 finite rational classical kernels，即使允许 finite adaptive interventions，也仍可用一个完整 finite counterfactual response table 事先采样并精确复现。所以 refinement、randomness 或 intervention syntax 本身都不能 operationally 证明 ontic creation。Bell locality 加 measurement-setting independence 提供了一个成熟、可检验的限制，它确实能排除一部分 pre-sampled completions；若仍坚持 locality、只放松 measurement independence，则当前选定 rational target 需要且可以用 sharp max-TV cost `2/15` 恢复 local completion。若进一步给定有限初始 latent-resource 上界，则当 full-support response language 的规模超过 seed capacity 时，还会出现独立的 counting obstruction。一个 observable class 不排除 hidden carrier geometry；nested refinement 自然诱导 hierarchy/ultrametric，而 connected leaf geometry 还必须增加显式 cross-fiber witness edges；ambient capacity 增长也不能单独推出 entropy conservation law。
