# 平方壳—乘法壳因子盲桥：研究回报

Task: `RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE`  
Publication: `TP2-A712090E5314373E5447`  
Researcher-ID: `EM-SMSB1-4A7E2C`  
Claim: `chatgpt-smsb1-20260829-1645-4a7e2c`  
Branch: `research/factor-blind-square-multiplicative-shell-bridge-em-smsb1-4a7e2c`

Terminal verdict:

`NEGATIVE_BOUNDARY`

Hard-target disposition:

`BCT_TPGR_NEW_CONDITIONAL_FAMILY_FAILS_INCREMENTAL_PREDICTIVE_BRIDGE / NO_S1 / NO_S2 / NO_S3`

本回报关闭的是一个**明确新增、预提交、factor-blind 的跨壳条件族**，不是一般分解复杂度下界，也不声称所有 `N`-only 非线性表示都不可能有算法收益。

---

## 1. 结论先行

本任务继承两个已冻结边界：

1. `RR-2A424E3B8EC11DC1278C`：单平方壳、局部 `sqrt(N)` 素数邻域、raw finite-multi-k residual family 没有得到可迁移的 total-cost 分解收益；
2. `RR-C28C28A7C8EF8B9C96F6`：固定 `Omega=2` 的 M2 replacement-shell geometry 与 semiprime Hamilton–Gray ray 是精确结构，但没有 factor-blind M2 localization rule。

本轮没有把旧 residual 换名重跑，而是冻结了两个新的 factor-blind 条件机制：

- **BCT — Beatty Carry Topology**：观察从 `s^2` 移动到 `N` 后，在 `kN` 跨尺度平方边界产生的整数 carry word；
- **TPGR — Transported Prime-Gap Resonance**：观察多个预提交 `sqrt(kN)` 附近的前后素数距离与局部 prime gap。

主候选 `BCT+TPGR` 在 24/32/40-bit、四种 factor-ratio strata、独立 held-out 上：

- 对小因子 prime-rank bucket：99% 与 99.9% recall 均需要**全部 24 个 corpus-support buckets**，support compression = `1.0`；
- 对真正的 multiplicative-shell `q` prime-token block：99% recall 需要 top-10/15，而 size-only baseline 只需 top-5/15；
- 对 frozen semiprime Hamilton–Gray rank block：99% recall 需要 top-11/16，而 size-only 只需 top-5/16；
- 对 Fermat midpoint offset bucket：99% recall 需要 17/18，99.9% 必须 18/18。

因此不存在满足任务定义的 **S1 predictive bridge**。既然用于实际试除的 `p`-rank candidate set 在高 recall 下没有缩小，而 BCT+TPGR 本身还要支付大量 integer-sqrt、prime-neighbor 与模型推理成本，所以也不存在 **S2 search bridge**；更不存在 **S3 competitive factorization gain**。

---

## 2. 信息守恒与精确基准

令非平方奇半素数

\[
N=pq,\qquad s=\lfloor\sqrt N\rfloor,\qquad
a=N-s^2,\qquad b=(s+1)^2-N,
\]

\[
L=2s+1,\qquad D=b-a.
\]

复核：

\[
4N-1=L^2-2D,
\qquad
N=\frac{L^2+1-2D}{4}.
\]

所以 `(L,D) <-> N` 是可逆重参数化。

对任意有限、预提交 multiplier 集，所有 `isqrt(kN)`、square-shell residual、carry、局部同余与由这些量确定的有限 signature 都是 `N` 的确定函数。正结果如果存在，只能是计算表示/归纳偏置/搜索顺序收益，不能解释成“产生新的因子信息”。

本轮所有 worker feature 函数的唯一秘密无关输入是 `N` 与 public constants；`p,q,T,factor-ratio,prime-index,M2/Gray truth` 只存在于 verifier 评估侧。

---

## 3. 新机制 A：BCT 的精确定义与降维定理

写

\[
N=s^2+r,\qquad 1\le r\le 2s.
\]

对固定 `k>=2` 定义

\[
c_k(N)
=
\left\lfloor\sqrt{kN}\right\rfloor
-
\left\lfloor\sqrt{k s^2}\right\rfloor.
\]

冻结

\[
K_{\rm carry}=\{2,3,\ldots,64\}.
\]

worker 使用：

- 全部 `c_k`；
- 一阶差 `c_k-c_{k-1}`；
- 六个预先固定的 carry mass/run/parity summaries。

