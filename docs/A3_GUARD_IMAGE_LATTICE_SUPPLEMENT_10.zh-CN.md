# A3 Guard-Image Lattice 补充 10 —— Global All-State Band Precision 与 Adaptive Shortcut 的边界

状态：`RESEARCH WIP / EXACT GLOBAL-BAND MINIMUM PARTITION THEOREM`

## 1. 为什么 finite-workload 还不是 global program

Supplement 08 已证明：

\[
\text{state-local minimum}
\neq
\text{finite-workload minimum}.
\]

但 finite workload 仍只是有限 state 集合。

本补充研究完整 fine domain：

\[
\boxed{c\in\mathbb Z^k}
\]

上的同一个 finite-band predicate：

\[
P_R(c):=[|w^Tc+b|\le R].
\]

问题是：给定 initial partition `P`，是否存在仍隐藏 scalar `w^Tc+b` 的 refinement，却能对**所有 coarse states / 所有 fine states**精确运行这个 Boolean query？

## 2. global scalar image

整数线性 map：

\[
c\mapsto w^Tc
\]

在整个 `Z^k` 上的像是一个整数 subgroup：

\[
\boxed{g\mathbb Z,}
\]

其中：

\[
\boxed{g=\gcd(|w_1|,\ldots,|w_k|).}
\]

若所有 coefficients 为零，则：

\[
g=0
\]

且 scalar 恒为常数 `b`。

若 `g>0`，全部 fine-domain scalar values 是：

\[
\boxed{b+g\mathbb Z.}
\]

因此 whole-domain band 是否有 True states 当且仅当：

\[
\boxed{\rho_g(b)\le R.}
\]

而因 progression 无界，若 `g>0` 则永远存在 False states。

## 3. A3-G37 —— Global Band Constancy Criterion

### `g=0`

scalar 恒等于 `b`，所以 band predicate 全局恒：

\[
\boxed{[|b|\le R].}
\]

任意 partition 都 exact。

### `g>0` 且 progression miss band

若：

\[
\rho_g(b)>R,
\]

则整个 fine domain 都没有 supported state：

\[
\boxed{P_R\equiv\mathrm{False}.}
\]

所以任何 partition 都 global exact，不需要 refinement。

### `g>0` 且 progression 命中 band

若：

\[
\rho_g(b)\le R,
\]

则 whole domain 中同时存在 True/False states：

\[
\boxed{P_R\text{ global nonconstant}.}
\]

这才是非平凡 global precision 问题。

## 4. A3-G38 —— Nonconstant Global Band Requires Scalar Descent

假设：

\[
P_R
\]

在 whole domain 上 nonconstant。

取任意 partition `A`。

若 scalar 在该 partition 下仍有 nonzero hidden step：

\[
q>0,
\]

则 whole domain 既然有 supported fine state，可取：

\[
c_0
\]

使：

\[
|w^Tc_0+b|\le R.
\]

同一个 coarse fiber：

\[
c_0+K_A
\]

的 scalar values 是：

\[
z_0+q\mathbb Z.
\]

由于 `q>0`，该 progression 无界，所以同一 fiber 必然还存在：

\[
|z|>R
\]

的 fine lift。

于是同一个 coarse state 同时对应 True/False：

\[
\boxed{\text{partition 不 global exact}.}
\]

因此 global exactness 必须：

\[
\boxed{w(K_A)=0.}
\]

即 scalar observable 本身完全 descend。

反过来，若 scalar descend，则 band truth当然可从 coarse scalar 精确计算。

所以对 nonconstant global band：

\[
\boxed{
\text{partition global exact}
\iff
\text{scalar observable descends}.
}
\]

## 5. A3-G39 —— Global Minimum Partition

给定 initial partition：

\[
P_0.
\]

### 若 predicate global constant

无需任何 refinement：

\[
\boxed{P_*=P_0.}
\]

### 若 predicate global nonconstant

G38 说明 global exact partition 与 exact scalar-observation partition完全相同。

对 coordinate partition，scalar descend 当且仅当 coefficient `w_i` 在每个 coarse block 内常数。

所以用已有 observation-aware refinement：

> 在每个 current block 内按 `w_i` coefficient 分组。

得到唯一最粗：

\[
\boxed{P_*=\operatorname{ObsRefine}(P_0,w).}
\]

这是 whole-domain finite-band query 的 complete minimum partition solver。

## 6. Adaptive residue shortcut 为什么会消失

