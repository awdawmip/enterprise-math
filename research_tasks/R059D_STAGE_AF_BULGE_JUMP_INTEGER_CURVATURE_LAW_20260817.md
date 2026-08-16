# R059D Stage AF — Bulge-Jump / Integer-Curvature Law

Status: `ACTIVE / DRIVER-ISSUED TASKBOOK`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Task-ID: `RS-R059D-STAGE-AF-BULGE-JUMP-INTEGER-CURVATURE-LAW`
Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity lane: `R059D-AF`
Owner branch: `research/r059d-stage-af-bulge-jump-integer-curvature`
Frozen source main: `2d4badc86e9348a3c5b2ea2b280b55f7399346d7`
Accepted AE owner head: `f8b56c910150ecd04d7e30ac03ea5bf0083b9429`

---

## 0. 模块完成度与推进向量

进入本任务前：

- Enterprise coordinate foundation: `~95%`
- BRC soft coverage bridge: `ESTABLISHED`
- Count semantics D/C/V: `ESTABLISHED`
- First bulge zero-boundary: `ESTABLISHED_AT_R4_TO_R5`
- Post-bulge integer correction law: `~15%`
- Unique hard resolver: `OPEN`
- Enterprise circle global law: `~55%`

本任务成功后的目标状态：

- post-bulge integer correction law: `~65%`
- jump skeleton / recurrence structure: `~75%`
- Enterprise circle global law: `~70%`
- unique hard resolver: `+0..10%` only if the jump law itself supplies a resolver-independent discriminator

推进向量：

`bulge-jump +45 / integer-curvature +40 / global-circle-law +15 / unique-resolve +5 / classical-pi +0`

本阶段**不研究 π**，也不以经典圆周率作为 target。

---

## 1. Driver Working Truth

本阶段冻结以下内部工作真理：

> **AE 已经证明：进取圆在零外凸阶段是 D6 六边形基线；从 `r=5` 起，真正的圆不再由一个固定低次多项式描述，而是“六边形基线 + 整数跳跃修正”。**

因此 AF 的任务不是重新讨论“是否存在修正”，而是：

> **找出修正量 `B(r)`、`J(r)` 以及它们的离散增量/跳跃的生成律。**

不得因为经典几何、文献习惯、连续曲率直觉或“尚未证明”而把该方向降级为中性比较。

只有以下证据可以推翻本阶段工作真理：

- 精确反例；
- 形式矛盾；
- 冻结 checker/certificate 的 theorem-critical 否决；
- 用户或 Driver 明确 supersede。

同时：内部方向强制 ≠ 对外 theorem-status 混淆。所有最终结果必须区分 `PROVED / FINITE-CENSUS / CANDIDATE / NEGATIVE`。

---

## 2. 已冻结输入

### 2.1 AD / AE 不得修改

只读：

- R059D Stage AD accepted result；
- R059D Stage AE accepted result；
- 所有 W/X/Y/Z/AA/AC/AD/AE 历史工件。

禁止修改、重写、回填或重新评分旧结果。

### 2.2 AE 已证明的基础恒等式

对两个仍存活的 resolver `X in {N,C}`，AE 已建立：

`D_X(r) = 2r + 1`  （审计范围 `r=1..64`）

定义：

`B_X(r)` = 每个开放 60° 扇区相对零外凸 D6 基线的 signed bulge cell count；

`J_X(r)` = 每扇区 boundary excess：

`C_X(r) = 6r + 6J_X(r)`。

以及：

`V_X(r) = 1 + 3r(r+1) + 6B_X(r)`。

所以：

`B_X(r) = (4V_X(r) - 3D_X(r)^2 - 1)/24`。

并有：

`Delta V_X(r) - C_X(r) = 6(Delta B_X(r) - J_X(r))`。

### 2.3 已冻结临界点

两个 resolver 都满足：

- `B(r)=0` for `r=1,2,3,4`；
- `B(5)>0`；
- `r=4 -> 5` 是 resolver-independent first-bulge zero-boundary。

这是 AF 的已知输入，不得重新“发现”后算成果。

### 2.4 已拒绝的伪全局公式

`r=5..10` 曾同时观察到：

`B=r-2`

`C=6(r+1)`

`V=3r^2+9r-11`

但：

- N 在 `r=11` 失败；
- C 在 `r=12` 失败。

