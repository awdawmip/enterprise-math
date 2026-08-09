# Legendre 压力测试 — 补充 11

状态：`ACTIVE RESEARCH NOTE`  
范围：围绕平方盆地共同中心的镜像对分离，以及跨不同盆地状态的横向素数资源计数  
依赖：P017 L001、anchor 消去与规范横向 support 语言  
纪律：**本文不证明 Legendre 猜想。** 下述结果是精确的跨状态约束；最后的 incidence 不等式仅是假想反例必须满足的必要条件。

## 1. 中心镜像分解

令

\[
M=k(k+1),
\qquad
I_k=\{n\in\mathbb N:k^2<n<(k+1)^2\}.
\]

则

\[
I_k=M+\{1-k,\ldots,k\}.
\]

对每个

\[
1\le r\le k-1,
\]

定义镜像对

\[
M-r,\qquad M+r.
\]

它们恰好给出 \(k-1\) 对。剩余两个未配对状态为

\[
M=k(k+1)
\]

与

\[
M+k=k(k+2),
\]

当 \(k\ge2\) 时二者均为合数。

因此平方盆地中的任何素数见证都必然位于某个镜像对中。

令 \(A_k\) 为所有满足 \(p\le k\) 且 \(p\mid M\) 的素数之积。若素数 \(p\le k\) 满足 \(p\nmid M\)，称其为**横向素数**。

---

## 2. L042 —— Anchor survival 在镜像对上全进或全出

状态：`PROVED`。

因为 \(A_k\mid M\)，对每个半径 \(1\le r<k\)，

\[
\boxed{
\gcd(M-r,A_k)
=
\gcd(r,A_k)
=
\gcd(M+r,A_k).
}
\]

因此

\[
\boxed{
\gcd(r,A_k)=1
\iff
\gcd(M-r,A_k)=\gcd(M+r,A_k)=1.
}
\]

所以 anchor 筛不会只删除镜像对的一侧：两侧要么同时通过，要么同时失败。

### 证明

由于 \(A_k\mid M\)，任意整数 \(x\) 都满足 \(\gcd(M\pm x,A_k)=\gcd(x,A_k)\)。取 \(x=r\) 即得。∎

---

## 3. L043 —— 镜像两侧横向 support 严格不交

状态：`PROVED`。

对每个半径 \(1\le r<k\)，

\[
\boxed{
\operatorname{Supp}_{\mathrm{tr}}(M-r)
\cap
\operatorname{Supp}_{\mathrm{tr}}(M+r)
=arnothing.
}
\]

这个结论甚至不需要 anchor survival。

### 证明

反设某个横向素数 \(p\le k\) 同时整除两个镜像状态，则

\[
p\mid(M+r)-(M-r)=2r.
\]

因为 \(M=k(k+1)\) 恒为偶数，素数 2 整除 \(M\)，故 2 不可能是横向素数。因此 \(p\) 为奇素数，于是 \(p\mid r\)。再结合 \(p\mid M-r\) 得 \(p\mid M\)，与横向性矛盾。∎

因此，同一个横向小素数资源不可能同时覆盖同一镜像对的两侧。

### 更强推论：通过 anchor 筛选的镜像三元组两两互素

若 \(\gcd(r,A_k)=1\)，则

\[
\boxed{
\gcd(M-r,M)=
\gcd(M,M+r)=
\gcd(M-r,M+r)=1.
}
\]

理由是：若某素数同时整除 \(M\) 与 \(r\)，由于 \(r<k\)，该素数不超过 \(k\)，于是属于 \(A_k\)，与 anchor survival 矛盾，所以 \(\gcd(M,r)=1\)。另外 \(2\mid A_k\)，故通过筛选的 \(r\) 为奇数，而 \(M\) 为偶数，因此两个镜像状态均为奇数。若某公因子同时整除 \(M-r\) 与 \(M+r\)，它是奇数并整除 \(2M\) 与 \(2r\)，故同时整除 \(M\) 与 \(r\)，只能为 1。

