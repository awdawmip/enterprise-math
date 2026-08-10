# P023 —— Precision generator rank 的边界，补充 19

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023  
依赖：P023-S15 dependency closure、S14/S17 acquisition cost  
纪律：closure systems、generators、bases 与 rank-like notions 都属于成熟数学。本补充记录一个负边界：generic task closure 不具有 matroid 性，因此在没有额外假设时，coordinate-count “dimension” 不是 intrinsic invariant。

## 1. 为什么 basis count 很诱人

S15 把 task basis 定义为声明 task family `T` 的一个 subset `S`，满足

\[
\operatorname{cl}(S)=\mathcal T.
\]

等价地，`S` 中的 tasks 已经能够生成完整 final joint partition。

很容易因此把某个 minimal basis 的大小叫作 precision state 的“维数”。

在一般 finite theory 中，这样做不成立。

## 2. P023-S19-T01 —— Inclusion-minimal task bases 的基数可以不同

状态：`PROVED BY EXPLICIT COUNTEREXAMPLE`。

取四个 states，带两个 binary coordinates：

\[
A=(0,0,1,1),
\qquad
B=(0,1,0,1),
\]

再加入 bundled four-way task

\[
C=(0,1,2,3)=(A,B).
\]

则

\[
\boxed{
\operatorname{cl}(\{C\})=\{A,B,C\},
}
\]

因为 `C` 能决定两个 binary coordinates。

同时

\[
\boxed{
\operatorname{cl}(\{A,B\})=\{A,B,C\},
}
\]

因为 `(A,B)` 也能决定 `C`。

但 `A` 或 `B` 单独都不能生成完整 joint state。

所以

\[
\boxed{\{C\}}
\]

和

\[
\boxed{\{A,B\}}
\]

都是 inclusion-minimal task bases，而基数分别为 1 与 2。

因此

\[
\boxed{
\text{任意 minimal task basis 的基数不是 invariant}.
}
\]

## 3. 为什么它不是 matroid rank

在 matroid 中，exchange law 会强迫所有 bases 具有相同基数。

S15 已给出 closure-exchange 的直接反例；T01 则给出更操作性的后果：basis cardinality 本身就不固定。

所以 generic precision closure 在没有额外结构时不存在 canonical matroid rank。

任何路线若想使用 rank/dimension theorem，都必须先为自己的 task family 证明 exchange-type axiom。

## 4. Minimum generator number 仍然存在，但它是 language-relative

定义

\[
\boxed{
g(\mathcal T)
=
\min\{|S|:\operatorname{cl}(S)=\mathcal T\}.
}
\]

对有限声明 task family，这当然是一个良定义整数。

但它不是 final joint partition 单独决定的。

在四状态例子中，如果 primitive task language 只有

\[
\{A,B\},
\]

则

\[
\boxed{g=2.}
\]

如果把 bundled coordinate `C=(A,B)` 加入 primitive language，final joint partition 完全不变，但

\[
\boxed{g=1,}
\]

因为 `{C}` 已经成为 basis。

所以 generator number 是**task language 加 dependency closure**的 invariant，而不是 semantic final precision state 自身的 invariant。

## 5. P023-S19-T02 —— 三种不同整数“大小”必须分开

固定整数 base `B>=2` 与 final joint precision `E_*`。

### Semantic final-state depth

\[
\boxed{
D_B(E_*)
=L_B(|X/E_*|).
}
\]

它只依赖 final partition，是给所有 final precision classes 编号的 integer symbol-depth lower bound。

### Generator number

\[
\boxed{
g(\mathcal T)
=
\min\{|S|:\operatorname{cl}(S)=\mathcal T\}.
}
\]

它统计：在固定 task vocabulary 下，最少需要多少个 primitive task coordinates 才能生成 final precision，因此依赖 task language。

### Operational acquisition depth

\[
\boxed{
A_B(\mathcal T)
=
\min_\sigma C_B(\sigma).
}
\]

它是 S14 的 exact minimum sequential symbol depth，依赖 task cardinalities、dependencies、repair factors 与 ordering。

这三个整数回答的是不同问题，不能统一叫作一个 universal “precision dimension”。

## 6. P023-S19-T03 —— Interface overhead 把 semantic depth 与 acquisition depth 分开

S17 定义

\[
\boxed{
H_B(\mathcal T)
=A_B(\mathcal T)-D_B(E_*)\ge0.
}
\]

它表示：通过声明 primitive task interface 获取 final precision 所强迫的最小 overhead。

加入 direct bundled final task 可以改变 `g(T)` 与 `A_B(T)`，却不改变 `D_B(E_*)`。

因此

\[
\boxed{
\text{semantic precision size}
\neq
\text{coordinate generator count}
\neq
\text{acquisition cost in general}.
}
\]

## 7. P023-S19-T04 —— Bundling 是 coordinate-language change，不是 semantic refinement

假设 bundled task `C` 是已有 tasks 的确定函数，并且加入以后没有使 final partition 更细。

把 `C` 加进 primitive language 不改变 `E_*`。

但它可能：

- 减少 minimum generator number；
- 减少 optimal acquisition depth；
- 改变 minimal bases 集合；
- 产生新的 zero-cost dependency closures。

所以 task-coordinate design 是一种独立于 final task semantics 的 representational degree of freedom。

这与 S18 “coordinate normalization 不等于 state-space quotient” 是同一类边界。

## 8. 对“precision dimension”提案的后果

任何 dimension 提案都应该明确它指的是：

1. final class cardinality/depth；
2. 固定 task language 中的 minimum primitive generator 数；
3. 固定 primitive interface 下的 minimum acquisition depth；
4. 另一个单独声明 state geometry 的 graph/geometric dimension。

若不声明，`dimension` 会仅仅因为 vocabulary 中加入一个 bundled coordinate 就改变。

尤其是

\[
\boxed{
\text{某个 minimal basis 的 coordinate 数}
}
\]

不能作为 foundation-level intrinsic invariant。

## 9. 与 P012/P018/P023 的关系

- P012 只有在 primitive adjacency/geometry 被明确声明后，才讨论 intrinsic geometric dimensions；
- P018 提供 precision axes 与 ambiguity，但不把 raw coordinate 数自动升格为 intrinsic dimension；
- P023 提供 task quotient、dependency closure 与 acquisition calculus。

S19 因此封住一个常见 category error：把“方便使用了几个 observables”误当成“它们共同表示的 precision state 的内禀大小”。

## 10. 研究工具规则

在报告一个“precision dimension”之前：

1. 检查 minimal bases 是否等基数；
2. 若想用 matroid/rank 语言，先检查 closure exchange；
3. 比较加入/不加入 bundled coordinates 的 task families；
4. 当 `D_B`、`g(T)`、`A_B(T)` 不同的时候分别报告；
5. 对保持 final partition 不变的 primitive task vocabulary 变化，只把 `D_B` 当作不变的 semantic final-state depth。

## 11. 可执行规范

`tests/test_precision_dependency_closure.py` 加入四状态 family，其 inclusion-minimal bases 为 `{C}` 与 `{A,B}`；并验证在保持 semantic final partition 不变时，加入 bundled coordinate 会把 minimum generator number 从 2 降到 1。

## 12. 前人工作与新颖性纪律

Closure-system bases 与 generator numbers 都属于成熟概念，这里的 nonmatroid counterexample 也是初等构造。

本项目新增价值在于：在 Enterprise Math precision calculus 中，显式拆开 semantic precision depth、task-language generator count 与 exact conditional acquisition depth。
