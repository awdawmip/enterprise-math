# P025 补充 124 —— Witness-Count Value Precision

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-witness-count-stage121`  
依赖：P025 补充 116–123  
硬阻断：`NONE`

## 1. 同一 query coordinate，不同 value precision

补充 121–123 已把 joint witness semantics 从 existence 增强到 exact counts。Stage 124 单独抽出剩余资源：即使 query geometry 完全固定，每个 query coordinate 的**value alphabet**也会改变可恢复的 state。

令

\[
N:=c(\varnothing)=\sum_{I\in J(P)}w(I)>0
\]

为 total witness multiplicity。

## 2. P025-T273 —— MAY/MUST 是 exact count 的三值 collapse

对任意 required query \(S\)，

\[
0\le c(S)\le N.
\]

ordinary joint support semantics 可以精确由下式恢复：

\[
\boxed{
\begin{array}{ccl}
c(S)=0 &\iff& S\text{ IMPOSSIBLE},\\
0<c(S)<N &\iff& S\text{ MAY but not MUST},\\
c(S)=N &\iff& S\text{ MUST}.
\end{array}}
\]

因此 exact integer count semantics 通过三格 value quotient

\[
\boxed{
\{0\},
\{1,\ldots,N-1\},
\{N\}
}
\]

factor 到 MAY/MUST semantics。

这是固定 query coordinates 上发生的 value collapse，与 Stage 119–122 的 antichain / query-arity collapse 相互独立。

## 3. P025-C42 —— same support family + same total 仍可隐藏 different counts

取二元素 antichain \(P=\{a,b\}\)。考虑两个 multiplicity assignments，它们具有完全相同的 positive support family

\[
\{\{a\},\{b\},\{a,b\}\}.
\]

令

\[
w_1(\{a\})=1,
\quad
w_1(\{b\})=1,
\quad
w_1(\{a,b\})=2,
\]

以及

\[
w_2(\{a\})=2,
\quad
w_2(\{b\})=1,
\quad
w_2(\{a,b\})=1.
\]

二者都有

\[
N=4
\]

且 admissible exact-state support 完全相同。所以所有 existential/universal joint-MAY/MUST truth values 都一致。

但

\[
\boxed{c_1(\{b\})=3,
\qquad
c_2(\{b\})=2.}
\]

所以即使 support identity 与 total multiplicity 都固定，exact witness-count semantics 仍严格更细。

## 4. Precision-resource separation

组合 Stage 119–124 得到三条独立 precision axes：

1. **query/support geometry** —— 哪些 essential antichain coordinates 存在；
2. **query arity horizon** —— 可以同时要求多少个 incomparable labels；
3. **value precision** —— 每个 coordinate 保存什么：Boolean existence、三值 MAY/MUST、thresholded counts，还是 exact integer counts。

因此同一 coordinate system 仅通过改变 value collapse，就可以服务不同 state quotients。

## 5. 与 P023/A2 的关系

P023/FQ-004 generic future-signature machinery 已说明 declared future 决定 response 上的 coarsest quotient。Stage 124 是有限 specialization，说明 quotient 可以只发生在 **codomain value** 内部，而 operation/query coordinates 完全不变。

不应把它升级成新的 generic threshold theorem。

## 6. 与 A4 的关系

A4 拥有 witness spectra 与 multivalued correspondence。Stage 124 表明，即使 witness support 与 witness multiplicity 位于同一个 witness complex 上，它们仍是不同 state resources。

future 若只问 MAY/MUST，不应保留 exact counts；future 若询问 counts，则 support alone 不足。

## 7. Prior-art 边界

integer count thresholding 与 existential/universal semantics 都是 elementary。这里不主张 generic novelty。

项目侧结果是 P025/A2/A4 hierarchy 中的 exact value-precision placement，以及 same-support/same-total collision。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 8. 可执行资产

新增：

- `src/enterprise_math/poset_witness_count_value_precision.py`；
- `tests/test_poset_witness_count_value_precision.py`。

executable layer 验证 IMPOSSIBLE/MAY/MUST count thresholds、same-support/same-total count collision，以及 MUST/IMPOSSIBLE 的 exact boundaries。

## 9. Natural generation boundary

Stage 121–124 已形成一个 coherent count-precision generation：

\[
\boxed{
\text{witness existence}
\to
\text{zeta counts}
\to
\text{exact multiplicity inversion}
\to
\text{sharp width horizon}
\to
\text{task-relative pushforward}
\to
\text{value precision}.
}
\]

下一 generation 应离开 ideal-state assumption，直接测试 width-based operation saturation 对 arbitrary A4 correspondences 是否仍成立。预期它会失败；exact minimal counterexample 能识别真正产生 width saturation 的条件是 ideal / downward-closure law，而不是“有一个 poset 标签”本身。
