# P025 补充 33 —— Relation Generation 的有限 Rank/Index Profile

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-shared-access-stage30`  
依赖：P025 补充 31–32  
Hard block：`NONE`

## 1. `rho_gen` 只是有限响应的终点

对 relation lattice `Lambda`，定义

\[
\boxed{
\Gamma_R
=
\langle Z_R(B)\cap\Lambda\rangle.
}
\]

因为

\[
Z_R(B)\subseteq Z_{R+1}(B),
\]

所以生成子群形成 nested chain：

\[
\boxed{
\Gamma_R\subseteq\Gamma_{R+1}\subseteq\Lambda.
}
\]

Stage 32 把 `rho_gen` 定义为第一次 `Gamma_R=Lambda` 的半径，但中间 subgroups 本身还携带精确的有限 precision 信息。

## 2. P025-T90 —— generated rational rank 单调不降

令

\[
r_R=\operatorname{rank}_{\mathbb Q}\Gamma_R.
\]

Nested subgroups 直接给出

\[
\boxed{r_R\le r_{R+1}.}
\]

定义 **full-rank radius**

\[
\boxed{
\rho_{\rm rank}
=
\min\{R:r_R=\operatorname{rank}\Lambda\}.
}
\]

这是当前可访问 relation states 第一次张成全部 rational relation directions 的半径。

但它仍可能早于 integer generator completeness。

## 3. P025-T91 —— finite indices 形成 divisibility chain

对 `R>=rho_rank` 定义

\[
\boxed{I_R=[\Lambda:\Gamma_R]<\infty.}
\]

由于

\[
\Gamma_R\subseteq\Gamma_{R+1}\subseteq\Lambda,
\]

普通 subgroup-index multiplication 给出

\[
I_R
=
[\Lambda:\Gamma_{R+1}]
[\Gamma_{R+1}:\Gamma_R].
\]

因此

\[
\boxed{I_{R+1}\mid I_R.}
\]

所以 finite index 不只是数值单调不增，而是满足更强的整除下降。

终点为

\[
\boxed{I_{\rho_{\rm gen}}=1.}
\]

## 4. P025-D21 —— strict rank/index profile

在 full rank 之前把 `I_R` 视为 infinity。只在 pair

\[
\boxed{(r_R,I_R)}
\]

发生变化的半径记录状态。

这样得到一条从第一次 nonzero relation state 到 generator completeness 的有限 strict-change profile。

它区分四个可能阶段：

1. 没有 nonzero relation state；
2. nonzero 但 rationally rank-deficient subgroup；
3. full rational rank，但 finite index `>1`；
4. full integral generator completeness，index `1`。

具体系统可以跳过其中若干阶段。

## 5. P025-T92 —— finite index-drop count bound

假设第一次 full-rank layer 的 index 为

\[
I_0>0.
\]

之后每次严格 finite-index 变化都会把当前 index 替换成一个 proper positive divisor，而正整数的 proper divisor 至多是其一半。

所以 distinct finite-index levels 的数量至多为

\[
\boxed{\operatorname{bitlength}(I_0).}
\]

这只是 strict index states 数量的有限组合界，不是构造 reachable layers 的 complexity bound。

## 6. Exact arithmetic example `1+22=23`

取 unit relation basis

\[
\boxed{g=(0,1,1).}
\]

radius 2 时可访问 common derivative scales 为 `0,±2`，所以 generated coordinate subgroup 为

\[
2\mathbb Z.
\]

此时 relation rank 已经 full：

\[
\boxed{\rho_{\rm rank}=2,}
\]

但

\[
\boxed{I_2=2.}
\]

radius 3 subgroup 不变。

radius 4 时 scale `3` 也可访问，scale `2` 与 `3` 一起生成 `Z`，因此

\[
\boxed{I_4=1,\qquad\rho_{\rm gen}=4.}
\]

Strict profile 为

\[
\boxed{
(2;\ r=1,I=2)
\longrightarrow
(4;\ r=1,I=1).
}
\]

这是实际 arithmetic relation 中“full rational information 严格早于 integral generator completeness”的样本。

## 7. `1+8=9` 跳过 finite-index intermediate layer

radius 2 时 primitive common derivative step 已直接可访问，所以

\[
\boxed{
\rho_{\rm rank}=\rho_{\rm gen}=2,
\qquad I_2=1.
}
\]

Strict profile 只有一个 nonzero point。

## 8. Rank-two `2+3=5` 也在 radius 1 立即 complete

两根标准 relation basis vectors radius 1 已可访问，因此

\[
\boxed{
\rho_{\rm rank}=\rho_{\rm gen}=1,
\qquad I_1=1.
}
\]

同样没有 finite-index defect layer。

## 9. 架构后果

Generation-completeness state 不能只用 rank 总结。

更忠实的 discrete precision ladder 是

\[
\boxed{
\text{accessible relation states}
\to
\text{rational span rank}
\to
\text{integral subgroup index}
\to
\text{index-one completeness}.
}
\]

Rank 只问是否已经看见所有 rational directions；index 进一步问 finite integral congruence obstruction 是否也已消除。

这与此前多条 Enterprise Math 区分相呼应：

- rational/free-rank 信息 vs torsion/congruence detail；
- support existence vs exact witness multiplicity；
- coarse span completeness vs exact integer-state completeness。

## 10. Prior-art / ownership 边界

Nested subgroup indices、finite index 的 divisibility 与 maximal-minor lattice index 都属于标准 algebra。

P025 不对它们本身主张创新。项目侧继续检验的是 arithmetic derivative-image access 所诱导的 radius-indexed finite precision profile。

该结果应 Relay 给 A3/P023，作为 worked relation-precision coordinate；generic subgroup-index theory 仍属于 prior art。

## 11. 可执行资产

新增：

- `src/enterprise_math/relation_generation_profile.py`
  - strict rank/index profile；
  - monotonicity/divisibility assertions；
  - first nonzero、full-rank、generator radii；
  - finite index-drop count bound。
- `tests/test_relation_generation_profile.py`
  - `1+22=23` full-rank/index-two intermediate state；
  - `1+8=9` immediate completeness；
  - rank-two abc immediate completeness；
  - long-basis invariance；
  - shared-prime rank-one boundary。

## 12. 下一前沿

没有 hard block。继续：

1. 寻找 higher-rank arithmetic example，使 `rho_rank<rho_gen`；
2. 找到不保留全部 accessible states 也能表示 index defect 的有限 quotient data；
3. 把该 index profile 与 A3 quotient-module torsion coordinates 对照；
4. 研究 certificate rank gain 是否也应附带 finite certificate-image index defect；
5. 在打开新的下一代研究 branch 前，冻结 Stage30–33 做 checkpoint。
