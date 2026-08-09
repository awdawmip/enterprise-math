# Legendre 压力测试 — 补充 13

状态：`ACTIVE RESEARCH NOTE`  
范围：对镜像 incidence 一阶矩进行精确 CRT/Möbius 求值，并得到有限的素数存在充分证书  
依赖：P017 L042–L045  
纪律：**本文不证明 Legendre 猜想。** 容斥原理与中国剩余定理均为经典数学。这里的新作用只是把已经证明的镜像必要条件变成对单个根 `k` 可直接计算的精确有限证书。

## 1. 从必要条件变成可计算证书

令

\[
M=k(k+1),
\]

并令 \(A_k\) 为所有满足 \(a\le k\) 且 \(a\mid M\) 的素数的平方自由乘积。

L045 定义

\[
S_k=\{1\le r<k:\gcd(r,A_k)=1\}
\]

以及横向 incidence 总量

\[
J_k
=
\sum_{r\in S_k}
\left(
|\operatorname{Supp}_{\mathrm{tr}}(M-r)|
+
|\operatorname{Supp}_{\mathrm{tr}}(M+r)|
\right).
\]

若平方盆地中没有素数，L045 必然要求

\[
J_k\ge2|S_k|.
\]

因此严格相反的不等式

\[
J_k<2|S_k|
\]

已经足以证明该平方盆地中存在素数。

剩下的问题是：能否只用有限余数数据直接求出 \(J_k\) 与 \(|S_k|\)，而不去测试平方盆地内部状态的素性？答案是可以。

---

## 2. 余数类计数器

对整数 \(K\ge0\)、\(m\ge1\) 与规范正余数

\[
1\le\rho<m,
\]

定义

\[
\mathcal C(K;m,\rho)
=
\#\{1\le r\le K:r\equiv\rho\pmod m\}.
\]

显式地，

\[
\boxed{
\mathcal C(K;m,\rho)
=
\begin{cases}
0,&\rho>K,\\
1+\left\lfloor\dfrac{K-\rho}{m}\right\rfloor,&\rho\le K.
\end{cases}
}
\]

这只是算术级数计数。

---

## 3. L049 —— Surviving radii 与横向素数 incidence 的精确 CRT/Möbius 公式

状态：`PROVED / CLASSICAL INCLUSION-EXCLUSION SPECIALIZATION`。

令

\[
K=k-1.
\]

### 通过 anchor 筛选的半径

对平方自由 anchor product 使用 Möbius 容斥，得到

\[
\boxed{
|S_k|
=
\sum_{a\mid A_k}
\mu(a)
\left\lfloor\frac{K}{a}\right\rfloor.
}
\]

### 固定一个横向素数

固定横向素数

\[
p\le k,
\qquad p\nmid M.
\]

令 \(N_p(k)\) 为 L045 中的计数：通过 anchor 筛选、且 \(p\) 整除镜像对某一侧的半径数量。

对每个平方自由 \(a\mid A_k\)，需要计算同时满足

\[
a\mid r
\]

以及

\[
r\equiv M\pmod p
\]

或

\[
r\equiv-M\pmod p
\]

的半径。

由于 \(p\nmid A_k\)，有 \(\gcd(a,p)=1\)。记 \(a^{-1}\) 为模 \(p\) 的逆元，并定义

\[
 t^+_{a,p}
 =
(Ma^{-1})\bmod p,
\qquad
 t^-_{a,p}
 =
(-Ma^{-1})\bmod p.
\]

因为 \(p\nmid M\)，两者都属于 \(\{1,\ldots,p-1\}\)。对应模 \(ap\) 的唯一正 CRT 代表元为

\[
\rho^+_{a,p}=a t^+_{a,p},
\qquad
\rho^-_{a,p}=a t^-_{a,p}.
\]

因此

\[
\boxed{
N_p(k)
=
\sum_{a\mid A_k}
\mu(a)
\left[
\mathcal C(K;ap,\rho^+_{a,p})
+
\mathcal C(K;ap,\rho^-_{a,p})
\right].
}
\]

