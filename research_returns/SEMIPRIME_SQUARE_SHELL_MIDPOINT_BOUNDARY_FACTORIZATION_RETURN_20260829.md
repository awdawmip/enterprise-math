# 半素数平方壳中点—边界—邻近素数分解广域探索：研究返回

Task: `RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION`  
Publication: `TP2-12778A2D48A1D5A57BA9`  
Researcher-ID: `EM-SSMF1-7D31C8`  
Claim: `chatgpt-ssmf1-20260829-1241-7d31c8`  
Execution branch: `research/semiprime-square-shell-midpoint-boundary-em-ssmf1-7d31c8`  
Execution base: `949a8eb7ba92b1d9de8a4ad5e494596b1a1077e3`

## Frozen verdict

`SUCCESS / STRUCTURAL_ONLY / EXACT_FACTOR-RATIO_AND_MULTIPLIER_BRIDGES / NO_GENERAL_SHELL-ONLY_FACTOR_SEARCH_REDUCTION_ESTABLISHED`

本任务在规定范围内完成了“中心—边界—邻近素数—multi-k—模筛”五条线的统一审计。平方壳确实紧贴 Fermat 分解状态，而且可以把若干关系写成比原任务书更强、更透明的精确公式；但本轮没有得到一个超出已知 Fermat / Lehman / Hart 类近平方路线的 factor-blind 搜索收缩规则。

最关键的结构结论是：

1. 真正的因子中点位移主项由因子比 `q/p` 决定；`sqrt(N)` 附近的邻近素数中心只能提供一个局部 prime-gap 尺度的加性修正。
2. 对 `k=ab`，真正 productive multiplier 的几何本质是小有理数 `a/b` 对隐藏因子比 `q/p` 的逼近；`4kN` 到上方平方的壳残差只是 rounding phase，单独按其大小排序 `k` 不可靠。
3. 壳坐标上的模筛可以大幅减少 Fermat 平方判定，但它精确等价于经典 quadratic-residue Fermat sieve，不构成本任务独有的新分解信息。
4. `(L,D)` 可逆确定 `N`，固定 `k` 的 `D(kN)` 也由 `N,k` 确定；因此“平方壳提供了额外信息”这一表述必须否定。未来若有增益，只能来自更便宜的表示、搜索顺序或可证明剪枝，而不是信息增量。

## 1. 基线恒等式与更强的因子比坐标

沿用任务书定义

`N=pq`, `A=(p+q)/2`, `B=(q-p)/2`, `A0=ceil(sqrt(N))`, `T=A-A0`,

以及上方平方残差 `b=A0^2-N`，则

`B^2 = b + 2*A0*T + T^2`。

令 `x=sqrt(N)`、`rho=q/p>=1`、`eta=(1/2)log(rho)`，则还得到精确双曲坐标

`A/x = cosh(eta)`,

`B/x = sinh(eta)`,

从而

`A-x = x(cosh(eta)-1) = B^2/(A+x) = (sqrt(q)-sqrt(p))^2/2`，

以及

`T = (A-x) - (ceil(x)-x)`。

这把“Fermat 需要走多远”拆成了一个由因子失衡完全决定的连续主项，加一个小于 1 的取整修正。近平衡时 `eta` 小，`A-x ~ x*eta^2/2` 是二阶量；因子明显失衡时该项迅速增长。

## 2. 邻近素数中心的精确边界

令

`ell=PrevPrime(x)`, `u=NextPrime(x)`, `g=u-ell`, `c=(ell+u)/2`。

因为 `ell<x<u`，严格有

`|c-x| < g/2`。

于是

`A-c = (A-x) + (x-c)`，

所以

`|(A-c)-(A-x)| < g/2`

并且

`|A-c| >= (A-x)-g/2`。

这给出一个清楚的 no-overclaim 边界：邻近素数中心可以改变 midpoint 误差，但其可解释部分被局部素数间隙控制；它不会消除由 `q/p` 造成的主失衡位移。

相对于整数 Fermat 起点还有精确式

