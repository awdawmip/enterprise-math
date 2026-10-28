# BRC N=4：动态历史压缩的真正双律 TV 误差可以严格超可加

**作者侧精确有理证明 · 2026-10-28 · UNREVIEWED / NOT_ADMITTED。**
这是外部有限双概率律序贯停止模型的定理，不是 P000 原生 X6 Cell 动力学结论。
冻结账户知识源：GLOBAL_KNOWLEDGE_V1 main@2bccd0522d7ed724311b3ed1c85842b95cdeba8d；
冻结项目输入：enterprise-math main@80377c37dc2d2a3eadedcff350a8e14ef591022a。
前作精确模型见 research_notes/brc_n4_complete_postflat_minimax_20261028_r1t11/VERIFY.py，
本文件的 CERTIFICATES.txt 和 VERIFY.py 为本轮独立新反例的完整可执行证据。

## 1. 固定的严格正 BRC 概率树与新的完整历史行为

保持此前的同一棵 N=4 树。每条标号历史 h 携带正有理数
\(q_h=Q(h)>0,\ r_h=P(h)/Q(h)>0\)，父子两律分别质量守恒。

t=1：A=(1/2,1/2)，B=(1/2,3/2)，括号内容依次为 (q,r)；
t=2：AU=(1/6,1)，AV=(1/3,1/4)，BU=(1/4,1)，BV=(1/4,2)。
t=3：每个父 h 的两个儿子 h0,h1 各有 q_h/2，似然比分别为
\(r_h(1-\epsilon_h),r_h(1+\epsilon_h)\)，
\((\epsilon_{AU},\epsilon_{AV},\epsilon_{BU},\epsilon_{BV})=(1/10,0,4/5,0)\)。
t=4：同样等分 Q 质量、似然比乘 \(1\mp\eta_h\)；
\(\eta_{AV0}=0,\eta_{AV1}=3/50\)，其余各 t=3 父历史为 \(1/20\)。
全部分支严格正，并可逐层直接检验
\(\sum_{\mathrm{child}}q=q_{\mathrm{parent}}\) 和
\(\sum_{\mathrm{child}}qr=q_{\mathrm{parent}}r_{\mathrm{parent}}\)。

完整历史策略 F 的 t=1 总继续。t=2：
AU 采用 (STOP P, STOP Q, CONTINUE)=(1/2,1/6,1/3)；
AV 全继续；BU=(0,1/2,1/2)；BV 全 STOP P。
t=3：AU0 全 STOP Q，AU1 全 STOP P；AV0=(0,1/2,1/2)，AV1 全继续；
BU0 全继续，BU1 全 STOP Q；BV0/BV1 不可达，任取合法动作。
t=4 全停止：当 \(r_h<2501/10000\) 判 Q，否则判 P。
没有隐藏的公共随机种子，每个即时行为动作独立随机化。

观察为完整的 \((T,D)\) 八事件联合分布，事件顺序是
(1P,1Q,2P,2Q,3P,3Q,4P,4Q)；逐标号叶路径计算得到
\[
\mu_Q(F)=(0,0,1/3,11/72,1/36,25/144,1/12,11/48),
\]
\[
\mu_P(F)=(0,0,7/12,11/72,11/360,19/120,53/2400,127/2400).
\]

S2 要求 t=2 时 AU/BU 这对同似然比历史共享决策，但 t=3 可用完整历史。
S3 要求 t=3 时 AV0/AV1、BV0/BV1 各自共享决策，但 t=2 可用完整历史。
S23 同时施加两处约束。t=1 各类均可自由 STOP/CONTINUE；
t=4 可使用时间及 LR 作为终端签名（证明的全局下界允许 t=4 更自由地使用完整历史）。
令
\[
d_J(F)=\inf_{\sigma\in S_J}
\max_{R\in\{P,Q\}}\mathrm{TV}(\mathcal L_R^F(T,D),
\mathcal L_R^\sigma(T,D)).
\]

