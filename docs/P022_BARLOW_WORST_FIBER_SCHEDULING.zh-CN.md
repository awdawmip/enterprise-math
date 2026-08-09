# P022 — 最大检查点 Fiber 的精确 Minimax 调度

状态：`ACTIVE RESEARCH NOTE / EXACT INTEGER OPTIMIZATION / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：Barlow selected-layer fiber 因子化；P011 collision spectrum

## 1. 第三个调度目标

最终层被观察时，正 segment lengths 满足

\[
\ell_1+\cdots+\ell_m=N,
\qquad \ell_j\ge1.
\]

普通 near-uniform spacing 已精确优化：

- observation image size；
- pair collision `J_2`。

但未来语言还可能关心最坏未分辨歧义：

\[
\boxed{M_{\max}(O)=\max_y|O^{-1}(y)|.}
\]

若最大 fiber 为 `M`，则全部

\[
J_k=0\qquad(k>M).
\]

所以最小化 `M_max` 等价于尽可能提前完整 collision spectrum 的零尾。该目标的最优 schedule 并非普通等距。

## 2. Segment 代价

长度 `ell` 的 segment 最大 binomial fiber 为

\[
\boxed{C_\ell=\binom{\ell}{\lfloor\ell/2\rfloor}.}
\]

独立 segments 给出

\[
\boxed{M_{\max}=\prod_jC_{\ell_j}.}
\]

## 3. P022-WF01 — 两类精确边际代价

奇数长度到下一个偶数长度永远满足

\[
\boxed{
\frac{C_{2j+2}}{C_{2j+1}}=2.
}
\]

而奇数长度增加两个单位：

\[
\boxed{
\frac{C_{2j+1}}{C_{2j-1}}
=
4-\frac{2}{j+1}.
}
\]

该 two-unit packet 代价严格随 `j` 增长，并永远小于 4。

所以把两个独立的 odd→even 单位增量放到不同 segments 上需要因子 `4`；把同样两个单位合成一个 odd→odd pair packet，代价严格更低。

## 4. P022-WF02 — 最优解至多含一个偶数 segment

若两个 segments 同时为偶数，各减 1 会把目标除以 `2*2=4`。把释放的两个单位作为一个 pair packet 加到某个奇数 segment 上，乘数严格小于 4，于是总目标严格下降。

因此任何 minimizer 至多有一个偶数 segment。

## 5. P022-WF03 — pair packets 必须尽可能均匀

从全部长度 1 出发，额外单位数为

\[
E=N-m.
\]

令

\[
P=\lfloor E/2\rfloor
\]

为 two-unit packets 数。某个 segment 已拥有 `p` 个 packet 时，下一个 packet 的边际因子严格随 `p` 增长。

所以若两个 segments 的 packet 数相差至少 2，把一个 packet 从更重的 segment 移向更轻的 segment 会严格降低乘积。

写

\[
P=qm+r,
\qquad0\le r<m.
\]

则 `m-r` 个 segments 获得 `q` 个 packets，`r` 个 segments 获得 `q+1` 个 packets。

## 6. P022-WF04 — 闭式 minimax 值

令

\[
e=E\bmod2\in\{0,1\}.
\]

pair-balanced 的两类奇数长度为

\[
2q+1,\qquad2q+3.
\]

若 `e=1`，唯一剩余单位可放到任一奇数 segment 上，目标都只额外乘 2。

因此

\[
\boxed{
M_{\min}(N,m)
=
2^e
\binom{2q+1}{q}^{m-r}
\binom{2q+3}{q+1}^{r}.
}
\]

相应 segment family 可称为 **odd-balanced / pair-balanced**：先均匀分配 two-unit packets，再至多留下一个 single unit。

## 7. 与普通 balanced spacing 的冲突

最小例子

\[
N=4,\qquad m=2.
\]

普通 balanced：

\[
(2,2),\qquad M_{\max}=4.
\]

pair-balanced：

\[
(1,3),\qquad M_{\max}=3.
\]

这正解释了高阶 collision note 中的差异：`(2,2)` 的 `J_2` 更小，但 `(1,3)` 已经使 `J_4=0`。

对所有 `m>=2,N=m+2`，pair-balanced 都是

\[
(3,1,\ldots,1)
\]

并有

\[
M_{\min}=3.
\]

因此该冲突是一整个无限族。

## 8. Collision cutoff

定义

\[
K_0=M_{\max}+1.
\]

则

\[
\boxed{J_k=0\quad(k\ge K_0).}
\]

故 pair-balanced 精确解决的是

\[
\boxed{
\text{最小化最高可能非零 collision order}.
}
\]

这与 image capacity 或 pair ambiguity 是不同目标。

## 9. 精度结论

| 未来统计 | 精确最优调度 |
|---|---|
| image size | 普通 balanced lengths |
| `J_2` | 普通 balanced lengths |
| maximum fiber / collision cutoff | odd-balanced pair packets |

所以固定 checkpoint 数量以后，precision 仍然不是 checkpoint density；segment 的奇偶结构与排布必须由未来统计决定。

## 10. 验证

- `src/enterprise_math/p022_barlow_worst_fiber_scheduling.py`；
- `tests/test_p022_barlow_worst_fiber_scheduling.py`。

独立穷举已覆盖所有 `N<=17,m<=7` 的正整数 compositions，闭式 minimax 值无反例。