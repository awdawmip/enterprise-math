# Legendre 压力测试 — 补充 10

状态：`ACTIVE RESEARCH NOTE`  
范围：在规范大模数命中定理之后，刻画通过 anchor 筛选的 support 闭合条件  
依赖：P017 L016 与 L039；编号位于规范 L040 之后  
纪律：**本文不证明 Legendre 猜想。** 本文只修正旧 WIP 中的 support 语义歧义，并保留尚未被 L039 吸收的部分。

## 1. L039 已经解决了什么

令

\[
I_k=\{n\in\mathbb N:k^2<n<(k+1)^2\},
\qquad M=k(k+1).
\]

L039 已经证明：任意模数 \(d\ge 2k\) 在 \(I_k\) 中至多命中一次，并给出精确的共同中心余数判据。因此，再单独保留一条“大 support incidence”定理只是在重命名 L039。

真正剩下的有用问题是：

> 当一个横向素数的平方自由乘积命中平方盆地后，这个命中什么时候**恰好**具有所提出的横向 support，而不是通过 cofactor 静默引入另一个小横向素数？

本补充回答这个问题，并补上旧 WIP 缺失的 anchor-survival 条件。

---

## 2. 设置

令 \(A_k\) 为所有满足 \(a\le k\) 且 \(a\mid M=k(k+1)\) 的素数之积。当素数 \(p\le k\) 满足

\[
p\nmid M
\]

时称其为**横向素数**。

令 \(P\) 为一个非空有限横向素数集合，并定义

\[
G_P=\prod_{p\in P}p.
\]

假设

\[
\boxed{G_P>2k.}
\]

若 L039 给出命中，则唯一写成

\[
\boxed{n=G_Ph.}
\]

由于 \(G_P>2k\) 且 \(n<(k+1)^2\)，L016 给出

\[
\boxed{h\le\left\lfloor\frac{k+1}{2}\right\rfloor\le k.}
\]

因此 \(h\) 的每个素因子本身都是不超过 \(k\) 的小素数。

称该命中为**通过 anchor 筛选**，若

\[
\boxed{\gcd(n,A_k)=1.}
\]

由于 \(P\) 中所有素数都横向，这等价于 cofactor \(h\) 不含 anchor 素因子。

---

## 3. L041 —— Anchor-surviving 的光滑闭合判据

状态：`PROVED`。

在上述设置下，假设唯一命中 \(n=G_Ph\) 通过 anchor 筛选，则

\[
\boxed{
\operatorname{Supp}_{\mathrm{tr}}(n)=P
\iff
\operatorname{PrimeSupp}(h)\subseteq P.
}
\]

也就是说：在通过 anchor 筛选的大 support 命中中，所提出的横向 support 恰好成立，当且仅当半尺度 cofactor 是 \(P\)-smooth。

### 证明

任取素数 \(q\mid h\)。由 \(q\le h\le k\) 知 \(q\) 是小素数。又因为命中通过 anchor 筛选，故 \(q\nmid A_k\)，因此 \(q\nmid M\)。于是 \(q\) 必为横向小素数。

若 \(n\) 的完整横向 support 恰为 \(P\)，则任何 \(q\mid h\) 都必须已经属于 \(P\)，所以

\[
\operatorname{PrimeSupp}(h)\subseteq P.
\]

反过来，若 \(h\) 的所有素因子都属于 \(P\)，则 cofactor 引入的所有素因子都已存在于 \(G_P\) 中；而 \(P\) 的每个成员本来就整除 \(G_P\)。因此完整横向 support 恰好是 \(P\)。∎

这里不限制 \(h\) 中素因子的重数；闭合是 support 条件，而不是 square-free 条件。

---

## 4. 正例

取

\[
k=16,
\qquad P=\{5,11\},
\qquad G_P=55>32.
\]

中心为 \(M=16\cdot17=272\)。L039 给出唯一命中

\[
n=275=55\cdot5.
\]

该命中通过 anchor 筛选，其 cofactor 为 \(h=5\)，显然是 \(P\)-smooth。因此

\[
\operatorname{Supp}_{\mathrm{tr}}(275)=\{5,11\}.
\]

---

## 5. 为什么 anchor survival 是必要条件

取

\[
k=10,
\qquad P=\{3,7\},
\qquad G_P=21>20.
\]

中心为 \(M=110\)，L039 给出唯一命中

\[
n=105=21\cdot5.
\]

这里 \(5\mid M\)，所以 5 是 anchor 素数，该命中**没有**通过 anchor 筛选。

然而

\[
\operatorname{Supp}_{\mathrm{tr}}(105)=\{3,7\}=P,
\]

而 \(h=5\) 并非 \(P\)-smooth。

因此不加限定的命题

\[
\operatorname{Supp}_{\mathrm{tr}}(n)=P
\iff
\operatorname{PrimeSupp}(h)\subseteq P
\]

是假的。L041 中 anchor-survival 条件是逻辑上必须的，不是表述偏好。

---

## 6. 与当前 P017 主线的关系

L041 不建立第二套大模数路线。它只细化规范 L039 命中 bit 触发之后的结构：

\[
\boxed{
\text{L039 唯一命中}
\longrightarrow
\text{半尺度 cofactor }h
\longrightarrow
\text{L041 support 闭合测试}.
}
\]

当后续论证按候选横向 support 对状态进行分组时，这一判据可以直接复用。特别是，一个 support product 虽然命中盆地，但 cofactor 若引入额外横向素数，它就不属于该 exact-support 类。

旧 WIP 中的四 support graph-tail 聚合本文不予升级：其历史实现依赖一个缺失模块，只有在重新独立构造并审计后才能进入规范主线。

---

## 7. 可执行验证

`src/enterprise_math/p017_support_closure.py` 与 `tests/test_p017_support_closure.py` 检查：

- 复用的共同中心命中与有界范围内直接枚举平方盆地一致；
- 所有 \(G_P>2k\) 的命中满足 L016 的半尺度 cofactor 上界；
- L041 在有界的 anchor-surviving 命中上成立；
- \((k,P)=(16,\{5,11\})\) 是正的 smooth-closure 例子；
- \((k,P)=(10,\{3,7\})\) 是去掉 anchor-survival 后的显式反例。

有限计算只用于审计实现；L041 的证明是上面的初等整数论证。
