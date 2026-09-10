# X6：更紧算术主项、乘数窗口前沿与符号见证安全压缩

Status: `RESEARCH_NOTE / PROOFS_IN_DECLARED_MODEL_AND EXACT_FINITE_CHECKS / NOT_INDEPENDENTLY_REVIEWED / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-11` (Asia/Taipei)
Researcher-ID: `EM-X6CM-F01144`
Research-Activity-ID: `RA-X6CM-F01144F76207`
Progress-Event-ID: `X6CM-SHARP-MAJORANT-WINDOW-20260911-11`
Mode: `DIRECT_USER_CONTINUATION / NO_FORMAL_TASK_CLAIM`
EM input snapshot: `cb8c275d6c330c1453fe34077f5271cda82e86b1`
Global input snapshot: `23caf7055b65cdbc453b73112d241292d0d84e21`
Parent: `research_notes/x6_sharper_logloss_and_multiplicative_windows_20260911.md`

## 0. 目的、并发吸收与不重复发布

当前远端已存在 `X6CM-LOGLOSS-WINDOWS-20260911-10`，它已经证明同一冻结族在 `o(X/log X)` 例外之外可取 `lambda1 >= N^(1/6)/(sqrt42*k^(3/8))`，并保护 `m <= 13 floor(k^(1/12))` 的增长乘数窗口；同时保留四个已锁定种子和全部先前研究节点。

此前本会话本地待发布稿中与该远端节点重合的 `3/8` 结论、共享种子秩公式和锁定回归不再另行重复提交。本文件只吸收其中尚未被远端覆盖的更紧算术主项，并在远端窗口定理基础上推出新的参数前沿。

保留相同模型：`R=Z[x]/(1+x+...+x^6)`、额外七阶整数作用 `U`、原生六轴格与 `Q(z)=sum z_i^2`、固定好种子乘积测度、全部合数观察、四个有限锁定。`U` 仍不是 P000 原生等距旋转；普通自然数算术不变。

## 1. BRC：先固定观察，再允许一个局部安全的 ± 压缩

本轮目标观察是布尔事件

    E_N(rho) = {存在 0!=z in M(N), Q(z)<rho^2}.

原细对象仍是带方向的整数向量 `z`、其局部种子/素数块 provenance、CRT 联合关系和未来 `U` 操作。对一般运输、方向、未来操作，`z` 与 `-z` 不能默认合并。

但仅对上述布尔短向量存在事件，因每个加性子格满足 `L=-L` 且 `Q(-z)=Q(z)`，映射 `z -> {z,-z}` 有精确观察下降证书。若

    Z_N(rho)=#{0!=z in M(N):Q(z)<rho^2},

则 `Z_N` 必为偶数。因此

    P(E_N(rho)) <= E Z_N(rho)/2.                         (1)

这是一个仅对布尔存在观察安全的常数因子改进，不用于删除方向 provenance，也不改变任何对数指数。后文为与父节点常数直接可比，仍使用父节点未除2的一阶矩界；式(1)只作为已证可选常数优化保留。

## 2. 定理 A：条件化算术主项的平均指数从 1/8 降到 5/59

沿用父节点

    a=64/59, c=a-1=5/59,
    F(n)=a^omega(n) product_(p|n)(1+1/p).                (2)

父节点已证 `A(n)<=F(n)` 与 `F(mn)<=F(m)F(n)`。定义非负平方自由乘法函数 `g`：

    g(1)=1,
    g(p)=c+a/p,
    g(p^j)=0, j>=2.

逐素数展开得到精确恒等式

    F(n)=sum_(d|n) g(d).                                 (3)

于是对 `X>=2` 与任意 `epsilon>0`，

    sum_(n<=X)F(n)
      = sum_(d<=X) g(d) floor(X/d)
      <= X sum_(d<=X)g(d)/d
      <= X^(1+epsilon) sum_(d>=1)g(d)/d^(1+epsilon).

