# 参与进取数论

感谢你帮助检验这个项目。

[英文版](CONTRIBUTING.md)

## 你不需要赞同整个理论

最有价值的贡献完全可能是证明某个候选规则错误。

可接受的贡献包括：

- 数学证明；
- 反例；
- 定义改进；
- 前人工作识别；
- 纯整数实现；
- 形式化证明；
- 物理反证方案；
- 文档与翻译。

## 从小问题开始

提出宏大新理论之前，请先阅读：

1. `docs/SPEC_v0.1.zh-CN.md`
2. `docs/THEOREMS.zh-CN.md`
3. `docs/COUNTEREXAMPLES.zh-CN.md`
4. `docs/OPEN_PROBLEMS.zh-CN.md`

尽可能选择一个已经编号的问题。

## 结论状态

每一个实质结论都应标记为以下一种：

- `DEFINITION`
- `PROVED`
- `CONJECTURE`
- `COUNTEREXAMPLE`
- `COMPUTATIONAL`
- `PHYSICAL-HYPOTHESIS`

不能把计算证据写成数学证明。

不能把数学类比写成物理证据。

## 双语规范文档

Issue 和讨论可以只使用英文或只使用中文。

规范性文字文件必须保持英文和中文语义对同步。贡献者不要求同时掌握两种语言：合并前可以由维护者补齐另一语言版本。

只修改一份规范语言文件、却没有同步另一份的 Pull Request 属于未完成状态。

## 代码规则

v0.1 参考核心只允许整数运算。

在 `src/enterprise_math/core.py` 中：

- 禁止浮点常量；
- 禁止真除法；
- 禁止偷偷调用浮点根函数；
- 行为必须服从文字规范。

运行：

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
python tools/check_bilingual_pairs.py
```

## Pull Request

一个 Pull Request 尽量只解决一个概念问题。

好的 Pull Request 应写清楚：

- 修改了哪个精确命题或定义；
- 它属于证明、反例、计算还是解释；
- 测试或证明证据；
- 相关的前人工作；
- 它对应哪个开放问题编号。

## 贡献信用

保留来源。

如果一个定理、反例、定义或实现思路来自某个 Issue 或 Pull Request，后续规范文档应在可行时保留该贡献来源。

项目不要求转让版权。被接受的贡献按仓库 MIT 许可证分发。

## 行为规范

可以对命题进行非常尖锐的批评，但应尊重参与研究的人。

详见 `CODE_OF_CONDUCT.zh-CN.md`。
