# Legendre 压力测试 — 补充 19

状态：`PROVED RESEARCH NOTE`  
范围：lower-band 精确窗口 root separation 及其真实 shell 推论  
依赖：P017 L051–L054、P007 quotient-window transport 补充 01、P023 image-separation 补充 08、P018 T113  
纪律：只使用有限整数不等式；不使用素数分布估计，也不声称证明 Legendre 猜想。

## 1. 为什么重新检查 L052

对 lower-band prime `p`，L052 把可能 root 输出扩大为一个两点候选集，并证明只有从 `k>=15` 起才统一跨 shell 分离。

L054 提供了更多信息：剥离 `p` 后，每个可能 cofactor 都落在精确 raw interval

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}p\right\rfloor
\right].
\]

这个区间的 root image 可以远小于 L052 的扩大候选对。例如 `k=14` 时，`p=2,3` 的候选集合都包含 root 9，但

\[
R_2(W_2(14))=\{9,10\},
\qquad
R_2(W_3(14))=\{8\}.
\]

因此 candidate collision 在 exact-window 层已经是假的。

## 2. 三个不同的状态层

这里必须做一个语义区分。

定义**精确窗口 root image**

\[
\boxed{
G_p^{\rm win}(k)=\{R_2(q):q\in W_p(k)\}.
}
\]

真实 least-prime shell 更小。令

\[
Q_p^{\rm sh}(k)
=
\{n/p:\ k^2<n<(k+1)^2,\ \operatorname{spf}(n)=p\}.
\]

则

\[
Q_p^{\rm sh}(k)\subseteq W_p(k),
\]

因为一个真实 shell cofactor 不仅要满足区间条件，还必须满足 `p`-roughness / admissibility。定义真实 root image

\[
\boxed{
G_p^{\rm sh}(k)=\{R_2(q):q\in Q_p^{\rm sh}(k)\}.
}
\]

因此

\[
\boxed{
G_p^{\rm sh}(k)\subseteq G_p^{\rm win}(k).
}
\]

正确的层级是

\[
\text{candidate root superset}
\supseteq
\text{exact-window root image}
\supseteq
\text{realized shell root image}.
\]

一个精确区间并不自动等于真实可实现 shell。

## 3. L055 —— exact-window lower-band root images 从 k=9 起两两不交

状态：`PROVED`。

设 `k>=9`，并令 `p<r` 为不同 lower-band primes：

\[
p^2<2k,
\qquad
r^2<2k.
\]

则

\[
\boxed{
G_p^{\rm win}(k)\cap G_r^{\rm win}(k)=\varnothing.
}
\]

因为真实 shell images 是 exact-window images 的子集，立即得到

\[
\boxed{
G_p^{\rm sh}(k)\cap G_r^{\rm sh}(k)=\varnothing.
}
\]

所以从 `k>=9` 起，保留 root coordinate 已足以恢复 lower-band least-prime shell label。

## 4. exact-window collision 的必要条件

反设两个 exact-window images 存在共同 root `s`。则存在

\[
q_p\in W_p(k),
\qquad
q_r\in W_r(k)
\]

满足

\[
R_2(q_p)=R_2(q_r)=s.
\]

因为

\[
s^2\le q\le s^2+2s,
\]

区间端点给出

\[
\boxed{k^2<p\,s(s+2),}
\tag{A}
\]

\[
\boxed{rs^2\le k^2+2k,}
\tag{B}
\]

\[
\boxed{k^2<r(s+1)^2.}
\tag{C}
\]

由 (A)、(B) 得

\[
\boxed{(r-p)s^2<2ps+2k.}
\tag{D}
\]

这些条件针对的是更强的 exact-window collision 问题，因此在这里得到矛盾会自动排除真实 shell collision。

## 5. 所有 r>=5 都不可能

若 `r>=5`，prime spacing 给出

\[
r-p\ge2,
\qquad
p\le r-2.
\]

由 (C) 和

\[
4r\le(r+1)^2
\]

得到

\[
\boxed{2k<(r+1)(s+1).}
\tag{E}
\]

结合 (D)、(E)：

\[
\boxed{2s^2<(3r-3)s+r+1.}
\tag{F}
\]

对 `r>=11`，lower-band 条件与 (C) 推出

\[
r^3<4(s+1)^2.
\]

于是必须有

\[
2s\ge3r-1,
\]

这会使 (F) 左侧不小于右侧，矛盾。

对 `r=7`，(F) 给出 `s<=9`；再由 (A) 与 `p<=5` 得 `k<=22`，但 lower-band 要求 `k>=25`。

