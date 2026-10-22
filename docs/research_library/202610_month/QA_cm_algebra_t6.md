# CM 代数、T6 与 Dixon 补充的独立文献忠实性核对

固定源快照：`56f5938da3f707c1d9db1b39afde124eac4634e3`。核对日期：2026-10-22 UTC。

本报告是摘录与既有来源之间的文献核对，不是数学重证明、独立科学复现、正式 review 或新增票。核对者没有编写 CM/T6/Dixon 的这些摘录。没有执行、导入或复跑科学程序、旧 checker、有限枚举、comparator、样本或求解器；仅做文本文献读取、归档解码、JSON 关联与摘要比对。P11/misc 本人稿不纳入此独立 QA；EM4 三项 misc 新补录已交 library_routes 独立核对。

结论：在以下明确读集和抽查范围内，未发现阻塞合并的公式转录、假设遗漏、来源状态升级或全域化错误。一项本地阅读缓存的末尾换行差异已单独报告给作者及 Root；它不改变数学文本，且不能被当作原始 Source bytes 的直接同一性。

## 1. 读集与证据强度

- 完整读取 `cm_algebra.json`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/cm_algebra.json`） 的 48 个条目，包括每条 hypotheses、formulas、conclusion、limits、status，以及全卷共同定义、开放边界和复用接口。
- 完整读取 `t6_formal.json`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/t6_formal.json`） 的 8 个条目、q1–q4 子结果、原始 RR/DR 状态字段和计数限制。
- CM 来源按高风险载体与新旧作用域分组抽查，使用既有合法 Source 缓存。没有声称重新完整阅读全部 119 个来源，也没有为每条 lemma 新造证书。
- T6 使用五个现有 `t6_*_source_cache.json`、`t6_static_members.json` 与原 Joukowski capsule 缓存，读取所选 proof/review 正文或有关段落。91 个 Source 缓存的原 bytes/sha/blob 与其 registry 全部吻合。8 组现有 RR→DR 目标与真实 review prose 的摘要绑定全部吻合：7 个 `ACCEPTED/terminal=true`，原全局部分进展为 `RETURN_TO_OWNER/terminal=false`。这是已有记录绑定核对，不是新增接受。明细见 `t6_documentary_pin_checks.json`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/qa_cm_t6_sources/t6_documentary_pin_checks.json`）。
- H0P 以实际 RR、DR 和 Driver 全文核对：`RR-D0D2E8489B7EC4AE9AB4` 对应 `DR-2ADE175464F69B245539`，现有 disposition 为 `ACCEPTED`、terminal true、destination NONE；实际 RR/prose 摘要均吻合原 Source 内容。

## 2. CM 48 条的主要核对点

| 条目 | 核对的高风险边界 | 来源抽查与判断 |
|---|---|---|
| CM-ALG-01–06 | 六维余核、指定 φ、任意完美剩余域与 σ | p10/r30 的六观察、实际 weak passage 和定量损失相符；有理正规形的唯一性有独立来源说明，没有被当作该篇已证明 weak primitive 唯一性。p17/r17 的条件是完整有限常数域塔 `C_beta(k)`，不是“k 无限”或“k 完美”即成立。指定 φ 与实际 canonical M、transpose、1-form derivative 和系数 σ 均保留。 |
| CM-ALG-07–12 | finite differential、strict φ、同一个 T、一般链映射的区别 | p12 的实际 strict 两个 degree 条件是整个 finite chain algebra 为 `Q_p I` 的前提；不假设 φ 在 weak 环上满射。非 strict 类别中的非零同伦边界、affine/free 子群没有与 strict 零核混淆。rank3 提升明确要求固定 kernel/quotient 与实际类方程。 |
| CM-ALG-13–19 | integral `R0`、p-inverted weak `R`、rational `K(r)` 与 char p | 不同源中 `R0` 符号按条目重新定型：CM-ALG-01 用 `A_alg` 避免和 integral `R0` 混同。integral torsion、两两不同格、generic p-curvature coarse invariant，与 rational rank4 的不分裂/PV/centralizer 结论分别保留。r13 的任意常数域扩张及有限代数 cover 量词与条目相符；未扩成任意 differential/analytic 扩张。 |
| CM-ALG-20–26 | completion/weak membership、固定 full matrix no-go、raw/log lift | p05 固定原 integral lift、指定 weak 环和 θ 的全部 `GL4` no-go，没有扩成几何 Frobenius 总不存。p26 的 conductor 是每个有限非约化层的 base-changed normalization；r04 的 node obstruction 仅固定 p=13、原 whole-`R_n` central map、unit representative，未扩成所有 split primes或所有 crystalline representations。条件 global F 的 translation/格界没有被当作 F 的存在证明。 |
| CM-ALG-27–36 | finite-level → H¹ → all-PD → named towers → trace/cup 的阶段区别 | extra11 的 matched HK specialization 仅证明有限层 derived 箭头，未偷加 H¹ base change/Rlim；r25 的后续 all-PD 与两个命名 derived towers 是另一个有来源的扩展，不等于所有独立 formal sites 同一。finite rings 不能先倒置 p。p=13 node 反例不被当作 LC 为假。conditional sign 与 actual proper witness、full-relative/functional 仍分开。 |
| HODGE-GEO-01/02 | 完整 object obstruction 与候选 family 的有限修改 no-go | extra16 的 dim≥3、dual numbers、finite/nonreduced D 与 perfect-lift 类型均保留。rank6 是固定 non-split Weil special fiber/diagonal family 的 `im Omega_D`，不是统一全部 Ext² 基。现有正式接受只满足 Task 的负替代，不解 Hodge conjecture、不排除 family 外对象或母问题。 |
| CM-ALG-37–46 | actual geometry 与人工 Legendre、有限 p² 参数、raw/σ correction、未知 κ | g02 的 char0 operator 差异、g06 的同一个 ε 与 Q full connection 的 `s^{-1}` 限制均保留。第四 entry 的有限递推未被写成已运行数值；embedded06_00/02 明确还没有 ambient jet、完整 period、divided response 或 whole Y/Z/κ。条目没有把有限 recurrence 重命名为已支付 κ。 |

代表来源的本地阅读路径包括 `cm_algebra_sources/primary10.md`、`review30.md`、`primary17.md`、`review17.md`、`primary19.md`、`primary12.md`、`primary05.md`、`review13.md`、`primary26.md`、`review04.md`、`extra11.md`、`review25.md`、`extra16.md`、`extra17.md`、`root4_member0.md`、`root6_member2.md`、`embedded06_00.md`、`embedded06_02.md`。精确公共固定链接及各自 blob 由 `source_manifest.json`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/cm_algebra_sources/source_manifest.json`） 的 p/r/x/g 来源 ID 保留。

