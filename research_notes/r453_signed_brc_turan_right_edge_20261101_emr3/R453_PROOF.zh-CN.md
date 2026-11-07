# R453｜signed BRC 右边缘119位的无限参数局部 PF₃ 证书与 Turán 恒等式

2026-11-01。作者侧计算机辅助精确数学研究。UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。P000、ACTIVE 世界观、正式 CLAIM/Result 未改。

## 模型与结果

沿用 R450–R452 原始 signed BRC 辅助标量模型，奇数 r=2k+1，a_s=H(r,s)，支持外取零。C_k=binom(2k,k)/(k+1)。此前已证原始带符号卷积与以下 Catalan 正式表达等价：

H(2k+1,s)=binom(2k+1+s,2s) Σ_{q=0}^{floor((s−1)/2)}binom(s−1,2q)4^q C_{k−q}.

定义 D2_s=a_s²−a_{s−1}a_{s+1}，D3_s=det[a_{s+i−j}]_{0≤i,j≤2}。它们对应此前列 j=r−s 的相邻 Toeplitz 子式（取转置不影响 determinant）。

**本轮新精确计算机辅助定理：**每个整数 101≤s≤120、每个整数 k≥floor((s+2)/2) 均满足 D2_s>0,D3_s>0。每个新 s 的结论覆盖无限多奇数 r，不是有限 r 抽样。合并前一 R452 的 2≤s≤100 证书，对每个奇数 r≥123，最右边 119 个合法位置 s=2,…,120 全部获得相邻二、三阶严格正性。对较小 r 只覆盖满足其各自物理下界的位置。

这仍不是完整半无限 PF₃ 定理；对任意 s≥121 无统一证明，也无原生 X6/heartbeat typed 保真映射。

## 一、精确 Turán–Dodgson 恒等式

任意序列 a_s 都满足

a_s D3_s=(a_s²−a_{s−1}a_{s+1})²−(a_{s−1}²−a_{s−2}a_s)(a_{s+1}²−a_s a_{s+2}).

证明：Desnanot–Jacobi 3×3 行列式凝缩式中，中心元为 a_s，中心 2×2 子式为 Δ_s=a_s²−a_{s−1}a_{s+1}，交叉的两个 2×2 子式分别为 −Δ_{s−1}、−Δ_{s+1}。代入即得；亦可直接展开五项。由原模型 a_s>0，可知 D3_s>0 当且仅当 Δ_s²>Δ_{s−1}Δ_{s+1}。在 Δ 本身严格正的区间，二阶和三阶局部正性等价于 a_s 及其 Turán 变换 Δ_s 的严格对数凹性。这是经典恒等式的具体再利用，不将其一般形式冒称新发现。

## 二、无限 k 的整数多项式证书

从 R452 的全部 s 因子分解起步，令 B_s(k)=H(2k+1,s)/C_k、m=floor((s−1)/2)，则

(2s)! B_s(k)=E_s(k)O_s(k)R_s(k),

E_s(k)=Π_{v=0}^{s−1}2(k+1−floor(s/2)+v),
O_s(k)=Π_{v=0}^{floor(s/2)}(2k+2v+1),
R_s(k)=Σ_{q=0}^{m}binom(s−1,2q)2^q Π_{t=q}^{m−1}(2k−2t−1) Π_{d=0}^{q−1}(k+1−d).

空乘积=1。每个 s 令 k0=floor((s+2)/2)、u=k−k0≥0、F=(2(s+2))!，取 Q_t(u)=F B_t(k0+u) (t=s−2,…,s+2)，设 A=Q_s, B=Q_{s−1}, C=Q_{s+1}, D=Q_{s−2}, E=Q_{s+2}。构造精确整数多项式

P2=A²−BC；P3=A³−2ABC+DC²+B²E−DAE。

严格等式 D2_s=C_k² P2/F²、D3_s=C_k³ P3/F³。实际整数算法完整计算 101≤s≤120 共40个多项式，逐个证明所有系数严格正。各阶次数精确为 4s、6s；总正系数数目为 Σ(10s+2)=22,140。因此对所有 u≥0 证成定理。没有浮点和数值外推。

另外对每个 s 直接检验 Z[u] 恒等式 A·P3=P2_s²−P2_{s−1}P2_{s+1}，其中邻位 P2 以同一个 F,k0 构造，共20次完整整数多项式等式。300项独立原始带符号卷积交叉检查覆盖每个 s 的 k=k0,k0+1,k0+2 和 t=s−2,…,s+2。有限交叉检查不承担无限参数推断。

实际执行分批为 101..107、108、109..114、115..118、119..120；只统计完成且有逐行哈希的20项。完整逐行系数 SHA256 及可重建编码在 R453_EVIDENCE_ALL.json 中，20项顺序合并哈希为 41b09ac261daf937f829d87f3479c584e72d28660a018e9a3a3788cabae078c2。R453_VERIFY.py 可分块确定性重建每项所有大整数系数，不依赖 SymPy / 随机数。

## 来源、权限、接续

原始 R452 公式与证书：PR #1708 提交 8e2d954a18eb8e3e27790d92cb9052c9107d691e (R452_PROOF.zh-CN.md, R452_CHECK.py)；R450 早期局部 PF3 判据：6d79677bda1fbce91c8b5f5af70dc830a33bd9dd。输入固定 GLOBAL_KNOWLEDGE_V1 main@ed55d1088122e12a27c271b8e2b5a8642fd5a8a2、Enterprise Math main@7a793b696f7933bd83b88f7a5c633d3c7281e089。P000 ACTIVE_LOCKED / ACTIVE Heartbeat X6 不作改变。

GitHub 身份 awdawmip；原生 Sites 为静态只读、research_authority_granted=false，活跃 owner 查询返回 CONTROL_QUOTA；不能推出无人拥有任务，也没有正式 CLAIM、Result、Driver Review 或项目数学接纳。

下一数学单元：把 Δ_s²−Δ_{s−1}Δ_{s+1} 与 E_s O_s R_s 结构结合，证明任意 s 的系数或数值正性，消除逐 s 枚举；或从 s≥121 找出首个非正多项式系数，进一步辨别证书方法失败与真正负子式（后者才是数学反例）。保留 signed cancellation 与原生 X6 保真对应的未解问题。
