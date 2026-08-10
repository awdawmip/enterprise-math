# R004 精度起源——补充 28：multi-target structural synergy

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + NONDISTRIBUTIVE TARGET INTERACTION`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_27.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 27 已给出 observation loss 与 target liveness 的二维 interaction module。本补充研究多个同时存在的 target modules，并关闭第一条 non-distributive boundary。

## 1. Joint target defect

令 U 为 current observation row module，W1,W2 为两个 target row modules。joint target 为

`W12=W1+W2`。

defect mass 为

`delta(U,W)=mu(W)-mu(U cap W)`。

如果只对 W1、W2 及其 intersection 做普通 inclusion-exclusion 会漏项，因为在 modular 但非 distributive 的 subgroup lattice 中，

`U cap (W1+W2)`

可以严格大于

`(U cap W1)+(U cap W2)`。

## 2. Structural synergy module

定义

`S_U(W1,W2)=(U cap (W1+W2))/((U cap W1)+(U cap W2))`。

该 quotient 为零，当且仅当 U-intersection 在这一组 target sum 上正好 distributive。

由 subgroup-sum cardinality identity 可得 exact formula：

`delta(U,W1+W2)`
` = delta(U,W1)+delta(U,W2)`
`   - delta(U,W1 cap W2)`
`   - mu(S_U(W1,W2))`。

所以 naive inclusion-exclusion 对 joint missing structure 的 overcount，精确等于 synergy module。

## 3. 最小 XOR-style example

在 `F_2^2` 上取

`U=<e1+e2>`, `W1=<e1>`, `W2=<e2>`。

则 `U cap W1=U cap W2=0`，所以两个 individual target defect 都为 1，target intersection defect 为 0。

但 `U cap (W1+W2)=U`，所以 synergy mass 为 1，joint defect 只有 1。

current observation 知道一个 cross-target combination，却不知道任何 individual target component。

## 4. Individual + overlap summary 仍不足

比较同一 W1,W2 下两个 systems：

- System A: `U=0`，individual/overlap defect masses 为 `(1,1,0)`，joint defect=2；
- System B: `U=<e1+e2>`，同样的 `(1,1,0)`，但 joint defect=1。

所以所有 individual target masses 加普通 overlap mass 仍不能决定 joint target precision；必须保留 targets 相对 current observation 的 embedding。

## 5. Validation

在 **6,000** 个 random small 2/3-power subgroup systems 上，two-target exact formula 全部成立，0 mismatch；其中 357 个 synergy 严格正。

## 6. Next frontier

三个以上 targets 不能默认使用 Boolean-lattice Möbius formula。下一步应寻找 grouping-independent canonical decomposition，避免 subgroup lattice 非 distributivity 带来的 parenthesization ambiguity。
