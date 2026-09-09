# 合数道路 RH：新研究员接手入口

Status: RESEARCH HANDOFF / NO RH PROOF / NO THEOREM PROMOTION
Handoff date: 2026-09-09
Provenance researcher: EM-FREE-C4A91D; exposed continuation, not a blind discovery.
Activity: RA-C4A91D-RH-HANDOFF-20260909
Parent objective: OBJ-RH-COMPOSITE-ROAD-20260905

## 先读什么

本文件是后续任务的共同入口，不要求访问旧聊天或联系原研究员。

1. 读取当前 `p000_reality_foundation.json` 及其联合关系观察方向 companion；尤其保留“合数是路，素数是坑”和 `UNPROVEN_RETAIN`。本交接不改变 P000，也不把研究猜想升格为前提。
2. 阅读本文件的状态分层、纠错和任务依赖。运行本目录 `stage2_verify.py`（普通 Python 3.10+，不能用 -O）。它是原包 `durable_certificate.py` 的逐字节副本，完整包含有理候选与整数对偶向量。
3. 按下列顺序读取 EM 的冻结原件。统一研究源快照为 `9d7c4c6eafc5479a6795a128fc0288fc893bed3c`；`git show <此SHA>:<路径>` 可恢复当时版本。后续当前修订须与该快照显式比较，不能悄悄混用。
4. 对自己领取的任务，读取机器任务书 `source_refs` 与本目录 `source_manifest.json`。后者由发布执行器从 Git 对象生成，记录原件路径、Git blob 和 SHA-256。

## 已有材料的阅读链

### A. 9 月 5 日的全整数余数坐标与严格分离证书

完整证明、所有原始有理输入及自包含程序的长期原件：
- repository: `awdawmip/chatgpt-global-knowledge`
- immutable commit: `bb649a26fd04db9bee3cf237b7c0d0311f99e7d2`
- path: `journal/enterprise-math/2026-09-05/20260905T073134Z-composite-residue-rh-stage2-c4a91d.md`

程序在本目录也有 EM 本地可运行副本，因此证书复核不依赖跨仓权限。

定义 r_n(m)=(m mod n)/n，w_m=1/[m(m+1)]，E(c)=sum_m w_m|1-sum_n c_n r_n(m)|^2。经典强 Nyman–Beurling–Báez-Duarte 判据给 RH iff inf_{c_2,...,c_N}E(c) -> 0；不宣称是本项目的新判据。

一般提取器 L_n(y)=sum_{d|n}mu(n/d)(y_d-y_{d-1})，y_0=0，满足 L_n(r_k)=-delta_nk、L_n(1)=mu(n)。因此成功逼近必须对每个固定 n 有 c_n -> -mu(n)；这是必要条件，不是充分收敛定理。L_6=2y_1-y_3-y_5+y_6 给 E(c)>=|1+c_6|^2/92。删除 6 或全部系数非负，都不能使误差趋零。

30 格整数对偶证书给所有素数专用线性组合统一平方误差下界
549980544461335314637000615 / 22936449866115041739513080208 > 0.0239。
九坐标有理候选 F10=(90r2+88r3+17r4+70r5-42r6+58r7+5r8+15r9-13r10)/100 的完整无限平方误差在 [0.0238598165,0.0238619688]，严格更小。
另外 N=60 的候选误差在 [0.0114871466,0.0115462992]；N=100 的候选在 [0.0102017223,0.0102790723] < 1/92。这些是特定候选的范数区间，不是最优距离的双侧区间。

2026-09-09 已对原包 12 个文件的 SHA-256 清单逐项核对，并重新执行原 verify.py 及自包含程序。14,161 对提取器回归与全部三个无限尾项证书通过。`stage2_remote_recheck.json` 为发布环境再次执行的输出，`stage2_verify.py` 的 SHA-256 必须为 df49a8cd07f84375466ff9e003ac7c96044936e5b9e5b5a73cb62165bb1ae436。

### B. 9 月 6 日推进至全整数正道路场（研究推导，未独立审定）

按依赖顺序阅读以下原件（均在上述 EM 快照，manifest 还列出同组全部笔记）：
- `research_notes/COMPOSITE_ROAD_RH_FUTURE_PORT_POSITIVE_DEFORMATION_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_BOUNDARY_SLOPE_CLOSURE_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_PENETRATION_JET_HIERARCHY_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_DISCRETE_L2_NONCOMMUTATION_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_RAMANUJAN_PHASE_COHERENCE_20260906.md`

关键载体对每个整数 n 保留 R_a(n)=sum_{d|n}mu(d)/d^a=prod_{p|n}(1-p^-a)，a>0，R_a(1)=1。S_a(x)=sum_{n<=x}R_a(n)，c_a=1/zeta(1+a)，E_a=S_a-c_a x，E_0=1_[1,infinity)。

