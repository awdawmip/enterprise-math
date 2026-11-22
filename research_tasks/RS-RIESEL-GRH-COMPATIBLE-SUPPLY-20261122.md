<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RIESEL-GRH-COMPATIBLE-SUPPLY-20261122",
  "title": "Riesel 构造的兼容同余素数供给与实际覆盖收益",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "现有覆盖、密度与有限窗口下界保留；尚无已确认既满足真实根/通道条件又能由Dirichlet-GRH同余供给改善的新通道。",
  "next_action": "从已保存的一条具体根族和覆盖通道提取实际素数条件，判断可由互素同余供给支付的部分，并研究其是否改变未覆盖类或新增成本。",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "source_refs": [
    "c2f563200a46fd4bc70ac44453c749ccd0a37bd1:research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md",
    "b2664a273150536823c6c3217732adf4cd84e784:research_notes/portable_direct/riesel_observers_20261122/README.md",
    "https://arxiv.org/pdf/1309.3595"
  ],
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "dependencies": [],
  "evidence_status": "SOURCE_BOUND_OPEN_RESEARCH",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "RH_APPLICATIONS",
    "USER_WEIGHTED_TASKSET"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-RIESEL-GRH-COMPATIBLE-SUPPLY-20261122",
  "parent_objective_id": "OBJ-RH-APPLICATIONS-WEIGHTED-20261122",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RH-APPS",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "taskset_id": "TS-RH-APPLICATIONS-20261122",
  "priority_basis": "按当前用户授权，以数学接口成熟度、可独立推进程度及预期研究价值分档。",
  "priority_weight_reference": "research_runtime_policy_v2.json#/selection_policy/priority_weights"
}
-->

# Riesel 构造的兼容同余素数供给与实际覆盖收益

对已保存 \(F_n(a)=a^2 2^n-1\) 根族与覆盖通道，寻找真正只需要互素同余素数供给的环节，并证明其带来的实际覆盖收益或有终点的搜索结论。起点包括旧素数字典、密度阶梯、固定25通道条件以及固定旧根的有限窗口下界；原作者为EM-DIRECT-970E1C，其固定根全程有限覆盖问题保留。

外部输入限定为Dirichlet-GRH及LLS同余类最小素数界：
\[
q>3,\ (r,q)=1\ \Longrightarrow\ P(r,q)\le(\varphi(q)\log q)^2.
\]
将它用到具体构造时，同时满足原根的强制因子、通道的gcd/阶和覆盖条件。\(p\equiv1\bmod d\)与\(\operatorname{ord}_p(2)=d\)分别保留；旧原始素因子存在性输入按其原有范围复用。

有效产出包括：一个兼容原条件的新通道及实际减少的未覆盖类/新增成本；明确参数族的有限搜索定理；或落实到真实候选族的障碍定理，说明为什么预期改善未实现及还缺什么关系。单独重复“必要同余不保证精确阶”不是新结果。

本任务整合外部素数供给与已有构造，不代替原固定根覆盖母问题。若没有适用的新通道，保存所检验实际条件与精确障碍即可，不能把有限检验提升为所有路线都不适用。

## 固定来源

- [research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md](https://github.com/awdawmip/enterprise-math/blob/c2f563200a46fd4bc70ac44453c749ccd0a37bd1/research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md)（c2f563200a46）
- [research_notes/portable_direct/riesel_observers_20261122/README.md](https://github.com/awdawmip/enterprise-math/blob/b2664a273150536823c6c3217732adf4cd84e784/research_notes/portable_direct/riesel_observers_20261122/README.md)（b2664a273150）
- <https://arxiv.org/pdf/1309.3595>
