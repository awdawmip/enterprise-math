# Perfect Prime：否定有限幂矩 lift，修复为有限 BRC 展开

状态：**原模型 m=3 的精确反例；一般有限 BRC 修复恒等式已证**。
这是 Owner 内部研究与消费审计，不是正式 V2 review、Working Truth 或 Foundation。
原 all-m 系数正性 / HCM0 目标保持开放。

## 1. 错误来源与实际反例

旧 research_returns/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_RETURN_20260903.md
第 9 节把有限列的全部有符号差分非负，称为存在正测度且
\(h_a=\int_0^1u^a\,d\mu(u)\) 的充要条件。这个有限版本不成立。
源 SHA256：617b34abac20d524023933a09777b85aa4220e1962283586c1c2121d3031b28d。
历史源码与接受记录均保持原样。

一般严格反例是 \((1,1/2,1/5)\)：全部六个允许的有符号差分均正，
但 \(L_h((u-1/2)^2)=-1/20\)。正测度不可能给平方负积分。
truncated 与 full moment problem 的区别也见
[Curto–Fialkow (1991)](https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf) 引言及第 4 节；
这里的否证只需平方非负这一直接必要条件。

更强的是，旧原模型本身在 m=3 已失败。保留原
\(h_{m,a}=(-1)^aq_{m,a}/\binom da\)，其中 \(d=(m-1)(2m-3)\)。
当 \(m=3,d=6\)，\(h_{3,0}=243/68068000>0\)。
归一化 \(\bar h_a=h_{3,a}/h_{3,0}\) 后准确值为

\[
\left(1,\frac{1445864051}{6614047440},
\frac{50080057}{1027026000},\frac{4900831}{513912000},
\frac{12679829}{10737090000},\frac{1597417}{33070237200},
\frac1{4686825}\right).
\]

取 \(p(u)=u^2+8u/7-3/10\)，直接展开得到

\[
L_{\bar h}(p^2)
=\bar h_4+\frac{16}{7}\bar h_3+\frac{173}{245}\bar h_2
-\frac{24}{35}\bar h_1+\frac9{100}
=-\frac{7205915063}{2893645755000}<0.
\]

因此这些前五个数就已不可能是任何实线上正测度的普通幂矩。
同一数据的全部 28 个允许的有符号有限差分仍严格为正。
这否定旧第 9 节的 all-m 幂矩表示路线，**不否定** HCM0、完整有限差分事实、
原系数正性或 cofactor 非零性目标。

Owner 仅用旧 exact checker 的 q_coefficients(3) 取得这一新障碍需要的数据，
未重跑旧 m=2..10 全套。checker SHA256：
05f75c3ae61b76ce8194df9a9d6305b1d5615f206fc0647f336e4f2ca0a412f9。
独立审计另从原 5×5 多项式 cofactor 的 120 项 Leibniz 展开和 126 候选
signed-secant 枚举核对所有系数，见 OWNER_PP_FINITE_MOMENT_INDEPENDENT_AUDIT_20260907.md。

## 2. 正确的有限表示定理

设 \(d\ge0\)，给定有限实数列 \(h_0,\ldots,h_d\)。定义

\[
\beta_j=(-1)^{d-j}\Delta^{d-j}h_j
=\sum_{a=0}^{d-j}(-1)^a\binom{d-j}{a}h_{j+a},
\qquad w_j=\binom dj\beta_j.
\]

**定理。** 全部 \((-1)^k\Delta^kh_r\ge0\)、\(r+k\le d\)，
当且仅当全部 \(\beta_j\ge0\)。
此时给每个带位置标签的二进制词 \(\omega\in\{0,1\}^d\) 质量
\(\beta_{|\omega|}\)，就得到一个明确有限正 BRC 总体；零质量词不产生正分支。

首先，二项反演给出

\[
h_a=\sum_{j=a}^d\binom{d-a}{j-a}\beta_j
=\sum_{j=a}^dw_j\frac{\binom ja}{\binom da}.
\tag{1}
\]

可把 \(\beta\) 定义代入，按
\(\sum_{b=0}^n(-1)^b\binom nb=0\)（\(n>0\)）直接验证。
第一式的上三角矩阵对角全为 1，所以原 h 唯一确定 beta。
组合上，右侧就是固定 a 个指定位置全为 1 的词质量。
再固定另 k 个位置为 0，包含–排除得到

\[
(-1)^k\Delta^kh_r
=\sum_{j=r}^{d-k}\binom{d-r-k}{j-r}\beta_j.
\tag{2}
\]

beta 非负时，这些质量均非负；反方向取 \(r=j,k=d-j\)。
严格差分全正同样等价于 beta 全正。总质量为 \(\sum_jw_j=h_0\)；
非负情况下 h0=0 只对应空正分支总体。

