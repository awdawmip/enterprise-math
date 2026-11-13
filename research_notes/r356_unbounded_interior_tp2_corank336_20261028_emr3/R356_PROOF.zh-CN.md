# R356｜BRC 第336条无界 Newton TP₂ 余阶带：精确证书与 R348 抽取边界审计

日期：2026-10-28。作者侧状态：**AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED**。全局快照 `awdawmip/chatgpt-global-knowledge@bf3b406f244a3ebdafeda33d61024d99ca0de8f6`；EM 项目规范基线 `main@4a729c315568b0b61240013dccaf49adb84b2728`。本轮不修改 P000、ACTIVE 世界观和已有 Result/Review。

## 命题、模型与条件

研究完整十二项保留符号的有序六边 BRC 辅助组合递推
[
B_0(t)=1+t,\quad B_s(t)=J_s(t)+\sum_{i=1}^{\min(12,s)}K_i(t)B_{s-i}(t).
]
K_i/J_s 的整数多项式定义采用存档 `R346_verify.py`，负系数不替换成正质量。令
[
D_{q,k}=\sum_{w=0}^k(-1)^{k-w}\binom{k}{w}2^{q-w}[t^q]B_{q+w}(t),\quad
M_{q,k}=D_{q,k}D_{q+1,k+1}-D_{q,k+1}D_{q+1,k}.
]

载重前提：R348(A1–A5) 的作者侧全指标有理抽取及次数界尚未独立审查，即对于 r,u≥0，
[
D_{r+u,u}=5^uH_r(u),\quad H_r\in\mathbb{Q}[u],\quad\deg H_r\le r.
]
以 L_r(v)=5^r H_r(v)，令
[
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1).
]
直接代入四个因子，`M_(r+k,k)=5^(2k+1-2r) Q_r(k-1)`，k≥1。以上 r,k 是辅助组合索引，不是心跳世界原生六维 X6 的 Cell/时间/动力学。未证明保留路径与联合关系的原生转移映射。

## 新有限证书：Q336 的 673 项全部严格正

从原始十二项带符号 K/J 递推，精确重建 B0…B1013，保留 t^0…t^675。依次重建 H334,H335,H336,H337，各自第 r+1 阶有限差分为零，最高差分为 6^r。注意：有限消失事实本身**不是**全指标次数证明；无限结论仍需 R348。

重算 Q335 的671项正差分，SHA256 `95e782ee91ff3b097d2af2d02106c53680b825c3290fbb3cb0365437096af943`，严格匹配 R355。

在 Q336 的 v=0,…,672 共673点上，求前向差分 c_i=Δ^i Q336(0) (0≤i≤672)，**673个系数均为严格正整数，无零项/负项**。原始证据按 `336,i,decimal_integer\n` 逐行保存，SHA256：

`b00f2a797802649c9b07d31fdf5301c17e0a4e002892c6939a723da72ca20736`

同时核验 c672=30^672·Catalan(336)，最高三阶比值 R353/R354 公式，并对 k=1…8 的原始 D 子式逐一比对上式，8项精确相等且为正。符号断言使用 Python 大整数与 Fraction，未使用浮点判号。

因为 R348 给出 deg Q336≤672，任意整数 v≥0 的**有限且精确** Newton 展开为
[
Q_{336}(v)=\sum_{i=0}^{672}c_i\binom{v}{i}>0.
]
从而**在 R348(A1–A5) 成立的条件下**：
[
\boxed{M_{336+k,k}>0\quad\forall k\in\mathbb{Z}_{\ge1}.}
]
与此前条件证书合并覆盖 k≥1、1≤q−k≤336。没有得到全二维 TP₂、k=0 边界、TP₃ 或 X6 原生结论。

## R348 的边界对抗审计

另用实际执行的 `R356_R348_boundary_audit.py` 从原始有符号 K/J 产生形式核 N(y,z),E(y,z)，重建 g_j(z)，核验 R348(A1–A5) 的**有限** 0≤r≤6、0≤u≤9 共70个 D 抽取相等式，70/70 PASS。对于核展开中确实出现的 q<m 项，逐项核查 0≤q−m+j<j 与二项式系数为零，共 **79/79** PASS。此审计将容易误用负次幂的位置显式检查；它不能代替 A1–A5 的全指标逻辑审查，也不是独立 Driver 审稿。

## 复现、可信范围、后继

在 PR 目录运行 `python research_notes/r356_unbounded_interior_tp2_corank336_20261028_emr3/R356_verify.py`（依赖 R346 原始递推源码），重建 673行数据及摘要；随后运行 `python research_notes/r356_unbounded_interior_tp2_corank336_20261028_emr3/R356_R348_boundary_audit.py`（需要 SymPy），重建70组抽取与79个边界检查。

实跑 R356_verify.py SHA256 `f752f09f673a13fa16b62241c7c2e939f844331871974aef35a314c97990a4b6`；实跑边界审计 SHA256 `d66fa7457e6056b53cd1b4b285d0e8ee31daace04c072b8f901771eb1f557527`。完整原始673行与日志见本轮 ZIP 保全材料，PR 的代码可逐字重建所需数据。

来源：R348 Draft PR #1599 commit `5347e506bd145028d7338e9f7993dcd2a2fed97c`；R355 Draft PR #1592 commit `e31d02e4a3f0eb58c20069489fa2994a70c3876e`。

Owner 只读查询返回 `CONTROL_QUOTA`；原生 session_start 在 host 身份下返回 `STATIC_READONLY_SCOPE_DENIED`、operation_sent=false。GitHub 项目具有 author-side 写权限，但未取得原生 CLAIM、Source Result、Driver 接纳。下一个具体研究问题是 Q337 的675项完整 Newton 差分和 R348(A1–A5) 的真正独立载重引理审查；更优先寻找对所有余阶 r、所有低阶 Newton 系数的统一证明或反例。
