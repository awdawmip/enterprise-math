# Enterprise Math / 进取数论共享研究面

状态：`ACTIVE / REQUIRED PREFLIGHT`  
生效：2026-08-09  
目的：让每一条研究路线在开始新的 theorem line 之前，都能看到同一份紧凑的可复用已证明数学、可执行工具、负向边界以及跨路线实时结果。

本文件是路由器，不替代正式证明。精确定理陈述仍以 canonical theorem/problem 文档为准；尚未进入 main 的 branch 结果则以带 source commit provenance 的 Research Relay 条目为准。

## 1. 所有 L1/L2/L3 研究路线的强制预检

开始新的 theorem line 前：

1. 阅读本共享研究面；
2. 阅读 `docs/RESEARCH_SCHEDULING_PROTOCOL.*`；
3. 阅读 `docs/PROBLEM_STATUS.*` 以及相关问题的 canonical result 文档；
4. 检索 Research Relay Issue #82 中最新且相关的条目；
5. 如果拟研究内容与已有工具/定理族重合，查看对应 executable specification/tests 或 Lean module；
6. 然后才判断下一步究竟是新母定理、特化、bridge、counterexample，还是重复结果。

不要求把整个仓库注入工作上下文。目标是“共享认知 + 选择性读取”。

## 2. 状态分类

通过共享面遇到的可复用结果必须明确属于以下一种：

- `CANONICAL_MAIN`：已证明并集成到 `main`；在声明 scope 内所有路线可直接消费；
- `LEAN_CHECKED_MAIN`：canonical result 且已由 root Lean build 覆盖；
- `PROVED_WIP_RELAY`：已在 research branch 证明并通过 Relay 传播，但尚未 canonical；可以作为显式 branch/WIP 输入使用，不得悄悄冒充 main truth；
- `EXECUTABLE_CHECKED`：有精确有限/参考实现验证支持，但不能替代证明；
- `COUNTEREXAMPLE / NEGATIVE_BOUNDARY`：可复用的不可能性或失败结果，传播优先级与正定理相同；
- `CONJECTURAL`：仅为研究目标。

## 3. Canonical 已证明定理知识通道

所有路线必须知道：canonical 已证明数学绝不只存在于 `docs/THEOREMS.*`。

### 基础 theorem catalogue

- `docs/THEOREMS.en.md` / `docs/THEOREMS.zh-CN.md`：最初 core 的紧凑 proved propositions；
- `docs/PROBLEM_STATUS.en.md` / `docs/PROBLEM_STATUS.zh-CN.md`：编号问题状态与 canonical result pointer 的权威账本；
- `PROBLEM_STATUS` 指向的 canonical `docs/Pxxx_*.{en,zh-CN}.md`：现代 theorem families 的精确陈述与 scope；
- `EnterpriseMath.lean` 及其导入的 `EnterpriseMath/**.lean`：Lean-checked 子集。

### 已证明但尚未 canonical 的实时通道

- Research Relay Issue #82：带 source branch/commit、最弱假设、relation class 与 requested action 的跨路线精确定理/反例。

任何路线都不得因为“自己的 branch 里没有”就推断某个结果“项目里未知”。

## 4. 全线路共享的可复用定理族

本节按 theorem-family 粒度列出；精确假设和编号必须回到相应 canonical 文档。

### A0 — primitive discrete state algebra

可复用工具/结果包括：

- integer roots 与 exact perfect-power collapse；
- basin characterization/cardinality 与 collapse-gap coordinates；
- root exponent composition 与 commutation；
- quotient/remainder 与 multiple-collapse 的不同语义；
- total scale-factor algebra、divisibility projection、gcd/lcm scale lattice、path independence 与 nonunique inverse refinement；
- signed-state distinctions；
- typed strict-rank descent；
- order-adjoint/right-adjoint 表述与 reductive idempotent collapse。

主要 canonical 入口：P001–P009 result docs 与 `docs/THEOREMS.*`。

### A1 — dynamics、kernels、collision、stabilization

可复用工具/结果包括：

- deterministic history merging：在相同后续 deterministic composition 下，已经合并的状态不会重新分裂；
- exact collision/fiber multiplicity observables 与 collision spectra；
- finite/eventual coalescence structures；
- well-founded order 上 monotone reductive stabilization；
- stable collapse-word behavior 与 lcm fixed-point structure。

主要 canonical 入口：P010、P011、P019、P020。

### A2 — observation 与 future-compatible quotient

可复用工具/结果包括：

- 所需 observable/operation 能通过 quotient 下沉，当且仅当其在 quotient fibers 上保持一致；
- 针对声明 future task 的 coarsest exact repair/refinement；
- finite predictive/future-signature refinement 与 stabilization；
- finite operation-family compatibility 与 operation-word semantics；
- arithmetic 特化中的 exact quotient/multiple-collapse compatibility 与 minimal boundary-bit repair；
- task-relative precision：脱离 future language 不存在一个普适 scalar precision。

