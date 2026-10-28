# 2026-10-28 第二轮研究前沿与证据边界

本页按不可变来源 `d1a8bb0db86016afa72b546f31142de071facec7` 整合第二轮成果。四项分别是同一成果链的加强、未决二分判别、既有工具的有界应用、补充静态审核，不能合计为四个新定理或正式接受结果。[首轮索引](RESULTS_INDEX.md)和 12 类／12 服务单元统计保持冻结，原月库 435 条文献计数不变。

以下数学陈述摘自作者完整接口；论文级复核按精确稿件散列绑定。创建时的 `PENDING` 字段保留其历史，后续审核作为另一个有来源的事实记录。当前正式 Task／owner 状态仍为 `UNKNOWN`；没有 Driver 接受、Task 完成、Working Truth、Foundation 晋升或新工具族。

## Student／Parity：同一尾部成果链推进到全部正第二间隙

对每个固定整数 `m≥2`，在原完整 signed secant trace 的同一规范化下，存在可计算有理数 `R_m≥1`，与 `S,a,c` 无关。若 `S≥0,a>0,c>0` 且 `S+a≥R_m/m`，则

$$
\operatorname{Gap}\ge\frac{m-1}{4}\left[\left(1+\frac{c}{S+a}\right)^{m+1}-1\right]
\ge\frac{(m^2-1)c}{4(S+a)}>0.
$$

这里不再限制 `c/(S+a)` 上界，也不要求正间隙有统一下界。最小输入是[最终完整证明](analysis/PARITY_FULL_TRACE_ALL_SECOND_GAPS_SUM_TAIL_AUTHOR.md)与[接口](analysis/PARITY_ALL_SECOND_GAPS_SUM_TAIL_INTERFACE.json)，以及其明确继承的[有界相对间隙证明](analysis/PARITY_FULL_TRACE_BOUNDED_RELATIVE_GAP_TAIL_AUTHOR.md)和原 centered metric。共同输入中心、共同 signature、完整 cross-parity 扰动和小比值精确因子都必须保留。

前一小锥、随后有界相对间隙、最终全部正第二间隙是同一链的嵌套范围，不重复计三个发现。`R_m` 未作数值求值；紧总尺度区域 `S+a<R_m/m`、`m` 一致阈值、逐项 P1／更高面正性及全部母目标仍开放。

[主要非作者复核](review/PARITY_ALL_SECOND_GAPS_REVIEW.md)和[另一位非作者交叉复核](formal/round2/PARITY_ALL_SECOND_GAPS_CROSS_REVIEW.md)分别在明确继承接口下报告没有未解决缺陷／must-fix。它们是纸面审核，没有科学扫描或 Lean 内核运行。

## CM：分离余核为 5 或 6，准确分支尚未决定

对象固定为原 `p≡13或19 mod24` 的 complete unramified DVR、指定 rank-two 连接及 `O[r,(1-r²)⁻¹,(4r²−1)⁻¹]` 的 p-adic 完备化再逆转 p。通过实际 integral partial-fraction lattice、有限 residue 的选定 integral column 及规范化 infinity Frobenius，原六个 weak 类满射到分离余核；以下五类仍独立：

$$
(1,0)dr,\quad(1/(r-1),0)dr,\quad(1/(r+1),0)dr,\quad
(1/(r-1/2),0)dr,\quad(1/(r+1/2),0)dr.
$$

第六类 `(r,0)dr` 的存活等价于原有理递推的全部系数在 p-adic 范数下有界：

$$
a_{j+2}=\frac{(5j(j+1)+2)a_j-j(j-1)a_{j-2}}{4(j+1)(j+2)},
\qquad a_0=0,\ a_1=1,\ a_{-1}=a_{-2}=0.
$$

有界时维数为 6，weak 比较为同构；无界时维数为 5，比较核是该 `r` 类的一维张成。**本轮没有判定递推属于哪一支**，有限样本不能代替全指标结论。无界分支只给 `r` 属于像的闭包，未证明它属于像；strong horizontal kernel 的精确维数、Y/Z/κ 等仍未解决。首轮无限维的是代数余核，本轮有限维的是其分离商，二者不混同。

最小输入见[完整证明](cm/round2/CM24_SEPARATED_QUOTIENT_FIVE_SURVIVORS.md)、[精确接口](cm/round2/ROUND2_INTERFACE.json)、[范围冻结](cm/round2/SCOPE_FREEZE.json)及首轮 strong 结果。两份[主要复核](review/CM_SEPARATED_QUOTIENT_REVIEW.md)／[交叉复核](formal/round2/CM24_SEPARATED_QUOTIENT_CROSS_REVIEW.md)在原 normal-form 与 Frobenius 接口下未发现 must-fix，并均保留 5／6 未决。

## FREE：查重归入既有 T0/T6 的精确回返计数应用

