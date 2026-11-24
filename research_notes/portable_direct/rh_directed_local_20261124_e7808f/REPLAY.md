# 五个研究分支的复算入口

`replay.py` 支持单个分支、指定多个分支及全部分支。每次必须用 `--output` 指定独立输出目录。已有证书作为发布记录保留；本次生成的证书、标准输出、错误输出和 `replay_run.json` 写到指定目录。

## 环境

- Python 3；本轮入口检查使用 Python **3.12.14**。
- `crossing_tree`、`directed_arithmetic`、`matching_transfer`、`harmonic_windows` 只使用 Python 标准库。
- `matching_order` 还需要当前 Python 环境安装 `sympy`；本轮检查的版本为 **1.14.0**。它用 SymPy 隔离多项式实根，随后以有理端点符号和精确有理矩验证有限输入。

`--check` 仅检查参数、文件路径和依赖，不执行数学计算，也不创建输出目录。

## 目录与旧依赖

当前目录应含 `replay.py` 及五个分支目录。前一轮完整包默认位于：

```text
prior/riemann_cumulative_haar_20261123/
```

也可用 `--prior /完整路径/riemann_cumulative_haar_20261123` 指定。只有 `directed_arithmetic` 和 `matching_transfer` 需要旧包；其他单分支可以独立运行。旧包需保留原 `dependencies/`、`prefix_compute/`、`inputs/` 的相对结构。

## 命令

在本包根目录执行；输出路径可换成自己的临时目录。

```bash
# 检查全部入口，默认使用包内 prior/ 目录，不进行计算。
python3 replay.py --check --output /tmp/riemann-replay

# 最轻量的谐和窗口分支；不依赖前一轮包。
python3 replay.py --branch harmonic_windows --output /tmp/riemann-replay-harmonic

# 单独复算跨零浅树，使用已冻结的312组 fixed_inputs.json。
python3 replay.py --branch crossing_tree --output /tmp/riemann-replay-trees

# 指定多个分支和旧包路径。
python3 replay.py --branch directed_arithmetic matching_transfer \
  --prior /完整路径/riemann_cumulative_haar_20261123 \
  --output /tmp/riemann-replay-arithmetic

# 全部分支；--branch all 可以省略。
python3 replay.py --branch all \
  --prior /完整路径/riemann_cumulative_haar_20261123 \
  --output /tmp/riemann-replay-all
```

## 分支和产出

| 分支 | 实际入口 | 生成证书 | 旧包依赖 |
|---|---|---|---|
| `crossing_tree` | `verify_crossing_tree.py` | `crossing_tree_certificate.json` | 无；使用本分支固定输入 |
| `directed_arithmetic` | `certify_local_arithmetic.py` | `local_arithmetic_certificate.json` | 谐和区间模块、匹配族、原三角矩证书 |
| `matching_transfer` | `certify_matching_kernel.py` | `matching_kernel_certificate.json` | 谐和模块、旧点值算法、匹配族、节点及旧样本证书 |
| `matching_order` | `certify_matching_order.py` | `matching_order_certificate.json` | 无；需要 SymPy |
| `harmonic_windows` | `verify_harmonic_windows.py` | `harmonic_window_certificate.json` | 无 |

`crossing_tree`、`matching_order`、`harmonic_windows` 的原脚本没有输出路径参数，入口会把脚本及必要固定输入复制到对应输出子目录，再运行副本。其余两个脚本使用真实的 `--output` 参数。所有子进程均使用 `-B`，不在输入目录生成字节码缓存。

全部分支的计算由各自脚本承担；`replay.py` 不改写数学算法、输入和原证书，也不把入口检查视为完成数学复算。证书中的实测时间及绝对输入路径可以随执行环境变化；数学数据和检查覆盖以各脚本实际输出为准。

## 本轮入口验证

五个分支的参数、输入路径和依赖检查全部通过。为验证复制输出与执行链，本轮仅通过此入口实际运行 `harmonic_windows`：680 个包、7,380 个精确阈值区间全部通过，生成的证书与已发布数学证书内容一致，源证书字节保持不变。其他分支的数学结果沿用各自已完成的核验，此处没有重新运行。
