# 单正支点 raw X6：有限整数 / DIV 消费者

范围：`ANCHOR_EXPOSED / OWNER_AUXILIARY_PACKAGE`。这是已独立检查的单正支点纸面证明的有限消费者，不是正式 task、claim、Driver review 或 Foundation 晋升。

## 先冻结的输入与输出合同

输入是同一共同 anchor、同一带标签 signed 六轴 chart 中的两个有限正质量总体。每条输入为原 `Spatial6` 和严格正的 Python 整数分子权重；可以为空，也允许不同输入分支落在同一 Cell。每条正权输入可解释为该侧正 BRC 总体的一条带权空间端点读出。两侧分别保持正权，之后才聚合空间质量并计算分析差 `f=mu-nu`；负号不构造负 BRC primitive。空间读出不恢复路径历史、branch 数或 CWM 最大权。

两侧共用既有 facade 构造的未求值质量单位 `division(1,s)`，s 是严格正整数。不会约分或计算这个单位。任意输入的共同 anchor/frame 是调用前提，不能从一串整数推断外部来源是否已经完成坐标运输。

`audit_case(case_id, mu, nu, denominator=1)` 检查分子类型和正性，按 Cell 聚合、消去重合质量并删除零项，再要求 `p(f)<=1`。原两侧都可有多个正支点；限制作用于聚合消去后的差。非正差与零差单独处理。

输出保存原两侧正权、消去账本、Jordan 正负质量、全部二十张带轴标签的完整 raw 边缘、L1 分子、单表恒等式以及整数比较 `20*L1<=3*D`。等总质量时另检查 `10*L1<=D`。常数、共同单位、质量及非零差比值只序列化真正的原 `DivisionExpr`；零差的比值是 null，不能构造 `DIV(0,0)`。这些 JSON 节点是既有表达式的编码，不是新 rational 类型或求值器。

非零差输出两种 sharp 取等条件及其与实际整数相等的双向一致性：一般情形要求 `N=2P`、所有负点只改变一个轴、每轴合计满足 `6*b_i=N`；等质量只要求单轴偏离。零差的数值相等另标 `TRIVIAL_ZERO`，不冒充非零 sharp 比值。

raw 三元地址可由联合 `(can3, min(raw))` 恢复。消费者对实际输入逐一调用原联合切片编码/恢复并检查；不以 can3-only 或两个分离直方图替代 raw 表。对角反例另外记录 can3-only 的信息丢失。

## 实际复用与明确未调用的边界

`COMPOSE_APPLIED`：组合既有已审单正支点证明、X6 坐标接口和 exact facade，不建立新工具家族。

- 原 `x6_signed.py` 的 `Spatial6`、`step`、`ALL_SLICES`、`hidden_slice_coordinates`、`from_hidden_slice_coordinates`：构造/验证实际输入与联合地址。负空间方向是合法 signed 轴方向，与负质量不同。
- 原 `signed_brc.py` 的 `support_size`：核对负支点与正支点的实际坐标区别数；`shortest_event_count`、`spatial_norm_squared`：核对所使用 sharp 见证的 signed 单位邻接。这些调用的函数体及 `_z6` 只使用整数；没有为了贴标签计算无关多重性。
- 原 `exact_arithmetic.py` 的 `division`、`DivisionExpr`、`compare_divisions`：构造未约分表达式与整数交叉乘比较，不请求 quotient、remainder、root 或数值近似。

使用原 canonical import：`enterprise_math.exact_arithmetic`、`x6_signed` 和 `signed_brc`，保持 `DivisionExpr` 与原生 Cell 类型身份及互操作，不复制算术函数或创建第二份私有类型。`enterprise_math/__init__.py` 会连带初始化旧模块，含历史 Fraction 状态；本包不声称这些初始化依赖已经迁移。它们不作为本次主账本的数据来源。

`signed_brc.py` 顶层仍导入旧 `Fraction` 名称。其 `endpoint_weight`、所有多重性函数以及旧 Branch / WeightHistogram / CWM 均未用于主账本或兼容回验，也没有登记为 `REUSE_EXECUTED`。本包没有 `LEGACY_INTEGER_COMPATIBILITY_ONLY` 回验结果。一个限定的动态调用检查覆盖导入完成后的主账本，拒绝其进入旧有理计算或 quotient/root 求值。选择的纯整数调用经过实际验证，不据此声称整份旧模块已经迁移或静态 PASS 具有传递性。

由于没有实际除法、余数或根读出，BRC 求值 trace 列表为空，含义是 `NO_EVALUATION_REQUESTED`。后续若要求这些读出，必须使用原 facade 并保存其实际 trace；本消费者没有提供求值捷径。

## 有限例与拒绝边界

仅使用固定的十二例：3/20 sharp、等质量 1/10 sharp、signed 加平移版本、N=0、q 处部分消去及同 Cell 分支聚合、q 处完全/过量消去后的非正差、零差、负投影碰撞、can3 对角丢失、N=2P 但轴质量不均的严格例、轴线上分拆质量仍 sharp 的例。

拒绝检查针对超出 `p<=1`、零/负/布尔分子、非法坐标和非法共同单位。它们不扩大数学枚举。辅助 (n,k) 公式不在执行器中推广，一般 p<=7 仍不在此单元范围；未使用 LP 或重复旧搜索。

## 执行与复核

在仓库根目录，以 Python 3.12 执行：

```text
python -X utf8 -B experiments/owner_one_positive_stability_20260908/check_one_positive_stability.py --write
python -X utf8 -B experiments/owner_one_positive_stability_20260908/check_one_positive_stability.py
python -X utf8 -B tools/check_exact_arithmetic_policy.py experiments/owner_one_positive_stability_20260908/check_one_positive_stability.py
```

`--write` 仅写本目录 `certificate.json`；默认模式重新计算并要求保存的 JSON 字节完全一致。执行器先核对固定来源 SHA，最后再次核对，拒绝在来源漂移后沿用原证据。输入、完整表、条件、预期有限例与拒绝结果均保存在 JSON，来源 SHA 也随结果保存。证明与独立审查记录保持原字节。

实际验证状态：`FINITE_CONSUMER_PASS`，Python 3.12.14。最终输入上完成 12 例、7 个非法输入拒绝、12 个原 signed 单位邻接检查、240 张 raw 表与联合地址检查，生成 JSON 后以独立新进程完成字节一致回放。V2 静态 gate 实际返回 `PASS (1 files)`。原 canonical `DivisionExpr` 类型身份保持；q 部分消去例原 mu 有两个正空间支点，消去后 p=1，验证计数发生在正确时点。

另在 TEMP 中做四个限定拒绝探针，均实际拒绝：主账本进入旧 Fraction 构造、请求原 BRC 除法求值、进入旧最短路径多重性、把 raw 投影替换为真实 can3-only 投影。前三项在函数体计算前被调用守卫拒绝，最后一项被联合地址一致性检查拒绝；探针未改任何源码。历史模块导入初始化不在该守卫范围，仍明确未迁移。

最初输入也通过了 V2/生成/回放；其后只增强共同分母类型验证，并在已有 q 消去例添加两侧完全重合的另一 Cell。以上最终验证是在这两个修改之后重新完成，不混用首轮 JSON。静态 gate 只检查明确提供的新 Python 文件；实际调用边界还须结合原函数审阅与执行证据，不把 gate 当作完整依赖合规证明。

Global-Knowledge-Sync: main@982a440 / GLOBAL_KNOWLEDGE_V1
