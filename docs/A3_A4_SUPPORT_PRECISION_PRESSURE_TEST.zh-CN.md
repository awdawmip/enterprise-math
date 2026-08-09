# A3→A4 Support Precision 压力测试 —— Cancellation 的 Guard-Quotient Module 定位

状态：`RESEARCH WIP / CROSS-ROUTE PRESSURE TEST / BRIDGE OWNERSHIP PRESERVED`

## 1. 目的

A3→A4 bridge 已保存一个 cancellation 反例：coarse support 可以成立，但不能推出 universal fine support。

本文件不重新拥有 bridge theorem，也不修改 A4 support 定义。它只用 A3 future-precision 工具回答一个更精确的问题：

> 该 cancellation failure 在 A3 的 hidden predicate quotient 中究竟丢掉了什么？

## 2. 四个 fine coordinates 与 coarse partition

取 unit capacities 和 fine totals：

\[
c=(c_0,c_1,c_2,c_3).
\]

coarse groups：

\[
A=\{0,1\},
\qquad
B=\{2,3\}.
\]

partition 只保留：

\[
C_A=c_0+c_1,
\qquad
C_B=c_2+c_3.
\]

对应 kernel：

\[
K_A
=
\{(a,-a,b,-b):a,b\in\mathbb Z\}.
\]

rank 为 2。

## 3. universal fine support 的四个 relation guards

四条 cross relations：

\[
z_{02}=c_0-c_2,
\]

\[
z_{03}=c_0-c_3,
\]

\[
z_{12}=c_1-c_2,
\]

\[
z_{13}=c_1-c_3.
\]

令 guard map：

\[
W(c)
=
(z_{02},z_{03},z_{12},z_{13})
\in\mathbb Z^4.
\]

在 hidden motion：

\[
\eta=(a,-a,b,-b)
\]

下：

\[
\boxed{
W(\eta)
=(a-b,\ a+b,\ -a-b,\ -a+b).
}
\]

所以 universal fine-support query 的 hidden predicate geometry 实际只含两个 integer degrees，而不是四个独立自由度。

## 4. A3-ABP01 —— hidden guard image 的 Smith profile

取 kernel basis：

\[
(1,-1,0,0),
\qquad
(0,0,1,-1).
\]

其 guard images：

\[
g_1=(1,1,-1,-1),
\]

\[
g_2=(-1,1,-1,1).
\]

因此 hidden lattice：

\[
L_G
=
\langle g_1,g_2\rangle_{\mathbb Z}
\le\mathbb Z^4.
\]

直接整数 minors 给：

\[
\Delta_1=1,
\qquad
\Delta_2=2.
\]

所以 Smith invariant factors：

\[
\boxed{(1,2).}
\]

于是 predicate quotient：

\[
\boxed{
\mathbb Z^4/L_G
\cong
\mathbb Z^2\oplus\mathbb Z/2\mathbb Z.
}
\]

即：

- hidden rank：`2`；
- coarse predicate free rank：`2`；
- 另有一个 parity 型 torsion bit/class。

因此 bridge cancellation failure 在 A3 中可精确定位为：

> coarse partition 删除了一个 rank-two hidden guard lattice；剩余 predicate quotient 还带一个 nontrivial `Z/2` torsion class，不能由 coarse relation scalar 一个值概括。

## 5. A3-ABP02 —— 同一 coarse state 同时含 universal-support True/False lifts

固定 coarse totals：

\[
(C_A,C_B)=(10,10).
\]

### supported lift

\[
c^{(+)}=(5,5,5,5).
\]

四条 cross relations 全为：

\[
0.
\]

所以 radius-0 universal fine support：

\[
\boxed{\mathrm{True}.}
\]

### cancellation lift

\[
c^{(-)}=(0,10,0,10).
\]

四条 cross relations：

\[
\boxed{(0,-10,10,0).}
\]

所以 universal radius-0 fine support：

\[
\boxed{\mathrm{False}.}
\]

但两者 coarse totals完全相同：

\[
(10,10).
\]

并且 coarse cross relation：

