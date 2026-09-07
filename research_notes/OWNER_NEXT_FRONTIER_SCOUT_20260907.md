# 下一组合决策：原生距离壳的整数锐界与 common-depth 首返尾

状态：`ANCHOR_EXPOSED SCOUT / TWO BOUNDED CANDIDATES / NOT_FORMAL_TASK`。
日期：2026-09-07。内部 owner 辅助工作；不是 CLEAN FREE、首次发现、正式 Researcher-ID
或 V2 审稿。只产出这一份候选笔记，未启动新数值程序、扩大枚举、注册任务或修改生产源码。

**建议先选 A：原生距离壳上最短词长度的整数锐界。** 它有明确全称命题，失败可给
有限整数反例证书，并能直接消费既有 signed BRC 接口。B 是独立的概率/更新理论备选：
研究 all20 相对首返所隐藏的 common-depth **逐点**尾律。B 的矩阈值可以先由已有
经典结果导出，不能继续把它包装为未知；真正缺口是带常数的双侧首返核反演。

## 0. 共同起点与有界去重

当前基础是 `X6_NATIVE_SPATIAL=AFFINE_TORSOR(Z^6)`；固定 anchor 后原生步为十二个
`±E_i`。原生 component quadratic readout 是 `sum z_i²`，原生正角仍为 120°。
每个三轴观察是 `Obs_S(z)=can3(z_S)`；全部二十张共同确定 z 模去
`D=(1,1,1,1,1,1)`，不能把 D 当零位移。

`z=r+hD`，`r=can6(z)`、`h=min z_i` 是无损坐标拆分；common-depth 属于完整原生
空间坐标的复合方向，不是第七空间轴。旧 V14 笔记曾讨论“depth 是否属于 Cell
identity”的不同 cover 选择，但当前 signed foundation 已固定完整 Z^6；不重开旧
本体选择。这里只研究经过明确声明的观察/计算问题。

已经排除本轮禁选的零边缘最小 trade、查询成本、finite HCM 勘误、N8 eta=.9 惯性、
平均 A_i 任意商；也不继续扩大路径监测器或 histogram 可行性实现。

理解两个具体结构后，实际调用了仓库 `tools/enterprise_toolbox.py` 的 coverage 接口：

| 查询 | 实际结果与语义判定 |
|---|---|
| `native signed lattice squared norm shortest path prescribed sum squares` | `REUSE_CANDIDATE_FOUND`；T0/T2/T3/T6/T7/T9 等词面命中。准确现成消费者是下述 `signed_brc.py`，不是那些仅含 signed/root 等词的无关模块。没有命中“固定六平方和时长度锐界”的实现。 |
| `BRC first return common depth random walk Green function` | `REUSE_CANDIDATE_FOUND`；T0/T12/T1/T2/T3/T4/T8 及 recurrent/moment 类候选。实际 finite recurrent 和 port 模块都限制有限状态；没有覆盖这里无限相对格上的 common-depth 首返尾。 |

进一步有界阅读了原生 signed 代码、有限 recurrent/port API、已有 path monitor 的
positive excursion / horizon 合同。`FREE_RESEARCH_POST1161_ADAPTIVE_RETURN_DEPTH_RESOURCE_LAW_20260904.md`
的 return-depth 是 AGM shape RG 的有限截断层，输入对象不同，不能据同名判为已覆盖。
此有界检查不构成全库、全数学新颖性认证。

实际可复用接口：

- `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`：
  `spatial_norm_squared`, `shortest_event_count`, `shortest_path_multiplicity`,
  `endpoint_multiplicity`, `endpoint_weight`。
- 同目录 `x6_signed.py`：`relative_class`, `from_residual_depth`, `depth_carry`,
  `joint_slice_equal`, `hidden_slice_coordinates`。
- `src/enterprise_math/brc_histogram.py`：完整 exact-weight Histogram 串联/再汇合；
  不重造长度、count、质量或直方图家族。
- `brc_recurrent_ports.recurrent_port_signature`：仅稳定的有限 hidden block；
  `brc_weighted_recurrent` 明确把无限状态递归留在接口之外。