## 3. T6 8 条的主要核对点

| 项 | 已对齐的来源内容与限制 |
|---|---|
| 原 p19/q0 进展 | `T6S024` 与现有 DR 明确保留原 `PARTIAL_PROGRESS_GLOBAL_T6_OPEN` 和 `RETURN_TO_OWNER`。旧 p19 70,285,694 是作者历史 campaign 计数，不变成这次独立穷举；全局 T6=2332 仍 OPEN。 |
| q1 | `T6S057`：16 required rows，12 admissible EMPTY，r=2,6,12,14 为 OUTSIDE 而非 relaxation-empty；299 named paths/1490 coordinate decisions，0 sphere leaves，不虚构叶预算检查。 |
| q2–q4 | q2 为272=154+118；q3 为3264=1405+1859；q4 为30992=10212+20780，后两项是 admissible/outside 的实际 literal 分类。`T6S054/S028` 的 q4 canonical representative、两子分支、严格 `>` norm prune、等号保留及 whole EOF 均与摘录相符。0 full leaf 不写成做过 leaf-vector/congruence/budget tests。 |
| branch/cost 上界 | `T6M067/M066` 明确 primitive budget bound15 和 maximal-prime admissible bound14 是不同量词；order15 outside 不能据此改为 EMPTY。半/四分之一半径、398/299 等是结构/条件上界，不是已完成向量数或全域执行成绩。 |
| portable DFS | `T6M059` 与实际 q4 proof 的证书规则相符；中断/缺失/额外字节是不验证，不是 EMPTY。原 q3 particular/旧投影不能用新 canonical 规则重解释。 |
| U2 | 条目保留 coherent H、正 degree、component 内 degree 恒定的准确范围；单布局 row-sum 补偿和 source-blind aggregate 更弱，未偷换为全部 row 必须1。G1–G5 与 occupancy successor 仍 UNKNOWN；固定 field 的唯一性不是动态材料后继唯一性。 |
| HJ 六行与 J1 | `T6S025` 的旧 J1 是 good-prime scoped；proper prime powers 需 char∤2s 的背景条件，不能只看整数 q∤2s。literal central residue SET 与普通区间长度、平方特征与 prime Legendre 已分开。旧 publisher403 保留，不称本次独立完整全文检验。 |
| q=2s−3 | `T6S026` 明确 s≥5 odd INTEGER、q prime、literal J_s，iff(5,7)。六输入表是历史支持，不是本次运行。没有扩到任意 prime powers、任意同大小对称集合、全部 offsets 或新的 native/共同 provenance 定理。 |

