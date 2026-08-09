# A3 Guard-Image Lattice 补充 09 —— Hidden Scalar Band Predicate、Residue Certificate 与 Support 精度不对称

状态：`RESEARCH WIP / EXACT SCALAR SUBGROUP BAND THEOREM + A3→A4 CONSEQUENCE`

## 1. 问题

A3 future-language 研究已经覆盖单 threshold 与 multi-guard threshold patterns。

但很多实际 relation query 不是 one-sided threshold，而是 finite band：

\[
\boxed{|z|\le R.}
\]

A3→A4 bridge 的 pairwise radius support 正是该形式，其中 `z` 是 weighted relation `Z_ij`，`R` 是整数 radius budget 乘 capacities。

核心问题：

> 若 exact scalar relation `z` 在当前 partition 下仍隐藏，一个 coarse fiber 能否仍然精确回答 finite-band predicate？

答案具有严格不对称性：**可以 exact False，但非零 hidden variation 下不可能 exact True。**

## 2. scalar hidden image

设整数线性 scalar observable：

\[
z(c)=w^Tc+b.
\]

对 coordinate partition `A`，hidden variation 是：

\[
w(K_A)\le\mathbb Z.
\]

任意 `Z` 的 subgroup 都有形式：

\[
\boxed{q\mathbb Z,\qquad q\in\mathbb N_0.}
\]

其中：

- `q=0`：scalar observable 已完全 descend；
- `q>0`：同一 coarse fiber 的全部 scalar values是
  \[
  \boxed{z_0+q\mathbb Z.}
  \]

对 coordinate partition，`q` 直接是所有 within-block coefficient differences 的 gcd。

## 3. A3-G34 —— Least Absolute Residue

对：

\[
q>0,
\]

定义：

\[
\boxed{
\rho_q(z_0)
=
\min_{t\in\mathbb Z}|z_0+qt|.
}
\]

若标准 residue：

\[
r=z_0\bmod q,
\qquad 0\le r<q,
\]

则：

\[
\boxed{
\rho_q(z_0)=\min(r,q-r).
}
\]

全是整数操作。

所以 arithmetic progression 是否命中 finite band：

\[
[-R,R]
\]

当且仅当：

\[
\boxed{\rho_q(z_0)\le R.}
\]

## 4. A3-G35 —— Hidden Finite-Band Exactness Theorem

考虑 predicate：

\[
P_R(z):=[|z|\le R],
\qquad R\in\mathbb N_0.
\]

### 情形 1：`q=0`

`z` 已 coarse-readable，predicate 普通 exact：

\[
P_R=[|z_0|\le R].
\]

### 情形 2：`q>0`

fiber：

\[
z_0+q\mathbb Z
\]

向正负两方向无界。

所以对任意 finite `R`：

\[
\boxed{\text{fiber 中永远存在 }|z|>R\text{ 的 states}.}
\]

因此 finite-band predicate 在 nonzero hidden fiber 上**不可能 uniformly True**。

另一方面，存在 supported state 当且仅当：

\[
\rho_q(z_0)\le R.
\]

故：

\[
\boxed{
q>0:\quad
P_R\text{ exact}
\iff
\rho_q(z_0)>R,
}
\]

且 exact 时唯一可能值是：

\[
\boxed{P_R=\mathrm{False}.}
\]

若：

\[
\rho_q(z_0)\le R,
\]

则同一 coarse fiber 同时含：

- supported fine states；
- unsupported fine states。

所以 predicate 不 quotient-readable。

## 5. 这不同于单 threshold

对单 threshold：

\[
z\ge0,
\]

只要 `q>0`，arithmetic progression 在正负方向都无界，因此每个 fiber 必然同时出现 True/False。

finite band 不同：它有**有限宽度**。一个 residue class 可以完全从 band 的缝隙中穿过去。

所以：

\[
\boxed{
\text{hidden scalar}
\not\Rightarrow
\text{所有 predicate 都必须 refinement}.
}
\]

predicate 的几何宽度与 hidden subgroup residue 同时决定 task precision。

## 6. A3-G36 —— Exact-False Residue Certificate

当：

\[
q>0,
\qquad
\rho_q(z_0)>R,
\]

四个整数：

\[
\boxed{(z_0\bmod q,\ q,\ \rho_q(z_0),\ R)}
\]

就是一个有限 exact-false certificate。

它证明：

