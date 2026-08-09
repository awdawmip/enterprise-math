# 精度演算 — 补充 20

状态：`ACTIVE RESEARCH NOTE`  
范围：一个完整平方 collapse basin 经过整数向下取整除法后的精确运输  
依赖：T007 整数根、P007 离散除法，以及截至 T109 的规范 P018 response/transport 层  
纪律：本文完全有限且只使用整数。`Nat.nthRoot` 与向下取整除法是成熟形式化工具；项目研究的问题，是把两者作用在平方盆地上后出现的精确兼容结构。

> **并发编号纠偏。** 本文由另一条并发 P018 路线以临时编号 `Supplement 12 / T110` 合入 `main`。PR #68 在此前已经形成并验证了连续的 `T110–T181` 序列。为了完整保留两条路线、同时消除 theorem identifier 冲突，本次集成只把这篇较晚进入 main 的并发研究重标为 **Supplement 20 / T182**；数学内容不变。

## 1. 动机

勒让德压力测试中反复出现同一种操作：

1. 从一个平方 collapse basin 中取状态；
2. 提取一个整数因子或除以一个整数；
3. 询问 quotient 会落在哪一个平方根尺度。

最初这看起来像 P017 中关于素因子 cofactor 的特殊事实。进一步推演后发现，素数条件完全不需要；这个现象应当回到精度演算本身。

令

\[
B_k=[k^2,(k+1)^2)\cap\mathbb N.
\]

对整数除数 `d>=2`，考虑向下取整 quotient projection

\[
Q_d(n)=\left\lfloor\frac nd\right\rfloor.
\]

核心问题是：`Q_d(B_k)` 最多会碰到多少个平方 collapse basins？

---

## 2. 基准 quotient root

定义

\[
m=\left\lfloor\frac{k^2}{d}\right\rfloor,
\qquad
j=R_2(m).
\]

于是

\[
j^2\le m<(j+1)^2.
\]

因为 `d>=2` 且 `k>0`，

\[
m<k^2,
\]

所以立刻得到

\[
\boxed{j<k.}
\]

也就是说，整数除法会严格降低基准平方根尺度。

---

## 3. 一个 quotient 辅助不等式

令

\[
a=\left\lfloor\frac kd\right\rfloor.
\]

则

\[
a^2\le\left\lfloor\frac{k^2}{d}\right\rfloor=m.
\]

理由是

\[
ad\le k,
\]

因此

\[
a^2d
\le ak
\le k^2,
\]

再利用 floor division 的序关系即可得到 `a^2<=k^2/d`。

所以

\[
a\le j.
\]

这个很小的不等式，正是 Euclidean quotient scale 与 square-root scale 之间的有限耦合点。

---

## 4. P018-T182 — 二盆地 quotient transport

状态：`PROVED`，并已进入 Lean 形式化。

设

\[
k\ge1,
\qquad d\ge2,
\qquad k^2\le n<(k+1)^2.
\]

定义

\[
j=R_2\!\left(\left\lfloor\frac{k^2}{d}\right\rfloor\right).
\]

则

\[
\boxed{
R_2\!\left(\left\lfloor\frac nd\right\rfloor\right)
\in\{j,j+1\}
}
\]

并且

\[
\boxed{j<k.}
\]

等价地说：对任意整数 `d>=2`，floor division 会把一个完整平方 collapse basin 映射到严格更低 root scale 上的至多两个相邻 square-root-index basins。

### 证明

下界直接来自整数除法的单调性：

\[
\left\lfloor\frac{k^2}{d}\right\rfloor
\le
\left\lfloor\frac nd\right\rfloor.
\]

又因为

\[
j^2\le\left\lfloor\frac{k^2}{d}\right\rfloor,
\]

所以

\[
j
\le
R_2\!\left(\left\lfloor\frac nd\right\rfloor\right).
\]

对上界，由 `j` 的定义，

\[
\left\lfloor\frac{k^2}{d}\right\rfloor<(j+1)^2,
\]

