# Legendre 压力测试 — 补充 14

状态：`ACTIVE RESEARCH NOTE`  
范围：中心镜像 incidence 的精确公式，以及分解后的双松弛素数证书  
依赖：P017 L042–L045 与规范 L049  
纪律：**本文不证明 Legendre 猜想。** Möbius 容斥与中国剩余定理均为经典数学。项目特化在于：把它们与已经证明的中心镜像分离定理结合，得到有限障碍证书。

## 1. 镜像 support 计数

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

并记

\[
a_r=|P_-(r)|,
\qquad
b_r=|P_+(r)|.
\]

L043 已证明两侧 support 不交。若平方盆地无素数，L044 对每个 surviving radius 强制

\[
a_r\ge1,
\qquad
b_r\ge1.
\]

定义一阶矩与跨侧矩

\[
J_k=\sum_{r\in S_k}(a_r+b_r),
\qquad
E_k=\sum_{r\in S_k}a_rb_r.
\]

我们先只用小素数余数数据精确求出这两个量，再抽取“无素数假设”真正强制为非负的**原始松弛量**。

---

## 2. 余数类计数器

对 \(K\ge0\)、\(m\ge1\) 与 \(1\le\rho<m\)，定义

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

### 通过 anchor 筛选的半径

Möbius 容斥给出

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

固定横向素数 \(p\le k\)，即 \(p\nmid M\)。令 \(N_p(k)\) 统计通过 anchor 筛选、且 \(p\) 整除某一侧镜像状态的半径。

对每个平方自由 \(a\mid A_k\)，施加 \(a\mid r\) 以及

\[
r\equiv M\pmod p
\]

或

\[
r\equiv-M\pmod p.
\]

由于 \(\gcd(a,p)=1\)，定义

\[
 t^+_{a,p}=(Ma^{-1})\bmod p,
\qquad
 t^-_{a,p}=(-Ma^{-1})\bmod p.
\]

它们模 \(p\) 都非零。模 \(ap\) 的规范正代表元为

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

L043 保证对横向素数而言，正负两个通道不会描述同一半径。于是

\[
\boxed{
J_k
=
\sum_{\substack{p\le k\\p\nmid M}}N_p(k).
}
\]

### 证明

\(|S_k|\) 的公式就是对 \(1\le r\le K\) 求和的经典 Möbius 指示恒等式

\[
\mathbf 1_{\gcd(r,A_k)=1}
=
\sum_{a\mid\gcd(r,A_k)}\mu(a).
\]

对 \(N_p(k)\)，在同一指示式上附加一个镜像同余条件；写 \(r=at\) 即得到上面的代表元。最后对横向素数求和，就是 L045 的按素数重索引。∎

这个公式不需要分解平方盆地内的任何状态。

---

## 4. L051 —— 跨侧有序素数对的精确公式

状态：`PROVED / CLASSICAL CRT SPECIALIZATION`。

固定两个不同的横向素数 \(p,q\le k\)。令 \(N_{p\to q}(k)\) 统计满足

\[
p\mid M-r,
\qquad
q\mid M+r
\]

且通过 anchor 筛选的半径。

对每个平方自由 \(a\mid A_k\)，写 \(r=at\)，并令

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

对固定半径，可以选择的有序素数对 \((p,q)\) 满足

\[
p\in P_-(r),
\qquad
q\in P_+(r),
\]

其数量恰为 \(a_rb_r\)。因此双计数给出

\[
\boxed{
E_k
=
\sum_{\substack{p,q\le k\\p,q\nmid M\\p\ne q}}
N_{p\to q}(k).
}
\]

L043 正好排除了对角项 \(p=q\)。∎

---

## 5. L052 —— 两个原始无素数松弛量

状态：`PROVED`。

定义

\[
\boxed{U_k=J_k-2|S_k|}
\]

与

\[
\boxed{V_k=E_k-J_k+|S_k|.}
\]

若平方盆地无素数，则

\[
\boxed{U_k\ge0,
\qquad
V_k\ge0.}
\]

### 证明

在无素数假设下，L044 对每个 \(r\in S_k\) 给出 \(a_r,b_r\ge1\)。因此

\[
U_k
=
\sum_{r\in S_k}
\bigl[(a_r-1)+(b_r-1)\bigr]
\ge0.
\]

同时

\[
V_k
=
\sum_{r\in S_k}
(a_r-1)(b_r-1)
\ge0.
\]

二者都是显式非负整数之和。∎

这个分解比把 \(E_k\ge|S_k|\) 当作独立原始不等式更强、更干净，因为

\[
\boxed{
E_k-|S_k|=U_k+V_k.
}
\]

所以旧的跨侧乘积证书 \(E_k<|S_k|\) 一旦触发，必然已经有至少一个原始松弛量为负。

