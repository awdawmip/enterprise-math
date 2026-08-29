<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-COPRIME-FIBER-BRIDGE-CLASSIFICATION",
  "title": "BRC 互素纤维桥分类：balanced coupling、单侧塌缩与可观测桥型",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "CBRC F3R2 already has an exact balanced-mixing survivor predicate expressed by determinant and gcd conditions, but it has not been interpreted as a bridge between multiplicatively separated coprime carrier sectors. Determine whether that structure really supplies a factor-blind bridge-existence mechanism or only a coefficient-support classifier.",
  "next_action": "Translate the accepted F3R2 carrier and survivor theorem into a multiplicative-support/CRT-channel language without changing its theorem strength. Define bridge-existence, one-sided collapse and endpoint notions separately; then prove which of them the current balanced-mixing structure can or cannot realize without factor labels.",
  "dependencies": ["driver_reviews/CBRC_F3R2_SURVIVOR_MEMBERSHIP_PREDICATE_DRIVER_REVIEW_20260823.md@main"],
  "source_refs": ["driver_reviews/CBRC_F3R2_SURVIVOR_MEMBERSHIP_PREDICATE_DRIVER_REVIEW_20260823.md@main"],
  "evidence_status": "DIRECT_USER_DIRECTION / INTEGRATION / CBRC_F3R2_EXACT_SURVIVOR_PREDICATE_ACCEPTED / MULTIPLICATIVE_BRIDGE_INTERPRETATION_OPEN",
  "hard_block": null,
  "tags": ["BRC", "CBRC", "balanced-mixing", "coprime-fiber", "gcd", "CRT", "survivor", "bridge", "one-sided-collapse", "rank-two"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-COPRIME-FIBER-BRIDGE-CLASSIFICATION",
  "parent_objective_id": "OBJ-MULTIPLICATIVE-BRIDGE-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "MBG-B0",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# BRC 互素纤维桥分类：balanced coupling、单侧塌缩与可观测桥型

Status: `READY / P1 / HIGH-LEVERAGE / BRC-INTEGRATION`

## Mother question

现有 CBRC F3R2 已把某类两槽 balanced mixing survivor 压缩到矩阵可逆性与两个 gcd 条件。这个结果能否被严格理解为

\[
\text{两个原本乘法分离的 carrier sectors}
\longrightarrow
\text{一个可观测 balanced bridge}
\]

并进一步产生“一个 hidden prime channel collapse、另一个不 collapse”的结构？必须区分 bridge existence、bridge observability 与 endpoint recovery，不能把 1 自动当 2，更不能把 2 自动当 3。

## Frozen inputs and scope

1. 现有 CBRC F3R2 theorem strength 只按已接受 Driver review 使用，不扩大为新的根公理。
2. 当前 survivor predicate 的 gcd 条件可以作为起点，但必须检查它们是在 operator coefficients 上、hidden factor support 上，还是只有类比。
3. 禁止把 \(|p-q|\)、\(|m-n|\)、Fermat offset、平方壳邻近或 factor-edit L1 当作 bridge quality。
4. 允许矩阵加法、balanced scalar、差分、同余等代数操作；禁止把这些操作解释成普通加法距离。
5. 对 \(N=pq\) 的 CRT 解释保持 factor-blind / factor-aware 两层分离：verifier 可用 \(p,q\) 解释 truth，proposed observable/operator 不得把它们作为输入。
6. 必须与经典 one-sided collapse 机制去重；若等价于已知 group-order/smoothness bridge，应降级。
7. 本任务不要求竞争性分解性能。

## Hard target and required outputs

**B0 Semantic translation.** 给出当前 CBRC carrier、operator、survivor 与 multiplicative carrier/fiber/bridge 的映射表，逐项标记 `EXACT / ANALOGY / NOT_JUSTIFIED`。

**B1 Bridge-existence theorem.** 尝试证明一个不含 factor labels 的命题：某类 balanced operator 满足可计算条件，当且仅当存在非平凡 support-splitting witness；若做不到，给出最小缺口。

**B2 One-sided collapse object.** 在 \(R=\mathbb Z/N\mathbb Z\) 或另一明确 carrier 上定义候选 \(C_\lambda(N)\)，目标事件为
\[
C_\lambda\equiv0\pmod p,\qquad C_\lambda\not\equiv0\pmod q
\]
或对称版本。必须说明它如何从 BRC 结构导出，不能直接把想要的 gcd witness 写进定义。

**B3 Symmetry obstruction.** 研究 p/q 标签交换对 balanced bridge 的限制。若所有 factor-blind BRC responses 在交换 hidden channels 下完全对称，证明何种额外 asymmetry primitive 是 endpoint recovery 的必要条件。

**B4 Rank-two classification.** 对最小 two-slot/rank-two family 分类：bridge exists；bridge observable but endpoint-free；one-sided collapse possible；impossible under current axioms。

**B5 Counterexamples.** 主动寻找“survivor 但无 multiplicative bridge”“有 coefficient gcd 但不对应 N factor channel”等反例。

Required outputs:

- `research_returns/BRC_COPRIME_FIBER_BRIDGE_CLASSIFICATION_RETURN_20260829.md`
- exact finite checker；
- `EXISTENCE -> OBSERVABILITY -> ENDPOINT` implication diagram，所有箭头分别证明或否定。

## Research value to preserve

现有 CBRC 已出现“用 gcd 决定 survivor membership、显式 witness 才需要分解”的裂缝。这可能正好对应 bridge existence 与 endpoint recovery 的区别。精确化它，可以判断 BRC 是真正的乘法桥理论，还是漂亮但 factor-aware 的 support classifier。

## Success, kill, and return criteria

**SUCCESS**：至少得到一个严格结果：BRC bridge-existence 定理、factor-blind observability 构造，或 p/q 对称性导致 endpoint recovery 不可能的 no-go。

**PARTIAL**：完成语义映射与反例分类，但 one-sided collapse 未构造。

**NEGATIVE_BOUNDARY**：证明当前 CBRC balanced-mixing 无法越过 bridge existence，endpoint 层需要新的非对称 primitive。

**KILL**：把 coefficient gcd 直接当 N 的因子；用 hidden \(p,q\) 选择 operator；把存在 witness 和可计算 witness 混为一谈；通过普通加法邻近重新引入旧路线。

Return 应明确下一步需要“新 bridge primitive”还是“endpoint recovery algorithm”。
