# P017 镜像证书附录

状态：`ACTIVE RESEARCH ANNEX`  
范围：中心镜像 incidence 的精确公式与聚合素数证书  
依赖：规范 P017 镜像分离 L042–L045  
编号：本附录使用局部编号 `MC01–MC06`，不再占用全局 `L0xx` 序列。  
纪律：**本附录不证明 Legendre 猜想。** Möbius 容斥与中国剩余定理均为经典工具；项目特化内容是它们与中心镜像分离结合后得到的有限充分证书。

## 1. 镜像数据

令

\[
M=k(k+1),
\qquad
S_k=\{1\le r<k:\gcd(r,A_k)=1\},
\]

其中 `A_k` 是所有不超过 `k` 且整除 `M` 的 anchor 素数的平方自由乘积。对 `r in S_k`，定义

\[
P_-(r)=\operatorname{Supp}_{tr}(M-r),
\qquad
P_+(r)=\operatorname{Supp}_{tr}(M+r),
\]

并令

\[
a_r=|P_-(r)|,
\qquad b_r=|P_+(r)|.
\]

L043 已证明两侧 support 不交。若平方盆地无素数，L044 强制每个 surviving radius 满足

\[
a_r\ge1,
\qquad b_r\ge1.
\]

定义

\[
J_k=\sum_{r\in S_k}(a_r+b_r),
\qquad
E_k=\sum_{r\in S_k}a_rb_r.
\]

对 `K>=0`、`m>=1` 与 `1<=rho<m`，使用算术级数计数器

\[
\mathcal C(K;m,\rho)
=
\begin{cases}
0,&\rho>K,\\
1+\left\lfloor\frac{K-\rho}{m}\right\rfloor,&\rho\le K.
\end{cases}
\]

---

## 2. MC01 —— 一阶矩的精确 CRT/Möbius 公式

状态：`PROVED / CLASSICAL INCLUSION-EXCLUSION SPECIALIZATION`。

令 `K=k-1`。Möbius 容斥给出

\[
\boxed{|S_k|=\sum_{a\mid A_k}\mu(a)\left\lfloor\frac K a\right\rfloor.}
\]

固定横向素数 `p<=k`。对每个平方自由 `a|A_k`，定义

\[
t^+_{a,p}=(Ma^{-1})\bmod p,
\qquad
t^-_{a,p}=(-Ma^{-1})\bmod p,
\]

以及 `rho^+_{a,p}=a t^+_{a,p}`、`rho^-_{a,p}=a t^-_{a,p}`。令 `N_p(k)` 统计通过 anchor 筛选、且 `p` 整除某一侧镜像状态的半径，则

\[
\boxed{
N_p(k)=\sum_{a\mid A_k}\mu(a)
\bigl[\mathcal C(K;ap,\rho^+_{a,p})+
\mathcal C(K;ap,\rho^-_{a,p})\bigr].}
\]

两个镜像通道对横向素数互不重叠，所以

\[
\boxed{J_k=\sum_{p\le k,\ p\nmid M}N_p(k).}
\]

**证明。** 对 `gcd(r,A_k)=1` 使用经典 Möbius 指示恒等式，并附加一个镜像同余条件。写 `r=at` 后得到上述余数类。最后对横向素数求和即得到镜像 incidence 的按素数重索引。∎

这个公式不需要分解平方盆地内的任何状态。

---

## 3. MC02 —— 跨侧有序素数对的精确公式

状态：`PROVED / CLASSICAL CRT SPECIALIZATION`。

固定两个不同的横向素数 `p,q<=k`。令 `N_{p->q}(k)` 统计通过 anchor 筛选且满足

\[
p\mid M-r,
\qquad q\mid M+r
\]

的半径。对每个平方自由 `a|A_k`，写 `r=at`，并令

\[
c_p=(Ma^{-1})\bmod p,
\qquad
c_q=(-Ma^{-1})\bmod q.
\]

模 `pq` 的唯一规范解为

\[
\boxed{t_{a;p,q}=c_p+p\bigl((c_q-c_p)p^{-1}\bmod q\bigr),}
\]

且 `1<=t_{a;p,q}<pq`。令 `rho_{a;p,q}=a t_{a;p,q}`，则

