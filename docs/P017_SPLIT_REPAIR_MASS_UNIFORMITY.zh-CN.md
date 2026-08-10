# P017 —— Uniform Dyadic Split-Repair Mass

状态：`PROVED OWNER RESEARCH`  
归属：P017 / `program/p017-legendre`  
消费：P017 精确 cofactor window；P018 two-root quotient-basin transport；经典 Jacobsthal 与 continued-fraction discrepancy 结果  
边界：本定理研究复合数 least-prime shells 及其 cofactor-root repair burden，**不**证明 Legendre 猜想。

## 1. 研究量

固定 square-basin index \(k\ge2\)。对每个 prime \(p\le k\)，考虑真实 least-prime shell

\[
\mathcal L_p(k)
=
\{n:\ k^2<n<(k+1)^2,\ \operatorname{spf}(n)=p\}.
\]

写成 \(n=pq\)，并且只保留 cofactor 的 square-root index \(R_2(q)\)。

P018 已保证：固定 \(k,p\) 后，cofactor root 至多取两个相邻值。定义

\[
I_p(k)=
\begin{cases}
1,&\text{两个 root values 都被真实 }p\text{-rough cofactors 实现},\\
0,&\text{否则}.
\end{cases}
\]

定义 active split-repair mass

\[
\boxed{
S(k)=\sum_{\substack{p\le k\\p\ {\rm prime}}} I_p(k).
}
\]

因此 \(S(k)\) 正是实际需要 binary residual root coordinate 的 least-prime shells 数量。

## 2. 精确边界算术

令

\[
a=\left\lfloor\frac{k^2}{p}\right\rfloor,
\qquad
m=R_2(a)+1,
\qquad
\tau=pm^2-k^2.
\]

精确 open cofactor window 为

\[
W_p(k)
=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,\,
\left\lfloor\frac{k(k+2)}p\right\rfloor
\right].
\]

在下一个 square boundary \(m^2\) 处分开该窗口。边界下方与上方的 raw quotient slots 数量精确为

\[
\boxed{
L_p(k)
=
\left\lceil\frac{\tau}{p}\right\rceil-1,
}
\]

以及

\[
\boxed{
U_p(k)
=
\left\lfloor\frac{2k-\tau}{p}\right\rfloor+1.
}
\]

所以 raw two-root split 当且仅当

\[
\boxed{
p<\tau\le2k.
}
\]

真实 split 还要求两个非空 branch 中分别至少存在一个 \(p\)-rough quotient。

## 3. Beatty core

upper branch 非空当且仅当

\[
pm^2<(k+1)^2.
\]

与 \(pm^2>k^2\) 合并后，恰好等价于

\[
\boxed{
k=\lfloor m\sqrt p\rfloor.
}
\]

因此固定 \(p\) 时的 raw candidate indices 落在由 \(\sqrt p\) 生成的 Beatty sequence 上。

在 dyadic block

\[
K<k\le2K
\]

中，这类 Beatty candidates 数为

\[
\boxed{
\frac{K}{\sqrt p}+O(1).
}
\]

剩下的问题只是：lower-boundary 条件与 \(p\)-rough realizability 会删除其中多少 candidates。

## 4. Uniform rough-gap input

记

\[
P_{<p}
=
\prod_{\substack{r<p\\r\ {\rm prime}}}r,
\]

并令 \(H_p\) 为满足下述性质的最小正整数：任意 \(H_p\) 个连续整数中都存在一个与 \(P_{<p}\) 互素的整数，也就是一个 \(p\)-rough integer。

若 \(r=\pi(p-1)\)，则 \(H_p\) 正是前 \(r\) 个 primes 的 primorial Jacobsthal function。

Iwaniec 的经典 Jacobsthal 定理给出

\[
h(r)\ll(r\log r)^2.
\]

再结合标准 prime-counting bound \(r\log r\ll p\)，得到 uniform consequence

\[
\boxed{
H_p\ll p^2.
}
\]

这是前人数学；P017 只把它作为 moving cofactor branches 的统一 occupancy certificate。

## 5. 每一个 realizability failure 都被压到端点

取一个 Beatty candidate

\[
k=\lfloor m\sqrt p\rfloor
\]

并写

\[
\delta=m\sqrt p-k\in(0,1).
\]

则

\[
\boxed{
\tau
=
pm^2-k^2
=
\delta(2k+\delta).
}
\]

