<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "title": "BRC 残差六维立体原生 X6 计算：三维晶包层、隐藏深度与平面读出",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "用户选定六维立体原生X6主计算、时间另记的有界诊断已完成并归档：三个声明核分别为全六轴扩散、质量半衰、双拍驱动，均保留满秩6×6协方差；它们不是旧平面模型的无损lift。完整均匀核K6=-t/3而STAR径向Kcar=0；rank2双深度隐藏模式及跨轴条件future反例PASS。旧11类结果保留声明维数/截断范围，不等同full6；一般晶包层选择、全地址codec与唯一真实核仍未解决，无正式CLAIM/Driver接受/N0或引力结论。",
  "next_action": "从commit 3843e27cdf5d7cabd38836bc165f619a8ab9a2ad恢复已完成X6程序、结果和独立审查，按六维立体、三维一层晶包、平面声明读出的用户术语评阅适用边界。保持六轴联合状态与完整协方差、时间另记；不凭三轴认完整层。仅在真实传播核、一般层选择映射、全局载体桥或地址codec有新依据时有界恢复，不自动无限继续。",
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
    "https://github.com/awdawmip/enterprise-math/blob/3843e27cdf5d7cabd38836bc165f619a8ab9a2ad/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json"
  ],
  "evidence_status": "FULL_X6_DECLARED_KERNEL_DIAGNOSTICS_COMPLETE_SOURCE_VERIFIED_LAYER_CODEC_TRUE_KERNEL_UNRESOLVED_NO_CLAIM_DRIVER_ACCEPTANCE_OR_N0",
  "last_progress_ref": "https://github.com/awdawmip/enterprise-math/blob/3843e27cdf5d7cabd38836bc165f619a8ab9a2ad/experiments/brc_native_x6_residual_20261002_fca717/REPORT.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "six-dimensional-solid-native-X6",
    "time-separate",
    "three-dimensional-crystal-packet-layer",
    "full-covariance",
    "hidden-depth",
    "conditional-future",
    "scope-correction",
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
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# BRC 残差六维立体原生 X6 计算：三维晶包层、隐藏深度与平面读出

Status: V2 task registration; execution authority is separate; completed full-X6 direct-research diagnostics are tracked by their activity and verified source.

沿用 `RS-BRC-BASELINE-RESIDUAL-20261002` 与 `DIRECT_USER_DIRECTION`，按用户明确修正的方法和术语 supersede `TP2-C8ACA99CAEFA8E281E3E`。旧 publication、taskbook 与报告字节保留。本代登记已完成的有界六维诊断和准确适用边界，不创建正式 CLAIM，不追溯授予 Driver 接受或 N0。

## 0. Mother question

用户明确选择“直接按完整六维原生空间计算”，并规定进取数论中六维才是立体，三维是该六维立体世界的一层晶包。即使经典模型只有平面定义，BRC 残差也在完整六维立体原生 X6 中计算，时间单独记录，然后作明确映射下的平面读出。

本轮完成检验：选定读出会隐藏原生平方残差，特定四阶读出甚至恰好为零，而完整六维结构非零；隐藏坐标还可能通过声明的条件程序改变未来读出。结果依赖指定核和观测，未证明所有程序都必然非零逸散，也未从六维推出反平方、引力或唯一真实传播律。

## 1. Frozen inputs and scope

### 用户术语与保留边界

- **立体**：完整六维原生 X6；时间不是第七条空间轴，另行记录。
- **三维**：六维立体世界中的一层晶包，不与立体互换，也不一概简化为 observer。
- **平面**：声明映射下的读出。任意三轴限制、三坐标投影或双共同深度程序不自动构成一个/两个完整晶包层。用户命名纠正没有新增一般层选择算子。

旧三类基准、尺度/壳平均和后续 11 类机制结果保留各自原始状态维数、截断、参数与指标；11 类仍包含控制，不是独立盲实验数。这些结果不能代替完整六维立体残差。本轮补充其适用范围，不追改旧已存证材料。

