# P025 补充 82 —— 四次幂反压力与分圆深度边界

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 72、79–81  
硬阻断：`NONE`

## 1. 下一次压力测试就是指数四

Stage 79 对奇素数指数证明了一个很强的结论：threshold-one activation 必然强迫唯一 nonlinear cyclotomic factor 中出现重复素因子。

很自然会想把这条结论推广到所有指数。指数四直接否定了这种推广。

失效原因并不只是奇偶性。真正决定性的对象是：**给定 sign 下的 cyclotomic factorization depth**。

## 2. 同指数四次幂 projective atoms

设

\[
3\le q<p
\]

为不同奇素数。complements 为

\[
p^4,\ q^4
\]

时，精确 equal-exponent projective denominator 为

\[
4(p+q).
\]

因此

\[
\boxed{
\rho_{4,+}=\frac{m(p^4+q^4)}{4(p+q)},
\qquad
\rho_{4,-}=\frac{m(p^4-q^4)}{4(p+q)}.
}
\]

引入 centered coordinates

\[
A=\frac{p-q}{2},
\qquad
B=\frac{p+q}{2}.
\]

则

\[
\gcd(A,B)=1,
\]

且 `A,B` 奇偶相反。

## 3. 两个 sign 的 cyclotomic depth 不同

sum branch 为

\[
\boxed{p^4+q^4=\Phi_8(p,q).}
\]

对这个 sign 而言只有一个 cyclotomic layer。

difference branch 则为

\[
\boxed{
p^4-q^4
=\Phi_1(p,q)\Phi_2(p,q)\Phi_4(p,q)
=(p-q)(p+q)(p^2+q^2).
}
\]

所以 difference branch 有**三层**：两个 linear layers 加一个 top quadratic layer。

这正是 Stage 79 top-factor forcing 第一次可能失效的位置。

## 4. P025-T169 —— 精确 centered difference 公式

令

\[
Q=A^2+B^2.
\]

则

\[
p^2+q^2=2Q
\]

并且

\[
p^4-q^4=8ABQ.
\]

由于 `A,B` 互素且奇偶相反，

\[
Q\text{ 为奇数},
\]

并且

\[
\gcd(A,Q)=\gcd(B,Q)=1.
\]

因此

\[
\boxed{m(p^4-q^4)=8m(A)m(B)m(Q).}
\]

又因为

\[
4(p+q)=8B,
\]

得到 exact atom

\[
\boxed{
\rho_{4,-}=\frac{m(A)m(Q)}{\operatorname{rad}(B)}.
}
\]

top homogeneous cyclotomic factor 为

\[
\Phi_4(p,q)=p^2+q^2=2Q,
\]

其 multiplicity residual 恰为 `m(Q)`。

所以如果 `Phi_4` squarefree，

\[
\boxed{
\rho_{4,-}=\frac{m(A)}{\operatorname{rad}(B)},
}
\]

这正好退化成 prime-square difference shell 已经出现过的 centered carrier。

因此指数四可以直接继承 lower-layer centered-radius pressure，而无需任何 repeated top cyclotomic prime。

## 5. P025-C24 —— 四次幂 difference activation 不要求 top repetition

取

\[
(q,p)=(23,41).
\]

则

\[
A=9,
\qquad
B=32,
\qquad
Q=9^2+32^2=1105=5\cdot13\cdot17.
\]

因此

\[
\Phi_4(41,23)
=41^2+23^2
=2210
=2\cdot5\cdot13\cdot17
\]

完全 squarefree。

但

\[
m(A)=3,
\qquad
m(Q)=1,
\qquad
\operatorname{rad}(B)=2,
\]

于是

\[
\boxed{
\rho_{4,-}=\frac32>1.
}
\]

所以自然推广

\[
\text{activation}
\Longrightarrow
\text{top nonlinear cyclotomic factor 必有重复}
\]

在指数四下明确为假。

这是一个 hard negative boundary，而不是“证明还没找到”。

## 6. P025-T170 —— 四次幂 sum 仍保留 top forcing

sum branch 的行为不同。在 centered coordinates 中，

\[
p^4+q^4=2H,
\]

其中

\[
\boxed{H=B^4+6A^2B^2+A^4.}
\]

由于 `A,B` 奇偶相反，`H` 为奇数。因此

\[
m(p^4+q^4)=m(H)
\]

并有

\[
\boxed{
\rho_{4,+}=\frac{m(H)}{8B}.
}
\]

