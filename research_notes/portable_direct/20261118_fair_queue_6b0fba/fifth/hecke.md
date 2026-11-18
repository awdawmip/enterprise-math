# 142-B　辅助素数的无条件密度界与逐点解析界

输入素数为 $p$，稠密多项式次数为 $n$，$L=\lceil\log_2 p\rceil$，$B=20+(n+1)(L+1)$。在大特征分支 $p>B^{200000}$，每个素数 $q\le n$ 需要素数 $\ell\notin\{2,3,p,q\}$ 满足 $\ell\equiv1\bmod 12q$ 且 $p^{(\ell-1)/q}\not\equiv1\bmod\ell$。本文的无条件结论是几乎所有输入素数都能在很短的表内命中，且可同时覆盖该分支的所有允许次数。逐个输入的解析界另有明确假设。冻结此前的项目记录只指出 003 的域范围不足，未给下述分母分区与密度界。[冻结任务](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/RS-OAI7-142-B-20261007-6F2A81.md) · [原稿输入定义](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/sections/00-introduction.tex) · [原项目基线](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_notes/chatgpt_direct/20261007_oai7_6f2a81/RESEARCH.md)

## 无条件的同时辅助素数界

**定理。** 固定 $A>1$。对充分大的 $X$，除去 $[X,2X)$ 中至多 $2(\zeta(2)-1)X/(\log X)^A$ 个输入素数 $p$，其余每个 $p$ 对**所有**素数 $q\le X^{1/24}$ 同时有辅助素数

$$
\ell\ll_A\bigl(q(1+\log\log X)\bigr)^6 .
$$

当 $p>B^{200000}$ 时，$n<p^{1/200000}\le(2X)^{1/200000}<X^{1/24}$。因此同一批输入素数对每个允许的 $n$ 都有效。按素数定理，异常素数的相对比例为 $O_A((\log X)^{1-A})$。

