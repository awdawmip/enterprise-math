# 双正支点 raw X6 稳定性：9/20 审查及 sharp 1/4 纸面增量

日期：2026-09-08（Asia/Shanghai）。作者：owner 内部辅助代理 `/root/control_fixture_recovery`。
状态：`ROOT_BOUND_PAPER_REVIEW_PASS / NEW_SHARP_DERIVATION_PENDING_SEPARATE_REVIEW`。

**限定结论。** Root 提出的有限质量推导 `9D >= 20M` 和矩形下界见证全部成立。进一步保留两个正点的轴相等结构，可证明更强的全输入不等式

\[
\boxed{p(f)\le2\quad\Longrightarrow\quad \|f\|_1\le\frac14D(f).}
\]

二维坐标矩形的等幅对角差取等，所以这里的 **1/4 是任意总质量、以及等总质量两个类共同的最优常数**。这是下文完整有限证明的结论，不来自数值求解、有限样本外推或只考察等总质量。一般 `p(f)<=7` 的 `[1,111/20]` 问题保持原状。

本记录是 owner 父目标下的纸面辅助；不是正式 task、claim、Result、Driver review、Working Truth 或 Foundation 接受。对 root 原推导作独立检查；本助手新增的 sharp 证明仍交另一位审查者复核。没有运行数学程序、LP、枚举、consumer 或 CI，没有远端写入。

## 1. 精确合同

固定同一个外部 Cell anchor 与同一套带标签 signed 六轴 frame，用现有原生 X6 torsor 的 `Z^6` chart 表示空间 Cell。轴集为 `C={1,...,6}`。先按同一 Cell 聚合空间质量并相减，删除零项，再定义

\[
S=\{x:f(x)>0\},\quad p(f)=|S|,\quad
f=f_+-f_-,\quad P=\sum_x f_+(x),\quad N=\sum_x f_-(x),\quad M=P+N=\|f\|_1.
\]

f 是有限支撑的有理 signed 空间质量，Jordan 两侧支撑不交。负侧支点数和坐标跨度不受限制。本文 M 只是全局 L1，不能与 BRC 的 CWM 中 dominant mass 分量混同。

对每个三轴集合 I，保留完整 raw 地址表（缺失地址按零）：

\[
(M_If)(t)=\sum_{x:x_I=t}f(x),\qquad
D(f)=\sum_{I\in\binom C3}\|M_If\|_1.
\]

D 是全部二十表的 L1 **之和**，不是平均值或最大单表误差。raw 三元组可由联合保留的 `(can3, per-slice common offset)` 等价编码；单独 can3、两个分离直方图或未配对的全局 depth 不满足本合同。

若原输入是两个有限非负总体 μ、ν，且 μ 至多两空间支点，则 `p(μ−ν)<=2`；必须先消去重合质量。正 BRC 输入保持严格正分支类型，减号仅是两个正总体空间 W 读出的分析差。没有宣告物理负分支、改变原生六维，或恢复已经擦除的路径身份。

## 2. 19 项覆盖与实际复用

源 HEAD 为 `8c546c2770977ccb26e7ac9ff7d7d70a1d135a99`。静态核对当前 owner 目录全部 19 项的 `input_contract/output_contract/core_law/hard_boundary`，并读取下表相关纸面来源。目录仍为候选路由，不把目录命中当作数学执行或正式接受。本次未运行 coverage CLI；实际处置如下。