`(A-c)-T = A0-c`。

因此把起点从 `A0` 改成 `c`，本质上只是加入一个由 `N` 附近局部素数间隙决定的有限平移。

### 连续素数因子的特殊族

若 `p<q` 本身是连续素数且 `N=pq`，则

`p < sqrt(N) < q`

且区间内没有其他素数，因此精确有

`PrevPrime(sqrt(N))=p`, `NextPrime(sqrt(N))=q`。

这确实给出一个“边界直接就是因子”的无限结构族。但它并不自动转化为优于 Fermat 的候选复杂度。由 Bertrand 定理 `q<2p`，令 `t=sqrt(q/p)`，则连续 Fermat 主位移与向下找到 `p` 的实数距离之比为

`(A-sqrt(N))/(sqrt(N)-p) = (t-1)/2 < (sqrt(2)-1)/2 ~= 0.2071`。

也就是说，在这个最漂亮的邻近素数边界族上，Fermat 的 midpoint 距离本来就比从 `sqrt(N)` 向下摸到因子的距离更短一个常数因子；边界精确性是结构事实，不是免费加速。

## 3. prime-rank 与 midpoint 的阶段转换

定义 `J_p=pi(floor(sqrt(N)))-pi(p)`。全量普查清楚显示：

- `q/p<=1.1` 时，Fermat 位移 `T` 几乎总比向下试素数的 rank 窗口短；
- `1.1<q/p<=2` 时出现过渡区；
- `q/p>2` 后，`T` 很快变得远大于 `J_p`；
- 强失衡时从 `sqrt(N)` 向下试素数虽然比 Fermat midpoint 更短，但此时“小因子优先”的普通试除/分解基线已经是必须比较的对象，不能把这一现象归功于平方壳。

这与上面的双曲公式一致：Fermat 对非常近平衡因子有二阶优势，prime-rank/距离则是一阶地离开 `sqrt(N)`。

## 4. multi-k 的精确分解：真正目标是有理逼近因子比

对任意 `k=ab`，直接展开得到

`(ap+bq)^2-(ap-bq)^2 = 4abpq = 4kN`。

更重要的是

`ap+bq - 2*sqrt(kN) = (sqrt(ap)-sqrt(bq))^2`。

因此对于给定分解 `k=ab`，若 `a/b` 逼近 `q/p`，`ap` 与 `bq` 接近，`4kN` 就存在非常近的真正 difference-of-squares 中点。

令

`c_k=ceil(sqrt(4kN))`, `b_k=c_k^2-4kN`。

若使用隐藏因子定义 oracle target `x=ap+bq`，则

`T_{k,a,b}=x-c_k`

满足

`T_{k,a,b}=(sqrt(ap)-sqrt(bq))^2-(c_k-2sqrt(kN))`。

这里第一项是由隐藏因子比控制的 Diophantine approximation defect，第二项才是平方壳的 rounding correction。故仅凭 `b_k` 小，不足以判断该 `k` 是否真正 productive。

这与 Lehman 1974 的结构完全对齐：Lehman 系统搜索 `x^2-y^2=4kN`，并明确使用 `k=ab` 与小分数 `a/b` 的 Farey-like dissection；Hart 2012 也明确把其 one-line algorithm 描述为 Fermat 的 multiplier variant。相关文献边界见文末。

## 5. 一个杀伤性精确反例：最好的 k 可以拥有最大的壳残差

取

`N=9,171,667 = 2,851 * 3,217`。

在 `1<=k<=64` 中，`k=56=7*8` 有

`7q+8p = 45,327 = ceil(sqrt(4*56*N))`，

且

`b_56=(7q-8p)^2=289^2=83,521`。

所以 `k=56` 在第一个 midpoint 就命中：`T_56=0`。

但是在全部 `k=1..64` 中：

- 按原始上方平方残差 `b_k` 从小到大排序，`k=56` 排第 `64/64`，即最后一名；
- 按归一化残差 `b_k/(2*c_k)` 排序，仍排第 `62/64`。