**构造及计数。** 对每个 $q$ 设 $r=2+\lceil A\log\log X/\log q\rceil$。用 Bertrand 定理在 $r+2$ 和 $4(r+2)$ 之间选与 $12q$ 互素的素数 $t$，连续两个二倍区间给出两个选择，至多一个等于 $q$。对 $i=1,\ldots,r$ 取 $\ell_i\equiv1\bmod 12q$、$\ell_i\equiv i\bmod t$ 的最小素数。中国剩余定理给出模 $12qt$ 的可逆剩余类，经典无条件 Linnik 定理给 $\ell_i\ll (qr)^6$ 且各 $\ell_i$ 互异。这里把文献可用的 5.5 放宽为 6。[Heath-Brown](https://doi.org/10.1112/plms/s3-64.2.265) · [Xylouris 对指数的说明](https://arxiv.org/abs/0906.2749)

写 $Q_q=\prod_i\ell_i$。因为 $r\log q\le3\log q+A\log\log X$ 且 $r=O_A(\log\log X)$，有

$$
\log Q_q\le 18\log q+O_A\bigl(\log\log X\,(1+\log\log\log X)\bigr)
\le(3/4+o_A(1))\log X.
$$

于是 $Q_q<X$，每个输入素数 $p\ge X$ 对各 $\ell_i$ 可逆。在循环群 $\mathbf F_{\ell_i}^\times$ 中，$q$ 次幂子群指数恰为 $q$。此行全失的单位类正好有 $\varphi(Q_q)/q^r$ 个，每类在区间里至多有 $X/Q_q+1$ 个整数。故该行失败的**素数**数目至多 $2X/q^r$。对 $q$ 求并集，以 $q^{-r}\le q^{-2}(\log X)^{-A}$ 得证。计数无须对于增长的模数引用素数等分布。表长及每个候选的数值均受上述界控制，候选可由枚举同余类中的素数取得。

**固定表的精确密度。** 固定 $n$，每个 $q\le n$ 预选 $r_q$ 个不同候选，允许不同 $q$ 的表共用同一 $\ell$。输入素数中，所有行同时命中的相对自然密度恰为

$$
\prod_{\substack{q\le n\\ q\ {\rm prime}}}(1-q^{-r_q}).
$$

事实上每个 $\mathbf F_\ell^\times$ 中，$q$ 次幂判据只取决于离散对数模 $q$ 是否为零。对于同一 $\ell$ 上不同的素因子 $q$，这些坐标由中国剩余定理相互独立。再对不同 $\ell$ 作 CRT，并用固定模数的素数算术级数定理，即得精确乘积。每行两枚候选给出至少 $1/\zeta(2)=6/\pi^2$ 的密度。反过来，任意固定有限表都漏掉整条 $p\equiv1\bmod \prod_{\ell\ {\rm distinct}}\ell$ 上的素数，故不能据此得到每个 $p$ 的界。

## 域、导子与逐点估计

伴随稿 *Primitive roots for every admissible integer base* 的定理 1.2 按陈述覆盖任意包含 $\mu_{12}$ 的分圆域、该域上的每个有限阶 Hecke 特征，主特征允许在 1 有极点；宽度 $10^{-6}$ 与域、导子、高度均无关。证明先固定域和特征，原文允许估计起点随它们变化。其 §6 最后的 Mellin 延拓把数值节省与起点依赖分开。本次复核定理的量词及应用，没有独立验证该预印本的整条无零点证明链。经典对数型零点自由区依赖判别式、导子和高度，通常还要处理可能的例外实零点。003 的 $7/8$ 结论适用于 Dirichlet 特征及 $\mathbf Q(\sqrt{-3})$ 上的有限阶 Hecke 特征。[伴随稿定理及量词](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/01-introduction.tex) · [§6 的目标与起点](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/06-zero-free.tex) · [003 的原定理](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)

取 $K=\mathbf Q(\mu_{12q})$，$M=K(p^{1/q})$，假设 $p\nmid12q$。令 $d=\varphi(12q)$，在 $q=2,3$ 时分别为 8、12，在 $q\ge5$ 时为 $4(q-1)$。由于 $p$ 在 $K$ 不分歧，$X^q-p$ 在其每个上方素理想 Eisenstein，故 $[M:K]=q$ 且 $M/K$ 循环。$M/\mathbf Q$ 也正规。分圆判别式和幂基判别式给出

$$
\log D_K\le d\log(12q),\qquad
\log D_M\le q\log D_K+d[q\log q+(q-1)\log p].
$$

**最小阿贝尔基域。** 对每个中间域 $\mathbf Q\subseteq F\subseteq K$，$M/F$ 阿贝尔当且仅当 $\mu_q\subseteq F$。若包含，$M=K\cdot F(p^{1/q})$ 是两个阿贝尔扩张的合成。反过来，把 $\sigma\in\mathrm{Gal}(K/F)$ 提升到 $M$，其对 $\mathrm{Gal}(M/K)=\langle\tau\rangle$ 的共轭作用为 $\tau\mapsto\tau^{\chi_q(\sigma)}$，其中 $\tau(p^{1/q})=\zeta_qp^{1/q}$。若所有提升都交换，$\chi_q$ 恒等于 1，故 $\mu_q\subseteq F$。因此单以 003 声明为条件，$q=2$ 可从 $\mathbf Q$ 供给，$q=3$ 可从 $\mathbf Q(\sqrt{-3})$ 供给。$q\ge5$ 时两者均缺少 $\mu_q$，这条直接的阿贝尔因式分解失效。

**带宽到大小的计算。** 对 $0<\delta\le1/2$，假设 $\zeta_K,\zeta_M$ 在 $\Re s>1-\delta$ 都无零点。取固定非负光滑 $\varphi$，支集在 $(1,2)$ 且不恒为零，$\Phi(1)=\int\varphi$。令 $\Psi_F(x)=\sum_{\mathfrak p,j\ge1}\log N\mathfrak p\,\varphi((N\mathfrak p)^j/x)$。标准光滑显式公式给出的误差为 $O_\varphi(x^{1-\delta}(\log D_F+[F:\mathbf Q]))$。先乘 $q^{-1}$ 再估误差，取 $H=q\log(12pq)$，便有

$$
\Psi_K-q^{-1}\Psi_M=(1-q^{-1})x\Phi(1)+O_\varphi(x^{1-\delta}H).
$$

两侧同分裂的素理想项抵消，主项的差保留系数 $1-1/q$。对不分歧且相对惰性的 $\mathfrak p$，$q\mid j$ 的幂次也恰好抵消，其余幂次留下正权。要找到有理一级素数，在 $K$ 侧删去 $fj\ge2$ 的项，其中 $f$ 是有理惯性次数。其总量为 $O_\varphi(d\sum_{k\ge2,\,2^k\le2x}\vartheta((2x)^{1/k}))=O_\varphi(d\sqrt{x})$。这里用每个有理素数上方的 $f$ 之和至多 $d$、Chebyshev 初等界及 $x^{1/3}\log x=O(\sqrt x)$。再扣掉 $2,3,p,q$ 的一级项 $O_\varphi(d\log(2x))$，故可取

$$
\ell\ll_{\varphi,\delta} H^{1/\delta}.
$$

在原大特征范围 $H\ll B$。宽域伴随定理若成立，$\zeta_M$ 在 $K$ 上按 $q$ 个有限阶 Hecke 因子分解，得到逐点 $\ell\ll B^{1,000,000}$。若假设 GRH，则 $\ell\ll B^2$。单以 003 条带为条件，在 $q=2,3$ 已有 $\ell\ll(\log(2p))^8$。原稿给出的数字是宽域输入下的 $B^{20,000,000}$。这些均为数值大小界；$O$ 的常数依赖于固定光滑函数及固定带宽。对每个固定 $(p,q)$，经典 Chebotarev 无条件给出合格 $\ell$ 的密度 $(q-1)/(qd)$，因为所需 Frobenius 集合为正规子群 $\mathrm{Gal}(M/K)$ 的全部非单位元。这项定性结论本身不控制首枚素数的大小。[原稿 §10 的显式公式与分裂测试](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/sections/10-analytic.tex)

每个输入另有无条件但大得多的显式上界。Ahn–Kwon 的有效 Chebotarev 定理用于 $M/\mathbf Q$，取任意非单位 $\tau\in\mathrm{Gal}(M/K)$ 所在的共轭类，给出 $\ell\le D_M^{12577}$。该类的素数在 $K$ 全分裂，在 $M/K$ 不全分裂；$2,3,q$ 在 $K$ 分歧，$p$ 在 $M/K$ 分歧，因而被该定理的非分歧条件排除。代入判别式得无条件的逐点界 $\ell\le[(12q)^{dq}q^{dq}p^{d(q-1)}]^{12577}$。其对二进制输入 $p$ 的依赖与前面的多对数界相差甚远。[Ahn–Kwon 定理](https://doi.org/10.5802/aif.3274)

## 精确复核与开放边界

$q=2,3$ 共用 $\ell=73,433$，它们都为 $1\bmod72$。模 $31609$ 的 31,104 个单位类中，两行成功 20,736 类，仅二次行成功 2,592 类，仅三次行成功 6,912 类，两行全失 864 类。两行都中的比例恰为 $(1-2^{-2})(1-3^{-2})=2/3$。

另取 GIMPS 已认证的 $p=2^{82589933}-1$ 及 $n=13$。此时 $B=1,156,259,096<2^{31}$，满足 $p>B^{200000}$。表中 $\ell$ 是逐一排除更小候选后得到的最小值。脚本只用 $2^{82589933}\bmod\ell$ 计算剩余类；输入 $p$ 的素性使用原公告。[GIMPS 素性公告](https://www.mersenne.org/primes/press/M82589933.html)

| $q$ | 最小 $\ell$ | $p\bmod\ell$ | $p^{(\ell-1)/q}\bmod\ell$ |
|---:|---:|---:|---:|
| 2 | 193 | 82 | 192 |
| 3 | 109 | 22 | 45 |
| 5 | 181 | 139 | 42 |
| 7 | 337 | 168 | 79 |
| 11 | 397 | 148 | 167 |
| 13 | 157 | 58 | 46 |

逐点全覆盖仍有一个具体障碍。单取 $q=2$，因为 $\ell\equiv1\bmod4$，二次互反律给出 $(p/\ell)=(\ell/p)$。所以全输入的 $\ell\ll(\log p)^C$ 已蕴含任意充分大素数模 $p$ 的最小二次非剩余为多对数大小。上面的异常素数计数和单个大输入核验都没有解决这个逐点问题。本节只取辅助表为输出；代入完整分解算法还取决于原稿独立的代数归约。
