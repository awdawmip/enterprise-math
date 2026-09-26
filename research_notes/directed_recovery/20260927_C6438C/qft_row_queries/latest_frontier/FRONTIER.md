# QFT 去量子化：最新来源前沿与下一步精确命题

Status: SHARED_AUTHOR_RETRIEVAL_AND_SYMBOLIC_SYNTHESIS / NOT_ADMITTED.
研究者共享贡献：EM-DIRECT-C6438C；活动 RA-CAAAC604CB513AEA8BBC1DFC。
本文件没有新增科学 BRC 执行、旧实验重放或远端写入。
当前任务给定并实际读取的 Enterprise Math 快照：
`d8447e4dc9c6500720c671649798e4ae08df2ae2`。
全局同步脚本返回 PASS / LEASE_REUSED：
`f44ed5959c92e6e088c61c102951d1ab2c5e98d4`。

**主要结论：** 当前剩余问题不是再把 61 个内部坐标降到 9 个、再融合 W²、或把所有相位字预编译一次。Stage101 已完成这些相应接口和有限证据。最有价值的下一步是把整个报告采样归约成很少的、完整相干行查询，然后研究这些查询的数论纤维求和复杂度。新的 single-walker 耦合给出了这个归约；它不自动提供便宜的查询器。

## 1. 实际读取范围与来源等级

先调用 `em_status`。服务可用，但其静态 source bundle 仍为
`ea8aefb33725fe7bf711dca4007b14fe323c274d`，创建于 2026-09-20；它不是最新科学来源。
本次所有实质新来源均通过 GitHub connector 在上面 d844 固定快照读取。

按 `research_notes` 目录路由，没有递归扫描整个仓库。Contents API 只返回 1000 项；随后只对该目录读取非递归 Git tree `b3bd7f948dda138dce9a3d23163c156a51e84d26`，得到 1040 项、`truncated=false`。补出的 40 项均为旧 x6 文件，未发现晚于 Stage101 的同线阶段名。读了 Stage94–101 的相关正文、weighted-kernel 正文，以及 Stage82/85 的必要边界，未下载或重新执行这些阶段的二进制包。

25 份实际读取的正文、政策和选定实现缓存于 `source_cache/`；逐份以 Git blob 格式重新计算 SHA-1，与 connector 返回的 blob 完全一致。完整路径、版本、URL、SHA-256 见 `SOURCE_PINS.json`。以下的“已执行”仅忠实报告源作者的执行记录，不冒称本次重放或独立审查。

## 2. 已有成果，不应再次登记为缺口

| 范围 | 当前来源中的成果 | 尚不能推出 |
|---|---|---|
| Stage94–95 | 无碰撞支持包络保证全后缀条件均匀；实际 SuffixRecipe、全部后态恢复、随机中断续接已完成 | 不知道阶时，证书免费；读数不可见意味着残差可删除 |
| Stage96–97 | 全范围短长步证书、结构键复用、容量排除、含失败竞争工作计费的有界组合已执行 | O(sqrt(2^ell)) 查询为 poly(ell)；证书查询下降等于场求值下降 |
| Stage98、执行99/100 | 有序低秩恒等式；同根任意幂正规形；W² 一次完整配对执行；实际根分母指数 118h+5 | 一次配对等于常数位工作；名义相位周期是真实周期 |
| Stage101 | 61×9 基 E 的秩认证、512 个实际有序算子、62464 个正逆列比较；完整行缓存、二进状态编码、重建优化 | 512 字对任意 t 足够；完整状态可由投影单独恢复；冷编译摊销天然有利 |
| weighted-kernel 20260926 | 保持正质量的作用类聚合；固定低层种子的一位修复非空时为仿射纤维；完整匹配族与基数证书；有限执行 | 保存相位抵消；多层全树自动为单个仿射空间；消除阶乘匹配代价 |

