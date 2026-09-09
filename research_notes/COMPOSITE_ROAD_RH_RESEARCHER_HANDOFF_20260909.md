# 合数道路 RH 路线：新研究员交接入口

Prepared: 2026-09-09
Provenance researcher: `EM-FREE-C4A91D / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`
Status: `STATE-MACHINE HANDOFF / NO RH PROOF / NO FOUNDATION ADMISSION`

本文件是“合数是路，素数是坑”RH 路线的正式交接入口。新领取任务的研究员不需要恢复前任聊天；从本文件、来源索引和各任务书即可继续。

## 1. 最高研究约束

用户锁定：**合数是路，素数是坑；路都没有了，光盯着坑有啥用。不允许轻易判定冗余。**

机器语义由当前 `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json` 控制。因子可重建不等于观察方向冗余；固定窗口小量、有限阶导数消失、数值系数接近零，都不是全局冗余证书。完整整数总体、联合合数方向、符号、相位、起点与尺度信息默认保留，除非有 observer-specific 的精确下降/张成/未来操作安全证书。

## 2. 已完成且不要重做的阶段

精确来源与不可变提交见：

`artifacts/composite_road_rh/handoff_20260909/source_index.json`。

推荐阅读顺序：`S0 -> S5 -> S6 -> S7 -> S3 -> S2 -> S4 -> S1`。

其中：

- `S0`：9月5日余数坐标、合数6不可删除下界、prime-only 对偶证书与完整有理数验证器；本次重跑记录为 `artifacts/composite_road_rh/handoff_20260909/verification/stage2_certificate_rerun.json`，状态 `EXACT_CHECK_PASS`。
- `S5`：修正版正道路能量 `Q_a` 与有限 Green 恒等式，是当前原始道路能量入口。
- `S6`：离散 midpoint discrepancy 与 thickness/horizon 极限不交换，明确提出 escaping-horizon 尾项。
- `S7`：Ramanujan 频率分解；平移平均丢失交叉相位，当前需要 fixed-origin/anchored coherence。
- `S3`：修正版边界斜率；必须区分 raw road energy `Q_a` 与 completed Schur energy `Delta_a`。
- `S2`：补全 `xi(s)/xi(s+a)` 的 Schur/Pick 等价接口；不能把条件正性当无条件证明。
- `S4`：正道路绝对控制只能到 `Re(s)>1-a`，说明纯绝对值路线的穿透边界。
- `S1`：有限 future-road port、正道路变形与 calibration capacity 的早期来源；必须与后续修正一起消费。

不要重做：冻结有理候选搜索、Euler 恒等式换名、原始 Weil 自动 PSD 捷径、直接认定 `Q_a=Delta_a`、用 fixed-horizon 小系数判合数冗余。

## 3. 当前真正的未解决单元

正道路权重：

`R_a(n)=sum_{d|n} mu(d)/d^a = product_{p|n}(1-p^(-a))`, `a>0`。

定义 `c_a=1/zeta(1+a)`, `S_a(x)=sum_{n<=x}R_a(n)`, `E_a(x)=S_a(x)-c_a x`，当前原始道路能量为

`Q_a = integral_0^infinity |E_a(x)-1_[1,infinity)(x)|^2 dx/x^2`。

结合已核对的经典接口，当前无条件目标是直接取得 `Q_a=O(a)` as `a downarrow 0`；这是 RH 等价目标，不是已完成证明。

离散形式使用

`B_(a,N)=S_a(N)-1-c_a(N+1/2)`

及 `sum B_(a,N)^2/N^2`。真正困难集中在两处：

1. **anchored cross-frequency coherence**：保留不同有理频率之间被 translation averaging 删除的交叉相位，并且保留 `-1-c_a/2` 常数通道；
2. **escaping horizon**：寻找 `M(a)->infinity` 并严格控制 `sum_{N>=M(a)} B_(a,N)^2/N^2`，不能用有限计算外推无限尾项。

## 4. 修正边界

`Z_a(s)=zeta(s)/zeta(s+a)`，而 `C_a(s)=xi(s)/xi(s+a)=K_a(s)Z_a(s)`。

`Q_a` 对应 raw `Z_a`；补全 Schur 能量 `Delta_a` 对应 `C_a`。两者不相等。当前修正版只在相应条件下通过显式 completion error 比较它们。有限 raw-road 否证阈值必须使用修正后的 `U_road(a)`，不能直接使用更小的 completed bound `U_comp(a)`。

同样，平移平均后的 diagonal power spectrum 不能自动替代 anchored observer；如果未来要做压缩，必须证明实际 observer-preservation，而不是仅凭“平均量无条件有限、完整量等价 RH”来下结论。

## 5. 已正式准备的三个状态机任务

三项任务共同属于父目标：`OBJ-RH-COMPOSITE-ROAD-UNIFORM-ENERGY`，研究者发布默认运行等级均为 `P2/MEDIUM`。publication 只使任务进入正式可领取定义，不授予 CLAIM、Working Truth、Foundation 或 theorem promotion。

- `RS-RH-COMPOSITE-ROAD-BASELINE-AUDIT`
  - Publication: `TP2-139EE61FF11BE2292C79`
  - Taskbook blob: `sha1:0085aef36d9c3a9b952cf42684ed5a1a38abb075`
  - 语义：`REPLAY`，独立核查修正版研究基线，不伪造历史父任务。

- `RS-RH-COMPOSITE-ROAD-ANCHORED-COHERENCE`
  - Publication: `TP2-18F1587AE8A5F365AE29`
  - Taskbook blob: `sha1:b574649f66b9c3b6cb86da2772cb92cc056614f5`
  - 语义：`CONTINUATION`，父任务为 baseline audit；构造 fixed-origin rational-frequency cross-phase kernel 与安全 tail interface。

- `RS-RH-COMPOSITE-ROAD-ESCAPING-TAIL`
  - Publication: `TP2-C026B13F6E5D1516A91C`
  - Taskbook blob: `sha1:52ffd0e28ddc36762b64dde3d2f0cbf84523549d`
  - 语义：`CONTINUATION`，父任务为 baseline audit；研究尺度增长的 Green-energy 尾项与严格误差预算。

后两个任务之间不是互相依赖关系；它们只消费 baseline audit 的可用结论，可并行推进。

## 6. 新研究员的执行纪律

先读本文件和 source index，再读自己领取的 taskbook。所有旧研究笔记仍保持原有 theorem status，不因本次状态机登记自动升级。任何有限数值证书、条件于 RH 的推导、RH 等价 reformulation 和无条件 theorem 必须分别标记。

如果发现旧结论错误，返回最小受影响作用域与修正证据；不要把整条合数道路路线一次性判废，也不要为了维持路线而掩盖反例。
