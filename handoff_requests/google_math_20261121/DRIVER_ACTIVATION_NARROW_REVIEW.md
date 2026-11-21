# 当前用户原话是否已激活 Driver

核验对象只有本句：**“仔细研究一下找到的线索，发布新的任务”**。

核验 Source：`f6384ca41ad91a8e1c62f664047e0431c560c3ea`。本轮重新读取的 `research_role_policy.json` blob 仍为 `fc2805f08f1a21c89e18fea816ab236a57696f54`，`research_objective_contract.json` blob 仍为 `8ea2ddf9c7592eace7ff01f41bb305b66470731f`。

## 逐字规则

`research_role_policy.json`：

> "default_role": "RESEARCHER"

> "default_research_mode_when_explicit_task_exists": "TASK_RESEARCH"

`driver_activation`：

> "mode": "EXPLICIT_CURRENT_CONVERSATION_ONLY"

> "Driver authority applies only after explicit activation in the current conversation and remains scoped to that conversation until the user changes it."

> "Do not infer Driver authority from memory, repository state, task importance, prior conversations, or another Project."

> "Driver authority adds portfolio reprioritization, Working Truth freeze and promotion decisions; it is no longer required merely to make a task exist."

`task_publication_authority`：

> "publisher_roles": ["RESEARCHER", "RESEARCH_DRIVER", "FOUNDATION_STEWARD"]

> "researcher_driver_approval_required": false

`delegated_driver_orchestration`：

> "activation": "EXPLICIT_CURRENT_USER_AUTHORIZATION_OR_OWNER_DELEGATION_WITHIN_THAT_AUTHORIZATION"

> "own_identity_and_current_activation_required": true

`research_objective_contract.json`：

> "publisher_roles": ["RESEARCH_DRIVER"]

> "required_parent_status_at_publication": "OPEN"

> "required_parent_generation": "exact operational objective head at publication preparation"

## 判定

该句已经明确授权深入核验线索和发布普通 Task。按默认角色，研究者即可执行这两类动作；不能再向用户重复索取普通 Task 发布授权。

但该句没有启用 Driver 角色，也没有点名其专有的父目标建立/选头、全局组合管理等操作。仓库刻意把普通 Task 发布与 Driver 激活拆开，且明确说仅使 Task 存在已不需要 Driver。因此不能反向从“发布新的任务”推定当前对话已经发生 Driver activation。`delegated_driver_orchestration` 保留显式当前用户授权或授权范围内 Owner delegation 路径；本句没有对应的明确 Driver delegation，不产生另外一个激活事实。

这不要求机械照抄规范示例口令：如果用户明确授权本对话以该组任务的 Driver 身份建立父目标，就满足当前对话的显式角色要求。现在仍缺的是这一个具体授权及其后真正原生成功 DA，不是科研、保存成果、portable Activity 或研究者 Task 发布许可。

主代理已完整排除18个现有OPEN父目标的真实适用性，本批需要新父目标。因而全部科学材料、具体任务书和发布包完成后，可以只确认：“请确认将本对话启用为这组任务的 Research Driver，用于建立并选定上述新父目标，随后按已审阅任务包正式发布。”同时说明此确认来自当前 `research_role_policy.json` 的显式激活要求与 `research_objective_contract.json` 的新父目标权限，而不是重新询问普通任务发布。

本复核未作任何远端写入、角色登记或DA激活。metadata骨架位于 `metadata_examples_unpublished.json`；generation字段留待真实选头产生，不造占位正式记录。
