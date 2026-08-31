# 半素数 residual-priority / Hart streaming 全成本审计：研究回报

Researcher-ID: `EM-SSMFCOST-401A6D`  
Task: `RS-SEMIPRIME-RESIDUAL-PRIORITY-HART-STREAMING-COST-AUDIT`  
Publication: `TP2-8E5A7D21C30F694B2D11`  
Claim: `chatgpt-ssmfcost-20260829-1727-401a6d`  
Branch: `research/semiprime-residual-priority-hart-cost-em-ssmfcost-401a6d`

Status: `TERMINAL_RESEARCH_RETURN / NEGATIVE_BOUNDARY / NO_WORKING_TRUTH_GRANT`

## 1. 结论

硬目标结论：

`RESIDUAL_PRIORITY_HART_STREAMING_TOTAL_COST_CLASSIFIED = NEGATIVE_FOR_FROZEN_SEQUENTIAL_SCORE_FAMILY`

父任务留下的 `score(k)=e_k/(2*x_k-1)` 确实存在**条件命中排名提前**，但在同一 multiplier 残差流、同一模筛预算、计入 residual generation / square test / gcd / queue-bucket 开销后，没有形成可复现的总成本优势。

本结果不是“所有 factor-blind 选 k 方法都不可能”。它关闭的是本任务冻结的这一族：

- `x_k=ceil(sqrt(4*k*N))`；
- `e_k=x_k^2-4*k*N`；
- `score(k)=e_k/(2*x_k-1)`；
- 按 `k=1,2,...,K` 顺序生成 Hart-M4 residual；
- 同一 `mod 6720` 二次剩余筛；
- 32 个 score buckets；
- chunk `W in {4,16,64,256,1024}` 的局部重排；
- 以及一个 `score<1/2` 先测、其余延迟并在失败时 fallback 的 completeness stress test。

## 2. 结构事实：score 是 Hart residual 的归一化位置，不是额外 oracle

令

`x=ceil(sqrt(4*k*N))`, `e=x^2-4*k*N`.

由

`(x-1)^2 < 4*k*N <= x^2`

立刻有

`0 <= e < x^2-(x-1)^2 = 2*x-1`.

因此

`0 <= score=e/(2*x-1) < 1`.

所以 `score` 精确表示 `4*k*N` 到其**上一个平方壳宽度内的下一个平方**的归一化距离。它没有引入 `N,k` 之外的新信息。

更关键的是：任何要按这个 score 决定优先级的 exact policy，必须先得到 `e_k`（或等价的精确 residual transport）。而 matched Hart 流在同一个 `k` 上也正需要这个 residual 才能进行模筛与平方判定。因此，若有人找到更便宜的 `e_k` 精确 transport，它同样可以直接供 Hart baseline 使用，不能只把 transport 优惠记到 residual-priority 一边。

## 3. 与 Hart 的精确匹配边界

Hart 2012 的 One Line Factor 直接迭代 multiplier `i`，计算 `s=ceil(sqrt(n*i))`，再测试 `s^2 mod n` 是否为平方；论文同时明确讨论先给 `n` 乘一个固定常数 multiplier `M` 再运行该流程。

父任务的 `4*k*N` residual 因而正是这个 Hart 流的固定 `M=4` 版本。为隔离“排序是否有价值”而不混入不同候选族，本审计使用：

`HART_M4_ASC`: 对相同 `k=1..K`，生成相同 `x_k,e_k`，通过相同 `mod 6720` sieve 后立即平方测试，遇到第一个 productive multiplier 即停止。

这比拿一个不同 multiplier 集合做比较更严格：两边 residual 生成、模筛和 gcd 语义完全相同，唯一变化是**何时测试已生成的 survivor**。

参考：

- W. B. Hart, *A One Line Factoring Algorithm*, J. Aust. Math. Soc. 92 (2012), 61–69, DOI `10.1017/S1446788712000146`.
- R. S. Lehman, *Factoring Large Integers*, Math. Comp. 28 (1974), 637–646, DOI `10.1090/S0025-5718-1974-0340163-2`.

## 4. 成本机制

### 4.1 no-hit 严格边界

对固定有限窗口 `1..K`，若窗口内没有 productive multiplier：

- complete Hart-M4 与 complete residual-priority 都必须生成同样的 `K` 个 residual；
- 同一 `mod 6720` sieve 后，它们最终必须检查同一批 surviving residual；
- 平方与 gcd 机会相同；
- residual-priority 还增加 enqueue / bucket scan / deferred-queue 维护。

