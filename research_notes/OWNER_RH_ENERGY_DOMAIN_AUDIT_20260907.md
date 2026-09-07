# RH / P2 Gram 能量的定义域与交换次序独立审计

状态：`LOCAL CORRECTION AUDIT / EXACT DOMAIN PROOFS / NOT_FOUNDATION`。
日期：2026-09-07。辅助工作包：`/root/exact_solver`；不是正式 task、claim 或 Researcher-ID。
只读审计对象：`research_notes/RH_X6_BRC_TRANSPORT_FRONTIER_20260906.md`，SHA256 `693a7b2888d3eb72faca74c7d166a8af78caa9107bbf532aea918e9085873412`。
本报告不修改历史笔记、冻结任务或 canonical，不重开其他 RH 路线。

## 1. 结论及需要纠正的准确位置

历史笔记第 84 行定义的是原始、未减常数的

`P2(x) = sum_{n>=1} mu(n) n^(-2) exp(-x/n^2)`。

第 254 行的 `E_sigma = integral_0^infinity |P2(x)|^2 x^(1-sigma) dx` 因此在零端**当且仅当 sigma<2** 可积。第 257 行“对每个 sigma>1/2 有限与 RH 等价”的字面说法错误：sigma>=2 时无条件发散。该问题与 RH 真伪无关。

第 263–265 行的 Gamma 核及第 272–274 行的临界系数正确，但普通积分表示必须限制实 sigma<2。有限 Gram 正半定也只在此普通积分范围成立。无限双重求和的绝对交换还有额外限制：恰好 `1<sigma<2`。

最小修正有两个互相兼容的版本：

`RH <=> for every 1/2 < sigma < 2, E_sigma < infinity`；

或改成尾能量

`E_tail(sigma) = integral_1^infinity |P2(x)|^2 x^(1-sigma) dx`，

则 `RH <=> for every sigma>1/2, E_tail(sigma)<infinity`。

以下逐项证明；没有把 RH 当作已知前提，也没有删去绝对值来利用有符号抵消。

## 2. 零端的自足反证与精确下界

在 x>=0 上，各项绝对值不超过 n^(-2)，故级数一致绝对收敛，P2 连续，并且

`P2(0) = sum mu(n)/n^2 = 1/zeta(2) = 6/pi^2 > 0`。

最后一个 Dirichlet 恒等式可在绝对收敛域由 Euler 乘积得到。事实上反证不需要 pi 的数值：

`P2(0) >= 1 - sum_{n>=2} n^(-2) >= 1 - (1/4 + integral_2^infinity t^(-2) dt) = 1/4`。

由 `0<=1-exp(-u)<=u` 得

`|P2(x)-P2(0)| <= x sum n^(-4) <= (4/3)x`。

所以在 `0<=x<=1/16`，严格可用 `P2(x)>=1/6`。同时 P2 有界。由正比较判别法，

`integral_0^1 |P2(x)|^2 x^(1-sigma) dx < infinity <=> sigma<2`。

特别地，对 `0<epsilon<1/16`，sigma=2 的截断能量下界为

`(1/36) log((1/16)/epsilon)`；

sigma>2 的下界为

`[epsilon^(2-sigma)-(1/16)^(2-sigma)] / [36(sigma-2)]`。

它们分别对数、幂次发散。证据脚本还给 sigma=5/2、epsilon=(1/16)4^(-j) 的全有理下界 `(2/9)(2^j-1)`。这是严格反证，不是数值拟合。

## 3. 单对核、有限 Gram 与 Gamma 定义域

记 `f_n(x)=n^(-2)exp(-x/n^2)`，`a=m^(-2)+n^(-2)>0`。对实 sigma<2，直接变量代换 y=ax 给

`K_sigma(m,n) = integral_0^infinity f_m(x)f_n(x)x^(1-sigma)dx`

`= Gamma(2-sigma) (m^2 n^2)^(-1) a^(sigma-2)`

`= 2^(sigma-2) Gamma(2-sigma) (mn)^(-sigma) sech(log(m/n))^(2-sigma)`。

