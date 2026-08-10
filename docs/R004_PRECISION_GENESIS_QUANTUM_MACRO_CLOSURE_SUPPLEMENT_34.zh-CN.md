# R004 精度起源——补充 34：binary k-local storage/update/readout Pareto

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + RESOURCE-PARETO SPECIALIZATION`
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_33.zh-CN.md`

在 full binary additive semantic module `F_2^r` 中，对 `1<=k<=r`，令 primitive ISA 包含全部 Hamming weight 不超过 k 的 nonzero vectors。

## 1. Exact family

primitive storage 数：

`S_k=sum_(j=1)^k binom(r,j)`。

streaming witness-update incidences：

`U_k=sum_(j=1)^k j*binom(r,j)=r*sum_(j=0)^(k-1)binom(r-1,j)`。

Hamming weight 为 w 的 semantic vector 的 exact 最短 readout length 为

`ell_k(w)=ceil(w/k)`。

下界来自一个 primitive 最多覆盖 k 个 support coordinates；上界来自把 support 分成大小不超过 k 的 disjoint chunks。

所以最坏 readout depth：

`D_k=ceil(r/k)`，

所有 nonzero semantic queries 的总 readout word length：

`R_k=sum_(w=1)^r binom(r,w)*ceil(w/k)`。

## 2. Pareto 解释

- `k=1`：basis/Hasse ISA，storage/update 最小，但最坏 readout depth 为 r；
- `k=r`：完整 semantic table，`2^r-1` 个 primitives，所有 query 一步读出；
- 中间 k 用持续 storage/write 成本换更短的 future semantic execution。

这与 Stage131 rule-table 的 storage/execution-depth Pareto 是同一个 finite compilation pattern 在 counter ISA 上的 specialization。

## 3. 重要负边界

k-local family 是透明 construction，不是 fixed readout depth 下的一般 storage optimum。补充 35 将 unrestricted optimization 精确识别为 linear covering-code length problem；其最佳 constructions 可以远小于 k-local table。

## 4. 验证

参考公式已通过小 rank semantic vectors 的 exact support partition 与 exhaustive enumeration 检查。
