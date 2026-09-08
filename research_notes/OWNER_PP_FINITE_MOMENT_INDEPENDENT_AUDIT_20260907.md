# PP finite-HCM 幂矩误读与有限 BRC 修复：独立审计

状态：`AUXILIARY_INDEPENDENT_AUDIT / EXACT_COUNTEREXAMPLE_CONFIRMED / FINITE_BRC_REPAIR_VERIFIED / NOT_FOUNDATION`。

辅助工作包 `/root/exact_solver`；不是正式 task、claim 或 Researcher-ID。只审计原模型的 `m=3` 与一个任意有限字长的组合恒等式；历史 return、冻结任务及 canonical 均未修改。

## 1. 审计结论与准确错误位置

历史 `research_returns/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_RETURN_20260903.md` 第 478 行、§9 把有限完整差分非负

\[
(-1)^k\Delta^k h_r\ge0\quad(r+k\le d)
\]

当成在 `[0,1]` 上存在正幂矩测度的充分必要条件。充分性错误。原模型 `m=3` 已有严格反例，且不能由实直线上任何正测度表示。

这并不否定 §7 的 HCM0 系数恒等式，也不否定 §8 已检查有限范围内的差分正性。§9 的 (9.1)、(9.2) 在**另行拥有幂矩表示**时是正确的代数推论，但该表示不能从有限 HCM 推出，原 `m=3` 的指定矩还直接排除了它。因此 §10 第 539 行附近要求“preferably”构造 (9.1) 的正测度不能继续作为本序列的可行证明目标；有限差分命题与全 `m` 系数目标仍应分别保留原边界。

## 2. 从原模型到反例：两条不同的精确路径

复用的旧检查器是 `research_checks/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_CHECK_20260903.py`：原输入 `actual_h` 在第 74 行，cofactor 在第 84 行，插值路径 `q_coefficients` 在第 119 行，signed-secant 路径 `cb_q_coefficients` 在第 161 行。

本审计**不调用** `q_coefficients` 或插值。独立脚本直接在 `Q[t]` 中取

\[
H_{ij}(t)=\frac1{i+1+3j}-\frac{2t}{i+1+3j+9}
+\frac{t^2}{i+1+3j+18},\qquad 0\le i,j\le2,
\]

以 `w=(1,-2,1)`、边权 `w_i H_ij w_j` 构造原二部 Laplacian，删除最后一个右顶点，展开 5×5 cofactor 的全部 `5!=120` 个 Leibniz 项。得到

\[
\tau_3(t)=t^2q_3(t),\qquad\deg q_3=6,\qquad
q_{3,0}=\frac{243}{68068000}>0.
\]

独立的旧 `cb_q_coefficients(3)` 枚举九个原子中的全部 `C(9,5)=126` 个候选 signed-secant 子集。两路逐系数完全一致。完整原始 `tau`、`q` 与有理归一化全部保存在证据 JSON 中，避免只绑定一个孤立数列。

原定义为 `h_raw,a=(-1)^a q_3,a/C(6,a)`。写 `h=h_raw/q_3,0`，则

\[
h=\left(1,
\frac{1445864051}{6614047440},
\frac{50080057}{1027026000},
\frac{4900831}{513912000},
\frac{12679829}{10737090000},
\frac{1597417}{33070237200},
\frac1{4686825}\right).
\]

直接检查全部 28 个有定义的差分单元，均严格为正。

取

\[
p(u)=u^2+\frac87u-\frac3{10},\qquad
p(u)^2=u^4+\frac{16}7u^3+\frac{173}{245}u^2-\frac{24}{35}u+\frac9{100}.
\]

对线性泛函 `L_h(u^a)=h_a`，精确计算给出

\[
\boxed{L_h(p^2)=-\frac{7205915063}{2893645755000}<0.}
\]

如果正 Borel 测度 `mu` 在实线上具有这些矩，则 `int p(u)^2 dmu=L_h(p^2)>=0`，矛盾。只需已给出的 0 至 4 阶有限矩；不需要任何矩问题存在定理，更不需要将绝对值删去或假设额外正性。

未归一化原序列同样有

\[
L_{h^{raw}}(p^2)=-\frac{64853235567}{7294988120420000000}<0.
\]

作为独立数值证据，归一化前三阶 Hankel 主式为

\[
\det(h_{i+j})_{0\le i,j\le2}
=-\frac{447963348953257251895594859}
{184525273837044841388688000000000}<0.
\]

平方证据本身已完成反证；Hankel 行列式不是必需前提。

## 3. 正确可调用合同：有限交换标签的分支质量

以下是经典有限差分与二项式反演的本地有类型应用，不宣称新的代数定理。

设 `d>=0` 为整数，`h_0,...,h_d` 为有限实数列（本消费者全部有理）。定义

\[
b(r,k)=(-1)^k\Delta^k h_r\quad(r,k\ge0,\ r+k\le d),
\qquad\beta_j=b(j,d-j),\qquad w_j=\binom dj\beta_j.
\]

有限 HCM 是所有 `b(r,k)>=0`。精确合同为

\[
\boxed{b(r,k)=\sum_{j=r}^{d-k}\binom{d-r-k}{j-r}\beta_j.}\tag{A}
\]

**证明。** 差分定义给出 `b(r,k)=b(r,k+1)+b(r+1,k)`。沿这个有限三角形递推到边界 `r+k=d`，到边界 `(j,d-j)` 的路径数为 `C(d-r-k,j-r)`。边界值正是 `beta_j`，故 (A) 对所有合法索引成立，包括 `d=0`。

于是

\[
\boxed{\text{finite HCM}\iff\beta_0,\ldots,\beta_d\ge0.}\tag{B}
\]