这不是旧任务测试的 raw near-square residual magnitude 或 residual-priority 排序；候选机制是**跨尺度 floor/carry event topology**。

### BCT step-function theorem

令

\[
u_k=\lfloor s\sqrt{k}\rfloor.
\]

则

\[
c_k=t
\iff
(u_k+t)^2\le k(s^2+r)<(u_k+t+1)^2.
\]

因此对固定 `s,k`，`c_k` 是 `r` 的单调阶梯函数。

又因为

\[
s\sqrt{k}
\le \sqrt{kN}
< (s+1)\sqrt{k},
\]

所以 `c_k` 的跳变数不超过

\[
\lceil\sqrt{k}\rceil.
\]

于是 `k=2..64` 的完整 carry word 在一个平方壳中至多切成

\[
1+\sum_{k=2}^{64}\lceil\sqrt{k}\rceil
=
1+371
=
372
\]

个 cell。

这给出本轮一个重要精确边界：

> 有限 BCT 并没有制造新的高维隐藏坐标；在固定 square shell 内，它只是对单一 shell phase `r` 的有限单调量化。

在 checker 的 `s=3160` 完整 shell 枚举中，实际只出现 `271` 个 BCT cells，满足上述上界。

---

## 4. 新机制 B：TPGR

冻结

\[
K_{\rm prime}=
\{1,2,3,5,7,11,13,17,19,23\}.
\]

令

\[
x_k=\lfloor\sqrt{kN}\rfloor.
\]

对每个 `x_k` 仅观察：

- `x_k - PrevPrime(x_k)`；
- `NextPrime(x_k) - x_k`；
- `NextPrime(x_k)-PrevPrime(x_k)`。

这是严格 factor-blind 的 transported prime environment。它和旧结果只观察 `sqrt(N)` 附近 prime gap 不同；本轮测试的是**多尺度 `sqrt(kN)` prime-gap resonance**。

成本必须计费：最多 10 个 transported roots、20 个 prime-neighbor 查询；和 BCT 合并时可复用部分 `isqrt(kN)`。

针对先验的定向检索仍表明：`kN` 的 near-square/multiplier 主结构属于 Lehman/Hart 及其后续 multiplier/continued-fraction 路线。TPGR 本轮不提出新颖性主张，只作为一个新的、可证 factor-blind 的候选 feature family 接受盲测。

---

## 5. 双舱 corpus 与泄漏审计

Authoring corpus：

- distinct odd semiprimes：`4,775`；
- train：`2,864`；
- tuning：`954`；
- held-out：`957`；
- bit bands：
  - `B24=[2^23,2^24)`；
  - `B32=[2^31,2^32)`；
  - `B40=[2^39,2^40)`；
- verifier-only factor-ratio strata：
  - near-twin `[1,1.05)`；
  - balanced `[1.05,1.5)`；
  - moderate `[1.5,5)`；
  - strong `[5,20)`。

本轮资源只冻结实际运行过的 24/32/40-bit；**没有**把未运行的 48/64-bit 写成证据。

切分在每个 `(bit-band, ratio-stratum)` 内按 `SHA256(public seed || N)` 排序后做 60/20/20；held-out label 不参与模型训练、feature 选择或 top-k 校准。

Pinned digests：

- public `N` state:
  `sha256:1c02964c1297ef8d498669688e5dd99ef206504602b482bd4a54e8dd2fd79a90`
- private verifier state:
  `sha256:b4550b90bd2f2781a822e04614e076bd180169e3af8b3dacf5756b7091681e28`

公开 manifest 不序列化 `p,q`。

---

## 6. Hidden targets 与 matched baseline

至少测试四类 target，其中两类直接来自 multiplicative-shell/Gray geometry：

1. `p_rank_bucket`：小因子在 `sqrt(N)` 以下的 prime-index 相对 bucket；
2. `m2_q_block`：较大 prime token `q` 的全局 log prime-index block，是真正的 M2 max-prime-token block；
3. `gray_rank_bucket`：使用已冻结 semiprime Hamilton–Gray ray 精确 rank 后再分桶；
4. `fermat_T_bucket`：Fermat midpoint offset

\[
T=\frac{p+q}{2}-\lceil\sqrt N\rceil.
\]

matched baseline `SIZE` 只使用：

- `log2(N)`；
- `frac(log2(N))`。

