# P022 — Collision Polynomial 作为无序 Checkpoint Geometry 编码

状态：`ACTIVE RESEARCH NOTE / EXACT P011 SPECIALIZATION / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：P011 collision-polynomial completeness；`P022_BARLOW_FIBER_CONVOLUTION.*`

## 1. 两个逆定理可以精确复合

P011 已证明完整 collision coefficients

\[
(J_1,J_2,\ldots,J_M)
\]

可通过整数 binomial inversion 恢复完整有限 fiber-size profile。

P022 fiber-convolution theorem 又证明 selected-layer Barlow fiber profile 可恢复

\[
(\{\ell_1,\ldots,\ell_m\},u),
\]

即 observed segment-length multiset 与完全未观察 tail length。

因此两组 inverse 可以直接复合。

## 2. P022-CG01 — 精确 collision-polynomial inversion

令

\[
K_O(t)=\sum_{k\ge1}J_k(O)t^k
\]

为 Barlow selected-layer quotient 的完整 P011 collision polynomial，则

\[
\boxed{
K_O(t)
\Longleftrightarrow
(\{\ell_1,\ldots,\ell_m\},u).
}
\]

右侧是无序 checkpoint interval geometry 加 hidden tail。

整个 inverse 纯整数、有限：

1. P011 binomial inversion 恢复每个 `c_s`；
2. 最小 represented fiber size 给出 `2^u`，恢复 `u`；
3. 所有 fiber sizes 除以 `2^u`；
4. 用 triangular binomial-profile peeling 恢复每个 segment length 与 multiplicity。

## 3. Segment order 是当前 sharp loss

collision polynomial 无法识别 segment order，因为完整 fiber profile 是可交换的 multiplicative convolution。

例如

\[
(1,2,3)
\]

与

\[
(3,2,1)
\]

产生相同 collision polynomial，但 checkpoint layers 分别为

\[
(1,3,6)
\]

与

\[
(3,5,6).
\]

所以 collision polynomial 识别的是 **segment multiset geometry**，不是 ordered placement。

## 4. 低阶 coefficients 不足

exact `J_2` alias theorem 已给出固定 `N,m,J_2` 但不同 segment multisets 的例子。因此 CG01 实质上需要完整 finite collision state，而不是只保留第一个非平凡 coefficient。

当前不主张存在某个固定小阶 `(J_2,...,J_k)` 可普遍识别 geometry；最小 sufficient collision order 是独立开放问题。

## 5. 对 P011 的解释边界

一般情况下，P011 collision polynomial 只完整编码 fiber-size statistics，并不恢复制造 quotient 的机制。

在 Barlow specialization 中，binomial segment factorization 提供额外三角结构，使同一 collision polynomial 还能恢复无序 observation geometry。

因此

\[
\boxed{
\text{irreversibility statistics}
\to
\text{observation geometry}
}
\]

不是一般 P011 theorem，而是 P022 的结构化 specialization。

## 6. 可执行资产

- `src/enterprise_math/p022_barlow_collision_geometry.py`；
- `tests/test_p022_barlow_collision_geometry.py`。

测试将 P011 coefficients 反演成 fiber profile，再恢复 segment multiset 与 hidden tail，并保留 segment-order counterexamples。