对 `r=5`，(F) 给出 `s<=6`；再由 (A) 与 `p<=3` 得 `k<=11`，但 lower-band 要求 `k>=13`。

所以

\[
\boxed{r\ge5\Longrightarrow\text{不存在 exact-window lower-band root collision}.}
\]

## 6. 最后只剩 (2,3)

对 `(p,r)=(2,3)`，(A)、(B) 变为

\[
\boxed{k^2<2s(s+2),}
\tag{I}
\]

\[
\boxed{3s^2\le k^2+2k.}
\tag{J}
\]

一个纯整数比较排除 `s>=8`。由 (I) 与 `98<100` 得

\[
7k<10(s+1),
\]

再与 (J) 合并得到

\[
47s^2<340s+240,
\]

此式从 `s=8` 起即失败，并且之后越来越失败。

因此 `s<=7`，再由 (I) 得 `k<=11`。在定理假设 `k>=9` 下，只剩 `k=9,10,11`；直接代入 (I)、(J) 即可逐一排除。因此 L055 得证。∎

## 7. 真实 shell 层的 sharpness

即使加上 `p`-rough 可实现性过滤，`k>=9` 仍是 sharp threshold。

在 `k=8`，取

\[
n_2=66=2\cdot33,
\qquad
n_3=75=3\cdot25.
\]

两者都位于平方盆地 `(64,81)`，而且

\[
\operatorname{spf}(66)=2,
\qquad
\operatorname{spf}(75)=3.
\]

但

\[
R_2(33)=R_2(25)=5.
\]

因此

\[
\boxed{5\in G_2^{\rm sh}(8)\cap G_3^{\rm sh}(8).}
\]

所以任何统一真实-shell 分离定理都不能从 9 以下开始。

## 8. exact-window collision 不一定可实现

中间层与最底层的区别在 `k=6` 已经出现。

精确窗口为

\[
W_2(6)=[19,24],
\qquad
W_3(6)=[13,16].
\]

所以两个 exact-window root images 都含 root 4。但 `p=3` 窗口中唯一产生 root 4 的 cofactor 是 `q=16`，对应

\[
3q=48,
\]

而 `48` 的最小素因子是 2。因此 root 4 **并未**被 `p=3` 真实 shell 实现。

所以 `k=6` 是 exact-window collision，却不是真实 shell collision。

这给出 L052 之后更细的一条 precision 纪律：

\[
\boxed{
\text{exact interval membership}
\neq
\text{admissible/realized state membership}.
}
\]

## 9. 有限回归 profile

可执行检查现在分别保存两个 collision profile。

`k<9` 时，exact-window images 的 collision 出现在

\[
k=5,6,8.
\]

加入 least-prime / `p`-rough realizability filter 后，有界 profile 变为

\[
k=5,8.
\]

这里它们只作为 regression evidence。补充 20 会进一步把全族分类升级成普通证明。

## 10. 与 L052 的关系

L052 仍然成立：它使用扩大后的两点 candidate set，在信息更少的情况下得到统一阈值 15。

L055 使用 exact quotient windows，证明更强的算术结论

\[
\text{exact-window separation from }k=9.
\]

真实 shell 是其子集，因此继承同一阈值，而 `k=8` 的真实 witness 又证明 sharpness。

层级现在应写成

\[
\boxed{
\text{candidate superset}
\to
\text{exact-window image}
\to
\text{realized-shell image}.
}
\]

每一步都加入了合法结构，也都可能删除假 collision。

## 11. A2 含义

P023-S8 在知道 admissibility 条件时，应当作用于**reachable/admissible shell state**。真实 shell images 两两不交，恰好就是删除 shell label 的 zero-repair criterion。

对 `k>=9`，root coordinate 足够恢复 lower-band shell identity。但它仍然不能恢复原始 cofactor 或 composite state，因为 root map 在单 shell 内仍是 many-to-one。

因此

\[
\boxed{
\text{shell identity retained}
\neq
\text{full state retained}.
}
\]

## 12. 可执行规范

- `src/enterprise_math/p017_actual_root_separation.py`
- `tests/test_p017_actual_root_separation.py`
- `experiments/p017_actual_root_separation_probe.py`

可执行层现在同时暴露 exact-window root images 与真实 least-prime-shell root images；固定 `k=6` 的语义反例、`k=8` 的真实 sharp witness，以及 `k>=9` 的大范围分离回归。

历史创新性继续标记为 `NOVELTY_UNVERIFIED`。项目真正新增的价值是 theorem-lifting 纪律，以及保留正确状态层后显现出的更强 P017 结构。
