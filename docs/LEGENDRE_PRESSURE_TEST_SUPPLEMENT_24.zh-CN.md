# Legendre 压力测试 — 补充 24

状态：`PROVED RESEARCH NOTE`  
范围：least-prime 与 cofactor-root precision 之间的精确双任务调度  
依赖：P017 L064、P023-S12 directed repair geometry、P023-S14 conditional task scheduling  
纪律：本定理比较精确有限表示成本，不规定一个 universal factoring algorithm，也不证明 Legendre 猜想。

## 1. 为什么 L064 不能决定 first task

L064 证明了很强的 conditional asymmetry：

\[
\rho(P,R)\le2,
\]

而反向 factor `rho(R,P)` 可以大很多。

很容易因此猜测：应该永远先获取 least-prime precision，再获取 cofactor-root precision。

这个猜测是错的。

first task 自己也有 class-count cost。即使一个 task 的 reverse repair 很贵，只要它自己的 classes 更少，或它已经能决定另一个 task，它仍可能是更便宜的 first task。

## 2. 双任务 cost 的精确闭式

令

\[
N_P=|X/P|,
\qquad
N_R=|X/R|,
\]

并记

\[
\rho_{P\to R}=\rho(P,R),
\qquad
\rho_{R\to P}=\rho(R,P).
\]

对整数 base `B>=2`，定义

\[
L_B(n)=\min\{\ell:n\le B^\ell\}.
\]

P023-S14 给出两个 sequential costs：

\[
\boxed{
C_{P\to R}
=
L_B(N_P)+L_B(\rho_{P\to R}),
}
\]

以及

\[
\boxed{
C_{R\to P}
=
L_B(N_R)+L_B(\rho_{R\to P}).
}
\]

双任务问题的最优顺序，恰好就是这两个整数中较小者。

这是完整判据。

## 3. L065-A —— k=11 时 root first 严格最优

状态：`PROVED BY EXACT FINITE CLASSIFICATION`。

在 square basin

\[
(11^2,12^2)=(121,144)
\]

中，真实 composite-shell state 满足

\[
\boxed{N_P=5},
\qquad
\boxed{N_R=6},
\qquad
\boxed{|X/(P\cap R)|=6}.
\]

两个 directed repair factors 为

\[
\boxed{
\rho(P,R)=2,
\qquad
\rho(R,P)=1.
}
\]

第二个等式说明：在这个 basin 中，cofactor-root coordinate 已经唯一决定 least-prime shell。

在 base two 下，

\[
C_{P\to R}
=L_2(5)+L_2(2)
=3+1
=4,
\]

而

\[
C_{R\to P}
=L_2(6)+L_2(1)
=3+0
=3.
\]

最终 joint quotient 有 6 个 classes，所以绝对 lower bound 为

\[
L_2(6)=3.
\]

因此

\[
\boxed{
C_{R\to P}=3<4=C_{P\to R},
}
\]

root-first 不仅更好，而且恰好达到 zero scheduling slack 的最优下界。

## 4. L065-B —— k=1737 时 factor first 严格最优

状态：`PROVED BY EXACT FINITE CLASSIFICATION`。

在

\[
k=1737
\]

时，真实 composite-shell state 有

\[
\boxed{N_P=157},
\qquad
\boxed{N_R=109},
\qquad
\boxed{|X/(P\cap R)|=164}.
\]

由 L064，

\[
\boxed{
\rho(P,R)=2,
\qquad
\rho(R,P)=8.
}
\]

所以

\[
C_{P\to R}
=L_2(157)+L_2(2)
=8+1
=9,
\]

而

\[
C_{R\to P}
=L_2(109)+L_2(8)
=7+3
=10.
\]

于是

\[
\boxed{
C_{P\to R}=9<10=C_{R\to P},
}
\]

factor-first 在该 basin 严格最优。

最终 joint lower bound 为

\[
L_2(164)=8,
\]

所以即使更好的两阶段 schedule，仍然保留 1 bit sequential worst-case slack。

## 5. L065-C —— 不存在 universal 固定 factor/root 顺序

状态：`PROVED`，由 L065-A 与 L065-B 直接给出。

两个 strict witnesses 方向相反：

\[
\boxed{k=11:\quad R\to P\text{ 严格更优},}
\]

而

\[
\boxed{k=1737:\quad P\to R\text{ 严格更优}.}
\]

因此以下两个 global rules 都不成立：

\[
\text{“永远先 factor”}
\]

以及

\[
\text{“永远先 root”}.
\]

最优顺序依赖 basin。

## 6. 为什么 conditional asymmetry 还不够

L064 比较的只是第二步成本

\[
\rho(P,R)
\quad\text{与}\quad
\rho(R,P).
\]

S14 要求完整 schedule 还必须支付 first task 本身的 class cost。

所以真正应该比较的是

\[
\boxed{
L_B(N_P)+L_B(\rho(P,R))
\quad\text{与}\quad
L_B(N_R)+L_B(\rho(R,P)).
}
\]

而不是只比较两个 `rho`。

这给出一个严格数论实例：

\[
\boxed{
\text{conditional repair geometry}
\neq
\text{complete acquisition schedule}.
}
\]

## 7. k=11 witness 的结构解释

`k=11` 时 root-to-factor repair factor 等于 1，所以每个 realized root block 都包含在唯一 least-prime block 内：

\[
R\subseteq P.
\]

因此保留 `R` 已经自动保留全部 `P` 信息。先获取 `P` 会先为一个 5-class coordinate 付费，随后 `R` 再细化它；先获取 `R` 则一步直接到达 final joint quotient。

这正是 1 bit scheduling advantage 的精确机制。

## 8. k=1737 witness 的结构解释

`k=1737` 时，root precision 作为 first coordinate 的 raw class count 更小：

\[
109<157.
\]

但它在一个 root fiber 中隐藏了 8-way least-prime ambiguity。额外 3 个 binary repair symbols 超过了 first-task class depth 所节省的 1 bit。

因此一个看起来更 coarse 的 first coordinate，在把 worst local reconstruction burden 计入以后，可能反而更贵。

## 9. 对 number-theoretic proof design 的影响

若一个证明最终同时需要 least-prime shell identity 与 cofactor-root identity，则不存在 universal static ordering heuristic。

精确有限规则是：

1. 数当前 actual task classes；
2. 计算到另一个 coordinate 的 directed repair factor；
3. 比较两个 integer schedule costs；
4. 超过两个 tasks 时使用 S14 conditional scheduling，而不能把双任务偏好机械外推。

这是 proof-state optimization rule，不是关于物理时间或一般整数 factoring complexity 的主张。

## 10. 可执行规范

- `src/enterprise_math/p017_root_factor_schedule.py`
- `tests/test_p017_root_factor_schedule.py`

回归固定 `k=11` 与 `k=1737` 的精确 class counts、directed repair factors、schedule depths 与相反的最优方向。较小范围 sweep 还验证返回 preference 与整数 cost comparison 完全一致，并检查两个 schedules 都不突破 final joint-class lower bound。

## 11. 工具反哺

完整回路现在是

\[
\boxed{
\text{P018 two-basin transport}
\to
\text{P023 directed precision geometry}
\to
\text{P017 L064 asymmetry}
\to
\text{P023 conditional scheduling}
\to
\text{P017 L065 order reversal}.
}
\]

这已经不是把旧结果换一种术语表达：抽象工具直接暴露了新的 basin-dependent ordering theorem，并同时反驳两个自然的全局 heuristics。
