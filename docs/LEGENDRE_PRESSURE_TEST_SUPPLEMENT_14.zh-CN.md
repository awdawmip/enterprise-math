# 勒让德压力测试 — 补充 14

状态：`ACTIVE RESEARCH NOTE`  
范围：全部 high-band composites 与 L049 three-prime hit union 的精确有限包络，以及经典 Mertens 渐近推论  
依赖：P017 L021、L030–L040、L049、T007 整数根  
仅在渐近步骤使用的前人工作：[SRC-ROSSER-SCHOENFELD-1962-PRIME-ESTIMATES]  
纪律：**本文不证明勒让德猜想。** 素数倒数和的 Mertens 估计与素数计数估计属于经典数学。项目专门内容，是在调用这些解析估计之前，由平方结构先导出 high-band threshold、有限资源区间与有限 hit-count 包络。

## 1. 两类不同的高带状态

令

\[
I_k=\{k^2+1,\ldots,(k+1)^2-1\},
\qquad |I_k|=2k.
\]

高带中有两个值得分别计数的量。

第一，令 `N_H(k)` 表示 `I_k` 中所有满足最小素因子 `p` 有

\[
p^2\ge2k
\]

的**全部 composite states** 数量。它同时包含 high-band semiprime 与 three-prime states。

第二，令 `T_H(k)` 表示高带 **three-prime** states 数量。L049 已经对这个子集给出了更强的资源敏感不等式。

L050 先为这两类状态分别给出解析透明的有限包络，再把这些有限式交给经典素数估计。

---

## 2. 全部高带 composites 的有限包络

对每个素数 `p<=k`，L021 已经把 raw cofactor-window 长度与旧盆地命中数识别为同一个量：

\[
|W_p(k)|=H_p(k).
\]

真正的 least-factor shell 只是这些 raw multiples 的子集，而不同 least-factor shells 又彼此不交。因此

\[
N_H(k)
\le
A_H(k),
\]

其中

\[
\boxed{
A_H(k)
=
\sum_{\substack{p\ \mathrm{为素数}\\
\sqrt{2k}\le p\le k}}
H_p(k).
}
\]

这已经是一个有限精确整数不等式，而且自动包含 semiprime contribution；不需要对 cofactor 的素性作任何估计。

---

## 3. L049 three-prime 资源并集的有限包络

L049 对每个 cofactor resource prime `r` 定义已实现的 hit-state union `X_r(k)` 与容量

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

其中 `E_H(k)` 是 prime-square cofactor states 的精确数量。

若资源素数 `r` 出现，则存在合格 least prime `p` 满足

\[
p^2\ge2k,
\qquad
p\le r,
\qquad
p^2r\le U,
\qquad
U=(k+1)^2-1=k(k+2).
\]

所以

\[
\boxed{
\sqrt{2k}
\le r\le
\left\lfloor\frac{k+2}{2}\right\rfloor.
}
\]

`X_r(k)` 中每个状态都被 `r` 整除，因此

\[
c_r(k)\le H_r(k).
\]

定义

\[
\boxed{
B_H(k)
=
\sum_{\substack{r\ \mathrm{为素数}\\
\sqrt{2k}\le r\le\lfloor(k+2)/2\rfloor}}
H_r(k).
}
\]

则

\[
C_H(k)\le B_H(k).
\]

每个 least-prime shell 至多贡献一个 prime-square cofactor，而每个这样的 least prime 都满足 `p^3<=U`。所以完全不需要素数计数定理就有

\[
E_H(k)\le R_3(U).
\]

于是

\[
\boxed{
T_H(k)
\le
\left\lfloor
\frac{B_H(k)+R_3(U)}{2}
\right\rfloor.
}
\]

第 2–3 节全部都是有限整数运算。

---

## 4. L050 — 高带 log(2) 密度上限

状态：`PROVED`；极限部分为 `CLASSICAL ANALYTIC COROLLARIES`。

上述有限不等式推出

\[
\boxed{
\limsup_{k\to\infty}
\frac{N_H(k)}{2k}
\le
\log2.
}
\]

