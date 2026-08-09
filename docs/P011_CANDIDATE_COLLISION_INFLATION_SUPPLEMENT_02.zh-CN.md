# P011 补充 02 —— 候选域扩张造成的碰撞虚增

状态：`PROVED RESEARCH NOTE`  
归属：A1 / P011 collision spectrum  
来源压力：P023 actual-image separation 与 P017 L052/L055 的 candidate-vs-realized 差异  
纪律：二项式与 Vandermonde 恒等式属于成熟组合数学；这里不提出历史优先权主张。

## 1. 设置

令 `I` 为有限标签集合。对每个标签 `i`，给定真实 image 与候选 superset

\[
A_i\subseteq C_i\subseteq Y.
\]

把带标签 incidence 状态 `(i,y)` 投影到 `y`。定义

\[
m_A(y)=\#\{i:y\in A_i\},
\qquad
m_C(y)=\#\{i:y\in C_i\},
\]

以及候选扩张厚度

\[
\boxed{\delta(y)=m_C(y)-m_A(y)\ge0.}
\]

对应 P011 碰撞多项式

\[
K_A(t)=\sum_y((1+t)^{m_A(y)}-1),
\qquad
K_C(t)=\sum_y((1+t)^{m_C(y)}-1).
\]

## 2. P011-S02-T01 —— exact candidate-domain collision inflation

有

\[
\boxed{
K_C(t)-K_A(t)
=
\sum_y
(1+t)^{m_A(y)}
\big((1+t)^{\delta(y)}-1\big)
\in\mathbb N[t].
}
\]

证明只需逐 `y` 使用

\[
(1+t)^{m_A+\delta}-(1+t)^{m_A}
=(1+t)^{m_A}((1+t)^\delta-1).
\]

因此 candidate enlargement 不会降低任何阶的碰撞系数。

## 3. P011-S02-T02 —— 每一阶的精确虚增

记

\[
J_k(A)=\sum_y\binom{m_A(y)}k,
\qquad
J_k(C)=\sum_y\binom{m_C(y)}k.
\]

由 Vandermonde：

\[
\boxed{
J_k(C)-J_k(A)
=
\sum_y\sum_{j=1}^k
\binom{m_A(y)}{k-j}
\binom{\delta(y)}j.
}
\]

每一项都是非负整数，所以所有 collision orders 同时单调增加。

## 4. 二阶假碰撞的闭式

当 `k=2`：

\[
\boxed{
J_2(C)-J_2(A)
=
\sum_y
\left(
m_A(y)\delta(y)
+
\binom{\delta(y)}2
\right).
}
\]

两项含义不同：

- `m_A delta`：新增候选 incidence 与真实 incidence 之间制造的假 pair collision；
- `binom(delta,2)`：两个都不真实的新候选 incidence 彼此制造的纯候选 collision。

因此“候选集比真实集大多少”可以直接转成整数 collision inflation，而不是只说“上界比较松”。

## 5. P011-S02-C01 —— actual images 已分离时，candidate collision 全是假的

若真实 shell images 两两不交，则

\[
m_A(y)\le1,
\]

从而对所有 `k>=2`，

\[
J_k(A)=0.
\]

因此候选层出现的任意高阶碰撞都完全由扩张产生。

这给 P023 image-separation 工具一个精确成本量：zero-repair 的真实系统，仍可能因为候选 superset 而在证明层人为产生非零 collision budget。

## 6. P017 k=14 的精确虚增

L052 的候选 root pairs 在 `k=14` 给出

\[
C_2=\{9,10\},
\qquad
C_3=\{8,9\}.
\]

但 exact windows 的真实 root images 是

\[
A_2=\{9,10\},
\qquad
A_3=\{8\}.
\]

仅在 `y=9`：

\[
m_A(9)=1,
\qquad
\delta(9)=1.
\]

所以

\[
\boxed{
J_2(C)-J_2(A)=1.
}
\]

即候选层恰好凭空制造了一个跨 shell pair collision。

这把 P017 的 “candidate threshold 15 vs actual threshold 9” 从定性 precision lesson 提升为 P011 可计量的 collision-inflation 语言。

## 7. 归属边界

- P011/A1 拥有 collision polynomial 与 candidate-domain inflation；
- P023/A2 拥有 future-compatible quotient、actual-image label erasure 与 minimal repair；
- P017 只保留 square-basin sharp specialization。

因此本结果不是在 P023 复制一套碰撞理论，而是把 A2 暴露的 over-approximation 现象回灌到已有 P011 mother owner。

## 8. 可执行审计

- `src/enterprise_math/candidate_collision_inflation.py`
- `tests/test_p011_candidate_collision_inflation.py`

回归直接核对二阶闭式、全部小阶的非负虚增，以及 `k=14,root=9` 恰好一个假 pair collision。计算只作 regression；证明是上面的二项式恒等式。
