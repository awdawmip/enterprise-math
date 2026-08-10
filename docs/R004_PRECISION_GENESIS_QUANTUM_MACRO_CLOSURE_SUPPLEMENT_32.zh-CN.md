# R004 精度起源——补充 32：无分数 COUNT coupling basis 与 Smith 出生谱

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + COUNT-COUPLING SPECIALIZATION`
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_31.zh-CN.md`
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 31 给出了 joint coupling 的 typed liveness gates。本补充专门处理 exact COUNT semantics，并为 one-way marginals 之外剩余的信息构造纯整数 basis。

## 1. Marginal-star / coupling-cell 分解

joint COUNT tensor 的 shape 记为 `(n_1,...,n_m)`，每个 axis 选一个 base value。base cell 或只在一个 coordinate 上偏离 base 的 cell 称为 star cell；至少两个 coordinates 同时偏离 base 的称为 coupling cell。

star cells 数为

`1 + sum_i(n_i-1)=sum_i n_i-(m-1)`，

coupling cells 数为

`d_coup=prod_i n_i-sum_i n_i+(m-1)`。

one-way marginal incidence map 的整数 rank 正好是 `sum_i n_i-(m-1)`，因此 joint-cell lattice 对 marginal row lattice 的 quotient 是 rank `d_coup` 的自由整数 lattice。

## 2. 无分数重建

保留全部 one-way marginals 与全部 coupling-cell counts。每个 single-change star cell 都可从对应 marginal 减去同一 marginal 中的 coupling cells 得到；最后 base cell 用 total count 减去所有 non-base cells 得到。

全程只有整数加减，不需要概率、比例、normalization 或除法。

## 3. 整数 coupling residual

对 integer query coefficient tensor `c`，由 base/star cells 构造 marginal-separable interpolation：

`c_hat(y)=c(base)+sum_i(c(star_i(y_i))-c(base))`。

令 `r_c=c-c_hat`。它在全部 star cells 上自动为 0，只在 coupling cells 上存活。`r_c` 在 coupling cells 上的坐标恰好给出 marginal row lattice 之外的整数 quotient coordinate。

因此一族 coupled COUNT queries 可以被编译成 `d_coup` 个 coupling coordinates 上的 integer residual matrix。

## 4. Smith 出生谱

若 residual query matrix 的非零整数 Smith invariants 为 `d_1,...,d_r`，则 p-adic cap K 下第 j 个 direction 的实际 depth 为

`e_j(K)=max(0,K-nu_p(d_j))`。

它的出生层为 `K_birth(j)=nu_p(d_j)+1`，总 coupling mass 为

`mu_K=sum_j max(0,K-nu_p(d_j))`。

因此 `mu_(K+1)-mu_K` 正好数当前已经出生的 directions；second finite difference 数新一层刚出生的 directions。

2x2 equality COUNT 的 coupling residual 只有一个 coefficient `2`：mod 2 完全不可见，mod 4 出生 1 bit，mod 8 有 2 bits；odd prime 下从第一层就 full-depth。

## 5. 坐标不唯一，但结构不变

改变 base tuple 会改变具体 coupling-cell coordinates，但每个 base 都给同一个 quotient lattice 的 integral splitting；不同坐标之间由 unimodular transformation 相连。因此 Smith invariants 与 p-adic birth spectrum 都与 base choice 无关。

## 6. 验证

研究过程中已对小 2D/3D shapes 做 exact marginal reconstruction；Supplement 31 的 COUNT liveness 做过全枚举；400 个随机 query families 在所有 base choices 下的 Smith invariants 一致；2x2 equality residual 精确为 2。

这里是 integer marginal lattice / Smith normal form 在 Representation Compiler 中的 specialization，不主张 contingency-table algebra 为新数学。

## 7. 直接后果

joint COUNT coupling 的无分数 primitive surface 是：

`one-way marginals + d_coup coupling counters`。

对具体 query family，真正 live 的 residual Smith profile 可以远小于完整 `d_coup`。因此 coupling distinction 会随 precision layer 出生，而不是一个从一开始就全部存在的 correlation state。
