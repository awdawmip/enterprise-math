# RB 当前卡点：原生工具复用与证书表达缺项

当前应先组合已有能力，尚无足够证据开一个新工具族。本轮以 Driver 辅助身份核对 main `745ee59a554d79c220d0b23b9d8ee51fcec8022a`，并只读已公布 v2 `12ab6940f1a769efc8b3c75472d407a89a17f2ca`；不构造候选、不执行数学、不作正式 Driver 判词。v2 仍是 `INCOMPLETE / SOURCE_EXPOSED`，不能退回 v1 的旧未完清单：它已给出域基、全 ODE、共同基点、两种度数与未平方微分的论证及精确检查绑定；本轮不独立重证这些主张。其明确剩余项是四张完整特殊纤维的赋值、平方类/半点定位与下降，以及独立检查和完整回传。[v2 证明](https://github.com/awdawmip/enterprise-math/blob/12ab6940f1a769efc8b3c75472d407a89a17f2ca/research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909/exact_map_proof.md)

已按当前路由执行一次 canonical coverage：

```text
python -B -X utf8 tools/enterprise_toolbox.py --json coverage "BRC Spatial6 operation safe quotient rational map basepoint valuation square class descent"
```

实际 exit 0、0.753 秒，`REUSE_CANDIDATE_FOUND`。首匹配 T6；方法首匹配 `t0.weighted_brc_newton_fiber_quotient`，同时命中 T0、T5 和已有 Newton observer lattice。原始输出与 argv 保存在 `lookup-receipt.json`；AST/docstring 解析有既有 invalid-escape SyntaxWarning，未阻止查询。此处只有匹配与接口审阅，不是工具执行、更不是全库缺失证明。路由、P000 和此前核过的 T0/T5/T6 等 13 个文件逐字相同，旧三次 lookup 不重跑。[调用合同](https://github.com/awdawmip/enterprise-math/blob/745ee59a554d79c220d0b23b9d8ee51fcec8022a/docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md)

| 已有能力 | 本任务可用强度与限制 |
| --- | --- |
| `T0_BRC`：`exact_arithmetic.py` 的未求值 DIV/ROOT 与明确求值 trace | 可保留符合其非负整数/正分母类型的子问题；不能把一般曲线函数 N/D、复数嵌入或选支根直接塞进整数节点。v2 明载实际 BRC、整数除法、根求值均为零，实际调用的是已存在的整数多项式 API；这不是宿主不能运行 BRC 的证据。 |
| `T0_BRC` 的 `brc_weighted.py`、`brc_rational_holonomy.py` | 正权数量/总量不可抹掉复系数抵消与分支符号；正有理素数赋值骨架也不等于带常数类的曲线函数域平方类。它们对这些替代用途为 `NOT_APPLICABLE`。 |
| `t0.weighted_brc_newton_fiber_quotient`、`t0.weighted_brc_newton_observer_lattice` | 已有固定 Newton scale、multiplicity、有限 Taylor 位置的全残差合并、观察等价、核及冻结有限日程观察工具。不能重新命名这套 jet/quotient 思路为创新；它不替调用者选局部参数、根、尺度或证明 Taylor 范围穷尽。当前代码输入为 `int/Fraction` 及冻结有理根日程，不直接接收 RB 的代数系数域/曲线点局部环。忠实域基展开能否在本任务整数/未求值合同下组合，须显式适配证明，不能默默改输入类型。 |
| `T6_OPERATION_SAFE_QUOTIENT`：`operation_quotient.py`、`predictive_quotient.py` | 直接复用“先声明观察和未来操作，再论证下降”的合同。软件处理声明的有限域/操作或有限日程；不自动保留平方类单位、目标纤维标签、Y 符号，也不把有限代表提升成 1980 个参数族结论。 |
| `T5_PRECISION_REFINEMENT` 与当前进取坐标入口 | T5 的有限整数尺度/余量重构并不提供代数曲线恒等式或下降证明。P000 的完整原生 Cell 是有锚点的六有符号轴扭子，坐标 observer、common depth、BRC/history 装饰分型。RB 的 R,t,w 属声明的代数模型，不因被编码就变成原生轴/动力学。P000 可指导哪些信息不能丢，不是曲线工具已覆盖的证明。 |

本次未发现“已有足够实现、只是当前宿主跑不了”的实例，因此不填写 `REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE`。现成 Newton 工具的 `Fraction`/冻结有理根接口与本任务承载方式尚未接合，属于明确的实现/输入适配边界；不是证明不存在对应数学能力。局部 v2 checker 已能做 `normalize/evaluate/norm_t/twice_delta` 与特定几何证书，扩充其四纤维输出本身也是正常任务实现，不自动构成数学创新。[v2 checker](https://github.com/awdawmip/enterprise-math/blob/12ab6940f1a769efc8b3c75472d407a89a17f2ca/research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909/check_exact_map.py)

仅保留以下两个**相对于已读接口与 v2 输出可证的缺项**，作为后续复用/扩展评估候选；不登记为全局 `CAPABILITY_GAP_CONFIRMED`：

1. **完整纤维的局部证书还未闭合。** 现有输出记录 N 的零点阶、共同最小阶及无穷点 pole orders；v2 明说尚未确定 B0 处 D0 的个别阶和消去后 X 值，更没有四纤维完整结果。所需输出必须连结每点/局部参数、分子分母个别阶、消去量、剩余单位与纤维标签，并带穷尽性依据。最小价值检验：用已有 B0 与 O 两个源点，保留 common minimum order=1 与 D0 的个别阶的区别；原表示和带共同因子的等价表示应产生同一最终纤维结论，遗漏单位/个别阶的输入应报告不足。这里只提出验收需求，未选择新因子、未执行检验。若结果只是把现有计算填入 JSON，归 `DOMAIN_FACADE`/任务实现；只有证明可复用的观察保持/组合律，才有 T6 或既有 Newton 子工具扩展价值。
2. **目标重标、平方类常数和下降的联合证书还未给出。** v2 指明原式空纤维为 1、lambda，而旧 RR 的空 infinity 规范需同时搬运标签和 Y，不能只对 cover 数量或赋值奇偶作商。最小价值检验先复用 v2 的 Y/-Y 对照：平方目标方程相同，未平方 phi 观察必须区分；再要求原四纤维到允许规范的完整标签/常数类/系数域及嵌入/半点数据可回放，删去任一必需证据就拒绝下降结论。这是输入完整性与 T6 操作语言的具体缺项；T9 的命中也不自动证明 Galois/原域下降。未指定合法变换、未提供完整单位类之前，不得开始编造其证书。

这两项都不需要先发明“通用曲线求解器”。本轮能确认的价值方向是：在进取数论既有观察保持原则下，让证书明确携带后续操作真正需要的分型信息，并给出信息丢失的拒绝见证。普通多项式归一化、改名、包装、宿主迁移或多跑算例均不足以成为新思想/工具族。所有基点/度数、周期/同调指数、1980 族分类及正式接受的证据强度仍以各自源合同为准。

本流程到此停止；没有 FREE 候选或新数学研究。若 Root 决定进入构造，须另用真实研究者身份、当前 session 的 LIVE 轻量 activity 与 EM 来源持久化；TASK 路线还要真实 task/publication/claim/ER/authorize。不得将本 Driver 记录借作研究者登记，或把已看过工具和来源的任务包装成独立 FREE Phase A。原始来源 SHA256、Git blobs、当前一次 lookup 与旧证据绑定见 `review-receipt.json`。

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@3ad395d / GLOBAL_KNOWLEDGE_V1