故

\[
k^2<d(j+1)^2.
\]

根据第 3 节，

\[
\left\lfloor\frac kd\right\rfloor\le j.
\]

Euclidean division 还给出

\[
k<d\left(\left\lfloor\frac kd\right\rfloor+1\right)
\le d(j+1).
\]

于是

\[
2k<d(2j+3).
\]

将这个不等式与 `k^2<d(j+1)^2` 合并，得到

\[
(k+1)^2\le d(j+2)^2.
\]

又因为 `n<(k+1)^2`，所以

\[
n<d(j+2)^2,
\]

从而

\[
\left\lfloor\frac nd\right\rfloor<(j+2)^2.
\]

因此它的整数平方根严格小于 `j+2`；结合前面的下界，只可能等于 `j` 或 `j+1`。

最后，`d>=2` 给出

\[
\left\lfloor\frac{k^2}{d}\right\rfloor<k^2,
\]

故 `j<k`。∎

---

## 5. 窗口形式

完整平方盆地经过 quotient 后的像恰好是整数区间

\[
Q_d(B_k)
=
\left[
\left\lfloor\frac{k^2}{d}\right\rfloor,
\left\lfloor\frac{(k+1)^2-1}{d}\right\rfloor
\right].
\]

T182 说明其中每个元素的 square-root index 都只能是 `j` 或 `j+1`。

若只看平方盆地内部严格大于 `k^2`、且被 `d` 整除的状态，对应 quotient/cofactor window 为

\[
\left[
\left\lfloor\frac{k^2}{d}\right\rfloor+1,
\left\lfloor\frac{(k+1)^2-1}{d}\right\rfloor
\right].
\]

只要该窗口非空，其中每个 `q` 都满足

\[
\boxed{j^2<q<(j+2)^2.}
\]

这正是 P017 提取 least prime factor 后所需的形式，但定理本身并不依赖 `d` 为素数。

---

## 6. 为什么它强于普通大小估计

粗略关系

\[
Q_d(n)\approx n/d
\]

只能说明除法会降低数值大小。T182 额外说明：

- square-root **index** 严格下降；
- 整个原盆地只有**两个可能的目标 index**；
- 不需要连续近似或实数平方根参与证明；
- 对任意整数 `d>=2` 成立，而不只对素因子成立。

因此，一个平方盆地不会在除法后散射到很多更低平方尺度，而只形成受到严格控制的二盆地像。

---

## 7. 形式化与可执行核验

Python 参考层提供：

- `square_basin_quotient_transport(k,d,n)`；
- `square_basin_quotient_window(k,d)`；
- `open_divisible_cofactor_window(k,d)`。

回归测试会穷举有限范围内的 `k`、`d` 和盆地状态，并明确覆盖真正落到上侧目标 index `j+1` 的情形。

Lean 模块 `EnterpriseMath.Precision.QuotientBasin` 使用以下有限对象形式化 statewise theorem：

- `Nat.nthRoot` 的序刻画；
- 自然数精确 floor division；
- 有限整数不等式。

证明不需要把实数平方根作为隐藏目标。

---

## 8. 对研究架构的影响

T182 改变了 P017 中 lower-band 问题的定位。

lower-band least prime 可能很小，所以直接筛计数仍然困难；但除以这个最小因子以后，quotient 并不是一个任意的小整数区间，而是被限制在两个相邻 square-collapse basins 中，并且基准 root index 严格小于 `k`。

这给出了真正的 root-scale descent：

\[
\boxed{
\text{一个平方盆地}
\xrightarrow{\;\lfloor /d\rfloor\;}
\text{至多两个相邻的更低平方盆地}.
}
\]

因此下一步 P017 应优先检验通过 T182 对 lower band 做递归运输，而不是再引入一套平坦筛法编码。真正的问题变成：反复提取因子并配合二盆地 transport 后，能否形成足够强的良基有限下降，从而控制剩余 lower-band composite mass。