\[
Z'_{AB}
=
\sum_{i\in A,j\in B}(c_i-c_j)
=
2(C_A-C_B)
=
0
\]

也完全相同。

因此：

\[
\boxed{
\text{coarse relation}=0
\not\Rightarrow
\text{universal fine radius-0 support}.
}
\]

这不是抽象“可能丢信息”，而是同一个 coarse fiber 中明确存在 True/False 两个 fine witnesses。

## 6. A3-ABP03 —— 每一个 individual fine pair support 在该 quotient 上也可能 ambiguous

例如：

\[
z_{02}=c_0-c_2.
\]

其 coefficient vector：

\[
(1,0,-1,0).
\]

在 partition `{{0,1},{2,3}}` 下，within-block coefficient differences 的 gcd 是：

\[
\boxed{q=1.}
\]

所以若当前 base relation value 为 0，整个 hidden fiber 上：

\[
z_{02}\in\mathbb Z.
\]

对 radius-0 band：

\[
|z_{02}|\le0,
\]

既有 `z=0` 的 supported lift，也有任意非零 unsupported lift。

因此 individual fine-pair support 本身也不 factor through coarse partition。

四条 cross pair 都具有同样的 hidden-step-1 现象。

## 7. coarse support 为什么仍然 exact

coarse relation coefficient vector是：

\[
(2,2,-2,-2).
\]

它在每个 coarse block 内常数，所以：

\[
\boxed{w(K_A)=0.}
\]

即 coarse relation本身完全 descend。

因此：

- coarse support observable 可 exact；
- universal fine support observable 不 exact；
- 差别不是数值误差，而是 future language 读取的 guard map 不同。

这正好符合 A3 future-precision core：

\[
\boxed{
\text{required precision depends on }W(K_A),
\text{ not only on the underlying coarse state}.}
\]

## 8. 对 A3→A4 bridge 的下游意义

本压力测试给 bridge 一个更细的结构分层：

### single coarse pair support

只需 coarse weighted relation，可在当前 partition exact。

### single fine pair support

是 rank-one scalar band；可用 A3 hidden-band / rank-one residue solver。

### universal cross-pair support

四个 pair relations 共同形成 rank-two hidden predicate lattice，且 quotient 带 `Z/2` torsion；需要 rank-two / quotient-module precision，而不是只检查 coarse signed sum。

因此：

\[
\boxed{
\text{support query 的 precision complexity 取决于 query scope}.}
\]

“coarse pair support”“one fine pair support”“universal all fine pairs support”是三种不同 future languages，不能用同一个 coarse truth 值替代。

## 9. ownership 边界

- A3 持有 `K_A -> W(K_A) -> quotient module -> required precision` 的通用分析；
- A3→A4 bridge 持有 support family、cancellation/interpolation 等 bridge statements；
- A4 持有 admissible-support/correspondence 母理论。

因此本文只作为 A3 pressure test，并通过 Research Relay 将 corollary 回流 bridge owner，不复制 bridge implementation。

## 10. 实现

新增：

- `tests/test_a3_a4_support_precision_pressure.py`。

测试直接验证：

1. cross-relation guard quotient profile：hidden rank `2`、free rank `2`、Smith `(1,2)`、torsion `Z/2`；
2. `(5,5,5,5)` 与 `(0,10,0,10)` 同 coarse state，却 universal support True/False；
3. 四条 individual fine pair radius-0 predicate 在 zero-base fiber上均 ambiguous；
4. coarse relation guard hidden step为 `0`，因此 coarse radius-0 support exact True。

## 11. 下一步

1. Relay 本 pressure test 给 `research/core/relation-support-bridge`；
2. bridge owner 可将 `universal fine support` 作为 A2/P023 future-sufficiency obligation 的 concrete guard family；
3. 对 staged support / split-completeness，把 endpoint + intermediate-witness predicates映射成 A3 guard quotient，测其 hidden rank / torsion；
4. P018 可据 query scope 选择 scalar/rank-one/rank-two precision solver，而不是统一 full refinement；
5. P022 若提供有限 lattice/admissible domain，需重新检查 full-integer-fiber假设是否保留。
