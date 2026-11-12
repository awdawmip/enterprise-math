# 研究者启动上下文协议

[英文版本](RESEARCHER_STARTUP_CONTEXT_PROTOCOL.md)

状态：`ACTIVE / CONTROL-PLANE / NO_NEW_MATHEMATICS`
模式：`ENTERPRISE_MATH_RESEARCHER_COLD_START_ENVELOPE_V1`

## 问题

新启动的 TASK_RESEARCH 对话不得在数学工作开始前，把大部分可用上下文消耗在重复的治理正文上。此前的静态上下文检查器只测量选定的仓库政策文件，并明确不测量全局知识输入、已连接工具输出、动态任务包或产品的 token 切分。该检查器仍然有用，但不能据此证明端到端冷启动的情况。

## 规范精简启动包

每次产生请求的 ChatGPT 规范调度桥运行，现在都会构建一份不可变启动包：

`control_plane/chatgpt_startup_packets/<request_id>.json`

模式：

`ENTERPRISE_MATH_RESEARCHER_STARTUP_PACKET_V1`

启动包是精确不可变调度回执与精确不可变任务发布记录的来源固定投影。它**不是** CLAIM、Result、评审、定理、Working Truth，也不授予数学权威。

固定约束：

`COMPACT_STARTUP_PACKET != TASK_CLAIM`。

`COMPACT_STARTUP_PACKET != MATHEMATICAL_AUTHORITY`。

`FULL_DISPATCH_RECEIPT = DIAGNOSTIC_SURFACE_NOT_ORDINARY_STARTUP_CONTEXT`。

`CURRENT_CONTROL_AUTHORITY_FULL_READ = TRIGGERED_CONTROL_DIAGNOSTIC_NOT_ORDINARY_TASK_START`。

## 任务投影

存在调度目标时，构建器：

1. 解析 `research_task_records/<task-id>/<publication-id>.json` 中精确的不可变发布记录；
2. 解析其精确的 `taskbook_path`；
3. 对照 `taskbook_blob_sha1` 验证当前任务书字节；
4. 仅当以下全部权威章节各出现一次、按其声明顺序排列且没有遗漏其他任务正文时，提取这些章节：
   - `Mother question`；
   - `Frozen inputs and scope`；
   - `Hard target and required outputs`；
   - `Research value to preserve`；
   - `Success, kill, and return criteria`；
5. 以 `taskbook_metadata` 保留完整前置元数据，以 `taskbook_title` 保留文档标题，包括未知的约束字段；
6. 仅在完整启动包仍符合启动包硬预算时，内联该精确投影。

如果精确投影过大，构建器会同时省略章节、元数据和标题，并指示消费者读取精确任务书。它绝不为满足上下文预算而截断或改述任务语义。只有文首任务头部才作为元数据；正文围栏中的元数据示例保持字面内容，不能选择依赖路径。

附加约束章节、含实质内容的前言、重复或重排的标题、未闭合的代码围栏，以及非标准布局，均采用 `EXACT_TASKBOOK_REQUIRED`。围栏示例中的 Markdown 标题保持为章节正文的字面内容。中文任务书或没有标题但合法的任务书，仍可通过其精确路径/blob 使用；五个英文标题是投影格式，不是任务发布资格要求。有界的 `projection_incomplete_reasons` 列表说明回退原因，不把被省略的任务正文放入诊断。

## 第一项依赖

启动包可以包含一个 `first_dependency_ref`，无需发现目录。当前目标的非空 `last_progress_ref` 优先于较旧元数据；以发布 ID 表示的哨兵值不属于前沿。如果无法精确解析该当前引用，就将其保留在 `task.last_progress_ref`，并把第一项依赖留为 null，不能静默选择旧工作。否则，按以下顺序优先选择证据：

1. 不可变发布记录未来明确提供的 `startup_read_plan.first_dependency_ref`；
2. `last_progress_ref` 中精确的持久前沿路径；
3. 精确的未满足依赖路径；
4. 精确的来源引用路径。

没有精确项时，该值为 null。依赖为 null **不**授予枚举目录的权限。理解任务后，使用有界定向搜索（初始建议 `topn = 20`，可按需扩大），再读取精确文件。

