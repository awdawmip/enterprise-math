# P019 补充 06 —— 值结合律与见证非结合性

状态：`RESEARCH WIP / COUNTEREXAMPLE PRESERVED`

## 1. 区分两个层级

Supplement 04/05 已证明 block energy 的 min-plus 合成满足

\[
\Psi_{a+b,s}=\Psi_{a,s}\square\Psi_{b,s},
\]

因此 value / minimum energy 对 block grouping 满足结合律。

但这不能推出逐层 boundary lift 的 exact witness 也与 grouping 无关。

## 2. 最小反例

取四个原始 unit slots、`s=2`、threshold `T=16`，最终都收缩成一个 block。

对链式 contraction tree

\[
(((1+1)+1)+1)
\]

按每层指定有向 channel 的唯一右端穿界 witness 反向 lift，得到

\[
\boxed{(2,1,0,-3)}.
\]

对平衡 contraction tree

\[
(1+1)+(1+1)
\]

同样规则得到

\[
\boxed{(2,2,-2,-2)}.
\]

两者不是简单 permutation，也不是全局取负再 permutation 可互换的同一坐标模式。

因此

\[
\boxed{
\text{value associativity}
\not\Rightarrow
\text{witness associativity}.
}
\]

## 3. 与 P021 的接口

这与 P021 direction-transport 的安全降维原则完全一致：aggregated cardinality/value 可以复合，不代表 exact middle witness identity 已被保留。

对 P019 contraction：

- 若后续只需要 minimum energy、ball count 或 block capacity，最终 block-size partition 足够；
- 若后续还要精确复合 boundary witness、direction history、causal path 或局部 incidence，则 contraction tree / witness relation 不能自动删除。

因此低维状态至少存在两个精度层：

`coarse contracted state = visible totals + block sizes`

`composition-complete contracted state = coarse state + contraction/witness trace`。

这给出一个新的安全规则：

> 只有在证明未来运算对 contraction history 不敏感时，才允许把 witness trace 压缩成单纯 block-size/cardinality shadow。

## 4. 下一步

1. 定义 typed `ContractionTrace`，避免把树历史混入普通数值；
2. 分类哪些 observables 只依赖最终 partition，哪些依赖 contraction tree；
3. 检验不同树产生的 witness 是否至少落在同一 automorphism orbit；当前四槽反例已否定最简单的 permutation/sign 等价，但完整图自同构分类仍需做；
4. 与 P021 witness relation 的 join 语义统一，避免重复造结构。
