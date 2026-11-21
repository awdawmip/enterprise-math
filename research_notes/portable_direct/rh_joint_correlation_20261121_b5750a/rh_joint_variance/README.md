# 完整相位方差分支交付

本目录只含本轮新结果，旧成果未修改。

- `JOINT_VARIANCE_GROWTH.md`：作者证明。核心是对任意不同正 Lagrange 节点，`V_H` 与 `H³[Ψ(logH)+2log2−1]²` 具有绝对双边常数；核再与 `min(logH,Σ1/a_j)` 比较。匹配节点在 `256≤H≤Z` 上给出显式 `H³log²H` 下界；固定节点的最终增长则为 `H³`。
- `certify_joint_variance.py`：新严格高分母带证书，直接读取上一轮精确有理节点，使用已存在的 60 位整数定向区间算术与完整系数计算函数。
- `joint_variance_certificate.json`：实际执行输出，含 `H=256,512,1024` 的完整方差、高带贡献、严格比例、一般界符合性与源文件散列。

运行环境只需 Python 标准库，并保留相邻依赖：

```text
rh_correlation_rational/certify_matched_nodes.py
rh_correlation_rational/rational_window_certificate.json
rh_correlation_phase/verify_phase_homogenization.py
```

运行命令：

```bash
python rh_joint_variance/certify_joint_variance.py
```

当前证书通过。其 `H=256` 的总方差还与上一轮证书一致；新增信息是此前没有单独认证的高分母带贡献及更大的截断。这里不存在固定窗口能量下界或 `4/5` 普遍最优的主张。父分支负责远端持久化与控制状态处理。
