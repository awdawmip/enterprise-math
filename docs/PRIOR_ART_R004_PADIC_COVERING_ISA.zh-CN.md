# 先行研究——R004 p-adic precision-native covering ISA

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

补充 36 不主张 finite chain ring linear codes、projective Hjelmslev geometry 或 modular-code covering radii 为新数学。

## 来源

### SRC-R004-CHAIN-RING-CODES-HONOLD-LANDJEV-2000

Honold 与 Landjev，*Linear Codes over Finite Chain Rings*，Electronic Journal of Combinatorics 7 (2000), R11。该工作从几何角度发展 finite chain ring 上的 linear codes，并建立 code 与 projective Hjelmslev geometry 的联系。

### SRC-R004-HJELMSLEV-ARCS-2024

Honold、Kiermaier、Landjev，*New Results on Arcs in Projective Hjelmslev Planes over Small Chain Rings*，arXiv:2409.02099。文中明确在 finite chain ring 上定义 projective Hjelmslev planes，把 points 视为 free rank-one submodules，并讨论其与 ring-linear codes 的联系。

### SRC-R004-MODULAR-COVERING-GUPTA-2012

Gupta、Durairajan，*On the Covering Radius of Some Modular Codes*，arXiv:1206.3038。该文研究 `Z_(2^s)` 上 modular codes 的 covering radius，但使用 homogeneous distance，因此这里只作为 broad ring-covering prior，不能用来替代本补充的 Hamming-specific derivation。

## R004 本地 under-test package

R004 只保留这些项目级内容：把 p-adic precision cap K 解释为 typed primitive-ISA alphabet；证明 `K+1 -> K` reduction 下的 storage 单调性；给出 one-step free projective-line storage 公式；给出 one-redundant full-support repetition null-line optimum；给出 `L_(2,1)(3,2)=4` 到 `L_(2,2)(3,2)=6` 的 precision phase change；并坚持同 cardinality 的 ring/field 属于不同 typed worlds，不能只看 state count。
