# Legendre 压力测试 —— 补充 05

状态：`ACTIVE RESEARCH NOTE`  
范围：完整平方盆地 smooth-tail 化约、精确 first-factor cofactor window、quotient-transport 窗口增长，以及正项 rough-window 素数计数恒等式  
依赖：P017 L001–L019 与 P018 factor-precision 结果  
纪律：**本文不证明 Legendre 猜想。** Rough number、最小素因子分割、smooth part 与 trial-division 逻辑都是成熟数论。项目要检验的是：它们在平方盆地中的精确有限组织是否能产生新的证明杠杆。

## 1. 审计：最近引入的哪些东西值得留下？

最近的压力测试引入了多种数学上成立的结构，但它们不应获得相同的基础地位。

本补充只保留能够直接压缩 P017 证明问题的部分：

1. 精确有限 factor horizon 与 least-factor partition；
2. 平方盆地状态的完整 `k`-smooth core；
3. 每个 first-factor shell 的精确 cofactor interval；
4. 该 interval 如何扩张的精确 quotient-transport / carry 描述；
5. 剩余素因子数量的 integer-root depth 上界。

以下内容降为特例或证明语言：

- centered symmetric prime pair —— 只在一般 cofactor window 已退化到两个 raw candidate 时有用；
- carry cocycle / cohomology —— 属于成熟代数语言；只有 quotient-defect transport 再次出现在平方盆地窗口宽度中时才保留其实际用途；
- threshold topology / Alexander duality —— 继续作为独立的前人工作化约工具，而不升格为底层本体；
- CRT/idempotent 等坐标编码 —— 只有产生新上界时才继续使用。

现在采用的规则是：

> **只有当一个新结构能缩短精确有限障碍，或在已有 P017/P018 层之间搬运有用信息时，才值得保留。**

---

## 2. L020 —— 平方盆地 smooth-tail 二分

状态：`PROVED`。

对

\[
k^2<n<(k+1)^2,
\]

定义完整 `k`-smooth core：

\[
S_k(n)=\prod_{p\le k}p^{v_p(n)},
\]

以及剩余 tail：

\[
Q_k(n)=\frac{n}{S_k(n)}.
\]

则

\[
\boxed{
Q_k(n)=1
\quad\text{或}\quad
Q_k(n)\text{ 是一个 }>k\text{ 的素数}.
}
\]

### 证明

按定义，`Q_k(n)` 的每个素因子都严格大于 `k`。

若 `Q_k(n)>1` 且为合数，则按重数至少含两个素因子，每个至少为 `k+1`。因此

\[
Q_k(n)\ge(k+1)^2.
\]

但

\[
Q_k(n)\le n<(k+1)^2,
\]

矛盾。∎

### 素性推论

对平方盆地状态，

\[
\boxed{
n\text{ 为素数}
\iff
S_k(n)=1.
}
\]

所以每个合数盆地状态都由以下两部分组成：

- 一个非平凡 `k`-smooth core；
- 再乘以 `1`，或者恰好一个大于 `k` 的素数 tail。

这比只记录 square-free small-prime support 更强，因为所有小素数重数都被保留。

---

## 3. L021 —— first-factor shell 的精确中心化 cofactor window

状态：`PROVED`。

令 `p<=k` 为素数，`L_p(k)` 表示平方盆地中最小素因子恰为 `p` 的状态。

设

\[
c=k+1,
\qquad
r=c-p,
\qquad
p=c-r.
\]

`L_p(k)` 中每个状态都可写成

\[
n=pq.
\]

则平方盆地条件

\[
(c-1)^2<pq<c^2
\]

等价于如下精确有限 cofactor window：

\[
\boxed{
q_{\min}
=
c+r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor
}
\]

以及

\[
\boxed{
q_{\max}
=
c+r+\left\lfloor\frac{r^2-1}{p}\right\rfloor.
}
\]

### 下端点

由 `pq>(c-1)^2`，

\[
q
\ge
\left\lfloor\frac{(c-1)^2}{p}\right\rfloor+1.
\]

利用 `c=p+r`，

\[
(c-1)^2
=(p+r-1)^2
=p(p+2r-2)+(r-1)^2,
\]

所以

\[
\left\lfloor\frac{(c-1)^2}{p}\right\rfloor+1
=
p+2r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor
=
c+r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor.
\]

### 上端点

由 `pq<c^2`，在整数中

\[
q\le\left\lfloor\frac{c^2-1}{p}\right\rfloor.
\]

再次利用 `c=p+r`，

\[
c^2-1
=p(p+2r)+(r^2-1),
\]

于是

\[
\left\lfloor\frac{c^2-1}{p}\right\rfloor
=
p+2r+\left\lfloor\frac{r^2-1}{p}\right\rfloor
=
c+r+\left\lfloor\frac{r^2-1}{p}\right\rfloor.
\]

这个 window 对任意素数 shell `p<=k` 都精确成立，不使用 near-diagonal 假设。

---

## 4. L022 —— first-factor shell 恰等于 p-rough cofactor window

