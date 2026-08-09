# P025 补充 26 —— Block Count Minus Relation Rank：Relation-Conditioned Derivative 的一般维数律

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
依赖：P025 补充 19–25；A3/P023 relation 与 quotient semantics  
Hard block：`NONE`

## 1. 为什么 ABC 会产生二维 block-value state

补充 20–25 中，primitive abc triple 的 block-value quotient 反复出现 rank-two lattice。这不是 Wronskian 特例，也不是数值巧合，而是一个一般有限 relation-rank law 的最初情形。

考虑两两互素的正整数 blocks

\[
\boxed{n_1,\ldots,n_m}
\]

以及有限族整数 additive relations

\[
\boxed{Ln=0,
\qquad L\in\mathbb Z^{r\times m}.}
\]

Pairwise coprimality 保证不同 non-unit blocks 的 prime-coordinate supports 互不重叠。

## 2. Block derivative images

对每个 non-unit block 定义 raw derivative image generator

\[
\boxed{A_i=\gcd_{p\mid n_i}\frac{n_i v_p(n_i)}p>0.}
\]

则 block `i` 的 arithmetic derivative value 满足

\[
t_i\in A_i\mathbb Z.
\]

若 `n_i=1`，derivative value 恒为 0，不贡献 active derivative coordinate。

令 `I` 为 active non-unit block 集，

\[
\boxed{s=|I|,}
\]

并从 relation matrix 删除 unit columns，得到

\[
L_I.
\]

## 3. P025-T75 —— exact block-value relation lattice

Arithmetic derivative 的线性性把每条 declared relation

\[
\sum_iL_{ji}n_i=0
\]

运输成

\[
\sum_iL_{ji}t_i=0.
\]

所以 compressed block-value state 精确为

\[
\boxed{
\Lambda_{L,A}
=
\left(\prod_{i\in I}A_i\mathbb Z\right)
\cap\ker_{\mathbb Z}(L_I).
}
\]

每个 fine relation-adapted witness 都映入该 lattice。

反过来，该 lattice 的每个点都可在互不重叠的 blocks 内独立选择 prime-coordinate preimages；kernel condition 保证这些 preimages 合并后满足全部 derivative relations。因此 fine witness family 满射到 `Lambda_(L,A)`。

## 4. P025-T76 —— compressed rank = active block count − relation rank

写

\[
D_A=\operatorname{diag}(A_i)_{i\in I}.
\]

每个 compressed state 可写成

\[
t=D_Ax,
\qquad x\in\mathbb Z^s,
\]

并满足

\[
L_ID_Ax=0.
\]

因为 `D_A` 在 `Q` 上可逆，

\[
\operatorname{rank}_{\mathbb Q}(L_ID_A)=\operatorname{rank}_{\mathbb Q}(L_I).
\]

因此

\[
\boxed{
\operatorname{rank}_{\mathbb Z}\Lambda_{L,A}
=s-\operatorname{rank}_{\mathbb Q}L_I.
}
\]

该 rank 由 active block 数与独立 relation directions 决定，而不是由 blocks 内部总 prime-coordinate 数决定。

## 5. ABC 是第一种情形

普通 non-unit abc triple 有

\[
L=(1,1,-1),
\]

所以

\[
s=3,
\qquad\operatorname{rank}L=1,
\]

从而

\[
\boxed{\operatorname{rank}\Lambda_{abc}=3-1=2.}
\]

这解释了补充 20–25 的 rank-two ceiling。

对 unit boundary `1+b=c`，先删掉 unit block，只剩两个 active blocks 与 restricted row `(1,-1)`，故

\[
\boxed{\operatorname{rank}=2-1=1.}
\]

这正是 unit Wronskian/floor state 只剩一个共同 derivative value 的原因。

## 6. Fine prime coordinates 很多，全局仍可只有 rank two

考虑

\[
\boxed{6+35=41.}
\]

三个 blocks 两两互素，其 fine prime supports 为

