# A3 Guard-Image Lattice 补充 02 —— Rank-Two Hidden Guard 的精确二维可达性

状态：`RESEARCH WIP / EXACT RANK-TWO INTEGER FEASIBILITY SOLVER + COMPLEXITY BOUND`

## 1. 目标

Supplement 01 已完整解决

\[
\operatorname{rank}L_G=1,
\qquad
L_G=W(K_A)\subseteq\mathbb Z^r,
\]

此时一个 coarse fiber 的 hidden guard scores 是整数等差线。

本补充解决下一层：

\[
\boxed{\operatorname{rank}L_G=2.}
\]

guard 数 `r` 不要求等于 3；只要 hidden image lattice 的 rank 是 2，本结果适用于任意有限 guard family。

目标仍然是精确回答：给定 coarse fiber 的 base scores

\[
g\in\mathbb Z^r
\]

与 threshold pattern

\[
\sigma\in\{\mathrm{False},\mathrm{True}\}^r,
\]

是否存在

\[
x\in g+L_G
\]

实现该 pattern。

全程不使用浮点、连续优化或有限 fine-state box 作为正确性依据。

## 2. A3-G07 —— rank-two lattice 的精确整数 basis

给定任意生成元

\[
v_1,\ldots,v_m\in\mathbb Z^r,
\qquad
\operatorname{rank}_{\mathbb Q}\langle v_i\rangle=2,
\]

先选字典序最早的两个 guard coordinates `(p,q)`，使该二维坐标投影在 rational span 上保持 rank 2。

由于该投影在 rank-two rational span 上单射，可以先在投影的 `Z^2` 子格中求 basis，再唯一 lift 回完整 `Z^r`。

构造只需两轮 Bezout/gcd：

1. 对所有第 `p` 坐标取 gcd `a`，用 Bezout combination 构造第一向量；
2. 从每个生成元消去第 `p` 坐标，对剩余第 `q` 坐标取 gcd `c`；
3. 用第二个 Bezout combination 得到 `(0,c)` 方向；
4. 对第一向量减去第二向量的整数倍，使投影满足

\[
\boxed{(a,b),(0,c),\qquad a,c>0,\ 0\le b<c.}
\]

得到完整 lattice 的精确 basis

\[
\boxed{L_G=\mathbb Z h_1+\mathbb Z h_2.}
\]

这不是选两个独立原生成元做近似；冗余生成元可能缩小 lattice index，因此 basis 必须对整个生成 subgroup 求出。

实现同时提供 exact membership coordinates：一个向量属于该 lattice，当且仅当它能以整数系数重建为 `s h_1+t h_2`。

## 3. threshold pattern 化成二维整数半平面

fiber 内任意 guard-score vector 唯一写成：

\[
\boxed{x=g+s h_1+t h_2,\qquad s,t\in\mathbb Z.}
\]

对第 `j` 个 guard：

- 若 pattern 要求 `True`，则
  \[
  h_{1j}s+h_{2j}t\ge -g_j;
  \]
- 若要求 `False`，整数条件 `x_j<0` 等价于 `x_j\le-1`，因此
  \[
  -h_{1j}s-h_{2j}t\ge g_j+1.
  \]

所以任意 branch pattern 精确等价于有限二维整数半平面系统：

\[
\boxed{a_i s+b_i t\ge c_i.}
\]

问题已经从无限 fine state space 降到两个整数参数。

## 4. A3-G08 —— exact 2D feasibility 的三类 certificate

定义上述二维 polyhedron 的 homogeneous recession cone：

\[
C=\{(u,v):a_i u+b_i v\ge0\ \forall i\}.
\]

二维时只有三种本质情况。

### 4.1 strict recession

若存在整数方向 `d` 使

\[
\boxed{a_i d_1+b_i d_2>0\quad\forall i,}
\]

则对足够大整数 `N`：

\[
Nd
\]

自动满足所有常数右端 `c_i`。

因此该 branch pattern 对任意 base offset 的相应 affine half-plane system都有一个显式整数 witness；无需搜索。

实现从 recession cone 的整数边界 rays / 法向量中构造 strict interior candidate，并直接给出最小足够放大倍数。

### 4.2 recession ray / line

若 recession cone 非零但没有二维 interior，则它是一条 rational ray 或 line。

取 primitive integer direction：

\[
d=(d_1,d_2).
\]

取 primitive perpendicular integer normal：

\[
n=(-d_2,d_1).
\]

由于 `d` primitive，可用 Bezout 找到 integer section `p` 满足：

\[
n\cdot p=1.
\]

任意整数点可按：

\[
q p+t d
\]

参数化。

沿 `d` 不增长的 constraints 只对单整数 `q` 给上下界；先解这个一维整数 interval，再沿 `d` 取足够大的 `t` 即得 witness。

因此这一类也不需要二维枚举。

### 4.3 bounded polygon

若 recession cone 只有零向量，则 real feasible set 若非空必为 bounded polygon/segment/point。

所有极值来自 constraint-line 两两交点。实现不用 rational/float object，而用：

`numerator / positive denominator`

的整数对做 cross-multiplication 比较，得到两个参数轴的 exact rational min/max。