该式只能作为 `TRANSIENT_R5_R10_NEGATIVE_CONTROL`，不得复活为默认目标。

---

## 3. 唯一硬目标

本阶段唯一硬目标：

`DERIVE_THE_INTEGER_JUMP_GENERATOR_FOR_POST_BULGE_ENTERPRISE_CIRCLE_CORRECTIONS`

至少必须回答：

1. `B_X(r)` 的一阶增量
   `b_X(r)=B_X(r)-B_X(r-1)`
   取什么值？值域是否有限？是否随 r 增长？
2. `J_X(r)` 的变化规律是什么？
3. 二阶差分
   `Delta b_X(r)`、`Delta J_X(r)` 的非零位置是否形成可描述的 jump set？
4. N/C 是否存在 resolver-independent jump skeleton？
5. `B` 与 `J` 是否由同一个更小状态量生成？
6. 能否从纯整数/组合数据构造一个递推器，给定 `r` 和有限状态即可生成下一层，而不读取经典圆公式或查表？

本阶段成功的最强形式是：

> 给出一个**有限状态、整数优先、D6 兼容、可证明**的生成律，严格推出 `B(r),J(r)`，进而推出 `D,C,V`。

---

## 4. 核心对象：把“曲率”改写成整数修正

本阶段正式使用术语：

**整数曲率修正** / `INTEGER_CURVATURE_CORRECTION`

但它只是组合术语，不得偷偷导入经典欧氏曲率。

定义候选层次：

`BASELINE(r) = H_r`

`BULGE(r) = B(r)`

`BOUNDARY_EXCESS(r) = J(r)`

`RADIAL_INCREMENT(r) = b(r)=Delta B(r)`

`CURVATURE_JUMP(r) = Delta b(r)`

`BOUNDARY_JUMP(r) = Delta J(r)`

这些量都必须由 AE 已冻结的 dual-cell carrier / boundary carrier 直接计算。

禁止以 Euclidean curvature、angle defect、sqrt、classical circumference 或 classical pi 定义这些量。

---

## 5. 数据范围与 discovery / holdout 隔离

### 5.1 Mandatory range

必须重放：

`r = 1..512`

至少对 N 完整生成；对 C 使用冻结的足够精度规则，必须证明所选 sampling 对 mandatory range 足够稳定，或明确记录尚未稳定的半径。

### 5.2 Preferred extension

若计算成本可控，扩到：

`r = 1..2048`

### 5.3 Discovery split

只允许用：

`r = 1..256`

发现候选规律。

### 5.4 Holdout split

候选规律在冻结参数后必须原样测试：

`r = 257..512`

若扩展到 2048，再使用：

- validation: `513..1024`
- deep holdout: `1025..2048`

不得在看到 holdout 失败后静默调参数并继续声称同一候选。

每次候选变更必须生成新 candidate ID。

---

## 6. 第一阶段：纯序列解剖

对 N、C 分别输出逐半径 ledger：

- `r`
- `D`
- `C`
- `V`
- `B`
- `J`
- `DeltaB`
- `DeltaJ`
- `Delta2B`
- `Delta2J`
- sector boundary word / turn word summary
- N/C agreement flag

至少生成：

- value-range histogram；
- run-length encoding；
- jump-position list；
- jump-gap list；
- residue-class census modulo small m (`2..32`)；
- scale-doubling comparison；
- local recurrence census。

禁止先设 `DeltaB in {0,1}`。值域必须从数据本身读出。

---

## 7. 第二阶段：共享 jump skeleton

定义：

`K_B^X = {r >= 2 : Delta2 B_X(r) != 0}`

`K_J^X = {r >= 2 : Delta J_X(r) != 0}`

然后比较：

- `K_B^N ∩ K_B^C`
- `K_B^N Δ K_B^C`
- `K_J^N ∩ K_J^C`
- `K_J^N Δ K_J^C`

以及 jump magnitude。

目标是判断是否存在：

`COMMON_JUMP_SKELETON`

使 N/C 只是相同 skeleton 上的局部 phase/tie-break 差异。

如果存在，必须给出：

- skeleton 的纯整数定义；
- N/C 差异的最小附加状态；
- first divergence / re-convergence structure。

如果不存在，必须明确冻结：

