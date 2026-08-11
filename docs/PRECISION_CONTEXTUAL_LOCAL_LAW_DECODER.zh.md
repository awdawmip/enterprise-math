# Contextual Local-Law Reflection 与 Modular-Only Decoder

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

bounded-local-law theorem 现在可以分成三个精度层次。全局 finite alphabet 给出清晰的 class-wide guarantee；realized split-content spectrum 则在跑过具体 refinement trajectory 后给出 one-world 的 sharp answer。两者之间还缺一层重要结构：**contextual codebooks**。

只要两个 exact values 永远处在 future language 已经区分开的 semantic coordinates 中，它们即使映到同一个 residue 也不会产生歧义。因此 precision 真正要求的不是“所有可能值全局唯一编码”，而是：**会在同一个语义槽位中竞争的值必须可区分。**

## 1. Weighted signature coordinate 自带 side information

对有限整数 weighted relation family 与 initial observation `O`，后续每一轮 partition 都 refine 初始 observation。

因此一个 local weighted transition coefficient 至少天然带有：

`(action, source initial-observation class, target initial-observation class)`

三个标签。

把这样的 triple 记为 semantic coordinate c。

对每个 c，收集在 target observation class 内继续 split 后，可能落入该 coordinate 的所有 exact target-block aggregates，得到有限 codebook：

`L_c subset Z`。

## 2. Contextual reflection theorem

令 `rho_M(z)=z mod M`。

若 `rho_M` 在每一个 `L_c` 内分别 injective，则完整 mod-M weighted refinement sequence 与 exact integer refinement sequence 完全相同。

### 证明结构

对任意后续 partition P：

- 一个 source block 仍包含在某个初始 source-observation class 内；
- 一个 target block 仍包含在某个初始 target-observation class 内；
- 因而固定 action/source-block/target-block coordinate 的 exact aggregate 必属于一个固定 `L_c`。

若同一 current source block 内两 states 的 modular signature vectors 相等，则每个 coordinate 内的 injectivity 都迫使 exact coordinate values 相等，因此 exact signature vectors 相等。于是一次 modular refinement step 与一次 exact step 相同；归纳即可得到直到 stability 的完整 equality。

## 3. Cross-coordinate collision 是无害的

把所有 local values 先做一个 global union 是安全的，但可能过度要求 numeric precision。

例如：

- action a 的 admissible values 是 `{0,1}`；
- action b 的 admissible values 是 `{0,4}`。

mod3 下 exact1 与4 在全局上 collision，但它们位于不同 action coordinates，永远不会作为同一 slot 的候选值互相比对。

mod3 分别在 `{0,1}` 与 `{0,4}` 内都是 injective，因此仍能完整复制 exact weighted refinement。

同样的压缩也可以来自 source-observation 或 target-observation context。

## 4. Context 本身就是 precision 的一部分

正确的 decoding 问题不是：

`residue r 能不能唯一确定一个全局 integer?`

而是：

`(semantic coordinate c, residue r)`

能否在 `L_c` 中唯一确定一个 admissible exact integer。

这就是带 side information 的 finite decoding。

它再次说明 task-relative precision 不能只用一个 raw modulus 或一个 global value alphabet 来定价。

## 5. 三层 precision guarantee

### Class-uniform primitive sumset

给定 primitive set P 与 local contribution 上限 d，要求 quotient 在 universal bounded sumset `S_d(P)` 上 injective。

这保证整个 world class 都 exact。

### Fixed-world contextual codebooks

利用真实 action 与 initial observation 结构，把 admissible alphabet 拆成 contextual codebooks `L_c`。

只要求每个 `L_c` 内 injective。它仍是静态、pre-execution 的 guarantee，但可能严格降低 safe modulus。

### Realized split-content spectrum

沿 exact refinement trajectory 只保留实际发生的 strict split differences。

已有 split-content theorem 给出该 concrete world 的 exact bad-modulus set。

因此可把三者理解为：

`universal class precision >= contextual guaranteed precision >= realized one-world precision`

这里比较的是 guarantee 的保守程度 / 假设强度，并不声称任意 representation family 中都存在一条单调 numeric scalar chain。

## 6. Modular-only decoder 消除 verification circularity

真正的 reflection compiler 不能先偷看 exact primitive weights，再宣称自己从 quotient 中恢复了 exact local law。

因此 contextual decoder 的输入只包括：

- exact state / edge incidence structure；
- primitive edge weights 的 canonical mod-M residues；
- 一个 refine observation 的 quotient partition；
- semantic context labels；
- 每个 coordinate 的 finite exact admissible codebook `L_c`。

Decoder **不会读取 exact primitive integer weights**。

对每个 action / source quotient block / target quotient block，它执行：

1. 在 mod M 中累加 primitive residues；
2. 检查 source representatives 的 modular block-weight vector 是否一致；
3. 确定 semantic coordinate c；
4. 在 `L_c` 内唯一 lift 该 residue。

所有 lifted vectors 组成 exact integer quotient matrices。

## 7. Sharp modular-only witness

取一个 action，两 source states 属于同一个 source observation class：

- x 以 weight1 指向 target observation class T1；
- y 以 weight4 指向另一个 target observation class T2。

在 mod3 中，两条 primitive weights 都只保存成 residue1。

Decoder 没有任何 exact primitive weight 输入，但可以恢复：

- T1 coordinate 中 residue1 的唯一 admissible lift 是1；
- T2 coordinate 中同一个 residue1 的唯一 admissible lift 是4。

因此相同 residue 可以借助显式 semantic side information 获得不同、但无歧义的 exact meaning。

## 8. Reflect before compose 的结论不变

Contextual decoding 只是进一步降低“恢复 exact local machine”所需的 precision。

恢复以后，future composition 在 exact integer algebra 中执行，可以生成远大于 M 的 derived values。

若一直停留在 `Z/MZ` 内执行，large derived values 仍然可能 collision。Contextual local reflection 并没有把 finite quotient 变成 globally exact execution algebra。

## 9. Structural scope boundary

当前 decoder 假设 edge incidence / primitive contribution identity 由独立 structural channel 保留；只有 integer primitive weights 被 quotient-coded。

若 coefficient collapse 同时擦掉 edge/support/witness structure，则还需要独立的 support / RELATION reflection theorem。Coefficient exactness 不能恢复从未保留过的结构。

## 10. Arithmetic interpretation

对一个 finite codebook S：

`mod M 在 S 上 injective`

当且仅当 M 不整除任何 nonzero difference `u-v`（`u!=v`，`u,v in S`）。

有多个 contextual codebooks 时，只需考虑**同一 context 内**的 difference spectra；cross-context differences 可以直接从 bad-modulus condition 中删除。

这给出下一条明确数论前沿：不再按 global interval width 选 modulus，而是直接针对 contextual difference-divisor spectrum 设计最小 modulus / CRT family。

## Owner-local assets

- `src/enterprise_math/contextual_local_law_decoder.py`；
- `tests/test_contextual_local_law_decoder.py`；
- 本双语 companion note。

parent bounded-local-law generation 继续拥有 generic class-uniform theorem 与 realized split-content theorem。

## Prior-art / status

带 side information 的 finite-alphabet decoding、modular residue coding、context-dependent codebooks 都是标准既有概念。P023/A2 保留 generic precision / future-signature ownership。本文只拥有 Enterprise Math 的 contextual-reflection routing 与 modular-only decoder specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。Hard block：`NONE`。
