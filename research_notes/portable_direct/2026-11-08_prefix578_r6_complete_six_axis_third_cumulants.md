# PREFIX-578-R6：六轴 BRC 与原生门控的完整三阶联合累积量

日期：2026-11-08（Asia/Shanghai）。研究状态：`AUTHOR_COMPUTED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED`。
科学输入（冻结）：`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`，四 STAR、48 原生相位、96 带分支位端口，每端口六个带标签动作。原始六轴奖励与门控由 `PREFIX565_positive_marginal_certificate.py` 定义；沿用 PREFIX-577-R6 的完整96端口观察和第二阶协方差，不改写科学输入或 P000。

## 科学问题与新结果

令 `X_n=(R_1(n),...,R_6(n),K(n))`，每一步在六个原生动作中等概率选择一个，`R_i` 是第 i 轴 BRC 奖励累计量，`K` 为原生门控次数。对任意初始端口，定义三阶渐近联合累积量率：

[
  kappa_{abc}=lim_{n	oinfty}rac{1}{n}
     operatorname{cum}(X_{n,a},X_{n,b},X_{n,c}).
]

**定理。** 在上述冻结的有限状态 BRC 模型内，该极限对全部七个原生奖励存在，并与初始端口无关；全部 84 个对称三阶分量由 56 个独立的有理数精确确定。具体有：

[
oxed{kappa_{K K K}=rac{206963}{42467328}},
qquad
oxed{kappa_{R_5 K K}=kappa_{R_6 K K}=-rac{6053}{10616832}},
]

[
oxed{kappa_{R_5 R_5 K}=kappa_{R_6 R_6 K}=rac{19}{82944}},
qquad
oxed{kappa_{R_5 R_6 K}=-rac{11}{82944}}.
]

其他独立分量在旁置的 `PREFIX578_R6_EXACT_THIRD_CUMULANTS.json` 中逐一给出，复现程序在 `PREFIX578_R6_compact_third_cumulant_certificate.py`。这些数值是第三阶**渐近联合累积量率**，不是固定路径长度的三阶中心矩。相应的门控独立统计与第五、第六轴对称结构可以作为未来高阶路径不变量的精确输入。

## 完整六轴的56坐标约简

零根处每条原生边恰有一个六轴指标等于1，因此逐条路径**精确**满足：

[
 R_1(n)+cdots+R_6(n)=n.
]

PREFIX-577 的根端点定理与已发布谱共轭证明说明，所许可根的归一化谱压力一致；特别地，对任何阶数 (mge2)，每个与六轴总和方向收缩的渐近累积量张量均为零。因此

[
 oxed{kappa_{R_6,b,c}=-sum_{a=1}^{5}kappa_{R_a,b,c}}
]

并递归重建含多个 (R_6) 的分量。只需 ((R_1,R_2,R_3,R_4,R_5,K)) 六个坐标，因此对称三阶独立计算为 (inom{6+3-1}{3}=56) 项；七维完整结果共有 (inom{7+3-1}{3}=84) 项。这是观察信息的**已证明保真压缩**，不是把原生六维空间减少到五维。

## 精确代数证明与计算证书

设 (P) 为96端口的六动作均匀转移矩阵，(pi=(1/96,ldots,1/96)) 为平稳分布。对于六个独立奖励向量 (mathbf w)，定义带权矩阵

[
 P(t)_{ij}=sum_{a:i	o j}rac16exp(tcdot mathbf w(i,a)).
]

有限原生图强连通，故 (P(0)) 的 Perron 本征值1为单根。选择 (P(t)v(t)=lambda(t)v(t))、(pi v(t)=1)。记 (L=I-P)，(P_a=partial_aP(t)|_0)，其余混合导数类似。以下线性系统均在 (pi v_alpha=0) 的归一化下求解：

[
lambda_a=pi P_amathbf1,qquad
Lv_a=P_amathbf1-lambda_amathbf1.
]