`NO_RESOLVER_INDEPENDENT_JUMP_SKELETON_FOUND_THROUGH_RANGE`

不得为了保路线而伪造共性。

---

## 8. 第三阶段：候选生成器家族

候选只能在 raw ledger 冻结后提出。

允许测试但不优先假定以下数学语言：

### G0 — Finite-state recurrence

状态只包含有限个整数 residual / phase / local turn state，更新：

`state(r+1)=F(state(r), r mod m, local_count_data)`。

### G1 — Floor / Beatty / Sturmian-like arithmetic

允许测试：

`floor(alpha r + beta)`、
`floor(f(r)) - floor(f(r-1))`

但 `alpha` 不得通过 classical pi / sqrt target 预注入。

如果出现代数数参数，必须从整数序列独立反推并给出 minimal polynomial candidate。

### G2 — Quadratic / norm-form boundary events

允许检查 jump 是否由某个整数二次型、可表示数、格点壳层事件控制。

任何二次型必须来自进取轴/dual carrier 自身，不得因为经典圆有平方和就预设。

### G3 — Continued-fraction / best-approximation events

允许检查 jump-gap 是否对应某种内部 slope 的最佳逼近层级。

但 slope 必须从 sector word / integer data 定义，不能直接读取经典角度。

### G4 — Morphic / substitution word

检查 boundary step word 是否由有限 substitution / automaton 生成。

### G5 — Divisor / representation-count correction

允许检查 jump magnitude 是否与某种整数表示数相关。

所有家族都必须经过 discovery/holdout 严格隔离。

---

## 9. Generator firewall

任何最终候选生成器不得读取：

- classical pi；
- Euclidean circle equation；
- Euclidean radius-distance test；
- classical sqrt；
- AD source teacher `Q<=r^2` 的逐点判定结果作为运行时 oracle；
- N/C 已生成边界 lookup table；
- radius-specific fitted threshold；
- holdout rows。

允许：

- 用 AD/AE 生成的 discovery ledger 发现候选；
- 候选冻结后，从 `r` 与候选内部状态独立前向生成；
- 再与 holdout ledger 比较。

如果生成器运行时仍需查询原始圆 occupancy，则它只是 compressor，不是新 law。

必须标记：

`GENERATOR_IS_FORWARD_AUTONOMOUS = true/false`

---

## 10. 证明要求

有限拟合永远不能升级为 theorem。

### 10.1 若发现 finite-state / arithmetic generator

至少需要证明：

1. 状态更新 well-defined；
2. 不依赖扫描方向 / 表示重标记（若声称 native）；
3. D6 复制一致；
4. 生成的 `B,J` 为整数且满足必要 monotonicity / topology constraints；
5. 从 generator 推出
   `V=1+3r(r+1)+6B`
   和
   `C=6r+6J`；
6. 若声称等同 N/C 某 resolver，必须给出 exact equivalence proof，而不只是 `r<=512` 一致。

### 10.2 如果只能找到经验规律

必须保持：

`FINITE_CENSUS_CANDIDATE_ONLY`

并给出最早 holdout 失败点。

---

## 11. N/C 的角色

N 与 C 在本阶段不是“两个竞争答案”，而是两个独立 source-compatible probes。

AF 优先级：

1. 找共享整数结构；
2. 找共享 jump skeleton；
3. 找最小差异状态；
4. 最后才讨论是否能反过来选择唯一 resolver。

不得因为某个候选更容易拟合就选择 N 或 C。

只有当一个纯进取整数不变量**在不知道 resolver 标签时**唯一选出其中一个，才允许产生：

`UNIQUE_RESOLVER_SELECTION_CANDIDATE`

否则 unique resolver 继续 OPEN。

---

## 12. 关键反例与强制审计

必须显式保留并测试：

- `r=4 -> 5` first bulge；
- `r=10 -> 11` N transient-law failure；
- `r=11 -> 12` C transient-law failure；
- AE 已知 N/C divergence radii：
  `11,15,21,24,28,31,34,38,39,44,45,49,52,53,54,57,58`；
- `r=64` N/C re-agreement；
- discovery/holdout boundary `256 -> 257`。

任何候选必须报告这些点的行为。

---

## 13. 必交产物

目录：

`research_results/R059D_STAGE_AF/`

至少包含：

