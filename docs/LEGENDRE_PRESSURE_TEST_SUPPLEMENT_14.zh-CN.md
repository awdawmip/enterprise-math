# Legendre 压力测试 — 补充 14

状态：`ACTIVE RESEARCH NOTE`  
范围：中心镜像 incidence 的精确公式，以及分解后的聚合素数证书  
依赖：P017 L042–L045 与规范 L049  
纪律：**本文不证明 Legendre 猜想。** Möbius 容斥与中国剩余定理均为经典数学。项目特化结果来自它们与中心镜像分离定理的组合。

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

以及

\[
a_r=|P_-(r)|,
\qquad
b_r=|P_+(r)|.
\]

L043 已证明两侧 support 严格不交。若平方盆地无素数，L044 对每个 surviving radius 强制

\[
a_r\ge1,
\qquad
b_r\ge1.
\]

定义

\[
J_k=\sum_{r\in S_k}(a_r+b_r),
\qquad
E_k=\sum_{r\in S_k}a_rb_r.
\]

我们先只用小素数余数数据精确求出两个矩，再提取无素数假设真正强制为非负的原始松弛量及其紧聚合二次上界。

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

令 \(K=k-1\)。Möbius 容斥给出

\[
\boxed{
|S_k|
=
\sum_{a\mid A_k}
\mu(a)
\left\lfloor\frac{K}{a}\right\rfloor.
}
\]

固定横向素数 \(p\le k\)。令 \(N_p(k)\) 统计通过 anchor 筛选、且 \(p\) 整除某一侧镜像状态的半径。对每个平方自由 \(a\mid A_k\)，定义

\[
 t^+_{a,p}=(Ma^{-1})\bmod p,
\qquad
 t^-_{a,p}=(-Ma^{-1})\bmod p,
\]

以及

\[
\rho^+_{a,p}=a t^+_{a,p},
\qquad
\rho^-_{a,p}=a t^-_{a,p}.
\]

由于 \(p\nmid M\)，两者模 \(p\) 都非零。于是

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

L043 保证两个镜像通道不重叠，因此

\[
\boxed{
J_k
=
\sum_{\substack{p\le k\\p\nmid M}}N_p(k).
}
\]

### 证明

对 \(1\le r\le K\) 使用经典 Möbius 指示恒等式

\[
\mathbf1_{\gcd(r,A_k)=1}
=
\sum_{a\mid\gcd(r,A_k)}\mu(a),
\]

并附加一个镜像同余条件。写 \(r=at\) 后即得到上面的余数类。最后对横向素数求和，就是 L045 的按素数重索引。∎

这些公式不需要分解平方盆地内的任何状态。

---

## 4. L051 —— 跨侧有序素数对的精确公式

状态：`PROVED / CLASSICAL CRT SPECIALIZATION`。

固定不同的横向素数 \(p,q\le k\)。令 \(N_{p\to q}(k)\) 统计满足

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

且 \(1\le t_{a;p,q}<pq\)。令 \(\rho_{a;p,q}=a t_{a;p,q}\)，则

\[
\boxed{
N_{p\to q}(k)
=
\sum_{a\mid A_k}
\mu(a)
\mathcal C(K;apq,\rho_{a;p,q}).
}
\]

对固定半径，可选择的有序素数对 \(p\in P_-(r),q\in P_+(r)\) 的数量恰为 \(a_rb_r\)。因此双计数给出

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

在无素数假设下，L044 给出 \(a_r,b_r\ge1\)。令

\[
x_r=a_r-1,
\qquad
y_r=b_r-1.
\]

则 \(x_r,y_r\ge0\)，并且

\[
U_k
=
\sum_{r\in S_k}(x_r+y_r)
\ge0,
\]

同时

\[
V_k
=
\sum_{r\in S_k}x_ry_r
\ge0.
\]

二者都是显式非负整数之和。∎

另外

\[
\boxed{E_k-|S_k|=U_k+V_k.}
\]

因此旧的 \(E_k<|S_k|\) 条件只是原始松弛结构的较弱推论。

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

则存在素数 \(q\) 满足

\[
k^2<q<(k+1)^2.
\]

这是 L052 的逆否命题。等价地，

\[
\boxed{
J_k<2|S_k|
\quad\text{或}\quad
E_k<J_k-|S_k|
\Longrightarrow
\text{存在平方盆地素数。}
}
\]

两个通道相互独立：

- \(k=37\)：\(|S|=17,J=33,E=18\)，因此 \(U=-1<0\)、\(V=2\ge0\)；
- \(k=46\)：\(|S|=22,J=47,E=18\)，因此 \(U=3\ge0\)、\(V=-7<0\)。实际 \(2129\) 是该平方盆地中的素数。

