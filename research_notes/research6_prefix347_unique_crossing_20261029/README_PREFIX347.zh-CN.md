# PREFIX-347｜完整六条 BRC 来源相位弧穿越风险基准 L 的唯一性证明

日期：2026-10-29。成果状态：AUTHOR_SIDE_EXACT_RATIONAL_T6_STRICT_MONOTONICITY / UNREVIEWED / NOT_ADMITTED。该证书适用于静态辅助复三维 S7-3 BRC 模型中已经精确隔离的六条具体来源的完整连续相位弧 T6(h)；完整真实来源纤维 S(h) 可能包含额外来源。

## 冻结输入和新定理

带来源标签的五 Port 振幅为 A 的五行：(4,4,0)，(0,-4,4)，(-5+3i,0,-3+i)，(-2-2i,4+4i,2+2i)，(-2,0,5+2i)，U=A/8，lambda=10/61，准确质量 q=(2125/3721,200/3721,29125/29768,5825/7442,31525/59536)。PREFIX-342 的六个 Newton–Banach 根盒（半径 10^-29）各有唯一复来源 a_j。令 w_j=(Ua_j)_3，则 |w_j|²=q3=29125/29768。

共同报告仅第三 Port 虚部目标为 h>1，其他九项为零，十项各容差 1，整体复相位保留。令 T6(h) 为六条具体来源的全部允许相位，F(h)=MEB²(T6(h))，L=1062562/458329。

在 I=[h_-,h_+]，h_-=166639681/100000000=1.66639681，h_+=83319841/50000000=1.66639682 内，证明全部实参数 h 均有：
- 最优球恰由五个端点 (0,-),(1,+),(3,-),(3,+),(4,+) 构成严格正接触，且球心唯一；
- 七个非接触端点严格在球内，端点覆盖由严格凸性扩展到六条完整连续相位弧；
- 平方半径可微，严格满足 -19811/10000 < F'(h) < -19808/10000 < 0。

PREFIX-346 的左右端点严格证书已在本轮实际重新执行：F(h_-)≥V(h_-)>L+10^-10，F(h_+)<L-10^-9。由连续性、严格递减，方程 F(h_c)=L 在 (h_-,h_+) **存在且仅存在一个解**。

## 数学证明

写 y=h-1，s(h)=sqrt(q3-y²)>0，b_j=conj(w_j)a_j/q3。每一来源弧端点精确为 p_{j,±}(h)=(±s(h)+iy)b_j，端点导数 p'_{j,±}(h)=(∓y/s(h)+i)b_j。第三 Port 以外的报告分量因其 q_i<1 自动可行；第三 Port 的实部也自动可行。因此每个相位集合正是 Im(z)≥y 的上圆弧，不存在额外角度采样假设。

将五接触点依次记作 p0,...,p4，d_k=p_k-p0 (k=1,...,4)，令 G_kl=Re⟨d_k,d_l⟩、rhs_k=G_kk/2。定义 beta=G^{-1}rhs，c=p0+Σ beta_k d_k，alpha=(1-Σ beta,beta_1,...,beta_4)。Gram 线性恒等式给出 ||p_k-c||²=||p0-c||²。严格 alpha_k>0 且 Σalpha_k=1、c=Σalpha_k p_k 时，对任意 c' 有

  max_k ||p_k-c'||² ≥ Σ alpha_k ||p_k-c'||²
                      = ||p0-c||²+||c'-c||².

所以 c 是五点唯一最小球心，若其余七个端点被同球严格覆盖，则是全部十二端点的唯一最小球。

对每条上圆弧，令 z=x+i sqrt(q3-x²)、x∈[-s,s]，定义 t_j=⟨c,a_j⟩/w_j。平方距离等于

  ||a_j||²+||c||²-2x Re(t_j)+2sqrt(q3-x²) Im(t_j).

若 Im(t_j)<0，此函数严格凸，弧上的最大平方距离由两个端点达到。因此十二端点覆盖即六条连续相位弧覆盖，五个正接触端点确实决定 F(h)。

在整个 I 上五点等距、alpha>0 且 c=Σalpha p。对 F=Σalpha_k||p_k-c||² 求导，alpha'_k 项因等距且 Σalpha'_k=0 消去，c' 项因 Σalpha_k(p_k-c)=0 消去，严格恒等式为

  F'(h)=2Σ_{k=0}^4 alpha_k(h) Re⟨p_k(h)-c(h),p'_k(h)⟩.

该式在 h 全区间成立，不要求另行数值微分最优球心。

## 全区间 Fraction/整数平方根严格证书

实际执行的 verify_prefix347.py 使用 Python Fraction 和整数平方根，包络**整段 I**、所有六个半径 10^-29 的代数根盒。以 Gram 区间中点的精确有理逆 B 及有理近似 beta0，设 E=I-BG、u=B(rhs-G beta0)，delta=||u||∞/(1-||E||∞)。由于 ||E||∞<1，Neumann 级数保证整个 I 上的 G 可逆，beta 的四个坐标各落在 [beta0-delta,beta0+delta]。

证书全部严格断言：
- ||I-BG||∞ < 1/100000；delta < 1/400000；
- 五个接触权每个 alpha_k > 1/10000；
- 七个非接触端点的半径平方内余量 > 3/1000；
- 六个 Im(t_j) < -97/100；
- -19811/10000 < F'(h) < -19808/10000。

所有不等式均由精确有理区间决定；输出中浮点数只用于浏览。程序通过 runpy 重新执行 PREFIX-342 的六根存在唯一性、五 Port 完整45项保留来源标签的有序 BRC 路径对，以及 PREFIX-346 的端点严格异号证书。此为作者侧的 exact computation 和解析证明，未经过独立 Driver 审核。

## 版本、复现和未决义务

冻结 GLOBAL_KNOWLEDGE_V1 main@61759c9e6113a3dc1e1711d8acc80e40c424b3d8、Enterprise Math main@4ffdef264544aeea65b68be98a36ab5a829d9f12，读取现行 P000、ACTIVE 世界观、可移植研究协议、定时研究协议和 BRC 优先约束。执行环境 Python 3 / SymPy；将本目录 verify_prefix347.py 与 PREFIX-342 的 verify_prefix342.py 和 PREFIX-346 的 verify_prefix346.py 放在同一目录运行即可复现，生成 RESULTS_PREFIX347.json。两个前驱的不可变科学提交分别是 1180caebc14a3470bca9624d8cb56d1467d6dc3d 和 3b7795e5522fd1f57360b4360d6e5d024d8fe8c2。

本轮源代码本地 SHA-256 为 1d615596147c062ac13f747b7e037711447d7b1bf62ea97f522adb405fde59f2；完整机器 JSON SHA-256 为 33531161855555a854020f6d650f6e4069cb6ebd2e4e23d5b45bb97d3ba738eb。当前 Sites 只读查询显示 research_authority_granted=false，活跃 owner 查询返回 CONTROL_QUOTA；本成果是便携研究材料，不授予 CLAIM、Source Result、Driver Review 或数学准入。

待证关键依赖：PREFIX-335/336/339 的全域来源穷尽性，包括消元分母、无穷远根、Sturm 根计数及正 Hermitian 回代。只有证明 S(h)=T6(h)，才能将本定理升级为全部来源风险的唯一穿越。辅助 C³ 与 P000 原生 X6、三维切片第三分量、Detector、联合观察、独立时间演化的保真映射仍须独立构造。下一单元参见 NEXT_PREFIX348.md。