再定义 upper square-boundary defect

\[
D=(k+1)^2-pm^2.
\]

则

\[
\boxed{
D
=
(1-\delta)(2k+1+\delta).
}
\]

假设 \(K<k\le2K\)。若 lower branch 中不存在 \(p\)-rough integer，则它的长度必然小于 \(H_p\)，因此

\[
\tau\le pH_p
\]

并得到

\[
\boxed{
\delta
\le
\frac{pH_p}{2K}.
}
\]

同理，若 upper branch 不存在 \(p\)-rough integer，则

\[
D\le pH_p
\]

并得到

\[
\boxed{
1-\delta
\le
\frac{pH_p}{2K}.
}
\]

所以 Beatty core 中任何没有真实 split 的 candidate，其 \(\{m\sqrt p\}\) 都必须进入 0 或 1 附近的两个 endpoint intervals；总长度只有

\[
O\!\left(\frac{pH_p}{K}\right).
\]

这一步正是对 L082 固定-\(p\) Pell constant 的 uniform 替代。

## 6. Uniform square-root rotation discrepancy

\(\sqrt p\) 的 continued fraction 是周期的，且所有非初始 partial quotients 都不超过 \(2\lfloor\sqrt p\rfloor\)。

因此，对任意 interval \(J\subset[0,1)\) 以及任意连续的 \(M\) 个 multiplier，标准 Ostrowski / Denjoy--Koksma 分解给出

\[
\boxed{
\#\{m:\{m\sqrt p\}\in J\}
=
M|J|
+
O(\sqrt p\log(2M)).
}
\]

implied constant 可以取 absolute constant。

证明路线是：先用 Ostrowski expansion 把长度 \(M\) 分解为 convergent-denominator blocks；Denjoy--Koksma 用 bounded variation 控制每个 denominator block 的 interval discrepancy；由于 partial quotients 为 \(O(\sqrt p)\)，而 convergent denominators 至少按 Fibonacci 速度增长，所以所有 Ostrowski digits 之和为 \(O(\sqrt p\log M)\)。

这里不引入随机性。

## 7. Uniform fixed-prime dyadic lower bound

在 \(K<k\le2K\) 中，相关 multiplier block 长度满足

\[
M=\frac{K}{\sqrt p}+O(1).
\]

将第 6 节用于第 5 节的两个 failure intervals。记 \(E_p(K)\) 为 dyadic block 内 Beatty candidates 中没有真实 split 的数量，则

\[
E_p(K)
\ll
M\frac{pH_p}{K}
+
\sqrt p\log K.
\]

因此

\[
\boxed{
E_p(K)
\ll
H_p\sqrt p
+
\sqrt p\log K.
}
\]

再用 \(H_p\ll p^2\)，得到

\[
\boxed{
E_p(K)
\ll
p^{5/2}
+
\sqrt p\log K.
}
\]

所以在后文使用的 growing-\(p\) 区间里可以统一写成

\[
\boxed{
\sum_{K<k\le2K} I_p(k)
\ge
\frac{K}{\sqrt p}
-
C\left(p^{5/2}+\sqrt p\log K+1\right),
}
\]

有限个小情形吸收到一个 absolute constant \(C\) 中。

## 8. P017-SRMU-T01 —— Polynomial dyadic mean growth

状态：`PROVED`。

存在常数 \(c>0\) 与 \(K_0\)，使所有 \(K\ge K_0\) 满足

\[
\boxed{
\sum_{K<k\le2K}S(k)
\ge
c\,\frac{K^{7/6}}{\log K}.
}
\]

等价地，

\[
\boxed{
\frac1K
\sum_{K<k\le2K}S(k)
\gg
\frac{K^{1/6}}{\log K}.
}
\]

### 证明

取

\[
Y=c_0K^{1/3}
\]

其中 \(c_0>0\) 是足够小的固定常数。因为 \(S(k)\) 至少包含全部 \(p\le Y\) 的 prime contributions，

\[
\sum_{K<k\le2K}S(k)
\ge
\sum_{p\le Y}
\sum_{K<k\le2K}I_p(k).
\]

第 7 节给出

\[
\sum_{K<k\le2K}S(k)
\ge
K\sum_{p\le Y}\frac1{\sqrt p}
-
C\sum_{p\le Y}p^{5/2}
-
C\log K\sum_{p\le Y}\sqrt p
-
C\pi(Y).
\]

