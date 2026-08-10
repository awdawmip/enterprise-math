# 先行研究——R004 Structural Target Cut Compiler

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

补充 20 不得被理解为把 Smith normal form、有限 p-group 结构、matroids over rings、valuated matroids 或 Nakayama/local-ring reduction 宣称为 Enterprise Math 新发明。

## 1. Smith normal form 与有限 module structure 属于先行数学

Mathlib 的 `Mathlib.LinearAlgebra.FreeModule.PID` 已形式化有限自由 PID module 的 submodule Smith normal form 与 diagonal inclusion 结构 [SRC-R004-STC-MATHLIB-SNF]。R004 这里只把经典整数 Smith form 作为 `mod p^K` 后 p-adic image cardinality 的 exact backend。

## 2. Local ring 上 residue-field generation 属于先行数学

Nakayama's lemma 给出经典 lifting principle：在相应假设下，有限 generation / surjectivity 可在 Jacobson radical quotient 上检测 [SRC-R004-STC-STACKS-NAKAYAMA]。这解释了补充 19 的 exact-state reset 问题为什么能降到 mod-p linear independence。补充 20 的重点恰恰是：一般 target quotient 即使 residue rank 不变，也仍可能携带额外 higher-p-adic information。

## 3. Matroids over rings / valuation rings 属于先行数学

Fink 与 Moci 引入 matroids over commutative rings，并说明 DVR 情形包含 valuated-matroid data；他们特别强调 module/group structure 能保留 ordinary matroid rank 或单一 multiplicity summary 丢失的信息 [SRC-R004-STC-FINK-MOCI-RING]。后续工作进一步研究 valuation-ring 上的 matroid 与 valuated-matroid/tropical structures [SRC-R004-STC-FINK-MOCI-VALUATION]。

因此 R004 不主张“ordinary residue matroid 之外还存在 p-adic/valuation-sensitive dependency data”这一一般现象为新发现。

## 4. 当前 project-local addition under test

补充 20 当前只保留以下更窄的 compiler package：

1. 把 retained coordinate-reset instructions 后指定 target quotient `Bx` 的 preservation 精确写成 `ker A_H subseteq ker B_H`；
2. 将其等价改写为 `Row(B_H) subseteq Row(A_H)`，并定义 missing-target module `D_H=(Row(A_H)+Row(B_H))/Row(A_H)`；
3. 把 `D_H` 作为 typed compiler defect object，其 p-group exponent profile 是 exact repair certificate；
4. 把 field specialization 识别为被 stacked `[A;B]` 坐标解除的 A-circuits，同时证明 relative-cut clutter 一般并不构成另一个 matroid；
5. 给出 mod-p rank 看不见的 higher-p-adic target obligation，证明补充 19 不能直接原样推广到 general structure preservation。

这套 Enterprise Math compiler bridge 与所选有限反例的历史 novelty 仍为 `NOVELTY_UNVERIFIED`。
