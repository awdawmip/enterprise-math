<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "title": "旧残差基准的严格匹配六维立体重算：传播、响应与逸散",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "旧残差子集的严格匹配X6重算已完成，summary PASS：4加权、6相关、3原振荡及2隐藏响应对照各128步，共1920个完整矩时点；旧标量与平面概率律匹配，完整CWM count/dominant按细化因子变化。128步平面已归零时仅约0.0165699%完整X6归零；rho=-1偶数步完整MSD=5n/6；rho=-1/2旧n*gamma趋+2而完整n*C6趋-11/32；同一旧阻尼响应可有隐藏有界/扩散/指数增长。原生X均为整数±Ei，响应Z/W另型；无唯一原生核、N0或引力结论。",
  "next_action": "从commit 8770476e36a10e79e6b03bdc67af3b5d8d106169恢复已完成严格匹配重算及交叉审查，评阅条件返回、相关四阶桥和隐藏响应不可辨识边界。旧参数、时钟和输出概率律与原生细化/响应程序分别保留；不默认重跑已完成单元，仅在具体新模型、数据、真实核或晶包层映射依据出现时有界恢复。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/src/enterprise_math/brc_transport.py",
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/research_notes/BRC_TRANSPORT_RESIDUAL_EXTRACTED_RESULT_20260919.md",
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/native_semantics_admissibility.json",
    "https://github.com/awdawmip/enterprise-math/blob/8946bbba19f1f8589ef8c2d0d69f1b6a84e4e84e/experiments/brc_model_benchmark_20261002_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/8946bbba19f1f8589ef8c2d0d69f1b6a84e4e84e/experiments/brc_model_benchmark_20261002_fca717/results.json",
    "https://github.com/awdawmip/enterprise-math/blob/8946bbba19f1f8589ef8c2d0d69f1b6a84e4e84e/experiments/brc_model_benchmark_20261002_fca717/METHOD_AUDIT.md",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/results.json",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/METHOD_AUDIT.md",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/run_spatial_decay.py",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/summary.json",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/run_all.py",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/RELATED_BRANCHES.md",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/GRAPH_BOUNDARIES.md",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/DYNAMICS_REVIEW.md",
    "https://github.com/awdawmip/enterprise-math/blob/3843e27cdf5d7cabd38836bc165f619a8ab9a2ad/experiments/brc_native_x6_residual_20261002_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/3843e27cdf5d7cabd38836bc165f619a8ab9a2ad/experiments/brc_native_x6_residual_20261002_fca717/run_x6.py",
    "https://github.com/awdawmip/enterprise-math/blob/3843e27cdf5d7cabd38836bc165f619a8ab9a2ad/experiments/brc_native_x6_residual_20261002_fca717/results.json",
    "https://github.com/awdawmip/enterprise-math/blob/3843e27cdf5d7cabd38836bc165f619a8ab9a2ad/experiments/brc_native_x6_residual_20261002_fca717/PROJECTION_REVIEW.md",
    "https://github.com/awdawmip/enterprise-math/blob/3843e27cdf5d7cabd38836bc165f619a8ab9a2ad/experiments/brc_native_x6_residual_20261002_fca717/CELL_SEMANTICS.md",
    "https://github.com/awdawmip/enterprise-math/blob/3843e27cdf5d7cabd38836bc165f619a8ab9a2ad/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.md",
    "https://github.com/awdawmip/enterprise-math/blob/3843e27cdf5d7cabd38836bc165f619a8ab9a2ad/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.en.md",
    "https://github.com/awdawmip/enterprise-math/blob/3843e27cdf5d7cabd38836bc165f619a8ab9a2ad/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json",
    "https://github.com/awdawmip/enterprise-math/blob/8770476e36a10e79e6b03bdc67af3b5d8d106169/experiments/brc_x6_replay_20261002_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/8770476e36a10e79e6b03bdc67af3b5d8d106169/experiments/brc_x6_replay_20261002_fca717/summary.json",
    "https://github.com/awdawmip/enterprise-math/blob/8770476e36a10e79e6b03bdc67af3b5d8d106169/experiments/brc_x6_replay_20261002_fca717/run_all.py",
    "https://github.com/awdawmip/enterprise-math/blob/8770476e36a10e79e6b03bdc67af3b5d8d106169/experiments/brc_x6_replay_20261002_fca717/CORRELATED_REPLAY.md",
    "https://github.com/awdawmip/enterprise-math/blob/8770476e36a10e79e6b03bdc67af3b5d8d106169/experiments/brc_x6_replay_20261002_fca717/OSCILLATION_REPLAY.md",
    "https://github.com/awdawmip/enterprise-math/blob/8770476e36a10e79e6b03bdc67af3b5d8d106169/experiments/brc_x6_replay_20261002_fca717/CROSS_REVIEW.md",
    "https://github.com/awdawmip/enterprise-math/blob/3313540155c62e9adfa2e0c3ce65ebb96f0ce2b6/AGENTS.md",
    "https://github.com/awdawmip/enterprise-math/blob/3313540155c62e9adfa2e0c3ce65ebb96f0ce2b6/research_notes/BRC_NATIVE_X6_SEMANTIC_ALIGNMENT_20261002_9D72AC.md",
    "https://github.com/awdawmip/enterprise-math/blob/3313540155c62e9adfa2e0c3ce65ebb96f0ce2b6/p000_reality_foundation.json"
  ],
  "evidence_status": "STRICT_MATCHED_X6_REPLAY_COMPLETE_SUMMARY_PASS_WITH_NONUNIQUE_REFINEMENT_AND_TYPED_RESPONSE_BOUNDARIES",
  "last_progress_ref": "https://github.com/awdawmip/enterprise-math/blob/8770476e36a10e79e6b03bdc67af3b5d8d106169/experiments/brc_x6_replay_20261002_fca717/REPORT.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "six-dimensional-solid-X6",
    "strict-baseline-replay",
    "matched-old-output-laws",
    "nonunique-refinement",
    "primitive-integer-neighbors",
    "typed-response-field",
    "completed-direct-research"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "parent_objective_id": "BRC-BASELINE-RESIDUAL-LAWS",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "BRC",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:2c37dc6decc8e7c5c2fa6784666bd3067bc9ab7bc5d38155bde44f05bdb79945",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 旧残差基准的严格匹配六维立体重算：传播、响应与逸散