所选 T6 正文缓存见 `qa_cm_t6_sources`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/qa_cm_t6_sources`）。这些是普通文献阅读副本及关联核对，不是新的科学证书。

## 4. Dixon R1/R2/R3 与 full-nine-jet 快核对

读取 `cm_analytic_four_supplements.json`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/cm_analytic_four_supplements.json`） 全部4项；对照三个固定 JSON 的完整 `report` 字段（5362、8879、7486 字符）及4137B fulljet Markdown 全文。未执行其中 `checker`、`checks` 或 `verification` 程序。

| 新项 | 文献忠实性核对 |
|---|---|
| CM-AN-DIXON-NORMAL-P3 | 所有 p=6m+1≥7 的有限有理代数域及 p-unit 分母保留。`S−C=pN/3+p²K/18 mod p³`、normal-subtracted quotient 与 least-representative carry 是不同观察，p13 的 carry3+curvature11→second1 未漏掉。原28素数 checks 是历史支持，不是全素数数值证明或独立 review。 |
| CM-AN-DIXON-MIXED-PATH | `N′=F_ad+K`、`C″=F_aa+2F_ad+K`、完整 `γN` 二阶路径端口与 `βN+pR=0 mod p²` 条件均保留。β=0 不会自动消去 γN；β=−2α 只消某 standalone K 项，不能删除 F_ad。 |
| CM-AN-DIXON-BIDIRECTIONAL | exact values 定义的 E 可满足 mod p² 恒等式，但从 source values mod p³ 实际只能抽出 E mod p；E mod p² 需 values mod p⁴。generic `G(x)=px−3x²` 的单侧核只在 generic rational-jet carrier上，不声称 fixed hypergeometric family 内存在同值两成员。 |
| CM-AN-D25-HIGHBAND-NINEJET | 完整9×9矩阵逐行与原稿吻合；p19 rank9/det6、左上7×7 rank6、需要第9 branch 的 prefix failure均在有限 p19 域。九个 prime 的历史 checks 不提升成 all-prime determinant 非零。exact endpoint operation 与 combined presentation jets 保留；完整 B11→LOW transport 不由此否定。 |

四项均保留 `UNREVIEWED / NOT_ADMITTED`、无正式 Task claim 和无独立数学审核的来源状态。原作者独立计算实现不是独立 peer/Native review；未知 LOW/Beta 真实参数路径与终点 residual 不被默认为已解。

## 5. 缓存格式发现与处理

初次归档摘要检查发现，CM 的110个可直接映射 primary/review/extra/root 阅读副本均比 Source 正文多末尾一个 LF。逐项恰去掉这一个已证实的额外 LF 后，110/110 对应 blob 与固定 Source registry 吻合。例：`primary10.md` 为9902B的阅读副本，原 Source 为9901B、blob `06a9fc065e334f4974bb43f0cd978502613c542a`。

这不是数学内容变化，也没有据此重写固定 Source pins。已通知作者和 Root：阅读副本应明确标为 derived copy，或以已验证的方式消除额外 LF，不能直接声称带附加换行的本地 bytes 就是 raw exact Source。`x18` 经作者提供新的完整合法 connector receipt，确为真实独立公开路径 `reviews/lc_primary_support/SUPPORT.md`，不是虚构的 capsule member 路径；原疑点已排除。receipt 为 `x18_connector_capture.json`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/cm_algebra_sources/x18_connector_capture.json`）。

该格式发现不增加或撤销任何数学审核。除这项已通知的归档表述/副本格式问题外，本次限定 QA 未发现阻塞性文献修正。没有重新作出任何数学 PASS、正式票、Foundation/Working Truth 或父目标完成判断。
