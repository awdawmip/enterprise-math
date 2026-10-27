# PREFIX-279｜Stage50 C4-BRC 同谱来源包、条件门反例与原生类型缺口

**状态**：AUTHOR_SIDE_EXACT_PROOF / 1320_INDEPENDENT_EXACT_PAIR_CHECKS_PASS / ORIGINAL_STAGE50_NOT_RERUN_THIS_TURN / NATIVE_TRANSFER_PENDING / NOT_ADMITTED。

## 固定来源与前沿
GLOBAL_KNOWLEDGE_V1 固定 `awdawmip/chatgpt-global-knowledge@71ae2614ae7b319034e9adbe1f9db72bd777f6ee`；P000 启动投影 canonical blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` 等于原件，ACTIVE 世界观已读。Enterprise Math 科学输入固定 `awdawmip/enterprise-math@5ff4f298aa50ed93ad08bdd47e9a214baa27cb8b`。Portable research `docs/PORTABLE_RESEARCH_PROTOCOL.md` blob `ca5de2d680d2439ff4b67c2c55fbd4159813cd5c`；BRC-only 约束 `research_constraints/heartbeat_brc_only.json` blob `62ffa6bbdafd54496e27284a26a2aeaf2d04df99`。

继承已验证前沿 `research_notes/research6_prefix278_original_stage50_c4_brc_20261027/PREFIX278_ORIGINAL_STAGE50_BRC.zh-CN.md`。其已使用原始 Stage50 源码（原始提交 `318f47839d6bc7c850a3b7cc0fcb22d48febd9ba`，`stage50/interference.py` SHA256 `43b23d47e5d3da191aeaeefefe4f378fea2166eefd228ae77475f7196ceca853`）实际验证十二 Port 的十外端口 C4-BRC 读出。之前24项原始调用**不重复算成本轮实验**。

## BRC 载体、精确观察和静态商定理
固定有限、带完整历史来源标签的 C4 包 `a_j=w_j i^{q_j}`，其中 `w_j∈Q_{>0},q_j∈Z/4`，无占据处视为零。来源历史差 `r≥0` **不是物理心跳时间**。定义全来源配对的有序路径对：
```
Z = Σ_j |a_j|² > 0
C_r = Σ_j conjugate(a_{j+r}) a_j
c_r = C_r/Z
E(r,p) = (5/18) × [1 − Re(i^p c_r)],   p=0,1,2,3
```
最后式严格复用 PREFIX-278 原始 Stage50 BRC 端口恒等式：十个外 Port 总质量、十二 Port coin、两输入 Port A/B、固定输入归一化 2Z。它不是普通传播器，也不能因是一次局部源码操作就称为完整 `H_n→H_{n+1}`。

**定理 1（全静态读数恰好恢复标准化自相关）**：两个有限 C4 包的全部 `E(r,p)`（每个 r≥0 与四个 p）相同，当且仅当每个 `c_r` 相同。证明由 `Re(c_r)=1−18E(r,0)/5` 与 `Im(c_r)=18E(r,1)/5−1` 精确反演；充分性直接代入。若同时记录 `Z`，则等价于完整 `C_r` 一致。这**不**代表可恢复带来源标签的振幅序列，更不是任意未来操作的充分状态。

## 定理 2：三个来源的最小长度非平凡碰撞
取连续历史标签 0,1,2 的两个严格正整数 C4 来源载荷：
```
f = (1,4,4)      g = (2,5,2)
Z_f = Z_g = 33
C_0 = 33,  C_1 = 20,  C_2 = 4,  C_r = 0 for all r≥3.
```
二者非同一包，也非反转、平移、整体 C4 相位或整体比例等价。故其完整 `E(r,p)` **对全部 r≥0、p=0..3** 严格相同，输入总质量也相同。

**无穷族的代数证明（不用 π/三角函数）**：任意正有理 `a,b`，记
```
F(z)=(1+a z)(1+b z),   G(z)=(a+z)(1+b z).
(1+a z)(1+a z^{-1})=(a+z)(a+z^{-1})=1+a²+a(z+z^{-1}).
```
故恒有 `F(z)F(z^{-1})=G(z)G(z^{-1})`。各 Laurent 系数正是严格保留路径来源标签的有序 BRC 自相关 `C_r`。取 `a=b=2` 得 f,g。此为完全代数的结构性同谱，不是有限测试拟合。

**最小长度的精确作用范围**：在连续占据、严格正实数、保留 `Z` 和全部自相关、把来源平移与反转视为等价的类别中，一个非零载荷由 `Z` 确定；两个载荷 x,y>0 由 `Z=x²+y²,C_1=xy` 确定其正和 `x+y=√(Z+2C_1)` 及积，因此只余反转，不存在非平凡碰撞。故三来源最少。对**三来源正整数**并限定每项不超过 M，完备穷举 M≤4 无非反转碰撞；M=5 才首次出现上述 f/g（有限整数幅值结论，不扩张为一般有理优化）。

## 定理 3：条件未来 C4 门破坏同谱商
**仅作额外声明的形式操作，尚非原生合法门**：若后续允许 `U_0` 只将来源历史 j=0 的 C4 character 乘 `−1=i²`，其它来源保持不变，则
```
U0f=(-1,4,4),  U0g=(-2,5,2);   Z=33 unchanged.
C1(U0f)=−4+16=12; C1(U0g)=−10+10=0.
E_U0f(1,0)=35/198;  E_U0g(1,0)=5/18;  difference=10/99.
```
因此同一个“U0 后读出”操作能严格区分两个全部**当前** Stage50 读数相同的来源包。只保留 `Z,(C_r)` 的静态商对这种**扩展后的未来操作语言**不封闭，必须保留来源结构或额外充足残差。**绝不可**据此声称 U0 已由真实 Cell/Port/材料/场/边界/物理时间实现。

## 原生 H_n 转接类型审核
当前 Source `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`（blob `94a02d067be2b039ca4c0f7ffedb5ebde8430e08`）规定心跳世界是六原生空间轴、独立时间、完整离散 Cell，`fixed_heartbeat_program=null`。另 `definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json`（blob `9942a9dd127c4d4db7a6045feb3cd93a53233203`）明确 H_n 需要 scope、native_cell_labels、material_labels、physical_time_or_order、state_and_momenta、field_state、source_boundary_conditions、constraints、branch_and_provenance、model_law_id、numerical_status。
- Stage50 `local(f,r,p)` 接入有限来源历史载荷、C4 控制、局部 Stage46 十二 Port coin 和 Stage49b link-current/Gauss 相容（PREFIX-278 已核验），但不提供完整六轴合法地址 codec、全局材料/动量、全部边界、全场约束、真实检测效应和独立时间演化。
- `r` 是来源标签差，不是实际时间或“第 r 次心跳”；三来源不是三个空间轴；十外 Port 的数学测度不自动成为实际仪器。
- `model_law_id` 到 `Φ:H_n→H_{n+1}` 的合法桥仍缺少已核验证据。**类型缺口≠证明全世界没有任何可实现更新**；本轮只能得出模型内条件反例，物理归因保持 UNKNOWN。

## 实际精确验证和执行边界
配套 `verify_prefix279_portable.py` 用 `fractions.Fraction` 与 C4 指数，逐来源 j、逐输出 Port、逐**有序路径对**计算十外 Port 的正质量，再独立用 c_r 公式核对。严格相等的独立计算：f/g 2包×5个 lag×4相位=40 次；此外 C4 三来源 64 个全相位配置×5个 lag×4相位=1280 次；**合计1320次 PASS**。f/g 各20种静态读数完全相同；对 M≤4 和 M=5 逐三元组穷举核验；条件门差 10/99 精确验算。一般所有 r 的结论来自上述 Laurent 证明，不靠有限枚举外推。

本轮 **未执行原始 Stage50 模块**；此前 PREFIX-278 的原始运行回执只作已验证来源。复用判定 `REUSE_APPLIED`（其端口观察法则）、`AUTHOR_EXACT_BRC_PAIR_CHECK_PASS`（本轮独立程序）。不做非 BRC 科学运算、不把正权质量冒充振幅。

## 真实身份、权限、Owner
GitHub 认证 `awdawmip`，对 enterprise-math 权限 admin。原生服务静态只读身份下 `em_session_start(RESEARCHER)` 返回 `STATIC_READONLY_SCOPE_DENIED`、`operation_sent=false`；`em_control_tasks` 返回 `CONTROL_QUOTA`。故当前活跃 Owner/CLAIM **UNKNOWN**，未进行任务抢占或冒充原生授权；本作者侧研究尚未正式 Result/Driver 接纳，原生研究活动登记亦未完成（SYNC_DEBT）。

## 下一 PREFIX-280
找出真实、可核验 `model_law_id` 及合法原生未来操作闭包，逐项验证六维 Cell codec、Port、材料、动量、完整场、三元/边界约束、C4 相位/来源门、检测效应和独立时间。如果存在真实来源选择门，先证明它的 H_n 映射，再在**原始 Stage50 Source** 对上述 f/g 执行并核对 35/198 vs 5/18；否则对**明确列举的真实合法操作**证明相关商是否因子化。保持 c_r 与来源关系残差，不预判物理解释。