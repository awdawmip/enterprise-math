# Legendre 压力测试 — 补充 12

状态：`ACTIVE RESEARCH NOTE`  
范围：用 CRT/idempotent 编码镜像两侧 support，并计算有界 sign-pattern 容量  
依赖：P017 L042–L045 及通过 anchor 筛选的镜像三元组两两互素推论  
纪律：**本文不证明 Legendre 猜想。** 中国剩余定理、平方自由乘积模意义下的 1 的平方根和幂等元都是经典代数。项目特化只在于：把它们与平方盆地共同中心以及有界半径 \(1\le r<k\) 结合。

## 1. 为什么还要引入 idempotent？

对一个通过 anchor 筛选的半径

\[
1\le r<k,
\qquad M=k(k+1),
\]

L043 给出两个镜像状态的横向 support 严格不交。若两侧 support 都非空，记

\[
P_-=\operatorname{Supp}_{\mathrm{tr}}(M-r),
\qquad
P_+=\operatorname{Supp}_{\mathrm{tr}}(M+r),
\]

对应平方自由乘积

\[
D_-=\prod_{p\in P_-}p,
\qquad
D_+=\prod_{p\in P_+}p,
\qquad
D=D_-D_+.
\]

CRT 并不会给这个划分增加新信息。它的价值在于：把完整的左右符号分配压缩成一个剩余类，然后精确计算在有限窗口 \(1\le r<k\) 中有多少半径可以实现这一符号模式。

---

## 2. L046 —— 镜像 support 划分对应一个 CRT 幂等元

状态：`PROVED / CLASSICAL CRT SPECIALIZATION`。

由于整除 \(D\) 的每个素数都是横向素数，

\[
\gcd(M,D)=1,
\]

且 \(D\) 为奇数。定义

\[
u\equiv rM^{-1}\pmod D.
\]

对 \(p\mid D_-\)，由 \(p\mid M-r\) 得

\[
u\equiv1\pmod p.
\]

对 \(p\mid D_+\)，由 \(p\mid M+r\) 得

\[
u\equiv-1\pmod p.
\]

因此

\[
\boxed{u^2\equiv1\pmod D.}
\]

因为 2 在奇数模 \(D\) 下可逆，令

\[
e\equiv(1+u)2^{-1}\pmod D.
\]

则

\[
\boxed{e^2\equiv e\pmod D.}
\]

而且

\[
e\equiv1\pmod p\quad(p\in P_-),
\qquad
 e\equiv0\pmod p\quad(p\in P_+),
\]

所以可以精确恢复两侧 support product：

\[
\boxed{
D_-=\gcd(e-1,D),
\qquad
D_+=\gcd(e,D).
}
\]

因为两侧都非空，\(e\) 是模 \(D\) 的非平凡幂等元。

这只是经典 CRT/idempotent 对应在镜像数据上的特化；本文不对该代数对应本身提出新颖性主张。

---

## 3. L047 —— 固定 sign pattern 的精确有界 lift

状态：`PROVED`。

反过来固定：

- 平方盆地根 \(k\) 与中心 \(M=k(k+1)\)；
- 一个奇的、平方自由的横向模数 \(D\)，满足 \(\gcd(M,D)=1\)；
- 模 \(D\) 的一个非平凡幂等元 \(e\)。

令

\[
u\equiv2e-1\pmod D,
\]

则 \(u^2\equiv1\pmod D\)。再定义

\[
\rho\equiv Mu\pmod D,
\qquad 1\le\rho\le D-1.
\]

一个半径实现这一固定的 CRT 左右符号模式，当且仅当

\[
\boxed{r\equiv\rho\pmod D.}
\]

因此所有正的有界 lift 恰为

\[
\boxed{r=\rho+jD}
\]

其中 \(j\ge0\) 且 \(r<k\)。未过滤的 sign-pattern 容量精确等于

\[
\boxed{
C^{\mathrm{sign}}_{D,e}(k)
=
\begin{cases}
0,&\rho\ge k,\\
1+\left\lfloor\dfrac{k-1-\rho}{D}\right\rfloor,&\rho<k.
\end{cases}
}
\]