式 (1) 是不放回抽样的阶乘矩读出
\(\binom ja/\binom da=(j)_a/(d)_a\)，不是 \((j/d)^a\)，
也不承诺独立抽样或某个幂矩混合测度。
有限可交换理论有经典先例，参见
[Diaconis–Freedman 的 Stanford 原始报告入口](https://statistics.stanford.edu/technical-reports/finite-exchangeable-probability)。
本轮贡献是纠正错误消费、提供原模型反例并接入已有 BRC，不另称新的概率表示定理。

## 3. 系数正性的有限 BRC 修复

定义 \(q(t)=\sum_{a=0}^d(-1)^a\binom da h_at^a\)。
由 (1) 以及二项式定理，

\[
q(t)=\sum_{j=0}^dw_j(1-t)^j,\qquad
\widehat B(x)=(1+x)^dq\!\left(\frac{x}{1+x}\right)
=\sum_{j=0}^dw_j(1+x)^{d-j}.
\tag{3}
\]

故

\[
[x^k]\widehat B(x)=\sum_{j=0}^{d-k}w_j\binom{d-j}{k}.
\tag{4}
\]

完整有限差分非负足以让 (4) 成为正分支质量读出。
在 w 非负的前提下，全部系数严格正当且仅当 w0>0：
最高次系数就是 w0，而 w0>0 对每个 k 都提供正项。
完整差分严格正当然是充分条件。这里不需要普通幂矩测度。
旧 HCM0 与系数正性的代数等价式继续有效。
本文件**没有证明所有 m 的 beta 非负**。

在归一化 m=3 实验中，(3)–(4) 的 q 和 Bhat 也都除以 h3,0。
证据 JSON 同时保存原 q、归一化常数和归一化 h，避免混用。

## 4. 实际 consumer 与类型边界

experiments/owner_pp_finite_brc_20260907/finite_hcm_brc.py 直接调用
现有 WeightHistogram、histogram_serial 和 histogram_recoalesce。
有界 coverage 检索查了当前 native/Common Surface、method inventory 与 brc*.py 的
有限可交换、Hausdorff、without-replacement、Bernstein、falling-factorial 关键词，
未定位同一输入输出接口。底层 histogram 与分支组合完全复用；
本适配器不是正式新增 tool family。

- build_certificate / verify_certificate：生成逐词 beta、逐 j 层和 histogram；
  验证器独立通过全部原始三角读出 (1) 核验，不重复生产用差分。
- prefix_observation_histogram：指定不同位置的 r 个 1、k 个 0，读出 (2)。
- coefficient_histogram：分支为“词、从零位置选 k 个标记”，每次选择保持原词质量；
  用实际 BRC 串联 unit 选择、再替代合并，质量恰为 (4)。
- verify_square_obstruction：平方读出为负才否定正幂矩测度；
  非负时返回 UNDETERMINED，不倒推可行。

j 层实际包含 \(\binom dj\) 个质量 beta_j 的词，
不能把它替换为一个质量 w_j 的词后声称 count/histogram 未变。
程序保留层与词的组合标签定义，histogram 只是明确忘标签的观察，
不承诺恢复任意单词身份或支持任意未来选择。
d 是抽象标签词长，**不是进取空间的新维数**；
本表示没有定义新的 native 旋转、距离或物理演化。
符号仅参与代数差分与最终多项式读出，正 BRC 质量不承担 signed cancellation。

独立审查发现的 bool/float 数字伪装、零分母、额外字段与任意迭代器问题已修复：
证书使用按状态闭合的字段 schema，先检查容器/长度，再检查精确 primitive 类型；
格式错误返回 INVALID_CERTIFICATE，明确资源预算不足返回 UNVERIFIED。
精确有理数的分子和分母各有 12000-bit 表示预算；超限的有效输入不被归为数学无解。
负 beta 排除的是已声明的可交换词族 / 对称阶乘读出：例如单词 10 的单位质量
可以给某一固定 prefix 列 (1,1,0)，但不能令所有指定位置的相应读出都相同；
它不属于这里被判定的可交换总体合同。

## 5. 验证与路线退出

run_finite_brc_checks.py 对 63 个明确词总体做直接枚举；
756 个固定位置观察、252 个“词及标记子集”系数观察与 BRC histogram 完全一致。
11 种证书篡改被拒；浮点/布尔输入被拒。
实际 m=3 的负平方、全部 28 个正差分和 7 个原多项式系数读出均通过。
finite_brc_certificate_20260907.json 绑定实际原 checker、consumer 和检查脚本 SHA256。
独立 consumer 审计另见 OWNER_PP_BRC_CONSUMER_INDEPENDENT_AUDIT_20260907.md。

关闭：原 all-m 正普通幂矩 lift，无需扩大 m 搜索同一路反例。
保留：all-m HCM0、完整有限差分正性以及可以使用 (3) 的有限正 BRC 构造。
剩余方向没有在这里被证明；下一工作须有真实信息缺口及可判别目标。

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
