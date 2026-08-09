# P019 补充 10 —— 一般碰撞幂的 Residue-Shell 层级

状态：`RESEARCH WIP / EXACT INTEGER FACTORIZATION PROVED`

## 1. 问题

Supplement 09 证明平方层 `s=2` 有异常干净的分解：

\[
m\Psi_{m,2}(c)
=c^2+r(m-r),
\qquad r=|c|\bmod m.
\]

因此平方层的 scale mismatch detail 完全有界，与 bulk quotient 无关。

但对 `s>=3`，直接复制“bounded detail”命题是错误的。

本补充给出正确的一般式：所有 collision-power orders 共享同一个 residue gate `r(m-r)`，但从 `s=3` 起其后乘上一个严格低于主 bulk 次数的整数多项式。

## 2. 定义 scaled power defect

对

\[
|c|=mq+r,
\qquad0\le r<m,
\]

定义

\[
\boxed{
D_{m,s}(c)
=
m^{s-1}\Psi_{m,s}(c)-|c|^s.
}
\]

`s=1` 时恒为 0。

对 `s>=2`，`D` 测量把总量 `c` 强制装入 `m` 个整数 slots 时，相对于完全整齐的 homogeneous power scaling 所产生的离散 defect。

## 3. P019-X22 —— 一般 residue-shell 精确分解

对任意整数 `s>=2`：

\[
\boxed{
D_{m,s}(c)
=
r(m-r)
\sum_{j=2}^{s}\binom sj q^{s-j}
\sum_{h=0}^{j-2}r^h m^{s-2-h}.
}
\]

右侧是有限整数和，系数全部非负。

### 证明

由

\[
\Psi_{m,s}(c)
=(m-r)q^s+r(q+1)^s
\]

得到

\[
\frac{D_{m,s}(c)}{m^s}
=
(1-\lambda)q^s
+\lambda(q+1)^s
-(q+\lambda)^s,
\qquad
\lambda=r/m.
\]

不使用极限或导数，只展开二项式：

\[
(1-\lambda)q^s
+\lambda(q+1)^s
-(q+\lambda)^s
=
\sum_{j=2}^s
\binom sj q^{s-j}(\lambda-\lambda^j).
\]

而

\[
\lambda-\lambda^j
=
\lambda(1-\lambda)
\sum_{h=0}^{j-2}\lambda^h.
\]

乘回 `m^s` 即得所述纯整数公式。∎

## 4. 共同 residue gate

X22 立即给出

\[
\boxed{r(m-r)\mid D_{m,s}(c)}
\]

在整数多项式意义下成立。

并且对于 `s>=2`：

\[
\boxed{
D_{m,s}(c)=0
\iff
m\mid c.
}
\]

因为 `0<r<m` 时右侧所有因子均非负，且 `j=s,h=0` 项保证 shell 因子严格正。

所以**所有 collision orders 的离散 defect 都由同一个最基础精度余数 `r=|c| mod m` 打开或关闭。**

这意味着提高 observation order `s` 不需要创造一个新的 precision remainder state；更高阶 defect 仍由同一个 `(q,r)` 生成。

## 5. 低阶展开

### `s=2`

\[
\boxed{D_{m,2}=r(m-r).}
\]

没有 bulk factor，是唯一的完全 bounded-residue 层。

### `s=3`

\[
\boxed{
D_{m,3}
=r(m-r)(3mq+m+r).
}
\]

correction 对 bulk quotient `q` 是一次。

### `s=4`

\[
\boxed{
D_{m,4}
=r(m-r)
\bigl(
6m^2q^2
+4m^2q
+m^2
+4mqr
+mr
+r^2
\bigr).
}
\]

correction 对 `q` 是二次。

所以一般 `s` 的 defect 在主量 `|c|^s` 之外，只达到 `s-2` 阶 bulk。

## 6. P019-X23 —— defect 是严格低阶 shell

固定 block size `m` 与 residue `r`，把 `q` 作为整数 bulk 层级。

由 X22：

\[
D_{m,s}
\]

是 `q` 的次数至多 `s-2` 的多项式，而主 homogeneous term

\[
|c|^s=(mq+r)^s
\]

是 `q` 的 `s` 次。

因此无需连续渐近语言，也可严格说：

> collision-power 的 non-divisibility correction 比主 power bulk 少至少两个离散多项式阶。

平方层 `s=2` 正好退化成 0 次 shell，因此完全有界。

## 7. 与 P018 precision detail 的关系

P018 使用 Euclidean quotient/detail：

\[
|c|=mq+r.
\]

X22 表明：对整个 `Psi_(m,s)` collision-power family，所有 scale mismatch 都不需要新的隐藏数值。

同一个：

`bulk quotient q + precision remainder r`

已经足够重建每个 `s` 的 exact power defect。

因此可把

\[
D_{m,s}(c)
\]

看成由同一个 precision detail `r` 在不同 observation order 下诱导出来的 **residue-shell hierarchy**。

## 8. 与 P011 collision spectrum 的关系

已有恒等式

\[
a^s
=
\sum_{j=1}^s
S(s,j)j!\binom aj
\]

说明 power `s` 读取至多 `s` 阶 collision multiplicity。

本补充进一步说明：即使 observation order 提高，integer balancing 与 block contraction 所产生的 defect 仍由同一个 divisibility remainder 组织，而不是每阶各自产生不相容的 precision state。

所以当前可把两个轴分开：

- `m / (q,r)`：dimension-capacity / precision allocation；
- `s`：collision observation order。

这避免再次把 `s` 误认成物理维度。

## 9. 一个有用的 exact-alignment 判据

对 `s>=2`：

\[
\boxed{
 m^{s-1}\Psi_{m,s}(c)=|c|^s
\iff m\mid c.
}
\]

即只有当总量能均匀分入全部 slots 时，contracted power energy 与 homogeneous power bulk 完全一致。

因此 `D_(m,s)>0` 可以作为一个纯整数 **precision-allocation mismatch witness**。

它不是物理能量结论，只是当前数学工具。

## 10. 实现与验证

`src/enterprise_math/dimension_contraction.py` 新增：

- `balanced_power_defect`；
- `balanced_power_residue_shell`。

`tests/test_collision_power_contraction.py` 对：

- `m<=9`；
- `s=2..7`；
- `|c|<=50`

逐项比较直接 defect 与 X22 residue-shell 闭式；并单独回归：

- `s=2` bounded residue；
- `s=3` exact lower-degree bulk shell；
- defect 非负及 `D=0 iff m|c`。

## 11. 下一步

1. 研究 `D_(m,s)` 在 block merge / min-plus 下是否存在自己的 shell composition law；
2. 把 residue-shell hierarchy 与 P018 Möbius precision shell 比较，确认哪些项可以在多尺度整除格上消去；
3. 检查 `s=2` 的特殊 boundedness 是否解释它为何特别适合作为 finite radial-distance 层；
4. 对 `s>=3` 研究是否可逐阶剥离 `q`-bulk，留下有限 remainder coefficient vector，而不是保存大整数 defect 本身。
