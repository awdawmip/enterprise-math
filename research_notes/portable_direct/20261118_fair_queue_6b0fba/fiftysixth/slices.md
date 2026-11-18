# 三维铺砌到 X6 切片的联合见证、周期与记忆下界

固定外稿把二维整数坐标和一个有限循环坐标提升为真正的三维整数铺砌。这里得到两个可检验的结论。其标准构造的全部整数周期恰为 \(\mathbb Z(0,0,mQ)\)。若用三个可逆可交换的空间动作、有限控制和两个只作加法的整数计数器读出这个指定铺砌，控制轨道至少有 \(mQ\) 个状态。另在项目实际 signed-X6 内核上，三个两两可共见的次序事件没有共同历史。两类结论分别约束地址记忆和事件关联。

本题 155-E 消费外稿的未准入构造。以下凡用「该瓦片可铺但没有完全周期铺法」，均以冻结预印本的相应结论为前提。旧轮分别研究了标签编码、堆叠的投影及网格对齐、两种子的容量。本篇问哪些带来源的原生态能共同满足同一套标记。以下固定 P000 的六条原生空间轴、三轴切片和独立的时间语义。[任务书](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_tasks/RS-OAI7-155-E-20261007-6F2A81.md) · [外稿 §7](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/07-three-dimensions.tex)

## 一、标准构造的精确周期

对有限集合 \(T\subset\mathbb Z^3\)，以二值中心标记 \(x:\mathbb Z^3\to\{0,1\}\) 表示一重铺砌。这要求每个 \(g\) 满足
\[
                     \sum_{t\in T} x(g-t)=1.                    \tag{1}
\]
这是有限型局部约束。若 (1) 的任一解具有两个线性独立的整数周期，则 (1) **另有**一个完全周期解。为了给出有限判据，设两个周期为 \(v_1,v_2\)，\(d\) 为 \(v_1\times v_2\) 各分量的正最大公因数，\(n=(v_1\times v_2)/d\)。商群 \(\mathbb Z^3/\langle v_1,v_2\rangle\simeq\mathbb Z\times K\)，其中 \(|K|=d\)；沿无限方向的坐标为 \(g\mapsto n\cdot g\)。这是整数矩阵 Smith 形或饱和二维格的指数公式。

设 \(h=\max_{t\in T}n\cdot t-\min_{t\in T}n\cdot t\)。每个高度有 \(d\) 个横向剩余类，以 \(d\) 位二值字母记一层。保留连续 \(h\) 层作状态，每加一层，检查所有横向类的一组 (1)；若两个瓦片位移在商中相同，其两份贡献都要计算。该图最多 \(2^{dh}\) 个状态。任何 \(h+2^{dh}\) 个连续层若通过全部内部检查，就含有一条闭游走。循环重复并提升，给出一个完全周期解。\(h=0\) 时合格单层本身即可重复。这也给出可逐对测试的有限阻碍：若外稿的无完全周期性成立，则外稿 \(T\) 的每个整数铺砌的周期秩至多一，不能只因某个铺法无满秩周期就对它应用这个结论。

**标准例的最小竖直周期也能确定。** 外稿 §3 取循环群
\[
 V=C_D\times\prod_i(C_{r_i^2}\times P_i),\quad
 P_i=C_{a_i}\times C_{b_i},\quad J=\prod_i r_i.
\]
其垂直低位映射的核 \(H_0\) 阶为 \(D\prod_i r_i a_i b_i\)，指数为 \(J\)。共同解 \(A\) 在每个水平坐标的垂直纤维都是 \(H_0\) 的一个完整截面，因为 \(A\oplus H_0=\mathbb Z^2\times V\)。\(J\) 的每个素因子都整除 \(|H_0|\)。

