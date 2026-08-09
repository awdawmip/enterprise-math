# P019 补充 09 —— Fiber Root、Slack 级联与平方层 Bulk/Detail 压缩

状态：`RESEARCH WIP / INTEGER IDENTITIES PROVED + BOUNDED REGRESSION`

## 1. 目标

Supplement 07/08 已把 contraction trace 分成：

- value；
- full fiber witness relation；
- selected boundary witness；
- future-safe quotient。

本补充继续问：即使某一步必须保留 selected boundary 信息，是否仍需要保存很大的 child totals？

平方层 `s=2` 的答案明显更强：**大尺度 proportional bulk 与真正 history-sensitive 的偏差可以精确分离。**

同时，每一步 boundary selection 本身也可以写成一个新的整数 root/collapse，而不是任意搜索。

## 2. P019-X16 —— directed fiber boundary 是一个整数 root

固定 block sizes `m,n`、power `s`、parent total `c`。

令右端 argmin endpoint 为

\[
a_0=\max\operatorname*{argmin}_{a\in\mathbb Z}
\bigl(\Psi_{m,s}(a)+\Psi_{n,s}(c-a)\bigr).
\]

对 `a>=a_0` 定义右支超额能量

\[
G(a)
=
\Psi_{m,s}(a)
+
\Psi_{n,s}(c-a)
-
\Psi_{m+n,s}(c).
\]

因为 fiber cost 是离散凸的，`G` 在右支严格递增。

给定 slack `omega>=0`，定义

\[
\boxed{
R_G(\omega)
=
\max\{a\ge a_0:G(a)\le\omega\}.
}
\]

这就是 directed right-boundary receiver total。

因此

\[
G(a)\le\omega
\iff
 a\le R_G(\omega)
\]

在右支上给出标准 order-adjoint 型整数根关系。

定义 consumed excess

\[
\gamma=G(R_G(\omega))
\]

与 remainder

\[
\rho=\omega-\gamma.
\]

则

\[
\boxed{
0\le\rho
<
G(R_G(\omega)+1)-G(R_G(\omega)).
}
\]

所以 boundary selection 自带一个有界 basin remainder。

这与 Enterprise Math 现有 `R_p/C_p`、P008 right-adjoint、P018 precision detail/carry 属于同一个有限整数骨架。

## 3. P019-X17 —— reverse contraction 是 slack 的望远镜级联

设全局 threshold 为 `T`，沿一个完整 oriented contraction flag 反向恢复 selected boundary witness。

在第 `t` 个 reverse split，当前 coarse partition minimum energy 为 `E_t`，定义剩余 slack

\[
\omega_t=T-E_t.
\]

该步 fiber root 消耗超额能量 `gamma_t`，产生 remainder `rho_t`。

拆分后 partition energy 为

\[
E_{t+1}=E_t+\gamma_t,
\]

所以

\[
\boxed{
\omega_{t+1}
=
\omega_t-\gamma_t
=
\rho_t.
}
\]

因此整条 reverse lift 是精确的 slack 级联：

\[
T
=
E_{final}+\omega_{final}
=
\sum_t\gamma_t+\omega_{final},
\]

根 single-block 零和状态的 minimum energy 为 0。

每一级同时满足

\[
0\le\omega_{t+1}<\text{next fiber gap}_t.
\]

因此 contraction trace 可以理解成一串：

`fiber-root state + bounded remainder`。

它不是隐藏实数误差，也不是无限精度展开。

## 4. `s=1` 的极简情况：二进制 fiber remainder

当 `s=1`：

\[
\Psi_{m,1}(c)=|c|
\]

与 block size 无关。

对任意两块与任意 parent total，沿一个有向 fiber 从右端继续向外移动一步，超额能量固定增加 2。

所以：

\[
\boxed{
\text{next gap}=2,
\qquad
\rho=\omega\bmod2.
}
\]

这说明 primitive graph-cost 层的 directed fiber trace detail 只需一个 binary remainder。

注意：即使 `rho=0`，`s=1` 的 argmin witness 本身仍可能高度退化；所以“无正超额 detail”不等于“无 provenance ambiguity”。

## 5. P019-X18 —— 平方能量的精确 bulk/detail 恒等式

定义

\[
\varepsilon_m(c)
=r(m-r),
\qquad
r=|c|\bmod m.
\]

由

\[
|c|=mq+r
\]

及 `Psi_(m,2)` 的闭式直接展开：

\[
\boxed{
m\Psi_{m,2}(c)=c^2+\varepsilon_m(c).}
\]

其中

\[
0\le\varepsilon_m(c)
\le\left\lfloor\frac{m^2}{4}\right\rfloor.
\]

因此平方层可精确分成：

- bulk：`c^2`；
- bounded residue detail：`epsilon_m(c)`。

这不是渐近式。

## 6. P019-X19 —— 两块 split 的精确失衡恒等式

令 block sizes 为 `m,n`，

\[
M=m+n,
\qquad
a+b=c.
\]

定义相对于比例分配的整数失衡坐标

\[
\boxed{
z=na-mb=Ma-mc.}
\]

