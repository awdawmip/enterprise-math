# 数论补卷独立文献忠实性核对

核对对象为 `supplement_number_theory.md/json` 与 `supplement_number_theory_coverage.json` 的最终14单元稿。统一 Source 固定在 `56f5938da3f707c1d9db1b39afde124eac4634e3`；当前稿列18个物理 Source。结论：下列已指出的文献转录修项均已回读关闭，所核范围没有未处理的 blocking 文献问题。此结论只指来源、假设、公式转录、作者和证据等级的一致性，不是数学证明评审、准入投票或新的 theorem PASS。

本核对者不是该补卷作者；数论57主卷为本核对者先前整理，故本报告只独立检查另一代理撰写的14单元补卷及其引用的旧复用边界，不自审57主卷。Euler25卷由另一代理独立核对，见 `QA_new_sources.md`，不由本报告自审。Root另派 Native 核对新增 Cauchy/reflection 两项，其范围不在本报告。

## 实际阅读和方法

逐一静态阅读全文：14单元对应primary；CRT affine、actual dictionary、joint carry、修正版offline batch的实际nonauthor review；RSA dyadic完整primary、main review、thin-subgroup/cost subreview；matched-cost完整primary及共享peer中§3成本/§4澄清。另读offline batch正式erratum与旧已发布版本的替换范围。所有原稿和review使用既有固定Source缓存及已解包文本，没有新外部检索或全树扫描。

J1 mod3的232356B decimal certificate仅检查schema、author/status、seed/U/range等metadata与伴随文档的绑定声明；没有重新检查75指数、300 triples或执行其verifier。本报告不宣称177个支持成员全做数学审查，也没有重新验算大整数见证、旧raw数据或科学table。

源原字节与56f tree OID的administrative绑定沿作者/全局来源审计复用；本核对没有逐lemma重复hash，没有用新的connector读取冒充已有缓存的新Source证据。没有科学执行、样本、checker、benchmark、proof、数学票、远程mutation或新工具注册。

## 已关闭的文献修项

1. `NT-SUP-CRT-DICTIONARY` 与 `NT-SUP-CRT-BATCH-CORRECTED` 的自足hypotheses原只写“coprime extension”，容易仅理解为u与v互素。已按primary/review明确补为 `gcd(u,v)=gcd(N,v)=1`，并明写旧selected primes皆coprime N。这样与 `D≠0` 及 `(v+χ(N))/2` 的来源输入域一致。没有改结论或补证明。
2. Gaussian原文的独立corollary已补到检索formula字段：所有odd m≥23的首六fixed-m residual（y=0..5）严格增加；m≥31用wedge，m=23/25/27/29用原positive-mass cyclic recurrence的例外处理。仍标 `SOURCE_REPORTED_AUTHOR_ONLY`，未取得完整大证书的gap保持。
3. 14单元已加 `author_credit` 检索字段，与primary/review开头一致。特别保留CRT dictionary辅助作者UNKNOWN、RSA dyadic作者及两reviewer UNKNOWN/DIRECTED_NONBLIND，不将原owner、Root或旧RSA作者移作所有新推导作者。它们原来已在全文引文里披露，此次只是恢复可检索归属。

## 逐单元对照结果

