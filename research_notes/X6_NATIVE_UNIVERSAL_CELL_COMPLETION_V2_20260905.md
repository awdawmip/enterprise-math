# X6 原生 Cell 的通用最小完成：四片闭路、返回判据与二阶隐藏伴随

Status: `DERIVED / UNIVERSAL_MINIMAL_NATIVE_COMPLETION_CANDIDATE / EXACT_ALGEBRA / NOT_P000_PROMOTION`
Date: `2026-09-05`
Research lane: `X6 native Cell/path construction`

## 0. 当前基础与类型边界

本结果同时使用以下当前已冻结事实：

1. P000：完整空间有六条原生空间轴；六轴两两 Enterprise-orthogonal，原生正角为 `120 degrees`；这属于定义，不是证明义务。
2. Packet/Path：Cell 是原生对象；路径是邻接 walk；允许 loop、revisit、immediate reversal；路径事件数与 Cell 对象数严格分型。
3. 四个 FCC/K4 三轴 slice 只作为六轴的重叠观察/载体图册，不是完整 native state identity。
4. 每个已建立三轴 slice 内：共享两个分量的 commuting diamond 给出同终点；第三族 reverse shortcut 与 `X_i X_j` 到达同一 terminal Cell；物理正轴跨相邻 chart 按 axis label 去重，而 chart-local path realizations 继续保留。
5. BRC：Path-formal / multiplicity / Boolean endpoint support 是不同观察者，不能因为终点相同就删除路径 witness。

本结果只构造 **Cell endpoint action 的通用最小完成**。它不把路径 quotient 当成路径历史本身，也不从经典载体秩推断空间维数。

## 1. 六轴标签

使用 K4 边标签

`AB, AC, AD, BC, BD, CD`。

四个三轴 slice 是四个 vertex stars：

- `A={AB,AC,AD}`;
- `B={AB,BC,BD}`;
- `C={AC,BC,CD}`;
- `D={AD,BD,CD}`。

共享轴在两个 slice 中是同一个 native axis generator；不同 chart-local realization 不因此被删除。

## 2. 从已冻结三轴事实推出的 Cell-endpoint relations

记六个可逆 adjacency generators 为 `x_e`。逆元表示沿同一 adjacency 立即 reverse，不是新增 native negative axis。

### 2.1 同片交换

在每个 star `S_v` 中，任意两个 incident axis generators 在 Cell endpoint observer 下交换：

`x_e x_f` 与 `x_f x_e` 到达同一 typed terminal Cell。

这来自已冻结 commuting diamond；它不把两个 Path-formal witnesses 识别为同一条路径。

### 2.2 同片三步闭路

三轴 slice 中，`X_i X_j` 与 reverse-third-family `-X_k` 到达同一 terminal Cell。把两边再接同一个正向 `X_k`，并使用 immediate reversal，得到 Cell endpoint relation

`x_{e1} x_{e2} x_{e3} = 1`

对每个 K4 star 成立。

这是一条 **Cell endpoint return relation**，不是 native vector identity `e1+e2+e3=0`，也不是 Path-formal BRC 中把三步 witness 删掉。

因此定义由当前局部事实强制出的 endpoint presentation：

`G6^cell = < x_e | star-local commutations; product_{e incident v} x_e = 1 for v=A,B,C,D >`。

任何满足这些当前局部事实的 pointed homogeneous Cell model，其六轴 endpoint action 都从 `G6^cell` 因子化；若实际模型还有额外 native return relations，则它是 `G6^cell` 的进一步 quotient。

故 `G6^cell` 是当前信息下的 **universal / no-extra-identification completion**。

## 3. 完整化简定理

令

`a=x_AB, b=x_AC, d=x_BC`。

由 A/B/C 三个 star relation：

`x_AD=(ab)^(-1)`;

`x_BD=(ad)^(-1)`;

`x_CD=(bd)^(-1)`。

A、B、C 三片的 commuting diamonds 又分别给出

`[a,b]=[a,d]=[b,d]=1`。

所以全部六轴 endpoint translations 自动交换；不需要把“对边 commute”另列公理。

令

`t = a b d`。

D-star relation 化成

`t^2=1`。

