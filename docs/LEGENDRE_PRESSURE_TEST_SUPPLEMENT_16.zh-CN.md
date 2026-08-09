# Legendre 压力测试 — 补充 16

状态：`ACTIVE RESEARCH NOTE`  
范围：first-factor cofactor windows 的精确跨 shell 分离  
依赖：canonical P017 cofactor-window 公式 L020–L027，以及 L051 lower-band root packing  
纪律：本文证明一个初等有限整数不等式。它**不证明** Legendre 猜想，也不使用素数分布估计。

## 1. 动机

L051 已经说明：在 lower least-factor band 中，一个下降后的 square-root index 最多只会收到两个 least-prime shells 的候选通道。

那是 root 坐标上的 packing 定理。下一步需要更细地问：

> 两个不同 first-prime shells，能否产生同一个 stripped cofactor 数值？

对一个 first-factor prime `p<=k`，把 shell state 写成

\[
n=pq,
\qquad
k^2<n<(k+1)^2.
\]

其精确 raw cofactor window 是

\[
\boxed{
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
}
\]

first-factor shell 就是在这个 raw interval 中保留 `p`-rough cofactors。

新的事实是：除了有限小盆地 `k=3`，这些 raw intervals 在施加 roughness 之前就已经两两不交。

---

## 2. L052 — Raw cofactor windows 严格分离

状态：`PROVED`。

设

\[
k\ge4,
\qquad
p<r\le k,
\]

其中 `p,r` 都是素数。

则

\[
\boxed{
\max W_r(k)<\min W_p(k).
}
\]

等价地，

\[
\boxed{
\left\lfloor\frac{k(k+2)}r\right\rfloor
\le
\left\lfloor\frac{k^2}p\right\rfloor.
}
\]

因此 first prime 越大，其 cofactor window 在整数 `q` 轴上越严格向下移动。

### 证明

只需证明

\[
\frac{k(k+2)}r\le\frac{k^2}p.
\]

所有量均为正，因此等价于

\[
p(k+2)\le rk,
\]

即

\[
\boxed{2p\le k(r-p).}
\]

分两种情况。

### 情形 1：`p=2`

因为 `r>p`，

\[
r-p\ge1.
\]

又因 `k>=4`，

\[
k(r-p)\ge k\ge4=2p.
\]

### 情形 2：`p>=3`

此时 `p,r` 均为奇素数，所以

\[
r-p\ge2.
\]

同时 `p<=k`，因此

\[
k(r-p)
\ge2k
\ge2p.
\]

故所有情形都有

\[
2p\le k(r-p),
\]

于是

\[
\frac{k(k+2)}r\le\frac{k^2}p.
\]

向下取整得到

\[
\left\lfloor\frac{k(k+2)}r\right\rfloor
\le
\left\lfloor\frac{k^2}p\right\rfloor
=
\min W_p(k)-1.
\]

因此

\[
\boxed{
\max W_r(k)<\min W_p(k).
}
\]

∎

---

## 3. k=3 是真实且最小的有限例外

条件 `k>=4` 不能直接删除。

当

\[
k=3
\]

时，

\[
W_2(3)=[5,7],
\qquad
W_3(3)=[4,5].
\]

二者在

\[
q=5
\]

相交。

对应原平方盆地中的两个 composite states：

\[
10=2\cdot5,
\qquad
15=3\cdot5,
\]

都严格位于 `3^2` 与 `4^2` 之间。

因此 `k=3` 是真实的最小 overlap witness，而不是证明技巧造成的边界。

---

## 4. 推论 — Least-factor stripping 跨 shell 单射

令

\[
I_k=\{k^2+1,\ldots,(k+1)^2-1\},
\qquad k\ge4.
\]

对 composite state `n in I_k`，令

\[
p=\operatorname{spf}(n),
\qquad
q=n/p.
\]

则映射

\[
\boxed{
\Psi_k(n)=q=n/\operatorname{spf}(n)
}
\]

在不同 first-prime shells 之间是单射的。

更具体地，若

\[
n_1=p_1q,
\qquad
n_2=p_2q,
\qquad
p_1\ne p_2,
\]

且每个 `p_i` 都是相应 state 的 least prime factor，那么同一个 `q` 必须同时落在 `W_{p_1}(k)` 和 `W_{p_2}(k)`。但 L052 已证明这些 windows 不交，因此不可能发生。

