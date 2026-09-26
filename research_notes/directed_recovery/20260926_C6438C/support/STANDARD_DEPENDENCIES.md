# 标准数学依赖核对

本轮谱证明依赖单位根的标准最小多项式次数定理。2026-09-26核对mathlib当前一手文档：

- [Cyclotomic Roots](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Cyclotomic/Roots.html) 收录 `Polynomial.cyclotomic.irreducible_rat` 和 `Polynomial.cyclotomic_eq_minpoly_rat`，连接有理不可约性与原始单位根最小多项式。
- [Cyclotomic Basic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Cyclotomic/Basic.html) 收录 `Polynomial.natDegree_cyclotomic`，给出分圆多项式次数为Euler totient。

这些来源只核对标准代数依赖。本包的K33共同不变空间、分支无核推导、dyadic正质量界及实现绑定是本次作者推导，没有在Lean运行或获得形式化认证。连分数和good底数依赖沿用此前完整成功定理 `../completion/SUCCESS_AND_COMPLETION_THEOREM.md` 及其来源；本包没有运行新的理想参考。

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