- `experiments/owner_path_monitor_20260907/path_monitor.py` 的
  `port_excursion_series` / `verify_port_series`：有限图、正长度 excursion、有限 horizon。
  可做未来有限证据 consumer；不能直接认证本笔记的无限尾。

## A. 第一候选：距离壳的最短原生词长度是否总达到奇偶锐界？

### 原生对象和真实 consumer

对每个整数 `N>=0`，考虑完整 raw signed 距离壳

`S_N={z∈Z^6 : sum z_i²=N}`。

已有 signed BRC 给每个端点的最小 primitive event 数
`ell(z)=sum |z_i|`，以及最短原生词数
`B_min(z)=ell(z)!/product |z_i|!`。新的 consumer 需要知道：仅声明原生平方距离 N
时，壳内最坏的**最短路径事件数**究竟是多少，并返回达到者的 raw z、全部 joint
can3 观察、common-depth 和可复用的 BRC 词数。这不是对固定 z 的旧公式改名，也
不是把已有 N=25 的三轴枚举上限换成一个更大的数字。

定义

`L_max(N)=max_{z∈S_N} ell(z)`，

`U(N)=max{k∈N_0 : k²<=6N and k≡N (mod 2)}`。

Cauchy–Schwarz 和 `z_i²≡|z_i| (mod 2)` 已直接证明 `L_max(N)<=U(N)`。
**精确未知命题 A：是否对每个 N>=0 都有 `L_max(N)=U(N)`？**

这里的“未知”是此轮有界覆盖后尚未完成的命题，不声称它是数学界公开难题。
符号取绝对值只用于这两个量的证明；返回的原生 Cell、signed 路径和 can3 观察
仍要保留，不能把不同 signed 端点宣布成同一个 Cell。

### common-depth / 固定和平方和的准确桥

充分性等价于寻找六个非负整数 a_i 满足

`sum a_i=U(N)`，`sum a_i²=N`。

令 `U(N)=6b+r`，`0<=r<6`，写 `a_i=b+u_i`，问题变为

`sum u_i=r`，`sum u_i²=N-6b²-2br`，`u_i>=-b`。

这是固定线性和的二次整数表示，不是仅检验模数的 relaxation。b 是平均值附近的
辅助整数中心，**并不自动等于 common-depth**。真正输出还须计算
`h=min a_i=b+min u_i`、`R=can6(a)`，并核对

`N=6h²+2h sum R_i+sum R_i²`，`U(N)=6h+sum R_i`。

例如手算 `N=25`，`U=11`，`a=(3,3,2,1,1,1)` 达到平方和 25、长度 11，
`h=1`、`R=(2,2,1,0,0,0)`，BRC 最短词数为 `11!/(3!3!2!)=554400`。
这是一个起始证人，绝不是全称命题的数值证明。

### 一手来源：只选一篇、只取所需引理