**定理（精确反例）：**
\[
\boxed{d_2(F)=1/3036,\quad d_3(F)=0,\quad d_{23}(F)=1037/1884240.}
\]
因此
\[
\boxed{d_{23}-d_2-d_3=105341/476712720>0.}
\]
同一棵树上此前 F_lambda 与终端 eta 族的严格次可加性仍成立；
本定理否定的是把那一局部性质推广到所有完整历史策略的全称猜想。

## 2. 可执行上界：标号因果占用而非错误凸化

对 t=2,3,4、原始标号历史 h 和行动 a 定义
\(u_{t,h,a}=\Pr(\text{到达后采取 a}\mid h\text{所在树分支发生})\)。
这是尚未乘 q_h 的占用概率，满足
\[
 \sum_a u_{2,h,a}=1,\qquad
 \sum_a u_{t,h,a}=u_{t-1,\mathrm{pa}(h),C}\quad(t=3,4).
\]
t=4 只允许 P/Q。记 \(s_{2,h}=1\)，
\(s_{t,h}=u_{t-1,\mathrm{pa}(h),C}\)。
在规定压缩的同一 (t,r) 纤维内，要求对全部动作 a
\[
u_{t,h,a}s_{t,k}=u_{t,k,a}s_{t,h}.
\]
这正是同**条件行为概率**约束；不同历史即使当前 LR 相同，
原始上游到达率也不能擅自合并。每个正的 s 用
\(\pi_{t,h,a}=u_{t,h,a}/s_{t,h}\) 重建合法独立即时随机策略；
s=0 的不可达历史任取合法动作。此重建不使用全局混合种子。

可观察的完整两律质量仍逐项保留：
\[
\mu_Q(t,D)=\sum_{h\in H_t}q_hu_{t,h,D},\qquad
\mu_P(t,D)=\sum_{h\in H_t}q_hr_hu_{t,h,D}.
\]
同层两律分别归一化，不能把有符号对偶权当作 BRC 正质量。

CERTIFICATES.txt 精确列出 S2、S3、S23 三份稀疏有理证书，
分别 30、28、30 项正占用值，其余动作占用为零；
VERIFY.py 逐节点验证非负、流量守恒、同纤维交叉乘一致性、
行为重建及全部十六项 Q/P 联合观察。所得真实上界是：

| 压缩类 | TV_Q | TV_P |
|---|---:|---:|
| S2 | 1/3036 | 1/3036 |
| S3 | 0 | 0 |
| S23 | 1037/1884240 | 1037/1884240 |

上界证书都选用 t=1 全继续；下界允许所有 t=1 行为。

## 3. 完整随机行为策略的对偶匹配下界

对每个有理双律观察权 W=(W_Q,W_P)，令
\(L_W(\mu)=\langle W_Q,\mu_Q\rangle+\langle W_P,\mu_P\rangle\)。
振幅和 \(\mathrm{osc}(W_Q)+\mathrm{osc}(W_P)=1\) 时，使用对两种概率律均成立的有界观察不等式：
\[
L_W(\sigma)-L_W(F)\le
\mathrm{osc}(W_Q)\,\mathrm{TV}_Q+
\mathrm{osc}(W_P)\,\mathrm{TV}_P
\le \max(\mathrm{TV}_Q,\mathrm{TV}_P).
\]
只需对所有同类策略证明 L_W 的全局最小值大于 L_W(F)。

两份精确观察权（依 Q 八坐标、P 八坐标连接顺序）：

S2 的 W_Q=(0,0,25/253,25/253,25/253,25/253,25/253,-25/253)；
W_P=(0,0,-203/506,-203/506,-197/506,-197/506,-197/506,203/506)。

S23 的 W_Q=(0,0,1293/13085,1293/13085,3736/39255,3736/39255,3871/39255,-1293/13085)；
W_P=(0,0,-10499/26170,-10499/26170,-30353/78510,-30353/78510,-30503/78510,10499/26170)。

