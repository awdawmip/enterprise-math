# P025 补充 27 —— Certificate Precision Dimension 作为 Augmented Relation-Rank Gain

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
依赖：P025 补充 25–26；P023 exact certificate quotient semantics  
Hard block：`NONE`

## 1. 用输出数量衡量 precision 是错误的

补充 26 给出 relation-conditioned block-value state

\[
\Lambda_{L,A}
\]

其 rational rank 为

\[
s-\operatorname{rank}L,
\]

其中 `s` 为 active block 数。

现在加入有限族 exact block-linear certificates，组成 matrix

\[
H.
\]

`H` 的 rows 可以很多，但真正新增的 precision 是它们在 relation-state 中实际切掉多少独立方向。

## 2. P025-T78 —— exact certificate rank-gain formula

令

\[
K=\ker_{\mathbb Q}L\subseteq\mathbb Q^s.
\]

Certificate family 限制到

\[
H|_K:K\to\mathbb Q^q.
\]

则

\[
\boxed{
\operatorname{rank}(H|_K)
=
\operatorname{rank}
\begin{pmatrix}L\\H\end{pmatrix}
-
\operatorname{rank}L.
}
\]

### 证明

Combined map

\[
x\mapsto(Lx,Hx)
\]

的 kernel 为

\[
\ker L\cap\ker H.
\]

因此

\[
\operatorname{rank}[L;H]
=s-\dim(\ker L\cap\ker H).
\]

同时

\[
\operatorname{rank}L=s-\dim\ker L.
\]

两式相减得到

\[
\dim\ker L-\dim(\ker L\cap\ker H),
\]

这正是 `H` 限制到 `ker L` 后的 rank。∎

定义 **certificate rank gain**

\[
\boxed{\Delta_H=\operatorname{rank}[L;H]-\operatorname{rank}L.}
\]

## 3. P025-T79 —— residual exact-certificate fiber rank

Exact certificate vector 把两个 relation states 视为相同，当且仅当它们差值属于

\[
\ker L\cap\ker H.
\]

所以 certificate family 尚未看见的 residual rational rank 为

\[
\boxed{
\operatorname{rank}_{\rm residual}
=(s-\operatorname{rank}L)-\Delta_H.
}
\]

等价地，

\[
\boxed{
\operatorname{rank}_{\rm residual}=s-\operatorname{rank}[L;H].
}
\]

因此 certificate rank gain 是相对于已声明 relation state 的 exact dimension-level refinement measure。

## 4. 两个端点判据

### Relation-redundant certificate family

\[
\boxed{\Delta_H=0}
\]

当且仅当 certificates 对 relation kernel 不增加 rational distinction。特别地，落在 `L` rational row span 中的 certificate rows 在 relation states 上恒为零。

### Block-value complete certificate family

\[
\boxed{\Delta_H=s-\operatorname{rank}L}
\]

当且仅当 residual certificate fiber rank 为零。此时完整 exact labeled certificate vector 在 rational relation state 上 injective，因而也在整数 compressed lattice 上 injective。

这推广了 Stage 25 的 rank-two completeness criterion。

## 5. ABC 校准

对 non-unit abc triple，

\[
L=(1,1,-1),
\qquad s=3,
\qquad\operatorname{rank}L=1.
\]

### 一个 Wronskian

Block-value Wronskian row 为

\[
H_W=(-b,a,0).
\]

它与 `L` 独立，所以

\[
\operatorname{rank}[L;H_W]=2
\]

并且

\[
\boxed{\Delta_{H_W}=1.}
\]

因此一个 Wronskian 只删除两个 block-value directions 中的一个，留下 rank-one fiber。Stage 22 的 affine floor line 正是固定 Wronskian value 后的这一 residual fiber。

### Wronskian 加一条独立 certificate

对 `2+3=5` 再加 certificate `t_a`，row 为

\[
(1,0,0).
\]

则

