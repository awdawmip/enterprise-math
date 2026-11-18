# 六字段地址取模与 A₃ 外壳的整数抬升

旧 A₃ 壳层采用 $r(x)=\max_i|x_i|$。对这个特定半径，逐项取模以后，最近的可实现壳层可以把余数排序求出；同一同余类在每层有多少整数点也有闭式。与地址迁移的交集是固定二维面。已登记的两轴地址须先解码再取模；若直接截取地址六栏的余数，同一组数字最多容许三个不同的平面位移余类，下一次原生步即可暴露差别。

## 一、原命题及新映射的类型

冻结原件使用 $\Lambda_{d-1}=\{x\in\mathbb Z^d:\sum_i x_i=0\}$，完整 A₃ 取 $d=4$。其面 $x_4=0$ 去掉最后的零后取 $d=3$。原壳为 $S_R=\{r(x)=R\}$，原点完整球为 $B_R=\{r(x)\le R\}$。旧报告给出 $R\ge1$ 时完整壳 $16R^2+2$ 个点，二维面壳 $6R$ 个点。原源码直接在整数四元组上计算半径和带符号置换。冻结的修订任务另有跨尺度部分作用的回归反例。以下沿用半径、面和指针；旧报告关于所有尺度上部分作用的结论仍受该修订约束。[原返回](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_returns/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_RETURN_20260828.md) · [原检查器](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/scripts/check_a3_recursive_shell_alignment_tomography.py) · [尺度修订](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_tasks/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_REVISION_V2_20260828.md)

冻结的公开 Cell 地址是带 codec、版本和固定帧的六个非负整数字段。只有已登记像集合法。固定两轴切片的完整地址 $a$ 有有符号解码 $D(a)=(u,v)\in\mathbb Z^2$。指定比较基以后，下面两条路线交换：
$$
 a\xrightarrow{D}(u,v)\xrightarrow{J}(u,v,-u-v,0)
       \xrightarrow{\bmod m}\overline{\Lambda_2},
 \qquad
 a\xrightarrow{D}(u,v)\xrightarrow{\bmod m}(\bar u,\bar v)
       \xrightarrow{\bar J}(\bar u,\bar v,-\bar u-\bar v,0).
$$
$J$ 的逆只取前两项，$\bar J$ 同理。图中的 $a$ 表示固定锚点和参照系中的 Cell，$J$ 是在该帧相对坐标上**明确选定的代数比较**。若要比较两个 Cell 的位移，先各自解码再取差。原生整数步分别对应比较面上的 $e_1-e_3,e_2-e_3$ 及反向。切片自身的原生平方距离在源码中是 $(\Delta u)^2+(\Delta v)^2$；本研究的 A₃ 观测半径是 $\max(|u|,|v|,|u+v|)$。前者不会随编码改变，后者属于选定目标域。整个三维 A₃ 格均可独立作下文整数运算，完整三维格的最终 Cell 地址未在此切片合同中登记。[地址合同](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/coordinate_address_contract.json) · [已验证的切片](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md)

## 二、有限环面离最近的壳有多远

取 $m\ge2$，正规余数 $r_i\in\{0,\ldots,m-1\}$，并要求 $\sum r_i=hm$。可把一个坐标减去 $hm$ 得到总和零的整数抬升；两个抬升相差 $m\Lambda_{d-1}$。因此这个余数总体恰为 $\Lambda_{d-1}/m\Lambda_{d-1}$，有 $m^{d-1}$ 元。以下用 $r_{(1)}\le\cdots\le r_{(d)}$ 表示排序，用 $R_m(r)$ 表示所有抬升中最小的无穷范数。

**最近壳定理。** $h=0$ 时余类为零。$h>0$ 时，在最大的 $h$ 个余数上减 $m$，其余保留，得到最优抬升，且
$$
R_m(r)=\max\{r_{(d-h)},\ m-r_{(d-h+1)}\}.
$$
正余数的数目严格大于 $h$，故这一候选落在半径 $m-1$ 内。任何最优抬升因此只可能在每一项选择 $r_i$ 或 $r_i-m$，为使和为零必须选 $h$ 项减 $m$。若已选较小项而遗漏较大项，交换它们会同时压低或保持正、负两侧的最大绝对值。该排序解给出数值最优，原像重数见下一节。

