# P019 补充 21 —— 关系场上的 Graph / Radial 球观察量

状态：`RESEARCH WIP / EXACT INTEGER IDENTITIES PROVED`

## 1. 目标

此前 graph ball 与 radial/collision-power ball 都已经统一到 weighted relation contraction。

还剩一个概念残余：ball membership 的定义仍常写成 block totals `c_i` 的函数。

本补充证明：至少最关键的 `s=1` 与 `s=2` 两层，都可以直接解释成同一个 weighted relation state 上的整数 observation functional。

关系本体不变；改变的是观察方式。

## 2. zero-total weighted cut identity

当前 blocks 有 capacities `m_i`、totals `c_i`，并满足：

\[
C=\sum_i c_i=0.
\]

总 capacity：

\[
M=\sum_i m_i.
\]

对任意 block subset `S`，定义 directed relation cut：

\[
Z(S,S^c)
=
\sum_{i\in S}
\sum_{j\notin S}Z_{ij}.
\]

由：

\[
Z_{ij}=m_jc_i-m_ic_j
\]

得到：

\[
Z(S,S^c)
=M_{S^c}C_S-M_SC_{S^c}.
\]

由于：

\[
C_{S^c}=-C_S,
\qquad
M_S+M_{S^c}=M,
\]

所以：

\[
\boxed{
Z(S,S^c)=M C_S.
}
\]

## 3. P019-X71 —— graph radius 是 relation field 的最大 directed cut

在所有 subsets 中，`C_S` 的最大值由取所有正 total blocks 得到：

\[
\max_SC_S
=
\sum_{c_i>0}c_i.
\]

零和条件下：

\[
\sum_{c_i>0}c_i
=
\frac12\sum_i|c_i|.
\]

因此：

\[
\boxed{
\max_S Z(S,S^c)
=M\sum_{c_i>0}c_i.
}
\]

而 collision-power family 的 `s=1` cost：

\[
E_{\mathbf m}^{(1)}(c)
=
\sum_i|c_i|.
\]

所以：

\[
\boxed{
M E_{\mathbf m}^{(1)}
=2\max_S Z(S,S^c).
}
\]

右侧一定被 `M` 精确整除。

对 unit `A_p`，`M=N=p+1`，且：

\[
E^{(1)}=2d_G.
\]

因此：

\[
\boxed{
N d_G(0,x)
=
\max_S Z(S,S^c).
}
\]

所以 primitive graph radius 可以完全由 pair/weighted relation field 的 max-cut observation 读取，不需要外部坐标轴或角度。

## 4. P019-X72 —— unit radial `q` 是 relation field 的 square-sum observation

unit capacities 下：

\[
Z_{ij}=d_{ij}=x_i-x_j.
\]

定义：

\[
P=\sum_{i<j}d_{ij}^2.
\]

Supplement 11 已证明零和时：

\[
\boxed{P=2Nq.}
\]

因此：

\[
\boxed{
q=P//(2N).
}
\]

所以在同一个 unit relation field 上：

- graph radius：max directed cut；
- radial quadratic state：all-pair square sum。

它们不是两个不同底层几何，而是同一个 relation object 的不同整数观察量。

## 5. coarse blocks 的内部最小 pair dispersion

对 capacity `m`、total `c` 的一个 coarse block，若把其内部 `m` 个 unit slots 以 square-energy minimum 方式平衡，则内部 pair dispersion：

\[
P_{internal}^{min}
=m\Psi_{m,2}(c)-c^2.
\]

Supplement 09 给：

\[
\boxed{
P_{internal}^{min}
=\varepsilon_m(c)
=r(m-r),
\qquad r=|c|\bmod m.
}
\]

这是 bounded integer residue。

## 6. P019-X73 —— 两 coarse blocks 的最小 cross-pair dispersion

取两个 blocks：

- capacities `m,n`；
- totals `a,b`；
- internal minimum dispersions：
  \[
  \varepsilon_m(a),\ \varepsilon_n(b);
  \]
- weighted relation：
  \[
  Z=na-mb.
  \]

令 `C_AB^min` 为两块各自内部取 balanced minimum 后，所有跨块 unit-pairs 的 squared difference 总和。

则：

\[
\boxed{
mnC_{AB}^{min}
=
n^2\varepsilon_m(a)
+m^2\varepsilon_n(b)
+Z^2.
}
\]

### 证明

设 blocks 内 unit values 分别为 `x_i,y_j`。

\[
C_{AB}
=\sum_{i\in A,j\in B}(x_i-y_j)^2.
\]

展开：

\[
C_{AB}
=n\sum_Ax_i^2
+m\sum_By_j^2
-2ab.
\]

又有：

\[
m\sum_Ax_i^2=a^2+P_A,
\qquad
n\sum_By_j^2=b^2+P_B.
\]

