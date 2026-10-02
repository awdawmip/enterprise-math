<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GOV-KB-CI-DEPENDENCY-REPAIR-20261003",
  "title": "知识库索引工作流 jsonschema 依赖修复",
  "kind": "GOVERNANCE",
  "owner": "governance/ci-maintenance",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "知识库索引工作流在干净 runner 中缺 jsonschema，触发单测和 LOCAL_VALIDATION_PENDING 连锁失败；需让声明依赖与本地/工作流验证入口一致。",
  "next_action": "读取私有知识库当前 main 的两个索引工作流、schema validator 与测试依赖，建立最小无敏感内容的缺包复现并制定共享安装入口。",
  "dependencies": [],
  "source_refs": [
    "git:awdawmip/chatgpt-global-knowledge@1469c496616e52b43e817ecbf73fd8fa793d3480:.github/workflows/knowledge-index-rebuild.yml",
    "git:awdawmip/chatgpt-global-knowledge@1469c496616e52b43e817ecbf73fd8fa793d3480:.github/workflows/knowledge-index-check.yml",
    "git:awdawmip/chatgpt-global-knowledge@1469c496616e52b43e817ecbf73fd8fa793d3480:tools/validate_legal_contracts.py",
    "https://github.com/awdawmip/chatgpt-global-knowledge/actions/runs/37007219111",
    "driver_reviews/portfolio/EM-DVR-E8DCE5/actions_followup_20261003/HANDOFF.md",
    "driver_reviews/portfolio/EM-DVR-E8DCE5/actions_followup_20261003/EVIDENCE.json",
    "git:awdawmip/chatgpt-global-knowledge@1469c496616e52b43e817ecbf73fd8fa793d3480:tools/requirements-legal-validation.txt"
  ],
  "evidence_status": "SOURCE_BACKED_CI_FAILURE; LOCAL_REPAIR_NOT_EXECUTED; NO_REMOTE_ACTIONS_AUTHORIZATION",
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GOV-KB-CI-DEPENDENCY-REPAIR-20261003",
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

# 知识库索引工作流 jsonschema 依赖修复

## Mother question

知识库索引工作流在干净 runner 中缺 jsonschema，触发单测和 LOCAL_VALIDATION_PENDING 连锁失败；需让声明依赖与本地/工作流验证入口一致。 怎样修复这一确切软件维护缺口并证明预期检查被真实执行，而不是仅改变表面 CI 颜色？

## Frozen inputs and scope

私有 Source chatgpt-global-knowledge@1469c496616e52b43e817ecbf73fd8fa793d3480。代表运行37007219111 实际启动但 generic错误为 ModuleNotFoundError: jsonschema；原私有日志保持在私有来源，不拷入公开任务产物。两个索引 workflow 都在 Python3.12 环境运行 unittest 和知识库 validator，而工作流未安装已有 tools/requirements-legal-validation.txt 中固定的 jsonschema==4.26.0。只修必要依赖/安装入口/最小回归，不改用户知识记录、法律合同内容、既有 schema 标准或全局同步行为。

本任务是有界 GOVERNANCE / MAINTENANCE 软件维护，仅本地验证，不领取数学研究、不授予 Owner、Steward 或数学接受权。P000 固定心跳世界原生 X6，原生“平面”不存在；时间按问题需要独立定型。本任务不改变该语义、数学真值或 Foundation 内容。仅访问获准两个仓库及现有工具，不扩网络、权限、凭据；不部署、不新建环境、不运行/重跑/dispatch GitHub Actions。

任务出版使用 canonical V2 preflight，完整 taskbook+record 通过可设置提交消息的原子 Git-data main CAS，并带 [skip ci]。不得改用已知服务器提交会自动触发 Actions 的 native publication/followup路径；保持已有授权会话，不为出版而重新注册身份。后续修复若需要超出当前授权，先返回精确补丁与阻碍，不绕过写入拒绝。

账户账单接口的现有 integration 只读返回 403，账户当期余额和计划仍未知。该外部待办只能由用户在已有私有 UI 查看；不额外索取凭据、不尝试提高支付/预算权限、不把历史余额或较新 runner 能启动推断为当前余额证明。该外部待办不阻塞本任务的独立本地代码/配置验证。公开 Enterprise Math 仅保存必要 generic error 与原私有链接，不复制知识库完整日志、账单或账户详情。


## Hard target and required outputs

1. 复用已有 tools/requirements-legal-validation.txt（当前 jsonschema==4.26.0），由两索引 workflow 共用真实声明的依赖安装入口；执行时重新核对精确当前文件，不创建第二套冲突版本或依赖 setup 现成包。
2. 在干净本地临时 Python3.12 环境安装现有 requirements 后运行 pip check、实际版本、unittest discover -s tests -v、受影响 validate_legal_contracts 入口，证明 LOCAL_VALIDATION_PENDING 缺包分支被真正解除；K01…K14 negative controls、外部 schema 访问拒绝与真实无效输入拒绝保持。
3. 执行 build_knowledge_index.py --validate；如需生成/--check，放在临时副本做确定性验证，不手编索引、更不本地照跑 scheduled rebuild 的 commit/push 步；任何测试夹具只含合成数据，不把私有记录内容和完整测试日志复制到公开 EM。记录命令/计数/退出码；不要把已有 warning 改成伪装通过或删除 schema；保留负例失败及禁止远程 schema 的规则，不执行自动提交步骤。
4. 更新必要工作流安装步骤与启动文档，产物补丁留知识库同一 repo/main 路线；发布消息 [skip ci]、非强制 CAS，禁止 schedule 手动触发/重跑/dispatch；当前无受支持写权限时返回精确补丁与阻碍，不能换凭据。
5. EM状态机仅保存 generic结论、私有 source URL/commit/path 和交接状态；详细证据留私有知识库授权位置。

## Research value to preserve

恢复知识库自动验证的可重复依赖边界，避免正常内容因 runner 缺包被误标未验证，同时保护私有来源。

## Success, kill, and return criteria

SUCCESS：干净依赖安装入口与两个 workflow 一致，相关单测和 schema 正反例在本地通过，必要索引确定性检查保持；详细证据仅留私有源。账户账单状态不由此任务推断。

ALREADY_COMPLETE：最新 main 已含精确有效修复时，消费来源与可重复验证，不重复写入。BLOCKED：记录具体命令、目标、拒绝/缺证据与最小下一动作；不吞并其他独立任务。禁止降低测试、收集、schema、语义迁移或安全门禁来制造通过。返回实际测试命令、数量、结果和未执行部分；本地通过不能宣称远程 Actions 已通过。
