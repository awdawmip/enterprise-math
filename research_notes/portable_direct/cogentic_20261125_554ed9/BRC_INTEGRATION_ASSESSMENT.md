# Cogentic 工具进入 BRC 的价值判断与两个精确说明例

日期：2026-11-26（Asia/Hong_Kong）。Researcher-ID：`EM-DIRECT-554ED9 / TASK_RESEARCH`。Research-Activity-ID：`RA-226AABA6B251DC420A415238`。

证据范围：基于先前已经取得并校验的十篇原文、已保存局部推导和精确计算，再对照当前 BRC 源码定义。本轮新增两个说明性例子的精确有理核验，不作新颖性主张，不宣称已审定原论文全部主定理，不修改 Foundation、Working Truth 或已有任务。下文优先级是本轮研究判断，不是状态机优先级变更。

科学定义快照：`awdawmip/enterprise-math@38ec2dc06dbbed82b730aa54c454886099506595`。普通研究 Foundation 投影的五个来源 blob 均与原文件元数据一致。P000、Heartbeat X6、联合关系及残差保真按该快照使用；分支、权重、标签、有限域、矩阵与概率分别按类型解释，不增加空间轴。

## 一、结论

最值得先补入 BRC 共享研究工具的是：低阶摘要的失真证书、面向真实未来目标的观测选择、保旧观察的合法增量构造、整数更新及核坐标恢复。Bézout 模环消元具有明确的辅助计算价值；Moore 独立性和 Walsh 正性适合条件明确的专题模块。多尺度能量工具在 RH/派生残差诊断中有价值，不能由滤波稳定推出分支系统稳定。

| 工具 | BRC 中的作用 | 当前建议 |
|---|---|---|
| 低阶矩湮灭、Vandermonde 分离 | 构造“同摘要、不同目标观察”的精确证据，定位需保留的联合残差 | 最高优先：可作共享诊断/回归工具 |
| 熵增、条件候选对分离 | 给允许新增观测排序，研究成本—未来误差关系 | 高优先：评分已可用；目标保真和算法保证另外证明 |
| 祖先消失因子、观察核内扰动 | 在保留已承诺观察的同时扩展证书或新增合法约束 | 高优先：补构造方法、合法性和代价证书 |
| 下降二项式基、无除法预像、核恢复 | 精确移位/累计，区分方程障碍和遗漏状态 | 高优先的条件方法；实际算子需匹配 |
| Bézout 模环消元 | 解有限模辅助观察与 CRT 线性相容性 | 可直接用于符合假设的算术后端 |
| Moore 行列式、兼容 Walsh 正性 | 特定有限域独立性或群表示一致性证书 | 条件调用，不强加到全部 BRC 对象 |
| 多尺度滤波、有限窗耗散 | 诊断尺度差异、边界和残差能量 | 应用层工具，优先沿既有 RH 任务验证 |

## 二、BRC 已有的结构必须作为起点

当前 R023 Boolean BRC 已有未来观察安全的分支/重聚语义，并明确当前粗读数相同不保证后续安全。正权层有 CWM 半环，显式正有理分支的精确载体为有限直方图

\[
H=\sum_q c_q[q],\qquad \mathcal H=\mathbb N[\mathbb Q_{>0}^{\times}],
\]

\[
C=\sum_qc_q,\quad W=\sum_qc_qq,\quad
M=\max\{q:c_q>0\},\quad P_m=\sum_qc_qq^m.
\]

现有 WBRC-T34 已说明：原始平行枝数 r 已知时，P0=r 与 P1,…,Pr 可恢复无标签权重多重集。Port 转移、固定矩与长度参数、Newton 观察核/有限日程接口也已存在。因此，外部材料的价值应落在更可构造的证书、计算方法和真实成本上，不重复包装这些已有结构。[S1–S5]

## 三、最有直接作用：低阶摘要失真证书

《Edge Reconstruction》Theorem 4.2(1)，pp.24–25：若 N 次齐次多项式 P(y)=Σc_u y^u 满足共同平移不变性 P(y+z1)=P(y)，则

\[
\sum_u c_u R(u)=0\qquad(\deg R<N).
\]

局部证明通过低阶导数及下降阶乘基得到，先前提取已手工核对。它提供系统构造低阶观察盲区的方法，而不仅是一个孤立例子。[C1]

### 本轮直接构造的正权 BRC 例

