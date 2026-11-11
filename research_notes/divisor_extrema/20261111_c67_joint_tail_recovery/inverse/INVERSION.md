# 原三尾标量的逆像与高规模最大读数

本节固定 C62 的库存、两条历史、三尾及正概率选择。令间隙为 $(b_0,\ldots,b_k)$。首块 $5^{b_0}23$ 后的两个标量端点是 $0,1$，剩余 $r=k-1,c=k+1-b_0$。每次取 $0\le m\le c-2$ 个 5 再执行 23，状态变为 $(r-1,c-m)$，输入映射为 $F(u)=a/[a+h+(b-h)u]$，其中 $a,b,h$ 是 C64 的正整数块系数。末隙取 $c-2$。本文的 $H$ 始终是 C62 标量，亦即原来三个完整尾概率之跨历史比的极差比。

## 一致规模截止

对内部块令 $\rho=b/h$。C62 的 $4^{-m}\le\rho\le4$ 与 Hilbert 坐标的最大收缩系数 $\kappa=|\sqrt\rho-1|/(\sqrt\rho+1)$ 给出
$$
\kappa\le \frac13(3/\sqrt5)^m.
$$
确实 $m=0,1$ 时 $\kappa\le1/3$，$m=2$ 时 $\kappa\le3/5$，$m=3$ 时 $\kappa\le7/9<9/(5\sqrt5)$，$m\ge4$ 时右侧至少 1。令 $m$ 是首个内部块的 5 数，其输出 Hilbert 跨度为 $|\ln\rho|\le\ln4\max(1,m)$。其余 $k-2$ 次收缩总共消耗至多 $k-1-m$ 个 5。末次正对角更新保持跨度，三尾似然的正线性映射使 $\ln H$ 至多等于输入 Hilbert 跨度。由于 $\max_{m\ge0}\max(1,m)(\sqrt5/3)^m=3(\sqrt5/3)^3$（相邻项比为 $(m+1)\sqrt5/(3m)$），得到
$$
\ln H\le \frac{25\ln4}{3} 5^{-k/2}<12\,5^{-k/2}.
$$
故产生 $H=p/q>1$ 的规模必满足 $5^k(p-q)^2<144p^2$。直接枚举到这个截止的候选数为 $O((12p/(p-q))^{\log_5 16})$；这里用每个规模的词数至多 $4^k$ 并累加等比级数。

## 端点偏序与精确最大值

固定后缀和末尾库存。择三尾中极端的两列且定向，使 $R=P/Q$ 在 $[0,1]$ 递增，$P,Q$ 是正仿射函数，允许分别乘正常数。各列斜率除以截距可给出其确定顺序，因为交叉行列式的符号与输入无关。任意 $x<y$ 有 $H_s(x,y)=R(y)/R(x)$ 和 $\ln H_s(x,y)=\int_x^y f_s(u)\,du$，其中
$$
f_s=\frac{D}{PQ},\qquad D=P'Q-PQ'>0.
$$
比较 $s,t$ 的 $f$，设 $\lambda_i=P_i'/P_i,\mu_i=Q_i'/Q_i$。若分子成比例，则差为 $\mu_t-\mu_s$，符号恒定。否则 $\lambda_s-\lambda_t$ 符号严格恒定。在 $f_s=f_t$ 之处，由 $\lambda_i'=-\lambda_i^2$ 和对 $\mu_i$ 的相同公式可得 $(f_s-f_t)'=-2f_s(\lambda_s-\lambda_t)$。于是每个零点都简单且穿越方向相同，故至多一个。特别地，两端均有 $f_s\ge f_t$ 时整个闭区间都如此，且除非曲线相同，任何正长度的积分比较都严格。两端同时相等强制曲线相同，其归一化赔率也相同。此为 C65 单交点引理在最大值递推中的用法。

给两列分别用互质正整数 $(P(0),P(1)),(Q(0),Q(1))$ 表示。若子列端值为 $(z_0,z_1)$，在边 $(a,b,h)$ 前接后变为 $(h z_0+a z_1,b z_0+a z_1)$，再约分定向。父导数是 $|F'| f_{\rm child}(F)$。所以清除一个在两端被支配且非同一的子候选，任何共同前缀都无法把它变成最大者；等价曲线合并并累积词数。每个库存格枚举所有首间隙和保留的子候选，按 $(f(0),f(1))$ 清除被支配项。该算法对每个正长度输入区间保留全部可能最大者，可对任何有限 $k$ 执行。最坏前沿大小未作先验假设。

