<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R009-SCALE-NATURAL-COLLAPSE-RESIDUE-CLASSIFICATION",
  "title": "R009 Scale-Natural Collapse Residue Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Classify all scale-natural deterministic lifts of a base map H, specialize to perfect-power collapse, and determine how naturality, downwardness, idempotence, fixed-point geometry, and information-erasure constraints restrict the residue system beyond the zero-residue lift discovered in R007.",
  "next_action": "Start from the forced form F_d(m)=d H(m//d)+rho_d(m) and the residue-coherence law floor(rho_e(m)/(e/d))=rho_d(m//(e/d)); prove the exact classification theorem for natural families, then specialize H=C_p and classify coherent residues under downwardness and idempotence before studying fixed points and information-erasure capacity.",
  "dependencies": [
    {"target": "R007 universal no-descent and natural-lift return", "action": "CONSUME", "satisfied": false},
    {"target": "P005 typed divisibility scale projection", "action": "CONSUME", "satisfied": true},
    {"target": "P009 typed collapse+coarsening", "action": "INFORM", "satisfied": true},
    {"target": "P023 future-compatible quotient/minimal repair", "action": "INFORM", "satisfied": true}
  ],
  "source_refs": [
    "research_tasks/R009_SCALE_NATURAL_COLLAPSE_RESIDUE_CLASSIFICATION_20260810.md",
    "research_tasks/R007_SCALE_COMPATIBLE_COLLAPSE_DESCENT_NOGO_20260810.md",
    "docs/P005_SCALE_LATTICE_CORE.zh-CN.md",
    "docs/P009_TYPED_SCALE_CORE.zh-CN.md",
    "docs/P023_COMPOSITION_SAFE_COLLAPSE.zh-CN.md"
  ],
  "evidence_status": "FOLLOWUP_TO_INDEPENDENT_R007_RETURN_NEEDS_REPRODUCTION",
  "last_progress_ref": "independent R007 return supplied by user",
  "last_progress_at": "2026-08-10T16:42:00+08:00",
  "hard_block": null,
  "tags": ["R009", "R007", "scale", "naturality", "collapse", "residue", "classification", "idempotence", "fixed-points", "A0"],
  "claim_lease_minutes": 1440,
  "context_policy": {
    "mode": "TASK_ISOLATED",
    "memory_policy": "UNTRUSTED_HINT_ONLY",
    "cross_task_import_policy": "EXPLICIT_ONLY"
  }
}
-->

# R009 — 尺度自然坍缩的 residue 系统分类

Status: `CANDIDATE RESEARCH HANDOFF / FOUNDATION-PRESSURE TEST / NOT CANONICAL`

## 0. 起点与纪律

R007 的独立回报给出了一个新的正向结构候选：在 P005 的尺度系统

\[
\pi_{e\to d}(m)=m//(e/d),\qquad d\mid e
\]

上，若一个自然族 `F_d : N -> N` 在尺度 `1` 满足 `F_1=H`，则自然性对 `d -> 1` 强迫

\[
F_d(m)//d = H(m//d).
\]

因此必有唯一余数

