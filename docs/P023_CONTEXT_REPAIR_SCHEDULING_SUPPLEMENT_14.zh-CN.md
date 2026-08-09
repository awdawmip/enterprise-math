# P023 —— Context-Derived Repair Scheduling，补充 14

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023，算法层桥接 P018 adaptive precision  
依赖：P023-S13 conditional repair；P018 finite dynamic-programming discipline  
纪律：finite subset dynamic programming 与 sequential coding bounds 都属于成熟方法。项目新增价值是让每个 task 的整数成本由 exact precision-incidence repair 内生地产生，而不是预先假定固定 external observation cost。

## 1. Final precision 与顺序无关，但 sequential cost 不是

令

\[
E_1,\ldots,E_m
\]

为同一个 state set `X` 上的 finite precision relations。

最终 joint precision

\[
C_*
=
\bigcap_{i=1}^mE_i
\]

与获取顺序无关。

选择一个顺序 `sigma`，并定义

\[
C_0=\top
\]

为 universal one-block relation，随后

\[
C_j
=
\bigcap_{r=1}^jE_{\sigma(r)}.
\]

第 `j` 步定义 exact conditional repair factor：

\[
\boxed{
\rho_j
=
R(C_{j-1}\to C_j)
=
\rho(E_{\sigma(j)}\mid C_{j-1}).
}
\]

这是一个内生成本：它取决于之前已经 retained 哪些 tasks。

## 2. P023-S14-T01 —— Exact class-count recurrence

状态：`PROVED`。

对每个 current block `B in X/C_{j-1}`，令

\[
s_j(B)
=
\#\{C_j\text{ blocks contained in }B\}.
\]

则

\[
\boxed{
|X/C_j|
=
\sum_{B\in X/C_{j-1}}s_j(B).
}
\]

按定义，

\[
1\le s_j(B)\le\rho_j,
\]

所以

\[
\boxed{
|X/C_j|
\le
|X/C_{j-1}|\rho_j.
}
\]

从 one-block context 迭代得到

\[
\boxed{
|X/C_*|
\le
\prod_{j=1}^m\rho_j.
}
\]

右侧就是该 task order 的 worst-case sequential repair capacity。

## 3. P023-S14-T02 —— Exact uniform-branching equality criterion

状态：`PROVED`。

单一步骤中，

\[
|X/C_j|
=
|X/C_{j-1}|\rho_j
\]

当且仅当

\[
\boxed{
s_j(B)=\rho_j
\quad\text{对所有 }B\in X/C_{j-1}.}
\]

也就是每一个 current context block 都必须达到相同的 maximal extension degree。

因此最终

\[
\boxed{
|X/C_*|
=
\prod_j\rho_j
}
\]

当且仅当**每一步**都是 uniform branching。

### 证明

stage recurrence 是 `|X/C_{j-1}|` 个正整数之和，每个都不超过 `rho_j`。只有所有 terms 都等于 `rho_j` 时，和才达到最大可能值。

一旦某一步严格小于这个最大值，后续 class count 至多继续乘上剩余 positive factors，因此这个严格缺口以后不可能重新追上最初的 full product bound。∎

所以 product slack 是 branch-dependent conditional precision 的结构性见证。

## 4. Integer symbol cost

固定整数 alphabet base

\[
B\ge2
\]

并沿用

\[
L_B(n)=\min\{\ell:n\le B^\ell\}.
\]

定义 stage depth：

\[
\boxed{
d_j=L_B(\rho_j),}
\]

以及 total sequential depth：

\[
\boxed{D_\sigma=\sum_jd_j.}
\]

因为

\[
|X/C_*|
\le
\prod_j\rho_j
\le
B^{\sum_jd_j},
\]

得到以下结果。

## 5. P023-S14-T03 —— Final-state depth lower bound

状态：`PROVED`。

对每个 acquisition order `sigma`，

\[
\boxed{
L_B(|X/C_*|)
\le
D_\sigma.
}
\]

定义 integer **depth slack**：

\[
\boxed{
S_B(\sigma)
=
D_\sigma-L_B(|X/C_*|)
\ge0.
}
\]

它衡量 sequential task acquisition 相对于“仅仅索引最终 joint classes 所需最小深度”多付出的 fixed-base worst-case symbols。

这不是 Shannon redundancy；没有使用 probability 或 expected code length。

## 6. P023-S14-T04 —— Product slack

