# Legendre 压力测试 — 补充 14

状态：`ACTIVE RESEARCH NOTE`  
范围：中心镜像 incidence 的精确一阶与二阶证书  
依赖：P017 L042–L045 与规范 L049  
纪律：**本文不证明 Legendre 猜想。** Möbius 容斥与中国剩余定理均为经典数学。项目特化在于：把它们与已经证明的中心镜像障碍结合，形成可直接计算的有限证书。

## 1. 从镜像分离到证书

令

\[
M=k(k+1),
\]

并令 \(A_k\) 为所有满足 \(a\le k\) 且 \(a\mid M\) 的素数的平方自由乘积。回顾

\[
S_k=\{1\le r<k:\gcd(r,A_k)=1\}.
\]

对 \(r\in S_k\)，定义

\[
P_-(r)=\operatorname{Supp}_{\mathrm{tr}}(M-r),
\qquad
P_+(r)=\operatorname{Supp}_{\mathrm{tr}}(M+r),
\]

并令

\[
a_r=|P_-(r)|,
\qquad
b_r=|P_+(r)|.
\]

L043 已证明 \(P_-(r)\cap P_+(r)=\varnothing\)。若平方盆地无素数，L044 对每个 surviving radius 强制

\[
a_r\ge1,
\qquad
b_r\ge1.
\]

因此得到两个有限障碍矩：

\[
J_k=\sum_{r\in S_k}(a_r+b_r),
\qquad
E_k=\sum_{r\in S_k}a_rb_r.
\]

在假想的无素数情形下，它们必须满足

\[
J_k\ge2|S_k|,
\qquad
E_k\ge|S_k|.
\]

本补充的目标，是只用小素数与余数数据精确求出这两个量，而不分解或测试平方盆地内部状态的素性。

---

## 2. 余数类计数器

对 \(K\ge0\)、\(m\ge1\) 与规范正余数 \(1\le\rho<m\)，定义

\[
\mathcal C(K;m,\rho)
=
\#\{1\le r\le K:r\equiv\rho\pmod m\}.
\]

则

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

---

## 3. L050 —— 一阶矩的精确 CRT/Möbius 公式

状态：`PROVED / CLASSICAL INCLUSION-EXCLUSION SPECIALIZATION`。

令 \(K=k-1\)。

### 通过 anchor 筛选的半径数量

对平方自由 anchor product 做 Möbius 容斥：

\[
\boxed{
|S_k|
=
\sum_{a\mid A_k}
\mu(a)
\left\lfloor\frac{K}{a}\right\rfloor.
}
\]

### 固定一个横向素数的 incidence

固定横向素数

\[
p\le k,
\qquad p\nmid M.
\]

令 \(N_p(k)\) 统计通过 anchor 筛选、且 \(p\) 整除某一侧镜像状态的半径。对每个平方自由 \(a\mid A_k\)，加入 \(a\mid r\) 以及

\[
r\equiv M\pmod p
\quad\text{或}\quad
r\equiv-M\pmod p.
\]

因为 \(\gcd(a,p)=1\)，定义

\[
 t^+_{a,p}=(Ma^{-1})\bmod p,
\qquad
 t^-_{a,p}=(-Ma^{-1})\bmod p.
\]

两者都位于 \(\{1,\ldots,p-1\}\)。模 \(ap\) 的规范正代表元为

\[
\rho^+_{a,p}=a t^+_{a,p},
\qquad
\rho^-_{a,p}=a t^-_{a,p}.
\]

于是

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

L043 保证对横向素数而言，正负两个通道不会描述同一个半径。因此

\[
\boxed{
J_k
=
\sum_{\substack{p\le k\\p\nmid M}}N_p(k).
}
\]

### 证明

\(|S_k|\) 的公式来自经典恒等式

\[
\mathbf 1_{\gcd(r,A_k)=1}
=
\sum_{a\mid\gcd(r,A_k)}\mu(a)
\]

对 \(1\le r\le K\) 求和。\(N_p(k)\) 的公式是在同一恒等式上同时施加两个镜像同余中的一个；写 \(r=at\) 即得到上面的代表元。最后对全部横向素数求和，正是 L045 的按素数重索引。∎

这些公式不需要分解 \((k^2,(k+1)^2)\) 中任何状态。

---

## 4. L051 —— 一阶矩素数证书

状态：`PROVED`。

若

\[
\boxed{J_k<2|S_k|,}
\]

则

\[
\boxed{
\exists q\text{ 为素数，满足 }k^2<q<(k+1)^2.
}
\]

### 证明

若盆地无素数，则每个 surviving mirror pair 都是双合数。L044 对每个 \(r\in S_k\) 给出 \(a_r+b_r\ge2\)，所以 L045 必须满足 \(J_k\ge2|S_k|\)，矛盾。∎

该证书是充分条件，不是必要条件。对 \(k=31\)，

\[
|S_{31}|=15,
\qquad
J_{31}=30,
\]

所以证书不触发；但 \(967\) 是素数，且 \(31^2<967<32^2\)。

---

## 5. L052 —— 跨侧有序素数对的精确公式

状态：`PROVED / CLASSICAL CRT SPECIALIZATION`。

一阶矩遗忘了小素数资源必须出现在**同一半径的相反两侧**这一事实。第一个真正跨侧的矩为

