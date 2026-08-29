# 平方壳—乘法壳因子盲桥：半素数局部坐标预测与分解收益盲测 — Research Return

Task: `RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE`  
Publication: `TP2-A712090E5314373E5447`  
Researcher-ID: `EM-SMSB1-73D4C2`  
Claim: `chatgpt-smsb1-20260829-1645-73d4c2`  
Execution record: `ER-4F1EC87814863CFA854B`

## Terminal verdict

`NEGATIVE_BOUNDARY / NO_S1 / NO_S2 / NO_S3`

本任务没有证明“一切由 N 派生的 factor-blind 观测都不可能帮助分解”。冻结的是两个更窄、但可复核且足以排除当前路线的边界：

1. **精确 no-go：** 任意固定有限同余模数组成、对 Fermat offset `t` 呈固定周期的合法筛，只能给出周期性的常数倍删减；它不能把真实 offset 前的候选数压到 `o(T)`。
2. **经验 no-go：** 本任务预提交的 `SHELL_RESIDUE_QR_CONDITIONAL_V1`（平方壳 + 小模同余 + 局部二次剩余统计）在 IID held-out 上有明显表面信号，但在独立对抗 challenge、跨位宽和 factor-ratio 分层后，高召回定位崩溃；99%/99.9% recall 基本需要保留全部 target buckets。把预测接到精确 prime-scan wrapper 后，near-twin 的漂亮结果不能升级为 S2，因为匹配的 Fermat comparator 在该层更强，而 moderate/strong strata 会出现严重甚至灾难性的反向优先级。

因此：**未建立 factor-blind 的 multiplicative-shell localization bridge，更未建立 factorization gain。**

---

## 1. 信息守恒边界复核

对非平方 `N`，令

\[
s=\lfloor\sqrt N\rfloor,\quad a=N-s^2,\quad c=s+1,\quad b=c^2-N,
\]

\[
L=2s+1,\qquad D=b-a.
\]

则

\[
4N-1=L^2-2D,
\qquad
N=\frac{L^2+1-2D}{4}.
\]

所以 `(L,D) <-> N` 是精确可逆重参数化。任意预先固定的有限 multi-k signature、carry/correction、固定模剩余及本任务所有 public features 都是 `N` 的确定函数。

这不禁止算法表示收益，但禁止把 positive correlation 表述成“新增了隐藏因子信息”。若某方法只是把 `N` 解码后执行既有算法，则只计为 reparameterization。

---

## 2. 平方壳到乘法坐标的精确桥其实就是 Fermat conic

令

\[
N=pq,\qquad 3\le p\le q,
\]

并定义

\[
c=\lceil\sqrt N\rceil,\qquad b=c^2-N,
\]

\[
A=\frac{p+q}{2},\qquad B=\frac{q-p}{2},\qquad T=A-c.
\]

由 `N=A^2-B^2` 得

\[
\boxed{B^2=b+T(2c+T)}.
\]

对任意候选 offset `t` 定义

\[
z_N(t)=b+t(2c+t)=(c+t)^2-N.
\]

则真实 `T` 满足

\[
z_N(T)=B^2,
\]

且

\[
\boxed{p=c+T-B,\qquad q=c+T+B}.
\]

这给出了一个非常干净的“平方壳 -> 隐藏乘法坐标”方程，但它没有创造新 oracle：**寻找隐藏坐标 T 等价于寻找第一个使 `z_N(t)` 成平方的 Fermat offset。**

因此，后续任何只对 `z_N(t)` 做 factor-blind 条件筛选的收益，都必须与相同成本口径下的 Fermat / residue-wheel baseline 比较，而不能把这个恒等式本身算作分解突破。

---

## 3. Fixed finite periodic residue filter no-go

### Theorem

固定有限模数 `m_1,...,m_k`，令

\[
M=\operatorname{lcm}(m_1,\ldots,m_k).
\]

考虑任一合法 factor-blind offset filter `F_N(t)`，若它的判定只依赖预先固定的 N-derived 参数及 `t mod m_i`，则对固定 `N`：

\[
F_N(t+M)=F_N(t).
\]

若 filter 具有 100% true-offset recall，即 `F_N(T)=1`，那么对每个满足 `0<=T-\ell M<=T` 的整数 `\ell` 都有

\[
F_N(T-\ell M)=1.
\]

所以从 `0` 搜到真实 offset `T` 时至少保留

\[
\boxed{\left\lfloor\frac{T}{M}\right\rfloor+1}
\]

个候选。

### Consequence

对固定 `M`：

\[
\#\text{candidates through }T=\Omega(T).
\]

