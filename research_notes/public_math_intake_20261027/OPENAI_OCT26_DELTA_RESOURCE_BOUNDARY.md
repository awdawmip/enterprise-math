# OpenAI 公开数学成果增量吸收：2026-10-27 冻结与资源模型审计

状态：`EXTERNAL_INTAKE_VERIFIED_AT_SOURCE / RESEARCH_NOTE_UNREVIEWED / NO_NEW_V2_TASK_PUBLICATION`  
本次作者：`Researcher-ID EM-DIRECT-69045B`，直接定向研究模式 `TASK_RESEARCH`；本地会话追踪键 `oct26-public-math-12ee0c868c2112c0`（**不是** ChatGPT 平台认证 ID，也不是 EM 原生 MCP session）。研究活动：`RA-PUBLICMATH-20261027-69045B`。外部源码已暴露，本文不作独立审核。观察时间：2026-10-27 UTC。

## 1. Frozen source pins / 先复用历史前沿

- `awdawmip/chatgpt-global-knowledge@07b8d313fe59948fcb976b9cdd7f6035656279f6`，入站读 `00_BOOTSTRAP.md`、`OPERATING_MANUAL.md` 及 EM/BRC/信息保真/研究活动偏好；EM 起点 `awdawmip/enterprise-math@55531a03bbe5b3b1d0dc8c5bd3c9c94901e89d02`，之后只读源码检测与自己的活动注册使 EM main 前进，不追认历史最新控制状态。
- 原已核验 OpenAI 数学 repo pin `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`；本轮实际 GitHub ref HEAD `openai/math@7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a`（2026-10-26 21:18 UTC），GitHub compare 显示从旧 pin **ahead 2** commits；变更文件列表 REST 比较接口截断在 300 条，不作全量变更数量断言。
- 官方公告：2026-10-26 `https://openai.com/index/building-scientific-understanding-with-academic-communities/`；官方版本历史 `https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/history.md`，blob `ff52ee4dba7ac9a2f145b934f282f582525a4c0d`。
- 主仓 `README.md` blob `cc5b0a03bca6c742f045d683b6647a6f44ef2cae`、`CONTENTS.md` blob `7e1ed90ac5a666f1bbecb22027387c4ad79e9d03`：**721 manuscripts / 373 families**。README 表述“~42% top-line results formalized”；旧 2026-10-07 `300/719` 是旧时间口径，不转写为新的精确数量。
- 已获真实 V2 发布及 Result、独立 Driver 审阅的 family129：`RS-PUBLIC-MATH-129-REENTRY-SUMMARY-20261007` / `TP2-61D08EEA98B46ED15916` / `RR-9FFBBB42790CCECD2FF8` / `DR-9B722991A865BCD49B36`，`disposition=ACCEPTED`，最后一项仅该 frozen finite/tool/comparator scope 通过。其论文固定旧 `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`，**不**为本轮更新重跑/重复发布。独立母目标 `OBJ-PUBLIC-MATH-ABSORPTION-20261007` 在起点 Source generation `OG-9C0E1497D407F544BF64` 仍为 `OPEN`，现存定义为*有界首轮*有限/类型吸收，不自动获得无界新增研究任务授权或关闭。

## 2. 外部新增、修订与撤回边界

### 2a. 新增（OpenAI 的外部主张，不是 EM 证明）

