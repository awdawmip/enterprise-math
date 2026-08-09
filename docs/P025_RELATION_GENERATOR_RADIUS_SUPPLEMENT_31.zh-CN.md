# P025 补充 31 —— First Witness 与 Primitive Direct Access 之间的 Relation-Generator Radius

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-shared-access-stage30`  
依赖：P025 补充 14–15、23、30  
Hard block：`NONE`

## 1. 第三种 access 尺度

补充 30 区分了 ambient derivative-image word norm 与 intrinsic relation-step geometry。由此自然产生一个新问题：有限半径下可直接访问的 relation-compatible states，何时已经足以**生成整个 relation subgroup**？

对 unit relation

\[
\boxed{1+b=c,}
\]

compressed additive relation state 为一维。令

\[
A_b=A(b),\qquad A_c=A(c),
\]

并定义 primitive positive common derivative-value group step

\[
\boxed{D=\operatorname{lcm}(A_b,A_c).}
\]

每个 relation state 的共同 derivative value 都可写成

\[
t=kD,\qquad k\in\mathbb Z.
\]

## 2. P025-D18 —— radius-`R` 可访问 scale factors

定义

\[
\boxed{
K_R
=
\{k\in\mathbb Z:
\kappa_b(kD)\le R,
\ \kappa_c(kD)\le R\}.
}
\]

每个有限 `R` 下，`K_R` 有限且关于符号对称。

半径 `R` 能直接访问的 relation states 恰为

\[
\boxed{D K_R.}
\]

它们生成的 subgroup 为

\[
\boxed{D\,g_R\mathbb Z,\qquad g_R=\gcd\{|k|:k\in K_R\}.}
\]

若只能访问 zero scale，则约定 `g_R=0`。

## 3. P025-D19 —— relation-generator radius

定义

\[
\boxed{
\rho_{\rm gen}=\min\{R:g_R=1\}.
}
\]

也就是说，`rho_gen` 是当前有限半径可访问的 relation-compatible derivative states 第一次**整体生成整个 rank-one relation group**的半径，即使 primitive group step `D` 本身还不可直接访问。

它与此前两个坐标不同：

- `mu`：第一次出现 nonzero/nondegenerate relation state；
- `nu`：第一次直接访问 primitive absorption-floor step `D`。

## 4. P025-T86 —— unit relation 中的 universal ordering

Unit relation 中任意非零 common derivative value 都给出非零 Wronskian，所以 `mu` 是 `K_R` 第一次出现非零元素的半径。

在 `nu` 时，primitive scale `k=1` 按定义已经可直接访问，因此 `g_nu=1`。

所以

\[
\boxed{\mu\le\rho_{\rm gen}\le\nu.}
\]

两边都不必取等。

## 5. Exact example `1+8=9`

这里

\[
D=12.
\]

radius 1 没有 nonzero common derivative value；radius 2 时 `k=1` 已经可访问。因此

\[
\boxed{\mu=\rho_{\rm gen}=\nu=2.}
\]

## 6. Exact example `1+22=23`

这里 derivative-image level 上两边分别 squarefree/prime，因此

\[
D=1.
\]

radius 2 时 common target `2` 已可访问：

\[
K_2=\{0,\pm2\},
\]

所以

\[
g_2=2.
\]

radius 3 仍没有 odd common scale，因此仍有

\[
g_3=2.
\]

radius 4 时 scale `2` 与 `3` 都可访问，于是

\[
\gcd(2,3)=1,
\]

当前可访问 relation states 已经生成整个 group，尽管 primitive state `k=1` 仍不可直接访问。

Primitive direct access 要到 radius 5 才发生。因此

\[
\boxed{\mu=2<\rho_{\rm gen}=4<\nu=5.}
\]

这精确分离了三类 finite precision semantics。

## 7. P025-T87 —— Sophie-type closed generator radius

假设

\[
q\ge5,\qquad q\text{ prime},\qquad2q+1\text{ prime}.
\]

考虑

\[
\boxed{1+2q=2q+1.}
\]

因为 `q>=5`，`2q+1` 为素数强迫

\[
\boxed{q\equiv5\pmod6.}
\]

Unit relation group step 为

\[
D=1.
\]

Stage 14 已给出

\[
\boxed{\mu=2,\qquad\nu=\frac{q-1}{2}.}
\]

而 generator radius 为

\[
\boxed{\rho_{\rm gen}=\frac{q+1}{3}.}
\]

### 证明

Even common target `2` 在 radius 2 已可访问：`2q` block 使用 coefficient-2 coordinate 一次，prime block 使用 coordinate value 2。

要生成整个 group `Z`，最终必须出现 odd common target。

把 `2q`-block target 写成

\[
qx+2y=t.
\]

假设 `t` 为奇数，且

\[
|x|,|y|,|t|\le R.
\]

若 `R<q`，任何 odd `x` 满足 `|x|>=3` 都不可能，因为

\[
|qx+2y|\ge3q-2R>R.
\]

所以第一次出现 odd target 时只能用 `x=±1`。由对称性取 `x=1` 且 `t>0`，则

\[
y=\frac{t-q}{2}.
\]

半径约束要求

\[
t\le R,\qquad\frac{q-t}{2}\le R.
\]

故

\[
q\le3R,
\]

即

\[
R\ge\left\lceil\frac q3\right\rceil.
\]

因为 `q=6k+5`，下界为

\[
2k+2=\frac{q+1}{3}.
\]

在这个半径恰好取

\[
t=2k+1,\qquad x=1,\qquad y=-(2k+2).
\]

`t` 为奇数且三个 magnitudes 都不超过 `(q+1)/3`，所以第一个 odd common scale 正好在这里出现。

由于 scale `2` 更早已经可访问，一旦出现任意 odd scale，可访问 scale 的 gcd 立即降为 1。∎

## 8. Strict three-level separation

`q=5` 时三者恰好都为 2。

在 stated scope 中，只要

\[
q\ge11,
\]

就有

\[
\boxed{2=\mu<\frac{q+1}{3}=\rho_{\rm gen}<\frac{q-1}{2}=\nu.}
\]

例如

\[
\begin{array}{c|c|c|c}
q&\mu&\rho_{\rm gen}&\nu\\\hline
11&2&4&5\\
23&2&8&11\\
29&2&10&14\\
41&2&14&20
\end{array}
\]

不主张这类 `q` 有无穷多个。

## 9. 架构后果

Unit-relation precision ladder 现在出现三种不同 access semantics：

\[
\boxed{
\text{first nonzero witness }\mu
\to
\text{group-generation radius }\rho_{\rm gen}
\to
\text{primitive direct access }\nu.
}
\]

中间层的含义是：

> 当前有限 precision 可直接访问的 relation-compatible states，经过允许的整数复合后已经能生成所有 relation states，即使 primitive generator 自身还在 direct-access ball 之外。

因此“当前 precision 直接可访问”与“由当前 precision 可访问状态代数生成”是不同概念。

## 10. Prior-art 边界

`Z` 的 subgroups、gcd generation、word-generation radii 与上述 elementary modular/Bezout arguments 都属于标准数学。

P025 不主张 generic priority。项目侧新增候选是：在 arithmetic-derivative relation system 中，把 generator-completeness precision 插入 first witness access 与 primitive floor access 之间。

## 11. 可执行资产

新增：

- `src/enterprise_math/abc_relation_generator_radius.py`
  - unit relation group step；
  - radius-accessible scale factors；
  - generated scale gcd；
  - exact generator radius；
  - Sophie-family closed profile。
- `tests/test_abc_relation_generator_radius.py`
  - `1+8=9` 三尺度重合；
  - `1+22=23` strict `2<4<5`；
  - Sophie examples `q=5,11,23,29,41`；
  - `q>=11` examples 的严格分离。

## 12. 下一前沿

没有 hard block。继续：

1. 用 HNF/index 而不是 scalar gcd 把 `rho_gen` 推广到 higher-rank relation subgroups；
2. 比较在 `rho_gen` 半径生成的 intrinsic word metric 与 ambient restricted access norm；
3. 判断允许 arbitrary integer composition 但不要求 direct primitive witness recovery 的 future language，是否应以 generator completeness 为合适状态；
4. 把新的 access/generation/direct-access 区分 Relay 给 P023/A5；
5. 寻找不依赖未解 infinitude statement、且 `rho_gen/mu` 或 `nu/rho_gen` 可证明无界的 families。