因此 fixed finite residue filter **不可能**给出 `o(T)` 的候选数，只能提供常数倍/周期性 sieve compression。

若让 `M=M(N)` 随规模增长，则模表、预处理、内存与构造成本必须进入总成本；上面的定理本身不再授权任何无条件 gain claim。

### Exact QR specialization

取平方剩余筛 mod

`[8, 9, 5, 7, 11]`,

则

\[
M=27720.
\]

真实 `T` 必过筛，因为 `z_N(T)=B^2`。20 个跨 bit-band / ratio representative 的一个周期内 survivor density 落在约

`0.004329 ... 0.020779`,

对应的有限常数倍压缩约 `48.125x ... 231x`。

但在一个 64-bit moderate representative 上：

- `T = 2,585,365,521,648`
- survivors through true `T = 22,384,117,071`
- compression `~115.5x`

在一个 64-bit strong-unbalanced representative 上：

- `T = 13,586,347,362,351,934`
- survivors through true `T = 282,313,711,425,494`
- compression `~48.125x`

数值上压缩可观，但候选数仍随 `T` 线性增长，不能作为 hidden multiplicative coordinate localization theorem。

---

## 4. Frozen feature-to-label contract

### Worker-visible feature family: `SHELL_RESIDUE_QR_CONDITIONAL_V1`

只使用公开 `N` 与预提交常数：

1. size：`bit_length(N)`、二进制 mantissa；
2. shell：`a/L, D/L, b/L`；
3. fixed small residues：对 `m in [3,5,7,11,13,17,19,23,29,31]` 使用 `(N mod m)/m` 与 `(c mod m)/m`；
4. local QR window：对 `t=0..63`、模数 `[8,9,5,7,11,13]` 只输出聚合统计：全通过比例、首个通过位置、通过模比例均值/标准差/最大值。

没有任何 `p,q,T,B,factor-ratio,prime-index,M2/Gray truth,gcd-with-hidden-target` 进入 worker features。

### Verifier-only hidden targets

固定 10 buckets：

- `p_bucket`: `p/c` interval；因 prime order 单调，它对应 prime-index interval target；
- `q_bucket`: `q/c` interval；`q` 是半素数 M2 block 的最大 prime-token index carrier，因此这是一个真正的 multiplicative-shell neighborhood target；
- `t_bucket`: `T/c` Fermat midpoint-offset interval。

输出形式是 calibrated bucket ranking；高召回时考察最小 top-k candidate-set size。

---

## 5. Corpus、split 与 leakage control

公开 manifest 共 1,400 个 `N`，不序列化因子：

- primary 800：24/32/40/48/64-bit，每 band 160；
  - train 510
  - tune 137
  - IID held-out 153
- adversarial challenge 600：每 band 120；全部只作最终 held-out。

primary split 由公开 hash rule 决定：

`sha256('SMSB1|20260829|'+N)[:8] mod 10`。

challenge 在生成时把 `N/2^(bit_length-1)` 强制压入 `[1.25,1.75]`，目的是减少通过绝对数值大小识别生成 stratum 的捷径；challenge 从未参与训练、阈值选择或超参数选择。

独立 checker 只读取公开 `N`，在 verifier 内临时用 deterministic 64-bit Miller-Rabin + Pollard-Brent 重建隐藏因子标签；因子不写入 manifest、summary 或 checker 输出。

---

## 6. Hidden-coordinate prediction: IID 表面成功，challenge 高召回失败

Authoring model 为固定超参数 Random Forest（240 trees, depth 8, min leaf 5；训练仅用 primary/train）。下面只列 decision-relevant 指标。

### IID held-out, n=153, conditional family

| target | top-1 | top-3 | top-5 | k@99 | k@99.9 |
|---|---:|---:|---:|---:|---:|
| p_bucket | 56.86% | 84.97% | 92.81% | 7 | 7 |
| q_bucket / M2 proxy | 58.17% | 83.01% | 94.12% | 7 | 8 |
| T_bucket | 58.17% | 84.97% | 94.12% | 7 | 7 |

这足以说明 shell-derived representation 对 IID 生成分布有明显 inductive bias；但还不满足本 taskbook 的 S1 稳定性门槛。

### Adversarial challenge, n=600, no refit

| target | top-1 | top-3 | top-5 | k@99 | k@99.9 |
|---|---:|---:|---:|---:|---:|
| p_bucket | 44.00% | 62.33% | 74.83% | **10** | **10** |
| q_bucket / M2 proxy | 43.50% | 63.83% | 74.00% | **9** | **9** |
| T_bucket | 50.67% | 70.00% | 76.83% | **10** | **10** |

