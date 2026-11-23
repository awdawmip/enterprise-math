# 本轮复算与接续

先读 `REPORT.md`。四个分支的完整证明、Python 标准库脚本及本次证书分别放在 `joint_prefix/`、`source_obstruction/`、`weighted_trees/`、`prefix_compute/`。

## 可复算范围

本包交付作者解析证明及有限有理／有向区间核验。一般源反例、结构恒等式和真实有限道路分别标注；无界匹配族的统一算术估计仍未证明。没有正式 Result 或独立 Review。

全部新脚本只依赖 Python 标准库。原运行使用 Python 3.12。复算会写回各脚本同目录的证书；点值脚本中的诊断时间正常变化。以下命令从本目录执行。

```bash
python3 joint_prefix/verify_cumulative_flux.py --source-root inputs
python3 source_obstruction/verify_obstruction.py
python3 weighted_trees/certify_weighted_energy_trees.py
python3 prefix_compute/certify_paired_prefix.py \
  --harmonic-module dependencies/certify_fast_harmonic_energy.py \
  --family prefix_compute/fixed_matched_family.json \
  --nodes prefix_compute/fixed_node_positions.json \
  --comparison-samples inputs/rh_partial_frontier_20261122/sparse_sample_observations.json
```

`--comparison-samples` 可省略；它只在新的点值生成完成后用于包含核对，不参与原道路上下包络的构造。累计场脚本省略 `--source-root` 时只运行一般有理结构核验。所有实际运行证书已包含在本轮文件中，无需为了阅读结论重跑。

## 已发布依赖

复算 ZIP 包含 `dependencies/` 与 `inputs/` 中的原字节副本。它们属于先前 Source，不是新研究结果。GitHub 本轮 Source 只保存新结果和 `DEPENDENCIES.json` 的不可变定位；在只下载本轮 Source 目录的场景，先按该清单取得需要的旧文件并核对 SHA-256，再运行上述命令。

- `dependencies/certify_fast_harmonic_energy.py` 是旧谐和六矩聚合代码，供新点值脚本导入；导入时不读取旧点值文件。
- `inputs/rh_partial_frontier_20261122/sparse_sample_observations.json` 是可选旧点值比较输入。
- `inputs/rh_tree_order_20261122/optimal_tree_order_certificate.json` 和 `inputs/rh_triangle_certificate_20261122/dyadic_triangle_certificate.json` 仅供累计场分支复核原44节点和38个三角包。
- `dependencies/` 的前置证明给出直接厚度余项、原最优树与旧深度障碍、旧谐和聚合定理。

`MANIFEST.json` 记录本轮 Source 文件哈希；交付包另有 `PACKAGE_MANIFEST.json`，同时记录新文件、复制的前置依赖及实际发布回执。分支文稿中的原绝对工作路径是本次实际运行定位；在其他位置复算时使用本页的相对命令。

## 下一条数学任务

令完整累计场 E_n=∑_{k≤n}(D_k−κ_k)、倒数测度 ν_n=1/[n(n+1)]。在不能自动控制的中粗层，对真实匹配参数统一证明

\[
\sum_{p\in\ell}\frac{h_p^4}{a_pb_p}
\frac{\nu[L_p,x_p)\nu[x_p,R_p)}{\nu[L_p,R_p)}
(\bar E_{L_p,x_p}-\bar E_{x_p,R_p})_+^2
\le C(A)^2X^2,
\quad C(A)=A^{o(1)}.
\]

同时保留真实骨架锚点，使用相位时支付返回原道路的代价。无符号方差与整个 E_- 的平方量可以作为更强的充分路线，不能当作这个定向分尺度目标的无损替代。
