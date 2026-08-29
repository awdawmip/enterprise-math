<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE",
  "title": "平方壳—乘法壳因子盲桥：半素数局部坐标预测与分解收益盲测",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "The adjacent-square-shell program has already frozen a negative boundary for its tested static shell/local-neighbor/raw finite-multi-k feature family, while the multiplicative-adjacency program has classified the hidden fixed-Omega/M2 geometry but found no factor-blind localization rule. Determine whether a genuinely new integration layer, using only factor-blind N-derived observables and reusing the sealed factor-blind benchmark discipline, can predict semiprime multiplicative-shell coordinates or candidate neighborhoods strongly enough to reduce held-out factor search without factor leakage; otherwise freeze the bridge as an exact or empirical no-go.",
  "next_action": "Freeze a leakage-free feature/label split: N-derived square-shell and precommitted transport observables are worker-visible, while factor tokens, factor midpoint/gap, prime-index/M2/Gray labels and successful-factor certificates remain verifier-only. Reuse the existing PCF2 sealed benchmark discipline, exclude the square-shell feature families already closed by RR-2A424E3B8EC11DC1278C unless a strictly new conditional mechanism is stated, then run stratified held-out prediction-to-search experiments and adversarial near-feature/far-factor tests before making any factorization claim.",
  "dependencies": [
    "research_result_records/RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION/RR-2A424E3B8EC11DC1278C.json@main",
    "research_result_records/RS-MULTIPLICATIVE-ADJACENCY-NUMBER-AXIS/RR-C28C28A7C8EF8B9C96F6.json@b74c886f5abc78e2a4da5985932f49063bf15b24",
    "research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/benchmark_result_summary.json@dce4a309f8d799030081ed82e310c26a92d8f465"
  ],
  "source_refs": [
    "research_returns/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_RETURN_20260829.md@main",
    "research_returns/MULTIPLICATIVE_ADJACENCY_NUMBER_AXIS_RETURN_20260829.md@b74c886f5abc78e2a4da5985932f49063bf15b24",
    "research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/README.md@dce4a309f8d799030081ed82e310c26a92d8f465",
    "research_tasks/SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT_20260829.md@main",
    "research_tasks/SEMIPRIME_SQUARE_SHELL_RESIDUAL_PRIORITY_PRIOR_ART_AUDIT_20260829.md@main"
  ],
  "evidence_status": "DIRECT_USER_DIRECTION / INTEGRATION / SQUARE_SHELL_NEGATIVE_BOUNDARY_FROZEN / MULTIPLICATIVE_SHELL_GEOMETRY_FROZEN / PCF2_SEALED_BENCHMARK_REUSE / FACTOR_BLIND_LOCALIZATION_OPEN",
  "last_progress_ref": "Integration frontier: RR-2A424E3B8EC11DC1278C closed the tested static square-shell feature family for total-cost factorization gain; RR-C28C28A7C8EF8B9C96F6 left factor-blind M2-neighborhood prediction open; PCF2 provides a sealed dual-compartment benchmark discipline.",
  "last_progress_at": "2026-08-29T07:07:00+00:00",
  "hard_block": null,
  "tags": [
    "semiprime",
    "factor-blind",
    "square-shell",
    "multiplicative-shell",
    "M2-neighborhood",
    "prime-index",
    "Gray-rank",
    "Fermat-offset",
    "multi-k-transport",
    "held-out",
    "leakage-control",
    "factorization",
    "integration",
    "counterexample"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE",
  "parent_objective_id": "OBJ-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "SMSB1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 平方壳—乘法壳因子盲桥：半素数局部坐标预测与分解收益盲测

Status: `PUBLISHED_REGISTERED / DIRECT_USER_DIRECTION / INTEGRATION / FACTOR-BLIND-BRIDGE-OR-NO-GO`

## Mother question

对未知因子的奇半素数

\[
N=pq,\qquad 3\le p\le q,\qquad p,q\text{ prime},
\]

只允许观察由整数 \(N\) 本身可计算的量。问题不是再次证明平方壳坐标与 \(N\) 等价，也不是在已知 \(p,q\) 后描述乘法壳，而是：

> 能否用 factor-blind 的平方壳、跨壳进位、同余或经明确计费的局部算术观测，预测隐藏的乘法壳位置——例如因子 prime-index 区间、M2 局部块、半素数 Gray block/rank bucket、Fermat 中点偏移或高价值 multiplier 候选——并把这种预测转换成 held-out 半素数上的实际搜索缩减？

如果不能，则要求把“平方壳可见结构无法定位隐藏乘法壳”的边界冻结成可复核的 no-go，而不是继续寻找训练集相关性。

## Frozen inputs and scope

### 1. 必须继承的两个已冻结边界

本任务从两个结果出发，但不把它们的结论升级为新的真理层级。

**平方壳边界。** `RR-2A424E3B8EC11DC1278C` 已给出 `NEGATIVE_BOUNDARY`：相邻平方壳、局部邻近素数与 raw finite-multi-k 的已测试 feature family 没有建立新的 factor-blind total-cost reduction。该结果中的精确恒等式仍可使用，但不得把同一 feature family 换目标名后重复当作新探索。

**乘法壳边界。** `RR-C28C28A7C8EF8B9C96F6` 已给出固定 \(\Omega\) 的 M2 replacement-shell geometry、半素数 prefix-compatible Hamilton–Gray ray 与纯一维轴 no-go，同时明确冻结 `NO FACTOR-BLIND FACTORIZATION GAIN ESTABLISHED`。本任务只处理其中尚未封闭的 factor-blind localization gap。

### 2. 信息守恒护栏

对非平方 \(N\)，令

\[
s=\lfloor\sqrt N\rfloor,\quad a=N-s^2,\quad b=(s+1)^2-N,
\]

\[
L=2s+1,\qquad D=b-a,\qquad r=\frac{1-D}{2}.
\]

已有精确恒等式

\[
4N-1=L^2-2D,
\]

从而

\[
N=\frac{L^2+1-2D}{4}.
\]

因此 \((L,D)\) 与 \(N\) 之间是可逆重参数化；任何由 \(N\) 确定的有限 multi-k shell signature 也不会凭空增加关于隐藏因子的 Shannon 信息。

本任务若得到正结果，只能表述为：

- 更好的算法表示；
- 更有利的计算几何；
- 对隐藏标签的可泛化 inductive bias；
- 在给定成本模型下的候选空间压缩。

禁止把确定性重编码表述成“产生了新的因子信息”。

### 3. Worker-visible factor-blind observables

允许进入候选方法的输入只能来自 \(N\) 与预先公开的固定参数，包括：

1. \(s,a,b,L,D,r\) 及整数安全的归一化/分桶；
2. 对预先固定的 multiplier 集 \(K\)，
   \[
   L_k=2\lfloor\sqrt{kN}\rfloor+1,\qquad D_k=D(kN),
   \]
   以及精确 carry/correction
   \[
   C_k=D(kN)-kD(N)=\frac{L_k^2-kL^2+1-k}{2};
   \]
3. 预先固定模数的 \(N\bmod m\) 与由此导出的合法同余类；
4. 仅依赖 \(N\) 的整数根、近平方残差、离散差分与排序统计；
5. 若使用 \(\sqrt N\) 周围素数密度、prime gaps 或 primality queries，必须把查询次数与测试成本计入总成本；
6. 已有 residual-priority / Hart 类任务若形成正式结果，只允许消费其明确通过的 factor-blind 组件，不在本任务内重复其 prior-art 或 streaming-cost 审计。

### 4. Verifier-only hidden labels

真实因子只允许存在于 corpus generator / verifier 侧，用于评估而不能序列化给候选 worker。可评估的隐藏标签包括：

\[
T=\frac{p+q}{2}-\lceil\sqrt N\rceil,
\qquad
B=\frac{q-p}{2},
\]

以及：

- 小因子 \(p\) 在 \(\sqrt N\) 以下的 prime-index / prime-rank；
- 因子 prime-token 的 index pair \((i,j)\)；
- M2 shell 中的 block / neighborhood label；
- 既有 semiprime Gray ray 的 block/rank bucket；
- 预先声明的 near-square criterion 下最优或前若干 multiplier \(k^*\)；
- factor-ratio stratum，仅用于分层评估。

### 5. 严禁泄漏

候选 worker 不得看到或间接获得：

- \(p,q\) 或其哈希/编码；
- \(T,B\)、factor ratio、真实 prime-index、M2/Gray 真值；
- 对隐藏因子或隐藏目标做 gcd 后形成的特征；
- 用测试标签选择 feature family、阈值、multiplier 集或模型超参数；
- 任何可从 verifier 私有状态反推出因子的缓存、排序键、文件名或随机种子。

沿用 PCF2 的 dual-compartment 思路：候选请求只携带公开 \(N\)、独立 public seed、候选标识和预提交参数。

### 6. 数据与对照范围

至少包含：

- balanced、near-twin、moderately unbalanced、strongly unbalanced semiprimes；
- 多个不重叠 bit-length band，优先覆盖 24/32/40/48/64-bit；资源不足时必须冻结实际完成的 bands，不能把未运行范围写成证据；
- train / tuning / held-out 三分区，held-out 的因子与标签直到规则冻结后才允许 verifier 使用；
- adversarial pairs：worker-visible fingerprint 很近但 factor layout / M2 label 很远，以及 fingerprint 很远但 factor layout 很近。

PCF2 sealed benchmark 是泄漏控制与成本记账基线；本任务不得重新发明一个更弱的 benchmark contract。

## Hard target and required outputs

### A. 精确 feature-to-label 合同

冻结一个机器可检查 schema，逐项标记：

- feature 名称；
- 是否只依赖 \(N\)；
- 计算成本；
- 是否属于平方壳旧 no-go family；
- 若为新 family，新的条件机制是什么；
- hidden label；
- 预测输出是 point、interval、bucket、candidate set 还是 ranking。

任何未能证明 factor-blind 的 feature 在进入实验前即失败。

### B. “不增加信息”基准定理与表示收益边界

至少形式化并复核：

1. \((L,D)\leftrightarrow N\) 的双射/可逆性；
2. 有限预提交 multi-k signature 是 \(N\) 的确定函数；
3. 因此 positive result 不能被解释成额外信息源；
4. 若某预测器只等价于直接解码 \(N\) 后执行基线算法，则必须归类为 reparameterization，不计 bridge gain。

### C. 隐藏乘法壳坐标预测

至少对以下目标中的三类进行严格 held-out 测试，其中必须包含一类真正的 multiplicative-shell target：

1. prime-index / prime-rank interval；
2. M2 block / candidate neighborhood；
3. Gray block/rank bucket；
4. Fermat midpoint offset \(T\) interval；
5. predeclared multiplier ranking / \(k^*\) candidate set。

对每个目标报告：

- base rate；
- top-k / interval coverage；
- candidate-set size；
- 99% 与 99.9% recall 下的 compression ratio；
- bit-length 与 factor-ratio 分层结果；
- calibration 与 held-out degradation；
- 对 adversarial pairs 的失效模式。

### D. 预测必须落到实际搜索

任何“预测成功”都必须接入一个 factor-blind search wrapper：

\[
N\longrightarrow\text{public observables}\longrightarrow\text{candidate ranking/set}\longrightarrow\text{exact divisibility/gcd certificate}.
\]

必须记录：

- feature preprocessing cost；
- candidate generation cost；
- primality / gcd / divisibility checks；
- 成功率；
- amortized cost per successful split；
- memory / table cost；
- seed amplification（若有）。

比较对象至少包括：

- trial division / prime-rank scan；
- Fermat midpoint scan；
- 与候选机制相匹配的无 shell-priority baseline；
- PCF2 中可复用的 factor-blind benchmark 参考算法；
- 若 Hart/residual-priority 正式结果在执行时可用，则按其已冻结 cost contract 比较，不重复审计。

### E. 三档结论，不允许混用

**S1 — Predictive bridge.** 在 held-out 上，shell-derived factor-blind observables 对至少一个 multiplicative-shell hidden label 给出稳定且显著优于 size/base-rate baseline 的 candidate compression，但未必降低完整分解总成本。

**S2 — Search bridge.** S1 预测能转化为 exact factor search，在固定高 recall / success-rate 下，对匹配的非 shell baseline 给出可复核的总成本下降。

**S3 — Competitive factorization gain.** 在预注册 corpus 与成本口径下，对最强适用 factor-blind comparator 仍保持优势。只有达到这一档才允许使用“factorization gain”而不加限定。

### F. 主动 no-go / 反例搜索

必须主动寻找：

1. 相同或近似 \((L,D,C_{k_1},\ldots,C_{k_t})\) fingerprint，但隐藏 \((i,j)\)、M2 block 或 \(T\) 相差巨大的半素数；
2. 训练区间相关性在新 bit band 上反转或消失的例子；
3. 仅对 balanced/Fermat-friendly semiprimes 有效的伪规律；
4. 通过 feature cost 抵消全部 candidate compression 的情况；
5. 与 direct-N baseline 等价的伪“坐标收益”。

若反例能给出无限族或精确同余构造，优先冻结为 theorem/no-go；否则给出最大规模的 exact finite counterexample family。

### G. 可复核输出

至少返回：

- `research_returns/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE_RETURN_20260829.md`；
- 一个公开 factor-blind corpus/parameter manifest；
- 一个不含私有因子的结果 summary；
- exact checker / independent verifier；
- 若有正结果，给出从候选输出到非平凡因子的完整证书路径；
- 若无正结果，冻结失败 family、反例和不得重复开启的边界。

## Research value to preserve

本任务把两条已经各自达到边界的研究线接到一个真正未解决的接口：平方壳一侧有 factor-blind、可精确计算的整数几何，但原始静态 feature family 已出现负边界；乘法壳一侧有清晰的 factor-token/M2 几何，却缺少未知因子时的定位入口。

如果存在 S1/S2 正结果，它将首次证明“可见的加法/平方壳坐标”能够预测“隐藏的乘法壳局部性”，并给出从结构观察到实际 factor search 的可复核桥。若结果为负，它同样重要：可关闭一大类把确定性 shell reparameterization 当作因子信息来源的路线，并把后续研究转向真正增加算法能力的 residual priority、代数筛或其他 factor-blind mechanism。

## Success, kill, and return criteria

### Success

任务在以下任一情形可 `SUCCESS`：

1. **S1+：** 至少一个预先冻结的新 feature mechanism 在完全 held-out、无泄漏条件下，对 multiplicative-shell target 达到稳定 compression，跨 bit/factor-ratio strata 仍保留，并通过 adversarial tests；同时明确其尚未达到的成本层级；
2. **S2/S3：** 上述预测进一步转化为 exact factor search 的总成本优势，并在预声明 comparator 与成本口径下复核；
3. **Exact negative closure：** 证明一个覆盖目标 feature class 的 no-go，或构造足够强的无限/参数化反例族，解释为何该类 N-derived shell observable 不可能产生所需 localization/search gain。

### Kill / no-go

以下任一情况不得报告 bridge success：

- 使用真实因子、factor-derived label 或 verifier 私有状态作为 feature；
- 只在训练/调参集合有效；
- 只重复 `RR-2A424E3B8EC11DC1278C` 已关闭的 raw shell/multi-k correlation search；
- 只在 balanced 或 near-twin semiprimes 上改善而在广义 strata 崩溃；
- candidate compression 被 feature/preprocessing cost 完全抵消，却仍宣称算法收益；
- 仅重排 N 或已知因子后的 M2/Gray 节点而没有 factor-blind 预测；
- 仅给统计相关性，不给 exact split certificate 或明确的 S1-only 限定；
- 未通过 PCF2 等级的 leakage tests。

### Return

返回必须给出单一 terminal verdict：

- `S1_PREDICTIVE_BRIDGE_ONLY`；
- `S2_SEARCH_BRIDGE`；
- `S3_COMPETITIVE_FACTORIZATION_GAIN`；
- `NEGATIVE_BOUNDARY`；
- `MIXED / PARTIAL`（仅当不同 feature class 被分别封闭且仍有明确未决残差）。

同时必须列出：已冻结 feature family、hidden targets、held-out corpus bands、leakage audit、对照算法、总成本口径、最强反例、可复核 checker，以及是否存在值得单独发布的 successor residue。任务终止不自动证明 parent objective 完成。
