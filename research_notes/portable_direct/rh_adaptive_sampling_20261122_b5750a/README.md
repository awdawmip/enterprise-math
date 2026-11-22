# 稀疏样本与自适应骨架：复算入口

主报告：[REPORT.md](REPORT.md)。批次起始 2026-11-22；整理完成 2026-11-23（香港时间）。

Researcher-ID: `EM-DIRECT-B5750A / TASK_RESEARCH`  
Research-Activity-ID: `RA-60C6D083A81B19084A74C5BA`  
Science freeze: `awdawmip/enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7`。

## 新增文件

- `rh_sparse_root_20261122/`：直接样本上包络、算术损失趋零、最终样本精度及谐和矩精确能量公式。
- `rh_partial_frontier_20261122/`：单侧信息类极值、单调查询、1,270 点输入与严格夹逼证书。
- `rh_arithmetic_next_20261122/`：算术细余项的筛法/Green 界、有限核对与组合证明核对。
- `rh_skeleton_local_20261122/`：真实骨架的局部边成本、最少新增节点及动态规划证书。
- `rh_sampling_lower_20261122/`：一般双侧源信息类的点查询下界和精确有理穷举。

## 复算方法

使用 Python 3 标准库，从解压目录运行。新的两个纯有理验证不需要任何旧算术缓存：

```bash
python3 rh_sampling_lower_20261122/verify_point_sample_lower_bound.py
python3 rh_sparse_root_20261122/verify_harmonic_energy_formula.py
```

稀疏证书默认使用随附 1,270 点表，不读取完整道路缓存：

```bash
python3 rh_partial_frontier_20261122/certify_sparse_curvature_envelope.py
```

真实骨架证书直接使用旧细节点证书及有理区间模块，不重新生成完整道路：

```bash
python3 rh_skeleton_local_20261122/certify_adaptive_skeleton.py
```

算术余项的有限复算使用完整旧道路缓存。附件不分发临时 pickle 缓存；先从可信的随附原生成代码重建，再执行新增核对：

```bash
python3 rh_joint_certificate/certify_joint_energy.py
python3 rh_arithmetic_next_20261122/certify_arithmetic_fine_bounds.py
```

原生成代码会在自己的目录内写出缓存与证书，新验证脚本会更新各自 JSON 结果。运行时间字段可能随机器变化。所有结论的数值比较使用 Fraction 或分母 `10^60` 的向外整数区间，不使用浮点作证明比较。

## 依赖与范围

Source 中本批保存新增研究文件及本入口；配套 ZIP 另收入实际所需、保持原内容的历史依赖。历史文件的归属和哈希记录于证书的 inputs/provenance，新增文件的逐文件哈希及远端保存回执在交付记录中。

复算中的实际算术窗口仍是 `[1024,32768]`。无界窗口的误差阶、信息类极值与查询下界由配套解析证明支持；有限计算核对它们的实现、实例及代数恒等式。独立 Project Review 尚未由本批取得。