| 单元 | 实际核对的主要内容 | 文献结论及边界 |
| --- | --- | --- |
| `NT-SUP-CRT-AFFINE` | `x=a+c+ut`、`s_a=(a+c)/u`、`D=4N/u²`、`T_a=V_D−s_a`；zero-inclusive indicator与D=0分支；半开cyclic rank | 同固定proved odd prime、affine输入才适用；D≠0 count `(v+χ(D))/2` 和D=0 count v均忠实。Root作者及原owner FB83AB分开；nonauthor directed NONBLIND paper PASS不是Native接受。 |
| `NT-SUP-CRT-DICTIONARY` | 保存的`(c0+k)²−N` predicate、必要候选坐标翻倍、`D=N/u²`、canonical row和两种carry | 不把`4N/u²`错误代入真实saved sieve；整数半开h与inclusive K转换正确；u=1无inverse mod1；新rank字典不声称旧code已经实现。 |
| `NT-SUP-CRT-CARRY` | 871/889两个真实full-product摘要碰撞；另行扩大payload输入的六cell碰撞；rational-linear repair维数 | 区分“少量numerical summary缺N/predicate”与“全marginals+carry但arbitrary payload”两个scope。`(r−1)(c−1)−δ`、有限cut维数、六cell修复、m组扩展均对照原文；未冒充bit/空间lower bound或旧全product算法错误。 |
| `NT-SUP-CRT-BATCH-CORRECTED` | no-tag two-pass、J≤min(v−1,r(Q+1))、row wrap、work/space、正式width erratum与替换review | 当前用 `(J+Q+1)B=o(v log M)`，只uniform B-slot comparator才有Θ(vB)。旧85fd paper/720c review是已发布历史，没有抹除。完整A、prime/root、provenance和output费用不免费；只offline空间/重算tradeoff，无strict total-work或factor gain。 |
| `NT-SUP-GAUSSIAN-WEDGE160` | 五port有序word生成式、全部alias的K、transfer、alias-free P_y、Newton wedge和non-real-rooted falsifier | 保留finite y≤160 / infinite odd m≥4y+11与folded region边界；首六corollary已恢复。190序列有限观察不升级全y/m theorem；1.18MB Newton证书原文明确not yet Source-published，未声称现已取得。 |
| `NT-SUP-J1-R61-64` | 原始输入重数E的二次判别式公式；r61–64四个odd-size square-witness报告 | q/s/k输入域及非output-set语义保持；E≥4依完整distinct index、square product与q非整除证书。count/maxj/divisor/digits只为作者历史摘要，不当完整证书；ZIP缺口保持。 |
| `NT-SUP-J1-MOD3-PELL` | r≥34且r≡1mod3；U=69698、m(r)、三kernel seed、norm multiplier、normalization和disjointness | E≥4m(r)、r70/100/130/196示例与even r≡4mod6子族一致；未扩大为全r。full certificate当前Source存在，但本文只元数据静态读，未重算triples；未接管原live owner。 |
| `NT-SUP-ADAPTIVE-THIRD` | 1161B portable checkpoint的7条reported frontier及remaining carrier | H/Q2边界求和仍未闭合；H,D,q_i,Q_i完整定义/证明未恢复，所以保持reported/unreviewed/source gap，未把七行标题补造成完整一般定理。 |
| `NT-SUP-RSA-DYADIC` | 非空valid unit transcript、odd stripping、max-depth supplied base、逐bit invariant、graph iff、thin subgroup与完整binary cost | n=pq distinct odd假设不由verifier认证；不生成collisions。t=0/空输入守卫、gcd proper范围、core squaring vs prototype assertions/cache成本都保留。两local review的UNKNOWN身份与DIRECTED_NONBLIND披露正确；historical finite checks未重跑。 |
| `NT-SUP-MATCHED-COST-INTERVAL` | K24 abstract label模型、预算内相同记录、成本和差/ratio、interval与covariance identities；peer§3/§4 | -91/24、271/24及384/475、696/425按原文；权1/2只缩放sum差不改符号。先除zero-weight、finite lower/possibly infinite upper、finite proper completions与inf/sup避免∞−∞；interval tight只在product信息模型，真实coupling仅safe外界。未声称真实Hart算术实现两表。 |
| `NT-SUP-RSA-ANTECEDENT` | 十月Driver报告内的八月冻结return、uniform full-group failure、lcm和graph barrier、aggregate law | `(4^m+2)/(3·2^(A+B))`及aggregate式按原文；uniform full units不与even-order/thin subgroup混淆。已额外全文读取actual DR-EA5EFB3177111D8A8A44与2037B RR，并确认DR结果SHA、report SHA/blob绑定；现可文献标注既存ACCEPTED/terminal/FOLLOWUP_TASK。只限旧extraction Task，不推出followup完成、母目标关闭或新dyadic接受；旧census不重命名十月新研究。 |
| `NT-SUP-HART-NEAR-CAP` | near-ratio p<q<2p的A0/16 inclusive offset证明、properfactor与public fee作用域 | 精确与旧ratio256/Hart480条分开，只提一次；Near40/Near48同字节载体不重复count。CENSOR后不声称已执行完coverage，小cap不推出实测优势；实际作者1F8B9B与Root明确direction保留。 |
| `NT-SUP-R004-PPRIMARY-PROFILE` | Sep30 checkpoint的finite module D_H、restriction surjection、c_j profile与Δ | 只按源载sum及layer monotonicity；old非sub/supermodular反例正文未恢复，所以只reported boundary。profile不自动证明future sufficiency或embedding/provenance可删；必要早源日期不伪写十月新证明。 |
| `NT-SUP-J1-INTERVAL-SCOPE` | 新增J1 source-comparison negative全文；外部阅读层级及d2 cutoff、H=s/s−1与surviving full-image规模 | 原文继承image cardinality，非重证；`H≤p^(2/19)`与p≥7 surviving interval域不交的陈述、p7/p≥11分支均忠实。Merai–Shparlinski仅原作者所报Cor1.2/图页阅读；另三篇为intro/abstract等不同层级，Bergman仍ABSTRACT_ONLY。本次未新外取全文或宣告无全库antecedent/六行audit完成。 |

