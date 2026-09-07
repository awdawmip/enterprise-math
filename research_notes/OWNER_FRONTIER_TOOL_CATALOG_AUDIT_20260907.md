# Owner frontier 候选工具目录：独立合同与检索审计

状态：`SEMANTIC_AND_ROUTING_AUDIT_PASS / FINAL_SOURCE_BINDING_PENDING`。2026-09-07，ANCHOR_EXPOSED 内部帮助；不是正式 task、claim、Driver/Steward 接受或新 family 认可。

审计对象：`research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json`。初读 SHA256 为 `9674211ecd509e3e6776c95f9f1023582f81dc83a8ec410f24012248d8d4f788`；下列实质修正由 root 完成后，本助手复核的语义版本 SHA256 为 **`47d8d4908e3bfbfb7303b830e7c19858211e912fdbf71ada19f4641bff488662`**。本助手未改 catalog 或任何实现。

本报告冻结时，18 项尚未填 `source_sha256`；平方壳独立审计 `OWNER_SHELL_LENGTH_INDEPENDENT_AUDIT_20260907.md` 尚未落盘，root 已声明另代理正在完成。故这里不声称最终来源链已封闭，也不把预先填入该路径当作已读取的证据。发布前须由根代理确认该文件真实存在、结论适用，并以最终校验器绑定当前源 hashes；若数学源码或合同改变，不能只补 hash 沿用本语义结论。

## 1. 发现与修正闭环

### 1.1 一般区间工具只先认证负惯性指数

初稿把 `candidate.certificate.rational_interval_inertia` 写成整个区间族的 matching inertia，强于实际 API。`inertia_certificate.py:304–319` 比较 `M-delta I`、`M+delta I` 的负指数；其相等给所有输入区间矩阵的同一负指数，尚不自动给非奇异性或完整惯性。

使用真实 `certify_interval_inertia` / `verify_interval_inertia` 的独立最小检查：

```python
bounds = [[{"lo": 0, "hi": 1}]]
labels = ["x"]
```

结果：两 API 均给 `CERTIFIED`、`negative_count=0`；minus 惯性为 `{negative:0, zero:1, positive:0}`，plus 为 `{negative:0, zero:0, positive:1}`。区间含零矩阵与正矩阵，完整惯性显然不恒定。源码合同正确，问题在初稿索引的概括。

修订已明确只固定 negative index，完整惯性另需严格端点证据，并保留 `[0,1]` 边界。RH N8 具体结果仍可单独登记 `(8,0,24)`，因它有该特例的完整验证来源；不得从通用 `CERTIFIED` 字样反推这一额外结论。

### 1.2 路径 verifier 的 kinds 边界

真实 `verify_port_series` 只独立枚举/核对 `WALKS`、`ENUMERATED_WALKS`；原始 `EXCURSIONS` 返回 `UNVERIFIED`。修订目录已明确，未宣称对 excursion 记录存在未实现的独立 first-return verifier。`coefficient` 仍只是已计算结果的方便读出；外部 COMPLETE 标签不替代独立核验。

### 1.3 工具 family 不能仅由同名词汇推定

复核 `enterprise_toolbox_registry.json` 的实际合同后提出并确认以下修正：

- Phase I、区间负惯性改为 `family_id=null`、`CANDIDATE_NOT_TOOL`；T2 只作 `NOT_APPLICABLE` 比较。T2 的 independent-block max-law 不证明任意矩阵 LP 或谱惯性。
- 稀疏稳定性、最小 weighted trade 改为 `family_id=null`；T4 只作 `NOT_APPLICABLE` 比较。源证明实际使用 owner 切片/支点引理与正 BRC 边缘质量律，未调用 T4 finite-fiber capacity/minima。
- 查询计划、含噪拟合归到真实 T0 consumer 与已调用的 owner solver/observer，不将 covering 词汇等同于 T4 定理，也不将 LP 证书等同于 T2 max-law。
- PP m3 平方障碍改为 `family_id=null`；T1 只说明有限差分对照，普通幂矩障碍由经典平方正性及原模型系数承担。
- 路径赋值谱保留真正相关的 T1 计数/赋值与 T0 histogram；移除未执行的 T5 supporting/matched 声明。普通数字进位一词不能代替调用或明确应用已有 precision 接口的证据。