\[
\{2,3\},\quad\{5,7\},\quad\{41\},
\]

共有五个 prime-coordinate directions。

但 active blocks 只有 3 个，独立 relation 只有 1 条，因此

\[
\boxed{5\text{ fine prime coordinates}\longrightarrow2\text{ global block relation directions}.}
\]

这是 exact structural reduction，不是近似。

## 7. 多条独立 relations 会继续降维

取 blocks

\[
(1,2,3,5)
\]

并声明

\[
1+2=3,
\qquad2+3=5.
\]

删除 unit block 后，active derivative variables 对应 `(2,3,5)`；restricted relation rows 为

\[
(1,-1,0),
\qquad(1,1,-1),
\]

其 rational rank 为 2。因此

\[
\boxed{\operatorname{rank}\Lambda=3-2=1.}
\]

例如 derivative-value state

\[
(0,1,1,2)
\]

同时满足两条 relations。

## 8. P025-T77 —— 一般 relation system 的 certificate rank ceiling

若 future certificate family 只线性依赖 block derivative values：

\[
H:\Lambda_{L,A}\to\mathbb Z^q,
\]

则自动有

\[
\boxed{
\operatorname{rank}_{\mathbb Q}H(\Lambda_{L,A})
\le s-\operatorname{rank}_{\mathbb Q}L_I.
}
\]

因此 Stage 25 的 rank-two certificate ceiling 只是 abc 特化。

## 9. 架构后果

一般 compression chain 为

\[
\boxed{
\text{blocks 内 fine prime coordinates}
\to
\text{每个 active block 一个 derivative value}
\to
\ker(L_I)
\to
\text{certificate/decision quotient}.
}
\]

决定性维数是

\[
\boxed{\text{active block count}-\text{independent relation rank}.}
\]

这分开了两个层面：

- block 内部 arithmetic complexity 可由补充 19 证明为任意丰富；
- global relation coupling 仍可拥有很低 rank。

## 10. Scope 边界

Pairwise coprimality 对简单 surjective product argument 是必要的，因为它确保 prime-coordinate supports 互不重叠。若 blocks 共享 primes，fine derivative coordinates 在 relation matrix 之前就已经耦合；本定理不会悄悄把这种 overlap 丢掉。

同样，若 future operations 读取 block 内 witness identity 或非线性 observables，需要更细的 language-specific state。

## 11. Prior-art 边界

Kernel dimension、rank-nullity、`Q` 上 diagonal scaling 与 disjoint coordinate sets 的 direct product 都是标准 linear algebra/module facts。

P025 不对这些数学本身作创新主张。项目侧候选是 arithmetic-derivative block compression 及其作为有限 precision dimension law 的使用。

因为结果已超出 abc，应 Relay 给 A3/P023 做 ownership audit，而不是静默提升成 P025 Foundation theorem。

## 12. 可执行资产

新增：

- `src/enterprise_math/relation_block_rank.py`
  - pairwise-coprime relation-block system validation；
  - exact rational matrix rank；
  - active block/image-generator state；
  - compressed rank calculation；
  - exact derivative-value lattice membership；
  - generic certificate rank ceiling。
- `tests/test_relation_block_rank.py`
  - ordinary abc rank two；
  - unit abc rank one；
  - `6+35=41` five-prime-coordinate reduction；
  - 两条独立 relations 留一个方向；
  - 四个 active blocks 一条 relation 留 rank three。

## 13. 下一前沿

没有 hard block。继续：

1. 量化 certificate family 相对于 relation rows 真正增加的 **rank gain**；
2. 把 P023-coarsest exact certificate quotient 识别成 relation kernel 的 image；
3. 从一条 relation 扩展 access-cost/Pareto semantics 到多 relations；
4. 研究 shared-prime blocks，作为 independent-block product model 的第一真实失败边界；
5. 在任何 Foundation 考虑前先把 dimension law Relay 给 A3/P023。
