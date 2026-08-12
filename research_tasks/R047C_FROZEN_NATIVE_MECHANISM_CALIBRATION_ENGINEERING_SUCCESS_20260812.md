<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R047C-FROZEN-NATIVE-MECHANISM-CALIBRATION-ENGINEERING-SUCCESS",
  "title": "R047C Frozen Native Mechanism Calibration against Engineering-Success Constraints",
  "kind": "RESEARCH",
  "owner": "program/foundational-logic-engineering-inversion",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_CALIBRATION / BLIND_GENERATION_AUDIT / ENGINEERING_SUCCESS",
  "frontier": "Open the precommitted R046 calibration target only after both blind Foundation candidate sets are frozen, then determine which frozen native mechanisms can explain independent engineering-success constraints with the least bridge/parameter/definition debt without altering candidate cores.",
  "next_action": "Verify both Foundation freeze hashes and the precommitted target blob; evaluate all twelve frozen candidates independently against the four target constraints using typed bridge ledgers, quantitative/holdout evidence where possible, and explicit explanatory-debt accounting before any cross-candidate ranking.",
  "dependencies": [
    {
      "target": "research_inputs/r047/R047_DUAL_FOUNDATION_FREEZE_MANIFEST_20260812.json",
      "action": "VERIFY_BOTH_FOUNDATION_FREEZES_BEFORE_CALIBRATION",
      "satisfied": true
    },
    {
      "target": "research_inputs/r047/R047P_FROZEN_CALIBRATION_PROJECTION_20260812.json",
      "action": "CONSUME_PROJECT_ARM_FROZEN_CANDIDATES_READ_ONLY",
      "satisfied": true
    },
    {
      "target": "research_inputs/r047/R047I_FROZEN_CALIBRATION_PROJECTION_20260812.json",
      "action": "CONSUME_ISOLATED_ARM_FROZEN_CANDIDATES_READ_ONLY",
      "satisfied": true
    },
    {
      "target": "research_inputs/r047/R047_CALIBRATION_TARGET_OPENED_20260812.json git blob bc24a121897a912f026b0c85af914268f00997e5",
      "action": "CONSUME_PRECOMMITTED_TARGET_AFTER_DUAL_FREEZE",
      "satisfied": true
    },
    {
      "target": "Foundational Logic V1 and Native-Semantics Admissibility Gate V3",
      "action": "CONSUME_FOUNDATION_CALIBRATION_SEPARATION_AND_NO_OUTPUT_COPYING",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R047 dual Foundation freeze manifest",
    "R047P accepted frozen head deff14d75ef93815d6a8dcb8aa79039e68aa390a",
    "R047I isolated bundle SHA-256 d85f3687c3cef311712ac18718cf41d51b6bee21db6efadea9576d971a2e4d96",
    "R046 target precommit git blob bc24a121897a912f026b0c85af914268f00997e5"
  ],
  "evidence_status": "POST_FREEZE_CALIBRATION / TARGET_PRECOMMITTED / CANDIDATE_CORES_IMMUTABLE",
  "last_progress_ref": "Both R047 Foundation arms accepted; target blob opened only afterward and byte-identical Git blob verified.",
  "last_progress_at": "2026-08-12T23:52:00+08:00",
  "hard_block": null,
  "tags": [
    "R047C",
    "calibration",
    "engineering-success",
    "blind-generation",
    "frozen-candidates",
    "bridge-debt",
    "holdout",
    "explanatory-compression",
    "anti-retrofit"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R047C",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R047C — Frozen Native Mechanism Calibration against Engineering-Success Constraints

Status: `READY / P0 / POST-FREEZE CALIBRATION / TARGET OPENED AFTER DUAL FREEZE / NOT CANONICAL`

## 0. 母问题

R047P 与 R047I 已在不知道 calibration target 内容的情况下分别冻结 6 个 native mechanisms。现在第一次打开预先承诺的 R046 target。

本任务问：

> **在不修改任何 frozen candidate core 的前提下，哪些机制能够以最少的 bridge、参数、目标特定补丁与有效定义债，真正解释 R046 中彼此独立的工程成功约束？**

这里“解释”不等于产生一个熟悉数值，也不等于概念上像某种经典现象。必须区分结构对应、定量预测、跨协议 holdout、尺度推广和 target-specific retrofit。

## 1. Freeze integrity gate — 第一动作

开始任何 calibration 前必须核验：

### Project arm

- source head: `deff14d75ef93815d6a8dcb8aa79039e68aa390a`
- candidate-set SHA-256: `bf309a1b6d0bebf10a58345af768bac0b63747934eccb63538d0e0fe6cf0d494`
- candidate count: 6

### Isolated arm

- identity: `ISO-R047F-91B6C2`
- original user-supplied bundle SHA-256: `d85f3687c3cef311712ac18718cf41d51b6bee21db6efadea9576d971a2e4d96`
- candidate-set SHA-256: `220e7f72ba9c4cbffc8fcd98b6b7df9b952bbccaaa0b4415cb36f47ea4b0eb3f`
- candidate count: 6

### Calibration target

必须验证：

`research_inputs/r047/R047_CALIBRATION_TARGET_OPENED_20260812.json`

Git blob SHA 恰为：

`bc24a121897a912f026b0c85af914268f00997e5`

这必须与候选冻结前的 seal 完全相同。

任何 freeze/hash/target mismatch 都必须先标记，不能静默继续。

## 2. Candidate core 绝对不可修改

对 12 个 frozen candidates：

- definition 不得改；
- state carrier 不得改；
- parameter domain 不得扩大或缩小；
- update/collapse law 不得改；
- theorem/counterexample boundary 不得回写；
- 不得因为看到 KENG target 而把一个新 primitive 塞进 candidate core；
- 不得把后验 bridge 伪装成 Foundation 时已经存在的对象。

若发现一个有前途的 repair/extension，只能记录：

`NEW_GENERATION_CANDIDATE_FOR_LATER_TASK`

不得在 R047C 内修复原 candidate。

## 3. Calibration target

唯一正式 target criteria 是 precommitted target blob 中的四个 constraints：

- `KENG-01_GEOMETRIC_MEASURE_COHERENCE`
- `KENG-02_CYCLE_CLOSURE_AND_RELATIVE_PHASE`
- `KENG-03_DIFFUSIVE_RELAXATION`
- `KENG-04_BOUNDED_MODE_SPECTRUM`

可以读取 R046 的来源/约束 artifacts 以核对 protocol provenance、scale 与 tolerance，但：

- 不得新增第五个 scoring target；
- 不得改变四个 target 的含义；
- 不得看完 candidate 后重写 tolerance；
- 不得以 classical pi 数值接近程度作为 loss。

## 4. 每个 candidate × KENG 必须建立 typed bridge ledger

对每一格 `(candidate M_i, KENG_j)`，先声明 bridge：

`frozen native state/dynamics -> calibration-layer bridge/readout -> target observable protocol`

bridge 里的每个对象必须类型化：

- `N0_DEFINABLE_FROM_FROZEN_CORE`
- `FROZEN_N1_STATE_OR_OPERATION`
- `CALIBRATION_READOUT`
- `PROTOCOL_MAPPING`
- `TARGET_SPECIFIC_ADAPTER`
- `ILLEGAL_EFFECTIVE_DEFINITION_IMPORT`

### Bridge 强度分类

`B0_NATIVE_DIRECT`
: target-relevant structure直接来自 frozen mechanism，自身无需新增动态状态。

`B1_UNIFORM_READOUT`
: 需要一个统一 readout，但同一个 readout family 能跨多个 protocol/KENG 使用，且不复制 target 定义。

`B2_CALIBRATED_PARAMETER_BRIDGE`
: 使用 candidate 冻结时已经允许的参数域；参数必须在明确 training slice 上确定，再在独立 holdout 上冻结验证。

`B3_TARGET_SPECIFIC_ADAPTER`
: 为一个 target/protocol 专门发明 adapter。可作为诊断，但不能计为强 foundational explanation。

`B4_ILLEGAL_LEAKAGE`
: 使用 center/distance/equidistance/radius/circle/radian/continuum/Fourier/Gaussian/classical-pi target 等被禁止定义来强制回收答案。该格直接 FAIL。

## 5. Calibration evidence 等级

每一格必须用以下最强合法等级之一：

`E0_UNMAPPED`
: 没有合法 bridge。

`E1_QUALITATIVE_MECHANISM`
: 有结构类比/机制，但没有 target-scale quantitative prediction。

`E2_EXACT_STRUCTURAL_CONSTRAINT`
: 能严格推出 target 的 definition-stripped structural law，但尚未达到工程量化协议。

`E3_QUANTITATIVE_IN_SAMPLE`
: 在声明的 calibration/training protocol 上满足数值/尺度/tolerance，但尚未独立 holdout。

`E4_QUANTITATIVE_HOLDOUT`
: 参数和 bridge 冻结后，在独立 protocol/scale/channel holdout 上仍满足 target tolerance。

`E5_CROSS_KENG_SHARED_EXPLANATION`
: 同一 frozen mechanism + 同一低债 shared bridge/state 同时达到至少两个 KENG 的 E4，并且没有 per-target adapter。

不得把 E1/E2 写成“工程验证通过”。

## 6. 参数纪律

候选冻结时已有参数可以使用，但必须逐一登记：

- structural parameter；
- protocol-controlled input；
- fitted calibration parameter；
- arbitrary choice；
- target-specific patch。

规则：

1. 不能新增 candidate-core 参数；
2. fitted parameter 必须声明 training 数据；
3. fit 后在 holdout 前冻结；
4. 同一参数如果每个 KENG 都重新拟合，不能宣称 shared explanation；
5. 参数越多不是自动失败，但必须计入 explanatory debt；
6. `s`、iteration depth、event order、initial state 等原冻结对象不能偷偷重命名成 radius/time/phase 等经典定义。

## 7. Holdout 设计

优先使用 R046 已经分离出的独立工程 channels。

### KENG-01
至少尝试：

- 一类 profile/wrap boundary protocol 用于 bridge construction；
- 其它 enclosed-measure / flow / gravimetric channel 做 holdout。

不能用 circumference/area/volume classical formula 在 bridge 中互相转换来伪造 holdout。

### KENG-02
至少把 mechanical cycle indexing 与 electronic time/fraction phase 分开，一边 calibration，一边 holdout。

### KENG-03
若只能给出“会扩散/会松弛”的图像，最多 E1/E2；达到 E4 必须给出 scale-time dependence 和实验 envelope 内 prediction。

### KENG-04
mode ordering/spacing 与 state-dependent shifts 必须作为同一预测体系；acoustic 与 microwave cross-channel 至少一边为 holdout。

若 frozen candidate 根本没有足够 bridge 到真实单位，诚实返回 E0/E1/E2，不得为了拿高分添加经典几何。

## 8. Explanatory debt vector — 不先压成一个总分

每个 candidate 返回：

`D(M)=(`

- `keng_E4_coverage`,
- `keng_E5_shared_pairs`,
- `independent_protocol_holdouts_passed`,
- `bridge_strength_profile`,
- `fitted_parameter_count`,
- `target_specific_adapter_count`,
- `illegal_import_count`,
- `unexplained_keng_count`,
- `frozen_state_information_cost`,
- `cross_keng_shared_state_count`

`)`

先做 Pareto，不要人为选择权重产生一个“综合分”。

只有当一个 candidate 在 target coverage 更高、bridge debt 不高、参数 debt 不高、且不存在 leakage 时严格支配其它 candidate，才允许写 `DOMINATES_ON_DECLARED_CALIBRATION_AXES`。

否则保留 Pareto family。

## 9. Cross-arm blind evidence

在所有 12 个 candidate 独立完成 calibration matrix **以后**，才允许分析 project/isolated arms 的相似性。

需要区分：

- `INDEPENDENT_REDISCOVERY`: 两臂盲生成了数学上同族/近同族机制；
- `CALIBRATION_CONVERGENCE`: 同族机制在 target 上独立表现相近；
- `ARM_SPECIFIC_SUCCESS`: 只有一臂生成的结构表现突出；
- `COMMON_ATTRACTOR_BUT_CALIBRATION_FAILURE`: 两臂都想到但工程 target 不支持。

独立重现本身不是 target success；target success 本身也不能抹掉独立 provenance。

## 10. 必做 kill tests

至少攻击：

1. `ONE_NUMBER_FIT`: 接近 classical pi 数值但 KENG coverage 低；必须判失败。
2. `METAPHOR_AS_EXPLANATION`: “看起来像周期/扩散/模态”但无结构/量化证据；不得超过 E1。
3. `TARGET_DEFINITION_BRIDGE`: 用 circle/radius/radian/PDE/Fourier/Gaussian 等直接把答案搬进 bridge；B4 FAIL。
4. `PER_KENG_PATCHWORK`: 四个 target 四套无共享关系 adapter；即使单格能 fit，也不得宣称 unified mechanism。
5. `PARAMETER_EXPLOSION`: 用大量自由参数逐协议拟合；计高 debt，并要求 holdout。
6. `TRAINING_AS_HOLDOUT`: 同一测量链重新包装成独立证据；必须杀掉。
7. `ARM_PROVENANCE_BIAS`: 不能因为 project arm 或 isolated arm 身份优先排序。
8. `FOUNDATION_REWRITE`: calibration 后回改候选 definition；立即失去 blind claim。

## 11. Required artifacts

至少返回：

- `research/r047c/R047C_REPORT.md`
- `research/r047c/R047C_FREEZE_INTEGRITY.json`
- `research/r047c/R047C_CALIBRATION_MATRIX.json` — 12×4 全矩阵
- `research/r047c/R047C_BRIDGE_LEDGER.json`
- `research/r047c/R047C_PARAMETER_DEBT.json`
- `research/r047c/R047C_HOLDOUT_LEDGER.json`
- `research/r047c/R047C_TARGET_LEAKAGE_AUDIT.json`
- `research/r047c/R047C_EXPLANATORY_DEBT_VECTORS.json`
- `research/r047c/R047C_PARETO_FRONTIER.json`
- `research/r047c/R047C_CROSS_ARM_REPLICATION_MATRIX.json`
- `research/r047c/R047C_NEW_GENERATION_QUESTIONS.json`
- exact checker/tests for all machine-checkable bridge/calibration claims.

## 12. 返回必须回答

1. 12 个 frozen candidates 中，哪些完全无法合法接到 KENG？
2. 哪些只有 E1/E2 的结构潜力，哪些真正达到 E3/E4？
3. 是否有任何 candidate 达到 E5 cross-KENG shared explanation？
4. 如果没有，缺失的最小 native structure 是什么？只记录，不修改 candidate。
5. 是否出现 project/isolated independent rediscovery + calibration convergence？
6. Pareto frontier 是谁，为什么？
7. 是否存在 strict dominance；如果没有，不选赢家。
8. 哪些 candidate 失败揭示了下一代机制应新增的 native-side necessity？
9. classical pi 数值在整个 calibration 中是否完全没有被用作 selection loss？必须给 machine-auditable YES/NO。

## 13. 成功边界

强成功不是“找到一个最像经典数学的 candidate”。

强成功是：

> 一个 blind-frozen native mechanism，在不复制 effective definitions、不过度增参、不过度定制 bridge 的情况下，对多个独立 KENG engineering constraints 给出可冻结、可 holdout、跨尺度的解释。

如果 12 个 candidates 都做不到，任务仍然成功：它应返回 precise missing-native-structure frontier，为下一代 blind generation 提供 native-side necessity，而不是偷偷修当前 candidate。

**Return target:**

`FROZEN_NATIVE_CALIBRATION_COMPLETE / EXPLANATORY_DEBT_CLASSIFIED / CROSS_ARM_BLIND_EVIDENCE_AUDITED / NEXT_GENERATION_FRONTIER_EXPOSED / NOT_CANONICAL`
