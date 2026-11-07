# R545｜实际精确执行证据与续接

2026-11-05（Asia/Shanghai）。冻结科学输入：R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f`；最近前沿 R544 `13f87f5f3d5a1da6ffc64f5210c204d32ab269b6`。运行方式：本地 Python 3 任意精度 Fraction 整数算术；独立验证使用 SymPy Matrix Berkowitz。除探索阶段为圆心寻找候选使用 SymPy nroots 外，证书的根隔离、根模长、相邻差分和行列式断言全部为精确有理或整数判断。

`python R545_VERIFY.py`：**R545_EXACT_RATIONAL_CERT_PASS**。主证书计算两个参数族、共 28 个圆盘及 183 对圆心，半径 1/1000，每个圆盘内恰有一个简单根。所有 Rouché 比率满足严格的有理不等式 `ratio<1/50`。完整覆盖全部 13 / 15 阶根。

```text
R545_K_CERT_PASS 7 degree 13 catalan 429 p2 2380
rational_disk_radius 1/1000 disk_count 13 disjoint_pairs 78 max_rouche_ratio_bound_lt_1/50
dominant_y_lower 126026431/25000000 other_y_upper 3417839/1000000
recurrence_exact_first_513_signchanges 144 first [6, 9, 12, 16, 19, 23, 26, 30, 34, 37, 41, 44, 48, 51, 55, 58]
signs_first_48 ++++++---+++----+++----+++----++++---++++---++++
R545_K_CERT_PASS 8 degree 15 catalan 1430 p2 3876
rational_disk_radius 1/1000 disk_count 15 disjoint_pairs 105 max_rouche_ratio_bound_lt_1/50
dominant_y_lower 324400649/50000000 other_y_upper 1911693/500000
recurrence_exact_first_513_signchanges 146 first [5, 9, 12, 16, 19, 23, 26, 30, 33, 37, 40, 44, 47, 51, 54, 58]
signs_first_48 +++++----+++----+++----+++----+++----+++----+++-
R545_EXACT_RATIONAL_CERT_PASS
```

`python R545_INDEPENDENT.py`：**R545_INDEPENDENT_PASS**。各族原始 H 系数与 Catalan 形式逐项一致；原始 Toeplitz 行列式来自 `det(method='berkowitz')`，独立于主证书的 Rouché 根计算。每族核对阶数 `m=1,2,3,4,5,6,8,9,12,16,20,24` 共 12 个；合计 30 项 H=B 系数和 24 个原始行列式，全等于对应递推。

```text
k 7 m 1 +; m 2 +; m 3 +; m 4 +; m 5 +; m 6 -; m 8 -; m 9 +; m 12 -; m 16 +; m 20 -; m 24 +
R545_RAW_BERKOWITZ_PASS 7 H_equals_ballot 14 raw_determinants 12
k 8 m 1 +; m 2 +; m 3 +; m 4 +; m 5 -; m 6 -; m 8 -; m 9 +; m 12 -; m 16 +; m 20 -; m 24 +
R545_RAW_BERKOWITZ_PASS 8 H_equals_ballot 16 raw_determinants 12
R545_INDEPENDENT_PASS
```

证明依据：完整 Rouché 根盘认证 + 简单最大模非实共轭对 + 余弦 Cesàro 一、二阶均值 + 次主导根指数上界。513 项检查不充当无限断言的证明。为复现提供 `R545_VERIFY.py`、`R545_INDEPENDENT.py` 和 `R545_PROOF.zh-CN.md`。源证书的外围语义与 X6 观测域按冻结输入保留。

研究角色/原生控制的当前状态需以本轮真实回执补充；GitHub 文件保存仅构成作者侧成果保全，正式 CLAIM、Result、Review 的权限须另行确认。下一题：`k≥9` 的根极点参数分类，尝试提供跨 k 的统一分离估计；备选为 `m=63` 全正整数 k 的符号分区。