原件给出以下推导，后续必须按审计状态使用，不能把作者的 PROVED 标签误读成已独立验证：
- 有限前缀的所有 n>M 坐标恰经一个斜率端口传递；只在声明的有限 horizon 内成立。
- R_a(n) 在 a=0 的接触阶为 omega(n)，第一导数为 Lambda(n)；多因子合数出现在较高阶，不可因当前导数看不到而删除。
- 原始道路能量 Q_a=int_0^infinity |E_a-E_0|^2 dx/x^2，与 RH 的 O(a) 条件的联系通过 Burnol/Báez-Duarte 及 raw/completed 比较建立，尚需独立逐步核验。
- 有限 Green 核 K_N(u,v)=1/max(u,v)-1/N 保留合数两两交互；有限 Q_{a,N} 单调增至可能无穷的 Q_a。
- 离散版本 B_{a,N}=S_a(N)-1-c_a(N+1/2)，D_a=sum_N B_{a,N}^2/N^2；在正确端点项下与 Q_a 同阶。
- 固定 M 时能量为 O_M(a^2)，不能把先 a->0 后 M->infinity 的结果冒充全局量；逃逸到增长 horizon 的尾部仍未受控。
- Ramanujan 展开 u_a(n)=c_a sum_{q>=2 squarefree} beta_a(q)c_q(n)，beta_a(q)=mu(q)/prod_{p|q}(p^(1+a)-1)。平移平均只保留对角功率；真正待研究的是固定起点的跨频率相位项。

## 必须携带的纠错与边界

1. Lambda_A-Lambda_C 的线性恒等式不赋予 Weil 平移算术矩阵半正定性；二峰反例已保留。不能恢复旧的 0<=T<=I 捷径。
2. Q_a 是 raw zeta 道路能量，Delta_a 是 completed xi Schur 能量。原件已纠正混同；有限反证阈值必须使用 U_road(a)=(sqrt(U_comp(a))+A(a))^2，而不是直接用 U_comp(a)。A(a) 的定义、收敛区和常数是独立审计对象。
3. 某个平移平均量无条件有限，而固定起点量与 RH 等价，这个区别本身不自动构成两个观察者不等价的严格证明。必须另给有限同功率、不同相位而固定起点能量不同的证据或下降失败证明。新谱任务明确包含此项。
4. 不消费未恢复证书的旧 Herglotz 数值断言，不消费未经本次核验的外部零点比例/方法上限说法。精细条件性 Nyman 渐近式不能反向充当无条件 RH 证明。
5. 有限数值小、拟合系数为零、可素因子分解，均不构成全局冗余证书。平方自由 q 的谱选择只在精确展开系数为零的声明层次适用，不删除完整整数道路人口。
6. 旧任务的证明、检查与新任务的独立证据必须分开。恢复不是重新发明，任务发布不是数学认可。

## 本次发布的任务关系

共同父目标为 OBJ-RH-COMPOSITE-ROAD-20260905。历史自由研究事件不是伪造的已完成正式任务。

- RH-ROAD-AUDIT-20260909：REPLAY。独立审计研究链、修订阈值与证据分层；源自用户要求核验和交接，不把原始自由候选冒充认可前提。
- RH-ROAD-KERNEL-20260909：CONTINUATION，正式 parent_task_id 为上述审计任务，运行依赖该任务。它是预先发布的条件后续，不断言父任务已完成。目标是固定起点双频核、相位丢失见证和保留耦合的有限/尾接口。
- RH-ROAD-TAIL-20260909：CONTINUATION，正式 parent_task_id 为核任务，依赖审计和核两任务。目标是尺度适配的逃逸尾界；允许明确的严格障碍或带隔离缺口的定量条件定理，但不允许只重述 RH 等价式。

正式是否存在以 `research_task_records/<task-id>/<publication-id>.json` 和执行生成的 `publication_receipt.json` 为准；本入口文本单独不是发布记录，不给任何人分配执行所有权。发布后的依赖状态不等于已领取或已完成。

## 最小未完成问题

令 h_N(theta)=sum_{n=1}^N exp(i*n*theta)。先把
K(theta,phi)=sum_{N>=1} h_N(theta) conjugate(h_N(phi))/N^2
做成带近零、近共振及截断误差控制的固定起点核，保留非对角相位；再在 full-road 权重上控制 N>=M(a) 的尾部。全局 O(a) 界仍未证明。

交接与复核程序只验证既有有限证书及源绑定；不宣称独立审计已完成，不将 P000 或最高保留原则改写成证明 RH 的附加数学公理。