**覆盖阈值及最远类。** 所有余类都有抬升进入 $B_R$ 的最小半径为
$$
D_d(m)=m-\left\lceil\frac m d\right\rceil .
$$
至少 $h+1$ 个余数不小于 $r_{(d-h)}$，故该项至多 $\lfloor hm/(h+1)\rfloor\le D_d(m)$。又有
$$
(d-h+1) r_{(d-h+1)}\ge hm-(h-1)(m-1)\ge m ,
$$
给出另一项的上界。将总和 $m$ 尽量均分于 $d$ 个余数，以 $h=1$ 取得等号。二维面的阈值为 $\lfloor2m/3\rfloor$，完整三维格为 $\lfloor3m/4\rfloor$。

完整 A₃ 中，除 $m=2$ 有七个最远类外，最远类的个数只取决于 $m\bmod4$。余数依次为 $0,1,2,3$ 时，个数依次为 **2、40、20、8**。证明先取 $m\ge10$。$h=2$ 时两项至多 $\lfloor2m/3\rfloor<D_4(m)$。$h=1$ 时正侧项至多 $\lfloor m/2\rfloor$，最远要求最大余数恰为 $t=\lceil m/4\rceil$。令 $r_i=t-b_i$，得 $b_i\ge0,\ \sum b_i=4t-m\le3$。该范围下 $t>4t-m$，故各 $r_i$ 都是正数；又因四个 $b_i$ 之和小于四，至少一个 $r_i=t$。这个分支有 $\binom{4t-m+3}{3}$ 类。余数逐项取负把它与 $h=3$ 的最远类双射。$2\le m\le9$ 从最近壳闭式逐项计得 $7,8,2,40,20,8,2,40$，涵盖边界。

## 三、每一层的原像、首次碰撞与框架稳定子

**每个同余类的完整壳计数。** 给定 $m,R,r$，写
$$
L_i=\left\lceil\frac{-R-r_i}{m}\right\rceil,\quad
U_i=\left\lfloor\frac{R-r_i}{m}\right\rfloor,\quad
b_i=U_i-L_i,\quad k=-h-\sum_i L_i.
$$
若有 $b_i<0$，该类的球原像数 $C_R(r)=0$。其余情况下 $x_i=r_i+mj_i$ 的总和与上下界等价于 $0\le j_i-L_i\le b_i,\ \sum_i(j_i-L_i)=k$。逐坐标有界整分拆给出
$$
 C_R(r)=\sum_{J\subseteq\{1,\ldots,d\}}(-1)^{|J|}
 \binom{k-\sum_{i\in J}(b_i+1)+d-1}{d-1},\qquad
 \#(S_R\text{ 中的抬升})= C_R(r)-C_{R-1}(r).
$$
上指标小于下指标时该项取零，约定 $C_{-1}=0$。对 $0\le R<m$ 还有只用一个二项式的算法。若某余数在开区间 $(R,m-R)$ 内，无抬升；否则令 $f=\#\{r_i>R\}$、$b=\#\{m-R\le r_i\le R\}$，即必减 $m$ 的坐标数和可自由选择的坐标数，则 $C_R(r)=\binom b{h-f}$，越界取零。这些公式也准确计数最优抬升；首个非零的球计数即为其重数。

**恢复阈值。** 对 $d=3,4$，在已知球 $B_R$ 或已知单一壳 $S_R$ 内，全部点都能由余数唯一恢复，当且仅当 $2R<m$。充分性逐坐标即得。若 $m/2\le R\le m$，取 $(R,R-m,m-2R)$ 与交换前两项所得点；二者同余、不同点且半径均为 $R$。若 $R>m$，取 $(R,0,-R)$ 与 $(R,-m,m-R)$。可附零坐标进入四元组。若仅需要球内**每一点的半径**，精确条件放宽为 $R\le\lfloor m/2\rfloor$，此时每项的绝对值都是 $\min(r_i,m-r_i)$，包括偶模数的正负半周同值。令 $u=\lfloor m/2\rfloor$；$(u+1)(e_1-e_2)$ 与 $(u+1-m)(e_1-e_2)$ 在 $B_{u+1}$ 内同余、半径不同，从此不能统一恢复。