---

## 6. L053 —— 分解后的双松弛素数证书

状态：`PROVED`。

若

\[
\boxed{
U_k<0
\quad\text{或}\quad
V_k<0,
}
\]

则

\[
\boxed{
\exists q\text{ 为素数，满足 }k^2<q<(k+1)^2.
}
\]

### 证明

这就是 L052 的逆否命题。∎

直接写成精确矩：

\[
\boxed{
J_k<2|S_k|
\quad\text{或}\quad
E_k<J_k-|S_k|
\Longrightarrow
\exists q\text{ 为平方盆地中的素数。}
}
\]

两个通道真正相互独立。

### `U` 通道例子

取 \(k=37\)，

\[
|S_{37}|=17,
\qquad
J_{37}=33,
\qquad
E_{37}=18.
\]

因此

\[
U_{37}=-1<0,
\qquad
V_{37}=2\ge0.
\]

一阶通道完成认证。

### `V` 通道例子

取 \(k=46\)，

\[
|S_{46}|=22,
\qquad
J_{46}=47,
\qquad
E_{46}=18.
\]

因此

\[
U_{46}=3\ge0,
\qquad
V_{46}=18-47+22=-7<0.
\]

第二通道在第一通道失败时仍可认证素数。实际 \(2129\) 位于 \((46^2,47^2)\) 内。

---

## 7. L054 —— 边界及其与原始跨侧乘积证书的关系

状态：`PROVED`。

恒等式

\[
E_k-|S_k|=U_k+V_k
\]

说明：

1. \(E_k<|S_k|\) 虽然是充分条件，但不是原始条件；
2. 只要它触发，\(U_k<0\) 或 \(V_k<0\) 至少有一个已经触发；
3. 反过来不成立，因此分解后的证书严格更强。

对 \(k=31\)，

\[
|S_{31}|=15,
\qquad
J_{31}=30,
\qquad
E_{31}=15,
\]

所以

\[
U_{31}=V_{31}=0.
\]

证书不触发，但 \(967\) 是素数且位于 \((31^2,32^2)\) 内。因此 L053 仍只是充分证书，不是素数存在的刻画。

---

## 8. 计算压力测试

状态：`COMPUTATIONAL`，不是定理。

对

\[
3\le k\le1000
\]

参考实现得到：

- \(U_k<0\)：273 个根；
- \(V_k<0\)：594 个根；
- 二者同时为负：140 个根；
- 分解后的联合证书 \(U_k<0\) 或 \(V_k<0\)：**727 个根**；
- 较弱的旧条件 \(E_k<|S_k|\)：323 个根。

因此代数分解显著增强了旧的二阶联合证书。更重要的是，它指出了真正遗漏的结构：

- \(U_k\) 衡量每侧超过“至少一个横向资源”之后的总 excess support；
- \(V_k\) 衡量**同一个 surviving radius 两侧同时出现 excess** 的程度。

在该有界范围内仍有 271 个根无法认证。下一步应直接攻击这些同时满足两个非负松弛条件的残余根，而不是继续无目的添加 moment。

---

## 9. 与当前 P017 路线的关系

各跨状态层现在职责明确：

- L041：一次大 support 命中后的 exact-support 闭合；
- L042–L045：中心镜像分离与基础资源障碍；
- L046–L048：完整 side-sign pattern 的有界 CRT 容量；
- 规范 L049：通过真实 hit-state union 对高带资源做跨 shell 去重；
- L050–L051：一阶与跨侧 incidence 的精确可加公式；
- L052–L054：分解后的非负松弛量与更强有限素数证书。

下一步最有希望的对象已经不再是“另一个 moment”，而是：针对 L053 未认证的根，利用 exact-support 闭合、least-factor 深度或不同半径之间的相关性，对两个原始松弛量之一建立结构上界。

---

## 10. 可执行验证

`src/enterprise_math/p017_mirror_certificate.py`、`src/enterprise_math/p017_mirror_cross.py` 及其测试检查：

- L050 中 \(|S_k|\)、每个 \(N_p(k)\) 与 \(J_k\) 的公式与直接镜像 support 计数一致；
- L051 的有序素数对 CRT 公式与直接 surviving-radius 枚举一致；
- 有序素数对总和严格等于 \(E_k=\sum_r a_rb_r\)；
- \(U_k\)、\(V_k\) 与 \(E_k-|S_k|=U_k+V_k\) 的恒等式逐点成立；
- 在有界范围内，只要 L053 触发，直接检查都确认平方盆地中存在素数；
- \(k=31\)、37、46 固定上述边界；
- `3<=k<=1000` 的计数严格等于 273、594、140、727、323。

有限计算只用于审计实现与覆盖率统计；L050–L054 由精确容斥、CRT、双计数与上述整数因式分解证明。
