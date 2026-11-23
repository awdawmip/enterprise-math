# 复算输入与命令

本目录仅保存四份保持原字节的历史 JSON 输入。每份的来源仓库、提交、完整路径、字节数、SHA256 与原始交付回执位置见 [PROVENANCE.json](PROVENANCE.json)。本次打包核对了本地字节与历史回执；没有重新运行计算或重新作远端回读。

从本轮包的根目录运行，使用 Python 3 标准库即可：

```bash
python3 arithmetic/verify_mesh.py
python3 skeleton/verify_global_allocation.py
python3 shallow_tree/certify_shallow_trees.py --source-root inputs
python3 harmonic_evaluation/certify_fast_harmonic_energy.py --input inputs/rh_partial_frontier_20261122/sparse_sample_observations.json --old-certificate inputs/rh_partial_frontier_20261122/sparse_curvature_envelope_certificate.json
```

四个程序会更新各自目录中的 JSON 结果，历史输入保持不变。`shallow_tree` 读取两份旧细节点证书；`harmonic_evaluation` 读取 1,270 点样本及其旧夹逼证书。其余两个程序不读取历史数据。不需要完整道路缓存或第三方 Python 包。

若另外需要逐整数汇总交叉检查，可在最后一条命令末尾加 `--scan-check`；常规复算无需重复该选项。