因此在任何给 bookkeeping 正成本的模型中，**no-hit case 上完整 residual-priority 被 matched Hart-M4 严格支配**。

最终冻结 holdout 里这一类是 `73/112 = 65.1786%`。

### 4.2 hit case 的 break-even 条件

如果 chunk/buffer 为了重排而越过 Hart 的首个 productive `k0` 才开始测试，则额外 residual generation 是不可回收的。只有平方测试节省满足

`saved_square_cost > extra_generation_cost + queue_cost + extra_filter_cost`

才可能打平。

threshold streaming 可以在 `k0` 自身 score 足够低时，边生成边延迟高-score survivors，从而在不多生成 residual 的情况下少做一部分 square tests；但为了保持有限窗口 completeness，一旦 productive `k0` 被延迟，就必须继续搜索乃至扫描到 `K`，然后 fallback。这形成了明显的右尾风险。

这正是实验里观察到的模式。

## 5. 实验设计

### 5.1 factor-blind 部署

算法函数只接收 `N,K`。`p,q` 和 factor-ratio stratum 单独冻结在 verifier-label 文件中，只有算法全部运行完成后用于核对 `N=p*q` 与分层报告；不参与 schedule、bucket、threshold 或 stopping。

### 5.2 位宽与分层

测试位宽：

`32,40,48,56,64,80,96`.

四个 factor-ratio 生成层对应不同 lower-factor bit budgets：

- balanced-ish: `pbits=floor(bits/2)`;
- moderate: `pbits=floor(bits/2)-2`;
- unbalanced: `pbits=floor(bits/2)-5`;
- strong: `pbits=floor(bits/3)`.

探索阶段共有 448 cases；在 bucket/threshold 参数冻结后，另生成 **112 个此前未运行的最终 holdout**（每 bit × stratum 4 个，seed `202608291729`）。

### 5.3 K 范围

`K_full=ceil(N^(1/3))`,  
`K_test=min(K_full,65536)`.

所以：

- 32/40/48-bit 是完整 `N^(1/3)` multiplier window；
- 56/64/80/96-bit 是 `65536` capped finite-window evidence。

高位部分不能被解释成“完整 Hart 范围失败率”。

### 5.4 模筛与成本向量

双方使用完全相同的 quadratic-residue table：

`QR_MOD=6720=64*3*5*7`.

冻结的操作向量为：

`(gen, mod, sq, gcd, enqueue, bucket_scan)`.

主报告 scalar proxy 只是便于排序：

- `gen=1`;
- `mod=1/64`;
- `sq=1/2`;
- `gcd=1`;
- `enqueue=1/64`;
- `bucket_scan=1/128`.

最终结论同时做 `sq/gen = 0.25,0.5,1,2,4,8` 的敏感性检查，不依赖单一权重。

## 6. 最终 unseen holdout：112 cases

Hart-M4 在测试窗口内命中 `39/112`；未命中 `73/112`。

按 bit：

| bits | hits / 16 | coverage | window |
|---:|---:|---:|---|
| 32 | 10 / 16 | 62.5% | full `ceil(N^(1/3))` |
| 40 | 12 / 16 | 75.0% | full |
| 48 | 13 / 16 | 81.25% | full |
| 56 | 4 / 16 | 25.0% | capped 65536 |
| 64 | 0 / 16 | 0% | capped |
| 80 | 0 / 16 | 0% | capped |
| 96 | 0 / 16 | 0% | capped |

### 6.1 chunk bucket

总成本比 `C_bucket/C_Hart`：

| W | median | mean | wins (<1) | max |
|---:|---:|---:|---:|---:|
| 4 | 1.060322 | 1.061408 | 0 / 112 | 1.0962 |
| 16 | 1.016033 | 1.022726 | 0 / 112 | 1.2635 |
| 64 | 1.004968 | 1.036175 | 0 / 112 | 1.9314 |
| 256 | 1.002202 | 1.174425 | 0 / 112 | 7.5942 |
| 1024 | 1.001511 | 1.888528 | 0 / 112 | 30.2417 |

**五个预冻结 W 在最终 holdout 上都没有一个总成本胜例。**

小 W 的问题是 bookkeeping 大于极小的 square-test savings；大 W 虽有更强的 residual rank 重排能力，但必须先多生成一整个 buffer，尾部代价迅速增大。

### 6.2 threshold stress test

冻结 stress policy：