### 不可变本轮来源

父执行已将八个文件保存于 commit `3843e27cdf5d7cabd38836bc165f619a8ab9a2ad`，并经真实全文件读取逐字匹配：

- `experiments/brc_native_x6_residual_20261002_fca717/REPORT.md`
- 同目录的 `run_x6.py`、`results.json`、`PROJECTION_REVIEW.md`、`CELL_SEMANTICS.md`
- `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.md`、`.en.md`、`.json`

完整不可变链接在 frontmatter `source_refs`。主报告为当前数学范围与术语的依据；世界定义仅按用户指令同步命名，数值维度仍为六轴加独立时间。研究活动为 `RA-BRC-BENCHMARK-20261002-FCA717`。

### 实際内态与读出

主状态是相对选定 Cell 的六个有符号原始坐标 `X_t in Z^6`，另保留时间/相位、正支路质量与相关控制态。完整均值有六项，协方差保留 `6×6` 全矩阵及交叉项，先在六维传播再读出。raw coordinates 不伪装成未注册的最终 Cell 地址；六坐标或协方差也不被声称包含全部支路来源/晶包内部状态。

已有原生 STAR 载体读出扩写为 `P X=(x1-x3,x2-x3)`，其核为四维。对于 `Qcar(u,v)=u^2+v^2-u*v`，完整平方读数分解为可见项 `(2/3)Qcar(PX)` 与隐藏项 `(x1+x2+x3)^2/3+x4^2+x5^2+x6^2`。这只是原始分量的代数分解，不改变 `PERP_E/120°` 的原生语义，不把平方项称为物理能量。正确读出度量与完整协方差须一并保留，不能只取投影矩阵的普通迹。

明确见证可有后三轴恰为零；这不是对未知内态默认补零。三维晶包层的选择与完整性仍须另外有定义，不能由该 STAR 或三坐标限制冒认。

### 三个实际完成的满秩六轴声明核

每个原始时间步只走一个 `+/-E_i`，所有六轴均有正概率参与。概率、衰减与相位规则属于本轮冻结的诊断程序，不是唯一规范原生心跳律。

| 基准 | 声明的六轴程序 | 完整结果 |
|---|---|---|
| 扩散 | 十二方向各 `1/12` | 质量 1，均值 0，`Sigma_t=(t/6)I6`，完整均方残差 `t` |
| 质量半衰 | 十二方向未归一化权重各 `1/24` | 质量 `2^(-t)`，条件分布同上，条件完整均方 `t`，未归一化平方读数 `t*2^(-t)` |
| 双拍驱动 | `p_t(dx)=[1+s_t(h·dx)/2]/12`，交替 `s_t=+/-1`，`h=(1,-1,1,-1,1,-1)` | 六维均值奇拍 `h/12`、偶拍 0；`Sigma_t=t[I6/6-hh^T/144]`，完整中心平方残差 `23t/24` |

质量半衰不是旧坐标收缩模型，双拍驱动不是旧旋转模型的无损提升。平面经典数据不唯一决定六维核、均值或隐藏分量；本表明确声明这些选择。

均匀扩散下，以原生平方读数收缩定义的完整四阶结构 `K6=-t/3`，标准化后 `-1/(3t)`；同一六维过程的 STAR 载体径向量 `Kcar=0`。所选 STAR 可见平方项只占完整均方的 `1/3`，其余 `2/3` 在读出核中。此零依赖核及读出指标，不意味着平面高斯、完整残差为零或所有指标同样失真。双拍基准则保留非对角协方差，完整四阶收缩 `-83t/288`。

### 已完成隐藏状态对照

双共同深度程序每周期选择两个独立符号；前三个原始步同符号依次走 `E1,E2,E3`，后三步另一个同符号依次走 `E4,E5,E6`。周期是六个原始步，控制态不能在步间删除。`n` 周期后协方差为 `n*diag(J3,J3)`，轴方差均为 `n` 但秩只有 2，原生均方 `6n`；STAR 在周期末回零而周期内前两步可见。它是对照，不替代满秩主基准，不自动定义两个完整晶包层。