这个更强推论将作为后续 CRT/idempotent 层的干净输入。

---

## 4. L044 —— 通过 anchor 筛选的双合数镜像对至少消耗两个不同横向资源

状态：`PROVED CONDITIONAL CONSEQUENCE`。

假设

\[
\gcd(r,A_k)=1
\]

且两个镜像状态

\[
M-r,\qquad M+r
\]

均为合数。

二者都位于开放平方盆地中，因此 root-factor horizon 保证每一侧至少存在一个不超过 \(k\) 的素因子。由 L042，两侧均通过 anchor 筛，所以这些小素因子不可能是 anchor 素数，只能是横向素数。再由 L043，两侧横向 support 不交。

因此两侧 support 都非空且互不相交，特别地

\[
\boxed{
|\operatorname{Supp}_{\mathrm{tr}}(M-r)|
+
|\operatorname{Supp}_{\mathrm{tr}}(M+r)|
\ge2.
}
\]

例如 \(k=20\)、\(M=420\)、\(r=17\) 时，

\[
403=13\cdot31,
\qquad
437=19\cdot23.
\]

不超过 \(k\) 的横向素因子分别是 13 和 19，位于相反两侧。

---

## 5. L045 —— 盆地级横向 incidence 必要条件

状态：`PROVED AS A NECESSARY CONDITION; NOT A CONTRADICTION`。

定义通过 anchor 筛选的半径集合

\[
S_k
=
\{r:1\le r<k,\ \gcd(r,A_k)=1\}.
\]

定义所有通过筛选的镜像状态上的横向小素数总 incidence：

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

若开放平方盆地内不存在素数，则所有镜像状态都是合数；两个未配对状态本来也已知是合数。对每个通过筛选的半径应用 L044，得到

\[
\boxed{J_k\ge2|S_k|.}
\]

这只是某个假想 Legendre 反例必须满足的必要条件；本文没有给出与之矛盾的上界。

### 按素数重新索引

对横向素数 \(p\le k\)，定义

\[
N_p(k)
=
\#\{r\in S_k:p\mid M-r\ \text{或}\ p\mid M+r\}.
\]

L043 保证对固定的 \((p,r)\)，两个条件不可能同时成立。因此普通双计数给出

\[
\boxed{
J_k
=
\sum_{\substack{p\le k\\p\nmid M}}N_p(k).
}
\]

左边按状态索引，右边按素数索引；这是一个精确的跨状态资源恒等式。

---

## 6. 相比当前 least-factor window 路线新增了什么

当前 P017 高带结果主要分离**同一个 least-factor shell 内部**不同 cofactor 的素数 support。L042–L045 则利用几何上互为中心镜像的两个不同盆地状态，给出跨状态关系。

新增的核心不是另一套筛计数，而是

\[
\boxed{
\text{一个通过筛选的半径}
\longrightarrow
\text{两个状态}
\longrightarrow
\text{横向 support 严格不交}.
}
\]

后续可以把它与 L041 的 exact-support 闭合以及 bounded CRT sign-pattern capacity 结合，但 L042–L045 本身不依赖这些后续工具。

L045 的一阶 incidence 很可能不足以单独证明 Legendre。真正值得继续的问题是：二阶重叠/容量约束能否阻止足够多的镜像对同时成为双合数。

---

## 7. 可执行验证

`src/enterprise_math/p017_mirror.py`、`src/enterprise_math/p017_mirror_incidence.py` 及其测试检查：

- 平方盆地恰好分成 \(k-1\) 个镜像对和两个已知合数状态；
- anchor survival 在镜像两侧全进或全出；
- 有界范围内镜像两侧的横向 support 始终不交；
- 所有测试到的通过筛选双合数镜像对都具有两个非空且不交的横向 support；
- 按状态与按素数计算的 incidence 总量严格一致；
- 通过 anchor 筛选的镜像三元组两两互素。

有限计算只用于审计实现；L042–L045 来自上面的初等整数论证。
