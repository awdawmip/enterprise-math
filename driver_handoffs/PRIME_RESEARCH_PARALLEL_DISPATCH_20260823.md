# Prime Research Parallel Dispatch — 2026-08-23

Status: `DRIVER_DISPATCH_ENVELOPE`

Dispatch batch source for the five newly issued taskbooks:

`b6377a8dc0ed92959ca73fa372d48af226168079`

Driver branch:

`driver/prime-research-parallel-batch-20260823`

This envelope allocates runtime researcher identities outside the taskbooks, as required by the current taskbook contract. Each identity is deterministically derived from the task id, the displayed lane, and its unique batch dispatch token through `tools/research_identity.py allocate --dispatch-id` semantics. Each researcher reads only the named taskbook and its declared locked inputs.

## Lane 1 — Native prime filament sharp bound

Dispatch-ID: `PRIME-BATCH-20260823-L1`

Researcher-ID: `EM-PNFREP-E2FE4E`

领取：

`RS-PRIME-NATIVE-FILAMENT-SHARP-BOUND-INDEPENDENT-REPLICATION`

只读取并执行：

`research_tasks/PRIME_NATIVE_FILAMENT_SHARP_BOUND_INDEPENDENT_REPLICATION_20260823.md`

Taskbook source：

`b6377a8dc0ed92959ca73fa372d48af226168079`

Owner branch：

`research/prime-native-filament-sharp-bound-replication`

唯一硬目标：

`NATIVE_PRIME_FILAMENT_SHARP_BOUND_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED`

在独立报告冻结前，不读取 native maximal-flower / filament 源笔记、源脚本、源见证或自由研究分支。

## Lane 2 — High-dimensional prime-wall equivalence audit

Dispatch-ID: `PRIME-BATCH-20260823-L2`

Researcher-ID: `EM-HDPWA-03E870`

领取：

`RS-HIGHDIM-PRIME-WALL-FILTER-ALGEBRA-EQUIVALENCE-AUDIT`

只读取并执行：

`research_tasks/HIGHDIM_PRIME_WALL_FILTER_ALGEBRA_EQUIVALENCE_AUDIT_20260823.md`

Taskbook source：

`b6377a8dc0ed92959ca73fa372d48af226168079`

Owner branch：

`research/highdim-prime-wall-equivalence-audit`

唯一硬目标：

`HIGHDIM_PRIME_WALL_FILTER_ALGEBRA_CLASSICALLY_EQUIVALENT_OR_RESIDUALLY_NEW_CLASSIFIED`

先冻结独立证明 checkpoint，再开展 classical-equivalence / prior-art audit；不得把 Jacobi theta、平方和公式或 Sato-Tate 本身包装成新工具。

## Lane 3 — Third-sector factor-phase reconstruction

Dispatch-ID: `PRIME-BATCH-20260823-L3`

Researcher-ID: `EM-TSFPR-D14474`

领取：

`RS-THIRD-SECTOR-FACTOR-PHASE-INDEPENDENT-RECONSTRUCTION`

只读取并执行：

`research_tasks/THIRD_SECTOR_FACTOR_PHASE_INDEPENDENT_RECONSTRUCTION_20260823.md`

Taskbook source：

`b6377a8dc0ed92959ca73fa372d48af226168079`

Owner branch：

`research/third-sector-factor-phase-independent-reconstruction`

唯一硬目标：

`THIRD_SECTOR_FACTOR_PHASE_BRIDGE_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED`

在独立报告冻结前，不读取 GLOBAL_KNOWLEDGE 中第三扇区 factor-phase 源事件；必须自行推导 forward bijection、scale bridge、generator 与 reverse recovery。

## Lane 4 — Valley pure-state equivalence

Dispatch-ID: `PRIME-BATCH-20260823-L4`

Researcher-ID: `EM-VBSEQ-7021BF`

领取：

`RS-VALLEY-BAND-PURE-STATE-EQUIVALENCE-CLASSIFICATION`

只读取并执行：

`research_tasks/VALLEY_BAND_PURE_STATE_EQUIVALENCE_CLASSIFICATION_20260823.md`

Taskbook source：

`b6377a8dc0ed92959ca73fa372d48af226168079`

Owner branch：

`research/valley-band-pure-state-equivalence`

唯一硬目标：

`VALLEY_STATE_RECURRENCE_CFRAC_EQUIVALENCE_AND_BAND_ROOT_SEMANTICS_CLASSIFIED`

重点是 exact equivalence、exception map、relation semantics 与 prior art；禁止用位数推进或单例速度代替证明。

## Lane 5 — Valley benchmark and ablation

Dispatch-ID: `PRIME-BATCH-20260823-L5`

Researcher-ID: `EM-VBBMK-A550CC`

领取：

`RS-VALLEY-BAND-FACTORING-REPRODUCIBLE-BENCHMARK-ABLATION`

只读取并执行：

`research_tasks/VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_ABLATION_20260823.md`

Taskbook source：

`b6377a8dc0ed92959ca73fa372d48af226168079`

Owner branch：

`research/valley-band-factor-benchmark`

唯一硬目标：

`VALLEY_BAND_FACTORING_RELATION_YIELD_AND_COST_MODEL_REPRODUCIBLY_CLASSIFIED`

必须冻结 corpus 与 seeds，记录 rank 而不只是 relation count，并保留更慢、失败和 null 结果；禁止复制自由研究原型。

## Lane 6 — Existing Prime Fusion phase-extension verification

Dispatch-ID: `PRIME-BATCH-20260823-L6`

Researcher-ID: `EM-PFVEXT-B47C27`

领取：

`RS-PRIME-FUSION-PHASE-EXTENSION-TARGETED-INDEPENDENT-VERIFICATION`

只读取并执行：

`research_tasks/PRIME_FUSION_PHASE_EXTENSION_TARGETED_INDEPENDENT_VERIFICATION_20260823.md`

Taskbook source：

`94f6222675abb38acf8ccfe15c9bc6df83b1f9da`

Owner branch：

`research/prime-fusion-phase-extension-targeted-verification`

唯一硬目标：

`PRIME_FUSION_PHASE_EXTENSION_T3_T6_T10_T11_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`

该任务已经在主干活动队列中，本批不重复建书。只验证 T3/T6/T10/T11，不重跑已闭合的 Prime Fusion 算术核心。

## Driver intake order

The six lanes are logically independent and may run in parallel.

Driver review order after returns freeze:

1. native filament and third-sector blind returns first, because source comparison must preserve the strongest evidence firewall;
2. high-dimensional equivalence audit next, because it determines which results can enter a theorem package at all;
3. valley equivalence before interpreting valley benchmark claims;
4. Prime Fusion phase extension after its four theorem clusters are individually classified.

No second-wave successor taskbook is activated by this envelope. Extremal-classification, theorem-package integration, or algorithm-optimization successors require a new Driver gate based on the frozen returns.
