# 正支点保护的 raw X6 压缩：独立纸面复核

状态：`BOUNDED_PAPER_PROOF_PASS / AUXILIARY_OWNER_REVIEW / NO_FORMAL_ACCEPTANCE`。
日期：2026-09-08（Asia/Shanghai）。这是 owner 父目标下的内部辅助记录；不是正式 V2 task、claim、Result、Driver review、Working Truth 或 Foundation 晋升。

**限定结论：所提压缩引理成立。** 对先按 Cell 聚合并完成 Jordan 分解的有限 signed 空间质量，按其正支点集合构造的逐轴压缩，保持正支点及其质量、正负总质量、全局 L1，以及每一个坐标子集的 raw 边缘 L1。因此全部二十张三轴表的 L1 逐表精确保留。保留的是这些范数，原表的地址及负质量分布可以改变。有限 carrier 的大小不是每个具体压缩结果的实际支撑数。

本次只做证明、来源读取和文件哈希核验；未运行数学 consumer、legacy Fraction 接口、LP、求解器或任何枚举。一般 p=2 或 p<=7 的 sharp 常数没有在这里求出。

## 1. 先查覆盖与精确复用决定

读取的 source HEAD 为 `8c546c2770977ccb26e7ac9ff7d7d70a1d135a99`。先核对当前 owner 候选目录 `research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json` 的全部 **19 项**，再读相关接口及来源。该目录 SHA256 为 `9b9b1851602200bbb207681dbac444a7e745b2915d6f8851bc999fd3a028f115`；其候选状态和未正式接受的边界保持不变。

相关覆盖是 `candidate.x6.raw_joint_observer_recovery`、`candidate.x6.one_positive_raw_stability_certificate`、`result.x6.sparse_marginal_stability` 与 `candidate.x6.nonlinear_channel_gate_quotient`。另核对当前 T0/T6 family、method inventory 及 `operation_descends` 的有限域合同。没有把词面上的 carrier、quotient 或 certificate 当作某个既有定理已经证明本命题。

| 既有接口 | 本次处理及实际依据 |
| --- | --- |
| T0 BRC / `candidate.x6.raw_joint_observer_recovery` | `COMPOSE_APPLIED`：沿用同一外部 anchor、带标签 signed X6 chart、正输入人口与辅助 signed 差的区分，以及完整 raw 边缘的类型。这里只使用空间质量读出；没有执行旧恢复器或恢复已擦除的分支资料。 |
| `candidate.x6.one_positive_raw_stability_certificate` / 既有 raw 稳定性来源 | `COMPOSE_APPLIED`：沿用聚合后正支点、Jordan 质量和全二十表之和 D 的合同。单正证明中的“非正地址只合并同号质量”在第 4 节被独立推广到任意有限正支点集合。没有把单正 sharp 常数推广到多正支点。 |
| T6 `operation_descends` | `REUSE_APPLIED`：采用声明观察与操作后才讨论下降的合同。这里直接证明 `pi_I o phi = phi_I o pi_I`。对非零 f 可取有限闭域 `E=supp(f) union phi(supp(f))`，以 `pi_I` 为分区、`phi` 为自映射，符合其有限判定的输入类型；本次没有执行该判定。下降本身不保证 L1 等号，等号由正地址 singleton fiber 的额外证明给出。 |
| `candidate.x6.nonlinear_channel_gate_quotient` | 其分类定理在本题为 `NOT_APPLICABLE`：原输入是完整有理六通道质量锥、指定平均算子 A_i 及 `q A_i=R_i q` 的单射后继；本题是 signed 空间测度、依赖 S 的坐标压缩及 raw 投影。二者 carrier、算子和保留合同不同。只保留其“商见证不是实际动力过程、质量观察不恢复微观 BRC”边界，不执行其 Fraction consumer，也不借用其总质量分类作为证明。 |

