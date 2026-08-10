# P022 — Franel 零位几何与 primitive midpoint

状态：`ACTIVE RESEARCH NOTE / EXACT ZERO-SET STRUCTURE`  
Owner：`program/p022-geometry-v2`  
依赖：Jarvis--Verrill 镜像同余；Franel recurrence；p-Lucas basin theorem

## 1. 三种结构同时约束 zero-digit set

对奇素数 `p`，记

\[
Z_p=\{1\le d\le p-1:p\mid F_d\}.
\]

现在有三个严格事实：

1. p-Lucas 使 `Z_p` 成为控制所有未来 Franel 整除的完整 digit alphabet；
2. Jarvis--Verrill 给出反射对称
   \[
   d\in Z_p\iff p-1-d\in Z_p;
   \]
3. Franel 的二阶递推禁止相邻两个 digit 同时为零。

第三点虽简单但很有用。递推为

\[
(k+1)^2F_{k+1}
=(7k^2+7k+2)F_k+8k^2F_{k-1}.
\]

若 `1<=k<=p-2` 且 `F_k=F_(k+1)=0 mod p`，则 `8k^2` 模 `p` 可逆，所以必有 `F_(k-1)=0`。不断向后传播最终会得到 `F_0=0`，与 `F_0=1` 矛盾。

故

\[
\boxed{Z_p\text{ 中不存在相邻整数}.}
\]

---

## 2. P022-LI18 — 强制中点是 primitive 当且仅当 zero alphabet 最小

假设

\[
p\equiv5,7\pmod8
\]

并令

\[
m=\frac{p-1}{2}.
\]

半指标定理已经给出

\[
m\in Z_p.
\]

反射固定 `m`。其他任何零位都必须形成一对

\[
\{d,p-1-d\},
\]

其中一个严格小于 `m`，另一个严格大于 `m`。

因此以下条件完全等价：

\[
\boxed{
\begin{aligned}
&p\text{ 在 }F_m\text{ 首次出现};\\
&r_p=m;\\
&Z_p=\{m\};\\
&z_p=1.
\end{aligned}}
\]

所以 **primitive half-index divisibility 恰好就是最小 p-Lucas basin**。

若中点不是 primitive，则 zero alphabet 至少有三个元素，并且必为

\[
\boxed{z_p=1+2s\quad(s\ge1).}
\]

最早的清晰边界是

\[
Z_{29}=\{12,14,16\},
\qquad r_{29}=12<14.
\]

---

## 3. P022-LI19 — Franel sequence 中存在无限多个 primitive-divisor events

半指标定理直接证明了：Franel sequence 被无限多个不同素数整除。

例如，由 Dirichlet 定理，存在无限多个

\[
p\equiv5\pmod8
\]

的素数。对每一个这样的 prime，都有

\[
p\mid F_{(p-1)/2}.
\]

对每个 prime 定义其首次出现位置

\[
r_p=\min\{n\ge1:p\mid F_n\}.
\]

在 `F_(r_p)` 中，`p` 按定义就是 Franel sequence 的 primitive divisor。

这些 `r_p` 不可能只落在有限多个指标上：固定的有限整数集合 `F_1,...,F_R` 只有有限多个素因子，而强制半指标 family 提供了无限多个互异 prime。

因此

\[
\boxed{
\text{Franel sequence 存在无限多个不同的 primitive-divisor events}.}
\]

等价地，强制半指标 prime family 的 rank of apparition 无界。

这**不**说明每个 `F_n` 都存在 primitive divisor，也不说明每个 composite-boundary defect 都能获得 primitive prime。

---

## 4. 对 composite-boundary family 的含义

进一步限制到无限素数剩余类

\[
p\equiv5,23\pmod{24},\qquad p>5.
\]

此时 `n=(p-1)/2` 位于 composite A-boundary，因为

\[
2n-1=p-2
\]

是大于 3 的 3 的倍数。

所以 composite-boundary half-index family 本身已经包含无限多个**互不相同**的 prime witnesses。即使其中一部分 prime 的首次出现位置更早，它们也不可能全部由某个有限初始 Franel prefix 反复解释。

这排除了一个很弱的替代解释：无限 composite witness family 并不是在循环复用有限几个旧素数。

---

## 5. 与 primitive-defect 充分条件的关系

现有全局低阶识别充分条件是：如果每个 composite-boundary `F_n` 都拥有新 primitive prime，就能把 pure defect family 三角化。

LI19 比这个条件弱，但已经告诉我们：

- primitive Franel events 确实无限出现；
- forced half-index primes 给出一条显式无限整除来源；
- 中点是否 primitive 已有局部精确判据 `z_p=1`；
- 真正未解决的是这些首次出现事件如何落到 composite-boundary indices，以及它们是否提供足够独立的 valuation 信息。

所以全局问题已经不再是“Franel 是否根本没有 primitive primes”。它们无限存在。困难已经被压缩到**出现位置与 defect 独立性**。

---

## 6. 可执行资产

新增：

- `src/enterprise_math/p022_barlow_franel_zero_geometry.py`；
- `tests/test_p022_barlow_franel_zero_geometry.py`。

测试核验 zero-set 镜像对称、递推禁止相邻零位、强制中点 family 的 odd zero-alphabet，以及 `p=23` 与 `p=29` 的 primitive / nonprimitive 精确对比。