反过来，取交换生成元 `u,v` 与中心二阶元 `t`，令

- `AB = u`;
- `AC = v`;
- `AD = -u-v`;
- `BC = -u-v+t`;
- `BD = v+t`;
- `CD = u+t`;

（这里是 endpoint translation group 的加法记号；不是 native vector equation。）

可直接核验全部 star relations，故得到精确同构

`G6^cell ~= Z^2 x Z/2`。

这一普通阿贝尔群秩绝不能被解释为 Enterprise 空间只有二维；P000 的 native dimension 由六个原生 axis relations 计数，禁止用 classical rank/quotient rank 重写维数。

## 4. 四个局部三轴 Cell 片都忠实嵌入

每个 star subgroup `G_v=<x_e:e incident v>` 精确同构于已知三轴 Cell translation group

`Z^3 / Z(1,1,1) ~= Z^2`。

没有额外 global relation 把一个 slice 内两个不同 Cell 再次压成同一个。

例如 A-slice 就是 `<u,v>`；其第三轴 `AD=-u-v`。B/C/D 由 S4 transport 得到同样结论。

因此 universal completion 保留全部已验证三轴 Cell geometry，而不是为了全局粘合牺牲局部状态。

## 5. 全局二阶伴随 `t`

四个 K4 triangular faces 的三边 endpoint products 全部给出同一个元素 `t`：

`AB+AC+BC = AB+AD+BD = AC+AD+CD = BC+BD+CD = t`。

并且

`t != 0` in the universal completion,

`2t=0`。

所以一次跨 slice face-triangle transport 不返回基 Cell；重复两次才返回。

同样有三组对边关系

`CD = AB + t`;

`BD = AC + t`;

`BC = AD + t`，

从而

`2 AB = 2 CD`, `2 AC = 2 BD`, `2 AD = 2 BC`

在 Cell endpoint observer 下成立。

这不表示不同轴是同一 native line：trace/component labels 与 path provenance 仍然不同；它只说明 endpoint Cell 可以重合。

`t` 暂称 `GLOBAL_CELL_COMPANION_CLASS`。不把它解释为自旋、物理相位、额外空间维或量子自由度。

## 6. 精确返回判据

对任意有向六轴 path 的净 exponent vector

`z=(z_AB,z_AC,z_AD,z_BC,z_BD,z_CD) in Z^6`，

定义三个 perfect-matching sums：

`M1=z_AB+z_CD`;

`M2=z_AC+z_BD`;

`M3=z_AD+z_BC`。

则 path 回到原 Cell 的充要条件为

1. `M1=M2=M3`；
2. 任意一个 K4 face 的三边 exponent sum 为偶数，例如
   `z_AB+z_AC+z_BC == 0 (mod 2)`。

在条件 1 下，四个 face sums 的 parity 相同，所以条件 2 与选哪个 face 无关。

### 证明

若 `z` 是四个 star-return vectors 的整数线性组合，三个 perfect matching 都各取每个 star coefficient 一次，所以三者相等；任一 face sum 每个相关 star coefficient 出现两次，所以为偶数。

反之，写 `a,b,c,d,e,f` 对应六边。若三 matching sums 相等且 `a+b+d` 为偶数，令

`k_A=(a+b-d)/2`;

`k_B=a-k_A`;

`k_C=b-k_A`;

`k_D=c-k_A`。

matching equalities 保证剩余 `BD,CD` 方程也成立，因此

`z = sum_v k_v r_v`

其中 `r_v` 是 v-star return vector。故 endpoint 为原 Cell。证毕。

这给出了纯整数、无浮点、无 carrier coordinate 的 native return certificate。

## 7. Smith 证书与信息类型

四个 star return vectors 组成 K4 无向 incidence matrix。其 determinantal divisors 为

`1,1,1,2`，

所以 Smith invariants 恰为

`(1,1,1,2)`，

再次得到

`Z^6 / <star returns> ~= Z^2 x Z/2`。

这里要纠正旧 BRC 压缩语义中的潜在混淆：

- 在 **path / algebra observer** 中把 star record `Q_v` 设为 1 会丢掉真实 loop provenance，因此是错误压缩；
- 在 **Cell endpoint observer** 中 star word 的 action 本来就返回同一 Cell，所以 endpoint map 对该 loop 取 identity 是正确的 typed quotient。

