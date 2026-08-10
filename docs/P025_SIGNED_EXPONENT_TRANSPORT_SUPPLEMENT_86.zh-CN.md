# P025 补充 86 —— Signed Exponent Transport 与 Dyadic Non-Attenuation

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 84–85  
硬阻断：`NONE`

## 1. 两张 sign graph 实际相连

Stage 85 分别研究 sum 与 difference 的 same-sign pressure transport。缺失的 cover edge 正是 exponent 乘以 2。

对奇素数 bases `p>q`，定义

\[
D_m:=p^m-q^m,
\qquad
S_m:=p^m+q^m.
\]

则

\[
\boxed{D_{2m}=D_mS_m.}
\]

所以自然存在 cross-sign cover

\[
\boxed{(m,+)\longrightarrow(2m,-).}
\]

同时 `(m,-)->(2m,-)` 仍是普通 difference cover。

## 2. P025-T180 —— 两个 lower components 的重叠恰为 2

由于 `p,q` 都是奇数，

\[
D_m,S_m\text{ 都是偶数}.
\]

任一公共因子同时整除

\[
S_m-D_m=2q^m
\]

以及

\[
S_m+D_m=2p^m.
\]

因为 `p,q` 为不同素数，

\[
\boxed{\gcd(D_m,S_m)=2.}
\]

因此任意 exponent `m` 上，这两个 blocks 之间的 overlap correction 恒为

\[
\boxed{\Gamma=2.}
\]

## 3. P025-T181 —— exact dyadic residual recomposition

radical identity 给出

\[
\operatorname{rad}(D_mS_m)
=
\frac{\operatorname{rad}(D_m)\operatorname{rad}(S_m)}2.
\]

所以

\[
\boxed{m(D_{2m})=2m(D_m)m(S_m).}
\]

与一般 cyclotomic overlap 不同，这里的 correction 是 universal 的，与 prime values 无关。

## 4. P025-T182 —— exact signed doubling transport

exponent `m` 的 projective denominator 为

\[
m(p+q),
\]

而 exponent `2m` 的 denominator 为

\[
2m(p+q).
\]

利用 P025-T181，

\[
\begin{aligned}
\rho_{2m,-}
&=\frac{2m(D_m)m(S_m)}{2m(p+q)}\\
&=\frac{m(D_m)}{m(p+q)}m(S_m)\\
&=\rho_{m,-}m(S_m).
\end{aligned}
\]

同理

\[
\boxed{\rho_{2m,-}=\rho_{m,+}m(D_m).}
\]

因此

\[
\boxed{
\rho_{2m,-}
=ho_{m,-}m(p^m+q^m)
=ho_{m,+}m(p^m-q^m).
}
\]

这就是 exact signed doubling law。

## 5. P025-T183 —— doubling 永不衰减 pressure

multiplicity residual 总是正整数，因此

\[
m(D_m)\ge1,
\qquad
m(S_m)\ge1.
\]

所以

\[
\boxed{\rho_{2m,-}\ge\rho_{m,-},\qquad\rho_{2m,-}\ge\rho_{m,+}.}
\]

即

\[
\boxed{\rho_{2m,-}\ge\max\{\rho_{m,-},\rho_{m,+}\}.}
\]

因此 exponent 的 prime-two cover 与一般 odd-prime cover 根本不同：它只能 resonant 或 amplified，永远不会 attenuate。

## 6. P025-C28 —— fourth-power 反例就是 resonant case

对

\[
(q,p)=(23,41),
\qquad m=2,
\]

Stage 82 给出

\[
p^2+q^2=2210
\]

squarefree，所以

\[
m(S_2)=1.
\]

于是

\[
\boxed{\rho_{4,-}=\rho_{2,-}=\frac32.}
\]

fourth-power counterexample 正是 resonant dyadic case。

从 sum branch 看，

\[
\rho_{2,+}=\frac1{128},
\]

而

\[
m(D_2)=192,
\]

因此同一个 doubled state 也可写成

\[
\rho_{4,-}=\frac1{128}\cdot192=\frac32.
\]

也就是说，一个 incoming edge resonant，另一个则强烈 amplified。

## 7. P025-C29 —— strict dyadic amplification 确实发生

对

\[
(q,p)=(7,17),
\qquad m=2,
\]

有

\[
S_2=17^2+7^2=338=2\cdot13^2,
\]

所以

\[
m(S_2)=13.
\]

因此

\[
\boxed{\rho_{4,-}=13\rho_{2,-}.}
\]

该例中

\[
\rho_{2,-}=\frac16,
\qquad
\rho_{4,-}=\frac{13}{6}>1.
\]

