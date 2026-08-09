# A3 Guard-Image Lattice 补充 11 —— Two-Guard Rank-One Quotient Coordinates：一个整数 + 一个有限 Residue

状态：`RESEARCH WIP / COMPLETE INTEGER COSET COORDINATES + SYMBOLIC COARSE MAP`

## 1. 目标

对两个 integer guards，若当前 partition 的 hidden guard image rank 为 1：

\[
L_G=\mathbb Z h\subseteq\mathbb Z^2,
\qquad h\neq0,
\]

则一个 coarse fiber 的全部 fine score vectors 是一个 affine coset：

\[
g+\mathbb Z h.
\]

问题：能否不用任意 fine representative，直接给这个 coset 一个**完整、纯整数、coarse-readable 的有限信息坐标**？

答案是可以：

\[
\boxed{
\mathbb Z^2/\mathbb Z h
\cong
\mathbb Z\oplus\mathbb Z/d\mathbb Z,
}
\]

其中：

\[
\boxed{d=\gcd(|h_1|,|h_2|).}
\]

所以完整 quotient state 只需要：

- 一个 free integer；
- 一个 modulo-`d` torsion residue。

## 2. primitive direction 与 unimodular transform

写：

\[
h=d p,
\qquad
p=(p_1,p_2),
\qquad
\gcd(|p_1|,|p_2|)=1.
\]

由 Bezout，存在整数：

\[
u,v
\]

使：

\[
\boxed{u p_1+v p_2=1.}
\]

定义整数矩阵：

\[
\boxed{
T=
\begin{pmatrix}
 u & v\\
 -p_2 & p_1
\end{pmatrix}.
}
\]

其 determinant：

\[
\det T=u p_1+v p_2=1.
\]

所以 `T` 是 unimodular integer transform。

并且：

\[
T h=
\begin{pmatrix}
d\\0
\end{pmatrix}.
\]

于是 hidden lattice 在新坐标中只沿第一轴每次跳 `d`。

## 3. A3-G40 —— Complete Two-Guard Coset Coordinates

对 score vector：

\[
x=(x_1,x_2),
\]

定义：

### torsion coordinate

\[
\boxed{
\tau(x)
=
(u x_1+v x_2)\bmod d.
}
\]

### free coordinate

\[
\boxed{
\phi(x)
=
-p_2 x_1+p_1 x_2.
}
\]

若：

\[
x'=x+n h,
\]

则：