| 目录条目 | 本次复用处置与精确边界 |
| --- | --- |
| `candidate.x6.raw_joint_observer_recovery` | `REUSE_APPLIED`：共同 chart、先聚合空间质量、完整 all20 raw 表及正 BRC/辅助 signed 差类型；不执行恢复器。 |
| `candidate.certificate.rational_nonnegative_phase1` | `NOT_APPLICABLE`：本证明没有求解有限方程组；不把 LP 的可用性当作 sharp 证明。 |
| `candidate.x6.budgeted_noisy_recovery` | `NOT_APPLICABLE` 于本次证明；它是声明 carrier/预算下的拟合接口，不提供本双正 sharp 常数。 |
| `candidate.x6.integer_histogram_realization` | `NOT_APPLICABLE`：整数逐权重直方图实现，不是空间 signed 质量比值。 |
| `candidate.x6.finite_reverse_step_port_monitor` | `NOT_APPLICABLE`：有限词和逆步观察，不是静态 raw 边缘。 |
| `candidate.x6.shortest_path_valuation_spectrum` | `NOT_APPLICABLE`：固定最短词长与赋值谱，不提供当前范数界。 |
| `candidate.x6.minimum_raw_query_plan` | `COMPOSE_APPLIED`：复用其轴对 parity 的纤维翻转见证；缺轴对时不辨识的证明可用于第 4 节。原接口给唯一性/最少表数，不给本 sharp 常数。 |
| `candidate.certificate.rational_interval_inertia` | `NOT_APPLICABLE`：区间矩阵负指数合同。 |
| `result.rh.n8_reference_eta09_inertia` | `NOT_APPLICABLE`：特定有限 RH reference。 |
| `candidate.brc.finite_exchangeable_factorial_observer` | `NOT_APPLICABLE`：有限 exchangeable/factorial 观察。 |
| `result.pp.finite_power_moment_lift_obstruction` | `NOT_APPLICABLE`：特定 ordinary-power-moment 障碍。 |
| `candidate.x6.nonlinear_channel_gate_quotient` | `NOT_APPLICABLE`：指定通道平均算子的质量锥分类，不能代替依正空间支点构造的 raw 压缩或稳定性证明。 |
| `result.x6.sparse_marginal_stability` | `EXTEND_EXISTING_TOOL`：沿用同一 p(f)、all20 stacked L1 与有限质量合同；111/20 可覆盖 p<=2 的粗界，但没有当前 1/4 强度。 |
| `result.x6.weighted_minimum_trade` | `NOT_APPLICABLE` 于本上界：恰八正点且零边缘的分类不证明双正非零残差的最佳常数。 |
| `candidate.x6.quadratic_shell_max_shortest_length` | `NOT_APPLICABLE`：固定平方壳的最短长度极值。 |
| `result.x6.common_depth_first_return_tail` | `NOT_APPLICABLE`：无条件首返尾律。 |
| `result.analysis.two_sided_reciprocal_cusp_tail` | `NOT_APPLICABLE`：Fourier reciprocal 尾部分析。 |
| `result.rh.energy_domain_correction` | `NOT_APPLICABLE`：历史能量定义域纠正。 |
| `candidate.x6.one_positive_raw_stability_certificate` | `REUSE_APPLIED`：采用其已证明的 p<=1 常数 3/20、等质量 1/10 以及 Jordan/零边界；不改消费者的 p<=1 前提。 |

另外，对已读 `OWNER_POSITIVE_SUPPORT_RAW_COMPRESSION_REVIEW_20260908.md` 作 `COMPOSE_APPLIED`：固定正支点 S，令 `A_i={q_i:q in S}`，逐轴固定 A_i、把其余值压到一个新值 `c_i`。其 singleton 正地址纤维证明保证压缩保持 P、N、M 和每一张 raw 边缘 L1。

因此本题可先转到 `Gamma=prod_i(A_i union {c_i})`。若两正点不同轴数为 d，carrier 大小是 `3^d 2^(6-d)`；这是可用地址数，不是实际支撑数或有限多个质量案例。正点固定，任一点是否与各正点在某轴相等也保持。下文的证明可在 Gamma 上进行并以保范数恒等式拉回；为清晰起见直接沿用原坐标记号。没有枚举 Gamma，也没有把保范数引理误读成已经求出了 sharp 常数。

在上述精确目录与已读来源内，没有已给出的双正 9/20 或 1/4 最优界。轴对 parity 见证本身已被 query-plan 来源覆盖，不能申报为新发现；新增量是对任意有限负侧和任意两正权的统一 1/4 上界。有限 L1 对偶与组合计数是普通证明方法，本记录不申报新 global 工具 family 或全球新颖性。

## 3. Root 的 9/20 上界：完整有限质量检查

先设 `p(f)=2`，写

\[
f=p_u\delta_u+p_v\delta_v-\nu,\quad
u\ne v,\quad p_u,p_v>0,\quad \nu\ge0,\quad \nu(u)=\nu(v)=0,
\quad P=p_u+p_v,\quad N=\sum_z\nu(z).
\]

