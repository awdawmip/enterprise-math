# Owner X6 raw 三轴边缘：未知支撑的统一质量稳定性

辅助工作包：`/root/stability_research`；owner 委派的本地数学辅助，非正式 task/claim，无身份注册声明。

状态：`PROVED_DERIVATION / LOCAL_OWNER_RESEARCH / NOT_FOUNDATION_PROMOTION`。
源：`enterprise-math@ef1893382`；续用本地 `b9adbb13` 中
`OWNER_FREE_CANDIDATE_20260907.md` 的七/八支点结果。
KB：owner 已验证并续用 `main@ccd838a220b00ad44a7f5375fffeee8aa6afaaa0` 六小时租约。
本文不是 FREE 盲发现、不是正式 Driver review，也不增加公理。

**实质推进。** 七支点原定理可以升级为不依赖候选载体大小、坐标间距和最小正质量的统一定量估计：

\[
\|\mu-\nu\|_1\leq \frac{111}{20}
\sum_{|I|=3}\|M_I\mu-M_I\nu\|_1.
\tag{1}
\]

这里只要求非负真分布 \(\mu\) 至多有七个空间支点；非负竞争分布 \(\nu\)
可以有任意有限多个支点，其支撑不必预先已知。\(111/20\) 是已证明的充分常数，**没有最优性声明**。
这一估计来自完整切片归纳，不来自固定支撑矩阵满秩、数值拟合或有限枚举。

## 1. 原生对象、噪声和信息保留契约

- 对象是 current X6 native spatial Cell torsor 中的空间 Cell 中心。
  固定一个共同 anchor 与同一套有标签 signed 六轴 chart；所有输入沿用这个 chart。
  原生六维和 120° 正角由 P000 固定，不由本文的线性代数或一般归纳参数重新定义。
- 质量是有限非负有理数组。空间支点指不同 Cell 中心；多条路径到达同一中心时若先合并，
  路径身份、精确路径权重直方图与内部状态已经不属于待恢复对象。
- 为实际求解声明任意有限候选集合 \(D\subset X6\)，并要求真分布支持包含在 \(D\) 中。
  \(D\) 是合法 Cell 的完整声明候选总体，不能为迎合恢复结果删掉竞争点。
  定理本身对任意两有限支持分布适用：取两者支持的并作为 \(D\) 即可，因此常数不依赖 \(|D|\)。
- 对每个 \(|I|=3\)，\(M_I\) 保留完整 **raw** 三坐标标签及对应质量表，包含隐含零项。
  共二十张表的标签不能混合。当前 `can3` 必须另留共同深度 `min`，
  使 `(can3, min)` 能恢复 raw；`can3` 单独不满足前提。
- 输出误差是同一 Cell 标签集上的 \(\ell^1\) 质量距离。
  数据范数固定为
  \(\|z\|_{\mathrm{stack},1}=\sum_{|I|=3}\sum_a|z_{I,a}|\)。
  这不是“每表最大误差”，不是每个表项的 \(\ell^\infty\)，也不是 Wasserstein 距离。
- 噪声向量 \(y\) 可以不具有一致的总质量，甚至含负项；不要求任意噪声恰好来自合法分布。
  恢复结论的条件是确有指定稀疏 \(\mu\)，以及所检查候选 \(\nu\) 非负，且它们各自对 \(y\)
  的残差满足声明的界。
- future-operation lease 仅含空间质量及明确的有界空间观察；路径延拓、force scatter、
  未知 frame 变化、相位和时间历史不自动受此恢复保证覆盖。

**BRC 实际输入/输出。** 依据
`ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`，在每个空间读出纤维中将非零 Cell
质量作为已声明的正分支，实际复用 `cwm_from_positive_weights` 的
\((C,W,M)\) 及替代合并律 \((+,+,\max)\)。本文的边缘表取其 \(W\) 分量。
两分布之差 \(f=\mu-\nu\) 是证明用的 signed 误差数组，**不是**正权 BRC 里的物理负质量。
没有将 \(CWM\) 宣告为完整分支状态，也没有从可重建性推断联合方向可默认删除。

## 2. 工具覆盖、实际复用与方法来源

问题先固定为“原七/八 raw 质量观察能否统一抗噪”，然后运行现有 toolbox coverage，结果保存为
`owner_stability_20260907_coverage.json` 和 `owner_stability_20260907_coverage_marginal.json`。
覆盖命中及处置如下。

