# P018 —— 有限精度证明演算：补充 08

状态：`ACTIVE RESEARCH NOTE`  
范围：near-diagonal factor proof slack 的 centered-prime radius 表示  
依赖：P018 第七至第八阶段  
纪律：围绕偶数中心的对称素数表示属于基本数论。本文不声称每一个中心都存在正半径对称素数对，也不证明任何 Goldbach 型猜想。

## 1. 把第八阶段重新以 upper square root 为中心

第八阶段用

\[
s=\sigma(k),
\qquad
p=k-s,
\qquad
q=p+2(s+1)
\]

描述 near-diagonal first-factor shell。

引入 upper-square center

\[
\boxed{c=k+1}
\]

和正半径

\[
\boxed{r=s+1.}
\]

于是

\[
\boxed{
p=c-r,
\qquad
q=c+r.}
\]

所以第八阶段的 prime pair 恰好关于 `c` 对称，并且

\[
\boxed{p+q=2c.}
\]

唯一 shell state 变成平方差

\[
\boxed{pq=c^2-r^2.}
\]

这使 factor proof slack 得到新的解释：`sigma+1` 是围绕 upper square root 的一个候选 symmetric-prime radius。

## 2. Centered prime radius

对整数中心 `c>=2`，若存在正整数半径使中心两侧同时为素数，定义 **positive centered prime radius**：

\[
\boxed{
\rho(c)=
\min\{r\ge1:c-r\text{ 与 }c+r\text{ 都为素数}\}.
}
\]

这里刻意要求半径为正，所以半径零的同一素数重复表示不包含在定义中。

定义集合可能为空。P018 不提出 universal existence 主张。

## 3. P018-T71 —— Centered shell 定理

状态：`PROVED`。

设 `c>=3`、`r>=1`，并令

\[
k=c-1,
\qquad
p=c-r.
\]

假设

\[
\boxed{
p\ge3\text{ 为素数},
\qquad p>r^2.}
\]

则

\[
\boxed{
L_p(k)\ne\varnothing
\iff
c+r\text{ 为素数}.}
\]

非空时

\[
\boxed{
L_p(k)=\{(c-r)(c+r)\}
=\{c^2-r^2\}.}
\]

证明：取 `s=r-1`。此时 `p=k-s`，而假设 `p>r^2=(s+1)^2` 正是第八阶段 T63 的条件。T63 给出等价关系以及 singleton shell，右侧素数为

\[
p+2(s+1)=c-r+2r=c+r.
\]

乘积公式只是平方差恒等式。∎

所以靠近 universal factor horizon 的 first-factor shell 可以按 upper square root 周围的 symmetric prime radius 编号。

## 4. P018-T72 —— 最小 centered radius 等于 factor proof slack 加一

状态：`PROVED`。

假设 `rho(c)` 存在，记

\[
r=\rho(c),
\qquad
p=c-r.
\]

再假设

\[
\boxed{p\ge3,
\qquad p>r^2.}
\]

令 `k=c-1`。则

\[
\boxed{
\sigma(k)=r-1.}
\]

### 证明

因为 `c-r` 与 `c+r` 都是素数，T71 给出

\[
L_{c-r}(k)\ne\varnothing.
\]

因此

\[
H(k)\ge c-r.
\]

反设 `H(k)>c-r`。非空 first-factor shell 的 index 必为素数，所以可写

\[
H(k)=c-r'
\]

其中

\[
1\le r'<r.
\]

又因为

\[
c-r'>c-r>r^2>(r')^2,
\]

T71 可用于半径 `r'`。`L_(c-r')(k)` 非空会迫使

\[
c-r',\qquad c+r'
\]

同时为素数，这与 `r=rho(c)` 的最小性矛盾。

所以

\[
H(k)=c-r.
\]

由 `k=c-1`：

\[
\sigma(k)=k-H(k)
=(c-1)-(c-r)=r-1.
\]

∎

因此在 near-diagonal 适用范围内，最小对称 prime radius **恰好比最小 factor precision slack 大一**。

## 5. P018-T73 —— 实际 factor slack 给出最小 centered radius

状态：`PROVED`。

反过来，假设

\[
\sigma(k)=s,
\qquad
r=s+1,
\qquad
c=k+1,
\qquad
p=c-r=k-s.
\]

并满足

\[
\boxed{p\ge3,
\qquad p>r^2.}
\]

则

\[
\boxed{
\rho(c)=r=s+1.}
\]

证明：第八阶段 T66 给出 `p=c-r` 与 `c+r` 都为素数，所以半径 `r` 处存在 centered pair。

若存在更小半径 `r'<r` 的 centered prime pair，则

\[
c-r'>c-r>r^2>(r')^2.
\]