条件未来反例以完整初态 `+e4` 和 `-e4` 开始，当前 STAR 与前三坐标读出相同。声明正质量程序按 `x4` 符号分别走 `+E1` 或 `-E1`（零时走 `+E2`），下一 STAR 读出分别为 `(1,0)`、`(-1,0)`。该状态依赖条件程序使用端点 CWM，不冒称固定仿射包的无条件矩闭包。独立均匀核可以有闭合平面边缘；这不表示完整立体残差由平面决定。

## 2. Hard target and required outputs

本轮有界诊断、代码核验与研究内审查已经完成，以下为当前完成证据与恢复边界：

- 三个满秩主基准共 192 个完整六维矩传播时点，至 `t=64`；31,089 个 CWM 端点观测和 145,548 条原始边检查。
- 18 个完整分布四阶核验、4 个独立完整词枚举层（至 4 步）、41 个六变量系数查询（含 64 步远期端点）。
- 双深度对照另完成 64 个矩时点、4,896 条原始边及 284 个精确端点 CWM 三元组。
- 数学脚本全部精确断言通过，现有世界接口 6 项 unittest 通过；无须安装额外依赖，生产数学模块未改。

计数是重复时点上的实现检查，不是独立实验数。完整端点按六维键核验至第 6 原始步；均匀核联合律由六变量生成式 `[sum_i(s_i+s_i^-1)/12]^t` 保留，支持精确端点系数查询。64 步低阶矩与四阶收缩采用已证明适用的精确压缩，不宣称枚举全部 `12^64` 条路径。

代码复用 `brc_transport.Affine`、`EffectHistogram.moment_action`、`MomentState` 与 `brc_weighted` 正质量 CWM。最终源含主报告、运行代码、结果、独立投影推导/代码审查及 Cell 语义核对；研究内审查不等于正式 Driver 接受。复现入口为 `python experiments/brc_native_x6_residual_20261002_fca717/run_x6.py`。

一般晶包层选择映射、全局载体桥、唯一真实传播核和完整最终地址 codec 没有因本轮诊断通过而建立。raw-coordinate 程序可执行与这些未定接口同时成立；三份世界定义的术语同步也不替代缺失数学接口。

## 3. Research value to preserve

纠正“平面补成三维即可完成立体残差”的范围错误，用完整六轴联合计算展示读出丢失当前平方量、高阶结构与条件未来的三种不同方式。保留满秩主核、秩 2 隐藏模式、完整交叉协方差与精确生成式之间的区别，同时标注实验核、用户术语与未定原生接口的来源边界，使后续能够从正确六维前沿恢复。

## 4. Success, kill, and return criteria

本轮有限诊断已完成并归档：完整六维内态与协方差实际推进；三个声明主核满秩；双深度对照未冒认满秩或完整晶包层；条件未来反例与独立均匀核的闭合边缘分开；代码、生成式、精确检查和研究内审查均有来源；未定接口没有伪装解决。

Kill/no-go：把三维称为立体；把一层晶包一概化约为 observer；将任意三轴限制当完整层；先算低维再补零；只保存单轴方差；把宏周期回零写成每步不变；把相同投影当相同完整状态；把诊断概率/耦合当唯一真实核；把 raw-coordinate 程序说成完整地址 codec；把旧模型称为本轮三核的无损提升；从六维或某个 `1/t` 指标推引力。上述做法均不受本轮证据支持。

下一步从不可变源评阅本轮完成前沿与边界，不默认重跑旧矩阵或无限继续。只有真实传播核、一般晶包层选择、全局载体桥或地址编码出现具体新依据，才在用户范围内有界恢复。六维立体、三维晶包层、平面声明读出及单独时间的约束持续适用；publication 不授予 CLAIM、Driver 接受、N0 或数学/物理真理。
