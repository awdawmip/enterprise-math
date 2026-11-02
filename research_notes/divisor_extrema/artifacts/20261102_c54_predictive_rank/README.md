# C54复算包

阅读 `RESEARCH_NOTE.md`；执行：

```bash
python run_checks.py
```

主程序只使用Python标准库及原样继承的BRC/因子词辅助源码。`results/exact_checks.json` 保存准确分子分母，`results/run_checks.log` 是本轮实际运行记录。运行覆盖有限完整概率与代数恒等式；一般证明见研究说明。`PUBLICATION.json` 区分项目/全局写入与原生登记。

本轮继承代码位于 `inherited/c53/`。源码用于实际复用，不将旧测试计入新结果。三状态概率模型和共同终端权是声明前提；未输入物理实验数据。