---

## 7. L054 —— 聚合判别式上界

状态：`PROVED`。

若平方盆地无素数，则

\[
\boxed{4V_k\le U_k^2.}
\]

### 证明

使用 L052 中的非负整数 \(x_r,y_r\)，对每个半径有

\[
4x_ry_r\le(x_r+y_r)^2.
\]

因此

\[
4V_k
\le
\sum_{r\in S_k}(x_r+y_r)^2.
\]

又因为所有 \(x_r+y_r\ge0\)，

\[
\sum_{r\in S_k}(x_r+y_r)^2
\le
\left(\sum_{r\in S_k}(x_r+y_r)\right)^2
=U_k^2.
\]

故得结论。∎

所以即使 \(U_k,V_k\ge0\)，只要

\[
\boxed{4V_k>U_k^2}
\]

仍可直接推出平方盆地中存在素数。

这个上界是只保留聚合量 \((U_k,V_k)\) 时的紧二次包络：固定总 \(U\) 后，要最大化乘积贡献，只需把 excess 集中到一个半径，并尽量平衡其左右两侧。

---

## 8. L055 —— 最终三通道证书与边界

状态：`PROVED`。

综合 L052–L054：

\[
\boxed{
U_k<0
\quad\text{或}\quad
V_k<0
\quad\text{或}\quad
4V_k>U_k^2
\Longrightarrow
\exists q\text{ 为素数，满足 }k^2<q<(k+1)^2.
}
\]

旧的 \(E_k<|S_k|\) 条件是冗余的，因为

\[
E_k-|S_k|=U_k+V_k.
\]

对 \(k=31\)，

\[
|S_{31}|=15,
\qquad
J_{31}=30,
\qquad
E_{31}=15,
\]

于是 \(U_{31}=V_{31}=0\)，三个通道都不触发；但 \(967\) 是 \((31^2,32^2)\) 中的素数。因此 L055 仍只是充分证书，不是素数存在的刻画。

---

## 9. 计算压力测试

状态：`COMPUTATIONAL`，不是定理。

对

\[
3\le k\le1000
\]

参考实现得到：

- \(U_k<0\)：273 个根；
- \(V_k<0\)：594 个根；
- 二者同时为负：140 个根；
- 两个负松弛通道的并集：727 个根；
- 仅由 \(4V_k>U_k^2\) 新增认证：6 个根；
- L055 三通道联合覆盖：**733 个根**；
- 较弱的旧条件 \(E_k<|S_k|\)：323 个根。

该范围内新增的 6 个二次包络例子从 \(k=128\) 开始。这些有限统计只用于诊断。

这一步基本封闭了只依赖聚合对 \((U_k,V_k)\) 的简单信息。继续推进时应使用这些聚合量已经丢失的结构，而不是再机械添加一个 moment。在 \(k\le1000\) 中尚有 265 个根未被认证，它们构成下一轮压力测试总体。

---

## 10. 与当前 P017 路线的关系

各跨状态层职责清楚：

- L041：一次大 support 命中后的 exact-support 闭合；
- L042–L045：中心镜像分离与基础资源障碍；
- L046–L048：完整 side-sign pattern 的有界 CRT 容量；
- 规范 L049：通过真实 hit-state union 对高带资源做跨 shell 去重；
- L050–L051：一阶与跨侧 incidence 的精确可加公式；
- L052–L055：原始非负松弛量、紧聚合二次包络与有限素数证书。

下一步必须解释同时满足

\[
U_k\ge0,
\qquad
V_k\ge0,
\qquad
4V_k\le U_k^2
\]

的残余根。候选工具应以能否通过 exact-support 闭合、least-factor 深度或不同半径之间的相关性实际缩小这个残余集合为准。

---

## 11. 可执行验证

`src/enterprise_math/p017_mirror_certificate.py`、`src/enterprise_math/p017_mirror_cross.py` 及其测试检查：

- L050 中 \(|S_k|\)、每个 \(N_p(k)\) 与 \(J_k\) 的公式与直接镜像 support 计数一致；
- L051 的有序素数对 CRT 计数与直接 surviving-radius 枚举一致；
- 有序素数对总和严格等于 \(E_k\)；
- \(U_k\)、\(V_k\) 与 \(E_k-|S_k|=U_k+V_k\) 的恒等式逐点成立；
- 在有界范围内，只要 L055 任一通道触发，直接检查都确认平方盆地中存在素数；
- \(k=31\)、37、46 固定上述边界；
- `3<=k<=1000` 的计数严格等于 273、594、140、727、6、733、323。

有限计算只用于审计实现与覆盖率统计；L050–L055 由精确容斥、CRT、双计数与上述整数不等式证明。