状态：`PROVED`。

称整数 `q` 为 **p-rough**，若它不存在严格小于 `p` 的素因子。

则

\[
\boxed{
L_p(k)
=
\left\{
pq:
q_{\min}\le q\le q_{\max},
\ q\text{ 为 p-rough}
\right\}.
}
\]

### 证明

若 `n=pq` 属于 `L_p(k)`，L021 把 `q` 放入上述窗口。若 `q` 有素因子 `<p`，该因子也整除 `n`，与 `p` 是最小素因子矛盾，所以 `q` 必为 `p`-rough。

反过来，设 `q` 位于精确窗口且为 `p`-rough。L021 给出

\[
k^2<pq<(k+1)^2.
\]

该状态被 `p` 整除，而 `q` 没有比 `p` 更小的素因子；因子 `p` 本身当然也没有。因此 `pq` 的最小素因子恰为 `p`，故 `pq in L_p(k)`。∎

这是本补充的核心化约：

> shell 的几何部分现在只是一个短而显式的整数区间；剩余算术障碍恰好是这个区间内的 roughness。

---

## 5. L023 —— 中心 correction coordinate 与平方边界 offset

状态：`PROVED`。

把候选 cofactor 写成

\[
q=c+r+j.
\]

由 L021，correction coordinate 的范围为

\[
\boxed{
j_{\min}
=-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor}
\]

到

\[
\boxed{
j_{\max}
=\left\lfloor\frac{r^2-1}{p}\right\rfloor.}
\]

因为 `p=c-r`，

\[
pq=(c-r)(c+r+j)=c^2-r^2+jp.
\]

所以到两个平方边界的余量分别精确为

\[
\boxed{
c^2-pq=r^2-jp}
\]

以及

\[
\boxed{
pq-(c-1)^2=p(j+2)-(r-1)^2.}
\]

因此偏离对称乘积 `c^2-r^2` 的量并不是模糊误差，而是整数 correction `jp`。

centered-prime 公式只对应特殊情形 `j=0`。

---

## 6. L024 —— raw window 宽度是精确 quotient-transport 事件

状态：`PROVED`。

在施加 `p`-rough 过滤前，raw integer cofactor 的数量为

\[
N_{\mathrm{raw}}
=q_{\max}-q_{\min}+1.
\]

由 L021，

\[
\boxed{
N_{\mathrm{raw}}
=
2
+
\left\lfloor\frac{r^2-1}{p}\right\rfloor
-
\left\lfloor\frac{(r-1)^2}{p}\right\rfloor.
}
\]

令

\[
a=(r-1)^2,
\qquad
h=2r-2.
\]

则

\[
a+h=r^2-1,
\]

所以

\[
\boxed{
N_{\mathrm{raw}}
=
2+\left(\left\lfloor\frac{a+h}{p}\right\rfloor-\left\lfloor\frac a p\right\rfloor\right).
}
\]

括号中的量正是状态增加 `h` 后 quotient 的精确 transport。

写成

\[
a=pA+u,
\qquad
h=pH+v,
\qquad
0\le u,v<p,
\]

可直接得到整数分解

\[
\boxed{
N_{\mathrm{raw}}
=
2
+
\left\lfloor\frac{2r-2}{p}\right\rfloor
+
\kappa_p
\left(
(r-1)^2\bmod p,
(2r-2)\bmod p
\right),
}
\]

其中

\[
\kappa_p(u,v)=\left\lfloor\frac{u+v}{p}\right\rfloor\in\{0,1\}.
\]

因此 cofactor-window 增长只有两部分：

\[
\boxed{
\text{确定性的整块增长}
+
\text{一次剩余边界 carry}.
}
\]

这正是 P018 审计后仍值得复用的 finite defect-transport 模式。上述公式在本文中直接证明，因此并不依赖那条分支的术语是否已经进入规范主干。

---

## 7. L025 —— 两/三候选区间与 symmetric-prime 退化

状态：`PROVED`。

### 两个或三个 raw candidates

若

\[
p>2(r-1),
\]

则

\[
\left\lfloor\frac{2r-2}{p}\right\rfloor=0.
\]

由 L024，

\[
\boxed{N_{\mathrm{raw}}\in\{2,3\}.}
\]

究竟是哪一个值，完全由剩余 boundary carry 决定。

### 强 near-diagonal 情形

若更强地满足

\[
\boxed{p>r^2},
\]

则 L021 中两个 floor 项都归零。因此

\[
\boxed{
q\in\{c+r-1,c+r\}.
}
\]

当 `p>=3` 时，素数 `p=c-r` 为奇数。所以 `c+r=p+2r` 为奇数，而 `c+r-1` 为偶数。由于 shell cofactor 必须 `p`-rough 且大于 `p`，这个偶数候选不可能存活。

另外 `p>r^2` 推出

\[
c+r=p+2r<p^2,
\]

所以 `c+r` 不可能是 `p`-rough 合数：任意大于 `p` 的 `p`-rough 合数至少为 `p^2`。

因此