Status: V2 task registration; execution authority is separate; completed matched-X6 direct research is tracked by its activity and verified source.

沿用 `RS-BRC-BASELINE-RESIDUAL-20261002` 与 `DIRECT_USER_DIRECTION`，supersede `TP2-BC004F331F91F6ED4C14`。响应用户选择旧残差研究、按完整六维立体重算的明确要求；旧 taskbook、record 和报告字节不改。本代仅登记已完成研究，不追溯授予 CLAIM、Driver 接受或 N0。

## 0. Mother question

严格保留选定旧基准的参数、零初值、时钟与标量/平面输出概率律，在完整六维原生传播和六分量响应中重算残差：哪些旧归零或衰减掩盖完整位移、高阶结构与隐藏响应？本轮得到三个有界对照：读出归零可隐藏原生位移，标量与完整六维四阶量可异号，相同全部旧振荡响应无法唯一决定隐藏响应稳定性。独立加权支路的有效独立次数关系在所选对称扩展中保留。不是从旧数据识别出了唯一原生逸散律，也不是重新发现既有概率论定理。

## 1. Frozen inputs and scope

当前入口依据 main commit `3313540155c62e9adfa2e0c3ce65ebb96f0ce2b6` 的 `AGENTS.md` 与 `research_notes/BRC_NATIVE_X6_SEMANTIC_ALIGNMENT_20261002_9D72AC.md`：P000 已固定原生六维离散 Cell 空间、单独时间，空间维数不是本轮待证明、证伪或再次确认的对象。低维概率律匹配只在本报告声明的完整状态—读出桥及未来范围内使用；不删除未经保真证明可删的联合关系、路径来源或相关性。本次仅更新入口约束与引用，不改变已完成数学内容、数值或作者归属。

