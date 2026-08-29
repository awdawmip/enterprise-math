<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION",
  "title": "半素数平方壳中点—边界—邻近素数分解广域探索",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "Determine whether the exact adjacent-square shell coordinates of an unknown odd semiprime, together with factor-blind neighboring-prime and multiplier-shell observables, contain enough structure to predict or sharply bound the factor midpoint, Fermat offset, factor-prime rank, or a productive near-square multiplier; separate genuine search reduction from algebraic restatement, factor leakage, and known Fermat/Lehman/Hart-type behavior.",
  "next_action": "Derive the exact bridge from square-shell coordinates to Fermat midpoint search, then build a factor-labeled but leakage-controlled census of odd semiprimes stratified by size and factor ratio; measure center, boundary, neighboring-prime, congruence, and multi-k shell features against the true midpoint offset and factor-prime rank before extracting any candidate pruning rule.",
  "dependencies": [],
  "source_refs": [
    "https://www.doubao.com/thread/xE7V1M49brmgyPaop",
    "PROJECT_DEFINITION.zh-CN.md@main"
  ],
  "evidence_status": "DIRECT_USER_DIRECTION / EXACT_SQUARE_SHELL_IDENTITIES_AVAILABLE / FACTORIZATION_LEVERAGE_UNPROVEN",
  "last_progress_ref": "Derived exact identities: 4N-1=L^2-2D; B^2=b+2*ceil(sqrt(N))*T+T^2 for odd semiprime N=pq with factor midpoint offset T.",
  "last_progress_at": "2026-08-29T04:32:00+00:00",
  "hard_block": null,
  "tags": [
    "semiprime",
    "factorization",
    "square-shell",
    "midpoint",
    "boundary",
    "neighbor-prime",
    "prime-rank",
    "Fermat",
    "Lehman",
    "multiplier",
    "near-square",
    "exact-integer",
    "counterexample",
    "broad-census"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION",
  "parent_objective_id": "OBJ-SEMIPRIME-SQUARE-SHELL-FACTORIZATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "SSMF1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 半素数平方壳中点—边界—邻近素数分解广域探索

Status: `PUBLISHED_REGISTERED / DIRECT_USER_DIRECTION / NEW_DIRECTION / BROAD_EXPLORATION`

## Mother question

给定一个只知道整数本身、未知因子的奇半素数

\[
N=pq,\qquad 3\le p\le q,\qquad p,q\ \text{均为素数},
\]

相邻平方壳给出的“中心—边界”坐标，是否与真正的因子中点、因子间距、Fermat 搜索位移或因子在 \(\sqrt N\) 附近的素数序号距离之间存在可计算的关系，并且这种关系能否在不使用隐藏因子的前提下，把分解搜索范围实质性缩小？

任务不预设答案为肯定。若所有表面规律最终只是 \(N\) 的代数重写、已知 Fermat/乘子近平方方法的同义表达、样本过拟合或因子信息泄漏，也必须把这种 no-go 精确冻结。

## Frozen inputs and scope

### 1. 相邻平方壳坐标

对任意非平方正整数 \(N\)，令

\[
s=\lfloor \sqrt N\rfloor,\qquad
a=N-s^2,\qquad
b=(s+1)^2-N,
\]

并定义

\[
L=2s+1,\qquad
D=b-a,\qquad
r=N-s(s+1)=\frac{1-D}{2}.
\]

必须保留以下精确恒等式：

\[
a+b=L,
\]

\[
4N-1=L^2-2D,
\]

\[
N=\frac{L^2+1-2D}{4}.
\]

这里 \(b\) 是从 \(N\) 到上方平方边界的距离，\(r\) 是以整数化平方壳中心为基准的有符号位置。研究中可引入其他等价坐标，但必须标明是否只是上述信息的可逆重参数化。

### 2. 半素数的真正因子中心与 Fermat 位移

对奇半素数 \(N=pq\)，定义

\[
A=\frac{p+q}{2},\qquad
B=\frac{q-p}{2},
\]

则

\[
N=A^2-B^2.
\]

令

\[
A_0=\lceil\sqrt N\rceil=s+1,\qquad
T=A-A_0\ge 0.
\]

则有精确桥梁

\[
B^2
=
A^2-N
=
b+2A_0T+T^2.
\]

因此 \(b\) 正是 Fermat 分解的初始平方残差，\(T\) 是从平方壳上边界对应的第一个 midpoint 候选走到真实因子中点所需的单位位移数。该关系是本任务的第一基线，不得把它本身误报为新的分解算法。

还应记录

\[
A-\sqrt N
=
\frac{(\sqrt q-\sqrt p)^2}{2},
\]

并研究它与 \(T\)、因子比 \(q/p\)、素数序号距离之间的离散修正关系。

### 3. 倍乘与跨壳信息

对整数 \(k\ge 1\)，令

\[
L_k=2\lfloor\sqrt{kN}\rfloor+1,\qquad
D_k=D(kN).
\]

保留精确输运式

\[
D_k
=
kD+
\frac{L_k^2-kL^2+1-k}{2}.
\]

同时必须单独研究 \(4kN\) 的上方平方残差、壳位置和跨壳进位，因为半素数分解中的近平方条件自然出现为

\[
x^2-y^2=4kN.
\]

需要判断壳坐标能否对 \(k\) 进行有效排序，从而比无结构枚举更早找到可产出非平凡 \(\gcd\) 的乘子；若其行为等价于已知乘子近平方路线，应明确分类为等价/重解释，而非新算法。

### 4. 邻近素数与“边界/中心”搜索对象

定义 \(\operatorname{PrevPrime}(x)\)、\(\operatorname{NextPrime}(x)\) 为 \(x\) 两侧最近素数。允许研究的 factor-blind 位置至少包括：

- \(\sqrt N\) 的整数邻域 \(s,s+1\)；
- 平方壳整数中心 \(s(s+1)\)；
- 原数 \(N\)；
- 对选定 \(k\) 的 \(kN\) 与 \(4kN\) 对应中心和平方边界；
- 上述位置到最近若干素数的距离、局部素数间隙和左右不对称性。

允许使用已知 \(p,q,A,B\) 构造 factor-labeled/oracle 诊断量来发现关系，例如真实因子在 \(\sqrt N\) 两侧的素数序号距离；但是任何声称可用于分解的最终规则，输入必须只来自 \(N\) 及可由 \(N\) 独立计算的量。必须把“发现用标签”与“部署用特征”严格分开。

重点目标之一是因子素数序号位置。令 \(\pi(x)\) 为素数计数函数，可记录例如

\[
J_p=\pi(s)-\pi(p),
\]

以及相应的上侧序号距离。探索平方壳坐标、局部素数间隙或 multi-\(k\) 观测是否能把 \(J_p\) 限制在显著窄于从 \(\sqrt N\) 向下无结构搜索的窗口。

### 5. 样本范围

至少覆盖以下互补数据层：

1. 对一个可复核的小整数上界做全部奇半素数精确普查，建议先达到 \(N\le 10^7\)，如资源允许再扩张；
2. 对 24、32、40、48、64 bit 半素数做分层随机/构造样本；
3. 按 \(q/p\) 分成近等因子、温和失衡、中度失衡和强失衡区间，避免只看 Fermat 最容易的近平方样本；
4. 加入素数、非半素数奇合数、随机奇数作为负对照；
5. 对最终候选规律保留未参与发现的 bit-size 与 factor-ratio holdout。

任何统计结果都必须同时报告样本规模、分层方式和是否使用隐藏因子标签。

### 6. 允许探索的主线

主线应至少包括：

- **中心线**：\((L,D,r,a,b)\) 与 \(A,B,T,q/p\) 的函数关系、同余关系、秩关系和条件分布；
- **边界线**：真实 \(p,q\) 相对 \(\sqrt N\) 邻近素数序列的位置，以及壳边界/壳中心附近的素数间隙是否给出可观察约束；
- **multi-\(k\) 线**：\(D(kN)\)、\(D(4kN)\)、跨壳修正、最近平方残差和局部素数特征能否预测“好乘子”；
- **模筛线**：从 \(N,L,D,b\) 及小模数推出对 \(T,B,A\) 的允许剩余类，量化能跳过多少 midpoint 候选；
- **反例线**：主动构造具有相同或近似壳特征、但因子结构极不相同的半素数，测试任何候选规律的可识别性上限；
- **基线等价线**：把有效结构逐项对照 Fermat、Lehman 类近平方乘子方法及其他直接相关的经典整数分解路线，区分真正新增的选择信息与现有方法的坐标重写。

## Hard target and required outputs

任务的硬目标不是“找到一些相关性”，而是完成以下分类之一：

### A. 可用于分解的结构

给出至少一个 factor-blind 规则，使其从 \(N\) 的平方壳/邻近素数/multi-\(k\) 信息中，对下列至少一个对象产生可验证的实质收缩：

- Fermat midpoint 位移 \(T\)；
- 因子 \(p\) 在 \(\sqrt N\) 以下素数序列中的 rank window；
- 半因子差 \(B\) 的候选区间或剩余类；
- 可产生近平方因式分解的乘子 \(k\) 的候选集合/排序。

必须提供正确性条件、失败条件和完整成本核算。若只是经验排序，则必须在独立 holdout 上保持，并继续追求可证明解释。

### B. 精确结构但无算法优势

若发现强恒等式、分段仿射规律、同余传递或边界定理，但无法减少总搜索成本，则把它们整理为结构性结果，并证明或实证说明为何没有形成分解优势。

### C. 可复核 no-go

若在规定特征族和数据范围内没有获得稳定收缩，必须给出：

- 最强观察到的相关性及其 holdout 衰减；
- 至少一组破坏候选规律的成体系反例；
- 对 factor-blind 可识别性的限制解释；
- 哪些方向只是 Fermat/乘子近平方方法的重参数化；
- 剩余尚未排除、值得后续研究的最小问题。

### 计算与比较指标

至少同时记录：

- midpoint 候选/平方判定次数；
- 被模筛排除的候选比例；
- 试探素数 rank 数；
- multipliers \(k\) 的测试数量；
- \(\gcd\)、素性测试和平方测试数量；
- 预计算邻近素数特征本身的成本。

不能用“命中率高”替代总成本比较。若邻近素数搜索本身比被节省的分解工作更昂贵，该候选规则应判为无算法收益。

### 必交付物

最终 return 至少应包含：

1. 精确定义和所有核心恒等式；
2. 可复核运算代码或脚本及数据生成规则；
3. 小范围 exhaustive census 与大范围分层 holdout 报告；
4. 中心、边界、邻近素数、multi-\(k\)、模筛五类结果的统一对比表；
5. 代表性正例、反例和失败模式；
6. 与 Fermat/Lehman 类近平方方法的等价/增益审计；
7. 最终分类：`FACTOR_SEARCH_REDUCTION`、`STRUCTURAL_ONLY` 或 `NO_GO_WITH_RESIDUE`；
8. 若形成候选算法，给出伪代码、正确性论证、复杂度/操作计数和适用半素数族。

## Research value to preserve

当前平方壳坐标已经把一个整数在相邻平方数之间的位置压成精确可逆的离散中心坐标，而半素数的 Fermat 分解又恰好以 \(\lceil\sqrt N\rceil\) 为 midpoint 搜索起点。两者之间不是松散类比：上方平方距离 \(b\) 就是 Fermat 初始残差。

真正未知的是：除这条基线恒等式外，平方壳的跨壳进位、multi-\(k\) 输运以及邻近素数的局部边界信息，是否还能提供“选择哪个 midpoint / 哪个因子 prime rank / 哪个 multiplier”的新增信息。即使最终得到 no-go，也能明确切断一批看似接近分解、实则只是在重写 \(N\) 的方向，并留下最小未解残差。

## Success, kill, and return criteria

### Success

满足以下任一条件即可形成正向成功返回：

1. 证明一个非平凡无限半素数族上，factor-blind 壳/邻近素数信息将 \(T\)、\(J_p\) 或 multiplier 搜索空间压缩到严格更小的可证明窗口，并可从中正确提取因子；
2. 得到一个经过独立 holdout 的搜索规则，在至少三个未参与发现的 bit-size 和多个 factor-ratio 区间中，对总 midpoint/prime-rank/multiplier 候选数产生稳定数量级级别改进，同时没有把成本转移到更昂贵的预处理；随后给出其数学解释或明确待证命题；
3. 发现平方壳输运与经典近平方分解之间一个此前未冻结的精确等价/分解公式，足以重写当前研究地图，即使其暂不提升复杂度。

### Kill / no-go

以下情形应停止对应分支并记录，而不是继续调参：

- 规律需要 \(p,q,A,B\) 才能计算，无法转化成 factor-blind 量；
- 所谓预测量由 \(N\) 可逆重参数化后没有新增选择信息，只是把 Fermat 初始残差换名；
- 邻近素数特征的计算成本抵消或超过减少的候选搜索；
- multi-\(k\) 规则在控制变量后与已知近平方乘子排序等价，且没有减少候选/操作数；
- 小样本相关性在 bit-size 或 factor-ratio holdout 上消失；
- 可构造大量壳特征相同/接近而 \(T\) 或 \(J_p\) 相差巨大的反例，足以否定拟议的强判据。

### Return

任务在得到 `FACTOR_SEARCH_REDUCTION`、`STRUCTURAL_ONLY` 或 `NO_GO_WITH_RESIDUE` 三者之一后冻结。返回必须清楚区分：已证明结果、有限计算事实、经验信号、已知方法等价项、被反例否定的猜想和仍未解决的最小问题。