因此猜想“优先测试更接近上方平方边界的 `kN`/`4kN`，就会更早找到好 multiplier”被一个完全精确的有限反例击穿。真正决定此例的不是 rounding residual，而是 `7/8` 与 `q/p` 之间的匹配。

## 6. 模筛：真实有效，但属于 Fermat 基线

对奇素数 `ell`，若 `ell` 不整除 `N`，考虑允许的 Fermat 中点剩余类

`A^2-N = square (mod ell)`。

精确计数为：

- 若 `N` 是模 `ell` 的二次剩余：允许 `(ell+1)/2` 个 `A mod ell`；
- 若 `N` 是非二次剩余：允许 `(ell-1)/2` 个；
- 若 `ell|N`：所有 `ell` 个剩余类均通过。

证明可由计数 `(A-B)(A+B)=N` 的有序非零因子对直接得到；checker 对 `ell=3,5,7,11,13,17,19,23,29,31` 的每个非零 `N mod ell` 全部复核。

对 wheel `(64,3,5,7,11,13)`，在 `N<=10^7` 的全部不同奇半素数上，允许 Fermat midpoint 剩余类的平均比例为

`0.0082359415221505`，

即平均只保留约 `0.824%` 的 full square-test 候选，约为 `121x` 的平方判定削减。

但这不是平方壳新增算法：`b+2*A0*T+T^2` 只是 `A^2-N` 用 `T` 坐标重写。经典 Fermat 优化本来就会用小模二次剩余跳过不可能候选；现代工作也继续研究对 close-factor Fermat 的更强筛法。因此本项记为 `BASELINE_EQUIVALENT / COMPUTATIONALLY_USEFUL`，不能记为新 shell leverage。

## 7. 全量普查：N <= 10^7

使用 Eratosthenes 精确生成素数，并枚举所有 `p<q`、`pq<=10^7` 的不同奇半素数；素数平方因可直接整数平方根识别而排除。总样本：

`1,555,366`。

| q/p 分层 | 样本 | T 中位 | T P90 | J_p 中位 | J_p P90 | T <= J_p+1 | 连续素数因子 |
|---|---:|---:|---:|---:|---:|---:|---:|
| <=1.01 | 699 | 0 | 0 | 0 | 1 | 100% | 322 |
| 1.01-1.1 | 7,202 | 0 | 2 | 6 | 12 | 100% | 110 |
| 1.1-2 | 51,701 | 33 | 111 | 42 | 84 | 65.836% | 13 |
| 2-10 | 140,169 | 524 | 1,425 | 136 | 221 | 0.0735% | 0 |
| >10 | 1,355,595 | 86,288 | 833,952 | 306 | 415 | 0% | 0 |

其他精确 census 统计：

- 连续素数因子对：`445`；`both_local_neighbors=445`，与定理完全一致；
- `p` 恰为 `sqrt(N)` 下方最近素数：`795`；
- `q` 恰为上方最近素数：`754`；
- 邻近素数中心相对 Fermat 起点的最大位移仅 `17`；局部最大素数间隙 `34`；
- 同一数据集中最大真实 Fermat `T=1,663,504`；最大向下因子 rank `J_p=444`；
- 将局部 prime-center 用作中点，绝对误差比 Fermat 起点改善 `572,472` 次、恶化 `781,497` 次、相等 `201,397` 次。它不是一个单调改进规则。

## 8. multi-k census 与独立 holdout

为避免 `k` 与小因子直接有 `gcd` 的平凡泄漏，multi-k reservoir 只取 `p>64`，测试 `1<=k<=64`。每个样本用隐藏因子标签仅计算 oracle “最佳 k”；部署特征只用 `N,k` 的壳残差。

### N<=10^7 reservoir