支持字符串依赖，以及以字典表示的未满足依赖。没有额外限定且实际存在的路径，指向启动包的来源快照。明确声明的 `path@ref` 或同仓库 GitHub blob URL 作为读取提示原样保留，不代表该引用版本已经在本地验证。使用前读取精确声明的来源；不得用当前 main 的字节替代固定版本。任务局部的来源访问隔离及冻结范围继续约束访问。

固定约束：

`UNKNOWN_FIRST_DEPENDENCY != DIRECTORY_ENUMERATION_AUTHORITY`。

## 普通新研究者的启动主路径

预期路径为：

`GLOBAL_BOOTSTRAP -> ENTERPRISE_TASK_BOOTSTRAP -> SOURCE_FOUNDATION_AT_REQUIRED_SCIENTIFIC_VERSION -> HOST_INJECTED_AGENTS_IF_PRESENT -> EXACT_COMPACT_STARTUP_PACKET -> INLINE_TASK_PROJECTION_OR_EXACT_TASKBOOK -> FIRST_EXACT_DEPENDENCY_IF_NEEDED -> SUBSTANTIVE_RESEARCH`。

普通启动不得仅因开始任务而远程获取 `AGENTS.md`。除非具体诊断条件使相应资料成为必要输入，否则不得加载完整调度回执、完整当前控制权威 JSON、完整 Issue #240 事件流、递归仓库树，或包含大量分支项的任务/结果目录。

### 角色与基础读取路径

只读取当前工作对应的路径，复用已加载且仍有效的上下文。全局 P000 V4 投影覆盖其自身的全局来源；它不能替代 Source P000 V5 及其强制 companion。Source 生成器 `tools/build_em_foundation_startup.py` 在两份确定性读取包中保留完整的五合同关系及实际规范值：

- `definitions/EM_FOUNDATION_STARTUP.json`：用于 TASK、Driver、Steward 以及已冻结的 FREE B；
- `definitions/EM_FREE_A_FOUNDATION_STARTUP.json`：用于 FREE A，不包含详细成果比较目录，也不包含尚未展开的条件主题菜单。

区分当前控制规则与冻结的科学输入引用。读取包只适用于其实际来源 blob；新的 main/控制快照不会静默更新旧任务的科学假设。读取包不授予角色、任务、定理、评审或 Foundation 权威。

| 当前工作 | 适用全局规则之后的必需路径 |
|---|---|
| 直接开展、未共享的 TASK 推导 | 相关基础、精确问题/输入及适用研究方法；开始实际论证或构造。正式新颖性、共享接纳和控制操作各自触发对应合同。 |
| 已调度/已恢复的 TASK | 复用已知任务或接续请求；仅在需要新任务时才进行选择。遵循实际返回的 prepare/claim/open/recovery 动作、精确启动包/任务书及必需依赖。 |
| FREE A | A 阶段基础包、当前 FREE 角色、反锚定规范及原始基础；需要时读取精确的其他原始概念。独立形成的问题实际包含相关结构后，可以在冻结前读取精确定义/工具资料。 |
| FREE B | 保留冻结候选、来源与暴露历史；使用普通基础包及相关 B 阶段比较/去重来源。 |
| Driver | `docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md`、实际传输/激活要求，以及精确决策或结果证据；仅在触发时读取优先级/接续资料。 |
| Steward | `foundation_steward.json`、实际控制要求，以及精确的 Foundation 维护证据。 |
| 进度/文档维护 | 精确的当前产物及适用的控制/语义保护来源；不自动创建研究身份、活动、CLAIM 或执行数学启动流程。 |

本地 `--read` 从已分类输入检查或重建符合角色要求的精确读取包。读取包缺失、陈旧或不受支持时，普通角色可以读取精确规范来源；FREE A 使用匹配的有效 A 阶段读取包，或精确的获准选段。其错误与回退不得暴露混合原始来源或构建覆盖资料。某个具体输入不可用，只影响依赖它的工作；其他独立工作继续。构建与查询的详细用法见 `docs/FOUNDATION_STARTUP_READING.en.md`。

## 产生并消费一个当前请求

