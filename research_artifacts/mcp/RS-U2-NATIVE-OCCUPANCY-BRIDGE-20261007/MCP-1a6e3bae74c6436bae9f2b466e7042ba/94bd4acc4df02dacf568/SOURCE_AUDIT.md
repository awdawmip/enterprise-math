# U2 源审计：条件结论、任意 anchored incidence 与占位接口边界

Status: NONBLIND_SHARED_CONTEXT_SOURCE_AUDIT / CONDITIONAL_BRC_IDENTITIES / NO_FORMAL_INDEPENDENT_REVIEW / NO_NATIVE_ADMISSION

Task: RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007
Publication: TP2-E49C20B8D0A6569355F6
Execution owner: EM-DIRECT-FA0C27; RA-283C0A8BF9F924806C568F05; claim MCP-e66fdda6de628ba14ad9c2de.
Execution authorization: `open_receipt.json`, request `u2-research-open-20261007-e1f2b6-06`, authorized=true；持久入口为 [Issue #2797](https://github.com/awdawmip/enterprise-math/issues/2797)。本文由同执行的临时协作者完成，不另建身份或认领。本协作者继承了完整上下文，并参与过方向整理及任务书编写；这不是盲审、正式独立审查或新的数学准入。

## 1. 读取范围、固定来源与实际复验

已加载 P000、心跳世界 X6/时间合同、joint relation preservation、residual fidelity、任务书、BRC 唯一运算政策及其机器合同。空间固定为原生六维离散 Cell，无原生平面；十二有向端口不是十二轴。下文空间坐标为有符号内部图表，不作为最终 Cell 地址。路径深度是关系深度，未加入物理时间；占位后继若进入研究须另行定型时间与存储更新。正响应预算与原始作用、质量、能量保持区分。

完整冻结来源来自连接器读回，本地见 `source/FETCH_MANIFEST.json`。归档发布的清单叶文件名为 `FETCH_MANIFEST.json`；复现时恢复到 `source/FETCH_MANIFEST.json`，再按其精确提交、路径和 blob 取回以下来源：

| 本地文件 | 固定提交 | 读回 Git blob |
| --- | --- | --- |
| `source/README.md` | `fe9ce58293ac77b72092512620e8670ca9be2d78` | `bd35175a2e5ca379e95a9c0b922395ce3be45ec7` |
| `source/packet_router.py` | 同上 | `7465f5aa16cbb8fba61ba4be80f8a6884b879c53` |
| `source/replay.py` | 同上 | `94c1abf48578f742c7cbd305c50d4f3e1c6e0ee9` |
| `source/CHECKPOINT.json` | `ccd05f7e0e68b8c04288985c38f5f0bd15381d4e` | `3f404aa25a5cb403106a21a65478b6fd2069d0c6` |
| `source/sources/brc_weighted.py` | `fe9ce58293ac77b72092512620e8670ca9be2d78` | `3f205696709e847909958a153f8fe10d3f6b70f0` |
| `source/U1.md` | `a2294c71268e009400e70f28dc0d4df604213c1d` | `d8d489ed4b2eaadcf2995a11ed4db6b25a804eff` |
| `source/ROADMAP.md` | `ff90471f4245464de9d132114e135ca235c5a63b` | `b39c6b4eb2c9a998c13ae5055ca1f25a64968941` |

七个本地文件字节在取回时分别与 Git blob 匹配。科学源文件未改动。本次在 `source/` 中仅原样执行一次 `python -B replay.py`，stdout 保存为 `replay_actual.json`，stderr 保存为 `replay_actual.stderr.log`。进程 exit=0，stderr 为 0 bytes。输出 SHA256=`95294dedf063702146d3f1186fbe53e4a8b221db184a31319dbea915f1a17e82`。

实际复验为 **3329 checks**；实际调用 `cwm_edge=102`、`cwm_propagate=172080`、`cwm_recoalesce=261478`、`one_state_recurrent_cwm=4`。这些是原程序的本次重放，不能作为 3329 个新发现或独立复制。JSON 中 `SAME_AUTHOR_EXACT_CIRCUIT_REPLAY` 是原程序保留的状态字样，不是本次正式审查结论。原四单位构型只随未改脚本回归，没有新增四单位实验。原详版 25074 检查及对话内继承数据未在本次取得或执行。

Reuse resolution: 现有 `cwm_edge/cwm_propagate/cwm_recoalesce/one_state_recurrent_cwm` 为 REUSE_EXECUTED；下文一般 H 的式子是这些正 BRC 组合律的精确读出推导。本审计协作者未另跑自定义 H 实验；同一正式任务的另一协作者已执行 `incidence_check.py`，其新增 BRC 证据见第 4 节，不能把本审计局部未执行误写成整个任务未运行。没有普通传播器或经典参考计算。

## 2. 原声明—证明—实现审计表

| 原声明 | 证明依赖 | 实现对应 | 可保留强度 | 未决点／不可转移项 |
| --- | --- | --- | --- | --- |
| 固定线性守恒核普遍变轴至少 2/3 | README 19–35；纯输入的任一轴最多取包预算的 1/3；再沿带输入标签的线性混合求和 | `packets` 99–120 先乘 1/\|H_p\| 再乘 1/3，三腿异轴 | 条件输出包覆盖结论成立 | 不是边际分布变化量、时间演化或力学定律；U1 仅对给定输入优化，不受普遍固定核量词约束 |
| 默认 K 与 m'_j=m_j/5+2T/15 | README 25–33；完整 40 族的组合对称与线性 | `triples_at` 75–80、`marginals` 123–128；replay 17–43 检查全部端口及有限混合 | 对默认完整 40 族成立 | 任意 incidence 子族不自动给出同一个仿射式；有限混合检查不替代一般证明 |
| 固定构型场唯一 l1 总响应与尾界 | README 41–47；正 BRC 路径级数及 rho<1 的列守恒收缩 | `transport_tables` 154–170 每列权 rho；`field_prefix` 173–215 保留 source/Cell/incoming，下一入射为 `q ^ 1`；一状态 recurrence 作比较器 | 对固定位置、固定线性无缺损转移的总响应成立 | 尾界不证明路径计数有限；unary 状态不能直接执行历史敏感、整包阻断或占位变更 |
| 两边自身回传 (12+3d_a)lambda² | README 49–53；默认 K 行和为 1，首次发射各向等量；材料返边权 4lambda | `field_prefix` 注入每源 12 个等权入射种子；replay 101–104 检查默认核 | 原默认公式成立 | 任意 H 的首发未必各向等量，需下节修正式；K(p,p)=1/3 单独不够 |
| P/Q 同边际和两两 CWM，双阻断可区分 | README 70–81；特定等权三元类的有限组合见证 | replay 45–77 用同默认种子、不同四步提取历史生成缓冲，逐端口和 pair 校核 | 对原明确有限准备成立 | 相等支路权重与类供给不能省略；没有一般“pair CWM 推出任意剩余 dominant 相等”的定理 |
| 三元 histogram 对阻断／释放充分且必要 | README 85–93；类一致作用与补集阻断隔离 | `gate` 131–139 整包保留，`histogram` 142–147 按类合并；replay 78–91 在两个正端口缓冲上检验 | 来源盲 total histogram 充分；全部阻断允许时类权重必要。若问 CWM，则保留类 CWM | source/incoming/path/phase 敏感操作不在该商的权限内 |

三元 histogram 的证明用每腿权重 `w_h`，代码存每包 budget 的 CWM，输出前再调用 `serial(value, THIRD)`；这两个约定相差显式因子 1/3，代码与证明一致。来源盲 total 观察只要求类 total；保存整个类 CWM 是更强接口，不能称它对仅 total 的语言也逐字段最小。

## 3. 换成任意 anchored H 后哪些恒等式保留

这里的 H 是**结构上可接受的候选关联**，未证明满足原生 `TRIADIC_CLOSURE_E`。固定每个入射 p 的有限非空集合 H_p，元素为规范排序的三端口 tuple，含 p 且三轴互异。H 与材料位置、当前正响应值无反馈依赖。沿现有包预算分割与腿传播律，令 n_p=|H_p|，则总响应读出核精确为

`K_H(q,p) = #{h in H_p : q in h} / (3 n_p)`。

这是对每条现有 BRC 支路权 `1/n_p` 再串联 `1/3` 的读出求和，不引入新世界传播规则。

每列和为 1；所有 h 含 p，故 `K_H(p,p)=1/3`；每个 h 的轴互异，故 `K_H(-p,p)=0`。因此同原始轴的份额恰为 1/3，带来源/入射标签的变轴份额恰为 2/3。任意正输入总量 T 的每轴输出仍不超过 T/3，因为任何一包对该轴至多贡献包预算的 1/3。一般的普遍覆盖核只有“至少 2/3”；anchored 构造给出等号。无需完整 40 族，但不能把这一响应分割推成不可分原始作用的实现。

不保留的默认细节包括：跨轴每端口 1/15、轴预算的特定仿射式、每输入 40 个包及 120 腿的分支计数、符号置换对称性，以及默认输入对所有 160 个三元类均匀供给。改变 H 后，CWM count/dominant 也必须沿实际新分支重算，不能仅凭列总量相同沿用默认 CWM。

若每个固定材料位置使用预先固定的列守恒 K_H，其邻接传播仍由相同的一步原生轴位移组成。设相应完整 unary 正转移为 P_H；对正总量其每列和 1。有限源总量 N、0<rho<1 时，BRC 深度 ell 的总响应为 `N rho^ell`；几何余项为 `N rho^(L+1)/(1-rho)`。总响应层面的 `Phi=J+rho P_H Phi` 仍有唯一 l1 解：对两个解之差，l1 范数经 rho P_H 至多缩小 rho 倍。这是有前提的精确接口延伸，不靠有限自定义 H 检查建立普遍量词。

加入状态依赖 incidence、材料移动、joint valve 或真实时间存储之后，不再直接拥有这个固定 unary P_H。尤其存储在物理时间中不衰减，与每关系深度统一乘 rho 是不同动作。必须先证明新的完整状态更新、预算及收敛条件，不能因旧尾界小而删除联合状态。

## 4. 两边自返的正确一般式与最小非转移见证

材料 a 位于 z_a，定义它的行和 `r_a(q)=sum_p K_a(q,p)`。仍按原脚本在材料胞注入十二个各重 1/12 的**入射种子**，故第一次发射到方向 q 的预算为

`(rho/12) r_a(q) = lambda r_a(q)`。

这一步只有在相应行和为 1 时才等于 lambda。第二条边要回到 z_a，邻胞入射为 -q，必须沿 -q 出口返回。空胞的返回权为 lambda；材料胞因 anchored 性有 `rho K_neighbor(-q,-q)=rho/3=4lambda`。逐两边支路串联并合并，得到

`R_a^(2) = lambda² [12 + 3 sum_{q : z_a+d(q) occupied} r_a(q)]`。

推导用了 `sum_q r_a(q)=12`。旧式对于某个固定准备恰好需要邻向行和之和为 d_a；所有行和均为 1 是足够条件。若要求旧式对任意单邻方向都成立，就需要所有对应方向行和为 1。默认 K 满足该条件，所以原 U2 没有因此被否定。

采用同一正式执行中 `INCIDENCE_REGULARITY.md` 的更强见证：所有入射族来自一个共同的五三元关系 H，`H_p={h in H:p in h}`，而非各自任意选族。其三元集合为

`{+1,+2,+3}, {-1,-2,-3}, {+4,+5,+6}, {-4,-5,-6}, {+1,+4,+5}`。

该 coherent 关系覆盖十二端口且每个三元集合三轴互异，仍有 `r(+1)=4/3`、`r(-1)=1`。相邻准备 `c,c+E_1` 两处使用相同 H，在 `lambda=1/48` 时，两边自身回传为 `(1/144,5/768)`，而仅代邻居数的旧式会给 `(5/768,5/768)`。`incidence_check.json` 的 `row_sums`、`two_edge_self_returns` 字段已实际记录上述值与 CWM；输入、源码 pin、逐来源路径和费用保留于该证据，不在本审计重复生成。

`INCIDENCE_REGULARITY.md` 同时给出 coherent、无重复、各入射均匀选择的准确条件：首次各向等量等价于每个 incidence-connected component 内端口度数恒定。一般的任意 anchored H 仍只受本节行和公式约束，不能无条件套用共同 hypergraph 的互易性或度正则判据。

这里消费的是同一非盲任务的新条件 BRC 执行，不是独立审查。反例只否定默认两边自返式的无条件转移；**没有证明此 H 原生合法，没有给第二个原生完成，也未宣称占位后继**。它没有修改 P000，没有使用三空间位移凑零，也没有把响应不对称认作物理力。

## 5. 实现覆盖缺口与 P/Q 的转移条件

对固定源 AST 的静态检查确认：

| 函数 | 参数 | 自定义 H 能否进入 |
| --- | --- | --- |
| `packets`（99） | incoming, state, tag, born_at, incidence | 可以；仅检查非空、tuple 去重、含入射和三轴互异 |
| `transport_tables`（154） | rho | 不可以；165 行调用 `packets(..., tag=...)` 时没有传 incidence，使用默认 40 族 |
| `field_prefix`（173） | material_cells, depth, rho, check | 不可以；185 行调用 `transport_tables(rho)` |

因此把合法 H 交给 `packets` 一次，并没有让既有 `field_prefix` 的场也使用它；这是一项具体的参数接线缺口。后续若要计算新 H，必须显式扩展材料散射表入口和所需来源/场状态，并验证默认回归与自定义参数实际被调用。当前 `replay.py` 成功只覆盖默认 incidence，没有覆盖这一扩展。

另有输入语义前置：自定义 incidence 不自动规范化 tuple 的排列。代码以 tuple 原值去重和做 histogram key，故同一个三元集合的不同排列可能被当成不同类；默认 `triples_at` 全部排序，所以原结果没有受此影响。把任意 H 解释为集合并使用“至多 160 类／补集阻断隔离一类”的最小性结论前，必须固定规范排序或者先证明排列商保真。代码结构检查从来不验证原生 signed triad 合法性。

P/Q 的原受控准备依赖默认核给八个所需三元集合供给相等的可选缓冲预算。一般 H 下应先列出实际可达三元支持、每类来源/入射子族与预算；缺少任一类或权重不匹配时，原四步提取与相等 pair-CWM 证书不能直接沿用。即便两个缓冲仍能受控准备，储库和提取历史仍是不同边界状态，不等于相同完整状态或同一无操控两材料轨道。

在**声明的实际三元支持**上，若所有端口阻断集合仍允许，source-blind 类 histogram 的总量充分性及补集隔离必要性保留；160 只是完整规范 signed-triple 空间的上界。若原生操作不能任意阻断，必要性需重做；如果要来源敏感读出、材料存储或后继，则先保留对应联合键。`field_prefix` 已压为 unary 状态，不能拿它的末层端口边际直接执行后来加入的整包阀门。

## 6. 审计结论与下一项最小缺口

默认 U2 的 2/3 条件核、固定构型场尾界、特定两边回传和 P/Q 受控见证，在上述明确量词内得到源级核对及一次原程序复验。它们仍是条件电路结论，未获正式独立审查、原生准入或物理标定。源中的 `material_positions_solved/native_triads_admitted/primitive_quantum_realization/physical_time/prime_claim` 五项在实际输出中均为 false。

本次可移交的新审计信息为：**任意 H 的列守恒与 2/3 可以保留，但首次发射需要行和，旧两边自返公式需要额外条件；当前场函数不能接受 H；原三元可达性及 histogram 最小性必须随新操作/支持重新核对。**这些将“换一份合法关联后直接复用全套 U2 输出”的捷径明确切断。

两单位占位问题尚缺：有来源的原生 signed triad incidence；响应预算到原始作用的类型对应；材料反作用／整包存储与边界回馈；从完整作用/材料状态到新占位的后继关系及其时间类型。最小下一步是给一项这样的来源接口并检查它是否满足以上保留条件，或返回精确前提缺失。缺少这些关系不证明世界无解，也不授权任意选一个占位更新；本审计未创建材料后继候选。
