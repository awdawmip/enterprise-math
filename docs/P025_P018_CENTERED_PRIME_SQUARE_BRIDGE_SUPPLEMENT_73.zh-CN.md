# P025 补充 73 —— `(2,2)` Difference Atom 的 Centered-Prime 对偶

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 72；canonical P018 centered-prime-radius layer  
Hard block：`NONE`

## 1. 从 prime bases 切换到 centered-prime coordinates

考虑 cutoff-five `(2,2)` difference shell，取不同奇素数

\[
p>q.
\]

两个 prime-power complements 为

\[
q^2,\qquad p^2,
\]

active difference component 为

\[
N=p^2-q^2.
\]

改用 P018 已采用的 centered-prime coordinates：

\[
\boxed{
B=\frac{p+q}{2},
\qquad
A=\frac{p-q}{2}.
}
\]

于是

\[
q=B-A,
\qquad
p=B+A.
\]

由于 `p,q` 是不同奇素数，

\[
\boxed{\gcd(A,B)=1,}
\]

且 `A,B` 奇偶性相反。

## 2. P025-T142 —— projective value 的精确闭式

P025 active component 化为

\[
\boxed{N=4AB.}
\]

由于 `A,B` 互素且恰有一个为偶数，

\[
\operatorname{rad}(4AB)
=
\operatorname{rad}(A)\operatorname{rad}(B),
\]

所以

\[
\boxed{m(4AB)=4m(A)m(B).}
\]

两个 complement capacities 都等于 2，因此 cross-capacity 为

\[
K=2p+2q=4B.
\]

故 active side projective term 精确等于

\[
\rho_{(2,2),-}
=
\frac{m(4AB)}{4B}
=
\boxed{\frac{m(A)}{\operatorname{rad}(B)}}.
\]

因此 threshold `T` 在 centered coordinates 中变成 exact 判据：

\[
\boxed{
\rho_{(2,2),-}\ge T
\iff
m(A)\ge T\operatorname{rad}(B).
}
\]

一旦 `(A,B)` 已知，就不再需要重新 factor 巨大的 active component `p^2-q^2` 才能回答该 query。

## 3. P018 与 P025 读取同一坐标上的对偶二次量

同一个 centered prime pair 在 P018 中给出 difference-of-squares shell：

\[
\boxed{
(B-A)(B+A)=B^2-A^2=pq.
}
\]

P025 读取的则是**prime squares 的 difference**：

\[
\boxed{
(B+A)^2-(B-A)^2=4AB=p^2-q^2.
}
\]

因此两条路线共享同一个 coordinate chart，但观察的是互补 quadratic forms：

\[
\boxed{
(B,A)\mapsto(B^2-A^2,\ 4AB).
}
\]

这是真正的 cross-route bridge，而不是符号巧合。

## 4. 边界：共享坐标不等于共享 minimal radius

P018 canonical factor-proof-slack theorem 只有在额外 hypotheses 下才把特殊 radius 与 slack 精确对应，其中包括

\[
q=B-A>A^2,
\]

而 exact slack equivalence 还要求 centered prime radius 的 minimality。

P025-T142 不需要这些条件；任意奇 centered prime pair 都成立。

因此绝不能因为两者都使用 `(B,A)`，就把 P025 radius `A` 直接等同于 P018 factor-proof slack。

正确边界是：

- centered-prime coordinate system：始终共享；
- P018 centered shell data：`q>A^2` 时可直接调用；
- P018 minimal-slack identification：还必须满足更强 canonical P018 hypotheses。

## 5. 精确样本

### P018 size range 之外

取

\[
q=5,\qquad p=59.
\]

则

\[
(B,A)=(32,27).
\]

P018 underlying product coordinate 为

\[
B^2-A^2=295=5\cdot59.
\]

P025 active component 为

\[
4AB=3456=59^2-5^2.
\]

projective value 为

\[
\boxed{
\rho=\frac{m(27)}{\operatorname{rad}(32)}=\frac92.
}
\]

该 radius 远不满足 `q>A^2`，因此不作任何 P018 factor-slack 主张。

### P018 canonical size range 内

取

\[
q=73,\qquad p=89.
\]

则

\[
(B,A)=(81,8),
\qquad73>8^2.
\]

P018 shell state 为

\[
\boxed{81^2-8^2=6497=73\cdot89.}
\]

P025 active component 为

\[
\boxed{89^2-73^2=2592=4\cdot81\cdot8.}
\]

且

\[
\boxed{
\rho=\frac{m(8)}{\operatorname{rad}(81)}=\frac43>1.
}
\]

所以 activated P025 `(2,2)` atom 确实会进入 P018 centered theorem range。

另一个样本是

\[
(q,p)=(503,521),
\quad
(B,A)=(512,9),
\]

其中

\[
\rho=3/2.
\]

## 6. 精度解释

Stage 72 已证明 exponent precision 到达饱和，必须切换坐标族。P025-T142 给出一个成功切换：

\[
(p,q,e=f=2)
\to
(B,A)
\to
(m(A),\operatorname{rad}(B)).
\]

对 projective-threshold query 而言，一旦知道 centered radius residual 与 center radical，就不再需要完整 prime bases `p,q`。

与此同时，P018 用同一个 `(B,A)` 回答完全不同的 shell/factor query。这再次说明：一个 coordinate chart 可以服务多个 future languages，但每个语言需要的 minimal derived state 不同。

## 7. Prior-art / ownership 边界

Centered prime pairs、difference-of-squares algebra 与 P018 centered-prime-radius machinery 都属于既有/canonical 数学。P025 不主张新坐标系。

项目侧结果仅是 `(2,2)` projective difference atom 到 `m(A)/rad(B)` 的 exact reduction，以及与 P018 quadratic shell 的 cross-route comparison；历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 8. 可执行资产

新增：

- `src/enterprise_math/abc_prime_square_centered_bridge.py`；
- `tests/test_abc_prime_square_centered_bridge.py`。

当 explicit size hypothesis 成立时，executable bridge 会直接调用 canonical P018 centered-prime helper；否则明确保留边界。

## 9. 下一前沿

Hard block 不存在。继续：

1. 利用 P018 size inequality `A^2<q<B` 与 `m(A)>=T rad(B)` 强化 overlap slice 的计数；
2. 比较同时落入两条路线时，P018 factor-proof slack 与 P025 projective ratio 哪一个是更便宜的 future state；
3. 对 `(3,3)` 尝试通过 sum/difference-of-cubes factorization 寻找类似 coordinate switch；
4. 将该 bridge Relay 给 P018，关系标为 `COMPOSABLE_INDEPENDENT`，而不是转移 mother-theorem ownership。