对于只能使用连接器的 TASK_RESEARCH 对话，使用托管 GitHub 连接器读取 `control_plane/chatgpt_dispatch_request.json` 当前 `main` 的 blob，再通过乐观并发控制，用以下最小 JSON 更新该精确路径：

```json
{
  "schema": "ENTERPRISE_MATH_CHATGPT_CONTROL_DISPATCH_REQUEST_V1",
  "request_id": "chatgpt-20260908T000000Z-0123456789abcdef",
  "kind": "RESEARCH"
}
```

将示例 ID 替换为本次请求的新时间戳/随机后缀；不得提交字面示例，也不得复用已经物化的 ID。完整 ID 必须匹配 `[A-Za-z0-9][A-Za-z0-9._-]{0,127}`。`kind` 接受 `RESEARCH`、`GOVERNANCE` 或 `ANY`；普通研究者使用 `RESEARCH`。新启动时省略可选的 `session_observations` 字段。仅当实际 owner 范围证据满足现行 V2 活跃性合同时才加入它；不得借此把未知对话判成过期 owner，也不得虚构身份/claim 证据。

获准的直接 main 写入与分支/PR 合并都是有效发布路径。请求变更到达 `main` 后，才成为持久的调度桥输入；单独的 PR 验证运行不会保存请求启动包。写入或合并前，刷新实际写入目标，并使用其预期 head/blob。发生并发写入拒绝时，重新读取该精确目标，使用新的保护值重试，保留其他作者的变更。不要创建第二套调度器。

记录请求 ID 及实际产生该请求的 main 提交。现有 `.github/workflows/chatgpt-control-dispatch-bridge.yml` 执行规范路由器，并持久化以下精确输出路径：

`control_plane/chatgpt_startup_packets/<request_id>.json`

读取这一份启动包，核对模式 `ENTERPRISE_MATH_RESEARCHER_STARTUP_PACKET_V1`、精确 `request_id`，以及与产生请求的 main 提交对应的 `source_sha`。读取所提供的任务投影或精确固定任务书，再按需读取第一项精确依赖。不得用可变的最新回执或其他请求的启动包代替。请求发布后立即缺少启动包，可能表示尚在处理：需要时仅检查该请求的调度桥运行，并保留精确请求键。不得产生重复请求或轮询无关 CI。工作流成功是传输证据；启动包中带类型的 `action` 仍决定下一步。

| 启动包 `action` | 必需的下一步 |
| --- | --- |
| `CLAIM_NEW_OWNER` | 针对精确发布记录及适用 lane 遵循当前 CLAIM 协议；写入前刷新实时 claim 权威，并在数学执行前验证获胜 claim。启动包本身不是 claim。 |
| `PREPARE_SUCCESSOR_CLAIM` | 保留精确前任 CLAIM/评论、任务/发布记录、lane 和持久前沿。遵循返回的接续守卫及现行角色授权；跨会话后继执行要求新的已认证 CLAIM、前任 CAS、旧写入者隔离及获胜回读。准备步骤不是执行权威。 |
| `ADOPT_OWNER_CLAIM` | 旧动作名称：依当前接续守卫重新判定，保留精确前任及前沿。跨会话恢复遵循已认证后继 CLAIM/CAS；只有适用的现行守卫允许时才能同会话恢复。名称本身不授权私下接管或执行。 |
| `VERIFY_SESSION_LIVENESS` | 只取得必需的精确 owner 范围证据。有证据时，带有效 V2 观测提交新请求；否则报告具体缺少的证据。此动作不是 `NO_DISPATCH`。 |
| `NO_DISPATCH` | 报告此精确请求/来源快照没有调度结果。不得据此推断队列永久耗尽，也不得手动扫描队列。 |

动作未知、请求/来源不匹配，或缺少返回动作所需的身份/发布记录/lane 绑定时，应进行有界诊断，不得猜测任务或制造权威。此时，启动包指定的精确不可变回执成为已触发的诊断资料。请求 ID 标识传输尝试，不是 Researcher-ID。既有研究身份、CLAIM、运行时、冻结输入及数学接纳规则继续适用。

### 精简控制细节与事件格式

