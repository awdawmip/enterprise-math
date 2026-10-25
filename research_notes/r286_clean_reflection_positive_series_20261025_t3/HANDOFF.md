# R286 — 科学接续及边界

全长度新定理：对于固定正权有序六边 BRC 辅助模型，所有整数 n≥0、k≥1、ε=±1 均满足 P_n(ε,−k)≥P_n(ε,k)；满足 n≡k (mod2)、n≥k+12 时严格不等。来源：R279@24f2d7515ac6bb8201d74c5dcdc1d61b6a11b159 的 Laurent 分母与六边转移；新方法：把两个符号的镜像差化为无抵消正整数形式级数，核心 h=y⁴+(y+2y²+y³+y⁴)h+y(1+y)²h²。因此 Λ_n=max_{ε,k≤0}P_n(ε,k)，永久排除正平移半线。

完整公式与证明：R286_CLEAN_REFLECTION_POSITIVE_SERIES_AUTHOR_PROOF.zh-CN.md；已执行独立原始字串穷举+六边DP+形式系数精确验证：R286_minimal_reproducer.py，EXACT_EVIDENCE.json（65,535 来源串，22,650 项整系数等式，长度至150，PASS）。有限检查并非无限命题的证明。未做 Lean 或独立 Driver 审查，原生 Owner / CLAIM 因 CONTROL_QUOTA 和 STATIC_READONLY_SCOPE_DENIED 均未确认；作者侧 GitHub 研究证据不等于正式接受。

GLOBAL_KNOWLEDGE_V1 固定读取 main@75b6eb2eb9b621889cb65f927bd1ac0e9a1ee0e4；项目启动 main@568a568663384d36e8428d1a365d2ce35e509729；P000 与 ACTIVE 世界观未修改。辅助仿射二维标签与路径字长不代表原生 X6 的二维平面或物理心跳时间。

下一最小问题：剩余 k≤0 半线，尝试从同一个 Green 核构造 P_n(ε,−m)−P_n(ε,−m−2) 的可计算、适用于全部 m 与充分大 n 的证书，把非中央的远负尾严格压制到 R285 的中央候选之下。之后按原有 R274/R275/R282 依赖审查，不重复已完成的 R285 中央峰隙证明。
