# 近同步可能影响的整数行数低于任意固定正幂

设 $K$ 为固定正奇数，$d=3K$、$\theta=256^{-1/d}$、$\mu=(5K+4)/8$。对任意固定实数 $B,\delta>0$，当 $V\ge2$ 时有
$$
\#\{2\le n\le V:\ \exists\,2\le s\le n,\ |1-\rho_K(n,s)|\le Bn^{-2}\}
   =O_{K,B,\delta}(V^\delta).
$$
一行指给定 $n$ 后所有可能的 $s$。在 $\kappa_1 c^{1/3}$ 的单读数逐词恢复定理中，这给出了一个精细计数：取 $V=\lfloor\kappa_1c^{1/3}\rfloor$，整三角区 $\binom V2$ 条词里有全库存唯一保证的至少为 $\binom V2-O_{\delta}(V^\delta)$。该估计描述充分条件留下的余量，实际并列数可以更少。

## 近同步迫使一条有理逼近

用 Gamma 格点引理的 $G_K(n)$。令 $L(n)=G_K(n)^{1/d}$，它在正轴满足
$$L(n)=n+\mu+O_K(1/n).$$
例如由移位差分的最高两阶，$T_K(n)=n^d+t_1 n^{d-1}+\cdots$，其中 $t_1=d(5K+4)/8$；开 $d$ 次根即得。$|1-\rho_K|\le B n^{-2}$ 时 $s\asymp_K n$（只需处理充分大 $n$），并且
$$
L(s-1)=\theta L(n)\rho_K(n,s)^{4/d}
      =\theta L(n)+O_{K,B}(1/n).
$$
故
$$s+\mu-1=\theta(n+\mu)+O_{K,B}(1/n).$$
取固定正整数 $D$ 清掉 $\mu$ 的分母，如取 $D=8$。令 $p=D(s+\mu-1),q=D(n+\mu)$，则 $p,q$ 都是正整数且
$$
|p/q-\theta|\le C_{K,B}/q^2. \tag{1}
$$
同一整数行在 $n$ 充分大时至多一项 $s$ 满足原不等式。两相邻 $\rho_K$ 的比为 $4(s+K)/(4s+K)$，在 $\rho_K$ 接近 1 的区域相邻增量 $\gg_K n^{-1}$。

## 二进分段计数

$\theta$ 是代数无理数：若 $\theta^d=2^{-8}$ 是有理数的 $d$ 次幂，则取 2 进赋值得 $d\mid8$，与 $d=3K$ 矛盾。Roth 定理在指数 $3>2$ 上给出固定 $b_K>0$，对于每个既约 $a/h$ 都有 $|\theta-a/h|\ge b_K h^{-3}$。定理留下的有限个小分母可吸收入常数。[K. F. Roth，Rational approximations to algebraic numbers，1955](https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F)

在一段 $Q\le q<2Q$ 中，式 (1) 把所有候选 $p/q$ 放入以 $\theta$ 为中心、长度 $O(Q^{-2})$ 的实区间。任何两个**不同**的这些有理数相隔至少 $1/(4Q^2)$，所以该段仅有 $O_{K,B}(1)$ 种不同的有理值。约成 $a/h$ 后，Roth 下界和 (1) 还给 $h\gg Q^{2/3}$。同一个 $a/h$ 对应的分母 $q$ 均为 $h$ 的倍数，至多 $O(Q/h+1)=O(Q^{1/3})$ 个。对各二进段求和先得到
$$ O_{K,B}(V^{1/3}). $$
一般地，Roth 定理可用任意 $2+\varepsilon$ 的指数，给每段 $O_{K,B,\varepsilon}(Q^{\varepsilon/(2+\varepsilon)})$ 个。对每个预先选定的 $\delta>0$ 取足够小的固定 $\varepsilon$，从而
$$
\#\{n\le V:\exists s,\ |1-\rho_K(n,s)|\le Bn^{-2}\}
=O_{K,B,\delta}(V^\delta).
$$
因此上述库存三角区实际至少覆盖 $\binom V2-O_\delta(V^\delta)$ 条；写成库存幂也即对每个 $\epsilon>0$ 留出 $O_\epsilon(c^\epsilon)$ 条。这个计数没有给出可计算的库存起点。方法无法从有理逼近指数 $2$ 直接推出精确近同步行只出现有限多次。

若只用初等估计，由 $256p^d-q^d$ 为非零整数，也能得 $|\theta-a/h|\gg_K h^{-d}$，按相同分段计数得 $O_{K,B}(V^{1-2/d})$ 条。在末块 $K=3$ 时即 $O_B(V^{7/9})$。这个版本完全可与奇偶格点证明一起使用。

在 $K=3$、$B=1$ 的 $2\le n\le1024$ 共 1023 行中，准确分数核验找到唯一满足 $|1-\rho_3|<n^{-2}$ 的 $(n,s)=(402,217)$，满足 $n^{-8}$ 严格阈值的为零，两个阈值都没有等号。程序按 $s$ 上的严格单调性对每行查最近两项，另在 $n\le64$ 整行穷举核对。[准确行扫描](check_rare.py) · [复算结果](rare_rows.json)
