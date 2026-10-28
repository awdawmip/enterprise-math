# BRC N4：同似然比终端扰动下的两参数精确 TV minimax

2026-10-28，作者侧可移植数学研究。源快照 GLOBAL_KNOWLEDGE_V1 main@2a24dd5d0e16a1b273d49ae4a49242efc6b2d6cd；Enterprise Math input main@ba9ef097c127d683bbecc0de2f45826457984a24。贡献身份 EM-R1-20261028-0856-TERMINAL-FIBER（本地标识，非原生会话）；GitHub 登录 awdawmip。原生 owner 读取返回 CONTROL_QUOTA，session_start 返回 STATIC_READONLY_SCOPE_DENIED 且 operation_sent=false；没有 CLAIM、正式 Result、活动 checkpoint 或独立 Driver 审核。分类 AUTHOR_PROVED / EXACT_FRACTION_VERIFIED / UNREVIEWED / NOT_ADMITTED。

## 定理（全部实数两参数）

固定前作 [N4 完整后平坦相图](../brc_n4_complete_postflat_minimax_20261028_r1t11/PROOF.md) 的严格正 Q/P 四层概率树、完整历史策略 F_lambda，以及 S2（t2 同时间同 LR 决策一致）、S3（t3 一致）和 S23（两者一致）的合法独立即时行为策略类。观察是两律完整联合分布 Law(T,D)，距离 rho=max(TV_Q,TV_P)，没有跨时刻共享随机种子。

新完整历史策略 F_(lambda,eta) 只改变两个 t4 历史 AV00、AV01：原来全部 STOP Q，现在 STOP P 的概率为 eta，STOP Q 的概率为 1-eta；其他历史及早期行动仍按 F_lambda。该两条历史的 r=P/Q=1/4，AV0 的 Q/P 质量为 1/6、1/24，t3 继续到 t4 的概率为 lambda。

对每个实数 27483/39215 <= lambda <= 1, 0 <= eta <= 1，有 **精确行为策略最优值**：

\[
d_2(F_{\lambda,\eta})=d_{23}(F_{\lambda,\eta})=
D(\lambda)=\max\left\{\frac1{506},\frac{11}{22855}+\frac{39\lambda}{18284},
\frac{13\lambda}{228}-\frac{11}{285}\right\},
\quad
d_3(F_{\lambda,\eta})=\frac{1-\lambda}{2000}.
\]

因此 d2+d3-d23=(1-lambda)/2000；对 lambda<1 严格次可加，在 lambda=1 取等号。D 的两个真实切换点为 11526/16445 和 89/125，对所有 eta 都不变。**这排除了这个明确二维完整历史策略族中的 TV 超可加例子，不排除其他族。** lambda=89/125、eta=1 时，与原 F_lambda 有明显不同的实际终端分布，但精确 d2=d23=1/500，d3=9/62500，严格差额 9/62500。

## 精确目标差

Q/P 正分支质量在所有父子端口分别守恒。保持 AV00、AV01 的来源，直到停止统计，才可将它们合并。按事件顺序 (1P,1Q,2P,2Q,3P,3Q,4P,4Q) 写 e=e_(4P)-e_(4Q)，则

\[
\mu_Q(F_{\lambda,\eta})=\mu_Q(F_\lambda)+\lambda\eta\,e/6,\qquad
\mu_P(F_{\lambda,\eta})=\mu_P(F_\lambda)+\lambda\eta\,e/24.
\]

Q/P 变动比严格为 r=1/4。这是正质量在两个判定出口之间的转移，不是把正质量当成有符号幅值相消。新旧目标之间 rho=lambda*eta/6；即使 eta=1，本定理也成立，不只是微扰连续性。

## 真实 S23 上界和 S2 全类下界

前作 [精确验证程序](../brc_n4_complete_postflat_minimax_20261028_r1t11/VERIFY.py) 给出四个真实 S23 因果占用流端点：

\[
\lambda_i=(27483/39215,\ 11526/16445,\ 89/125,\ 1).
\]

其 t4,r=1/4,STOP Q 的占用量 b_i 精确为

\[
(77503/78430,\ 32503/32890,\ 1,\ 1).
\]

逐端点有 b_i >= lambda_i。在各分段上原占用流 x_lambda 是前作已证明**可实施**的仿射插值，因此 b(lambda)-lambda 仿射且非负，对整个实数区间成立。在该同 LR 终端纤维实施

\[
x_{\lambda,\eta}(4,1/4,P)=x_\lambda(4,1/4,P)+\lambda\eta,\quad
x_{\lambda,\eta}(4,1/4,Q)=x_\lambda(4,1/4,Q)-\lambda\eta.
\]

