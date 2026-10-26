# PREFIX-275｜固定全开来源路径的C4-BRC层析：最少探针与不可见对角残差

状态：AUTHOR_SIDE_EXACT_PROOF / LOCAL_EXACT_VALIDATION_PASS / NATIVE_TRANSFER_PENDING / NOT_ADMITTED。日期：2026-10-27。此文为作者侧研究，不是原生任务状态机中的正式Result或真实心跳演化实验。

## 1. 来源、问题及边界

本轮冻结 GLOBAL_KNOWLEDGE_V1 main@59e3da7b1c0781ca47152f09faaa5e5af0ae73b4，Enterprise Math科学输入 main@c317e3a87685f1e6b089e9d9b808404ad6c26ab2。已按现行00_BOOTSTRAP、OPERATING_MANUAL、EM项目路由、P000原件、P000_STARTUP、ACTIVE世界观、PORTABLE_RESEARCH_PROTOCOL、BRC-only算术及研究注册协议读取。P000六维原生离散Cell空间+独立时间、三元原始力闭合及无原生平面起点不受本文改变。路径数k不是空间轴数。

精确复用既有Stage50来源文件 research_notes/HEARTBEAT50_INTERFERENCE_KERNEL_20260923_6DD798.md (Git blob 0f4ec78225cfc799a267ca6b96d9f994422f8ad2)，其完全带来源Gram及双端口C4外部读出；继承 PREFIX-274 仅Z2不能恢复复Gram虚部的证明。此处研究的是一个【声明的形式效应语言】，并未证明真实原生Source允许任意k条路径的独立C4控制。SOURCE原有 src/enterprise_math/brc_weighted_recurrent.py@c317e3a8 (blob 4e6b3132580e3cd70a20a0d8bd4d28792b961afb) 提供正有理总质量，不可冒充相位抵消的原始执行器。

## 2. 有序来源路径对的精确语义

取 k>=2，来源路径标签1..k，固定有理正幅值m_i>0，固定一个检测端点/准备背景的Hermitian PSD Gram矩阵 Γ∈Herm_k(Q(i))。假设所有k条路径一直开启，不允许置零；唯一可选的是逐标签相位s_i∈{1,i,−1,−i}，改变相位不改变Γ。保存全部有序路径对(a,b)，定义

I_Γ(s) = Σ_(a,b) m_a m_b conjugate(s_a) s_b Γ_ab ∈ Q_>=0.

这是声明的Stage50型路径对BRC读数而非直接从P000导出的物理概率。令
D=Σ_a m_a² Γ_aa，
B_ab=2m_am_b Re(Γ_ab)，C_ab=2m_am_b Im(Γ_ab) (a<b)。
置 u_ab+i v_ab=conjugate(s_a)s_b。成对展开得到

(1) I_Γ(s)=D+Σ_(a<b)[u_ab B_ab−v_ab C_ab].

全部k路共享全局相位规范，固定s_k=1即可。可观测线性参数数 d=1+k(k−1)。

## 3. 定理A：全部C4可用时，严格观察等价类的核

对两个Hermitian PSD矩阵Γ与Λ，所有4^(k−1)个相对C4读数相等，当且仅当
(i) Γ_ab=Λ_ab 对所有a≠b；
(ii) Σ_a m_a² (Γ_aa−Λ_aa)=0。

从(1)得充分性。必要性由下述定理B构造满秩d个读数、逐项反演D,B,C；因m_a>0，可恢复全部非对角复数条目，剩余只是一个对角带权和。故不可见差矩阵的精确线性核为
K={diag(δ_1,...,δ_k): Σ_a m_a² δ_a=0}，维数k−1。

严格正定性亦不足以消去该核：m=(1,1)，Γ=diag(1,1)，Λ=diag(3/2,1/2)均正定；任意C4相位固定全开读数均为2，单路径读数不同(1与3/2)。非零残差不是计算噪声，而是对此观察操作族的真实失辨；新增未来操作会改变这个结论的范围。

## 4. 定理B：恰好1+k(k−1)个全开C4探针的显式最优设计

固定s_k=1。先做Z2准备：基准s≡1，单独翻转各i<k，以及同时翻转任意1<=i<j<k；共1+binom(k,2)次。记录e=I(基准)，e_i=I(翻i)，e_ij=I(翻i,j)。二阶差分和一阶关系精确给出：

B_ij = (e_ij−e_i−e_j+e)/4  (i<j<k)，
B_ik = −(e_i−e)/2 − Σ_(j<k,j≠i) B_min(i,j),max(i,j)，
D = e − Σ_(a<b) B_ab.