[Phase A 原始冻结](free/phase_a/phase_a_candidate.md)只观察从选定真实 Cell 出发、十二 signed-unit 输入词下的当前及所有未来前缀回返。`H` 固定，外部步数时钟可供读出和更新，但不能偷存历史；成本只计运行时内部字母表，代码表、更新规则及该外部时钟不计入。

其保留的具体应用公式是

$$
M(H)=C_6(\lfloor H/2\rfloor),\quad
C_6(r)=\sum_{j=0}^{\min(5,r)}\binom5j\binom{r-j+6}{6},
\qquad \text{bits}=\lceil\log_2M(H)\rceil.
$$

[Phase B 查重](free/phase_b/phase_b_audit.md)确认 near/FAR 商、区分词、递减 horizon 的安全更新已由 `t0.brc_finite_horizon_contact`／T6 覆盖。准确处置是 `DERIVED_NOT_AXIOM / BOUNDED_APPLICATION / RESULT_ONLY`：保留对恰步长可达奇偶总体的计数及 clock 成本实例；核心机制按已知复用，不注册新公理、工具或后继线。精确峰值公式的外部优先权为 `UNKNOWN / NOT_CLAIMED`。T0/T6 的[实际有限复用记录](free/phase_b/phase_b_reuse_check_output.json)覆盖 `H=0,…,5`，不代替普遍证明。

[固定 alphabet 补桥](free/post_freeze/clock_alphabet_clarification.md)由审稿者 `EM-REVIEW-58D6A2` 请求并提供提纲，作者在冻结后另写。因此该审稿者对这一贡献的检查不算独立票。另一未参与者 `EM-DIRECT-099801` 给出[独立补桥复核](formal/round2/FREE_EXTERNAL_CLOCK_ALPHABET_CROSS_REVIEW.md)，只审核原合同下的编码桥。完整[后续复用处置](review/FREE_RETURN_REUSE_DISPOSITION.md)保留这些署名与边界，不追认 clean-blind 身份。

此处 `Θ(H⁶)` 是状态数、`Θ(log H)` 是 bits；不能与另一 visited-set 问题的 `Θ(H⁶)` bits 混合。计入 clock／code table／workspace 的模型、物理记忆律和完整 Cell 状态压缩均未给出。

## OAI7-090：有限证书的静态覆盖审核及一次未绑定执行记录

[作者静态审计](native/round2/OAI090_FINITE_COVERAGE_AUDIT.md)与[覆盖表](native/round2/OAI090_PROOF_COVERAGE.json)针对 `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a` 的固定原 checker：blob `23768a5c2d88e100399bb5c4347447e86a7160cb`，TeX blob `dad316cc2ad861a7482d79b46b6f840ed83d2a5e`。外部模型是 Euclidean R² 与 two-body potentials，未提供原生 X6 读出桥。

已将五组有限引理对应到实际代码，并局部核对固定 sqrt 调用域、wave decay／jet monotonicity、参数 polytope 与 Bernstein 下界条件。[非作者审核](review/OAI090_STATIC_COVERAGE_REVIEW.md)阅读完整 389 行 checker 和所列 TeX 部分，在这一静态及局部前提范围内未发现不匹配；没有审核完整 universal-optimality 证明，也没有再次执行 checker。

流程事实必须一并保留：作者曾在正式 claim／runtime 未绑定时运行原 checker **一次**，实际 exit code 为 0、stdout/stderr 均为空，记录见[原执行票据](native/round2/ORIGINAL_RUN_RECEIPT.json)与[NO_RETROACTIVE_AUTHORIZATION](native/round2/NO_RETROACTIVE_AUTHORIZATION.json)。该执行与已有 `RS-OAI7-090-A-20261007-6F2A81` 范围重叠，live owner 未知；后续活动登记、静态复核和归档不能倒推执行授权，不能将它记成正式 Task 完成、RR 或数学接受。后续工作已限定为静态对应与局部前提分析。

谱恒等式、无限系统／Schur tail、连续曲率极值、全径向符号及能量迁移等仍在未审核范围。下一个最小义务是经正确归属后审核连续曲率极值及 raw bounds 的迁移，不需为该纸面问题重跑 checker。本项计 **0 个新定理、0 个新工具族**。

## 审核账册与来源

[Round 5](review/REVIEW_LEDGER_ROUND5.json)、[Round 6](review/REVIEW_LEDGER_ROUND6.json)、[Round 7](review/REVIEW_LEDGER_ROUND7.json)、[Round 8](review/REVIEW_LEDGER_ROUND8.json)新增 9 个精确稿—审绑定；与首轮合计 23 个绑定。绑定数不是独立发现数，同一报告被台账再次读取不增加数学票。[机器索引](SECOND_ROTATION.json)保留完整作者接口、原依赖、署名贡献、执行异常、未付义务与源 pins。

文献整合重新核对截至 wave9 的 172 份完整回读、154 个去重有效路径以及全部绑定；不运行科学程序、不作新数学审核、不改正式状态。首轮文件与计数均保持冻结，父研究目标仍开放。
