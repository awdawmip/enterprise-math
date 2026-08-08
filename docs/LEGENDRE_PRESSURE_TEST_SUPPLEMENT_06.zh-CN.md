# Legendre 压力测试 —— 补充 06

状态：`ACTIVE RESEARCH NOTE`  
范围：平方盆地 cofactor window 内的精确 least-factor recursion、高 least-factor 收缩，以及一条 sieve-density 禁止捷径结果  
依赖：P017 L020–L027  
前人工作：rough-number 计数与 Buchstab 最小素因子递归属于成熟筛法。[SRC-FAN-2023-ROUGH-NUMBERS] [SRC-LI-2025-BUCHSTAB]  
纪律：**本文不证明 Legendre 猜想。** 本文要检验的是：相邻平方强制产生的特殊移动窗口，是否比一般 rough-number 密度提供更强的有限约束。

## 1. 为什么下一步不是一种新筛法

L022 已把每个 first-factor shell 化约为

\[
L_p(k)=\{pq:q\in W_p(k),\ q\text{ 为 p-rough}\}.
\]

若存活的 cofactor `q` 仍为合数，数学上最规范的下一步就是暴露它的最小素因子。这就是标准 Buchstab / least-factor recursion，而不是新的进取数论构造。

项目真正的问题更窄：

> `W_p(k)` 具有由平方几何给出的精确端点和精确 bulk-plus-carry 宽度律；标准 least-factor recursion 在这些窗口上是否会产生异常强的收缩？

答案是在一个显式的高 least-factor 带中确实如此。

---

## 2. L028 —— 精确有限区间 least-factor recursion

状态：`PROVED SPECIALIZATION OF ESTABLISHED BUCHSTAB-TYPE RECURSION`。

对整数

\[
1\le A\le B
\]

以及阈值 `z>=2`，定义

\[
\mathcal R_z[A,B]
=
\{q\in[A,B]:q\text{ 不存在 }<z\text{ 的素因子}\}.
\]

把该集合分成素数和合数两部分。

若 `q` 为合数，令

\[
\ell=\operatorname{spf}(q).
\]

因为 `q` 是 `z`-rough，

\[
\ell\ge z.
\]

写成

\[
q=\ell s.
\]

由于 `ell` 是最小素因子，

\[
s\ge\ell,
\]

并且 `s` 为 `ell`-rough。区间条件给出

\[
\left\lceil\frac A\ell\right\rceil
\le s\le
\left\lfloor\frac B\ell\right\rfloor.
\]

所以 rough interval 的合数部分是如下不交并：

\[
\boxed{
\mathcal R_z[A,B]_{\rm comp}
=
\coprod_{\substack{\ell\text{ 为素数}\\
\ell\ge z}}
\left\{
\ell s:
\max\!\left(\ell,\left\lceil\frac A\ell\right\rceil\right)
\le s\le
\left\lfloor\frac B\ell\right\rfloor,
\ s\text{ 为 ell-rough}
\right\}.
}
\]

只有

\[
\ell\le\sqrt B
\]

可能产生非空分支。

### 证明

每个正合数都有唯一最小素因子。上述条件直接来自唯一分解、roughness 定义以及用正数 `ell` 除区间不等式。反过来，任意显示出的 `ell,s` 对，其乘积最小素因子恰为 `ell`，且位于 `[A,B]`，因此对应 rough interval 中唯一一个合数成员。∎

这就是标准 least-prime-factor / Buchstab 分解的精确有限区间形式。[SRC-LI-2025-BUCHSTAB]

用于 P017 时取

\[
A=q_{\min}(k,p),
\qquad
B=q_{\max}(k,p),
\qquad
z=p.
\]

---

## 3. L029 —— 每个 child window 长度仍是 quotient response

状态：`PROVED`。

设父区间为 `[A,B]`，长度

\[
N=B-A+1.
\]

对固定素数 `ell`，父区间中 `ell` 的倍数个数为

\[
M_\ell
=
\left\lfloor\frac B\ell\right\rfloor
-
\left\lfloor\frac{A-1}\ell\right\rfloor.
\]

