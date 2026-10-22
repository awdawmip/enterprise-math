# 本月成果库覆盖说明

全部当前物理文件及已知可达历史科学Source已按其实际证据层归账；真实来源缺口继续保留。

固定快照 `56f5938da3f707c1d9db1b39afde124eac4634e3`，基线 `ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec`；时间范围2026-10-01至2026-10-22。此表核对文献归属与Source保全，不新增证明、数学评审票、Tool注册或科学运行。

## 物理文件与分卷

当前分母为选定16个科学Source根目录中的2474个新增或修改文件：研究笔记1418、其他科学材料690、补充来源365、静态检查脚本1。它不是仓库全部文件数，也不等同本月所有历史版本数。2474条路径各出现一次，未归属为0。

12卷的文献整理单元数：

| 文献卷 | 文献整理单元 |
|---|---|
| [p11.json](p11.json) | 40 |
| [student_parity.json](student_parity.json) | 46 |
| [native_brc.json](native_brc.json) | 14 |
| [cm_algebra.json](cm_algebra.json) | 48 |
| [cm_analytic.json](cm_analytic.json) | 61 |
| [number_theory.json](number_theory.json) | 57 |
| [brc_residual.json](brc_residual.json) | 69 |
| [t6_formal.json](t6_formal.json) | 8 |
| [misc_formal.json](misc_formal.json) | 23 |
| [cell_euler.json](cell_euler.json) | 30 |
| [euler_measurement.json](euler_measurement.json) | 25 |
| [supplement_number_theory.json](supplement_number_theory.json) | 14 |

“单元”包含原定理、同族推论、条件接口、反例、来源比较与已注明证据等级的历史报告；不按文件数计论文，不表示新增独立发现或全部接受。既有23条库按原有状态复用。

## 逐路径清单

[汇总与缺口](global_month_coverage.json)；四个互不重叠分片都小于1MiB：

- [coverage_notes_1.json](coverage_notes_1.json)：709条，435484字节。
- [coverage_notes_2.json](coverage_notes_2.json)：709条，508172字节。
- [coverage_other_1.json](coverage_other_1.json)：528条，382103字节。
- [coverage_other_2.json](coverage_other_2.json)：528条，373083字节。

| 处置 | 路径数 |
|---|---|
| EXISTING_LIBRARY_REUSE | 145 |
| EXTRACTED | 852 |
| DUPLICATE | 802 |
| CONTROL_ONLY | 545 |
| RAW_SUPPORT_NOT_EXECUTED | 36 |
| DUPLICATE_CUSTODY | 64 |
| PREREQUISITE_REUSE | 2 |
| SOURCE_GAP | 28 |

每行保留精确路径、当前Git blob、处置、负责归档的owner、固定Source链接和全部有实际结论的分卷/entry关联。owner是归档职责，数学作者归属沿各卷原始Source。

## 合并、重复与混合归档

同一volume先取明确逐文件分类，再处理package继承；跨卷的EXTRACTED/REUSE/DUPLICATE优先于OTHER_OWNER/OUT_OF_RANGE。共享Source只计一个物理文件，保留所有实际采收条目。控制目录或owner文件名不能决定科学分类：头标93、实际95常规成员的CM/CRT混合包、175原稿、RSA与CM/cost混合包均沿实际成员采收，没有整体吞作control。

静态代码、原始输入、日志与实验计划只保全其实际角色，本轮没有执行。Taskbook的目标不是已证明成果；已有历史结果的摘要保留指向其实际primary文稿。Source发布、作者自检、普通有界whole审核、正式Task接受分别记录。

## 来源缺口与未解决问题

物理归账完整不等于所有原始证据已恢复，更不等于数学母问题已解决。28条当前物理SOURCE_GAP主要保留P11 prospective/stopped执行未产出arith Result的边界（文件本身存在），另有LP011未定位证据与CELL原包缺失。分母之外的NF peer精确404、CELL-U17/U18/U22原包、Gaussian/J1完整证书、adaptive checkpoint完整假设等仍按各卷明确列出。Eq16所需无索引κ未被canonicalδ arithmetic或任何translation参数替代。

已知历史隐藏残差Source已按 `BRC-R-200` 补录：固定历史REPORT、summary、三篇推导及两篇任务内交叉review共7份正文均实际读取。它们在当前2474分母之外；review代码hash与summary最终hash不一致等原始边界仍保留，未补跑、未新增数学票。

## 历史、删除和分支

284个已读Git tree缓存加固定当前root用于端点Merkle核查，16个范围内23个变化tree比较均无截断或缺tree，删除/重命名候选为0。此方法无法发现仅在月中创建后又删、两端都不存在的瞬态文件，故不宣称不可到达历史快照已穷尽。已知historical实验和open PR1525/1526另外归档，不冒充当前main，不纳入2474分母。

本轮仅做Source读取、归档与文献结构检查；数学探索保持暂停。