由 T71，必有一个非空 shell `L_(c-r')(k)`，其 index 严格大于

\[
c-r=H(k),
\]

与 factor horizon 定义矛盾。∎

因此 T72–T73 合并得到

\[
\boxed{
\rho(k+1)=\sigma(k)+1
}
\]

只要两边处于共同 near-diagonal 范围：

\[
k-\sigma(k)>(\sigma(k)+1)^2,
\]

等价地，最小 centered pair 的左素数大于其半径平方。

## 6. P018-T74 —— 固定 slack 的 first-centered-pair 判据

状态：`PROVED`。

固定 `s>=0`，令

\[
c=k+1,
\qquad
r=s+1,
\qquad
p=c-r=k-s,
\]

并假设 `p>=3` 为素数且 `p>r^2`。

则

\[
\boxed{
\sigma(k)=s
}
\]

当且仅当：

1. `c-r` 与 `c+r` 都为素数；
2. 对每个整数 `1<=t<r`，`c-t`、`c+t` 至少一个不是素数。

等价地，在该大小条件下

\[
\boxed{
\sigma(k)=s
\iff
\rho(c)=s+1.
}
\]

证明：正向是 T73，反向是 T72。∎

所以 factor-slack strata 可以重新理解为 **first centered-prime-radius strata**。

第八阶段的两个特殊情形立即得到：

- `sigma=0`：第一个 centered prime pair 出现在 radius `1`，即 twin-prime stratum；
- `sigma=1`：第一个 centered prime pair 出现在 radius `2`，即 gap-four stratum。

## 7. P018-T75 —— Radius、prime gap、square offset 与 parity 是同一个坐标

状态：`PROVED`。

在 T73 条件下，令 `r=sigma(k)+1`，最后一个 near-diagonal composite shell 满足

\[
\boxed{
\begin{aligned}
p&=k+1-r,\\
q&=k+1+r,\\
q-p&=2r,\\
p+q&=2(k+1),\\
pq&=(k+1)^2-r^2.
\end{aligned}}
\]

因为 `p,q>=3` 都是奇素数，center `k+1` 与 radius `r` 奇偶性相反，等价于

\[
\boxed{r\equiv k\pmod2.}
\]

又因为 `sigma=r-1`，也得到

\[
\boxed{\sigma(k)\equiv k+1\pmod2.}
\]

只要 factor horizon 落在这个 near-diagonal odd-prime 范围。

因此一个整数 `r` 同时测量：

- 第一个 symmetric-prime search radius；
- forced prime gap 的一半；
- upper-square offset 的平方根；
- factor proof slack 加一。

这把第八阶段多个坐标进一步压缩成一个 centered finite-precision coordinate。

## 8. 证明论解释

第七阶段问：要积累多少 factor precision，才能确保所有 survivor 已经是 prime？

第九阶段在该 precision requirement 接近 universal cutoff 时给出几何解释：

> proof 从 universal factor horizon 向内移动，直到遇到围绕 `k+1` 的第一个 symmetric prime pair。

向内移动量是 `sigma`；centered radius 是 `sigma+1`。

这**不**意味着 centered prime pair 就是证明每个平方盆地存在 prime survivor 的机制。这里的 centered pair 描述的是**最后一个 composite first-factor obstruction** 的位置，不是 prime survivor 本身。

Legendre existence target 仍然开放。

## 9. 防止 Goldbach 型过度主张的边界

恒等式

\[
(c-r)+(c+r)=2c
\]

意味着：只要 centered pair 已存在，它当然给出偶数 `2c` 的一个两素数表示。

P018 只使用那些已经由第八阶段 factor-shell 条件，或者由显式给定 prime pair 保证存在的 centered pair。

本文**不**主张：

- 每个 `c` 都存在 positive centered prime radius；
- 每个偶数都有 distinct-prime centered representation；
- 任何形式的 Goldbach conjecture。

`rho(c)` 的 universal existence 是独立困难数论问题，不是 T71–T75 的前提。

## 10. 第九阶段状态

- P018-T71 centered shell theorem：`PROVED`
- P018-T72 minimal centered radius => exact factor slack：`PROVED`
- P018-T73 actual near-diagonal slack => minimal centered radius：`PROVED`
- P018-T74 fixed-slack / first-centered-pair criterion：`PROVED`
- P018-T75 unified radius/gap/square-offset/parity coordinate：`PROVED`
- positive `rho(c)` 的 universal existence：`NOT CLAIMED / OPEN`
- 利用 centered radius 证明每个平方盆地存在 prime survivor：`OPEN`
- `rho(k+1)` 在相邻盆地之间的 recurrence 或 deterministic bound：`OPEN`

可执行有限检查位于 `src/enterprise_math/centered_prime_radius.py` 与 `tests/test_centered_prime_radius.py`。
