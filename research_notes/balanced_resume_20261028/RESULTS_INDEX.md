# 2026-10-28 首轮平衡研究成果索引

本轮对本月成果库的 **12 个已知研究分类，各完成一个有界研究或实际复用单元**。这是服务覆盖计数，不是 12 个已正式接受的定理，也不代表遍历了全部 canonical Task。原库 435 条仍是文献整理单元。

来源冻结于 `7d2acd57622cbe7ad6acf4547d450e918dd670bb`（研究分支）。以下陈述与限制摘自作者接口；独立复核依据冻结稿与报告的精确 SHA256 绑定。作者稿内原有 `PENDING` 保留其创建历史，后续复核见本索引；这些复核不授予 Driver 接受、Task 关闭、Working Truth 或 Foundation 状态。正式任务实时状态仍为 `UNKNOWN`。

| 分类 | 本轮单元 | 实际进展与范围 | 原作者明确保留的边界 |
| --- | --- | --- | --- |
| `p11` | [完整有符号 Cauchy 外环的显式首端点区间](analysis/P11_OUTER_CAUCHY_EFFECTIVE_FIRST_ENDPOINT_AUTHOR.md) · [复核](review/P11_ENDPOINT_REVIEW.md) | 继承 A₀ 非奇异后，以显式有理 K_m 给出 η_m=min(1,1/(2K_m))（K_m=0 时 η_m=1）；0<t≤η_m 内同号且 \|det S_m(t)\|≥2⁻ⁿ\|det A₀\|tⁿ。 | 不闭合 η_m<t≤1，不证明 m 一致区间；core98、fixed233、m7 固定证书 NO_INVOKE 保留。 |
| `student_parity` | [完整 Parity trace 的小线性锥正尾](analysis/PARITY_UNBOUNDED_SMALL_CONE_AUTHOR.md) · [复核](review/PARITY_REVIEW.md) | 实际多项式支撑 p+q≤j−1 给出可计算 δ_m；(1+a+c)/(m(S+a))≤δ_m 时 Gap>0，因此全部正间隙路径 a+c=o(S) 最终适用。 | 固定 m；不推出所有 S、m 一致阈值、路径单调性或逐项系数正性。 |
| `native_brc` | [模二次读出的固定非自适应最少 probe 数](native/QUADRATIC_EVEN_PROBES.md) · [复核](review/NATIVE_REVIEW.md) | 在原有全 signed X6 chart、精确输出及全部平移未来语言下，K(1)=0，K(2)=1，K(4)=6，其余 m 的 K(m)=7。 | 允许空方案；不是完整 Cell 身份压缩，也不含自适应、噪声、混合模数或有界域最优。 |
| `cm_algebra` | [实际强完备化的非闭像及无限维代数余核](cm/CM24_STRONG_COMPLETION_NONCLOSED_RANGE.md) · [复核](formal/CM24_STRONG_COMPLETION_CROSS_REVIEW.md) | 对指定 p-adic 完备环及原 rank-two 连接，dim H⁰≤2，L 的像非闭，代数余核无限维；原 weak 六维余核比较不能满射。 | 以原 integral Frobenius rows 为继承接口；不决定 H⁰ 精确值、separated quotient、比较核或显式非像源。 |
| `cm_analytic` | [多端点 Hasse jets 的最优 trace decoder](cm/CM24_MULTIPOINT_TRACE_ENDPOINT_DECODER.md) · [复核](review/CM_REVIEW.md) | 在 p=6m+1、p≡13或19 mod24、D=Σd_i≤m 的指定载体上，用恰 D 个 F_p 外部线性标量重建全部目标 jets，给出最多三次扩域后的 trace 降回构造。 | 复用已有维数下界；a=0 保留 Laurent 偏移；不求实际 Y/Z/h_div/κ，也不覆盖 D>m。 |
| `number_theory` | [固定 prime-fiber 容量的非单调性与永久阈值](nt/prime_capacity_threshold.md) · [复核](review/NT_REVIEW.md) | 固定 S={2,3}, a=(0,0), L=2：C(27)=5、C(28)=4；C(H)=7 当且仅当 H∈[45,62] 或 H≥66。 | 继承 exact quotient 及原状态；永久阈值证明使用 Nagura 1952 的素数区间定理；不推出一般 S,a,L 结论。 |
| `t6_formal` | [signed moment completion 的耦合必要 cuts](analysis/T6_COUPLED_MOMENT_COMPLETION_CUTS_AUTHOR.md) · [复核](review/T6_MOMENT_REVIEW.md) | 由 M₀,…,M₆ 与两个非负预算构造 −C_hk B₊≤L_hk≤C_hk B₋；解析 cutoff≤49 后，21 个 scalar maxima 用 Fraction 精确求值。 | 21 个 cuts 是一个接口单元；仅必要条件，无实际 surviving class 筛除、无新 census、无全局 T6 闭合。 |
| `misc_formal` | [非反射线性载体：单 seed 模拟与流完成边界](formal/NONREFLECTIVE_LINEAR_BOUNDARY.md) · [复核](review/FORMAL_LINEAR_REVIEW.md) | 同一论文给出 single nonzero seed 的 pre-query gcd 模拟、已知完整有限生成表的有效反射，以及无完成标记的 streamed finite module 基数/支持不可统一终止求取边界。 | 单 seed/线性/精确 equality 与已知生成表或无完成标记三种域分别保留；不构造新的 factoring mechanism，不宣称通用定理新颖性。 |
| `brc_residual` | [既有 passive pulse 的等待时钟实际复用](native/BRC_PASSIVE_CLOCK_REUSE.md) · [复核](review/BRC_CLOCK_REUSE_REVIEW.md) | 复用 BRC-R-160 的 12-period pulse 与 Euler 等待变换：首次观测 τ=T₁₁，pgf=F¹¹；同均值 deterministic/geometric 时钟有不同响应，后者趋于 1/48 并有显式界。 | 继承 pulse 原 provisional 状态；时钟独立、每整数 tick 可观测且无跳过/反作用；不改进旧 adversarial skip 定理，不产生原生时钟。 |
| `cell_euler` | [固定 finite-layout U2 的 incidence prefix adapter](native/U2_INCIDENCE_ADAPTER.md) · [复核](review/U2_ADAPTER_REVIEW.md) | 显式 material/incoming incidence 下保留有标记 path/packet 叶及 source-target-incoming 读出，给出 W=Kᵀ；复用正质量 BRC 实现并执行有限验证。 | 固定 Cells、每 port 非空 distinct anchored three-axis triples、uniform packet 与等权三腿、0<ρ<1；不支付 G1–G5 或任意深度/非线性未来闭合。 |
| `euler_measurement` | [声明独立等待时钟的 held-state 接口与尾界](native/EULER_CLOCK_BRIDGE.md) · [复核](review/EULER_CLOCK_REVIEW.md) | iid 正整数等待且独立于整个 source edge 过程时，A(u)=(1−F(u))/(1−u) C(F(u))，联合 return-mark 为 R_h(F(u))；有限均值时同单元附录提供显式 tail/horizon 界。 | 状态在等待中保持；有界观察，F(0)=0；均值仅为均值/尾界所需条件；不允许 state-dependent waits 的简单替换，不等同 clock-duration parity 或物理校准。 |
| `supplement_number_theory` | [固定六 cell coupled payload 的精确 repair bits](nt/crt_repair_bits.md) · [复核](review/CRT_REPAIR_REVIEW.md) | 固定 N871 六 cell 支撑，已供 marginals+carry 时纤维 C=min(e,γ₁)−max(0,e−γ₄)+1；总质量 M 下最大 C=⌊M/2⌋+1，所需额外固定 bits 为 ⌈log₂ C⌉。 | 非负整数 payload 且 baseline 一致；全部 prefix 在相同固定支撑上。不是 unweighted QRWheel 内存、runtime/factoring 下界，baseline/取 t 成本另计。 |

