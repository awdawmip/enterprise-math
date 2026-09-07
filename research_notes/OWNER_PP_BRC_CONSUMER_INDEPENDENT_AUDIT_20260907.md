# 有限 HCM → BRC consumer 独立审计

状态：`PASS_AFTER_IDENTIFIED_FIXES / AUXILIARY_INDEPENDENT_AUDIT / NOT_FOUNDATION`。

辅助工作包 `/root/stability_research`，2026-09-07；内部只读审计作者实现，未领取 Perfect Prime 正式线路、未创设 claim 或 Researcher-ID。Global Knowledge 沿用已验证租约 `main@4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563`。

**结论。** 本次范围内，一般 finite-HCM 等价、逐词正 BRC 适配、固定位置观察、带零位标记的系数观察及针对原 h 的独立证书核验均成立。初审实际发现的精确类型、额外字段、非法分母、迭代器和资源状态问题由作者修复，最终局部复核通过。结论绑定第 8 节源码 hash；不把有限阶乘表示升级为正幂矩表示。

## 1. 审计范围与复用证据

先读 `OWNER_PP_FINITE_MOMENT_INDEPENDENT_AUDIT_20260907.md`，确认原模型 m=3 的负平方已经由另一个辅助工作包绑定到原 cofactor 和 signed-secant 两条精确路径。本审计未重跑这两条路径，也未运行作者的 63 个 ensemble 全套。

本次逐段阅读：

- `finite_hcm_brc.py` 全部 public API、证书分支、精确数类型与资源处理。
- `run_finite_brc_checks.py` 及其现成 JSON，区分作者检查与本次独立检查。
- 现有 `src/enterprise_math/brc_histogram.py` 的 `WeightHistogram`、`from_counts`、`histogram_serial`、`histogram_recoalesce`，确认适配器实际调用已存在的正 BRC carrier。
- 作者最终证明 `OWNER_PP_FINITE_MOMENT_CORRECTION_20260907.md` 第 2–4 节，确认公式、归一化与 API scope 一致。

这里的标签词长度 d 不是原生空间维数。适配器没有把抽象二进制位置硬贴为 X6 物理轴，没有增设 anchor、距离或旋转定义。实际复用的是有限正分支、按计数推前、保留重数的直方图和 BRC 串联/替代合并。

## 2. 一般有限等价与独立验证方向

设 `d≥0`，给定有限实数列 `h_0,...,h_d`，定义

`β_j=Σ_{a=0}^{d−j}(−1)^a C(d−j,a)h_{j+a}`，`w_j=C(d,j)β_j`。

生产器按差分计算 β；验证器走另一方向，核验全部原始 h 的三角恒等式

`h_a=Σ_{j=a}^d C(d−a,j−a)β_j`。  (1)

此式确实是前式的逆。将 β 展开，h_l 的系数为

`C(d−a,l−a) Σ_{j=a}^l (−1)^(l−j)C(l−a,j−a)`，

其值在 l=a 时为 1，在 l>a 时为 0。三角矩阵的对角元均为 1，故通过全部原 h 的核验就唯一确定 β；验证器没有仅相信作者 status，也没有仅重算一个孤立的负差分。

令 `b(r,k)=(−1)^kΔ^k h_r`，其中 `r,k≥0,r+k≤d`。有限包含–排除，或恒等式 `b(r,k)=b(r,k+1)+b(r+1,k)` 向终端边界迭代，给出

`b(r,k)=Σ_{j=r}^{d−k}C(d−r−k,j−r)β_j`。  (2)

因此全部合法差分非负当且仅当全部 β 非负：一向由非负线性组合，另一向读取终端单元 `b(j,d−j)=β_j`。严格全正也等价。证明只用有限求和，对实数成立；程序准确限定为精确整数/有理输入。

任一负 β 经 (1) 绑定原 h 后，足以排除声明的正交换词族。该证明不需要全体差分由程序逐个重新枚举，也不从有限实验外推无限 m。

## 3. 逐词、逐层与真实直方图

模型明确给每个具体词 `ω∈{0,1}^d` 质量 `β_|ω|`，零质量词不产生正分支。恰有 j 个 1 的层有 `C(d,j)` 个词，故总层质量是 `w_j=C(d,j)β_j`。两者类型不同：

- β_j 是每个具体词的质量；
- w_j 是整层质量；
- `WeightHistogram` 记录每个实际正词质量及它的词数，允许不同 j 层的相同 β 合并计数。

代码 `_histogram` 以 `counts[β_j]+=multiplicity_j` 调用现有 `WeightHistogram.from_counts`，没有将整层误作一个质量 w_j 的分支。`histogram_record` 的 `branch_count` 是正质量词数，`total_mass` 是质量之和；二者不同。d=0 有一个空词：β_0>0 时一条分支，β_0=0 时空正分支族，均正确。

