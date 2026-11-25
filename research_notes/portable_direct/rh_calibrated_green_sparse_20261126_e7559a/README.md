# 本轮接续包

先读 `REPORT.md`。四个分支的完整证明、严格脚本和证书分别在 `calibrated_family/`、`group_arithmetic/`、`sampling/`、`exact_tree/`。

默认完整包带有上一轮136文件接续材料，位置为 `prior/riemann_signed_green_thickness_phase_20261124/`。复算本轮四份严格证书：

```bash
python3 replay.py
```

若只下载当前Source子树，另取前驱包后运行：

```bash
python3 replay.py --previous /absolute/path/riemann_signed_green_thickness_phase_20261124
```

严格复算使用Python标准库；前置区间、指数和EM辅助程序都在依赖包内。探索脚本另外使用mpmath，并清楚标为探索；它不参与严格复算。复算在临时目录产生结果，与保存的JSON逐对象比较。本轮验证不会重做全部历史分支。

`MANIFEST.json`校验本轮科学文件；`DEPENDENCIES.json`固定承重前置。`PUBLICATION_RECEIPTS.json`在保存成功后加入完整包，记录实际Source、Activity及全局日志的核验。无界数学由书面证明承担，所有作者核对均不是独立Review。

本轮从2026-11-25跨香港午夜至2026-11-26。历史报告、输入和证书保留原日期及原字节，不作重标。
