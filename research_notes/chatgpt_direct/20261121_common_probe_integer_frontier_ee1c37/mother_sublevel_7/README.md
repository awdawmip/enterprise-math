# 第七种 E2 配置：完整原执行回执

母内大小 `(12,13)`，proper 大小 `(9²,10⁷,12)`，总费用至多 9,995：六个完整母类框架全部正常结束，**51,672,395 个搜索节点，0 个整表**。这使完整两母内类预算层的已完成配置数由 D 固定包中的 6/14 增至 **7/14**。

本目录保存真实原执行回执及输入/源码绑定。搜索使用 D 已独立重跑验证的同一 `native_regional.cpp`、同一完整 proper 银行和同一逐费用偏差容量表。此处没有另行重跑五千余万节点，也不声称进行了第二次全搜索。

与 D 中两个 `(13,13)` 配置相比，本型的母并集内余量 `d` 为 0 或 1。候选库替换已经在 D 中与原生成器逐掩码核对了这两种余量；区域预过滤只使用不会增加的初始 `d`，且原母内类终局分配和实际费用检查保持原样。因此没有需要通过重复全搜索解决的新完整性缺口。

`verify.py` 检查完整源与候选银行绑定、C 的六框架全集、全部命令参数、逐框架原 stdout/stderr、聚合计数，以及该大小型确在 C 的完整十四型计划内。它不运行覆盖搜索。

```bash
python -B verify.py \
  --D-proof /absolute/path/to/proof_bundle_D \
  --mixed-proof /absolute/path/to/C_mixed_proof_bundle \
  --mother-proof /absolute/path/to/C_mother12 \
  --output /absolute/path/to/execution7_verification.json
```

这里的 E 计所有大小的母内类；不改为仅计大母内类。其余七种 E2 大小配置仍不由本目录宣告排除。