1. **Local smoothing / Kakeya**：官方 10/26 声称用辅助偏微分方程在所有欧氏维数 `n >= 2` 建立局部平滑估计，进而涉及 Kakeya maximal/维数与 Stein restriction。声称产出 10/18、Lean 完成 10/19。对应 `lean/docs/079.md` blob `e6ea535832d6dfef60c539a2e0537b560c1b7108`、`lean/ComparatorChallenges/LocalSmoothing.json` blob `88c1e1c3368f66f9d64206a2b166a89bc87b4f9b`。6 个定理根名：`euclidean_local_smoothing`, `bochner_riesz`, `spherical_restriction`, `kakeya_maximal`, `kakeya`, `stein_square`。空间 `EuclideanSpace ℝ (Fin n)`，范数/测度/积分均为经典外部欧氏模型。
2. **ETH false / deterministic exact #SAT**：官方 10/26 声称 ETH 被证伪，产出 10/16、Lean 完成 10/17，已公开 Lean 和论文供 Impagliazzo/Paturi/Williams 组织的**独立解释/核验工作组**审查；不能把工作组成立等同其认可。对应 `lean/docs/378.md` blob `223bbe187394bffca8a2c7ba1656538bfba26e3b`、`lean/ComparatorChallenges/SubexponentialSAT.json` blob `d4cc9e7074e900c1aa6371151cfd234c121a0b82`、Comparator theorem `OAI.Algorithms.SubexponentialSAT.SqrtLogSpace.exact_count_and_sat`，实装 `lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean` blob `a69635a2492e06a26f2e33d4251edd1e21ba3332`。该 Lean 根声明固定 `k>=2`，全体规范编码 `k`-CNF，确定性原始机器准确输出 #SAT 和 SAT 位，时间 `(L+1)^O_k(1) 2^{O_k(n(loglog(n))²/sqrt(log(n)))}`，每个运行前缀访问纸带格数量 `(L+1)^O_k(1)`。**论文另声称** `(n+m)^O_k(1)2^{O_k(n loglog(n)/sqrt(log n))}`，在 `m<=Dn` 固定 `D` 时更强；不可把论文强式写为 `exact_count_and_sat` comparator 的形式化结论。
3. **Yang–Mills / QCD**：官方称 AI 有自然语言及 Lean 工作，但决定让独立物理工作组先解释，**暂不公开 AI 原始证明工件**。本轮无可核验 Lean source pin，不入 EM 原生定理库或新增可执行形式化任务。

### 2b. 更改/修订

官方 10/26 history 还说明新增 `The rational Hodge conjecture for CM abelian varieties` 的 Lean formalization；这**不是**修复 10/07 撤回的“split abelian eightfold Weil classes / Kuga–Satake K3 / K3-product rational Hodge”三篇。新的 Hodge Comparator 配置 `lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/main.json`，blob `7a3ee084f1de09a45618654cd1c11f2f0c8d878a`，定理名 `HodgeCM.hodge_conjecture_for_cm_abelian_varieties`；尚未对独立内核、目录依赖或现有 EM Hodge 线作独立评审。另修复部分 Comparator 配置、形式化，恢复六维 MUB 的 C++ 源、数值日志、Python 一致性检查器；这些是源/辅助证据，不是我们的重跑记录。
10/07 三篇撤回仍由 `history.md` 标为撤回，失效的证明不等于猜想反证，本轮**未发现 10/26 重新纳入三篇的证据**。

## 3. 实际 Lean 检查级别（必须严格区分）

- 看过 `lean/lean-toolchain` blob `ba8ebf2dbaf6a668cd2a0e086186d6d569b69ff5`：`leanprover/lean4:v4.34.1`；`lean/formalization.yaml` blob `372bcd714cd3a186a9139ac8e0f3318961fb2df1` 记录新目标/关联文件及 comparator。
- 两份 `lean/ComparatorChallenges/{LocalSmoothing,SubexponentialSAT}.lean` 都是**题面/challenge，含 `by sorry` 占位**：LocalSmoothing 6 个，SubexponentialSAT 1 个。这是 Comparator 题面预期，不代表实际 solution 以 sorry 通过。
- 实读 solution `lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean` blob `6def181857b8148d9dbaed288876a225ca9ddbfb`，所见 6 个根定理是对内部 OAI 模块中定理的 `exact` 桥接；局部文件未见 `sorry` 或 `axiom`。实读 `lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean`，所见根定理依赖 `compiled_exact_count_and_sat`；局部同样未见 `sorry` / `axiom`。**没有**完整转移依赖闭包审计、`#print axioms`、Comparator 执行、Lean 内核运行或独立复验，不能宣称已核验整套证明。两个 JSON 配置限制基础可用公理 `propext`, `Quot.sound`, `Classical.choice`，仅为配置要求，不是实际跑过的报告。
- 无自造公理/不以“文本无 sorry”推断无公理依赖。外部论文非 EM 已验收数学定理；前述“formalized”是 OpenAI 自述和源文件可见，不等于本会话的独立验证。