state-local 层可以出现：

\[
\rho_q(z_0)>R,
\]

所以某个具体 fiber 在 scalar hidden 时已经 exact False。

finite workload 也可能只覆盖一组幸运 residue classes。

但 global nonconstant task 必然包含至少一个 supported fine state。任何 nonzero hidden step 在这个 supported state 的 fiber 中都会同时制造 unsupported lift。

所以：

\[
\boxed{
\text{residue shortcut 是 adaptive/state-restricted optimization，
不是 global all-state visibility 的替代品。}
}

这给 precision architecture 一个清楚边界。

## 7. 三层 precision 现在有 exact 定义

对 finite-band task：

### state-local

只要求当前 coarse fiber exact。可能：

- no refinement；
- finite-index hidden subgroup refinement；
- full scalar visibility。

### finite workload

要求同一个 refinement 对有限多个 fibers 都 exact。cost 可以严格高于每个 state 的 local minimum。

### global all-state

若 predicate whole-domain nonconstant：

\[
\boxed{
\text{必须 exact scalar visibility}.}
\]

所以：

\[
\boxed{
\Delta d_{local}
\le
\Delta d_{workload}
\le
\Delta d_{global},
}
\]

但两个不等号都可能严格，也可能取等。

注意第一不等式这里指一个 workload中某个 state 的 local minimum与该 workload common minimum；不同 state 的 local costs 应分别比较。

## 8. 例子

取：

\[
w=(0,2,4),
\qquad
R=1,
\qquad
b=0.
\]

whole-domain scalar image：

\[
2\mathbb Z,
\]

包含：

\[
0\in[-1,1],
\]

同时也无界，所以 predicate global nonconstant。

### initial single block

`w` 不 constant，scalar hidden，不 global exact。

### intermediate partition

\[
\{\{0,2\},\{1\}\}
\]

hidden step：

\[
4.
\]

某些当前 fibers 可以因 residue miss band而 exact False，但 whole domain 中仍有 base residue `0 mod 4` 的 fibers命中 band，因此 intermediate partition不 global exact。

### singleton

scalar exact visible，global exact。

所以：

\[
\boxed{
\text{某 partition 可以对特定 state exact，
却对同一 task 的 whole domain 不 exact}.}
\]

## 9. globally constant false 例子

取：

\[
w=(4,8),
\qquad
b=1,
\qquad
R=0.
\]

whole-domain scalar image：

\[
1+4\mathbb Z.
\]

永远不含 `0`，所以：

\[
\boxed{P_0\equiv\mathrm{False}.}
\]

这里即使 scalar 完全 hidden，任意 partition 都 global exact。

因此 G38 的 visibility necessity 必须明确限定在 **global nonconstant task**；不能漏掉全局恒值退化情形。

## 10. 实现

扩展：

- `src/enterprise_math/hidden_band_predicate.py`；
- `tests/test_hidden_band_predicate.py`。

新增接口：

- `scalar_global_image_step`；
- `global_band_profile`；
- `band_partition_globally_exact`；
- `minimum_global_band_partition`；
- `GlobalBandProfile`。

测试覆盖：

- global scalar image gcd；
- global constant-false no-refinement case；
- nonconstant band 必须 scalar descend；
- unique coarsest coefficient refinement；
- small whole-domain box 与 global truth-variability 公式一致。

## 11. 对 P018 / A2 的含义

该 theorem 给 adaptive precision 一个硬边界：

> **task-local precision savings 与 one-model-fits-all global exactness 是不同 optimization problem。**

P018 若做 adaptive per-state/per-region precision，可以利用 hidden subgroup residue 省 relation degrees。

若要求一个固定 partition 对 whole infinite domain exact，则非恒定 scalar band不能使用这种 shortcut，必须回到 exact observable descent。

A2/P023 的 general behavioral quotient仍是母理论；本文只是 A3 scalar-band 的 complete all-state specialization。

## 12. 下一步

1. 将 finite-workload / global-band gap Relay 给 P018/P023；
2. 对 rank-one general multi-guard branch effects研究 symbolic all-state coarse program，而非只看 band；
3. 分析 coarse-readable score quotient `Z^r/L_G` 是否能作为 global program 的有限/typed condition state；
4. 把 support corollary Relay 给 A3→A4 bridge；
5. 对 A4/P021 的真实 future language 区分 state-local adaptive precision 与 global shared precision。
