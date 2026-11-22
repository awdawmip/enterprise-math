# 数学研究流程减负：2026-11-22 定点审查与修正

范围：CONTROL_PLANE_MAINTENANCE。依据用户本轮要求：“我们是数学研究，不是每个步骤都要按照代码来要求的。”

基准：Enterprise Math `594db5af2151819bc5e0cec58df6b557d972b3a1`；全局知识库 `32af83eeef0400eb1c33ec17519f802d0e10b71f`。本次定点沿研究入口及直接消费者核查，未做全仓流程普查，没有改变研究定时任务或历史科研记录。

## 已有改进

四个常规工作流 `quality`、`reference-integrity`、`lean`、`bilingual-sync` 已经只保留 `workflow_dispatch`。AGENTS 是短路由。普通未共享推导、科学文件保存和成果汇报已经不以 Activity 预登记、严格观察审计或正式任务完成权为前提。工具覆盖及复用比较已主要限于方法新颖性主张或共享工具接纳，没有证据把其五字段比较记录说成所有手算的必填表。本次复用这些已完成改进。

## 实际残余与本次修改

| 残余 | 修正 | 直接来源 |
|---|---|---|
| 贡献指引把每项实质结论都要求加标签，外部引用容易立即触发来源与谱系登记 | 连贯论证可共用状态；普通笔记用可定位学术引用，登记和双语图更新限于规范整合 | `CONTRIBUTING.md` / `.zh-CN.md`；`docs/CITATION_POLICY.en.md` / `.zh-CN.md` |
| 精确计算的证据说明容易被解读为每个短脚本都须另造证书 | 全局数学政策明确完整书面证明、可复算精确计算与方法所需证书的适用范围；计算脚本不自动成为软件产品 | GK `knowledge/preferences/MATH_RESEARCH_POLICY.json` v3；`docs/PORTABLE_RESEARCH_PROTOCOL.md` |
| 保存触发文字可能把每次换路、试值和中间推理都变成提交 | 一个有意义、可恢复的研究批次可含多步推理与失败尝试；在成果、交接、中断风险或最终交付边界保全 | `research_persistence_policy.json`；GK `PROGRESS_JOURNAL_PROTOCOL.md` |
| Activity 文档仍教启动／回复前反复提供完整注册观察，并错误描述 guard 重验 sidecar | 按实际实现区分轻量关联检查与按需 audit；删除每步审计旧示例，已有科学文件由其他台账引用 | `docs/RESEARCH_ACTIVITY_PROTOCOL.md`；未改 `tools/research_activity.py` |
| 交接文档无条件要求 Task ID、下一动作及易被理解为独立 manifest 的列表 | 有正式任务才填其真实 ID；现有笔记或简短定位段落可承担交接；完成或未知后继可留空 | `docs/RESEARCHER_DURABLE_HANDOFF_PROTOCOL.md` |
| 双语政策仍声称每次 push／PR 自动运行，且把所有正式文字都当成同步对象 | 已登记规范文档在整合时对齐；笔记、草稿和交接可以单语，说明工作流已手动化 | `docs/BILINGUAL_POLICY.en.md` / `.zh-CN.md` |
| 双语检查即使只改一对文件也读取全部 143 对文档 | 新增 `--paths`，检查所选文档对及对应文件；默认完整审计保留，显式未登记路径报错 | `tools/check_bilingual_pairs.py`；`tests/test_check_bilingual_pairs.py` |
| 运行时返回的 hot_start／rebase 提示把已有任务接续又引向 dispatch | 复用有效任务／接续和已验证前沿；只在确实选新任务时调用 dispatch | `control_plane/research_startup_transport.py` |
| 正式 Result CLI 强制研究者每次选择工具分类 | 省略 `--method-harvest` 时采用现有 `RESULT_ONLY`；显式分类和写入值校验保持 | `control_plane/research_result_records_impl.py` |

上述变化让方法、表达与验证方式服从实际数学问题，不添加研究登记表或新的流程状态机。前提、证明缺口、实验范围、真实出处及形式化声明仍按其实际内容核验；正式共享状态的 owner、CLAIM、审查和写入权限仍由原机制处理。

## 本地验证

- 现有 startup transport 测试 7 项通过；保留实际 authority、epoch、rebase 和任务选择检查，只删除一条强制旧提示字符串出现的过时断言。
- 双语选择测试 6 项通过，使用临时真实文件和真实 Git diff，覆盖对应文件缺失、未登记请求、多对选择、字符／标题检查、局部检查与默认全量检查，以及带 base 的单边修改失败／补齐通过。
- 本批 CONTRIBUTING、CITATION_POLICY、BILINGUAL_POLICY 共 3 对文档，用实际新增 `--paths` 一次检查通过；共检查 6 个文档，不读取全部 286 个配对文档。该结果是结构核验，另已审阅中英语义一致性。
- Result 的真实 `main()` 参数入口：省略分类得到 `RESULT_ONLY`，8 个现有显式分类全部保留，非法值在执行 handler 前被拒绝。测试只替换解析后的 handler，不声称完成正式 Result 远端写入端到端验证。
- 两份修改后的 JSON 可解析；persistence 的 invariants、machine_freeze、activity_entrypoint 和 precedence 完全保留。

未运行远程 CI 或全仓回归。本次验证针对改变的实际行为；纯文字范围澄清采用内容审阅。本报告记录源代码及本地入口的结果，没有执行研究中控台部署或以此声称在线中控台已加载新代码。

## 后续使用

日常研究直接围绕问题、前提、论证、计算和来源推进。完整证明按数学内容复核；有限实验据覆盖范围报告；需要形式化时再取得实际检查证据。保存可恢复的连贯研究批次，其他台账引用同一份成果。只在发生规范整合、共享任务操作或软件行为变化时进入相应的专门检查。
