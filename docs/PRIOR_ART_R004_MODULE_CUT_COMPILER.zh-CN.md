# 先行工作——R004 Module Cut Compiler

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

补充 19 把一类 finite p-power future-language compiler 精确化成 representable-matroid obstruction problem。所使用的 matroid 与 local-ring 数学都是成熟先行工作。

## 1. Matroid circuit 与 duality 是先行工作

Mathlib matroid library 直接把 circuit 定义为 minimal dependent set，并提供完整 circuit API [SRC-MATHLIB-MATROID-CIRCUIT]。

Mathlib duality module 通过 bases 的 complements 定义 dual matroid；`M` 的 bases 的 complements 正好是 `M*` 的 bases [SRC-MATHLIB-MATROID-DUAL]。

因此“minimal dependent column supports 是 circuits”和“column bases 的 complements 是 dual-matroid bases”都不是 Enterprise Math 新发明。

## 2. Local maximal ideal 上 reduction 是成熟 algebra

`Z/p^K Z` 是 maximal ideal `(p)` nilpotent 的 finite local ring。Nakayama/local-ring 技术标准地使用 maximal ideal quotient 恢复 generation/basis 信息 [SRC-STACKS-NAKAYAMA]。

补充 19 对 restricted free-module matrix map injectivity 使用更直接的有限证明：nonzero kernel vector 除去 coordinates 的 minimum p-adic valuation 后模 `p`；反向则把 mod-p kernel vector lift 后乘 `p^(K-1)`。

这一 local-ring reduction 不主张 novelty。

## 3. 当前 project-local bridge

R004 只主张以下 typed compiler specialization：

1. exact carrier `(Z/p^K Z)^d`；
2. current linear observation `Ax`；
3. coordinate-reset future generators；
4. primitive-column assumption，保证一次 reset 可恢复一个 retained coordinate；
5. retained quotient `(Ax,x|_S)`；
6. carrier cuts = `A mod p` column matroid 的 circuits；
7. minimal Carrier Bases = dual-matroid bases，大小精确为 `d-rank(A mod p)`。

这套 compiler bridge/certificate package 的历史 novelty 仍为 `NOVELTY_UNVERIFIED`。
