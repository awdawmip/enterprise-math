# P019 补充 24 —— Weighted Relation Map 的 Smith Quantum 与内生 Precision Scale

状态：`RESEARCH WIP / INTEGER-LATTICE STRUCTURE PROVED`

## 1. 目标

weighted relation field：

\[
Z_{ij}=m_jc_i-m_ic_j
\]

天然带有 capacity common divisor。

本补充把这个现象从“每个 entry 都能被某个数整除”提升为 relation map 的完整整数格陈述，并研究它在 partition coarsening 下如何变化。

## 2. relation map

固定 capacities：

\[
m=(m_1,\ldots,m_k)^T\in\mathbb Z_{>0}^k.
\]

定义整数线性 map：

\[
\boxed{
\phi_m:\mathbb Z^k\to\bigwedge^2\mathbb Z^k,
\qquad
\phi_m(c)=c\wedge m.
}
\]

在标准 pair basis 中：

\[
(\phi_m(c))_{ij}
=c_im_j-m_ic_j
=Z_{ij}.
\]

所以 weighted relation field 就是 `phi_m(c)`。

## 3. capacity gcd 与 primitive capacity vector

令：

\[
\boxed{
g=\gcd(m_1,\ldots,m_k),}
\]

并写：

\[
\boxed{m=g\hat m,}
\qquad
\gcd(\hat m_i)=1.
\]

则：

\[
\boxed{
\phi_m=g\phi_{\hat m}.
}
\]

所以所有 weighted relation entries 必然被 `g` 整除。

但注意：一个具体 state 的全部 `Z_ij` 可能还共享更大公因数。`g` 表示 capacity pattern 强制的结构性 quantum，不等于每个具体 field 的 entry gcd。

## 4. P019-X84 —— relation map 的非零 Smith invariants 全为 `g`

因为 `hat m` 是 primitive integer vector，存在 unimodular basis change：

\[
U\in GL(k,\mathbb Z)
\]

使：

\[
U\hat m=e_1.
\]

在 domain 与 exterior-square codomain 同步换整数基，`phi_hatm` 等价于：

\[
c\mapsto c\wedge e_1.
\]

该 map：

- kernel 为 `Z e_1`；
- image 由：
  \[
  e_2\wedge e_1,\ldots,e_k\wedge e_1
  \]
  自由生成；
- 非零 Smith invariants 全为 1。

再乘回 `g`：

\[
\boxed{
SNF_{nonzero}(\phi_m)
=(g,g,\ldots,g)
}
\]

共 `k-1` 个非零 invariant factors。

所以：

\[
\boxed{
\operatorname{rank}\phi_m=k-1,
}
\]

并且 `g` 是每个 independent relation direction 的共同整数 scale quantum。

Smith normal form 与 primitive-vector unimodular reduction属于成熟整数线性代数；P019 不作原创声明。

## 5. P019-X85 —— 相同 relation field 的 state 差恰为 primitive capacity shift

若：

