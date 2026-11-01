# PREFIX-410 — 实际执行、范围、来源和下一问题

日期 2026-11-01。状态：AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING。没有借用他人 owner、claim 或独立 review。

来源固定：GLOBAL_KNOWLEDGE_V1 main@50bd0cf9511f7730690d8c69b86ac37475e95115；Enterprise Math 科学输入 main@e5f31bafe2c7dd421430023f4d717013c424525f。读取规范入口、P000、ACTIVE 世界观、联合观察保真、BRC 及 portable research 协议。GitHub 实际账户 awdawmip，可 push；EM service0.6.11 research_authority_granted=false、UPSTREAM_CODE_REVIEW_REQUIRED、active_jobs=5/5，Owner 查询 CONTROL_QUOTA。

## 完成的可证伪结论

- 六观察域：ε=β=10^-6、η=10^-4，I1=1 准确，其余六观察为闭区间。
- 对每条 u≈±i 来源叶，逆观测定位 |u−σi|<6ε/5，且必须保留 σ 分支。
- 连续全域 NO: κ<243919763/61000000，不存在单一相干来源。
- YES 见证：u=9/10000000+i·19999991/20000000，v=2499/50000000−i·7/50000；同一原始五 Port 矩阵重建 Y；κ≥79973935043034167/20000000000000000 为合法来源。
- 故 κ_* 在上述准确有理数上下界之间（宽度14777625084187/1220000000000000000）；尚未获得 κ_* 精确值。
- κ_* 小于 PREFIX-409 的双基准准确阈值；静态辅助模型不是 P000 原生结论。

## 确实执行的程序和日志节选

```
python3 prefix410_exact_lipschitz_certificate.py
PASS exact remainder for branch 1
PASS exact remainder for branch -1
PASS rational global remainder bounds: Cplus=25668725967/1525000000 Cminus=17474733481/1150000000
PROVED_NO_BELOW=243919763/61000000
PASS coherent rational witness, six noisy observations
WITNESS_KAPPA_UPPER=79973935043034167/20000000000000000
NO_GO_TO_YES_CERTIFIED_WINDOW_WIDTH=14777625084187/1220000000000000000
PASS_PREFIX410_EXACT_TWO_SHEET_LIPSCHITZ_AND_FULL_NOISY_BRACKET
python3 prefix410_independent_original_matrix.py
PASS original five-Port A, recovered Y, all six interval inequalities
PASS_PREFIX410_INDEPENDENT_ORIGINAL_MATRIX_SOURCE_WITNESS
```
两份检查器实际使用精确算术。独立程序从原矩阵重算，不依赖主程序的 I4/I5 化简。证明的全称范围来自正文逐式严格不等式，并非运行有限输入就自动成立。未执行全噪声 CAD、Lean、原生 typed BRC 或任何共享数学成果准入操作。BRC: COMPOSE_APPLIED；来源分支、相位和联合测量保留。

外部文献仅背景：arXiv:1109.4499（2011），arXiv:2608.02450（2026-08-03）。下一 PREFIX-411：κ_*(ε) 在 ε=0+ 的精确右导数和联合活跃边界/来源叶；继续保留原生 BRC-X6 桥接为未证明义务。
