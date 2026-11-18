# Hart 乘数壳的尖锐平方命中计数与素数间距阈值

令 $N=pq$，$p<q$ 是不同奇素数，$K=N^{1/3}\ge4$。对整数 $K\le k\le2K$，置
$$
 x_k=\lceil2\sqrt{Nk}\rceil,\qquad e_k=x_k^2-4Nk,\qquad
 S(k)=\frac{e_k}{2x_k-1}.
$$
记 $H(N)$ 为这个壳中 $e_k$ 是完全平方的乘数个数。写 $c=\sqrt2-1$。下列一阶常数在全体这类半素数上是尖锐的：
$$
 \boxed{\ H(N)\le\min\{\,2p/K+12,\ c\sqrt K+289\,\},\qquad
 \limsup_{pq\to\infty}\frac{H(pq)}{\sqrt K}=\sqrt2-1.\ }
$$
在决定等号首项的近素对上，全部命中都是平方乘数，且其评分可以一致趋零。差平方分解和以多个 $k$ 检验上方首个平方是 Fermat、Lehman、Hart 的已有机制。下文研究特定壳上的命中数及其分布。这里的计数可使用已知 $p,q$ 做证明，不能据此估算未给出因子时的筛选成本。旧保留样本未被用作验证数据。[原评分和乘数约定，§§7–8](https://github.com/awdawmip/enterprise-math/blob/efb544eab119480aaea4b2a6d79d764909d9a0e2/research_returns/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_RETURN_20260829.md) · [Lehman，1974](https://doi.org/10.1090/S0025-5718-1974-0340163-2) · [Hart，2012](https://doi.org/10.1017/S1446788712000146)

### 命中与整格点的双射

一次命中等价于存在一对正整数 $u,v$ 满足
$$
 k=uv,\qquad (\sqrt{pu}-\sqrt{qv})^2<1 .
$$
此时 $x_k=pu+qv$，$e_k=(pu-qv)^2$，而且有序对 $(u,v)$ 唯一。

事实上，若 $e_k=y^2$，则 $x_k,y$ 同奇偶，$a=(x_k-y)/2,\ b=(x_k+y)/2$ 是正整数，$ab=Nk$。由首个上方平方的定义，
$$
 x_k<2\sqrt2K^2+1,\qquad y^2<4\sqrt2K^2+1<9K^2.
$$
故 $a\le b<(\,2\sqrt2K^2+1+3K\,)/2<2K^2<N$。因此 $p,q$ 分属 $a,b$ 且方向唯一，即使 $k$ 本身含有其中某个素因子亦然。写成 $pu,qv$ 后，相应根差的平方正是 $x_k-2\sqrt{Nk}<1$。反过来，若根差平方小于 $1$，整数 $pu+qv$ 就是该上取整。给定 $k$，无序因子对已由 $x_k,y$ 唯一确定。

命中格点必满足矩形约束
$$
 0<v<2K^2/q=2p/K,\qquad |u-(q/p)v|<3K/p .
$$
固定 $v$ 时，可用整数 $u$ 至多 $1+6K/p$ 个，故命中数至多 $2p/K+12$，特别是 $O(\sqrt K)$。

### 原始斜率与首项常数

将 $(u,v)=t(u_0,v_0)$ 约成互素正整数向量。变换 $(u,v)\mapsto(v,u-(q/p)v)$ 的行列式绝对值为 1，各原始向量仍落在上节矩形内，其面积为 12。从原点按斜率依次连接原始向量，相邻向量与原点张成的三角形有不相交的内部，每个面积至少 $1/2$。这些有限个三角形位于矩形闭包内，总面积严格小于 12，因为所有顶点的第一坐标都严格小于 $2p/K$。所以原始斜率至多 **24 条**。每条原始斜率上可用的 $t$ 还满足
$$
 \sqrt{K/(u_0v_0)}\le t\le\sqrt{2K/(u_0v_0)},
 \qquad t(\sqrt{pu_0}-\sqrt{qv_0})^2<1 .
$$
仅前一条件已给出 $1+c\sqrt{K/(u_0v_0)}$ 个的上界。

若 $p/K\le3$，直接计数至多 18 个。若 $2p/K\le c\sqrt K$，直接计数给出 $c\sqrt K+12$。在其余情形，$p>3K$ 强迫 $u\ge v$，否则 $qv-pu>3K$。两条不同原始斜率若都满足 $v_0<p/(6K)$，则其整数行列式的绝对值小于 $(3K/p)(v_0+v'_0)<1$，矛盾。因此至多一条这样的斜率，贡献至多 $1+c\sqrt K$ 个乘数。其余每条有 $\sqrt{u_0v_0}\ge v_0\ge p/(6K)$，乘数个数严格小于 $1+12=13$。合并即得首段的统一界，常数 289 未作优化。

### 近素对上的相变与评分

记 $\Delta=q-p$。任何命中都有
$$
 |u-v|\le |u-(q/p)v|+(\Delta/p)v<3K/p+2\Delta/K .
$$
右端小于 1 就强迫 $u=v=t$。特别是沿 $\Delta=o(K)$ 的序列，$p\sim q\sim K^{3/2}$，该判据最终恒成立。命中数遂精确等于
$$
 \#\left\{t\in\mathbf Z:\sqrt K\le t\le\sqrt{2K},
       \quad t<\frac{(\sqrt p+\sqrt q)^2}{\Delta^2}\right\}.
$$
因此沿 $\Delta=o(K)$ 且 $\Delta/\sqrt K\to\gamma\in[0,\infty]$ 的序列，
$$
 \frac{H(N)}{\sqrt K}\longrightarrow
 \left[\min\!\left(\sqrt2,\frac4{\gamma^2}\right)-1\right]_+ ,
$$
其中 $[a]_+=\max(a,0)$，$4/0^2=\infty$，$4/\infty^2=0$。这是因为阈值除以 $\sqrt K$ 后趋于 $4/\gamma^2$，整数取整只造成 $O(1)$ 误差。$\gamma\le2^{3/4}$ 时达到整段平方乘数的极限密度，$\gamma\ge2$ 时命中密度为零；特别地，$\gamma=0$ 时极限为 $\sqrt2-1$，$\gamma=2$ 只给出 $H=o(\sqrt K)$；$\gamma>2$（含 $\infty$）时阈值最终低于壳下端，故最终 $H=0$。无需假设每个 $\gamma$ 都能由某个素数间距序列实现。

素数定理给出 $[X,2X]$ 内渐近 $X/\log X$ 个素数，抽屉原理保证其中有相邻素对的间距 $O(\log X)$。取不相交的这类区间便得到无限多组 $\Delta=O(\log p)$。阈值最终严格大于 $\sqrt{2K}$，故每个壳内平方乘数都命中，且再无其他命中：
$$
 H(N)=\lfloor\sqrt{2K}\rfloor-\lceil\sqrt K\rceil+1
      =(\sqrt2-1)\sqrt K+O(1).
$$
每个命中的原评分为
$$
 S(t^2)=\frac{t^2\Delta^2}{2t(p+q)-1}
       =O\!\left(\frac{\log^2p}{K}\right)
$$
并对整个壳一致成立。由此得到全局上界的尖锐首项，也给出固定小评分阈值下仍能出现 $\asymp\sqrt K$ 个真命中的无限族。

### 独立整数核验

标准库脚本穷举全部 $3\le p<q\le151$ 且 $pq\ge64$ 的 **587** 对奇素数。一条路径用整数平方根逐个 $k$ 验 $e_k$，另一条只用 $k=uv$ 及 $(pu+qv-1)^2<4Nuv$ 枚举见证。共得到 **1037** 个命中，乘数、有序因子对与有理评分逐项吻合。例 $(5,47)$ 的壳为 $7\le k\le12$，六个不同原始斜率全部命中。三组近素对 $(1009,1013),(1013,1031),(1009,1031)$ 的命中数分别为 $4,2,0$，中间一组仅有 $11^2,12^2$。上述样本由小素数重新生成。[程序](hart_hits_check.py) · [确定性证书](hart_hits_checked.json)