再做C4准备。逐行i=1..k−1，令s_i=i，其余+1，形成一次z_i^0；对每个i<j<k再令s_j=−1，形成z_i^j。把相应真实强度减去已知的D和与i无关的实交叉项Σ_(a<b,a,b≠i) s_a s_b B_ab，所得差数仍记z。这些准备的有序路径对中，i参与的交叉相对相位纯虚，其他交叉纯实。于是
z_i^0 = Σ_(j>i) C_ij − Σ_(j<i) C_ji，
z_i^j = z_i^0−2 C_ij，
C_ij=(z_i^0−z_i^j)/2 (i<j<k)，
C_ik=z_i^0+Σ_(j<i) C_ji−Σ_(i<j<k) C_ij。

共增加binom(k,2)次，反演全部带标签复交叉项。总探针数
(2) N=1+binom(k,2)+binom(k,2)=1+k(k−1)。

最少性只对【一般严格正定Hermitian Gram的全部可观测线性商】而言：参数(D,B,C)在正定锥的开邻域独立取值，每次固定相位只给一个实线性方程；若少于d次，测量算子在d维商上有非零核。取足够大的正对角基准加足够小的Hermitian差矩阵，两种结果仍正定、已测相同，而定理中的满秩设计能区分该核向量。故普适线性商恢复至少d次，构造达到下界。它不是离散rank-one相位承诺、单次二值判别、非线性编码等其他问题的无条件下界。

## 5. 定理C：可合法隔离路径时完整Gram恢复

在【单独隔离路径不改变同一个Γ】的额外假设下，再取k−1个单路径读数，恢复相应Γ_ii，最后一个由D恢复，合计 d+k−1=k² 次恢复完整Hermitian Gram的k²个实系数。一般正定Gram的每个标量强度读数对Γ线性，故少于k²次不能普适线性完全重建。若隔离改变Source、边界、detector或准备历史，从不同Γ混合读数无效。

k=6条【来源路径而非六个空间轴】：全相对相位1024种；固定全开31次(16 Z2+15 C4)能恢复D+15个Re+15个Im，但不能恢复5个独立对角残差；额外五条保持Γ的隔离读数使总数36次。

## 6. 精确验证与证据

同轮作者侧verify_prefix275.py使用fractions.Fraction、二元Gaussian rational以及显式全部有序路径对累计；Γ由Q(i)^(k+2)的私有路径单位坐标+公用残差载体生成而严格正定。对k=2,3,4,5,6分别精确枚举4、16、64、256、1024个C4准备；校验路径对与反演恢复全部B,C,D的读出一致，总1364个准备。设计行矩阵整数Bareiss行列式依次为−2、32、−4096、4194304、−34359738368，皆非零。二路径对角正定失辨反例通过。

Stage50来源声明的双端口外部公式 p_external(r,p)=5/18*(1−Re(i^p c_r)) 在 c_r=i/2 时得到p=0,1,2,3依次5/18、5/12、5/18、5/36；这是文献中声明的接口公式的独立精确回归，不是Stage46原始导入。实际原始Stage46导入、原生model_law_id、真实Source相位门合法性、完整H_n→H_(n+1)与独立审查【均未执行/未核准】，不可由形式PASS替代。正权BRC与C4路径对幅值严格分型。

## 7. 控制权限与下一步

当前GitHub认证身份awdawmip有repo push权限；原生em_session_start请求被 STATIC_READONLY_SCOPE_DENIED(operation_sent=false)拒绝，em_control_tasks报告CONTROL_QUOTA。因此活跃Owner/CLAIM未可靠核实；当前只允许作者侧研究和GitHub有来源储存，未取得正式Task/Result/Driver数学接纳，不以Drive绕过原生访问拒绝。

实际已读 HEARTBEAT_WORLD_NATIVE_X6_TIME.json 的 fixed_heartbeat_program=null，HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json要求model_law_id字段却并未定义完整可执行演化律。这说明【已核查的两项契约】存在指定转接缺口，不证明整个未来系统不存在合法动力学。PREFIX-276要取得原生有来源model_law_id、相位准备与来源路径端口动作，再计算其真实可执行探针矩阵的秩、零空间和非零PSD邻域失辨证书，运行原始Stage46入口并回读stdout证据。直到合法性建立，31次仅是条件性数学设计。

经典复极化恒等式与相干四相读出本来已有先例（例如 https://proofwiki.org/wiki/Polarization_Identity/Complex_Vector_Space/Corollary 和 https://pmc.ncbi.nlm.nih.gov/articles/PMC7901320/ ）。不把一般极化思想冒称本轮首创，也不把本文形式模型当物理发现。

SOURCE PINS: Global main 59e3da7b1c0781ca47152f09faaa5e5af0ae73b4; EM input main c317e3a87685f1e6b089e9d9b808404ad6c26ab2. 研究文件可独立核对，Local complete version见当轮交接包。
