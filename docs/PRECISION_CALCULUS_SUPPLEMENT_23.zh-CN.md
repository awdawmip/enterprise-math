# 精度演算 — 补充 23

状态：`ACTIVE RESEARCH NOTE`  
范围：T182 二盆地像内部的精确单阈值响应，以及多个 quotient divisor 之间的共享 offset coherence  
依赖：P018-T182/T195/T196、T007 整数根、P007 离散除法  
纪律：阈值比较和 floor division 序关系属于成熟初等算术。项目专门内容，是平方盆地上的精确响应律，以及把它作为后续跨尺度论证中的共同 offset coherence 层。

> **并发编号纠偏。** 本文由并发 QuotientBasin 路线以临时编号 `Supplement 14 / T113` 合入 `main`，而 PR #68 此前已经存在并验证了更早的 T113。集成分支保留旧编号，只把这条后来的并发定理重标为 **Supplement 23 / T197**。其中临时 T110/T111/T112 同时对应迁移为 T182/T195/T196。

## 1. 二盆地陈述还缺少什么

T182 已证明：若

\[
k^2\le n<(k+1)^2,
\qquad d\ge2,
\]

并定义

\[
j_d=R_2\!\left(\left\lfloor\frac{k^2}{d}\right\rfloor\right),
\]

则 quotient root 只能是

\[
j_d\quad\text{或}\quad j_d+1.
\]

但这还没有说明两个值究竟在什么位置切换。这个切换实际上是精确的，而且只发生一次。

---

## 2. P018-T197 — 精确 quotient-root 切换阈值

状态：`PROVED`，并已进入 Lean 形式化。

在 T182 条件下，

\[
\boxed{
R_2\!\left(\left\lfloor\frac nd\right\rfloor\right)=j_d+1
\iff
d(j_d+1)^2\le n.
}
\]

等价地说，在到达这个 state threshold 之前，root 恰好处于下侧分支。

### 证明

T182 已把 quotient root 限定在 `j_d` 或 `j_d+1`。达到上侧值，当且仅当

\[
(j_d+1)^2\le\left\lfloor\frac nd\right\rfloor.
\]

利用自然数 floor division 的精确序伴随关系，这又等价于

\[
d(j_d+1)^2\le n.
\]

没有使用任何近似。∎

Lean 定理为 `EnterpriseMath.Precision.square_basin_div_upper_root_iff`。

---

## 3. Offset 形式

写

\[
n=k^2+s,
\qquad0\le s\le2k.
\]

定义正 offset threshold

\[
\boxed{
\tau_d=d(j_d+1)^2-k^2.
}
\]

则 T197 等价于

\[
\boxed{
R_2\!\left(\left\lfloor\frac{k^2+s}{d}\right\rfloor\right)
=j_d+\mathbf1[s\ge\tau_d].
}
\]

若 `tau_d>2k`，整个盆地都不会进入上侧分支。因此 quotient-root response 在有限 basin offset 上就是一个真正的单跳变阶跃函数。

---

## 4. 多个 divisor 的共享 offset coherence

固定

\[
d_1,\ldots,d_h\ge2.
\]

对每个 `d_i` 定义 T197 上侧 bit

\[
\varepsilon_i(s)=\mathbf1[s\ge\tau_{d_i}].
\]

所有坐标都由**同一个** offset `s` 驱动，所以

\[
\boxed{
\varepsilon(s)=(\varepsilon_1(s),\ldots,\varepsilon_h(s))
}
\]

并不是 `{0,1}^h` 中任意独立的 bit 组合。

随着 `s` 增加，每个坐标只会在跨过自身 threshold 时翻转一次。把 distinct thresholds 排序后，向量只会在这些位置变化，因此

\[
\boxed{
\#\{\varepsilon(s):0\le s\le2k\}\le h+1.
}
\]

朴素独立 bit 计数则会给出 `2^h`。

它与 T195 从不同方向加强结构：

- T195 说明固定总除数时，最终 quotient state 与因式分解路径无关；
- T197 说明即使同时观察多个 divisor 的 root branch bits，它们也被一个共同 state coordinate 约束。

---

## 5. 整除条件与大模数相变

若 divisor `D` 实际整除

\[
n=k^2+s,
\]

则

\[
\boxed{s\equiv-k^2\pmod D.}
\]

当 `D>2k` 时，允许 offset 区间长度只有 `2k+1`，因此满足该同余的正 interior offset 至多一个。

这只是 P017 已使用的大模数唯一命中现象在下平方边界坐标中的表达。T197 不建立新的竞争性 large-hit 机制，而是给同一有限 state 增加 exact root-response coordinate。

---

## 6. Mirror 坐标

对

\[
M=k(k+1),
\qquad M-r,\ M+r,
\qquad1\le r<k,
\]

相对于 `k^2` 的 offsets 是

\[
\boxed{s_-=k-r,\qquad s_+=k+r.}
\]

下侧 divisor `p` 的 T197 upper-root bit 为

\[
\boxed{
\varepsilon_p^-(r)=\mathbf1[k-r\ge\tau_p]=\mathbf1[r\le k-\tau_p].
}
\]

上侧 divisor `q` 则为

\[
\boxed{
\varepsilon_q^+(r)=\mathbf1[k+r\ge\tau_q]=\mathbf1[r\ge\tau_q-k].
}
\]

所以 quotient-root branch selection 变成一个**有界 radius 半区间条件**，可以与现有 mirror CRT progression 直接求交。

---

## 7. 对 P017 lower band 的解释

若

\[
n=pq
\]

且 `p` 是平方盆地 composite 的最小素因子，T182/T195/T196 已说明 cofactor root 下降并且 quotient factorization 不产生指数级分支；T197 再给出精确 branch selector：

\[
R_2(q)=j_p+\mathbf1[n\ge p(j_p+1)^2].
\]

如果 `q` 仍为 composite，其下一最小素因子就被这个 exact descended root 截断。因此下一因子 cutoff 不必总取粗糙 `j_p+1`，可以由一次整数 threshold comparison 逐状态确定为 `j_p` 或 `j_p+1`。

---

## 8. 可执行核验

Python 层新增：

- `quotient_root_threshold`；
- `square_basin_offset_root_response`；
- `quotient_root_threshold_pattern`。

测试检查：

- threshold 始终高于下平方边界；
- root response 精确等于 `base_root + 1[offset>=tau]`；
- threshold 既可能落在 basin 内，也可能位于 basin 外；
- 对固定 `h` 个 divisors，实际 bit-vector family 大小至多 `h+1`。

Lean 层形式化 exact upper-branch equivalence；有限 bit-vector pattern 目前保留在文档/参考测试层，除非后续证明需要 typed finite-set theorem。

---

## 9. 下一目标

T182/T195/T196/T197 已经把当前 lower-band 路线需要的 quotient transport 几何压得足够紧：

- 严格下降；
- 无因式分解路径爆炸；
- 精确单阈值 branch response；
- 共享 offset coherence。

所以下一个真正有用的定理应当是**跨 shell**，而不是继续增加 quotient identity。

当前最强 P017 候选是 lower-band root-target overlap bound：在满足 `p^2<2k` 的 least primes 中，每个 descended root index 最多只出现在两个不同 least-prime shells 的 T182 candidate pair 中。

若能证明，每个 lower square-root scale 只接收常数个 shell channels，这正是递归 composite-mass 论证所需要的结构类型。