## 状态、作者与复用核对

CRT affine与actual dictionary的helper/Root归属、CRT carry/batch的EM-CRTJC-5F30D8A2与nonauthor EM-NONAUTHOR-5DF3A9B6、near-cap的EM-SEMIPRIME-1F8B9B、R004的EM-DIRECT-B74C91、adaptive的EM-DVR-A5A686均依源保留。RSA原冻结作者EM-RSACOL-C76042、十月报告EM-DVR-FBF223与新dyadic UNKNOWN作者/UNKNOWN reviewers分开，没有用旧identity给新稿授予能力。

数论57主库的ordinary-QR character stream与本补卷shifted-square preimage不是同一predicate；accepted完整CRT child/旧full-list paid obstruction只是继承输入，没有被新offline contract重新接受或否定。ratio256与near-ratio<2的精确cap、旧RSA graph barrier与新algorithmic membership、J1已关闭cardinality antecedent与未关闭interval layer也都分开。没有看到同source副本/旧review被重复计成新结果。

全部ASSERTIONS、fixture、historical formula census或sample均按原报告证据强度保留；没有将算验改写手证。三个明确source gap继续保留：Gaussian完整Newton证书与reproducer、J1 r61–64完整certificate/portable ZIP、adaptive完整hypotheses/proof source。J1 mod3的certificate当前可得不意味着本文重新验证其每一大整数；J1 interval源的外部阅读报告不等本次重取外文。

## 读取载体索引

固定Source URL、blob、bytes和SHA均在补卷每项`primary_source/existing_reviews`与18-source manifest中。本次主要实际读本地解包文本：`c01_m00/01.txt`（affine及peer）；`parent_45/46.txt`（dictionary及peer）；`parent_71/91.txt`（carry及peer）；`c00_m00/01/02.txt`（修正版batch、peer、erratum）；`c02.md/c03.md/c05.md/c06.md`（Gaussian/J1两组/adaptive）；`rsa_m02/06/15.txt`（dyadic及两review）；`three_m01/03.txt`（cost及对应review段）；`rsa_antecedent.txt`、`near0.txt`、`r004.txt`、`j1_scope_audit.txt`。`c04.json`只metadata层。所有这些路径属于本地工作证据，不能把它们写成公开Source伪链接。

本报告没有新增Source写入、Native状态写入、数学证明或接纳；后续若公式、来源或状态字节再次改变，应对变更范围补文献核对，不继承本报告为新的数学审核。

## 既有RSA实际审核记录的追加文献绑定

已独立快回读作者的 `supplement_number_sources/RSA_ANTECEDENT_ACTUAL_DR_BINDING_RECEIPT.json`，并实际阅读全文的2187B DR与2037B RR；对三份现有本地原字节作行政bytes/SHA/blob比对，均与回执一致，没有运行数学程序。DR的current-main changed manifest精确匹配blob `24166863826a6f1f8527936c2dc9a57d9a864441`；RR不在changed manifest中的空matches不是内容缺失，其实际2037B原字节SHA直接匹配DR的result_record_sha256。具体链为：

- DR：`research_result_reviews/RR-2D43CCB30B906AFB6E20/DR-EA5EFB3177111D8A8A44.json`，blob `24166863826a6f1f8527936c2dc9a57d9a864441`，SHA256 `c3ed65f48c84cb9dd4153f6555236cb112272918f02ac1751ebcb95298842755`。
- RR：`RR-2D43CCB30B906AFB6E20`，2037B，blob `48e59507afa688c544a584a84b35566f0bac362c`，SHA256 `b69dd5e3107caf2e214e2e37df47e41d22d8a88d2e12a3cc165afa2bc7b6b9aa`，与actual DR引用完全一致。
- 已读review报告：8267B，blob `c2739f041d858167a923edf629aa3402bcd4900b`，SHA256 `40764e71d4574765e57a08824ef0ce178459a7706637919b055abef0bfd3ff5f`，与actual DR的review_path、review_blob、review_sha绑定一致。

实际已存disposition为 `ACCEPTED`、`terminal=true`、destination=`FOLLOWUP_TASK`，确切后续为 `RS-RSA-EXPONENT-COLLISION-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`。补卷条目现标 `EXISTING_TASK_REVIEW_ACCEPTED_TERMINAL_FOLLOWUP_TASK_BOUND_TO_ACTUAL_DR`，与记录一致。原先只掌握报告时保留SOURCE_REPORTED边界；此次只是补齐已经存在的正式文献绑定，未产生新review或新数学票。它不接受新的dyadic membership论文，不宣告外部prior-art followup完成，不补造Gen1的REQUEST记录，母目标仍OPEN。原数学公式、作者披露、historical unrerun和三个source gaps不变。