这份新证明的精确增量是：**在既有 raw 边缘分析接口中，为任意有限正支点集合提供同时保持全局及逐表 L1 的有限 carrier 归约。** 建议复用归类为 `EXTEND_EXISTING_TOOL`，具体是现有 raw/X6 分析方法的局部扩展，并组合 T0 的语义与 T6 的下降合同；它不是新 global family，也不是既有 channel quotient 定理的同义别名。本次不修改 catalog、不建立新工具 ID，不声称做过全库或全球数学新颖性证明。

## 2. 合同与映射

固定一套原生六轴标签 `C={0,1,2,3,4,5}`，在同一个外部 anchor 与 signed frame 下用 `Z^6` 记 Cell 的 raw 坐标。设 f 为有限支撑的有理 signed 空间质量，先合并同一 Cell 的分支并删除零项。令

\[
S=\{q:f(q)>0\},\qquad p=|S|,\qquad 1\le p<\infty.
\]

减号仅属于分析账本，不能输入为负 BRC primitive。若输入采用整数分子和共同单位 `DIV(1,s)`，以下等式可先对整数分子证明，并保留同一个未求值单位；不需要约分、求商、求余或求根。

对每轴 i 定义

\[
A_i=\{q_i:q\in S\},\quad c_i=\max A_i+1,\quad
B_i=A_i\cup\{c_i\},\quad \Gamma=\prod_{i\in C}B_i,
\]

\[
\phi_i(t)=
\begin{cases}t,&t\in A_i,\\ c_i,&t\notin A_i,\end{cases}
\qquad
\phi(x)=(\phi_i(x_i))_{i\in C}.
\]

每个 A_i 有限非空，故 c_i 存在且不属于 A_i。对有限测度定义普通有限求和的 pushforward

\[
g=\phi_*f,\qquad g(y)=\sum_{x:\phi(x)=y}f(x).
\]

这里的 pushforward 是分析用地址重编码，不是声明某个物理事件或可执行原生运动。

## 3. 正支点、Jordan 质量与全局 L1

对每个 `a in A_i`，有

\[
\phi_i^{-1}(\{a\})=\{a\}. \tag{1}
\]

因为 A_i 内的输入保持自身，外部输入只去 c_i，而 c_i 不在 A_i。于是 phi 固定 `prod_i A_i`，特别固定 S，且对每个 q in S，**在整个 Z^6 中**仍有

\[
\phi^{-1}(\{q\})=\{q\}. \tag{2}
\]

写 Jordan 分解 `f=f_+-f_-`，两侧非负且支撑不交，令 `P=sum f_+`、`N=sum f_-`。正侧全部固定在 S，负侧没有任何点能压到 S，因此

\[
g_+=\phi_*f_+=f_+,\qquad g_-=\phi_*f_-.
\]

特别地，g 的正支点恰为 S，每个正点的原质量逐点不变；负点之间只会合并同号质量。有限求和给出

\[
P(g)=P(f),\quad N(g)=N(f),\quad
\sum g=\sum f,\quad \|g\|_1=P+N=\|f\|_1. \tag{3}
\]

压缩并不声称保留每一个负支点。

## 4. 每个 raw 坐标边缘的 L1 精确不变

令 `I subseteq C`，`pi_I` 为保留这些实际轴标签的 raw 坐标投影，`M_I=(pi_I)_*`。设 `phi_I=prod_(i in I) phi_i`。由逐轴定义立即有

\[
\pi_I\circ\phi=\phi_I\circ\pi_I,
\qquad M_Ig=(\phi_I)_*(M_If). \tag{4}
\]

第二个等式也可直接交换两个有限求和验证，不涉及无限级数或未声明的观察。

记 `h=M_I f`、`T=pi_I(S)`。不同正 Cell 可以投影到同一地址，正负投影也可以在 T 内原本就相消；以下证明不要求投影在 S 上单射，也不假定 h 在 T 的每一项为正。

任意 `t in T` 的每个坐标均属于对应 A_i，所以由 (1)

\[
\phi_I^{-1}(\{t\})=\{t\},\qquad
((\phi_I)_*h)(t)=h(t). \tag{5}
\]

另一方面，T 外没有任何来自 f_+ 的投影质量，故 `h(a)<=0` 对所有 `a notin T` 成立。(5) 还说明 T 外地址不能压进 T。因而 T 外的重编码只合并非正项，绝对质量相加，不产生额外异号抵消。令 `h'=(phi_I)_*h`，则

