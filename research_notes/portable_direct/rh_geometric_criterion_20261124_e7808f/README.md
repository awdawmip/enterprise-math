# 固定几何正三角矩：2026-11-24 续研包

研究身份 `EM-DIRECT-E7808F / TASK_RESEARCH`；Activity `RA-0B92AAF774CA466C1C1BC38B`。

从 [REPORT.md](REPORT.md) 阅读本轮结论和范围；无界解析证明与有限程序分开保存。

## 本轮文件

| 目录或文件 | 内容 |
|---|---|
| `geometric_criterion/` | 固定 9:12:16 全整数参数族的单侧 RH 判据、精确增长指数、条件常数、普通素数与真实变化匹配族转移 |
| `one_sided_mellin/` | 自足 Landau 引理、完整参考道路的 Mellin 接口、平滑显式公式、单侧能量与骨架指数 |
| `geometric_green/` | 有限几何链的显式正核、最优一致常数、闭整数权及真实校准 |
| `geometric_compute/` | 原固定 11 厚度输入的 1,935 个几何包严格区间及后验包含证书 |
| `AUTHOR_CROSSCHECK.md` | 同轮作者交叉核对范围；各分支另有具体记录 |
| `replay.py`、`REPLAY.md` | 统一复算入口与实际接口说明 |
| `DEPENDENCIES.json` | 前轮完整依赖的版本、字节数与散列 |
| `MANIFEST.json` | 本轮 Source 文件的确定性散列清单，不递归包含自身 |

用户完整 ZIP 另包含 `prior/riemann_directed_local_20261124/`，其原字节及内部的 20261123 前置依赖保持不变。Source 提交按不可变版本引用这些已保存依赖，不重复上传前轮整个目录。`DELIVERY.md`、`DELIVERY_RECEIPT.json` 与 `PACKAGE_MANIFEST.json` 在实际保存之后写入交付包。

## 复算

从包根目录运行：

```bash
python3 replay.py --check --output /tmp/riemann-geometric-check
python3 replay.py --branch all --output /tmp/riemann-geometric-replay
```

如果前轮包放在其他位置，传入 `--prior /path/to/riemann_directed_local_20261124`。只有 `one_sided_mellin` 分支需要 SymPy，其余使用标准库及冻结区间模块。完整命令和输入布局见 `REPLAY.md`。

## 科学状态

在本稿规定的真实校准与全整数参数量词下，已经证明固定几何正三角矩的条件与 RH 等价，并识别了增长指数；没有证明该未知单侧上界成立。几何包合法性不等于原实际树的覆盖，完整道路回接还保留真实骨架和插值余项。1935 个包相互重叠，其最大值证书不是一个不交层的平方和预算。

全部核对为同轮作者工作。历史 `NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED` 状态不变；本轮没有登记新的 formal Result 或独立 Review。

科学基础：`9fc068244e4f1117f1e75df5eb0285c6697d21d7`；前轮 Source：`42e7aa4dbd01a6eb66e2f881c7cddcba72a3d775`；更早累计场 Source：`55804530fd8f7936834054bd99e8e1de492a545f`。