这里用到 `m^2+n^2=2mn cosh(log(m/n))`。无穷端因指数衰减没有限制，零端要求 sigma<2。sigma=1/2 代入 `Gamma(3/2)=sqrt(pi)/2`，正好得到历史系数 `sqrt(pi)/2^(5/2)`，无系数错误。

对任意有限指标集及复系数 c_n，

`sum_{m,n} c_m conjugate(c_n) K_sigma(m,n)`

`= integral_0^infinity |sum_n c_n f_n(x)|^2 x^(1-sigma)dx >= 0`。

因此有限矩阵正半定。P2 在正实轴上是实值，故有限 Möbius 系数时 `|P2_N|^2=P2_N^2`，但不能将平方的绝对值理解成对每个有符号交叉项取正，也不能用该有限恒等式略去无限极限的论证。

sigma>=2 时，单对原积分已发散。Gamma 的亚纯延拓不是它的积分值。例如在 sigma=5/2、m=n=1，延拓公式给 `2^(1/2)Gamma(-1/2)=-2sqrt(2pi)<0`，实际正积分却是 +infinity；这直接排除把延拓核继续叫原正 Gram 核。整数处的 Gamma 极点也不修复积分。

若采用尾能量，正确单对核为

`K_tail(sigma;m,n) = (m^2 n^2)^(-1) a^(sigma-2) Gamma(2-sigma,a)`，

其中 `Gamma(b,a)=integral_a^infinity t^(b-1)exp(-t)dt`，a>0。这一积分对每个实 sigma 都有限且正，有限 Gram 也正半定；不能继续沿用未截断的完整 Gamma 核。

## 4. 无限双和何时可以绝对交换

定义笔记中同一正载体

`A_x = sum |mu(n)| f_n(x) = sum mu(n)^2 n^(-2)exp(-x/n^2)`。

Tonelli 对非负量总是允许（结果可为 +infinity）

`sum_{m,n} |mu(m)mu(n)| K_sigma(m,n)`

`= integral_0^infinity A_x^2 x^(1-sigma)dx`，

其中完整单对核先要求 sigma<2。A_x 在零附近有正的有限极限。在无穷端，`A_x asymp x^(-1/2)`；这里只需双边比较，不需要历史 note 的精确常数。

该比较可独立证明。上界用正函数 `t^(-2)exp(-x/t^2)` 的单峰性，把全整数和控制为全正实积分加两倍最大值；积分为 `sqrt(pi)/(2sqrt(x))`，最大值是 O(1/x)。下界用平方自由数计数 Q(t)：

`Q(t)=sum_{d<=sqrt(t)} mu(d) floor(t/d^2)=t/zeta(2)+O(sqrt(t))`。

这里 `mu(n)^2=sum_{d^2|n}mu(d)`，floor 误差和截尾误差均 O(sqrt(t))，所以不需要 RH。在 `[sqrt(x),2sqrt(x)]` 中有与 sqrt(x) 同阶的平方自由数，每个项至少 `exp(-1)/(4x)`，得到所需下界。

于是绝对积分零端要求 sigma<2，无穷端等价于 `integral_1^infinity x^(-sigma)dx`，要求 sigma>1。结论为

`absolute double-sum / Fubini validity <=> 1<sigma<2`。

在这一范围，原能量无条件有限且

`E_sigma = sum_{m,n>=1} mu(m)mu(n)K_sigma(m,n)`

是绝对收敛恒等式。对尾核，绝对交换范围相应为 sigma>1，没有零端上界。

在 `1/2<sigma<=1`，绝对双和发散，即便 RH 成立也不会改变此正载体事实。这不说明有符号能量发散；它说明不能用绝对 Fubini 证明该能量等式。此报告不声称 sigma=1 的有符号能量未知，也不依靠超出必要范围的无条件对数衰减结果。

## 5. 临界带内可合法使用的极限合同

### 5.1 无条件的有序截断

