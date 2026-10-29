# R345 portable research handoff

**母目标：**验证或精确否定 BRC Newton 辅助阵列 `D_{q,k}` 的内区 TP₂ 正性，兼顾 `k=0` 已有负子式和 `TP₃` 已有负三阶反例。P000 心跳世界 X6 与 ACTIVE 世界观不变；BRC 辅助模型不直接转为原生动力学。

**最新作者侧研究增量：**由 R344 `1≤r=q-k≤255` 扩展至 **`1≤r≤300`，`k≥1` 无界**；新增45条斜带、25,065个正 Newton 整数证书；总90,600个均严格正。依赖 R330 作者侧尚未独立审查的 `D_{r+u,u}=5^u H_r(u), deg(H_r)≤r`。

**精确材料：**`R345_PROOF.zh-CN.md` 完整论证；`R345_VERIFY.py` 原始带符号 K/J 整数递推和差分验证；`R345_EVIDENCE_SUMMARY.json` 数据摘要；`R345_NEW_BAND_CERTIFICATES.csv` 新45条带逐条 SHA256（可由程序生成并比对）。对每个 `r≤301` 额外一个插值点检验次数界；B_s 重建到905，所需 t 幂不超过603；正性全部精确整数/Fraction，未用浮点符号。

**复验：**`python R345_VERIFY.py --max-r 300 --out R345_EVIDENCE.json`。选传 `--prior R331_INTERPOLATION_EVIDENCE_256.json` 和 `--r332 R332_EXACT_EVIDENCE.json` 做历史全部33153个系数及44条摘要交叉核对。新增25,065项整数规范文本 SHA256 `5835f388f9a78bbcde8bff10a4ff5bfa85364794a8658084efb48526d5fbb136`；旧65,535项复现 SHA256 `6b3f762cada37f8b00a51541a2568d93633911d6839fe0fee9bcf2ebf85aa795`。

**控制/权限：**本次连接的 GitHub 身份为 `awdawmip`（项目读写权限）；原生 `em_control_tasks` 返回 `CONTROL_QUOTA`，不能确认活跃 Owner，无本对话获得的原生 CLAIM/Source Result/独立 Driver Review。Research-Activity-ID `RA-EMR3-20261028-R345-TP2-300-F4F94AED59B7` 使用本真实执行对话自分配的 local session key，并非服务签发的执行 ID。仅作 `AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED` 研究交付。

**冻结并不重算：**R339 边界 TN₂ 反例、R342 内区 TP₃ 反例、R343 `q≤1024` 内区有限精确证书、R344 `r≤255` 无限条带、R331 的33153项旧系数。本轮已经复核 R344 全部65,535项摘要，不必在下轮为确认身份再执行相同任务。

**下一最小判别问题：**构造 `H_{302}` 与 `Q_{301}(v)` 的603项 Newton 差分。若非正需区分正锥充分条件失败与真实 `M_{q,k}` 变号。并继续寻求可控制 `r,k` 同步增长的结构证明及 R330 引理的独立数学审查。

**保存/准入区别：**PR 的研究证据持久化与 activity 登记都不代表原生任务所有权、数学审查或准入。
