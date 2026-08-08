# Legendre 压力测试 —— 补充 08

状态：`ACTIVE CONSOLIDATION NOTE`  
范围：把新的 cofactor-window recursion 与早期平方盆地 hit-count / carry 机器做精确同一化  
依赖：P017 L002–L003 与 L020–L036  
纪律：本补充不引入新的基础对象。目的恰恰是删掉重复路线，证明最近两种表示其实是完全相同的有限计数事件。

## 1. 为什么还需要一次合并

早期 P017 路线研究精确计数

\[
H_d(k)
=
\#\{n:k^2<n<(k+1)^2,\ d\mid n\}.
\]

新的 least-factor 路线则对素数 `p<=k` 研究精确 cofactor window

\[
W_p(k)=[A,B],
\]

使得

\[
L_p(k)=\{pq:q\in W_p(k),\ q\text{ 为 p-rough}\}.
\]

一开始它们像两种不同的证明语言：

- 原变量 `n` 上的 modular basin hit；
- 除掉 `p` 后变量 `q=n/p` 上的 rough cofactor window。

实际上它们不是两条路线。quotient window 正是把旧 hit-count 问题除去已知因子 `p` 后得到的像。

---

## 2. L037 —— Cofactor-window 端点就是直接 quotient 端点

状态：`PROVED`。

令 `p<=k` 为素数。L021 的中心化公式为

\[
A
=
k+1+r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor,
\qquad
r=k+1-p,
\]

以及

\[
B
=
k+1+r+\left\lfloor\frac{r^2-1}{p}\right\rfloor.
\]

它们可以精确化简成

\[
\boxed{
A=\left\lfloor\frac{k^2}{p}\right\rfloor+1
}
\]

以及

\[
\boxed{
B=\left\lfloor\frac{(k+1)^2-1}{p}\right\rfloor.
}
\]

### 下端点证明

因为

\[
r-1=k-p,
\]

有

\[
\left\lfloor\frac{(r-1)^2}{p}\right\rfloor
=
\left\lfloor\frac{k^2}{p}\right\rfloor-2k+p.
\]

同时

\[
k+1+r-1=2k+1-p.
\]

相加即得

\[
A=\left\lfloor\frac{k^2}{p}\right\rfloor+1.
\]

上端点对

\[
r^2-1=(k+1-p)^2-1
\]

做同样展开即可。

所以 `W_p(k)` 就是把开放平方盆地按已知因子 `p` 做整数商以后得到的直接 quotient interval。

---

## 3. L038 —— Raw cofactor-window 长度恰等于旧平方 hit count

状态：`PROVED`。

由 L037，

\[
|W_p(k)|
=B-A+1
\]

等于

\[
\left\lfloor\frac{(k+1)^2-1}{p}\right\rfloor
-
\left\lfloor\frac{k^2}{p}\right\rfloor.
\]

但这恰好就是两平方之间 `p` 的倍数个数定义。因此

\[
\boxed{|W_p(k)|=H_p(k).}
\]

所以新的 window-width identities 并不是竞争性不变量，而是同一个 `H_p(k)` 在除去已知最小因子后得到的精化视图。

特别地，L024 的 bulk-plus-boundary-carry 公式就是原 Euclidean basin descent / square-carry decomposition 的另一组坐标。

---

## 4. L039 —— 每个第二因子 child count 都等于 H_(p ell)(k)

状态：`PROVED`。

固定任意正整数 `ell`。cofactor window 中被 `ell` 整除的数目为

\[
M_\ell
=
\#\{q\in W_p(k):\ell\mid q\}.
\]

乘回已经抽出的因子 `p`，映射

\[
q\longmapsto n=pq
\]

把这些 cofactor 与平方盆地中被 `p ell` 整除的状态建立双射。

因此

\[
\boxed{
M_\ell=H_{p\ell}(k).
}
\]

这个恒等式对任意 `ell` 都精确成立，不需要 high-band 假设。

### 高带推论

若

\[
p^2\ge2k
\]

且 `ell>=p`，则

\[
p\ell\ge2k.
\]

开放平方盆地由恰好 `2k` 个连续整数构成，其跨度为 `2k-1`。因此模数至少为 `2k` 时至多命中一次。于是

\[
\boxed{
H_{p\ell}(k)=M_\ell\in\{0,1\}.
}
\]

所以 L034 的二值第二因子 branch，正是原始 P017 hit count 在大模数区域的专门化。

---

## 5. 同一个二值事件的公共中心形式

状态：`PROVED`。

令

\[
d\ge2k
\]

并写平方盆地中心

\[
M=k(k+1).
\]

每个盆地状态都可写成

\[
M+s,
\qquad
1-k\le s\le k.
\]

令

\[
a=M\bmod d,
\qquad
0\le a<d.
\]

由于盆地状态数少于 `d+1`，至多一个 offset 能解

\[
M+s\equiv0\pmod d.
\]

负代表 `s=-a` 位于盆地中当且仅当

\[
a<k.
\]

正代表 `s=d-a` 位于盆地中当且仅当

\[
a\ge d-k.
\]

所以

\[
\boxed{
H_d(k)
=
\mathbf 1[a<k]
+
\mathbf 1[a\ge d-k],
\qquad d\ge2k.
}
\]

在该范围两项不会同时为 `1`。

一旦命中，唯一状态显式为

\[
\boxed{
 n=
 \begin{cases}
 M-a,&a<k,\\
 M+(d-a),&a\ge d-k.
 \end{cases}
}
\]

取

\[
d=p\ell
\]

就精确恢复 L034 从 cofactor-window residue step 得到的候选状态。

因此三种描述完全相同：

\[
\boxed{
\text{cofactor residue hit}
=
\text{quotient-response carry bit}
=
\text{large-modulus square-basin hit }H_{p\ell}(k).
}
\]

---

## 6. 这次审计带来的直接结论

研究期间引入的几个对象现在可以合并掉。

### 不再作为独立 P017 路线维护

- raw cofactor-window branch bits；
- 旧 `H_d(k)` large-modulus hit indicators；
- 同一模数上的 quotient-response carry events。

它们只是同一有限事件的不同坐标表示。

### 当前证明步骤需要哪种表示就用哪种

- 全局盆地恒等式和 modular descent 用 `H_d(k)`；
- 正项 least-factor / Buchstab recursion 用 cofactor windows；
- transport/coherence 恒等式才使用 response/carry 语言。

这就是 P018 审计应该发挥的作用：新记号只有在改变可证明内容时才保留，而不是因为它能重新命名已有计数就独立生长。

## 7. 新的收窄目标

完成上述同一化后，高带 three-prime 问题只剩：

1. 选一个第二素数 `ell>=p`；
2. 检查单个旧 hit bit
   \[
   H_{p\ell}(k)\in\{0,1\};
   \]
3. 若为 `1`，把唯一命中状态除以 `p ell`；
4. 检查剩余 tail 是否为不小于 `ell` 的素数。

唯一仍可能具有项目专门价值的问题是：随 `ell` 变化的公共中心 residues

\[
k(k+1)\bmod(p\ell)
\]

是否存在足够强的相关性，从而超越一般 short-interval sieve 的上界。

若证明不了这样的相关性，这条路线就应停在这里。
