# P025 补充 32 —— 用 Determinantal Index 定义 Higher-Rank Relation-Generator Radius

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-shared-access-stage30`  
依赖：P025 补充 30–31  
Hard block：`NONE`

## 1. 从 scalar gcd 推广到 lattice index

Stage 31 对 rank-one unit relation 用 accessible scale factors 的 gcd 定义 `rho_gen`。高 rank 中对应的对象，是 accessible relation states 在完整 relation lattice 内生成的 subgroup index。

令

\[
\Lambda\subseteq\operatorname{im}_{\mathbb Z}B
\]

为 relation subgroup，并给定整数 basis

\[
\boxed{g_1,\ldots,g_k.}
\]

在 ambient access radius `R` 下定义

\[
\boxed{S_R=Z_R(B)\cap\Lambda.}
\]

把每个 `t in S_R` 写成 exact basis coordinates：

\[
t=\sum_{i=1}^k z_i(t)g_i,
\qquad z(t)\in\mathbb Z^k.
\]

Accessible relation states 生成整个 `Lambda`，当且仅当这些 coordinate vectors 生成全部 `Z^k`。

## 2. P025-T88 —— maximal-minor index criterion

令

\[
C_R=\langle z(t):t\in S_R\rangle\subseteq\mathbb Z^k.
\]

若 coordinate vectors 的 rational rank 小于 `k`，则 `C_R` 在 `Z^k` 中 index 为无穷。

若 rank 已为 `k`，有限 index 精确为

\[
\boxed{
[\mathbb Z^k:C_R]
=
\gcd\{|\det M|:M\text{ 为 coordinate generator matrix 的任意 }k\times k\text{ minor}\}.
}
\]

因此

\[
\boxed{
C_R=\mathbb Z^k
\iff
\operatorname{rank}_{\mathbb Q}C_R=k
\text{ 且 }
\gcd(\text{maximal minors})=1.
}
\]

这就是 `Z^k` 中 full-rank sublattice 的标准 determinantal-divisor 判据。

## 3. P025-D20 —— higher-rank relation-generator radius

定义

\[
\boxed{
\rho_{\rm gen}(B,\Lambda)
=
\min\{R:\langle Z_R(B)\cap\Lambda\rangle=\Lambda\}.
}
\]

使用 `Lambda` 的任意整数 basis，P025-T88 都给出每个 radius 的 exact finite test。

该定义与 basis 无关。换 basis 只会对 coordinate vectors 施加 unimodular transformation，不改变 rational rank 与“maximal-minor gcd 是否为 1”。

## 4. P025-T89 —— finiteness 与 direct-basis upper bound

每个 basis vector `g_i` 都属于 `im_Z B`，所以拥有 finite ambient access radius

\[
\kappa_B(g_i)<\infty.
\]

令

\[
R_{\rm basis}=\max_i\kappa_B(g_i).
\]

到 radius `R_basis` 时，整组 declared basis vectors 已可直接访问，当然生成整个 `Lambda`。因此

\[
\boxed{\rho_{\rm gen}\le R_{\rm basis}<\infty.}
\]

`R_basis` 依赖所选 basis；`rho_gen` 不依赖。

## 5. Rank-one recovery

当 `k=1` 时，每个 accessible state 只有一个整数 coordinate `z(t)`，maximal minors 就是这些整数本身，因此 index criterion 退化成

\[
\boxed{\gcd\{|z(t)|:t\in S_R\}=1.}
\]

所以 Stage 31 正是 Stage 32 的 rank-one specialization。

## 6. Shared-prime relation example

对 blocks `(2,4,6)` 与 relation

\[
4\cdot2+4-2\cdot6=0,
\]

Stage 30 给出的 rank-one relation subgroup 由

\[
\boxed{g=(2,8,8)}
\]

生成。

radius 1 没有 nonzero relation state；radius 2 时 `g` 本身可直接访问，因此

\[
\boxed{\rho_{\rm gen}=2.}
\]

## 7. Rank-two abc example

对 `2+3=5`，block derivative matrix 为 identity，

\[
\Lambda=\{(u,v,w):u+v=w\}.
\]

取 basis

\[
\boxed{g_1=(1,0,1),\qquad g_2=(0,1,1).}
\]

两者 radius 1 已可访问，所以

\[
\boxed{\rho_{\rm gen}=1.}
\]

## 8. P025-N13 —— Generator completeness 可以远早于 chosen basis 的 direct access

Direct-basis upper bound 不是 intrinsic quantity。

取 ambient matrix `B=I_2`，无 relation constraint，因此

\[
\Lambda=\mathbb Z^2.
\]

故意选择很长的 unimodular basis

\[
\boxed{g_1=(10,1),\qquad g_2=(11,1).}
\]

两根 basis vectors 的 direct access radii 分别为 10、11，所以

\[
R_{\rm basis}=11.
\]

但 radius 1 时 ambient accessible set 已包含

\[
e_1=(1,0),\qquad e_2=(0,1).
\]

它们在 chosen basis 下坐标为

\[
\boxed{[-1,1],\qquad[11,-10].}
\]

determinant 为

\[
(-1)(-10)-11=-1.
\]

因此两个 radius-one states 已经生成整个 `Z^2`。

所以

\[
\boxed{\rho_{\rm gen}=1<R_{\rm basis}=11.}
\]

Generator completeness 关心的是**所有当前可访问 states 所生成的 subgroup**，而不是某组偏好的 coordinate basis 是否已经逐个进入 direct-access ball。

## 9. 架构后果

Generator-completeness layer 现在 basis-free，并适用于任意 finite relation rank：

\[
\boxed{
\text{ambient access ball}
\to
S_R=Z_R\cap\Lambda
\to
\langle S_R\rangle
\to
[\Lambda:\langle S_R\rangle]
\to
\rho_{\rm gen}.
}
\]

它与以下概念不同：

- first nonzero/nondegenerate access；
- chosen primitive/basis state 的 direct access；
- 由 radius-one relation-compatible states 重新生成的 intrinsic word geometry。

这些量在特殊系统中可以重合，但不能通过定义强行等同。

## 10. Prior-art / ownership 边界

Maximal minors 的 lattice index、sublattice generation 与 unimodular basis invariance 都是标准 integer-lattice mathematics。

P025 不对这些数学本身主张创新。项目侧继续检验的是：它们作为 arithmetic derivative-image access geometry 中 exact finite-precision generation-completeness layer 的作用。

该结构邻接 A4 split-completeness 与 A5 intrinsic geometry，但 Stage 32 **不**重复推导这些路线已经拥有的 generic split-completeness/geodesicity theorem。

## 11. 可执行资产

新增：

- `src/enterprise_math/relation_generator_radius.py`
  - exact integer basis coordinates；
  - Bareiss maximal minors；
  - basis coordinates 中的 subgroup index；
  - radius-level generation layer；
  - 带 direct-basis upper bound 的 exact higher-rank generator radius。
- `tests/test_relation_generator_radius.py`
  - rank-one shared-prime relation；
  - rank-two abc relation；
  - basis-dependent direct-access upper bound counterexample；
  - maximal-minor/gcd index checks。

## 12. 下一前沿

没有 hard block。继续：

1. 保留整个 radius-index profile，而不只记录第一次 index=1；
2. 区分 first full-rational-rank radius 与更晚的 index-one generator radius；
3. 寻找显式 relation systems，使某个中间 radius 已 full rank 但 subgroup index 仍大于 1；
4. 将 index-drop profile 与 Stage 18/24 finite precision profiles 比较；
5. 把 higher-rank generator-completeness coordinate Relay 给 P023/A3/A5，但不把 generic lattice-index theory 据为 P025 新数学。