**被冻结的指针。** 原作用是 $T_\sigma=\operatorname{sgn}(\sigma)P_\sigma$，指针 $a_R=(R,-R,0,0)$，$R>0$。整数稳定子 $H=\{1,(12)\}$ 的阶为 2。作用与取模交换，但模稳定子的阶依次为
$$
 |\operatorname{Stab}(\bar a_R)|=
 \begin{cases}
 24,&R\equiv0\pmod m,\\
 4,&R\not\equiv0,\quad 2R\equiv0\pmod m,\\
 2,&2R\not\equiv0\pmod m .
 \end{cases}
$$
第二行中两个非零坐标相等且等于自身的负元，所以稳定子为 $S_{\{1,2\}}\times S_{\{3,4\}}$。第三行的 $R,-R,0$ 互异，偶置换只能固定指针的两个标记位置，奇置换必须交换它们，分别仅有恒等与 $(12)$。旧指针轨道有 12 个方向标记。若需从该轨道的模读出恢复原标记，三个分支每个纤维分别须另分 12、2、1 类。这是观测损失，整数框架本身的稳定子没有变化。

## 四、直接对六栏取模会丢什么

只看前三栏，其余三栏始终为零。记 $\tilde a=(a,b,c)$ 为三个**字段余数**，允许活动栏的原正数是 $m$ 的倍数。若原来的不活动栏依次是 A、B、C，对应的有符号点余数为
$$
A:(1-c,b-c),\qquad B:(1+a-c,1-c),\qquad C:(a,b)\pmod m .
$$
每一种等于零的栏都可指定为原不活动栏，另外两栏有正整数抬升，所以每个候选都实际可达。两栏为零时，A/B、A/C、B/C 三类两两差分别为一个坐标单位或两个单位的同步变化；三栏皆零时三个候选是 $(1,0),(1,1),(0,0)$，在 $m\ge2$ 时互异。故读数的确切分布为

| 三栏余数里的零数 | 对应的平面余类数 | 这类读数个数 |
|---:|---:|---:|
| 1 | 1 | $3(m-1)^2$ |
| 2 | 2 | $3(m-1)$ |
| 3 | 3 | $1$ |

单次解码的最坏补充信息是三选一，保存原不活动栏名即达到下界。若还要根据这样的有限记录**继续输出未来的字段余数**，连当前区号也不够。原生点 $(1,1),(m+1,1)$ 起初同为 C 区且三个字段同余，作同名操作 E1_REVERSE 后变成 $(0,1),(m,1)$，其地址第三栏分别为 $1,0$。只走一步即可分离。

事实上，任意有限状态记录都不能对全部有标记原生步持续给出准确的字段余数。若点 $p,q$ 在所有未来端点观察下等价，因为四个具名正反步生成 $\mathbb Z^2$，则 $z=q-p$ 必是函数 $F(p)=E(p)\bmod m$ 的全局平移周期。到足够深的 C 区知 $z=(s,t)\equiv(0,0)\bmod m$。若 $s\ne0$，必要时换用 $-z$ 取 $s>0$，令 $p=(0,M)$ 且 $M$ 充分大；$p$ 的第三栏为 1，而 $p+z$ 落入 C 区，第三栏为零。若 $s=0,t>0$，换 $p=(M,0)$ 同样矛盾。故全局周期只有零；各原生点两两有可分延续。相对地，若未来操作只需读**解码位移的模 $m$ 值**，$\mathbb Z^2/m\mathbb Z^2$ 恰有 $m^2$ 个充分且必要的状态。这两种下游读出具有不同的信息成本。[冻结编码和直接步表](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/src/enterprise_math/_cell_slice_codec.py) · [公开类型与步进 API](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/src/enterprise_math/cell_address.py)

## 五、逐条依赖与历史材料