| q/p | n | raw b_k 排序下最佳 k 的中位 rank | Top-10 命中 | 最坏 rank |
|---|---:|---:|---:|---:|
| <=1.01 | 699 | 1 | 100% | 5 |
| 1.01-1.1 | 1,000 | 6 | 79.2% | 19 |
| 1.1-2 | 1,000 | 14 | 42.4% | 63 |
| 2-10 | 1,000 | 14 | 41.8% | 64 |
| >10 | 1,000 | 36 | 18.1% | 64 |

近平衡层 raw residual 看起来很好，主要原因是 `k=1` 本来就常是 oracle 最优；离开近平衡区后排序迅速退化。

### 24/32/40/48/64-bit holdout

每个 bit-size × ratio-band 独立生成 `40` 个 semiprime，总计 `1,000` 个 holdout。

按 ratio 分层，raw residual 排序下 oracle 最佳 k 的中位 rank / Top-10 命中分别为：

- `<=1.01`: `1 / 88.5%`
- `1.01-1.1`: `7 / 70.5%`
- `1.1-2`: `15 / 39.0%`
- `2-10`: `13 / 46.0%`
- `>10`: `39 / 20.0%`

归一化 residual 也没有救回这一问题；强失衡层中位 rank 为 `27`，Top-10 仅 `27%`。

另以最简单壳相位 `b/L` 对 `log(q/p)` 做 Spearman 诊断，24/32/40/48/64 bit 的相关系数分别为

`0.516, 0.324, 0.197, 0.298, 0.229`。

这不足以支持一个稳定、可部署的 factor-ratio predictor；它最多是有限样本信号，不作算法结论。

## 9. 负对照

固定 `N<=10^7`、`k<=64`，用独立 deterministic negative-control replay：

- 2,000 个素数：非平凡 immediate multi-k factor hit = `0`；
- 2,000 个三素数乘积：hit = `1,885`；
- 2,000 个随机奇数：hit = `1,619`。

因此 multi-k difference-of-squares 的即时命中并不是“半素数专属签名”。负对照不赋予 semiprime-only 的 `T/J_p` 标签，只用于防止把一般合数现象误判成 semiprime structure。

## 10. 与经典路线的等价/增益审计

### Fermat

平方壳上方残差 `b` 就是 Fermat 从 `A0=ceil(sqrt(N))` 出发时的初始 `A0^2-N`。模筛也是对同一个二次剩余条件的坐标改写。因此：

`SHELL_FERMAT_BASELINE = EXACT_REPARAMETERIZATION`。

### Lehman / Lawrence 路线

Lehman 的原始 1974 工作明确以 Fermat difference-of-squares 的修改为出发点，搜索 `x^2-y^2=4kN`，并让 `k=ab` 与小分数 `a/b` 参与 Farey-like dissection。当前推导出的

`ap+bq-2sqrt(kN)=(sqrt(ap)-sqrt(bq))^2`

正好解释了为何该路线是在逼近隐藏 `q/p`。因此：

`MULTI_K_RATIONAL_APPROXIMATION = CLASSICAL_ROUTE_BRIDGE / NOT_NEW_ALGORITHM`。

### Hart one-line factorization

Hart 2012 明确把算法称为 Fermat 的变体，并说明其作为一般 factoring algorithm 的 heuristic `O(n^(1/3))` 行为，同时把 Lehman 列为直接先驱。当前 raw shell-residual ordering 没有提供一个取代该类 multiplier strategy 的稳定新 selector。因此：

`RAW_SHELL_RESIDUAL_K_ORDERING = REFUTED_AS_GENERAL_SELECTOR`。

### 外部文献锚点

- R. Sherman Lehman, *Factoring Large Integers*, Mathematics of Computation 28 (1974), 637–646, DOI `10.1090/S0025-5718-1974-0340163-2` / JSTOR `10.2307/2005940`.
- William B. Hart, *A One Line Factoring Algorithm*, Journal of the Australian Mathematical Society 92 (2012), 61–69, DOI `10.1017/S1446788712000146`.
- Markus Hittmeir, *Integer factorization as subset-sum problem*, 2022, arXiv `2205.10074`;该文明确给出对 close-factor Fermat 的 sieve 改进，进一步说明“模筛减少平方测试”不是新的 shell-only 现象。