\[
\tau(x')=\tau(x),
\qquad
\phi(x')=\phi(x).
\]

反过来，若：

\[
\tau(x')=\tau(x),
\qquad
\phi(x')=\phi(x),
\]

则 `T(x'-x)` 的第二坐标为 0，第一坐标可被 `d` 整除，因此：

\[
T(x'-x)=(nd,0)
\]

某个 `n in Z`，从而：

\[
\boxed{x'-x=n h.}
\]

所以：

\[
\boxed{
 x,x'\text{ 属于同一 hidden coset}
\iff
(\tau,\phi)\text{ 完全相同}.
}
\]

这是 complete invariant，不是 hash / statistic。

## 4. deterministic canonical representative

因为：

\[
T^{-1}
=
\begin{pmatrix}
 p_1 & -v\\
 p_2 & u
\end{pmatrix},
\]

给定 quotient coordinate：

\[
(\tau,\phi),
\qquad 0\le\tau<d,
\]

可以选择 canonical score representative：

\[
\boxed{
 x_{can}
=
(
 p_1\tau-v\phi,
 p_2\tau+u\phi
).
}
\]

它与该 quotient class 中任意真实 fine score vector 相差 hidden step 的整数倍。

因此 branch reachability 可以直接从 quotient coordinate 重建：

1. 构造 `x_can`；
2. 在：
   \[
   x_{can}+\mathbb Z h
   \]
   上运行 rank-one threshold sweep。

所以：

\[
\boxed{
\text{reachable branch patterns}
=
F(\tau,\phi),
}
\]

不再依赖 fine representative。

## 5. A3-G41 —— Symbolic Coarse Map

现在回到 fine coordinates `c in Z^k`。

两个 guard scores：

\[
s_1=w^{(1)}\cdot c+b_1,
\]

\[
s_2=w^{(2)}\cdot c+b_2.
\]

partition：

\[
P=\{B_1,\ldots,B_\ell\}.
\]

假设：

\[
\operatorname{rank}W(K_P)=1.
\]

在每个 coarse block `B_a` 中任选 anchor `i_a`。

coarse totals：

\[
y_a=\sum_{i\in B_a}c_i.
\]

用 anchor section 构造 score representative：

\[
\tilde s(y)
=
 b
+
\sum_a y_a
\begin{pmatrix}
 w^{(1)}_{i_a}\\
 w^{(2)}_{i_a}
\end{pmatrix}.
\]

若换 block anchor，coefficient vector 的差是一个 within-block hidden generator，所以属于：

\[
\mathbb Z h.
\]

因此 quotient coordinate 不变。

于是得到 exact symbolic map：

### free

\[
\boxed{
\phi(y)
=
\phi_b+
\sum_a \alpha_a y_a,
\qquad \alpha_a\in\mathbb Z.
}
\]

### torsion

\[
\boxed{
\tau(y)
=
\left(
\tau_b+
\sum_a \beta_a y_a
\right)\bmod d.
}
\]

其中全部 coefficients 都是从 guard coefficients + Bezout transform 纯整数得到。

所以：

\[
\boxed{
\text{coarse block totals}
\longrightarrow
(\tau,\phi)
\longrightarrow
\text{exact fiber branch geometry}
}
\]

是一条完全不用 fine-state reconstruction 的符号链。

## 6. quotient precision state 的解释

该结果说明，即使两个 guards 都不 individually descend，未来 branch geometry 也可能只需要：

\[
\boxed{
\text{one free integer}
+
\text{one finite torsion residue}.
}
\]

这比：

`保存两个 exact guard scores`

更粗，但又比：

`只保存 hidden rank`

更完整。

所以 A3 precision state 至少存在第三类 typed information：

\[
\boxed{
\text{quotient free coordinates}
+
\text{torsion residues}.
}
\]

它们来自 integer quotient group 本身，不是人为添加的 metadata。

## 7. support 型 two-guard 的特别简化

finite band support：

\[
|z|\le R
\]

编码为两个 guards：

\[
s_-=R-z,
\]

\[
s_+=R+z.
\]

若 hidden scalar relation step 为 `q`，score hidden step 是：

\[
(-q,q)
\]

或其 canonical sign。

primitive direction 与 `(1,-1)` 同向，所以 free row 与 `(1,1)` 同向。

于是：

\[
\boxed{
\phi
=
\pm(s_-+s_+)
=
\pm2R.
}
\]

即 free integer 对整个 support task 是常数。

所有真正变化的 fiber information只剩：

\[
\boxed{\tau\in\mathbb Z/q'\mathbb Z}
\]

（`q'` 为 canonical score-step torsion modulus），它是 hidden relation residue 加上 guard bias 的一个固定 affine transform。

因此 A3→A4 pairwise radius support 在 two-guard quotient 中实际上是：

\[
\boxed{
\text{constant radius invariant}
+
\text{finite hidden residue}.
}
\]

Supplement 09 的 least-absolute-residue support certificate正是这一 quotient state 的 scalar化表达。

## 8. 与 relation quantum 的关系

这里的 torsion modulus：

\[
d=\gcd(|h_1|,|h_2|)
\]

是**guard-score hidden lattice** 的 Smith torsion，不应与 A3 weighted relation state 的 capacity gcd `g` 自动认同。

二者可能通过具体 observable map 相关，但：

\[
\boxed{
\text{capacity relation quantum}
\neq
\text{guard quotient torsion modulus}
}

除非另有 theorem 证明。

这一命名边界必须保留，避免把所有 gcd 都误写成一个“精度尺度”。

## 9. 实现

新增：

- `src/enterprise_math/two_guard_coset.py`；
- `tests/test_two_guard_coset.py`。

接口：

- `two_guard_quotient_basis`；
- `two_guard_coset_coordinate`；
- `two_guard_same_hidden_coset`；
- `canonical_scores_from_two_guard_coordinate`；
- `two_guard_reachable_patterns_from_coordinate`；
- `two_guard_coarse_map`；
- `evaluate_two_guard_coarse_map`。

测试覆盖：

- hidden step 被 unimodular transform 送到 `(d,0)`；
- quotient coordinates 对整个 hidden coset不变且完备；
- canonical representative 正确；
- symbolic coarse map 对 fine section 选择不敏感；
- reachable patterns 只依赖 quotient coordinate；
- support guard pair 的 free invariant固定为 `2R`，torsion为 relation residue 的确定 affine 变换。

## 10. 前人工作边界

`Z^2 / Z h` 的 Smith normal form、unimodular change of basis、free + torsion decomposition 都是成熟 integer module / lattice algebra。

A3 不把该 quotient decomposition 当作原创。

当前项目特化是：

\[
\boxed{
\text{coarse partition kernel}
\to
\text{hidden guard quotient module}
\to
\text{typed predicate precision state}
\to
\text{branch reachability}.
}
\]

novelty 仍保持未验证。

## 11. 下一步

1. 对 arbitrary guard count + hidden rank `d`，用 Smith/Hermite 给 `Z^r/L_G` 构造 free/torsion quotient coordinates；
2. 研究 quotient coordinate 上 branch-effect function 是否可符号编译为 finite/piecewise coarse program；
3. support bridge 只需消费 `(radius, torsion residue)` 特化，不复制 A3 quotient machinery；
4. 把 quotient torsion 与 relation-rank / relation-quantum 并列成 typed precision certificate；
5. 对 P021 multi-predicate role/witness query测试其 hidden guard quotient 是否也有低 free-rank / 小 torsion 表示。