标准 prime-counting estimates 给出

\[
\sum_{p\le Y}\frac1{\sqrt p}
\gg
\frac{\sqrt Y}{\log Y},
\]

\[
\sum_{p\le Y}p^{5/2}
\ll
\frac{Y^{7/2}}{\log Y},
\]

以及

\[
\sum_{p\le Y}\sqrt p
\ll
\frac{Y^{3/2}}{\log Y}.
\]

因此主项为

\[
\gg
c_0^{1/2}
\frac{K^{7/6}}{\log K}.
\]

第一项误差具有相同的 \(K\)-幂次，但它的系数只有 \(O(c_0^{7/2})\)。把 \(c_0\) 取到足够小，即可让该误差小于主项的一半；其他误差都是 \(o(K^{7/6}/\log K)\)。定理成立。∎

## 9. P017-SRMU-C01 —— Polynomial pointwise limsup

由 dyadic mean theorem，

\[
\boxed{
\max_{K<k\le2K}S(k)
\gg
\frac{K^{1/6}}{\log K}.
}
\]

因此存在无限多个 basin indices \(k\)，满足

\[
\boxed{
S(k)
\gg
\frac{k^{1/6}}{\log k}.
}
\]

所以 active binary root-repair support 不只是无界，而是在一条无限子序列上达到 polynomial scale。

## 10. Repair-spectrum consequence

每个 least-prime shell 内，cofactor root 最多只有两个值。因此 factor-to-root refinement 的 local split multiplicity 只能是 1 或 2。

于是 \(S(k)\) 同时等于：

- 真正发生 split 的 factor blocks 数；
- factor/root joint class count 相对于 factor-only class count 的增量；
- second binomial repair-spectrum mass。

所以 T01 的同一 dyadic lower bound 同时作用于这三个量。

这是对 A2 repair-spectrum 的 consumer interpretation；T01 的证明本身只使用 P017 arithmetic 与经典 rough-gap / discrepancy 输入。

## 11. P017-SRMU-T02 —— Rough-gap exponent transfer principle

前面的证明还给出一条可复用 transfer law。

假设未来能够得到某个统一 \(p\)-rough gap guarantee

\[
\boxed{
H_p\ll p^\theta
}
\]

其中 \(\theta>0\) 为固定常数。

则第 7 节自动变成

\[
E_p(K)
\ll
p^{\theta+1/2}
+
\sqrt p\log K.
\]

取

\[
Y=c_0K^{1/(\theta+1)}.
\]

相同求和立即得到

\[
\boxed{
\frac1K
\sum_{K<k\le2K}S(k)
\gg
\frac{K^{1/(2(\theta+1))}}{\log K}.
}
\]

因此任何 uniform rough-gap exponent 的改善，都会机械地转化成更强的 split-repair mass exponent。

当前 Jacobsthal exponent \(\theta=2\) 正好给出上面的 \(1/6\)。

## 12. 本定理没有证明什么

本定理**不**给出 \(S(k)\) 的 pointwise asymptotic formula。

它**不**把 fixed-prime finite-pattern independence 自动升级为 growing prime cutoff 的 simultaneous theorem。

它**不**声称每个 basin 中有正比例的 prime shells 都 split。

它**不**证明每个 consecutive-square basin 中存在 prime。

它证明的是另一件结构性事实：local binary repair alphabet 可以永远只有两个 symbols，但真正需要这个 repair 的 coarse blocks 数量，在 dyadic 平均意义下具有 polynomial lower bound。

## 13. Prior-art boundary

以下输入均属于经典前人数学：

- Jacobsthal function，以及 Iwaniec 的 asymptotic upper bound \(h(r)\ll(r\log r)^2\)；
- quadratic irrational 的 continued fractions；
- Ostrowski expansion 与 Denjoy--Koksma rotation discrepancy；
- 标准 prime-counting estimates。

项目特有对象是由精确 P017 cofactor-root boundary calculus 强制出来的 split-repair mass \(S(k)\)。这一综合方式及其 exponent 的历史新颖性仍未验证。

## 14. Executable specification

- `src/enterprise_math/p017_split_repair_mass_uniformity.py`
- `tests/test_p017_split_repair_mass_uniformity.py`

可执行层验证 exact branch-slot formulas、Beatty-core equivalence、actual/raw filtering 与 bounded dyadic counts。它不以有限计算代替 asymptotic theorem 的普通证明。