## 4. 有限、可复验数学信息增益与模型防火墙

**数学范围内的条件推导，不采纳尚未独立审核的定理：** 固定 `k` 的规范编码 `k`-CNF（每个 Clause 为最多 `k` 个、来自 `2n` 种带符号变量的有限集合；CNF 是 Clause 的 finite set），总候选子句数至多 `Σ_{j=0}^k binom(2n,j)=O_k(n^k)`。采用源码中的长度随整数线性增长的 `encodeNat` 与定界列表编码，有 `L=O_k(n^{k+1})` 的多项式上界。故如果 solution 所声明的机器与代价定理在规范输入上成立，`(L+1)^d=2^{O_k(log n)}`，且 `n(loglog(n+16))²/sqrt(log(n+16))=o(n)`，从而 `k=3` 的运行界确实是 `2^{o(n)}`。此处仅检查“**已声明目标 ⇒ ETH 不成立**”的外部数学/编码适用边界；不是对其前提完成独立核验。

**已有 family129 与新 ETH 结果严格不互斥：** family129 的下界对象是只读输入头、无可写工作带的确定性二向有限自动机，其度量为**控制状态数**；新 Lean `PrimitiveMachine` 有 `tapeCount`、Turing tapes、带位置/访问上下界的配置，并证明**多项式被访问纸带空间**（含写入）。写入的 `b` 个独立二值工作格可有 `2^b` 种内部配置；若后续操作/输出可辨认其差别，任何只保留当前有限状态数且丢掉纸带的摘要都需要先提供保持观察的商/纤维常值证明，不能把论文的时间/空间折成 family129 的状态数。反之，family129 的指数状态下界不否定一台使用多项式可写空间的 SAT 算法。这是**精确不同的资源类型**，不是宣称新的复杂度分离证明，也不提供通用状态压缩界。
- BRC 判别：如果探讨迁移，优先沿已有 T0/T6/T8 的布尔可达支持与未来观察等价关系工作，必须声明总体 `(F,input,working tape history)`、observer `exact#SAT/SAT`、允许未来操作、完整/有界时间视域、保留的路径/支路/可写历史；无 observer descent 证明不消去写存储。正质量 BRC 不等于有符号相消/量子幅值。工具处理暂记 `REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE`（本轮未运行 EM native formal/数值方法，不是能力缺口）。
- P000 的 `6D native space + separate 1D time`、无原生平面、三轴受限切片继续有效。LocalSmoothing 的 `EuclideanSpace ℝ (Fin n)` 与 `PrimitiveMachine` 皆是独立**外部比较模型**。没有明确定义 X6 嵌入/读出及未来操作保持归约时，不把欧氏局部平滑、Kakeya 或资源复杂度声称为 EM 原生定理。

## 5. 建议给授权 Owner/Driver 的唯一优先候选（当前仅 handoff）

### Mother question
OpenAI 10/26 发布的规范 k-CNF exact #SAT Lean 主根，按固定源码，能否获得一项**独立可复验**的“源命题—锁定依赖—内核/Comparator—时间/空间—EM 观察器”闭合证书？若存在不闭合项，输出最低依赖与最小反例/失败回执。避免以 10/26 宣传或 `sorry` 题面替代核验。