\[
\begin{aligned}
\|h'\|_1
&=\sum_{t\in T}|h(t)|+\sum_{b\notin T}(-h'(b))\\
&=\sum_{t\in T}|h(t)|+\sum_{a\notin T}(-h(a))
=\|h\|_1.
\end{aligned} \tag{6}
\]

结合 (4)，得所需的逐表恒等式

\[
\boxed{\|M_I(\phi_*f)\|_1=\|M_If\|_1
\quad\text{对每一个 }I\subseteq C.} \tag{7}
\]

I 为空时只有总质量这一项，等式仍成立；I=C 时就是全局 L1。尤其

\[
D(\phi_*f)=D(f),\qquad
D(f)=\sum_{|I|=3}\|M_If\|_1,
\]

其中是全部二十表之和，没有换成平均值或最大单表值。

## 5. 有限 carrier 与 sharp 问题的准确归约

phi 在 Gamma 上恒等，而且其整个像恰为 Gamma，因此 **可用 carrier** 的大小准确为

\[
|\Gamma|=\prod_{i\in C}(|A_i|+1)\le(p+1)^6. \tag{8}
\]

具体 g 只满足 `supp(g) subseteq Gamma`，不必占满 Gamma。若 p=2，两个不同正 Cell 恰在 r 条轴上不同，则 `1<=r<=6`；这些轴的 A_i 有两个值，其余轴只有一个值。于是

\[
|\Gamma|=3^r2^{6-r}\le3^6=729. \tag{9}
\]

固定 S 后，考虑全部正支点恰为 S 的有限 signed 差。每个这样的 f 都压成支撑在 Gamma、正支点仍恰为 S 的 g，并保留

`(P,N,global L1,(all twenty raw L1 values))`。

反向，Gamma 上的每一个这类差本来就是合法的有限 raw X6 差，并被 phi 固定。因此在这个固定 S 的问题中，上述数值元组的可达集合在压缩前后相同。固定正点质量、总质量相等或其他仅由这些保留量表达的条件，也可同时保留。对 `D>0` 的比值优化，这给出等价的有限 carrier 归约；`D=0` 必须保留为单独情形，不能制造比值。

**有限 carrier 不等于有限多个权重案例。** 有理权重及正负质量分配仍是待处理变量；本证明没有优化这些变量，没有给出 p=2 的常数，也没有解决 p<=7 的统一 sharp 常数。即使 p 更大并存在非零零边缘差，(7) 也只是把这种差保留到有限 carrier，绝不据此声称一般可恢复性。

p=1 时每轴两类，共 64 个 carrier 地址。对唯一正点 q，任意负点 z 的不同轴集合 `{i:z_i!=q_i}` 被逐项保持；因此既有单正证明的 `a_I`、各不同轴集合的聚合负质量，以及单轴负点条件均保留。多处轴线位置可合并，但是否单轴以及六轴聚合权重不改变，所以既有 `3/20` 与等质量 `1/10` 的不同取等条件不会被混同。这是对已证明单正接口的兼容性检查，未重新授予或扩大其数学状态。

## 6. p=0 与不可越过的边界

若 p=0，则 f 整体非正；原定义中的 `max A_i` 不可使用。另取任意常值映射，例如将所有点送到原点。全局 L1 保持为 N，每张 raw 边缘也都是非正并具有相同总绝对质量 N。f=0 时仍为零，不报告 0/0。这个独立平凡边界不需要空集合的最大值。

本引理有以下明确限制。

1. **S 是映射的输入。** 它不是对所有 signed 差统一有效的固定 L1 isometry。例如按 `S={0}` 构造 phi 后，`delta_(2e_0)-delta_(3e_0)` 的两点都压到 e_0，L1 从 2 变为 0；这个新差的正支点已不属于原合同。不能在换了 S 后继续复用旧 phi 的保范数声明。
2. **只保证声明的 raw 坐标投影。** 取 `f=delta_0-delta_z`、`z=(1,2,3,0,0,0)`。此时 S={0}，压缩后 `phi(z)=(1,1,1,0,0,0)`。对 `I={0,1,2}`，原 can3 地址分别是 `(0,0,0)` 和 `(0,1,2)`，单独 can3 读出的 L1 为 2；压缩后两者 can3 都是 `(0,0,0)`，该 L1 变为 0。raw 地址仍是两点，raw L1 均为 2。这是 can3-alone 不自动继承的纸面反例。
3. **任意线性观察也不自动继承。** 同一反例中，`ell(x)=x_0-x_1` 原来区分 0 和 z，观察差的 L1 为 2；压缩后两者 ell 都为 0，L1 为 0。
4. **没有物理或微观等价。** phi 非线性且一般不可逆，不是原生 isometry、合法事件 word 或 channel 平均动力。比如上例 signed 位移从 `(1,2,3,0,0,0)` 变为 `(1,1,1,0,0,0)`；实际坐标跨度已改变。路径数、事件长度、common-depth、分支历史与微观直方图都不在保留合同中。不能从未保存的资料恢复这些对象。
5. **联合编码不是数据不变。** raw 三元组与其联合 `(can3, common offset)` 编码之间的双射，允许用联合编码表达同一 raw 质量范数；它不表示压缩前后的地址或 offset 相同。丢掉 offset、分别保留两种边缘直方图，或换成其他观察，均需另证。
6. **这是分析层的归约。** 原生维数仍为六；没有增加轴、修改 signed 步集、改变外部 anchor，或把辅助 signed 账本当成负 BRC primitive。也没有证明从任意完整 BRC 对象先擦除到空间质量是无损的。

## 7. 来源与冻结记录

以下文件均按本次读取的实际字节绑定；文中的引用只使用其声明的合同和相应证明，不把旧状态改写为新正式接受。

| 来源 | SHA256 |
| --- | --- |
| `research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json`（19 项） | `9b9b1851602200bbb207681dbac444a7e745b2915d6f8851bc999fd3a028f115` |
| `research_notes/OWNER_ONE_POSITIVE_STABILITY_20260907.md`，第 1、2、3、4 节 | `b49eac9291c7b6a6ec458a133700ee17a4573972e58787a976871512746dd4e7` |
| `research_notes/OWNER_X6_STABILITY_20260907.md` | `2915e70210dce5bc136c915e45e96a7c8a1f6dd414fae1590a4687f41bff3127` |
| `research_notes/OWNER_NONLINEAR_CHANNEL_QUOTIENT_20260907.md`，第 1、2、4、5 节 | `edcc5694bd2a85cebc0836110d03142ad3637cd953e96b2c98c08fbbe8e77ffc` |
| `experiments/owner_nonlinear_channel_20260907/channel_quotient.py`（仅阅读） | `c90d67e9d56bc14e2d2adea36b8f69ba2e1afc21c794c22aee73e69de34bd844` |
| `src/enterprise_math/operation_quotient.py`，`operation_descends` | `39e62738077eaddb2a3b19a679d0e6a2e7a3415cee7cffa894fe810bb034927e` |
| `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py`，`hidden_slice_coordinates` | `e48b6f2133edc588fde98b1b0f02ce27fecda915b152b7901300898920d52b8e` |
| `enterprise_toolbox_registry.json` | `f2281d98a05aa23feaa4b163e7ab37a41f30ecbb84f499b0b820443bcfa97170` |
| `research_method_inventory.json` | `f6b221bcd7050ddea5965bcb80d6cf64c98e99d23f9ae6cbadb8e23a390f7402` |
| `tool_invocation_policy.json` | `57e6c427699d4a6f877757efeb8f0a1b77482874af3bfac672f5351db4e712dd` |

唯一新增文件是本辅助记录；没有修改源实现、已有研究、19 项目录、任何 registry 或状态。没有 commit/push。后续是否采用此归约、实现符合当前算术运行时的 consumer 或进入正式研究流程，由 owner 在各自权限边界内处理。

Global-Knowledge-Sync: main@990d7c1 / GLOBAL_KNOWLEDGE_V1
