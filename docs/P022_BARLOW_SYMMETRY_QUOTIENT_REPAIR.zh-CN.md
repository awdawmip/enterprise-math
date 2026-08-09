# P022 — 对称 Quotient 将 Event Repair 化为 Path-Lift Multiplicity

状态：`ACTIVE RESEARCH NOTE / GENERAL BRIDGE CANDIDATE / PRIOR-ART SENSITIVE`  
本 specialization 归属：`program/p022-geometry-v2`  
潜在母定理归属：A2/P023 quotient safety，A4 count/equitability  
Prior art：群作用图、equitable partition、quotient/orbit graph 与 path lifting 属于已有数学

## 1. 从 event bits 到 quotient-graph 定理

Barlow two-sided repair 已发现两类 bit-producing events：

- 离开 zero boundary；
- equal absolute pair 分裂成 unequal sides。

精确 fiber size 为

\[
2^{E+B}.
\]

更深层的解释是：coordination observation 是 microscopic transition graph 的 symmetry quotient，而 `E+B` 正是 quotient-edge lift multiplicities 乘积的 base-two 指数。

## 2. Equitable transition quotient

设 `X` 是 directed transition graph，并将 vertices 分成若干 blocks。若 partition 对 outgoing transitions 是 **equitable**：对任意 source block `A`、target block `B` 和任意 `x,x' in A`，

\[
\#\{y\in B:x\to y\}
=
\#\{y\in B:x'\to y\},
\]

则可定义与代表元无关的 edge multiplicity

\[
\boxed{m(A,B)=\#\{y\in B:x\to y\}.}
\]

若一个群以 graph automorphisms 作用并在每个 block/orbit 上传递，则 orbit partition 自动满足这一条件。

## 3. P022-SQ01 — Quotient-path lift product

固定 microscopic start `x_0 in A_0` 与 quotient path

\[
A_0\to A_1\to\cdots\to A_n.
\]

任意到达 `A_i` 的 microscopic lift prefix 都恰有

\[
m(A_i,A_{i+1})
\]

个进入下一 block 的 continuations。归纳得到

\[
\boxed{
\#\{\text{从固定 }x_0\text{ 出发的 microscopic lifts}\}
=
\prod_{i=1}^{n}m(A_{i-1},A_i).
}
\]

若初始 microscopic state 本身也只观察到一个 orbit，则再乘 initial fiber size。

该 path-lift 结构本身属于既有 quotient/equitable graph 数学；本项目特定贡献是把 finite repair 精确解释成这些整数 lift multiplicities。

## 4. Barlow microscopic symmetry

两条 signed prefix drifts 组成

\[
(\delta^+,\delta^-)\in\mathbb Z^2
\]

每步增量为

\[
(\pm1,\pm1).
\]

signed-permutation 群

\[
\boxed{G=(\mathbb Z_2)^2\rtimes S_2}
\]

通过改变两坐标符号及交换两 channels 作用，并保持 transition graph。

其 orbit 由 sorted absolute pair

\[
\boxed{0\le a\le b}
\]

唯一决定，这正是 coordination history 恢复的 hidden state。

因此 chamber `0<=a<=b` 不只是方便坐标，而是 microscopic symmetry quotient 的 fundamental domain。

## 5. P022-SQ02 — Barlow quotient-edge multiplicities

对 quotient edge

\[
(a,b)\to(c,d),
\]

microscopic continuation multiplicity 总属于

\[
\boxed{1,2,4.}
\]

具体：

- `(a,b)` 中每个 zero coordinate 贡献一个 factor `2`，因为离开 zero 可以选择 microscopic sign；
- 若 `a=b` 且 successor unequal，再贡献一个 factor `2`，因为任一 labelled channel 都可取得较大的 absolute successor。

所以

\[
\boxed{m((a,b),(c,d))=2^{z+s},}
\]

其中

\[
z=\mathbf1_{a=0}+\mathbf1_{b=0},
\]

\[
s=\mathbf1_{a=b,\ c\ne d}.
\]

因此：

- ordinary interior transition：`m=1`；
- 一个 zero departure 或一个 diagonal split：`m=2`；
- origin departure：`m=4`。

## 6. P022-SQ03 — Event-repair theorem 就是 path-lift theorem

对 coordination history `P_0,...,P_N`，将 SQ02 edge weights 相乘：

\[
\prod_qm(P_{q-1},P_q)
=
2^{\sum_qz_q+\sum_qs_q}
=
2^{E+B}.
\]

由 SQ01，这个乘积正是 microscopic signed labelled word-pair lifts 数。

故

\[
\boxed{|O^{-1}(P)|=2^{E+B}}
\]

并非孤立组合恒等式，而是 symmetry quotient 的 orbit-path lift multiplicity。repair bitstream 只是从这些 microscopic branches 中选定一个 lift 的坐标。

## 7. Repair polynomial 作为 weighted quotient-path enumerator

已有

\[
R_N(z)=\sum_hz^{r(h)}
\]

现在可以解释成 quotient paths 的 weighted enumerator：lift multiplicity 为

\[
2^c
\]

的 edge 赋 weight

\[
z^c.
\]

于是：

- `z=1` 统计 quotient paths；
- `z=2` 将 edge weight 替换成 microscopic lift multiplicity，恢复全部 microscopic paths；
- 在 `2` 处求导得到 lift-weighted repair load。

## 8. Negative boundary — Non-equitable partition 会破坏局部 product state

代表元无关的 edge weight 是必要条件。

取

\[
A=\{a_1,a_2\},
\quad
B=\{b_1,b_2\},
\]

且

\[
a_1\to b_1,b_2,
\]

而

\[
a_2\to b_1.
\]

同一 coarse edge `A->B` 从 `a_1` 出发有 2 个 microscopic continuations，从 `a_2` 出发只有 1 个。

因此

\[
m(A,B)
\]

不能定义，coarse edge-weight product 也不可能精确表示 future lift count。

这与此前 A4/A2 count-lumpability 的边界完全一致：**只有 quotient 对被查询 transition algebra equitable 时，future count semantics 才能下降。**

## 9. Cross-route 结论

真正一般的陈述不属于 Barlow 专有：

> 对 equitable transition quotient，exact path-lift multiplicity 可局部因子化为 quotient-edge continuation counts；若 quotient 非 equitable，representative identity 仍是 future-relevant hidden state。

该一般结果在晋升前必须与 A2/A4 既有 equitability/lumpability 结果做语义去重。P022 保留 signed-permutation/Barlow specialization 与发现 provenance。

## 10. Precision 解释

更精确地说：

\[
\boxed{\text{repair 恰发生在 lift multiplicity}>1\text{ 的 quotient edges 上}.}
\]

boundary events 重要，是因为 symmetry quotient 在这些位置不再有唯一 microscopic continuation。

自然 primitive 是整数 branching multiplicity `m`，不是 logarithm。Barlow 中 `m` 都是 2 的幂，因此可等价用 bits；一般 quotient 若出现非 2 次幂，应保留 exact integer branch count，而不强行转成实数信息量。

## 11. 可执行资产

- `src/enterprise_math/p022_symmetry_quotient_repair.py`；
- `tests/test_p022_symmetry_quotient_repair.py`。

测试用短 horizon Barlow microscopic fibers 验证 quotient-edge product，另验证一个 generic equitable finite graph，并保留 explicit non-equitable counterexample。