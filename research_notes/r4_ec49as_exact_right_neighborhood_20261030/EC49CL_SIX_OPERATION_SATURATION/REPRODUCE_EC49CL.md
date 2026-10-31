# EC49CL — 在 GitHub 分支直接复核真实路径秩证书

本文件是作者侧可移植证据说明，不代替原生 Source Result 或独立 Driver review。

同目录含：`README_EC49CL.md`（完整解析定理、假设与适用范围）；`EC49CL_LITERAL_WITNESS_CERTS.tar.xz.b64`（四份真实有序路径证书的无损Xz+base64文本）；`RECHECK_EC49CL_GITHUB.py`（独立字面路径/后缀/类型化权重/DFA及模整数子式复核）；`CHECK_EXTREME_EC49CL_PUBLIC.py`（额外的两极端12×12完整独立构造）；`AUDIT_SUMMARY_EC49CL.json`（原生整数DP和后缀观察检查的已执行报告摘要）。

复制这些文件到同一目录后，直接运行：

```sh
python RECHECK_EC49CL_GITHUB.py
python CHECK_EXTREME_EC49CL_PUBLIC.py
base64 -d EC49CL_LITERAL_WITNESS_CERTS.tar.xz.b64 > EC49CL_LITERAL_WITNESS_CERTS.tar.xz
sha256sum EC49CL_LITERAL_WITNESS_CERTS.tar.xz
tar -tJf EC49CL_LITERAL_WITNESS_CERTS.tar.xz
```

可复核预期输出：n=14，`S^6` 秩381且26个满秩纤维，`S^≤6` 秩441且26个满秩纤维；n=16，分别秩393和453，28个纤维均满秩。独立极端脚本对两个轴输出 `390243 mod 1000003`，且返回PASS。XZ原始字节SHA256必须是 `bd483801753d8428f0a3d9c41fc90ee2c4c619bd12ef7fcd75d2be7091d78497`。Git Blob原件已核验：b64 `a9fbbbccf5f78da3efc0d05008a84a513d4b9aff`，独立复核脚本 `c312359bb4f482b2f58b0e2853195f6b5012e2eb`，和本轮实际执行的本地原件完全一致。

证明结构：恰好六次与至多六次的形式 DFA 行空间秩393/453（结合可复核0/1行秩）；n14两极端各缺6维的分析上界；n16 26个非极端完整证书前缀提升以及两极端12条实路径非零子式；奇偶障碍及双步前缀延伸，严格得 `n_sat(6)=16`。形式上界、真实路径模子式下界和有限原生DP交叉核对必须分开理解。

完整13文件原始归档 `EC49CL_EVIDENCE.tar.xz`（包含扩展生成器、完整原生BRC整数DP审核脚本、日志）保存在本次研究对话附件，sha256 `73b4409e9da2747f42a251b3c93ebdef205d3f6e185590f70203becc01d76d33`；**整个13文件归档并未上载本PR，只有四份精确实路径证书已无损远端保存**。因此 GitHub 直接可执行的复核涵盖四份模整数路径证书及两极端证明，原生DP的全量执行日志仍以该归档为准；不能把有限计算当成物理验证。

状态 `AUTHOR_ANALYTIC_PROOF / EXACT_MODULAR_WITNESS_AUDIT_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED`。下一EC49CM研究任意h饱和阈值的一般定理或严格反例，优先h7。