这些是来源与语义修正，不是否定对应结果，也不要求建立替代 family。

## 2. N 的两种含义与实际 API

目录的两个 N 已正确区分，不能跨条目直接传递：

| 条目 | 输入 N | 所观察的对象 |
|---|---|---|
| `candidate.x6.shortest_path_valuation_spectrum` | 最短事件长度 `N=sum(abs(z_i))`，API 参数名 `radius` | 该 L1 壳上的 signed 端点，按 active-axis 数与 `v_p(N!/prod(abs(z_i)!))` 统计 |
| `candidate.x6.quadratic_shell_max_shortest_length` | 平方读数 `N=sum(z_i^2)` | 平方壳上最大最短长度 `U(N)` 及一个达到它的 raw 端点 |

真实小检查，使用源码当前 public API：

```text
signed_valuation_spectrum(25, 2): radius=25, endpoint_count=5291820
upper_length(25): 11
construct_endpoint(25): (3,0,2,2,2,2)
verify_endpoint(25, endpoint): valid=True, actual_norm_squared=25,
                              actual_shortest_length=11
```

此检查验证接口含义和一个实例，不替代 all-N 证明或尚待落盘的平方壳独立审计。目录也正确区分辅助中心 `b=floor(U/6)` 与实际 common-depth，未引入第七空间轴。

对列出的 Python 源进行 AST 对照：18 项共有 **44 个 API 名称出现项**，全部在各自列出的 `.py` 文件中找到定义。不是仅凭自然语言名称猜测 API。实验接口的必要依赖仍要随冻结 source snapshot 消费：recovery 的 SymPy 与 owner Phase I/observer；histogram realization 的 observer/scout generator；nonlinear channel 的原 geometry kernel；shell 的原 signed native modules；各 BRC consumer 的 repository `src`。只复制 shard 可以检索，不能保证执行这些依赖完备。

## 3. 18 项的独立复用价值

| 条目尾名 | 保留理由及分类边界 |
|---|---|
| `raw_joint_observer_recovery` | 全20 raw 观察导出与≤7支点唯一恢复；不恢复 branch 身份 |
| `rational_nonnegative_phase1` | 独立原方程 primal/Farkas verifier；一般候选，非整数可行器 |
| `budgeted_noisy_recovery` | 明确 carrier/残差预算的编译器；不替代最优拟合或真值前提 |
| `integer_histogram_realization` | 逐精确权重整数层与窄均匀二值谱；不把 rational relaxation 当整数解 |
| `finite_reverse_step_port_monitor` | 聚合前保留有序词上下文及独立有限枚举；不重复泛化长度/直方图工具 |
| `shortest_path_valuation_spectrum` | signed 端点的 active/prime-valuation 谱；明确删去 coprime unit 与标签 |
| `minimum_raw_query_plan` | 任意静态 Q 的保证分类与原表反例；不是全20恢复器重命名 |
| `rational_interval_inertia` | 一般有限有理区间的负指数证书；区别于具体 RH 输入来源证明 |
| `n8_reference_eta09_inertia` | 已冻结特例的正负边界，避免把该 reference 再当正矩阵；仅 RESULT_ONLY |
| `finite_exchangeable_factorial_observer` | 有限差分到实际 exchangeable-word BRC；零 beta 不生成正分支 |
| `finite_power_moment_lift_obstruction` | 纠正有限差分到 ordinary power measure 的错误消费；不否定修正后的有限 BRC |
| `nonlinear_channel_gate_quotient` | 去掉线性假设的 q=f∘L 与可验 gate witness；不是真实 A_i-word 可达性 |
| `sparse_marginal_stability` | noisy consumer 的有界误差前提；保留未解锐常数区间 |
| `weighted_minimum_trade` | 关闭八正点/多负点的错误后续路线；不证明最佳稳定常数 |
| `quadratic_shell_max_shortest_length` | 固定平方壳的最优长度与构造；不同于固定端点旧长度公式 |
| `common_depth_first_return_tail` | native 归一化步律的无条件双侧首返渐近；不是有限 histogram 证书 |
| `two_sided_reciprocal_cusp_tail` | 可独立用于其他非消失 Fourier 符号的数学接口；比上一具体步律 consumer 广 |
| `energy_domain_correction` | 阻止沿用错误 full/tail/absolute-Gram 参数域；不是 RH 证明 |

