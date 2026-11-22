# 三角矩尺度与相位研究批次 · 2026-11-22

从 [REPORT.md](REPORT.md) 阅读本轮数学结论、真实有限数据及未证目标。四个子目录分别保存尺度条件与辅助源构造、真实道路三角矩、算术核与相位正交、真实骨架和下降筛选障碍的完整推导及计算材料。各论证在当前范围内共同构成本次研究批次；没有单独的定理接纳或正式独立 Review。

## 研究来源

- 研究者 `EM-DIRECT-B5750A / TASK_RESEARCH`；Activity `RA-60C6D083A81B19084A74C5BA`；原任务上下文 `RS-RH-METHOD-TRANSFER-20261121`。
- 科学入口冻结在 `awdawmip/enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7`；P000 / X6 及完整道路含义保持适用。
- 本轮进入时核验控制 `f64efbd2e0e6e01a1643324af004341634b690d9`；保存时已读取最新适用的 `d39eedce95fbe62e853b67596d2521e531054bc7` 研究与保存说明。
- 全局入口初读 `c614a428f8d926d0fa536c7281a72fd4d2dbb491`；保存前读取 `bbe0c3600830e2e67bf8cef304335da0604157f6` 的最新数学政策及进度协议（2026-11-22 10:29:58 +08:00）。
- 前一批数学与固定输入：[Source a1a75fe](https://github.com/awdawmip/enterprise-math/tree/a1a75fe96789c1c3f40d5f58f1cda07661a5ef15/research_notes/portable_direct/rh_joint_correlation_20261121_b5750a)。复用其完整道路与节点输入，没有改写旧研究文件。

## 复算

仅需 Python 标准库。在包含四个新目录的根目录依次运行：

```bash
python3 rh_triangle_scale_20261122/certify_scale_examples.py
python3 rh_triangle_certificate_20261122/certify_dyadic_triangles.py
python3 rh_triangle_arithmetic_20261122/verify_triangle_arithmetic.py
python3 rh_triangle_skeleton_20261122/verify_signed_skeleton.py
```

真实道路程序复用可重建缓存。缓存缺失时会由原固定输入生成；不把大缓存当作独立数学输入。算术分支不读取这个缓存，而由固定厚度节点另算小除数前缀和实际节点相位。

若只下载本 Source 目录，需从上一批的上述不可变 Source 取以下已有文件，放在本目录根的相应并列路径。完整复算 ZIP 已附这些**不变输入副本**；它们不重复发布到本次 Source：

- `rh_joint_certificate/certify_joint_energy.py`
- `rh_joint_certificate/joint_energy_certificate.json`
- `rh_correlation_rational/certify_matched_nodes.py`
- `rh_correlation_rational/rational_window_certificate.json`
- `rh_correlation_phase/phase_homogenization_checks.json`

计算文件记录其影响数学结论的输入、分母与区间端点；有限覆盖不外推为无界估计。文件哈希和提交只用于精确定位材料，不证明数学结论。真实道路证书采用作者给出的有限恒等式与有向区间；辅助源无限族由书面证明承担。部分运行时间或输入文件记录可能随重新生成改变，数学范围与区间判断应按内容核对。

## 当前前沿

已经证明尺度预算弱化、自动细区与短尾界、两类严格区别源族、整除核和短区间表示、消元树双正交、真实相位代价、骨架保留引理及逐包下降筛选障碍。真实有限窗口亦已核验。

仍需对无界实际匹配窗口证明不能自动支付的中粗层联合三角矩，以及真实骨架预算；sigma 与大除数交叉、修正回转、匹配参数一致性均须保留。下一步可直接从算术分支的短区间 c(d)、c(d)/d 表示推进。混合符号逐包截断只有严格接口，本轮没有实施优化或证明改善。

既往正式 Result 的历史错误 `NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED` 未重试、未更改。该状态不替代本轮已经实际完成的数学推导与有限核验，也不被本批保存改写成正式成功。
