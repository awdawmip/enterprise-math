# C78／C87 因数库存有理化重证：续研结果

研究日期：2026-11-22—2026-11-23（Asia/Hong_Kong）。
用户任务：“C78／C87 因数库存，你跑下这个的重证试试”，本轮指令：“继续”。

**本轮完成 C78 近库存锐阈值的整条重证，并把 C87 推到原有限库存、全部舍入原点的准确证书。**
C78 的有限归一化不再含 Gamma 常数；证明中的解析恒等传播和解析零集计数改由有限代数与原格点多项式小值界承担。
C87 得到了指定目录的全原点严格优势、准确最低精度、排序反转实例，以及一个与目录大小无关的相位平均稳定性界。

这些是作者侧完整证明与精确有限计算。没有把保存、同上下文交叉核对或程序 PASS 等同于独立 Review、Working Truth 或 Foundation 接纳。
本轮没有修改任务权重、共享 Task 状态或原定义。

## 1. 最重要的 C78 结论

对基库存 \(c\)，保持全部
\[
\mathcal T_c=\{(V,W):2\le W\le V\le c\},\qquad
|\mathcal T_c|=\binom c2
\]
个原安排。用库存 \(c,c+b\) 各读一次原 \(g=H(0,1)\)，
每次保留 \(p\) 个二进制小数位，两轴全局格原点任意且可随 \(c\) 改变。
记完整目录中独占二维输出格的比例为 \(\mathscr V_c\)。

取完全有理的精度量
\[
\boxed{\Xi_c=\frac{2^{4p_c}b_c^2}{c^9}.}
\]

本轮整合证明：

| 条件 | 已重证的原全库存结论 | 范围 |
| --- | --- | --- |
| \(\Xi_c\to\infty\) | \(\mathscr V_c\to1\)，且对格原点统一 | \(1\le b_c=o(c)\) |
| \(\mathscr V_c\to1\) | 必须 \(\Xi_c\to\infty\) | 全部 \(1\le b_c\le c\) |
| \(\Xi_c\) 沿一子列有界 | 该子列保留固定正比例歧义 | 全部 \(1\le b_c\le c\) |
| \(\Xi_c\to0\) | \(\mathscr V_c\to0\)，且对格原点统一 | 全部 \(1\le b_c\le c\) |

因此在近库存范围，
\[
\boxed{\mathscr V_c\to1\iff\Xi_c\to\infty.}
\]
相邻库存 \(b=1\) 已包含，不需要 \(b\) 增长或额外幂次余量。

如果把结果翻译成传统位数，
\[
p_*(c,b)=\frac94\log_2c-\frac12\log_2b.
\]
“趋于全部可识别”需要 \(p-p_*\to+\infty\)；
相邻库存的临界系数仍是 \(9/4\)。
这不是声称固定加一两位就使所有有限库存完全可识别，也不声称临界窗口已有统一极限函数。

完整证明：[NEAR_STOCK_SHARP_REPROOF.md](NEAR_STOCK_SHARP_REPROOF.md)。

### 本次“有理化”已经支付到哪里

原读数、归一化、有限差分、乘积误差、格点小值和有限计算证书都由整数／有理运算给出。
辅助四次根通过有限代数扩张、乘法矩阵和非零有理多项式处理。
证明仍使用实数极限、紧性、局部逆函数定理、\(C^2\) 插值及单调格行计数。
所以这里没有声称“一切实分析都已经删除”，也没有将全部极限数值断言为有理数。

原 C78 的全部 \(1\le b\le c\) 充分性还可与原 C77 的固定正比例差输入按子列拼接。
本轮独立重做的是最敏感的 \(b=o(c)\) 充分性；C77 其余正比例差证明仍保留来源。
本轮另补了 C77 所用的固定实参数仿射刚性代数证明，见 [REAL_PARAMETER_AFFINE_RIGIDITY.md](REAL_PARAMETER_AFFINE_RIGIDITY.md)。

## 2. 原对象与准确归一化