对 $2\le k\le64$，构造 348,523 个候选曲线，每格最多留 8 条，每个规模的最大者均严格唯一。$2\le k\le10$ 的 125,475 个安排另逐词作全分数对照，验证全部最大者及其数值。$17\le k\le64$ 的最大者在 $k=17$，间隙向量为
$$
(0,2,2,2,2,0,2,0,2,0,2,0,0,0,0,0,0,0).
$$
记其准确值为 $M$，有 $2.67903976677\times10^{-18}<M-1<2.67903976678\times10^{-18}$。准确分数在 upper_frontier.json 的 $k=17$ 行。对 $k\ge65$，$144<5^{65}(1-1/M)^2$，由规模截止可知 $H<M$。因此 $M$ 是所有 $k\ge17$ 的严格唯一最大值。

## 高于阈值的全规模单原像

C66 的精确模筛与有理回查已给出 $2\le k\le16$ 的 405,187,824 个 $H$ 两两互异。故这些范围中任何 $H>M$ 的安排，在全部 $k\ge2$ 有唯一原像。threshold_count.py 对 $k\le10$ 逐词比较有理数，直接得到 119,538 个。singleton_count.py 用纯整数误差界筛全范围，得到至少 2,927,017 个。其整数判据如下。

把 $[0,1]$ 分成 64 格；每个前缀以两个向外取整的网格端点包住两历史的像。由 $F'=\pm a|b-h|/[a+h+(b-h)u]^2$，可在该区间一端精确得到最小绝对导数，并给整个输入跨度乘上这一下界。子区间由 $F$ 对两网格端点的像向外取整得到。末尾在区间上用 $D/(\max P\max Q)$ 下界 $f$。上述各因子 $t$ 均为正有理数；逐项把 $32\log_2 t$ 向下取整，求和 $s$。若 $s\ge\lfloor32\log_2(M-1)\rfloor+1$，必有 $H-1\ge\ln H>M-1$。向下取整通过整数 32 次幂和位长比较完成。以 $(r,c,\text{左右格点},s)$ 为键记忆化，枚举所有合法下一间隙，准确计出满足充分条件的词数。

census_threshold.py 与 census_threshold.cpp 给出严格误差保护的全量阈值比较。用齐次坐标 $(u,1-u)$，在每个内部块两端点同时左乘 $T=\left(\begin{smallmatrix}a&a\\ b&h\end{smallmatrix}\right)$，必要时交换端点使 $x<y$。令端点齐次向量为 $X,Y$，末尾 $R=P/Q$ 递增，则
$$
 H-1=\frac{D\prod_e|\det T_e|}{P(X)Q(Y)},\qquad D=P(1)Q(0)-P(0)Q(1)>0 .
$$
行列式在转为数值前用有理数算出。矩阵除以最大系数，各个尾列除以最大端值，不改变上述等式。此后递推的所有运算是非负数的加法与乘法。binary64 系数和四则舍入，每次相对误差至多 $\varepsilon=2^{-52}$；程序检查输入舍入、对所有可能库存路由给出 $2^{-990}$ 的正中间值下界，且上界小于 $2^{990}$。从两个始端的 $0,1$ 出发，每步齐次坐标的相对误差因子在 $(1\pm\varepsilon)^3$ 之内。两个尾部内积每个再用三次，乘以阈值与比较保护因子合计，指数对 $k\le16$ 小于 200。因 $(1+\varepsilon)^{200}/(1-\varepsilon)^{200}<1+2^{-39}$，判别用保护带 $1\pm2^{-38}$ 可严格覆盖误差；带内标作未决。编译禁用快速数学和浮点乘加收缩。程序核对全范围各规模计数，并逐规模与 $k\le10$ 的直接有理数结果对照。保护带内词数及准确的阈值两侧计数见 census_threshold.json。

## 小规模完整覆盖的整数筛

令 $h_*$ 为 $2\le k\le8$ 全部标量中最小值，$\tau=1-1/h_*$。考虑任一后缀，置 $w=f^{-1/2}=\sqrt{PQ/D}$。正仿射两列的几何平均是凹函数（可直接平方求二阶导数），且在前接边时
$$
 w_{es}(u)=\frac{a+h+(b-h)u}{\sqrt{a|b-h|}}w_s(F(u)).