绝对收敛区内

    sum_d g(d)/d^(1+epsilon)
      = product_p [1+(c+a/p)p^(-1-epsilon)]
      <= exp(c sum_p p^(-1-epsilon)+a sum_p p^(-2-epsilon))
      <= e^a zeta(1+epsilon)^c.                          (4)

这里 `sum_p p^(-1-epsilon)<=log zeta(1+epsilon)`，而 `sum_p p^(-2-epsilon)<1`。取 `epsilon=1/log X`；积分比较给 `zeta(1+epsilon)<=1+1/epsilon`，且 `X^epsilon=e`，故

    sum_(n<=X)F(n)
      <= e^(1+a) X (1+log X)^c
      < 16 X (1+log X)^(5/59).                          (5)

这严格强于父节点的 `O(X(log X)^(1/8))` 指数，因为 `5/59<1/8`。证明不使用素数定理、Mertens 定理、RH 或合数事件独立性。常数16刻意粗，不宣称最优。

## 3. 定理 B：例外强度、几何损失与乘数窗口的参数前沿

父模型的一阶矩界可写为

    P(E_N(gamma)) <= F(N)/(64 k(N)^(6 gamma)),           (6)

其中

    E_N(gamma)={lambda1(M(N))<N^(1/6)/(sqrt42*k^gamma)},
    k(N)=floor(log2 N).

固定 `beta>=0`，目标是在起点 `N<=X` 中只允许

    o(X/(log X)^beta)

个失败。再固定 `alpha>=0`，要求同一个起点同时保护所有

    1<=m<=C k(N)^alpha                                  (7)

的乘积 `mN`，`C>0` 是任意固定常数。

由次乘性与(5)，对 `k=k(N)`，

    P(exists m in window with E_(mN)(gamma))
      <= F(N)/(64 k^(6gamma)) * sum_(m<=Ck^alpha)F(m)
      << F(N) k^(alpha-6gamma)(1+log k)^c.               (8)

在 `2^k<=N<2^(k+1)` 上再用(5)，若 `c_k` 是失败起点数，则非负损失

    H=sum_k k^beta c_k/2^k

的第 `k` 项期望满足

    E[k^beta c_k/2^k]
      << k^(beta+c+alpha-6gamma)(1+log k)^c.             (9)

因此只要

    6 gamma > 1 + beta + c + alpha,                      (10)

右侧可求和。与父节点相同的二进分组论证给出一个保留任意有限好种子锁定的永久族，使窗口失败起点满足

    #{N<=X: window failure}=o(X/(log X)^beta).            (11)

这是同一冻结族、同一观察和同一合数人口上的结论，不是给不同 `N` 重新选种子。

### 临界窗口

若取等号

    alpha = 6gamma-1-beta-c,                              (12)

则可把窗口缩为

    m <= C k^alpha/(1+log k)^eta                         (13)

并要求

    eta > 1+c = 64/59.                                   (14)

此时(9)化为 `1/[k (log k)^(eta-c)]` 型可求和级数。临界式只说明当前一阶矩/卷积法的可证边界，不声称几何本身无法超过它。

## 4. 直接改进父节点：3/8 门槛下，窗口可从 k^(1/12) 推到 k^(1/7)

保持父节点的例外强度 `beta=1` 和几何损失 `gamma=3/8`。由(10)，允许的多项式窗口指数满足

    alpha < 6*(3/8)-2-5/59
          = 39/236
          ≈ 0.165254.                                    (15)

因此可取简单的

    alpha=1/7≈0.142857,                                  (16)

其严格求和余量为

    39/236-1/7 = 37/1652 >0.                             (17)

所以存在保留当前四个有限锁定的同一永久族，使除 `o(X/log X)` 个起点外，所有

    1<=m<=13 floor(k(N)^(1/7))                           (18)

的 `mN` 同时满足父节点 `gamma=3/8` 的 `lambda1` 下界及其 `lambda6`/无盒运输上界。

