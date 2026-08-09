# Legendre 压力测试 — 补充 15

状态：`ACTIVE RESEARCH NOTE`  
范围：lower least-factor band 中 P018-T110 目标 root 的跨 shell packing  
依赖：P017 L001 root-factor horizon、规范 P018-T110–T112  
纪律：本文**不**证明 Legendre 猜想。只使用初等整数不等式、素数奇偶/间距以及已规范化的 quotient-root transport，不调用素数分布估计。

## 1. lower-band 下降为什么还需要跨 shell 定理

P018-T110–T112 已经从根本上改变了 lower-band 问题。

若

\[
n=pq,
\qquad k^2<n<(k+1)^2,
\]

且 `p` 是最小素因子，则提取 `p` 后，cofactor root 会落到严格更低的平方根尺度。

对一枚 lower-band prime

\[
p^2<2k,
\]

定义

\[
\boxed{
j_p
=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right).}
\]

T110 说明 cofactor root 只能落在

\[
\boxed{C_p(k)=\{j_p,j_p+1\}.}
\]

剩余危险是跨 shell 累积：许多不同 least-prime shells 可能都下降到同一个 lower root scale，使递归求和仍然承担很大的重数。

下面的定理排除了这种情况。

---

## 2. L051 — lower-band root-target 重叠至多为 2

状态：`PROVED`。

令

\[
\mathcal P_L(k)
=\{p\le k:p\text{ 为素数且 }p^2<2k\}.
\]

对每个 `p in P_L(k)` 定义上述 `j_p` 与 `C_p(k)`。

则任意整数 root index `t` 最多属于两个 candidate pairs：

\[
\boxed{
\#\{p\in\mathcal P_L(k):t\in C_p(k)\}
\le2.
}
\]

该上界是 sharp 的：在 `k=5` 时，target root `3` 同时属于 `p=2` 与 `p=3` 的 candidate pair。

证明先给出一个更强的 endpoint-separation 结论。

---

## 3. 更强形式：每隔一条 shell，base roots 至少相差 2

取三枚不同 lower-band primes

\[
p<q<r.
\]

则

\[
\boxed{j_p\ge j_r+2.}
\]

这才是真正的 packing 定理，L051 是它的直接推论。

记

\[
u=j_r.
\]

由定义

\[
u^2
\le
\left\lfloor\frac{k^2}{r}\right\rfloor,
\]

于是

\[
\boxed{ru^2\le k^2.}
\]

关键是先证明 `u` 已经至少等于 `r`。

---

## 4. lower-band 自放大：u >= r

由于有三枚不同素数且最后一枚是 `r`，必有

\[
r\ge5.
\]

lower-band 条件给出

\[
r^2<2k.
\]

平方后

\[
r^4<4k^2.
\]

因为 `r>=5`，

\[
4r^3<r^4.
\]

所以

\[
4r^3<4k^2,
\]

从而

\[
r^3<k^2.
\]

特别地

\[
r^2
\le
\left\lfloor\frac{k^2}{r}\right\rfloor.
\]

取整数平方根得到

\[
\boxed{u=j_r\ge r.}
\]

这个初等不等式把“素数间距”转化成了“root-scale 间距”。

---

## 5. 一般素数间距情形

除特殊三元组

\[
(p,q,r)=(2,3,5)
\]

之外，总有

\[
\boxed{r-p\ge4.}
\]

因为：

- 若 `p>=3`，三枚素数都是奇数，相邻素数差至少为 `2`；
- 若 `p=2` 且不是 `(2,3,5)`，则 `r>=7`。

结合 `u>=r`，得到

\[
p\le r-4\le u-4.
\]

比较两个平方阈值：

\[
\begin{aligned}
ru^2-p(u+2)^2
&=(r-p)u^2-4pu-4p\\
&\ge4u^2-4p(u+1).
\end{aligned}
\]

又由 `p<=u-4`，

\[
p(u+1)
\le
(u-4)(u+1)
=u^2-3u-4.
\]

因此

\[
ru^2-p(u+2)^2
\ge12u+16>0.
\]

故

\[
\boxed{p(u+2)^2<ru^2\le k^2.}
\]

于是

\[
(u+2)^2
\le
\left\lfloor\frac{k^2}{p}\right\rfloor,
\]

从而

\[
\boxed{j_p\ge u+2=j_r+2.}
\]

---

## 6. 特殊三元组 (2,3,5)

只剩

\[
p=2,
\qquad r=5.
\]

第 4 节已给出

\[
u=j_5\ge5.
\]

对 `u>=5`，

\[
5u^2-2(u+2)^2
=3u^2-8u-8.
\]

