# 有符号骨架、准确最优树与全厚度分类复算包

主报告：[REPORT.md](REPORT.md)。作者统筹 `EM-DIRECT-E7559A / TASK_RESEARCH`；Activity `RA-D2F111EA1C0D4B1DBEFBC1B4`。

## 内容

- `signed_green/`：实际符号合并、双矩远场压缩、原11锚点的闭能量证书，以及连续达到M的最小深度5树。
- `residual_strength/`：物理道路下凸包表示、形状费用、固定帽在全部整数尺度上的Mellin强度。
- `coherent_matching/`：全部正单厚度及全部真实端点网格的一致匹配分类。
- `fixed_family/`：原固定11有理厚度的密度符号、完整道路常数及显式最终负性阈值。

无界命题由完整解析证明承担。有限精确/区间证书用于实现和边界；浮点探索单独标记。所有交叉核对均为共同作者工作。

## 统一严格复算

Python3.12及标准库。在完整下载包解压目录运行：

```bash
python3 replay.py
```

若仅取Source新增目录，可指定完整前驱：

```bash
python3 replay.py --previous /path/to/riemann_native_residual_growth_20261124
```

入口核对文件与关键输入散列，运行四个严格验证器，将临时生成证书与保存结果作结构比较，不覆盖证书。既有前驱输入保留在 `prior/riemann_native_residual_growth_20261124/`，不重跑前驱研究。

单独的 `coherent_matching/explore_uniform_thickness.py` 使用mpmath及浮点源，输出36行探索。它不在严格入口中，不作为无界证明或严格区间证书。

原1,270点道路能量证书保持原样；新骨架表只针对原11锚点及其9个矩。固定11族的最终符号与随窗口变化的单厚度族分别列明，避免混用参数范围。
