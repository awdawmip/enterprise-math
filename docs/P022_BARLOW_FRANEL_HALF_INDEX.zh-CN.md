# P022 — Franel 半指标整除与无限复合边界见证族

状态：`ACTIVE RESEARCH NOTE / PROVED INFINITE SUBFAMILY / PRIOR-ART INPUT EXPLICIT`  
Owner：`program/p022-geometry-v2`  
依赖：Franel p-Lucas / rank 分析；低阶 Franel-defect 约化  
跨路线相关：P011 collision identifiability；A2/P023 witness precision；P018 defect/holonomy 语言

## 1. 问题

Barlow 低阶识别问题已经约化为纯 Franel defects 的乘法独立性：

\[
2,\qquad D_n\quad(2n-1\text{ 为合数}).
\]

一个很强的充分路线，是为每个相关 `F_n` 找到 primitive prime divisor；但这比当前已经证明的内容强得多。

本笔记先证明一个较弱但真正无限的结论：存在无限多个 **composite-boundary** 指标 `n`，使 `F_n` 有一个规范的

\[
p=2n+1
\]

型素因子。

证明使用经典 Jarvis--Verrill Franel 镜像同余，而不是继续扩大有限 determinant。

---

## 2. Prior art：Franel 镜像同余

记

\[
F_k=\sum_{j=0}^k\binom{k}{j}^3.
\]

Jarvis 与 Verrill 已证明：对任意素数 `p` 与 `0<=k<=p-1`，

\[
\boxed{
F_k\equiv(-8)^kF_{p-1-k}\pmod p.
}
\]

这是已有数学成果。

P022 在这里所做的是：利用反射不动的半指标与剩余类算术，把该同余转化为 Barlow 低阶识别中 **复合 defect 一侧**的无限见证族。

---

## 3. P022-LI12 — 半指标强制为零

令 `p` 为奇素数，并设

\[
n=\frac{p-1}{2}.
\]

半指标在反射下不动：

\[
p-1-n=n.
\]

因此 Jarvis--Verrill 同余给出

\[
F_n\equiv(-8)^nF_n\pmod p.
\]

由 Euler 判别法，

\[
(-8)^n
=(-8)^{(p-1)/2}
\equiv\left(\frac{-8}{p}\right)
=\left(\frac{-2}{p}\right)
\pmod p.
\]

而标准二次特征公式为

\[
\left(\frac{-2}{p}\right)
=
\begin{cases}
+1,&p\equiv1,3\pmod8,\\
-1,&p\equiv5,7\pmod8.
\end{cases}
\]

因此若

\[
p\equiv5,7\pmod8,
\]

则

\[
F_n\equiv-F_n\pmod p.
\]

因为 `p` 为奇数，得到

\[
\boxed{
p\mid F_{(p-1)/2}.}
\]

这是严格定理。

注意：这里**不声明逆命题**。当 `p≡1,3 mod 8` 时，镜像因子为 `+1`，该同余本身只是不再强迫半指标为零。

---

## 4. P022-LI13 — 无限多个见证真正落在 composite defect 一侧

现在要求 Barlow defect 边界

\[
2n-1
\]

为合数。

取素数

\[
p\equiv5\ \text{或}\ 23\pmod{24},
\qquad p>5,
\]

并仍令

\[
n=\frac{p-1}{2}.
\]

这两个剩余类都满足

\[
p\equiv5,7\pmod8,
\]

所以 LI12 给出

\[
p\mid F_n.
\]

同时它们满足

\[
p\equiv2\pmod3.
\]

因此

\[
2n-1=p-2\equiv0\pmod3.
\]

且因 `p>5`，有 `p-2>3`，所以

\[
\boxed{2n-1\text{ 为合数}.}
\]

于是每个 `p>5`、`p≡5` 或 `23 mod 24` 的素数，都给出一个真正的 composite-boundary segment

\[
n=(p-1)/2
\]

以及规范见证

\[
\boxed{p=2n+1\mid F_n.}
\]

由算术级数中的 Dirichlet 素数定理，这两个互素剩余类中都有无穷多个素数，因此：

\[
\boxed{
\text{存在无限多个 composite-boundary }n
\text{ 满足 }(2n+1)\mid F_n.
}
\]

