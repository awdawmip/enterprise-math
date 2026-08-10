# P025 补充 74 —— P018/P025 Centered Overlap 上的 Small-Radical 压缩

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 73；canonical P018 centered-prime size range；external de Bruijn radical counting  
Hard block：`NONE`

## 1. 加入 canonical P018 size hypothesis

使用 Stage-73 centered coordinates

\[
q=B-A,
\qquad
p=B+A,
\]

其中 `p>q` 为不同奇素数，并进一步假设该 pair 落在 P018 centered theorem range：

\[
\boxed{q=B-A>A^2.}
\]

于是特别有

\[
\boxed{A^2<B.}
\]

若 P025 `(2,2)` difference atom 穿过 threshold `T>=1`，Stage 73 给

\[
\boxed{m(A)\ge T\operatorname{rad}(B).}
\]

## 2. P025-T143 —— overlap 压成一个 small-radical integer

由于 `A,B` 互素，

\[
\operatorname{rad}(AB)=\operatorname{rad}(A)\operatorname{rad}(B).
\]

projective threshold 写成

\[
\frac A{\operatorname{rad}(A)}
\ge
T\operatorname{rad}(B),
\]

故

\[
\boxed{T\operatorname{rad}(AB)\le A.}
\]

定义

\[
\boxed{n=AB.}
\]

P018 size range 进一步给出两个 exact integer inequalities：

\[
\boxed{n^2=A^2B^2<B^3,}
\]

以及

\[
\boxed{T^2\operatorname{rad}(n)^2\le A^2<B.}
\]

所以一个同时涉及两个 centered primes 与 prime-square abc relation 的状态，被压成了**单个整数 `n=AB`**，且其 radical 极小。

## 3. Center-height 形式

限制

\[
B\le X.
\]

P025-T143 变成

\[
\boxed{
n<X^{3/2},
\qquad
\operatorname{rad}(n)<\frac{X^{1/2}}T.
}
\]

这正是 Stage 62/64 所使用的 de Bruijn radical-counting tool 的 theorem-native input form。

一旦完成这一步编译，`B-A` 与 `B+A` 是否 prime 对外部 counting theorem 已不是必要输入；这些额外 primality conditions 只会进一步缩小候选集。

## 4. P025-C18 —— de Bruijn overlap scale

导入 Stage 64 同一形式的经典 de Bruijn radical-counting estimate。

整数 `n` 的 height 为 `X^(3/2)`，而 radical height 只有 `X^(1/2)/T`，恰好是 product-height exponent 的三分之一。

再用标准 divisor bound 从 `n=AB` 恢复 `(A,B)`，得到 overlap slice 的形式尺度

\[
\boxed{
N_X^{\rm overlap}(T)
\ll_\varepsilon\frac{X^{1/2+\varepsilon}}T.
}
\]

这里的 `X` 是 **center height**，不是原 abc `c=p^2` height。

这远小于仅使用 `B<=X`、`A^2<B` 所得到的平凡 `O(X^(3/2))` integer-pair 数量。

解析计数依赖 external prior art；新的项目内部 theorem 是 exact compression P025-T143。

## 5. 为什么 cross-route overlap 会进一步降指数

Stage 64 generic projective compiler 会把 height-`X` additive state 送入大约 `X^2` 尺度的 pair product。

在 P018 centered overlap 上，canonical size hypothesis 强迫

\[
A<\sqrt B,
\]

所以 theorem-native product 只有

\[
AB<B^{3/2}.
\]

同一个 projective threshold 又把 radical 控制在 `B^(1/2)/T`。

因此 cross-route theorem 直接从 de Bruijn 需要计数的对象 height 中削掉了半个维度。

这项增益单独从任一条路线都得不到：

- P025 提供 radical inequality；
- P018 提供 radius-square size restriction。

## 6. 精确样本

### `(q,p)=(73,89)`

\[
(B,A)=(81,8),
\qquad73>8^2.
\]

P025 threshold-one state 有

\[
n=81\cdot8=648,
\qquad
\operatorname{rad}(n)=6.
\]

确有

\[
6\le8,
\qquad
648^2<81^3.
\]

### `(q,p)=(503,521)`

\[
(B,A)=(512,9),
\]

并且

\[
n=4608,
\qquad
\operatorname{rad}(n)=6.
\]

threshold one 同样成立。

### `(q,p)=(997,1051)`

\[
(B,A)=(1024,27),
\]

projective value 为 `9/2`。在 threshold four 下

\[
4\operatorname{rad}(AB)=24\le27.
\]

这是落在 P018 size range 内的 higher-threshold overlap 样本。

## 7. Centered coordinates 中的 pointwise squarefree guard

Stage 73 exact formula

\[
\rho=\frac{m(A)}{\operatorname{rad}(B)}
\]

立即推出

\[
\boxed{
\rho\ge1
\Longrightarrow
A,B\text{ 都 nonsquarefree}.}
\]

因为：

- 若 `A` squarefree，则 `m(A)=1<rad(B)`；
- 若 `B` squarefree，则 `rad(B)=B>A>=m(A)`。

因此在调用任何 counting theorem 前，center/radius 任一 squarefree bit 就足以认证这个 P025 shell 为 subunit。

这是 Stage 69 coarse safe basin 在 centered coordinate chart 中的对应版本。

## 8. Cross-route precision 解释

完整 overlap pipeline 现在是

\[
\boxed{
(p,q)
\to
(B,A)
\to
[\text{P018 size guard }A^2<B]
+
[\text{P025 ratio }m(A)/rad(B)]
\to
n=AB
\to
\text{small-radical external count}.
}
\]

不同路线贡献独立 coordinates，而它们的 join 生成了比保留原始 prime pair 更便宜的 theorem-native state。

这是 composable precision 的具体例子，而不是一条路线吞并另一条路线。

## 9. Prior-art / ownership 边界

P018 size theorem 在其 scope 内属于 canonical Enterprise Math；de Bruijn radical counting 与 divisor bound 属于 external prior mathematics；`n=AB` 的代数转换是初等的。

P025 只保留这些输入的 exact cross-route composition，历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

不主张 P025 脱离 imported radical count 独立证明了新的 prime-pair density theorem。

## 10. 可执行资产

新增：

- `src/enterprise_math/abc_p018_centered_overlap.py`；
- `tests/test_abc_p018_centered_overlap.py`。

代码只保存 exact finite inequalities 与 formal height powers，不实现 external asymptotic theorem。

## 11. 下一前沿

Hard block 不存在。继续：

1. 将 P025-T142/T143 Relay 给 P018，作为 composable centered-coordinate consumer；
2. 与 P018 existing factor-proof horizon 比较，不重复建立另一套 prime-pair counting machinery；
3. 在 `(3,3)` 与 `(4,4)` shells 中寻找类似 cross-route size gain；
4. 把 `independent route coordinates -> cheaper joined theorem-native state` 作为 Foundation backflow 样本。