Vandermonde 正、负指数支撑分别为
{(2,1,0),(1,0,2),(0,2,1)} 与 {(2,0,1),(1,2,0),(0,1,2)}。
取 L(u)=2u2+3u3，将它们推送成 {2,6,7} 与 {3,4,8}；再各加入同一主导权 9，得

\[
H_+=[2]+[6]+[7]+[9],\qquad
H_-=[3]+[4]+[8]+[9].
\]

| 观察 | H+ | H− |
|---|---:|---:|
| C | 4 | 4 |
| W=P1 | 24 | 24 |
| M | 9 | 9 |
| 主导重数 d | 1 | 1 |
| P2 | 170 | 170 |
| P3 | 1296 | 1332 |

因此，若声明的目标包含 P3，`CWM + Lead + P2` 不足以合并这两态。若目标仅为 CWM 且允许操作保持该商，本例不强制保留 P3。两个 H 都是正权分支态；加减号只区分两个系统，不是负质量分支。

还可把所有权重除以100，作为单状态的四条平行自环。两系统的总质量矩阵都是 [6/25]，h=1 是稳定证书；但三阶一步矩分别为 81/62500 与 333/250000，长度 n 的三阶路径矩分别是这两个数的 n 次幂（复用 T33）。这把“同总质量、同稳定性但不同矩观察”直接放进现有递归 BRC 对象。[S2,S3]

全部数值本轮用 Fraction 精确核验，脚本与结果见文末。新增价值是可执行的盲区证书，不是对 T34 有限矩完备性的否定。

## 四、观测选择：熵增有价值，验收必须对应真实目标

《Near-Quadratic Sample Compression》Lemma 4.4，pp.17–18：对明确的候选权重 π，已有观察分区 τ 的质量为 πτ，新观察 h 把该类分成条件质量 qτ,j，则

\[
\Delta H\ge G(h\mid\mathcal O),\qquad
G(h\mid\mathcal O)=\sum_\tau\pi_\tau
\left(1-\sum_jq_{\tau,j}^2\right).
\]

右侧是对旧类条件独立抽样的候选对被分开的平均概率。有理权重时可全程精确算分，不必计算对数。它适合给新 Port/通道/联合观察排序，并可研究 G/成本。[C2]

### 本轮满支持、等成本反例

候选 a,b,c 的权重为 (1/2,1/3,1/6)，旧观察常量，真正要恢复的目标为 g(a)=g(b)=0、g(c)=1。允许两项成本均为1的观察 h1=1_{a}、h2=1_{c}。

| 新观察 | 新二分质量 | 熵增（bits） | 候选对分离概率 | 同签名内最坏目标差 |
|---|---|---|---|---:|
| h1 | (1/2,1/2) | 1 | 1/2 | 1 |
| h2 | (5/6,1/6) | H2(1/6)<1 | 5/18 | 0 |

所有候选都有正权、成本相等，熵增和总分离评分仍都偏好 h1；但只有 h2 完成目标。数值与候选对枚举已精确核验；熵比较来自二元熵在1/2的唯一最大性，无需浮点。

所以值得引入的研究对象是：在允许目录与成本下减少真正的未来目标误差，例如

\[
E_{\mathcal L}(\mathcal O)=
\sup_{S_{\mathcal O}(x)=S_{\mathcal O}(y)}
\sup_{g\in\mathcal G_{\mathcal L}}|g(x)-g(y)|,
\]

并保留操作合法性差异、单位、时域和噪声语义。熵与分离概率是可比较评分，最终用现有预测商/闭包/完整有限状态基线判定保真。对任务重要候选对加权是值得测试的修正方向；这里未宣称通用近似比。

### BRC Δ 与 Shannon 熵的准确联系

对每个正分支 q_i，已有 Δ=ln(W/M)。如果另行定义质量抽样 p_i=q_i/W，则

\[
\Delta=-\ln\max_i p_i=H_\infty(p)\le H_{\rm Shannon}(p).
\]

候选对象先验 π 与这个分支质量抽样 p 是两种不同数据。两个等重自环若每条权为1/4或3/4，都有 p=(1/2,1/2)、Δ=ln2、Shannon熵=ln2，但总质量分别为1/2和3/2，一者稳定一者发散。当前 BRC 的有限非负有理矩阵稳定判据仍是存在正有理 h 使 Wh<h。[S1,S3]

## 五、保旧观察的合法增量构造

《Integer Factorization》Lemmas 4.4、4.6，pp.35–40 的祖先消失因子

\[
P_{\rm anc}(X,Y)=\prod_t(b_tX-a_tY),\qquad
\delta f=P_{\rm anc}H
\]

