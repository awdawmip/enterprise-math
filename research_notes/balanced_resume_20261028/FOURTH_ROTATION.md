# 第四轮：固定递推、记号补充与经典工具复用

2026-10-28。本入口摘录三项冻结结果及其非作者审核，不提供 Owner 数学票、正式 Driver 接受或 Lean 证明。精确版本、散列和前提见[机器索引](FOURTH_ROTATION.json)。第三轮及原 435 条文献保持历史冻结；根研究目标 OPEN，正式任务实时状态 UNKNOWN。

| 单元 | 本轮推进 | 不随之解决 |
| --- | --- | --- |
| CM24 固定递推 | 对全部 k≥1，`v_p(a_(p^k))=−k`；原分离商的 5/6 二分选定为 5 | 实际像成员资格、强水平核维数、κ/Y/Z |
| C34 | 显式补齐 raw / centered 定义和选择坐标维数，非参与者审核无待修项 | 实际独立性证据、有限样本、合法最小二元实现 |
| FREE 原生有限邻接 | 完整计数与等号分类；通过保真编码复用 Simon 引理 | 新公理、新工具族、动力学或物理稳定性 |

## CM24：一项算术定理及其固定载体推论

[全文](cm/round4/CM24_P_POWER_INDEX_VALUATIONS_AND_SEPARATED_DIMENSION.md)与[接口](cm/round4/ROUND4_INTERFACE.json)固定 `a0=0,a1=1,a[-1]=a[-2]=0` 和递推

`4(j+1)(j+2)a[j+2]=(5j(j+1)+2)a[j]−j(j−1)a[j−2]`。

对素数 `p≡13,19 (mod 24)`、归一化 `v_p(p)=1`，证明 `v_p(a_(p^k))=−k` 对每个 k≥1 成立。可复用的计算接口是 `U=1−3z²/4` 与
`A(z)=z U^(−2/3) ₂F₁(1/3,5/6;7/6;z⁶/(16U²))`。
令 `n_k=(p^k−1)/6`，超几何系数在 n_k 的 valuation 为 −k，先前系数均至少 −(k−1)；整系数代入使目标系数具有唯一最低 valuation 项，排除相消。

在[第二轮](cm/round2/CM24_SEPARATED_QUOTIENT_FIVE_SURVIVORS.md)完全相同的非分歧 DVR、强完备化、连接与 infinity 归一化下，这支付原递推有界性义务：`dim_K X/closure(L(X))=5`，weak 六类到分离商的核为 `K[(r,0)]`。同时有范数不超过 `p^(−k)` 的显式逼近。这是一项算术结果加既有接口的推论，不能拆作多项新发现；原“5 或 6”文稿保持不改。

[analysis 审核](analysis/round4/CM_RECURRENCE_INDEPENDENT_REVIEW.md)与[formal 审核](formal/round4/CM24_P_POWER_VALUATION_PAPER_REVIEW.md)由两位非作者各自冻结后再比较，均无 must-fix、未贡献必要补桥。作者的三项有理恒等式零残差检查仅补充纸面证明，没有 prime/recurrence 样本外推；审核者未运行该 checker。实际 `(r,0)∈L(X)`、强水平核、非 Hausdorff 部分分类及 κ/Y/Z 仍未付。分离商五维不是原生空间维数。

## C34：支付精确记号义务，保留条件

[补充稿](formal/round4/C34_CENTERED_COVARIANCE_SUPPLEMENT.md)、[接口](formal/round4/C34_CENTERED_COVARIANCE_INTERFACE.json)及[NT 非参与审核](nt/round4/C34_SUPPLEMENT_CROSS_REVIEW.md)把三路读出中不同统计量明确分开。对选择 q 个不同原坐标的 H，`v=Hm`、`Gamma_l=H C_l H^T`，

`R_l^(rs)=D_r(Gamma_l+vv^T)D_s`，
`G_l^(rs)=R_l^(rs)−mu_r mu_s^T=D_r Gamma_l D_s`。

同刻同坐标的校准 g 来自 **raw R0**，不能改用 G0；正 bias 用正平方根恢复。全过程独立、准确平稳总体矩、无扰动且对齐的读出仍是前提。`C_l=A^l Sigma` 是额外的继承模型输入，不由校准一致性推出。

第三轮 `VALID_WITH_REQUIRED_NOTATION_SUPPLEMENT` 是原短稿的真实历史；本轮另有署名补充及非参与者审核，支付该精确缺口，未追认旧原稿已经定义完整。原 finding 的作者也是补充作者，因此该旧报告不是补充稿的独立审核票。实际仪器独立性、有限样本、合法最小二元实现、原始计算与登记历史均未被此次补充解决。

## FREE：原生有限集中的标准复用

[原始证明](free_round4/phase_a/phase_a_candidate.md)研究固定 signed Z6 Cell 的静态、有限、非空诱导子集：若每点至少有 k 个内部单位轴邻居，则存在性恰为 `0≤k≤6`，`|S|≥2^k`；等号恰为 k 条不同原生轴上的平移单位盒。k=6 得 64 个 Cell；k≥7 不可能有限支撑。未选轴仍保留固定坐标，没有原生平面或降维本体。

[Phase B](free_round4/phase_b/phase_b_report.md)将有限坐标区间编码为 prefix-one 位串，精确保留 `Hamming distance=Σ|x_i−y_i|`，从而保留邻接、度数与集合大小；等号子立方体在每个轴块中至多有一个自由位。由此实际复用 Ambainis–Vihrovs `arXiv:1406.0073v3` §3 的 Simon 引理及等号分类。分类为 **DERIVED_NOT_AXIOM / STANDARD_COMPOSE / RESULT_ONLY**；关闭本候选的新机制方向，不自动续题。

[原证明审核](review/round4/FREE_MIN_DEGREE_PAPER_REVIEW.md)和[Phase B 审核](review/round4/FREE_MIN_DEGREE_PHASE_B_DISPOSITION.md)由同一非作者分两范围完成，不能计作两位审核者。T7 实际处理 64 个轴子集及 720 个置换；766 个有限子集与 64 个构造只提供补充检查，非无界证明。Phase A 保留 `ANCHOR_EXPOSED`；两个外部原始 web 响应仅在本地，[来源索引](free_round4/phase_b/source_refs.json)及[发表边界](free_round4/phase_b/PUBLICATION_BOUNDARY.json)已入 Source，不声称原始响应已发布。

既有五项方法入口仅追加这些精确来源。上述公式按其完整假设复用；不增加工具族或改变旧数学状态。
