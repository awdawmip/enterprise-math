# 素因子替换图的近一次谱矩与特征向量的团间读数

固定 $k\ge2$。顶点是整数 $n\le X$ 且 $\Omega(n)=k$，重素因子计重。不同顶点间连一条无向边，当且仅当 $\Omega(\gcd(n,m))=k-1$。令 $A$ 为邻接矩阵，$V$ 为顶点数，$P=\pi(X)$。第 51 轮已证明：将 $\Omega(g)=k-1$ 的整数按大小排序，对应排序的大特征值能逐一读回 $\pi(X/g)$，并已求出其二阶偏移的常数。本篇给出两项延伸。一是让绝对谱矩的阶数随 $X$ 向 1 移动，确定正负两部分的极限；二是在原特征值偏移基础上，求特征向量对相邻公共因子及团外顶点的显式响应。这是独立的数值窗口算术。原任务的前缀 Hamilton 路问题在同轮另一篇计入登记。[第 51 轮的谱定位、偏移常数及负谱重数](../fiftyfirst/multiplicative.md) · [第 111 轮的前缀和边长](adjacency.md)

## 从固定谱矩到两种临界尺度

**定理一。** 给定任意 $s=s_X>0,\ s\to0$。设下列极限存在，容许无穷，记 $e^{-\infty}=0$：
$$
 \tau=\lim s\log X,\qquad
 \alpha=\lim\min\!\left(1,\frac{\log(1/s)}{\log\log X}\right).
$$
设 $\lambda$ 遍历 $A$ 的特征值并计重数。则
$$
 \boxed{\displaystyle
 \frac{P}{V}\sum_\lambda |\lambda/P|^{1+s}
 \longrightarrow \alpha^{k-1}+(2k-1)e^{-\tau}.}                     \tag{1}
$$
其中正谱贡献 $\alpha^{k-1}+(k-1)e^{-\tau}$，负谱贡献 $k e^{-\tau}$。当 $s=(\log X)^{-u}$、$0<u<1$ 时，总极限为 $u^{k-1}$；当 $s=t/\log X$、$t>0$ 固定时，它是 $1+(2k-1)e^{-t}$。恰在一次矩 $s=0$ 时，归一化极限是 $2k$。这些过渡无法由某个固定二次矩的极限直接推出。

令 $C_g=\{gp:p\text{ 素},gp\le X\}$，$d_g=|C_g|$。关联矩阵 $R_{ng}=1_{n\in C_g}$ 的列数 $K=\#\{g\le X/2:\Omega(g)=k-1\}$。两点相邻时公共列是它们的 gcd；不同两列的交点若存在，只可能是最小公倍数。因此
$$
 A=RR^{\mathsf T}-D,\quad D_{nn}=\omega(n),\qquad
 R^{\mathsf T}R=\operatorname{diag}(d_g)+E,\quad
 \|E\|_{\rm HS}^2=\sum_n\omega(n)(\omega(n)-1)\le k(k-1)V .           \tag{2}
