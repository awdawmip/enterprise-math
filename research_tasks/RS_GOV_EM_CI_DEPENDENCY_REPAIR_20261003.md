<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GOV-EM-CI-DEPENDENCY-REPAIR-20261003",
  "title": "EM quality 测试依赖与真实收集修复",
  "kind": "GOVERNANCE",
  "owner": "governance/ci-maintenance",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "quality 代表运行在导入 test_group_ring_batch_response.py 时缺 pytest；只安装包仍须核对自定义 unittest 分片器对 pytest 参数化与 fixture 注入的真实收集语义。",
  "next_action": "冻结 quality.yml、run_unittest_shard.py 和 pytest 风格测试的精确当前字节，区分依赖缺失与收集/参数注入问题，先完成最小本地失败证明。",
  "dependencies": [],
  "source_refs": [
    "git:awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:.github/workflows/quality.yml",
    "git:awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:scripts/run_unittest_shard.py",
    "git:awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:tests/test_group_ring_batch_response.py",
    "https://github.com/awdawmip/enterprise-math/actions/runs/37036070877",
    "driver_reviews/portfolio/EM-DVR-E8DCE5/actions_followup_20261003/HANDOFF.md",
    "driver_reviews/portfolio/EM-DVR-E8DCE5/actions_followup_20261003/EVIDENCE.json"
  ],
  "evidence_status": "SOURCE_BACKED_CI_FAILURE; LOCAL_REPAIR_NOT_EXECUTED; NO_REMOTE_ACTIONS_AUTHORIZATION",
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GOV-EM-CI-DEPENDENCY-REPAIR-20261003",
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

# EM quality 测试依赖与真实收集修复

## Mother question

quality 代表运行在导入 test_group_ring_batch_response.py 时缺 pytest；只安装包仍须核对自定义 unittest 分片器对 pytest 参数化与 fixture 注入的真实收集语义。 怎样修复这一确切软件维护缺口并证明预期检查被真实执行，而不是仅改变表面 CI 颜色？

## Frozen inputs and scope

控制 Source enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90。代表失败运行 37036070877 / head84cf8737b384651c6ec5f8a69c93ed166525e0b8，unit-shard (0) 实际启动，报 ModuleNotFoundError: pytest。当前 quality.yml 的 Python3.12 unit-shard 没有安装测试依赖。缺包与 runner 对带参数 pytest function 的语义不兼容是不同修复义务；不能把 test import 成功视为测试全部执行。范围限必要测试依赖声明、runner/工作流一致性及针对性回归；不借此改科研实现、跳过重测试或改变现有分片覆盖。

本任务是有界 GOVERNANCE / MAINTENANCE 软件维护，仅本地验证，不领取数学研究、不授予 Owner、Steward 或数学接受权。P000 固定心跳世界原生 X6，原生“平面”不存在；时间按问题需要独立定型。本任务不改变该语义、数学真值或 Foundation 内容。仅访问获准两个仓库及现有工具，不扩网络、权限、凭据；不部署、不新建环境、不运行/重跑/dispatch GitHub Actions。

任务出版使用 canonical V2 preflight，完整 taskbook+record 通过可设置提交消息的原子 Git-data main CAS，并带 [skip ci]。不得改用已知服务器提交会自动触发 Actions 的 native publication/followup路径；保持已有授权会话，不为出版而重新注册身份。后续修复若需要超出当前授权，先返回精确补丁与阻碍，不绕过写入拒绝。

账户账单接口的现有 integration 只读返回 403，账户当期余额和计划仍未知。该外部待办只能由用户在已有私有 UI 查看；不额外索取凭据、不尝试提高支付/预算权限、不把历史余额或较新 runner 能启动推断为当前余额证明。该外部待办不阻塞本任务的独立本地代码/配置验证。公开 Enterprise Math 仅保存必要 generic error 与原私有链接，不复制知识库完整日志、账单或账户详情。


## Hard target and required outputs

1. 给出实际测试依赖来源和版本约束，采用仓库可维护的单一安装入口，令干净 Python3.12 环境与 quality unit shards 使用同一测试依赖；不依赖当前 setup 已预装包。
2. 当前 scripts/run_unittest_shard.py:90–115 对 required参数 fail-closed；test_group_ring_batch_response.py 使用 pytest.mark.parametrize 的 (n,b)/(n,a)/call 注入。列明自定义分片器实际支持的 unittest、无参函数、pytest.mark.parametrize、fixture/参数注入边界。对 test_group_ring_batch_response.py 实际参数行和其他已存在 pytest 风格测试做精确清单，不能悄悄跳过带参数函数或执行一次伪装全部实例。
3. 选择最小且可维护的兼容方案：保留/完善分片器时证明参数化实例被正确收集执行；转用现有 pytest 收集时保持既有 unittest、分片不重不漏与隔离慢测试边界。选择由实际配置推导，不预设安装 pytest 足够。
4. 在本地可写临时环境运行 import/dependency 检查，以及最小参数化/fixture 与故意失败 sentinel，证明执行而不是空收集；记录八分片精确集合并与受支持完整入口的用例集合/计数对账，保留 bootstrap 和 heavy-P017 隔离；不支持 async 或 fixture 必须明确失败，不能静默 skip。记录受影响真实测试和退出码。只运行与修改相关的必要验证；不得触发 Actions 或重做数学实验。
5. 交付最小补丁、依赖清单、收集/执行证据及恢复步骤。保留无 skip/xfail/continue-on-error 掩盖的失败传播。

## Research value to preserve

使现有真实测试在 CI 与新环境中按声明语义执行，防止缺依赖及参数化漏测长期遮蔽研究基础软件回归。

## Success, kill, and return criteria

SUCCESS：干净声明依赖可复现，受影响参数化/fixture 实例被精确执行且失败会传播，分片覆盖保留，本地必要测试通过；交付完整补丁和证据。外部 Actions 未运行仍应明确标注，不以等待远程 CI 阻塞交付。

ALREADY_COMPLETE：最新 main 已含精确有效修复时，消费来源与可重复验证，不重复写入。BLOCKED：记录具体命令、目标、拒绝/缺证据与最小下一动作；不吞并其他独立任务。禁止降低测试、收集、schema、语义迁移或安全门禁来制造通过。返回实际测试命令、数量、结果和未执行部分；本地通过不能宣称远程 Actions 已通过。
