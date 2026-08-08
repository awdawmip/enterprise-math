# P008 mathlib 审计框架

状态：研究中

## 目的

本文记录哪些结构属于已有 mathlib 数学，哪些属于进取数论特化，哪些可能成为未来 upstream 候选。审计采取从严原则：如果发现某项 P008 结果已经存在于 mathlib，就主动缩小我们的创新边界，并把这种发现视为研究进展。

当前形式化审计固定到 mathlib 提交 `87adeaebd370a3b6a41ac4f044fddd4bf81803ad`，以及与其匹配的 Lean 工具链 `v4.33.0-rc2`。以后可以更新固定版本，但除非另行说明，下列判断均针对这一已检查快照。

## 分类

每个结果分为：

- `MATHLIB_EXISTING`：mathlib 已有 API 或定理。
- `MATHLIB_DERIVED`：由 mathlib 已有结构直接推出，但当前不视为需要单独 upstream 的定理。
- `ENTERPRISE_SPECIALIZATION`：成熟数学在进取数论定义或语义上的应用。
- `UPSTREAM_CANDIDATE`：当前审计尚未在 mathlib 找到等价定理、且可能具有一般复用价值的普通数学结果。只有编译与更广泛查重通过后，该状态才继续保留。

## 详细审计

| 内容 | 状态 | mathlib 证据 / 进取数论处理 |
| --- | --- | --- |
| 自然数整数 nth root | `MATHLIB_EXISTING` | 直接复用 `Nat.nthRoot`，Lean 层不另造平行根原语。 |
| 根的序伴随关系 | `MATHLIB_EXISTING` | `Nat.le_nthRoot_iff` 在 `p ≠ 0` 时给出 `a ≤ Nat.nthRoot p b ↔ a^p ≤ b`。 |
| 完全幂精确恢复 | `MATHLIB_EXISTING` | 复用 `Nat.nthRoot_pow`。 |
| 完全幂判定 | `MATHLIB_EXISTING` | 复用 `Nat.exists_pow_eq_iff'` 等定理。 |
| Galois connection | `MATHLIB_EXISTING` | 直接使用 `GaloisConnection`，不建立进取数论专用替代品。 |
| `l ∘ u` 的向下收缩性 | `MATHLIB_EXISTING` | `GaloisConnection.l_u_le`。 |
| `l ∘ u` 的单调性 | `MATHLIB_EXISTING` | `GaloisConnection.monotone_l_comp_u`。 |
| 诱导投影的幂等性 | `MATHLIB_EXISTING` | `GaloisConnection.l_u_l_eq_l` 已直接提供核心等式。 |
| 不动点与下伴随像集的关系 | `MATHLIB_EXISTING` | `GaloisConnection.exists_eq_l` 已给出像集/不动点刻画。 |
| 伴随的复合 | `MATHLIB_EXISTING` | `GaloisConnection.compose` 已给出右伴随反序复合。 |
| 交换方块跨伴随传递 | `MATHLIB_EXISTING` | `GaloisConnection.u_comm_of_l_comm` 与 `l_comm_iff_u_comm` 已存在；P008 尺度论证背后的通用母定理由此被 mathlib 吸收。 |
| 自然数乘法 / 向下除法伴随 | `MATHLIB_EXISTING` | 正乘数情况下已有 `Nat.galoisConnection_mul_div`。 |
| 整数根作为进取数论内部完整精确状态运算 | `ENTERPRISE_SPECIALIZATION` | 属于进取数论基础解释，不属于 mathlib。 |
| 把 `C_p(n) = Nat.nthRoot p n ^ p` 称为完全幂坍缩 | `ENTERPRISE_SPECIALIZATION` | 该算子是成熟伴随投影规律在项目中的特化和重新解释。 |
| 正指数下 `Nat.nthRoot (p*q) n = Nat.nthRoot p (Nat.nthRoot q n)` | `UPSTREAM_CANDIDATE` | 对固定 mathlib 快照的精确名称与源码检索尚未发现等价定理；已写出基于现有伴随 API 的 Lean 证明，必须先通过真实编译再讨论 upstream。 |
| 正整数根迭代顺序交换 | `UPSTREAM_CANDIDATE` | 预计由前一复合规律和乘法交换律推出；在同一审计门槛下保持暂定。 |
| 进取数论尺度相容 | `ENTERPRISE_SPECIALIZATION` | 计划直接形式化为现有 `u_comm_of_l_comm` 加上幂映射/乘法映射交换方块的特例。 |

## 对原 P008 “母定理”计划的修正

原计划提出四个通用母定理。源码审计已经表明，其一般序论内容均已存在于 mathlib：

1. 伴随诱导向下收缩、幂等坍缩——已有；
2. 不动点等于下伴随像集——已有；
3. 右伴随按反序复合——已有；
4. 左伴随交换方块诱导右伴随交换方块——已有。

因此，P008 **不得**把这些结果换名后作为 upstream 新定理。Lean 层可以为了项目可读性保留薄包装，但文档必须明确数学内容继承自 mathlib。

## Lean 架构规则

形式化层按下列顺序组织：

```text
mathlib
  ↓
EnterpriseMath.Order.Adjoint      -- 面向项目的薄包装
  ↓
EnterpriseMath.Arithmetic.IntegerRoot
  ↓
尺度 / 坍缩复合等特化
  ↓
进取数论解释与物理假说（文档层，不作为 mathlib 数学主张）
```

项目固定 mathlib 提交和匹配的 Lean 工具链，以保证形式化证据可复现。`Nat.nthRoot` 是实际 Lean 原语；`R_p` 继续作为进取数论数学记号。

## Upstream 门槛

一个结果只有同时满足以下条件，才能继续保留 `UPSTREAM_CANDIDATE`：

1. 在固定 mathlib 版本上无 `sorry` 编译通过；
2. 精确名称检索、语义/API 检索和源码检索均未找到等价定理；
3. 陈述是脱离进取数论本体解释仍可复用的普通数学；
4. 假设与定理方向符合 mathlib API 习惯；
5. 具有足够复用价值，值得增加 upstream API。

一次初步检索没有找到同名定理，绝不构成创新或历史优先权证明。
