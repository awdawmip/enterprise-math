# Prefix Semantic Quotient 下 Literal Words 的 Exact Fibers

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Class count 只能说明 literal words quotient 后还剩多少 semantic states，却不能说明每个 semantic class 实际吸收了多少 literal syntax。

对 terminal / discovery / timing ladder，这些 quotient fibers 可以精确计算。结果表明 full-timing 层的 semantic redundancy 非常不均匀。

## 1. Fixed setup

取 k 个 generator labels 与 exact literal word length H。

假设一个 word 一共使用 s 个 distinct generators。

Semantic ladder：

`literal word -> full timing RLE -> discovery order -> terminal set`。

我们计算每一层具体 quotient class 的 fiber cardinality。

## 2. Terminal-set fiber

固定一个特定 s-element terminal generator set S。

该 fiber 内的 literal words 恰好是长度 H、alphabet=S、且每个 symbol 至少出现一次的 words，也就是从 H 个 labelled positions 到 s 个 generator labels 的 surjections。

数量：

`F_terminal(H,s)=s! * S(H,s)`，

其中 `S(H,s)` 是 Stirling number of the second kind。

`s!` 用来把 s 个 partition blocks 分配给真实 generator labels。

## 3. Discovery-order fiber

固定一个 ordered first-appearance list：

`(g_1,...,g_s)`。

每个 generator 对应的 literal positions 把 H 个 positions 划成 s 个 nonempty blocks。按每个 block 的 least position 排序后，generator labels 已由 `(g_1,...,g_s)` 唯一确定。

所以：

`F_discovery(H,s)=S(H,s)`。

这正是 restricted-growth-string 与 set partition 的标准 correspondence。

## 4. Terminal fiber 比 discovery fiber 大 s! 倍

一个 terminal set 会忘记所有 `s!` 种 first-appearance orders。

因此：

`F_terminal(H,s)=s! * F_discovery(H,s)`。

Executable layer 既核该 identity，也在 bounded literal words 上直接按 quotient 分组核实。

## 5. Full-timing fiber 取决于 duration vector

固定一个 exact RLE semantic form：

`((g_1,r_1),...,(g_s,r_s))`，

其中所有 `r_i>=1`，且 `sum r_i=H`。

Phase i 中：

- 第一条 action 必须是 newly introduced generator `g_i`；
- 后续 `r_i-1` 个 positions 可以任取当前已经 discovered 的 i 个 generators，而 prefix state 不变。

所以这个具体 timing fiber 下 literal words 数精确为：

`F_timing(r_1,...,r_s)=product_(i=1)^s i^(r_i-1)`。

Branch 通过实际 literal-word grouping 逐 RLE class 验证该公式。

## 6. Timing fibers 高度 nonuniform

固定 H 与 s，把 `H-s` 个 extra stutter positions 分配给 s 个 phases。

### Minimum fiber

把所有 extra stutters 都放在 phase1。

Phase1 只有一个已见 generator，所以：

`F_min=1`。

确实存在只对应一个 literal word 的 timing classes。

### Maximum fiber

把所有 extra stutters 放在 phase s。

此时 s 个 generators 都已经 available：

`F_max=s^(H-s)`。

所以同一个 H、s 下，timing fibers 的大小可以相差 stutter count 的指数因子。

## 7. Timing fibers 求和恢复 discovery fiber

固定一个 s-generator discovery order。其下 full-timing classes 对应 positive compositions：

`r_1+...+r_s=H`。

把所有 timing literal fibers 加总：

`sum_(r_i>=1,sum H) product_i i^(r_i-1)=S(H,s)`。

这正好恢复 discovery-order fiber。

Branch 对一大段 bounded H/s 逐项验证该 identity。

## 8. Discovery fibers 求和恢复 terminal fiber

一个 fixed s-element terminal set 下有 `s!` 个 discovery orders，每个 fiber size 都是 `S(H,s)`。

因此总和：

`s! S(H,s)`，

精确恢复 terminal quotient fiber。

## 9. Terminal fibers 重建全部 literal words

先以 `C(k,s)` 种方式选 s-element terminal set，再对 s 求和：

`sum_s C(k,s) s! S(H,s)=k^H`。

这就是按 used distinct symbols 数量分解全部 k-ary length-H words 的标准 identity。

Executable compiler 会通过 terminal fibers 独立重建 `k^H`。

## 10. Discovery fibers 也独立重建全部 literal words

Ordered s-tuple distinct generator identities 有：

`P(k,s)=k!/(k-s)!`

种，每个 discovery order 下有 `S(H,s)` 个 literal words。

因此：

`sum_s P(k,s) S(H,s)=k^H`。

两种 reconstruction 对 quotient hierarchy 提供独立 consistency check。

## 11. Semantic class count 不足以决定 cache savings

若 literal cache 按 full prefix timing dedup，semantic entries 数量只是一个 resource。

每个 entry 实际合并多少 syntax 取决于 duration pattern。

Early phases 长时间 stutter 的 class 可能 fiber 极小；stutter 都发生在许多 generators 已 visible 后的 class，则可以吸收多达 `s^(H-s)` 个 literal words。

所以 average compression ratio 会掩盖很强的 heterogeneity。

## 12. Uniform literal workload 会诱导 nonuniform semantic probabilities

若所有 `k^H` literal words 等概率，则一个 semantic class 的 probability 正比于它的 fiber size。

Terminal / discovery 层在 fixed s stratum 内 fiber size 只依赖 s，因此 classes 等概率。

Full timing 层即使 s 相同也**不等概率**：duration vector 直接控制 fiber size。

这会影响 expected cache hit rate、entropy coding 与 workload-aware representation optimization。

本文不再扩 average-case optimization theorem；这里只提供 exact input distribution。

## 13. Precision interpretation

沿 quotient ladder 向下会删除不同 semantic distinctions：

- timing -> discovery 删除 duration placement；
- discovery -> terminal 删除 first-appearance order；
- 若还要从 terminal 反推 literal，则必须恢复所有 repeated-action provenance。

Fiber formulas 精确测量每一层中多少 literal syntax 变成 semantic indistinguishable。

## 14. Stage131 consequence

Representation-resource analysis 现在可以进一步区分：

- semantic cache entry count；
- maximum fiber / best-case dedup；
- minimum fiber / worst-case dedup；
- workload-weighted fiber distribution；
- semantic entry 到 required outputs 的 decoder cost。

所以 “semantic class count” 自己也不是完整的 storage / compression descriptor。

## Owner-local assets

- `src/enterprise_math/prefix_semantic_fiber_decomposition.py`；
- `tests/test_prefix_semantic_fiber_decomposition.py`；
- 本双语 theorem note。

## Prior-art / status

Stirling numbers、surjection、restricted-growth string 与 positive composition 都是标准既有 combinatorics。P023/A2 保留 future-signature / precision ownership。本文只拥有 exact semantic-fiber accounting specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
