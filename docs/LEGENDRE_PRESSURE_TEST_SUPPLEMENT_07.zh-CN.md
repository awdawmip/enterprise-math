# Legendre 压力测试 —— 补充 07

状态：`ACTIVE RESEARCH NOTE`  
范围：高 least-factor 带中的二值第二因子 branch、素因子支撑分离与有限 prime-resource 上界  
依赖：P017 L020–L033  
纪律：本文不引入新的筛法形式。输入的递归属于成熟 least-prime-factor / Buchstab 机器；下面的结果来自把它与 P017 已证明的平方盆地窗口收缩结合。

## 1. 高带设置

固定平方盆地参数 `k` 与 least shell prime `p`，满足

\[
\boxed{p^2\ge2k.}
\]

令

\[
W_p(k)=[A,B]
\]

为 L021 的精确 cofactor window，并写

\[
N=B-A+1.
\]

L030 已给出

\[
\boxed{N\le p.}
\]

L032 已给出

\[
\boxed{\Omega(n)\le3}
\]

对每个 `n in L_p(k)` 成立。

因此每个 shell state 只能是

\[
pq
\]

其中 `q` 为素数，或者

\[
p\ell s
\]

其中

\[
p\le\ell\le s
\]

均为素数。

剩余问题是：这些 three-prime branches 是否还有更强的确定性结构？

---

## 2. L034 —— 每个第二因子 branch 都是一个精确 response bit

状态：`PROVED`。

固定素数

\[
\ell\ge p
\]

且

\[
\ell\le\sqrt B.
\]

`[A,B]` 中 `ell` 的倍数个数为

\[
M_\ell
=
\left\lfloor\frac B\ell\right\rfloor
-
\left\lfloor\frac{A-1}\ell\right\rfloor.
\]

由 L029，

\[
M_\ell
=
\left\lfloor\frac N\ell\right\rfloor
+
\kappa_\ell((A-1)\bmod\ell,\ N\bmod\ell).
\]

因为

\[
N\le p\le\ell,
\]

所以

\[
\boxed{M_\ell\in\{0,1\}.}
\]

定义 residue step

\[
\boxed{
d_\ell=(-A)\bmod\ell,
\qquad
0\le d_\ell<\ell.
}
\]

则

\[
\boxed{
M_\ell=1
\iff
d_\ell<N.
}
\]

### 证明

使 `A+d` 被 `ell` 整除的最小非负整数 `d` 恰为 `d_ell`。父区间由

\[
A,A+1,\ldots,A+N-1
\]

组成，所以区间内存在 `ell` 的倍数当且仅当 `d_ell<N`。由于区间长度不超过 `ell`，该倍数一旦存在就唯一。∎

当这个 bit 为 `1` 时，唯一 raw multiple 为

\[
\boxed{
q_\ell=A+d_\ell
=\ell\left\lceil\frac A\ell\right\rceil.
}
\]

令

\[
s_\ell=\frac{q_\ell}{\ell}
=\left\lceil\frac A\ell\right\rceil.
\]

由于 L032 已把 cofactor `q` 的素因子数压到至多两个，所以这个 branch 真正产生 three-prime shell state 当且仅当

\[
\boxed{
s_\ell\ge\ell
\quad\text{且}\quad
s_\ell\text{ 为素数}.}
\]

此时唯一状态为

\[
\boxed{
n_{p,\ell}=p\ell s_\ell.}
\]

因此在这个高带中，第二层 Buchstab recursion 已不再是另一个区间筛：对每个候选第二素数，只剩

\[
\boxed{
\text{一个 carry/residue bit}
+
\text{一次显式素性检验}.
}
\]

---

## 3. L035 —— 不同高带 cofactor survivors 两两互素

状态：`PROVED`。

设

\[
q_1,q_2\in W_p(k)
\]

为两个不同的 `p`-rough survivors。

则

\[
\boxed{\gcd(q_1,q_2)=1.}
\]

### 证明

假设某个素数 `ell` 同时整除二者。由于两者都是 `p`-rough，

\[
\ell\ge p.
\]

同时 `ell` 还整除非零差

\[
q_1-q_2.
\]

父窗口长度 `N<=p`，所以

\[
0<|q_1-q_2|\le N-1\le p-1<\ell,
\]

非零整数不可能既小于 `ell` 又是 `ell` 的倍数，矛盾。∎

因此对不同 shell states

\[
n_i=pq_i,
\]

有

\[
\boxed{\gcd(n_1,n_2)=p.}
\]