库存包含两个 2、两个 3、\(n\) 个 5、一个 7；
原三态速率为 \(1/4,1,4\)，两种制备为 \(e_u=(7,u,1-u)/8\)，\(u=0,1\)。
同一安排的前缀是
\[
5^{n-V}\,23\,5^{V-W}\,23\,5^{W-2},
\]
接完整的 \(557,575,755\) 三条尾。
对每条尾取两制备概率比 \(R_j=P_j(1)/P_j(0)\)，原观察量保持
\[
g(n,V,W)=\frac{\max_jR_j}{\min_jR_j}.
\]
增加库存时，额外 5 全放在第一次 23 之前。

前轮已经证明所有尾值准确等于两层有限有理分式；
本轮继续调用其原准确核，没有改用抽样目录或独立竞争者模型。
原生 Heartbeat X6、路径和联合关系保持原对象，
\(x=V/c,y=W/c\) 只是库存标签的辅助参数。

令
\[
F_k(n)=\prod_{j=1}^n\frac{4j+k}{4(j+k)}.
\]
本轮找到固定基库存的准确有理归一化
\[
\boxed{\Gamma_c(n,V,W)=\frac{5[g(n,V,W)-1]}{27F_1(c)}.}
\]
改变观察库存 \(n\) 时，分母始终用同一个 \(F_1(c)\)。

对 \(W\ge4\)，三终尾严格满足 \(z_1<z_2<z_3\)，而且
\[
z_3-z_1=\frac{27}{5}F_1(W)K_W,
\qquad |K_W-1|\le9100/W^3.
\]
常数 \(27/5\) 来自准确分数
\((81/32)/(15/32)\)。
小端点 \(W=2,3\) 的不同极尾次序没有被忽略；它们在原准确核中仍全部计算。

在固定正则内片上，
\[
\Gamma_c(c,V,W)\to
|R(x^{1/4},y^{1/4})|,
\]
\[
R(r,s)=
\frac{50176r^6s^{42}(r^9-4s^9)(1-4r^{15})}
{(1+448r^{51}s^9)(1+1792r^{66}s^9)}.
\]
旧共同 Gamma 常数已从这个有限归一化和极限表示中消去。
这不涉及证明 Gamma 常数本身有理。

完整恒等式与任意固定阶联合差分：
[RATIONAL_NORMALIZATION_AND_DISCRETE_JETS.md](RATIONAL_NORMALIZATION_AND_DISCRETE_JETS.md)。

## 3. C78 重证中原先缺的四座桥

### 3.1 从离散原值到真正 \(C^2\) 的辅助图

对
\[
Z_{c,b}=\frac cb[\Gamma_c(c+b)-\Gamma_c(c)]
\]
使用准确有限平均
\[
Z_{c,b}
=\frac1b\sum_{j=0}^{b-1}c\,\Delta_n\Gamma_c(c+j).
\]
空间二阶控制只需联合三阶差分，因此相邻库存不会产生 \(1/b\) 的误差损失。

有理五次 Hermite 插值每格只用 \(4\times4\) 个原合法节点，
准确保留节点读数，整体为 \(C^2\)。
其值算子的差分因式分解给统一稳定常数 16，
避免把独立节点误差乘上 \(c^2\)。
得到
\[
(\Gamma_c(c),Z_{c,b})
\longrightarrow
(G,-EG-\tfrac34G)\quad\text{于 }C^2,
\]
局部误差形式为
\[
C_K\bigl(F_1(c)+1/c+b/c\bigr).
\]

证明与全部形函数系数：
[RATIONAL_HERMITE_C2_BRIDGE.md](RATIONAL_HERMITE_C2_BRIDGE.md)。

### 3.2 原谱的正则性已经有具体整数多项式证据

直接对 \(R\) 本身计算：

| 对象 | 清分母后的整数多项式项数 | 16维范数格点次数参数 |
| --- | ---: | ---: |
| \(\det D(R,ER)\) | 39 | 1588 |
| \(\det D^2R\) | 86 | 2188 |

全部系数、电路除法、乘回恒等式及非零最低齐次项已经实际核验。
由有限 Lagrange 格点界，原 \(c^{-1}\) 格上两种退化零点合计不超过
\[
\boxed{3776(c+1).}
\]
更重要的是，保留小值而不只零点后，同样可以删除任意小的固定密度，
取得足够大的正则原格点集合。
不需要从“解析零集面积为零”直接跳到原格点密度。