主要 canonical 入口：P018 precision-state 结果、P023 及其 canonical supplements、P024 specializations。branch extension 通过 Relay #82 传播。

### A3 — structured relation-state algebra

共享 WIP/core 概念包括整数 weighted relation field

`Z_ij = m_j*c_i - m_i*c_j`，

partition coarsening `Z' = A Z A^T`、partition kernels、integer relation scale/rank、refinement memory 与 task-derived exact relation precision。

在 canonical replay 完成前，消费 A3 结果必须显式保留 `PROVED_WIP_RELAY`/branch provenance，不能把它们伪装成 main theorem。

### A4 — admissible support / correspondence algebra

共享 WIP/core 概念包括 finite multivalued relations、relation composition/converse、common-target structure、radius-indexed supports、split-completeness boundaries、MAY/MUST semantics、witness/group spectra，以及在 total-function graph 上退化回 P011。

同样必须区分 WIP 已证明结果与 canonical-main 结果。

### A5 — intrinsic discrete geometry

可复用 canonical/WIP 工具包括 primitive adjacency、graph distance、finite balls/shells、lattice/root-lattice candidates、radial/quadratic observations、distance carry 与 geometry-specific contraction。P012 给出 canonical metric foundation；更广的 P022 geometry 仍在 active research。

## 5. 所有路线都必须知道的高价值负向边界

- coarse equality/support/cardinality 不自动保留后续 composition；必须针对声明的 operation language 证明 future sufficiency；
- A3 signed relation information 在 quotient 时会 cancellation，因此 coarse support 不能证明 universal fine support；
- pairwise/common-target cardinality shadow 可能丢失 multi-step composition 所需的 witness identity；
- 单纯 geometry collision fact 可能不足以唯一选择 response，可能还需要 action/material/symmetry-breaking state；
- 对一个 observable 安全的 quotient，面对更丰富 future language 可能失效；
- 文件名相同、branch ancestry 或 `ahead(main)>0` 都不能证明存在新数学；semantic identity 才控制 replay；
- Galois connection、semigroup、numerical semigroup、partition refinement 等成熟一般工具，即使被 Enterprise Math 使用，仍属于 prior art。

## 6. 全线路共享的 executable 工具面

所有路线都可以复用 canonical executable assets；它们不归“最初发现它们的 branch”独占。

### Python exact/reference tools

根目录：`src/enterprise_math/`

重要工具族包括：

- `core.py`、`division.py`、`scale_algebra.py`、`signed.py`、`typed_scale.py`、`geometry.py` —— A0/A5 primitive tools；
- `composition_safe_collapse.py` 与 predictive/future-signature modules —— A2 quotient-safety tools；
- `action_language_precision.py`、clearance/guard/boundary precision modules —— P024/A2 specializations；
- P017 mirror/cofactor/Legendre modules —— square-basin pressure-test tools；
- relation/support modules —— 在其已 canonical，或被显式从 WIP owner 消费时可跨路线复用。

`src/enterprise_math/__init__.py` 只导出一个紧凑 stable subset；未 export 的 module 仍可能是合法 internal executable specification。把它当 canonical API 前必须先检查 theorem/provenance status。

### Lean tools

- `EnterpriseMath.lean` 是 root import surface；
- `EnterpriseMath/**.lean` 是 formalized subset；
- 只有 module 被 root build 导入，或被仓库 warnings-fatal formalization gate 显式覆盖时，才可以声称 “Lean-checked”。

### Tests 与 reconstruction tools

- `tests/`：exact regression/counterexample suites；
- `experiments/`：bounded pressure tests 与 engineering probes；
- `tools/check_bilingual_pairs.py`：中英文 pairing gate；
- `tools/check_references.py`：reference-integrity gate。

Executable checks 用于 proof discovery、falsification 与 regression，不能单独把 `EXECUTABLE_CHECKED` 升级为 `PROVED`。

## 7. 共享知识传播规则

任意路线证明或发现了可复用结果后：

1. 如果其他 active route 可能受益，立即 Relay；
2. 把 downstream action 标为 `INFORM`、`CONSUME`、`TEST` 或 `HARD_DEPENDENCY`；
3. 标明 mother-theorem owner 与 relation class；
4. 若结果进入 canonical `main`，必须保证未来路线能通过 `PROBLEM_STATUS`、canonical theorem/result doc、lineage/prior-art 与本共享面发现它；
5. 若形成可复用 executable method/tool，在下一次 common-surface update 中登记对应 canonical module/tool family；
6. 不等待所有 consumer ACK 才继续推进。

## 8. 非阻断规则

知识共享的目的，是提高并行度，而不是制造全局 barrier。

发现上游已有定理，就消费并继续；发现上游存在缺口，就隔离精确 missing lemma，然后继续其他可推进方向，除非确实可以按 `RESEARCH_SCHEDULING_PROTOCOL` 写出一个完整 `HARD_BLOCK`。