Stage101 的标准 N21/a2/t10 全树读取加恢复有 7626 次 transform 请求、3038 次全字求值、512 个不同实际算子；根语义需求仍 13803。原单次追踪的相位求值约 1 秒，而重建及旧十进哈希占更大份额。这个分解准确解释旧性能，却不构成规模扩展的数学证明。

Stage100 的 `lde_2(W^h)=118h+5` 是在原坐标下的真实矩阵分母下界。它允许以短字描述 W^h，但阻止把展开后的精确数值位长当成 O(log h)。同样，Stage101 的 52 维相位公共正交补被保留；算子差的低秩不许可把完整输入行扔掉。

## 3. 工具覆盖与明确复用决议

本次读取 `tool_invocation_policy.json`、registry、method inventory、相关 dated addenda，以及 `src/enterprise_math` 的非递归 300 项公开源目录和 6 个匹配模块。`tools/enterprise_toolbox.py` 的 AST/公开定义发现合同也已读。没有把目录查到名字算作执行。

| 已有工具或方法 | 本任务的复用决议 | 保持的边界及精确缺口 |
|---|---|---|
| T0_BRC、recent.cbrc_f0.signed_group_completion | REUSE_APPLIED | 完整带符号行及相干求和必须来自已认证列，不以正质量替代振幅 |
| t0.brc_conditional_distribution_lift | REUSE_APPLIED；新 sampler 为 EXTEND_EXISTING_TOOL / DOMAIN_OPERATOR | 借用受限输入族与 joint endpoint intertwining 的证明结构；现 API 是固定非负有限 L、mu=alpha L、LW=QL，不提供依赖当前完整相干行的动态采样比值或点查询 |
| t0.brc_control_mass_quotient | REUSE_APPLIED（边界判定） | 仅正质量商，明确不保存 signed/amplitude cancellation、类内目标身份；不能直接拿来取代 Shor 状态 |
| t0.brc_weighted_kernel_lift | REUSE_APPLIED（聚合/完整性与边界） | 可复用“完整匹配而非样本猜闭包”的证明纪律；其源明确排除 phases/amplitudes，不能声称已解决相干纤维求和 |
| T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA、T8_RELATION_OBSERVABLE_SPECTRUM | COMPOSE_APPLIED | 用于明确已声明的纤维与碰撞；不能凭工具名创造可廉价计算的商 |
| T6_OPERATION_SAFE_QUOTIENT、quotient.operation_family_closure | REUSE_APPLIED | 固定未来观察/控制语言；single-walker 的 latent 标签不是完整后态的可恢复替身 |

准确 source API：`brc_conditional_lift.py:138 certify_conditional_lift`；
`brc_control_mass.py:31 certify_control_mass_partition`；
`heartbeat_weighted_kernel_lift.py:218 lift_weighted_kernel`；
`brc_weighted_recurrent.py:145 recurrent_mass_power`。
最后者模块开头直接把 signed/amplitude cancellation 排除在正质量接口外。

registry/inventory/已选源码均未查到现成 typed Jacobi 或 amplitude point-query 接口；默认分支定向 connector 搜索 `jacobi`、`amplitude_point`、`single_walker` 都无返回。该负检索不是全仓或文献穷尽证明。已知可复用实际 typed 长除法在本项目冻结 lazy-modular 交付；Jacobi 若新增，应是该算术族的域内组合，不另立一般工具家族。

## 4. 命题一：精确报告采样只需每轮两个完整行查询

优先级最高。精确命题由同团队 audit 作者本轮提出，本文件做来源覆盖与代数核对，不能把它计成本代理独立首创。

固定一条真实报告前缀 h，完整未归一化场的行是 v_h(w)∈R^D，
M_h=Σ_w||v_h(w)||²>0。下一轮实际作用为 U_h=P_h⊗T_h，P_h 是认证置换，T_h 是完整正交字；K_sigma=(I+sigma U_h)/2，sigma∈{+1,-1}。