证明与证书：
[EXPLICIT_REGULARITY_AND_NORM.md](EXPLICIT_REGULARITY_AND_NORM.md)、
[explicit_algebra_certificate.json](explicit_algebra_certificate.json)。

### 3.3 跨逆分支方向小值已转回原有理格

在实际等谱对应的有限代数分量上，存在一个固定坐标方向 \(i\)，使
\[
\nabla G(q)\cdot m-k\,\partial_iG(S(q))
\]
对全部整数 \(m\)、正整数 \(k\) 都不是恒零域元素。

证明把可能的两个方向恒等合成有理矩阵，
经等谱、等 Euler 读数的形式微分和非退化 Hessian 推出仿射配对；
已经重证的仿射刚性排除非恒等配对。
这一步不再调用实解析恒等传播。

乘法特征多项式必须先去掉恒零分量产生的最大零根因子，再清基域分母。
这样得到非零有理多项式，其小值集合包含真实方向小值点。
偶发的数值零点仍完整保留，不能在数值点直接除以该方向函数。

完整构造：
[ALGEBRAIC_DIRECTION_AND_SMALL_VALUES.md](ALGEBRAIC_DIRECTION_AND_SMALL_VALUES.md)。
小型机制核对：
[FACTOR_REMOVAL_CHECK.md](FACTOR_REMOVAL_CHECK.md)。

本轮没有实际展开完整大对应代数的全部乘法矩阵。
这项存在性构造足以支付渐近定理；
它不等于已经提供所有有限库存可用的统一数值常数。

### 3.4 必要尺度直接由原库存同步带给出

对固定有理 \(0<h\le1/16\)、充分大的 \(c\)，
原有限同步带中至少有
\[
\frac{hc^2}{1152}
\]
个安排。
这些安排的两次归一读数位于长 \(O(h)\)、厚 \(O(hb/c)\) 的对角带。
任意原点、同宽 \(\delta\) 的格数上界明确为
\[
(2+Mh/\delta)(3+2Mh(b/c)/\delta),
\]
其中 \(M\) 是文稿列出的固定有理常数。
条目数与格数直接比较，就得到有界精度盈余下固定比例的歧义。

另一份跨同步有限条带界对全部 \(W\ge\eta c\) 保留安排给出
\[
0\le\Gamma_c(n)\le C_0(\eta),\qquad
|\Gamma_c(c+b)-\Gamma_c(c)|\le C_1(\eta)b/c,
\]
包括内外同步和同步穿越；没有除以 \(1-\rho\)。
该界使 \(\Xi_c\to0\Rightarrow\mathscr V_c\to0\) 覆盖全部 \(1\le b\le c\)。

证明：
[NATIVE_SYNC_BAND_PACKING.md](NATIVE_SYNC_BAND_PACKING.md)、
[NORMALIZED_STRIP_BOUND.md](NORMALIZED_STRIP_BOUND.md)。

## 4. C87：指定有限目录已经覆盖全部连续舍入原点

取 \(c=8\)，完整目录有 28 个安排。
固定首末库存 8、24，比较三个中间库存：

| 方案 | 三次库存 | 中间相对位置 |
| --- | --- | --- |
| Q | \((8,12,24)\) | \(1/4\) |
| M | \((8,16,24)\) | \(1/2\) |
| E | \((8,23,24)\) | \(15/16\) |

在每个方案中，所有安排共享同一三轴原点 \(\mathbf u\in[0,1)^3\)；
比较方案时也使用同一个 \(\mathbf u\)。
每个标签 \(\lfloor2^pg+u_j\rfloor\) 仅在一个准确有理断点变化，
全部断点的公共分区因而把连续原点全集化成有限半开盒。
左端点按照原 floor 约定归入右侧区间，零测边界也没有遗漏。

### 每次保留12位

| 量 | 全原点最小值 | 全原点最大值 |
| --- | ---: | ---: |
| \(U_Q\) | 22 | 28 |
| \(U_M\) | 24 | 28 |
| \(U_E\) | 7 | 26 |
| \(U_Q-U_M\) | -4 | 4 |
| \(U_M-U_E\) | **2** | **21** |

