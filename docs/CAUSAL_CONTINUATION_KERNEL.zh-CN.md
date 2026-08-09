# Causal Continuation Kernel —— Coupled Fiber Composition 的最小充分 Witness 状态

状态：`CROSS-ROUTE RESEARCH WIP / EXACT FINITE THEOREM + EXECUTABLE REFERENCE`

归属：A3 relation quotient specialization；一般 future-safe equivalence 母理论仍归 A2/P023。

## 1. 问题

单层 coupling 可以用匿名 multiplicity

\[
\kappa(r)=\#\{\text{joint witnesses above coarse/marginal class }r\}
\]

完整描述当前 forgetting fiber 的大小。

但多步 composition 中，两个当前 witnesses 即使落在同一个 `r`，后续 continuation 也可能不同。因此：

- 只保存 `kappa(r)` 一般不充分；
- 保存完整 witness identity 又一般过度。

问题是：**最少还需要保存什么？**

## 2. CC-01 —— continuation type

固定从当前时刻以后真正允许的 future operation / observation language。

对当前 witness `w`，定义它的 continuation signature：

\[
\Sigma^+(w).
\]

定义：

\[
\boxed{
w\sim_+w'
\iff
\Sigma^+(w)=\Sigma^+(w').
}
\]

其等价类记为：

\[
\tau(w).
\]

`tau` 不是外加类型，而是剩余未来实际能否区分 witness 所产生的因果类。

## 3. CC-02 —— typed continuation kernel

若 `r(w)` 是当前 coarse/marginal class，定义：

\[
\boxed{
\kappa(r,\tau)
=
\#\{w:r(w)=r,\ \tau(w)=\tau\}.
}
\]

于是原匿名 kernel 只是：

\[
\boxed{
\kappa(r)=\sum_\tau\kappa(r,\tau).
}
\]

## 4. CC-03 —— witness identity 可删除

若两个 witnesses 具有相同 `(r,tau)`，它们对所有剩余未来完全等价。

因此精确 future composition 不需要保留 witness identity，只需保留该 class 的 multiplicity：

\[
\boxed{
\text{raw witnesses}
\to
\kappa(r,\tau)
}
\]

是 future-safe collapse。

这比“永远保留完整 incidence”更强：真正必要的是 continuation-type incidence，不是永久身份。

## 5. CC-04 —— typed kernel 的 composition law

设一个 continuation type `tau` 的单个 current witness 对下一阶段 target `z` 有：

\[
p(\tau,z)\in\mathbb N_0
\]

个 continuation witnesses。

则：

\[
\boxed{
N(r,z)
=
\sum_\tau
\kappa(r,\tau)p(\tau,z).
}
\]

这是直接 witness counting，不需要先验矩阵乘法。

传统 sum-product 只是在给 `(r,tau)` 和 `(tau,z)` 排坐标以后出现的 shadow。

## 6. CC-05 —— anonymous `kappa(r)` 的充分必要条件

若只想保存：

1. 当前 multiplicity `kappa(r)`；
2. 每个 `r` 一个 induced future profile；

那么这是 exact 的当且仅当：

\[
\boxed{
\#\{\tau:\kappa(r,\tau)>0\}=1
\quad\forall r.
}
\]

也就是：同一 coarse fiber 内所有 witnesses 已属于同一个 continuation-signature class。

此时令唯一 type 为 `tau_r`，则：

\[
\boxed{
N(r,z)=\kappa(r)p(\tau_r,z).
}
\]

注意 `p(tau_r,z)` 只保存一次，不能把相同 profile 再按 fiber size 聚合一次，否则会重复计数。

## 7. CC-06 —— anonymous multiplicity 不足的最小反例

两个系统都只有：

\[
\kappa(r)=2.
\]

系统 A：

\[
\kappa(r,\tau_a)=2.
\]

系统 B：

\[
\kappa(r,\tau_a)=1,
\qquad
\kappa(r,\tau_b)=1.
\]

若：

\[
p(\tau_a,z_0)=1,
\qquad
p(\tau_b,z_1)=1,
\]

则 A 的下一未来是：

\[
N_A(r,z_0)=2,
\]

而 B 是：

\[
N_B(r,z_0)=1,
\qquad
N_B(r,z_1)=1.
\]

因此相同 `kappa(r)` 不能恢复未来。

## 8. CC-07 —— 完整 identity 也不是必要量

四个 raw witnesses：

\[
w_1,w_2,w_3,w_4
\]

若：

\[
\tau(w_1)=\tau(w_2)=\tau_a,
\]

\[
\tau(w_3)=\tau(w_4)=\tau_b,
\]

则完整 future state 只需：

\[
\boxed{
\kappa(r,\tau_a)=2,
\qquad
\kappa(r,\tau_b)=2.
}
\]

所以最小因果层严格位于：

\[
\boxed{
\text{anonymous multiplicity}
\;<\;
\text{continuation-type multiplicity}
\;<\;
\text{raw witness identity}
}
\]

这里 `<` 表示一般情况下的信息细度，而不是数值大小。

## 9. 与 P021 / P023 的关系

P021 的 witness necessity 应细化为：

> 若未来仍能区分两个 witnesses，则不可合并；若未来已无法区分，则其身份可以删除，只保留 class multiplicity。

P023 的 future-safe quotient 给出 mother criterion；本文件给出 coupled-fiber counting specialization。

因此 `kappa(r,tau)` 是 future-equivalence quotient 在 coupling/fiber 场景中的整数 counting realization。

## 10. 与 matrix / convolution 的关系

若 `tau` 是 exact intermediate continuation signature，composition counting：

\[
N(r,z)=\sum_\tau \kappa(r,\tau)p(\tau,z)
\]

产生传统 matrix multiplication shadow。

若提前把不同 `tau` 合并，只因为它们当前 `r` 相同，则可能产生 false cross pairing。

所以矩阵合法的中间 index 不是任意 coarse label，而必须是对后续 future-sufficient 的 continuation type。

## 11. 最小充分状态候选

对有限 coupled fiber 与固定 future language：

\[
\boxed{
\text{minimal exact counting state}
=
\{\kappa(r,\tau)\}_{r,\tau},
}
\]

其中 `tau` 已经是最大程度的 future-safe witness quotient。

若还要保存非 counting observation，则 `tau` 自身必须按完整 future signature 定义，而不能只按一步 continuation count 定义。

## 12. 当前边界

本结论是有限 deterministic / finite-multiplicity causal setting 的 exact result。

尚未自动推广到：

- infinite fibers；
- continuous measure；
- quantum amplitudes；
- nondeterministic semantics 中非 counting 权重；
- 未声明 future language 的 universal ontology。

## 13. 可执行资产

- `src/enterprise_math/causal_continuation_kernel.py`
- `tests/test_causal_continuation_kernel.py`

## 14. 下一步

1. 证明 multi-stage continuation type 可由有限 future partition refinement 自动求得；
2. 把 `kappa(r,tau)` 与 A4 missing interpolation witness 合并成统一 incidence language；
3. 研究 dimension contraction 是否能把 deleted internal relation 直接解释成 continuation-type fiber；
4. 推导当 `tau` 自身可 LEGO-factor 时更低阶的递归压缩律。