一般地，若 \(H\le C_{DJ}\) 阶为 \(D\)，截面 \(E\) 的平移稳定子 \(P\) 满足 \(P\cap H=0\)，否则同一陪集有两个代表。故 \(|P|\mid J\)，而两个循环子群交的阶为 \(\gcd(|P|,D)\)，所以 \(|P|\) 整除 \(J\) 中与 \(D\) 互素的最大因子。此上界可达：取该阶的子群，它在商 \(C_{DJ}/H\) 上自由作用；每个轨道选一项和一个提升，再平移补全整轨道。对外稿的 \(H_0\)，上界恰为一，因此每个水平纤维都不允许非零竖直周期。[外稿 §3 的 \(V,H_0\) 与图方程](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/03-cyclic-encoding.tex#L64-L109)

外稿 §6 的标准提升为 \(A\times\{0\}\)，新增 \(C_q\) 取 \(q\nmid|V|\)，垂直群 \(V\times C_q\simeq C_Q\)，\(Q=q|V|\)。这个提升依然没有非零纯竖直稳定子。§7 取 \(B\) 为该标准解在 \(\pi:\mathbb Z^3\to\mathbb Z^2\times C_Q\) 下的满原像，铺砌大瓦片的平移中心为 \(mB\)。故其纯竖直周期恰为 \(mQ\mathbb Z e_3\)：周期必须属于 \(m\mathbb Z^3\)，除以 \(m\) 后再模 \(Q\) 须稳定原截面。已有这条周期，并且上一段排除了两个独立周期，所以
\[
          \operatorname{Per}(1_{mB})=mQ\mathbb Z e_3 .           \tag{2}
\]
这确定的是上述标准构造的精确周期；其他整数铺法受周期秩至多一的共同限制。[外稿 §6 标准堆叠](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/06-stacking.tex#L63-L78) · [§7 满原像、标准平移集](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/07-three-dimensions.tex#L131-L165)

## 二、可逆可交换地址系统的锐下界

固定下面的记忆模型。状态为 \((s,c)\in S\times\mathbb Z^C\)，其中 \(S\) 有限，三个有名字的正负空间动作由可逆、彼此可交换的
\[
           T_i(s,c)=(\pi_i s,c+b_i(s))
\]
及其逆给出。计数增量只依赖控制态，读数 \(R(s,c)\in\{0,1\}\) 是同一个固定函数。从给定初态读出全体 \(T^g\)，生成标记 \(x(g)\)。若有外部地址、随计数值选择不同转移或不相容的换序路径，就需要另立模型。

设 \(H\le\mathbb Z^3\) 是起始控制态的稳定子。由于动作可交换，\(H\) 固定整个可达控制轨道，且在该轨道上每个 \(a\in H\) 的计数位移相同。事实上将 \(T^aT^g=T^gT^a\) 作用于初态即可。因而得到同态 \(\beta:H\to\mathbb Z^C\)，
\[
        \ker\beta\subseteq\operatorname{Per}(x),\qquad
        \operatorname{rank}\operatorname{Per}(x)\ge3-C.          \tag{3}
\]
对任一外稿整数铺法，至多一个计数器的系统被上节有限型判据排除。

若给定标记恰有 \(\operatorname{Per}(x)=P\mathbb Z e_3\)、\(P\ge1\)，且 \(C=2\)，则 \(\ker\beta\) 秩至少一，必为竖直方向的非零子群。记 \(d\) 为 \(e_3\) 在 \(\mathbb Z^3/H\) 中的阶。\(de_3\in H\)，其某个正倍数在 \(\ker\beta\) 中。因为 \(\mathbb Z^2\) 无挠，已有 \(de_3\in\ker\beta\)，故 \(P\mid d\)。于是
\[
     P\mid [\mathbb Z^3:H]=\#\{\text{可达控制态}\}.              \tag{4}
\]
对 (2) 代入 \(P=mQ\)。这既是状态数下界也是整除约束。纯地址表示达到下界：两个整数存 \((g_1,g_2)\)，\(P\) 个状态存 \(g_3\bmod P\)，固定读数查询所给铺砌在该处的值。这一上界需要原铺砌谓词的访问权；它没有制造出该谓词、一个有限计算程序或任何原生占据规则。

## 三、从原生动作到同一套标记

冻结源给出 X6 原生空间是带选择锚点的六维整数仿射挠子，最终 Cell 地址另守六个非负字段的合同。选择三个不同原生轴 \(E_{i_1},E_{i_2},E_{i_3}\) 和一个具名锚点 \(a\)，定义原始位移切片
\[
 \iota(g)=a+g_1E_{i_1}+g_2E_{i_2}+g_3E_{i_3}.
\]
三个分量均可独立改变；其余三个字段保留锚点的原值。\(g\mapsto g\pm e_j\) 在源 \(\texttt{Spatial6.step}\) 上是一个有来源的原生单轴步。多个步的完整路径有次序、可能有多支。这里的整数仅用于原始位移；报告并未产出任意 X6 Cell 的注册最终地址编码。[原生 Cell 挠子及地址合同](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md) · [实际原始位移／切片接口](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py)

**一个足够且可核查的联合接口。** 在这条切片上，须声明一个允许的全局装饰态 \(s\in\mathcal S_{\rm native}\)，以及同一个有来源的局部查询 \(R\)。它读的是「这一具名 Cell 是否作为一个平移中心」。若多条路径抵达同一中心，须指明中心标识、路径见证及二者的读出关系。对目标 \(g\) 的见证为所有 \((R(s,\iota(g-t)),t)_{t\in T}\)，在**同一** \(s\) 中恰有一项取 1。若对所有 \(g\) 成立即给原生装饰到某个外部铺法的实现；若还希望实现标准 \(mB\)，必须逐个核对 \(R(s,\iota(g))=1_{mB}(g)\)。原生作用、所有检测到的场或通道约束也须在该 \(s\) 上成立，另选一个中心集附到每张局部图不足以给出这个见证。

在附加的有限字母闭约束模型里，此接口可化为各尺度的同现问题。具体地，若允许的原生装饰集合是非空紧配置空间的闭子集，查询是局部连续的，则每个有限目标集的检查对应闭集。若任意有限目标集都能通过一个共同装饰，有限交性质就给出全局装饰。已给定具体 \(mB\) 时可把逐位置相等也并入闭约束。只有可行的二点查询并不保证任意有限目标有共同见证；若允许每个位置取无界离散值，紧性也不自动成立。例如在整条整数线上要求共同的非负整数状态 \(s(z+1)=s(z)+1\)，每个有限段都能选足够高的起始值，全线却不可能。

**两个实际源限制。** 第一，选三轴的 \(\texttt{observe}\) 读数仅将三个可见数减去共同最小值，故对 \((1,1,1)\) 的切片平移恒定。任何仅依这个读数的标记都有该周期；再加仅由平移更新的有限置换标签，也保存此向量的某个非零倍数为周期。它与 (2) 的纯竖直周期不平行，故这类读数不能生成标准铺法。在 \(\texttt{hidden_slice_coordinates}\) 中可见共同偏移和三个外轴原值足以恢复具名 Cell，但源函数没有给它一个铺砌中心位。

第二，固定一次各走一条不同正原生轴。具有指定先后条件 \(i\prec j\) 的共同最短历史数，恰等于这些条件的线性扩张数。因为最短词是这些轴的一次置换；在已走轴的子集格中，仅当前置轴都已出现时才添加新轴，正权邻接矩阵的定长 BRC 路数即为该数。三轴例的起点是 \((3,-5,7,11,-13,17)\)，选原生轴 1、3、5；终点为 \((4,-5,8,11,-12,17)\)。冻结 signed-X6 核给最短词恰六个，起终点的可见三元读数均为 \((16,20,0)\)，真实共同偏移却由 \(-13\) 变为 \(-12\)。对局部序号条件 \(1\prec2,2\prec3,3\prec1\)，分别每个条件有三条合法历史，每一对有一条，三者合在一起有零条。程序实际调用两个公开 BRC 内核核对端点、每条有名步以及约束组合；六条路径只抵达一个具名终点。[signed-X6 定长核](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py) · [正权矩阵核心](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/src/enterprise_math/brc_weighted_recurrent.py)

## 四、两个可完整核对的小模型

- **共同合法层的有限寿命。** 对 \(T=\{0,e_1,e_3\}\) 强制周期 \(2e_1,e_2\)。横向两余类为一个二位字母。逐层应用 (1)，唯一允许的有向边为 \(11\to00\)、\(00\to01\)、\(00\to10\)。用正权矩阵全起点求和的 \(0,1,2,3,4\) 步路径计数为 \(4,3,2,0,0\)。局部有合法试放，连续通过三个层转移就不可能。此处所有量都在小瓦片上精确枚举。
- **两计数器界确实可达的显式装饰。** 取竖直棒瓦片 \(T_P=\{0,e_3,\ldots,(P-1)e_3\}\)，\(P\ge2\)。每条竖线以 \(z\equiv\mathbf1_{(x,y)=(0,0)}\pmod P\) 为中心。每个目标被唯一覆盖。远离例外柱的两条柱迫使任一周期的竖分量为 \(P\) 的倍数；例外柱随即迫使横分量为零。其周期群恰为 \(P\mathbb Z e_3\)。两整数计数器与 \(P\) 个有限状态按此显式公式读出，无需外部表。\(P=5\) 时程序核对了 275 个三维位置的精确覆盖和 539 个平移，竖端口的周期在固定正权循环矩阵上复算。该棒瓦片也允许其他完全周期铺法；例子检验的是指定装饰的锐记忆下界。这个小型读数是人为声明的条件装饰。

真实外源的循环群算术另以 34 种核阶和指数、19919 个截面逐个验证稳定子上界并核对可达性。运行 \(\texttt{python slices_check.py --repo /path/to/enterprise-math}\) 会比对三份实际源代码的 SHA-256，再加载源函数。两个可选参数可核指定外稿各章节和 P000 快照。原任务所缺的最小输入已定位为一个对真实原生装饰有效、具名且平移相容的中心位查询，连同其所有有限目标的共同见证；现有签名路数和坐标接口只验证了上面声明的地址及历史层。这里只作条件算术传递，未获得原生非周期世界的构造。[复算程序](slices_check.py) · [确定性结果](slices_checked.json)
