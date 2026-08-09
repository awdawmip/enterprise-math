# Legendre 压力测试 — 补充 17

状态：`ACTIVE RESEARCH NOTE`  
范围：平方盆地状态的完整重数 `k`-smooth core，以及唯一可能的大素数 tail  
依赖：P017 L001 root-factor horizon 与规范平方盆地  
纪律：smooth numbers、素因子分解与 valuation 都是成熟算术。项目专门内容，是平方盆地带来的精确结论：把 root cutoff 以下的**全部素数幂**剥离后，cutoff 以上至多只可能剩下一枚素因子。

## 1. 为什么 squarefree support 已经不够

现有 P017 mirror 路线经常只记录 small transverse primes 的 squarefree support。对于 Möbius 消去和 sign-pattern CRT，这是正确对象，但它会主动忘掉重数。

而在后续 bounded-capacity 论证中，重数可以真正改变 modulus。例如 `k=16` 的盆地中，

\[
279=3^2\cdot31.
\]

small squarefree support 只有 `{3}`，但完整 small-prime contribution 是 `3^2=9`。

更大的 modulus 可能直接减少 bounded CRT lifts，所以在进入 mirror capacity 前必须先抽出保留重数的对象。

---

## 2. 定义——full k-smooth core 与 large tail

令

\[
I_k=\{n\in\mathbb N:k^2<n<(k+1)^2\}.
\]

对 `n in I_k`，定义 **full `k`-smooth core**

\[
\boxed{
S_k(n)
=\prod_{p\le k}p^{v_p(n)}.
}
\]

这里完整保留所有重数。

再定义 residual tail

\[
\boxed{
Q_k(n)=\frac{n}{S_k(n)}.
}
\]

按构造，`Q_k(n)` 的每个素因子都严格大于 `k`。

---

## 3. L053 — 单一大 tail 分类

状态：`PROVED`。

对任意 `n in I_k`，

\[
\boxed{
Q_k(n)=1
\quad\text{或}\quad
Q_k(n)\text{ 是一枚 }>k\text{ 的素数}.
}
\]

不存在第三种情况。

### 证明

假设 `Q_k(n)>1`。

其所有素因子至少为 `k+1`。若 tail 为 composite，则按重数至少含两枚素因子，所以

\[
Q_k(n)\ge(k+1)^2.
\]

但

\[
Q_k(n)\le n<(k+1)^2,
\]

矛盾。

因此 `Q_k(n)` 必为素数；又因为不超过 `k` 的素因子已经全部进入 core，所以该素数严格大于 `k`。∎

这是 root cutoff 的精确有限后果，不是密度陈述。

---

## 4. smooth-core 坐标中的精确素性判据

状态：`PROVED`。

对任意 `n in I_k`，

\[
\boxed{
n\text{ 为素数}
\iff
S_k(n)=1.
}
\]

### 证明

若 `n` 为素数，则 `n>k^2>=k`，没有不超过 `k` 的素因子，所以 `S_k(n)=1`。

反之若 `S_k(n)=1`，则 `n` 没有不超过 `k` 的素因子。L001 / square-basin root-factor horizon 说明每个 basin composite 都必须有这种素因子，因此 `n` 必为素数。∎

所以 prime-count 问题也可以改写为：盆地中是否存在 smooth core 为 1 的状态。

---

## 5. 存在 large tail 时 core 有界

状态：`PROVED`。

若

\[
Q_k(n)>1,
\]

则

\[
\boxed{S_k(n)\le k.}
\]

因为 L053 给出 `Q_k(n)>=k+1`，而

\[
n<(k+1)^2.
\]

所以

\[
S_k(n)=\frac{n}{Q_k(n)}<k+1,
\]

且 `S_k(n)` 是整数。

对该分支中的 composite state，精确得到

\[
\boxed{
2\le S_k(n)\le k,
\qquad
n=S_k(n)Q_k(n),
\qquad
Q_k(n)>k\text{ 为素数}.
}
\]

