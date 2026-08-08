# Legendre 压力测试——补充 03

状态：`ACTIVE RESEARCH NOTE`  
范围：把成熟 threshold-complex 拓扑专门化到整数截断，并建立进取数论的整数根—维数约束。  
结论纪律：**本文不声称证明了 Legendre 猜想。**

## 1. 前人工作纠偏

补充 02 中的截断穿越配对，在成熟数学中已经有一个自然的拓扑归宿。

Pakianathan 与 Winfree 建立 scalar quota/threshold complex 理论，并证明任意 scalar quota complex 都同伦等价于一束球面，这些球面由 quota 附近的 shell faces 编号；他们还明确研究 `LogPrime`：给素数顶点赋权 \(\log p\)，使加法 quota 条件编码乘法素数乘积阈值。[SRC-PAKIANATHAN-WINFREE-2013-THRESHOLD]

因此，进取数论**不**声称 threshold complex、LogPrime 拓扑、shell/bouquet 定理或 Möbius 消去的拓扑解释属于我们的新数学。

当前压力测试真正值得问的问题更窄：当 quota 恰好来自平方盆地截断、而最小素数又受整数根层级约束时，还会额外产生什么结构限制？

## 2. L013 —— 乘法阈值复形与 Euler 尾和

状态：`ESTABLISHED PRIOR ART + SPECIALIZED EXACT IDENTITY`

令

\[
G=\prod_{p\in\mathcal P}p
\]

为平方自由数，\(T\ge1\) 为整数。定义单纯复形

\[
K(G,T)
=
\left\{
F\subseteq\mathcal P:
\prod_{p\in F}p\le T
\right\}.
\]

空面乘积取 1。若一个乘积不超过 \(T\)，其任意子乘积也不会超过 \(T\)，所以向下封闭性直接成立。

平方自由除数的 Möbius 函数满足

\[
\mu\!\left(\prod_{p\in F}p\right)=(-1)^{|F|}.
\]

若 \(G>1\)，完整 Boolean 除数和为零：

\[
\sum_{d\mid G}\mu(d)=0.
\]

所以

\[
\sum_{\substack{d\mid G\\d>T}}\mu(d)
=
-
\sum_{\substack{d\mid G\\d\le T}}\mu(d).
\]

而对上述复形，

\[
\sum_{\substack{d\mid G\\d\le T}}\mu(d)
=
1-\chi(K(G,T)),
\]

故

\[
\boxed{
\sum_{\substack{d\mid G\\d>T}}\mu(d)
=
\widetilde\chi(K(G,T))
}.
\]

因此，大 Möbius 尾和就是一个精确的约化 Euler 特征。

这个整数恒等式本身不需要对数。若要与成熟 quota-complex 理论连接，只需把外部权重取成

\[
w(p)=\log p,
\]

并取 quota

\[
q=\log(T+1).
\]

因为面乘积为整数，

\[
\sum_{p\in F}\log p<\log(T+1)
\iff
\prod_{p\in F}p\le T.
\]

所以 \(K(G,T)\) 正是前人理论中的一个有限 scalar quota complex。

## 3. L014 —— Shell faces 恰好就是截断穿越除数

状态：`SPECIALIZATION OF ESTABLISHED QUOTA-COMPLEX SHELL THEOREM`

令 \(p\) 为 \(\mathcal P\) 中最小素数，并假设 \(p\le T\)。Pakianathan–Winfree 的 scalar quota 定理对每一个不含最小权重顶点、且落入 shell

\[
q-w(p)\le w(F)<q
\]

的面给出一个球面。

在乘法专门化

\[
w(r)=\log r,
\qquad
q=\log(T+1)
\]

下，写

\[
c=\prod_{r\in F}r.
\]

shell 条件变为

\[
\frac{T+1}{p}\le c<T+1.
\]

因为 \(c\) 是整数，这恰好等价于

\[
\boxed{c\le T<pc.}
\]

这正是 L010 中不能被配对消去的截断穿越边。

若 \(|F|=s+1\)，对应球面维数为 \(s\)。它对约化 Euler 特征的贡献为

