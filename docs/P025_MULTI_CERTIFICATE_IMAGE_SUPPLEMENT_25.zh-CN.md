# P025 补充 25 —— 任意多个 Block-Linear Certificates 的 Rank-Two 上限

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
依赖：P025 补充 20–24；P023 future-language precision  
Hard block：`NONE`

## 1. 给 future language 同时加入很多证书

补充 20 已证明，当前 additive witness language 精确下沉到 compressed block-value lattice

\[
\Lambda_{abc}\subseteq\mathbb Z^2.
\]

现在让 future language 同时包含任意有限族整数线性 certificate observables：

\[
\boxed{
\ell_j(u,v)=r_j u+s_j v,
\qquad j=1,\ldots,q.
}
\]

把它们合成

\[
\boxed{H:\Lambda_{abc}\to\mathbb Z^q.}
\]

输出 certificate coordinates 的数量 `q` 可以任意大，但底层独立 relation-state rank 不会随之增长。

## 2. P025-T73 —— certificate image rank 至多为二

令 `g_1,g_2` 是 non-unit rank-two compressed lattice 的任意 basis；unit boundary 只有一个 basis vector。

Labeled certificate image 由

\[
\boxed{H(g_1),\ H(g_2)\in\mathbb Z^q}
\]

生成。

所以

\[
\boxed{
\operatorname{rank}_{\mathbb Q}H(\Lambda_{abc})
\le
\operatorname{rank}_{\mathbb Z}\Lambda_{abc}
\le2.
}
\]

因此继续增加 block-linear certificates 不会产生新的独立 relation-state directions。可以增加更多有标签输出，但它们都活在 rank-at-most-two 的整数 image 上。

## 3. P025-T74 —— full certificate rank 已经 block-value complete

若三个 blocks 都非 unit，则 `Lambda_abc` rank 为 2。若 joint certificate map 的 rational rank 也为 2，则它的线性扩展

\[
H:\mathbb Q^2\to\mathbb Q^q
\]

为 injective，所以限制到 `Lambda_abc` 仍然 injective。

因此

\[
\boxed{
\operatorname{rank}_{\mathbb Q}H=2
\Longrightarrow
\text{完整 labeled certificate vector 唯一决定 }(u,v).
}
\]

在 unit rank-one boundary 中，只要 certificate image 非零，就对这一维 lattice 同样 injective。

所以一旦已经存在两个 rationally independent 的 block-linear certificate directions，再加入第三、第四乃至更多线性证书，都不能继续细分 block-value state。它们仍可用于不同阈值任务，但不会增加底层 exact state partition 的独立维数。

## 4. 两个独立 certificate rows 的显式恢复

对两行

\[
(r_1,s_1),
\qquad(r_2,s_2)
\]

若

\[
\Delta=r_1s_2-r_2s_1\ne0,
\]

观测值为 `y_1,y_2`，则 Cramer rule 给出

\[
\boxed{
 u=\frac{y_1s_2-y_2s_1}{\Delta},
\qquad
 v=\frac{r_1y_2-r_2y_1}{\Delta}.
}
\]

对已知来自实际 certificate image 的 vector，这两个有理式精确恢复原整数 block-value state。

例如 `2+3=5` 中，取 Wronskian row `(-3,2)` 再加 `(1,1)`，determinant 为 `-5`，所以 `(W,u+v)` 已经构成 block-value state 的完整坐标系。

## 5. P025-D15 —— Smith/determinantal image invariants

令 basis-image matrix 的两列为

\[
y_1=H(g_1),
\qquad y_2=H(g_2)
\]

位于 `Z^q`。

标准 determinantal divisors 给出 abstract Smith invariant factors。

令

\[
\delta_1=\gcd\{y_1,y_2\text{ 的全部 entries}\}.
\]

若全部 `2x2` minors 为零，则 image rank 为 1，唯一非零 Smith factor 为 `delta_1`。

否则令

\[
\delta_2=\gcd\{\text{全部 }2\times2\text{ minors}\}.
\]

则 rank-two invariant factors 为

\[
\boxed{
(d_1,d_2)=\left(\delta_1,\frac{\delta_2}{\delta_1}\right).
}
\]