假设维护一个 latent W，其条件律是 ||v_h(W)||²/M_h。取新公平位 C：C=0 时 Z=W，C=1 时 Z=P_h W。仅查询

    x = v_h(Z),       y = T_h v_h(P_h^{-1} Z).

令 A=||x||²+||y||²，按

    Y_sigma(Z) = ||x+sigma y||²/(2A)

抽取 sigma，更新 W'=Z。A=0 的点在真实提议中概率为零；实现必须拒绝伪造的零支持 latent 输入，不能除以零。

证明：Z 的提议概率为 A/(2M_h)，完整正交性给
Σ_sigma||x+sigma y||²=2A，因此 Y 是合法两项分布，并且

    Pr(Z=z,sigma | h) = ||x+sigma y||²/(4M_h).

右边正是下一真实报告与下一 work 端点的联合律。由标准 work 初态 W=1 归纳，所有实际自适应历史的终端报告分布正确；没有小父态质量除法，也不需每轮从全场重建新的 SQ 数据结构。

**执行与未证状态：** 代数归约已由团队给出；audit 正在独立目录实现实际版本，本文件没有运行它。最坏成本由完整行查询器决定，不能把“两个查询”直接写成 poly(log N) 算法。完整 history、原字、源与可重建表达必须保留；latent W 只为抽样耦合，不是物理测量工作寄存器，也不是原条件态等于单行。

## 5. 命题二：完整行查询是非交换系数的模乘纤维求和

这是接下来的主要数学工作接口；root 正在开发有界 MITM 版本。

对固定已选报告 h=(sigma_0,…,sigma_(j-1))，所有 T_i 已由该前缀确定。设实际工作乘数为 b_i。从标准 |1>e0 出发，有精确式

    v_h(w)=2^(-j) Σ_{e∈{0,1}^j: (Π_i b_i^e_i)·1=w}
                      (Π_{i=j-1…0} sigma_i^e_i T_i^e_i)e0.

工作乘法按真实全域认证规则组合；系数矩阵保持右因子先作用的原顺序。对主域单位轨道可用模乘标签描述，padding 行不偷换为该循环轨道。式子是完整选中仪器支路的展开，不把 W/read/W 跨记录改为 W²。

把 j 划为 j_L+j_R，按左半段工作端点 s 聚合完整向量
F(s)=Σ_{e_L: endpoint=s} A(e_L)e0。随后

    v_h(w)=2^(-j) Σ_{e_R} B(e_R) F(P(e_R)^(-1)w).

这给无需未知阶、因数或理想参考的 meet-in-the-middle 求值：枚举并收费 2^j_L+2^j_R 个路径项，以最均衡分割得到 O(2^ceil(j/2)) 项。每个系数的实际矩阵/低秩作用、typed 模乘与逆、整数位长及证据均另计。碰撞桶要对完整带符号向量相加，不能 dictionary overwrite，也不能先平方后聚合。

**已证与未证必须分开：** 上式和指数项数界由代数直接成立；本次未执行。它是可检验的渐近中间步骤，但默认 t≈2log2 N 时 2^(t/2) 仍约 N，绝不是总体多项式去量子化。真正的待证命题是：能否用 poly(log N,t,所需精度) 大小的数论证书或可计算表示，评价上述带非交换有序系数的纤维和，而不先求阶、分解 N、或展开指数多个桶。

Stage101 编译只压缩每项的内部作用，并没有解决这个纤维和。weighted-kernel 聚合的等质量正类匹配也不能直接替代它。建议验收明确包含相消、两个不同半路径落同标签、非交换 T 次序和全部残差方向；只有范数相同或终端一个直方图相同不够。

## 6. 命题三：可计算 character 提供不依赖支持大小的全后缀证书

设 q=2^ell，G 为标准初态所在的工作单位群。若有一个可验证同态

    chi:G -> Z/qZ,        chi(a)=1,

且当前支持 S⊂chi^(-1)(c)，则 a^e S（0≤e<q）两两不交：碰撞会给 c+e=c+f mod q，因此 e=f。直接组合 Stage94 定理，剩余 ell 位条件联合公平，不需枚举 |S|q 个标签。