因为 `u>=5`，

\[
3u^2\ge15u,
\]

所以

\[
3u^2-8u-8
\ge7u-8>0.
\]

故仍有

\[
2(u+2)^2<5u^2\le k^2,
\]

因而

\[
\boxed{j_2\ge j_5+2.}
\]

所以更强的三 shell separation 在所有情况下都成立。

---

## 7. 推出 multiplicity bound

反设同一 root index `t` 同时属于三枚素数

\[
p<q<r
\]

对应的 candidate pairs。

则

\[
t\in\{j_p,j_p+1\}
\quad\text{且}\quad
 t\in\{j_r,j_r+1\}.
\]

于是 `j_p` 和 `j_r` 都属于

\[
\{t-1,t\},
\]

所以

\[
j_p-j_r\le1.
\]

但第 3–6 节已经证明

\[
j_p\ge j_r+2,
\]

矛盾。

因此

\[
\boxed{
\#\{p\in\mathcal P_L(k):t\in\{j_p,j_p+1\}\}
\le2.
}
\]

∎

---

## 8. L051 对 lower-band recursion 的改变

T110–T112 给出单 shell 内部的**纵向**结构：

\[
\text{factor extraction}
\longrightarrow
\text{严格更低的 root scale}.
\]

L051 补上跨 shell 的**横向**结构：

\[
\boxed{
\text{一个 lower target root scale}
\longleftarrow
\text{至多两条 lower-band least-prime shells}.
}
\]

这与“对所有小素数分别做一次递归然后全部相加”在结构上已经不同。

它提示 lower-band recursion 应当按下降后的 root scale 重索引，而不是继续按原始 least prime 重索引。

不过 L051 本身仍然不是有用的 composite-mass bound。若把每个精确 cofactor subwindow 粗暴替换成整个 target square basin，上界会远大于原始 `2k` 盆地。必须继续保留精确 quotient subwindows 和 roughness / least-factor 条件。

---

## 9. 与 T113 threshold coherence 的关系

P018-T113 把每条 shell 的 candidate pair 进一步压成精确单阈值响应。

对盆地 offset

\[
n=k^2+s,
\]

有

\[
R_2\!\left(\left\lfloor\frac np\right\rfloor\right)
=j_p+\mathbf1[s\ge\tau_p].
\]

L051 说明：即便不使用这个 threshold bit，一个 target root 也最多只有两条 lower-band shell channels。

因此 T113 只会逐状态进一步减少实际 channel 数量。

正确使用顺序是：

1. L051 给出统一跨 shell packing bound；
2. T113 用单个 basin-offset threshold 选择实际 branch；
3. 下降后的 root 再通过 L001 约束下一 least factor。

---

## 10. 与 mirror certificate 的关系

对中心 `M=k(k+1)` 的 mirror radius `rho`，两侧相对于 `k^2` 的 offsets 为

\[
s_-=k-\rho,
\qquad
s_+=k+\rho.
\]

T113 将每个 least-factor root branch 变成 radius half-interval 条件，而现有 mirror 路线已经有 CRT progressions 与 transverse-support separation。

L051 再提供一个全局限制：对任意下降后的 root cutoff，最多只有两条 lower-band least-prime shell channels 可以输入该尺度。

三者组合自然形成 **least-factor-gated mirror capacity** 的候选结构。应优先压力测试这一组合，而不是继续增加无结构的 mirror moments。

---

## 11. 可执行核验

`src/enterprise_math/p017_lower_band.py` 提供：

- `lower_band_primes`；
- `lower_band_base_root`；
- `lower_band_candidate_roots`；
- `lower_band_root_channels`；
- `lower_band_root_overlap_bound`。

`tests/test_p017_lower_band.py` 检查：

- lower-band 定义与 candidate roots；
- 稠密有限范围内 multiplicity-two 定理；
- 更大根直到 `k=200000` 的三 shell endpoint separation；
- sharp 的首个双重重叠 witness：`k=5`、target root `3`、shells `2` 与 `3`。

有限测试用于审计实现；证明是上面的纯整数论证。

---

## 12. 下一目标

下一步必须保留**精确 subwindow geometry**。

真正有用的递归不等式应联合：

- T110/T112 strict root descent；
- T113 exact branch thresholds；
- L051 至多二重的跨 shell target multiplicity；
- 精确 cofactor-window endpoints 与 p-rough 条件；
- 必要时叠加 mirror CRT / least-factor gating。

如果最终只是换坐标后的普通 Buchstab bookkeeping，就应降级；目标是得到真正更小的 lower-band composite-capacity bound，而不是再做一次精确重索引。