这正是 parity-sensitive prime-tail branch 的精确形式。

---

## 6. 另一分支是 fully k-smooth

若

\[
Q_k(n)=1,
\]

则

\[
\boxed{n=S_k(n)}
\]

并且 `n` 的所有素因子都不超过 `k`。

所以每个 square-basin composite 精确落入两类之一：

### Fully smooth branch

\[
\boxed{n=S_k(n),\qquad Q_k(n)=1.}
\]

### Single-large-prime-tail branch

\[
\boxed{
2\le S_k(n)\le k,
\qquad
n=S_k(n)Q_k(n),
\qquad
Q_k(n)>k\text{ 为素数}.
}
\]

任何 composite state 都不可能再携带两枚 cutoff 以上的 residual prime factors。

---

## 7. 重数为什么会真正改变 mirror route

取 `k=16`、`r=7` 的 surviving mirror pair，中心

\[
M=16\cdot17=272.
\]

两侧为

\[
M-r=265=5\cdot53,
\]

\[
M+r=279=3^2\cdot31.
\]

squarefree small-support products 为

\[
D_-=5,
\qquad
D_+=3,
\qquad
D=15<k.
\]

而 full smooth cores 为

\[
S_-=5,
\qquad
S_+=9,
\qquad
S=S_-S_+=45\ge k.
\]

因此保留重数的 CRT modulus 可以严格大于旧 squarefree support modulus。

这本身还不是新的 bounded-lift theorem；它只是精确指出下一步必须保留的信息。

---

## 8. prime-tail mirror 分支的直接推论

设 `r` 为 anchor-surviving mirror radius，并且两侧 composite 都属于 single-large-prime-tail branch：

\[
M-r=S_-P_-,
\qquad
M+r=S_+P_+,
\]

其中

\[
2\le S_-,S_+\le k
\]

且 `P_-,P_+>k` 为素数。

规范 mirror theorem 已证明 surviving mirror pair 两侧互素，因此

\[
\boxed{\gcd(S_-,S_+)=1.}
\]

并且每一侧的完整分解已经被“一个有界 full smooth core + 一个大素数 tail”耗尽。

由此真正最难的子分支被显式隔离：

- 若 smooth core 含多个 small primes 或重复 prime power，则 full modulus 会大于 squarefree support product；
- 容量增益最小的情况，正是 core 只有一枚 small prime 且指数为 1。

这个 exponent-one singleton-core branch 就是本分类暴露出的真正 parity hard core。

---

## 9. 本定理没有解决什么

L053 **没有**证明 prime-tail branch 很少。

它没有约束 mirror CRT cell 中两条 affine large tails 同时为素数的频率。

它没有突破 sieve parity barrier。

它的职责是分类与信息保留：后续容量论证不能再先丢掉 prime-power multiplicity，再希望事后恢复。

---

## 10. 可执行核验

`src/enterprise_math/p017_smooth_core.py` 提供：

- `square_basin_smooth_core`；
- `square_basin_smooth_core_profile`。

`tests/test_p017_smooth_core.py` 检查：

- residual tail 总是 `1` 或一枚 `>k` 的素数；
- `n` 为素数当且仅当 `S_k(n)=1`；
- 非平凡 large tail 必留下 `S_k(n)<=k`；
- 完整保留 prime-power multiplicity，包括 `279=3^2*31`；
- 完整 basin profile 正确划分全部 `2k` 个 interior states。

有限计算用于审计实现；L053 的证明就是上面的初等平方盆地论证。

---

## 11. 下一目标

下一步合理的是 **full-core mirror CRT upgrade**。

对 prime-tail mirror pair，使用

\[
S=S_-S_+
\]

而不是仅使用 distinct small primes 的 squarefree product。由于 `S_-` 与 `S_+` 互素，同一 sign/idempotent encoding 应能恢复完整 prime-power cores。

真正的容量问题是：更大的 full-core modulus 是否能在不改变 CRT 经典数学地位的情况下，严格收紧 bounded-radius capacity。