未发现只是为凑数而无实际后续 consumer 的记录。具体结果、反例和通用候选分开有用；它们不能因此统称“18个已接受工具”。

## 4. 检索真实输出与最小修复

使用现有 `method_suggestions`（`--json methods` 的同一调用入口），仅打印 ID/rank，避免大输出截断。下列自然语言查询的目标均排第1：

```text
quadratic shell maximal shortest length
signed shortest path multinomial valuation spectrum
sparse marginal recovery seven support
integer histogram realization Rao
rational nonnegative feasibility Farkas
symmetric interval matrix inertia certificate
finite completely monotone factorial moments
nonlinear reversible channel quotient
minimum three axis query plan
common depth first return tail
Fourier reciprocal cusp derivative jump tail
```

初稿查询 `finite path reverse step port monitor` 把目标排第14，默认 limit=12 漏掉。root 按本审计建议只向该条目增加 `reverse step`、`port monitor` 和该完整查询的 triggers 后，复核已排第1；未改 router。

当前 router 的 `TOKEN_RE` 只提取 ASCII，纯中文 need 为空时提前返回0；因此纯中文 `含噪三轴拟合`、`平方壳最短词长锐界`、`共同深度首返尾律` 实测全部返回空列表，不能把存在中文 triggers 描述成已经支持纯中文搜索。现有可用路径是准确 API 名或中英混合查询，例如 `reverse_step_monitor`、`平方壳 quadratic shell maximal shortest length`、`共同深度 common depth first return tail`、`含噪 noisy recovery residual budget`，均目标排第1。root 已将该限制写入共享说明；本工作包不扩大为 router 改造。

默认 `methods` 文本输出隐藏 status/boundary，故共享指引应保持 `--json methods` 或 `--json coverage`。索引只读取当前 checkout；旧分支不会自动看到另一个 Draft PR。目录明确指向包含 shard 和依赖的不可变发布快照，main replay 是另一个受门禁约束的动作。

## 5. 状态、来源与冻结边界

18项均为 `TOOLBOX_INTEGRATION_CANDIDATE` status；classifications 使用现有 `DOMAIN_OPERATOR`、`CANDIDATE_NOT_TOOL`、`RESULT_ONLY`。目录顶层正式 acceptance 与 official claim 均为 null；`new_global_tool_family=false`、`foundation_mutation=false`。内部审计没有被冒充为正式 Driver/Steward 接受。目录 main 落地后也应保留这些数学状态，不能把 routing publication 当 proof promotion。

已读并据之判断的关键实现 SHA256：

| 文件 | SHA256 |
|---|---|
| `tools/enterprise_toolbox.py` | `321625e6e2d2fa95a25c81d3bc2588cee1b26b16c70d10dd28f4f0da3c2b49b0` |
| `enterprise_toolbox_registry.json` | `f2281d98a05aa23feaa4b163e7ab37a41f30ecbb84f499b0b820443bcfa97170` |
| `experiments/owner_rh_reference_20260907/inertia_certificate.py` | `eedb0fbdfebfec478a18f418fcf8b3eb386903870bea1ae9b9948afce1e67bc5` |
| `experiments/owner_path_monitor_20260907/path_monitor.py` | `86c7e3e751f1f4817ed836b397b3779dc65bdaf0a10da71c0ee1e434150daccd` |

准入依据是 `ENTERPRISE_TOOL_INVOCATION_PROTOCOL` §8–9、`tool_invocation_policy.json` post-return harvest、Common Surface 状态纪律；本报告只核对 candidate 路由、源合同及有限实测，不重审全部18项分析证明。除本报告外未写任何文件、未改源码或远端、未创建正式评审。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
