# 第8轮研究包

日期：2026-11-28（Asia/Hong_Kong）。同一作者 `EM-DIRECT-E7559A / TASK_RESEARCH`。

先读 [REPORT.md](REPORT.md)。四份完整证明分别为：

- [定向锥与原 Green 转移](directed_dyadic/DIRECTED_DYADIC_GREEN_TRANSFER.md)
- [二幂窗口、二幂长度与真实整数桥](arithmetic_sampling/DYADIC_WINDOWS_AND_INTEGER_BRIDGES.md)
- [完整整数源、有限修复与解析刚性](arithmetic_rigidity/ORDINARY_INTEGER_SOURCE_RIGIDITY.md)
- [固定校准道路的双向返回能量](return_energy/LOGARITHMIC_RETURN_ENERGY.md)

每份证明都有对应脚本、固定输入和准确证书。Python 3.10+，仅标准库；无需外部零点表、ζ 服务或网络。交付包中的前驱树位于 `previous/riemann_sparse_lengths_canonical_return_20261126`，保持全部原字节。

从交付包根目录统一复算：

```bash
python replay.py --previous previous/riemann_sparse_lengths_canonical_return_20261126
```

开发目录默认入口：

```bash
python research_round8/replay.py
```

统一入口核对前驱文件 SHA256，在临时目录重生成四份当前证书并逐字节比较。它不会重新执行前驱计算。`DEPENDENCIES.json` 列出准确前驱，`MANIFEST.json` 列出当前科学文件；远程保存回执在交付包中另列。研究 Source 本身不复制整个历史树，按前驱固定提交引用。

实际验证范围见 [VALIDATION.md](VALIDATION.md) 及 [AUTHOR_CROSSCHECKS.md](AUTHOR_CROSSCHECKS.md)。本轮新增筛及普通素数统计不等于新增真实道路能量区间。无界定理由解析证明承担，作者检查不构成独立 Review；历史 formal Result 失败状态未改变。

尚开放：真实无界普通素数亏缺的统一次多项式上界，以及真实骨架锚点控制。二幂统计的 RH 等价判据说明了所需算术估计的强度，未证明其成立。
