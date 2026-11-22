# 真实骨架与逐包最小值障碍

本目录属于 2026-11-22 的 RH 方法转译继续研究，保留原研究身份与 Activity。

- `SIGNED_SKELETON_ENERGY.md`：真实 dyadic 骨架、闭窗口真实端点、精确临界 Gram 及正化骨架质量的损失。
- `PACKETWISE_MINIMUM_NO_GO.md`：固定树、固定真实骨架及细余项下，逐包只降低三角矩的选择不能改善返回原道路后的正包预算。
- `verify_signed_skeleton.py`：标准库精确有理核验；运行 `python3 rh_triangle_skeleton_20261122/verify_signed_skeleton.py`。
- `signed_skeleton_checks.json`：72 个 Gram、72 个凸端点、72 个正支撑、325 个标量 no-go 和 36 个重叠包检查；全部通过。

根作者完成推导；真实证书分支已完整阅读两份证明，手算核对三点归一化、端点核算、骨架辅助例及 no-go 的符号范围，未发现错误。这是同作者交叉核对，不是正式独立 Review 或项目数学接受。

一般辅助例与实际算术道路严格分开；真实完整道路数值见相邻 `rh_triangle_certificate_20261122/`。逐包相位实现与正交代价见相邻 `rh_triangle_arithmetic_20261122/`。
