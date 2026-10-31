# PREFIX-396 — 实际执行、原始证书、来源、权限、接续

日期：2026-10-31。工作属性：本对话作者侧 portable research（静态外部辅助复三振幅模型）。结果是研究证据，不是正式 Task Result、独立审查或 P000/X6 证明。前置是已在本仓库存在的 PREFIX-395 精确六源示例和通用六次约化，本轮独立重建通用恒等式并增加完整联合噪声盒。

**固定输入版本**：
- GLOBAL_KNOWLEDGE_V1 main@77bab1fc42ec5a2c4e2bc09c748a1cbb753df4a0；读取规范 00_BOOTSTRAP.md / OPERATING_MANUAL.md、P000、ACTIVE 世界观、数学研究及 BRC 优先规则。
- Enterprise Math main@b0b289e4d42cd5df4831fc990910c9d39e622e9b；读取 PORTABLE_RESEARCH_PROTOCOL.md、current_control_authority.json 及前置 PREFIX-395。
- GitHub 实际用户 awdawmip。原生 Enterprise Math MCP 状态 research_authority_granted=false，活跃 Task/Owner 列表查询返回 CONTROL_QUOTA；没有新的 CLAIM、open、Result 或独立 Reviewer 身份，当前 owner 未能从原生服务核实。本次通过普通 GitHub 文档保存，但不冒称原生权限。

**实际本地执行环境**：Python 3.13.5；SymPy 1.14.0；有理区间检验只用 Python 标准库 fractions.Fraction，任意有限中间分数均准确计算，不使用浮点判符号。

执行主证书，原样输出：

    CERTIFIED_RAW_INTENSITY_NOISE_RADIUS 1/10000000
    CERTIFIED_CU_MEASUREMENT_NOISE_RADIUS 1/200
    CERTIFIED_ROOT_INTERVAL_SIGNS [('-', '+', '-'), ('+', '-', '-'), ('-', '+', '-'), ('+', '-', '+'), ('-', '+', '+'), ('+', '-', '-')]
    CERTIFIED_CU_GAP_LOWER_BOUNDS ['659154499/20250500000', '8461233/8500000', '68638932421/34344500000', '39268283/45250000', '55224673999/5133000500000']
    FAILED_LARGER_RADII [('1/1000000', "('root sign', 0, '0?', '+')")]
    PASS_PREFIX396_ALL_SIX_REAL_SOURCES_UNDER_JOINT_RAW_INTENSITY_AND_CU_NOISE

执行独立 SymPy 检查，原样输出：

    PASS_PREFIX396_INDEPENDENT_SYMPY_UNIVERSAL_SEXTIC_DEGREE_AND_DETERMINANT

**代码和证据**：同一 research_notes 下的 prefix396_exact_interval_checker.py、prefix396_symbolic_sextic_checker.py，均为可执行的 UTF-8 源码。作者实际本地执行同算法的完整本地程序并保存了完整日志和 JSON 机器结果。远程两份源码由 GitHub connector 创建并回读，Git blob SHA 分别为 88659b639b714a17e59e60cad9ed5e1ac0ee213e 与 e35f9b6d7da546ae6365510ff99e9efea5a6a25b；远程程序与本地记录的文件字节排版不完全相同，不将两者宣称为字节完全一致。实际运行证据只对已执行的本地版本负责，远端版本的执行仍可由未来消费者直接复核。

**数学认证范围**：全部五维强度立方体 |Ij-Ij0|<=1/10000000，外加单相干量绝对误差 <=1/200；每个真强度向量有六个全局相位不等价规则来源、没有额外奇异或 Cayley 无穷源；六个来源标签的相干观察包围集合在整个强度盒上两两不交。证明包含解析约束归一化、通用六次多项式恒等式、完整区间 IVT 符号、D2 严格非零包围与间距证书。10^-6 未被本次保守实现认证不等于反例；没有证明最优联合噪声半径，也没有给定任意带噪读数的完整可实现性算法。

**BRC 来源保持**：保留六个带相位来源与 Port 标签。Cu 的充分性只适用于上述一个六分类观察任务和误差预算，不授予删除其它干涉/来源结构的权限；没有运行原生 typed BRC 或完成 P000 原生模型对应。

**后继最小研究单元 PREFIX-397**：中心化/预条件根盒尝试扩大 ξ；给定不确定强度与 Cu 读数，构造真实来源集合的双向可实现性证书，而不仅是单向拒判/标签分离；研究超过最优标签间距阈值时的精确不可辨识反例。正式纳入任务状态机与独立审阅需由真实当前授权者处理。

状态：GITHUB_PUBLISHED / AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING。GitHub 文档回读是存储成功，不等于数学接纳。