## 复核与计数

四轮[复核台账](review/REVIEW_LEDGER.json)、[第二轮](review/REVIEW_LEDGER_ROUND2.json)、[第三轮](review/REVIEW_LEDGER_ROUND3.json)、[第四轮](review/REVIEW_LEDGER_ROUND4.json)共给出 **14 个稿件—报告绑定**：12 个服务单元的主稿，另含 Euler 同单元尾附录和跨线比较。CM 强完备化采用[独立交叉复核](formal/CM24_STRONG_COMPLETION_CROSS_REVIEW.md)，台账的再次读取不算第二张数学票。

复核者未参与所评新证明的构造，但共享项目控制背景并读取所声明来源；不标记为 clean-blind。报告均在各自冻结的新范围内未发现未解决缺陷或 must-fix；继承 Frobenius、原 quotient、pulse 等接口的状态与条件继续保留。没有运行 Lean 内核；作者和复核者的有限精确运行仅覆盖各日志所列范围。控制整理未重跑科学程序、未给数学票。

21 个 T6 cuts、formal 论文内三个接口、prime-capacity 的两个陈述和 CRT 的两个陈述均按各自**一个服务单元**记录。Euler 尾界为[同单元附录](native/EULER_CLOCK_TAIL_CERTIFICATE.md)。BRC 时钟成果为已有接口的实际复用应用。

## 另行记录的支持工作

- [RSA 原始先例核对](nt/rsa_prior_art_boundary.md)：核对 Pohlig–Hellman 原文中的 digit lifting；未完成整个 membership-or-factor 包装的 prior-art gate，不计新定理。
- [缺包查证记录](nt/line_dossier.json)：Gaussian Newton 证书、J1 r61–64 包、adaptive-third 完整证明仍有明确源缺口；未伪造已恢复或已验证。
- [跨线接口比较](nt/CROSS_LINE_CAPACITY_BOUNDARIES.md)及其[复核](review/CROSS_LINE_CAPACITY_REVIEW.md)：复用已有 finite-fiber/observer-safety 工具，保留 repair bits、限定 probes 与有效反射三条线的载体、观察语言及成本差异；不合并成新通用工具。

## 下一前沿

每类原作者保留的具体义务见 [FAIR_ROTATION_OUTCOMES.json](FAIR_ROTATION_OUTCOMES.json)。首轮覆盖不表示分类内每个问题均已推进或解决。先前已接受 census、PCF7 修正及历史大枚举不因本轮轮转重做。

Student 同阶缩放的第二轮新稿正在另行复核，**不在本次首轮冻结与统计中**；后续须用自己的不可变来源及审核绑定记录，不能倒填首轮状态。

## 来源核对

整理者重新核对 waves 1–5 的 99 份完整文件回读，得到 89 个去重后的有效路径；字节数、SHA256、Git blob 与相应发布参数一致。14 组主稿/报告散列与这些真实回读一致。数字包含登记与证据文件，不是科学成果数量。

[完整机器索引](RESULTS_INDEX.json)保留作者原始接口、适用条件、排除项、源 pins、复核者、台账和实际验证产物。父研究目标仍开放。