\[
\boxed{
L_p(k)\ne\varnothing
\iff
c+r\text{ 为素数},
}
\]

且此时

\[
\boxed{
L_p(k)=\{(c-r)(c+r)\}
=\{c^2-r^2\}.
}
\]

因此此前研究的 centered-prime radius 不是独立基础对象，而是**一般 cofactor window 的双候选退化**。

### 边界例子：k=10

取

\[
k=10,
\quad c=11,
\quad p=7,
\quad r=4.
\]

L021 给出

\[
q\in\{15,16,17\}.
\]

其中只有 `17` 是 `7`-rough，所以

\[
L_7(10)=\{7\cdot17\}=\{119\}.
\]

这里 centered-prime 特例公式失败，是因为 `7>4^2` 不成立；但一般 cofactor-window 定理仍然完全精确。

---

## 8. L026 —— Integer-root depth 限制剩余素因子数量

状态：`PROVED`。

令

\[
U=(k+1)^2-1.
\]

设 `p` 是某个 shell 状态的最小素因子，并且

\[
\boxed{p^{m+1}>U.}
\]

等价地，

\[
p>R_{m+1}(U).
\]

则每个 `n in L_p(k)` 都满足

\[
\boxed{\Omega(n)\le m,}
\]

其中 `Omega` 按重数计素因子个数。

### 证明

若 `Omega(n)>=m+1`，由于 `n` 的所有素因子都至少为最小素因子 `p`，有

\[
n\ge p^{m+1}>U.
\]

但每个盆地状态满足 `n<=U`，矛盾。∎

因为 `n=pq`，cofactor 还满足

\[
\boxed{\Omega(q)\le m-1.}
\]

所以提高 least-factor precision 会产生一个精确有限层级：

\[
\text{一般 p-rough cofactor}
\to
\text{有界 factor depth}
\to
\text{prime cofactor}
\to
\text{symmetric-prime 退化}.
\]

---

## 9. L027 —— 正项 rough-window 素数计数恒等式

状态：`PROVED REINDEXING`。

开放平方盆地恰含 `2k` 个状态。

每个合数状态恰属于一个 first-factor shell `L_p(k)`，其中 `p<=k` 为素数。因此

\[
\Pi(k)
=
2k-
\sum_{p\le k}|L_p(k)|.
\]

代入 L022 得

\[
\boxed{
\Pi(k)
=
2k-
\sum_{p\le k}
\#\left\{
q\in[q_{\min}(k,p),q_{\max}(k,p)]
:
q\text{ 为 p-rough}
\right\}.
}
\]

于是 Legendre 猜想等价于正项不等式

\[
\boxed{
\sum_{p\le k}
\#\{q\in W_p(k):q\text{ p-rough}\}
\le2k-1.
}
\]

因为合数按唯一最小素因子分割，这个表示中不再出现 Möbius 符号。

这只是重述，不是证明。它的诊断价值在于：平方几何被压缩成精确有限窗口以后，剩余障碍被单独暴露出来。

---

## 10. 现在几何上已经解决什么，真正困难还在哪里？

first-factor shell 的平方盆地几何已经不再开放：

- 精确 cofactor endpoints 已知；
- 精确 square offsets 已知；
- 精确 raw candidate count 已知；
- window widening 有精确 bulk-plus-carry law；
- 高 least-factor shell 有有界 `Omega` depth；
- centered-prime 公式已被理解成极限退化。

真正困难现在被精确定位为：

\[
\boxed{
\text{控制所有精确窗口 }W_p(k)\text{ 中 p-rough survivors 的总数量。}
}
\]

若要沿此路线证明 Legendre，必须对这个 total survivor count 得到真正新的上界。只是重新命名 roughness、逐项使用 inclusion-exclusion，或者把同一个 parity barrier 换一种记号带回来，都不算推进。

## 11. 下一步攻击

后续方向故意收窄为以下几项。

1. **递归 rough-window factorization。** 若 `p`-rough cofactor `q` 仍为合数，暴露它的最小因子 `p_2>=p`，继续推导下一层精确 finite factor/cofactor window，而不是马上退回全局 inclusion-exclusion。
2. **Root-depth aggregation。** 按允许的 `Omega` depth 汇总高 `p` shell，从 semiprime 层开始。
3. **Smooth-core coupling。** 用 L020 检验可选的单个 `>k` prime tail 能否与完整 `k`-smooth core 分离，同时保留共同 square-center 约束。
4. **Defect-transport 复用。** 只有当 P018 transport calculus 真正产生像 L024 这样的 shell-count 或 boundary-crossing 恒等式时才引入；不把整套 P018 术语搬进 P017。
5. **Counterexample-first gate。** 任意针对 total rough-window count 的新上界都必须先经过有限盆地反例压力测试，再升格为定理候选。

因此研究线现在只剩更少的对象：

\[
\boxed{
\text{square basin}
\to
\text{least-factor shell}
\to
\text{exact cofactor window}
\to
\text{p-rough survivors}
\to
\text{root-depth recursion}.
}
\]
