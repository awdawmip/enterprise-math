# 半素数平方壳中点—边界—邻近素数分解广域探索：研究回报

Researcher-ID: `EM-SSMF1-5A7C2E`  
Task: `RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION`  
Publication: `TP2-12778A2D48A1D5A57BA9`  
Claim: `chatgpt-ssmf1-20260829-1240-5a7c2e`  
Branch: `research/semiprime-square-shell-midpoint-boundary-em-ssmf1-5a7c2e`

Status: `TERMINAL_RESEARCH_RETURN / EXACT_STRUCTURE_PLUS_REPRODUCIBLE_NO_GO / NO_WORKING_TRUTH_GRANT`

## 0. 结论先行

本任务得到的是 **B + C 型结果**，不是新的分解算法：

1. **单平方壳中点路线严格等价于 Fermat difference-of-squares 扫描。** 上方平方残差 `b` 恰好是 Fermat 的首个残差；真实中点偏移 `T` 恰好是从 `A0=ceil(sqrt(N))` 开始，第一次使残差成为平方所需的步数。
2. **真正控制宏观中点距离的是隐藏因子比 `q/p`，平方壳只贡献小于 1 的舍入修正。** 精确式为
   
   `T = sqrt(N) * (cosh(0.5*log(q/p)) - 1) - (ceil(sqrt(N)) - sqrt(N))`。
3. **局部邻近素数特征没有稳定预测因子 prime-rank。** 从 `sqrt(N)` 附近向下测试素数直到 `p`，其候选数就是 `J_p+1`，本质上是重新排序的 trial division；`J_p` 本身是带因子标签的 oracle 诊断量，不可作为部署输入。
4. **multi-k 平方壳路线落在 multiplier-Fermat / Lehman / Hart 已知族中。** 对 `kN` 或 `4kN` 的上方平方残差，本质上就是这些算法测试的近平方残差；平方壳表示没有额外增加 factor-blind 信息。
5. 对 `N<=10^7` 的全部 `1,555,366` 个奇、非平方半素数做了精确普查。单壳位置与中点/因子比的总体相关几乎为零；加入局部素数间隙及 `k=2..16` multi-k 壳特征后，在独立 `8e6..1e7` holdout 上对 `log(1+T)` 的预测反而略差于只用 `log N` 的基线。
6. 发现一个值得保留但**尚不能称算法优势**的残余：在小尺度固定 `k<=64` 窗口内，按 normalized upper-square residual 排序，能在“窗口内本来存在立即 productive multiplier”的条件样本中提前命中；但命中覆盖率随 bit size 快速坍塌（24 bit 43.3%，32 bit 8.8%，40 bit 2.2%，48 bit 0.6%，64 bit 0%）。它只留下一个窄的后续成本审计问题。

因此当前硬目标分类为：

`EXACT_STRUCTURE_WITHOUT_NEW_FACTORIZATION_ADVANTAGE + REPRODUCIBLE_FEATURE_FAMILY_NO_GO`

这不声称排除所有可能的 N-only 分解算法；只关闭本任务规定的“相邻平方壳 / 局部邻近素数 / 原始 multi-k 壳相位”作为独立 factor-selection 信号的当前路线。

---

## 1. 精确结构 I：平方壳就是 Fermat 的起点坐标

令

`N=pq`, `3<=p<q`, `s=floor(sqrt(N))`, `A0=s+1`,

`b=A0^2-N`, `A=(p+q)/2`, `B=(q-p)/2`, `T=A-A0`。

定义

`F_N(t)=b+2*A0*t+t^2`。

直接展开得

`F_N(t)=(A0+t)^2-N`。

于是：

### Theorem 1 — least-square characterization

对 distinct odd semiprime `N=pq`，

`T = min { t>=0 : F_N(t) is a perfect square }`。

证明：在 `t=T` 时

`F_N(T)=A^2-N=B^2`。

反过来，若 `F_N(t)=y^2`，则

`N=(A0+t-y)(A0+t+y)`。

