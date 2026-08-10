# P022 — half-defect A-support 的结构定位

状态：`ACTIVE RESEARCH NOTE / EXACT SUPPORT BOUND`  
Owner：`program/p022-geometry-v2`  
依赖：canonical central-binomial prime-basis expansion；half-index composite-boundary family  
跨路线相关：P018 cancellation；P023 quotient-stable witness sufficiency

## 1. 为什么 support localization 重要

对目标无限 half-index family

\[
p>5,\qquad p\equiv5\text{ 或 }23\pmod{24},
\qquad m=\frac{p-1}{2},
\]

我们已经知道

\[
p\mid F_m
\]

并且

\[
2m-1=p-2
\]

为合数。

pure defect 只有在 canonical central-binomial elimination 使用了一个同样被 `p` 整除的旧 Franel index 时，才可能擦除这个 witness。

通用 midpoint companion 已把这个问题变成 offset-prime 问题。本笔记再补上一条独立结构事实：canonical A-support 本身高度局域。

---

## 2. 整数 prime-basis support bound

回忆精确中央二项式递推：

\[
\frac{A_n}{A_{n-1}}
=\frac{2(2n-1)}{n},
\qquad
A_n=\binom{2n}{n}.
\]

对奇素数 `q`，canonical 递归表示在

\[
h=\frac{q+1}{2}
\]

处由

\[
q=\frac{h}{2}\frac{A_h}{A_{h-1}}
\]

产生。

新 A-indices 只有 `h,h-1`，再加上递归表示整数 `h` 本身所需的更小 indices。

令 `P(v)` 为正整数 `v>1` 的最大素因子。沿 prime-factor tree 归纳可得

\[
\boxed{
\max\operatorname{supp}_A(v)
\le
\frac{P(v)+1}{2}.}
\]

`v=1` 时 support 为空。

这是 P022 当前 canonical basis 的精确性质，不是渐近估计。

---

## 3. canonical half-index elimination

在 composite midpoint boundary 上，

\[
A_m
=A_{m-1}\frac{2(p-2)}{m}.
\]

因此 canonical A-relation 的 support 包含于

\[
\{m-1,1\}
\cup
\operatorname{supp}_A(p-2)
\cup
\operatorname{supp}_A(m).
\]

显式项 `m-1` 是唯一必然紧邻 midpoint 的 support index。

其他 indices 全部受 largest-prime-factor bound 控制。

---

## 4. P022-LI32 — `p=5 mod 24`：非邻接 support 全部落在左侧约三分之一

设

\[
p\equiv5\pmod{24}.
\]

则

\[
m=\frac{p-1}{2}
\]

为大于 2 的偶数，因此

\[
P(m)\le\frac m2.
\]

同时

\[
p-2=2m-1
\]

是 3 的奇合数倍数，所以

\[
P(p-2)\le\frac{p-2}{3}=rac{2m-1}{3}.
\]

套用 prime-basis support bound：

\[
\max\operatorname{supp}_A(m)
\le\frac{m+2}{4},
\]

而

\[
\max\operatorname{supp}_A(p-2)
\le
\left\lfloor\frac{m+1}{3}\right\rfloor.
\]

后者更宽，因此除显式 `m-1` 外，所有 canonical support index 都满足

\[
\boxed{
j\le\left\lfloor\frac{m+1}{3}\right\rfloor.}
\]

---

## 5. P022-LI33 — `p=23 mod 24`：非邻接 support 全部落在左半区

设

\[
p\equiv23\pmod{24}.
\]

此时 `m` 为奇数并且可能本身就是 prime，所以只能使用

\[
P(m)\le m.
\]

因此

\[
\max\operatorname{supp}_A(m)
\le\frac{m+1}{2}.
\]

`p-2` 的 factor-three bound 更小。故除 `m-1` 外，全部 support index 都满足

\[
\boxed{j\le\frac{m+1}{2}.}
\]

---

## 6. offset 形式：大块 automatic-safe zone

写 companion offset

\[
d=m-j.
\]

显式 support index `m-1` 对应 `d=1`。其余 support index 都满足 `j<=B`，其中

\[
B=
\begin{cases}
\lfloor(m+1)/3\rfloor,&p\equiv5\pmod{24},\\
(m+1)/2,&p\equiv23\pmod{24}.
\end{cases}
\]

所以每一个非平凡 support offset 都满足

\[
\boxed{d\ge m-B.}
\]

于是任意 companion zero 若位于

\[
2\le d<m-B,
\]

就**自动不可能**参加 canonical defect cancellation。

这在 midpoint 周围产生一块很大的 support-free 区域：

- `5 mod24` family 中，大约前 `2m/3` 的 offset range 自动安全；
- `23 mod24` family 中，大约前 `m/2` 自动安全。

精确端点以上述整数公式为准。

---

## 7. 尚未解决的部分

localization 并没有证明 full support avoidance。

远端 companion zeros 仍可能落到递归生成的左侧 support。目标 family 之外已经有 `p=157` 的精确 cancellation counterexample，说明这种现象确实存在。

因此目标 family 剩余问题已被严格缩窄成：

> **Far-offset collision problem.** 是否存在 prime divisor of the universal companion sequence，位于 `d>=m-B`，且反射回的 index `j=m-d` 正好属于 `m` 或 `p-2` 的 canonical prime-halving support tree？

当前压力范围内目标 `5,23 mod24` family 尚未发现这样的 hit，但在得到无限证明前仍只是有限证据。

---

## 8. 精度含义

现在一大类局部可见 Franel witnesses 可以**完全不用检查 Franel 值**就证明 quotient-stable：仅由 canonical elimination geometry 就能排除 cancellation。

因此 witness sufficiency 被拆成

\[
\boxed{
\text{structural safe zone}
+
\text{far-offset arithmetic residue}.}
\]

这给出了“确定性 representation bound”与真正“算术 repair frontier”的清楚分层。

---

## 9. 可执行资产

新增：

- `src/enterprise_math/p022_barlow_half_support_localization.py`；
- `tests/test_p022_barlow_half_support_localization.py`。

测试核验 recursive largest-prime-factor support bound、两个目标剩余类的定位定理，以及具体 support-offset 示例。
