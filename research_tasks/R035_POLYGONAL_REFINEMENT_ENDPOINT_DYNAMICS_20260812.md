<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R035-POLYGONAL-REFINEMENT-ENDPOINT-DYNAMICS",
  "title": "R035 Polygonal Refinement Endpoint Dynamics",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_EXPLORATION",
  "frontier": "Explore the exact integer dynamics obtained by repeatedly refining polygonal-number states by an integer factor and replacing each refined state by its neighboring polygonal endpoints, without predeclaring a phase taxonomy or preferred representation.",
  "next_action": "Build an exact integer laboratory for polygonal endpoint dynamics, independently discover useful coordinates/invariants/regimes or counterexamples, preserve the exploration trace, and return exact statements with clear evidence boundaries.",
  "dependencies": [],
  "source_refs": [
    "Classical polygonal numbers P_s(k)=((s-2)k^2-(s-4)k)/2",
    "Exact integer arithmetic and integer square-root inversion"
  ],
  "evidence_status": "FRESH_EXACT_INTEGER_EXPLORATION_GATE",
  "last_progress_ref": "Fresh paired research problem selected for independent project-context and isolated-context execution without embedding a preferred theorem decomposition",
  "last_progress_at": "2026-08-12T12:26:00+08:00",
  "hard_block": null,
  "tags": [
    "R035",
    "polygonal-numbers",
    "figurate-numbers",
    "integer-dynamics",
    "endpoint-support",
    "refinement",
    "fresh-exploration"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R035",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R035 — Polygonal Refinement Endpoint Dynamics

Status: `READY / P0 / FRESH EXACT-INTEGER EXPLORATION / NOT CANONICAL`

## 0. 任务前后完成度与推进向量

这是 fresh lane。任务开始前不假定存在任何已知相图、三分律、最小 carrier 或最佳坐标。

任务前估计：

- exact executable model：`~5%`；
- structural laws：`~0%`；
- counterexample/minimal-witness atlas：`~0%`；
- long-run support dynamics：`~0%`；
- prior-art rooting：`~0%`。

目标推进向量：

`exact model +70% / structural discovery +50% / counterexample atlas +50% / representation discovery +40% / unsupported generalization -60%`.

本任务不以“尽快得到一个漂亮定理”为成功标准。成功可以是：

- 一个新的 exact law；
- 一个被最小反例杀掉的强猜想；
- 一个更好的状态坐标；
- 一个反复出现的结构性边界；
- 一个把复杂支持压缩成可证明对象的表示；
- 一个明确的 prior-art absorption + project-specific residue。

---

## 1. 冻结对象

对整数 `s >= 3`、`k >= 0`，定义第 `k` 个 `s`-边形数：

\[
P_s(k)=\frac{(s-2)k^2-(s-4)k}{2}.
\]

所以：

\[
P_s(0)=0,\qquad P_s(1)=1.
\]

对任意 `n >= 0`，定义 lower polygonal index：

\[
L_s(n)=\max\{k\in\mathbb N: P_s(k)\le n\}.
\]

定义 endpoint-index support：

\[
E_s(n)=
\begin{cases}
\{m\}, & n=P_s(m),\\
\{m,m+1\}, & P_s(m)<n<P_s(m+1),
\end{cases}
\]

其中 `m=L_s(n)`。

允许使用 exact integer square root / discriminant arithmetic 实现 `L_s`；定理关键路径不得依赖浮点近似。

---

## 2. 动力学

固定整数 refinement factor：

\[
r\ge1.
\]

从一个有限 root-index support `S_t ⊂ N` 出发，定义：

\[
S_{t+1}=\bigcup_{k\in S_t} E_s\bigl(r P_s(k)\bigr).
\]

默认初值：

\[
S_0=\{k_0\}.
\]

集合语义意味着来自不同 parent 的相同 child 自动 recoalesce；不记录 multiplicity，除非研究过程中明确另开一个类型化 observable 并单独说明。

对应 actual polygonal-value support：

\[
A_t=\{P_s(k):k\in S_t\}.
\]

不要把 index support 与 actual-value support 字面混同。

---

## 3. 母问题

自由研究以下对象：

> 固定 `(s,r)` 时，上述 finite endpoint-support dynamics 随 `k_0` 与时间如何演化？存在什么 exact invariants、特殊参数、重复结构、增长律、支持几何、碰撞/recoalescence 机制、周期/冻结/漂移现象或更自然的状态坐标？

本任务故意不提供候选相图、候选三分律或候选 theorem family。

研究员可以自行选择：

- index 坐标；
- gap/phase/residual 坐标；
- graph/automaton 表示；
- generating function；
- modular/arithmetic 表示；
- symbolic interval；
- matrix/relation；
- 或完全不同的表示。

任何表示都必须说明它保留什么、丢失什么、对哪些 future/horizon 有效。

---

## 4. Exact executable surface

至少建立一个可复核 exact oracle，支持：

- `P_s(k)`；
- exact `L_s(n)`；
- exact `E_s(n)`；
- one-step support；
- multi-step support；
- parent→child incidence；
- support cardinality；
- duplicate/recoalescence count（作为研究统计即可，不自动升级成语义）；
- actual-value/index-support bridge。

建议的最低 sanity window，只作为起步而不是研究边界：

- `3 <= s <= 12`；
- `1 <= r <= 40`；
- `0 <= k_0 <= 200`；
- depth 至少 `10`。

最终主张必须在独立 holdout 区域复核；研究员可自行扩大或改变参数范围。

---

## 5. 自由探索纪律

### 5.1 先记录，再搜索

在首次主动检索项目历史、外部文献或工具库之前，保存一个 `INITIAL_EXPLORATION_CHECKPOINT`，只记录当时真实想到的：

- 至少两个候选表示/研究入口（若确实只想到一个，也如实写一个，不凑数）；
- 第一批 conjectures/questions；
- 最想攻击的边界；
- 当前最不确定的地方。

这个 checkpoint 是实验记录，不要求其中任何想法正确。

### 5.2 Exploration trace

维护 `EXPLORATION_TRACE.md`，按发生顺序记录：

- 新假设何时出现；
- 何时卡住；
- 何时主动搜索内部/外部资料或工具；
- 哪个搜索结果真正改变了方向；
- 哪条路线何时被自己判定为 false / narrowed / absorbed / abandoned；
- 失败后留下了什么 surviving structure；
- 新生成的问题。

禁止在最终返回时把 trace 追溯改写成“从一开始就知道正确方向”。

---

## 6. 研究输出

至少返回：

1. `docs/R035_POLYGONAL_REFINEMENT_DYNAMICS_REPORT.md`
   - 研究过程；
   - surviving exact laws；
   - killed/narrowed claims；
   - minimal witnesses；
   - representation choices；
   - unresolved questions；
   - prior-art rooting。

2. `experiments/r035_polygonal_dynamics.py`
   - exact executable core；
   - 不依赖 theorem-critical float。

3. `tests/test_r035_polygonal_dynamics.py`
   - focused regression + mutation tests。

4. `R035_MACHINE_SUMMARY.json`
   - 参数范围；
   - exact check counts；
   - result classes；
   - principal laws/counterexamples；
   - evidence grade。

5. `EXPLORATION_TRACE.md`
   - 真实顺序的探索轨迹。

6. 如发现 productive failure，再额外返回 `R035_ERROR_LESSONS.json`；没有则不要强行制造。

---

## 7. Evidence discipline

必须区分：

- exact theorem/proof；
- bounded exhaustive evidence；
- random stress evidence；
- heuristic pattern；
- analogy；
- prior-art rooted fact。

有限数据不能自动变成 universal theorem。

如果发现很漂亮但证据不足的规律，应明确返回 `THEOREM_CANDIDATE` 而不是硬推。

如果发现最强 conjecture 错了，但失败逼出新结构，这算正研究结果。

---

## 8. Prior-art rooting

不要以“是否早已有这个 exact task”为前提限制探索。

在初始独立探索 checkpoint 后，再做 prior-art rooting，至少检查：

- polygonal/figurate number arithmetic；
- polygonal-number inversion；
- integer dynamical systems；
- floor/quadratic recurrences；
- related automata/symbolic dynamics（若实际触及）；
- any exact theorem family that materially overlaps discovered results。

若某个方向已有经典结果，应说明：

`ROOTED COMPONENT / SURVIVING TASK-SPECIFIC RESIDUE`。

prior-art absorption 本身允许作为 productive failure。

---

## 9. Return classification

不要预设唯一 PASS token。根据真实结果选择类似：

- `POLYGONAL_ENDPOINT_DYNAMICS_STRUCTURE_FOUND / EXACT_LAWS_AND_BOUNDARIES_FROZEN / NOT_CANONICAL`
- `POLYGONAL_ENDPOINT_DYNAMICS_PARTIAL / STRONG_CONJECTURES_KILLED / PRODUCTIVE_FAILURES_FOUND / NOT_CANONICAL`
- `POLYGONAL_ENDPOINT_DYNAMICS_PRIOR_ART_ROOTED / TASK_SPECIFIC_RESIDUE_ISOLATED / NOT_CANONICAL`
- `POLYGONAL_ENDPOINT_DYNAMICS_NO_STABLE_GLOBAL_LAW / LOCAL_STRUCTURE_ONLY / NOT_CANONICAL`

也可以给出更准确的新分类。

---

## 10. 结束条件

当以下四件事都完成即可返回，不需要为了“更漂亮”无边界加数据：

1. exact oracle 可信；
2. 至少一轮 conjecture → attack → survive/kill/narrow 已发生；
3. 主要发现经过独立 holdout；
4. exploration trace 与 evidence boundary 完整。

保持 Draft research provenance；canonical integration 不是本任务内容。