对每张表置 `T_I={u_I,v_I}`；若两个投影相等，T_I 只有一个地址。定义避开全部正投影的负质量

\[
a_I=\sum_{z:z_I\notin T_I}\nu(z),\qquad A=\sum_I a_I.
\]

T_I 外全是非正投影，负点碰撞只合并同号质量，其范数合计为 a_I。T_I 内的有符号质量总和为 `P−N+a_I`，不需要每个地址都为正。因此

\[
\|M_If\|_1\ge a_I+|P-N+a_I|\ge P-N+2a_I. \tag{1}
\]

任一有负质量的 z 不等于 u、v。令

\[
Q(z)=\{i:z_i=u_i\},\qquad R(z)=\{i:z_i=v_i\}.
\]

两集合大小各至多 5。该点的投影落在 T_I 内，当且仅当 `I subseteq Q` 或 `I subseteq R`。分别把 Q、R 扩到两个 5 元子集；扩集只会增加这种表数。两个 5 集若相同，含有 10 个三元子集；若不同，其交集恰为 4 元，三元子集并有

\[
\binom53+\binom53-\binom43=10+10-4=16
\]

个。因此每个负点至少在 4 张表中避开 T_I。交换有限求和：

\[
A=\sum_z\nu(z)\#\{I:z_I\notin T_I\}\ge4N. \tag{2}
\]

由 (1)、(2)，以及每张边缘保存有符号总质量，分别得到

\[
D\ge20(P-N)+2A\ge20P-12N,\qquad
D\ge20|P-N|\ge20(N-P). \tag{3}
\]

即使 (3) 某个右端为负，其下界仍成立；不需要除以 P−N 或 N。取非负权重 5/9、4/9：

\[
D\ge\frac59(20P-12N)+\frac49\,20(N-P)
=\frac{20}{9}(P+N).
\]

故 root 的 `9D>=20M` 正确。p=1 使用既有 `M<=(3/20)D`，p=0 为非正差，所以也得到整个 p<=2 类的粗上界 9/20。

若 P=N，(3) 已直接给出 `D>=8N=4M`。这一步比 9/20 更强，且只使用已经证明的有限质量式；结合下一节见证，**等总质量的 1/4 已在这里取到 sharp**。

## 4. 矩形见证：下界 1/4 已取到

取任意合法 Cell q 和两个不同实际轴 a、b。考虑

\[
f=\delta_q+\delta_{q+e_a+e_b}-\delta_{q+e_a}-\delta_{q+e_b}.
\]

四点是同一 X6 chart 的合法不同 Cell；其余四轴坐标相同。正侧、负侧分别是两个单位正 BRC 空间质量分支，P=N=2，M=4。

恰有 `C(4,1)=4` 张三轴表同时含 a、b；其投影在四点上单射，每张范数为 4。任何其他表都遗漏 a 或 b，沿所漏轴翻转矩形顶点可在每个纤维内把正负单位质量配对，故整张表为零。

\[
D=4\cdot4=16,\qquad M/D=1/4. \tag{4}
\]

这给任意质量类和等总质量子类相同的下界。共同正有理缩放不改变比值；两侧各归一化为概率时同样达到它。没有把两个活动轴解释为原生空间只有二维。

## 5. 按两正点的不同轴数加强上界

令 `J={i:u_i!=v_i}`，`d=|J|`，则 `1<=d<=6`。保留第 3 节 Q、R、a_I 的含义。

### 5.1 d=1：至少十张避正表

除唯一不同轴外，u、v 在所有轴相等。Q、R 在这些共同轴的部分完全相同；在不同轴上，z 至多等于 u、v 之一。因此 Q、R 必嵌套，较大者大小仍至多 5。

被正投影覆盖的三轴集合最多 `C(5,3)=10` 个，所以 `A>=10N`。由 (1)、(3) 得

\[
D\ge20P,\qquad D\ge20(N-P),\qquad
3D\ge20(P+N)
\]

（前两式权重分别为 2/3、1/3）。因此 d=1 的充分常数 3/20 已严格小于 1/4；不主张本分层常数本身最优。

### 5.2 d>=3：至少七张避正表

`Q intersect R` 只能含 u、v 相同的轴，因此其大小 c 至多 `6−d<=3`。