对于真正的 square schedule，从 work1 出发，在剩余 ell 轮时，所有已用指数都是 q 的倍数，所以 S⊂ker chi 可以通过初态与调度不变量证明，毋须查看每行。必须绑定认证的初态、乘数平方关系、真实轮次和工作域，不能给任意用户场自动颁证。

ell=1 时可用标准 Jacobi character：odd N、unit a，若 Jacobi(a,N)=-1，则以前的偶次幂均为 +1，最后乘 a 到 -1 类。因此最后位公平；Jacobi 可由不输入因数/阶的 reciprocity 算法求得。Jacobi=+1 或 0 只使此证书不可用，不能推定当前位不公平。

**当前状态：** 此同态充分条件是上面给出的符号证明；typed Jacobi 与原程序调度绑定尚待当前后续子任务实现。它补的是 Stage94 明确留下的紧凑着色证书缺口，不重复 Stage95–97 的枚举证书。通用更高 2-power character 的无分解构造、以及对含大奇部输入的有效性尚未解决。只省一位的 Jacobi 不应取代命题二作为整体突破目标。

可以借用 weighted-kernel 的有限提升与完整性证明思路探索 character refinements，但其 PGL6 加权作用核与模单位群 character 不是同一输入类型；若需要未知群表示或全部关系，必须将取得它的成本计入。不能宣称原一位仿射纤维定理已经给出可高效构造的任意高阶 character。

## 7. 首要来源 pins 与下一动作

| 来源（全部位于 d844 快照） | Git blob |
|---|---|
| HEARTBEAT94_UNIFORM_SUFFIX_PROOF | 6d6552cdcfaa58a609d88b9582ef79bfa3ff0d82 |
| HEARTBEAT95_UNIFORM_SUFFIX_EXECUTION | c791e6975c5af1c0ee571555f3d986cf955addff |
| HEARTBEAT96_MEET_CERTIFICATE_REUSE | 4a5ad2f94e6e0db7d13811904c12caa197c530ce |
| HEARTBEAT97_BOUNDED_CERTIFICATE_PORTFOLIO | 752f827c7e7ff4bc07068bec31a02b522d61e70d |
| HEARTBEAT98_ORDERED_LOW_RANK_WORD | ab90e40498ce3d953e5e201aa888e8090d67abef |
| HEARTBEAT99_DYADIC_ROOT_POWER_NORMAL_FORM | 477843bd971541f021f3c602e8d94eab5f6a1771 |
| HEARTBEAT99_ONE_PAIR_SQUARE_EXECUTION | fc9d78dae63754286aa6f1e88fdd39b32ded5d00 |
| HEARTBEAT100_EXECUTED_DYADIC_ROOT_POWERS | 06126ae0ea874674a03924ef110124a041718c5c |
| HEARTBEAT101_EXECUTED_WORD_CACHE_CENSUS | 7f283a8a16dccf7ad948e3c640fd2879d4dcd171 |
| weighted-kernel RESEARCH_NOTE.md | 4ecad40e12d7fe3fe1c0320bac89a976c9ce3660 |
| tool_invocation_policy.json | 7c11ccc90f2dcfed61444cfe97fe89d5d117aa26 |
| enterprise_toolbox_registry.json | 3889506451091ebcfbf7a58cda6517c4af8c3597 |
| research_method_inventory.json | 9289039bc689c638fbef10f9f4489e3793e999f0 |

接续时先消费 root/audit 正在产生的 single-walker 与 MITM 实际结果，不重做 Stage101 census。当前本代理下一项是独立新增 typed Jacobi 与严格调度证书，结果写入 sibling `character_certificates/`，不修改上述冻结来源。主目标仍为 QFT 去量子化；本报告、可运行采样归约和局部着色改进都不是总复杂度闭合。

Global-Knowledge-Sync: main@f44ed59 / GLOBAL_KNOWLEDGE_V1
