# 变更类型

- [ ] 定义
- [ ] 证明
- [ ] 反例
- [ ] 计算
- [ ] 形式化
- [ ] 前人工作
- [ ] 物理假说
- [ ] 文档

## 精确变更

描述这个 Pull Request 修改的最小命题、定义或实现内容。

## 证据

根据情况提供证明、反例、测试输出或一手资料。

## 结论状态

说明变更前后的结论状态。

## 共享定理/工具面

对 canonical promotion，说明可复用 theorem、formalization、executable family、negative boundary 或 active interface alert 的 shared-surface delta。

- [ ] 若晋升结果/工具可被其他路线复用，已同步更新 `docs/RESEARCH_COMMON_SURFACE.*` 与 `research_common_surface.json`；若不需要更新，PR 已明确说明 shared-surface delta 为 `N/A` 的理由。
- [ ] `EnterpriseMath.lean` 的 root import 如有新增/删除，已在 human/machine shared surface 的精确 root-Lean indexes 中同步更新。
- [ ] `tools/*.py` 如有新增/删除，已在 human/machine shared surface 的精确 repository-tool indexes 中同步更新。

## 双语一致性

- [ ] 每个被修改的规范性文字文件，都在同一个 Pull Request 中同步修改了另一语言版本。
- [ ] 两个版本包含相同的实质结论。

## 验证

列出已经运行的命令或检查；当 shared surface、root Lean imports 或 repository tools 发生变化时，应包含 `python tools/check_research_common_surface.py`。