保持每个旧求值点。对已有合法线性辅助表示，这启发具体构造

\[
c'=c+\delta,\qquad A_{\rm old}\delta=0,
\qquad c'\in\mathcal C_{\rm legal}.
\]

若承诺保持所有允许未来词，条件相应是 δ∈∩_w ker(OT_w)，而不只是 Oδ=0。合法生成器可达、正权/整数性、标签来源及资源成本需要实际证明。这与现有 T57/T58 观察核结构衔接；新增价值在可实现的核内构造，而非重复“安全商”原则。[C3,S4]

Riesel 已有 a'=a+tM 的具体接口：F_n(a')−F_n(a)=2^n(2atM+t²M²)，全部旧模M读数保持。新 q∤M 且合法根 r 已取得时，用 t≡(r−a)M^{-1}(mod q) 接入新通道。取得根、阶和通道的代价仍计算。多通道受同一 n 驱动，不能当作独立新增空间轴。[C0]

## 六、整数更新与残差恢复：分清余核和核

《Fictitious Play Convergence》Lemmas 7–10（pp.18–19）使用下降二项式基和幂零 J：

\[
b(k+1)=(I-J)^{-1}b(k)=(I+J+\cdots+J^\ell)b(k).
\]

有明确多项式更新结构时，可以用整数矩阵完成精确移位与块求和。Definition 7、Lemmas 13–16（pp.20–22）对

\[
\mathcal T_\ell(P)=P^T-(I-J)^TP
\]

构造只用加减的预像 Sℓ(Z,φ)，余核障碍 R(Z)=TℓSℓ(Z,0)−Z 仅在 {(2r,0)} 上非零；另有精确恢复

\[
\mathcal S_\ell(\mathcal T_\ell(A),\phi_A)=A.
\]

**余核障碍 R(Z) 判断目标方程可解性；核坐标 φ_A 保存读出之后遗漏的状态。** 对真实读出 Z=Tℓ(A)，R(Z)=0，但 A 未必唯一。例如 Tℓ(0)=Tℓ(Eℓℓ)=0，而核坐标不同。故“求解残差归零”不能作为“未来相关结构残差消失”的证明。[C4]

这适合 BRC 的整数累计、内部记忆与精确解码研究。实际更新必须有相应算子结构，才能复用稀疏位置结论；一般 BRC 算子不能直接套用。完整恢复的总自由度没有自动减少，稀疏也不等于小数值。先前 ℓ=2,…,6 全矩阵基的验证仍只是其明确范围的检查。

## 七、条件计算工具与专题模块

### Bézout 模环消元

DLP Lemma 6.3(2)，p.31：d=su+tv=gcd(u,v)>0 时，

\[
U=\begin{pmatrix}s&t\\-v/d&u/d\end{pmatrix},\qquad
\det U=1,\qquad U(u,v)^T=(d,0)^T.
\]

关系矩阵在每个 p|M 上满列秩时可用这类操作消元，无需预分解模数；一般右端还要检查相容性。模6矩阵 [[2,3],[3,2]] 没有任何单位元素，却整体可逆，已在原提取中精确复算。适合BRC明确的有限模/CRT辅助约束；负系数属于方程变换，不是负枝质量，也不能以模同余证明 Wh<h 等有序不等式。[C5]

### Moore 与 Walsh

DLP Lemma3.1（pp.10–11）：在真正扩域 K⊇Fq 中，Moore 行列式 det(z_i^{q^{j−1}}) 非零当且仅当 z_i 对 Fq 线性独立。它可验证特定有限域编码的新关系独立性；只在基域中取标量时不能产生所需扩域秩。[C5]

Deterministic Factoring Lemma5.1（pp.20–22）的可分离代数工具是兼容群表示的 Fourier 正性：在 F2^K 上，f(ℓ)=Σa_u(−1)^{ℓ·u}、g(ℓ)=Σb_u(−1)^{ℓ·u}，a_u,b_u≥0，则 Σℓf(ℓ)g(ℓ)=2^KΣ_u a_ub_u≥0。适合经过认证的联合符号结构；任意拼接边际符号不具有这个结论，代数符号也不成为正质量路径的相消。[C6]

### 多尺度滤波