由于 `N` 是两个不同奇素数的乘积，正整数因子对只有 `(1,N)` 与 `(p,q)`。非平凡因子对的 midpoint 唯一是 `A=(p+q)/2`；平凡因子对 `(1,N)` 的 midpoint `(N+1)/2` 更大。因此从 `A0` 向上第一次出现平方残差的位置正是 `A`，即 `t=T`。

所以任务给出的桥

`B^2=b+2*A0*T+T^2`

不是“接近 Fermat”，而是 **Fermat 扫描的精确坐标化**。

### 成本含义

- naive Fermat：`T+1` 个 midpoint candidates，最多 `T+1` 次平方判定；
- 壳写法：仍然必须识别 `F_N(t)` 首次成为平方的 `t`；若逐点做，候选数完全相同；
- 任何只对 `F_N(t)` 做二次剩余筛选的规则，属于 Fermat quadratic-residue sieve 的同一候选空间，除非证明能在不逐点覆盖等价候选的情况下跳跃。

在 3000 个 census 样本上，使用模数

`M=6720=64*3*5*7`

保留 `F_N(t) mod M` 为平方剩余的 residue classes，中位 survivor fraction 为 `0.0285714`，即中位可排除约 `97.1429%` 的昂贵平方测试。这是非常有效的常数因子优化，但它是标准 Fermat 模筛，不是新的平方壳分解规律；每个 `t` 仍需廉价模测试或等价周期跳转。

---

## 2. 精确结构 II：宏观中点距离来自因子比，壳只给 subunit correction

置

`lambda=q/p >= 1`, `h=(1/2) log(lambda)`。

因 `sqrt(N)=p*sqrt(lambda)`，有

`A=(p+q)/2 = sqrt(N) * (sqrt(lambda)+1/sqrt(lambda))/2 = sqrt(N) cosh(h)`。

再记

`delta=A0-sqrt(N)`。

由于 `b=A0^2-N`，

`delta = b/(A0+sqrt(N))`, 且 `0<delta<1`。

因此精确得到

`T = sqrt(N)(cosh(h)-1) - delta`。

等价地，

`A-sqrt(N) = (sqrt(q)-sqrt(p))^2/2`。

这给出了本任务最重要的结构解释：

- `b` 精确控制的是 `delta`，即平方根向上取整产生的 **不到一个单位** 的离散修正；
- 当 `q/p` 离开 1 后，`sqrt(N)(cosh(h)-1)` 可以增长到 `Theta(sqrt(N))` 甚至更大尺度的 midpoint displacement；
- 因而不能期待单个局部壳相位在普适意义上编码因子不平衡。

这不是信息论意义上的“`N` 不含因子信息”：承诺 `N` 为 semiprime 时，唯一分解当然由 `N` 决定。这里的结论是：`(s,b)` / `(L,D)` 是 `N` 的可逆重参数化，本身没有提供一个已证明更便宜的搜索判据。

---

## 3. 全量小整数普查

范围：全部

`N=pq <= 10^7`, `3<=p<q`, `p,q prime`。

总数：`1,555,366`。

所有样本均通过：

- `a+b=L`；
- `4N-1=L^2-2D`；
- `B^2=b+2*A0*T+T^2`；
- 稀疏抽样的 multi-k 输运恒等式。

任务专用 checker：

`research_checks/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_CHECK_20260829.py`

本次执行结果：`PASS`，`bridge_identity_failures=0`，`shell_identity_failures=0`，`multik_transport_failures=0`。

### 3.1 单壳位置的总体相关

令 `u=b/(2s+1)`。

| 量 | Pearson correlation |
|---|---:|
| `u` vs `log(1+T)` | `0.0073965` |
| `u` vs `T/A0` | `-0.00021884` |
| `u` vs `log(q/p)` | `0.0026842` |
| `u` vs `log(1+J_p)` | `0.0175963` |

宏观上没有可用的单壳 factor-imbalance signal。

局部两侧素数 gap 与 `log(1+J_p)` 的未分层相关达到 `0.11394`，是本轮最强的表面相关之一；但按 `N` 大小分层后显著衰减并改变方向：例如在 `1e5..1e6`、`1e6..3e6`、`3e6..6e6`、`6e6..1e7` 区间，相关约为 `0.0600, 0.0168, -0.0091, 0.0147`。这是典型 size/density confounding，而不是稳定 rank 规则。