因此已有直接原有限库存全称结论：
\[
\boxed{
U_{(8,16,24)}(\mathbf u)
-U_{(8,23,24)}(\mathbf u)\ge2
\quad\text{对全部共同原点 }\mathbf u.
}
\]
唯一率优势至少为 \(2/28=1/14\)。

例如：

- \(\mathbf u=(1/8,29/32,601/1024)\) 时，三方案计数为 \((28,26,24)\)；
- \(\mathbf u=(11/32,1/64,0)\) 时，计数为 \((24,28,7)\)。

比较条件必须保留“共同原点”。
如果中点另选 \((0,0,0)\) 得24条，而靠端点方案另选
\((3/8,99/128,3/4)\) 得26条，则跨两套原点不具有上述优势。
这两种量词不可混用。

### 每次保留13位及准确最低精度

中点方案 \((8,16,24)\) 在全部原点都能识别28条。
对任何有限有理目录，令
\[
d_*=\min_{\alpha\ne\beta}\max_j
|g_j(\alpha)-g_j(\beta)|.
\]
则准确充要判据是
\[
\boxed{\text{全部原点、全部安排都唯一}
\iff 2^pd_*\ge1.}
\]
等号有效，因为距离一整个格宽的两个数永远不同格。
这个判据不依赖不同精度下任意平移的格是否嵌套。

每个方案准确比较全部 378 对安排，得到：

| 三次库存 | 全原点全目录可辨认的最小非负整数位数 |
| --- | ---: |
| \((8,12,24)\) | 14 |
| \((8,16,24)\) | **13** |
| \((8,23,24)\) | 15 |

这是三项指定方案各自的准确最低精度，没有声称已搜索所有可能中间库存的全局最优位置。
它也不同于 C78 “绝大多数安排可识别”的渐近位数系数。

完整定理、断点算法、极值见证及分数：
[NATIVE_FINITE_ORIGIN_THEOREMS.md](NATIVE_FINITE_ORIGIN_THEOREMS.md)、
[native_gap16_all_origins.json](native_gap16_all_origins.json)。

## 5. C87 的有限排序反转及平均排序

另固定首末库存 8、12，每次保留10位，比较
\(A=(8,9,12)\) 与 \(B=(8,10,12)\)。

全部共同原点下，
\[
\boxed{-8\le U_A-U_B\le8.}
\]
两个准确见证：

| 共同原点 | 四分点唯一数 | 中点唯一数 |
| --- | ---: | ---: |
| \((1/16,11/256,0)\) | 9 | 17 |
| \((0,9/16,3/8)\) | 23 | 15 |

这已排除“有限库存中某个位置不看原点就总是占优”的一般断言。
它不否定 C87 在规定极限顺序下的辅助主常数排序。

对全部原点作准确有限体积平均，同一个例子却有严格平均排序：
\[
0.698883463720<\overline V_A<0.698883463721,
\]
\[
0.705786828679<\overline V_B<0.705786828680,
\]
\[
\boxed{
0.006903364959<
\overline V_B-\overline V_A<
0.006903364960.
}
\]
这里平均率与逐原点率明确区分。
所有小数端点均由准确有理外包比较给出，完整分数保存于
[phase_average_results.json](phase_average_results.json)。

## 6. 可继续复用的有限稳定性定理

设 \(X,Y\) 是同一完整目录的 \(N\times d\) 归一读数阵列，
已经除以观察格宽；原 \(p\) 位读数对应 \(X=2^pg\)。
记
\[
d_{ij}=\min(1,|X_{ij}-Y_{ij}|),\qquad
p_i=1-\prod_{j=1}^d(1-d_{ij}).
\]
则相位平均唯一率满足
\[
\boxed{
|\overline V(X)-\overline V(Y)|
\le\min\left(1,\frac2N\sum_i p_i\right).
}
\]
若每轴统一误差不超过 \(\varepsilon_j\le1\)，还可用
\[
|\overline V(X)-\overline V(Y)|
\le2\left[1-\prod_j(1-\varepsilon_j)\right]
\le2\sum_j\varepsilon_j.
\]
常数与目录大小 \(N\) 无关，系数2有准确取等号实例。

证明只用：一条安排改换输出格至多改变两个唯一安排计数；
再在公共有理相位分区上作有限加权和。
不同竞争者共享原点的联合关系完全保留。

