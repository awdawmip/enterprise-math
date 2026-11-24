# 固定几何三角族：复算说明

`PROOF.md` 给出完整解析推导，`fixed_input.json` 固定所有有限输入，`certify_geometric_criterion.py` 生成 `geometric_criterion_certificate.json`。`RESEARCH_NOTES.md` 保留研究接口；`CROSSCHECK.md` 记录本轮作者间核对的实际范围。

从包含 `replay.py`、`geometric_criterion/` 与 `prior/` 的本包根目录运行：

```bash
python3 replay.py --branch geometric_criterion --output /tmp/riemann-geometric-criterion
```

证书写入 `/tmp/riemann-geometric-criterion/next/geometric_criterion/geometric_criterion_certificate.json`。统一入口的 `--prior` 默认指向本包的 `prior/riemann_directed_local_20261124/`；若前轮完整包另存于其他位置，可显式传入该目录。完整参数说明见本包根目录的 `REPLAY.md`。

也可以直接执行分支脚本，但须显式指定其数值依赖目录：

```bash
python3 -B geometric_criterion/certify_geometric_criterion.py \
  --prior prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123 \
  --input geometric_criterion/fixed_input.json \
  --output /tmp/geometric_criterion_certificate.json
```

直接脚本的 `--prior` 指向包含 `dependencies/certify_fast_harmonic_energy.py` 的 **20261123 数值包**，与统一入口接收的 **20261124 完整包** 层级不同；外置依赖可替换为相应绝对路径。脚本只依赖 Python 标准库和该冻结的向外整数区间模块，以上命令将新证书写入指定临时目录。

本次固定结果：4,824 个源脉冲有理恒等式，24 个完整背景对数系数恒等式，69 个三角参数（1 至 64 以及 128、256、512、1024、2048）。最大局部右端为 32,768。69 个参考矩中 31 个严格为正、38 个严格为负，未出现含零区间。

每个参考矩都以两种入口核对：局部 `Λ` 帽和，以及稀疏三个端点的共同前缀。后一个入口仅为三角核核对而消去仿射 `γx`，证书没有把这个仿射等价代表冒充重新生成的完整道路。所有普通素数幂成本均在区间内保留；不读取或生成厚度 `D,c,q` 全缓存。

区间模块采用 80 位整数缩放、向外舍入和精确有理对数级数尾项。输入、脚本及依赖文件的 SHA-256 写入证书。程序不查询零点，也不把 RH 作为断言。

证书另外认证 RH 条件上界中的显式实常数。冻结的 `γ` 区间、各 100 项的 Machin 交错有理级数、对数区间与整数平方根，给出

\[
0.09755443072883494551767459919057286
\le C_{\rm geo}\le
0.09755443072883494551767459919057287.
\]

相应结论仍是 **RH ⇒** `|t_n|≤C_geo/√n+1/(1440n³)`；常数的计算本身不认证 RH。若将末项统一并入 `n^(-1/2)`，系数严格小于 `0.09824887517327938996211904363501731`。

这些是有限算法和恒等式检查。所有无界等价、增长指数及匹配族量词由 `PROOF.md` 的解析证明承担；有限结果不证明判据的上界成立。
