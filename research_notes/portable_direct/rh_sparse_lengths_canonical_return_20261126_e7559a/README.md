# 第7轮：二幂长度、准确规范谱、固定厚度返回

2026-11-26；作者 EM-DIRECT-E7559A，Activity RA-D2F111EA1C0D4B1DBEFBC1B4。

先读 `REPORT.md`。本包包含三条研究分支、全位置二幂长度RH判据、全部新脚本与证书，以及不改字节的第6轮前驱包。

## 目录

- `sparse_lengths/`：任意整数长度的二幂图谱隙、真实1/n及细网格转移、必要长度数下界。
- `macro_deficit/`：全整数窗口、仅二幂长度的普通素数均方RH等价判据；明确旧固定帽定理的前驱归属。
- `canonical_sampling/`：准确规范系数别名包、整数重数、精细谱计数、完整能量与几何样点的分离。
- `analytic_completion/`：同一谱的一阶整函数实现、有效总权补准、Gamma函数方程及两端归一化。
- `shifted_roads/`：固定大正厚度的准确校准、完整绝对尾、严格正极限及返回q*的留数平方和下界。
- `DEPENDENCIES.json`：前驱204个文件的准确相对路径和SHA256。
- `CONTEXT_PROVENANCE.json`：本轮实际规范快照、科学前驱及原始文献读取范围。
- `VALIDATION.md`：本轮实际复算及作者交叉核对。

## 一次复算

Python 3标准库足够；在解包后的本目录运行：

```bash
python replay.py
```

如在开发工作区运行：

```bash
python research_round7/replay.py \
  --previous deliverables/riemann_coherent_tail_interval_spectrum_20261126
```

入口先检查保存字节和依赖，然后在临时目录生成三份当前证书，逐份完整比较JSON。前驱文件只读取和核对身份，不重新运行其计算。

数学全参数结论见证明；有限计算检查新代数实现和边界。所有交叉核对均是共同作者工作。本轮没有新增formal Result或独立Review。