再施加 \(\gcd(r,A_k)=1\) 的 anchor survival 条件，只会减少该数量。

特别地，

\[
\boxed{D\ge k\Longrightarrow C^{\mathrm{sign}}_{D,e}(k)\le1.}
\]

所以一个足够大的固定左右符号模式在平方盆地内至多由一个有界镜像半径实现。

---

## 4. L048 —— Exact-support 容量只被 sign-pattern 容量上界，不与之相等

状态：`PROVED`。

若希望 \(D\) 表示一个镜像对的**完整**横向 support，并由 \(e\) 指定左右分配，那么任何 exact-support 实现都必须满足 L047 的同余条件。因此

\[
\boxed{
C^{\mathrm{exact}}_{D,e}(k)
\le
C^{\mathrm{anchor}}_{D,e}(k)
\le
C^{\mathrm{sign}}_{D,e}(k),
}
\]

其中中间项只计算同时通过 anchor 筛选的 sign-pattern lift。

第一个不等式可以严格成立，因为某个有界 lift 虽然满足 \(D\) 上所有指定同余，但可能额外获得一个不属于 \(D\) 的横向素数。

### 严格例子

取

\[
k=46,
\qquad M=46\cdot47=2162.
\]

在半径 \(r=7\) 时，横向 support 为

\[
P_-=\{5\},
\qquad
P_+=\{3\}.
\]

因此

\[
D=15,
\qquad e=6\pmod{15}.
\]

对应的、通过 anchor 筛选的有界 sign-pattern lifts 为

\[
\boxed{r=7,37.}
\]

在 \(r=7\) 时，完整横向 support 正好是 \(\{3,5\}\)。

但在 \(r=37\) 时，左侧状态为

\[
M-r=2125=5^3\cdot17,
\]

因此同一个模 15 的符号模式额外获得了横向素数 17，已经不再是 \(D=15\) 的 exact-support 实现。

所以该例中

\[
C^{\mathrm{exact}}_{15,6}(46)=1
<
C^{\mathrm{anchor}}_{15,6}(46)=2.
\]

这直接纠正了一个诱人的错误解释：CRT sign-pattern progression 并不会自动分类完整 support cell。

---

## 5. 与 L041 和镜像路线的关系

现在三层工具的职责彼此独立：

\[
\boxed{
\text{L041：一次大模数命中后的 support 闭合}
}
\]

\[
\boxed{
\text{L042--L045：跨状态镜像 support 分离}
}
\]

\[
\boxed{
\text{L046--L048：有界 CRT sign-pattern 容量}
}
\]

CRT 层只有在它真正缩短后续容量论证时才值得保留。凡是需要完整素因子内容的证明，不应让 sign pattern 取代原始 support set，因为 sign-pattern lifts 是 exact-support 实现的超集。

下一步真正有意义的问题，是把这些**上界容量**再施加 anchor survival 与 exact-support/smooth-closure 过滤后，其总和是否会小于一个假想无素数盆地所必须覆盖的镜像对数量。

若答案是否定的，则 CRT 路线应降格为坐标工具，不再继续扩张词汇。

---

## 6. 可执行验证

`src/enterprise_math/p017_mirror_crt.py` 与 `tests/test_p017_mirror_crt.py` 检查：

- 实际观测到的两侧镜像 support 产生一个 1 的平方根和非平凡幂等元；
- 与 \(e\)、\(e-1\) 的 gcd 精确恢复两侧 support product；
- 固定 sign pattern 的所有有界实现落在模 \(D\) 的一条算术级数中；
- anchor 过滤不会增加容量；
- exact-support lifts 是 anchor-surviving sign-pattern lifts 的子集；
- \((k,D,e)=(46,15,6)\) 使第一个包含严格；
- 当 \(D\ge k\) 时，固定 sign pattern 至多有一个有界 lift。

有限计算只用于审计参考实现；CRT 事实与计数公式由上文证明。