10 buckets 中，99% recall 对 `p` 和 `T` 必须保留全部 buckets；真正 M2 proxy `q_bucket` 也要保留 9/10，compression 仅约 `1.11x`。

### Cross-band 64-bit challenge

只用 24/32/40-bit primary training，再测试 64-bit challenge：

- p_bucket: top1 43.33%, top3 71.67%, top5 76.67%, `k@99=10`；
- q_bucket: top1 44.17%, top3 70.83%, top5 77.50%, `k@99=9`；
- T_bucket: top1 69.17%, top3 76.67%, top5 83.33%, `k@99=10`。

高召回 candidate compression 仍没有出现。

### Independent stdlib KNN15 verifier

为了避免把结论绑定在 sklearn/Random-Forest 上，checker 使用同一 frozen public feature family，但独立采用标准化后的 15-NN distance-weighted ranking：

| target | top-1 | top-3 | top-5 | k@99 | k@99.9 |
|---|---:|---:|---:|---:|---:|
| p_bucket | 43.17% | 60.00% | 71.17% | **10** | **10** |
| q_bucket / M2 proxy | 42.67% | 60.50% | 71.50% | **10** | **10** |
| T_bucket | 58.17% | 71.17% | 76.17% | **10** | **10** |

独立模型给出同一边界：在 challenge 上 99% / 99.9% recall 均无 bucket compression。

---

## 7. Ratio-stratum failure: strongest apparent signal由 near-twin 主导

以 authoring conditional p_bucket 为例：

| hidden evaluator stratum | n | top-1 | top-5 | k@99 |
|---|---:|---:|---:|---:|
| near_twin | 150 | 100.00% | 100.00% | 1 |
| balanced | 150 | 0.67% | 22.67% | 10 |
| moderate | 157 | 35.03% | 80.89% | 8 |
| strong | 143 | 40.56% | 96.50% | 7 |

这不是“普适定位器 + 少量尾部误差”的形态，而是明显的 regime dependence。尤其 balanced challenge 与 IID 的差异说明：模型学到的是生成分布/近平方条件的可泛化程度有限的 bias，而非稳定的 M2 coordinate surrogate。

Taskbook 明确规定“只在 balanced 或 near-twin 有效、广义 strata 崩溃”不得报告 bridge success；这里直接触发 kill condition。

---

## 8. Prediction-to-search wrapper: no S2

独立 KNN p-bucket ranking 被接入 exact factor-blind wrapper：

\[
N\to public\ features\to p/c\ bucket\ ranking\to prime\ divisibility\ scan\to exact\ divisor.
\]

对 120 个 64-bit challenge cases，比较 ordinary ascending-prime scan 到真实小因子 `p` 的 exact prime-candidate count：

| stratum | n | median cost ratio | total cost ratio | max ratio |
|---|---:|---:|---:|---:|
| near_twin | 30 | 0.00476 | 0.00514 | 0.0101 |
| balanced | 30 | 1.271 | 1.057 | 1.399 |
| moderate | 32 | 1.000 | 4.827 | 213.98 |
| strong | 28 | 1.000 | **801.46** | **29,555.20** |

总体 aggregate 因 near-twin 的 ascending-prime baseline 极其昂贵而会出现误导性的总和优势，但这不能升级为 S2：

1. near-twin challenge 的真实 `T=0`，匹配的 Fermat comparator 只需立即测试 `c^2-N` 是否为平方；它严格支配“先预测 p-bucket 再扫大量 prime”的解释；
2. balanced 已无稳定优势；
3. moderate/strong 出现大幅 cost inflation；
4. taskbook 要求跨 strata 保持并与匹配 comparator 比较，不能用容易层的大分母掩盖困难层退化。

因此：`NO S2 SEARCH BRIDGE`，更无 S3。

这里的 candidate-count ratio 只在“prime divisibility candidate checks”内部比较；不把它与 PCF2 的 gcd/operation counters 混成统一 wall-clock 单位。

---

## 9. Adversarial same-public-fingerprint / far-hidden-coordinate collisions

使用更粗、完全公开的 fingerprint

`(bit_band, floor(32*a/L), N mod 105, count_QR_passes(t=0..63))`

发现至少以下 exact collisions；两数 fingerprint 相同，但 verifier-only p_bucket 相差很远：

1. `N=3,596,999,671` vs `N=3,208,542,511`：bucket gap `6`；
2. `N=811,633,206,883` vs `N=713,031,446,353`：bucket gap `6`；
3. `N=742,770,913,727` vs `N=763,443,573,707`：bucket gap `5`。

