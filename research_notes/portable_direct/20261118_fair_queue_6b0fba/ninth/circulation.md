# 六轴按权次序的一阶方差：精确抵消、剩余方差与速率分裂

把六条轴按单个名字的选取权分成 $q$ 组。反对称边权矩阵 $\lambda$ 消去 $1/N$ 方差项的充要条件是：**对每条轴，它指向每一个等率组的边权和都为零**。满足条件的空间维数为 $\binom{6-q}{2}$。因此有五种或六种不同速率时，任何非零读数都保留 $1/N$ 项。速率很接近时，这个正系数可以极小：本文给出一个六个速率全异、但首项系数随分裂参数恰以八次方出现的例子。

## 1. 由有序分支概率计算精确方差

每条使用中的轴有 $m_i=Nw_i>0$ 个名字，$m_i$ 为整数，单名固定权为 $a_i>0$。在剩余库存 $r=(r_i)$ 处，下一步属于轴 $i$ 的概率为 $r_i a_i/\sum_j r_j a_j$，同轴名字均匀选取。令每个名字独立取一枚率 $a_i$ 的指数排序键 $X_{iu}$。指数时钟的最小值选择概率与上述分支概率相同，取走最早名字后由无记忆性逐步得到完整排序律。排序键仅用于这一有偏路径抽样，目标位移给出的各轴原生正负方向仍保留。冻结材料已给出两轴加权方差与六轴等率环流，本文从完整六轴加权分支计算。[任务书](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/RS-X6-WEIGHTED-CIRCULATION-CANCELLATION.md) · [固定的加权抽样](https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/weighted.md) · [等率六轴投影](https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/x6_projection3.md)

对 $i<j$ 令 $A_{ij}$ 为 $X_{iu}<X_{jv}$ 的步对比例，$p_{ij}=a_i/(a_i+a_j)$。记 $H=\sum_{i<j}\lambda_{ij}(A_{ij}-p_{ij})$，并以 $\lambda_{ji}=-\lambda_{ij}$ 定向。给定率 $a$ 的一个名字取值 $x$，它先于率 $b$ 名字的中心化条件期望为
$$
 f_{a,b}(x)=e^{-bx}-\frac{a}{a+b}.
$$
一条边对两个名字的一元投影分别为 $f_{a_i,a_j}(X_{iu})$ 和 $-f_{a_j,a_i}(X_{jv})$。从中心化指标减去二者得到二元余核 $R_{ij}$，对任一名字单独取条件期望均为零。于是
$$
 H=\sum_i\frac1{m_i}\sum_{u=1}^{m_i}g_i(X_{iu})
 +\sum_{i<j}\frac{\lambda_{ij}}{m_i m_j}\sum_{u,v}R_{ij}(X_{iu},X_{jv}),
 \qquad g_i=\sum_{j\ne i}\lambda_{ij}f_{a_i,a_j}.
$$
两部分正交。任意不同的具名二元余项，若无共同名字则独立；若恰共用一个名字，则条件于该名字后二者的中心化使协方差为零。

定义
$$
 K_a(b,c)=\operatorname{Cov}_{X\sim\operatorname{Exp}(a)}(e^{-bX},e^{-cX})
 =\frac{abc}{(a+b+c)(a+b)(a+c)}.
$$
单条命名边的指标方差减去两项一元方差，给出
$$
 r(a,b)=\frac{ab}{(a+b)^2}-K_a(b,b)-K_b(a,a)
 =\frac{ab(a^2+ab+b^2)}{(a+b)^2(a+2b)(2a+b)}>0.
$$
故对每一合法整数库存，精确成立
$$
 \operatorname{Var}H=\frac{C_1}{N}+\frac{C_2}{N^2},\qquad
 C_1=\sum_i\frac1{w_i}\sum_{j,k\ne i}
      \lambda_{ij}\lambda_{ik}K_{a_i}(a_j,a_k),\qquad
 C_2=\sum_{i<j}\frac{\lambda_{ij}^2}{w_iw_j}r(a_i,a_j).
$$
该式同时给出定向符号：两个不同轴对仅共享轴 $i$ 时，若 $i$ 在两边同为起点或同为终点，协方差为 $+K_{a_i}(a_j,a_k)/m_i$，角色相反时为其负。两对轴不交时，其完整内部次序独立。由于 $r>0$，只要 $\lambda\ne0$，$C_2$ 严格为正。完整方差恒零当且仅当所有边权为零。

## 2. 等率组分类与可计算的见证

设不同速率为 $b_g$，$G_g=\{j:a_j=b_g\}$。写 $d_{ig}=\sum_{j\in G_g}\lambda_{ij}$。由 $C_1=\sum_i\operatorname{Var}(g_i)/w_i$，其为零当且仅当每个 $\sum_g d_{ig}e^{-b_gx}$ 为常数。该连续函数在 $x\to\infty$ 时趋零，互异正指数函数线性独立，故所有 $d_{ig}=0$。反向代入立得抵消。数值上也可用柯西型 Gram 矩阵；对互异 $b_1,\ldots,b_q$ 有
$$
 \det[K_a(b_g,b_h)]_{g,h=1}^q
 =a^q\prod_g\frac{b_g^2}{(a+b_g)^2}\,
 \frac{\prod_{g<h}(b_h-b_g)^2}{\prod_{g,h}(a+b_g+b_h)}>0.
$$
库存比例 $w_i$ 改变方差系数，但只要都正，就不改变抵消核。

