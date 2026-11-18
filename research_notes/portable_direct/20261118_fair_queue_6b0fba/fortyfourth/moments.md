# 相关 Beta 矩的 Hankel 行列式与 Laguerre 谱

取整数 $m\ge1$，实数 $r>-1/m$，并将辅助矩定义为
$$
D_u(r)=\int_0^1t^{mr}(1-t)^{m-1}(1-t^m)^u\,dt,\qquad u>-m .
$$
两个开不等式分别正是两端的可积条件。本文求任意固定阶 $n$ 的矩阵 $M_s=(D_{s+i+j})_{0\le i,j<n}$、其行列式 $H_{n,s}$，以及矩阵对 $(M_{s+1},M_s)$ 的谱。允许实数 $s>-m$。数值复算中的有限正项展开使用整数 $s\ge0$。

公开的 $m=7$ 补遗已给出 $j=0,\ldots,6$ 各矩的共同归一与 $49/r$ 误差；原作者再以七个带符号系数组合这些矩，随后独立评审给出了原标量的大参数范围。这里取辅助积分本身为研究对象，所有阶数均可选，矩阵及其谱不读取原标量的系数、分支或原生运行结果。既有 Wallis 工作求的是给定有限矩时其它函数积分的极值，Bernstein/Simpson 型区间工作控制的是特定求积或多项式证书，本题求固定已知测度的 Hankel 谱。下述经典行列式积分、Selberg 公式和 Laguerre 恒等式按既有工具使用。[补遗原文](https://github.com/awdawmip/enterprise-math/blob/22338e996c7908348438efb449dcf5d8f700a0f7/research_notes/owner_goal_20261016/cm24_convergence_new_anchor/parity_m7/PARITY_M7_ACTUAL_TRACE_POSITIVE_INTERVAL_ADDENDUM.md) · [既有独立评审](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_notes/owner_goal_20261016/p11_independent_native_driver/parity_m7_review/PARITY_M7_COMBINED_INTERVAL_AND_ACTUAL_TRACE_INDEPENDENT_REVIEW.md)

## 一　全部参数上的正性与精确界

记 $x=1-t^m$、$a=m+s>0$、$b=r+1/m>0$，并令 $F(x)=m[1-(1-x)^{1/m}]/x$，在零点连续取 1。矩阵为单项式 $1,x,\dots,x^{n-1}$ 在正测度
$$
d\mu_s(x)=m^{-m} x^{a-1}(1-x)^{b-1}F(x)^{m-1}\,dx
$$
下的 Gram 矩阵。故 $M_s$ 严格正定。经典 Heine–Andréief 公式将行列式写成 $\frac1{n!}\int\prod_i d\mu_s(x_i)\prod_{i<j}(x_i-x_j)^2$，由展开两个 Vandermonde 行列式、按排列对称性积分即可证明。回到 $t_i$ 变量后，对 $r$ 求 $k$ 次导数只乘以 $(m\sum\log t_i)^k$；在允许区间的紧集上这些对数幂可积，因而 $(-1)^k H_{n,s}^{(k)}(r)>0$，包括 $k=0$。[Andréief 与正矩阵](https://math.iisc.ac.in/~khare/teaching/Math341-notes.pdf)

定义
$$
J_n(a,b)=\prod_{j=0}^{n-1}
\frac{j!\,\Gamma(a+j)\Gamma(b+j)}{\Gamma(a+b+n+j-1)}.
$$
这是 Jacobi 权 $x^{a-1}(1-x)^{b-1}$ 的 Gram 行列式，由 Selberg 积分的指数 1 情形或 Jacobi 首一正交多项式的范数乘积得到。$1\le F\le m$ 给出严格正的可计算下界和上界
$$
m^{-mn}J_n(a,b)\le H_{n,s}(r)\le m^{-n}J_n(a,b).
$$
$m=1$ 两者完全相同，这时 $D_u=B(r+1,u+1)$。$m>1$ 时两边严格，且下界与真实行列式在 $r\to\infty$ 下有相同首项。[Selberg 积分](https://dlmf.nist.gov/5.14) · [Jacobi 与 Laguerre 权及范数](https://dlmf.nist.gov/18.3)

**无消去的有限算法。** 当 $s$ 为非负整数，在 Heine 积分中取 $0<t_1<\cdots<t_n<1$，此时无需 $1/n!$。写 $t_i=z_i\cdots z_n$，Jacobian 是 $\prod_{k=1}^n z_k^{k-1}$。每个 $t_j^m-t_i^m$（$i<j$）成为 $t_j^m[1-(z_i\cdots z_{j-1})^m]$。分解 $1-t_i$ 与 $1-t_i^m$ 同理。每个因子 $1-\prod_{k=h}^{j}z_k^d$ 有有限正展开
$$
\sum_{0\le e_k\le d,\ (e_h,\ldots,e_j)\ne(d,\ldots,d)}
\prod_{k=h}^j {d\choose e_k}z_k^{e_k}(1-z_k)^{d-e_k}.
$$
所以整个有序积分等于非负系数乘一维 Beta 积分乘积的有限和，无需行列式相减。当 $r$ 有理时各项均有理：每个 Beta 积分第二个参数为正整数。算法适用于 $-1/m<r<0$，项数随阶数增长；此处没有计算复杂度改进的主张。独立对照可以对每个 $D_j$ 用
$$
\sum_{k=0}^j(-1)^k{j\choose k}B(m(r+k)+1,m)
$$
再组装行列式。脚本还单独核对正项单矩公式，即以 $(1+\cdots+t^{m-1})^j$ 的系数对 $B(mr+k+1,m+j)$ 求和。

## 二　固定维数的行列式和普通特征值

令 $N=n(n+a-1)$、$\beta=(m^2-1)/(2m)$。则固定 $m,n,s$，$r\to+\infty$ 时
$$
H_{n,s}=\frac{\prod_{j<n,\,j\ge0} j!\Gamma(a+j)}{m^{mn}r^N}
\left[1+\frac{h_n}{r}+O(r^{-2})\right],\qquad
h_n=-\frac{N}{2}\left(2n+s-1+\frac1m\right).
$$

先写 $y=rx$。去掉公因子 $m^{-m}r^{-a}$ 后，测度对 $y$ 的密度在有限阶矩意义下为
$$
y^{a-1}e^{-y}\left[1+\frac{v(y)}r\right],\qquad v(y)=\beta y-y^2/2 .
$$
控制余项的方法如下。$G(x)=(1-x)^{1/m-1}F(x)^{m-1}$ 在 $[0,1/2]$ 上二阶导有界，$G=1+\beta x+O(x^2)$。在 $y\le r/2$ 上，$r\log(1-y/r)=-y-y^2/(2r)-R$ 且 $0\le R\le2y^3/(3r^2)$。由 $|e^{-u-v}-(1-u)|\le u^2/2+v$（$u,v\ge0$），括号误差乘 $e^{-y}$ 后绝对值至多 $C_m e^{-y}(y^2+y^3+y^4)/r^2$。在 $r/2<y<r$，原密度除去 $y^{a-1}$ 后至多 $m^{m-1}2^{1-r}$（$r\ge2$），扩展的指数密度尾也是指数小。因此每个预先给定次数的多项式积分均可带 $O(r^{-2})$ 替换。固定 $m,n$，在 $s$ 的任意紧子集 $(-m,\infty)$ 中常数可统一，未取 $n$ 随 $r$ 增长的极限。

多项式 $P_k(y)=(-1)^kk!L_k^{(a-1)}(y)$ 是首一 Laguerre，范数平方 $k!\Gamma(a+k)$，递推为 $yP_k=P_{k+1}+A_kP_k+B_kP_{k-1}$，其中 $A_k=2k+a$、$B_k=k(k+a-1)$。在正交基上，行列式的一阶对数修正是 $\sum_{k<n}\langle vP_k,P_k\rangle/\|P_k\|^2$。对 $y$ 和 $y^2$ 分别求和得到 $\sum A_k=N$ 与 $\sum(A_k^2+B_k+B_{k+1})=N(2n+a-1)$，即上式 $h_n$。变量缩放在第 $i,j$ 元另给 $r^{-i-j}$，从而总幂恰为 $N$。[Laguerre 递推与导数](https://dlmf.nist.gov/18.9)

若读数是 $M_s$ 本身的普通特征值，按降序记 $\lambda_1\ge\cdots\ge\lambda_n$。定义 $h_0=0$，则
$$
\lambda_k=\frac{(k-1)!\,\Gamma(a+k-1)}{m^m r^{a+2(k-1)}}
\left[1+\frac{h_k-h_{k-1}}r+O(r^{-2})\right].
$$
确实，第 $k$ 个基本对称函数是全部 $k$ 阶主子式之和。任取主指标 $I$，其首项幂为 $r^{-ka-2\sum_{i\in I}i}$，极限 Gram 系数严格正。除 $I=\{0,\ldots,k-1\}$ 外其余至少再小 $r^{-2}$。基本对称函数与前 $k$ 大特征值乘积之比在 $[1,{n\choose k}]$ 内，这先给逐个特征值的幂次，故相邻特征值比为 $O(r^{-2})$。再代回基本对称函数，其与前 $k$ 大特征值乘积的相对误差仅 $O(r^{-2})$。相邻阶之比给出公式。

## 三　广义谱、全域比较和尖锐二阶差距

把广义特征值按升序记为 $\theta_k$。它们是测度 $d\mu_s$ 的 $n$ 阶 Gauss 节点，均单且在 $(0,1)$。确实，$M_{s+1}v=\theta M_sv$ 等价于 $(x-\theta)p_v(x)$ 与所有次数小于 $n$ 的多项式正交；由正测度的标准零点定理即得。设 $\ell_k$ 是 $L_n^{(a-1)}$ 的相应零点，则
$$
r\theta_k=\ell_k-\frac{\ell_k(\ell_k+2n+s+1/m)}{2r}+O(r^{-2}).
$$

由上一节的统一矩展开及 Gram 可逆，缩放的首一正交多项式为 $P_n+r^{-1}Q_n+O(r^{-2})$（逐系数）。一阶正交关系给
$Q_n=-\sum_{j<n}\langle vP_n,P_j\rangle P_j/\|P_j\|^2$。
递推后仅剩 $B_n(2n+a-1-\beta)P_{n-1}+B_n B_{n-1}P_{n-2}/2$，次数不存在的项取零。在根处用 $\ell P_n'(\ell)=B_nP_{n-1}(\ell)$ 及 $P_n$ 的递推，根的修正 $-Q_n(\ell)/P_n'(\ell)$ 即为所示。固定 $n$ 时，Laguerre 相邻简单根在 $a$ 的正紧集上保持分离，所以 $O(r^{-2})$ 对该集统一。[正交多项式零点](https://dlmf.nist.gov/18.2#vi) · [Gauss 节点](https://dlmf.nist.gov/3.5#v)

**全域单调。** 对任意光滑权参数 $\tau$，归一广义特征向量所定义的概率测度 $d\sigma=p_v(x)^2d\mu_s/\int p_v^2d\mu_s$ 满足
$$
\partial_\tau\theta=\mathrm{Cov}_{\sigma}(x,\partial_\tau\log w(x)).
$$
这是简单对称广义特征值的 Hellmann–Feynman 微分式，直接微分矩阵方程并左乘 $v^T$ 即可。故所有节点对 $r$ 严格递减，对 $s$ 严格递增，因为 $\log(1-x)$ 严减、$\log x$ 严增；对严格单调函数协方差的符号由两个独立样本的差乘积得到。这也是正交多项式零点 Markov 单调性的一个证明。[零点的参数单调性](https://dlmf.nist.gov/18.2#xii) · [Feynman 的特征值微分式](https://doi.org/10.1103/PhysRev.56.340)

令 $j_k(a,b)$ 为 $(0,1)$ 上 Jacobi 权 $x^{a-1}(1-x)^{b-1}$ 的第 $k$ 个节点，$d=(m-1)^2/(2m)$。对于 $m>1$ 有
$$
j_k(a,b)<\theta_k,\qquad
\theta_k<j_k(a,b-d)\quad(b>d).
$$
证明写 $F=m/(1+t+\cdots+t^{m-1})$。则
$$
(1-x)(\log F)'=\frac{\sum_{k=0}^{m-1}k t^k}{m\sum_{k=0}^{m-1}t^k}.
$$
作为 $t$ 的函数，右边对 $\log t$ 的导数是该有限分布的方差除 $m$。故数值从 0 严增至 $(m-1)/(2m)$。相对下界权的密度比 $F^{m-1}$ 严增，相对上界权的密度比 $(1-x)^d F^{m-1}$ 严减；在两权间取密度比的实幂插值，用协方差式即得。端点 0 和 $d$ 是这种全区间单调密度比方法的锐指数。上界权只有 $b>d$ 时可归一。

**上界与真节点的首个非零差。** 固定 $m>1,n,s$，有
$$
r^3\big[j_k(a,b-d)-\theta_k\big]\longrightarrow
\frac{(m-1)(m^2-1)}{24m^2}\,\ell_k(\ell_k+2n+a).
$$
在 $x=0$，相对上界权的密度比 $R=(1-x)^dF^{m-1}$ 满足
$R=1-cx^2/2+O(x^3)$，其中 $c=(m-1)(m^2-1)/(12m^2)$；此处用到均匀 $0,\ldots,m-1$ 的方差 $(m^2-1)/12$。上界权和真实权有相同的 $r^{-1}$ 扰动，比较时首个差为 Laguerre 极限权乘 $-cy^2/(2r^2)$。上式的紧区间 Taylor 余项与指数尾控制在这里同样有效：$[0,1/2]$ 上 $R$ 三阶导有界，$x>1/2$ 时两权均有指数小的可积尾。对首一正交多项式的系数作为有限矩的光滑函数取差，只需计算上述一次线性化。在前一根修正中只保留 $-cy^2/2$，结果为 $-c\ell_k(\ell_k+2n+a)/2$。这也证明上界在 $r\theta$ 尺度上精确到一阶，却有严格的二阶差距。

## 四　可复算样例

标准库脚本核对 200 组单矩正和与交错差分；另对四组完整行列式，直接计算有序积分的全正项 Beta 和，再与独立生成的精确有理行列式比较。包含 $m=7,s=1,n=2,r=2/3$ 的 492 项证书，以及 $m=1$ 时 60 组 Jacobi–Selberg 精确式。谱检查用有理矩解首一正交多项式，用 Sturm 变号计数隔离每个根；二分 72 次后才舍入展示，覆盖原权及两个 Jacobi 权。[复算程序](moments_check.py) · [归档结果](moments_checked.json)

例如 $m=7,s=1,n=3$ 的 Laguerre 节点约为 $(4.892750458,9.322989913,15.784259629)$。在 $r=2048$，$r\theta$ 约为 $(4.878413768,9.285649576,15.696337370)$。此时 $r^3(j_k-\theta_k)$ 约为 $(22.4662,52.7330,113.6548)$，所证极限分别为 $(22.6378,53.2506,115.1320)$，其中 $j_k$ 采用上界参数 $b-d$。运行 `python3 moments_check.py` 即可复算。本轮没有调用持有人所约束的原生 $[7,8]$ 程序，没有计算原迹、其符号或其分支权重。
