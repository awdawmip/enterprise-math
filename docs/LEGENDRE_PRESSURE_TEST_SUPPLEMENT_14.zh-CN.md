# 勒让德压力测试 — 补充 14

状态：`ACTIVE RESEARCH NOTE`  
范围：L049 hit-state union 之上的精确有限包络，以及其经典 Mertens 渐近推论  
依赖：P017 L039、L049、T007 整数根  
仅在渐近步骤使用的前人工作：[SRC-ROSSER-SCHOENFELD-1962-PRIME-ESTIMATES]  
纪律：**本文不证明勒让德猜想。** 素数倒数和的 Mertens 定理及素数计数估计属于经典数学。项目专门内容，是在调用这些解析估计之前先推导出有限资源区间与有限 hit-count 包络。

## 1. 从精确命中并集到更粗的解析包络

L049 对每个 cofactor resource prime `r` 定义已实现的高带 hit-state union `X_r(k)` 与容量

\[
c_r(k)=|X_r(k)|.
\]

令

\[
C_H(k)=\sum_r c_r(k).
\]

L049 已证明

\[
2T_H(k)-E_H(k)\le C_H(k),
\]

其中 `T_H(k)` 是全部高带 three-prime states 数量，`E_H(k)` 是 prime-square cofactor states 的精确数量。

精确并集很强，但不易做统一解析估计。本文把它放在一个更简单的有限量之下，使其渐近大小可以由经典素数估计直接读取。

---

## 2. 通用资源区间

令

\[
U=(k+1)^2-1=k(k+2).
\]

若资源素数 `r` 出现在 L049 的高带构造中，则存在合格 least prime `p` 满足

\[
p^2\ge2k,
\qquad
p\le r,
\qquad
p^2r\le U.
\]

因此

\[
\boxed{r\ge\sqrt{2k}}
\]

且

\[
\boxed{r\le\frac{U}{2k}=\frac{k+2}{2}.}
\]

所以每个高带 cofactor resource 都落在有限素数区间

\[
\boxed{
\sqrt{2k}
\le r\le
\left\lfloor\frac{k+2}{2}\right\rfloor.
}
\]

这个区间完全由平方盆地上端点与 high-band threshold 强制产生。

---

## 3. L050 — 有限命中数包络与 log(2) 上限

状态：`PROVED`；其中渐近部分为 `CLASSICAL ANALYTIC COROLLARY`。

定义

\[
B_H(k)
=
\sum_{\substack{r\ \mathrm{为素数}\\
\sqrt{2k}\le r\le\lfloor(k+2)/2\rfloor}}
H_r(k).
\]

则

\[
\boxed{C_H(k)\le B_H(k).}
\]

再令

\[
R_3(U)=\max\{m\in\mathbb N_0:m^3\le U\}.
\]

则得到完全有限的整数上界

\[
\boxed{
T_H(k)
\le
\left\lfloor
\frac{B_H(k)+R_3(U)}{2}
\right\rfloor.
}
\]

最后，经典素数倒数和与素数计数估计推出

\[
\boxed{
\limsup_{k\to\infty}\frac{T_H(k)}{k}
\le
\log2.
}
\]

相对于开平方盆地中的 `2k` 个状态，等价地有

\[
\boxed{
\limsup_{k\to\infty}\frac{T_H(k)}{2k}
\le
\frac{\log2}{2}.
}
\]

### 有限包络的证明

`X_r(k)` 中每个状态都被 `r` 整除，所以

\[
c_r(k)\le H_r(k).
\]

第 2 节说明显示区间外不可能出现任何资源素数，因此求和得到

\[
C_H(k)\le B_H(k).
\]

对于平方修正，每个 least-prime shell 至多贡献一个 prime-square cofactor；而每个这样的 shell 都满足

\[
p^3\le U.
\]

所以甚至无需使用素数计数定理，就有

\[
E_H(k)\le R_3(U).
\]

结合 L049：

\[
2T_H(k)-E_H(k)\le C_H(k)\le B_H(k),
\]

从而

\[
T_H(k)
\le
\left\lfloor\frac{B_H(k)+R_3(U)}2\right\rfloor.
\]

至此全部都是有限整数运算。∎

### 经典解析推论

盆地长度为 `2k`，所以对任意正模数 `r`，

\[
H_r(k)
\le
\frac{2k}{r}+1.
\]

因此

\[
\frac{B_H(k)}{2k}
\le
\sum_{\substack{r\ \mathrm{为素数}\\
\sqrt{2k}\le r\le(k+2)/2}}
\frac1r
+
\frac{\pi((k+2)/2)}{2k}.
\]

经典素数倒数 Mertens 定理给出

\[
\sum_{p\le x}\frac1p
=
\log\log x+B_1+o(1),
\]

标准素数计数估计给出

\[
\pi(x)=o(x).
\]

所以第二项趋于零，而素数倒数区间贡献为

\[
\log\log\frac{k+2}{2}
-
\log\log\sqrt{2k}
+o(1).
\]

由于

\[
\frac{\log((k+2)/2)}{\log\sqrt{2k}}
\longrightarrow2,
\]

这个差趋于

\[
\log2.
\]

又因为 `R_3(U)=O(k^(2/3))`，

\[
\frac{R_3(U)}{2k}\longrightarrow0.
\]

把有限 L050 上界除以 `k`，即得

\[
\limsup_{k\to\infty}\frac{T_H(k)}k\le\log2.
\]

这里 Mertens 与素数计数步骤都属于成熟外部数学；项目专门内容只在于平方几何导出的端点和把问题约化到这个素数区间。∎

---

## 4. 有限回归值

整数参考实现直接从精确 hit counts 计算 `B_H(k)`。

在

\[
k=110
\]

时，

\[
B_H(110)=72,
\qquad
R_3(U)=23,
\]

所以粗有限 L050 包络为

\[
T_H(110)\le47.
\]

L049 的精确 union bound 则是 `4`。这完全符合预期：L050 故意牺牲状态并集信息，以换取解析透明性。

在

\[
k=500
\]

时，

\[
B_H(500)=418,
\qquad
R_3(U)=63,
\]

从而

\[
T_H(500)\le240,
\]

而 L049 精确并集给出 `17`。

所以 L050 不是 L049 的替代物，它的作用是从一个刻意更容易估计的量获得统一渐近上限。

---

## 5. 压力测试解释

`log(2)` 并不是新素数分布规律的证据。它只是项目推导出的资源窗口

\[
[\sqrt{2k},\,(k+2)/2]
\]

所承载的经典素数倒数质量。

真正处于项目压力测试中的，是链条

\[
\text{平方盆地}
\to
\text{high-band factor threshold}
\to
\text{有限资源区间}
\to
\text{L049 精确 hit unions}
\to
\text{L050 解析包络}.
\]

这个渐近结论有价值，因为它证明高带 **three-prime** composites 单独不可能占据超过某个固定渐近比例的盆地。但它离勒让德仍然很远：semiprimes 与 lower least-factor shells 尚未被这个常数控制。

所以下一个严肃目标应当是：

1. 为 semiprime contribution 得到可比的非平凡包络；
2. 把 lower band `p^2<2k` 分解并运输到更小 root scale；
3. 建立 L049/L050 与 L045 mirror-incidence demand 之间的真实不等式。

除非能改善上述缺口之一，否则不应继续细化同一个素数倒数窗口。