## 11. 统一分类表

| 主线 | 本轮结论 | 分类 |
|---|---|---|
| 中心 / Fermat | `T` 的连续主项由 `q/p` 精确控制 | `EXACT_STRUCTURE` |
| 邻近素数边界 | 修正受 local prime gap 控制；连续素数因子族可精确恢复 | `EXACT_STRUCTURE / SPECIAL_FAMILY` |
| prime rank | 近平衡 Fermat 优；失衡后 rank 短但落入普通小因子搜索基线 | `STRUCTURAL_TRADEOFF` |
| 模筛 | 平均 wheel 保留约 0.824%（census） | `USEFUL_BUT_CLASSICAL_FERMAT_SIEVE` |
| multi-k | productive k 等价于小 `a/b` 逼近 `q/p` | `EXACT_LEHMAN_BRIDGE` |
| raw residual 排 k | 中度/强失衡不稳定，存在 best-k-last 精确反例 | `REFUTED_GENERAL_SELECTOR` |
| `(L,D,D_k)` 信息量 | 全部由 `N,k` 决定 | `NO_EXTRA_INFORMATION` |

## 12. 成本与 no-overclaim

本任务没有把任何 oracle 标签用于部署规则：`p,q,A,B,T,J_p` 只用于评价。所有 candidate deployed features 都能从 `N` 独立计算。

同时必须明确：

- 计算 `PrevPrime/NextPrime` 本身有素性搜索成本，不能视为免费；
- wheel 预计算可摊销，但其收益属于标准 Fermat sieve；
- multi-k 每个候选至少要支付平方根/平方测试或等价增量更新成本；
- 对强失衡数，普通 trial division、Pollard 类方法、Lehman/Hart 等都是更合理的比较基线；本返回不声称平方壳优于一般整数分解算法；
- 全量/holdout 统计只证明所测试特征的行为，不能证明不存在更复杂的 factor-blind shell-derived predictor。

## 13. 最小未解残差

本任务最值得继续的残差已经被压缩为一个更具体的问题：

> 是否存在一种只由 `N` 可计算、且计算成本显著低于分解本身的 feature，能够稳定估计隐藏因子比 `q/p` 的某个小分数近似 `a/b`，从而在 Lehman/Hart 型 `k=ab` 搜索中提前选出 productive multipliers？

这比继续研究“哪个 `kN` 离平方边界更近”更准确。后者已被精确反例否定为一般 selector。若未来任务没有新的 ratio-approximation feature、复杂度论证或新的结构来源，仅扩大同一 census 不构成有价值 successor。

## 14. 冻结边界

最终分类：`STRUCTURAL_ONLY`。

已证明：双曲因子比坐标、邻近素数中心 gap bound、连续素数因子边界、`k=ab` multiplier identity、odd-prime modular filter count、壳信息可逆性边界。  
有限计算事实：`N<=10^7` 全量 census、`k<=64` reservoir、1,000 个 24–64 bit holdout、负对照和精确 `N=9171667` 反例。  
经验信号：简单 shell phase 对因子比存在弱到中等相关，但跨 bit 不稳定，不提升为算法。  
经典等价项：Fermat 初始残差、quadratic-residue wheel、Lehman/Hart multiplier near-square route。  
未解决：低成本 factor-blind `q/p` rational-approximation predictor 是否存在。

## Replay

主 checker：

`python scripts/check_semiprime_square_shell_midpoint_boundary_factorization.py --limit 10000000 --reservoir 1000 --kmax 64 --holdout-per-cell 40`

终端：`SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_CHECK=PASS`

负对照：

`python research_artifacts/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION/negative_controls_20260829.py`

终端：`SEMIPRIME_SHELL_NEGATIVE_CONTROLS=PASS`

Frozen certificate: `research_artifacts/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION/certificate_20260829.json`.

No Working Truth, Foundation mutation, novelty claim, canonical promotion, or automatic merge is requested. Driver review is required.