这是当前 density-one composite 一侧得到的第一条无限算术 family；它并没有解决所有 composite indices。

---

## 5. P022-LI14 — Franel 零位集合的镜像对称

因为 `(-8)^k` 模 `p` 永不为零，同一镜像同余立即给出

\[
\boxed{
F_k\equiv0\pmod p
\iff
F_{p-1-k}\equiv0\pmod p.
}
\]

因此零位集合

\[
Z_p=\{1\le k\le p-1:p\mid F_k\}
\]

关于

\[
k\mapsto p-1-k
\]

对称。

当 `p≡5,7 mod 8` 时，半指标本身属于 `Z_p`，所以 Franel rank of apparition 满足

\[
\boxed{r_p\le\frac{p-1}{2}.}
\]

结合 p-Lucas，这说明这两个剩余类中的素数都不是 Franel Lucas-Type-I prime：其 digit table 至少存在一个零位。

---

## 6. Primitive-divisor 边界是真实存在的

LI12 **不意味着** `p=2n+1` 在 `F_n` 中是 primitive divisor。

最小且有用的警告例子是

\[
p=29,\qquad n=14.
\]

半指标定理给出

\[
29\mid F_{14},
\]

但实际上更早已经有

\[
29\mid F_{12}.
\]

所以

\[
r_{29}=12<14.
\]

因此只能写

\[
\text{forced half-index divisor}
\not\Rightarrow
\text{primitive divisor}.
\]

这一点非常重要，因为 primitive-divisor criterion 足以把整个 defect family 三角化，而 LI13 目前只提供无限多个严格的局部整除见证。

---

## 7. 更强的 defect valuation 规律——目前仅为猜想

精确压力测试显示，在已测试的 LI13 family 中似乎总有

\[
\boxed{v_p(D_{(p-1)/2})=1}.
\]

即便 `p` 并不是 `F_n` 的 primitive prime，这个规律仍然出现。例如 `p=29` 早已整除 `F_12`，但 `n=14` 的 pure defect 对 29 的 valuation 仍为 1。

这比 LI13 强得多，因为它意味着 canonical A-elimination 并没有把半指标素数见证消掉。

目前 P022 **没有无限证明**，因此该命题保持：

`CONJECTURAL / PRESSURE-TEST TARGET`。

真正有价值的证明路线应来自 Franel mirror / recurrence / p-Lucas 或 transfer-defect holonomy，而不是继续机械扩大 finite determinant cutoff。

---

## 8. 对全局研究策略的改变

现在 composite 一侧已经不再完全是黑箱。

当前至少有三类机制：

1. `2n-1` 为素数：中央二项式 A-side 自动新 pivot；
2. `2n+1` 为 `5` 或 `23 mod 24` 的素数：在 composite A-boundary 上得到强制 Franel divisor；
3. 任意 composite index：pure Franel defect `D_n`，其全局独立性仍开放。

第二类给出了 composite regime 内无限多个严格锚点，因此可以开始研究局部 Franel 同余如何与 defect transfer map 相互作用。

下一高价值目标是：证明或否定上述 one-unit defect valuation 是否对这一无限 family 恒成立，然后再寻找是否存在其他非 midpoint 的剩余类 family。

---

## 9. Prior-art / novelty 边界

已有输入包括：

- Jarvis--Verrill 的 Franel 镜像同余；
- Euler 判别与 `(-2/p)` 的标准二次特征公式；
- 算术级数中素数的 Dirichlet 定理。

P022 特定贡献是：

- 把半指标同余接入 composite-boundary Franel-defect 研究；
- 提取 `5,23 mod 24` 两个剩余类形成无限 composite-boundary witness family；
- 严格区分已证明整除、primitive-divisor 条件与更强 defect-valuation 猜想。

这一组合的历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

新增：

- `src/enterprise_math/p022_barlow_franel_half_index.py`；
- `tests/test_p022_barlow_franel_half_index.py`。

测试从 Franel 精确整数直接重建小素数下的镜像同余，核验强制半指标剩余类与 composite-boundary 算术，并保留 `p=29` 作为明确的非 primitive 边界例子。