因为

\[
B=(A-1)+N,
\]

所以这恰好是

\[
\boxed{
M_\ell
=
Q_\ell((A-1)+N)-Q_\ell(A-1).
}
\]

因此 P018 的 quotient-response 恒等式再次适用：

\[
\boxed{
M_\ell
=
\left\lfloor\frac N\ell\right\rfloor
+
\kappa_\ell((A-1)\bmod\ell,\ N\bmod\ell).
}
\]

特别地，

\[
\boxed{
M_\ell\le\left\lceil\frac N\ell\right\rceil.
}
\]

真正的 least-factor child 还要求

\[
s\ge\ell,
\]

所以其 raw 长度不会超过 `M_ell`。

这给出精确递归收缩机制：

> 提取下一最小素因子后，当前 raw window 长度至少被该素数除一次，只允许再出现一个 boundary carry。

---

## 4. L030 —— 高带父窗口上界

状态：`PROVED`。

回到 P017 cofactor window `W_p(k)`，令

\[
N_p=|W_p(k)|_{\rm raw}.
\]

L024 给出，令

\[
r=k+1-p,
\qquad
h=2r-2=2k-2p,
\]

则

\[
N_p
=2+\Delta Q_p,
\]

其中

\[
\Delta Q_p
=
\left\lfloor\frac{a+h}{p}\right\rfloor
-
\left\lfloor\frac a p\right\rfloor
\le
\left\lceil\frac hp\right\rceil.
\]

假设

\[
\boxed{p^2\ge2k.}
\]

则

\[
h=2k-2p
\le p^2-2p
=p(p-2).
\]

所以

\[
\left\lceil\frac hp\right\rceil\le p-2,
\]

从而

\[
\boxed{N_p\le p.}
\]

这是一个真正依赖平方盆地的收缩阈值，因为它使用了 P017 窗口中的精确关系 `r=k+1-p`。

---

## 5. L031 —— 高带中每个第二最小素因子至多一个 raw child

状态：`PROVED`。

在

\[
p^2\ge2k
\]

条件下，令 `ell>=p` 为 composite cofactor `q` 的一个可能第二最小素因子。

由 L029，

\[
M_\ell
\le
\left\lceil\frac{N_p}{\ell}\right\rceil.
\]

因为

\[
N_p\le p\le\ell,
\]

得到

\[
\boxed{M_\ell\le1.}
\]

因此：

\[
\boxed{
\text{对每个可能的第二最小素数 }\ell,
\text{父 cofactor window 中至多存在一个 }\ell\text{ 的 raw multiple。}
}
\]

进一步施加 `s>=ell` 与 `ell`-rough 条件后，一个 branch 可以消失，但永远不会裂成两个候选。

所以第二层 Buchstab recursion 在这里变成了**二元存在/不存在 branch**。

---

## 6. L032 —— 高带 factor-depth 分类

状态：`PROVED`。

继续假设

\[
p^2\ge2k.
\]

令

\[
U=(k+1)^2-1.
\]

则

\[
p^4\ge4k^2.
\]

对任意 `k>=1`，

\[
4k^2>k^2+2k=U.
\]

所以

\[
p^4>U.
\]

应用 L026，取 `m=3`，得到

\[
\boxed{\Omega(n)\le3}
\]

对每个 `n in L_p(k)` 成立。

由于 shell 状态必为合数且最小素因子为 `p`，只剩两种可能：

### 类型 A —— semiprime

\[
\boxed{n=pq,\qquad q\text{ 为素数},\quad q\ge p.}
\]

### 类型 B —— three-prime state

\[
\boxed{n=p\ell s,\qquad p\le\ell\le s,\quad \ell,s\text{ 为素数}.}
\]

由 L031，对每个固定第二素数 `ell` 至多存在一个 raw child，所以最多对应一个类型 B 状态。

因此高 least-factor 带满足精确计数分解

\[
\boxed{
|L_p(k)|
=
\#\{q\in W_p(k):q\text{ 为素数}\}
+
\sum_{\substack{\ell\text{ 为素数}\\
\ell\ge p}} I_{p,\ell}(k),
}
\]

