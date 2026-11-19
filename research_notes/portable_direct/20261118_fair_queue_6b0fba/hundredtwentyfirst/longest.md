# Hart 残差门的最长连续乘子段

令 $K=N^{1/3}$，在原壳 $K\le k\le 2K$ 的整数乘子上使用原分数
$$
 f(k)=2\sqrt{Nk},\qquad x_k=\lceil f(k)\rceil,\qquad
 s_k=\frac{x_k^2-4Nk}{2x_k-1}.
$$
令 $L_\alpha(N)$ 为全部 $s_k\le\alpha$ 的最长连续段的长度；没有命中时取零。对每个固定 $1/4<\alpha<1$ 及所有充分大的整数 $N$，有
$$ K^{1/4}\ll_\alpha L_\alpha(N)\ll_\alpha K^{1/3}. \tag{1}$$
进一步，当 $1/4<\alpha<1/3$ 时，最长段的量级完全由 $3K/2$ 在半整数网格中的位置决定。写 $b=3K/2$，$d_-,d_+$ 分别为它到下、上最近半整数的非负距离；命中网格时都取零，约定 $1/0=+\infty$。一致地有
$$
 L_\alpha(N)\asymp_\alpha
 \min\!\left(K^{1/3},\,\max\!\left\{d_-^{-1},(K/d_+)^{1/4}\right\}\right). \tag{2}
$$
同样靠近网格，从上侧与从下侧接近会给出不同的增长率。两种极端 $K^{1/4}$ 与 $K^{1/3}$ 都出现在具有两个趋于无穷的不同奇素因子的真实半素数列上。有限小整数需要排除，例如 $N=7,\alpha=3/10$ 时没有命中。

