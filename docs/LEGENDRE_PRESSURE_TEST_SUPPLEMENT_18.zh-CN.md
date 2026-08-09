# Legendre 压力测试 — 补充 18

状态：`ACTIVE RESEARCH NOTE`  
范围：first-factor cofactor windows 的精确跨 shell 分离  
依赖：规范 P017 L020–L027、L051–L053，以及 P018 T110–T113  
纪律：只使用有限整数算术；不使用素数分布估计，也不声称已经证明 Legendre 猜想。

## 1. L054 — Raw cofactor windows 严格分离

对素数 `p<=k`，定义

\[
W_p(k)=\left[\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor\right].
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

即

\[
2p\le k(r-p).
\]

若 `p=2`，则 `r-p>=1` 且 `k>=4`，所以 `k(r-p)>=4=2p`。

若 `p>=3`，则 `p,r` 都是奇素数，故 `r-p>=2`；又 `p<=k`，所以

\[
k(r-p)\ge2k\ge2p.
\]

因此 `p(k+2)<=rk`，进而

\[
\frac{k(k+2)}r\le\frac{k^2}p.
\]

向下取整后，由于 `W_p(k)` 下端点比 `floor(k^2/p)` 大 1，得到严格分离。∎

## 2. 尖锐有限例外

`k=3` 时

\[
W_2(3)=[5,7],\qquad W_3(3)=[4,5],
\]

二者在 `q=5` 相交，对应

\[
10=2\cdot5,\qquad15=3\cdot5.
\]

因此统一阈值 `k>=4` 是 sharp 的。

## 3. Least-factor stripping 为单射

对 open square basin 中的复合状态 `n`，令

\[
p=\operatorname{spf}(n),\qquad\Psi_k(n)=n/p.
\]

当 `k>=4` 时，`\Psi_k` 在全部 square-basin composite states 上为单射。同一 first-prime shell 内显然成立；不同 shells 若 stripped cofactor 相同，则同一个 q 必须同时属于两个 raw windows，与 L054 矛盾。

因此

\[
\boxed{n_1\ne n_2\Longrightarrow
\frac{n_1}{\operatorname{spf}(n_1)}\ne
\frac{n_2}{\operatorname{spf}(n_2)}}
\]

对 `I_k` 内任意两个不同复合状态成立。

## 4. 与 L052、L053、T113 的关系

L052 说明 `k>=15` 后不同 lower-band least primes 的候选 root pairs 两两不交。L054 工作在更细的整数 quotient 坐标：从 `k>=4` 起，所有 first-prime shells 的 exact quotient windows 已经两两不交，即使小 k 中粗 square-root basin 仍可能重合。

L053 与此正交：它在 mirror CRT cell 中保留 prime-power multiplicity，并可进一步压低 bounded radius capacity。T113 则说明每个 exact quotient window 内实际 root branch 至多由一个 threshold 切换。

因此 lower-band 现在同时具有：

1. exact parent quotient windows 有序且不交（L054）；
2. 稳定 lower-band root channels 不交（L052）；
3. full-core mirror CRT 能收缩 bounded lift capacity（L053）；
4. 每个 window 内 actual quotient-root branch 由单一 threshold 控制（T113）。

## 5. L054 尚未解决什么

单射 `n -> n/spf(n)` 把原来的 `2k`-state basin 映入更大的 cofactor 数值区间，因此 injection 本身不能推出 cardinality deficit。把 exact windows 扩大为完整 target square basins 同样会丢掉新结构，退化回普通 rough-number bookkeeping。

下一步必须保留 exact subwindows，并与原平方盆地约束耦合，尤其是 L053 的 multiplicity-sensitive mirror state。

## 6. 可执行验证

本次 replay 新增 `p017_cofactor_separation.py` 及其回归测试，覆盖严格排序、zero/positive integer gap、算术 spacing margin、least-factor stripping injection，以及 sharp `k=3` 例外。

历史创新性继续标记为 `NOVELTY_UNVERIFIED`。