\[
\boxed{
N_{p\to q}(k)=
\sum_{a\mid A_k}\mu(a)\mathcal C(K;apq,\rho_{a;p,q}).}
\]

对固定半径，满足 `p in P_-(r)`、`q in P_+(r)` 的有序素数对恰有 `a_r b_r` 个。因此

\[
\boxed{E_k=\sum_{p\ne q,\ p,q\le k,\ p,q\nmid M}N_{p\to q}(k).}
\]

这只是 CRT 与双计数；镜像 support 分离排除了 `p=q`。∎

---

## 4. MC03 —— 两个原始无素数松弛量

状态：`PROVED`。

定义

\[
\boxed{U_k=J_k-2|S_k|,}
\qquad
\boxed{V_k=E_k-J_k+|S_k|.}
\]

若平方盆地无素数，则

\[
\boxed{U_k\ge0,\qquad V_k\ge0.}
\]

**证明。** 令 `x_r=a_r-1`、`y_r=b_r-1`。在无素数假设下 `x_r,y_r>=0`，且

\[
U_k=\sum_r(x_r+y_r),
\qquad
V_k=\sum_r x_ry_r.
\]

二者都是非负整数之和。∎

同时

\[
\boxed{E_k-|S_k|=U_k+V_k.}
\]

---

## 5. MC04 —— 双松弛素数证书

状态：`PROVED`。

若

\[
\boxed{U_k<0\quad\text{或}\quad V_k<0,}
\]

则存在素数 `q` 满足

\[
k^2<q<(k+1)^2.
\]

这是 MC03 的逆否命题。

两个通道互不支配。`k=37` 时

\[
|S|=17,\ J=33,\ E=18,\quad U=-1,\ V=2,
\]

而 `k=46` 时

\[
|S|=22,\ J=47,\ E=18,\quad U=3,\ V=-7.
\]

后者的平方盆地包含素数 `2129`。

---

## 6. MC05 —— 聚合二次包络

状态：`PROVED`。

若平方盆地无素数，则

\[
\boxed{4V_k\le U_k^2.}
\]

**证明。** 对 MC03 中的非负 `x_r,y_r`，逐点有

\[
4x_ry_r\le(x_r+y_r)^2.
\]

因此

\[
4V_k\le\sum_r(x_r+y_r)^2
\le\left(\sum_r(x_r+y_r)\right)^2=U_k^2.
\]

∎

所以即使 `U_k,V_k>=0`，只要 `4V_k>U_k^2`，仍可直接推出平方盆地中存在素数。

---

## 7. MC06 —— 三通道证书与边界

状态：`PROVED`。

\[
\boxed{
U_k<0\quad\text{或}\quad V_k<0\quad\text{或}\quad4V_k>U_k^2
\Longrightarrow
\exists q\text{ 为素数，满足 }k^2<q<(k+1)^2.}
\]

`k=31` 时

\[
|S|=15,\ J=30,\ E=15,
\qquad U=V=0,
\]

三个通道都不触发，但 `967` 是 `(31^2,32^2)` 中的素数。因此 MC06 只是充分证书，不是素数存在的刻画。

---

## 8. 计算压力测试

状态：`COMPUTATIONAL`，不是定理。

对 `3<=k<=1000`，参考实现得到：

- `U_k<0`：273 个根；
- `V_k<0`：594；
- 二者同时为负：140；
- 两个负松弛通道并集：727；
- 仅由 `4V_k>U_k^2` 新增认证：6；
- MC06 三通道联合覆盖：**733**；
- 较弱的 `E_k<|S_k|`：323。

该范围内仍有 265 个根满足全部三个无素数必要不等式。本附录在这里主动停止无结构的 moment 扩张。

## 9. 研究边界

下一步必须使用 `(U_k,V_k)` 已经丢失的信息：exact-support 闭合、least-factor 深度或不同半径之间的相关性。一个值得优先验证的方向是 **least-factor gating**：使用一侧唯一的最小横向素因子，同时保留另一侧完整 support。它严格介于单个有序素数对与完整 support cell 之间，应先做压力测试再升级。

可执行验证位于 `src/enterprise_math/p017_mirror_certificate.py`、`src/enterprise_math/p017_mirror_cross.py`、`tests/test_p017_mirror_certificate.py` 与 `tests/test_p017_mirror_cross.py`。
