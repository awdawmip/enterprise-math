# R347 HANDOFF — BRC Newton 内区 TP2 余阶302

项目研究入口：沿用 Draft PR #1592 的 R345→R346→R347 分支，勿重复已完成前301条带。规范读取：GLOBAL_KNOWLEDGE_V1 main@fa7202d5e3a897cc6e295d9da5c1341a06c3bb16；项目 main@178b13bf780c92917be8eb49b414df3743f30886；R346 不可变前沿 37516cc5bb8d72098ce25f2d64881ec5da4279cd。

本轮新单元：十二项有符号 BRC 辅助递推，完整验证第302余阶 Q_302 的605项 Newton 差分全部严格正，SHA256 b7a222c6840358ba7d92943a376e58dc6a3dfe08e14a9acf3eaf8f3a404069df；精确交叉核验 R346 第301余阶603项 SHA256 242f508cdf355e238c7052d3e7bb66b71754d5e474c85e617328210f951c4484；仅重新建立 H_300..H_303，其他历史带复用原已存证据。

证明全文 R347_PROOF.zh-CN.md；可运行源码 R347_verify.py（实际执行源码 Git Blob 710296e71176ff6c694a1ccc592cf3d5fa890952）；R347_EVIDENCE.json 是真实执行证据的浓缩记录。运行时生成605行 R347_Q302_COEFFICIENTS.txt。完整已运行输出与日志见本轮用户研究附件。

数学状态：AUTHOR_SIDE_EXACT / CONDITIONAL_ON_R330 / UNREVIEWED / NOT_ADMITTED。所有无界命题依赖尚待独立复审的 R330 有理抽取与次数界。没有将组合模型推为原生 X6 动力学。未取得活跃 Owner 权威确认、原生 CLAIM、Source Result 或数学接纳。作者来源 LOCAL_R347_4147DCF1CA。

下一最小单元：H_304、Q_303、607项完整差分；独立检查 R330 全指标抽取/次数界，探索全二维 TP2 正性或精确反例。保持 PR Draft，等待合法 Driver 独立审查。
