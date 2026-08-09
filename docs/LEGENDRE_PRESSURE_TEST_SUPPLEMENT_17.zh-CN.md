# Legendre 压力测试 — 补充 17

状态：`ACTIVE RESEARCH NOTE`  
范围：first-factor cofactor windows 的精确跨 shell 分离  
依赖：canonical P017 cofactor-window 公式 L020–L027、lower-band root packing L051–L052，以及 P018 T110–T113  
纪律：只使用有限整数算术；不使用素数分布估计，也不声称已经证明 Legendre 猜想。

## 1. L053 — Raw cofactor windows 严格分离

对素数 `p<=k`，精确 raw first-factor cofactor window 为

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

### 定理

设 `k>=4`，并令 `p<r<=k` 为素数，则

\[
\boxed{\max W_r(k)<\min W_p(k).}
\]

等价地，

\[
\left\lfloor\frac{k(k+2)}r\right\rfloor
\le
\left\lfloor\frac{k^2}p\right\rfloor.
\]

### 证明

只需证明

\[
p(k+2)\le rk,
\]

也就是

\[
2p\le k(r-p).
\]

若 `p=2`，则 `r-p>=1`，而 `k>=4`，因此

\[
k(r-p)\ge4=2p.
\]

若 `p>=3`，则 `p,r` 均为奇素数，所以 `r-p>=2`；同时 `p<=k`，因此

\[
k(r-p)\ge2k\ge2p.
\]

于是 `p(k+2)<=rk`，进而

\[
\frac{k(k+2)}r\le\frac{k^2}p.
\]

向下取整后，由于 `W_p(k)` 的下端点比 `floor(k^2/p)` 大 1，得到严格分离。∎

## 2. 尖锐的有限例外

`k>=4` 不是证明技巧造成的条件。`k=3` 时

\[
W_2(3)=[5,7],
\qquad
W_3(3)=[4,5],
\]

二者在 `q=5` 相交。对应的平方盆地状态为

\[
10=2\cdot5,
\qquad
15=3\cdot5.
\]

## 3. Least-factor stripping 为单射

对 open square basin 中的 composite state `n`，令

\[
p=\operatorname{spf}(n),
\qquad
\Psi_k(n)=n/p.
\]

当 `k>=4` 时，`Psi_k` 在整个平方盆地 composite states 上为单射。

同一 first-prime shell 内这一点显然成立；不同 first-prime shells 之间，如果 stripped cofactors 相同，则同一个 q 必须同时落入两个不同 raw windows，但 L053 已证明这些 windows 两两不交。

因此对所有 `k>=4`，

\[
\boxed{
n_1\ne n_2\text{ 为 }I_k\text{ 中 composite}
\Longrightarrow
\frac{n_1}{\operatorname{spf}(n_1)}
e
\frac{n_2}{\operatorname{spf}(n_2)}.
}
\]

这比原 state 空间中 first-factor shells 不交更强：它说明这些 shells 的 quotient images 也互不相交。

## 4. 与 L052 和 T113 的关系

canonical L052 说明：当 `k>=15` 时，不同 lower-band least primes 的候选 root pairs

\[
\{j_p,j_p+1\}
\]

已经两两不交。

L053 工作在 root 坐标之下更细的整数 q 坐标上：从 `k>=4` 开始，**所有** first-prime shells 的 exact cofactor windows 都已经不交，包括小 k 中两个 windows 仍可能落入同一个粗 square-root basin 的情形。

随后 P018-T113 又在每个 exact window 内最多用一个 square-root boundary 把它切成两段。

因此 lower-band recursion 现在同时受到三层约束：

1. exact parent cofactor windows 有序且不交（L053）；
2. `k>=15` 时 lower-band parent root channels 也已经不交（L052）；
3. 每个 parent window 内的 actual quotient-root branch 由单一精确 threshold 控制（T113）。

## 5. L053 尚未解决什么

单射 `n -> n/spf(n)` 会把原来的 `2k`-state basin 映入更大的 cofactor 数值范围，因此单靠 injection 不能推出 cardinality deficit。

同样，如果把每个 exact cofactor window 扩大成完整 target square basin，就会丢掉刚得到的精确结构，重新退化为普通 rough-number 账本。

真正下一步必须保留 exact local subwindows，同时和原平方盆地中的约束耦合，例如 centered mirror certificates。任何候选如果实际上偷偷恢复了完整 small-prime sieve，都应立即降级。

## 6. 可执行验证

本次 replay 新增：

- `src/enterprise_math/p017_cofactor_separation.py`；
- `tests/test_p017_cofactor_separation.py`。

测试覆盖严格排序、zero/positive integer gap、算术 spacing margin、least-factor stripping injection，以及 sharp `k=3` 例外。

历史创新性继续标记为 `NOVELTY_UNVERIFIED`。
