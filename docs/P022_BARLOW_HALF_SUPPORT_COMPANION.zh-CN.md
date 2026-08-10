# P022 — Companion 坐标下的 half-defect support avoidance

状态：`ACTIVE RESEARCH NOTE / EXACT COORDINATE REDUCTION + COUNTEREXAMPLE`  
Owner：`program/p022-geometry-v2`  
依赖：通用 midpoint-offset companion；canonical A-elimination；pure Franel defect  
跨路线相关：P018 cancellation/defect；P023 minimal repair 与 future-safe witnesses

## 1. support-avoidance 障碍

令 `p` 为强制 midpoint prime：

\[
p\equiv5,7\pmod8,
\qquad
m=\frac{p-1}{2},
\]

并假设 A-boundary

\[
2m-1=p-2
\]

为合数。

中央二项式坐标存在 canonical triangular elimination：

\[
A_m
=
\prod_{j<m}A_j^{\alpha_{m,j}}.
\]

对应 pure Franel defect 为

\[
D_m
=
\frac{F_m}{\prod_{j<m}F_j^{\alpha_{m,j}}}.
\]

即使 `p|F_m`，同一个 prime 仍可能已经出现在 A-elimination 使用的某个旧 `F_j` 中，从而在 `D_m` 中被抵消。

本笔记把这一障碍精确改写为通用 midpoint-companion 坐标下的整数序列避让问题。

---

## 2. P022-LI30 — support / companion 精确等价

定义 canonical A-elimination support：

\[
S_p
=
\{j<m:\alpha_{m,j}\ne0\}.
\]

对每个 `j in S_p`，定义 midpoint offset

\[
d_j=m-j.
\]

通用 companion theorem 给出

\[
p\mid F_j
\iff
p\mid N_{m-j}.
\]

因此

\[
\boxed{
S_p\cap Z_p=\varnothing
\iff
p\nmid N_{m-j}
\text{ 对所有 }j\in S_p.}
\]

右边已经完全不含 Franel table。support-avoidance 被改写成两个**通用整数构造**之间的相互作用：

1. central-binomial elimination support `S_p`；
2. midpoint companion numerators `N_d`。

这是严格坐标变换，不是猜想。

---

## 3. valuation 分解

任意本笔记范围内的 prime 都满足

\[
\boxed{
v_p(D_m)
=
v_p(F_m)
-
\sum_{j<m}\alpha_{m,j}v_p(F_j).}
\]

所以一旦 LI30 证明 support avoidance，修正和中的每一项都为 0，从而

\[
\boxed{v_p(D_m)=v_p(F_m).}
\]

这解释了为什么此前 one-unit half-defect 猜想必须拆成两个逻辑独立问题：

- support avoidance；
- midpoint 在模 `p^2` 下是否 simple lift。

通用 companion 解决了第一个问题的**正确形式**；参数 transversality theorem 则解决了第二个问题的**正确形式**。

---

## 4. P022-LI31 — 强制 midpoint divisibility 可以被完全抵消

素数

\[
\boxed{p=157}
\]

给出了对下面这个诱人推广的第一个尖锐反例：

\[
p\mid F_m
\Longrightarrow
p\mid D_m.
\]

这里

\[
m=78,
\qquad
2m-1=155=5\cdot31.
\]

canonical A-elimination 为

\[
\boxed{
A_{78}
=
A_1^2A_2^{-1}A_3^2A_4^{-1}
A_6A_7^{-1}A_{15}^{-1}A_{16}A_{77}.}
\]

通用 midpoint companion 满足

\[
157\mid N_{62}.
\]

而

\[
78-62=16,
\]

故 LI30 立即给出

\[
157\mid F_{16}.
\]

精确 valuation 为

\[
\boxed{v_{157}(F_{78})=1,}
\]

\[
\boxed{v_{157}(F_{16})=1.}
\]

canonical A-support 中没有其他指标贡献 `157`-valuation，而 `A_16` 的消元指数恰为 `+1`，因此

\[
\boxed{v_{157}(D_{78})=1-1=0.}
\]

强制 midpoint witness 被 canonical A-elimination **完整擦除**。

---

## 5. 为什么这个反例重要

此前的无限 half-index theorem 采用更窄的素数剩余类

\[
p\equiv5,23\pmod{24},
\]

它们满足 `p≡2 mod 3`，从而保证 `p-2` 为 composite boundary。

而反例

\[
157\equiv13\pmod{24}
\]

不属于这个 family。

这**不能**证明剩余类限制本身足以保证 support avoidance；但它证明该限制并非无关紧要：在更宽的强制 midpoint primes 中，support cancellation 确实会发生。

当前目标 `5,23 mod24` family 的精确压力测试尚未发现 support hit，但在有无限证明之前仍只是 finite evidence。

---

## 6. 新的算术 frontier

对目标 family，现在问题已经变成

\[
\boxed{
\text{证明或反驳 }
 p\nmid N_{m-j}
\text{ 对每个 canonical support index }j.}
\]

canonical support 来自把 `m` 与 `p-2` 递归展开到 central-binomial prime basis；zero 一侧则已经变成单一通用 numerator sequence `N_d`。

因此真正缺失的 theorem 可以精确命名为：

> **Companion-support avoidance problem.** 对 `p=5,23 mod24` 的目标剩余类，canonical A-elimination support 的 offset image 是否永远避开 midpoint companion numerator sequence 的 `p`-divisor set？

若找到反例同样价值很高，因为它会给出目标 infinite family 内第一个精确 cancellation mechanism。

---

## 7. 精度解释

这是 task-relative repair 的一个非常具体的负边界。

局部 witness `p|F_m` 并不自动在 canonical quotient/elimination 后保持可见；变换后的 observable 可能把它与保留的低层坐标精确抵消。

所以

\[
\boxed{
\text{local visibility}
\not\Rightarrow
\text{quotient-stable visibility}.}
\]

真正充分的状态必须针对声明的 future computation 验证——这里就是定义 pure defect 的 exact A-elimination。

这是 P022 对 A2/P023 一般原则的压力测试：witness sufficiency 必须在**应用 quotient/operation algebra 之后**检查，而不是之前。

---

## 8. 可执行资产

新增：

- `src/enterprise_math/p022_barlow_half_support_companion.py`；
- `tests/test_p022_barlow_half_support_companion.py`。

测试逐项交叉验证 direct Franel support hits 与 companion 坐标，并把 `p=157` 作为 `v_157(D_78)=0` 的精确 cancellation counterexample 长期保留。
