# 第三批：Borsuk 量词反例与 T6 源恢复

本批新增 **一个经不同代理复核的科学服务单元**，另有 **一个文献源恢复单元**。与前两批合计八个科学服务单元加一个源恢复；这些不是九个新定理、正式任务接受数或101母题覆盖率。前两批已分别经 PR1768、PR1769 进入 main。

## Borsuk：同一跨输入并图不能回答逐输入最优合并

在旧 GEO8 的同一个六维 lens、同一 cap 与32符号扇区上，作者给出528个合法 unit-diameter 有限输入；每个输入的原子合并只需2块，但它们的 diameter graph 并图是 K33。加入同 lens 的7点正单纯形后，并图仍为 K33，逐输入最坏最优块数却精确变成7。两个族若要求一套共同原子着色，都需33色。

这区别 `chi(union G_K)=33` 与 `max_K chi(G_K)=2 or7`。保留输入身份、原子标记与该输入的直径边，才能回答后一问题。它不改善 b6 上界，不提供全体输入的32合并法，也不启动或解除 BLOCKED GEO9。

[冻结作者稿](../../../research_notes/balanced_resume_20261104/cm_formal/borsuk_next/BORSUK_INPUT_INDEXED_COARSENING_COUNTEREXAMPLE.md) · [接口](../../../research_notes/balanced_resume_20261104/cm_formal/borsuk_next/BORSUK_COARSENING_INTERFACE.json) · [独立全文复核](../../../research_notes/balanced_resume_20261104/inventory/review_borsuk/BORSUK_INDEPENDENT_REVIEW.md) · [精确绑定](../../../research_notes/balanced_resume_20261104/inventory/review_borsuk/REVIEW_BINDING.json)。作者 EM-C34-D16900；非参与构造的复核者 EM-REVIEW-53C747；结论 PASS，披露共享来源与非盲上下文，无正式数学投票。

## T6：精确 q14 计划已恢复，实际 residual caller 仍缺

恢复了已有 q14 (7,7) 最终计划，最终规格哈希为 `b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24`，并核对 q1–q4 的四条既有 RR/DR、return 和审稿哈希链。q14 原胶囊明确 roster cardinality、pair N、roster hash 为 null，执行文件与科学枚举为 false。旧 pre-q0 的每侧292仅是族上界，不能代替某个实际候选的 B+/B− 或 M0–M6。

下一输入须给出真实有符号 vertical t、q0 的16维 u、六个混合同余、M0–M6、实际两侧成本及非负 B+/B−。Oct28 的21个 coupled cuts已有，不能重算新发现。若精确输入尚未生成，下一窄单元应是已有 q14 计划的 roster/preflight 输入合同；旧预算和计划不是新的执行授权，也不要求额外发明权限门。

[源恢复报告](../../../research_notes/balanced_resume_20261104/nt/t6_recovery/T6_LATER_ORDER_RESIDUAL_SOURCE_RECOVERY.md) · [缺输入请求](../../../research_notes/balanced_resume_20261104/nt/t6_recovery/SUPPORT_REQUEST.json) · [来源绑定](../../../research_notes/balanced_resume_20261104/nt/t6_recovery/SOURCE_BINDING.json) · [独立文献审计](../../../research_notes/balanced_resume_20261104/inventory/review_t6_source/SOURCE_AUDIT.md)。审计核34个源文件、23个胶囊成员及4个最小摘本；这是 SOURCE_RECOVERY_NOT_NEW_SCIENCE_RESULT，不重新证明或接受旧四阶结果。完整胶囊已在 Source，本批不复制全部23成员。

## 公平续接

[续接清单](../../../research_notes/balanced_resume_20261104/FAIR_CONTINUATION_QUEUE.json)结合本轮实际服务与未服务冷线；它是非执行的研究建议，不是实时 owner/lease 或 canonical 调度记录。完整101母题和525结构叶仍由[原盘点](../../../research_notes/balanced_resume_20261104/inventory/all_declared_parent_groups.json)保留。先消费最高现有结果和精确输入，再决定每条线一个新的可手审单元；避免把同一母题的常数变体挤占其它线。

原创建状态保持字节不变，后续审核和 Source 保全单独记录。机器条目见 [THIRD_PASS_RESULTS.json](THIRD_PASS_RESULTS.json)。未修改正式 Task/Result/Review、P000、工具族或 Foundation。

EM-Source-Status: Read=Verified snapshot reused (39556bf5207aa5ba559a27ec591c1bc1bf43b457); Write=Documentary intake staged; actual publication receipts maintained separately.
