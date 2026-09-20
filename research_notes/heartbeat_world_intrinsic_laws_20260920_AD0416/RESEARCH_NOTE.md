# 心跳世界自有规律：周期单值化、余数扩张与进位 holonomy

Status: RESEARCH_CONSTRUCTION / SCOPED_PROOFS / EXECUTABLE_CHECKS / NOT_FOUNDATION
Date: 2026-09-20
World: HEARTBEAT_WORLD
Researcher: EM-DIRECT-AD0416

## 0. 研究边界

“心跳世界”只固定原生 X6 六维离散 Cell 空间 + 单独类型的一维时间；没有固定倍率、固定六拍周期或固定缩放程序。因此具体数值律不能直接升级成世界公理。

本轮研究的通用子类是

z_(t+1)=A_t z_t+a_t,  A_t in M_6(Z), det(A_t)!=0.

当程序 p 拍周期时 A_(t+p)=A_t, a_(t+p)=a_t。以下主定理先研究线性部分；仿射平移影响周期漂移但不改变有限子格指数。Smith 正规形、有限阿贝尔群扩张和周期 monodromy 都是经典代数工具；本轮研究的是它们在心跳世界六轴、时间和 BRC 语义下形成的结构。

## 1. 相位互绕律

从相位 t 开始的一周期线性 monodromy 为

M_t=A_(t+p-1)...A_(t+1)A_t.

周期性给出整数恒等式

M_(t+1) A_t = A_t M_t.

若 det(A_t)!=0，则在 Q^6 上

M_(t+1)=A_t M_t A_t^(-1).

所以不同周期切相位具有相同的行列式、特征多项式和有理谱。相位不会改变周期的有理线性谱，但可改变离散 Cell 的余数群结构。

## 2. 余数扩张律

对单射整数映射 A，定义有限余数群

Gamma_A = Z^6 / A Z^6,

其大小为 |det A|。

若两拍依次为 A 再 B，则有短正合列

0 -> Gamma_A -> Gamma_(BA) -> Gamma_B -> 0,

其中左箭头由 [x] -> [Bx] 给出。证明来自子格链

BA Z^6 subset B Z^6 subset Z^6.

因此

|Gamma_(BA)|=|Gamma_A| |Gamma_B|.

但 Gamma_(BA) 不必是 Gamma_A x Gamma_B 的直积。若扩张不分裂，总余数数量不变，但原来独立的 digits 会耦合成进位结构。

对固定起点的多拍 M_k=A_(k-1)...A_0，每一拍都把已有余数群再扩张一次。因此非幺模心跳会沿时间建立一个有限余数信息滤链。这里的信息计数是精确 Cell 表示的离散计数，不是热力学熵。

## 3. 相位进位 holonomy

由相位互绕律，不同相位的 M_t 行列式相同，所以 |Gamma_(M_t)| 相位不变。但是若相位变换 A_t 非幺模，Gamma_(M_t) 的有限阿贝尔群类型不必相同。

六轴反例只在前两轴作用、后四轴恒等：

A_0 = [[1,0],[0,-2]] direct-sum I_4,
A_1 = [[-2,1],[2,-2]] direct-sum I_4.

每一拍自身的 Smith 因子都是

(1,1,1,1,1,2),

即每拍只增加一个二元余数。

但

M_0=A_1 A_0,
M_1=A_0 A_1

分别具有

SNF(M_0)=(1,1,1,1,2,2),
SNF(M_1)=(1,1,1,1,1,4).

所以

Gamma_(M_0) ~= Z/2 x Z/2,
Gamma_(M_1) ~= Z/4.

两者都有 4 个余数态且周期有理谱相同，但一个相位保留两枚独立二进制余数，另一个相位把它们耦合成一个四进制进位。本文把这种“总余数体积不变、余数扩张类型随相位改变”的现象称为相位进位 holonomy。这个名称是项目术语，不主张为新的经典群论概念。

若 A_t 幺模，则相位 monodromy 在 GL_6(Z) 中共轭，余数群必同构；所以非幺模缩放是这种相位 carry holonomy 的必要入口，但不是充分条件。

BRC 观察反例：若只记“4 个分支”会把两个相位视为相同；但观察“余数乘 2 后是否为零”，在 (Z/2)^2 中 4/4 个余数被消去，在 Z/4 中只有 2/4。未来若访问余数加法或进位，总分支数并不是安全的完整状态。

## 4. 六轴循环 radix 阶梯律

定义任意整数基数 b>=2 的六轴循环心跳

A_b(z_1,...,z_6)=(b z_6,z_1,z_2,z_3,z_4,z_5).

有

