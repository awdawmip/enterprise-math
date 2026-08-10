# R004 精度起源——补充 36：p-adic precision-native covering ISA

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + PRECISION-RESOURCE SPECIALIZATION`
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_35.zh-CN.md`

补充 35 已把 full additive finite-field primitive ISA 精确识别成 linear covering-code problem。本补充把同一 compiler 问题提升到 precision-native ring `R_K=Z/p^K Z`，研究 K 增长时 minimum primitive storage 如何变化。

finite chain ring 上的 linear code 与 projective Hjelmslev geometry 都是先行数学。R004 当前只保留 precision/resource 的 compiler 解释。

## 1. Ring null-program 模型

设 `H:R_K^s -> R_K^r` 为 surjective R_K-linear primitive-action map，null-program module 为 `C=ker H`。因为 `R_K^r` 是 free/projective，exact sequence split，C 是 rank `s-r` 的 free direct summand。

semantic action y 的 primitive readout depth 等于所有 `H e=y` coefficient words 的最小 Hamming support，也就是 coset 到 C 的最小 Hamming distance；worst readout depth 因而就是这个 R_K-linear null-program code 的 Hamming covering radius。K=1 时精确退化到补充 35。

## 2. Precision 单调性

定义 `L_(p,K)(r,D)` 为 R_K 上 semantic rank r、worst readout depth 不超过 D 的最小 primitive storage s。

任何 `(K+1)`-precision ISA mod `p^K` 后仍是 K-precision ISA，且 word support 不增加，因此

`L_(p,K)(r,D) <= L_(p,K+1)(r,D)`。

提高 p-adic precision 永远不会让 fixed-depth primitive ISA 变便宜。

## 3. Ring Hamming-volume 下界

令 `q=p^K`。support 不超过 D 的 coefficient words 数为

`V_(p,K)(s,D)=sum_(j=0)^D binom(s,j)(q-1)^j`。

semantic actions 有 `q^r` 个，所以必须 `V_(p,K)(s,D)>=q^r`。

对 fixed `D<r`，由 `V <= (D+1)s^D q^D` 得到纯整数增长律

`(D+1)s^D >= p^(K(r-D))`。

因此当 readout depth 固定低于 r 时，primitive storage 必须随 precision cap K 指数增长。

## 4. Exact 一步 storage

D=1 时，每个 nonzero semantic vector 必须落在某一 primitive column 生成的 cyclic submodule 中。

`R_K^r` 的 primitive vectors 数为 `p^(Kr)-p^((K-1)r)`；每条 free rank-one line 有 `p^K-p^(K-1)` 个 primitive generators；primitive vector 只属于唯一 free line。因此

`L_(p,K)(r,1)=p^((K-1)(r-1))*(p^r-1)/(p-1)`。

从而

`L_(p,K+1)(r,1)=p^(r-1)L_(p,K)(r,1)`。

每提高一层 p-adic precision，一步 ISA storage 精确乘 `p^(r-1)`。

## 5. Exact one-null-program 区间

若 `s=r+1`，null-program module rank 为 1。最优 rank-one null code 的 generator 必须所有 coordinates 都是 units；经 coordinate unit scaling 可归一化为 repetition line `<(1,...,1)>`。

令 `q=p^K`, `n=r+1`，worst covering radius 精确为

`D_one-null=n-ceil(n/q)`。

相对 bare basis 的 depth gain 为

`ceil((r+1)/p^K)-1`。

一旦 `p^K>=r+1`，多出的这一个 null instruction 对 worst-case readout depth 完全没有改善。

因此低 precision 世界中有价值的 redundancy，精度提高后可能 execution-useless。

## 6. 最小 precision phase-change 例子

取 p=2、semantic rank r=3、目标 D=2。

K=1 时 4 条 primitives 足够，binary one-null repetition code radius=2。

K=2，即 `R=Z/4` 时，所有 s=4 ISA 都只有 rank-one null module，由上式 radius 至少为 3。identity-normalized exhaustive search 把 s=5 的 1,953 个 extra-column pairs 全部扫完，没有一个 depth-2 covering。

而 6-column ISA

`(1,0,0),(0,1,0),(0,0,1),(0,1,1),(0,1,2),(1,1,3)`

能在最多两条 primitives 内覆盖全部 `(Z/4)^3` semantic actions。

所以 declared ring-linear ISA model 中：

`L_(2,1)(3,2)=4`,
`L_(2,2)(3,2)=6`。

precision refinement 改变的不只是旧 primitives 的 bit depth，而是 minimum primitive 数量本身。

## 7. Algebra type 不能省略

alphabet cardinality `p^K` 不能单独决定 compiler。K>1 时 `Z/p^K` 是 finite chain ring，不是同 cardinality finite field。projective directions、null modules 与合法 scalar actions 都取决于 declared algebra。

因此正确 resource law 是：

`precision + typed algebra + future readout depth -> primitive storage requirement`。

## 8. 先行研究边界

finite chain ring linear codes、projective Hjelmslev geometry 与 modular-ring covering research 都有成熟先行工作。R004 不主张 ring coding theory；这里只保留 precision-native primitive-ISA reduction、D=1 / one-null closed forms，以及 K 作为 representation resource layer 的解释。

## 9. 下一 frontier

下一题是 precision lifting：K 层已有 ISA 升到 K+1 时，哪些 columns 可以保留、哪些 primitive directions 必须新出生、minimum ISA 能否跨 precision 嵌套，以及没有 nested optimum 时是否需要 anticipatory storage。这是 temporal instruction retirement 的 precision-lift 对偶问题。
