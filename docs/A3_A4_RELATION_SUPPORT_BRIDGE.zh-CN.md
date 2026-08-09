# A3 ↔ A4 Relation-Support Bridge — Stage 01

状态：`ACTIVE RESEARCH NOTE`  
范围：从 A3 weighted relation state 到 A4 admissible support family 的首个已证明生成桥梁  
来源归属：A3 `research/core/relation-quotient`；A4 `research/core/admissible-support-relations`

## 1. 这不是把 A3 与 A4 认定为同一理论

A3 与 A4 仍然是不同结构。

- A3 保存整数 present-state relation field：
  \[
  Z_{ij}=m_jc_i-m_ic_j,
  \]
  其中 `m_i>0` 是 block capacity，`c_i` 是 block total。
- A4 保存有限多值 support relation：
  \[
  R_r\subseteq X\times X,
  \]
  并用关系复合表达 support 的组合。

本说明证明的是：**A3 可以生成一类受限制的 A4 family**。并不主张任意 A4 relation 都来自 A3。

## 2. A3 weighted closure

任意 closed A3 field 满足

\[
m_kZ_{ij}+m_iZ_{jk}+m_jZ_{ki}=0.
\]

结合反对称性得到

\[
\boxed{m_jZ_{ik}=m_kZ_{ij}+m_iZ_{jk}}.
\]

于是

\[
\boxed{
m_j|Z_{ik}|\le m_k|Z_{ij}|+m_i|Z_{jk}|.
}
\]

这是一个纯整数 weighted triangle inequality，不需要除法，也不需要隐藏的实数 density。

## 3. Zero-relation quotient

定义

\[
i\sim_0 j\iff Z_{ij}=0.
\]

由于 capacities 全为正且 weighted closure 成立，`~_0` 是等价关系：

- 自反：`Z_ii=0`；
- 对称：由 antisymmetry；
- 传递：若 `Z_ij=Z_jk=0`，weighted closure 给出 `m_j Z_ki=0`，因 `m_j>0`，故 `Z_ki=0`。

记

\[
X_0=X/{\sim_0}.
\]

这个 quotient 是必要的。若直接在原始 A3 blocks 上定义 radius 0 support，则 capacity-normalized state 相同的两个不同 blocks 仍会互相支持；在 `X_0` 上，radius 0 才能严格成为 A4 的 identity relation。

## 4. Bridge theorem B01 — A3 生成 A4 admissible support family

对整数 `r>=0`，在 zero-relation classes 上定义

\[
\boxed{
[i]R_r[j]
\iff
|Z_{ij}|\le r m_i m_j.
}
\]

### B01a — representative independence

若 `i~_0 i'` 且 `j~_0 j'`，则

\[
|Z_{ij}|\le r m_i m_j
\]

的真假不会因为把代表元换成 `i',j'` 而改变。

也就是说，经交叉乘法表示的 normalized relation magnitude 在 zero-relation classes 上是良定义的。该结论由 weighted closure 与 `Z_(ii')=0`、`Z_(jj')=0` 推出。

### B01b — zero identity

在 `X_0` 上，

\[
R_0=I.
\]

因为 `[i]R_0[j]` 当且仅当 `Z_ij=0`，也即 `[i]=[j]`。

### B01c — monotonicity

若 `r<=s`，则

\[
R_r\subseteq R_s.
\]

### B01d — relational subadditivity

若

\[
[i]R_r[j],\qquad [j]R_s[k],
\]

则

\[
|Z_{ij}|\le r m_i m_j,
\qquad
|Z_{jk}|\le s m_jm_k.
\]

weighted triangle inequality 给出

\[
m_j|Z_{ik}|
\le
m_k r m_im_j+m_i s m_jm_k.
\]

由于 `m_j>0`，可在整数域中精确消去 `m_j`，得到

\[
|Z_{ik}|\le(r+s)m_im_k.
\]

所以

\[
\boxed{R_r;R_s\subseteq R_{r+s}.}
\]

因此，一个 A3 state 会在 `X_0` 上规范生成一个满足 A4 最小 admissible-support 公理的 radius family。

## 5. 这个桥梁的含义

A3 的 weighted relation coordinate 得到了一个 operational reading：整数 `r` 是对 capacity-normalized relational difference 的容许预算。A4 support 表示两个 zero-distinct quotient states 是否落在该预算内。

这是真桥梁，因为 A4 relation 完全从 A3 整数数据中导出，而它的复合法则又直接来自 A3 的 weighted closure identity。

但这**不**意味着所有 support / collision relation 都应该采用这一生成方式。

## 6. Bridge theorem B02 — universal fine support 可以下沉到 A3 partition quotient

把 fine blocks 分成两个 coarse groups `A,B`。A3 quotient 给出

\[
Z'_{AB}=\sum_{i\in A,j\in B}Z_{ij},
\qquad
m'_A=\sum_{i\in A}m_i,
\qquad
m'_B=\sum_{j\in B}m_j.
\]

若所有 fine cross pair 都满足半径 `r` support：

\[
|Z_{ij}|\le r m_i m_j
\quad
\text{对全部 }i\in A,j\in B,
\]

则

\[
|Z'_{AB}|
\le
\sum_{i,j}|Z_{ij}|
\le
r\sum_{i,j}m_im_j
=
r m'_A m'_B.
\]

因此

\[
\boxed{
(\forall i\in A,j\in B:\ iR_rj)
\Longrightarrow
A R'_r B.
}
\]

这是一个**单向** quotient compatibility theorem。

## 7. Negative boundary B03 — coarse support 无法恢复 universal fine support

B02 的逆命题不成立。

取所有 capacities 都为 1，totals 为

\[
(c_0,c_1,c_2,c_3)=(0,10,0,10),
\]

并令 coarse groups 为

\[
A=\{0,1\},\qquad B=\{2,3\}.
\]

四个 fine cross relation 分别为

\[
0,-10,10,0,
\]

于是

\[
Z'_{AB}=0.
\]

所以两个 coarse blocks 在 radius 0 下彼此 supported；但多个 fine cross pair 并不满足 radius 0 support。

因此

\[
\boxed{
A R'_r B
\not\Longrightarrow
\forall i\in A,j\in B:\ iR_rj.
}
\]

障碍来自 A3 quotient 中 signed relation 的抵消。

## 8. 对 A2 / P018 / P023 的后果

B03 给出了 hidden refinement information 的精确解释：

> coarse support 可以是合法的 coarse observable，但它并不是 universal fine support 的证明。

若未来运算或 query 需要 fine support witness，仅凭 coarse A3 quotient 上 support predicate 为真并不足够。是否必须恢复细节，应交由 A2/P023 的 future-compatibility criterion 判定。

这形成了第一条直接的三路桥梁：

\[
\boxed{
A3\ \text{relation state}
\longrightarrow
A4\ \text{support observable}
\longrightarrow
A2\ \text{future-sufficiency test}.
}
\]

## 9. 当前关系分类

- A3 → A4 threshold-support construction：`GENERATOR`；
- A3 partition quotient → A4 support：单向 `SPECIALIZATION / LAX COMPATIBILITY`，不是同构；
- coarse-support ⇒ universal-fine-support：由 B03 判定为 `CONFLICT / NEGATIVE_BOUNDARY`；
- A3 与 unrestricted A4：仍为 `COMPOSABLE_INDEPENDENT`，不主张等价。

## 10. Executable reference

- `src/enterprise_math/relation_support_bridge.py`
- `tests/test_relation_support_bridge.py`

可执行层检查 zero-class 构造、representative independence、radius-zero identity、monotonicity、relational subadditivity、B02，以及 B03 cancellation counterexample。