| 候选 | 处置及理由 |
|---|---|
| 现有七/八支点切片证明 | `EXTEND_EXISTING_TOOL`：扩展同一有限切片归纳，加入范数账本；不创设新顶层工具家族。 |
| `t0.weighted_brc_cwm`（由已读基底和前轮覆盖精确定位） | `REUSE_APPLIED + REUSE_EXECUTED`：正质量纤维求和及后文 C/W/M 边界见证直接运行既有实现。 |
| `t0.weighted_brc_histogram` | `REUSE_APPLIED`：沿用其精确权重形状与 CWM 不等价的 carrier 边界；本文未调用直方图恢复算法。 |
| signed completion / BRC multipath | `REUSE_APPLIED` 于正输入与代数差的类型区分；没有引入物理 signed 分支语义。 |
| Newton fiber / observer lattice | `NOT_APPLICABLE`：没有 Newton jet、冻结代换 schedule 或 root selector；其秩接口不能代替本题非负全局估计。 |
| finite recurrent / critical / moment-transfer | `NOT_APPLICABLE`：静态三轴质量边缘不具所需 transition recurrence。 |
| multiplier basin / Pell / path-root / native-line / Bellman 等词法命中 | `NOT_APPLICABLE`：不是整数开方扫描、路径闭包或原生直线追踪问题。 |
| min-zero normalization | `REUSE_APPLIED` 于 raw/common-depth 防护；单独商掉共同深度会违反此题 observer lease。 |

使用的方法是有限切片、三角不等式和归纳，均是既有数学方法；本文不申报这些方法的外部新颖性。
七/八 trade 极值的外部先例及链接沿用前轮笔记 §7；这里的定量不等式由下文直接证明承担。
未作全库或全体外部文献无重复声明。

## 3. 一般定量切片引理及完整证明

令 \(f\) 是 \(A_1\times\cdots\times A_n\) 上有限支持有理数组，\(0\leq k\leq n\)。
令 \(p(f)=|\{x:f(x)>0\}|\)，并定义

\[
D_{n,k}(f)=\sum_{|I|=k}\|M_I f\|_1,
\qquad M_\varnothing f=\sum_x f(x).
\]

所有 \(A_i\) 可以无限；运算和证明中出现的支持始终有限。
只把不在合法坐标集上的位置零延拓为计算数组，不将其宣告为额外合法 Cell。

定义有理常数

\[
C(n,0)=C(n,n)=1,
\quad
C(n,k)=\frac{(n-k)C(n-1,k)+2kC(n-1,k-1)}{n}
\quad(0<k<n).
\tag{2}
\]

**引理。** 若 \(p(f)<2^k\)，则
\[
\|f\|_1\leq C(n,k)D_{n,k}(f).
\tag{3}
\]

**证明。** 对 \(n\) 归纳。

1. \(k=0\) 时 \(p(f)<1\)，即 \(f\leq0\)，故 \(\|f\|_1=|\sum f|\)。
   \(k=n\) 时唯一一张边缘就是 \(f\) 本身。两端的常数均为 1。
2. 取 \(0<k<n\)，固定任一轴 \(j\)，按其值 \(b\) 切片得 \(f_b\)，每片在剩余 \(n-1\) 轴上。
   因不同片的正支点不交且 \(p(f)<2^k\)，至多有一个片具有至少 \(2^{k-1}\) 个正支点。
   称其为重片 \(g\)（若存在）；其余全是轻片。
3. 对轻片逐一使用 \((n-1,k-1)\) 归纳。记
   \(B=\sum_{b\text{ light}}\|f_b\|_1\)，则
   \[
   B\leq C(n-1,k-1)D_j(f),
   \qquad
   D_j(f)=\sum_{|I|=k,\,j\in I}\|M_I f\|_1.
   \tag{4}
   \]
   此处关键的无抵消等式是：对不含 \(j\) 的 \(|J|=k-1\)，
   \(\sum_b\|M_J f_b\|_1=\|M_{J\cup\{j\}}f\|_1\)。
   原边缘保留了 \(b\) 标签，所以把不同 \(b\) 的范数加起来没有先混片后抵消。
4. 令 \(F=\sum_b f_b\) 为删除轴 \(j\) 的聚合数组。
   每个 \(F(x)>0\) 都需要其纤维中至少一个原正支点；这些纤维不交，故
   \(p(F)\leq p(f)<2^k\)。
   对 \(F\) 使用 \((n-1,k)\) 归纳，得到
   \[
   \|F\|_1\leq C(n-1,k)D_{\bar j}(f),
   \quad D_{\bar j}(f)=\sum_{|I|=k,\,j\notin I}\|M_I f\|_1.
   \tag{5}
   \]
   等式 \(D_{n-1,k}(F)=D_{\bar j}(f)\) 源自有限求和交换。
   **没有**对重片错误使用 \((n-1,k-1)\) 稀疏界。