对 three-prime 子集，L049 再结合更窄的资源区间给出更强结论

\[
\boxed{
\limsup_{k\to\infty}
\frac{T_H(k)}{2k}
\le
\frac{\log2}{2}.
}
\]

等价地，

\[
\limsup_{k\to\infty}\frac{T_H(k)}k\le\log2.
\]

### 全部 high-band composites 的证明

对任意正模数 `d`，长度为 `2k` 的盆地满足

\[
H_d(k)\le\frac{2k}{d}+1.
\]

因此

\[
\frac{A_H(k)}{2k}
\le
\sum_{\substack{p\ \mathrm{为素数}\\
\sqrt{2k}\le p\le k}}
\frac1p
+
\frac{\pi(k)}{2k}.
\]

经典素数倒数 Mertens 定理给出

\[
\sum_{p\le x}\frac1p
=
\log\log x+B_1+o(1),
\]

标准素数计数估计给出 `pi(x)=o(x)`。所以素数计数余项趋于零，而

\[
\sum_{\sqrt{2k}\le p\le k}\frac1p
=
\log\log k-
\log\log\sqrt{2k}+o(1)
\longrightarrow
\log2.
\]

由于 `N_H(k)<=A_H(k)`，第一条 boxed limit 得证。∎

### three-prime 子集的证明

同理，

\[
\frac{B_H(k)}{2k}
\le
\sum_{\substack{r\ \mathrm{为素数}\\
\sqrt{2k}\le r\le(k+2)/2}}
\frac1r
+
\frac{\pi((k+2)/2)}{2k}.
\]

素数倒数区间贡献为

\[
\log\log\frac{k+2}{2}
-
\log\log\sqrt{2k}
+o(1)
\longrightarrow
\log2,
\]

素数计数项趋于零。另外 `R_3(U)=O(k^(2/3))`，故

\[
\frac{R_3(U)}{2k}\longrightarrow0.
\]

把有限 three-prime bound 除以 `2k`，得到

\[
\limsup\frac{T_H(k)}{2k}
\le
\frac{\log2}{2}.
\]

两段证明中的 Mertens 与素数计数步骤都属于成熟外部数学；项目专门内容只在于先把问题约化到这些由平方几何强制产生的特定素数区间。∎

---

## 5. 有限回归值

整数实现只检查有限不等式。

在 `k=110` 时，

\[
A_H(110)=106,
\qquad
N_H(110)=19.
\]

对 three-prime 资源包络，

\[
B_H(110)=72,
\qquad
R_3(U)=23,
\]

所以粗 L050 three-prime envelope 是 `47`，而 L049 的精确 hit union bound 是 `4`。

在 `k=500` 时，

\[
A_H(500)=534,
\qquad
N_H(500)=77,
\]

且

\[
B_H(500)=418,
\qquad
R_3(U)=63,
\]

所以粗 three-prime envelope 是 `240`，而 L049 给出 `17`。

这种松弛是故意的：L049 是精确有限工具；L050 是暴露统一解析常数的那一层。

---

## 6. L050 真正改变了什么

在 L050 之前，high-band semiprime contribution 仍被列为独立未控部分。第一条 L050 不等式改变了这个诊断：**全部** high-band composites，包括 semiprimes，现在都有一个非平凡的渐近密度上限。

因此渐近上至少有比例

\[
1-\log2
\]

的平方盆地状态**不是** high-band composites。它们仍可能是 lower-band composites，所以这不是素数密度定理，也不能推出勒让德猜想。

剩余阻碍现在更集中：

1. 满足 `p^2<2k` 的 lower least-factor shells；
2. 把 high-band deficit 与 L045 mirror-incidence demand 真正耦合起来；
3. 对 lower band 做 root-scale descent 或得到其他确定性上界，使其不能填满剩余比例。

下一步应直接攻击 lower band 或建立真实的 high/low-band coupling。除非能改善这个核心阻碍，否则不应继续细化同一个 Mertens 区间。
