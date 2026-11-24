<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-POWER-CERTIFIED-RESIDUAL-LATTICE-20261124",
  "title": "特殊算术残差格的保根构造与认证精度成本",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "现有格原型存在尺度判定、保根与势函数语义缺口；特殊算术关系下的合法压缩、所需精度及完整认证成本尚无可靠结论。",
  "next_action": "在完整保根关系或明确整数基上提出可检验的结构性精度/压缩问题，给出其正确性条件与全成本比较。",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "parent_objective_id": "OBJ-POWER-RESEARCH-TRANSFER-20261124",
  "parent_objective_generation_id": "OG-F544DAB4BAD84437CB9D",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-POWER-CERTIFIED-RESIDUAL-LATTICE-20261124",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "POWER_TRANSFER",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/src/power/lattices/lll.py",
    "https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/src/power/weapons/provably_exact_adaptive_float_lll.py",
    "https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/src/power/weapons/asymptotic_high_bit_projected_bkz.py",
    "https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/src/power/weapons/schnorr_euchner_deep_insertion_lll.py",
    "https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/docs/79_ASYMPTOTIC_HIGH_BIT_PROJECTED_BKZ_MONOGRAPH.md",
    "https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/docs/83_SCHNORR_EUCHNER_DEEP_INSERTION_LLL_MONOGRAPH.md",
    "https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/docs/84_PROVABLY_EXACT_ADAPTIVE_FLOAT_LLL_MONOGRAPH.md",
    "https://perso.ens-lyon.fr/damien.stehle/FPLLL.html",
    "https://arxiv.org/abs/cs/0701183",
    "https://arxiv.org/abs/1307.7534",
    "https://github.com/awdawmip/chatgpt-global-knowledge/blob/ae6894814c8637560bd1e1d4b6dbc0131ddbc788/journal/power/2026-11-24/20261124T190334%2B0800-power-source-review-5561f5a.md"
  ],
  "evidence_status": "INFORMED_SOURCE_REVIEW; PROSPECTIVE_QUESTION; NO_NEW_MATHEMATICAL_ACCEPTANCE",
  "hard_block": null,
  "tags": [
    "POWER",
    "joint-residual",
    "user-directed-research"
  ],
  "claim_lease_minutes": 180
}
-->

# 特殊算术残差格的保根构造与认证精度成本

#### 目标与对象

研究特殊算术残差格中低精度决策、必要残差保存与精确认证的配合，并使输入格保持原始多项式关系和目标根。输入明确给定整数格或多项式、模数、变量界和已知同余信息来源；原基、尺度、联合系数及必要来源属于完整关系状态。

可从

\[
f(x,y)=(p_0+Mx)(q_0+My)-N
\]

及可明确接入的关系族出发。多项式到格的编码与格上的数值归约是两个可独立推进的子问题，共享正确性实例和成本账。

#### 已有可复用基础

- [精确有理 LLL](https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/src/power/lattices/lll.py) 可作小规模对照。
- [84 号浮点原型](https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/src/power/weapons/provably_exact_adaptive_float_lll.py) 保留整数基并尝试浮点建议和回退。
- [83 号深插实现](https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/src/power/weapons/schnorr_euchner_deep_insertion_lll.py) 有精确有理 Gram–Schmidt，可比较操作选择。
- 已有 L²、reducedness 认证与 PotLLL 是可复用方法。新增贡献落在本项目结构、精度需求、保根压缩或实际成本上。

#### 具体增量与成果验收

研究行尺度、稀疏关系、取消误差与决策间距对精度需求的影响；寻找局部且可组合的认证证据。对输入格，研究完整系数和单项式位置的保留、合法行变换、移位选择及压缩收益。已有误判和丢根反例直接作为校正依据。

交付声明范围内的正确构造或算法、成立条件与可复算结果。精确归约需有相符的归约条件判定；格身份、根保持和归约质量分别核查。总成本计入构造、认证、回退、重新计算及同余候选获取。只有实际计时比标为时间加速；首基向量长度按其实际含义标注。有限特殊族或有效认证条件可以独立交付，不以一般整数分解突破为唯一成果标准。



### 精确来源与已知反例

原审阅给出：84号在 diag(2^60,2^59) 上未满足其声明的 Lovász 条件；79号 f-shift 遗漏线性项，N=77 的真实根例子不保留；83号的单投影深插条件并不保证文档采用的势下降。关键源码在本次固定 POWER 提交与原审阅版本之间未变。反例的参数、原计算范围和来源见审阅记录，作为校正输入复用，不记作本任务新增实验或独立验收。

本问题是未登记过的特殊结构精度/保根成本问题；现有有限关系格或 Smith 重建任务不是本任务的替代。辅助欧氏内积是明示算法载体，原生 X6 与算术关系观察保持各自类型。已有有效 LLL、L²、认证及 PotLLL 方法允许直接复用；创新强度以特殊结构的实际新结论为准。

### 研究价值与交接

将联合残差保真落到格编码和数值决策，区分合法算术压缩、可靠归约以及最终恢复的真实收益。

研究依据为上述固定源码、定义与来源。方法和具体对象选择由研究者按信息增量决定；成果按实际命题范围、正确性与可复算性验收。任务发布只保存问题，不表明领取、执行或独立科学审查。