A_b^6=b I.

若

k=6q+r, 0<=r<6,

则 Smith 因子精确为

(b^q repeated 6-r times, b^(q+1) repeated r times).

所以

Gamma_(A_b^k) ~= (Z/b^q)^(6-r) direct-sum (Z/b^(q+1))^r,

其中 Z/1 为平凡因子。

这表示：
1. 每拍只把一个轴的 radix 深度增加一层；
2. 任意时刻六轴 digit-depth 最大差不超过 1；
3. 每六拍重新齐平；
4. 第 6q 拍时为 (Z/b^q)^6。

对 b=2，第一轮六拍依次产生 1 到 6 个独立二元余数；第 7 拍不会创造“第七空间轴”，而是把某个 Z/2 延长成 Z/4。时间深度表现为已有轴的进位深度，不是新增空间维数。

## 5. 余数—分支对偶律

对任意 det(M)!=0，固定 Gamma_M 的余数代表集合 R。每个 z in Z^6 唯一写成

z=Mq+r,  r in R.

保留 r 时粗化可精确逆转；丢掉 r 后，同一粗状态 q 反向展开时有

|R|=|det M|

个合法细状态分支。

所以

被删除的有限余数 <=> 未来必须重新面对的多分支.

对循环 radix 心跳的 k 拍，branch count=b^k。这里是 support/branch 数，不自动赋予均匀权重。

而第3节又说明，只保留 branch count 仍可能不够：未来若访问进位结构，必须保留 Smith/torsion profile 或经证明足够的修复坐标。

## 6. 心跳对主动位移的着色律

设一周期仿射作用

F_t(z)=M_t z+c_t

和主动原生平移

T_u(z)=z+u.

则

F_t o T_u = T_(M_t u) o F_t.

所以“先走 u 再经历一周期”在周期末变成 M_t u；“先周期再走同样 u”仍为 u。时间排序缺陷为

(M_t-I)u.

满足 M_t u=u 的位移构成周期透明子格。这里静态空间加法没有失去交换律；非交换来自跨时间仿射作用与主动位移的半直积。

## 7. 自有规律的层级

世界定义级（已有约束，不是本轮新定理）：
- 六空间轴 + 一时间轴；
- 空间返回不等于事件返回；
- 余数/相位/BRC 状态不是额外空间维数；
- 无固定六拍或固定倍率。

周期整数心跳族的派生规律：
- 相位互绕律；
- 余数扩张律；
- 相位进位 holonomy；
- 余数—分支对偶；
- 主动位移着色律。

典型六轴循环 radix 家族：
- A_b^6=bI；
- radix 阶梯律；
- 六轴 digit-depth 始终相差至多一层。

这三层不得混写成一个世界公理。

## 8. 工具复用与能力缺口

已检查：
- T5 Precision/Refinement：复用 carry/repair-coordinate 语义；无整数 monodromy cokernel/Smith 谱执行器。
- T9 Holonomy/Cocycle：复用周期路径与 holonomy 语义；无非幺模整数余数谱执行器。
- T0 BRC：复用 support/provenance 安全边界与“忘余数 => 多分支”解释。

当前仓库搜索未发现 Smith normal form / integer cokernel / heartbeat monodromy 现成执行器。因此 heartbeat_residual_holonomy.py 作为 DOMAIN_OPERATOR，属于 COMPOSE(T5,T9,T0) 后的明确能力缺口补充，不新建顶层工具族。

## 9. 精确验证

纯标准库检查通过：
- 60 组三拍随机六轴 monomial 心跳，共 180 个相位，验证 M_(t+1)A_t=A_tM_t 与周期行列式一致；
- 六轴相位 carry 反例：两相位余数群分别 (Z/2)^2 与 Z/4；
- b=2,3,5,7，k=1..24：96 个 radix 阶梯 Smith 公式全部一致，branch count=b^k；
- 200 组随机两拍有限指数映射验证余数数量乘法；
- 二维有限调查：元素取 [-2,2]、|det|=2 的 184 个矩阵产生 33,856 个有序两拍组合，其中 15,488 个满足 SNF(AB)!=SNF(BA)。

最后一项只是有限盒统计，不是频率定理或自然分布结论。

## 10. 非均匀六轴加权循环：素数估值平衡律

令正整数因子为 b=(b_1,...,b_6)，定义
A_b(z_1,...,z_6)=(b_6 z_6,b_1 z_1,b_2 z_2,b_3 z_3,b_4 z_4,b_5 z_5).
则 A_b^6=B I，其中 B=product_i b_i。因此局部倍率不均匀仍可在完整六拍精确齐平。