并定义该 split 相对 merged fiber minimum 的 excess

\[
\omega
=
\Psi_{m,2}(a)
+
\Psi_{n,2}(b)
-
\Psi_{M,2}(c).
\]

把 X18 分别用于三个 blocks，再用恒等式

\[
nMa^2+mMb^2-mnc^2=(na-mb)^2
\]

得到：

\[
\boxed{
mnM\omega
=
z^2
+nM\varepsilon_m(a)
+mM\varepsilon_n(b)
-mn\varepsilon_M(c).
}
\]

全部量都是整数。

## 7. P019-X20 —— history-sensitive 失衡有整数根界

由于中间两个 correction 项非负：

\[
z^2
\le
mn\bigl(M\omega+\varepsilon_M(c)\bigr).
\]

因此

\[
\boxed{
|z|
\le
R_2\!\left(
mn\bigl(M\omega+\varepsilon_M(c)\bigr)
\right).
}
\]

特别地，在 minimum layer `omega=0`：

\[
\boxed{
z^2\le mn\varepsilon_M(c).}
\]

而 `epsilon_M(c)` 只依赖 `|c| mod M`，不依赖 bulk quotient。

所以 minimum 层里可以让 parent total `|c|` 任意增大，但真正需要区分左右 block 的 history-sensitive deviation 不随 bulk 增长。

## 8. P019-X21 —— minimum imbalance profile 只依赖 remainder

写

\[
|c|=Mq+r,
\qquad0\le r<M.
\]

对 `s=2` 的 minimum split，Supplement 07 中额外 `q+1` 槽位的左侧数量记为 `h`，满足

\[
\max(0,r-n)
\le h\le
\min(m,r).
\]

左 total 为

\[
a=\sigma(mq+h),
\qquad\sigma=\operatorname{sgn}(c).
\]

所以失衡坐标恰为

\[
\boxed{
z_h=\sigma(Mh-mr).}
\]

对应 labeled multiplicity 为

\[
\boxed{
\binom mh\binom n{r-h}.
}
\]

因此整套 minimum imbalance profile 只依赖：

`m,n, sign(c), |c| mod M`。

**不依赖 quotient `q`。**

这是一个非常强的 finite-detail 压缩。

## 9. 用 `z` 代替大 child totals

由

\[
z=Ma-mc
\]

可恢复

\[
\boxed{
a=(mc+z)//M,
\qquad b=c-a,}
\]

前提是

\[
M\mid(mc+z).
\]

所以对平方层，一次合法 split 不必保存两个可能很大的 child totals。

给定 parent total `c`、block sizes `m,n`，一个合法的整数 deviation tag `z` 已足够精确恢复该 split。

这给出新的 candidate trace coordinate：

`parent bulk transported exactly + bounded/controlled imbalance tag z`。

在 minimum layer，`z` 的候选集合甚至是由 remainder 决定的有限集合。

## 10. 与 P018 的接口

P018 的基本结构是：

`fine state = transported coarse state + bounded precision detail`。

平方 contraction 当前得到：

`child allocation = proportional parent bulk + integer imbalance detail`。

由于避免真正分数，比例关系使用交叉乘法坐标 `z=Ma-mc` 表示。

所以 P019 的 dimension contraction 不需要另造“近似误差”概念；其 trace-sensitive 部分可以直接进入 P018 的有限 detail/carry 语言。

## 11. 与 P011/P021 的接口

- P011：`fiber_witness_interval=[L,U]` 给出 block-total fiber multiplicity `U-L+1`；
- P021：exact witness relation 在多步复合前不能仅按 cardinality 删除；
- 本补充：在 square layer，单步 witness 的大数值部分可以进一步坐标化为 parent total + bounded imbalance `z`。

因此“保留 witness identity”并不等于“原样保存全部高维大整数状态”。

## 12. 实现与验证

`src/enterprise_math/contraction_trace.py` 新增：

- `directed_boundary_decomposition`；
- `BoundaryTraceStep` / `reverse_boundary_witness_with_trace`；
- `square_residue_correction`；
- `square_split_imbalance`；
- `square_split_from_imbalance`；
- `square_minimum_imbalance_profile`；
- `square_scaled_excess_identity`；
- `square_imbalance_bound`。

`tests/test_contraction_trace.py` 对：

- `s=1..4` fiber-root remainder；
- `s=1` binary remainder；
- reverse slack telescoping；
- square scaled identity；
- imbalance root bound；
- `z` 的精确恢复；
- minimum imbalance profile 的 bulk quotient 不变性；
- `epsilon_m` 的有界性

进行有限整数回归。

## 13. 下一步

下一步优先攻击：

1. 在 square layer 上研究一整条 contraction flag 的 `z_t` 序列是否满足更强的全局约束/守恒式；
2. 判断哪些 future query 只需要 `z_t + rho_t`，不需要完整 block membership history；
3. 把 Supplement 08 的 future-safe quotient 算法实际施加到 contraction trace 上，寻找第一个非平凡可安全商掉的 history class；
4. 推广 X18–X21 到 `s>2`，寻找 higher collision-order 的 `bulk polynomial + bounded residue shell` 分解。