若 `H` squarefree，则 `m(H)=1`，从而

\[
\rho_{4,+}<1.
\]

所以

\[
\boxed{
\rho_{4,+}\ge1
\Longrightarrow
H\text{ nonsquarefree}.
}
\]

换言之，四次幂 **sum** activation 仍然强迫唯一 top factor `Phi_8` 中出现重复。

## 7. P025-T171 —— repeated fourth-power sum primes 必为 `1 mod 8`

若奇素数 `r` 在 `H` 中重复，即

\[
r^2\mid p^4+q^4,
\]

因为 `r` 与 `pq` 互素，ratio

\[
x=pq^{-1}\pmod r
\]

满足

\[
x^4\equiv-1\pmod r.
\]

所以 `x` 的精确阶为 8，进而

\[
8\mid r-1.
\]

因此

\[
\boxed{r\equiv1\pmod8.}
\]

对奇 `p,q`，`p^4+q^4` 中素数 2 的 valuation 恰为 1，所以它不会贡献 residual。

一个精确 activated example 是

\[
(q,p)=(839,1277),
\]

其中

\[
p^4+q^4
=2\cdot17401\cdot9521^2,
\]

且

\[
\boxed{
\rho_{4,+}=\frac{9521}{8464}>1.
}
\]

repeated prime 满足

\[
9521\equiv1\pmod8.
\]

## 8. 真正边界是 cyclotomic factorization depth

标准 homogeneous factorization 为

\[
p^n-q^n=\prod_{d\mid n}\Phi_d(p,q),
\]

以及

\[
p^n+q^n
=\prod_{\substack{d\mid2n\\d\nmid n}}\Phi_d(p,q).
\]

对奇素数指数 `ell`：

- difference indices 只有 `{1,ell}`；
- sum indices 只有 `{2,2ell}`。

所以只有一个 linear layer 加一个 nonlinear layer，而 Stage 79 已证明 linear layer 单独无法激活。

对指数四：

- sum indices 只有 `{8}`；
- difference indices 为 `{1,2,4}`。

于是 sum 仍保留 top forcing；difference 却因为增加了足够多的 lower layers，可以在 top squarefree 时依然承载 pressure。

所以正确的组织原则是

\[
\boxed{
\text{sign-specific cyclotomic divisor depth},
}
\]

而不是单纯奇偶性。

## 9. 架构后果

Stage 72 已证明 exponent-only precision 会饱和。Stage 79 进一步证明，对 prime exponent 可以换到单个 top cyclotomic congruence coordinate。

Stage 82 又证明：对 composite exponent，这仍然可能太粗。下一层 state object 必须能够回答：

> projective multiplicity pressure 究竟由哪一个 cyclotomic layer，或哪些 layers 的组合承载？

因此下一候选不应再是单个 top-factor state，而应是 **cyclotomic divisor-lattice carrier state**。

在指数四 difference 中，即使 `Phi_4` squarefree，carrier 仍可以完全落在 lower `Phi_1/Phi_2` geometry。

## 10. Prior-art / novelty 边界

cyclotomic factorization、centered fourth-power identities、multiplicative orders，以及 primitive eighth-order support 的 `r=1 mod 8` 都是经典数学。

P025 不单独主张这些组成部分的新颖性。

项目侧结果是：top-factor forcing 的 exact projective counterexample、同一指数下 sign-dependent contrast，以及由此确定的 precision-routing boundary。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/abc_fourth_power_cyclotomic_boundary.py`；
- `tests/test_abc_fourth_power_cyclotomic_boundary.py`。

executable layer 验证：

- centered factorization 与 pairwise gcd structure；
- exact difference formula `rho_4,-=m(A)m(A^2+B^2)/rad(B)`；
- squarefree-top 但 activated 的显式反例 `(23,41)`；
- sum-side top forcing；
- repeated sum support 的 exact order eight。

## 12. 下一前沿

不存在硬阻断。继续：

1. 对任意 exponent `n` 定义 sign-specific cyclotomic index set；
2. 构造 divisor-lattice carrier state，按 cyclotomic layer 记录 residual pressure，同时不假装不同 layer values 总是互素；
3. 给出“某个 upper set of layers 何时被强迫承载 repetition”的 exact criterion；
4. 用指数九 `Phi_1 Phi_3 Phi_9` 做第一个 odd-composite counter-pressure；
5. 只有 divisor-lattice semantics 经受这些测试后，才把抽象回流 A2/P023。