NASH Lemma3.1（pp.15–16）给出指数核耗散结构；先前提取另推导了离散带权有限窗恒等式，含尺度方差、时间增量与完整初末边界。适合派生标量残差的能量诊断，尤其已有 RH 的1/n²权问题。滤波参数ρ<1只控制该滤波器，不给 BRC 质量矩阵的稳定性、Port安全或完整直方图保持结论。使用现有 RH 任务比较完整支付后的实际收益。[C0,C7]

## 八、哪些内容保留为外部参照

完整分解/DLP复杂度、完整VC压缩大小、1/5近似Nash、logrank通信复杂度以及凸博弈黑箱查询下界，都依赖各自的输入、oracle、代价与输出语义。它们可启发专题研究，不直接提供通用BRC塌缩/提取算法。完整VC重构还可能输出代表概念的加权多数票，不保证输出某个合法原BRC状态。

特别保留实际成本：平滑权重评估在F-LV Lemma3.5（pp.18–19）以完整因数分解已给出为前提；DLP Lemma6.4（pp.31–32）在有成本的Descent已经给出群坐标后才作廉价gcd恢复。F-DET Lemma11.1（p.55）的饱和给消去指数，不自动给精确阶。这些都不能在BRC比较中免费调用。[C3,C5,C6]

## 九、与已发布任务衔接

本轮不新增重复任务。上轮已发布：

- `RS-COGENTIC-OBSERVATION-COMPLETION-COST-20261126`：承接本评估最有通用价值的观察选择与误差—成本部分。
- `RS-COGENTIC-RIESEL-CHANNEL-SELECTION-20261126`：承接合法核内扩展的具体算术应用。
- `RS-COGENTIC-RH-MULTISCALE-ENERGY-20261126`：承接多尺度的完整误差/成本比较。

它们的已验证发布提交为 `3c7e16ce8718eca48e2236520a7da748e94543fe`；本评估不宣称其当前执行状态仍与上轮读回相同。本文新增例子可被这些任务引用，不是替代它们的正式成果或审查。

## 复算

同目录 `brc_integration_verify.py` 只用 Python 标准库 Fraction；运行 `python brc_integration_verify.py`，输出应与 `brc_integration_verified.json` 一致。检查正权四分支例、缩放单状态递归例以及满支持三候选观测反例的全部有理计数。没有重新执行十篇论文完整算法或Lean证明。

## 固定来源

- [S1：Weighted/Log BRC，CWM、Δ、未来安全商](https://github.com/awdawmip/enterprise-math/blob/38ec2dc06dbbed82b730aa54c454886099506595/definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md)
- [S2：Universal histogram，T33–T38](https://github.com/awdawmip/enterprise-math/blob/38ec2dc06dbbed82b730aa54c454886099506595/definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md)
- [S3：Finite recurrent BRC，Wh<h及整数证书](https://github.com/awdawmip/enterprise-math/blob/38ec2dc06dbbed82b730aa54c454886099506595/definitions/ENTERPRISE_BRC_FINITE_RECURRENT_FOUNDATION_20260902.md)
- [S4：Newton observer lattice，T57/T58](https://github.com/awdawmip/enterprise-math/blob/38ec2dc06dbbed82b730aa54c454886099506595/definitions/ENTERPRISE_BRC_NEWTON_OBSERVER_LATTICE_FOUNDATION_20260904.md)
- [S5：R023及共享研究接口](https://github.com/awdawmip/enterprise-math/blob/38ec2dc06dbbed82b730aa54c454886099506595/docs/RESEARCH_COMMON_SURFACE.en.md)
- [S6：Residual fidelity](https://github.com/awdawmip/enterprise-math/blob/38ec2dc06dbbed82b730aa54c454886099506595/definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json)
- [C0：此前完整提取、局部证明及核验范围](https://github.com/awdawmip/enterprise-math/blob/b00f6cef0711ccc285106b7fb00d93e8fd808662/research_notes/portable_direct/cogentic_20261125_554ed9/REPORT.md)
- [C1：Edge Reconstruction](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/edge_reconstruction/paper.pdf)
- [C2：Near-Quadratic Sample Compression](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/vc_sample_compression/Near_Quadratic_Sample_Compression.pdf)
- [C3：Integer Factorization](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization/paper.pdf)
- [C4：Fictitious Play Convergence](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/fictitious_play_convergence/Fictitious_Play_Convergence.pdf)
- [C5：Discrete Logarithms](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/discrete_logarithm/paper.pdf)
- [C6：Deterministic Factoring](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/deterministic_factoring_l34/paper.pdf)
- [C7：Bimatrix Nash](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/bimatrix_nash_equilibrium/paper.pdf)
