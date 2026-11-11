<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-SORT-SCALING-ROBUSTNESS-20261111",
  "title": "BRC整数残差排序：同分布规模成本与抽样选择鲁棒性",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "公开实验已明确子层重新学习和分组计数的端到端成本；缺少同一生成法多规模曲线，以及在完整输出不变前提下可支付自身成本的根层决策证据。",
  "next_action": "读取673ac528的README和复现入口；先定义固定分布与随n缩放分布两套独立协议，运行至少四个几何递增规模的同输入强基线对照，再处理一项抽样误选机制。",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/tree/673ac528d167d35bbb87442df87eceecf7f31e4c/experiments/brc_residual_sort_preflight_20261111_b118ef26c242",
    "https://github.com/awdawmip/enterprise-math/commit/46352a6399b785a169d997fbfedc5043c5fe6f7f"
  ],
  "evidence_status": "AUTHOR_SIDE_PUBLIC_EXPERIMENTS_NOT_CANONICAL_ACCEPTANCE",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-SORT-SCALING-ROBUSTNESS-20261111",
  "parent_objective_id": "OBJ-BRC-UINT64-RESIDUAL-SORTING",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL"
}
-->

# 问题与范围

对有限 uint64 多重集，完成完整升序输出并精确保留每个值及其出现次数。在同样的输入、输出和计费口径下，何时局部计数加残差值得做，低成本决策能否可靠避免昂贵退化？不要把数学研究转成冗长软件流程，也不要以预期加速代替实际证据。

这是用户明确要求把后续研究交入状态机后的首次正式任务登记，不是宣称本路线首次提出。查重时现有正式任务没有整数排序执行项；此前工作是直接研究实验，不存在可继承的正式 parent Task/CLAIM/Result。因此 NEW_DIRECTION 仅表示首次正式直接任务入口，并非清空既有研究或把第八阶段伪装成新方向。保留以下全部已公开前序；不以私有对话、不可访问文件或未公开实现作为执行前提。

## 已有材料与不重复范围

主入口：[第5–7轮报告与复现包](https://github.com/awdawmip/enterprise-math/tree/673ac528d167d35bbb87442df87eceecf7f31e4c/experiments/brc_residual_sort_preflight_20261111_b118ef26c242)。README、REPRODUCE、brc_sort_rounds_5_to_7.zip 给出代码、前序依赖、原始计时、验证和来源。第4轮提交为46352a6399b785a169d997fbfedc5043c5fe6f7f。

已公开事实：仅增加预检样本并不自动改善端到端成本；直接对子层做偏移基数在部分三簇族有稳定局部收益；父网格有足够计数槽也不保证比基数快。第7轮已证明至多k段覆盖有限整数支撑集的最小槽数等于全包络宽度减去最大的k−1个内部空隙。消费这些材料，不把重跑已保存表格当成新成果。旧数据只作基线/校准，后续新增证据应有自己的输入协议与种子。

## 第一单元：同分布多规模成本

选择少量能区分机制的家族，例如均匀64位、窄范围重复、少量远端异常、分离稠密簇。至少四个几何递增规模，建议从约一万至百万并覆盖缓存转折；具体规模服从可用资源，不要求买机器。必须区分：固定值域/分布仅增加样本量；值域或簇宽随n按明确公式增长。不要把比例、位宽、异常率、簇距变化混成单一复杂度斜率。

同时比较完整残差路径、子层直接基数、整数组偏移基数、固定版本pdqsort、std::sort及适用的计数/频数强基线。同一数组配对、串行计时，明确输入复制/分配/学习/输出/析构是否计入；正确性对照放在计时之外。保留逐输入逐算法原始数据，报告T(n)、T(n)/n、相邻规模比、至少一种波动范围；若拟合指数，注明有限区间和不能据此证明渐近阶。针对真实实现给出时间/空间界，区分固定64位字长与可变位长，以及选择器所包含的所有后端。比较排序后端的最坏界不可被基数分支的线性界替代。

## 第二单元：决策开销与误选

以公开根模型、覆盖预检及完整排序后端为起点，选择一项有明确成本机制的低开销决策改进。将建模样本、验证样本、实际全量残差检查的职责分开。样本看似规则不等于总体规则；检查等距采样别名、未采样位置污染、簇与异常位置变化，区分自然输入与为机制构造的对抗输入。允许研究随机分层、独立验证或预算保底等替代，但不预设哪种必须胜出。

所有路由都必须对完整原输入给出正确输出，不能删除未采样值、用抽样正确代替全量正确，或者把事后逐条件赢家当成已实现选择器。度量误选损失与决策自身费用，并和直接调用强基线比较。参数校准和最终新输入评价分开；冻结的是实验可复核实现，不是禁止后续数学修正。新证据允许修改方法，但应标明新的评价批次。

## 交付与研究判断

交付可运行源码、输入生成协议与种子、原始计时、完整输出校验结果、必要的内存/未定义行为检查或精确未执行说明、时间空间推导、正负例和一个明确未决点。保存到本仓库任务自有成果目录并给不可变链接；沿用普通项目贡献许可，不携带凭据、机器秘密或私有对话材料。

成功不是必须更快：明确划出可复现收益条件、给出一般上界或实质误选反例都可形成有效成果。若决策费和错误路由成本持续吞掉收益，记录适用域/负结论，停止堆叠同机制规则并转向有新信息的备选；不以没有普遍优势为由丢失局部结构发现。若第一单元产生具体可检验下一步且仍在本任务范围内，直接继续，不等用户说“继续”。若遇到权限或环境阻断，保全已得材料并明确缺项，其他独立数学工作仍可推进。

数学状态保持作者侧观察/证明的准确范围；任务发布、计时通过、对照一致不等于被独立接受，更不授予Working Truth或Foundation变更。