随后只扫描整数跨度更小的那个轴；每固定一个整数坐标，另一个坐标又退化成一维整数 interval。

所以 bounded case 的 search width 是一个**显式有限 certificate**，而不是任意截断盒子。

## 5. bounded real feasibility 不等于 integer reachability

rank-two 情形保存了一个重要负边界：

> real half-plane intersection 非空，仍可能没有任何整数 lattice parameter witness。

因此不能用连续 LP feasibility 后简单 round 参数替代 integer solver。

新测试保存了这种 bounded real region / no integer witness 的反例。

## 6. A3-G09 —— strict cone 的 base-independent reachability

若某 threshold pattern 的 homogeneous parameter cone 含 strict integer direction，则：

\[
\boxed{
\text{该 pattern 对所有 affine base scores }g\text{ 都可达。}
}

原因是常数项只改变需要沿 strict direction 前进多少步，不改变最终可达性。

所以 rank-two 中真正依赖 coarse state / arithmetic residue 的困难 branch patterns，只来自：

- lower-dimensional recession；或
- bounded parameter cells。

full-rank guard-image 的“所有 orthants 都可达”可以看成这一机制的高自由度极端版本。

## 7. A3-G10 —— branch pattern 数量至多二次增长

取精确 basis `h_1,h_2` 后，第 `j` 个非恒定 guard 在 `(s,t)` 参数平面上只定义一条 affine threshold line：

\[
g_j+s h_{1j}+t h_{2j}=0.
\]

设实际非恒定 guard line 数为 `q`。

二维 `q` 条直线 arrangement 的全部 faces（regions + edges + vertices）最多为 simple arrangement 的：

\[
\boxed{2q^2+1.}
\]

binary `>=0 / <0` pattern 在每个 relative-open face 上恒定；integer lattice 取样只会删除某些 faces，不会创造新的 sign pattern。

因此：

\[
\boxed{
\#\{\text{reachable branch patterns in one rank-two fiber}\}
\le 2q^2+1.
}
\]

这说明 hidden rank 固定为 2 后，实际 branch geometry 至多二次增长，而不是程序语法表面上的 `2^r`。

该 arrangement face bound 属于成熟 hyperplane-arrangement 数学；A3 只把它作为 `W(K_A)` 的复杂度工具使用。

## 8. 实现

新增：

- `src/enterprise_math/rank_two_guard_reachability.py`；
- `tests/test_rank_two_guard_reachability.py`。

主要接口：

- `rank_two_lattice_basis`；
- `rank_two_basis_coordinates`；
- `rank_two_threshold_pattern_witness`；
- `rank_two_threshold_pattern_reachable`；
- `rank_two_threshold_pattern_face_bound`。

`RankTwoPatternWitness` 同时返回：

- exact lattice basis；
- integer parameters `(s,t)`；
- 实际 guard scores；
- certificate mode；
- bounded case 的 finite scan width。

## 9. 验证

当前验证包括：

1. 冗余 rank-two generators 的 exact basis reconstruction；
2. 原 generator 与大量整数 linear combinations 的 membership recovery；
3. strict recession witness；
4. recession ray/line witness 与 unreachable case；
5. bounded finite-scan witness；
6. bounded real-but-no-integer counterexample；
7. small rank-two families 上 closed solver 与 bounded parameter brute-force 的双向压力测试；
8. actual reachable pattern count 不超过 arrangement face bound。

另做了数千组随机小整数 rank-two lattice / base / pattern 压力测试，未发现 closed solver 与直接参数枚举冲突。该随机测试属于实现压力证据，不替代上面的整数证明。

当前环境仍无法通过本地 DNS clone GitHub，因此不声明全仓 pytest/CI 已通过。

## 10. 前人工作边界

以下均属于成熟数学工具，不能作为 A3 原创：

- Hermite normal form / integer lattice basis；
- Bezout 与 Smith/Hermite 型 subgroup reduction；
- 低维 integer linear feasibility；
- polyhedral recession cones；
- hyperplane arrangements 与 face-count bounds。

A3 当前 novelty 仍只处于未验证的组合/interface 层：

\[
W(K_A)
\to
\text{exact reachable branch patterns}
\to
\text{future-safe relation precision}.
\]

正式 novelty claim 前继续保持 `NOVELTY_UNVERIFIED`。

## 11. 下一步

rank 0、1、2 与 full-rank 端点现在都有 exact 处理。

下一步集中处理：

\[
\boxed{2<\operatorname{rank}L_G<r.}
\]

优先路线：

1. 把 rank-two 的 certificate 三分法抽象成 fixed hidden rank `d` 的 rational polyhedral cone / lower-rank face recursion；
2. 研究 fixed `d` 时 branch-pattern 数的 `O(r^d)` arrangement bound 与整数 lattice holes 的分离；
3. 判断是否可用 Smith/Hermite + fixed-dimension integer feasibility 形成统一 solver，而不在 A3 复制一般 Presburger/ILP 理论；
4. 将 rank-two branch reachability 接入 piecewise coarse-effect equality，形成 state-dependent exact branch-erasure checker；
5. 把该结果通过 Research Relay 回流 A2/P023，标记为 A3 specialization 与复杂度/precision obligation。