最后由 L045 得

\[
\boxed{
J_k
=
\sum_{\substack{p\le k\\p\nmid M}}N_p(k).
}
\]

### 证明

\(|S_k|\) 的公式来自普通恒等式

\[
\mathbf1_{\gcd(r,A_k)=1}
=
\sum_{a\mid\gcd(r,A_k)}\mu(a)
\]

对 \(1\le r\le K\) 求和。

对 \(N_p(k)\)，在附加两个镜像同余条件之一的同时应用同一恒等式。因为 \(a,p\) 互素，写 \(r=at\) 后，同余化为

\[
t\equiv\pm Ma^{-1}\pmod p,
\]

其模 \(ap\) 的唯一正代表元正是上式的 \(\rho^\pm_{a,p}\)。L043 保证对横向素数而言，正负两个通道不可能描述同一个半径，因此两个计数可以直接相加。∎

这个公式不需要分解平方盆地中的任何状态。

---

## 4. L050 —— 精确镜像 incidence 素数证书

状态：`PROVED`。

用 L049 计算 \(|S_k|\) 与所有 \(N_p(k)\)，并令

\[
J_k=\sum_{p\le k,\ p\nmid M}N_p(k).
\]

若

\[
\boxed{J_k<2|S_k|,}
\]

则必有

\[
\boxed{
\exists\text{ 素数 }q
\quad\text{满足}\quad
k^2<q<(k+1)^2.
}
\]

### 证明

若不存在这样的素数，则所有镜像状态都为合数，而两个未配对状态本身已知为合数。于是 L045 必须给出

\[
J_k\ge2|S_k|,
\]

与严格不等式矛盾。∎

因此 L050 是针对给定 \(k\) 的有限充分证书。它只使用：

- 不超过 \(k\) 的素数；
- 这些素数对显式 anchor \(k(k+1)\) 的整除关系；
- 模逆与 floor division。

它不需要对 \((k^2,(k+1)^2)\) 中任何整数做素性测试。

---

## 5. 边界：该证书是充分条件，不是必要条件

严格不等式并不与素数存在等价。

取

\[
k=31.
\]

精确公式给出

\[
|S_{31}|=15,
\qquad
J_{31}=30=2|S_{31}|.
\]

因此 L050 不触发。但

\[
967
\]

是素数，且满足

\[
31^2<967<32^2.
\]

所以绝不能把 L050 从充分证书悄悄升级成刻画定理。

---

## 6. 计算压力测试

状态：`COMPUTATIONAL`，不是定理。

参考实现会在有界范围内把 L049 的余数公式与直接镜像 support 计数进行交叉验证。

扫描

\[
3\le k\le1000
\]

时，L050 对其中 273 个 \(k\) 成功触发。也就是说，镜像 incidence 的一阶矩在一个显著的有限子集上确实具有证明能力，但无法认证该范围内的大多数根。

这给出正确的研究信号：

> L045 不是装饰性重写，但仅靠一阶 incidence 不足以形成一般证明。

下一步必须利用 L049 刻意遗忘的信息来进一步压缩容量，例如：同一侧的联合素数碰撞、exact-support 闭合、least-factor 深度，或不同半径之间的高阶约束。

---

## 7. 可执行验证

`src/enterprise_math/p017_mirror_certificate.py` 与 `tests/test_p017_mirror_certificate.py` 检查：

- \(|S_k|\) 的 Möbius 公式与直接 gcd 枚举一致；
- 每个 \(N_p(k)\) 公式与直接 surviving-radius 计数一致；
- 按素数求和的公式严格等于 L045 按状态计算的 \(J_k\)；
- 在有界范围内，每当 L050 触发，直接检查都确认平方盆地至少有一个素数；
- \(k=31\) 是证书不触发但素数仍存在的显式边界；
- `3<=k<=1000` 的触发数量确为 273。

有限计算只用于审计实现与覆盖率统计；公式与证书已由上文证明。