也就是说，同一高带 shell 内，不同状态唯一共享的 prime resource 就是最小因子 `p`；所有 cofactor prime supports 在不同 survivors 之间完全分离。

这比 L031 的 branchwise uniqueness 更强，因为它分离的是整个 survivor cofactor 的素因子支撑。

---

## 4. L036 —— 所有 three-prime branches 的有限 prime-resource 上界

状态：`PROVED`。

设一个高带 three-prime state 为

\[
n=p\ell s,
\qquad
p\le\ell\le s,
\]

三者均为素数。

令

\[
U=(k+1)^2-1
\]

并定义

\[
\boxed{
K_p=\left\lfloor\frac{U}{p^2}\right\rfloor.
}
\]

因为

\[
p\ell\ge p^2,
\]

所以

\[
s
\le
\frac{U}{p\ell}
\le
\frac{U}{p^2},
\]

从而

\[
\boxed{p\le\ell\le s\le K_p.}
\]

因此 three-prime state 中公共 `p` 以外的全部 prime factors 都落在有限资源区间

\[
[p,K_p].
\]

令

\[
R_p
=
\#\{\text{素数 }q:p\le q\le K_p\}
=
\pi(K_p)-\pi(p-1).
\]

再令 `T_p` 为 `L_p(k)` 中 three-prime states 的个数。

由 L035，不同 cofactor survivors 两两互素。因此两个不同 three-prime states 不会复用任何 cofactor prime resource。

若某个状态形如

\[
p\ell^2,
\]

它只消耗一个不同的 cofactor prime，而不是两个。但父窗口中至多出现一个这样的 square cofactor。

### 为什么 square cofactor 至多一个？

若

\[
a^2<b^2
\]

为两个不同平方数，且

\[
a,b\ge p,
\]

则

\[
b^2-a^2
=(b-a)(a+b)
\ge2p+1.
\]

但父 cofactor window 中任意两数之差至多为

\[
N-1\le p-1.
\]

矛盾。

因此，若用 `E_p` 表示是否存在 square branch，则

\[
E_p\in\{0,1\}.
\]

`T_p` 个 three-prime states 消耗的不同 cofactor prime resources 数量恰为

\[
2T_p-E_p.
\]

这些资源全部落在 `[p,K_p]`，故

\[
2T_p-E_p\le R_p.
\]

又因 `E_p<=1`，得到

\[
\boxed{
T_p
\le
\left\lfloor\frac{R_p+1}{2}\right\rfloor.
}
\]

这是高带收缩第一次给出的 shell-wide resource bound。

还可以与父窗口长度上界组合：

\[
\boxed{
T_p
\le
\min\left(
N,
\left\lfloor\frac{R_p+1}{2}\right\rfloor
\right).
}
\]

第一项来自父区间长度，第二项来自互不复用的 prime-resource 消耗。

---

## 5. 这解决了什么，又没有解决什么

当

\[
p^2\ge2k
\]

时，高 least-factor 带现在满足：

1. `N<=p`；
2. 每个第二素数 branch 是一个 binary quotient-response / residue hit；
3. 每个成功 branch 只有一个显式 candidate tail；
4. 不同 cofactor survivors 两两互素；
5. 不同 three-prime states 的 cofactor resources 完全分离；
6. 所有 three-prime resources 落在 `[p,K_p]`；
7. 总 three-prime 数受 L036 约束。

这是实质压缩，但它仍没有控制 shell 中 semiprime 部分的 prime cofactors。若想证明 Legendre，还需要同时约束：

- 这些短移动窗口中的 prime cofactors；
- 二值 three-prime branches。

所以下一步不应再发明新结构，而应检验：**所有第二素数 branch bits 共享同一组平方导出端点 `A,B`，这种共同端点是否制造了比普通短区间筛更强的相关性。**

## 6. 下一目标

在高带定义

\[
b_\ell(k,p)
=
\mathbf 1[d_\ell<N],
\qquad
 d_\ell=(-A)\bmod\ell.
\]

raw branch family 于是成为一个以 `ell>=p` 素数为索引的确定性二值向量。

下一问题是：

> 这些 `b_ell(k,p)` 是否因为共享平方导出的 `A,N` 而存在足够强的相关性，从而迫使成功 prime-tail branches 的数量低于一般短区间筛所允许的水平？

若答案是否定的，就记录并停止这条支线；若答案肯定，那么真正新的 P017 杠杆将是这种相关性，而不是 Buchstab recursion 本身。
