## Fermat–Landau 局部因子筛选：迹的指数拼接错误、二级筛轮与共享工作预算

任务 `RS-FERMAT-LANDAU-SCREENING-IMPLEMENTATION-REPAIR-20261101`，发布 `TP2-A3769AB88B65DCB73E47`，任务书 blob `69ef9402bad085105de4ed21fae80f55a38df48d`。冻结稿件 SHA-256 为 `af082f3c0485a309346a7e92791b7b75ff62f62e2db549d970900e9a5d4b95ad`。以下是对稿件二次 Lucas 与 wheel 分支的可执行局部修复和数学检验。

**Lucas 迹引理。** 设 \(V_0(T)=2,V_1(T)=T,V_{n+1}(T)=TV_n(T)-V_{n-1}(T)\)。伴随矩阵 \(A=\begin{pmatrix}T&-1\\1&0\end{pmatrix}\) 的行列式为 1，\(\operatorname{tr} A^n=V_n(T)\)。对 \(A^b\) 用同一递推得 \(V_a(V_b(T))=V_{ab}(T)\)，适用于任意整数模数。梯形递推的交叉项是 \(V_i(T)V_{i+1}(T)-T\)。追加一位 \(z\) 将下标 \(i\) 变成 \(2i+z\)。因此老代码跨阶段沿用一对寄存器与初始常数 3 时，输入各素数的最大幂 \(e_j\) 实际产生拼接指数
\[
S_0=0,\qquad S_j=2^{\operatorname{bitlen}(e_j)}S_{j-1}+e_j .
\]
新代码让每个阶段以自身 \(T\) 建立 \((2,T)\)，返回其 \(V_{e_j}(T)\) 作为下一阶段的 \(T\)。这给出乘积指数 \(E_j=\prod_{i\le j}e_i\)。

用 CPython 3.12.14 执行原稿里的原函数，\(108391,B_1=50,k=2\) 返回 None，\(1497,D=210\) 返回 Unsplit。前一输入的原拼接指数为 310438200996101862365935，迹 99205，与 \(N\) 取 \(\gcd(V-2,N)=1\)。正确 \(E=\mathrm{lcm}(1,\ldots,50)=3099044504245996706400\)，最终迹 87421，对应 gcd 107。允许各阶段提早命中时，第一阶段 \(e=32\) 得 11282，第二阶段 \(e=27\) 得 78005，已提取可验证因子 107。第二个输入先用公开 \(D\) 的素因子试除，得 \(1497=3\cdot499\)。实现按预算生成 \(D\) 的素因子，即使 \(N\mid D\) 也逐个验证；\((21,210)\) 取得 3。

**单预算筛选。** 运行入口只接受 \(N,B_1,D\)、路线与非负整数预算，算法无需种子；成功均执行 \(1<d<N\) 及 \(N\bmod d=0\) 的独立检查。返回带原参数和分项用量的 `FACTOR_FOUND`、`BUDGET_EXHAUSTED`、`NO_HIT_IN_DECLARED_SEARCH` 或 `INVALID_INPUT`。在尝试下一计费步骤前检查同一余款；若合法状态用光额度，返回打断的操作名。Lucas 候选试素、构造最大素数幂均付费，对指数 \(e\) 支付 \(2\operatorname{bitlen}(e)\) 次模乘。在轮筛中，预处理、\(D+1\) 个 Fermat 候选、每个被试整数的筛轮 gcd、保留项各一次模乘、两端点 gcd 与因子验证均计数；两个区间顺序流式执行，内存不随 \(\sqrt N\) 线性增长。一个 Fermat 候选工作单位允许其固定数量的平方、减法、整根与比较；gcd 以单次调用为单位。这些是可重放操作计数，位复杂度与各次操作的整数长度有关。

**实测边界。** Lucas 修复检查了模数 \(3,\ldots,100\)、迹 \(2,\ldots,7\)、上界 \(2,\ldots,15\) 的全部 8,232 组，均与独立二阶矩阵幂的迹相符。\(N=2,\ldots,999\) 和 \(D\in\{2,6,12,30,210\}\) 的 4,990 次轮筛给出 4,135 个已验因子和 855 次无命中。所有该范围的半素数均命中。无命中中含 15 组至少三个素因子的合数，例 \(385=5\cdot7\cdot11,D=2\) 的两个轮端点 gcd 都等于 385，清楚展示了该局部筛选输出与素性判断的边界。另在 \(N\le99\) 检查 490 组 Lucas 先行再进入轮筛的组合路线。

按七种输入逐个测试从零至“完整用量加一”的所有预算，共 128 次截断测试，对照真实执行前缀全相符。\(108391\) 的早停仅用 36 单位（一次偶性、两次素候选、八次素幂试验、各十一次交叉乘和平方、两次 gcd、一次验证）；\(1497\) 用 7 单位。\(97,B_1=2,D=6\) 组合路线完整需 39 单位，额度为 30 时，在第二个 wheel 积区间检查候选之前正确停止；进入 fallback 后未重置余款。四个无效参数例和平方、素数、小素因子全覆盖及 gcd 饱和均已核对。本工作保留直接逐项模乘的实际成本，环面四次分支以及更快的积树求值仍各有独立问题。

[冻结原稿](https://github.com/awdawmip/enterprise-math/blob/a5902327c911630a2c6a387fbbc4822232edaebd/research_inputs/2026-11-01/fermat_landau_wheel_dichotomy_complete_monograph.md) · [原作者核验与组合覆盖证明](https://github.com/awdawmip/enterprise-math/blob/1e41c0acc37b9347c91c1d4ded6327433d898edb/research_notes/2026-11-01/fermat-landau-monograph-review-6de891.md) · [冻结任务书](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/RS-FERMAT-LANDAU-SCREENING-IMPLEMENTATION-REPAIR-20261101.md)

[可运行的修复](fermat/repair.py) · [回归](fermat/test_repair.py) · [从冻结稿提取的原实现](fermat/original.py)。在本目录运行 `python fermat/test_repair.py`。
