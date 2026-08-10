# P025 补充 107 —— Quadratic Rank Observable Boundary

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-nonlinear-observable-stage107`  
依赖：P025 补充 97、106  
硬阻断：`NONE`

## 1. 为什么要换 observable

Stages101–106 已在线性 activation-area observable 上建立 state / operation precision split。特别是 endpoint semantics -> full trace semantics 可以只细化 operation-word quotient，而不细化 compact state generator。

Stage107 改问：如果真正增强的是 **observable 自身**，这个结论还成立吗？

保留完全相同的 ordered threshold incidence geometry，只把 activation area 换成 nonlinear column-rank energy

\[
\boxed{E:=\sum_j r_j^2,}
\]

其中

\[
r_j:=\#\{k:\rho_j\ge T_k\}.
\]

## 2. Area 与 quadratic energy

线性 area 为

\[
A=\sum_j r_j.
\]

它只保留 column-rank distribution 的 first moment。

quadratic energy 为

\[
E=\sum_jr_j^2,
\]

它会感知相同总 rank mass 是否集中在少数 columns 上。

因此 equal area 一般并不能推出 equal energy。

## 3. P025-CE42 —— exact arithmetic observable collision

固定同一 threshold grid

\[
T=\left(\frac12,1\right),
\]

并复用 Stage97 area collision 中的两条 exact P025 dyadic pressure states。

### Flat orbit

`(q,p,m)=(3,5,2)` 在 exponents `2,4` 上 pressure values 为

\[
\left(\frac12,\frac12\right).
\]

所以 column ranks 为

\[
\boxed{(1,1)},
\]

并且

\[
A=2,
\qquad
E=1^2+1^2=2.
\]

### Jump orbit

`(q,p,m)=(7,17,2)` 的 pressure values 为

\[
\left(\frac16,\frac{13}{6}\right).
\]

所以 column ranks 为

\[
\boxed{(0,2)},
\]

并且

\[
A=2,
\qquad
E=0^2+2^2=4.
\]

因此

\[
\boxed{
A_{\rm flat}=A_{\rm jump}=2,
\qquad
E_{\rm flat}=2\ne4=E_{\rm jump}.
}
\]

## 4. P025-T245 —— 对 area sufficient 的 state 可以对更强 observable 失效

两个 states 被 scalar area coordinate 合并，但 quadratic-energy future 能区分它们。

因此任何只保留 area distinction 的 quotient，都不足以回答要求 `E` 的 future language。

特别地，

\[
\boxed{
\text{observable refinement can force state refinement}.
}
\]

这与 Stage106 恰好互补：Stage106 的 endpoint -> trace language refinement 并没有强迫 state refinement。

## 5. future refinement 的两条独立轴

Stages106–107 暴露出两个逻辑独立机制。

### Operation-semantic refinement

endpoint area -> full area trace：

- compact state generator 可保持不变；
- operation-word quotient 必须变细。

### Observable refinement

area -> quadratic rank energy：

- operation language 可以保持不变；
- state quotient 必须变细，因为 equal-area states 可以有不同 energy。

所以不注明 future 到底在哪个方向变强时，

> richer future means finer state

这句话是错误的。

## 6. 架构后果

future-compatible precision architecture 至少应把三种 declared objects 分开：

1. **state observable family** —— 当前/未来 state 的哪些函数必须可预测；
2. **operation language** —— 允许哪些 actions/words；
3. **observation semantics** —— 只看 endpoint，还是包含 intermediate trace。

不同声明被增强时，precision 可以被迫落到不同组件上。

## 7. Prior-art / novelty 边界

moments、quadratic energies 以及 equal first moment 不决定 second moment 都是 elementary prior mathematics。P025 不单独主张这些事实新颖。

项目侧结果是 exact arithmetic pressure-test collision：observable refinement 与 trace refinement 会作用于不同 precision components。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 8. 可执行资产

新增：

- `src/enterprise_math/abc_quadratic_rank_energy.py`；
- `tests/test_abc_quadratic_rank_energy.py`。

## 9. 下一前沿

Stage108 将计算 `E` 对 finite actions 的 exact response polynomial。核心压力测试是：Stage102 的 second-order history closure 是否能跨 observable 保留，还是 nonlinear observable 会产生真正的 third-order action interaction。