# Causal Graded Operation Geometry —— 同一 Primitive Law 生成移动几何与未来精度

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE THEOREMS + EXECUTABLE REFERENCE`

归属：P012 应消费 transport bridge；P023/A2 应消费 future-equivalence / quotient 层；P011 应消费 revelation spectrum；P018 只在存在 bridge theorem 时消费 precision transport。A3 保留 finite weighted compiler。

## 1. Primitive data

给：

- finite raw state set `X`；
- causal operation generators `G`；
- 每个 primitive generator 的正整数 grade/cost：
  \[
  c:G\to\mathbb N_{>0};
  \]
- 当前离散 observation：
  \[
  O:X\to Y.
  \]

对 finite operation word：

\[
w=g_1g_2\cdots g_m,
\]

定义：

\[
\boxed{
|w|_c=\sum_{i=1}^m c(g_i).
}
\]

空 word cost 为 `0`。

正 cost 是当前 finite-budget compiler 的必要纪律：若允许能反复执行的 zero-cost generator，budget `0` 本身就可能需要无限 closure，必须另行定义。

## 2. GG-01 —— transport cost

定义：

\[
\boxed{
d_{move}(x,y)
=\min\{|w|_c:w(x)=y\}.}
\]

若不可达则记 `infinity`。

这就是 P012 primitive-operation distance 的 graded/directed 版本。

若 generators 非可逆，则 `d_move` 一般是 directed reachability cost，不自动是 metric。

只有在 operation set 具有反向 primitive operations，并且正反 cost 对称等额时，才可进一步得到传统 symmetric shortest-path metric shadow。

所以：

\[
\boxed{
\text{transport geometry}
\text{ 由 primitive operations + integer grade 生成，}
\text{不是先给 norm。}
}
\]

## 3. GG-02 —— future distinguishing cost

定义：

\[
\boxed{
d_{sep}(x,y)
=\min\{|w|_c:O(w(x))\ne O(w(y))\}.}
\]

若任何 finite future 都不能区分，则记：

\[
d_{sep}(x,y)=\infty.
\]

注意这不是普通 metric：

\[
d_{sep}(x,x)=\infty,
\]

不是 `0`。

它的语义是：

> 数值越大，两个 states 要到越深/越昂贵的 causal future 才能被分开。

因此应称 **agreement depth / distinguishing cost**，而不是直接称传统距离。

## 4. GG-03 —— finite-budget future quotient

对整数 budget `R>=0`，定义：

\[
\boxed{
x\equiv_R y
\iff
d_{sep}(x,y)>R.}
\]

等价地：所有 total cost 不超过 `R` 的 future words 都给出相同 observation。

得到 nested partitions：

\[
\boxed{
E_0\succeq E_1\succeq E_2\succeq\cdots
}
\]

budget 越大，允许的未来 probes 越多，state 只能继续细化。

finite compiler 的 exact recurrence：

\[
P_0=\ker O,
\]

\[
\boxed{
P_R(x)=
\left(
O(x),
P_{R-1}(x),
\bigl(P_{R-c(g)}(g(x))\bigr)_{c(g)\le R}
\right).
}
\]

稳定等价类就是 budget `R` 下的完整 causal future signature。

实现：

- `causal_weighted_future.py`
- `tests/test_causal_weighted_future.py`

## 5. GG-04 —— strong agreement law

对任意 states：

\[
\boxed{
d_{sep}(x,z)
\ge
\min\{d_{sep}(x,y),d_{sep}(y,z)\}.}
\]

证明完全离散。

若存在一个 future word `w` 在 cost `r` 区分 `x,z`，且：

\[
r<d_{sep}(x,y),
\qquad
r<d_{sep}(y,z),
\]

则同一个 `w` 必同时满足：

\[
O(w(x))=O(w(y))=O(w(z)),
\]

与 `x,z` 被区分矛盾。

因此 nested future partitions 自动给出 ultrametric-like agreement structure。传统 real ultrametric 只有在进一步选择单调数值反编码时才出现，不作为 primitive ontology。

## 6. GG-05 —— ultimate quotient 与 cost regrading 分离

只要所有 primitive generators 的 cost 始终为正整数，且 operation set `G` 不变，则：

\[
\boxed{
E_\infty
=E_G
}
\]

只取决于**哪些 finite operation words 存在**，不取决于它们被赋予什么正整数 cost。

因此改变 grade 只改变 distinction **何时**暴露，不改变 distinction **最终是否**暴露。

### generatorwise cost increase

若：

\[
c'(g)\ge c(g)\quad\forall g,
\]

则同一 budget 下：

\[
\boxed{
E_R^{c}\preceq E_R^{c'},
}
\]

也就是更昂贵的 operation 使固定预算看到更粗的 future state。

并且：

\[
\boxed{
d_{move}^{c'}\ge d_{move}^{c},}
\]

\[
\boxed{
d_{sep}^{c'}\ge d_{sep}^{c}.}
\]

### uniform integer rescaling

若：

\[
c'=m c,
\qquad m\in\mathbb N_{>0},
\]

则严格：

\[
\boxed{d'_{move}=m d_{move},}
\]

\[
\boxed{d'_{sep}=m d_{sep},}
\]

以及：

\[
\boxed{
E_R^{c'}=E_{\lfloor R/m\rfloor}^{c}.
}
\]

所以 integer cost unit 可以重标；不能仅凭数值大小把它直接认作物理空间长度。

实现：

- `causal_cost_regrading.py`
- `tests/test_causal_cost_regrading.py`

## 7. GG-06 —— operation cost 是 precision-layer transport degree

这是本轮最重要的 bridge theorem。

若 generator `g` cost 为：

\[
c(g)=c,
\]

则：

\[
\boxed{
xE_{R+c}y
\Longrightarrow
g(x)E_Rg(y).}
\]

证明：若 `g(x),g(y)` 能被某个 cost 不超过 `R` 的 future `w` 区分，则 `w o g` 的 total cost 不超过 `R+c`，会区分 `x,y`，矛盾。

因此 `g` 天然诱导：

\[
\boxed{
\bar g_R:
X/E_{R+c}\to X/E_R.
}
\]

而不是必须成为同一 layer 的 endomorphism。

对任意 word `w`，total cost：

\[
C=|w|_c,
\]

有：

\[
\boxed{
\bar w_R:
X/E_{R+C}\to X/E_R.
}
\]

若 `u` 后接 `v`，cost 分别 `C_u,C_v`，则：

\[
\boxed{
\overline{v\circ u}_R
=
\bar v_R\circ\bar u_{R+C_v}.
}
\]

cost addition 与 quotient-map composition 完全一致。

实现：

- `causal_graded_precision_transport.py`
- `tests/test_causal_graded_precision_transport.py`

## 8. GG-07 —— agreement depth loss bound

由上一条直接得到：

\[
\boxed{
d_{sep}(g(x),g(y))
\ge
d_{sep}(x,y)-c(g).}
\]

若 `d_sep(x,y)=infinity`，则：

\[
d_{sep}(g(x),g(y))=\infty.
\]

更一般：

\[
\boxed{
d_{sep}(w(x),w(y))
\ge
d_{sep}(x,y)-|w|_c.}
\]

这不是从传统 error propagation 搬来的公式，而是由 future budget 的 composition 结构自动生成。

解释：

> 已执行 operation 最多消耗与其 causal grade 同量的未来 agreement budget。

## 9. GG-08 —— P011 precision revelation spectrum

对 budget partition `E_R`，定义：

\[
\boxed{
J_k(R)
=
\sum_{C\in X/E_R}\binom{|C|}{k}.
}
\]

随着 `R` 增加，partition 只会细化，所以：

\[
J_k(R+1)\le J_k(R),
\qquad k\ge2.
\]

定义 revelation spectrum：

\[
\boxed{
\Lambda_k(R)
=J_k(R-1)-J_k(R),
\qquad R\ge1.
}
\]

它精确计数：

> 在 budget `R-1` 仍完整落在同一个 future class、但到 budget `R` 首次被 split 的 `k` 元 history groups。

特别地：

\[
\boxed{
\Lambda_2(R)
=
\#\{\{x,y\}:d_{sep}(x,y)=R\}.
}
\]

并有 telescoping：

\[
\boxed{
\sum_{R=1}^{B}\Lambda_k(R)
=J_k(0)-J_k(B).
}
\]

因此 P011 collision spectrum 不只测已经发生的 collapse；在 graded future 中，它还能精确记录**distinctions 在哪个整数 budget 被重新暴露**。

实现：

- `causal_revelation_spectrum.py`
- `tests/test_causal_revelation_spectrum.py`

## 10. 与 P012 的 bridge

P012 已经主张 primitive adjacency/operation 是几何 datum，最短 primitive walk 是 intrinsic integer distance。

本文件把这个原则扩成 graded operation law：

\[
(G,c)
\to
d_{move}.
\]

同时同一 `(G,c)` 配合 observation `O` 又生成：

\[
(G,c,O)
\to
(E_R,d_{sep},\Lambda_k).
\]

因此 transport geometry 与 distinguishability geometry 的当前关系应从过去的：

`COMPOSABLE_INDEPENDENT`

升级为：

\[
\boxed{
\text{COMMON_CAUSAL_SOURCE / NOT_IDENTIFIED}.
}
\]

它们共享 primitive operation/cost layer，但一般绝不相等。

## 11. 传统前人工作边界

Weighted transition systems、weighted automata、bisimulation metrics / behavioral distances 都是成熟研究邻域。

因此本项目不主张以下一般事实为原创：

- transition system 可以带 weights；
- shortest weighted paths；
- behavioral equivalence / behavioral distance；
- partition refinement；
- ultrametric-like nested equivalence representations。

当前需要审查的项目性贡献候选是它们在 Enterprise Math 本体顺序中的统一：

\[
\boxed{
\text{primitive causal operations}
+\text{integer grade}
+\text{future observation}
\to
\text{transport}
+\text{precision tower}
+\text{revelation spectrum}
+\text{cross-layer operation transport}.
}
\]

## 12. 当前边界

尚未完成：

- infinite-state graded compiler；
- physical derivation of primitive cost rather than declared cost；
- locality / energy / latency 等不同 cost semantics 的 typed separation；
- stochastic/quantum channels；
- P018 block precision 与 future-budget precision 的严格双尺度 bridge；
- Lean formalization；
- clean-integration CI。
