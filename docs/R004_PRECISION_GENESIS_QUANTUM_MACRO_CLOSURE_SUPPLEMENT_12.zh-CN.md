# R004 精度宇宙生成 —— Supplement 12：kernel-only semantic reconstruction no-go

状态：`PROVED_WIP + EXECUTABLE_CHECKED + NEGATIVE_BOUNDARY + FOUNDATION_FEEDBACK_CANDIDATE`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_11.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

Representation Compiler 已经逐步把 future kernels 转换成 structured states：p-adic tries、product kernels、quotient modules、relation matrices、exponent profiles 与 integer determinant relations。

本补充记录这条路线的一条极限：裸 equivalence kernel 能确定 quotient **set**，但不能确定 future language 在该 quotient 上要求的 typed operations、relations 或 witness semantics。

所以 canonical compiler input 不能只有 `exact carrier + kernel`。Typed future language 必须继续作为 semantic input；kernel 只是 intermediate representation。

## 1. 最小 exact example：parity quotient

取 exact state：

`X=Z/4Z`

与 current observation：

`q(x)=x mod 2`。

Kernel partition 为：

`{{0,2},{1,3}}`。

现在考虑同一个 exact carrier 上的两个 binary operations。

### Addition

`x+y mod 4` 可以合法下降到 parity quotient，因为 sum 的 parity 只依赖 input parities。

在 `{0,1}` 上的 induced quotient table 是 XOR：

`0+0=0`、`0+1=1`、`1+0=1`、`1+1=0`。

### Multiplication

`x*y mod 4` 同样可以合法下降，因为 product 的 parity 也只依赖 input parities。

Induced quotient table 是 AND：

`0*0=0`、`0*1=0`、`1*0=0`、`1*1=1`。

两个情形的 quotient carrier 与 equality kernel 完全相同，但 descended operation semantics 不同。

因此一个只拿到 partition `{{0,2},{1,3}}` 的 compiler，不可能从 kernel 本身判断 required quotient operation 应该是 XOR、AND、两者都要，还是两者都不要。

## 2. R004-COMP-C01 —— kernel semantic underdetermination

Finite equivalence relation `E` 只能确定 quotient set `X/E`（忽略 class labels 的重命名）。

如果 additional structure 没有包含在输入 language 中，并被证明可下降，`E` 本身不能确定这些结构。

特别是，同一个 kernel 可以承载不同的：

- binary operation tables；
- order / metric structures；
- relation / witness semantics；
- action families 与 composition laws。

所以不存在一个 general kernel-only procedure，可以唯一重建 intended typed future semantics。

这是一条 semantic identifiability boundary；并不是说 quotient operation 无法计算。只要 exact operation / future language 被明确输入，下降后的 operation 当然可以计算。

## 3. 正确的 compiler interface

研究目标必须写成：

`Exact Carrier + Typed Future Language`

`-> Future Kernel IR`

`-> Structured Gates / Minimal Safe Carrier`

`-> Descended Typed Operations / Relations / Witness Semantics`。

Future kernel 很有用，因为它捕获 exact future equality 与 class minimality；但它只是一层 intermediate representation。

这进一步 sharpen P023 已有的 operation-family rule：safe equality 与 safe operation semantics 有关联，但不是同一 payload。Compiler 不能算完 kernel 后就把 declared operation family 丢掉。

## 4. 对 A3/A4 fallback 的直接后果

Supplement 11 证明部分 noncongruent kernels 仍可由 integer linear-lift relations 表示，而且 A3 weighted relation field 恰好是 rank-one determinant / exterior token。

但是即使一个 kernel 存在多个数学上合法的 coordinates，kernel 本身仍不能告诉 compiler：原 future task 真正要求哪一种 coordinate semantics。

因此进入 A3/A4 的转移必须由 typed requirements 驱动，例如：

- 保留 weighted relation field 与 closure law；
- composition 中保持 witness identity；
- 保留 MAY/MUST support；
- 保留声明的 common-target relation；
- 保留某个 specific action algebra。

Bare partition 不足以证明应该选择这些结构中的哪一个。

## 5. Architecture correction

此前的 slogan

`future kernel -> minimum representation`

只有在 “representation” 仅指 declared equality language 的 unlabeled quotient set 时才完整正确。

对真实项目目标，更强也更正确的 contract 是：

`typed future language -> minimum typed representation`。

Compiler 可以内部使用 kernel 最小化 equality classes；但 compression 以后仍然重要的每个 operation / observable / relation，都必须有显式 descent / factorization certificate。

这可以同时防止两类对称错误：

1. 保留未来任何 operation 都用不到的 exact detail；
2. 压缩成 equality partition 后，又默默发明从未证明合法的 quotient operations。

## 6. Executable witness

`precision_kernel_semantics_nogo.py` 记录 `Z/4Z -> parity` example。

它机械验证：

- addition modulo 4 可以下降到 parity；
- multiplication modulo 4 可以下降到 parity；
- 二者使用完全相同的 parity kernel；
- descended quotient tables 分别为 XOR 与 AND；
- 两个 tables 不相同。

这是 kernel-only semantic reconstruction 的最小 executable counterexample。

## 7. Revised compiler state machine

Supplements 06–12 后，compiler architecture 为：

### Semantic input

`Exact finite carrier + typed observations/actions/relations/witness requirements`。

### Equality IR

把声明的 deterministic / future outputs 编译成 future signature 与 kernel。

### Structured carrier gates

在有证明时依次尝试：

1. p-adic translation trie；
2. product factorization；
3. modular relation factorization；
4. additive quotient module / exponent profile；
5. integer linear-lift determinant relation；
6. A3 rank-one exterior specialization；
7. 只有实际需要时才进入 richer A3/A4 state。

### Semantic output

对每个 required operation / relation / witness structure，在 chosen safe carrier 上输出显式 descended implementation / certificate。

所以 compiler output 不只是 class identifier，而是一个 typed finite state machine：保留的 detail 与允许的 operations 都由 declared future language 证明合法。

## 8. Next frontier

目前剩余的 Foundation-level 问题可以无歧义地写成：

> **定义 minimum typed representation object 与 compiler interface：既保存 future equality，也保存 declared algebra / relation / witness operations，同时总是优先选择最弱可用 structured carrier，而不是 opaque partition。**

Equality 部分已经被 P023/FQ-004 与 R004 compiler specializations 大量覆盖。仍未闭合的是：functional、A3 relation、A4 witness/correspondence 三层之间，typed descended structure 应如何统一暴露，同时不把任意一种 coordinate system 升格成 universal primitive。

R004 应把这个 interface question 回交 Foundation/A3/A4，而不是再造一个竞争性的 mother layer。