状态：`PROVED`。

定义

\[
\boxed{
P(\sigma)
=
\prod_j\rho_j,
\qquad
S_\times(\sigma)
=
P(\sigma)-|X/C_*|.
}
\]

则

\[
S_\times(\sigma)\ge0,
\]

并且

\[
\boxed{
S_\times(\sigma)=0
\iff
\text{每个 acquisition stage 都 uniform branching}.}
\]

与 `D_sigma` 相比，product capacity 在转成 base-`B` symbol depth 前保留了 exact multiplicative repair alphabet sizes。

## 7. P023-S14-T05 —— 最优顺序的 exact finite dynamic program

状态：`PROVED / STANDARD ALGORITHM`。

对已经 retained 的 task subset `S`，令

\[
C_S=\bigcap_{i\in S}E_i,
\]

并取 `C_empty=top`。

由于 `C_S` 只依赖 subset，不依赖获取历史，最小剩余 symbol depth 满足 Bellman recurrence：

\[
\boxed{
D(S)
=
\min_{i\notin S}
\left[
L_B(\rho(E_i\mid C_S))
+D(S\cup\{i\})
\right],
}
\]

终点为

\[
D(\{1,\ldots,m\})=0.
\]

同理，最小 product capacity 满足

\[
\boxed{
P(S)
=
\min_{i\notin S}
\left[
\rho(E_i\mid C_S)
P(S\cup\{i\})
\right],
}
\]

终点值为 `1`。

这是一个完全有限的 subset dynamic program，不需要概率状态。

## 8. 最小 four-state order-dependence witness

取 states `0,1,2,3`，以及三个 binary tasks：

\[
A=(0,0,0,1),
\]

\[
B=(0,0,1,1),
\]

\[
C=(0,1,0,1).
\]

无论顺序如何，最终 common refinement 都是四个 singleton classes。

### 高效顺序 B -> C -> A

conditional factors 为

\[
\boxed{(2,2,1).}
\]

保留 `B,C` 后 state 已完全区分，所以 `A` 变成 redundant。

于是

\[
P=4,
\qquad
D_2=1+1+0=2.
\]

final joint precision 有四个 classes，因此

\[
L_2(4)=2,
\]

product 与 depth slack 都为零。

### 浪费顺序 C -> A -> B

factors 为

\[
\boxed{(2,2,2).}
\]

前两个 tasks 只形成三个 context classes，`B` 仍然会 split 其中一个。于是

\[
P=8,
\qquad
D_2=3.
\]

最终 precision 仍完全相同，都是四个 singleton classes，但

\[
\boxed{S_2=1.}
\]

仅仅因为 acquisition order 不同，就多付了一个完整 worst-case binary symbol。

## 9. 与 P018 adaptive precision 的关系

P018 现有 adaptive decision algorithms 接收外部给定的正整数 observation costs，并优化 predicate decision tree。

S14 解决的是另一个问题：

- 目标是把整个声明的 finite task family 都精确保留下来；
- 每个 task cost **不是固定常数**；
- 它由当前 precision context 自动给出：
  \[
  L_B(\rho(E_i\mid C_S)).
  \]

两套框架可以兼容。下一步可以把 context-derived repair cost 放进 state/predicate-specific adaptive decision program，但本补充不预设这层更复杂优化已经完成。

## 10. 研究工具规则

当多个 observations/tasks 最终会被联合保留时：

1. 不要预设每个 task 有互相独立的固定 storage/precision cost；
2. 应针对当前 joint context 计算 conditional repair factor；
3. 及时识别变成 redundant 的 tasks（`rho=1`）；
4. 检查 uniform branching，以判断 sequential capacities 是 exact 还是存在 slack；
5. 当顺序差异显著时，使用 finite subset DP，而不是没有证明地使用 static greedy ranking。

## 11. 可执行规格

- `src/enterprise_math/precision_task_scheduling.py`
- `tests/test_precision_task_scheduling.py`

回归固定 four-state order-dependence witness，对所有 task permutations 检查 final-depth lower bound，验证 uniform-branching equality criterion，并把 subset DP 与 exhaustive permutation search 交叉比对。

## 12. Foundation 边界

`S_B` 与 `S_x` 是声明 mathematical precision tasks 下的 exact finite scheduling/encoding slack measures。没有额外 realization model 时，它们不自动等于 thermodynamic cost、physical memory cost 或 ontological information content。
