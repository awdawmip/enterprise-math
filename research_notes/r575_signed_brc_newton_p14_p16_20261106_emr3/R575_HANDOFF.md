# R575｜研究接续材料（2026-11-06）

冻结源 R462@`18783e01e3646c72b7aab3b16d3f565e83e6446f`；上轮 R574@`2860e9a1596027fba449e3ce2522a985e9519bea`。研究对象仅为 signed BRC 辅助标量谱。

本轮定理：p14(k)>0 对全部 k≥2；p16(k)>0 对 2≤k≤6，p16(k)<0 对 k≥7；全参数精确有理系数证明使谱半径下界指数从 23/12 推至 31/16，常数精确见 `R575_PROOF.zh-CN.md`。

材料：`R575_PROOF.zh-CN.md`（定义和推导）、`R575_VERIFY.py`（实际执行的精确符号及独立整数核验程序）、`R575_EVIDENCE.txt`（真实 stdout）、本文件。复现 `python R575_VERIFY.py > R575_EVIDENCE.txt`，要求终止标记 `R575_NEWTON_P14_P16_EXACT_PASS`。Python 3.13.5、SymPy 1.14.0；k=2..1000 完成 31968 项 Fraction 恒等核验，另检查 k=2..20 原始 signed coefficient。

科研接续问题：对 p18/p20 寻找新的有理首系数与全参数符号证书，研究固定 m 首系数的生成函数及其零点。研究仍为作者侧；原生 X6 任务的当前 Owner/CLAIM 单独核对。不得把精确标量结果提升为原生世界论断或正式 Driver 数学接纳。