\[
E_k=\sum_{r\in S_k}a_rb_r.
\]

固定不同的横向素数 \(p,q\le k\)。令 \(N_{p\to q}(k)\) 统计满足

\[
p\mid M-r,
\qquad
q\mid M+r
\]

且通过 anchor 筛选的半径。

对每个平方自由 \(a\mid A_k\)，写 \(r=at\)，并定义

\[
c_p=(Ma^{-1})\bmod p,
\qquad
c_q=(-Ma^{-1})\bmod q.
\]

模 \(pq\) 的唯一规范解为

\[
\boxed{
 t_{a;p,q}
=
c_p
+p\left((c_q-c_p)p^{-1}\bmod q\right),
}
\]

且 \(1\le t_{a;p,q}<pq\)。令

\[
\rho_{a;p,q}=a t_{a;p,q}.
\]

则

\[
\boxed{
N_{p\to q}(k)
=
\sum_{a\mid A_k}
\mu(a)
\mathcal C(K;apq,\rho_{a;p,q}).
}
\]

对“左 support 选一个素数、右 support 选一个素数”的有序选择进行双计数，得到

\[
\boxed{
E_k
=
\sum_{\substack{p,q\le k\\p,q\nmid M\\p\ne q}}
N_{p\to q}(k).
}
\]

### 证明

CRT 公式只是 L050 的双同余版本。由于 \(a,p,q\) 两两互素，模 \(apq\) 恰有一个余数类。L043 排除 \(p=q\)。对固定半径，可选择的有序素数对数量恰为 \(a_rb_r\)；先按半径求和或先按有序素数对求和得到同一整数。∎

---

## 6. L053 —— 跨侧乘积证书

状态：`PROVED`。

若

\[
\boxed{E_k<|S_k|,}
\]

则开放平方盆地中必有素数。

### 证明

若盆地无素数，则每个 surviving mirror pair 都是双合数，由 L044 得 \(a_r,b_r\ge1\)。所以对每个 \(r\in S_k\) 有 \(a_rb_r\ge1\)，求和得到 \(E_k\ge|S_k|\)，矛盾。∎

这个证书独立于 L051。对 \(k=46\)，

\[
|S_{46}|=22,
\qquad
J_{46}=47\ge44,
\]

L051 失败；但

\[
E_{46}=18<22,
\]

所以 L053 证明素数存在。实际 \(2129\) 位于 \((46^2,47^2)\) 内。

反过来，对 \(k=37\)，

\[
|S_{37}|=17,
\qquad
J_{37}=33<34,
\qquad
E_{37}=18\ge17.
\]

此时 L051 触发，而 L053 不触发。

---

## 7. L054 —— 两矩联合证书

状态：`PROVED`。

合并两个相互独立的充分条件：

\[
\boxed{
J_k<2|S_k|
\quad\text{或}\quad
E_k<|S_k|
\Longrightarrow
\exists q\text{ 为素数，满足 }k^2<q<(k+1)^2.
}
\]

两个分支互不支配。

---

## 8. 计算压力测试

状态：`COMPUTATIONAL`，不是定理。

在有界范围

\[
3\le k\le1000
\]

内，参考实现得到：

- L051 一阶证书：273 个根；
- L053 跨侧证书：323 个根；
- 两者同时触发：269 个根；
- 仅 L053：54 个根；
- 仅 L051：4 个根；
- L054 联合覆盖：327 个根。

因此跨侧乘积矩严格增加了证明力，但前两个矩合并后，在该有界范围内仍然只能认证少数根。

这是一个有价值的负边界：下一步不应无结构地堆叠 moment，而应利用这两个矩刻意遗忘的信息，例如同侧联合碰撞、exact-support 闭合、least-factor 深度，或不同半径之间的相关性。

---

## 9. 与其他 P017 跨状态工具的关系

当前各层职责明确：

- L041：一次大 support 命中后的 exact-support 闭合；
- L042–L045：中心镜像分离与基础资源障碍；
- L046–L048：完整 side-sign pattern 的有界 CRT 容量；
- 规范 L049：通过真实 hit-state union 对高带资源做跨 shell 去重；
- L050–L054：可加的一阶与二阶镜像证书。

L052 刻意位于粗糙的一阶矩与完整 CRT support cell 之间：它只固定一对位于相反两侧的有序素数资源，因此既保留真实跨状态结构，又仍然可以对全盆地求和。

---

## 10. 可执行验证

`src/enterprise_math/p017_mirror_certificate.py`、`src/enterprise_math/p017_mirror_cross.py` 及其测试检查：

- L050 中 \(|S_k|\)、每个 \(N_p(k)\) 和 \(J_k\) 的公式与有界范围内直接镜像 support 计数一致；
- L052 的有序素数对 CRT 公式与直接 surviving-radius 枚举一致；
- 所有有序素数对求和严格等于 \(\sum_r a_rb_r\)；
- 在有界范围内，只要任一证书触发，直接检查都确认平方盆地至少有一个素数；
- \(k=31\)、\(k=37\)、\(k=46\) 固定上述边界；
- `3<=k<=1000` 的覆盖计数严格等于 273、323、269、54、4、327。

有限计算只用于审计实现与覆盖率统计；L050–L054 由精确容斥、CRT 与双计数证明。
