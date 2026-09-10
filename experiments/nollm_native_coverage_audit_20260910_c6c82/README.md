# Nollm 原生 Coverage / Recall 研究核验

研究记录，不是 Nollm 补丁或完整集成测试。默认几何采用当前固定源码中的 96 点采样核；不把它替换成理想 Hecke 格。

## 执行

Python 3.10+，核验程序仅使用标准库：

```sh
python experiment.py --output results
```

下载包已包含四份完整、原字节的 `source_snapshots/*.py`。从 EM 单独获取本目录时，按 `source_manifest.json` 从 `awdawmip/Nollm@91bd14ab394e87931b45baaaa87671f30fcfd706` 获取这四份文件，放在 source_snapshots 中；或令 `NOLLM_CORE_SOURCE` 指向已有本地固定版本的 `packages/nollm-core/src/nollm_core`。不要绕过 SHA 校验。

## 关键范围

`kernel_harness.py` 仅移除原文件的相对导入，提供地址、标记 atom、trace 和存储 fixture。核函数与 Recall 函数体按固定源代码执行；没有运行完整 NollmCore、持久化工作区或 OpenClaw Provider。

原生几何实验只开启 coverage_up/down。四节点资源测试是明确的合成图；hybrid 测试使用真实 Coverage 加两条显式测试 Bridge，并不代表向生产记忆添加了 Bridge。

`results/research_only_filter_order.diff` 只供审阅和核验。它修复本次发现的候选截断顺序，但单独不能修复剩余 bridge 预算被压缩丢失的问题。没有修改 Nollm 仓库。

全部数学解释、计数和边界见 `research_note.md` 或 EM 的同名研究笔记。结果中的坐标统一为 `[layer, q, r]`。