### 3.2 独立 holdout 预测

Discovery/training：`1e6 <= N < 8e6`，固定随机抽样 `300,000`。  
Holdout：`8e6 <= N <= 1e7`，固定随机抽样 `120,000`。

目标：`log(1+T)`。

Baseline 只使用 `log N`；shell-rich 输入加入：

- `u=b/(2s+1)`；
- `s-PrevPrime(s)`、`NextPrime(s)-s`、两侧 gap；
- `k=2..16` 的 normalized upper-shell residual phase。

同一 `HistGradientBoostingRegressor` 配置下：

| model | holdout R^2 | MAE |
|---|---:|---:|
| `log N` baseline | `-0.0007864` | `2.21878` |
| shell-rich | `-0.0015426` | `2.22749` |

壳特征没有形成可迁移预测，反而轻微恶化。

---

## 4. 成体系反例：壳几乎相同，因子结构可以完全不同

### Counterexample family A — 同一个 shell index、相同局部 prime neighborhood

`N1=9,917,459 = 3079*3221`

- `s=3149`
- `b=5041`
- `PrevPrime(s)=3137`, `NextPrime(s)=3163`
- `T=0`
- `q/p≈1.04612`

而仅相差 2 的

`N2=9,917,461 = 1009*9829`

- `s=3149`
- `b=5039`
- 相同 `PrevPrime/NextPrime = 3137/3163`
- `T=2269`
- `q/p≈9.74133`

即：相同整数平方壳、完全相同的 `sqrt(N)` 局部素数环境，`b` 只差 2，但真实 midpoint displacement 从 `0` 变为 `2269`。

### Counterexample family B — 极端放大

`N1=9,990,157 = 3119*3203`：`s=3160`, `b=1764`, `T=0`, `q/p≈1.02693`。

`N2=9,990,159 = 3*3,330,053`：`s=3160`, `b=1762`, `T=1,661,867`, `q/p≈1,110,017.67`。

二者仍拥有同一 `s` 和同一局部 prime neighborhood；壳 residual 只差 2。

### Counterexample family C — exact same `b`

`5,157,223 = 2203*2341` 与 `9,979,063 = 1013*9851` 都有 `b=218`，但 `T` 分别为 `1` 与 `2273`，因子比约 `1.063` 与 `9.725`。

这三组反例并不证明任何复杂度下界；它们精确反驳的是“局部平方边界残差/邻近素数环境本身近似决定 midpoint 或 factor ratio”的候选规律。

---

## 5. 邻近素数与 prime-rank 路线

定义

`J_p=pi(s)-pi(p)`。

如果从不超过 `s` 的最大素数开始向下枚举素数并做整除测试，则找到 `p` 之前恰需测试 `J_p+1` 个 prime candidates。因此这个操作是 **descending prime trial division**；它不是由壳坐标推导出来的新 factorization primitive。

在 `N>=10^6` 的 census 中，按隐藏因子比仅用于诊断分层：

| `q/p` | median prime candidates `J_p+1` | median Fermat candidates `T+1` |
|---|---:|---:|
| `[1,1.01)` | 1 | 1 |
| `[1.01,1.05)` | 4 | 1 |
| `[1.05,1.1)` | 10 | 2 |
| `[1.1,1.25)` | 22 | 7 |
| `[1.25,1.5)` | 42 | 27 |
| `[1.5,2)` | 70 | 81 |
| `[2,4)` | 117 | 290 |
| `[4,10)` | 181 | 970 |
| `[10,100)` | 255 | 4038 |
| `[100,inf)` | 336 | 173883 |

这解释了一个容易误判为“邻近素数捷径”的现象：因子非常不平衡时，从 `sqrt(N)` 向下按素数枚举的候选数量可以明显少于 Fermat midpoint 步数；但这只是两个经典基线在不同 factor-ratio 区域的性能交叉，并没有使用平方壳预测 `J_p`。

邻近素数特征本身也不是免费输入。对 24/32/40/48/64-bit 分层样本，`sqrt(N)` 两侧最近素数总 gap 的中位数约为 `12/14/20/24/32`，95% 分位约 `28/36/50/66/90`；部署时仍需相应 primality testing / prime-generation 成本。更重要的是，这只能得到局部 gap，不能得到隐藏下端点 `p`，所以不能直接给出 `J_p`。

