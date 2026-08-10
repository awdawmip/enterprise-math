# P025 补充 62 —— Pair-Radical 压缩与 de Bruijn 前人工作上界

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 47、50、60、61  
Hard block：`NONE`

## 1. Stage 61 把非 unit PCC failure 压成一个 pair product

固定 `eta in (0,1)`。Stage 61 证明，每个非 unit `PCC_eta` failure 都存在两个不同 components `x,y` 满足

\[
\boxed{m(x)m(y)\ge\frac12c^{1+\eta}.}
\]

由于 primitive abc 的三个 components 两两互素，

\[
\operatorname{rad}(xy)
=\operatorname{rad}(x)\operatorname{rad}(y)
=\frac{xy}{m(x)m(y)}.
\]

在 dyadic 区间

\[
X/2<c\le X
\]

内有 `xy<=X^2`，故

\[
\boxed{\operatorname{rad}(xy)\ll_\eta X^{1-\eta}.}
\]

因此双 component failure state 可以再次压缩成单一整数

\[
\boxed{n=xy\le X^2}
\]

及其 small-radical 条件。

这一压缩是项目内的精确算术；下面使用的计数定理属于经典前人工作。

## 2. 外部 de Bruijn 输入

当前 abc exceptional-set 文献明确记录经典 de Bruijn 估计

\[
\#\{n\le x:\operatorname{rad}(n)\le x^\lambda\}
=O_\varepsilon(x^{\lambda+\varepsilon})
\]

[SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2026-ABC-EXCEPTIONAL-CURRENT]。Lichtman 的说明文也记录了由此得到的经典 almost-all abc 结论 [SRC-LICHTMAN-2025-ABC-ALMOST-ALWAYS]。

P025 只把这些结果作为 prior art 使用，不主张任何新的 radical-counting theorem。

## 3. P025-T129 —— de Bruijn 将 PCC-specific failure 指数进一步降为 `1-eta`

对 pair product

\[
n=xy\le X^2
\]

应用 de Bruijn。Stage-61 给出的 radical 尺度为

\[
\operatorname{rad}(n)\ll X^{1-\eta}
=(X^2)^{(1-\eta)/2}.
\]

因此在允许任意 `+epsilon` 损失后，pair product 的数量为

\[
O_{\eta,\varepsilon}(X^{1-\eta+\varepsilon}).
\]

每个 product 的 factor pair 数由标准 divisor bound 再贡献 `X^epsilon`，而第三个 additive component 随后被确定。于是

\[
\boxed{
N^{\rm nonunit}_{\rm PCC-fail}(X)
=O_{\eta,\varepsilon}(X^{1-\eta+\varepsilon}).
}
\]

对于 unit triple，Stage 50 已经强迫一个非 unit component `n<=X` 满足

\[
m(n)\ge c^\eta,
\]

所以在 dyadic 区间同样有

\[
\operatorname{rad}(n)\ll_\eta X^{1-\eta}.
\]

此时只有一个变量，de Bruijn 直接给出相同数量级。故总体

\[
\boxed{
N_{\rm PCC-fail}(c\le X)
=O_{\eta,\varepsilon}(X^{1-\eta+\varepsilon}).
}
\]

这是“项目特有 paired-state reduction + 外部经典计数定理”的组合结果。

## 4. 对 Stage-60 Oesterlé benchmark 的影响

Stage 60 证明：固定 `M>1` 后，只要

\[
0<\eta<1-1/M,
\]

所有充分大的

\[
c\ge\operatorname{rad}(abc)^M
\]

failure 必然也是 `PCC_eta` failure。

把 `eta` 取到边界任意近，P025-via-PCC 路线可得到内部 benchmark

\[
\boxed{
N_M(X)=O_{M,\varepsilon}(X^{1/M+\varepsilon}).
}
\]

这比 Stage 60 的纯初等 exponent 强很多，但依然没有达到经典直接 radical 路线。

## 5. P025-NB12 —— 经典 de Bruijn global-radical selector 严格支配该 Oesterlé 路线

Oesterlé-M failure 本身已经给出

\[
R=\operatorname{rad}(abc)\le X^{1/M}.
\]

由于 `a,b,c` 两两互素，三个 pair-radical products 中至少一个不超过

\[
R^{2/3}\le X^{2/(3M)}.
\]

经典 de Bruijn 论证于是直接得到

\[
\boxed{
N_M(X)=O_{M,\varepsilon}(X^{2/(3M)+\varepsilon}),
}
\]

这正是当前 exceptional-set 文献记录的标准 pair-radical-selector bound [SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2026-ABC-EXCEPTIONAL-CURRENT]。

由于

\[
\frac{2}{3M}<\frac1M,
\]

对每个 `M>1`，经典直接路线都严格优于 P025-via-PCC exceptional exponent。

因此形成一个明确的**负向路由结果**：

> 除非出现真正能够击穿经典 pair-radical selector 的新输入，否则不应继续把 P025 的 Stage-50/60 精力用在“竞争普通 abc exceptional exponent”上。

## 6. prior-art 撞线之后仍然保留的项目价值

P025 仍得到一个不同对象：

\[
\text{PCC failure}
\to
\text{paired residual state}
\to
\text{pair-product radical state}.
\]

PCC failure set 本身并不等于经典 abc exceptional set。P025-T129 是关于项目自定义 finite-precision observable 的无条件稀疏定理。

更重要的架构意义是：同一个 failure certificate 可以逐级压缩为

1. 一个失败的 cyclic weighted-radical coordinate；
2. 两个 residual components；
3. 一个 pair product；
4. 一个 pair radical；
5. 最后把外部计数定理作用在该 coarse state 上。

但对于普通 Oesterlé exceptional counting，原始 global radical 反而拥有更粗、更强的 selector，因此 projective 绕行对这个 future task 丢掉了有价值的信息。

这正是一个 P023 型 task-relative quotient 边界：一种表示在一个 future language 中很有价值，在另一个 future language 中却可能严格劣于另一种表示。

## 7. Prior-art discipline

De Bruijn radical-counting 及其 abc exceptional-set 推论全部属于外部前人数学；当前文献还拥有远强于该经典 bound 的结果。P025 不做这些结果的优先权主张 [SRC-LICHTMAN-2025-ABC-ALMOST-ALWAYS; SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2026-ABC-EXCEPTIONAL-CURRENT]。

P025-T129 只是外部 theorem 与 Stage-61 project-specific paired compression 的组合，其历史 novelty 仍是 `NOVELTY_UNVERIFIED`，不得宣传为有竞争力的解析数论结果。

## 8. 可执行资产

新增：

- `src/enterprise_math/abc_projective_debruijn_bridge.py`；
- `tests/test_abc_projective_debruijn_bridge.py`；
- `sources_p025_paired_tail.json`。

可执行层只保存 exact finite reductions 与有理 exponent 比较，不实现、也不重新证明外部渐近 radical-counting theorem。

## 9. 下一前沿

Hard block 不存在。继续：

1. 若没有能超过 classical pair-radical selector 的新输入，停止优化 Stage-60 普通 abc exceptional exponent；
2. 把 PCC failure 作为自身的 finite-precision exceptional language 研究，此时 P025-T129 仍有意义；
3. 比较 explicit weighted-radical projective state 与现代 exceptional-set work 的 anatomic radical decomposition；
4. 将这个负路由结果回流 A2/P023：task-relative coarse state 会改变“哪一种表示最省信息”的排序。
