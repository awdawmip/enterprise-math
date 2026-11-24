# 本轮研究包与复算

主报告：[REPORT.md](REPORT.md)。作者统筹 `EM-DIRECT-E7559A / TASK_RESEARCH`；Activity `RA-D2F111EA1C0D4B1DBEFBC1B4`。本包为作者证明、精确/区间证书及明确标注的探索，没有新增正式 Result 或独立 Review。

## 内容

- `matching/`：一个厚度的完整匹配族、正卷积误差、固定宽度 0.56 log B 阶族及验证。
- `deficit/`：单穿越池局部化、小漂移、原 38 包严格证书，以及 19 个宏观包的浮点探索。
- `anchors/`：保留真实边界的 Green 接续、参考道路归一化和作者交叉核对。
- `seams/`：原 11 个实际锚点和跨接缝矩的有理区间验证。
- `radius/`：原 1,270 个点的新半径及严格能量区间。
- `DEPENDENCIES.json`：不可变科学前驱及所需输入。
- `MANIFEST.json`：本轮科学文件的 SHA-256 与 Git blob SHA-1。

## 统一复算

使用 Python 3.12（仅标准库）。下载 ZIP 已包含 `prior/riemann_directed_local_20261124/`。解压后在本目录运行：

```bash
python replay.py
```

它先检查本包文件散列及前驱的关键输入，再运行六个严格验证器，将生成证书放到临时目录，与包内证书作结构比较。输入的绝对位置仅为运行环境元数据，比较时按路径后缀规范化；数值、区间端点、覆盖计数和证明参数必须一致。它不覆盖包内证书。

若使用 GitHub 上只含新增文件的 Source 目录，先准备不可变前驱包，再运行：

```bash
python replay.py --prior /path/to/riemann_directed_local_20261124
```

探索数据可另行复算：

```bash
python deficit/explore_macroscopic_pools.py --max-power 20 --output /tmp/macroscopic_exploration.json
```

该脚本使用双精度浮点；19 个包的探索不能作为原 38 包的区间证书或无界定理使用。不同浮点环境允许末位差异。主报告的全部严格数值来自精确有理数或 80 位向外区间。

## 对象范围

单厚度 `a_B=1/B` 与固定宽度 Chebyshev 族是新的无界参数族。1,270 点收紧继续使用原来的固定 11 厚度输入。无穷远线性归一化只对固定参考道路 q* 证明；实际匹配族通过窗口内完整道路误差转移，不假定固定厚度道路的无穷远行为。

前驱任意跨零浅树定理保留。本轮锚点与单调池结果扩大可用算术接口，没有证明真实无界素数输入上的统一次幂亏缺。