在同一个固定 shell 内，`n=pq -> q` 显然也是单射。

所以对 `k>=4`，整个平方盆地 composite states 的 least-factor stripping map 都是单射。

这比“first-factor shells 在原 state 空间里互不相交”更强：它说明它们的**quotient images 也互不相交**。

---

## 5. 与 L051 root-target packing 的关系

L051 是在 stripped cofactor 上再取 square-root coordinate 后工作的。

对 lower-band prime `p`，

\[
j_p
=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right),
\]

T110 把 cofactor root 限制到

\[
\{j_p,j_p+1\}.
\]

L051 证明：任意 target root index 最多只会收到两个 prime-shell channels。

L052 现在在更细的 q 坐标上补上：

\[
\boxed{
\text{即使两个 shells 共享一个 target root basin，它们的 exact q-subwindows 仍然不相交。}
}
\]

所以一个 target square basin 可以接收两个 parent shells 的局部片段，但这些片段是有序、互不重叠的整数子区间。

这正是 recursive capacity argument 需要的结构：不能再把每个 parent shell 粗暴扩大成整个 target square basin。

---

## 6. 与 T113 精确 branch threshold 的关系

P018-T113 已把一个 parent shell 内的 quotient-root response 写成原 basin offset 上的单一阈值。

因此每个 first prime `p` 的精确 cofactor window 最多被一个 root boundary 分成两段，分别进入 root basin `j_p` 与 `j_p+1`。

L052 又保证这些精确片段与其他 first-prime shells 产生的片段仍不重叠。

组合后 lower-band 有如下有限结构：

1. 每个 first-prime shell 对应一个 exact raw cofactor interval；
2. T113 最多在一个 root boundary 处分裂该 interval；
3. L051 说明一个 lower target root basin 最多只有两个 parent shells；
4. L052 说明这些 parent subwindows 在该 root basin 内不交。

所以 lower-band recursion 不是任意分叉树，而是一族进入严格更低 root scales 的**有序、互不重叠 exact subwindows**。

---

## 7. 为什么它仍然没有证明 Legendre

单射

\[
n\mapsto n/\operatorname{spf}(n)
\]

会把原来的 `2k` 个 basin states 映到数值范围更大的 cofactor 轴上。仅靠全局 injection 并不能得到有用的 cardinality deficit。

同样，如果把每个下降后的 target square basin 都按完整 basin size 计数，就会丢掉 exact-window 信息，把我们刚得到的增益全部抹掉。

真正有用的下一对象必须保留每个 descended root basin 内的**局部 occupancy ratio**。

对 target root `t`，定义 exact incoming cofactor pieces

\[
J_{p,t}(k)
=
W_p(k)\cap[t^2,(t+1)^2-1].
\]

由 L051，相关 lower-band primes `p` 至多两个；由 L052，这些 intervals 互不重叠。

所以下一个定量问题应当是：

> 一个 target square basin 中，这一到两个 exact incoming windows 的并集最多能占多大比例？再保留 parent `p`-rough 条件后，容量还能下降多少？

如果最终求和只是换坐标后的普通 Buchstab 账本，就应降级，而不能包装成突破。

---

## 8. 可执行验证

参考实现新增：

- `raw_cofactor_interval(k,p)`；
- `cofactor_window_pair_separation(k,p,r)`；
- `all_cofactor_windows_separated(k)`；
- `least_factor_strip_injection(k)`。

回归测试覆盖：

- bounded `k>=4` 上的严格 window 排序；
- `integer_gap=0` 的紧贴情形与正 gap 情形；
- 算术 margin `k(r-p)-2p>=0`；
- least-factor stripping 跨 shell 单射；
- sharp `k=3, q=5` 例外。

计算只用于实现审计；证明就是上面的有限整数不等式。

---

## 9. 当前结论

L051 与 L052 给出两种互补的跨 shell 约束：

\[
\boxed{
\text{root 坐标：每个 lower target root 最多两个 parent shells}
}
\]

以及

\[
\boxed{
\text{cofactor 坐标：}k\ge4\text{ 时 exact parent windows 两两不交。}
}
\]

再结合 T112 strict descent 与 T113 one-threshold splitting，lower-band geometry 已经从“对小素数做平坦求和”变成了一族良基下降的、精确且互不重叠的子窗口。

下一步应该直接攻击 target-basin local occupancy，而不是再引入新表示。