对每项权设 \(c_W(t,r,a)=W_Q(t,a)+rW_P(t,a)\)。
在 t=4，先对每个叶的 P/Q 决策分别取最小；
t=3 则对 S2 的每个历史单独取
\(\min(c_W(3,r,P),c_W(3,r,Q),\text{该历史的最优续接成本})\)；
对 S23 把同 LR 纤维内这些历史的 Q 权重成本先相加，
再对该纤维的 P/Q/CONTINUE 三个共同行为取最小。
加上 t=1/2 已 STOP 的成本，并对
t=1 的 A、B 和 t=2 的 U(=AU/BU)、AV、BV
共 \(3^2\cdot3^3=243\) 个确定性前缀完全枚举。

为什么这证明所有**实数即时随机**行为？
每条样本路径在一个指定时刻至多经过一个给定信息集合；
线性观察值是各信息集合行为概率的多重仿射函数。
逐个单纯形变量取极值后，最小值必有确定性顶点达到。
上述枚举和 Bellman 递推是完整的顶点优化，不是仅检查243个普通样本。

精确 Fraction 结果：
S2 的全局 Bellman 最小值 -153/506，
而 F 的 L_W=-919/3036，差值为 1/3036；
S23 的全局 Bellman 最小值 -7913/26170，
而 F 的 L_W=-570773/1884240，差值为 1037/1884240。
两个下界均匹配第二节的真实行为上界。
S3 有零误差可执行证书，TV 非负推出 d3=0。定理得证。

## 4. 改变上游真实生存率之后仍严格超可加

令 F_epsilon 在 t=2 的 AU 把
(1/2,1/6,1/3) 改为
\((1/2+\epsilon,1/6,1/3-\epsilon)\)，其它动作不变，
\(0\le\epsilon\le1/10000\)。这是真正改动 STOP/CONTINUE，
未来 t=3/4 的到达概率也发生变化，不是最终判定的同 LR 置换。
AU 在 Q/P 下均有质量 1/6，因此
\[
\max_R\mathrm{TV}(\mu_R(F_\epsilon),\mu_R(F))=\epsilon/6.
\]

对任一合法策略图像集合 C，度量空间到集合的距离
\(d_C(y)=\inf_{z\in C}\rho(y,z)\) 恒为1-Lipschitz；
这里 \(\rho=\max(\mathrm{TV}_Q,\mathrm{TV}_P)\)。
所以三项误差组合差 G=d23-d2-d3 满足
\[
G(F_\epsilon)\ge G(F)-3\epsilon/6
\ge 105341/476712720-1/20000
=\boxed{20376341/119178180000>0}.
\]
这在完整实数参数区间上成立，不是浮点样本外推。

## 5. 验证、边界与后续

运行 Python 3 标准库命令：
python VERIFY.py
会用完整标号 Q/P 质量重建 Law(T,D)，核验三套有理占用，
对 S2/S23 各执行243个精确前缀 Bellman 检查，
打印 PASS_EXACT_FRACTION_N4_TRUE_TV_SUPERADDITIVITY。
SciPy 仅在寻找候选证书时使用；已发布验证不依赖 SciPy 或浮点数。

BRC 实际复用正分支质量、历史来源、似然比、两律守恒、
因果占用和未来操作观察保真要求。所有时间 t 是外部序贯步骤，
未构造 Heartbeat World 原生六维 X6 Cell、独立时间更新和
三维切片的保真观察桥；不得将本外部结果提升为 P000 原生命题。
独立 Driver 评审、External-prior-art 去重和 Source 正式 Result 仍属后续。
原生 Owner 查询 CONTROL_QUOTA，own-session 登记
STATIC_READONLY_SCOPE_DENIED (operation_sent=false)；
GitHub 已认证用户 awdawmip 可以提交作者侧科研工件，
但该权限并不等于原生 CLAIM 或数学准入。
后续精确任务见 NEXT_TASK.md。