若 Q、R 都至多 4 元，则所含三元子集的并最多 `4+4=8` 个。若其中一个是 5 元，不妨为 Q，由 `|Q union R|<=6` 得 `|R|<=c+1`。故覆盖数至多

\[
\binom53+\binom{c+1}3-\binom c3
=10+\binom c2\le13. \tag{5}
\]

上标小于下标的二项系数按零；c=0,1,2,3 全部被 (5) 包含。因此每个负点至少在 7 张表中避正，`A>=7N`。由 (1)、(3)：

\[
D\ge20P-6N,\qquad D\ge20(N-P).
\]

取权重 20/33、13/33 得

\[
33D\ge140(P+N),\qquad M\le\frac{33}{140}D<\frac14D. \tag{6}
\]

最后一个严格系数比较是 `4*33=132<140`；没有数值近似。这里也只给足够强的上界，不主张各 d 的最优值。

### 5.3 d=2：四张主表加十六张惩罚表的对偶证书

此时 `J={a,b}`，其他四轴 u、v 完全相同。令

\[
\mathcal H=\{I\in\tbinom C3:J\subseteq I\},\qquad |\mathcal H|=4.
\]

对每张表的**所有 raw 地址** t 定义有界系数

\[
b_I(t)=
\begin{cases}
 1,& I\in\mathcal H,\ t\in T_I,\\
-1,& I\in\mathcal H,\ t\notin T_I,\\
 0,& I\notin\mathcal H,\ t\in T_I,\\
-1,& I\notin\mathcal H,\ t\notin T_I.
\end{cases}
\qquad G(x)=\sum_{I\in\binom C3}b_I(x_I).
\]

每个系数属于 `{−1,0,1}`。u、v 在四张主表的系数为 +1，其余为 0，所以

\[
G(u)=G(v)=4. \tag{7}
\]

对任意 `z notin {u,v}`，分两种完整情形：

1. **两差轴地址不等于任一正对角。** 若 `(z_a,z_b)` 不属于 `{(u_a,u_b),(v_a,v_b)}`，则四张主表全部不在正地址，合计 −4；其他表系数均至多 0。因此 `G(z)<=−4`。
2. **两差轴地址等于一个正对角。** 因 z 不是该正点，至少有一个共同轴 c 满足 `z_c!=u_c=v_c`。主表 `{a,b,c}` 的系数为 −1，其他三张主表至多 +1，主表合计至多 2。包含 c 的三轴表有 `C(5,2)=10` 张，其中恰一张是 `{a,b,c}`；余下 **9 张非主表** 因 c 值不同而不等于任一正投影，系数都是 −1。其余非主表系数至多 0，故 `G(z)<=2−9=−7<−4`。

这一分类允许 z 在任何轴上取任意整数值；未把负点限制为二值矩形，也未假定它们只有两个。于是所有负支点都满足 `G(z)<=−4`。由有限求和交换和 `|b_I(t)|<=1`：

\[
\begin{aligned}
D(f)
&=\sum_{I,t}|(M_If)(t)|\\
&\ge\sum_{I,t}b_I(t)(M_If)(t)
=\sum_xG(x)f(x)\\
&=4p_u+4p_v-\sum_zG(z)\nu(z)
\ge4(P+N)=4M.
\end{aligned} \tag{8}
\]

这就是任意两正权、任意有限负侧、**无 P=N 前提**的 d=2 上界。使用的是显式逐表 L1 对偶系数；没有调用线性规划对偶求解器，也未假设所有投影的正地址互不碰撞。

### 5.4 合并及强化原因

d=1、d>=3 已由 (6) 及前式给出严格小于 1/4 的充分系数；d=2 由 (8) 给出 1/4。p=1 用既有 3/20，p=0 时 f 非正，每张边缘范数都等于 M，因此 `D=20M`。f=0 时 `M=D=0`，不构造 0/0；N=0 也直接有 `D=20M`，证明中没有除以 N。

所有 p<=2 的有限差遂满足 `D>=4M`。非零差自动有 D>0，再结合 (4)：

\[
\boxed{
\sup_{f\ne0,\ p(f)\le2}\frac{\|f\|_1}{D(f)}
=\sup_{f\ne0,\ p(f)\le2,\ \sum f=0}\frac{\|f\|_1}{D(f)}
=\frac14.}
\]