$$
Landau 定理给出 $V\sim P(\log\log X)^{k-1}/(k-1)!$、$K=o(V)$。平方自由的 $k$ 个素因子乘积已占同一主项。于是 $A+kI=RR^{\mathsf T}+(kI-D)$ 是半正定的，秩至多是 $K$ 加非平方自由顶点数，即 $o(V)$。因此 $V-o(V)$ 个特征值恰为 $-k$，其余负值的模至多为 $k$。在 (1) 的归一化下，它们合计趋于 $k e^{-\tau}$。$s=0$ 时用 $\operatorname{Tr} A=0$ 可直接得到全谱的 $2k$。[几乎素数计数与素数定理](https://doi.org/10.1090/gsm/163)

为控制正谱，把正特征值按序、不足时补零。$A$ 的正特征值至多 $K$ 个。移去 $D$ 对其与 $RR^{\mathsf T}$ 的对应非负特征值的绝对差和贡献至多 $kK$，因为 $0\le D\le kI$。对另一侧 Gram 矩阵，Hermitian 矩阵的 Hoffman–Wielandt 不等式与 Cauchy 不等式给出排序谱对角线 $d_g$ 的绝对差和至多 $\sqrt K\|E\|_{\rm HS}$。两种 Gram 矩阵的非零谱相同。故
$$
        \sum_j|\lambda_j^+(A)-d_{g_j}|=o(V).                        \tag{3}
$$
所有归一化特征值至多为 $k$，可由最大度数界得出。$x^{1+s}$ 在 $[0,k]$ 上有统一的 Lipschitz 常数（$0<s\le1$），所以 (3) 允许在 (1) 的正谱部分用 $d_g$ 代替 $\lambda_j^+$。[经典矩阵不等式与图谱背景](https://doi.org/10.1007/978-1-4614-1939-6)

将得到的和按关联关系翻转：
$$
 \frac1V\sum_g d_g(d_g/P)^s
   =\frac1V\sum_{\Omega(n)=k,\,n\le X}\ \sum_{p\mid n}
               (d_{n/p}/P)^s .                                      \tag{4}
$$
均匀选一个顶点，令 $G=n/P^+(n)$，即删掉最大素因子后的公共因子。对每个 $0<u<1$，
$$
 \mathbb P\{\log\log G\le u\log\log X\}\longrightarrow u^{k-1}.
                                                                    \tag{5}
$$
确实，取 $Y=\exp((\log X)^u)$。对 $g\le Y,\ \Omega(g)=k-1$，适合的最大素因子在 $[P^+(g),X/g]$，故计数等于 $\sum_g(\pi(X/g)-\pi(P^+(g))+1)$。扣除项共 $O(Y^2)=o(V)$；素数定理在该范围一致给出 $\pi(X/g)\sim P/g$。而
$\sum_{g\le Y,\Omega(g)=k-1}1/g\sim(\log\log Y)^{k-1}/(k-1)!$，可由所有素因子分别截在 $Y^{1/(k-1)}$ 和 $Y$ 的两端夹逼，并用 Mertens 素数倒数和；重素因子的贡献为低阶。与 $V$ 相除即得 (5)。

全窗 $G\le X^{1-1/k}$，素数定理的两侧界给 $\log(P/d_G)=\log G+O_k(1)$。在 (5) 中用两个固定指数夹住 $\alpha$：对指数比 $\alpha$ 小一固定量的 $G$，$s\log G\to0$；对比它大一固定量的 $G$，$s\log G\to\infty$。结合 $0\le(d_G/P)^s\le1$，再令夹逼间隔缩小得 (4) 中删去最大因子的贡献 $\alpha^{k-1}$，端点只需单侧夹逼。由 (5)，$G=X^{o(1)}$ 依概率成立；由 Landau，$\log n/\log X\to1$ 依概率成立。因而删去任意另一个素因子 $p$ 时，$\log(n/p)/\log X\to1$，$\log(P/d_{n/p})/\log X\to1$。最后一式由 $1\le d_{n/p}\le X/(n/p)$ 即得。各项的 $s$ 次幂遂依概率趋于 $e^{-\tau}$，有界性允许取均值。平方自由性以概率趋于 1，故这类项的总贡献是 $(k-1)e^{-\tau}$。

**固定阶的补充。** 对每个固定 $a>1$，$A/P$ 的排序正谱在 $\ell^a$ 收敛到 $(1/g_j)_j$，负谱绝对值的 $\ell^a$ 范数趋零。对 $1<a<2$，将 (2) 的排序谱 $\ell^2$ 误差 $O_k(\sqrt X/P)$ 乘以维数因子 $O(X^{1/a-1/2})$ 即为 $o(1)$；对 $a\ge2$ 直接用 $\ell^2$。固定 $g$ 有 $d_g/P\to1/g$。$g\le\sqrt X$ 时比值 $\ll1/g$；更大 $g$ 的 $a$ 次幂尾和至多 $O((\log X)^a\sum_{g>\sqrt X}g^{-a})=o(1)$。从而
$$
 \lim P^{-a}\operatorname{Tr}|A|^a=[z^{k-1}]\prod_p(1-zp^{-a})^{-1}.
$$

## 特征向量在别的团上留下什么信号

记 $g$ 固定、$d=d_g,\ b=d-1,\ v_g=1_{C_g}/\sqrt d,\ w=(A-b)v_g$。取对应大特征值 $\lambda_g$ 的单位特征向量 $e_g$，选符号使 $\langle e_g,v_g\rangle>0$。对不同的固定 $h$，设 $h=(g/p)q$、$p\mid g,\ q\ne p$ 均为素数时叫它相邻核，记 $a=p/q$。这类表示唯一。

**定理二。** 对固定 $h\ne g$，
$$
 \lim d\langle e_g,v_h\rangle =
 \begin{cases}
 (1+\min(1,a))/[\sqrt a(1-a)], & h=(g/p)q,\\
 0, &\text{其余}.
 \end{cases}                                                       \tag{6}
$$
该读数的符号可区分被换入的素数比换出的素数大或小。令 $T_g=1-|\langle e_g,v_g\rangle|^2$。特征向量的角度损失与特征值偏移之间有严格正的常数差：
$$
 d^2 T_g-d(\lambda_g-b)\longrightarrow
 L_g=\sum_{p\mid g,\ p\ {\rm prime}}\left(
 \sum_{q<p,\ q\ {\rm prime}}\frac{(p+q)^2}{(p-q)^2}
 +\sum_{q>p,\ q\ {\rm prime}}\frac{4p^2}{(q-p)^2}\right).          \tag{7}
$$
用第 51 轮已给出的 $\kappa_g$ 可把 (7) 写作
$d^2T_g=4\sum_{p\mid g,\ p\ {\rm prime}}p\log\log X+\kappa_g+L_g+o(1)$。

证明沿用第 51 轮 §§2–3 的三个已证估计。第一，$w$ 在团内为零，在团外每个坐标至多 $2/\sqrt d$，且 $\|w\|^2=4\sum_{p\mid g,\ p\ {\rm prime}}p\log\log X+O_g(1)$。第二，各固定特征值有量级 $d$ 的谱隙，$\|e_h-v_h\|=O_h(\sqrt{\log\log X}/d)$；若 $h=(g/p)q$，则 $\langle w,e_h\rangle\to(a+\min(1,a))/\sqrt a$，其它固定 $h\ne g$ 给零。第三，谱权 $|\lambda_j||\langle w,e_j\rangle|^2/d$ 的和有界，且除去有限多相邻核后，剩余谱权的上极限可任意小。这三点的直接来源是团外顶点的唯一表示 $(g/p)uv$：$uv$ 为半素数，邻居由 $u,v$ 中不超过 $X/g$ 的不同素数给出。特别是第三点比单纯的谱隙更强。[旧估计、紧性与常数 $\kappa_g$](../fiftyfirst/multiplicative.md)

由 $\langle w,e_h\rangle=(\lambda_h-b)\langle v_g,e_h\rangle$，可计算 $d\langle e_g-v_g,e_h\rangle$。换 $e_h$ 为 $v_h$ 的误差为 $O_g((\log\log X)/d)$。若 $h$ 与 $g$ 相邻，二团的唯一交点最终在窗口内，故 $d\langle v_g,v_h\rangle\to1/\sqrt a$；其它情形为零。相加即得 (6)。

对 $j\ne g$，令 $u_j=|\langle w,e_j\rangle|^2$。有两个精确谱恒等式
$$
 T_g=\sum_{j\ne g}\frac{u_j}{(b-\lambda_j)^2},\qquad
 (\lambda_g-b)(1-T_g)=\sum_{j\ne g}\frac{u_j}{b-\lambda_j}.
$$
第二式用 $\langle Av_g,v_g\rangle=b$。代入 (7) 左端时，因 $T_g=O_g(\log\log X/d^2)$、$\lambda_g-b=O_g(\log\log X/d)$，省略 $1-T_g$ 的误差趋零。在两项之差中，$u_j$ 的系数为 $d(1+\lambda_j)/(b-\lambda_j)^2$。分子中的常数 1 总贡献 $O_g(\|w\|^2/d)=o(1)$；其余由上述谱权紧性和间隙控制。对固定相邻核，取极限给 $(a+\min(1,a))^2/(1-a)^2$。分 $q<p$ 与 $q>p$ 合计即 (7)。

式 (6) 还有整体向量版本。令 $c(a)=a(a+\min(1,a))/[\sqrt a(1-a)]$，则在各有限图的欧氏范数中
$$
 \left\|d(e_g-v_g)-w-
 \sum_{\substack{p\mid g,\ q\ne p\ {\rm primes}\\h=(g/p)q\le X/2}}
 c(p/q)v_h\right\|\longrightarrow0.                               \tag{8}
$$
沿 $e_j,\ j\ne g$ 投影，$d(e_g-v_g)-w$ 的系数是 $(1+\lambda_j)\langle w,e_j\rangle/(b-\lambda_j)$；沿 $e_g$ 的分量由前述角度及偏移界为 $o(1)$。固定相邻核的系数趋于 $c(a)$，非邻接核趋零；系数平方尾由同一组紧谱权控制，因为 $|\lambda_j|/d$ 有界且分母离零。最后 $|c(p/q)|=O_g(q^{-3/2})$，允许将有限截断中的 $e_h$ 替为 $v_h$ 后再移去截断。式 (8) 用团指示与一次邻接即可构造特征向量的 $o(1/d)$ 精度近似。

## 有限整数窗口

程序对小窗口从所有整数对的 gcd 直接建图，再在三个整数谱参数上分别验证完整邻接矩阵的精确行列式和关联矩阵给出的行列式。八个数值窗口逐顶点核对团外的唯一分解与邻居数。对 $k=2,X=100000,g=2$，团有 5133 点，排序所得特征值约为 $5132.0045989$，对应单位特征向量与团指示的内积平方约为 $0.99999813$。在 $h=3,5$ 两个团上的式 (6) 读数分别约为 $6.68136,3.88838$，其极限为 $6.12372,3.68932$；取 $k=3,X=60000,g=4,h=9$ 可对照非邻接核，读数约为 $0.01440$，极限为零。

用 200000 以内的素数逐项做整数有向取整，并以 $\sum_{q>N}(q-p)^{-2}\le1/(N-p)$ 压住余项，得 $19.05704<L_2<19.05713$、$37.93216<L_3<37.93235$。大图的特征值与内积取自稀疏对称矩阵的数值求解；边数、团外计数和 $L_p$ 的包络用整数确定。式 (1) 的两个极限分别由解析计数证明。复算使用 NumPy、SciPy、SymPy，运行 <code>OPENBLAS_NUM_THREADS=1 python spectrum_check.py</code>。[复算程序](spectrum_check.py) · [整数计数、谱读数及常数包络](spectrum_checked.json)