同一个代数关系在两个 observer 上有不同合法性，不能跨类型复用。

## 8. 每个三轴 slice 都只看见一个 index-2 sheet quotient

对 vertex/slice `v` 定义

`lambda_v(x_e)=0` 若 `e` incident to `v`，否则 `1 mod 2`。

每个 star relation 与该函数相容，所以 `lambda_v:G6^cell -> Z/2` 是良定义同态。

其 kernel 精确等于本地 slice subgroup `G_v`，并且

`lambda_v(t)=1`。

故

`G6^cell = G_v x <t>`

作为集合/阿贝尔群的一个 slice-dependent splitting。

任意 full state `g` 可唯一写成

`g = h_v + lambda_v(g) t`, `h_v in G_v`。

定义 ordinary slice-visible endpoint

`Obs_v(g)=h_v`。

则

`Obs_v(g+t)=Obs_v(g)`。

而四个 ordinary slice observations 的共同 kernel 恰为

`{0,t}`。

因此：

`ALL_FOUR_3AXIS_VISIBLE_CELL_OBSERVATIONS determine a universal full Cell only up to the companion t`。

给任意一个 slice observation 再加该 slice 的 binary sheet bit `lambda_v(g)`，就能恢复 full universal state。

这与 P000 的

`SLICE_OBSERVATION != FULL_CELL_STATE`

形成一个精确的有限代数实现。

## 9. BRC / path provenance 边界

Cell endpoint state 可压成 `G6^cell`，但 Path-formal BRC 不可。

典型例子：

- 空路径与 A-star 三步 path 都终止在同一 Cell，但事件数分别 0 与 3；
- `AB;AC` 与 `AC;AB` 是两个具体 witnesses，虽 endpoint 相同；
- `2*AB` 与 `2*CD` endpoint 相同，但 native axis trace 不同；
- face triangle endpoint 是 `t`，重复 face triangle 才返回。

因此推荐类型链：

`PATH_FORMAL / WEIGHTED_BRC -> NET_AXIS_TRACE + PROVENANCE -> CELL_ENDPOINT G6^cell -> SLICE_VISIBLE SUPPORT`。

任何需要 length、trace、multiplicity、weight、history 或 holonomy observer 的研究，不得提前降到 Cell endpoint quotient。

## 10. 与六轴两两 120° 正交定义的关系

P000 新定义决定的是 native axis relation 与 typed component Pythagorean readout：六轴两两 `PERP_E`，正角为 `120 degrees`。

本结果决定的是 Cell endpoint return algebra。二者不冲突：

- orthogonality 不等于 classical linear independence；
- 一个 nonzero path/trace 可以形成 closed Cell loop；
- same Cell endpoint 不等于 same line/trace/path；
- `G6^cell ~= Z^2 x Z/2` 的 classical group rank 不能重定义 P000 六维空间。

## 11. 当前结论强度

### 已闭合

- 从四个已知三轴 Cell 片构造的 universal endpoint presentation；
- 全部六轴 endpoint translations 自动交换；
- 精确结构 `Z^2 x Z/2`；
- 四个 local slice subgroup 的忠实嵌入；
- canonical order-2 companion class `t`；
- face-triangle / opposite-edge endpoint laws；
- 纯整数 return certificate；
- slice index-2 decomposition 与 `{0,t}` visible ambiguity；
- endpoint quotient 与 BRC/path observer 的严格类型分离。

### 尚未自动晋升

要直接写

`X6_native := torsor(G6^cell)`

还差一个 Foundation 选择：采用 **NO_UNFORCED_CELL_IDENTIFICATION / universal minimal completion**，即除已证明/已定义的 native return relations 外不额外合并 Cell。

如果未来发现独立 native cross-slice return law，则实际 `X6_native` 会是 `G6^cell` 的进一步 quotient；该新 relation 必须显式进入 Foundation，而不能从 FCC carrier 的经典线性关系静默导入。

在当前 BRC / packet-count 信息保持原则下，universal minimal completion 是最保守、最不丢信息的默认候选，但本笔记不越权把这一研究候选直接升级为 P000。
