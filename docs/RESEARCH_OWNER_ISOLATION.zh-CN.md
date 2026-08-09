# Enterprise Math 研究 Owner 隔离合同

状态：`ACTIVE / CANONICAL GOVERNANCE CONTRACT`  
生效：2026-08-09  
范围：L1 core owner、L2 program owner、L3 bridge/probe 与 L4 integration replay。

Architecture v2 的真实多 agent 迁移暴露出一个反复出现的故障：把持续移动的整个 `main` 同步进研究 owner，会让无关数学变成该 owner PR 的 changed files，重新制造 semantic replay 本来要消除的分支缠结。

旧迁移说明若可被理解为“owner 必须持续吸收 main”，以本合同为准。

## 1. 核心不变量

> **Owner 负责研究；Integration 负责运输。**

L1/L2/L3 branch 拥有边界明确的数学前沿，允许落后于 `main`。

只有 L4 在 canonical promotion 时应从最新 `main` 建立。

因此：

- L1/L2/L3 owner **不得**仅为“保持最新”而 merge/rebase 整个 `main` 或复制整棵 main tree；
- owner 在研究确有需要时，可以显式消费某个具体 canonical theorem/module；
- 与该 owner 无关的 canonical 变化，不应成为 owner-local changed files；
- `main` 移动本身不构成重新构建已证明 owner result 的理由。

## 2. Owner generation

Owner branch 是一代有明确 semantic payload 的研究前沿，不是仓库滚动镜像。

健康的一代 owner 应能写成：

```text
owner: <A/P/E home>
base_seen: <main SHA or common-surface revision>
frontier: <有边界的数学问题>
owned_assets: <本 owner 新增/修改的 theorem/docs/code/tests/Lean/lineage>
hard_block: NONE | <explicit HARD_BLOCK>
```

main 在其它路线前进时，owner 可以继续研究。

若新 canonical result 与本 owner 有关，只语义消费那个 theorem；不要把与它同时进入 main 的所有无关文件一起同步过来。

## 3. Canonical promotion 流程

进入 main 是独立的 L4 动作。

对已经验证的 owner payload：

1. 冻结精确 source commit/blob/theorem statement；
2. 从**当时最新的 `main`**新建一条 L4 integration branch；
3. 只 replay owner-owned payload，以及必要的 canonical registration/provenance 更新；
4. integration PR 明确声明 `NO NEW MATHEMATICS`；
5. 在该 exact integration state 上运行适用的最终组合门禁；
6. 合入 `main`；
7. owner/source 历史原样保留作为 provenance；
8. 若研究继续，下一代 owner 从合适的新 canonical state 开始，或显式记录必要 owner dependency；不要通过周期性同步整个 main 来延长上一代 owner。

要求的是**最终状态兼容**，不是持续追逐每一个中间 main head。

## 4. Scope purity

每个 L1/L2/L3 owner 都有明确 theorem home。其 PR/change surface 原则上只应包含：

- owner 自己的数学；
- owner-specific tests/formalization/prose/provenance；
- owner 真正需要的最小显式 dependency change。

如果 branch 的 changed-file surface 仅因为同步另一个 branch 或 main，而出现其它 theorem home 的文件，就发生了 **scope drift**。

典型 scope drift：

- A3 relation-state PR 突然带入 P017 Legendre supplements；
- A4 correspondence PR 带入 A2 quotient formalization；
- A2 generic quotient PR 带入 P024/E001 material specialization；
- L4 lifecycle tooling PR 带入任何新数学 theorem family。

即使所有被带入的 theorem 都是正确的，scope drift 仍是治理故障。

## 5. Scope drift 的非破坏恢复

恢复时不得改写历史：

1. 所有既有 commit 保留为 provenance；
2. 确认真正的 owner-local asset set；
3. 用正确 canonical base + owner-local assets 构造当前 branch tree；
4. 新增一个 descendant commit 恢复 scope purity；
5. 不 force-delete，也不假装污染历史没有发生；
6. 从 current tree 移出的 off-owner asset，必须确认其真实 owner/source route 仍存在。

目标是数学归属清晰，不是 Git 历史美化。

## 6. Bridge

L3 bridge 同样受隔离规则约束。

Bridge 可以依赖两个 owner，但只应保留 weakest hypotheses 真正同时涉及两端结构的桥梁 theorem；不得同步任一端的整棵 owner tree。

若某 bridge result 已不依赖其中一端，应回收到相应 L1/L2 owner。

## 7. Integration branch

L4 比 owner 更严格：

- promotion 时从 latest `main` 创建；
- 必须声明 `NO NEW MATHEMATICS`；
- 只允许 replay/registration/conflict-resolution；
- 除非明确作为经过审计的 multi-owner release，否则不得临时聚合多个 owner payload；
- 通常 merge 后立即退出活动面。

L4 一旦积累 owner mathematics，就已经失效，必须在 merge 前恢复为 transport-only scope。

## 8. Scope-drift 审计

治理工具最终应独立报告两个维度：

1. **ancestry state**：ahead/behind、absorbed/replay-required、semantic override；
2. **scope state**：changed files 是否仍在声明的 owner/integration asset set 内。

`ahead/behind` 无法识别 scope drift。一个 branch 即使离 main 很近，也可能同时混入五个 theorem homes。

建议的 machine-readable owner metadata 示例：

```json
{
  "owner": "A3_STRUCTURED_RELATION_STATE",
  "allowed_assets": [
    "src/enterprise_math/weighted_relation_field.py",
    "src/enterprise_math/relation_lattice.py"
  ],
  "allowed_prefixes": [],
  "forbidden_owner_classes": ["P017", "A4", "P021"]
}
```

具体 schema 可以演化，但 semantic invariant 不变。

## 9. 与其它 canonical governance 的关系

本合同补充：

- `RESEARCH_ARCHITECTURE`：唯一数学 owner；
- `RESEARCH_BRANCH_LIFECYCLE`：L0–L5 生命周期；
- `RESEARCH_SCHEDULING_PROTOCOL`：研究并行、canonical promotion 必要时串行；
- `RESEARCH_COMMON_SURFACE`：共享知识，但不要求同步整仓。

四者合起来就是：

> **知识全局共享，研究归属局部隔离，只在 integration 边界做 canonical replay。**

## 10. 迁移证据

本规则来自 Architecture v2 的真实迁移压力测试：原本干净的 A2、A3、A4 以及 lifecycle-auditor integration，都曾因 whole-tree 同步而带入无关 P017/P024/material/core assets。把 current tree 恢复为 intended scope 没有删除任何数学 provenance，却显著缩小了各 PR 的 semantic surface。

这些是治理 provenance，不是数学 theorem。