\[
\phi_m(c')=\phi_m(c),
\]

则：

\[
(c'-c)\wedge m=0.
\]

由于：

\[
m=g\hat m
\]

且 `hat m` primitive，所以所有整数 kernel vectors 恰为：

\[
\boxed{
\ker\phi_m
=\mathbb Z\hat m.
}
\]

因此：

\[
\boxed{
c'=c+t\hat m,
\qquad t\in\mathbb Z.}
\]

这给 tree-independent relation field 的 translation ambiguity 一个精确整数描述。

## 6. P019-X86 —— field-preserving grand-total period

总 capacity：

\[
M=\sum_i m_i.
\]

primitive shift：

\[
c\to c+\hat m
\]

保持整个 `Z` 不变，但 grand total 改变：

\[
\Delta C
=\sum_i\hat m_i
=M/g.
\]

定义：

\[
\boxed{
\tau=M/g.
}
\]

则对固定 relation field，所有 compatible grand totals 位于一个 arithmetic progression：

\[
\boxed{
C=C_0+t\tau.
}
\]

因此：

\[
\boxed{g\tau=M.}
\]

`g` 与 `tau` 是由 capacities 内生的一对 dual integer scales。

## 7. P019-X87 —— relation quantum 沿 coarsening 只能保持或变粗

设 fine capacities 为 `m_i`，fine quantum：

\[
g_f=\gcd(m_i).
\]

partition coarsening 后，每个 coarse capacity 都是一些 `m_i` 的和。

所以 `g_f` 整除每个 coarse capacity，从而：

\[
\boxed{
g_f\mid g_c.}
\]

因此 relation quantum 沿 coarsening chain 在 divisibility order 上单调：

\[
g_0\mid g_1\mid g_2\mid\cdots.
\]

由于总 capacity `M` 不变：

\[
\tau=M/g,
\]

所以：

\[
\boxed{
\tau_c\mid\tau_f.
}
\]

coarsening 可能把 relation lattice 变粗，同时缩短同-field translation period。

## 8. primitive relation state + scale tag

由于：

\[
m=g\hat m,
\qquad
Z=g\hat Z,
\]

可把 current relation state 写成：

\[
\boxed{
(g;\ \hat m,\hat Z,\ C),
\qquad
\gcd(\hat m)=1.
}
\]

其中：

- `g`：relation precision scale；
- `(hat m,hat Z)`：primitive relation structure；
- `C`：grand total / translation-coset selector。

## 9. P019-X88 —— partition coarsening 产生整数 scale carry

从 primitive capacities `hat m` 出发做 partition `A`：

\[
\tilde m=A\hat m,
\qquad
\tilde Z=A\hat Z A^T.
\]

定义新产生的 common factor：

\[
\boxed{
h=\gcd(\tilde m).}
\]

则：

\[
\boxed{
g'=gh,}
\]

\[
\boxed{
\hat m'=\tilde m/h,
}
\]

\[
\boxed{
\hat Z'=\tilde Z/h.
}
\]

由于 `g'` 是 coarse capacity gcd，`h` 必然整除所有 `tilde Z` entries，因此除法 exact。

所以一次 coarsening 可以读作：

\[
\boxed{
\text{primitive relation quotient}
+
\text{integer scale carry }h.
}
\]

## 10. P019-X89 —— scale carry 沿 chain 乘法复合

若连续 coarsening 产生：

\[
h_1,h_2,\ldots,h_r,
\]

则：

\[
\boxed{
g_r=g_0\prod_{t=1}^r h_t.}
\]

这只是 gcd scale 的整数递推，不需要连续 renormalization。

例如 8 个 unit blocks：

\[
(1,1,1,1,1,1,1,1)
\]

按 equal pairs coarse-grain：

\[
(2,2,2,2)
\to
(4,4)
\to
(8),
\]

scale carries：

\[
2,2,2,
\]

最终：

\[
g=8.
\]

## 11. 与 P018 precision 的接口

这里出现一个完全内生的 finite precision chain：

\[
\boxed{
\text{partition}
\to
\text{capacity gcd }g
\to
\text{relation quantum}
}
\]

refinement 可减少 common capacity factor、暴露更细 relation quantum；coarsening 只能保持或增加 `g`。

所以 relation precision 不一定需要外部预先指定一个 scale number；某些 scale 可以由当前 partition capacities 自己产生。

这不替代 P018 的一般 precision lattice，但提供一个具体几何实例。

## 12. 实现与验证

新增：

- `src/enterprise_math/relation_lattice.py`
  - capacity gcd；
  - primitive capacity vector；
  - relation quantum；
  - translation period；
  - field-preserving shifts；
- `src/enterprise_math/relation_scale.py`
  - primitive relation factorization；
  - coarsening scale carry；
  - scale-chain product；
- tests：
  - `tests/test_relation_lattice.py`；
  - `tests/test_relation_scale.py`。

回归覆盖：

- `g*tau=M`；
- primitive capacity gcd=1；
- field-preserving shift exactness；
- bounded search 中 same-field states 均为 primitive-capacity shifts；
-所有 relation entries 被 structural `g` 整除；
- coarsening quantum divisibility；
- equal-block coarse-graining 的 scale carries 乘法链。

## 13. 下一步

1. 把 relation quantum `g` 与 P018 scale factor / precision detail 正式对齐；
2. 研究不等 capacity partition 中 `g` 跳变的组合条件；
3. 用 SNF 给 arbitrary weighted quotient 的合法 relation lattice 做 canonical normal form；
4. 研究 relation scale carry 是否与 collision carry / distance carry 有统一整数搬运解释；
5. 将 primitive relation state + scale tag 纳入 future-safe quotient cost。