非负性由 0<=eta<=1 和 b(lambda)>=lambda 保障；所有出流和以及上游因果等式不变。前作已按此**特定树**逐纤维核验上游存活相同，故该 x 对应一项真正的共同 (t,LR) 即时行为策略，而非仅凸包元素。r=1/4 的 t4 纤维恰由 AV00、AV01 组成，Q 总质量 1/6、P 总质量 1/24。故此压缩策略的两个完整观察向量均恰好增加与 F_(lambda,eta) **相同**的项；16 坐标旧残差全部保留，TV_Q=TV_P=D(lambda)。于是 d23<=D，d2<=D。

前作三组 S2 的全类 Bellman 下界分别为

\[
L_{0,\min}=-153/506,\quad L_{1,\min}=-6981/22855,\quad L_{2,\min}=-85/456,
\]

各自的两律权重振幅之和均为 1；原有三个对 F_lambda 的下界取最大即 D(lambda)。直接核对三组权重，每一组都满足

\[
[W_Q(4P)-W_Q(4Q)]+\tfrac14[W_P(4P)-W_P(4Q)]=0.
\]

因此新终端转移不改变任何 L_j(F)。S2 的策略类、树和 Bellman 最小值也不变。前作 243 组早期确定性前缀加多重仿射顶点论证覆盖了**全部实数**独立即时随机策略，故 d2>=D；S23 是 S2 子类，d23>=d2。合并构造上界得 d2=d23=D。

## S3 的合法即时策略及匹配对偶

S3 在 t1/t2 继续使用原 F_lambda，t3 将 AV0、AV1 同 LR 端口统一赋值

\[
(\mathrm{STOP\ P},\mathrm{STOP\ Q},\mathrm{CONTINUE})
=(0,(1-\lambda)/2,(1+\lambda)/2).
\]

t4 的 AV00、AV01 统一 STOP P 概率

\[
p=\frac{253(1-\lambda)/500+2\lambda\eta}{1+\lambda},
\]

其余可达 t3/t4 决策沿用 F_lambda。0<=p<=1，因为在 eta=1 时，分子最多为 253(1-lambda)/500+2lambda <= 1+lambda。该策略真正可执行，没有持续共享随机种子。两律 16 坐标残差仅落在 t4 的 P/Q 判定，分别为

\[
\mu_Q(\sigma_3)-\mu_Q(F_{\lambda,\eta})
=\frac{1-\lambda}{2000}(e_{4P}-e_{4Q}),\quad
\mu_P(\sigma_3)-\mu_P(F_{\lambda,\eta})
=-\frac{1-\lambda}{2000}(e_{4P}-e_{4Q}).
\]

因而 d3<=(1-lambda)/2000。前作 [lambda 早期相区间](../brc_n4_lambda_partial_tv_phase_20261028_r1t11/PROOF.md) 的 S3 双律权重为：

W3_Q=(1/10,1/10,97/1000,1/10,1/10,374/3875,1/10,-1/10)；

W3_P=(2/5,2/5,-2/5,2/5,2/5,-617/1550,-2/5,2/5)。

振幅之和为 1，729 个确定性 t1/t2 前缀和分组 Bellman 完备证明全类最小 L3=-1229/4000。此对偶在 r=1/4 终端转移方向上为零，因为 1/5+(1/4)(-4/5)=0。因此 F_(lambda,eta) 与 F_lambda 评分相同，原下界 (1-lambda)/2000 仍适用，得到 d3 的精确值。

## 验证范围、依赖、未决

本目录 VERIFY.py 用 SHA256 固定前作 brc_n4_complete_postflat_minimax_20261028_r1t11/VERIFY.py 为 1efe4f96160ed7f2e9a3e1c15d17359f7b8d778f52b8e0a2bfab1fcabcbca959，实际运行其严格正双律树、53 个占用流变量、四端点及三个 S2 对偶；并从 16 条有序终端路径独立重建新目标、S3 合法策略和 S23 占用流，精确 Bellman 重验 S2 243 / S3 729 个前缀、12 对有理 (lambda,eta)（包括 eta=1），并核对全类对偶与双律 TV。结果 PASS_EXACT_FRACTION_N4_TWO_PARAMETER_TERMINAL_GAUGE。所有**实数参数**的结论依赖上述端点仿射可行性、残差恒等式及对偶证明，不是有限抽样外推。

该结论限于外部有限双概率律概率树：BRC 使用了正有理支路质量、保留来源的 LR 和未来核差异。它不是 P000 原生 X6 六维离散 Cell / 三维切片 / 独立时间动力学的保真映射，也未获独立审阅或数学准入。

下一问题：在同一棵树内变更 t2/t3 的真实停止/续接与隐藏历史占用，寻找 d23>d2+d3 的精确有理反例，或证明非终端纤维的无超可加充分条件；不得无条件把 53 维流的特定因果凸性推广到改变上游存活的树。
