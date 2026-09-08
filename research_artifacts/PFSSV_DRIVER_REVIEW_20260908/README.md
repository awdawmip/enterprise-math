# PFSSV 独立实验设计审查：历史证据包

这是 `RS-PRIME-FACTOR-SEMIPRIME-SHELL-RESIDUAL-VALIDATION` 的辅助独立审查归档。原报告、原执行脚本和实际回执逐字节保留；只有本 README 是打包时新增。正式 Driver 结论及整改任务书由 owner 在其现有权限下另行绑定和持久化，可从 `driver_reviews/` 引用本包；本包自身不建立正式 Review、Result、claim、publication 或判词状态。

## 文件与不可变来源

| 文件 | SHA256 | 性质 |
| --- | --- | --- |
| [INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md) | `53db4b935131fe33f9b084ba4014fad29af2c141aab2cb400fee063a1d01ec6a` | 原独立报告；不修改历史措辞或同步 footer |
| [small_boundary_review.py](small_boundary_review.py) | `463a082b919283220892373f40d05a0f27bfe91ef2b8d3be13bc7c8998ff60f7` | 实际执行过的原脚本；保留硬编码路径 |
| [small_boundary_receipt.json](small_boundary_receipt.json) | `d4f1f3c976c4fd9ed391e673c890eea0d5c8b5bc9c2222889687adcbde005f66` | 原实际回执；不是本次打包重新执行生成 |

审查时工作树基线为 `154d649a419bf72fac1b2bf5cb6426a878ac9dbe`。恢复的七个文件逐字节来自 `1cac434cb9ac542a38a8e7bb6defa414fefb2e4d`；其逐路径 pins 与任务书 pin 已在原回执记录。传输不重新 freeze、不改原 Result/ER、claim、publication、时间或实验材料。

## 实际执行范围

原执行只用了已公开 discovery 尺度 X=100000 的宽度 1/100、1/1000。独立 trial-division 素数表上限为 50500，直接对乘核得 raw counts 237、25，与原函数和历史表一致。小核验确认观测支持选择、幸存行 rank 和 profiles 序列化缺口；回执的 PASS 表示这些审查边界核验通过，不表示原研究硬目标通过。

没有执行原 checker 的 `main()`、原 50.5-million sieve、注册 holdout 或完整全量统计；没有新 blind test、native certification、正式 Driver 接受。本次打包也没有重跑这些小核验。原脚本／回执的历史硬编码路径、时间和环境均不被发布动作改写。

## 复用前须显式选择根目录

原脚本没有 `--repo-root` 接口。它固定：

```text
ROOT = D:/em/integration-pfssv-resume-20260908
OUT = 原脚本所在目录
```

直接执行仓内归档脚本会使用该历史绝对根，并把新 `small_boundary_receipt.json` 写在脚本相邻位置。因此不能将仓内归档目录用作新执行输出目录，也不能仅追加一个未被实现的 `--repo-root` 参数。

需要复核时，先明确选择一个包含既定 source 对象和相同七个冻结源字节的独立 checkout，再把脚本复制到一个新的 TEMP 目录。在该 TEMP 副本中只把 ROOT 绑定到已选择的 checkout；保留 SOURCE、原 checker SHA 检查和原七文件不变检查。记录这个派生脚本的新 SHA、选定根及 commit/tree、依赖环境、真实命令和新回执，原归档三文件保持原样。若旧 source 对象或输入 bytes 缺失，应先解决精确来源，不能通过删 pin 检查来让脚本运行。

这是一份复用说明，没有新增或冒称已执行的 portable wrapper。对新根上的实际运行应明确记为“原有两个已公开 discovery 小例的非盲复核”；不把它当成原历史执行、重新 blind 的 holdout 或已完成的整改实验。

## 结论与权限边界

独审认为原“硬目标已完整完成／无剩余”需要修订，原实验可作为粗 null 失配的历史诊断保存。正式 Driver 记录应自行绑定当次有效 Result 字节与现有 review authority；本目录中的独审建议和程序回执不能替代那个授权步骤。

本包只收录既有研究的独立审查证据，未增加数学 API、工具族、Working Truth、Foundation 或研究任务。

Global-Knowledge-Sync: main@114964c / GLOBAL_KNOWLEDGE_V1