其中

\[
I_{p,\ell}(k)\in\{0,1\}
\]

表示唯一可能的第二因子 branch 是否实际产生一个 `s>=ell` 的素数 tail。

这比一般 rough-number count 更具体：该高带中的非素数 cofactor 已经被压成二值 three-prime branches。

---

## 7. 更强的上带：只剩 semiprime

L026 已给出更强条件

\[
p^3>U,
\]

此时

\[
\Omega(n)\le2.
\]

因为 shell 状态必为合数，每个状态都恰为 semiprime：

\[
\boxed{n=pq,\qquad p\le q\text{ 为素数}.}
\]

因此高 least-factor 区域有两个精确层：

1. `p^3>U`：只有 semiprime；
2. `p^2>=2k` 但 `p^3<=U`：semiprime 加二值 three-prime branches。

在 `p^2<2k` 以下，child window 可能含多个候选，确实需要更深 Buchstab recursion。

---

## 8. L033 —— 一阶 sieve-density 权重精确望远镜

状态：`PROVED FINITE ALGEBRAIC IDENTITY`；其解释只作诊断，不是严格短区间估计。

设

\[
p_1<p_2<\cdots<p_m
\]

为前 `m` 个素数，并定义进入 `p_i` 以前的独立筛存活因子

\[
V_i
=
\prod_{j<i}\left(1-\frac1{p_j}\right).
\]

则

\[
V_{i+1}
=V_i\left(1-\frac1{p_i}\right),
\]

所以精确有

\[
\boxed{
\frac{V_i}{p_i}
=V_i-V_{i+1}.
}
\]

求和得到有限望远镜

\[
\boxed{
\sum_{i=1}^m\frac{V_i}{p_i}
=1-V_{m+1}.
}
\]

### 为什么重要

“最小素因子恰为 `p_i`”的一阶独立密度模型因此使用一组会随着加入更多素数而几乎耗尽总密度的权重。它并不存在一个显然固定为正的 density margin，可以轻易保证每个平方盆地一定剩下一个素数。

这阻断了一条很诱人的错误研究捷径：

> 不能仅因为每个单独 p-rough window 的平均密度较低，就把这些密度相加并假定最后必然留下统一常数余量，从而证明 P017。

如果仍有额外杠杆，只能来自**特殊移动平方窗口相对平均筛密度的结构性 discrepancy**，而不是一阶平均密度本身。

---

## 9. 这次审计真正得到什么

P017 当前活跃路线已经明显变短。

### 几何

L021–L025 已精确解决：

\[
\text{最小素数 }p
\to
\text{有限 cofactor window }W_p(k).
\]

### 算术递归

使用成熟 Buchstab least-factor decomposition，但 child-window transport 由 L029 精确控制。

### 高带简化

当

\[
p^2\ge2k
\]

时，每个第二素数 branch 至多一个候选且 `Omega<=3`。

### 禁止捷径

L033 表明平均独立筛密度没有固定余量。

因此下一个真正新的目标被精确缩为：

\[
\boxed{
\text{控制 p-rough survivors 在平方导出移动窗口中的 discrepancy}
}
\]

或者证明这种额外 discrepancy 上界根本不存在。

## 10. 下一步攻击

1. **二值 three-prime branch 几何。** 推导每个 `(p,ell)` 高带 branch 中唯一可能 child `s` 的精确公式，并寻找不同 `ell` 之间的共同中心约束。
2. **短窗口筛上界。** 将已有 upper-bound sieve 结果与 P017 精确窗口长度比较，记录现有常数究竟是否真的不够。
3. **递归 transport。** 连续两层追踪 boundary-carry bit，检验嵌套平方端点是否制造非一般性的相关性。
4. **反例优先 discrepancy 测试。** 任意 rough-window discrepancy 的符号或上界猜想，在升格前必须先做大范围有限压力测试。
5. **不要换名字重新引入 Möbius parity。** 如果递归最终只复现经典 parity obstruction，应明确记录为负结果并换路线。
