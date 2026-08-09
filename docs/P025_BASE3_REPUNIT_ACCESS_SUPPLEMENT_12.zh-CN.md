# P025 补充 12 —— Base-3 Repunit-Prime Family 的闭式 Access Radius

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 05、10–11  
Hard block：`NONE`

## 1. 条件 family

假设

\[
\boxed{
1+2r=3^m,
\qquad
r=\frac{3^m-1}{2}\text{ 为素数}.
}
\]

这是一个条件 family theorem：对每个满足上述 repunit 为素数的指数成立。它**不**假设或主张这类指数有无穷多个。

由于 `2r` squarefree，P025-T17 立即给出

\[
\boxed{\eta_{\min}=m.}
\]

本补充的新内容是：对应的精确 floor-access radius `nu` 同样可以写成闭式。

## 2. P025-T34 —— 指数必须是素数

若

\[
r=(3^m-1)/2
\]

为素数，则 `m` 必为素数。

### 证明

若 `m=ab` 且 `a,b>1`，则

\[
3^m-1=(3^a)^b-1
\]

含有非平凡因子 `3^a-1`。除以 `3-1=2` 后，base-3 repunit

\[
\frac{3^m-1}{2}
=1+3+\cdots+3^{m-1}
\]

仍通过标准 repunit factorization 非平凡分解。因此其为素数时，`m` 必为素数。∎

所以 `m` 为奇素数。若 `m>3`，则

\[
m\equiv1\text{ 或 }5\pmod6.
\]

## 3. Floor-access 方程

补充 10 取 `q=2`、另一素数为 `r`，把 floor witness 化为

\[
\boxed{
r u+2v=m3^{m-1},
\qquad
x_3=1.
}
\]

因为 `r` 与右端均为奇数，每个解都满足

\[
\boxed{u\equiv1\pmod2.}
\]

所以 `u` 只能沿奇整数变化，而

\[
v=\frac{m3^{m-1}-ru}{2}
\]

随之唯一确定。

实数 balance ratio 为

\[
\frac{m3^{m-1}}r
=
\frac{2m3^{m-1}}{3^m-1},
\]

它只略大于 `2m/3`。

## 4. P025-T35 —— 精确闭式 witness 与 radius

minimum-`L_infinity` floor witness 由最接近上述 balance ratio 的允许奇整数 `u` 给出。

### 情形 `m=3`

\[
r=13,
\qquad
(u,v)=(3,-6),
\]

所以

\[
\boxed{\nu=6.}
\]

### 情形 `m>3` 且 `m congruent 1 mod 6`

取

\[
\boxed{u=\frac{2m+1}{3}.}
\]

则

\[
\boxed{
v=\frac{2m+1-3^m}{12}.}
\]

因此

\[
\boxed{
\nu
=
\frac{3^m-(2m+1)}{12}.
}
\]

### 情形 `m>3` 且 `m congruent 5 mod 6`

取

\[
\boxed{u=\frac{2m-1}{3}.}
\]

则

\[
\boxed{
v=\frac{3^m+2m-1}{12},}
\]

从而

\[
\boxed{
\nu
=
\frac{3^m+2m-1}{12}.
}
\]

在 coordinate order `(2,r,3)` 下，完整 floor witness 为 `(u,v,1)`。

### 最优性证明

parity condition 强制 `u` 只能取奇整数。所选 `u` 正是离实数比值 `H/r` 最近的奇整数，其中 `H=m3^(m-1)`。

换成其它允许的 `u` 至少会变化 `2`，于是 `v` 会变化 `r` 的整数倍。所选 residue 满足 `|v|<=r/2`；任何其它允许解都有

\[
|v'|\ge r-|v|\ge|v|.
\]

当 `m=3` 时直接有 `|v|=6>=|u|=3`。对 `m>3` 的素数情况，由上述闭式立即有 `|v|>|u|`。因此所选解最小化 `max(|u|,|v|)`，其最大坐标正是上述 `nu`。∎

## 5. 精确样例

### `m=3`

\[
r=13,
\qquad
1+2\cdot13=27.
\]

此时

\[
\eta_{\min}=3,
\qquad
\nu=6.
\]

### `m=7`

\[
r=1093,
\qquad
1+2\cdot1093=2187.
\]

floor witness 为

\[
(5,-181,1),
\]

因此

\[
\boxed{\eta_{\min}=7,\qquad\nu=181.}
\]

### `m=13`

\[
r=797161,
\qquad
1+2\cdot797161=3^{13}.
\]

floor witness 为

\[
(9,-132858,1),
\]

所以

\[
\boxed{\eta_{\min}=13,\qquad\nu=132858.}
\]

## 6. Arithmetic 与 geometric certificate cost 的强分离

在这个条件 family 中，

\[
\eta_{\min}=m
\]

只随指数线性增长，而对 family 中每个 `m>3` 的素数都有

\[
\nu
=
\frac{3^m+O(m)}{12}.
\]

因此 arithmetic obstruction floor 与真正访问该 floor 的 geometric cost 可以处在完全不同的尺度。

这里不能推出无界 family 结论，因为我们没有假设 base-3 repunit primes 有无穷多个。它只是对每个实际 family member 给出 exact formula，并且在上面的已知工作样例中已经明显展示尺度分离。

## 7. 对 P025 的意义

这个 family 是四类 witness quantity 的一个非常干净的校准样本：

\[
\text{support/valuation obstruction}
\to
\eta_{\min}
\to
\text{floor-access geometry}
\to
\nu.
\]

两个成本由同一个 relation 生成，却不能由一个 scalar precision rule 相互替代。

特别是，一个较小的 arithmetic redundancy target 并不意味着 prime-coordinate lattice 中附近就存在对应 certificate。

## 8. Prior-art discipline

Repunit factorization、“prime repunit 要求 prime exponent”、parity constraints 与 two-variable Diophantine minimization 都是经典数学。

P025 不主张这些工具本身的新颖性。项目侧作用是把这个 family 用作 exact certificate-precision calibration，并坚持区分 `eta_min` 与 `nu`。

## 9. 可执行资产

新增：

- `src/enterprise_math/abc_absorption_repunit.py`
  - primality/domain validation；
  - 对 prime exponent 各 residue class 的 exact closed floor witness；
  - 与 generic exact two-variable solver 的独立一致性审计。
- `tests/test_abc_absorption_repunit.py`
  - 指数 `3`、`7`、`13` 的 exact checks；
  - composite repunit case 的拒绝测试。

## 10. 下一前沿

不存在 hard block，继续：

1. 搜索其它 `p^m-1` factorization families，其中 `nu` 也能写成闭式；
2. 把这些 exact formulas 与 Pasten Geometry-of-Numbers norm bound 直接比较，而不只与 exact optimum 比较；
3. 测试 `1+q^e r=p^m` 这类非 power 侧含一个 repeated factor 的 family 是否也有 closed access formula；
4. 用这些 families 校准高于三个 prime coordinates 的 access 问题；
5. 不从本 family 推断 ABC-quality theorem：这里的价值是 certificate costs 的结构分离。