5. 若存在重片，则 \(g=F-\sum_{b\text{ light}}f_b\)，从而
   \[
   \|f\|_1=\|g\|_1+B\leq\|F\|_1+2B
   \leq C(n-1,k)D_{\bar j}(f)+2C(n-1,k-1)D_j(f).
   \tag{6}
   \]
   若没有重片，\(\|f\|_1=B\)，由 (4) 也得到同一个较松的 (6)。
6. (6) 对每个轴 \(j\) 都成立。对 \(n\) 个轴平均：每张 k 轴表在 \(D_j\) 中出现 k 次，
   在 \(D_{\bar j}\) 中出现 \(n-k\) 次，恰得到 (2)–(3)。证毕。

也可不用平均而逐次取较松常数，得到 \(C(n,k)\leq2^k\)。
平均递推在本题给出更好的常数。设 \(c(n,k)=\binom nk C(n,k)\)，则内部递推为
\(c(n,k)=c(n-1,k)+2c(n-1,k-1)\)，边界 \(c(n,0)=c(n,n)=1\)。

| n | c(n,0), …, c(n,n) |
|---|---|
| 1 | 1, 1 |
| 2 | 1, 3, 1 |
| 3 | 1, 5, 7, 1 |
| 4 | 1, 7, 17, 15, 1 |
| 5 | 1, 9, 31, 49, 31, 1 |
| 6 | 1, 11, 49, 111, 129, 63, 1 |

因此 \(C(6,3)=111/20\)。一般归纳中的 n 是数组参数；其余值只用于证明切片，
不把 native X6 的维数改写成这些参数。

## 4. 从引理到真正的有噪恢复

对非负 \(\mu,\nu\)，令 \(f=\mu-\nu\)。
\(f(x)>0\Rightarrow\mu(x)>0\)，故 \(|\operatorname{supp}\mu|\leq7\) 即保证 \(p(f)<8\)。
将 \(n=6,k=3\) 代入 (3)，得到 (1)。竞争分布无需稀疏。

若 \(y\) 是二十张有标签噪声表，且
\[
\|M\mu-y\|_{\mathrm{stack},1}\leq\varepsilon,
\qquad
\|M\nu-y\|_{\mathrm{stack},1}\leq\eta,
\]
则
\[
\boxed{\|\mu-\nu\|_1\leq\tfrac{111}{20}(\varepsilon+\eta).}
\tag{7}
\]
两者残差均不超过 \(\varepsilon\) 时，右端是 \(111\varepsilon/10\)。
若分别声明的是**每张表的** \(\ell^1\) 残差均不超过 \(\varepsilon\)，
则先转成 stacked 残差 \(20\varepsilon\)，结论相应变为 \(222\varepsilon\)，不能混用两个噪声口径。

**有限候选集的求解承诺。** 在 \(D\) 上任意非负残差最小化器
\(\widehat\mu\in\arg\min_{v\geq0}\|Mv-y\|_{\mathrm{stack},1}\)
满足 \(\eta\leq\varepsilon\)，因真分布 \(\mu\) 是可行竞争者。
这一有限维目标有最小值：\(v\geq0\) 时
\(\|Mv-y\|_{\mathrm{stack},1}\geq20\|v\|_1-\|y\|_{\mathrm{stack},1}\)，
故非空有限次水平集有界且闭。
有理数据下这是有理线性规划，存在有理最优解。
此数学可实现性不宣称当前求解器一定已实现或已有多项式性能证书；本笔记不修改恢复模块。

**与固定支撑的区别。** 固定一个至多十五点的集合 \(S\)，任何支持于 \(S\) 的 signed 数组
非零时总有一种符号的支点数至多七；必要时将 \(f\) 换成 \(-f\)，同一个稳定性界仍成立。
故已知至多十五个候选支点时所有权重也有此统一估计。
这与“未知支撑、一方至多七、另一方任意非负”的定理是不同输入承诺。
固定矩阵满秩本身不提供后者。

**近似稀疏。** 对任意有限非负 \(\mu\)，保留质量最大的至多七个 Cell 得 \(\mu_7\)，
尾质量 \(\tau=\|\mu-\mu_7\|_1\)。由正尾在每张表中保质量，
\(D_{6,3}(\mu-\mu_7)=20\tau\)。对 \(\mu_7-\nu\) 应用 (1) 并用三角不等式得
\[
\|\mu-\nu\|_1\leq\tfrac{111}{20}D_{6,3}(\mu-\nu)+112\tau.
\tag{8}
\]
这是有显式稀疏尾项的充分估计，不承诺其常数最优。

## 5. 精确下界与必要边界

### 5.1 已知下界：常数仍可优化

