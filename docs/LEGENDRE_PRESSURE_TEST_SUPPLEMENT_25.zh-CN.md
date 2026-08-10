# Legendre 压力测试 — 补充 25

状态：`PROVED RESEARCH NOTE`  
范围：factor-first 获取 root/factor precision 的 universal one-symbol near-optimality  
依赖：P017 L064–L065 与 P023-S16 bounded-repair scheduling approximation  
纪律：这是有限 representation-cost theorem，不是整数 factorization complexity theorem，也不证明 Legendre 猜想。

## 1. L065 否掉 universal exact optimality，但留下了更强的鲁棒问题

L065 已证明 factor-first 与 root-first 都不可能在所有 square basins 上精确最优。

但 L064 同时给出一个 universal structural bound：

\[
\boxed{
\rho(P,R)\le2.
}
\]

因此更正确的问题不是“factor-first 是否永远最优”，而是：

> 即使 factor-first 不是 exact optimum，它最多会差多少？

答案是统一一个 binary symbol。

## 2. L066-A —— Factor-first 永远距离 final lower bound 至多一个 bit

状态：`PROVED`。

记

\[
N_P=|X/P|,
\qquad
N_*=|X/(P\cap R)|.
\]

factor-first binary depth 为

\[
C_{P\to R}
=L_2(N_P)+L_2(\rho(P,R)).
\]

因为 joint precision 细化 factor partition，

\[
N_P\le N_*.
\]

而 L064 给出

\[
L_2(\rho(P,R))\le1.
\]

因此

\[
\boxed{
C_{P\to R}
\le
L_2(N_*)+1.
}
\]

所以 factor-first 对任意 square basin 都最多只比 absolute joint-class cardinality lower bound 多一个 bit。

## 3. L066-B —— Factor-first 永远是 optimum 的 one-bit approximation

状态：`PROVED`。

令

\[
C_{\rm opt}
=
\min(C_{P\to R},C_{R\to P}).
\]

任何 exact schedule 都必须满足

\[
C_{\rm opt}\ge L_2(N_*).
\]

结合 L066-A，得到

\[
\boxed{
C_{P\to R}-C_{\rm opt}
\le1.
}
\]

因此 factor-first strategy 是所有 square basins 上对最优 two-task precision schedule 的严格 additive-one approximation。

这比 heuristic recommendation 更强，因为 approximation gap 本身已经被证明。

## 4. L066-C —— 任何严格 root-first advantage 都恰好只有 1 bit

状态：`PROVED`。

若 root-first 严格更优：

\[
C_{R\to P}<C_{P\to R},
\]

两个 costs 都是整数。L066-A 给出

\[
C_{P\to R}\le L_2(N_*)+1,
\]

而任意 exact schedule 都满足

\[
C_{R\to P}\ge L_2(N_*).
\]

严格不等式只留下一个可能：

\[
\boxed{
C_{R\to P}=L_2(N_*),
\qquad
C_{P\to R}=L_2(N_*)+1.
}
\]

所以 root-first 即使胜出，也绝不可能比 factor-first 多省超过一个 binary symbol。

L065 的 `k=11` witness 正好实现这个 equality case。

## 5. L066-D —— Base-B 版本

状态：`PROVED`。

因为对任意整数 base `B>=2` 都有

\[
2\le B,
\]

L064 同样推出

\[
L_B(\rho(P,R))\le1.
\]

所以

\[
\boxed{
C^{(B)}_{P\to R}
\le
L_B(N_*)+1
}
\]

在所有 base `B>=2` 上都成立。

因此 robust approximation theorem 并不依赖 binary；binary 只是最小 alphabet 下最 sharp 的实例。

## 6. 与 L065 两个反向 witnesses 的关系

`k=11` 时，

\[
C_{R\to P}=3,
\qquad
C_{P\to R}=4,
\qquad
L_2(N_*)=3.
\]

root-first 达到 lower bound，而 factor-first 恰好多 1 bit。

`k=1737` 时，

\[
C_{P\to R}=9,
\qquad
C_{R\to P}=10,
\qquad
L_2(N_*)=8.
\]

这里 factor-first 胜出，但它相对于 raw final-class lower bound 仍保留 1 bit stagewise worst-case slack。

所以两个例子共同说明：

\[
\boxed{
\text{没有 universal exact optimum}
\quad\text{但存在 universal factor-first additive-one guarantee}.
}
\]

## 7. 为什么这是更强的 research-tool outcome

一种常见错误是：一旦 universal optimality 出现 counterexample，就把所有结构性指导一起放弃。

L066 给出更好的处理方式：

1. 保留 counterexample——exact optimality 确实是假的；
2. 找出 directed structural bound——`rho(P,R)<=2`；
3. 把它转成 certified approximation theorem；
4. 只有 downstream proof 真正在乎那 1 bit 时，才需要 instance-wise exact scheduling。

这样可以严格区分 theorem-backed near-optimality 与脆弱的 universal heuristic。

## 8. 对 P017 proof architecture 的影响

若后续 P017 recursion 同时需要 least-prime shell 与 cofactor-root coordinates，则 factor-first 可以作为 robust default，精确含义是：

\[
\boxed{
\text{其 binary acquisition depth 至多为 optimum}+1.
}
\]

因此可以在 proof architecture 中默认采用 factor-first，而无需声称它对每个 basin 都 exact optimal。

若某一步精确节省 1 bit 会改变证明阈值，再调用 L065/S14 做 instance-wise root-first 选择。

## 9. 可执行审计

`tests/test_p017_root_factor_schedule.py` 固定两个方向相反的 optimum witnesses，并在 bounded range 检查两个 schedule costs 都不会突破 final joint-class lower bound。

后续 regression 还可以加入 bounded version

\[
C_{P\to R}\le L_2(N_*)+1
\]

作为 implementation guard；定理本身直接来自 L064，不依赖 bounded enumeration。

## 10. 工具反哺

这就是 P023-S16 在 P017 中的特化：

\[
\boxed{
\text{bounded directed repair}
\Longrightarrow
\text{certified additive scheduling approximation}.
}
\]

又一次完成了抽象闭环：数论 two-basin transport 先产生 general precision bound，再返回成为稳定的数论 scheduling guarantee。