对任意素数 p，记 v_i=v_p(b_i)，V=sum_i v_i。若 k=6q+r，则 A_b^k 的六个 Smith 因子的 p-adic 深度，是六个循环 r-窗口和
qV + sum_(j=0..r-1) v_(i+j mod6)
的排序。

所以完整六拍统一给六轴增加 V 层 p-adic 深度；轮内各轴深浅差只依赖 r 和固定 v_i，与完成轮数 q 无关。p-adic 各向不均匀只周期振荡，不逐轮累积。

当所有 b_i=b 时退化为原 radix staircase。80 组随机因子、18 拍、p=2,3,5 共 4,320 个精确 Smith-valuation 比较全部通过。该规律要求固定倍率跟随轴循环；任意周期整数矩阵程序不保证成立。

## 11. 周期单项心跳的 p-adic 漂移充要条件

把范围再扩大：假设每拍都是原生轴的“置换 + 非零整数倍率”，即整数 monomial 矩阵。取一个周期的 monodromy M；它仍然是 monomial 矩阵。设其底层置换分解成循环 C。对素数 p，令

V_C = sum_(j in C) v_p(w_j),  l_C=|C|,

其中 w_j 是该循环各源轴携带的整数倍率。定义循环平均增长率

mu_C = V_C/l_C.

则：

**M^n 的六个 p-adic Smith 深度差在 n->infinity 时有界，当且仅当所有置换循环的 mu_C 完全相同。**

证明：若 j 属于循环 C，写 n=q l_C+r，则该轴累计深度为

q V_C + 一个长度 r 的循环窗口和
= n mu_C + 有界周期余项。

若所有 mu_C 相等，每条轴都等于共同线性增长 n mu 加一个有界周期项，因此全局深度差有界。反之若两个循环均值不同，取 n 为两循环长度的公倍数，周期余项同时消失，深度差正好按 n|mu_C-mu_D| 线性增长。

因此对周期 monomial 心跳：
- 多个循环平均 p-growth 一致 => p-adic anisotropy 只振荡、不累积；
- 存在两个循环平均 p-growth 不同 => p-adic anisotropy 线性发散。

这个判据对心跳起始相位不变，因为换相位只把同一周期序列平移有限拍；有限前后缀不可能把线性发散变成有界，也不能把有界变成发散。执行器也逐相位复核这一事实。

单一 6-cycle 只有一个循环，所以第10节的非均匀轴倍率模型自动满足所有素数 p 的有界条件。这解释了为什么“每轴倍率不同但跟着同一个六循环走”仍会整轮自平衡。

反例：若 monodromy 为 diag(2,1,1,1,1,1)，对 p=2 有六个长度1循环，其中一个平均增长1，其余为0；第 n 周期的深度 profile 为 (0,0,0,0,0,n)，差值线性增大。

本轮随机验证：
- 40 个六轴 monomial 矩阵，p=2,3,5，k=1..12，共 1,440 个 Smith-depth 精确比较；
- 120 个循环均值分类检查；
- 40 组三拍周期 monomial 程序 × p=2,3,5，共 120 个相位不变性检查；
- 单 6-cycle 正例和多循环不平衡反例均通过。

## 12. 一般轴混合：Newton carry-slope 定理

monomial 情形的循环均值判据可以推广到任意非奇异整数 monodromy，而不需要每列只有一个非零项。

令 M in M_6(Z), det(M)!=0。记 M^n 的 Smith 因子为

d_1(n) | ... | d_6(n),

并定义 p-primary 深度

s_i(n)=v_p(d_i(n)).

另一方面，把 M 的六个特征值放到 Q_p 的代数闭包中，按 p-adic valuation 排序：

lambda_1 <= ... <= lambda_6.

则存在最终周期的有界修正 epsilon_i(n)，使得对充分大的 n：

s_i(n)=n lambda_i + epsilon_i(n).

证明并非新的 Smith 定理：对第 k 个 determinantal divisor gamma_k(M^n)，其 p-adic valuation就是第 k 个 compound/exterior-power matrix (wedge^k M)^n 的 entrywise minimum valuation。Noferini 对整数矩阵幂证明
v_p(gcd(A^n))=a n+h(n)，h 最终周期；应用到 wedge^k M，线性项 a 是其最小特征值 valuation，也就是 lambda_1+...+lambda_k。再用
v_p(gamma_k)=s_1+...+s_k
逐项相减，就得到上式。

因此有精确的长期判据：

lim_(n->infinity) [max_i s_i(n)-min_i s_i(n)]/n
= lambda_6-lambda_1.

所以

**p-adic carry-depth 不均匀长期有界 iff 六个 p-adic eigenvalue valuations 全相同。**