相位平均本身也有准确有限公式
\[
\overline V(X)=\frac1N
\sum_{\varnothing\ne S}(-1)^{|S|-1}|S|
\prod_j\left(1-\max_{i\in S}X_{ij}+\min_{i\in S}X_{ij}\right)_+.
\]
所有不可能共同碰撞的子集可以准确删零；这不是独立碰撞近似。

在上节 \(c=8,p=10\) 的例子中，把原 \(g\) 向下截断到
**21个二进制小数位**，已有
\[
\boxed{
\overline V_B-\overline V_A
\ge\frac{8060749}{7516192768}>0.
}
\]
观察精度仍是10位，21位仅是计算输入的充分证书精度。
未声称21位是所有算法的最小计算精度。
截断阵列的团容斥与45,414个正体积相位盒求和准确相等。

完整证明：[FINITE_PHASE_STABILITY.md](FINITE_PHASE_STABILITY.md)。

## 7. 额外得到的实际谱范数证书

原四次根辅助谱的 16 维范数可以写成
\[
\operatorname{Norm}(R)=
\frac{50176^{16}x^{24}y^{168}
(x^9-256y^9)^4(1-256x^{15})^4}
{\big[(1-448^4x^{51}y^9)(1-1792^4x^{66}y^9)\big]^4}.
\]
整数素因子赋值说明四个相关因子在正有理 \(x,y\) 上均不为零：
前两个由2进赋值矛盾，后两个由7进赋值模3矛盾。

因此在全部原有理库存格上，可给正根分支的保守有理下界
\[
|R|\ge
\frac{50176}{805057\cdot85^2c^{36}}.
\]
这支付有限代数可逆性与下界用途，
不表示原有限 \(\rho\) 永不同步，也不表示不同安排不会同格。

证明与实际16维行列式检查：[SPECTRUM_NORM.md](SPECTRUM_NORM.md)。

## 8. 实际执行证据及其限度

| 已执行工作 | 本轮确切规模／结果 |
| --- | --- |
| 实际 Jacobian、Hessian 整数电路 | 39项与86项；准确除法、乘回、非零首项及范数检查通过 |
| 有理 Hermite 系数 | 端点匹配、移位整除、权重和、Bernstein界通过；二维稳定常数16 |
| 原终尾与归一化 | 61个尾次序／因式案例，内外符号四种组合均逐分数相等 |
| 联合差分误差计算 | \(c=256,\ldots,16384\)，126组准确误差比较 |
| 原谱范数 | 8个原有理格点的16维行列式，加3个正根有理点下界 |
| 零特征因子机制 | 6个有理参数、42个特征行列式值，以及两类矩阵恒等式 |
| C87全部原点 | 最终三案例合计190,907个完整半开盒 |
| 原路径与新库存 | \(n=23,24\) 的56个库存／安排组合、168个单尾准确等式 |
| C87相位平均 | 两方案96项／63项非空团；另一路45,414个相位盒求和逐分数一致 |
| 原有限同步带 | 明确常数和27个逐行有理实例；完整证据见 sync_band_checks.json |

有限抽查用来核验索引、实现、系数和指定结论；
全称命题由对应书面证明承担。

特别保留一个实际数值限制：
在 \(x=(3/4)^4,y=(1/2)^4\) 的例点，第一归一读数相对极限值的绝对相对误差为：

| \(c\) | 准确有理外包 |
| ---: | --- |
| 2048 | \([0.714325385,0.714325386]\) |
| 4096 | \([0.314253781,0.314253782]\) |
| 8192 | \([0.147553425,0.147553426]\) |
| 16384 | \([0.071515283,0.071515284]\) |

相邻库存差商在 \(c=16384,b=1\) 的相对误差仍约7.01%。
这说明“证明收敛”不能直接替代任一有限库存的误差预算；
本轮没有为改善展示数字继续扩大库存。

## 9. C87 哪一部分仍继承原分析

前轮已经用有限正部面积公式重证辅助 \(I_\theta\) 的严格凹性、
对称和位置排序，并构造61段有理代理。
它继承原准确位置积分恒等式及原核正性证书。
本轮新增有限原点证书和平均稳定性，未把那些继承输入抹掉。