[
lambda_{ab}=pi(P_{ab}mathbf1+P_av_b+P_bv_a),
]

[
Lv_{ab}=P_{ab}mathbf1+P_av_b+P_bv_a
-lambda_av_b-lambda_bv_a-lambda_{ab}mathbf1.
]

第三阶本征值导数无需再解新向量：

[
lambda_{abc}=pileft(
P_{abc}mathbf1+
P_{ab}v_c+P_{ac}v_b+P_{bc}v_a+
P_av_{bc}+P_bv_{ac}+P_cv_{ab}
ight).
]

[
oxed{kappa_{abc}=
lambda_{abc}-lambda_{ab}lambda_c-lambda_{ac}lambda_b
-lambda_{bc}lambda_a+2lambda_alambda_blambda_c.}
]

这些恒等式直接来自三次微分 `P(t)v(t)=lambda(t)v(t)` 与 `log(lambda)`；指标重复时，式中重复项自然提供正确的多项式重数。有限图有周期也不影响 Perron 分支的解析性：对每个周期同余子序列，其权重期望的首项是 (lambda(t)^n) 乘局部解析且在零处非零的系数，因此所有固定阶的对数导数除以 (n) 后趋于 (partial^mloglambda(0))。这是**全长度极限命题**所需的解析桥。

原生奖励均为0/1整数，故 (P_alpha) 按带标签边逐项精确构造，不使用浮点差分。对6个一阶和21个二阶导数右端，调用两轮 Fraction 有理数 Gauss-Jordan，逐行验证全部27个96维 Poisson 等式，再由显式公式计算56项三阶导数。所有21项二阶渐近协方差与 PREFIX-577-R6 所发布的有理数矩阵完全一致，全部三阶六轴守恒收缩 (sum_{a=1}^6kappa_{abc}=0) 对任意 (b,c) 均精确成立。

独立重写的较详细整数/有理数证书与发表的精简版两种实现，对56项有理数三阶结果逐项一致。额外的96端口、平稳起点、原生动作整数路径动态规划，计算门控三阶有限深度累积量除以深度 (n=16,32,64,128)，分别得到约 0.0048768146564、0.0048751423870、0.0048743032624、0.0048738836997，向精确极限 (206963/42467328approx0.00487346413695) 收敛。这是独立有限证据，并不替代上述全阶代数证明。

## 复现与证据边界

将当前目录已发布的 `PREFIX565_positive_marginal_certificate.py`（冻结核）与 `PREFIX578_R6_compact_third_cumulant_certificate.py` 同目录，运行后者。标准库 `fractions.Fraction` 执行全部证明性计算并输出84项完整有理数张量；`ALL_CHECKS_PASS` 出现在终端JSON顶层。Python执行记录：本地精简证书耗时约6.21秒（该时长仅描述一次环境观测）。

本次数学结果为上述原生六轴奖励和门控的随机均匀动作观察的严格模型内计算机辅助定理。冻结根使用零根加一至四轴的八个 (pm e_i)；其余三值根只作过早期代数端点恒等式检查，不用作本次科学输入扩张。36/37类压缩不足以完整保留六轴奖励，因此所有Poisson与三阶运算仍使用96端口。作者与验算不构成独立数学审查，尚未登记原生CLAIM、Result、Review，也未提升为Working Truth。

## 后续最小研究单元

利用已给出的全三阶张量，选择对所有允许根均定义的二/三阶 BRC 观察，对比门控中心化残差 (K-etacdot R) 的三阶偏斜率，其中 (eta=(5,-1,5,-1,-4,-4)/192) 是基于PREFIX-577-R6的精确最优线性二阶补偿。计算其三阶系数，并研究能否得到有符号/无符号分支保真下的非负性或配对对称零式。然后在实际原生Owner/CLAIM恢复后按当前控制协议关联本独立作者证据。
