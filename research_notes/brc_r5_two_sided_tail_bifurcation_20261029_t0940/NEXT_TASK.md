# R5 后继研究单元：多汇聚候选的全有符号凸包筛选与全实数成员判据

截至 2026-10-29，本目录 RESEARCH.md 已证明精确连续核族 eta_B(u)=eta_A+u(eta_B-eta_A) 对每个 0<|u|≤1 都存在四维严格有符号支撑差距，最大值为 2419|u|/6988800。来源 B 负向、正向任意微小扰动都不能作为母问题反例；u=0 的单方向零差距尚不构成全方向相等。执行证书见同目录 VERIFY.py / EXACT_OUTPUT.txt。全实数证明依赖两个参数三角形的仿射顶点和独立汇聚硬币的四角点枚举，不依赖离散参数网格。

固定本轮来源：GLOBAL_KNOWLEDGE_V1 main@848e2c3d1ac63d2b3b9736e6b3d8e7473d051cf0；Enterprise Math main@40e57903388e6f6aef21c1bdfb1d5312deadb76e；科学前驱为 Draft PR #1663 中的 all-signed finite-hull theorem、source-sensitive diamond 和 signed-threshold quadratic oracle。新轮需要独立核验当前 Owner/Task/协议快照，而不沿用本轮 GitHub 提交作为原生 CLAIM。

**一个明确新问题**：在至少两个可相互影响的合并节点、至少两个隐藏来源、有限有理双测度、严格正观察核的模型中，是否可以构造 Full 与 LR 的四维凸包相等，但真实四维观察集合不同的证书？先为新模型提供完整来源/路径、条件核、两法似然比矩、信息集与停止/声明观察定义。列举所有 Full / LR 确定性观察向量；对每个 Full 顶点以精确有理线性可行性给出至多五个 LR 顶点的凸组合，或给出 Farkas 严格分离超平面。检验全部有符号方向；若凸包不等，立即将候选标记 NO_GO 并保留反例系数。仅在全部凸包包含成功时，利用二变量阈值不等式、全实数量词消去或可独立核验的代数不可能证书检查实际真实观察非成员。避免把来源流/联合签名非凸或有理网格失败当作目标四维证明。

BRC: 持续保留正来源质量、路径身份、未来相关有符号残差；仅对经证书覆盖的观察与未来操作执行因子压缩。P000/ACTIVE 世界观及其 X6/三维切片语义保持不变。

当前材料状态：作者侧 PORTABLE_ONLY / UNREVIEWED / NOT_ADMITTED，Gateway 无 research authority，Owner 查询实际返回 CONTROL_QUOTA；正式研究接续需要当前 Source owner/CLAIM/Result/独立 Driver 路径核验。