### 来源、用语与类型

最终研究源为 commit `8770476e36a10e79e6b03bdc67af3b5d8d106169`，目录 `experiments/brc_x6_replay_20261002_fca717/`。父执行已将 14 文件真实全文读取并逐字匹配；本修订直接读取最终 `REPORT.md` 与 `summary.json`，后者为 PASS。不可变报告、summary、运行入口、相关/振荡推导及交叉审查链接在 frontmatter。

严格采用用户术语：立体是完整六维原生 X6；三维是其中一层晶包，任意三轴或二维读出不自动定义完整层；时间单独记录。原生位移 `X in Z^6` 每个基本步只为 `+/-E_i`。权重、衰减和有理旋转作用于同路径驱动的六分量响应 `W/Z`，不把响应值称为原生 Cell 地址。支路质量为正，坐标符号与质量分开。

### 实际重算的旧模型子集

- Source `46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c` 的 `related_branches.py`：四组独立权重 `1,j,(3/4)^(j-1),(4/3)^(j-1)`；六组旧符号相关系数 `-1,-1/2,0,1/2,3/4,1`，均至 128 步。
- 同 source 的 `dynamics_types.py`：旧旋转 `R=[[3/5,-4/5],[4/5,3/5]]` 与 `c=3/4,1,4/3`；另有两种隐藏响应对照，与原阻尼项构成相同旧观测、不同隐藏稳定性的比较。
- Source `b7bec0be19987620eb77e7e72122c79e557aeb1a` 的 `run_spatial_decay.py`：旧 `d=1,2` 单位轴概率律，以同一个完整六轴 iid 程序保留两个旧读出，精确返回查询延伸至 128 步。

实际导入并重算旧函数，旧文件未改；没有声称全部旧类型都已重做。新增明确假设是：每次旧正负创新独立均匀路由到六轴，路由独立于完整相关符号过程；振荡则由同一整数原生创新驱动六分量响应。六维扩展不唯一，不把某选定程序说成旧模型唯一或无损的原生恢复。

### 匹配强度与完整状态

旧标量为 `S=sum_i X_i`，逐路径保持旧符号累加。旧平面读出为 `U X=(X1+X3+X5,X2+X4+X6)`；iid 十二方向经 U 推为旧四方向各 `1/4`。U 是此经典基准的读出，不冒称 STAR 或晶包层选择。

每个旧标量词有 `6^n` 个原生轴词，每个旧平面词有 `3^n` 个。概率推前相等，CWM 的 count 乘细化因子、dominant 除该因子，故保持旧概率律不等于完整 CWM 三元组不变。实际短深度端点合并亦核对这些等式。

保留完整六轴核、隐藏符号/控制状态、完整响应协方差，以及同一创新驱动的 `(X,Z)` 交叉协方差。满六坐标计算不保证协方差永远满秩；严格交替的偶数步协方差为秩 5，不能误称秩 6。原生位移、响应幅度、返回事件和标准化高阶收缩分别定义，不互相替代。

### 已完成的核心结果与边界

1. **返回事件不同。** 第 128 步旧平面已归零时，完整 X6 同时归零的比例约 `0.0165699%`，约 `99.9834%` 仍有非零原生位移。概率来自精确系数，不是采样估计。完整六维返回概率和有限、两个旧读出和发散，报告结合既有随机游走原理区分暂留/常返，不声称发现新概率论定理。`p6/p2` 的反平方自变量是半时间，不能换成距离或引力。
2. **相关符号桥。** 旧 `V=Var(S)` 与 `kappa_S` 给完整 `Sigma6=nI/6+(V-n)J/36`、`MSD=(5n+V)/6`、`K6=(kappa_S-10n)/36`。`rho=-1` 偶数步旧 S 恒零，完整 MSD 为 `5n/6`；`rho=-1/2` 旧 `n*gamma` 趋 `+2`，完整 `n*C6` 趋 `-11/32`。这不是旧标量算错，而是对象/收缩改变。所有混合参数的渐近负号与六个实际参数的有限时点核验分开，不推成所有有限参数定理。
3. **隐藏响应不可辨识。** 旧 `Y_next=cRY+eta` 保持不变，完整响应 `Z_next=AZ+xi` 与原生位移 `X_next=X+xi` 另型。旧阻尼 `c=3/4` 下三种匹配响应程序分别给隐藏响应有界、线性增长、指数增长；旧全部响应及未来序列相同。三者原生 X 仍是同一六轴随机游走，不能把隐藏响应指数增长称为原生 Cell 指数扩散。
4. **保留有效独立次数关系。** 所选独立加权响应满足 `C6=-1/(3*N_eff)=旧标量gamma/6`；四组原生 `E||X||^2=n` 均相同。权重改变响应宽度/高阶量，不自动改变原生位移逸散律。