---

## 6. multi-k：精确落入 multiplier-Fermat / Lehman / Hart

对每个 `k>=1`，令

`x_k=ceil(sqrt(4kN))`,

`e_k=x_k^2-4kN`。

若 `e_k=y^2`，则

`x_k^2-y^2=4kN`，

并可通过 `gcd(x_k-y,N)` 或 `gcd(x_k+y,N)` 检查是否得到非平凡因子。

若首点不成功，再令 `x=x_k+j` 向上扫描，本质上就是对 `4kN` 做 multiplier Fermat。

任务的跨壳 identity

`D_k = kD + (L_k^2-kL^2+1-k)/2`

是正确且可复核的，但它只是 `N,k,floor(sqrt(kN))` 的精确输运；没有新增一个 factor selector。

### 与已知路线的边界

- R. Sherman Lehman, *Factoring Large Integers*, Mathematics of Computation 28 (1974), 637–646, DOI `10.1090/S0025-5718-1974-0340163-2`：系统搜索乘子并在 `sqrt(4kN)` 附近寻找平方差，给出经典 `O(N^(1/3))` elementary-operation 路线。
- William B. Hart, *A One Line Factoring Algorithm*, Journal of the Australian Mathematical Society 92 (2012), 61–69, DOI `10.1017/S1446788712000146`：直接以乘子后的近平方残差为核心做 Fermat 变体。

因此把 `kN/4kN` 上方平方 residual 解释为“多壳信号”在坐标上可以很新颖，但算法对象与 multiplier-Fermat family 相同。任何新优势必须来自 **新的 k 排序/跳过定理或更低成本 residual transport**，而不能来自 residual 本身的重新命名。

### 6.1 原始 multi-k 相位无稳定预测

在小整数 census 的固定 `300,000` 样本上，对 `k=1..32`：

- `u_k` 与 `log(1+T)` 的最大绝对相关 `<0.01`（观测最大约 `0.00951`）；
- 与 `log(1+J_p)` 的最大绝对相关约 `0.01876`。

另做 24/32/40/48/64-bit、每 bit 1000 个、每 factor-bit split 250 个的分层半素数样本。20 个 strata 中，针对 `k=1..32` 事后取最大绝对相关可到约 `0.195`，但最大值对应的 `k` 与符号在 strata 间不断改变，未形成可冻结的跨尺度方向；单 `k=1` 相关同样正负混杂。

---

## 7. 一个保留下来的窄残余：小 residual multiplier priority

对 `k<=64` 定义 factor-blind score

`score(k)=e_k/(2*x_k-1)`，

即 `4kN` 到上方平方边界的 normalized residual。

如果只看那些在 `k<=64` 内本来就存在 `e_k=y^2` 且 gcd productive 的样本，则按 `score` 从小到大测试，会在小范围内显著提前遇到成功 k：

- 全部 `N<=10^6`：168,330 个半素数中 29.57% 在 `k<=64` 有立即 productive hit；条件样本的 median `k`-order rank 为 18，score-rank 为 5。
- discovery `1e6..8e6` 的 50,000 随机样本：hit rate `19.81%`，条件 median rank `27 -> 12`。
- holdout `8e6..1e7` 的 50,000 随机样本：hit rate `16.33%`，条件 median rank `30 -> 14`。

但跨 bit 后 coverage 快速崩溃：

| bit size | `k<=64` immediate productive hit rate |
|---|---:|
| 24 | 43.3% |
| 32 | 8.8% |
| 40 | 2.2% |
| 48 | 0.6% |
| 64 | 0% |

而且该排序要先为所有候选计算 `x_k/e_k`，若全排序还增加 `O(K log K)` 排序成本；没有证据表明它减少总 `k` 生成成本或得到渐近改进。它目前只能记为：

`FINITE_WINDOW_RESIDUAL_PRIORITY_HEURISTIC / NOT_A_FACTORIZATION_RESULT`

不能把条件命中排序的改善与整体成功率混淆。

---

