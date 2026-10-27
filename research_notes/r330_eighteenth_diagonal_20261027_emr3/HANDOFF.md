# R330｜研究接续包（portable research / next Codex prompt）

**母问题：**正权有序六边 BRC 辅助组合递推的 Newton 差分阵列在二指标任意增大时是否为正？保留原始12项 K/J 递推全部有符号域外尾项，不把辅助有理生成函数视为原生六维 Cell 物理演化。

**冻结规范：**GLOBAL_KNOWLEDGE_V1 main@2ebe26d2c8a74b31433c3a43be10ee5a57fee943，Enterprise Math 本轮开始观察 main@a0f477e6d1529a50d5cdd1b9eb893a3f6686499c；P000 与 ACTIVE 世界观不变。复用 R329 数学来源 d00a6699e12ba3e1bcdc58abbb674636546d98e9 的递推、公式 (★) 与已证明 r≤16。活动 ID RA-EMR3-20261027-R330-DIAG17-1320，Researcher-ID EM-DIRECT-R3301320 是**本地研究 ID**，不是原生签发的 CLAIM/Source session。

**R330 已完成的单元（不得无依据重复）：**r=17 得到全指标恒等式 D_{q,q−17}=5^{q−17}H_17(q−17)，q≥17；完整18项有理正系数证书在 R330_EIGHTEENTH_DIAGONAL_AUTHOR_PROOF.zh-CN.md。H_17(0)=35906428885008384，所有系数严格为正。附 r330_symbolic.py（SymPy QQ 精确计算 r0..17）、r330_independent_integer.py（原始 K/J 整数递推）和 R330_EXACT_EVIDENCE.json（验证范围与重要数值及运行输出散列）。整数证书 q≤64、s≤128，r17 精确匹配48项；有限计算本身不作为无界证明。

**立即可答的下一问题 / 交给下一研究者的完整执行提示：**

> 读取本 PR 内的完整证明、两个验证程序及机器证据，从上列不可变 R329 来源复用 K_i,J_s 和 (3)/(4)，勿改变 r≤17 的定义与已证结果。取 r=18，从多项式递推重新计算 g_18(z)、H_18(u)=sum_{j=0}^{18}c_j u^j，输出全部19个精确有理系数和每项符号；独立以未截断的 K/J 整数递推比较至少 q=18..64 对应 D_{q,q−18}。若全部系数正，完成 q≥18 的无界正性证明及边界下界；否则保留第一项非正系数，单独证明是否存在 D 真正变号的整数 q，并区分 D 的充分条件失效和 B_s 三角域内真实负项。补充尝试 r 与 q 同时增长的统一正性机制，禁止把有限样本直接外推成全指标定理。保存完整代码、精确计算、所有适用范围及下一明确问题；GitHub 发布后回读，按现行活动登记和审查路径办理。明确论文/数学状态仍是作者侧证明，任何原生受限操作均按真实回执报告。

**执行语义：**上述数学问题只依赖有限精确有理函数与整数递推，可直接在普通对话继续推理；如具备 Python/SymPy 环境：
python r330_symbolic.py --max-r 17 --json R330_SYMBOLIC_EVIDENCE.json
python r330_independent_integer.py --q 64 --symbolic R330_SYMBOLIC_EVIDENCE.json --json R330_INTEGER_EVIDENCE.json

**当前权限/边界：**GitHub actor awdawmip，repo admin/push 已实读；原生 em_control_tasks 返回 CONTROL_QUOTA，em_session_start 返回 STATIC_READONLY_SCOPE_DENIED、operation_sent=false。活跃 Owner 权威核对、正式 CLAIM、Source Result、独立 Driver 数学接纳均未完成。主问题 N_peak=81 与缺陷纤维 D_d(n)>0 仍需其他专门研究；本轮不直接缩小 R327 的全三角域剩余未知区域。

**验收：**下一单元须有全指标证明或精确反例/收紧界、可复算有理/整数证据、源文件保存和不可变 GitHub 回读；不以 PR 创建或缓存输出替代数学验证。