\[
\operatorname{rank}
\begin{pmatrix}
1&1&-1\\
-3&2&0\\
1&0&0
\end{pmatrix}=3.
\]

因此

\[
\boxed{\Delta_H=2}
\]

且 residual fiber rank 为零：`(W,t_a)` 已恢复完整 block-value state。

### 很多 dependent Wronskians

Rows

\[
H_W,
\ 2H_W,
\ -7H_W
\]

仍然只有

\[
\boxed{\Delta_H=1,}
\]

而不是 3。Output count 与 precision-rank gain 是不同量。

## 6. Unit abc boundary

对 `1+b=c`，删掉 unit block 后只有两个 active variables 与一条 `(1,-1)` relation，因此 compressed rank 为 1。

任何在这条 line 上非零的 certificate direction 都有 rank gain 1，并且 block-value complete。

这解释了为什么 unit relation 中一个共同 derivative/Wronskian value 就能完整参数化 relation state。

## 7. 多 relation 校准

对 blocks `(1,2,3,5)` 与 relations

\[
1+2=3,
\qquad2+3=5,
\]

有三个 active blocks、relation rank 2，只剩一个 derivative-value direction。

任何在该方向上非零的 certificate row 都有

\[
\boxed{\Delta_H=1}
\]

并已 complete，不管还附带多少 dependent outputs。

## 8. 架构后果

对 exact block-linear certificate languages，真正自然的 precision-dimension increment 是

\[
\boxed{\Delta_H=\operatorname{rank}[L;H]-\operatorname{rank}L,}
\]

而不是 certificate 输出数量、ambient prime-coordinate 维数、某个 generator list 大小或 universal scalar precision level。

它给出一个 compact relation-relative accounting rule：

\[
\boxed{
\text{declared relations}
\to
\text{remaining relation kernel}
\to
\text{certificate rank gain}
\to
\text{residual hidden directions}.
}
\]

这只是 dimension-level theorem。Integer torsion、labeled image constraints、access costs 与 threshold semantics 仍可区分 rank gain 相同的系统。

## 9. P023 ownership 边界

Exact certificate quotient 本身就是 image

\[
H(\Lambda_{L,A}),
\]

其 kernel relation 是 full certificate vector 的 coarsest exact equivalence。这属于 P023/general quotient factorization/minimal-repair 原理。

因此 P025 应把 rank-gain formula 作为 reusable relation-specific coordinate Relay 出去，而不是另称新的 generic quotient theorem。

## 10. Prior-art 边界

Rank-nullity、stacked-matrix rank identities、restricted linear-map rank 与 quotient-kernel dimension 都是标准 linear algebra。

P025 不对这些内容主张创新。项目侧候选是它们在 arithmetic block-value compression 后作为 precision-dimension accounting layer 的 exact 使用。

该结果应先 Relay 给 A3/P023 做 ownership audit。

## 11. 可执行资产

新增：

- `src/enterprise_math/relation_certificate_rank.py`
  - exact augmented rank gain；
  - residual certificate-kernel rank；
  - relation-redundant / block-complete flags；
  - abc Wronskian row helper。
- `tests/test_relation_certificate_rank.py`
  - one Wronskian gain one；
  - dependent certificate multiplicity；
  - Wronskian + independent certificate completeness；
  - relation-row redundancy；
  - unit 与 multiple-relation boundaries。

## 12. 下一前沿

没有 hard block。继续：

1. 把 Stage 26 推出 pairwise-coprime scope，处理 shared primes 在 relation 之前对 block derivative values 的耦合；
2. exact certificate values 下，用 integer image/torsion 与 labeled-image 数据细化 rank gain；
3. 给 residual certificate fibers 附加 access-cost profiles；
4. 检验 rank gain + access cost 是否能支持 adaptive certificate selection，但不把 dimension 与 total proof cost 混淆；
5. 把 rank law/gain pair Relay 给 A3/P023 作为候选 reusable research tool。