规范路径提供相应字段时，启动包保留 `surface`、`target_key`、`required_guard`、精确 cohort/lane/输出范围，以及目标的最新进展引用/时间。这些是投影，不是新授予的权威。对于 `VERIFY_SESSION_LIVENESS`，`liveness_targets` 按来源顺序最多承载 20 条精确 owner 范围摘要；必要时进一步减少，以满足字节上限。`total`、`omitted`、`next_index` 及不可变回执的 `/route/targets` 指针，明确展示被省略的尾部。这个诊断前缀不属于任务选择；显示的前缀为空也不是 `NO_DISPATCH`。使用可用的有界读取器，仅读取所需的剩余回执范围；这不意味着要新增分页服务，也不要求启动时读取完整回执。

调度器事件评论必须是原始 JSON 对象，不能包含 Markdown 围栏或附加正文。发送前解析精确的待发送正文。现有服务端信封认证及获胜 CLAIM/运行时检查仍然必需；仅完成序列化不授予执行权限。

## 缓存旧路径的 404 恢复

旧对话尝试读取根目录 `research_task_registry.json` 并收到 404 时，不得把该文件缺失视为空队列或当前调度器失败。执行一次有界的控制基线更新：

1. 解析新取得的全局知识规范 `main` 及其当前 Enterprise Math TASK 入口；解析新取得的 Enterprise Math `main`，并从同一来源快照读取本精确启动协议。记录解析后的 SHA；缓存 SHA 仍只是历史来源证据，不是新鲜度检查。
2. 如果当前入口使用上述请求/精简启动包路径，将缺少旧注册表归类为陈旧入口引用。不得重建它、搜索替代 V1 注册表，或枚举任务目录/Issue #240。
3. 在同一对话继续使用上述规范请求，或消费本对话已经发布的精确请求启动包。保留已有获胜 owner claim 及持久的未完成前沿；恢复过程不授予新 claim，也不授权重放已经完成的数学工作。

此例外由旧路径失败触发，不给普通启动增加额外诊断预加载。当前必需的请求、启动包、发布记录或任务书返回 404，属于另一类失败：只检查精确仓库/ref/路径及连接器响应，区分启动包尚在处理、陈旧 ref、访问/端点失败，以及真实来源完整性不匹配。如果必需的当前来源无法读取或验证，报告该具体阻断及已保留的请求/前沿。不得重复同一查找、重建旧控制面，或把所有 404 都标为无害。

## 预算

`research_context_budget.json` 提供按需软预算，不规定模型认知上限。模型根据任务需要和可用上下文自主增加定向读取，无需例外申请，也不因两次读取、64/80 KiB 或组件目标而停止。兼容保留的读取 `max`/`hard` 字段均为建议值；静态大小超额只报告，不拒绝。避免无效批量灌入上下文；真实平台传输限制、授权来源范围和盲实验隔离仍有效。

8192 字节仅是精简包的序列化格式上限。超大的任务书转为外部精确读取，不截断语义。启动包加外置任务书的计量只是部分载荷，不代表端到端上下文或 token 总量。建议启动路径是资料路由，不预定研究思考步骤。

## 调度桥持久化与并发

精简启动包与不可变调度回执在产生请求的同一事务中持久化。它没有可变的 `latest` 指针。消费者使用精确请求 ID。

仅工作流重放仍会执行实时路由与启动包构建以进行验证，但没有持久回执/启动包写入权限。本协议切换后，已拥有回执的请求 ID 也必须拥有匹配的启动包；孤立或不匹配的启动包按失败关闭处理。

## 验证

`control_plane/check_context_budget.py` 验证静态政策及组件层面的冷启动边界。

`tests/test_researcher_startup_packet.py` 覆盖精确投影、大任务回退、摘要不匹配及无目标路由。

`tests/test_researcher_startup_context_envelope.py` 使用仓库当前真实调度回执运行启动包构建器，并验证大块诊断字段不会混入精简启动包。

可在本地执行的启动包、边界及基础测试验证这些变更。现有 `.github/workflows/researcher-startup-context-validation.yml` 是托管检查入口；其实际启用/必需状态是另一项部署事实。不得仅为此次本地验证新增或调度托管检查。任何既有且具有约束力的传输或必需检查依赖，在出现已验证替代路径前，继续保留其作用域。