已读 Meng–Sun，*Sums of four polygonal numbers with coefficients*，
Acta Arith. 180 (2017)，[期刊原文](https://www.impan.pl/shop/en/publication/transaction/download/product/92360)，
尤其 Lemma 2.4 和式 (2.2)。其四平方固定和引理要求 `B²<4A`、
`3A<B²+2B+4`，以及 `A,B` 都奇数，或 `A≡2 (mod 4)` 且 B 偶数；结论给四个
非负整数平方和 A、坐标和 B。原文用 Gauss–Legendre 三平方判别与整数 Hadamard
变换证明，并实际处理非负性。这提供具体构造工具；它没有直接陈述上述六轴全称
锐界。下一步可选两个 a_i 后对剩余四项检查该引理，所有奇偶/正性前提都必须保留。

### 成功、反例与停止条件

成功：给所有 N 的整数构造证明，或证明 N>=N0 且用**完备有限**证书处理 N<N0；
原 raw 矩阵/向量检查器只验证给定证人，不靠猜测上界来宣告构造存在。

反例：某个具体 N，对 `sum a_i=U(N)` 的全部六项非负整数分拆给可重放穷举证书，
或给严格整数表示阻碍；同时另给一个合法壳端点，说明差距不是空壳造成。仅“没有
搜到”不算。不能以有限样本支持全称命题，也不能以模约束通过代替整数存在。

停止条件：若准确的一手定理已完整覆盖同一六变量/非负/固定和合同，停止研究
“新定理”，只做短的 typed reuse；若通用断言出现反例，立即关闭全称版本，转为
该反例背后的模类或 common-depth 缺陷机制，不无条件改成更大的参数搜索。若
构造只在丢掉 common-depth 后成立，则拒绝该构造。

替代路线：研究有明确反例支撑的整数亏损 `U(N)-L_max(N)`，或由现成固定和
平方和引理给经证明的有界亏损；先由 owner 决定，不自动新开一般二次型工具族。

## B. 第二候选：相对首返隐藏的 common-depth 逐点重尾

### 原生对象和真实 consumer

额外声明一个研究用正有理 BRC 步律：每个 `±E_i` 的分支权为 `1/12`，每条
primitive step 用一次既有离散时间 tick。概率解释来自这个归一化选择，不是从
P000 邻接推导物理随机性。

设原生端点过程 Z_n 从零 anchor 出发，保留每条原生 word 及其权 `12^-n`。
取同时观察二十个 `can3` 的相对返回时刻

`tau=min{n>=1 : relative_class(Z_n)=0}`。

若 tau 有限，则 `Z_tau=H D`，H∈Z 是真实 common-depth 位移。中间不访问相对
零 fiber，且排除零长 excursion。令

`f_n(h)=P(tau=n,H=h)`，`F(h)=sum_{n>=1} f_n(h)`。

consumer 是“观察上第一次回到起点”事件的**隐藏原生位移分布**，不是把这种
事件当 native return，也不是重做有限长度 histogram。任意固定 n 的原始观察仍是
`a_n(h)[12^-n]`，其中 a_n(h) 是整数 word 数；降到 F(h) 是另行声明的质量投影。

### 已有工具达到哪里，真正剩下什么

已有 `endpoint_multiplicity(n,hD)` 给
`u_n(h)=P(Z_n=hD)` 的精确有限系数。按首次相对返回分解，得到非负有限系数恒等式

`u_n(h)=1_(n=0,h=0)+sum_{t=1}^n sum_k f_t(k) u_(n-t)(h-k)`。

每个固定 n 的内层求和都有限。这是 BRC positive excursion 分解的复用，不是新
串联代数。手算起始检查为 `f_2(0)=1/12`，`f_6(1)=f_6(-1)=6!/12^6=5/20736`。
后者每个正/负轴恰走一次，所有真前缀都未回到相对零。

记访问核 `U(h)=sum_n u_n(h)=G_Z6(hD)`、`S=sum_h U(h)`。
要寻找的是**带常数的逐点**结论

`F(h) ~ [1/(12*pi^3*S²)] |h|^-4`，当 `|h|->infinity`。

**精确未知命题 B** 就是该渐近及其适用合同。只知道访问核的幂律，不等于已知
禁止中间相对返回的首返核有同样幂律；也不能用一张 finite transfer 矩阵宣告无限
相对格的尾已被包围。

### 两篇一手来源及已能导出的较弱结论

1. Lawler–Limic，*Random Walk: A Modern Introduction*，作者公开的
   [原稿](https://www.math.uchicago.edu/~lawler/srwbook.pdf)，Theorem 4.3.1（该
   PDF 第 81–82 页附近）。它给有限范围对称格上 Green 核的远场渐近，包含
   二分周期处理。对这里的六分量简单步律，直接代入得到
   `U(h)=1/(12*pi^3)|h|^-4+O(|h|^-6)`。这个外部概率分析没有改变原生 120°
   正角或把概率协方差当新的空间本体。
2. Asmussen–Foss–Korshunov，*Asymptotics for sums of random variables with
   local subexponential behaviour*，2003，作者
   [arXiv 原文](https://arxiv.org/pdf/1303.4709)，§6 Proposition 12。它对
   **正半线**上的有缺陷更新测度给局部渐近，并要求相应局部长尾/次指数条件。
   本题 H 有正负两向，且已知的是 U 的尾而非先验 F 的局部次指数性质，所以该
   命题不能不加证明地倒用。它提示需要何种精确桥，但不替代这座桥。

作为本轮小规模纯代数检查，以下较弱结论已经可以由第一来源加非负分解推出，
不应该再开任务去“猜它们”：U 可求和，所以 `S<infinity`；对
`p=sum_h F(h)`，非负更新恒等式给 `S=1+pS`，故 `p=1-1/S<1`。
此外 `F(h)<=U(h)`。因此对 `0<a<3`，`sum_h |h|^a F(h)<infinity`。
若某个 a>=3 的 F 绝对矩有限，把 F/p 归一化并用几何次数的独立和展开
`U=sum_{k>=0}F^{*k}`；不等式
`|x_1+...+x_k|^a<=k^(a-1) sum |x_j|^a` 会使 U 的同阶矩也有限，
与 `U(h)~c|h|^-4` 矛盾。故 F 的绝对矩阈值确为 3。

这个矩阈值不是逐点渐近证明：它不能排除局部起伏或确定常数。因此 B 的最小
研究单元应直接检验“双侧有缺陷核的局部反演”，而不是重新计算均值/方差或
拟合一条 log-log 直线。

### 成功、反例与停止条件

成功：给完整双侧卷积反演/傅里叶奇性或 killed Green 证明，所有级数交换与局部
渐近余项可控，最终常数与声明的 1/12 步律一致；有限 BRC 系数只作一致性验证。

反例/证伪输出：证明 F 沿某条无穷整数子列不具有所述比值极限，或发现实际首返
定义/归一化与预期核不一致并给精确 word 证书。单个有限系数、拟合误差或有限
截断未收敛均不能否定渐近命题。

停止条件：若有准确的一手结果直接覆盖该双侧 killed trace 核，改为 typed 引理
复用，不研发新概率工具；若在一个有界证明工作包中不能补上从 U 到 F 的局部
反演，就 park 带常数结论，保留上面已证的返回概率/矩阈值，并明确不由更大
模拟代替证明。任何企图丢掉 H 或只保存 endpoint=relative-zero 的方案都不满足
这个 consumer 的 joint-observer 合同。

替代路线：只做有限 horizon 的 `(length,H)` 正权 histogram 与确切 renewal
恒等式证据，直接复用既有 signed BRC/port 语义；不把该有限结果命名为无限尾
定理，也不扩大现有 14-state path monitor 作为默认后继。

## 3. 下一决策的成本和取舍

A 的第一步应是六个固定和余类的纸上整数构造/阻碍检查。它有立即可判的数学
成功与反例出口，且同现有最短词接口衔接最短。B 的定义更直接暴露 common-depth
被相对返回擦除的长期效果，但分析依赖更重，已有两篇来源没有消除双侧局部
反演缺口，所以列为备选。二者都只是在当前世界观与明确 consumer 下引入经典
数学方法；不把“换了数学分支名称”当作新工具 family。

本轮未执行新枚举/Monte Carlo/新的数值程序；手算两个原生证人和有限系数恒等式
用于约束问题，而不是报告未运行的数值验证。文件、覆盖查询和一手来源阅读均
止于上述范围。

## 4. 当前直接依赖字节

路径相对 `D:/em/owner-20260907`。

| 文件 | SHA256 |
|---|---|
| `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` | `519a16725156be5461c6e28a0dcef664e267cff4e85120cfb257d5d540ec459e` |
| `definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md` | `f5f637a97154c9516053efde1c0222ba444eb68cc5afebc9b347ff9b042e1515` |
| `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json` | `22e17d9bf7f3cb644f5f91785b8c80f82820462d7ddefc72abf2d1acc7da033b` |
| `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py` | `e48b6f2133edc588fde98b1b0f02ce27fecda915b152b7901300898920d52b8e` |
| `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` | `6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4` |
| `src/enterprise_math/brc_weighted_recurrent.py` | `7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26` |
| `src/enterprise_math/brc_recurrent_ports.py` | `7cda953e1f01c537f0747becc666b3c5e2255c20006b9e948c570623250f02b9` |
| `experiments/owner_path_monitor_20260907/path_monitor.py` | `86c7e3e751f1f4817ed836b397b3779dc65bdaf0a10da71c0ee1e434150daccd` |

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
