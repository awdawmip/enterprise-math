<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-P32-FIXED-ODD-PORT-WIDTH",
  "title": "32位具名单比特轨迹的固定奇模双端口最优位宽",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "20位已有全域可逆构造，任何18位方案均因容量不足而失败。19位方案的可逆性未定。PREFIX-874、881、897、902、903等保存的证据存在重叠，903的显式并集仅是全部已知排除的一部分。",
  "next_action": "对齐874与903的有序模数域及碰撞见证语义，用已保存判据识别尚未覆盖、最可能改变19/20结论的族。之后择可复算的构造、排除证明或反例路线推进。",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@ced7ed3ee59f16390046a5f56c7ff34ed4d0fcd8:research_notes/portable_direct/2026-11-17_r6_prefix870_balanced_gcd_exact_odd_p33_to_p55.md",
    "awdawmip/enterprise-math@a580bb6310cb307f4513f8fbb11c975ca5c2a4fe:research_notes/portable_direct/2026-11-17_r6_prefix871_even_p64_to_80_and_gcd_fiber_capacity.md",
    "awdawmip/enterprise-math@f4f8386b37d4413a548199d490dc9f55e70f2ec1:research_notes/portable_direct/2026-11-17_r6_prefix874_sparse_gap_collision_family.md",
    "awdawmip/enterprise-math@dfea6068620584beee528a6c54093f79b1f6b62a:research_notes/portable_direct/2026-11-18_r6_prefix881_complete_collision_dp_characterization.md",
    "awdawmip/enterprise-math@e7f1915d803f318662796f3ad692179c229a6a57:research_notes/portable_direct/2026-11-18_r6_prefix902_third_panel_192_row_union.md",
    "awdawmip/enterprise-math@1425c5f94c9fe9c228b5f270262b7e373f87da77:research_notes/portable_direct/2026-11-18_r6_prefix903_dyadic_gap_uniform_collision.md"
  ],
  "evidence_status": "AUTHOR_PROOFS_AND_FINITE_CERTIFICATES_SAVED; 19_BIT_GLOBAL_INJECTIVITY_OPEN; INDEPENDENT_REVIEW_PENDING",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "NAMED_XOR_TRAJECTORY",
    "TWO_FIXED_ODD_MODULI",
    "OPTIMAL_PORT_WIDTH"
  ],
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-P32-FIXED-ODD-PORT-WIDTH",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION"
}
-->

# 32位具名单比特轨迹的固定奇模双端口最优位宽

设 $N=2^{32}$。允许的具名有向轨迹为零步 $(x,x)$ 或 $(x,x\mathbin{\mathrm{XOR}}2^i)$，其中 $0\le x<N$，$0\le i<32$。两个预先固定的正奇模数 $a,b\ge3$ 产生的联合观察为 $(u\bmod a,v\bmod b)$。要求从两次读数对所有合法输入恢复完整有序轨迹，含起点、终点和翻转来源。峰值位宽是两个模数二进制长度的较大者。求其最小值 $B_{\mathrm{fix,odd}}(32)$。

## 已有数学依据

总轨迹数为 $33\cdot 2^{32}=141733920768$。PREFIX-870 给出20位可逆构造 $(536469,536603)$，也证明用两模数的公因子余数差单独辨认全部有符号增量的方法需要20位。19位任意解码器的可行性仍然开放。若任一奇模数低于262145，另一至多524287，其积小于轨迹数，可直接排除。故19位只需考察 $Q=\{262145,262147,\ldots,524287\}$ 的 17,179,869,184 个有序对。

PREFIX-874 已对模数差为两个二幂之和、差或单个二幂给出统一碰撞。PREFIX-881 给出对固定参数的完整碰撞判据。PREFIX-903 加强了二幂差的见证，使两条轨迹可翻转同一具名位；其相对 PREFIX-902 的增量为2,336,712个有序对。其报告的明确并集覆盖7,617,211,750组，余9,562,657,434组在该并集之外；此前的其他排除定理可能已经覆盖其中一部分。各项作者证明、证书及可执行程序见上述固定来源。

## 科学目标与验收

若19位可行，给出一个确定的有序模数对及覆盖整个合法轨迹域的单射证明或完整可核验证书。若19位不可行，给出覆盖全部候选域的碰撞存在性证明或可复算的有限覆盖证书；既有20位构造由此给出最优值。可自由采用联合余数构造、解析排除、有限分类或其组合。允许报告确实推翻既有论据的新反例并给出准确修正。

部分结果应记录新增见证、定理或确切覆盖范围、交叠与尚未决定的集合。统计统一使用有序模数对，区分“模数对的覆盖数”与“一个模数对中的碰撞轨迹对数”。复用现有检查器与已证明的整族判据，保留复算所需的定义、输入、输出和必要的有效范围。核查较小实例可以检验实现；全域判定需要对应强度的证明或完整证书。

## 与现有工作的关系

此任务整合独立 PREFIX 科学工件，把尚未正式登记的32位阈值作为一个两种答案均可成立的问题。它服务于几何/BRC 母目标的观察相对最小记忆分支。这里的两端余数是有类型的辅助观察；其结论只涉及给定的有限轨迹和固定模数，不会直接给出 X6 原生时间动力学定律。已有任务中的原生时间、未来操作下的线性商，以及半素数端点恢复分别采用其他对象和判据。
