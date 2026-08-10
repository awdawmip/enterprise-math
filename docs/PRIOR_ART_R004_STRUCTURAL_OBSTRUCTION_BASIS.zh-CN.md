# 先行工作——R004 Structural Obstruction Basis 与 typed adequacy cuts

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

补充 16–17 把 typed future-language basis extraction 归约成 generator-side minimal cuts 与 hypergraph transversals。这里的 hypergraph / blocker / dualization 数学都是成熟先行工作。R004 只主张 compiler-specific reduction、canonical forbidden-world certificates，以及 carrier / semantic typed cut decomposition。

## 1. Hypergraph transversal / monotone dualization 是先行工作

Eiter、Gottlob、Makino 研究 monotone dualization 与 hypergraph transversals 生成，把 minimal transversals / minimal hitting sets 作为既有计算问题处理 [SRC-EITER-GOTTLOB-MAKINO-2002-DUALIZATION]。

Murakami、Uno 把 hypergraph dual 定义为 minimal hitting sets family，并研究 large-scale hypergraph dualization algorithms [SRC-MURAKAMI-UNO-2011-HYPERGRAPH-DUALIZATION]。

Mary 的后续工作同样把 minimal-transversal enumeration 与 transversal-hypergraph dualization 表述为长期开放/经典问题，并给出 bounded-VC-dimension 情形结果 [SRC-MARY-2024-MINIMAL-TRANSVERSALS]。

因此 R004 不把 minimal hitting sets、transversal hypergraphs、blocker duality 或一般 monotone Boolean dualization 宣称为新发明。

## 2. Clutter / antichain 是成熟组合数学

inclusion-minimal deletion cuts family 本身是 clutter（Sperner family）：任意一条 cut 都不包含另一条。标准 antichain theory 因而直接给 generator-side cardinality bounds。R004 只是在 future-safe compiler 产生 cut family 之后消费这些先行结果。

## 3. Minimal semigroup generating sets 仍属先行工作

补充 15 已经把 finite transformation-semigroup generation/rank 与 minimum generating-set problems 映射为 prior mathematics。补充 17 的 semantic reconstruction closure 在 unary operation term 情形继续复用该边界；semiring generation 也归对应成熟 algebraic setting。

## 4. 当前项目级 addition

R004 当前 WIP 新增严格限定为：

1. 对 typed future-safe compiler 定义 monotone carrier adequacy predicate `Phi(S)=[Compile_S(P0)=Q*]`；
2. 把改变 carrier 的 inclusion-minimal generator deletions 识别为 carrier-cut clutter；
3. 证明每个 minimal cut `H` 都有 compiler 自动生成的 canonical forbidden-world witness `P_H=Compile_(G\H)(P0)`，且 exact kill set 恰为 `H`；
4. 用 generator cut clutter 的 minimal transversals 替代 Bell-number forbidden-partition hitting；
5. 单独定义 quotient-level semantic reconstruction adequacy predicate；
6. 证明 typed joint-cut decomposition：`C_joint=Min(C_car union C_sem)`；
7. 把 `C_joint` 的 minimal transversals 解释为同时保持 world generation 与 requested descended semantics 的 adequate primitive instruction sets。

这套 Enterprise Math reduction 与 selected finite certificates 的历史 novelty 仍为 `NOVELTY_UNVERIFIED`。
