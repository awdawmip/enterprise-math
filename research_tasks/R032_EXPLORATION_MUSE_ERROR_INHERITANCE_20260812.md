<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R032-EXPLORATION-MUSE-ERROR-INHERITANCE",
  "title": "R032 Exploration Muse, Productive Wrongness, and Post-Error Research Inheritance",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "RESEARCH_PRODUCTIVITY_FOUNDATION",
  "frontier": "Determine how Enterprise Math can preserve free exploratory research during a theory-explosion phase while making failed routes accumulate reusable value: reasoning tools remain dormant by default, may be pulled as inspiration when the researcher is stuck, and become structured inheritance only after a route has genuinely failed or been narrowed by evidence.",
  "next_action": "Build and adversarially test a pull-based Exploration Muse plus post-error Lesson Compiler; replay productive failures from R020/R022/R025/R027/R028; measure whether the system increases branch diversity and post-failure novelty without steering researchers toward historically preferred directions; freeze a minimal error-inheritance schema if the positive core survives.",
  "dependencies": [
    {
      "target": "R029 Draft PR #512",
      "action": "CONSUME_REASONING_TOOL_LIBRARY_AS_PASSIVE_SEARCHABLE_INSPIRATION_SOURCE_NOT_STARTUP_DIRECTIVE_SET",
      "satisfied": true
    },
    {
      "target": "R030 Draft PR #511",
      "action": "RETAIN_HISTORICAL_REPLAY_AS_NEGATIVE_CONTROL_FOR_PRESELECTION_AND_CONTEXT_OVERLOAD",
      "satisfied": true
    },
    {
      "target": "R020/R022/R025/R027/R028 productive negative results",
      "action": "MINE_HOW_FAILED_OR_NARROWED_ROUTES_GENERATED_NEW_DISTINCTIONS_TOOLS_AND_RESEARCH_BRANCHES",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R029 Draft PR #512 reasoning_tools.json and composition matrix",
    "R030 Draft PR #511 context-compiler backtest",
    "R020 Draft PR #501 dynamic-completeness negative boundaries",
    "R022 Draft PR #497 generic-search novelty negative / certificate calculus positive",
    "R025 Draft PR #504 H4/H6 kills and microphase replacements",
    "R027 Draft PR #507 quantitative-growth narrowing after exact Lean proof",
    "R028 Draft PR #509 intrinsic scalar/submodularity kills and typed credit-profile replacement",
    "User design correction: in theory-explosion phase, error should be experienced rather than preempted; the key is that lessons after error must stand on prior shoulders"
  ],
  "evidence_status": "EXPLORATORY_RESEARCH_MUSE_AND_ERROR_INHERITANCE_GATE",
  "last_progress_ref": "User rejected both startup preselection and adversarial early correction as premature convergence; Driver reframed the meta-tool program around pull-based inspiration and post-error inheritance",
  "last_progress_at": "2026-08-12T08:41:00+08:00",
  "hard_block": null,
  "tags": [
    "R032",
    "meta-research",
    "exploration",
    "productive-wrongness",
    "research-muse",
    "error-inheritance",
    "reasoning-tools",
    "theory-explosion",
    "novelty-preservation",
    "postmortem"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R032",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R032 — Exploration Muse, Productive Wrongness, and Post-Error Research Inheritance

Status: `READY / P0 / META-RESEARCH / THEORY-EXPLOSION / EXPLORATION-FIRST / NOT CANONICAL`

## 0. 任务前后完成度与推进向量

任务前估计：

- reasoning-tool library：`~70%`，R029 已证明可工具化，但尚未证明应如何进入自由研究；
- startup injection：`~0% accepted`，R030 的预选择方案不批准；
- delayed adversary：`design only / not accepted`，仍有过早收敛风险；
- productive-error inheritance：`~15%`，历史上反复发生，但尚未成为正式机制；
- inspiration-on-demand：`~10%`，尚无可检验协议。

目标推进向量：

`free-exploration +35% / post-error inheritance +55% / tool-library reuse +30% / premature convergence -60% / forced correction -70%`

本任务若成功，不要求减少错误数量。成功标准是：

> 错误仍然允许发生，但同类概念成本不必每次从零支付；失败路线能够留下比“不要再做这个”更丰富的研究遗产。

---

## 1. 母问题

当前进取数论仍处于理论爆发期。

在这个阶段，研究价值不能简单等同于：

- 更快找到正确 theorem；
- 更快杀掉错误 hypothesis；
- 更高历史 gold recall；
- 更少无效 branch；
- 更快向既有工具库的 taxonomy 收敛。

很多重要进展本身来自失败路线：

- 一个错误的 compression claim 可能逼出新的 carrier distinction；
- 一个错误的 covariance 可能暴露 microphase；
- 一个过强 growth law 可能逼出精确的 interval invariant；
- 一个失败的 scalar credit theory 可能留下更稳定的 vector profile；
- 一个 generic-algorithm novelty negative 可能留下 certificate calculus。

因此本任务研究的不是“怎样防错”，而是：

> 怎样让研究员拥有犯错、走偏、尝试陌生表示的自由，同时让每次成熟的失败都能沉淀成下一次探索的肩膀？

核心假说：

`FREE EXPLORATION -> SELF-RECOGNIZED STUCKNESS / MATURE FAILURE -> OPTIONAL INSPIRATION OR LESSON EXTRACTION -> NEW FREE EXPLORATION`

而不是：

`TASK -> SYSTEM PRESELECTS CORRECT DISTINCTIONS -> RESEARCH`

也不是：

`CLAIM -> SYSTEM ATTACKS UNTIL CONVERGENCE`。

---

## 2. 冻结设计原则：错不是异常路径

R032 必须把错误路线当作一级研究对象，而不是仅作为 failure code。

区分至少五种 outcome：

1. `FALSE_ROUTE`：核心 claim 被反例/证明杀掉；
2. `OVERSTRONG_ROUTE`：主方向有价值，但 statement 必须收窄；
3. `MIS-TYPED_ROUTE`：对象/carrier/observable 类型错位；
4. `PRIOR_ART_ABSORBED_ROUTE`：数学有效但 project novelty 被 rooted away；
5. `UNPRODUCTIVE_ROUTE`：目前未产生清晰 theorem/counterexample/tool/residue。

前四类都可能是高价值研究结果。

不得把“失败越少”设为目标函数。

---

## 3. Exploration-First Protocol

默认状态是：

`TOOLS_DORMANT`。

研究员启动时只能获得：

- task contract；
- accepted facts；
- frozen theorem/counterexample/status；
- source provenance；
- 明确的任务 exclusion。

不得默认注入：

- 推荐 reasoning tools；
- 推荐 problem decomposition；
- 推荐 ontology；
- 推荐 regime split；
- “你应该警惕 X”式历史诊断；
- 过去研究员最后采用的最佳路径。

研究员必须拥有提出陌生坐标、错误类比、错误 conjecture 和新 representation 的空间。

---

## 4. Muse 只能由研究员主动拉取

定义：

`EXPLORATION_MUSE` = researcher-invoked inspiration service。

合法触发只有：

1. 研究员明确声明 `STUCK / NEED_NEW_IDEAS / SEARCH_TOOL_LIBRARY`；
2. 研究员主动请求某类类比、工具、邻近理论或替代表达；
3. 研究员主动请求“给我一些完全不同的方向”。

禁止：

- 系统根据 taskbook 预测研究员可能卡住并提前提示；
- 系统根据历史 gold 自动选择“正确工具”；
- 系统因某个 claim 看起来错误就自动打断并纠正；
- 系统把一个工具排序为“最应该用”而没有研究员提供排序目标。

---

## 5. Muse 输出必须是发散式，不是收敛式

当研究员主动拉取 Muse 时，输出目标是增加 search branching，而不是指出正确路线。

至少支持四类返回：

### 5.1 Tool Shelf

从 reasoning/tool library 中返回多个异质工具，附：

- tool 的用途；
- 它通常会问什么问题；
- 可能产生什么新对象；
- 不承诺适合当前任务。

不得写成：

`推荐优先使用 A，因为历史上 A 是正确的`。

### 5.2 Analogy Shelf

提供来自不同数学/物理/CS/哲学领域的类比，但明确：

`ANALOGY_IS_GENERATOR_NOT_EVIDENCE`。

### 5.3 Mutation Shelf

对研究员自己的当前 model 提供方向扩散式 mutation，例如：

- 换 carrier；
- 换 observable；
- 换 horizon；
- 反转方向；
- 放宽/加强一个假设；
- 改成 stochastic / relational / weighted / signed 版本；
- 从小域 exhaustive 转大域 asymptotic，或反之。

这些 mutation 必须作为探索候选，不作为 correction。

### 5.4 Strange Tool

允许随机/低相似度返回少量“远邻工具”，测试 serendipity。

不得只做 semantic-nearest-neighbor retrieval，因为这会让研究不断在已有 taxonomy 邻域内打转。

---

## 6. Post-Error Lesson Compiler

只有当研究员自己接受一条路线已被：

- counterexample killed；
- theorem narrowed；
- evidence downgraded；
- prior-art absorbed；
- 或明确标为暂时 abandoned，

才允许启动：

`POST_ERROR_LESSON_COMPILER`。

它不是写“错误原因总结”，而要提炼研究遗产。

每个 lesson 至少包含：

```text
lesson_id
source_route
failure_class
original_question
original_claim_or_model
what_failed
minimal_witness_or_failure_evidence
what_survived
unexpected_structure_revealed
new_distinctions
new_objects_or_coordinates
new_tool_candidate
new_negative_boundary
new_questions_generated
analogous_prior_failures
how_prior_failures_helped
what_should_NOT_be_inferred
novelty_status
confidence/evidence_grade
```

特别要求：

`what_survived` 和 `new_questions_generated` 不得缺省。

因为目标不是建立“错误黑名单”，而是最大化失败后的新生长点。

---

## 7. Error Inheritance 不等于禁止重复错误

这是本任务最重要的边界之一。

历史 lesson 不应自动变成：

`DO_NOT_TRY_THIS`。

新的研究员仍然可以重新走一条已失败路径，只要：

- task semantics 不同；
- carrier 不同；
- horizon 不同；
- assumptions 不同；
- 或研究员认为失败边界本身值得再攻击。

所以 lesson 应表达：

`在条件 H 下，旧路线 C 曾这样失败，并留下结构 S`，

而不是：

`C 是错误方向`。

错误遗产提供肩膀，不提供围栏。

---

## 8. Shoulder Search

当一条路线失败后，允许自动执行一次：

`SHOULDER_SEARCH`。

输入不是原始 taskbook，而是本次**已经发生的失败结构**：

- failure class；
- minimal witness；
- broken implication；
- surviving invariant；
- newly exposed object。

然后检索历史 lesson library 中结构相似的失败。

这一步可以自动，因为方向已经由研究员自己的失败产生，而不是系统提前指定。

输出必须回答：

- 以前有没有类似失败？
- 前人从那个失败里提炼出了什么？
- 哪些结构可能迁移？
- 哪些条件不同，不能迁移？
- 前人的失败是否生成过后来成功的路线？

---

## 9. 重点历史回放：productive wrongness

R032 必须至少回放以下案例。

### R020

失败/边界：one-step cardinality/static statistic 不能自动作为 dynamic state。

检查该错误如何生成：

- carrier typing；
- composition-safety distinction；
- Boolean/count/provenance separation。

### R022

失败：没有找到新 generic search algorithm。

检查 negative novelty verdict 如何反而留下：

- certificate calculus；
- precision debt；
- distinction cover；
- adaptive acquisition；
- interface factorization。

### R025

失败：H4 p-power covariance 与 H6 p-power-free refinement kernel 被杀。

检查如何生成：

- scale microphase；
- refinement sensitivity；
- phase atlas 新问题。

### R027

失败/收窄：`strict subbinary every funnel layer` 不成立。

检查如何留下更精确的：

- interval/no-hole theorem；
- one-step card bound；
- exact witness of binary-sized funnel layer。

### R028

失败：unique intrinsic scalar credit、universal submodularity/supermodularity 被杀。

检查如何生成：

- typed credit/cost profile；
- ordered telescoping；
- declared-vs-realized credit；
- recoalescence bridge。

要求建立：

`FAILURE -> SURVIVING STRUCTURE -> NEW TOOL/QUESTION` lineage graph。

---

## 10. 关键实验：启发是否真的比纠偏更适合理论爆发期

至少比较四种模式：

1. `FREE_ONLY`：无 meta-tool；
2. `STARTUP_PRESELECT`：R030-style control；
3. `CLAIM_ADVERSARY`：R031-style control；
4. `MUSE_PLUS_ERROR_INHERITANCE`：R032 candidate。

评价不以“最早找到已知答案”为唯一目标。

至少测：

- hypothesis count；
- representation diversity；
- novel distinction yield；
- non-registry concept yield；
- productive failure ratio；
- lesson yield per failed route；
- new question yield；
- convergence speed（仅作为一个副指标）；
- premature abandonment rate；
- repeated conceptual cost after an analogous prior failure；
- researcher-requested tool usage rate；
- muse-induced branch diversity。

必须尝试设计 open-ended synthetic research worlds，其中 gold theorem 不唯一，甚至允许多个不同的有价值理论对象。

禁止只使用“历史最终答案能否被提前找回”作为评价。

---

## 11. Productive Failure Metric

提出并攻击至少一个候选指标，例如：

```text
productive_failure(route) =
  w1 * new_valid_distinctions
+ w2 * new_counterexamples
+ w3 * new_tool_candidates
+ w4 * new_questions
+ w5 * reusable_negative_boundaries
- w6 * unsupported_overclaims
```

但不得预设单一 scalar 是最终正确度量。

优先比较：

- vector profile；
- Pareto frontier；
- scalar summaries。

如果 scalar 强迫方向收敛，保留 vector/Pareto 而杀 scalar。

---

## 12. 理论爆发期 vs 理论收敛期

R032 必须研究阶段依赖。

候选 phase：

### THEORY_EXPLOSION

默认：

- 自由探索；
- Muse pull-based；
- 弱纠错；
- 高容忍错误；
- 强 post-error extraction。

### THEORY_CONSOLIDATION

可能允许更多：

- theorem checker；
- composition checker；
- prior negative boundary alerts；
- formal validation coverage checks。

### CANONICALIZATION

允许强 gate：

- proof checking；
- evidence grading；
- root coverage；
- prior-art/status correctness。

研究工具的介入强度应可能是 phase-relative，而不是全项目统一。

---

## 13. 必杀命题

优先寻找反例或边界，不得默认：

1. `fewer wrong hypotheses -> better research`；
2. `faster convergence -> better research`；
3. `historical error warning should always be surfaced before retry`；
4. `most semantically similar tool is the best inspiration`；
5. `post-error lesson should prescribe the next direction`；
6. `a failed route has zero value if no theorem survived`；
7. `one scalar can rank all productive failures`；
8. `the same meta-tool policy is optimal in explosion/consolidation/canonicalization phases`；
9. `repeating a historically failed idea is necessarily wasted work`；
10. `tool-library retrieval should optimize correctness rather than idea diversity`。

---

## 14. 推荐 executable artifacts

优先建立：

- `research_muse_registry.json`
- `research_error_lessons.json`
- `research_error_lesson_schema.json`
- `experiments/r032_exploration_muse.py`
- `experiments/r032_error_lesson_compiler.py`
- `experiments/r032_shoulder_search.py`
- `experiments/r032_productive_failure_backtest.py`
- `tests/test_r032_exploration_muse.py`
- `docs/R032_EXPLORATION_MUSE_REPORT.md`
- `R032_PRODUCTIVE_FAILURE_MATRIX.json`

不要修改 canonical theorem/common surface。

---

## 15. 与 R029 reasoning_tools 的关系

R029 registry 的定位改为：

`SEARCHABLE TOOL LIBRARY`，

不是：

`STARTUP CHECKLIST`，

也不是：

`AUTOMATIC ADVERSARY`。

每个 tool 应逐步增加：

- inspiration examples；
- generated question shapes；
- historical productive failures；
- neighboring tools；
- far-neighbor/serendipity links；
- phase suitability。

工具不仅要会说“哪里可能错”，还要会说：

> “如果你卡在这里，这个工具可能帮你长出一个新的问题。”

---

## 16. Meta-Tool Delta 改写

若 R032 正向，未来 `META_TOOL_DELTA` 不应只记录：

- new validator；
- new kill test；
- new negative boundary。

还应记录：

```text
new_inspiration_pattern
new_question_generator
new_productive_failure
new_serendipity_link
new_failure_to_tool_lineage
new_failure_to_question_lineage
```

目标从“让未来研究更少犯错”改为：

> “让未来研究员即使犯新的错，也不必重复支付旧错误已经支付过的全部概念成本。”

---

## 17. Prior-art rooting

必须系统比较但不得简单照搬：

- scientific discovery / exploratory search；
- divergent thinking / creativity support；
- case-based reasoning；
- failure-driven learning；
- explanation-based learning；
- CEGAR / counterexample-guided refinement；
- design rationale / postmortem knowledge；
- negative results publication；
- serendipity/recommender diversity；
- novelty search / quality-diversity；
- philosophy of scientific error and falsification。

重点判断 Enterprise Math 的 project-specific residue 是否是：

`future-relative exact mathematics + typed research lessons + pull-based inspiration + post-error structural inheritance`。

---

## 18. PASS / NARROW / KILL

### PASS

若 evidence 支持：

`EXPLORATION_MUSE_POSITIVE / PRODUCTIVE_ERROR_INHERITANCE_FOUND / PULL_BASED_TOOL_LIBRARY_SUPPORTED / POST_ERROR_SHOULDER_SEARCH_USEFUL / THEORY_EXPLOSION_POLICY_DISTINCT / NOT_CANONICAL`

### NARROW

若只有 post-error inheritance 稳定，而 Muse 效果不稳定：

`POST_ERROR_INHERITANCE_POSITIVE / MUSE_EFFECT_TASK_DEPENDENT / NO_STARTUP_PRESELECTION / NOT_CANONICAL`

### KILL

若 lesson library 也强烈造成历史路径锁定：

`ERROR_INHERITANCE_ANCHORING_FOUND / FREE_EXPLORATION_PREFERRED / TOOL_LIBRARY_PULL_ONLY_OR_MANUAL / NOT_CANONICAL`

---

## 19. 返回要求

必须返回：

1. researcher 原始探索与 meta-tool 暴露的时间顺序；
2. productive-failure lineage matrix；
3. Muse retrieval 策略和 diversity/serendipity evidence；
4. error lesson schema；
5. shoulder-search results；
6. explosion/consolidation/canonicalization phase comparison；
7. 被杀掉的收敛式 assumptions；
8. prior-art rooting；
9. 是否建议修改 R029/R030 infrastructure 的精确建议；
10. 若建议下一任务，必须是从 surviving evidence 自然长出的窄任务，不得预设统一 researcher policy。

本任务研究的是如何让错误产生复利，而不是如何消灭错误。
