# P023 —— Quotient-Projection Repair Spectrum，补充 11

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023，消费 canonical P011 collision spectrum  
范围：finite precision relations 与 refinement chains  
纪律：finite equivalence-relation lattices、quotient projections、binomial inversion 与 partition block statistics 都属于成熟数学。项目新增价值是把 P011 irreversibility spectrum 与 precision states 之间的高阶 P023 repair spectrum 精确等同起来。

## 1. Precision refinement 天然产生一个 many-to-one map

令 `X` 为有限非空集合，并令

\[
F\subseteq E
\]

为 `X` 上两个 equivalence relations，其中 `F` 比 `E` 更细。

每个 fine class 都落在唯一 coarse class 内，因此天然存在 surjection：

\[
\boxed{
\pi_{F,E}:X/F\to X/E,
\qquad
[x]_F\mapsto[x]_E.
}
\]

这个 map 就是**忘掉 `F` 相对 `E` 多保留的精度**。

对一个 coarse block `B in X/E`，定义

\[
\boxed{
s_{E\leftarrow F}(B)
=
|\pi_{F,E}^{-1}(B)|
=
\#\{C\in X/F:C\subseteq B\}.}
\]

由 P023-S9，这正是只保留 `B` 后，要恢复原 fine class `C` 所需的局部最小 repair alphabet。

## 2. P023-S11-T01 —— P011/P023 quotient-projection 对偶

状态：`PROVED`。

forgetting map `pi_{F,E}` 的 P011 local fiber multiplicity，恰好等于 precision upgrade `E -> F` 的 P023 local repair multiplicity：

\[
\boxed{
m_{\pi_{F,E}}(B)=s_{E\leftarrow F}(B).}
\]

因此

\[
\boxed{
R(E\to F)
=
\max_B m_{\pi_{F,E}}(B).
}
\]

### 证明

`pi_{F,E}` 在 coarse block `B` 上的 fiber，按定义就是所有包含于 `B` 的 fine blocks。P023-S9 已证明这些不同 target blocks 在同一 coarse fiber 内必须使用不同 repair symbols，而不同 coarse blocks 可以复用 symbols。∎

所以每个 finite precision upgrade 都天然带有一个 deterministic map；它的 P011 irreversibility multiplicities 就是该 upgrade 的 P023 repair multiplicities。

## 3. P023-S11-T02 —— 高阶 repair spectrum

状态：`PROVED`。

定义

\[
\boxed{
\mathcal R_k(E\leftarrow F)
=
J_k(\pi_{F,E})
=
\sum_{B\in X/E}
\binom{s_{E\leftarrow F}(B)}k.
}
\]

则：

- `R_1(E<-F)=|X/F|`，即 fine classes 总数；
- `R_2` 数忘掉 `F` 精度后，被合并进同一个 coarse class 的 fine-class pairs；
- `R_k` 数被同一 coarse class 合并的 fine-class `k`-subsets。

这是一个**相对 precision-loss spectrum**。除非 `F` 就是 identity relation，否则它数的是 class-level ambiguity，而不是 raw-state ambiguity。

## 4. P023-S11-T03 —— 完整恢复 local repair-size distribution

状态：`PROVED`。

令

\[
c_r(E\leftarrow F)
=
|\{B\in X/E:s_{E\leftarrow F}(B)=r\}|.
\]

则由 P011 binomial inversion：

\[
\boxed{
c_r(E\leftarrow F)
=
\sum_{k=r}^{|X/F|}
(-1)^{k-r}\binom kr
\mathcal R_k(E\leftarrow F).}
\]

所以完整 relative repair spectrum 能精确恢复：有多少 coarse blocks 分别需要 `1,2,3,...` 个 repair symbols。

特别地，

\[
\boxed{
R(E\to F)
=
\max\{r:c_r(E\leftarrow F)>0\}.
}
\]

P023-S9 只保留了这个 worst-case maximum；S11 则保留完整 distribution 与所有高阶 ambiguity counts。

## 5. P023-S11-T04 —— Relative repair polynomial

状态：`PROVED`。

定义

\[
\boxed{
K_{E\leftarrow F}(t)
=
\sum_{B\in X/E}
\left((1+t)^{s_{E\leftarrow F}(B)}-1\right).
}
\]

则

\[
\boxed{
K_{E\leftarrow F}(t)
=
\sum_{k=1}^{|X/F|}
\mathcal R_k(E\leftarrow F)t^k.
}
\]

它恰好就是 canonical P011 collision polynomial 在 quotient projection `pi_{F,E}` 上的值。

所以这个多项式同时记录 `F -> E` forgetting map 丢掉的全部高阶 precision classes。

## 6. Absolute ambiguity 是 identity-refinement 特例

取最细 relation

\[
F=\Delta_X.
\]

此时 `X/F` canonical 地就是 `X`，而

\[
\pi_{\Delta,E}:X\to X/E
\]

就是 precision `E` 对应的 observation/quotient map。

因此

\[
\boxed{
\mathcal R_k(E\leftarrow\Delta_X)
=
\sum_{B\in X/E}\binom{|B|}k.
}
\]

一个公式同时包含项目已有的三种视角：

- P018 pointwise ambiguity：局部 `|B|`；
- P023 worst-case reconstruction：`max_B |B|`；
- P011 collision spectrum：对所有 blocks 的 binomial aggregate。

所以三条路线过去其实是在读取同一个 finite partition profile 的不同投影。

## 7. P023-S11-T05 —— Precision refinement 使 absolute ambiguity spectrum 单调下降

状态：`PROVED`。

若

\[
F\subseteq E,
\]

则对所有 `k>=2`，

\[
\boxed{
\mathcal R_k(F\leftarrow\Delta_X)
\le
\mathcal R_k(E\leftarrow\Delta_X).
}
\]

### 证明

每个 coarse `E` block 都是若干 fine `F` blocks 的不交并。因为

\[
n\mapsto\binom nk
\]

对非负整数是 superadditive，把一个 coarse block 拆成 fine subblocks 只能令总和下降或保持。∎

因此同一个 spectrum 在两种 foundational process 下方向恰好相反：

\[
\boxed{
\text{deterministic time postcomposition/coarsening}:
\mathcal R_k\uparrow,
}
\]

\[
\boxed{
\text{precision/task refinement}:
\mathcal R_k\downarrow.
}
\]

无需 entropy 或 real-valued information measure 就能表达这个双向单调性。

## 8. P023-S11-T06 —— 精确高阶 precision gain

状态：`PROVED`。

对 `F subseteq E`，定义

\[
\boxed{
G_k(E\to F)
=
\mathcal R_k(E\leftarrow\Delta_X)
-
\mathcal R_k(F\leftarrow\Delta_X).
}
\]

则 `G_k>=0`，并且它精确计数：原本属于同一个 coarse `E` block、但新增精度以后被分到至少两个 fine `F` blocks 中的 raw-state `k`-subsets。

### 证明

在一个 coarse block `B` 内，令其 fine subblock sizes 为 `a_1,...,a_s`。局部 gain 为

\[
\binom{a_1+\cdots+a_s}{k}
-
\sum_i\binom{a_i}{k},
\]

由 multinomial Vandermonde identity，它恰好数使用至少两个不同 fine subblocks 的 `k`-subsets。对所有 coarse blocks 求和即可。∎

这正是 P011 collision increment 的 precision-direction 镜像：后者数 time coarsening 新合并了哪些 `k`-subsets。

## 9. P023-S11-T07 —— Refinement gains 精确 telescope

状态：`PROVED`。

对 refinement chain

\[
E_0\supseteq E_1\supseteq\cdots\supseteq E_m,
\]

有

\[
\boxed{
\mathcal R_k(E_0\leftarrow\Delta_X)
-
\mathcal R_k(E_m\leftarrow\Delta_X)
=
\sum_{j=0}^{m-1}G_k(E_j\to E_{j+1}).
}
\]

这是高阶 precision gain 的 exact integer telescoping law。P018 的 pointwise ambiguity gain 是局部 block-size 视角；S11 为 `k>=2` 补上了 global subset-separation hierarchy。

## 10. P023-S11-T08 —— Refinement-chain quotient projections 精确复合

状态：`PROVED`。

对

\[
G\subseteq F\subseteq E,
\]

canonical quotient projections 满足

\[
\boxed{
\pi_{G,E}
=
\pi_{F,E}\circ\pi_{G,F}.
}
\]

对每个 coarse `E` block `B`，direct local repair size 满足 exact sum law：

\[
\boxed{
s_{E\leftarrow G}(B)
=
\sum_{C\in\pi_{F,E}^{-1}(B)}
s_{F\leftarrow G}(C).
}
\]

因此 P011 的整个 composition calculus 可以直接作用到 staged precision forgetting 与 staged repair。

特别得到

\[
\boxed{
R(E\to G)
\le
R(E\to F)R(F\to G),
}
\]

这正好恢复 P023-S9-T04，而且现在它只是更强 quotient-projection composition law 的 maximum-fiber shadow。

## 11. 概念收敛

这条结果删除了三个词之间原本不必要的分离：

- P011 的 **collision**；
- P018 的 **ambiguity**；
- P023 的 **repair**。

在 finite precision 下，它们全部来自同一个 block/fiber structure。真正不同的是方向与 task：

- forward dynamics 问 blocks 怎样合并；
- observation precision 问当前 blocks 有多大；
- repair 问一个 retained coarse block 内包含多少需要恢复的 fine blocks。

canonical quotient projection 在不改变底层数学的情况下把三种读法连接起来。

## 12. 可执行规格

- `src/enterprise_math/precision_projection_spectrum.py`
- `tests/test_precision_projection_spectrum.py`

回归检查 exact quotient-projection fibers、与 generic P023-S9 minimum alphabet 一致、binomial inversion、exact chain composition、strict product-bound examples，以及 absolute ambiguity spectrum 在 refinement 下的单调性。

## 13. Foundation 边界

该 spectrum 是关于 finite partitions、prediction 与 reconstruction 的定理。它不表示 ontological many-to-one transition 丢掉的 physical histories 仍隐藏在自然状态中。reverse repair alphabet 只是声明某个 reconstruction task 后，由外部定义出的 minimum distinction。