本研究对应 P1 任务 RS-SEMIPRIME-RESIDUAL-PRIORITY-HART-STREAMING-COST-AUDIT 的整数阈值流。第二十二轮已有固定长窗口的环面律、三连门槛、真平方见证计数；本篇中窗口长度随输入增长。说的是平方判定以前通过分数门的到达流。剩余模筛、真正平方、揭示因子的首次停时和总运行收益各有额外条件。[冻结任务书与同成本义务](https://github.com/awdawmip/enterprise-math/blob/53cc9a7836bf7f34e9dafbd621c1712026b5a2f6/research_tasks/SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT_CANONICAL_REPUBLICATION_20261013.md) · [原评分定义](https://github.com/awdawmip/enterprise-math/blob/e93b8427ced87bc1ce740082df3d2edf52f141fc/research_returns/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_RETURN_20260829.md#L209) · [固定窗定理](../twentysecond/hart.md) · [三连击](../twentysecond/hart_runs.md)

## 1. 三阶振荡给出全域上界

写 $u_k=x_k-f(k)$。精确恒等式 $s_k=u_k+u_k(1-u_k)/(2x_k-1)$ 给出 $u_k\le s_k$ 和 $s_k-u_k=O(K^{-2})$。若整个 $H$ 点段全中，$\{f(k)\}$ 在 $(0,1-\alpha)$ 中无点。Erdős–Turán 不等式给出仅依赖 $\alpha$ 的正整数 $B$ 和 $c>0$，使某个 $1\le h\le B$ 满足 $|\sum e(hf(k))|\ge cH$，$e(t)=\exp(2\pi it)$。可在上述开区间取一段紧子区间，故 $f(k)$ 恰为整数也不妨碍推论。

在壳内 $f'''(t)=3K^{3/2}/(4t^{5/2})\asymp1/K$。对位移 $1\le r<M\le H/2$，差分相位 $h(f(t+r)-f(t))$ 的二阶导数介于 $c_h r/K$ 和 $C_h r/K$；经典 van der Corput 二阶导数检验给出差分和 $O_B(H\sqrt{r/K}+\sqrt{K/r})$。代入 Weyl 差分，得到
$$
 H^{-2}\left|\sum e(hf(k))\right|^2
 \ll_B M^{-1}+\sqrt{M/K}+\frac1H\sqrt{K/M}.
$$
从任何更长的段先截取 $H=\lfloor D K^{1/3}\rfloor$ 项，取 $M=\lfloor H/2\rfloor$。第三项为 $O(D^{-3/2})$，其余随 $K$ 趋零；充分大的固定 $D$ 与前述低频下界矛盾。这一上界对每个固定 $\alpha<1$ 均成立。[van der Corput 差分与导数法](https://doi.org/10.1017/CBO9780511661976)

## 2. 半整数共振及其方向

置 $g(t)=f(t)+t^2/4$。在 $[K,2K]$ 有
$$
 g'(K)=b,\qquad g''(t)=\tfrac12(1-(K/t)^{3/2})\asymp(t-K)/K,\qquad
 g'''(t)\asymp K^{-1}.
$$
对 $j\in\frac12\mathbb Z$ 记 $G(t)=g(t)-jt$。在整数 $k$ 上，$jk-k^2/4\bmod1$ 的偶数值为零，奇数值为 $1/4$ 或 $-1/4$。故 $\alpha>1/4$ 时，两种奇偶性允许的 $\{G(k)\}$ 总有一段共同开弧，长至少 $\alpha-1/4$；可固定在其内部并留出仅依赖 $\alpha$ 的正裕量。进入此弧就有 $u_k<\alpha-\varepsilon_\alpha$，大 $N$ 下原分数 $s_k$ 同样合格。

选上侧半整数 $j=b+d_+$。因 $d_+\le1/2$，方程 $g'(x_0)=j$ 在壳左端附近有唯一解，$x_0-K\asymp\sqrt{K d_+}$，$d_+=0$ 时取 $x_0=K$。写
$$ R_+=\min(K^{1/3},(K/d_+)^{1/4}). $$
由导数式，$g''(x_0)R_+^2+R_+^3/K\asymp1$。在 $[x_0+DR_+,x_0+2DR_+]$ 上，$G$ 单调，每单位变化至多 $C_D/R_+$，总变化至少 $cD^2$。固定充分大的 $D$，$G$ 穿过一整段上述共同开弧，原像长度 $\gg_\alpha R_+$，从而得到连续整数段。两端都位于原壳，因为 $x_0-K=O(\sqrt K)$ 且 $R_+\le K^{1/3}$。特别 $R_+\gg K^{1/4}$，得到 (1) 的下界。

下侧取 $j=b-d_-$，写 $R_-=\min(K^{1/3},1/d_-)$。在 $[K+DR_-,K+2DR_-]$ 上，同一论证使用 $d_-R_-+R_-^3/K\asymp1$，给出 $\gg_\alpha R_-$ 个连续整数；若 $R_-$ 有界或小于 $R_+$，已有上侧构造即可。综合得到 (2) 的下界。下侧驻点可能在壳外，故两种方向的量纲不同。

## 3. 对连续长段的反推

现在固定 $1/4<\alpha<1/3$。设一个全中段长 $H$，并用 (1) 限 $H=O_\alpha(K^{1/3})$。写 $C_k=-\Delta^2 f(k)$，则 $1/(4\sqrt2)<C_k<1/2$，且它在全段的变化为 $O(H/K)$。整数 $\Delta^2x_k=\Delta^2u_k-C_k$ 只能取 $0,-1$。若全为零，则 $\Delta^2 u_k=C_k>1/(4\sqrt2)$，与 $0\le u_k\le\alpha$ 合起来使 $H=O(1)$（取等距三点的二差即可）。

若出现 $-1$，该点有 $C_k\ge 1-2\alpha$。因为 $1-2\alpha>\alpha$，在足够大的 $N$ 下全段 $C_k>\alpha$。连续两个零会使两二差相加 $u_k-u_{k+1}-u_{k+2}+u_{k+3}>\!2\alpha$；连续两个 $-1$ 会使同一量小于 $-2\alpha$。故二差严格交替。于是 $X_k=x_k+k^2/4$ 满足 $X_{k+2}-X_k=2j$ 为同一个整数，两条奇偶子列斜率均为 $j\in\frac12\mathbb Z$。在任一奇偶子列上 $g(k)-jk=X_k-jk-u_k$ 的摆幅至多 $\alpha$。

设整段始于 $t_0$，取其中一条奇偶子列的首末点，割线给某点 $\xi$ 满足 $|g'(\xi)-j|\ll_\alpha 1/H$。同子列中依次取三个相距 $\asymp H$ 的等距点，凸性和二重积分给 $g''(t_0)\ll_\alpha H^{-2}$，故 $t_0-K\ll K/H^2$。结合 $H^3\ll K$ 得 $\xi-K\ll K/H^2$，于是 $0\le g'(\xi)-b\ll(\xi-K)^2/K\ll K/H^4$。若 $j\le b$，有 $d_-\le b-j\ll1/H$；若 $j\ge b$，有 $d_+\ll K/H^4+1/H\ll K/H^4$。这连同全域上界即证 (2)。在 $\alpha=1/3$ 时，强迫交替的正裕量消失，此证明未给出同样分类。

## 4. 两个指数都由真半素数达到

Baker–Harman–Pintz 证明，充分大的实数 $x$ 左侧长度 $O(x^{0.525})$ 的区间含有素数。固定大偶整数 $m$，先取 $T=m$，再独立地取 $T=m+1/6$。对两种 $T$ 用 Bertrand 定理选奇素数 $P\asymp T^{1/8}$，在 $x=T^3/P$ 左侧取上述素数 $Q$。两因子均趋于无穷，且充分大时不等。对 $N=PQ$ 有
$$
 0\le T^3-N\ll T^{1/8+(3-1/8)0.525}
      =T^{523/320}=o(T^{5/3}),\qquad K=T+o(T^{-1/3}).
$$
第一列到半整数网格的距离是 $o(K^{-1/3})$，由 (1) 和第2节得 $L_\alpha\asymp_\alpha K^{1/3}$（任意 $1/4<\alpha<1$）。第二列的 $d_-,d_+\to1/4$，由 (2) 得 $L_\alpha\asymp_\alpha K^{1/4}$（$1/4<\alpha<1/3$）。这个构造允许不平衡素因子。[Baker、Harman 与 Pintz，*The difference between consecutive primes, II*](https://doi.org/10.1112/plms/83.3.532)

在顺序生成候选的实现中，一段全中就是连续的平方判定入口请求。若等到失配才把整段逐项写出，峰值挂起键数至少为最长段；用起点和长度存储，每个段只需一对整数。由第二十二轮的二点均匀分布，全壳命中数为 $(\alpha+o(1))K$，段数为 $(\alpha(1-\alpha)+o(1))K$（除了首点，按从未中到命中的相邻事件逐项计数）。所以平均段长趋于 $1/(1-\alpha)$，编码后的总段数仍为线性阶。实际平方检测与服务速率、提前停机、模筛后的负载均不在这个计数内。

## 5. 全扫与连续段证书

<code>python -I longest_check.py --out longest_checked.json</code> 只用标准库。以整数立方根确定壳两端，以整数平方根及交叉乘积判原分数。九个输入分别在五档门槛上全扫，另在 $1\le N\le128$ 用从零逐个整数递增的办法交叉核验平方根和残差。$\alpha=3/10$ 时 $N=1009\cdot1013$ 与 $N=1000003\cdot1000033$ 的全壳最长段分别为 3、4，后者有 2115 个不同段。

另外九个半素数用递归的阶证书认证两个真素因子；小叶以试除结束。程序在每个输入精确定位上侧驻点，再枚举两个构造短窗，核对返回段中每个原分数，并输出该段最大分数的分子分母。各组以 $T$ 给出靠近的立方根位置。

| $T$ | $P$ | 上侧短窗最长段 | 下侧短窗最长段 |
|---|---:|---:|---:|
| $2^{24}$ | 11 | 17 | 13 |
| $2^{24}+1/6$ | 11 | 8 | 0 |
| $2^{24}+1/128$ | 11 | 6 | 6 |
| $2^{24}-1/128$ | 11 | 8 | 4 |
| $2^{36}$ | 23 | 140 | 13 |
| $2^{36}+1/6$ | 23 | 96 | 0 |
| $2^{48}$ | 67 | 2224 | 13 |

这些有限短窗给出全壳最长段的下界；程序以字段另标完整扫描。最后一组 2224 个连续乘子从 $281474976839506$ 开始。短窗里的零也只表示所查区间没有命中。原保留基准和因子生产性标签均未用于选例。[程序](longest_check.py) · [完整整数记录](longest_checked.json)