- score bucket `0..15`（即 `score<1/2`）立即测试；
- bucket `16..31` deferred；
- phase 1 无命中时按原 k 顺序 fallback，恢复有限窗口 completeness。

结果：

- phase-1 hit: `33`;
- fallback hit: `6`;
- no-hit: `73`;
- 成本 wins: `26/112`;
- median ratio: `1.000628`;
- mean ratio: `3.965533`;
- p95: `19.6403`;
- max: `110.0836`.

这说明 residual score **确实能在一部分样本上减少平方测试**；但同一个规则对高-score 首命中和 no-hit case 要承担扫描/回退风险，整体不是稳定成本改进。不能把那 26 个 wins 单独当作算法收益而忽略 73 个 no-hit 与 6 个 fallback。

### 6.3 权重敏感性

把 `sq/gen` 从 `0.25` 一直提高到 `8`：

- 五个 chunk family 的 holdout **median 和 mean 始终 > 1**；
- `W=4` 在所有权重上仍 `0` wins；
- 即使把平方测试计为 residual generation 的 8 倍，较大的 W 会出现少数个体 wins，但总体中位/均值仍没有翻转；
- threshold `score<1/2` 在整个权重带上 median 仍略高于 1，mean 仍大于 3。

所以负结论不是 `sq=0.5` 这一单点权重造成的。

## 7. 探索集与 holdout 一致性

在前 448 个 pre-freeze cases 上，默认成本下：

- W=4: median `1.060320`, wins `0`;
- W=16: median `1.016035`, wins `0`;
- W=64: median `1.004968`, wins `1`;
- W=256: median `1.002201`, wins `3`;
- W=1024: median `1.001511`, wins `3`.

最重要的是，最终 112-case unseen holdout 把这些零星 wins 全部压回 `0/112`，同时保留“大 buffer 尾部更坏”的同一结构。不是只看一个偶然 discovery split 得出的结论。

## 8. Terminal classification

本任务硬目标结论：

`NEGATIVE_BOUNDARY / SCORE_RANK_GAIN_DOES_NOT_SURVIVE_MATCHED_TOTAL_COST`.

可冻结的事实是：

1. residual-priority score 是 Hart-M4 residual 的归一化平方壳位置；
2. 它可能改善**条件 square-test rank**；
3. 对冻结的 sequential/bucket/threshold family，没有得到可复现总成本收益；
4. complete no-hit case 存在精确的额外-bookkeeping 支配边界；
5. 大 buffer 通过更强重排换来的 square-test savings 被 generation-ahead 与尾部损失吞掉；
6. threshold deferral 的个体 wins 真实存在，但 completeness fallback 造成不可接受的右尾，不能提升为一般算法优势。

## 9. 不应过度外推

本结果不排除：

- 一个能**非顺序选择 k**、且无需先生成中间 Hart residual 的新 factor-blind selector；
- 一个比 Hart baseline 也能共享的 residual transport 更强、真正产生新信息的廉价 observable；
- 不同 sieve / arithmetic / SIMD 实现下的常数工程优化；
- ECM、SQUFOF、Lehman 其他 schedule 等不同算法族。

因此不能写成“一切乘法壳/平方壳都无助于分解”，更不能写成一般 factoring lower bound。

## 10. Tool reuse gate

任务理解后检查了 `enterprise_toolbox_registry.json`。通用 `T1 Enterprise Scale Enumeration / Valuation Calculus` 的 `shell` trigger 不提供整数分解所需的 multiplier/square/gcd 语义，故：

`GENERIC_TOOLBOX = NOT_APPLICABLE_FOR_FACTORIZATION_CORE`.

本任务复用的是父结果已经冻结的 exact square-shell / multiplier-Fermat transport 与 checker discipline；没有产生值得抽成新全局工具族的机制。

## 11. 冻结输出

- `research_returns/SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT_RETURN_20260829.md`
- `research_checks/SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT_CHECK_20260829.py`
- `research_artifacts/SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT/frozen_holdout_public_cases_20260829.json`
- `research_artifacts/SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT/frozen_holdout_verifier_labels_20260829.json`
- `research_artifacts/SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT/summary_20260829.json`
- `research_execution_records/RS-SEMIPRIME-RESIDUAL-PRIORITY-HART-STREAMING-COST-AUDIT/ER-CD403E891A486183B5B9.json`

Local frozen-holdout checker result before publication:

`PASS` — 112 cases, 39 Hart-window hits, 73 no-hits, zero metric/signature/label failures.

No Working Truth, Foundation authority, new global tool, or canonical-promotion claim is made.
