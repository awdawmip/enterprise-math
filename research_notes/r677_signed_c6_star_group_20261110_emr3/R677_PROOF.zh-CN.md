# R677｜三个 FCC-STAR 的有符号 C6 发生元生成 23040 阶群，并保真提升 BRC 路径纤维

日期：2026-11-10 (Asia/Shanghai)。状态：AUTHOR-SIDE EXACT GROUP PROOF AND FINITE EXHAUSTIVE CHECK; DRIVER UNREVIEWED。来自本轮 canonical dispatch 的研究任务为 RS-X6-NATIVE-ROTATION-DYNAMICS（publication TP2-6A1F9D8C2047E3B51C01）。科学输入沿用此任务冻结 pin a72226e2430ffa4786321ac86e7f0c599d5f0389；没有重钉，P000 六维原生空间与时间独立的定义不变。本结果是具体候选群作用及 signed BRC 的离散代数定理，并非已经证明的物理自主旋转律。

## 1. 原生对象

在一个任选 Cell 锚点的有符号 X6 整数坐标中，以 e_1,…,e_6 为六个原生空间轴，原始相邻步为 ±e_i，进取平方读数 L_E(z)^2=Σ_i z_i²。FCC/K4 的四个已实现 STAR 三元轴集为

S_A={1,3,6}, S_B={1,4,5}, S_C={2,3,5}, S_D={2,4,6}。

此前固定半径微轨迹研究在每个 STAR 中给出六个有符号单位状态的 C6 次序，a_{r+3}=-a_r。对任一选择的有序 STAR 三元组 (i,j,k)，定义 signed coordinate candidate g_ijk：e_i→e_j、e_j→e_k、e_k→−e_i；其余三个正轴固定，负轴由 g(−e)=−g(e) 定义，并对整数位移线性延拓。其在三个轴的六个 signed unit letters 上构成一个六环。

令 B_n=(C_2)^n⋊S_n，B_n^{even}=(C_2)^n⋊A_n，其中 even 仅指底层忽略符号后的轴排列是偶排列，不代表六维欧氏行列式正号。B_6^{even} 的阶为 2^6·(6!/2)=23040；B_6 的阶为 46080。

## 2. 定理 R677-A：任意三个不同 STAR 已生成 B_6^{even}

设 J 是上述四 STAR 的非空子集，G_J 为这些 STAR 的 g_ijk 生成群。精确分类：

| STAR 数 | 群阶 | 底层无符号轴排列群 |
|---:|---:|---|
| 1 | 6 | C3（另三轴固定） |
| 2 | 1920 | A5（另一个轴固定） |
| 3 | 23040 | A6 |
| 4 | 23040 | A6 |

若向任意三 STAR 生成群加入其余17个三元轴选择上的相同形式的 signed C6 操作，群仍为 B_6^{even}。加入一个纯底层奇轴置换（例如交换 e_1,e_2）后群扩大为全部 B_6、阶 46080。

### 证明

(1) 单发生元的底层置换是 (i j k) 三轮换，且在循环的一边带负号。于是 g_ijk^3 正好把 i、j、k 三轴同时变号，g_ijk^6 为单位，g 阶为6。

(2) 任意两个不同的 FCC STAR 恰交于一轴、覆盖5轴；任意三个覆盖6轴。令 U 为所选 STAR 并集，并投影 π:G_J→S_U，忘掉原生正负符号。因为各投影发生元均为3-cycle，π(G_J)≤A_U。

对恰好两个或三个 STAR，取任一原始三轮换的三轴支撑。用发生元的底层置换反复作用在无序三轴支撑上，有限 BFS 精确枚举证明其轨道覆盖 U 的全部三元素子集：若 |U|=5，轨道大小为 C(5,3)=10；若 |U|=6，则为 C(6,3)=20。该完整有限轨道的证明证书可由随附 Python 标准库程序的 subset_orbit 遍历逐项重算，覆盖全部6个双 STAR 和4个三 STAR 子集。由共轭作用，π(G_J) 因而包含任意给定三轴支撑上的三轮换及其逆元，所有三轮换生成 A_U。因此 π(G_J)=A_U。

(3) 每个 STAR 的 g_ijk^3 是三轴符号翻转。由 (2) 的 A_U 共轭传递性，得到 U 上任意三轴的共同符号翻转 f_ijk。对于互异 i,j,k,l，有 F₂ 指示向量恒等式