两向都准确：正向读取 HCM 边界；反向使用 (A) 的非负二项式系数。严格版本也成立：全部单元严格正当且仅当全部 `beta_j>0`。

令 `k=0` 并用组合恒等式，得到

\[
\boxed{h_a=\sum_{j=a}^d\binom{d-a}{j-a}\beta_j
=\sum_{j=a}^d w_j\frac{\binom ja}{\binom da}.}\tag{C}
\]

在二进制标签词 `omega in {0,1}^d` 上给每个具体词质量 `beta_|omega|`。这定义一个有限、交换对称、非负 BRC 分支表，且总质量为

\[
\sum_{\omega}\beta_{|\omega|}=\sum_jw_j=h_0.
\]

指定 `r` 个互异标签为 1、另 `k` 个互异标签为 0，其 cylinder 质量就是 (A)。等价地先选总计数 `J=j`，质量为 `w_j`，再在恰有 `j` 个 1 的词中均匀分配。`h_a` 是指定 `a` 个互异标签全为 1 的质量，即不放回抽取的阶乘矩读数。

`d` 是标签字长。这个例子的 `d=6` 不增加原生 X6 的空间维度，不要求将标签轴识别成物理轴；P000、anchor 和进取坐标的几何合同没有变化。这里真正使用的 BRC 结构是有限分支质量、按计数的推前以及 cylinder 读数。

如需概率，必须另有 `h_0>0` 并将全部质量除以 `h_0`。若 finite HCM 且 `h_0=0`，由 (A) 的 `(0,0)` 单元可知全部 `beta`、`w`、`h` 为零；概率归一化没有定义。

## 4. 多项式修复、归一化与严格正性的边界

对上节未预设归一化的序列定义

\[
Q_h(t)=\sum_{a=0}^d(-1)^a\binom da h_at^a,
\qquad\mathcal B_h(x)=(1+x)^dQ_h\!\left(\frac{x}{1+x}\right).
\]

代入 (C) 后只交换有限和，用二项式定理得

\[
\boxed{Q_h(t)=\sum_{j=0}^dw_j(1-t)^j,\qquad
\mathcal B_h(x)=\sum_{j=0}^dw_j(1+x)^{d-j}.}\tag{D}
\]

第二式是多项式恒等式；虽然分式形式在 `x=-1` 不直接定义，经多项式延拓后仍成立。

对原始 `h_raw`，`Q_h=q_3`、`mathcal B_h=Bhat_3`。对第 2 节使用的归一化 `h`，则必须使用 `Q_h=q_3/q_3,0`、`mathcal B_h=Bhat_3/q_3,0`。不能只归一化数列后仍把右端写成未归一化原多项式。

这给出所有系数的非负性，但不会把弱非负条件自动升级为严格正性：

\[
[x^k]\mathcal B_h(x)=\sum_{j=0}^{d-k}w_j\binom{d-j}{k}
=\binom dk b(0,k).
\]

在 `w_j>=0` 前提下，全部系数严格正恰当且仅当 `w_0=beta_0>0`，因为最高次系数就是 `w_0`，而该项也给每个低次系数正贡献。原严格 HCM 比这一条件强，原 HCM0 与系数严格正性之间的恒等式完全保留。

有限 urn 表示不提供 `h_a=int u^a dmu`：前者使用 `C(j,a)/C(d,a)`，后者使用 `u^a`。因此不能在修复中把它替换为 iid Bernoulli 参数混合或将 `sum w_j(1-t)^j` 改成 `int(1-tu)^d dmu`。原 `m=3` 的负平方已经具体阻止这种替换。

## 5. 有界验证与来源绑定

脚本：`experiments/owner_pp_finite_moment_audit_20260907.py`。结果：同名前缀 `.json`。

运行：

```powershell
python experiments/owner_pp_finite_moment_audit_20260907.py --output experiments/owner_pp_finite_moment_audit_20260907.json
```

本次结果 `PASS`，只使用 Python 标准库 `Fraction`：

- 原 `m=3` cofactor 的 120 项精确多项式展开，与 126 候选 signed-secant 路径逐系数相等；没有调用旧插值或运行 `m=2..10` 扫描。
- 给定 7 项归一化 `h`、负平方与负 Hankel 主式均精确一致；28 个有限差分单元仍严格正。
- 所有 `beta_j`、`w_j`、总质量、(A)/(C)/(D) 及 HCM0 都直接核验；显式枚举 64 个标签词，独立累加全部 28 类 cylinder 质量。

精确证据的 SHA-256：

| 文件 | SHA-256 |
|---|---|
| 原 frozen return | `617b34abac20d524023933a09777b85aa4220e1962283586c1c2121d3031b28d` |
| 原 legacy checker | `05f75c3ae61b76ce8194df9a9d6305b1d5615f206fc0647f336e4f2ca0a412f9` |
| 本独立脚本 | `3497b9093612a90c69db13f67f7cba3896c7ed4d626c8ebf4ff6699cdce30b00` |
| 本独立结果 JSON | `c4722335bee9797064f60a70f8aebd6c8998998ae418cdd0701653ca92d4bd98` |

`/root/branch_scout` 另以三角递推独立复核 (A) 及其边界、归一化零质量情形；该消息只支持这些组合恒等式，不替代原模型反例的源码验证。本报告的反证与修复证明自足，不依赖外部截断矩定理。

本轮关闭的是错误的正幂矩充分性解释及本 `m=3` 序列的正幂矩表示目标。全 `m` HCM0、全有限 HCM 和 parent 非消失目标的状态没有被本审计擅自提升或否定。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
