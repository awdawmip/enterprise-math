# 固定奇库存的近同步只可能在有限多个超二次窗口中出现

固定正奇数 $K$ 和正实数 $B,\varepsilon$。记 $d=3K$、$\theta=256^{-1/d}$。满足
$$
  2\le s\le n,\qquad |1-\rho_K(n,s)|\le B n^{-2-\varepsilon}
$$
的整数对只有有限多。于是对所有 $n\ge s\ge2$ 都有 $|1-\rho_K(n,s)|\ge b_{K,\varepsilon} n^{-2-\varepsilon}$，其中 $b_{K,\varepsilon}>0$。后一句先取 $B=1$，再利用 C74 已逐整数证明 $\rho_K\ne1$ 并吸收有限例外。这里不报可计算的有限例外上界，也没有把 $\varepsilon=0$ 纳入结论。此证明使用 Schmidt 子空间定理。

## 代数的第二项

取 $L(n)=[\Gamma(n+K+1)/\Gamma(n+K/4+1)]^{4/d}$，$\mu=(5K+4)/8$，$h=3K/4$，$x=n+\mu$。Gamma 两个自变量为 $x+(1+h)/2$ 和 $x+(1-h)/2$。固定平移的 Gamma 比 Stirling 渐近给
$$ L(n)=x+\frac{a_K}{x}+O_K(x^{-2}),\quad a_K=\frac{1-h^2}{24}. $$
例如对数 Gamma 比的一次修正由两个 $B_2$ 值之差给出，$B_2(1-u)=B_2(u)$ 故为零；二次修正为 $-[B_3((1+h)/2)-B_3((1-h)/2)]/(6h)=(1-h^2)/24$。指数化即得上式。$a_K\ne0$，因为 $h=3K/4$ 不等于1。也可以将递推所得 $t_1,t_2$ 代入 $(G_K)^{1/d}$ 独立核验。[NIST DLMF §5.11](https://dlmf.nist.gov/5.11)

由 $\rho_K(n,s)^4=256 L(s-1)^d/L(n)^d$，接近同步时 $s\asymp n$。令 $p=8(s-1+\mu)$、$q=8(n+\mu)$。$p,q$ 为正整数，且 $p\asymp q\asymp n$。在定理的窗口内，$\zeta=\min(1,\varepsilon)$，有
$$
 p+64a_K/p=\theta(q+64a_K/q)+O_{K,B,\varepsilon}(q^{-1-\zeta}).
$$
先由此得 $p=\theta q+O(1/q)$，再在校正项中使用 $q/p=1/\theta+O(1/q^2)$。因此
$$
 q(p-\theta q)=b+O(q^{-\zeta}),\qquad b=64a_K(\theta-\theta^{-1})\ne0. \tag{1}
$$
$\theta,b$ 都是实代数数，$\theta$ 的次数恰为 $d$。确实 $\theta^{-1}=2^{8/d}$，$\gcd(8,d)=1$。由贝祖系数组合两边幂次，$\mathbb Q(2^{8/d})=\mathbb Q(2^{1/d})$，而 $X^d-2$ 在2处满足 Eisenstein 判据。特别是 $1,\theta,\theta^2$ 在有理数域线性独立。

## 一次四维应用

使用整数向量 $\mathbf z=(p^2,pq,q^2,1)$，高度 $H=\|\mathbf z\|_\infty\asymp q^2$。取四个实代数系数线性形式
$$
 L_1=z_1-2\theta z_2+\theta^2z_3,\quad
 L_2=z_2-\theta z_3-bz_4,\quad
 L_3=z_3,\quad L_4=z_4.
$$
系数矩阵上三角且对角元全为1，由 (1) 有 $L_1=(p-\theta q)^2=O(q^{-2})$、$L_2=O(q^{-\zeta})$。因此 $|L_1L_2L_3L_4|=O(q^{-\zeta})\le H^{-\zeta/3}$ 对充分大的 $q$ 成立。Schmidt 子空间定理表明所有这些整点位于有限个真有理线性子空间。若有无穷多个整点，其中一个子空间将含一个 $q\to\infty$ 的子列，于是有一组不全为零的有理数 $A,B_1,C,D$，该子列满足
$$ A p^2+B_1 pq+C q^2+D=0. $$
除以 $q^2$ 并取极限得到 $A\theta^2+B_1\theta+C=0$，故 $A=B_1=C=0$。随后 $D=0$，矛盾。[Schmidt, Norm form equations (1972)](https://annals.math.princeton.edu/1972/96-3/p06) · [Evertse, Theorem 10.1.2 的线性形式表述](https://pub.math.leidenuniv.nl/~evertsejh/Subspace.pdf)

## 两块逐词识别和舍去外部定理时的界

C74 的立方根区域只在 $|1-\rho_3(v,w)|<v^{-8}$ 时留待进一步处理。以上取 $K=3,B=1,\varepsilon=6$ 得到仅有限对 $(v,w)$ 可能落在这个窗口。C74 无条件区域 $v\le\kappa_0c^{4/13}$ 当 $c$ 充分大时包含所有这些固定对。因此，存在 $\kappa>0$，每个充分大 $c$ 的三角区域 $2\le w\le v\le\kappa c^{1/3}$ **每一条**安排都由原单项 $g$ 在完整同库存中唯一确定。所得区域直接含 $\Omega(c^{2/3})$ 条保证。常数和库存起点属于存在性结论。

若只用初等有理分数间隔，也可从 (1) 单独得到定量结论。取窗口 $|1-\rho_K|\le Bn^{-3}$，则 $p/q=\theta+b/q^2+O(q^{-3})$。在任意 $Q\le q<2Q$ 中，$p/q$ 落在长度 $O(Q^{-2})$ 的区间里，不同有理数彼此距离至少 $1/(4Q^2)$，故只有 $O_{K,B}(1)$ 种不同斜率。同一斜率对应 $q_1,q_2$ 时，由 $b\ne0$ 可知 $|1/q_1^2-1/q_2^2|\ll Q^{-3}$，又因其左侧至少为常数倍的 $|q_1-q_2|Q^{-3}$，所以 $|q_1-q_2|=O_{K,B}(1)$。每段仅有 $O(1)$ 个整数行，总数 $O_{K,B}(\log V)$。这个初等估计对更窄的 $v^{-8}$ 窗口同样成立，从而即使不引用子空间定理，立方根区域内也只有 $O(\log c)$ 条词需要其余论证。

## 临界指数的另一侧

记 $m_K(n)=\min_{2\le s\le n}|1-\rho_K(n,s)|$。对每个固定正奇数 $K$，
$$
 \limsup_{n\to\infty}\frac{-\log m_K(n)}{\log n}=2 .
$$
上界见前述子空间论证。下界要在可用整数库存中构造。取 $\theta$ 连分数的两个相邻收敛向量 $(P_j,Q_j),(P_{j-1},Q_{j-1})$，其行列式为 $\pm1$，所以在模8下可逆。选择 $1\le A,B\le8$，使
$$
 (p,q)=A(P_j,Q_j)+B(P_{j-1},Q_{j-1})\equiv(5K+4,5K+4)\pmod8 .
$$
有 $Q_j\le q\le16Q_j$，由收敛分数误差界 $|P_j-\theta Q_j|<1/Q_{j+1}$ 得 $|p-\theta q|\le16/Q_j\le256/q$。取 $n=(q-5K-4)/8$、$s=(p-5K+4)/8$，对充分大 $j$ 是合法整数。此时 $L(s-1)/L(n)=\theta+O_K(q^{-2})$，由确切的 Gamma 比恒等式得到 $m_K(n)\le C_Kn^{-2}$。由于 $q$ 无界，此构造产生无穷多行。此处没有确定临界窗口的最佳常数和频率。

## 精确核验

运行 `python near_sync_controls.py`。脚本首先用独立的多项式移位递推核验 $K=1,3,5,7,9,11$ 的两个展开系数，再对 $K=3$ 的 $2\le n\le65536$ 搜全部整数 $s$。逐行保持跨过1的两侧精确分数；在 $n\ge3$ 时相邻比至少 $1+9/(4n+3)>(1+n^{-2})/(1-n^{-2})$，故两个邻点已能查全命中，另对前47行的所有列做重复直接乘积核验。含等号的 $n^{-2}$ 窗口恰得 $(402,217),(12468,6733)$，含等号的 $n^{-3}$、$n^{-8}$ 窗口均为空。输出见 `near_sync_controls.json`。