主候选 `BCT_TPGR` 使用 size control + square-shell phase control + BCT + TPGR。

分类器固定为 `ExtraTreesClassifier`：

- `n_estimators=160`；
- `min_samples_leaf=5`；
- `max_features=sqrt`；
- 固定 random seed family；
- tuning 只用于 top-k 高 recall 校准。

---

## 7. Held-out 主结果

下面 compression 以**训练集实际出现的 target bucket support**为分母；这避免把 corpus 中根本不可能出现的空 bucket 当成“算法压缩”。

### 99% recall，tuning-calibrated top-k

| hidden target | SIZE baseline | held recall | BCT+TPGR | held recall | 增量结论 |
|---|---:|---:|---:|---:|---|
| `p_rank_bucket` | 24/24, compression 1.00 | 100% | 24/24, compression 1.00 | 100% | 无压缩 |
| `m2_q_block` | top-5/15, compression 3.00 | 99.5820% | top-10/15, compression 1.50 | 99.0596% | **明显更差** |
| `gray_rank_bucket` | top-5/16, compression 3.20 | 99.8955% | top-11/16, compression 1.4545 | 99.5820% | **明显更差** |
| `fermat_T_bucket` | top-17/18, compression 1.0588 | 99.6865% | top-17/18, compression 1.0588 | 99.7910% | 无实质压缩 |

### 99.9% recall

- `p_rank_bucket`：两者都要 24/24；
- `m2_q_block`：
  - SIZE：12/15；
  - BCT+TPGR：15/15；
- `gray_rank_bucket`：
  - SIZE：11/16；
  - BCT+TPGR：16/16；
- `T_bucket`：两者都要 18/18。

因此 BCT+TPGR 不只是“没有显著赢”，而是在真正的 M2/Gray hidden target 上需要**更大的 candidate set**。

---

## 8. 分层失效：strong-unbalanced 是关键反例区

`m2_q_block` 在 held-out strong-unbalanced 240 例上：

- SIZE，top-5：recall `98.75%`；
- BCT+TPGR，top-10：recall `96.25%`。

也就是说，新候选已经使用 baseline 两倍的 bucket 数，却在最需要 localization 的失衡区域表现更差。

按 bit band：

- B24：top-10 recall `99.6845%`；
- B32：`98.4375%`；
- B40：`99.0625%`。

未出现跨尺度增强。

Gray target 同样没有增量优势；`p`-rank 在 moderate/strong strata 的 top-1 近乎失效，高 recall 只能回退到全 support。

---

## 9. 精确 adversarial collision

找到一个特别强的 collision：

\[
N_1=9,990,157=3119\cdot 3203,
\]

\[
N_2=9,990,159=3\cdot 3,330,053.
\]

二者满足：

- `floor(sqrt(N_1))=floor(sqrt(N_2))=3160`；
- 对**全部 `k=2..64`**：
  `BCT(N_1)=BCT(N_2)`；
- 对
  `k in {1,2,3,5,7,11,13,17,19,23}`：
  `floor(sqrt(kN_1))=floor(sqrt(kN_2))`；
- 因此所有 TPGR 前后素数距离与 local gaps 也完全相同。

但 verifier hidden layout 极远：

- 第一例小因子几乎贴近 `sqrt(N)`；
- 第二例小因子为最小奇素数；
- Fermat offset 分别为

\[
T_1=0,\qquad T_2=1,661,867.
\]

在本轮 32-bucket verifier 中，两者：

- `p_rank_bucket`: `31` vs `0`；
- `m2_q_block`: `15` vs `31`；
- `gray_rank_bucket`: `14` vs `31`；
- `T_bucket`: `0` vs `29`。

这不是一般复杂度下界，但它**精确否定**了“有限 BCT+当前 TPGR signature 可以点定位隐藏乘法壳”的主张，并解释 strong-unbalanced 层为何是系统性失败点。

---

## 10. 从预测接到 exact factor search

预注册 search wrapper：

\[
N
\to
\text{factor-blind features}
\to
\text{predicted }p\text{-rank buckets}
\to
\text{prime divisibility tests}
\to
\text{exact nontrivial divisor certificate}.
\]

这一步没有隐藏 gcd/factor feature。

但在 99% 与 99.9% recall，BCT+TPGR 都需要全部 `24/24` corpus-support `p`-rank buckets。

因此：