\[
\forall t\in\mathbb Z,
\qquad
|z_0+qt|>R.
\]

不需要恢复 exact fine scalar，也不需要保存 branch/witness identity。

这是 task-specific detail preservation 的一个极小整数 certificate。

## 7. refinement 如何改变 band exactness

若 parent scalar image：

\[
q\mathbb Z
\]

经过 refinement 变成 subgroup：

\[
q'\mathbb Z,
\qquad q'\text{ 是 }q\text{ 的正整数倍},
\]

则 child fiber只保留 parent arithmetic progression 的一个 residue class。

于是：

\[
\rho_{q'}(z_0)
\]

可能大于：

\[
\rho_q(z_0).
\]

若最终跨过 `R`：

\[
\boxed{
\rho_{q'}(z_0)>R,
}
\]

predicate 就从 ambiguous 变成 exact False，尽管 scalar relation 仍然 hidden。

这正是 Supplements 05/06 中“residue refinement 小于 full visibility precision”的 scalar band 版本。

## 8. A3→A4 radius support corollary

A3-generated A4 support family 使用：

\[
\boxed{
|Z_{ij}|\le r\,m_i m_j.
}
\]

固定：

\[
R=r\,m_i m_j.
\]

假设一个更粗 partition 把 future query 所需的 exact `Z_ij` 隐藏，使同一 coarse fiber 上：

\[
Z_{ij}\in z_0+q\mathbb Z.
\]

### `q=0`

exact relation 可读，support truth 普通 exact。

### `q>0` 且 residue miss

若：

\[
\rho_q(z_0)>R,
\]

则：

\[
\boxed{
\text{所有 fine lifts 都不满足 radius support}.
}
\]

所以即使 exact `Z_ij` 被隐藏，support observable仍可安全 descend 为：

\[
\boxed{\mathrm{False}.}
\]

### `q>0` 且 progression 命中 band

若：

\[
\rho_q(z_0)\le R,
\]

则同一个 coarse fiber 中：

- 有 fine lifts support=True；
- 也有 fine lifts support=False。

因此：

\[
\boxed{
\text{support truth 本身不 factor through 当前 quotient}.
}
\]

特别地，在完整整数 fiber 假设下：

> **nontrivially hidden `Z_ij` 不可能给出“所有 fine lifts 都 support=True”的 exact certificate。**

这与已有 bridge 的 signed-cancellation 反例一致，但更强地给出了 arithmetic residue 判据。

## 9. ownership 边界

本 supplement 的通用 scalar-band theorem 属于 A3 future-precision / hidden relation algebra。

A3→A4 support 只是一个 `SPECIALIZATION / DOWNSTREAM COROLLARY`；其正式 bridge ownership 仍在：

`research/core/relation-support-bridge`。

因此 A3 不复制 bridge module，只通过 Research Relay 回流该 corollary。

## 10. 实现

新增：

- `src/enterprise_math/hidden_band_predicate.py`；
- `tests/test_hidden_band_predicate.py`。

接口：

- `scalar_hidden_step`；
- `least_absolute_residue`；
- `hidden_band_profile`；
- `hidden_band_profile_for_partition`；
- `HiddenBandProfile`。

测试覆盖：

- scalar hidden step 的 gcd law；
- least absolute residue 与直接整数枚举一致；
- hidden nonzero fiber 的 exact-false case；
- hidden nonzero fiber永不 exact-true；
- visible scalar 的普通 exact truth；
- progression 命中 band 的完整小整数压力测试；
- 一个 relation仍 hidden、但 finite band 已 exact False 的 partition例子。

## 11. 当前边界

该 theorem 依赖：

- 完整整数 affine fiber `z_0+qZ`；
- finite radius `R`。

若具体应用 domain 额外限制 fine states，例如只允许有限 ball / admissible subset，则“unsupported states 永远存在”的结论可能失效，必须在应用分支重新证明。

不应把本 full-integer-fiber corollary机械搬到有限/受限物理 state space。

## 12. 下一步

1. Relay support corollary 到 A3→A4 bridge；
2. 用 bridge 的 actual cancellation example 计算 hidden step/residue certificate；
3. 给 staged support / split-completeness query分析多个 finite bands 的共同 minimum precision；
4. 把 scalar band certificate 接入 P018 task precision profile；
5. 对 global all-state coarse program，研究 quotient score coset 如何符号化决定 band truth，而不是按 state 枚举。