在前轮合法四轴二值矩形中，\(\mu\) 取八个 even Cell 中去掉原点后的七点单位质量，
\(\nu\) 取八个 odd Cell 的单位质量。前轮整套 even/odd 三轴边缘相同，所以此处
每张边缘差恰为所删点投影处的 \(-1\)：

\[
\|\mu-\nu\|_1=15,
\quad \|M_I\mu-M_I\nu\|_1=1\ (20\text{ 张}),
\quad D_{6,3}=20.
\]

任何对本题所有 raw 质量分布有效的最优 stacked 常数 \(C_*\) 因而满足
\[
\frac34\leq C_*\leq\frac{111}{20}.
\]
这个差距是具体后续信息缺口；不能将当前充分常数包装为最佳条件数。
该见证总质量分别为 7 与 8。若预先额外限制双方都是概率分布，最优常数是另一个问题。

### 5.2 八支点、can3、anchor 与非负性

- 八对八 even/odd 原见证仍使 \(D_{6,3}=0\) 而 \(\ell^1\) 差为16，故不能统一把七扩成八。
- `can3`-only 下原点与 \((1,1,1,1,1,1)\) 的单位单支分布所有表相同，\(\ell^1\) 差为2；
  即使零噪声也无稳定性。
- 未知 anchor 若允许双方各用自己的原点，任意平移后的单支都可能读作零；需要共同 chart 或精确已知 transport。
- 非负竞争是实质前提。令 \(h\) 是四轴 parity 零边缘 signed 数组，\(\mu=\delta_0\)，
  \(\nu=\mu+t h\)（\(t>0\) 有理），则边缘完全相同而 \(\nu\) 通常带负项。
  此时 \(\mu-\nu\) 的正支点不再必然包含于 \(\operatorname{supp}\mu\)。

### 5.3 质量稳定不等于分支计数与几何矩稳定

1. \(\mu=\delta_0\)，\(\nu=\delta_0+t\delta_{e_1}\)。
   \(\ell^1\) 差为 \(t\)，stacked 边缘差为 \(20t\)，但非零 Cell 计数由1变2。
   正权 BRC 实际得到 \((C,W,M)=(1,1,1)\) 与 \((2,1+t,1)\)（\(0<t\leq1\)）。
   因此支撑计数 C 不连续；没有最小质量条件时不能承诺精确支撑或计数恢复。
2. 对**已按 Cell 聚合的质量分支**，\(W\) 与 \(M\) 各自对 \(\ell^1\) 是 1-Lipschitz。
   这是质量数组函数，不是已经丢掉路径身份后重建原路径 dominant weight 的结论。
3. \(E=W/M\) 与 \(\Delta=LN(E)\) 没有穿过零总质量的绝对误差统一连续性。
   例 \(\mu=t\delta_0\)、\(\nu=(t/2)(\delta_0+\delta_{e_1})\)：质量误差趋零，
   E 恒为1与2；正质量下若要相对误差界须另给 W/M 分母的下界。
4. 有界联合观察 \(F:D\to\mathbb Q\) 满足
   \(|\sum_xF(x)(\mu-\nu)(x)|\leq\|F\|_\infty\|\mu-\nu\|_1\)。
   对四轴乘积等无界观察不能省略该依赖。
   例如 \(\mu=\delta_0\)，\(\nu=(1-t)\delta_0+t\delta_{(R,R,R,R,0,0)}\)：
   对有理 \(t\in(0,1)\)、整数 \(R\geq1\)，两者均为概率，\(D_{6,3}=40t\)，
   四轴乘积差为 \(tR^4\)。取 \(t=R^{-4}\) 则边缘误差趋零而该联合矩差恒为1。
   这也是保留联合方向/位置尺度而不轻易宣告冗余的具体理由。

## 6. 精确验证与下一步

`owner_stability_20260907_check.py` 使用 `Fraction` 检查常数递推、切片账本、
固定种子的有限数组压力样本及上述精确见证；并原样调用现有正权 CWM 实现。
结果在 `owner_stability_20260907_check.json`。
这些检查用于发现实现、常数或见证错误；一般定理的证据仍是 §3 的完整证明。

owner 已独立重建并检查核心切片推导（尤其重片与聚合 F 的区别）；这只是本轮交叉检查，
不冒充独立盲发现、正式 Driver disposition 或 Foundation 提升。

有价值的后续方向是：在确切的 common-anchor raw observer 下缩小
\([3/4,111/20]\) 常数区间；为具体有限 D 生成可精确复核的更锐利误差证书；
将残差范数与当前恢复器输出绑定。不要仅因精确满秩检查通过便创建“已解决有噪恢复”的空泛结论。

辅助工作包：`/root/stability_research`；未创建正式 task、claim 或 review。

Global-Knowledge-Sync: main@ccd838a / GLOBAL_KNOWLEDGE_V1