\[
\boxed{\text{candidate-set reduction}=0}
\]

相对于由公开 corpus ratio support 已经允许的 matched trial-division domain，不存在搜索空间缩减。

与此同时 BCT+TPGR 的 preprocessing 上界包括：

- `s` 与 `k=2..64` 的 exact square-root/carry 计算，最多约 127 次 integer-sqrt；
- 20 次 transported prime-neighbor lookups；
- 160-tree inference。

所以即使忽略模型推理本身，它也不可能在本实验中升级为 S2。

---

## 11. 为什么 M2/Gray 的“好成绩”不能算 bridge

size-only baseline 对 `m2_q_block`/`gray_rank_bucket` 已有较高 compression，是因为：

- bit length 强烈限制 `q` 的绝对 prime-index 尺度；
- Gray rank 主量级由最大 prime index `j` 决定；
- 这是 size/base-rate geometry，不是 square-shell 新增 localization。

任务定义要求 shell-derived feature **显著优于 size/base-rate baseline** 才能记为 S1。

实际 BCT+TPGR 在这些 target 上反而把 top-k 从 `5` 扩大到 `10/11`。

因此必须分类为：

`BASELINE_GEOMETRY_ONLY / NO_INCREMENTAL_SHELL_BRIDGE`.

---

## 12. 冻结边界

本轮新增并关闭的 feature family：

1. `BCT[2..64]`：
   finite cross-scale carry word + first differences + fixed summaries；
2. `TPGR[1,2,3,5,7,11,13,17,19,23]`：
   transported-root two-sided local prime-gap signature；
3. 二者与 size/shell-phase control 的 supervised candidate-ranking combination。

冻结结论：

> 在本轮 24/32/40-bit、near-twin/balanced/moderate/strong、train/tune/held-out 双舱协议中，该 family 对 prime-rank、M2 max-prime-token block、Hamilton–Gray rank block、Fermat midpoint offset 均没有产生相对 size/base-rate 的稳定高-recall candidate compression；其中 M2/Gray target 明显退化。它不能支撑 S1，更不能支撑 S2/S3。

不得把以下现象重新包装为 successor：

- BCT 的不同 summary / tree model / bucket 数微调；
- 在同一个 `sqrt(kN)` 集合上增加更多 raw local gap 列；
- 只报告 balanced/near-twin 的 top-1 改善；
- 用 test labels 选择 `k`、feature 子集或 threshold；
- 把 size-only 已有的 M2/Gray bucket compression 写成 square-shell bridge。

---

## 13. 尚未封闭的最小 residue

本任务不证明所有 factor-blind localization 都不可能。

若另开 successor，必须至少满足：

1. feature 机制不只是固定有限 shell-phase quantization；
2. 不只是 `sqrt(kN)` 附近有限 local prime environment 的扩表；
3. 在规则冻结前说明它为何可能约束**两个隐藏 prime tokens 的关系**，而不仅是 `N` 的绝对大小；
4. 预先指定 matched high-recall search comparator 与 preprocessing/queue/primality/gcd 成本；
5. 先过 strong-unbalanced adversarial gate，再看整体均值。

优先级不高于当前已冻结的 residual-priority/Hart cost audit；没有新的 factorization claim。

---

## 14. 可复核输出

- `research_returns/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE_RETURN_20260829.md`
- `research_artifacts/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE/public_manifest.json`
- `research_artifacts/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE/result_summary.json`
- `research_checks/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE_CHECK_20260829.py`

独立 checker 复核：

- `(L,D)<->N` 精确恒等式；
- BCT 单调 step-function 与 `372`-cell 上界；
- `s=3160` shell 实际 BCT cell count `271`；
- adversarial pair 的 primality / factorization；
- 全 `k=2..64` BCT collision；
- 全 TPGR transported-root / prime-gap collision；
- verifier hidden-label separation digest；
- 终态不得升级到 S1/S2/S3。

Observed local checker result:

`PASS`.

---

## 15. 最终分类

\[
\boxed{\texttt{NEGATIVE\_BOUNDARY}}
\]

更具体：

`FINITE_BCT_PLUS_TRANSPORTED_PRIME_GAP_FEATURE_FAMILY_CLOSED_AS_NONINCREMENTAL`

没有 Working Truth 请求。  
没有 Foundation mutation。  
没有 canonical promotion。  
没有 factorization gain 声明。  
等待 Driver review。