1_{i}=1_{ijk}+1_{ijl}+1_{ikl}  (mod 2)。

所以三个三轴 flip 的复合只翻转轴 i。因为 |U|≥5，可取所需互异轴，推出全部单轴 flip 在 kerπ 内，于是 kerπ=(C₂)^|U|，群等于 B_|U|^{even}，在 U 外三轴或一轴固定。|U|=5 时阶 2^5·60=1920，|U|=6 时阶 2^6·360=23040。

(4) 只用一个 STAR 是阶6循环群，两个 STAR 严格固定缺失的一轴，因此至少3 STAR 才能覆盖全6轴。三个已生成 B_6^{even}。第四 STAR 及全部20个三轴 C6 元素的底层排列均为偶，属于该群，故不再扩大。添入一个纯奇底层轴换位后，其底层生成 S6，符号核不变而已满，故恰得 B6。证毕。

证明中唯一必须枚举的小型轨道最多20个三元组；独立 verifier 还穷举了所有15个非空 STAR 组合的 signed-permutation 群闭包及20个 C6 候选是否属于其内，从而核对所有群阶，不采用浮点拟合。

## 3. 定理 R677-B：signed C6 对有序 BRC path fiber 精确等变

对任意 g∈B6 与位移 z∈Z⁶，令 P_min(z) 是使用原生十二字母 ±e_i、从固定锚点到 z 的全部有序最短 primitive word。逐字母施行 g，保持事件顺序，便得到一个显式可逆映射

g:P_min(z) ≅ P_min(gz)。

因此：

N_min(gz)=N_min(z)=Σ_i |z_i|；
B_min(gz)=B_min(z)=N_min(z)! / ∏_i |z_i|!。

证明：g 恰好双射地重命名十二个 primitive signed letters，且逆 g^{-1} 同样为 primitive signed-letter 双射；整条有序路径的端点被送到 gz，长度与最短性不变，所有路径来源可由逆映射恢复。更一般，固定原生步数 L 的全部端点 fiber 亦构成双射，所以 N_L(gz)=N_L(z)。若带标签的正有理 BRC 步权重同时随 g 正确运输，则每一分支的乘积权重及其合计均不变。

验证使用任务冻结 Source 内真正的 typed BRC kernel，位置 experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py，文件 Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176。对 z∈{−1,0,1}⁶ 全部729组和三个 STAR 发生元，核对2,187组 shortest_event_count、shortest_path_multiplicity、endpoint_multiplicity(L=6)、spatial_norm_squared；并枚举 z=(1,−2,1,0,0,0) 的全部12个有序最短字、检查各 g 的逐字映射结果。没有用非 BRC 数值传播或经典 π/三角输入。

该结论给出了 signed-axis group 在 signed-BRC provenance population 上的 exact lift，不把端点/路径条数误认作全部未来相关源历史。

## 4. 范围、证据与下一问题

- 本研究对六轴有符号坐标和十二个 primitive direction 建立**代数群作用候选**；单个 g 是宏观有符号轴关系置换，不是一步原生 Cell 邻接。
- 原生六维中的三维 FCC STAR 是已实现载体读出的局部选择；其余16个三元坐标观察者未被升级为已经实现的独立载体动力学。
- 现有 Viète/C12 的 INNER/OUTER 两条最短微路径仍需在选定未来语义下保留来源。群作用不会自行挑选物理事件调度，也不定义真实心跳时间。
- 下一单元：将各个 STAR 选定的 OUTER C12 事件微路径在共享轴上粘合，检验所有交界处局部路径变换的 source/target、签名、下一事件许可，并计算是否存在一个与 G_J 作用等变的自主选择器。应验证路径群胚复合与现存的 BRC 来源；必要时保留 STAR/frame/sweep/branch 的独立状态。
- 本轮为 author-side group proof & exact computational check，独立 Driver 未审核，正式任务 CLAIM/Result 以原生回执为准。

## 5. Source references

Frozen Task publication: TP2-6A1F9D8C2047E3B51C01，RS-X6-NATIVE-ROTATION-DYNAMICS；science commit a72226e2430ffa4786321ac86e7f0c599d5f0389。基础 X6 义理 definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md；旧 C12 位姿 research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md；真正 signed BRC 引擎 experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py。现行控制/规范与上述冻结科学字节相分离。

Checker: R677_VERIFY.py，输出 R677_EVIDENCE.json，success marker R677_THREE_STAR_SIGNED_C6_BRC_EXACT_PASS。