\[
(-1)^s,
\]

而

\[
\mu(pc)=(-1)^{s+2}=(-1)^s.
\]

所以 L010 不只是与 quota shell 定理“相似”：在有限素数支撑上，它就是该 shell 分解在 Euler 特征层面的无对数整数写法。

## 4. L015 —— Shell 维数的整数根约束

状态：`PROVED`

现在把成熟拓扑与进取数论的整数根层级接起来。

设 \(F\) 为维数 \(s\) 的 shell face，所以它包含除最小顶点 \(p\) 之外的 \(s+1\) 个素数。由于 \(p\) 最小，\(F\) 中每个素数都不小于 \(p\)。因此

\[
c=\prod_{r\in F}r\ge p^{s+1}.
\]

另一方面，每个 shell face 都满足 \(c\le T\)。所以

\[
p^{s+1}\le T,
\]

由精确整数根定义直接得到

\[
\boxed{p\le R_{s+1}(T).}
\]

这给出了一个完全不依赖实值渐近的维数过滤。

在 Legendre 应用中 \(T=2k\)，于是

\[
\boxed{p\le R_{s+1}(2k).}
\]

因此：

- 1 维 shell 球面对 Euler 特征贡献为负，只有在 \(p\le R_2(2k)\) 时才可能出现；
- 3 维负球面要求 \(p\le R_4(2k)\)；
- 5 维负球面要求 \(p\le R_6(2k)\)；
- 一般地，维数 \(2m-1\) 的奇维负 shell 球面必须满足 \(p\le R_{2m}(2k)\)。

L011 正是这一奇维结论的除数语言版本。

## 5. 剩余 parity 问题的同调形式

记

\[
\beta_s(G,T)
\]

为维数 \(s\) 的 shell 球面数量；在 scalar quota complex 的 bouquet 分解下，这也是对应维度的约化 Betti 秩。于是

\[
\boxed{
\sum_{\substack{d\mid G\\d>T}}\mu(d)
=
\sum_{s\ge0}(-1)^s\beta_s(G,T).
}
\]

因此，筛法 parity obstruction 得到了一个精确有限的拓扑版本：

> 控制偶维与奇维 shell 同调之间的平衡。

整数根约束本身还不能证明所需平衡，但它说明奇维同调并不是自由分布的：越高的奇维只能出现在越低的最小素数根壳层中。

所以，可以把原来一个混在一起的 parity 总和改写成双参数过滤：

\[
(\text{最小素数根壳层},\ \text{同调维数}).
\]

## 6. 下一轮攻击

当前最前沿的未解决负层已经变成 1 维 shell 同调，对应深度 3 的负截断除数

\[
b=pqr,
\qquad
qr\le2k<pqr.
\]

更高奇维会被 L015 自动进一步压向小 \(p\) 区域。

所以下一步压力测试目标应集中为：

1. 按最小素数 \(p\) 分类或配对 1 维 shell cycles；
2. 比较同一根壳层内的 1 维负 Euler 质量与 0 维、2 维正 shell 质量；
3. 检查 `根 = 截断 = k` 的自洽条件，是否会在这些 Betti 层之间制造一般 quota complex 不具备的额外关系；
4. 把仍未消去的负 shell 质量连接到 \(b\le k\) 的小模数差异区。

仅仅获得拓扑重述并不等于解决问题。真正的进展必须给出使用平方盆地/根—截断条件的新不等式、注入、递推或消去。

## 7. 可执行检查

`src/enterprise_math/cutoff_pairing.py` 与 `tests/test_cutoff_pairing.py` 现在在有限素数支撑上检查：

- shell 球面交替计数等于 Möbius 尾和；
- 按维数统计 shell 数量可重构约化 Euler 特征；
- 每个 shell 维数 \(s\) 都满足整数根约束 \(p\le R_{s+1}(T)\)；
- 对真实平方盆地合数，拓扑尾和与 L010 截断配对尾和完全一致。

quota-complex 同伦定理属于已引用的前人工作；有限测试不替代该定理，也不替代本文专门化恒等式的初等证明。
