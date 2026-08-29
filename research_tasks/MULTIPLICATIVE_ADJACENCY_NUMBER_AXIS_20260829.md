<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-MULTIPLICATIVE-ADJACENCY-NUMBER-AXIS",
  "title": "乘法相邻与新数轴：相邻半素数/合数的因子编辑几何",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "Establish exact separation and distortion between additive adjacency among semiprimes/composites and multiplicative adjacency induced by prime-factor edits/divisibility covers, then determine whether a factor-local adjacency can support a canonical and useful alternative number axis or only an inherently branched graph/shell geometry, without relabeling known divisor-poset, exponent-lattice, log, or Gray-code structures as novelty.",
  "next_action": "Freeze M1 divisibility-cover adjacency and M2 fixed-Omega replacement adjacency; prove the fixed-Omega parity theorem, semiprime gcd classification, composite additive-neighbor M1 exclusion, and two-way unbounded distortion; then enumerate finite prime/exponent horizons to test one-dimensional obstructions, Hamiltonian or Gray spines, and projectively compatible multiplicative coordinates.",
  "dependencies": [
    "docs/P001_ROOT_MULTIPLICATIVITY.zh-CN.md@main",
    "docs/P008_MINIMAL_ORDER_CORE.zh-CN.md@main",
    "docs/P018_POWER_ATLAS_ATOM_MONOID_BRIDGE.md@main"
  ],
  "source_refs": [
    "docs/P001_ROOT_MULTIPLICATIVITY.zh-CN.md@main",
    "docs/P008_MINIMAL_ORDER_CORE.zh-CN.md@main",
    "docs/P018_POWER_ATLAS_ATOM_MONOID_BRIDGE.md@main",
    "research_tasks/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_EXPLORATION_20260829.md@main"
  ],
  "evidence_status": "DIRECT_USER_DIRECTION / EXACT_ADJACENCY_SEEDS / TWO_WAY_DISTORTION_CONSTRUCTION_AVAILABLE / AXIS_STATUS_OPEN",
  "last_progress_ref": "Exact seed package: fixed-Omega exponent vectors have positive even factor-edit distance; distinct semiprimes have distance 2 iff they share one prime token and distance 4 iff coprime; adjacent composites cannot be divisibility-cover neighbors; CRT gives consecutive composites with arbitrarily large factor-edit distance; n and 2n give factor-edit distance 1 with arbitrarily large additive gap.",
  "last_progress_at": "2026-08-29T04:50:00+00:00",
  "hard_block": null,
  "tags": [
    "multiplicative-adjacency",
    "semiprime",
    "composite",
    "prime-exponent",
    "factor-edit",
    "divisibility-cover",
    "number-axis",
    "Gray-code",
    "Hamiltonian",
    "Omega-shell",
    "exact-integer",
    "CRT",
    "distortion",
    "counterexample"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-MULTIPLICATIVE-ADJACENCY-NUMBER-AXIS",
  "parent_objective_id": "OBJ-MULTIPLICATIVE-ADJACENCY-NUMBER-AXIS",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "MNA1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:6f7a3ff4948371bb8e0758e61f46ef35eb11d18d21d6ed17cfb790c5263446ef",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 乘法相邻与新数轴：相邻半素数/合数的因子编辑几何

Status: `PUBLISHED_REGISTERED / DIRECT_USER_DIRECTION / NEW_DIRECTION / EXACT-ADJACENCY-AND-AXIS-EXPLORATION`

## Mother question

普通正整数数轴以差值和顺序定义局部性：整数相邻意味着差为 1；半素数或合数子集中的相邻元素意味着其间没有同类元素。

本任务研究另一种局部性：若两个整数只需一次局部的素因子乘入、除去或替换就能彼此到达，它们是否应被视为“乘法相邻”？

核心问题分为两层：

1. 普通数轴上相邻的半素数、相邻的合数，在乘法因子结构上究竟有多远？能否证明这种两种邻近关系存在系统性乃至无界分离？
2. 反过来，以素因子局部变化定义的乘法邻接，能否产生一个可计算、可扩展、非任意的“新数轴”；若一维轴不可能，最小正确替代物究竟是分支图、分层壳、还是带一个选定主脊的离散结构？

任务不预设“新数轴”必然存在，也不把成熟的整除偏序、素指数格或对数坐标简单改名为新结构。

## Frozen inputs and scope

### 1. 加法相邻

对正整数子集 \(S\subseteq\mathbb N_{>0}\)，定义

\[
x\prec_+^S y
\]

当且仅当

\[
x<y
\]

且不存在 \(z\in S\) 满足 \(x<z<y\)。

重点考察：

- 全体正整数；
- 合数集合 \(\mathcal C\)；
- 半素数集合
  \[
  \mathcal S_2=\{n:\Omega(n)=2\}.
  \]

这里 \(\Omega(n)\) 按重数计算素因子个数。

### 2. 素指数向量与乘法编辑距离

由算术基本定理，把

\[
n=\prod_p p^{v_p(n)}
\]

编码为有限支撑的素指数向量

\[
\nu(n)=(v_p(n))_p.
\]

定义首要乘法编辑距离

\[
d_\times(m,n)=\sum_p\left|v_p(m)-v_p(n)\right|.
\]

若 \(g=\gcd(m,n)\)，则必须验证并使用精确恒等式

\[
\boxed{d_\times(m,n)=\Omega(m/g)+\Omega(n/g)}.
\]

该距离表示从一个整数的素因子多重集合变到另一个所需的最少单素因子删除/加入次数。

### 3. 两种乘法相邻

**M1：整除覆盖相邻。**

\[
m\sim_{\times,1}n
\iff
d_\times(m,n)=1.
\]

等价地，较大的数等于较小的数乘以一个素数。

**M2：固定 \(\Omega\) 层的单因子替换相邻。**

在 \(\Omega(m)=\Omega(n)\) 时，定义

\[
m\sim_{\times,2}n
\iff d_\times(m,n)=2.
\]

它表示删除一个素因子 token、再加入另一个素因子 token；半素数层首先研究这种邻接。

### 4. 加权候选距离

作为次级比较量，允许研究

\[
d_{\log\times}(m,n)=\sum_p|v_p(m)-v_p(n)|\log p
=\log\!\left(\frac m g\frac n g\right).
\]

必须与普通

\[
|\log m-\log n|
\]

区分。后者仍主要刻画数值比例，不自动刻画因子支撑的局部变化。

### 5. 有限分辨率窗口

为测试“新数轴”候选，允许固定素数上界 \(P\)、总素因子数上界 \(K\)、或数值上界 \(X\)，得到有限图后再研究随窗口扩张的兼容性。

### 6. 成熟结构边界

任务必须与以下成熟对象比较：

- 整除偏序及其覆盖图；
- 自由交换幺半群的素指数坐标；
- \(\ell_1\) 型指数向量距离；
- 对数嵌入；
- Gray 型遍历与有限图 Hamilton 路径。

若候选结构与成熟对象同构，则只能记录精确翻译、恢复或用途，不得仅因换了术语而主张新颖性。

## Hard target and required outputs

### A. 相邻性分离的精确定理包

至少完成或推翻以下命题。

**T1 — 固定 \(\Omega\) 层偶距离定理。**

若

\[
m\ne n,\qquad \Omega(m)=\Omega(n)=k,
\]

则

\[
d_\times(m,n)\in2\mathbb N_{>0},
\]

因而 \(d_\times(m,n)\ge2\)。

推论：任何固定 \(\Omega\) 层都不存在 M1 边；特别地，两个不同半素数永远不是 M1 相邻。

**T2 — 半素数乘法距离的 gcd 分类。**

对不同半素数 \(m,n\)，证明或修正：

\[
d_\times(m,n)=2
\iff
\Omega(\gcd(m,n))=1,
\]

而

\[
d_\times(m,n)=4
\iff
\gcd(m,n)=1.
\]

必须覆盖平方半素数的重数情况。

**T3 — 相邻合数不是 M1 相邻。**

若

\[
a\prec_+^{\mathcal C} b,
\]

则证明

\[
d_\times(a,b)\ne1.
\]

要求给出不依赖数值普查的统一证明。

**T4 — 加法近、乘法可任意远。**

对每个 \(K\ge2\)，用精确构造得到连续整数 \(n,n+1\)，二者均为合数，且

\[
d_\times(n,n+1)\ge2K.
\]

首选构造为联立

\[
n\equiv0\pmod{2^K},
\qquad
n\equiv-1\pmod{3^K},
\]

并用中国剩余定理封闭证明。

这将给出

\[
|n-(n+1)|=1
\]

但乘法编辑距离无界增长。

**T5 — 乘法近、加法可任意远。**

证明对任意 \(n\)，

\[
d_\times(n,2n)=1,
\]

同时

\[
|2n-n|=n\to\infty.
\]

由 T4 与 T5，精确刻画普通加法局部性与乘法局部性之间的双向无界失真。

### B. 相邻半素数与相邻合数的广域普查

对足够大的精确有限窗口统计：

- 普通顺序下连续半素数对的 \(d_\times\) 分布；
- 连续合数对的 \(d_\times\) 分布；
- \(\gcd\)、\(\Omega\)、\(\omega\)、最大/最小素因子与距离之间的关系；
- 普通差值很小但乘法距离很大的极端对；
- 乘法距离很小但普通差值很大的极端对。

有限普查只作为发现结构、找反例和校准尺度的证据，不得替代全称证明。

### C. 一维“乘法数轴”的阻碍定理

首先检验完整 M1 邻接图能否成为普通意义的一维数轴。

至少证明或推翻：若一个离散全序的“相邻关系”仅连接前驱和后继，则每个点的相邻度数至多为 2；而 M1 图中一个整数可通过乘以不同素数产生多个乃至无穷多个邻居，因此完整 M1 图不可能直接等同于一维全序的相邻图。

在有限素数窗口中，也要确定何时内部点度数大于 2，从而产生同样的一维阻碍。

### D. 新数轴候选与最小替代结构

在承认 C 的阻碍后，系统探索至少三类候选：

1. **有限 M1 图的主脊：** 是否存在覆盖全部允许整数的 Hamilton/Gray 型路径，使连续位置尽可能保持 M1 相邻？
2. **固定 \(\Omega=k\) 壳的 M2 主脊：** 特别是半素数壳，能否按“每次只替换一个素因子”的方式遍历，并随素数窗口扩大保持兼容？
3. **径向—壳内坐标：** 以 \(\Omega(n)\) 或其他可证明的乘法复杂度作径向层，以素因子支撑/指数结构作壳内坐标；若一维轴失败，判断这种分层结构是否是更小、更诚实的乘法几何。

对任何称为“数轴”的候选，至少要求：

- 每个允许整数有唯一位置或唯一坐标；
- 邻接规则由乘法结构决定，而不是事后任意排序；
- 坐标可计算；
- 有限窗口扩大时存在明确兼容规则；
- 能保留某种非平凡的乘法局部性；
- 与成熟结构的关系被准确分类。

### E. 与半素数分解任务的交叉检验

把本任务与平方壳半素数任务保持弱耦合：只检验乘法坐标是否能提供独立的因子搜索排序、候选邻域或壳层约束。

只有在严格 factor-blind 输入下产生可重复的搜索缩减，才记录为分解相关增益；否则把它保留为纯结构性结果。

### F. 先验技术边界与去重

若完整结构最终只是

\[
\mathbb N_{>0}\cong\bigoplus_{p\ \mathrm{prime}}\mathbb N_0
\]

及其已有图距离，那么任务仍然必须保留：

- “普通相邻”和“乘法相邻”的精确失真定理；
- 半素数/合数子集上的特化分类；
- 一维轴不可能性的最小证明；
- 若存在，具有额外有限分辨率兼容性或算法用途的主脊/壳坐标。

## Research value to preserve

即使最终不存在真正的一维“乘法数轴”，本任务仍有独立价值。

T4 与 T5 若成立，将证明两种局部性不是轻微重参数化：普通数轴上距离 1 可以对应任意大的素因子编辑距离，而一次素因子乘法可以跨越任意大的普通数轴区间。

固定 \(\Omega\) 层又天然形成与 M1 不同的替换几何。半素数层因此不是一条普通数轴的稀疏子序列那么简单，而可能更自然地表现为素因子多重集合的离散壳。

一个严格的负结果同样重要：若分支度数或兼容性证明排除所有自然的一维化，就应冻结“乘法结构本质上需要多分支坐标”的结论，而不是强行制造一个任意编号。

## Success, kill, and return criteria

### Success

任务在以下任一强结果下可以成功冻结：

1. 完成 T1–T5 的精确定理包，并构造一个满足上述唯一性、局部性、可计算性和窗口兼容性的非任意乘法数轴/主脊；或
2. 完成 T1–T5，同时证明自然的一维乘法数轴存在结构性障碍，并给出一个更小且精确的替代结构，例如 M1 分支图加固定 \(\Omega\) 壳/M2 坐标；或
3. 找到反例推翻当前 M1/M2 候选中的关键命题，并据此给出更正确的乘法邻接定义，再完成相同级别的分离与轴结构判定。

### Kill / no-go

以下结果不能算成功的新数轴：

- 仅使用 \(\log n\) 重新标号；
- 任意给整数排一个序，却没有乘法局部规则；
- 只复述整除图或素指数格而不产生额外定理、兼容结构或用途；
- 只展示有限样本图形而没有精确命题；
- 为了得到一条线而丢失几乎全部 M1/M2 邻接信息，却没有量化损失。

### Return

最终返回必须同时包含：

- 所有已证明的邻接/失真定理；
- 最小反例与极端构造；
- 半素数和合数的精确有限统计；
- 一维化可行或不可行的理由；
- 最强 surviving multiplicative coordinate/graph/shell proposal；
- 与成熟整除/指数向量/Gray 型结构的去重结论；
- 对半素数分解是否产生真实新搜索信息的单独判定。

## First executable experiment

第一轮直接从精确定理开始，不先画图：

1. 用指数向量证明固定 \(\Omega\) 层距离偶性；
2. 封闭半素数 \(d_\times\in\{2,4\}\) 的 gcd 分类；
3. 给出相邻合数排除 M1 的统一奇偶构造；
4. 用 CRT 构造 \(d_\times\) 任意大的连续合数；
5. 以 \(n\leftrightarrow2n\) 给出反向无界失真；
6. 再进入有限素数窗口，检查 M1/M2 图的度数、连通性、最短路、可遍历性与窗口扩张兼容性。