当前 C84 原库存到 Haar 联合模型的桥，仍要求固定有理位置，
先固定精度倍率，并满足外间距增长条件。
所读原证明的跨分支、空间二次及插值误差分别为
\(O(c^{1/2}/B^{3/2})\)、\(O(D^3/c)\)、\(O(B/c)\)，其中 \(D=\sqrt{c/B}\)，
没有附可直接用于本轮指定有限库存的全域数值常数。
C86 高精度比较还保留 \(o(L^{-1/10})\)，明确未给显式起效 \(L_0\)。

所以已经完成的 C87 有限结论是指定原目录的严格证书。
尚未得到的是“辅助全位置高精度排序在任意给定有限库存开始成立”的统一阈值。
有限反转例子也说明，这个连接不能凭渐近图形直接宣布。

可恢复的研究接口现在很明确：
原有限完整阵列及每条坐标的误差预算，
可以直接代入本轮稳定性定理；
逐原点结论则使用全部有理断点分区。
原库存—Haar 的全域有效误差仍是单独的数学工作，
不能把相位平均误差界当作逐原点一致误差。

## 10. 复算与来源

除两个符号系数核对脚本使用 SymPy 外，其余实际计算使用 Python 标准库、
任意精度整数和 fractions.Fraction。
本目录的脚本默认复用前轮已保存准确核，避免复制出第二个来源。

从本目录运行：

    python check_explicit_algebra.py
    python check_direction_denominators.py
    python check_rational_hermite.py
    python check_rational_jet_bridge.py ../c78_c87_rational_reproof_20261122_af81e5b398b7
    python verify_spectrum_norm.py
    python verify_zero_factor.py
    python verify_sync_band.py
    python check_new_native_paths.py --kernel ../c78_c87_rational_reproof_20261122_af81e5b398b7/exact_inventory.py
    python all_origins_compare.py --kernel ../c78_c87_rational_reproof_20261122_af81e5b398b7/exact_inventory.py --c 8 --gap 4 --middles 1 2 --precisions 10 --output native_gap4_all_origins.json
    python all_origins_compare.py --kernel ../c78_c87_rational_reproof_20261122_af81e5b398b7/exact_inventory.py --c 8 --gap 16 --middles 4 8 15 --precisions 12 13 --output native_gap16_all_origins.json
    python phase_average.py --kernel ../c78_c87_rational_reproof_20261122_af81e5b398b7/exact_inventory.py

当前源阅读快照：
enterprise-math@07764cb22422a2710c8a329a0c67ba60013312d4。
前轮已保存研究包：
enterprise-math@46eec634a39fd202babd05e66b251d90945be948，
research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/。

关键原来源：

| 原文件 | Git blob |
| --- | --- |
| C78 SHARP_NEAR_STOCKS.md | 41d996898817258383a4232262540f5629b88059 |
| C78 LOCAL_ADJACENT.md | a2259ca801cccf447083fb4449537d354fba393e |
| C77 TWO_STOCK_PRECISION.md | dd67713b07026321ffc706f2c510ced697b2ba67 |
| C84 READING_POSITION.md | a23a818c9356a08e0e5e6feee05447ddc26ee4d7 |
| C86 CERTIFIED_HIGH_PRECISION_COMPARISON.md | 771ee74f492ace2a2d85dbbc26128708b68bc675 |
| C87 GLOBAL_POSITION_THEOREM.md | ace988b74f301e6937570dbab8b4deb727e49924 |
| C87 INTEGRATED_KERNEL_PROOF.md | 40b327ba8a5ec56544d1166c605af78ea960cabe |
| 前轮原准确核 exact_inventory.py | 873aa277eb51e489a37a8d028f7f43b1e5c2a3f7 |

本次证明没有调用黎曼猜想；其依据是这些原有限模型、列明的代数证明与辅助实分析步骤。
同上下文作者分工为主会话、c78_explicit_algebra、c78_algebraic_direction、c87_native_bridge。
沿用 Driver-ID EM-DVR-2D6C6F / CONTROL_PLANE，
会话 MCP-d6362c0d7d31434e82af45c5e425dc26，DA-F510B2698ACA7B1E8F0B；
本轮没有制造新的 Task CLAIM 或独立审查身份。
