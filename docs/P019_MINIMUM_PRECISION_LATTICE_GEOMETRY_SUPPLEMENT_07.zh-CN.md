# P019 补充 07 —— 压缩纤维见证与有向收缩链

状态：`RESEARCH WIP / PROVED LOCALLY + ENUMERATION PRESSURE TEST`

## 1. 目标

Supplement 06 已证明：

\[
\text{minimum value associativity}
\not\Rightarrow
\text{selected boundary witness associativity}.
\]

因此不能把 `ContractionTrace` 简单删掉；但也不能因此把每个细状态、每棵树、每个 fiber 全量保存。

本补充寻找介于二者之间的最小整数结构。

核心区分：

1. `minimum-value layer`：只问 fiber minimum；
2. `full-witness-relation layer`：保留所有当前可行 fine witnesses；
3. `selected-boundary layer`：每个有向 fiber 只选择一个右端/左端 boundary representative；
4. `historical-identity layer`：还要求知道真实发生的是哪一个 fine witness / 哪一条 contraction history。

这四层不能混写。

## 2. balanced power kernel 回顾

对 `m>=1, s>=1, c in Z`：

\[
\Psi_{m,s}(c)
=
\min_{a_1+\cdots+a_m=c}
\sum_{i=1}^m |a_i|^s.
\]

写

\[
|c|=mq+r,
\qquad 0\le r<m,
\]

则

\[
\boxed{
\Psi_{m,s}(c)
=(m-r)q^s+r(q+1)^s.
}
\]

并且

\[
\Psi_{m,s}(1)=1.
\]

## 3. P019-X09 —— `s>1` 时 minimum witness 的完整分类

当 `s>1` 时，固定总和 `c` 的 minimum fine witness 必须满足：

- 所有非零坐标与 `c` 同号；
- 任意两个绝对值之差至多为 1。

因此若 `|c|=mq+r`，每个 minimum witness 恰由：

- `m-r` 个绝对值 `q`；
- `r` 个绝对值 `q+1`

组成。

所以 labeled minimizer 数为

\[
\boxed{
M^{\min}_{m,s}(c)=\binom mr,
\qquad s>1.
}
\]

证明只需整数 exchange：若两个同号坐标满足 `u>=v+2`，则把 `(u,v)` 改为 `(u-1,v+1)` 严格降低 `u^s+v^s`；若同时存在正负坐标，则同时向 0 移一步保持总和不变并严格降能量。

### `s=1` 的特殊性

`Psi_(m,1)(c)=|c|`。此时 minimum witness 不要求均匀，只要求无符号抵消。

若 `c!=0`，minimum labeled witness 数为弱组合数

\[
\boxed{
M^{\min}_{m,1}(c)
=
\binom{|c|+m-1}{m-1}.
}
\]

所以 `s=1` 与 `s>1` 在 value 层统一，但 witness degeneracy 不同。

## 4. P019-X10 —— 两块 argmin profile 是有限整数区间

合并大小 `m,n` 的两个 blocks，总量为 `c`。

对 `s>1`，写

\[
|c|=(m+n)q+r,
\qquad 0\le r<m+n.
\]

设左 block 获得 `h` 个额外 `q+1` 槽位，则

\[
\max(0,r-n)
\le h\le
\min(m,r).
\]

若 `sigma=sgn(c)`，左、右 block totals 为

\[
a=\sigma(mq+h),
\qquad
b=c-a.
\]

对应的 labeled fine-witness multiplicity 精确为

\[
\boxed{
\binom mh\binom n{r-h}.
}
\]

全部 argmin multiplicity 求和：

\[
\sum_h
\binom mh\binom n{r-h}
=
\binom{m+n}{r}.
\]

所以 minimum-witness provenance 在 block merge 下是完全可组合的，不需要保留 contraction tree。

## 5. provenance polynomial

对多个 blocks `m=(m_1,...,m_k)`，总 remainder 为 `r`，定义

\[
P_{\mathbf m,r}(z_1,\ldots,z_k)
=
[t^r]
\prod_{i=1}^k(1+z_i t)^{m_i}.
\]

展开系数为

\[
[z_1^{h_1}\cdots z_k^{h_k}]
P_{\mathbf m,r}
=
\prod_i\binom{m_i}{h_i},
\qquad
\sum_i h_i=r.
\]

若合并 blocks `i,j` 并令 `z_i=z_j=z`，则对应因子严格变为

\[
(1+zt)^{m_i+m_j}.
\]

因此该 minimum-provenance 表达对 block merge 严格结合。

这是一种 candidate provenance tool；其一般 semiring/provenance 前人工作必须在合并前正式映射，本补充不作原创优先性声明。

## 6. P019-X11 —— 完整 fiber sublevel relation 只需两个整数

固定两块大小 `m,n`、总量 `c`，定义

\[
f(a)
=
\Psi_{m,s}(a)
+
\Psi_{n,s}(c-a).
\]

设 merged minimum 为

\[
f_{\min}=\Psi_{m+n,s}(c).
\]

给定非负 slack `omega`，定义可行 split：

\[
I_{m,n,s}(c,\omega)
=
\{a\in\mathbb Z:
 f(a)-f_{\min}\le\omega
\}.
\]

### 离散凸性

令

\[
\Delta\Psi_{m,s}(u)
=
\Psi_{m,s}(u+1)-\Psi_{m,s}(u).
\]

`Delta Psi` 在整数轴上非递减。

