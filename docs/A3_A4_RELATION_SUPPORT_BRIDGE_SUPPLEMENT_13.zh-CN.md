# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 13

状态：`ACTIVE RESEARCH NOTE`  
范围：count semantics 到 existence semantics 与 Pareto budget semantics 的可复合投影

## 1. 为什么这一阶段重要

Bridge 目前已经形成多层状态：

- exact witness identities；
- non-negative-integer count matrices/tensors；
- boolean support relations；
- Pareto budget frontiers；
- selected truth bits。

本文件检验这些中间投影是否只是 lossy summary。对声明好的 future language，它们实际上是**可复合 semantic shadows**：先投影再复合，和先复合再投影得到相同结果。

其中 non-negative coefficient 假设是必要条件。

## 2. B53 — positive-support map 是 semiring homomorphism

定义

\[
\sigma:\mathbb N\to\mathbb B
\]

为

\[
\sigma(n)=1[n>0].
\]

则

\[
\boxed{
\sigma(a+b)=\sigma(a)\lor\sigma(b),
\qquad
\sigma(ab)=\sigma(a)\land\sigma(b).
}
\]

并且 `sigma(0)=false`、`sigma(1)=true`。

因此 positive support 是 natural-number semiring 到 Boolean semiring 的 homomorphism。

这是标准代数；在这里的重要性是 `N` 中不存在 coefficient cancellation。

## 3. B54 — count composition 精确投影到 relation composition

令 `A,B` 为 non-negative-integer matrices，`supp(A)` 为它们 entrywise positive-support relation。

则

\[
\boxed{
\operatorname{supp}(AB)
=
\operatorname{supp}(A)\circ\operatorname{supp}(B).
}
\]

因为

\[
(AB)_{xz}>0
\iff
\sum_y A_{xy}B_{yz}>0
\iff
\exists y:A_{xy}>0\land B_{yz}>0.
\]

归纳得到任意 finite count-operation word：

\[
\boxed{
\operatorname{supp}(M_1\cdots M_k)
=
\operatorname{supp}(M_1)\circ\cdots\circ\operatorname{supp}(M_k).
}
\]

所以 boolean A4 existence 是更丰富 non-negative-integer witness-count algebra 的精确 compositional shadow。

## 4. B55 — graded count support 精确投影为 achievable cost sets

固定 stage depth，令 exact count tensor 为

\[
H(\mathbf a)\in\mathbb N,
\]

其中 `a` 是 stage-cost vector。

定义 positive coefficient support：

\[
S(H)=\{\mathbf a:H(\mathbf a)>0\}.
\]

在 coefficient convolution 下，positive support 满足

\[
\boxed{
S(H^{(p)}\ast H^{(q)})
=
\bigcup_y
\{u\Vert v:u\in S(H^{(p)}_{xy}),\ v\in S(H^{(q)}_{yz})\}.
}
\]

原因是 convolution coefficients 是 non-negative products 的和；coefficient >0 当且仅当至少存在一个 represented prefix/suffix pair 贡献。

所以 path-cost support layer 同样是 count layer 的 compositional shadow。

## 5. B56 — Pareto projection 与 future composition 交换

对有限 cost set `S subset N^k`，定义

\[
\pi(S)=\operatorname{ParetoMin}(S).
\]

Stage 08 已证明，若 `u<=v`，则对任意 suffix `w` 都有 `u||w<=v||w`。因此 dominated costs 在 future concatenation 后永远不会重新变成 nondominated。

所以

\[
\boxed{
\pi(S\star T)
=
\pi(\pi(S)\star\pi(T)),
}
\]

其中 `star` 表示通过 intermediate states 做 path-cost concatenation 后取 union。

在 matrix 层面，这正是 antichain convolution theorem：

\[
\boxed{
F^{(p+q)}
=F^{(p)}\star F^{(q)}.
}
\]

所以 existence-budget state 可以 online compression，而不需要先恢复更丰富的 count tensor。

## 6. Commuting semantic-shadow diagram

对 generated staged-support language，目前得到 compositional chain：

\[
\boxed{
\text{labeled paths}
\to
H^{(k)}\in\mathbb N^{(\mathbb N^k)}
\to
S^{(k)}
\to
F^{(k)}
\to
\text{budget truth}.
}
\]

相关 operations 与这些 projections 交换：

- labeled-path concatenation → coefficient convolution；
- coefficient convolution → positive-support concatenation；
- positive-support concatenation → Pareto antichain convolution；
- antichain state → 通过 dominance 精确回答 budget truth。

因此每个更低层都是一个对自己较弱 observable language 数学闭合的 machine。

## 7. B57 — equitable count quotient 自动给出 existence quotient

假设某 witness partition 对 non-negative-integer count matrix `M` equitable，quotient matrix 为 `Q_M`。

对任意 source coarse cell `a` 与 target coarse cell `b`：

\[
Q_M(a,b)>0
\]

当且仅当 `C_a` 中每个 fine source state 至少有一条 positive-weight transition 进入 `C_b`。

所以对 quotient count matrix 做 booleanization，就得到精确 coarse block-existence relation。

对于 equitable operation family，

\[
\operatorname{supp}(Q_{M_1}\cdots Q_{M_k})
\]

就是 operation word 后的精确 block-existence relation。

所以 count-lumpability 一旦证明，existence closure 作为更低层 homomorphic shadow 自动获得。

## 8. Shadow maps 的严格不可逆性

这些箭头一般不能反演：

- boolean support 无法恢复 positive count magnitudes；
- Pareto frontier 无法恢复 dominated achievable costs；
- truth bit 无法恢复 frontier；
- block quotient 无法恢复 erased witness identities。

前面各阶段已有明确 counterexamples 见证这些信息丢失。

当 declared future language 不读取这些信息时，这并不是缺陷，而正是合法 collapse 的目标。

## 9. B58 — non-negative coefficients 是 contract 的一部分

positive-support homomorphism 依赖没有 cancellation。

在 signed integer weights 上，可以出现多个 nonzero contributing paths 的 algebraic sum 等于零；这时

\[
\operatorname{supp}(AB)
\]

未必等于 entrywise nonzero supports 的 Boolean composition。

所以 count→existence shadow theorem 只适用于**non-negative witness multiplicities/counts**，不适用于任意 signed relation amplitudes。

这一边界尤其重要，因为 A3 weighted relation field `Z` 是 signed。不能类比 count incidence 去直接 booleanize signed `Z` algebra。

## 10. 架构后果

Bridge 现在明确暴露出两种完全不同 algebraic role：

1. **signed A3 relation coordinates**：保留 cancellation/orientation 信息，使用自己的 quotient rules；
2. **non-negative witness/count coefficients**：允许精确 positive-support 与 Pareto semantic shadows。

这进一步说明 A3 与 A4 不能仅因为都使用 matrix/relation-like language 就合并。

## 11. Prior-art discipline

Semiring homomorphism、non-negative path algebra 的 Booleanization、weighted automata、provenance semiring 与 Pareto/idempotent path algebra 都已有成熟 prior art。

当前 project-specific value 是把这条 commuting state-reduction chain 精确放入已经建立的 A3→A4→P023 bridge，并用 signed/non-negative 边界阻止错误的 cross-algebra 类比。

## 12. Executable audit

Bridge test layer 比较有限例子中的：

- natural-number matrix product 的 positive support 与 Boolean relation composition；
- coefficient convolution 的 positive support 与 achievable cost concatenation；
- full composition 后 Pareto projection 与已压缩 antichain convolution；
- equitable quotient count words 与其 booleanized block-support shadows。