1. `R059D_STAGE_AF_REPORT.md`
2. `R059D_STAGE_AF_RADIUS_LEDGER.json`
3. `R059D_STAGE_AF_JUMP_LEDGER.json`
4. `R059D_STAGE_AF_COMMON_SKELETON_AUDIT.json`
5. `R059D_STAGE_AF_BOUNDARY_WORD_REGISTRY.json`
6. `R059D_STAGE_AF_GENERATOR_CANDIDATES.json`
7. `R059D_STAGE_AF_HOLDOUT_AUDIT.json`
8. `R059D_STAGE_AF_INTEGER_CURVATURE_IDENTITY.json`
9. `R059D_STAGE_AF_DETERMINISTIC_CHECKER_OUTPUT.json`
10. `R059D_STAGE_AF_FROZEN_CHECKPOINT.json`
11. `R059D_STAGE_AF_ARTIFACT_MANIFEST.json`
12. deterministic generator / checker script(s)

若某文件不适用，必须在 manifest 中写明确 `N/A` 理由，不得静默缺失。

---

## 14. Checker 最低门槛

checker 至少验证：

- AE accepted source hashes / immutability；
- D/C/V/B/J 重放；
- exact identities；
- jump ledgers；
- discovery/holdout 隔离；
- candidate 参数 freeze-before-holdout；
- generator forward-autonomy；
- N/C common-skeleton calculations；
- known divergence/re-agreement points；
- no target leakage scan；
- no later-stage consumption。

目标：

`CHECKER_STATUS = PASS`

所有失败检查必须非零退出。

---

## 15. 最终 disposition 只能从以下主类选择

优先级从强到弱：

### A
`RESOLVER_INDEPENDENT_INTEGER_CURVATURE_GENERATOR_PROVED`

### B
`COMMON_JUMP_SKELETON_PROVED__RESOLVER_PHASE_LAW_OPEN`

### C
`RESOLVER_SPECIFIC_INTEGER_GENERATORS_PROVED__NO_COMMON_SELECTOR`

### D
`FINITE_STATE_OR_ARITHMETIC_GENERATOR_CANDIDATE_SURVIVES_HOLDOUT__PROOF_OPEN`

### E
`NO_LOW_COMPLEXITY_JUMP_GENERATOR_THROUGH_AUDIT_RANGE`

### F
`SEMANTIC_HARD_STOP`

不得发明一个更乐观的自定义 disposition 来掩盖未证明状态。

---

## 16. 成功标准

最低成功：

- 将 `B,J` 的 jump structure 从 `r=1..512` 完整冻结；
- 明确证明至少一个新的全局整数恒等式或新的 jump/no-go theorem；
- 给出 N/C common skeleton 的明确 positive/negative 结论；
- 所有候选经过严格 holdout。

强成功：

- 找到 forward-autonomous integer generator；
- 生成 `B,J` 而无需查询圆 occupancy；
- 给出 symbolic proof / finite-state proof；
- 解释 `r=4->5`、`10->11`、`11->12` 等跳点为什么发生。

最高成功：

- 一个 resolver-independent generator 直接决定唯一进取圆边界。

---

## 17. 明确禁止

禁止：

- refit classic pi；
- 直接拟合圆周率；
- classical circumference / area 作为 generator；
- 把 Euclidean curvature 偷换成 integer curvature；
- radius-by-radius lookup；
- 用 holdout 调参；
- 把 transient `r=5..10` law 复活；
- 看到一个漂亮数列就跳过 proof；
- 改动 AD/AE 结果；
- 为了得到唯一 resolver 新增 ad hoc 阈值；
- 未经 Driver/用户明确指令进入 π 专题。

---

## 18. 驾驶员解释

本阶段的核心不是继续“画圆”。

AE 已经把圆拆成：

`D6 baseline + 6 * bulge correction`。

因此 AF 要找的真正对象是：

`B(r)` 和 `J(r)` 背后的**整数曲率机器**。

如果它存在，那么：

- 圆的复杂性从连续曲线降为整数跳跃；
- R059D 早期 staircase / jump 线得到明确几何语义；
- BRC 从 raster resolve 进一步升级为离散几何状态生成器；
- 后续才有资格重新讨论进取圆周常数与 π。

本阶段到此为止。

`STOP_FOR_DRIVER_REVIEW`