\[
\boxed{F_d(m)=d H(m//d)+\rho_d(m),\qquad 0\le\rho_d(m)<d.}
\]

对 `e=dr`，完整自然性候选等价于 residue coherence

\[
\boxed{\left\lfloor\frac{\rho_e(m)}r\right\rfloor=\rho_d(m//r).}
\]

R007 还给出零余数族

\[
F_d^H(m)=dH(m//d)
\]

作为 natural、pointwise minimal 的候选；当 `H=C_p` 时，它同时 downward、idempotent，并在尺度 `1` 恢复裸 `C_p`。

这些结论来自独立研究回报，当前任务必须重新证明后才能升级为本任务前提。不得因为模型 memory 记得 R007 就直接使用。

---

# 1. 第一母定理：全部自然族的 exact residue classification

优先严格证明：

### Candidate R009-T01 — Natural-family residue normal form

固定任意 `H:N->N`。所有满足 `F_1=H` 且对全部 `d|e` 有

\[
\pi_{e\to d}\circ F_e=F_d\circ\pi_{e\to d}
\]

的族 `(F_d)`，与所有满足

\[
0\le\rho_d(m)<d
\]

和

\[
\left\lfloor\frac{\rho_{dr}(m)}r\right\rfloor=\rho_d(m//r)
\]

的 residue 系统一一对应。

必须证明 necessity + sufficiency + uniqueness。

目标不是只给公式，而是把 natural dynamics 的自由度完全搬到 `rho` 上。

---

# 2. residue coherence 自身是什么结构

不要默认它只是 bookkeeping。研究：

- 是否可由 prime-power scale arrows 局部生成；
- 是否等价于某种 projective/inverse-system compatible section；
- 是否可由 base data on residue classes 重构；
- 给定有限尺度集合时，自由参数数目是多少；
- 在所有正整数尺度上，非零 coherent residue systems 是否存在丰富分类；
- 是否存在 canonical normal form。

必须主动寻找最小非零例子和不可扩张局部系统。

---

# 3. 专化 `H=C_p`：downwardness

令

\[
F_d(m)=dC_p(m//d)+\rho_d(m).
\]

分类何时

\[
F_d(m)\le m
\]

对全部 `d,m` 成立。

把 `m=dq+s` (`0<=s<d`) 代入，寻找 `rho_d(m)` 的 sharp upper bound；研究它与 `q-C_p(q)`、输入 residue `s` 的关系。

目标：给出 downward natural collapse family 的必要充分条件，而不是只证明零余数族可行。

---

# 4. 专化 `H=C_p`：idempotence

分类何时

\[
F_d(F_d(m))=F_d(m)
\]

对全部 `d,m` 成立。

必须把条件写成 residue functional equation，并研究 downwardness + idempotence 是否大幅压缩非零 residue freedom。

优先回答：

> 零余数族是否在某个自然、非人为的附加公理下唯一？

允许的候选附加公理包括但不限于：

- output divisible by scale `d`；
- no-new-residue；
- monotonicity；
- fixed-point minimality；
- maximal information erasure；
- compatibility with a declared basin semantics。

不要为了唯一性事后发明公理；每个附加条件必须说明数学/语义动机。

---

# 5. fixed-point geometry

对一般 coherent residue family，分类

\[
\operatorname{Fix}(F_d).
\]

零余数族给出的候选是

\[
\operatorname{Fix}(F_d^H)
=
\{d q:H(q)=q\}
\]

（在 `H=C_p` 时为 `{d k^p}`）。

研究非零 residue 会怎样改变：

- fixed-point set；
- basin partition；
- absorption order；
- scale-to-scale fixed-point transport。

目标是判断 scale-typed perfect-power semantics 是否有唯一合理 extension，还是存在真正不同的自然几何。

---

# 6. information-erasure capacity

自然 lift 不应只按代数性质比较。定义精确有限域 `0..N` 上的 fiber statistics，研究：

- kernel partition size；
- maximal/average fiber size；
- preserved input residue information；
- future-safe sufficiency；
- zero-residue family 是否在某个偏序中是 maximally erasing natural lift。

寻找 theorem，而不是仅做 entropy 类比。

如果需要定义 partial order：

\[
F\preceq G \iff \ker(F)\supseteq\ker(G)
\]

或由 observation quotient induced refinement 明确定义，并检查它是否与 pointwise minimality 是不同概念。

---

# 7. 与 R007 one-bit repair 的 bridge

R007 同时报告两种修复：

1. state repair：
   \[
   q_*=(q_r,q_rC_p);
   \]
2. law repair：
   \[
   C_p\leadsto \widetilde C_{p,d}=dC_p(m//d).
   \]

本任务要问：

> state refinement 与 scale-law modification 是否存在统一的 universal property？

研究是否可以把它们看成同一 commuting-square problem 的两种最小 completion：

- 固定 fine law，最小细化 quotient；
- 固定 quotient，最小修改 law。

如果能给出一般定理，这可能比 `C_p` specialization 更有 Foundation 回流价值。

---

# 8. 必须主动攻击

- residue coherence 是否其实是经典 inverse-system section 的直接重命名；
- downward + idempotent 是否仍有大量非零解；
- zero-residue 的“最小”是否仅是 pointwise order，和信息最小/最大完全不同；
- fixed points `{d k^p}` 是否只是一个方便选择而非 canonical necessity；
- law repair 是否改变了太多语义，以至不能再称为同一个 collapse；
- 是否存在无法同时满足 naturality、downwardness、idempotence、monotonicity、指定 fixed-point geometry 的 no-go。

任何一个负结果都可以成为主要成果。

---

# 9. 计算与 Lean

建立 exact integer explorer，有限尺度图优先覆盖：

- `p=2..6`；
- `d` 来自有限 divisor lattices；
- 小域 exhaustive enumeration of coherent residues；
- 自动检查 naturality/downwardness/idempotence/fixed points/kernel。

如果主定理稳定，优先 Lean：

1. natural-family residue normal form；
2. zero-residue natural lift；
3. `H=C_p` downward/idempotent specialization；
4. 若有 sharp classification，再形式化 residue constraints。

---

# 10. 第一阶段交付

至少包括：

- R007 相关 natural-lift 结论的独立复现；
- T01 exact iff classification；
- coherent residue system 的结构分析；
- `H=C_p` downward + idempotent constraints；
- 一个非零 coherent family 或其 no-go；
- fixed-point classification；
- information-erasure comparison；
- state-repair vs law-repair bridge theorem/counterexample；
- exact explorer + tests；
- prior-art boundary；
- Foundation Feedback 候选。

方向可以激进，证据必须残酷。