令 `P2_N=sum_{n<=N}mu(n)f_n`。在任意 `0<delta<R<infinity` 上，P2_N 一致收敛到 P2，所以对任意实 sigma，

`integral_delta^R |P2|^2 x^(1-sigma)dx`

`= lim_{N->infinity} sum_{m,n<=N} mu(m)mu(n) K_sigma^[delta,R](m,n)`。

这里 K^[delta,R] 的积分只在 [delta,R] 上。随后才让 delta->0、R->infinity，外层对非负积分可用单调收敛，得到 E_sigma（允许 +infinity）。特别可固定顺序 `lim_{J->infinity} lim_{N->infinity}`，积分窗为 [1/J,J]。没有一个有限截断值能自行认证无限能量有限。

### 5.2 明确算术假设下的方形 Gram 截断

若另已证明 `|M(t)|=|sum_{n<=t}mu(n)|<=C t^theta`（t>=1），其中 `0<theta<sigma<2`，则完整核可以按方形截断得到能量。给出充分条件的证明，而非默认 RH。

对 `R_N=P2-P2_N`，分部求和给

`R_N(x)=-M(N)f_x(N)-integral_N^infinity M(t) f_x'(t)dt`，

其中 `f_x(t)=t^(-2)exp(-x/t^2)`，`f_x'(t)=2t^(-3)exp(-x/t^2)(x/t^2-1)`。所以

`|R_N(x)| <= C N^(theta-2)exp(-x/N^2)`

`+2C integral_N^infinity t^(theta-3)exp(-x/t^2)(1+x/t^2)dt`。

若 x<=N^2，直接积分得到 O_theta(N^(theta-2))。若 x>=N^2，令 u=x/t^2，积分控制为常数乘 `x^((theta-2)/2)`；相关 Gamma 积分在 theta<2 时有限，边界项也有同一界。因此

`|R_N(x)| <= C_theta * {N^(theta-2), x<=N^2; x^((theta-2)/2), x>=N^2}`。

分割加权平方积分，得到

`||P2-P2_N||_{L2(x^(1-sigma)dx)}^2`

`<= C_theta^2 [1/(2-sigma)+1/(sigma-theta)] N^(2(theta-sigma)) -> 0`。

故在该明确假设下

`E_sigma = lim_{N->infinity} sum_{m,n<=N}mu(m)mu(n)K_sigma(m,n)`。

这允许指定的方形截断，不允许任意重排一个非绝对收敛双和。RH 通过经典 Littlewood/Mertens 界给每个 theta>1/2 的上述算术假设，因此只在条件推论中覆盖全部 `1/2<sigma<2`。完整能量有限本身不是这里未经说明的交换定理。

## 6. 修正后 RH 等价的完整论证