这些结论来自声明的完整核与响应程序，不解决唯一真实核、一般晶包层选择、全局载体桥或地址 codec 的未定问题。没有依据支持所有类型共享单一指数。

## 2. Hard target and required outputs

本轮有限重算、严格匹配及交叉核验已完成。统一复现入口为 `python experiments/brc_x6_replay_20261002_fca717/run_all.py`。全套使用 Fraction 精确算术，展示图才转浮点，无随机采样或学习拟合。

- 加权 4 组、相关 6 组、振荡 5 组各至 128 步，共 1920 个完整矩时点；不是 1920 个独立实验。
- 加权、相关分别比较 512、768 个旧标量参考行；相关模块另有 768 个独立径向闭包核验，保留 64 个旧归一化未定义时点。
- 振荡模块 45,275 项精确断言，包括完整协方差、响应核、旧源码采样行和联合 `(X,Z)` 交叉协方差。
- 共同 iid 极限在 9 个时点核验 18 个精确跨模块等式。
- 完整端点/CWM 分别核至加权联合 3 步、相关隐藏状态 4 步、振荡联合 3 步、返回过程 6 步。返回过程有 10,363 个端点观测、70 次精确系数查询，其中包含全部 64 个偶数时点至 128 步。

详细计数保留于 summary，各计数有重叠，不相加为独立实验。长期运用已证明闭包/响应核系数，不宣称枚举 `12^128` 路径。代码实际复用生产矩/CWM 模块及既有端点系数工具；数学模型证明、有限实现检查和独立交叉审查分层。研究内审查不是正式 Driver 接受。

交付为上述 14 个已核验源文件；主报告、代码、三个结果 JSON、summary、推导、交叉审查与图均保存。当前恢复从该归档开始，不默认重跑整个旧矩阵。

## 3. Research value to preserve

在旧输出概率律严格保持的前提下，识别完整六维传播与响应中新出现的信息，排除“同时换模型/时钟”造成的假发现。条件返回、相关四阶异号和隐藏响应稳定性不可辨识分别解释了读出能丢失什么；匹配后保持的有效独立次数关系也应保留。不唯一扩展是结论的一部分，而不是以某一程序代替真实原生规律的理由。

## 4. Success, kill, and return criteria

本轮有限重算完成并归档：实际旧代码/参数/时钟/输出概率律得到核对；原生 Cell 步合法；完整响应与联合信息保存；CWM 细化与概率保持分开；零、负号变化、未定义指标和不可辨识反例完整返回。所有计数按最终 summary，不新增未执行项目。

Kill/no-go：更换旧模型而不披露；只匹配低阶矩就称完整旧概率律相同；将 CWM 概率质量相同写成所有三元组相同；把响应旋转/缩放当原生位移；隐藏宏时钟；只存对角方差；把任意三轴称完整层；把六维扩展认作唯一；把返回的时间指数改称空间力律；把重复旧理论当新数学发现。

后续从当前已完成前沿审阅，或在具体新数据、模型、真实核或层映射依据出现时有界恢复。不自动无限增加验证，不默认重跑已完成单元。保持六维立体、三维晶包层和时间另记的约束；publication 不授予 CLAIM、Driver 接受、N0 或物理规律。