独立小例取 `d=3, β=(1/2,0,1/2,2/3)`。直接列举八个词得到

`h=(8/3,5/3,7/6,2/3)`，

完整正 histogram 是 `{1/2:4, 2/3:1}`，正词数 5，总质量 `8/3`。j=0 和 j=2 的同权词必须合计为四条，j=1 的三条零质量词必须省略。适配器与直接列举完全一致。

这个直方图已经忘掉单词身份和 j 标签。后续 `prefix_observation_histogram` 与 `coefficient_histogram` 接受完整 h，并重建带 j 的 β 信息；它们没有声称只从裸 histogram 就能恢复任意单词观察。

## 4. 固定位置与系数观察的合同

指定 r 个互异位置为 1，再指定 k 个与其不交的位置为 0。对总计数 j，满足条件的词数为 `C(d−r−k,j−r)`；每词质量仍为 β_j，得到 (2)。位置可以任意选择，不能将“固定指定位置”乘上选择这些位置的组合数。API 只接收 r,k，是因为该模型对位置交换对称，不是因为位置身份被任意忽略。

独立检查遍历所有位置状态 `free/0/1`，所以 d=3 的 27 个实际带标签 cylinder 都检查了，不只检查首 r 位/随后 k 位的一个代表。

设

`q(t)=Σ_a(−1)^a C(d,a)h_a t^a`，

则由 (1) 得 `q(t)=Σ_j w_j(1−t)^j`，继而

`Bhat(x)=Σ_j w_j(1+x)^(d−j)`，

`[x^k]Bhat(x)=Σ_j C(d,j)β_j C(d−j,k)`。  (3)

`coefficient_histogram` 的分支是 `(具体词,该词零位置的一个 k 元子集)`。逐 j 层的词 histogram，与 `C(d−j,k)` 个单位质量选择进行现有 `histogram_serial`，每个结果分支保持质量 β_j，重数相乘；再以现有 `histogram_recoalesce` 合并不同 j。代码正好实现 (3)，没有把系数质量误作分支数。

有限差分非负只给系数非负。在 w 非负前提下，全部系数严格正当且仅当 w_0>0：最高项系数就是 w_0，其正项也贡献所有较低次数。这与作者证明相符，不额外假定所有 β 严格正。

## 5. 必须保留的反例边界

**交换性边界。** `OBSTRUCTED` 排除的是有限交换词族 / 对称阶乘读出。它不能否定任意非交换总体的单一固定 prefix 序列。单位词 `10` 给“首 a 位全为 1”读数 `(1,1,0)`，却有 `β=(-1,1,0)`。原因是固定首位与固定第二位的读数不相同，且不满足对称阶乘平均的合同。作者已将公开 SCOPE 改为

`FINITE_EXCHANGEABLE_WORDS_AND_SYMMETRIC_FACTORIAL_OBSERVATIONS_ONLY`，

并在 verify docstring 和证明中明确这一反例。

**幂矩边界。** `h_a=Σ_j w_j C(j,a)/C(d,a)` 使用不放回的阶乘读数，不是 `Σ_j w_j(j/d)^a`。有限 HCM 不推出正幂矩测度。小例 `(1,1/2,1/5)` 的 finite-HCM 为正，仍有 `L_h((u−1/2)^2)=−1/20`。`verify_square_obstruction` 只有负平方才返回排除结论；非负返回 `UNDETERMINED`，没有反向宣布可实现。`REALIZED` 证书的 `power_moment_measure` 固定为 `UNCLASSIFIED`。

本次只对比现有作者 JSON 与已独立审计的 m=3 JSON：归一化 h、原 q、负平方值逐项相同，并对提供的 h 调用新 verifier 核验其现成 BRC 证书。没有再次计算旧 cofactor、signed-secant、插值或 m 扫描。源到 m=3 数据的独立证明继续由先前专项审计承担。

## 6. 实际发现、作者修复与资源语义

初始 consumer SHA `04f35fbd2720796715aac0d280a4c8311f509526ae7e1fb0d762d30c238d5313` 存在以下可复现问题，已先逐条消息交作者，审计员未改作者源码：

1. 仅靠 Python 字典数值相等，`j=False`、`word_count=1.0`、`branch_count=4.0` 可获 `valid=True`。
2. `beta[0]='1/0'` 导致公开 verifier 未捕获 `ZeroDivisionError`。
3. `OBSTRUCTED` 可附加 `power_moment_measure='EXISTS'` 或伪造 `layers`，仍获 valid；状态没有对应闭合 schema。
4. β 先完整迭代解析再检查长度，任意 iterable 未受有限向量长度约束。

