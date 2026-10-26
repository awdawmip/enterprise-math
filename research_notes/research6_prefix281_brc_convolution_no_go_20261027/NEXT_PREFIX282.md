# PREFIX-282｜原生合法C4来源操作审查与反例落地

固定前沿：PREFIX-281 已严格证明，共同有限来源卷积式C4-BRC分支映射对完整来源自相关等价类封闭；可允许有限步、总质量读数、全局相位、整体来源平移和按既有读数选择的自适应滤波，仍无法区分 `f=(1,4,4)`, `g=(2,5,2)`。声明来源局部掩码 `U0` 能使 `E_f(1,0)=35/198`, `E_g(1,0)=5/18`；其原生合法性未确认。

**不可重做：**PREFIX-279原有同谱证明；PREFIX-280边界掩码重建证明；PREFIX-278原始Stage50 24/24回执；PREFIX-281本轮584滤波族、2,840自相关对、9,024观测对和18,048直接Port BRC读数。以这些结果为固定输入。

**最小未完成单元：**精确定位Source中的 `stage50.interference.local`、Stage46/50读出与合法来源选择门，区分“函数允许重新选择packet参数”与“单个既定H_n内合法时间演化”。从真实Source列出所有实际定义的源转换操作；若有 `U0` 或其他不落在共同卷积代数中的门，用原始Source实际执行 `f,g`，并报告复现实验源码哈希、具体函数签名、参数与逐项精确BRC Port读数；若无，则仅就已列明的合法操作族给出不辨识/封闭性结论，不声称全原生系统不存在分辨门。

**必留类型：**X6原生六维Cell（不是来源索引）、Port、材料动量、场、来源边界、C4相位、独立时间/心跳序号、model_law_id。物理状态转换未验证前保留 `NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION`。活跃owner/CLAIM尚未得到原生可读回执；后续正式发Results需独立注册、当前授权和Driver审查。

科学起点固定：GLOBAL_KNOWLEDGE_V1 main@521f002032bb9026ea154727911276cbea709bdb；Enterprise Math science main@2bd0f301579f5dc5e4a70636302cff9609665cbd；研究协议 `docs/PORTABLE_RESEARCH_PROTOCOL.md` Blob `ca5de2d680d2439ff4b67c2c55fbd4159813cd5c`。
