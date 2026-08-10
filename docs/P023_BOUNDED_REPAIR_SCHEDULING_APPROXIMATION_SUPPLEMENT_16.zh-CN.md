# P023 —— 有界 repair 的调度近似定理，补充 16

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023  
依赖：P023-S12 directed repair depth 与 P023-S14 conditional scheduling  
纪律：这是初等整数 coding bound。本补充的项目作用，是把 directed repair 的结构上界转化成 finite task acquisition 的严格 additive guarantee。

## 1. 双任务设置

令 `E,F` 是同一个有限状态集 `X` 上的两个 finite precision tasks。

记

\[
N_E=|X/E|,
\qquad
N_F=|X/F|,
\qquad
N_*=|X/(E\cap F)|.
\]

固定整数 alphabet base `B>=2`，并定义

\[
L_B(n)=\min\{\ell:n\le B^\ell\}.
\]

两个精确顺序的 costs 为

\[
C_{E\to F}=L_B(N_E)+L_B(\rho(E,F)),
\]

以及

\[
C_{F\to E}=L_B(N_F)+L_B(\rho(F,E)).
\]

final joint-state cardinality lower bound 为

\[
D_*=L_B(N_*).
\]

## 2. P023-S16-T01 —— 有界 directed repair 给出 additive schedule guarantee

状态：`PROVED`。

若对整数 `c>=0` 有

\[
\boxed{
\rho(E,F)\le B^c,
}
\]

则

\[
\boxed{
C_{E\to F}
\le
D_*+c.
}
\]

### 证明

joint quotient 细化 `E`，所以

\[
N_E\le N_*.
\]

因此

\[
L_B(N_E)\le L_B(N_*)=D_*.
\]

repair 假设又给出

\[
L_B(\rho(E,F))\le c.
\]

两式相加即得。∎

所以一个小 directed repair factor 不只是局部性质；它会直接给对应 two-task schedule 一个全局 additive approximation guarantee。

## 3. P023-S16-T02 —— 反向顺序即使更优，优势也至多为 c

状态：`PROVED`。

令

\[
C_{\min}=\min(C_{E\to F},C_{F\to E}).
\]

任何 exact schedule 至少必须能够编号所有 final joint classes，因此

\[
C_{\min}\ge D_*.
\]

结合 T01 得到

\[
\boxed{
C_{E\to F}-C_{\min}
\le c.
}
\]

所以即使 `F -> E` 才是精确最优，选择 `E -> F` 最多损失 `c` 个 base-`B` symbols。

## 4. P023-S16-T03 —— one-symbol 情形具有刚性

状态：`PROVED`。

若

\[
\rho(E,F)\le B,
\]

则

\[
C_{E\to F}\le D_*+1.
\]

若反向顺序还严格更便宜，因为 costs 都是整数，只可能有

\[
\boxed{
C_{F\to E}=D_*,
\qquad
C_{E\to F}=D_*+1.
}
\]

因此严格的 reverse-order advantage **恰好只能是一个 symbol**，不可能更多。

这说明即使 exact optimal order 会随实例变化，bounded directed repair 仍然给出很强的鲁棒性。

## 5. P023-S16-T04 —— Multi-task prefix 版本

状态：`PROVED`。

考虑一个顺序

\[
E_{\sigma(1)},\ldots,E_{\sigma(m)}
\]

以及 S14 的 stage repair factors `rho_j`。若第一步之后每个 stage 都满足

\[
\rho_j\le B^{c_j},
\]

令 `N_*` 为 final joint class count。first task 的 classes 数不会超过 `N_*`，所以

\[
L_B(|X/E_{\sigma(1)}|)\le L_B(N_*).
\]

因此

\[
\boxed{
C_B(\sigma)
\le
L_B(N_*)+
\sum_{j=2}^m c_j.
}
\]

所以只要能找到 later conditional repairs 都有小结构上界的 schedule，它就自动接近 final cardinality lower bound，而且这个结论与 raw state space 多大无关。

这给出一个有用的 proof heuristic：优先寻找 later conditional repair factors 可被结构控制的 order。

## 6. 与 dependency closure 的关系

若 later task 已经落入 S15 dependency closure，则它的 repair factor 为 1，因此可以取

\[
c_j=0.
\]

所以 S15 与 S16 是互补的：

- closure 删除 conditional repair depth 恰好为 0 的 tasks；
- bounded-repair approximation 控制剩余 nonzero transitions。

## 7. 数论反哺：P017

P017 L064 已证明

\[
\rho(P,R)\le2.
\]

取 base `B=2`，即 `c=1`。因此 factor-first 获取 least-prime + cofactor-root precision 的成本，对任意 basin 都距离 final joint-class lower bound 至多一个 binary symbol。

P017 补充 25 将这一点写成 L066，并进一步得到：任何严格 root-first advantage 都必然恰好只有 1 bit。

## 8. 研究工具规则

当 exact task-order optimization 本身较贵时：

1. 先选一个 candidate first task `E`；
2. 证明 `rho(E,F)` 或 later conditional repairs 的结构上界；
3. 用 S16 把这些上界变成 additive integer guarantee；
4. 只有当剩余 slack 对 theorem 真正重要时，再运行 exact DP；
5. 不要把 certified near-optimality 偷换成未证明的 exact optimality。

这把**严格近似保证**与 heuristic preference 清楚分开。

## 9. 前人工作与新颖性纪律

这里的不等式属于初等 coding arithmetic；由 bounded branching 推导 approximation guarantee 也不主张为新数学。

项目新增价值在于：这里的 branching factor 不是猜测或外部设定，而是由声明 precision tasks 精确生成的 P023 conditional repair multiplicity。
