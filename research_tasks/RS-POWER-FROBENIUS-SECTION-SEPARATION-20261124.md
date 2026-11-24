<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-POWER-FROBENIUS-SECTION-SEPARATION-20261124",
  "title": "循环 Frobenius 细粗层的双素数截面分离条件",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "单侧稀疏支撑不保证另一素数截面非零；尚缺明确数族的非平凡分离、环宽/种子界及可复算总成本。",
  "next_action": "在明确数族、种子与循环环宽下给出双侧系数分离或失败分类命题，并界定其相对既有短有理脊线的增量。",
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
  "registry_key": "RS-POWER-FROBENIUS-SECTION-SEPARATION-20261124",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "POWER_TRANSFER",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/src/power/factor/special_structure_factorer.py",
    "https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/tests/test_special_structure_factorer.py",
    "https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/docs/20_SPECIAL_STRUCTURE_SEMIPRIMES_MONOGRAPH.md",
    "https://github.com/awdawmip/enterprise-math/blob/f20c4ac4ab48c937f570f5193051eba733a5b563/research_tasks/ADDMUL_DELTA_FROBENIUS_DEFECT_TOWER_20260830.md",
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

# 循环 Frobenius 细粗层的双素数截面分离条件

### 目标

研究循环 Frobenius 系数的细层支撑、整除层相消和关系碰撞，在哪些明确条件下能把 N 的两个素数截面分开；获得适用于声明数族、环宽与种子的充分条件、分类或实际成本收益。重点找出超出现有近有理比值样本解释能力的增量。

### 数学对象与条件

取 N=pq，p<q 为不同奇素数，c 为满足所选种子条件的整数，R≥2。定义

    P_R(X)=(X+c)^N mod (X^R−1,N)=Σ Cᵣ Xʳ。

对 d|R，整除层投影为

    Cⱼ^(d)=Σ_(r≡j mod d) Cᵣ mod N。

模 p 的 Frobenius/Lucas 支撑约束可以控制哪些系数为零；非平凡因子提取还需要同一系数、投影和或系数关系在另一素数截面不同时消失。研究其结构条件、所需环宽、种子与粗层选择，以及两侧同时消失/碰撞饱和的失败机制。

例如，若 q=Σ aᵢpⁱ，在适用种子条件下，未合并前的支撑大小受 ∏(aᵢ+1) 控制；折叠到循环环后还须保留合并与相消。该支撑上界本身不替代模 p 与模 q 的分离证明。种子改变时使用对应的对称关系；c≠1 时不直接套用 c=1 的未加权反射等式。

### 已有基础与已知局限

- [当前实现](https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/src/power/factor/special_structure_factorer.py) 的 factor_lucas_defect_sparse 已实现细层系数 GCD、整除粗层投影和系数差批量 GCD；批量 GCD 等于 N 时可逐项分离。可复用这套精确整数计算。
- [现有测试](https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/tests/test_special_structure_factorer.py) 中两个代表样本为 q=2p+3 和 q=3p+4。旧快照局部复算确认 Frobenius 成功，同时对应 k=2、k=3 的小乘数平方差在第0步成功。因此这些样本验证已有机制的正确性，尚未提供其相对短有理脊线的独立优势。
- [专论20](https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/docs/20_SPECIAL_STRUCTURE_SEMIPRIMES_MONOGRAPH.md) 中从一侧稀疏支撑、另一侧概率说法到确定性分解的推断，需要按具体数族补足分离条件。固定小 R 的一次探测成本可为多项式；成功覆盖范围须另行确定。
- P017 的 cofactor-window separation 工具研究连续平方盆地中首因子剥离后的不同余因子窗口；它与本任务的循环系数截面分离对象不同。本轮已检查该文件，避免因“cofactor separation”同名而将其当作本任务已完成的证明。

### 真正需要取得的增量

可选择的成果包括明确构造族的分离定理、粗层相消严格增加可分离性的条件、最小可用 R 或可选种子规模的界、失败纤维的结构分类、以及能提前判断有用层的可计算特征。条件要从数族结构或可计算数据推出，不能仅把“存在一个非平凡 GCD”重述为充分条件。

若主张超出短有理脊线已有机制的收益，应声明比较的方向集合与搜索窗口。可用精确间隙

    Δ_(a,b)=ap+bq−ceil(sqrt(4abN))

衡量已有平方差方向的覆盖范围，并说明新数族在比较预算下的情况。p、q可用于离线构造和验证，求解器实际获得的输入、先验或提示应单独列明。

当尚未找到严格优势族时，明确的分离条件、失败分类或参数选择改进也可作为真实研究增量；保留“能否得到更广数族/更低成本”的开放状态。

### 验收与交付

研究者自主选择数族、证明方法、算法和参数化方式。交付应清楚说明本轮解决的具体命题及其适用条件，并保留母问题的未完成部分。

- 论证细层到粗层的映射与模素数截面行为，区分单侧零支撑、两侧相同消失以及真正非平凡分离；已有正确恒等式直接复用。
- 给出固定可复算输入、实际见证、正确因子乘积验证；若采用有限穷举，应说明范围、枚举完整性和精确算术。
- 比较实际总成本，包括环幂、层选择、投影、GCD/批量隔离、种子搜索和失败尝试；明确所用整数乘法/卷积模型或直接报告可复算操作量与计时。
- 对有加速主张的数族，以适用的现有短有理脊线、普通分解工具和相同提示条件作比较；不能仅用新方法特别容易的两个样本或“均通过”替代比较结论。
- 保存可以后续复用的数族条件、证据与最小未完成问题，不要求预定证明步骤，也不要求先解决一般整数分解。



### 与已有任务的区别

RS-ADDMUL-DELTA-FROBENIUS-DEFECT-TOWER 已研究整数 δ_p 的加法缺陷、重建与赋值结构；本题研究复合模数循环环中细/粗系数在两个隐藏素数截面上的分离，输入、成功事件和成本对象均不同。P017 的余因子窗口分离亦不等于循环系数分离。复用相关恒等式和正确精确计算，不重复把既有公式当新定理。

输入族和求解器可用先验须明确。构造或离线验证时可知道 p、q；求解阶段若使用其信息，应按实际提示计入范围和成本。原生 X6、整数及模环观察分别保留类型。

### 研究价值与交接

把已有精确系数探测推进到可复用的数族条件与失败机制，避免将概率描述或易样本等同于确定性分解优势。

研究依据为上述固定源码、定义与来源。方法和具体对象选择由研究者按信息增量决定；成果按实际命题范围、正确性与可复算性验收。任务发布只保存问题，不表明领取、执行或独立科学审查。