| 受查陈述 | 输入、算子、处置 |
|---|---|
| X6 旧平面的位移、距离和共同深度 | 旧稿在三个有符号坐标上以 $\Delta=q-p$ 求平方规范、步数和步序重数；保留共同层的 $(z-\min(z)\mathbf1,\min(z))$ 可逆。**KEEP** 于内部位移，**ADAPT** 公开地址入口为已登记解码器，不把三轴完整态塞入两轴编码。原返回 RR-943A793DB1F7B8012A85 的来源保全记录给出 7,632 字节和 SHA-256 4d3a2eb6984318b53bc2506e1f07a0d15b926a7477150c0be2fe3583c562e1cf，原台账为 12 项重定型、16 项仅归档。返回原件可复核，正式终态绑定按任务书留作 **REVIEW_ONLY**。[原件及哈希保全](https://github.com/awdawmip/enterprise-math/blob/6e2c199a005c9d44ac5f6bca2c3b9d4f582103a2/research_artifacts/HISTORICAL_RESULT_CUSTODY/RS-X6-LEGACY-PLANE-RECONCILIATION/a0bfa8eace20b061f5b228c733acdc46221388d7/CUSTODY_MAP_V1.json) |
| FCC 六条载体线、四个切片与 A₃ 壳 | 载体线读出和原生身份分别保留。**KEEP** 既有具名载体；完整三轴公开地址登记仍 **UNKNOWN** 于本切片。A₃ 球的逐点成员与指针稳定子以整数格计算为 **KEEP**，若输入只剩有限余数则 **RECOMPUTE** 为第二、三节公式。旧壳层部分动作的评审沿用既有修订。[FCC 综合任务](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_tasks/P000_FCC_NATIVE_COORDINATE_BRIDGE_ROTATION_ATLAS_SYNTHESIZED_V3_20260829.md) |
| Viète 分支相位、BRC 路径权重 | Viète 的 C6→C12 细化读取选定宏边的中间 Cell。BRC 顺序边、端口、权和叶端接收条件可登记在完整编码的解码轨迹上。**KEEP** 固定切片的轨迹推前；**ADAPT** 只给字段余数的实施，第四节说明下一步已可分离。切片外的 C12 地址另需其合法编码。[选定中点所需数据](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_notes/VIETE_X6_EQUIVARIANT_OUTER_ROOT_LAW_SELECTION_20260906.md) · [有限带权路径的已验证运送](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md) |
| RB/CM24 的六次映射 | 固定代数数嵌入、曲线函数域及 $\delta=t\,d/dR$ 后，$X:C\to\mathbb P^1$ 与伴随曲线态射的次数都是 6。这里的 $X$ 是有理函数。**KEEP** 指定公式和已有证书；这次阅读属于来源明示的审计。[精确映射原返回](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_returns/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_CERTIFICATE_RETURN_20260909.md) |
| Hodge 的块投影、RH 的中心化进位 | 前者读给定代数循环及 $\Pi_W$，例外源循环是否存在仍由原题处理。后者读整数赋值、素数端口和中心化 $J(n)$ 的块能量，估计的常数与均匀性仍需原分析。两者的这些具体命题均 **KEEP**；没有依赖公开 Cell 字段的运算。RH 各路线是否合并仍由原负责人决定。[Hodge 修订](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_tasks/HODGE_H0O_CONTRACT_ALIGNMENT_REVISION_20260908.md) · [RH 任务](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_tasks/RH_BRC_COUNT_CENTERED_CARRY_CLOSURE_20260909.md) |

复算先核对冻结协议、Python 公共编码和壳检查器的 Git blob，并验证已存切片证明文件的 SHA-256。它通过实际 API 做三区编码、解码和一步回归，同时调用原球枚举器及带符号置换。对 $m=2,\ldots,10$、$R=0,\ldots,m+1$，二维面逐类核验 3,792 个球计数，三维格逐类核验 31,380 个，逐项比较精确壳差和唯一性。最远类另遍历至 $m=40$，指针稳定子测至 $m=24$。已存证明作为输入，本文没有另作形式化。[复算脚本](bridge_check.py) · [逐模数整数结果](bridge_checked.json) · [审计任务书](https://github.com/awdawmip/enterprise-math/blob/b4dbf92417211d7286cad72629080bbdf310f1b4/research_tasks/RS-COORD-RESEARCH-BRIDGE-AUDIT-20260916.md)

~~~sh
python bridge_check.py --repo "$ENTERPRISE_MATH_ROOT" --json /tmp/bridge-replay.json
cmp /tmp/bridge-replay.json bridge_checked.json
~~~