令 $U$ 为各组指示向量张成的空间。抵消条件等于 $\lambda U=0$；因 $\lambda$ 反对称，可自由选择的部分恰为 $U^\perp$ 上的反对称矩阵。由此

| 速率种数 $q$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| 六轴 $C_1=0$ 的维数 | 10 | 6 | 3 | 1 | 0 | 0 |

在同一组内，条件是各轴净流为零，可由三角环生成。不同两组之间的矩形子矩阵要求行和与列和同时为零，可由两边各选两轴构成的四环生成。各块的自由度分别为 $\binom{|G_g|-1}{2}$ 和 $(|G_g|-1)(|G_h|-1)$。特别地，普通三环只有在所涉三条轴的速率相同时才消去首项。

下表均取 $m_i=N$。箭头表示沿环的每条有向边系数为 $+1$，其反向为 $-1$。

| 六轴速率 | 边权环 | $C_1$ | $C_2$ |
|---|---|---:|---:|
| $(1,1,1,2,2,2)$ | $1\to2\to3\to1$ | $0$ | $1/4$ |
| $(1,1,1,2,2,2)$ | $1\to4\to2\to5\to1$ | $0$ | $14/45$ |
| $(1,1,2,3,4,5)$ | $1\to2\to3\to1$ | $1/90$ | $43/180$ |
| $(1,2,3,4,5,6)$ | $1\to2\to3\to1$ | $263/12600$ | $5767/25200$ |

第三行在 $N=1$ 时完整方差恰为 $1/4$，与第一行相同；唯有分开 $1/N$ 与 $1/N^2$ 两项或增加库存，才可辨别首项已恢复。全等率时 $K_a(a,a)=r(a,a)=1/12$，公式回到已知逐轴净流平方和。

## 3. 接近等率时，首项以哪一阶恢复

取一条明确的线性分裂 $a_j(\varepsilon)=b_g+\varepsilon h_j$（$j\in G_g$），$\varepsilon$ 充分小以保持各率为正。固定原来满足抵消条件的 $\lambda$ 与正库存比例。写
$$
 M^{(k)}_{ig}=\sum_{j\in G_g}\lambda_{ij}h_j^k .
$$
若 $d\ge1$ 是某个 $M^{(d)}_{ig}\ne0$ 的最小阶，则
$$
 C_1(\varepsilon)=c_{2d}\varepsilon^{2d}+O(|\varepsilon|^{2d+1}),\qquad
 c_{2d}=\sum_i\frac{1}{w_i(d!)^2}
 \operatorname{Var}_{T\sim\operatorname{Exp}(a_i(0))}
       \left(T^d\sum_g M^{(d)}_{ig}e^{-b_gT}\right)>0 .
$$
逐组展开 $e^{-(b_g+\varepsilon h_j)T}$ 即得；前 $d-1$ 阶逐项为零。余项受多项式乘衰减指数控制，时钟密度同时随速率变化只影响下一阶。首个非零组合在无穷远趋零，又不能恒零，所以至少一个方差严格为正。若第 $g$ 组内有 $s_g$ 种不同斜率，则要求从 $0$ 至 $k$ 阶矩都为零的核维数为
$$
 \binom{6-\sum_g\min(s_g,k+1)}{2}.
$$
理由是各组的指示向量乘 $1,h,\ldots,h^k$ 分别给出秩 $\min(s_g,k+1)$ 的 Vandermonde 块。若所有这些组内矩最终仍为零，则 $\lambda$ 已逐一湮灭分裂后每个等率组，首项在这一线性分裂上继续精确为零。

**八次方例。** 令 $a_j=1+\varepsilon(j-1), w_j=1$，取
$$
 u=(1,-4,6,-4,1,0),\quad v=(0,1,-4,6,-4,1),\quad
 \lambda=uv^\mathsf T-vu^\mathsf T .
$$
两个四阶差分向量都消去 $1,h,h^2,h^3$，对 $h^4$ 的内积均为 24。于是 $\lambda h^4=24(u-v)$，$\|u-v\|^2=252$，从而
$$
 C_1(\varepsilon)=252\!\left(\frac{8!}{3^9}-\frac9{16}\right)\varepsilon^8
 +O(|\varepsilon|^9)
 =\frac{363979}{972}\varepsilon^8+O(|\varepsilon|^9),\qquad C_2(0)=147 .
$$
六种互异斜率从单一重率分开时，非零固定 $\lambda$ 首次恢复的阶数 $2d$ 最高为八；再要求四阶矩也消失，剩余正交补仅一维，没有非零反对称矩阵。一般的首次恢复阶数 $2d$ 对应两项方差的交界尺度 $|\varepsilon|\asymp N^{-1/(2d)}$。例中是 $N^{-1/8}$。这一尺度比较仅涉及方差，未使用等率分布极限来推算不等率分布。

## 复算

同目录运行 $\texttt{python circulation_check.py}$，仅需 Python 标准库。程序按剩余名字的总权逐步递推条件一阶、二阶矩，独立核对表中单库存与双库存、非等库存及正有理速率的均值和方差。另以有理数消元核对六轴全部 11 个组大小分拆，以有理幂级数除法直接从 $K_a$ 的精确表达式恢复八阶系数。指数键只给出已声明分支概率的表示；本次没有引入物理时钟参数。[复算程序](circulation_check.py) · [原有 X6 有序步重数](https://github.com/awdawmip/enterprise-math/blob/c4d450536bf71ed87fd74555295ec60485262f0a/experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py)