经典输入：Riesz 判据为 `RH <=> P2(x)=O_epsilon(x^(-3/4+epsilon))` 对每个 epsilon>0、x->infinity 成立。[Agarwal–Garg–Maji 的原始研究论文](https://arxiv.org/pdf/2202.00637) 第 2 页式 (1.5) 及 Theorem 1.2 给出同一 P2 定义和判据；第 10 页式 (3.20) 给出上节用到的 RH 条件下 Mertens 界。本审计只调用这些经典输入，不调用该文 Lemma 2.4 延拓后的表达来替代不收敛的原 Mellin 积分。

**RH 推出修正能量族。** 固定 `1/2<sigma<2`，选择 epsilon>0 使 `2epsilon<sigma-1/2`。Riesz 界给

`|P2(x)|^2 x^(1-sigma) = O(x^(-1/2-sigma+2epsilon))`，

该指数严格小于 -1，所以无穷端可积；零端由 sigma<2 保证。每个 sigma 的 epsilon 单独选择，不宣称临界 sigma=1/2 的能量有限，也不需要简单零点假设。

**修正能量族推出 RH。** 设每个 `1/2<sigma<2` 的 E_sigma 有限。考虑普通 Mellin 积分

`F(s)=integral_0^infinity P2(x)x^(s-1)dx`。

零端因 P2 有界，在 Re(s)>0 绝对可积。设 u=Re(s)<3/4，选择 `1/2<sigma<2-2u`。Cauchy–Schwarz 给

`integral_1^infinity |P2(x)|x^(u-1)dx`

`<= E_sigma^(1/2) [integral_1^infinity x^(2u+sigma-3)dx]^(1/2) < infinity`。

在任意闭子带取同一个 sigma 并留严格余量，可控制对 s 的导数所带的 log x 因子；故 F 在 `0<Re(s)<3/4` 全纯。

在初始子带 `0<Re(s)<1/2`，有

`sum_n |mu(n)| n^(-2) integral_0^infinity exp(-x/n^2)x^(u-1)dx`

`=Gamma(u) sum_n |mu(n)| n^(-2+2u)<infinity`，

从而严格逐项积分得到

`F(s)=Gamma(s)/zeta(2-2s)`。

以亚纯函数恒等定理延续**这一恒等式**到整个 `0<Re(s)<3/4`。由于左边 F 全纯，Gamma 在此既无零点也无极点，1/zeta(2-2s) 不能有极点。任何 Re(rho)>1/2 的非平凡 zeta 零点都会在 `s=1-rho/2` 产生这种极点，矛盾。zeta 在 1 的极点对应 1/zeta 的零点，不构成障碍。再用 zeta 函数方程的零点对称性，得到 RH。这里没有把一个发散 Mellin 积分强行解析延拓成普通积分：全纯性先由假设能量和 CS 独立建立。

尾能量版本与此等价：若原修正族有限，则对 sigma<2 尾部当然有限；对 sigma>=2，x>=1 时被任取较小 sigma_0∈(1/2,2) 的权重控制。反过来，尾能量族加上已证明的 sigma<2 零端可积，给出原修正族。

## 7. 最小正确可调用合同

| 调用对象 | 参数与可返回结论 | 必须保留的限制 |
| --- | --- | --- |
| 原 P2 与原完整 E_sigma | P2 用第 84 行未减常数定义；sigma>=2 可直接返回 `DIVERGES_AT_ZERO` 及第 2 节证书。 | 不用 RH；不能改定义后仍冒充原 E。 |
| 有限完整 Gram | 正整数有限索引集、有限实/复系数、实 sigma<2；返回第 3 节核与有限 PSD 恒等式。 | 核一般为实数权重，不伪报有限正有理 BRC 库已求得所有超越量。 |
| 无限完整 Gram 的绝对和 | `1<sigma<2`；绝对求和等于 E_sigma，且无条件有限。 | `.5<sigma<=1` 不接受绝对交换。 |
| 临界带有符号能量 | `.5<sigma<2`；无条件仅准许“有限 x 窗先取 N 极限，再扩窗”的有序定义。 | 若要先积分到 infinity 后取方形 Gram 极限，提供上节 Mertens 界或另一个已证 L2 收敛条件。 |
| RH 等价接口 | `for every .5<sigma<2: E_sigma<infinity`，或 `for every sigma>.5: E_tail(sigma)<infinity`。 | 这是等价判据，不是已经成立的有限性；临界 sigma=.5 不含在内。 |
| 尾核替代 | 全部实 sigma 的有限 Gram 可用上不完全 Gamma 核。 | 它是新声明的尾积分核，不等于原完整 Gamma 核；绝对无限交换仍需 sigma>1。 |

BRC 的正载体和 Möbius 最终符号观测保持区分。有限核 PSD、无穷能量存在、绝对交换、RH 条件下的有符号极限是四个不同结论。本修正仅为这些结论补齐域和量词，不更改 P000、X6 原生维度或历史其他数学路线。

## 8. 小证据与状态

`owner_rh_energy_domain_20260907_check.py` 只使用标准库 Fraction，本次执行 PASS，完整输出已保存到同名 `.json`。它验证有理零端证书、sigma=5/2 的增长下界、192 个整数 sigma 核重写、64 个临界系数平方恒等式及几个有限 Möbius Gram 值。有限值不用于推断 RH 或无限能量收敛。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