第一轮修复加入按状态闭合字段、确切 dict/list/int/string 类型、容器长度先验检查、精确整数计数、非法分母捕获、节点及标量预算。17 类坏证书的独立测试全部拒绝；generator 在拒绝前消费 0 项。

随后发现第二个真实资源问题：`d=0,h=(10^4500,)` 的合法单词证书，在原 100000 字符预算内，却因当前 Python 默认 4300 位整数字符转换限制，被误报为 `INVALID_CERTIFICATE`。作者进一步修复输入与输出序列化的有理分子/分母 12000-bit 表示预算、解析前每个整数段 4000 字符预算，并使 build 的自验 `UNVERIFIED` 转为 `ResourceLimit`。

最终独立复核：同一大整数合法输入，build 以 `ResourceLimit` 中止，verify 返回 `UNVERIFIED`；不是无解，也不是数学无效证书。格式反例例如 `1/0` 仍为 `INVALID_CERTIFICATE`，没有笼统把所有 `ValueError` 当资源不足。

最终资源合同实际覆盖：默认 d≤256 的维数预算、输入/序列化有理标量预算、certificate 节点/字符串/整数预算及闭合结构限制。它不是精确 wall-clock 保证，也不承诺所有内部有理运算始终保持 12000-bit；运算结果需要导出时仍受表示预算约束。预算耗尽不推出有限 HCM 不成立。

## 7. 本次独立验证

独立脚本：`experiments/owner_pp_brc_consumer_audit_20260907.py`；结果：同名前缀 `.json`。

```text
python experiments/owner_pp_brc_consumer_audit_20260907.py
```

最终结果 `PASS`：

- 3 个局部 ensemble：d=0 的零/非零族，以及 d=3 的零权、跨层同权例。
- 29 个实际带标签 cylinder，6 个显式 `(word,marked-zero-subset)` 系数读出。
- 17 类坏证书拒绝，覆盖 bool/float/Fraction 冒充整数、错误 β、把 w 当 β、删除 multiplicity、原 h 不匹配、伪幂矩声明、额外字段、坏分母、非规范有理串与非法向量容器。
- 6 类资源语义检查（维数、字符串、节点、合法大有理验证、大输入 build、大证书有理字符串），5 类不精确/非法输入拒绝；generator 零消费。
- 小负平方和非负平方的单向判定；非交换 prefix 反例的 scope 区分。
- 现成 m=3 h/q/负平方与既有独立证据一致；新证书对提供的 h 核验通过。

作者的 63 ensemble / 756 prefix / 252 coefficient 是其报告的检查结果，本审计没有再运行它们。一般定理由第 2–4 节有限组合证明承担，不由这三个小例外推。

## 8. 最终冻结来源

| 文件 | SHA256 |
| --- | --- |
| `experiments/owner_pp_finite_brc_20260907/finite_hcm_brc.py` | `389b9551bbd4929964b28361c0a927abcb7a078b02da7b2bd6269bdd59b21f3b` |
| `experiments/owner_pp_finite_brc_20260907/run_finite_brc_checks.py` | `32ea7a7425df42640665db260a6172893777753fb25ef07b56cd17ad13e4530e` |
| `experiments/owner_pp_finite_brc_20260907/finite_brc_certificate_20260907.json` | `0e80b0e60823e32c8c2c16d008322eedff907c2a1cd2cf19ae2992f5387d3ae9` |
| `research_notes/OWNER_PP_FINITE_MOMENT_CORRECTION_20260907.md` | `804d85f5fc34cda940b41b917a684595bd2037e67726e501debbbc494e42a530` |
| `research_notes/OWNER_PP_FINITE_MOMENT_INDEPENDENT_AUDIT_20260907.md` | `469a388a971adb20e2ef11dcfce02b0fd6314487dbe0cc7cf7332b8054b9cd81` |
| `experiments/owner_pp_finite_moment_audit_20260907.json` | `c4722335bee9797064f60a70f8aebd6c8998998ae418cdd0701653ca92d4bd98` |
| `src/enterprise_math/brc_histogram.py` | `256ef167e2aee651c042195522a0013ba619f265f9e4d8fa24f07d3399695a67` |
| 本独立脚本 | `cbecf1e31b56da5c2f6efdd46a1c1a00521488a29f8448703d527755a307fc99` |
| 本独立结果 JSON | `3980461015170dbc2303d81af71c31ab3ad9c8d13d26c4801024b75fea3cb3b8` |

定位：最终 consumer 的 L21 scope，L29–92 输入/表示预算，L94 终端权重，L117 build，L141 原 h 验证，L208 固定位置观察，L223 系数 consumer，L246 单向平方障碍。

本轮审计只关闭该适配器合同中的已识别问题；未证明 all-m HCM0、all-m β 正性或其他 Perfect Prime 主目标，未修改历史 frozen 材料或 canonical BRC。