Root 的 9/20 只是把每个负点一律计为至少四张避正表，随后用有符号总质量下界加权；它丢掉了两个正点的不同轴结构。真正的强化来自：d≠2 时更强的覆盖计数，以及 d=2 时另外十六张表提供的非正惩罚。不是宣称仅把原来两个标量下界重新配权就能得到 1/4。

## 6. 范围与交接

- 这是聚合后正支点至多两点的结果。没有把单正 consumer 放宽为两正，也不改变 p<=7 的一般常数或八正点零边缘障碍。
- 正负质量、任意碰撞和不等总质量均已被证明覆盖；最优值由合法等总质量矩形取到。没有在这里分类所有取等输入。
- 必须保留 all20 raw 表或等价的联合 can3/局部 offset。单独 can3 下原点与全对角平移的单支点仍可完全不可见；当前证明不适用。
- 六轴与共同 anchor 是现有原生合同。压缩只是依 S 的分析重编码；双对偶也只是质量观察证书，不是新的物理事件、通道动力、旋转或未知 frame 的恢复。
- 不从空间 W 读出推回分支标签、历史、精确权重直方图、branch count 或原微观 dominant mass。BRC 类型边界保留。
- 本次没有数学执行证据；纸面证明承担全体有限质量的量词。程序消费者、独立新证明审查、source publication 和后续工具归类由 owner 分别处理。原单正纸面、压缩复核、19 项目录及数学 L4 包均未改。

## 7. 实际来源字节

下表绑定本次读取的实际 UTF-8 文件字节。HEAD 如第 2 节；其中压缩复核当时是工作树已有的未跟踪辅助文件，**不是**声称已包含于该 HEAD。这里只引用其精确 SHA。其他材料的历史状态保留，不把旧程序 PASS 或旧正式状态当作本次重新执行/接受。

| 来源 | SHA256 |
| --- | --- |
| `research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json`（19 项） | `9b9b1851602200bbb207681dbac444a7e745b2915d6f8851bc999fd3a028f115` |
| `research_notes/OWNER_X6_STABILITY_20260907.md` | `2915e70210dce5bc136c915e45e96a7c8a1f6dd414fae1590a4687f41bff3127` |
| `research_notes/OWNER_STABILITY_CONSTANT_FRONTIER_20260907.md` | `e81c20d9b9c44dc6af00beb500552d4245f3ed5c207c3e210707b3f572697134` |
| `research_notes/OWNER_ONE_POSITIVE_STABILITY_20260907.md` | `b49eac9291c7b6a6ec458a133700ee17a4573972e58787a976871512746dd4e7` |
| `research_notes/OWNER_ONE_POSITIVE_STABILITY_INDEPENDENT_AUDIT_20260908.md` | `f6fe6713fb46bc0fd9c6626333cb44afd14c88b13b7f7d99fe8f928859434038` |
| `research_notes/OWNER_POSITIVE_SUPPORT_RAW_COMPRESSION_REVIEW_20260908.md` | `2cb061262e713859fd419871d0be9e4d5041698a01a46a55bd5ef5fc3f7e38b4` |
| `research_notes/OWNER_OBSERVATION_QUERY_DESIGN_20260907.md`，第 1、4、6 节 | `16df4e2f39f0caaa7f58e62cdbc34839afe8e52348eb14079f6d9894c75a9aa7` |
| `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` | `519a16725156be5461c6e28a0dcef664e267cff4e85120cfb257d5d540ec459e` |
| `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`，正分支/质量/signed 边界 | `58b33c9ebd89aafb21cff5c7f20b01099ac5c71b6e809a91966f23911496d3f6` |
| `enterprise_toolbox_registry.json` | `f2281d98a05aa23feaa4b163e7ab37a41f30ecbb84f499b0b820443bcfa97170` |
| `research_method_inventory.json` | `f6b221bcd7050ddea5965bcb80d6cf64c98e99d23f9ae6cbadb8e23a390f7402` |
| `tool_invocation_policy.json` | `57e6c427699d4a6f877757efeb8f0a1b77482874af3bfac672f5351db4e712dd` |

唯一新增文件为本记录。未 commit/push，未运行数学程序或改变任何正式权限。

Global-Knowledge-Sync: main@eb09a0a / GLOBAL_KNOWLEDGE_V1