这些都是标准 Smith-normal-form 事实，不属于 P025 新数学。

## 6. P025-N09 —— Smith factors 不能决定 labeled certificate image

若 future language 给每个 certificate coordinate 固定含义，那么 abstract invariant factors 太粗。

取 prime triple

\[
2+3=5,
\]

此时

\[
\Lambda_{235}=\mathbb Z^2.
\]

比较两套 two-certificate maps：

\[
H_1(u,v)=(u,2v),
\]

与

\[
H_2(u,v)=(u,u+2v).
\]

两者 Smith invariant factors 都是

\[
\boxed{(1,2).}
\]

但 labeled images 不同：

\[
H_1(\mathbb Z^2)=\{(x,y):y\equiv0\pmod2\},
\]

而

\[
H_2(\mathbb Z^2)=\{(x,y):y\equiv x\pmod2\}.
\]

Labeled target

\[
\boxed{(1,0)}
\]

属于第一 image，却不属于第二 image。

因此

\[
\boxed{
\text{相同 Smith invariants}
\not\Rightarrow
\text{相同 labeled certificate language}.
}
\]

若 future queries 关心具体 certificate coordinates，必须保留 labeled image generator/HNF-style state，而不是只保留 abstract Smith factors。

## 7. 与 Wronskian-only precision 的关系

单个 Wronskian observable 在 rank-two block-value lattice 上 rank 只有 1，因此故意忘掉一条 rational direction。这条被忘方向正是为什么单个 Wronskian value 不能恢复完整 additive state，以及为什么 Stage 22 的 `W=D` fiber 是一条 affine line。

加入一个独立 block-linear observable 后，joint rank 提升到 2，每个 certificate fiber 立即缩成单个 block-value point。

所以

\[
\boxed{
\text{一条 certificate direction}
\to
\text{两条独立 directions}
}
\]

与继续添加第三、第四、第一百个 dependent observable 有本质区别。

## 8. 架构后果

对 block-linear certificate language 存在一个硬 representation ceiling：

\[
\boxed{
\text{certificate 输出数量}
\not=\text{独立 precision dimension},
\qquad
\text{独立维数}\le2.
}
\]

这不是任意 dimensionality reduction，而是 relation-state quotient 的直接结果。

真正的状态层级为

\[
\boxed{
\Lambda_{abc}
\xrightarrow{H}
\text{labeled rank-}\le2\text{ certificate image}
\to
\text{task-specific threshold/decision quotient}.
}
\]

最后一步仍由 P023 拥有：若 future 只问 certificate vector 的 threshold predicates，完整 labeled image 本身还可能过细。

## 9. Prior-art 边界

Smith normal form、determinantal divisors、Cramer rule、整数线性映射 rank 与 full-column-rank injectivity 都属于标准数学。

P025 不对这些内容主张创新。项目侧继续检验的是：它们在 arithmetic block-value quotient 之后的精确位置，以及由此得到的 block-linear future language 独立状态维数上限。

该 packaged interface 的历史创新状态仍为 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

新增：

- `src/enterprise_math/abc_multi_certificate.py`
  - labeled certificate evaluation；
  - 从 compressed lattice basis 得到 image generators；
  - rational rank 与 Smith invariant factors；
  - full-rank injectivity test；
  - two-row explicit recovery；
  - same-Smith/different-labelled-image counterexample。
- `tests/test_abc_multi_certificate.py`
  - 任意多个 certificates 仍 rank<=2；
  - Wronskian + 一个独立 form 恢复 state；
  - dependent-family boundary；
  - unit rank-one boundary；
  - labeled Smith counterexample。

## 11. 下一前沿

没有 hard block。继续：

1. 把 exact certificate values 换成 finite threshold languages，计算 P023-minimal block-value quotient；
2. 同时研究多个 certificate costs，在 rank-two state compression 之后形成有限高维 antichain；
3. 判断“一条 Wronskian + bounded witness parameter”和“再加一条独立 certificate”之间的 representation cost tradeoff；
4. 把 image-rank 分析推广到拥有多条 additive relations 的 relation-conditioned systems，此时 compressed relation-state rank 可以超过 2；
5. 后续工具中始终区分 labeled-image state 与 abstract Smith-module state。
