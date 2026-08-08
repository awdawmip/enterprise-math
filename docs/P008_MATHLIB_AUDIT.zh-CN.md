# P008 mathlib 审计框架

状态：研究中

## 目的

记录哪些结构属于已有 mathlib 数学，哪些属于进取数论特化，哪些可能成为未来 upstream 候选。

## 分类

每个结果分为：

- `MATHLIB_EXISTING`：mathlib 已有 API 或定理。
- `MATHLIB_DERIVED`：由 mathlib 已有结构直接推出。
- `ENTERPRISE_SPECIALIZATION`：成熟数学在进取数论定义上的应用。
- `UPSTREAM_CANDIDATE`：mathlib 尚缺失且具有一般复用价值的数学结果。

## 初步审计

| 内容 | 状态 | 说明 |
| --- | --- | --- |
| 自然数 nthRoot 刻画 | MATHLIB_EXISTING | 复用 Nat.nthRoot 及序关系定理。 |
| 平方根特例 | MATHLIB_EXISTING | 复用 Nat.sqrt API。 |
| Galois connection | MATHLIB_EXISTING | 使用已有序理论结构。 |
| 整数根作为精确状态语义 | ENTERPRISE_SPECIALIZATION | 属于进取数论解释层。 |
| 完全幂坍缩算子 | ENTERPRISE_SPECIALIZATION | 基于已有结构加入项目语义。 |
| 一般缺失序论引理 | UPSTREAM_CANDIDATE | 需要独立确认。 |

## 规则

进取数论不重复定义成熟 mathlib 结构。任何 upstream 贡献必须是独立可复用的普通数学，不能依赖物理解释层。