公开文件不记录这几个数的因子。checker 临时分解并复核 collision 与 hidden bucket gap。

这不是对全部 30-dimensional feature vector 的无限族 no-go；它是 taskbook 要求的 finite adversarial witness，说明有限壳/同余粗 fingerprint 的近似或完全碰撞可以伴随很远的 multiplicative location。

---

## 10. PCF2 comparator boundary

本任务继承 PCF2 dual-compartment / leakage discipline，不重新发明更弱 benchmark。

PCF2 的原始 89-case 小规模 suite 中 Pollard rho、trial division、Fermat 等有各自 algorithm-local exact proxy counters；这些 raw counters不能与本任务 24–64-bit challenge 的 prime-candidate counts直接相加或当作统一 wall-clock。

因此本 return 只作两层合法比较：

- hidden-label compression：同 bucket vocabulary / 同 recall；
- search wrapper：同一 64-bit corpus内的 exact prime-candidate count，并用匹配 Fermat regime 拒绝 near-twin 的伪 S2。

没有声称击败 PCF2 中最强 factor-blind algorithm，因此 S3 明确为 false。

---

## 11. Closed boundary / open residue

### 冻结，不得换名重复开启

1. `FIXED_FINITE_PERIODIC_RESIDUE_FILTERS_ON_FERMAT_OFFSET`：精确关闭为 `Omega(T)` candidate count，只能常数倍 sieve；
2. `SHELL_RESIDUE_QR_CONDITIONAL_V1`：在本次 24/32/40/48/64-bit primary + adversarial challenge 合同下，关闭“稳定 99%/99.9% 高召回 multiplicative-shell bucket localization”主张；
3. 仅靠 IID / near-twin 的高命中，不得再次包装成 factor-blind M2 bridge；
4. 把 bucket reordering 在 easy strata 的收益汇总后掩盖 hard strata inflation，不得算 S2；
5. `B^2=b+T(2c+T)` 只是 Fermat coordinate identity，不得作为新增因子信息。

### 仍开放，但不在本任务内偷渡成功

- 非周期、随状态演化的 residual-priority / Hart streaming mechanism；该方向已有独立 taskbook，当前任务不重复发布 successor；
- 真正新的 algebraic/factor-blind mechanism，若其能力超出固定有限 residue wheel 与本次 static conditional family；
- 能在严格 challenge 与匹配 comparator 上保持高召回压缩、且成本计费后仍为正的 M2 surrogate。

所以本结果是**窄而强的 negative boundary，不是 universal impossibility theorem**。

---

## 12. Tool reuse

`REUSE_APPLIED`：

- T1 Scale Enumeration / Valuation：平方壳与 shell extraction；
- T4 Finite Fiber Capacity / Collision-Minima：公开 fingerprint collision / candidate compression 解释；
- T5 Precision / Refinement：carry / residue refinement 视角。

没有创建新的 general-purpose tool family。

---

## 13. Reproducibility outputs

- `research_returns/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE_RETURN_20260829.md`
- `research_artifacts/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE/public_corpus_manifest.json`
- `research_artifacts/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE/result_summary.json`
- `research_checks/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE_CHECK_20260829.py`
- `research_execution_records/RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE/ER-4F1EC87814863CFA854B.json`

Core independent verify:

```bash
python research_checks/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE_CHECK_20260829.py \
  --manifest research_artifacts/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE/public_corpus_manifest.json \
  --summary research_artifacts/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE/result_summary.json
```

本研究会话已执行 core independent checker：`PASS`；复核 1,400 个公开 rows、1,110 个 verifier-side semiprimes、`M=27720` periodic no-go、三类 independent KNN high-recall failure 与 3 组 adversarial collisions。

`--full-search` 额外重算较慢的 exact prime-count search audit；它不参与 core theorem truth。

## Final disposition

`NEGATIVE_BOUNDARY`.

- S1: `NOT GRANTED` — challenge high-recall compression collapses；
- S2: `NOT GRANTED` — matched comparator + generalized strata cost kill；
- S3: `NOT GRANTED` — no competitive factorization gain claim；
- strongest exact result: `FIXED_FINITE_PERIODIC_RESIDUE_FILTER -> OMEGA(T) CANDIDATES`；
- strongest empirical result: `SHELL_RESIDUE_QR_CONDITIONAL_V1 -> IID SIGNAL BUT ADVERSARIAL HIGH-RECALL FAILURE`；
- successor residue: `NONPERIODIC / ALGEBRAIC FACTOR-BLIND MECHANISM`, with the already-published residual-priority/Hart audit kept separate.

Return is frozen for Driver review; no Working Truth or canonical promotion is claimed.
