<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GOV-EM-MIGRATION-BASELINE-REPAIR-20261003",
  "title": "EM 迁移 dry-run 目标状态与 no-op 幂等修复",
  "kind": "GOVERNANCE",
  "owner": "governance/ci-maintenance",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "当前迁移目标字段已到达目标；old == target == false 的字段被先判为 old/pending，错误触发不共享 exact baseline 的拒绝。根因来自当前源码只读检查，修复尚未执行。",
  "next_action": "冻结两条迁移注册、当前目标字段和 applier old/target 分类代码；在临时夹具复现目标状态被误判为 pending，修复 no-op 幂等并保留真 pending 的 exact baseline 与第三状态拒绝。",
  "dependencies": [],
  "source_refs": [
    "git:awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:.github/workflows/reference-integrity.yml",
    "git:awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:control_plane/control_semantic_migration_registry.json",
    "git:awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:control_plane/apply_registered_json_migration.py",
    "git:awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:control_plane/check_control_semantic_migration_registry.py",
    "https://github.com/awdawmip/enterprise-math/actions/runs/37036070865",
    "driver_reviews/portfolio/EM-DVR-E8DCE5/actions_followup_20261003/HANDOFF.md",
    "driver_reviews/portfolio/EM-DVR-E8DCE5/actions_followup_20261003/EVIDENCE.json",
    "git:awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:tests/test_registered_json_migration_applier_unittest.py"
  ],
  "evidence_status": "SOURCE_BACKED_CI_FAILURE; LOCAL_REPAIR_NOT_EXECUTED; NO_REMOTE_ACTIONS_AUTHORIZATION",
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GOV-EM-MIGRATION-BASELINE-REPAIR-20261003",
  "parent_objective_id": "OBJ-GITHUB-ACTIONS-CI-BLOCKER-REPAIR-20261003",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GOV-CI",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "temporary_overrides": [
      {
        "conflict_id": "TB-REMOTE-RUNTIME",
        "scope": "本CI维护任务中的workflow诊断与配置，仅本地验收",
        "reason": "用户明确要求发布这些既有CI后续事项且禁止触发Actions；敏感词属于对象/禁令而非远程运行要求",
        "replacement_behavior": "只作本地准备/测试；发布原子Git-data CAS + [skip ci]；不调用native自动Actions提交，不dispatch/rerun；不扩大网络、凭据或权限",
        "expires_when": "该有界任务终结；任何远程执行需另有明确授权"
      }
    ],
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS"
  },
  "parent_objective_generation_id": "OG-5196D92746645E3A7DF3"
}
-->

# EM 已达目标迁移 no-op 分类与精确 baseline 保护修复

## Mother question

为何已经到达目标的迁移字段仍被错误判为 pending，如何修复 no-op 幂等而保留真正待迁移字段的精确基线及 fail-closed 保护？

## Frozen inputs and scope

Source enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90；代表运行37036070865 / head84cf8737b384651c6ec5f8a69c93ed166525e0b8 的 dry-run 报 requested pending migrations do not share one exact baseline blob。工作流明确一起请求 CSM-RUNTIME-CANONICAL-DISPATCH-004 与 CSM-RUNTIME-OWNER-SCOPE-LIVENESS-006。current_control_authority 与 semantic migration registry 控制该变化；本任务不授权迁移数学语义、不等于既有 mixed字段审批。最新静态核定：两项三个目标字段均已目标；006 的 /owner_lease_is_session_liveness 是 old=false、target=false、actual=false，applier 先命中 actual==old 后将 all_already_target=False，才错误进入不同历史baseline拒绝。004与006不同旧基线本应保留。ordinary fresh_selector 仍须 tools/research_dispatch.py；不得把它改成 control router。任务收窄为 no-op 幂等分类及其必要测试；不修改历史 pins 或默认 apply 未获批准 migration。

本任务是有界 GOVERNANCE / MAINTENANCE 软件维护，仅本地验证，不领取数学研究、不授予 Owner、Steward 或数学接受权。P000 固定心跳世界原生 X6，原生“平面”不存在；时间按问题需要独立定型。本任务不改变该语义、数学真值或 Foundation 内容。仅访问获准两个仓库及现有工具，不扩网络、权限、凭据；不部署、不新建环境、不运行/重跑/dispatch GitHub Actions。

任务出版使用 canonical V2 preflight，完整 taskbook+record 通过可设置提交消息的原子 Git-data main CAS，并带 [skip ci]。不得改用已知服务器提交会自动触发 Actions 的 native publication/followup路径；保持已有授权会话，不为出版而重新注册身份。后续修复若需要超出当前授权，先返回精确补丁与阻碍，不绕过写入拒绝。

账户账单接口的现有 integration 只读返回 403，账户当期余额和计划仍未知。该外部待办只能由用户在已有私有 UI 查看；不额外索取凭据、不尝试提高支付/预算权限、不把历史余额或较新 runner 能启动推断为当前余额证明。该外部待办不阻塞本任务的独立本地代码/配置验证。公开 Enterprise Math 仅保存必要 generic error 与原私有链接，不复制知识库完整日志、账单或账户详情。


## Hard target and required outputs

1. 保存两个 migration 的 target file、JSON pointer、old/target/current、baseline Git blob、当前 Git blob 与批准状态，明确当前已目标字段；不得将历史 baseline 改成当前 SHA 来越过检查。
2. 在临时测试夹具复现 old == target == current == false 被先判 old/pending 的问题；修复目标优先或等价 no-op 分类，让已目标状态不进入 pending 基线集合。不得把真实 pending 当作已完成。
3. 保留真 pending 的 exact baseline、第三状态、未批准迁移、protected selectors、非目标结构/文本字节的拒绝/保真规则。需提供全目标 no-op、old==target、真实 pending、混合 pending/no-op、错误基线和第三状态的必要回归证据。
4. tests/test_registered_json_migration_applier_unittest.py 中仍期待 ADOPT_EXISTING_CLAIM 的陈旧断言须对照当前 successor CLAIM + predecessor CAS 规范纠正，不把生产契约倒退为旧机制。保持研究、Working Truth、Foundation 和作者身份语义不变。
5. 本地运行原双 migration dry-run、相关 registry/equivalence/受保护字段检查及受影响测试；全目标状态应无变化成功，真实非法输入须仍明确失败。记录命令、计数、退出码及 before/after 字节。没有真实需要不得在生产目标执行 --write migration。
6. 交付有界代码/测试补丁与证据，不调整两条历史 baseline 或 whole-file 重排来消除红灯。若执行工具发布有代码审查或 pin 审核要求，保留该路线；不自行部署或扩大权限。

## Research value to preserve

使现有 fail-closed 语义迁移检查可执行，保护非目标研究语义与精确来源，避免长期 CI 红灯或为消红而弱化基线门禁。

## Success, kill, and return criteria

SUCCESS：原双 migration dry-run 在已目标源上返回无变化；old==target==false 正确 no-op；真 pending、混合状态及拒绝分支保留精确基线和语义保护；当前 successor-CAS 断言正确。必要本地回归实际通过；无法通过时据实 BLOCKED，不以非执行请求冒充修复完成。

ALREADY_COMPLETE：最新 main 已含精确有效修复时，消费来源与可重复验证，不重复写入。BLOCKED：记录具体命令、目标、拒绝/缺证据与最小下一动作；不吞并其他独立任务。禁止降低测试、收集、schema、语义迁移或安全门禁来制造通过。返回实际测试命令、数量、结果和未执行部分；本地通过不能宣称远程 Actions 已通过。