## 8. 成本核算

### Fermat / single shell

- midpoint candidates：`T+1`；
- naive square tests：至多 `T+1`；
- QR sieve：每 candidate 至少一次/若干次廉价 residue evaluation，可把昂贵 square tests 减到一个常数比例；本次 `M=6720` 示例中位约 2.86%；
- gcd：成功平方出现后常数次；
- shell `(s,b,L,D)` 计算本身只需 integer sqrt + O(1) arithmetic，不改变搜索长度。

### neighbor-prime scan

- prime candidates：`J_p+1`；
- divisibility tests：`J_p+1`；
- 计算局部 `PrevPrime/NextPrime` 还需额外 primality/prime-generation 工作；
- 若想直接知道 `J_p`，必须知道 `p`，因此 `J_p` 只能当标签，不可计为免费部署特征。

### multiplier shell

对 `K` 个 multipliers：

- 至少 `K` 个 `ceil(sqrt(kN))` 或等价递推状态更新；
- naive 至多 `K` 个 residual square tests；
- productive square 时再做 gcd；
- residual priority 若预先完整排序，额外 `K` 个 score + `O(K log K)` 排序；若做 streaming top-m，仍必须把生成/维护成本完整计入。

因此任何后续正结果必须比较 **总操作数和 wall-clock**，不能只比较“第几个平方测试命中”。

---

## 9. Tool reuse gate

按 `enterprise_toolbox_registry.json` 做了当前工具覆盖查询。Registry 中 `T1 Enterprise Scale Enumeration / Valuation Calculus` 的 trigger 含 `shell`，但其能力是企业尺度枚举/有限差分/valuation shell extraction；本任务的核心对象是整数平方边界、Fermat residual 与 multiplier factorization。没有找到可直接替代本任务 exact-integer census / factorization baseline audit 的已接受通用工具。

分类：`NOT_APPLICABLE_FOR_FACTORIZATION_CORE`。

因此只提交 task-specific checker，不主张新工具家族。

---

## 10. 可复核 no-go 的精确边界

本任务现在支持以下窄 no-go：

> 在所测试的特征族——单相邻平方壳 `(s,a,b,L,D,r)` 的局部/归一化位置、`sqrt(N)` 附近的最近素数距离与局部 gap、以及有限 `k` 的原始平方壳相位——中，没有发现能在独立尺度 holdout 上稳定预测 `T`、因子比或 `J_p` 并形成低于 Fermat / trial division / multiplier-Fermat 基线总成本的 factor-blind 规则。

并且：

- single-shell midpoint 扫描被精确归约为 Fermat；
- modular restrictions 被精确归约为 Fermat residue sieve；
- neighbor-prime rank scan 被精确归约为 prime trial division order；
- raw multi-k near-square residual 被精确归约为 multiplier-Fermat / Lehman / Hart family。

未证明：一般整数分解复杂度下界、所有 shell-derived nonlinear 特征的 no-go、所有可能的 multiplier 排序 no-go。

---

## 11. 最小未关闭问题

只保留一个足够窄且可证伪的后续问题：

`RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT`

问题：令 `K(N)` 随规模增长到 Lehman/Hart 有意义的范围（首先 `K≈N^(1/3)` 的受控截断），能否不完整排序全部 k，而用可流式维护的 upper-square residual threshold / bucket，在 **完整计入 kN sqrt/transport、mod sieve、residual square test、gcd、queue/bucket 成本** 后，比 sequential Hart/Lehman baseline 稳定减少总成本？

Kill condition：

- 只减少条件命中 rank，但总 `k` 生成/平方根成本不降；或
- coverage 继续随 bit size 坍塌；或
- 最终等价于已有 Hart multiplier order + standard modular sieve；

则关闭该残余。

当前不建议继续在“单壳 midpoint 与邻近素数的静态相关”上扩大数据量；精确等价式与反例已经说明那条路线的主要瓶颈不是样本不足。

---

## 12. 产物

- `research_returns/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_RETURN_20260829.md`
- `research_checks/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_CHECK_20260829.py`
- `research_artifacts/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY/experiment_summary_20260829.json`

No Working Truth or canonical-promotion claim is made by this return.