一个 subunit difference state 在一次 doubling 后就变成 hard state。

## 8. P025-T184 —— dyadic difference towers 单调

迭代 P025-T182。令

\[
e_j:=2^jm,
\]

则

\[
\boxed{
\rho_{e_{j+1},-}
=ho_{e_j,-}m(p^{e_j}+q^{e_j}).
}
\]

所以

\[
\boxed{
\rho_{2^am,-}
=ho_{m,-}
\prod_{j=0}^{a-1}m(p^{2^jm}+q^{2^jm}).
}
\]

乘积中的每个因子都是正整数，因此

\[
\boxed{
\rho_{m,-}\le\rho_{2m,-}\le\rho_{4m,-}\le\cdots.
}
\]

特别地，

\[
\boxed{
\rho_{m,-}\ge1
\Longrightarrow
\rho_{2^am,-}\ge1
\quad\forall a\ge0.
}
\]

而首次 cross-sign doubling 同样永不衰减，所以

\[
\boxed{
\rho_{m,+}\ge1
\Longrightarrow
\rho_{2^am,-}\ge1
\quad\forall a\ge1.
}
\]

## 9. 对 hard-state counting 的后果

一旦某个固定 prime-base pair 的 lower state 激活，就会产生无限 exponent descendants。

这些 descendants 不是彼此独立的 hard mechanisms，而处于同一个 deterministic dyadic transport orbit。

所以未来如果 exceptional-set argument 同时遍历 exponents，不应把

\[
m,2m,4m,8m,\ldots
\]

在已识别共同 active ancestor 后继续当成无关事件重复计数。

正确 state 应是 orbit / ancestor representation 加 integer edge multipliers。

## 10. Signed Hasse graph

结合 Stage 85–86，cover types 有三类：

1. difference odd-prime cover
   \[
   (m,-)\to(mp,-);
   \]
2. difference dyadic cover
   \[
   (m,-)\to(2m,-);
   \]
3. sum covers
   \[
   (m,+)\to(mp,+),\quad p\text{ odd prime},
   \]
   再加 cross-sign edge
   \[
   (m,+)\to(2m,-).
   \]

exponent divisibility 不产生 reverse difference-to-sum cover。

因此两张 same-sign Hasse diagrams 只是一个 directed signed transport graph 的两个 shadows。

## 11. Primitive roots 不变，但 descendants 发生耦合

加入 cross-sign edges 不会给 prime difference node 或 Stage 85 的 sum roots 新增 incoming edge。

所以 primitive nodes 仍为：

- difference roots：prime exponents；
- sum roots：odd prime exponents 与 powers of two。

但 descendants 现在耦合：每个 sum node 都向 doubled difference node 输送 pressure。

这说明 operation language 同时改变 connectivity 与 monotonicity。

## 12. Precision 解释

特殊 prime-two edge 的 universal overlap correction 恰好抵消 exponent normalization cost：

\[
\frac{\Gamma}{2}=1.
\]

剩下的 multiplier 只是一个正整数 residual。

所以 dyadic refinement 是一种 **lossless-or-amplifying pressure transport**。用 precision language 说，doubling operation 永远不会在 difference output 上遗忘一个已经可见的 hard-state signal。

这比一般 future compatibility 更强：它是 distinguished refinement edge 上的 monotone signal preservation。

## 13. Prior-art / novelty 边界

差平方分解以及 odd coprime inputs 下 `gcd(x-y,x+y)=2` 都是经典数学。

P025 不单独主张这些组成部分的新颖性。

项目侧候选是 exact projective signed-doubling law、其 non-attenuation consequence，以及用它识别后续 precision/counting 中应去重的 dyadic hard-state orbits。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 14. 可执行资产

新增：

- `src/enterprise_math/abc_signed_exponent_transport.py`；
- `tests/test_abc_signed_exponent_transport.py`。

executable layer 检查 universal overlap two、exact residual recomposition、两个 incoming doubling multipliers、resonant / amplified examples，以及有限 dyadic towers 上的 monotonicity。

## 15. 下一前沿

不存在硬阻断。继续：

1. 推导 generic odd-prime cover `m->rm` 的 local multiplier，用 new cyclotomic quotient 与 ancestor overlap 表示；
2. 精确识别 odd-prime cover 何时必 attenuate、resonate 或 amplify；
3. 判断 prime two 的 universal non-attenuation 是否在 cover primes 中唯一；
4. 构造 orbit-normal form，在任何 exponent-family counting 前先 quotient 掉 deterministic dyadic descendants；
5. 然后把 signed transport / monotone dyadic refinement Relay 给 A2/P023。