若相同，深度差最终只剩周期摆动；若不同，深度差按 lambda_6-lambda_1 线性增长。

lambda_i 不需要显式求 p-adic 根。它们就是特征多项式 p-adic Newton polygon 的负斜率，按水平长度计重数。新增执行接口用精确 Faddeev-LeVerrier 计算整数特征多项式，再用 Fraction 构造 Newton 下凸包。

本结论以 Vanni Noferini, "Eventual periodicity of the Smith forms of integer matrix powers", arXiv:2511.22814 / Linear Algebra and Its Applications 748 (2026), DOI 10.1016/j.laa.2026.06.014 的 Smith-power eventual-periodicity 结果为经典底座；Newton polygon 读出根的 p-adic valuations 也是经典局部域结论。这里的项目贡献是把这些结果与心跳世界的 phase/carry/BRC 类型接口对齐，而不是主张经典定理的新颖性。

## 13. 有限相位 holonomy 与长期 slope 可以同时存在

由 HBW-INTR-001，不同心跳相位的一周期 monodromy 在 Q^6 中共轭，因此具有同一个特征多项式，也就具有完全相同的 Newton carry-slope spectrum。

于是出现两层同时成立的结构：

- 当前有限余数群 coker(M_t) 可以随相位从 (Z/2)^2 变成 Z/4；
- 长期每个 p-primary Smith depth 的线性增长斜率却对相位不变。

所以相位进位 holonomy 描述的是**有限阶段的 carry 组织方式**，而 Newton carry spectrum 描述的是**长期 carry 增长率**。二者不能互相替代。

本轮另外对 60 组三拍稠密 2x2 轴混合块嵌入 X6 的程序检查全部三个 phase cut，共 180 个相位，Newton carry spectrum 完全一致。

## 14. “每拍平衡”不推出“周期平衡”

取二维块

A=[[0,2],[1,0]],
B=[[1,1],[1,-1]].

两者都满足

A^2=B^2=2I,

所以对 p=2，单独重复 A 或 B 时两个 carry slope 都是 1/2。把该块复制三份得到六轴 A_6,B_6，则每一拍单独都是六轴 carry-balanced。

但是两拍周期的 monodromy

P=B A=[[1,2],[-1,2]]

具有特征多项式

x^2-3x+4.

其 2-adic Newton slopes给出 root valuations 0 和 2。六轴周期因此具有

(0,0,0,2,2,2)

的 carry-slope spectrum。实际 Smith 深度对周期幂 n=1..8 精确为

(0,0,0,2n,2n,2n).

所以：

**beatwise carry balance 不是可组合性质；必须检查完整时间周期的 monodromy。**

这是真正的时间顺序效应：两个各自自平衡的心跳操作，交替后可以产生持久线性 carry 漂移。

## 15. 几何伸缩谱与整数 carry 谱是独立观察

同一个 P=[[1,2],[-1,2]] 的复特征值为

3/2 +/- i sqrt(7)/2,

两者普通绝对值都等于 2；从 Archimedean eigenvalue magnitude 看它是平衡的，但 p=2 carry slopes 是 0 和 2，极不平衡。

反向例子取

C=[[0,-2],[1,6]],

特征多项式 x^2-6x+2，实特征值 3+sqrt(7) 与 3-sqrt(7) 的普通绝对值明显不同；但其 2-adic Newton polygon 只有一个 slope，因此两个 carry slope 都是 1/2。

所以：

**real/metric scale balance != p-primary carry balance.**

心跳世界里“空间伸缩看起来均匀”不能代替整数 Cell 的进位平衡检查；反过来也一样。这进一步说明 BRC 若未来会访问 carry，不能只保留普通几何尺度谱。

## 16. 最终仿射周期 carry 控制器

对固定整数 monodromy M，Noferini 的 Smith-power 定理还给出比“只有斜率”更强的结论：存在 n0、正整数 T 和固定对角整数矩阵 D，使得

SF(M^(n+T)) = D * SF(M^n)

对所有 n>=n0 成立。

因此，充分长时间以后，完整 residual-group isomorphism type 并不是每拍产生一种不可压缩的新结构。它由：

- 一个有限 transient；
- n mod T 的有限相位；
- 每跨 T 个周期乘一次的固定对角增长 D；

精确生成。

换言之，长期 carry 可以表示成“有限控制器 + 整数增长计数器”。对每个素数 p，D 的对角 p-valuations 除以 T 正是上一节的 carry slope spectrum。

这个结果非常适合 BRC，但必须保留边界：

