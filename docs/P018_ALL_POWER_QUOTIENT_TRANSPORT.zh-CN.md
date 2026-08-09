# P018 —— 任意幂商映射盆地运输

状态：`ACTIVE RESEARCH NOTE`  
范围：把平方盆地的商映射运输定理推广到任意正整数根指数  
依赖：整数根盆地语义、精确整数除法，以及 P018 已有平方盆地运输  
纪律：证明只使用初等整数序关系，不对这些基础不等式主张优先权；项目特有价值在于有限精度/根盆地的组织方式及其作为可复用运输引理的用途。

## 1. 问题

当前 P018 的 quotient-basin 定理以平方盆地表述。同一个结构问题对任意正整数根指数都存在。

固定

\[
p\ge1,\qquad k\ge1,\qquad d\ge2,
\]

以及规范 `p` 次根盆地

\[
B_{p,k}=\{n\in\mathbb N:k^p\le n<(k+1)^p\}.
\]

记

\[
q_0=\left\lfloor\frac{k^p}{d}\right\rfloor,
\qquad
j=R_p(q_0).
\]

商映射像 `Q_d(B_{p,k})` 最多会穿过多少个 `p` 次根盆地？

## 2. P018-APQ-T01 —— 任意幂两盆地商映射定理

状态：`PROVED`。

对任意

\[
n\in B_{p,k},
\]

都有

\[
\boxed{
R_p\!\left(\left\lfloor\frac nd\right\rfloor\right)
\in\{j,j+1\}
}
\]

并且

\[
\boxed{j<k.}
\]

因此，任意非平凡 floor quotient 都会把一个完整的 `p` 次根盆地送入至多两个相邻的 `p` 次根盆地。已有平方定理就是 `p=2` 的特例。

### 证明

由于 `d>=2`，

\[
\left\lfloor\frac{k^p}{d}\right\rfloor<k^p,
\]

所以

\[
j<k.
\]

下界由单调性直接得到：

\[
\left\lfloor\frac{k^p}{d}\right\rfloor
\le
\left\lfloor\frac nd\right\rfloor,
\]

因此

\[
j\le R_p\!\left(\left\lfloor\frac nd\right\rfloor\right).
\]

根据 `j` 的根盆地刻画，

\[
\left\lfloor\frac{k^p}{d}\right\rfloor<(j+1)^p,
\]

于是

\[
\boxed{k^p<d(j+1)^p.}
\]

由于 `j<k`，整数序立即给出

\[
j+1\le k.
\]

因此

\[
(k+1)(j+1)\le k(j+2),
\]

因为右端减左端正好是 `k-j-1>=0`。对两边取正整数次幂 `p`：

\[
(k+1)^p(j+1)^p\le k^p(j+2)^p.
\]

再与 `k^p<d(j+1)^p` 合并，得到

\[
(k+1)^p(j+1)^p
<d(j+1)^p(j+2)^p.
\]

由于 `(j+1)^p>0`，约去该正整数因子：

\[
\boxed{(k+1)^p<d(j+2)^p.}
\]

对 `n<(k+1)^p`，遂有

\[
\left\lfloor\frac nd\right\rfloor<(j+2)^p,
\]

故其 `p` 次根指标严格小于 `j+2`。与前述下界结合，只可能是 `j` 或 `j+1`。∎

整个证明没有使用实数根或实数比例。

## 3. P018-APQ-T02 —— 精确分裂判据

状态：`PROVED`。

令

\[
q_{\max}
=
\left\lfloor
\frac{(k+1)^p-1}{d}
\right\rfloor.
\]

上方目标根 `j+1` 确实被商映射像取到，当且仅当

\[
\boxed{
d(j+1)^p\le (k+1)^p-1.}
\]

等价地，

\[
\boxed{
R_p(q_{\max})=j+1
\iff
d(j+1)^p\le (k+1)^p-1.
}
\]

### 证明

上分支出现恰好等价于

\[
q_{\max}\ge(j+1)^p.
\]

对于正整数 `d`，这又等价于

\[
(k+1)^p-1\ge d(j+1)^p.
\]

两盆地定理已经排除了任何更大的根指标。∎

所以，在 `p,k,d` 已知时，整个盆地运输只需一个精确二值分支位即可概括。

## 4. 商映射路径扁平性仍然成立

对任意有限个正整数除数

\[
d_1,\ldots,d_h,
\]

普通欧几里得除法给出

\[
Q_{d_h}\circ\cdots\circ Q_{d_1}=Q_D,
\qquad
D=\prod_i d_i.
\]

因此 APQ-T01 只需对总除数 `D` 使用一次：

\[
\boxed{
R_p(Q_D(n))\in\{j_D,j_D+1\},
\qquad
j_D=R_p(Q_D(k^p)).
}
\]

重复 quotient 步骤不会制造指数增长的最终 `p` 次根指标分支。这就是已有平方根 path-flatness 结论的任意幂版本。

不同分解方式下的中间 quotient 状态仍然可以不同；如果所用操作并不只是同一个乘积除数的因子分解，阶段顺序也可能有意义。本结论只针对由总乘积除数精确表示的最终 quotient。

## 5. 有限精度解释

这个定理把信息分成三个层次：

1. 粗源根指标 `k`；
2. 可由 `k,p,d` 直接计算的基础目标指标 `j=R_p(k^p//d)`；
3. 至多一个附加 bit，用来决定实际目标是 `j` 还是 `j+1`。

这**不**表示完整 quotient 状态可以由一个 bit 恢复。它只表示：在每个源根盆地内部，最终 `p` 次根盆地这一观察量只剩二值残余不确定性。

若结合 P023 的 future-compatible quotient 机制，则

\[
(k,\,R_p(Q_d(n)))
\]

正是针对这一特定未来根观察量，对源根盆地观察的最粗一步修复。APQ-T01 说明附加标签至多是二值；APQ-T02 精确判断它何时真正非平凡。

## 6. 与平方结果的关系

当 `p=2` 时，APQ-T01 就退化为 P018 已有的两平方盆地运输定理。一般证明显示，该机制并不依赖特殊的勾股或二次结构。真正需要的是：

- 精确完全幂盆地边界；
- 非平凡整数除法；
- 序关系 `j<k`；
- 初等交叉乘法不等式
  \[
  (k+1)(j+1)\le k(j+2).
  \]

平方情形仍然很重要，因为当前 P017 围绕相邻平方组织；但运输规律本身属于更一般的整数根层。

## 7. 可执行验证

`src/enterprise_math/p018_power_basin.py` 实现：

- `power_basin_quotient_window`；
- `power_basin_quotient_transport`；
- `iterated_power_basin_quotient_transport`。

`tests/test_p018_power_basin.py` 在较宽的有限指数、盆地指标和除数网格上检查两盆地界、精确分裂条件、小盆地逐状态运输以及 quotient-path flattening。这些测试用于审计实现；上面的证明才是数学依据。

## 8. 下一问题

下一步不应再复制同一条两盆地定理。更有价值的是两个方向：

1. 刻画整个源盆地的**实际**目标 `p` 次根何时必然严格小于 `k`，其精确条件等价于
   \[
   (k+1)^p\le d k^p;
   \]
2. 把 APQ-T01 与 operation-safe precision selection 组合，判断给定 quotient/collapse 运算族究竟必须保留哪些根盆地区分。

后续结果仍须保持纯整数；如果只是换一种方式重述标准 quotient 恒等式，应当降格而不是继续扩张。
