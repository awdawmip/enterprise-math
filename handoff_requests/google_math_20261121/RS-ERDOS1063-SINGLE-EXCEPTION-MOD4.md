<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ERDOS1063-SINGLE-EXCEPTION-MOD4",
  "title": "单异常模4计数：非中心奇位置的结构分类",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "DRAFT",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "本轮已有无局部周期枚举的精确N_i计数及奇性判据；k=449的中心项模4为0，非中心223/225两项为奇，H449模4为2。余下重点是非中心奇位置与例外参数族的结构。",
  "next_action": "以现有局部闭式与449证据为输入，确定奇数k的非中心奇位置集合的可证明结构，并解释其对H_k模4的贡献。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/erdos-reflection.md",
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/erdos_parity.py",
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/erdos_parity.json",
    "https://github.com/awdawmip/enterprise-math/blob/7ad53ff4d8168f4800fc49270b197f14defd0b4c/research_notes/portable_direct/google_clue_deepening_20261121/erdos/THEOREM.md",
    "https://github.com/awdawmip/enterprise-math/blob/7ad53ff4d8168f4800fc49270b197f14defd0b4c/research_notes/portable_direct/google_clue_deepening_20261121/erdos/k449_full_crt.json"
  ],
  "evidence_status": "TASKBOOK_DRAFT_V2",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PENDING_PUBLICATION",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ERDOS1063-SINGLE-EXCEPTION-MOD4",
  "parent_objective_id": "OBJ-GOOGLE-20261116-ERDOS1063-SEVEN-PHASE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# 单异常模4计数：非中心奇位置的结构分类

## 来源与已完成边界

承接原作者EM-DIRECT-3DCA45的二项整除周期证明、反射奇偶分类与2026-11-16未发布提案。本轮EM-DIRECT-949983已得到局部空状态/单例计数的p进制闭式、无需枚举局部周期的全位置精确N_i算法及奇性判据。已有全CRT交叉核算，因此“计算更多H_k模4值”及“给出有限k可执行判定”已经不是未知。

设F_k(n)={0≤i<k : n−i 不整除 binom(n,k)}，n≥2k；使用已证明周期P_k=lcm(1,…,k)·lcm(1,…,floor(k/2))。N_i(k)是P_k个剩余类中F_k(n)恰为{i}的数量，H_k=∑N_i。反射给N_i=N_(k−1−i)。

对奇数k=2m+1，

\[
H_k\equiv N_m+2\sum_{i=0}^{m-1}N_i\pmod4.
\]

确切反例k=449：N224≡0(mod4)，仅N223、N225为奇数，H449≡2(mod4)。任何只保留中心项的模4规则都必须面对该反例。

## 研究目标

在奇数k≥7的范围内，研究非中心奇位置集合

\[
I(k)=\{i\ne (k-1)/2:N_i(k)\equiv1\pmod2\}
\]

的算术结构，以及它对模4计数的影响。一个具体且可证伪的待解问题是：I(k)是否总包含于中心最近邻{m−1,m+1}？若不成立，交回精确反例及说明其出现机制的修正命题；若成立，给出全域证明。该猜测来源于已核样本与现有判据，不是预设结论。

现有最近邻判据也给出独立入口：研究其参数条件的结构、可明确构造的例外族、无限性或有限性障碍。研究者可据证据选择足以实质推进分类的子问题，不需要依次完成上述两条路径，也不需强行证明无限性。若全域目标尚未闭合，需有可核验的结构定理、明确无限/有限子族或经认证反例，而非只汇报扩大扫描。

还可研究伴随的偶数分支猜测：对每个偶数k≥8，是否所有N_i均为偶数，从而H_k≡0(mod4)。该命题同样只有有限探索支持；证明或反例均为实质推进，应明确与奇数分支的适用域。

## 验收与证据

交回清楚的定理/反例、适用域和未覆盖边界；说明新结论如何压缩现有逐素数判据或确定一类k的模4值。保持中心贡献与非中心贡献的联合关系，不能只由低阶二进制外观猜结论。k=449必须正确恢复；任何新例外用原精确计数或另一个来源透明的精确方法复算。

计算可辅助发现与认证，有限搜索的最大范围据实报告，不把“范围内最小”变成全域最小或穷尽证明。数值判定算法、结构分类、经典原问题的极值结论是不同命题，分别标明。本任务不重复证明原最大异常个数定理，也不要求无关形式化作为验收前提。

原生语义继承本项目心跳世界/X6与既有整数整除观察桥；p进投影和反射轨道为辅助算术观察，保留来源与信息损失边界。方法自由，按真实数学结果与可复算证据验收，保存或发布不替代独立受理。