### Frozen inputs and scope
`openai/math@7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a`：`lean/docs/378.md`、上述 1 定理 comparator/solution、`lean/lean-toolchain`、完整 lock/依赖/实际命令。EM dedup 基线：起点 `enterprise-math@55531a03bbe5b3b1d0dc8c5bd3c9c94901e89d02` 的 family129 immutable V2/ACCEPTED review；工具 T0/T6/T8；P000/ACTIVE worldview 与 observer preservation。不得以旧 OpenAI 129 结果当新验收，也不得将有可写工作纸带模型和只读 2DFA 混同。

### Hard target and required outputs
(1) 逐字比对 `exact_count_and_sat` 与 paper 关于 m,n 的更强式和固定 k；(2) 审查 Main/Final 的全 import 依赖、`sorry`/自定义 `axiom`，执行锁定 Lean / `#print axioms` / Comparator（依真实授权工具环境）；(3) 给出源语言至标准 ETH 输入的编码长度/变量数资源证明；(4) 保留完整可写工作带及未来输出观察，给出向 EM T6/T8 的 exact typed bridge 或最小资源阻碍；(5) 形成独立署名审阅和真实 log/checker SHA/Source readback。该目标不要求复制/检查整个 721 稿仓库，不要求证明 P vs NP，也不提前把 ETH 的否定判为 EM 工作真理。

### Research value to preserve
将一条足以冲击复杂度文献的外部重大主张变为一个**可复核的前提链和资源类型证书**，避免把“发布/Lean 有文件/已运行/独立证明接受”混为一谈，同时保护 family129 已认可的有限结果不被重复开发。

### Success, kill, and return criteria
`SUCCESS`：独立核验准确命题及 Lean 可复现内核/公理/比较回执，或得到精确类型化的迁移阻碍证书；`PARTIAL`：锁定被卡住的最短导入/算法/配置步骤并回传 hash 与回执；`KILL/DEFER`：已知前沿完全重复或被不可补足的类型前提阻断。始终保留外部作者与贡献独立性。

优先单元只此一项；LocalSmoothing/Kakeya 留在第二顺位的**欧氏观察器/X6 嵌入边界核查**；Hodge CM 新 Lean 先向既有 Hodge 线做 prior-art 去重，再决定，不默认发新线；未公开 Yang–Mills 源不列为 Lean 执行目标。

## 6. 真实执行/权限/关闭状态与交接

- 已按本对话自己的**本地** `Researcher-ID` 与本地追踪键在 GitHub 项目 Source 创建、不可变 commit 回读研究活动 `RA-PUBLICMATH-20261027-69045B`；GitHub user `awdawmip` 对仓库具有 push 权限。此注册是活动观察，不授予研究 CLAIM、Review、Driver/Owner 活跃 DA 或本对话 Native session。
- 原生 EM 服务 `em_status` 实读 v0.6.11，backend Source pin 为 `enterprise-math@55531a03...`；当前连接客户端是 `sites-em-...-ro`、`research_authority_granted=false`、`executor_binding_configured=false`、`registered_session_count=0`；因此**本对话没有可证的原生 Driver/owner 发布授权，不创建伪 V2 publication、不发 CLAIM、不继承旧凭据**。有权限的 Driver/owner 应从自己全新原生 session/DA 恢复上述现存 family129 Accepted/母目标 OPEN，重新判定本轮外部增量是否纳入目标范围；需要扩展旧 Objective 时按原生修订/新 Objective 合同，按正式 V2 preflight+taskbook/record 同时写回并回读 receipt。
- 本文仅为自己的新源研究观察与可执行交接；**未**执行 Lean/Comparator、未获新结果独立审核、**未**创建正式新 Task 或完成母目标。历史三篇撤回保留。下一合法操作为归口 Driver 的 live review/parent intake / candidate publication gate；若本次研究审核因工具/权限拒绝，只停拒绝对应的 native write，不换身份绕行。

