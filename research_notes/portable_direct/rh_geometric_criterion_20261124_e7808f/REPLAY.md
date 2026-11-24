# 本轮四个分支的复算

`replay.py` 支持单个分支、指定多个分支和全部分支。用 `--output` 指定独立输出目录；已有数学脚本、固定输入和证书保持原样。

## 包结构与依赖

本包根目录包含 `replay.py`、`geometric_compute/`、`geometric_criterion/`、`one_sided_mellin/`、`geometric_green/`。

`--prior` 指向**前一轮完整20261124包**，默认：

```text
prior/riemann_directed_local_20261124/
```

前三个分支需要的20261123数值依赖位于该目录内部：

```text
prior/riemann_cumulative_haar_20261123/
```

因此默认完整路径为本包的 `prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123/`。`geometric_green` 不需要旧包。

使用 Python 3。只有 `one_sided_mellin` 需要 SymPy；其他分支仅需标准库。本轮入口验证使用 Python **3.12.14**、SymPy **1.14.0**。所有子进程均使用 `-B`，不在源目录写入字节码缓存。

## 命令

在本包根目录执行：

```bash
# 一次检查全部参数、依赖和输入路径，不计算、不写文件。
python3 replay.py --check --output /tmp/riemann-next-check

# 单分支。
python3 replay.py --branch geometric_green --output /tmp/riemann-green

# 轻量的Mellin有限代数与单元曲率核验。
python3 replay.py --branch one_sided_mellin \
  --prior /path/to/riemann_directed_local_20261124 \
  --output /tmp/riemann-mellin

# 选两个分支。
python3 replay.py --branch geometric_compute geometric_criterion \
  --prior /path/to/riemann_directed_local_20261124 \
  --output /tmp/riemann-geometric

# 全部；--branch all可以省略。
python3 replay.py --branch all \
  --prior /path/to/riemann_directed_local_20261124 \
  --output /tmp/riemann-next-all
```

输出位于指定目录的 `next/<分支名>/`；每个分支保存证书、`stdout.txt`、`stderr.txt`，顶层保存 `replay_run.json`。

| 分支 | 真实脚本入口 | 生成证书 |
|---|---|---|
| `geometric_compute` | `certify_geometric_tents.py` | `geometric_tent_certificate.json` |
| `geometric_criterion` | `certify_geometric_criterion.py` | `geometric_criterion_certificate.json` |
| `one_sided_mellin` | `verify_mellin_interface.py` | `mellin_interface_certificate.json` |
| `geometric_green` | `verify_geometric_green.py` | `geometric_green_certificate.json` |

其中三个脚本有真实的 `--output` 参数，入口直接传入输出路径。`one_sided_mellin` 的原脚本没有CLI，且依赖固定目录关系；入口会把它、同版 `PROOF.md` 和所需区间模块按原关系复制到输出目录，再运行副本。没有改写该数学脚本或用字符串替换其依赖。

`geometric_compute` 默认在所有新三角矩生成后，再对具备完整三个旧端点的包作后验包含检查。全部依赖来自已保存的前轮包，不下载零点表，不进行网络请求。

有限程序承担各自声明的代数、曲率、局部算术或Green核核验；它们不代替相应文稿的无界解析证明。证书中的绝对路径与实测时间可以随运行位置和环境变化。

## 本轮入口验证

已实际执行一次全部分支的 `--check`，输入路径、参数和依赖全部通过，且没有创建输出目录。随后只通过本入口端到端运行 `one_sided_mellin`：6项精确符号代数、518项向外区间曲率检查全部通过。复算数学字段与原证书一致，原证书字节保持不变。其他分支未在入口验证阶段重新计算。