$$
在网格 $u_i=i/n$、$n=8$、$S=2^{80}$ 上，构造库存格的整数下界 $L_i\le S w_s(u_i)$，网格点间采用弦线。终点直接向下取整。对子节点下界，在父节点 $u_i$ 处置 $E=na+(n-i)h+ib$，$j,z=\operatorname{divmod}(n^2a,E)$。父边节点的下界为
$$
 V_{ei}=\left\lfloor\sqrt{\frac{((E-z)L_{j}+zL_{j+1})^2}{n^2 a|b-h|}}\right\rfloor,\qquad L_i^{\rm parent}=\min_e V_{ei}.
$$
因 $w$ 凹，子格弦线给出的下界对每个后缀均成立。定义 $\gamma_e=\min_i V_{ei}/L_i^{\rm parent}\ge1$，再令 $d_e=\lfloor16\log_2\gamma_e^2\rfloor$。沿路径归纳，真实 $S w$ 在父格网点至少是全路径的 $\prod\gamma_e$ 乘父网点整数，进而在网格间也由此倍数的弦线下界。故对指定首库存以及某一路径，
$$
 \ln H\le 2^{-\sum_e d_e/16}\,U,
 \qquad U=\sum_{i=0}^{n-1}\frac{S^2}{nL_iL_{i+1}}.
$$
右式来自 $1/\text{弦线}^2$ 的准确积分。若 $H\ge h_*$，则 $\sum d_e\le\lfloor16\log_2(U/\tau)\rfloor$。上述递推全用整数平方根与有理数。$k\ge67$ 已由一致规模界排除，在 $17\le k\le66$ 间只有 $17,18,19,20,21$ 的某些首隙通过上界。五个规模总共 361,429,204,290 个安排，整数预算与后缀最小成本筛后余 9,826,097,651 个末叶；对每个保留末叶在 $p=2^{61}-1$ 上计算定向原三尾 $H$，程序断言所有分母可逆。与 8,787 个目标的模值无一相同。相同有理数必有相同的良定义模值，故这五层完全排除；$2\le k\le16$ 区间用 C66 跨规模证书。独立参考回放 $k=6$ 的 462 个词全部命中各自目标库。

综合起来，$k=2,\ldots,16$ 中 **3,658,803** 个读数严格大于 $M$，阈值两侧比较没有未决项。$k\le8$ 的 8,787 个都已全局唯一，其中恰有 30 个落于 $M$ 以下。$M$ 自身有唯一的 $k=17$ 原像。三部分互不重复，共得到至少 **3,658,834** 个原始标量 $H$ 的全规模单原像。这里的下界未假设全体读数单射。

### 复算

以下命令从 C67 目录执行。把 MODEL 改成相邻 C64 证据目录；需要 Python 3 与 g++（支持 ISO C++17 和 128 位无符号扩展）。grid 的全量模筛会执行近百亿次末叶比较。

~~~bash
MODEL=../C64
python inverse/upper_frontier.py --checks "$MODEL/checks" --inherited "$MODEL/inherited" --output /tmp/c67-frontier.json
python inverse/threshold_count.py --checks "$MODEL/checks" --inherited "$MODEL/inherited" --frontier /tmp/c67-frontier.json --output /tmp/c67-direct.json
python inverse/singleton_count.py --checks "$MODEL/checks" --inherited "$MODEL/inherited" --frontier /tmp/c67-frontier.json --output /tmp/c67-lower.json
python inverse/census_threshold.py --checks "$MODEL/checks" --inherited "$MODEL/inherited" --frontier /tmp/c67-frontier.json --direct /tmp/c67-direct.json --output /tmp/c67-threshold.json
python inverse/inverse_grid.py --checks "$MODEL/checks" --inherited "$MODEL/inherited" --output /tmp/c67-grid.json
cmp /tmp/c67-frontier.json inverse/upper_frontier.json
cmp /tmp/c67-direct.json inverse/threshold_count.json
cmp /tmp/c67-lower.json inverse/singleton_count.json
cmp /tmp/c67-threshold.json inverse/census_threshold.json
cmp /tmp/c67-grid.json inverse/inverse_grid.json
~~~
