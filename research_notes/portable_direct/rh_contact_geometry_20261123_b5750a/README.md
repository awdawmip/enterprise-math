# 本轮复算与接续

先读 `REPORT.md`。本轮完成任意骨架的相对根能量浅树证明、非减回归与凸下包络识别、接触区间预算及阈值修复，并对原实际窗口作有支付误差的有限比较。

## 完整证据

所有新程序只依赖 Python 标准库；原运行使用 Python 3.12。三个结构分支可独立运行，实际计算只需三个旧小依赖和本轮固定几何，不需要旧实际 q 样本表或完整 D 缓存。

主实际证书 `monotone_compute/monotone_projection_certificate.json` 为完整约9.52MB的JSON。复算ZIP直接包含原文件。为使Source中的每个证据对象可以逐个读取核对，Source以 `monotone_compute/certificate_storage/` 中的六个有序文本分片保留它的无损XZ/base64表示；`ENCODING.json` 记录原文件、压缩数据和各分片的SHA-256。恢复命令如下，已有正确JSON时只核对字节：

```bash
python3 monotone_compute/restore_certificate.py
```

这是完整字节的存储表示，未删减任何数学字段。`summary.json` 另供快速查看，不能替代主证书。

## 从本目录复算

```bash
python3 monotone_correlation/verify_monotone_contact.py
python3 threshold_pools/verify_threshold_pools.py
python3 general_trees/certify_general_weighted_trees.py
python3 monotone_compute/certify_monotone_projection.py \
  --harmonic-module dependencies/certify_fast_harmonic_energy.py \
  --oracle-module dependencies/certify_paired_prefix.py \
  --family dependencies/fixed_matched_family.json \
  --geometry monotone_compute/fixed_geometry.json
python3 monotone_compute/diagnose_contact_thresholds.py \
  --main-module monotone_compute/certify_monotone_projection.py \
  --harmonic-module dependencies/certify_fast_harmonic_energy.py \
  --certificate monotone_compute/monotone_projection_certificate.json \
  --geometry monotone_compute/fixed_geometry.json
```

复算会写回各脚本同目录的输出。实际计算的计时字段正常变化；数学整数区间、固定输入和作用范围都在证书中。分支文稿的绝对或原工作目录路径保留了原运行位置，在其他位置应使用本页的相对参数。

## 前置依赖

ZIP包含 `dependencies/`，所有文件保持既有字节。Source只记录 `DEPENDENCIES.json` 的不可变来源与哈希，不把旧材料复制称为新结果。只下载本轮Source目录时，先按清单取得三个运行依赖；其余旧文稿供阅读证明依赖。

## 核验范围

- 结构恒等式和一般定理由完整解析证明承担。
- 有理有限例检查程序、边界、常数与反例；不能替代无界算术量词。
- 实际E、回归距离与Haar预算均支付完整厚度误差；参考接触没有被标成真实接触。
- 阈值表控制真实细插值，完整未采样q仍需细余项。
- 本轮是作者研究，没有正式Result或独立Review。

## 下一条数学任务

任意骨架的浅树存在性已闭合。算术上并列保留原定向Haar尺度预算与新的接触区间／阈值预算，研究真实匹配族的长区间局部抵消、负凸骨架的联合支付及参数统一性。普通全局非减回归在当前实际窗口保留了至少99.9037%的细投影方差，不宜仅凭投影存在就预设它会大幅节省预算。