因此

\[
f(a+1)-f(a)
=
\Delta\Psi_{m,s}(a)
-
\Delta\Psi_{n,s}(c-a-1)
\]

也是非递减。

所以 `f` 是一维离散凸函数，其任意有限 sublevel set 都是整数 interval：

\[
\boxed{
I_{m,n,s}(c,\omega)
=[L,U]\cap\mathbb Z.
}
\]

于是完整 block-total witness relation 无需逐点保存，只需：

\[
\boxed{(L,U)}.
\]

其 block-total fiber multiplicity 为

\[
\boxed{M=U-L+1.}
\]

这直接把 P019 contraction fiber 接到 P011 multiplicity 语言。

## 7. directed boundary 是 fiber endpoint

若 transfer direction 规定 `donor -> receiver`，receiver total 记为 `a`，那么一条 split edge 穿出 sublevel ball 当且仅当

\[
f(a)\le f_{\min}+\omega
< f(a+1).
\]

因为 feasible set 是 `[L,U]`，唯一 right-boundary witness 就是

\[
\boxed{a=U.}
\]

反方向对应 `L`。

所以 boundary representative 不是新 primitive；它是 full fiber relation 的一个 endpoint selection。

## 8. 有向收缩历史 = partition lattice 上的 oriented maximal chain

从 `N` 个 labeled unit slots 开始，每一步合并两个当前 blocks。

忽略 receiver/donor 方向时，在当前有 `k` 个 blocks 的一步有

\[
\binom k2
\]

种 merge。

所以完整无向收缩链数为

\[
\boxed{
H_N^{\mathrm{unoriented}}
=
\prod_{k=2}^N\binom k2
=
\frac{N!(N-1)!}{2^{N-1}}.
}
\]

若每次 merge 还记录 receiver/donor 次序，则一步有 `k(k-1)` 种，故

\[
\boxed{
H_N^{\mathrm{oriented}}
=
\prod_{k=2}^N k(k-1)
=
N!(N-1)!.
}
\]

这说明 exact directed trace 若完全保留，会阶乘增长。

partition-lattice maximal-chain counting 是成熟组合数学；这里的贡献目标不是重命名该计数，而是研究它在 finite-precision contraction witness 中何时可以安全商掉。

## 9. P019-X12 —— oriented flag 足以重放 selected boundary witness

一个完整 oriented contraction history 记录每步 ordered pair：

`(receiver_block, donor_block)`。

给定：

- power `s`；
- global threshold `T`；
- 完整 oriented history；

可以从最终 single block `total=0` 反向逐步恢复：

1. 当前要拆的 merged block total 为 `c`；
2. 计算其他当前 blocks 的 minimum energy `E_other`；
3. 当前 fiber slack 为

\[
\omega
=T-E_{other}-\Psi_{m+n,s}(c);
\]

4. 计算 interval `[L,U]`；
5. 按该步方向取 `U` 作为 receiver total；
6. 重复直到 singleton partition。

因此 oriented partition flag + `(s,T)` 是 selected-boundary replay 的一个充分 trace。

## 10. 小维完整枚举：final partition 远远不够

对 `s=2`，直接枚举所有 labeled oriented contraction histories，并比较它们在多个 integer thresholds 下生成的完整 boundary-witness map。

结果：

- `N=3`：`12` 条 histories；在阈值扫描中得到 `12` 个不同 labeled witness maps；
- `N=4`：`144` 条 histories；得到 `144` 个不同 labeled witness maps；
- `N=5`：`2880` 条 histories；扫描偶数阈值 `0..100` 后得到 `2880` 个不同 labeled witness maps。

这不是一般 injectivity theorem，但它是很强的有限反例库：在这些规模上，没有任何两条不同 oriented histories 能在该测试族下被无条件合并。

所以不能声称“tree shape”“最终 block size”“最终 minimum energy”已经足够恢复 selected boundary history。

## 11. 当前最小层级表

### A. value only

保存：

`visible totals + block sizes + power`

即可。

### B. minimum witness multiplicity/provenance

对 `s>1`，保存 block sizes、totals/remainders；用 binomial / provenance polynomial 重建。

不需要 contraction history。

### C. full one-step fiber relation

保存两个 endpoint：

`[L,U]`。

### D. selected multi-step boundary witness

当前已知充分对象：

`oriented contraction flag + power + threshold`。

是否还能进一步压缩必须相对于“未来允许的操作/观测”定义，不能无条件删除。

### E. exact historical identity

若问题本身要求“真实发生的是哪一个 fine witness”，则任何把不同真实 witness 合并的 summary 都不是 history-exact。

这属于 provenance/ontology 选择，不应由 value algebra 偷偷决定。

## 12. 实现

新增：

- `src/enterprise_math/contraction_trace.py`
  - `balanced_minimizer_count`
  - `two_block_argmin_profile`
  - `fiber_witness_interval`
  - `fiber_witness_multiplicity`
  - `directed_boundary_split`
  - `reverse_boundary_witness`
  - partition-chain counts
- `tests/test_contraction_trace.py`

公式通过 `s=1..4`、多 block sizes、正负 totals、多个 slack 的穷举交叉检查。

## 13. 下一步

下一步不再追求一个“万能最小 trace”，而定义：

> 对指定 future operation family，什么是最粗但仍保持全部未来可组合性的 quotient？

这将在 Supplement 08 中形式化为 future-composition equivalence / safe trace erasure。