乘以 `mn`：

\[
mnC_{AB}
=n^2P_A+m^2P_B+(na-mb)^2.
\]

在 balanced minimum 时：

\[
P_A=\varepsilon_m(a),
\qquad
P_B=\varepsilon_n(b).
\]

得证。∎

所有除法在合法整数 state 上都是 exact。

## 7. P019-X74 —— tagged square energy 可完全由 weighted relation geometry 重建

对全部 coarse blocks，令：

\[
P_{min}
=
\sum_i\varepsilon_{m_i}(c_i)
+
\sum_{i<j}C_{ij}^{min}.
\]

这是把每个 block 内部展开成 balanced unit representative 后的完整 all-pair dispersion。

若 grand total 为零，总 unit count/capacity 为 `M`，则对 expanded unit state：

\[
P_{min}
=M\sum_{units}x_u^2.
\]

而：

\[
E_{\mathbf m}^{(2)}
=
\sum_i\Psi_{m_i,2}(c_i)
=
\sum_{units}x_u^2.
\]

因此：

\[
\boxed{
P_{min}
=M E_{\mathbf m}^{(2)}.
}
\]

于是：

\[
\boxed{
E_{\mathbf m}^{(2)}
=P_{min}//M.
}
\]

其中每个 `C_ij^min` 又由 X73 的：

`capacity + local residue + weighted Z_ij`

重建。

所以 tagged radial square ball membership 可以完全从 current weighted relation state 与 capacities 读取，不需要保存 underlying fine unit allocation。

## 8. graph/radial 的最终关系层对照

当前得到：

### graph / `s=1`

\[
\boxed{
E^{(1)}
=2\max cut(Z)//M.
}
\]

### radial square / `s=2`

\[
\boxed{
E^{(2)}
=P_{min}(Z,m,\varepsilon)//M.
}
\]

两者底层都只需要：

\[
\boxed{
\text{capacity-weighted relation state}.
}
\]

差别是 observation functional：

- `s=1` 读取最大 directed cut；
- `s=2` 读取平方 relation dispersion + bounded internal residue。

因此此前“graph geometry vs radial geometry”的语言可进一步替换成：

> **relation geometry 上的不同 observation channels。**

## 9. 与有限精度的关系

同一个 underlying weighted relation state 可以被不同 observation order 映射到不同 coarse scalar。

这符合此前结论：

\[
\text{same integer distance}
\ne
\text{same relation state}.
\]

反过来现在又得到：

\[
\text{same relation state}
\to
\text{可选择不同 finite observations}.
\]

所以 scalar distance 更明确地降为 relation state 的观察影子，而不是本体。

## 10. 与“挖球”的关系

Supplement 16 X53 的 directional boundary theorem 可以重述为：

- 先在 weighted relation state 上选 observation functional `E^(s)`；
- 取其 sublevel set / ball；
- 沿 internal relation kernel direction 移动；
- directional boundary 每个 coarse quotient fiber 恰取一个 endpoint；
- 该 endpoint set 与降一维后的 weighted relation ball 双射。

所以“挖球后表面降一维”已经不依赖把球先嵌入连续空间。

## 11. 实现与验证

新增：

- `src/enterprise_math/relation_geometry.py`
  - directed weighted cut sum；
  - maximum directed cut；
  - zero-total graph radius / `s=1` energy；
  - unit relation-field quadratic `q`；
- `src/enterprise_math/weighted_relation_geometry.py`
  - minimum cross-pair dispersion；
  - balanced expanded pair dispersion；
  - zero-total square energy from weighted relations；
- 对应测试：
  - `tests/test_relation_geometry.py`；
  - `tests/test_weighted_relation_geometry.py`。

整数回归验证 max-cut identity、unit `P=2Nq`、X73 cross formula 与 explicit balanced expansion、以及 relation-based `E^(2)` 与直接 `Psi` 计算一致。

## 12. 研究纪律

max-cut、graph Laplacian quadratic forms、variance/pairwise-square identities 都有成熟前人工作。

本补充不把这些一般工具当原创。

当前 P019 的研究连接是：

- 以 finite-precision weighted relation state 为共同底层；
- 把 graph/radial distance 降为不同 observation channels；
- 再把同一 directional quotient theorem 作用到这些 channels。

## 13. 下一步

1. 判断 `s>=3` 是否也存在直接 relation-field observable，而无需展开 child allocation；
2. 比较 max-cut 与 square-dispersion observation 的共同 algebraic properties，寻找统一但不过强的 relation-observable 接口；
3. 把 graph/radial ball 的 membership/boundary reference implementation 改为 relation-first API；
4. 对 intrinsic automorphism directions 直接作用 relation field，研究 observation channel 的 direction dependence；
5. 检查物理 pressure tests 中哪些量其实只需要 relation state，不需要 coordinate embedding。
