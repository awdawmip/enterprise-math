# P025 补充 71 —— Projective Failure 的 Complement-Capacity 分层

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 51、64、70  
Hard block：`NONE`

## 1. Stage 64 擦掉了一个仍然精确的增益坐标

对一个 active cyclic projective term，记 active component 为 `n_i`，两个 complements 为 `n_j,n_k`。

令

\[
R_i=\operatorname{rad}(n_i),\qquad C_i=C(n_i).
\]

active term 为

\[
\rho_i=\frac{m_i}{R_kC_j+R_jC_k}.
\]

Stage 64 只使用 `C_j,C_k>=1` 来生成 pair-radical state；完整 denominator 其实保留了更强的 orientation-dependent capacity coordinate。

## 2. P025-T140 —— 双 complement-capacity pair bounds

固定整数 threshold

\[
T\ge1
\]

并假设

\[
\rho_i\ge T.
\]

则

\[
m_i\ge T(R_kC_j+R_jC_k).
\]

分别保留两个 summands：

\[
m_i\ge TR_kC_j,
\qquad
m_i\ge TR_jC_k.
\]

由 `m_i=n_i/R_i` 精确得到

\[
\boxed{R_iR_k\le\frac{n_i}{TC_j},}
\]

以及

\[
\boxed{R_iR_j\le\frac{n_i}{TC_k}.}
\]

也就是说，每一个 complement capacity 都控制着“active component + 另一个 complement”的 pair radical。

## 3. P025-C16 —— 至少一个 pair 获得最大 complement capacity 的全部增益

定义

\[
\boxed{H_i=\max\{C_j,C_k\}.}
\]

若 `C_j>=C_k`，就使用第一条不等式与 pair `(i,k)`；反之使用 `(i,j)`。因此总存在某个 complement `ell` 使

\[
\boxed{
\operatorname{rad}(n_in_\ell)=R_iR_\ell
\le\frac{n_i}{TH_i}
\le\frac{c}{TH_i}.
}
\]

这就是 generic Stage-64 pair-radical compiler 的 exact capacity-stratified refinement。

Stage 64 等价于擦掉 `H_i`，只留下 `H_i>=1`。

Stage 70 则是一个 specialization：当某 complement 是 squarefree side `s` 时，`C(s)=s'` 给 `H_i` 一个显式下界。

## 4. 高容量 branch

对任意声明的 capacity floor

\[
H\ge1,
\]

若某个 threshold-active orientation 满足

\[
H_i\ge H,
\]

则会生成 pair product radical bound

\[
\boxed{\operatorname{rad}(n_in_\ell)\le\frac{c}{TH}.}
\]

因此 Stage 64 可用的任何外部 pair-product radical count，都可以把原 threshold `T` 强化成 `TH`。

在 Stage 64 导入的同一个 de Bruijn 使用范围内，得到 capacity-stratified scale

\[
\boxed{
N_X(\sigma_{\rm proj}\ge T,\ H_{\rm active}\ge H)
\ll_\varepsilon\frac{X^{1+\varepsilon}}{TH}.
}
\]

这里 `H_active` 表示至少存在一个 threshold-active cyclic orientation 满足 `H_i>=H`。

渐近计数依赖外部 prior theorem；P025-T140/C16 才是项目内部 exact arithmetic compiler。

## 5. 低容量 branch 与 Stage 51 精确闭环

互补情形并不是一个无结构 remainder。

若 active orientation 满足

\[
H_i<H_0
\]

其中 `H_0>=2` 为固定整数 cutoff，则

\[
C_j,C_k\le H_0-1.
\]

Stage 51 可以分别作用于两个 complement blocks。

每个 complement `n` 都满足

\[
\boxed{
C(n)\le H_0-1
\Longrightarrow
\begin{cases}
n=p^e,\ 1\le e\le H_0-1, &\text{prime-power branch};\\
n\mid Q_{H_0-1}, &\text{finite non-prime-power branch}.
\end{cases}}
\]

因此一个 low-complement-capacity active orientation 会让**两个 complements 同时刚性化**。

唯一无限低容量部分就是 bounded-exponent prime-power pairs，其余全部进入只依赖 cutoff 的 finite core。

## 6. P025-C17 —— cutoff 5 给出有限指数 atom family

Stage 51 已证明

\[
C(n)<5\Longrightarrow n=p^e,
\qquad e\in\{1,2,3,4\}.
\]

所以

\[
\boxed{
H_i<5
\Longrightarrow
n_j=p^e,\quad n_k=q^f,
\quad e,f\in\{1,2,3,4\}.
}
\]

一旦两个 complements 选定，active component 由 additive relation 唯一决定。

因此 threshold-active universe 被精确分流为

\[
\boxed{
\text{high complement capacity}
\quad\cup\quad
\text{bounded-exponent prime-power atoms / finite core}.
}
\]

而 cutoff 5 时 finite core 完全消失。

## 7. 精确样本

### `3+125=128`, `T=4`

active term 为 c-oriented。complement capacities 是

\[
C(3)=1,\qquad C(125)=3,
\]

所以

\[
H_c=3<5.
\]

两个 complements 恰是 Stage-51 atoms

\[
3=3^1,\qquad125=5^3.
\]

较大的 capacity `3` 控制 pair `(128,3)`：

\[
\operatorname{rad}(128\cdot3)=6,
\]

且

\[
4\cdot3\cdot6=72\le128.
\]

### `10+2187=2197`, `T=6`

active term 为 b-oriented，complement capacities 为

\[
C(10)=7,\qquad C(2197)=3.
\]

故

\[
H_b=7.
\]

较大的 `C(10)=7` 控制 pair `(2187,2197)`：

\[
\operatorname{rad}(2187\cdot2197)=39,
\]

并且

\[
6\cdot7\cdot39=1638\le2187.
\]

这从一般 dual-capacity formula 中自动恢复了 Stage 70 的 derivative gain。

## 8. 精度架构后果

Stage 71 给出一个 adaptive theorem-native routing state：

\[
\boxed{\text{active cyclic index}+H_i.}
\]

它对应两条完全不同的 downstream path：

- `H_i` 大：擦除绝大多数 factor data，只把 strengthened pair-radical state 交给外部 counting theorem；
- `H_i` 小：停止 generic counting，转而进入 Stage 51 的 finite-core / bounded-exponent prime-power atlas。

这是一个明确的 **precision-dependent algorithm selection**：同一个 scalar capacity coordinate 决定下一任务应该选择哪种最省信息的表示。

## 9. Prior-art / ownership 边界

Stage 51 low-capacity rigidity 是已有 P025 WIP；de Bruijn radical counting 属于 external prior art；P025-T140 的代数是初等的。

项目侧结果是把这些对象精确组合成 projective observable 的 high-capacity-count / low-capacity-rigidity dichotomy。历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

若提升为 generic query routing/minimal repair，则母层应归 A2/P023。

## 10. 可执行资产

新增：

- `src/enterprise_math/abc_projective_capacity_stratified.py`；
- `tests/test_abc_projective_capacity_stratified.py`。

## 11. 下一前沿

Hard block 不存在。继续：

1. 研究 cutoff-five atom families `p^e +/- q^f`, `e,f<=4`，判断哪些真正能支持 `sigma_proj>=1` 或更高 threshold；
2. 只有确认 imported de Bruijn bound 的 uniformity 后，才让 capacity floor 随 `X` 移动；
3. 将 capacity split 与 Stage 68 adaptive precision budget 合并；
4. 把 `large coordinate -> coarse theorem-native count; small coordinate -> rigid structural refinement` Relay 给 A2/P023。
