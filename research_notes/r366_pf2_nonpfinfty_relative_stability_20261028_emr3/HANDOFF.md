# R366｜可移植研究交接与下一执行指令

**研究目标：**继续进取数论／Enterprise Math。保持原始十二项有符号 BRC K/J 辅助组合模型，不把它冒充 P000 原生六维 X6 或三维切片物理定理。作者侧现有成果未取得原生 CLAIM/Result 或独立 Driver 审查。

**两份独立规范读取 pin：**GLOBAL_KNOWLEDGE_V1 `awdawmip/chatgpt-global-knowledge main@05b476005671b3ac9f4cfff09ff08db977cc9e42`；Enterprise Math `main@35b25780e54fb34378f305e2b3bd06fe7f782f92`。下一轮应按自己的当前快照刷新规范，不要将本文件的旧 pin 当作永远的最新版本。

**最高已确认科学前沿：**R365 保存的原始 BRC 完整整数证书 r=345..352，5584行 SHA256 `50bf1a56fabe89d4752ed71634cbb95d6c7c320d61b09aba1c501857650555a7`，原始源码在邻近 `r365_brc_pf2_not_pfinfty_q345_352_20261028_emr3/`。R366 本目录新增证明：针对 **八条已验证有限余阶的所有逐坐标实系数相对扰动**，如果扰动幅度≤1/730，系数序列必为 PF₂ 但不为 PF∞；该界在整数倒数 1/p 的序列里最优，因为 p=729 时 r=352、j=344 的明确 perturbation 使普通 Turán 严格失败。r=1 的 F₁(z) 还得到精确非实根 `(-21±i√214)/15`。无需为报告目的重跑 R365 原始全扫描。

**复现路线：**若手头已有完整 R365 原始系数文件，可直接运行 `python R366_robust.py /path/to/R365_Q345_352_FULL_COEFFICIENTS.txt`；若无，先按 R365 原始源码 `python R365_scan.py` 与原有 R346 保留符号内核重建。程序校验每一行精确 SHA256，不允许用浮点近似判号。查看 `R366_PROOF.zh-CN.md`、`R366_EVIDENCE_SUMMARY.json`。所有重计算属于辅助组合模型，不代表原生物理实验。

**可直接交给下一研究者/Codex 的任务：**先消耗 R366 的系数空间稳定性定理，寻找真实**合法的 K/J 参数扰动 → Newton 系数误差**的定量传递估计；或转向全 r 严格普通 Turán/PF₂ 的统一定理或精确反例。明确是否保存支路的正负号和来源，切勿使用 PF∞ 或 ULC 作为先验，因为这在已有有限证书里被反证。另独立审查 R363 形式抽取与次数界。若选择继续有限 r，请只处理 r≥353、保留 r352 回归摘要，不把新的有限行包装为全 r 证明。

**实际状态：**原生 Sites `research_authority_granted=false`；查询活跃 Owner 返回 `CONTROL_QUOTA`，无法权威确认；无 Source CLAIM、Result、独立 Driver 数学接纳。此目录是现有 Draft PR #1592 的作者侧研究材料，不影响控制状态机任务归属；未更改 P000、ACTIVE 世界观及共享权限。