父节点窗口指数为 `1/12`；本轮将其提高到 `1/7`，没有改变 `3/8` 几何门槛或例外计数强度。`13` 仍只是固定窗口常数，不是自然常数。

一个有限尺度差异：`floor(k^(1/7))` 首次达到2是在 `k>=128`，而 `floor(k^(1/12))` 首次达到2要到 `k>=4096`。这只是窗口参数的可见性比较，不构成计算复杂度结论。

临界地，可取 `alpha=39/236`，但需除以 `(1+log k)^eta`，`eta>64/59`。

## 5. 单目标的当前一阶矩临界指数：41/118

令 `alpha=0,beta=1`。由(10)，纯多项式阈值需要

    gamma > (2+c)/6 = 41/118 ≈0.3474576.                 (19)

这严格低于父节点从 `1/8` 平均指数得到的 `17/48≈0.3541667`。若要落在临界等号，可像此前本地推导一样加入迭代对数：

    lambda1(M(N))
      >= N^(1/6)/[sqrt42*k^(41/118)*ell(k)^(1/3)],       (20)
    ell(k)=1+floor(log2 k),

仍可保持 `o(X/log X)` 例外计数。这里 `ell^(1/3)` 对应概率预算中的 `ell^2`，不能在当前非负求和法里直接删除。

在这个临界单目标门槛上，仍可同时保护缓慢增长的乘数窗口：对任意固定 `0<=theta<1`，可取

    m <= C ell(k)^theta,                                 (21)

并保持 `o(X/log X)` 的失败起点。若希望达到 `theta=1`，需要再除以 `(1+log ell(k))^eta`，`eta>64/59`。这是(9)在临界 `k` 指数下对迭代对数预算的直接计算。

## 6. 为什么本轮没有声称“二阶矩已经解决”

父节点已经给出共享种子的精确联合秩公式：两个或多个向量事件的联合概率取决于合并 Krylov 约束的秩；协方差既可正也可负。仅知道二阶矩，不会自动给出比 Markov/并集界更强的坏事件上界。

首先，`z` 与 `-z` 是完全重复见证；若不先按当前布尔观察做安全的 ± 商，二阶矩会被这种结构性重复污染。式(1)完成了这一最小安全压缩。其次，即使去掉符号重复，共享局部块仍有正相关见证，因此不能把剩余事件按独立 Bernoulli 处理。

下一步若继续二阶矩，应在保留向量/素数块 provenance 的前提下，统计**不同 ± 见证类**之间的 Krylov-span 交叠数，并把联合秩公式求和成真正的 factorial-moment 或 Hunter/Janson 型证书。没有这个重叠计数，就不把“有联合概率公式”包装成“已有集中定理”。

## 7. 精确有限检查与状态

新验证脚本 `experiments/x6_sharp_majorant_20260911/verify.py` 完成：

- 32767 个 `F(n)<=tau(n)` 精确有理检查；
- 前2048个整数的卷积恒等式 `F(n)=sum_(d|n)g(d)`；
- 参数恒等式 `alpha_crit=39/236`、显式窗口 `1/7` 的求和余量 `37/1652`、单目标临界 `gamma=41/118`；
- 对布尔短向量存在观察的 ± 安全商最小示例。

有限数值仅作一致性检查。无穷平均界、窗口前沿和临界迭代对数结论由本文证明承担，不是数据外推。

本轮没有选择第五个种子、没有改变四个锁定、没有重新计算并宣称旧运输成本是新发现，也没有修改 Foundation/Working Truth。

## 8. 当前最小未解单元

在父节点联合秩公式基础上，对固定 `N` 的短向量候选先按 ± 类分组，再统计不同见证类在每个共享局部块中的 Krylov-span 交叠。目标是得到一个可求和的二阶 factorial-moment 上界或一个严格的 union 上界改进，并判断它是否能改变(10)中的指数前沿，而不是只改善常数。

若二阶项只给常数改善，应明确记录该负结果；不要用相关性术语替代实际的异常集指数改进。
