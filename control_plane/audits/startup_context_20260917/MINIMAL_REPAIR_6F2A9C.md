# 启动包最小修复与后续减负方案

Status: `LOCAL_VALIDATION_PASS / MINIMAL_SOURCE_REPAIR`
Mode: `CONTROL_PLANE_MAINTENANCE / NO_NEW_MATHEMATICS`
Progress-Event-ID: `STARTUP-MINIMAL-REPAIR-20260917-6F2A9C`
Source base: `awdawmip/enterprise-math@290b2f44082f94a3ffe4bb98dc1564537e2a53c4`
Authority: user explicitly requested minimal optimization and direct publication to `main`.

## 已实施的范围

本补丁只修现有启动包的信息投影和部分字节记账，复用原调度器、原领取解析器与原授权守卫。未新增调度器、执行平台、任务或常驻服务。此报告不是研究启动必读文件。

1. 保留规范route已给出的surface、target_key、required_guard，以及精确cohort/lane/output范围和最新进度引用/时间；不生成或改变这些字段的权限。
2. VERIFY_SESSION_LIVENESS保留有界目标摘要，最多20项且继续服从8192字节限制。明确给出total、omitted、next_index和同一不可变回执的/route/targets定位。只展示原列表前缀，不重新排序、不替用户或调度器选任务；显示为空但还有省略项时仍是核验动作，不是无任务。
3. 当前live frontier优先于旧任务元数据。无法精确解析时保留原引用、返回空的首依赖，不静默回退到旧成果。publication-ID占位值不当成进度。
4. 支持字符串形式依赖；path@ref及本仓库GitHub blob URL保持原样。它们是待验证的读取指针，不是本地已核验的其他版本。禁止借正则截掉显式版本后误读当前文件。盲测和任务source firewall照旧。
5. 报告taskbook_bytes、external_taskbook_bytes和packet_plus_external_taskbook_bytes；内联任务书不重复计数。明确这是包体加外置任务书的局部计量，不是整个会话预算或token统计。
6. 既有协议补充字段用法、显式省略的处理、原始JSON正文发送前解析要求；没有放宽真实服务器事件或获胜CLAIM核验。

## 本地验证

精确旧源文件从前轮已回读的审计包恢复，并与当前连接器返回的Git blob核对相同。原生成器blob为f987bd676b07abc2d57ffeda1bd22aae31515108；原测试blob为329bbd7c5f7e207004616705e14bd278a4d37894；原协议blob为b9cae1db6eeb0b6795102b673b0439b80859f8a6。

- 23项局部单元测试通过，失败0，错误0；其中含5项原有核心测试和18项新增测试。独立重跑仍通过。
- 28个附加存活目标组合通过：列表长度0/1/2/20/21/100/1000，标识长度1/32/500/5000个中文字符。检查实际UTF-8大小、原序前缀、明确省略、不修改输入回执。
- 两个Python文件py_compile通过。新增断言在旧生成器上出现预期失败，再在补丁上通过；没有把旧实现的缺口当成基线成功。
- 原有的1项文档/工作流集成测试未运行，因为完整工作流未在本地恢复；没有假造其fixture或把缺项算作通过。
- 未执行全仓库运行时/权限/工作流测试，未启动真实研究会话，未发任何CLAIM，未测实际启动延迟或产品token。局部测试通过不等于全部控制面通过。

可在完整仓库执行`python -m unittest discover -s tests -p test_researcher_startup_packet.py`；本轮实际局部runner明确排除了`test_documented_fresh_request_matches_the_actual_bridge_envelope`。源测试和复现包保留全部断言与日志。

## 隔离样例的实际包体大小

| 样例 | UTF-8包体字节 |
|---|---:|
| 普通新任务 | 2452 |
| 单个待核验目标 | 1623 |
| 100个待核验目标（显示20，明确省略80） | 5150 |
| 恢复已有领取 | 2794 |
| 并行通道 | 2611 |

以上是构造输入，不是当前队列、线上平均性能或提速承诺。额外大任务书样例的包体为2121字节，外置任务书210520字节，两者合计212641字节；现在明确报告该成本，但未将其错误标成端到端预算通过。

## 不改变的边界

任务选择和优先级、原始JSON事件解析、服务器鉴权、领取赢家、租约、独立复核、数学状态、P000、任务书及盲测均未改动。未修改Actions工作流、Actions设置、分支保护或请求文件。已有push触发器可能自行运行；本轮没有手动触发或依赖Actions完成验证。旧的不可变请求包不重写，新字段应用于之后实际生成的包。

## 剩余优化方案（尚未实施）

下一步只在现有校验入口补真实读取清单：分别统计规则、任务材料、登记/领取回读、工具描述和诊断响应；缺失观测时标UNKNOWN，不能报完整PASS。宿主工具描述注入和精确token需要宿主提供，不能靠仓库配置宣称已强制拦截。

再用极小文档补丁澄清注入AGENTS与普通TASK启动的触发边界；不新增一个必读手册，也不删权限条款。本轮未改AGENTS，未声称该入口冲突已经解除。

较大的liveness尾部只提供定位和明确省略，不部署新的分页服务。所用宿主没有有界读取能力时仍须如实暴露该限制，不能假装已经读完省略目标。缺包fallback仍是现有路由说明，不把本补丁冒充程序级防重复派单。

## 发布与回滚

将生成器、测试、原协议增补和本报告作为一个Git树/提交直接写入main。写前核对实际父提交及三个旧blob；以non-force更新引用，若并发冲突则重读并重建，不覆盖他人提交。发布后在不可变commit回读并核对blob。这个事务不需要创建研究身份、研究活动或真实任务领取。

回滚使用一个新的正常提交，只撤销本补丁的三个既有文件变更；保留审计历史和其他作者的工作，不reset或force-push main。

## 测试后文件身份

- `control_plane/researcher_startup_packet.py`: 17599 bytes; Git blob `80b5386da6f577b7f39670793b43623b96cf1dff`; SHA256 `cc78b3ea40f30622dd0b73d5d8c85f9dd0625519d8d5828f805bdc8cfcad089b`.
- `tests/test_researcher_startup_packet.py`: 20213 bytes; Git blob `b7c812aff78000c8c405bc0ecbb70293764daabc`; SHA256 `a5adb34033738e408800e14b1d383aeb246ea5de60c6fc98146dbd6be4d5b7e5`.
- `docs/RESEARCHER_STARTUP_CONTEXT_PROTOCOL.md`: 12857 bytes; Git blob `261dd0d5407228b184afc9a36462a1aae0166142`; SHA256 `fc244f358794323dc30bfe201b2a7b81a9f16356192828ab78daa743161a0804`.