1. 它压缩的是 Smith/isomorphism-type 级的余数结构，不自动恢复具体 residual 元素、空间代表或路径 provenance；
2. 一般 n0 和 T 可能很大，文献中两者都可以任意大，不能把“最终有限控制器”误说成“小常数状态”；
3. 有限窗口里看到重复增长比，只是诊断，不构成一般 eventual-periodicity 证明。

新增执行器 `smith_factor_ratio` / `smith_increment_trace` 只做有限窗口检查。统一 radix 2 模型从开始就显示 6 周期增长比；上一节的失衡 P 模型则从开始就是固定增长比 (1,1,1,4,4,4)。

## 17. BRC 的两层 carry 表示

至此，对固定线性周期心跳，可以把 carry 信息至少分成两个观察层：

- **有限结构层**：当前相位的 Smith invariant factors / residual group type，决定当前的元素阶、进位与 torsion 观察；
- **长期增长层**：Newton carry-slope spectrum，决定各 p-primary 深度的长期线性增长率。

只问长期漂移时，slope spectrum 比完整 residual group 更小；若未来允许精确余数加法、zero-test 或选代表，则还需要有限结构层甚至具体元素坐标。

因此

branch count < carry-slope spectrum < current Smith group type < labeled residual/path state

不是全局等价链，而是按观察能力逐层增强的 BRC carrier 层级。

## 18. 有限状态依赖心跳：最终周期 carry 律

把固定周期程序再放宽一层。设有限控制状态集 S，每个状态 s 有：
- 一个确定的下一控制状态 f(s)；
- 一个非奇异整数 X6 线性作用 A_s。

从任意初态出发，有限确定系统必经过有限 transient 后进入唯一循环

C=(c_0,...,c_(L-1)).

定义该循环的一圈 monodromy

M_C=A_(c_(L-1))...A_(c_0).

那么该轨迹的长期 p-primary Smith-depth 斜率（按每一拍归一）就是

(1/L) * carry_slope_spectrum(M_C,p).

理由：在足够晚的时刻，总作用可写成固定前缀/后缀乘以 M_C^q。对任意 exterior power，左右乘固定非奇异矩阵只会把 p-adic entrywise minimum / determinantal-divisor valuation 改变一个与 q 无关的常数，因此线性斜率不变。

所以**长期 carry 记忆不依赖完整历史，只依赖最终进入哪个控制周期以及该周期的 monodromy。**

这给 BRC 一个新的安全压缩层：
- 若只观察长期 carry 斜率，可以把所有进入同一 carry-spectrum 周期的 transient 状态合并；
- 若两个可达周期 carry spectrum 不同，则即使当前空间位置、总 determinant growth 或当前观察相同，也不能在该观察下合并；
- 若要保留有限时刻 carry holonomy，仍需比最终 slope 更丰富的相位/Smith 状态。

六轴精确例子：控制图有两个 2-cycle，外加一个 transient。
第一周期使用 A,A，其中 A^2=2I，长期每拍 slopes 为 (1/2,...,1/2)；
第二周期使用 A,B，其中 B^2=2I，但 BA 的 2-adic slopes 为 (0,0,0,2,2,2)，所以每拍归一后为 (0,0,0,1,1,1)。
两个周期每拍的总 determinant valuation 相同，但 carry 分配完全不同。transient 状态只继承最终进入周期的 slope。

新增接口 `eventual_control_cycle`、`control_cycle_monodromy`、`control_carry_spectrum`、`control_carry_spectra` 复用已有 T6 finite-control 语义；不是新的顶层工具族。

## 19. 对分支控制的直接推论

若控制不是确定的，而是 BRC 真分支，则一个起点可能到达多个 recurrent cycle。此时长期 carry 观察天然是一个**关系值/分支值的 slope spectrum family**，不能先平均后再决定是否平衡。

因此状态依赖心跳形成一个清楚的层级：

deterministic eventual cycle
-> one carry-slope vector

branching reachable cycles
-> provenance-aware family of carry-slope vectors.

把后者压成平均 slope 会丢失“部分分支稳定、部分分支漂移”的区别；是否允许这种压缩必须重新声明观察目标和未来操作。

## 20. 下一前沿

1. 当余数群发生 (Z/2)^2 <-> Z/4 型变化时，哪些 BRC 权重只依赖总 branch count，哪些必须依赖元素阶/进位层级？
2. 能否以 p-primary Smith/valuation 数据替代完整余数枚举，并对声明的未来余数运算闭合？
3. 有限确定控制已经闭合到 eventual-cycle carry spectrum；下一步研究真正分支/随机 cocycle 的 slope family、极值增长率与 BRC 权重如何共同传播。
