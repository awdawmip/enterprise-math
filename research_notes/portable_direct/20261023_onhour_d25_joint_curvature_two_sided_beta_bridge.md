# D25/LIFT — 双向二阶曲率的有限 Beta 证书及原 LOW 二阶联合标量缩减

**2026-10-23 / TASK_RESEARCH / portable exact rational mathematics.** 作者推导、精确分数自检：**AUTHOR_PROOF / EXACT_RATIONAL_SELF_CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**。不是 Source 注册、CLAIM、run、正式 checkpoint、Result/freeze、独立审阅或 native benchmark 完成。

**来源与不可变约束。** Research 来源逻辑标识 chatgpt-research-onhour-enterprise-math-20260923（仅为该 lane 来源，不是当前 Source 身份凭证），不属于 CONTROL_PLANE_MAINTENANCE。母目标 RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT，任务 TP2-B6F4FC938FF94941C1B7；冻结原 Source pin c47e13e4aba0e006366f989d6334d443f6333ae3，**不随项目 current-main 漂移**。复用而不重新证明：原 D24/LOW/Beta 和 WZ/B11、20261023_onhour_d25_BC_mirror_second_digit_transfer.md @ 45f127fee1f2f506fee5b448f90acebcf0fe17d4、20261023_onhour_d25_reflection_curvature_single_beta.md @ 67538d64a044e9899b96b2d14d83507fc52bb0e0、20261023_onhour_d25_LOW_Ablock_parity_exact_collapse.md @ 25f291ca9ad309e0e70c0935cbc64f440202633e、20261023_onhour_d25_J2_scalar_holonomic_modp_reduction.md @ 1a3790a15ab9366feccffc0105bdb24e5c4500d5。规范读快照 GLOBAL_KNOWLEDGE_V1 main@61cfa2a580230863c0d02b5f818381adbb3cb11b；P000 ACTIVE_LOCKED 原 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc 已核对。本笔记的积分是外部精确有理数工具，不产生原生 X6 语义或新公理。

## 1. 新的全整数恒等式：左反射 U₂ 曲率的单和

令 m≥1，p=6m+1（下列 **精确恒等式无须 p 为素数**），定义

\[
b_n={(-1)^n\over2^n}{m\choose n},\quad
w_n=6n-1,\quad
U_{2,n}=H_{2m}^{(2)}-H_{2m-n}^{(2)},\quad
V_{2,n}=H_{2m+n}^{(2)}-H_{2m}^{(2)},
\]
\[
a_j={(-1)^j\over2^j}{m-1\choose j},\qquad 0\le j<m.
\]

左、右 signed second-curvature observer 分别为
\(\mathcal U_m=\sum_{n=0}^{m}b_nw_nU_{2,n}\) 与
\(\mathcal V_m=\sum_{n=0}^{m}b_nw_nV_{2,n}\)。定义不含嵌套调和数的两个端口

\[
Q_m^-:=\sum_{j=0}^{m-1}{a_j\over(2m-j)^2},\qquad
Q_m^+:=\sum_{j=0}^{m-1}{a_j\over(2m+j+1)^2}.
\]

**新定理（LEFT-CURVATURE-EXACT）：**
\[
\boxed{\mathcal U_m=Q_m^-+{p\over2}E_m^-},\qquad
\boxed{E_m^-:=-\sum_{j=0}^{m-1}a_j
          \sum_{k=1}^{j+1}{1\over(2m-k+1)^2}.}
\tag{1}
\]

此前的右曲率证书（不重复证明）是
\[
\boxed{\mathcal V_m=Q_m^+ +{p\over2}E_m^+},\quad
E_m^+=\sum_{j=0}^{m-1}
 { -2^{1-m}+\sum_{k=0}^{j-1}a_k\over(2m+j+1)^2}.
\tag{2}
\]
(1) 与 (2) 因此构成来自 **同一个有限二项式 carrier** 的左右双向 Beta-log 证书。当 p=6m+1 为素数，所有显示分母为小于 p 的正整数（及 2 的幂），故
\[
\boxed{\mathcal U_m\equiv Q_m^-,\qquad
       \mathcal V_m\equiv Q_m^+\pmod p.}
\tag{3}
\]
没有在需要 mod p² 的阶段提前删去 pE/2；(1)(2) 都保留了相应精确修正。

### (1) 的全体 m 证明

有限二项式求和先给出
\[
F_m(z):=\sum_{n=0}^mb_nw_nz^n
=(6z\partial_z-1)(1-z/2)^m
=-(1-z/2)^{m-1}\bigl[(1-z)+pz/2\bigr].
\tag{4}
\]
逐个 n 的有限 Euler 对数积分为
\[
U_{2,n}=\int_0^1 t^{2m}(-\log t){t^{-n}-1\over1-t}\,dt.
\tag{5}
\]
全部求和是有限求和，端点 t=1 可去；代入 (4) 得到**精确** Laurent 多项式核
\[
{F_m(1/t)-F_m(1)\over1-t}
={1\over t}\left(1-{1\over2t}\right)^{m-1}
+{p\over2}\,
 {2^{1-m}-t^{-1}(1-\frac1{2t})^{m-1}\over1-t}.
\tag{6}
\]
因为 \(\sum_ja_j=2^{1-m}\)，有无极点的有限恒等式
\[
{2^{1-m}-\sum_{j=0}^{m-1}a_jt^{-j-1}\over1-t}
=-\sum_{j=0}^{m-1}a_j\sum_{k=1}^{j+1}t^{-k}.
\tag{7}
\]
逐项用
\(\int_0^1t^{q-1}(-\log t)\,dt=1/q^2\)，其中
\(q\in[m+1,2m]\)，由 (5)–(7) 直接得到 (1)。所有步骤在有理数域精确成立，不依赖样本、非终止级数或对 p 的素性假设。

## 2. 新的联合缩减：原 LOW 的 M 二阶层只剩一个混合 harmonic 和

对 0≤n≤m 令
\[
A_n=H_m-H_{m-n},\quad A_{2,n}=H_m^{(2)}-H_{m-n}^{(2)},
\quad U_n=H_{2m}-H_{2m-n},\quad
V_n=H_{2m+n}-H_{2m},
\quad\Lambda_n=2U_n-V_n .
\]
原 LOW 系数保持**原定义**：
\[
L_n=-A_n/2+2U_n/3+(H_{4m}-H_{4m-n})/3,
\quad
M_n=L_n^2/2-A_{2,n}/8+4U_{2,n}/9
            +5(H_{4m}^{(2)}-H_{4m-n}^{(2)})/18 .
\]
设
\[
\mathsf P_m={1\over8}\sum_{n=0}^mb_nw_n(A_n^2-A_{2,n}),\qquad
\mathsf X_m={1\over18}\sum_{n=0}^mb_nw_n\Lambda_n(\Lambda_n-3A_n).
\tag{8}
\]
这里 \(\mathsf P_m\) 的奇偶封闭式已经在原纯 A 笔记证明；**本轮不重做**，而 \(\mathsf X_m\) 是明确标出的未消去 mixed quadratic 端口。

对素数 p=6m+1，逐项把 \(4m-j=p-(2m+1+j)\) 反射，得到
\(H_{4m}-H_{4m-n}\equiv-V_n\pmod p\)，
\(H_{4m}^{(2)}-H_{4m-n}^{(2)}\equiv V_{2,n}\pmod p\)。
因此原始 \(M_n\) （**不是** 擅自丢掉 first digit 的镜像替代量）满足
\[
M_n\equiv {A_n^2-A_{2,n}\over8}
+{\Lambda_n(\Lambda_n-3A_n)\over18}
+{4\over9}U_{2,n}+{5\over18}V_{2,n}\pmod p.
\]
配合 (3) 得到本轮第二项结论：
\[
\boxed{\mathsf M_m:=\sum_{n=0}^mb_nw_nM_n
\equiv\mathsf P_m+\mathsf X_m
       +{4\over9}Q_m^-+{5\over18}Q_m^+\pmod p.}
\tag{9}
\]
这直接消去原 LOW 二阶矩中 **U₂ 和 V₂ 两个嵌套曲率 harmonic 层**。净系数 5/18 对应**原** \(M_n\) 的 second digit；若单独改用镜像 \(M_n^\sharp\)，必须同时补回此前 PAIR-CANCEL 的 divided-first-digit 修正，不能误写成 -1/18。这里未改变 \(\Theta_m\)，所以原 divided-first-digit 也未被偷换。

## 3. 真正的剩余 JOINT LOW 证书（精确目标，仍 OPEN）

先前的 LOW/Beta 已把母目标化为
\[
\mathscr D_m^\beta =
{\mathcal A_m\Theta_m-1\over p}
+\mathcal A_m(2^{-m}C_m-2V_m^{\rm beta}
+\mathsf M_m+J_m^{(2)})-\chi_p,
\]
其中
\(\mathcal A_m=(p-1)!/[3^{p-1}((2m)!)^3]\)，
\(\chi_p=((4/3)^{p-1}-1)/p\)，
\(\Theta_m,C_m,V_m^{\rm beta}\) 保持原 Beta 论文中的**精确定义**，
\(\Delta_m=(\mathcal A_m\Theta_m-1)/p\) 的 p-integrality 由原 first digit 保证。

复用 **前一单元已证明** 的整个 reflected high-band 一阶参数 jet 缩减
\(J_m^{(2)}\equiv F_0(1/2)+6R_m(1/2)\pmod p\)，其中
\(R_m=\mathcal L_mF_1\) 是原 m-seam/3m-terminal 多项式的确切差分 forcing；
原高段 r>m 的权重 1/3、整数标识和 cutoff 均不动。
本轮新推导 (9) 直接代入原始 LOW，得到一条**与原目标模 p 等价**的合成证书：
\[
\boxed{\begin{aligned}
\mathscr D_m^\beta\equiv {}&
\Delta_m+\mathcal A_m\Big[
2^{-m}C_m-2V_m^{\rm beta}
+\mathsf P_m+\mathsf X_m
+\tfrac49Q_m^-+\tfrac5{18}Q_m^+\\[-1mm]
&\hspace{24mm}+F_0(1/2)+6R_m(1/2)\Big]
-\chi_p\pmod p .
\end{aligned}}
\tag{10}
\]
因此 **仅一个低段二次混合调和端口 \(\mathsf X_m\) 仍含低段乘积 harmonic**；其余低段纯 A 端口已有奇偶证书，两个曲率端口是有界长度 m 的单层有理和，高段整个 first-jet 由已证 holonomic forcing 取代。式 (10) 不是声称各端口独立为零：第一位 \(\Delta_m\)、Beta 全区间 \(V_m^{\rm beta}\)、右端 Fermat quotient 和尾部 seam 都仍要参与整体相消。EP/LIFT 的全素数结论、native benchmark、独立审阅仍**未完成**。

## 4. 实际精确运算与 witness

使用 Python 3 标准库 Fraction、comb、factorial，**独立按原 n/r harmonic 与 Beta moment 定义**求原 \(\mathcal U,\mathcal V,\mathsf M,J^{(2)},\mathscr D^\beta\)，另一路计算 (1)(2) 的有限单和、(8)(9) 的缩减和、(10) 的 \(F_0+6R\) 表达。没有使用旧 611 素数 endpoint 扫描。

- m=1,...,18：\(\mathcal U_m=Q_m^-+pE_m^-/2\) 及引用的 \(\mathcal V_m=Q_m^++pE_m^+/2\) 全部**严格 Fraction 相等**。
- 在 p=7,13,19,31,37,43,61,67,73,79,97,103,109（13 个 p=6m+1 的素数且 m≤18）上，原 \(\mathsf M_m\) 与式 (9) 及原整个 \(\mathscr D^\beta\) 与式 (10) 的差均为 p-整分子的模 p 零；原全目标 defect 也均为零，属于有限交叉自检，不是全称证明。
- 三个高辨识度实例（每格取模 p）：

| p | \(\mathcal U_m\equiv Q^-\) | \(\mathcal V_m\equiv Q^+\) | \(\mathsf P_m\) | \(\mathsf X_m\) | 原 \(\mathsf M_m\)=缩减 M | \(J^{(2)}\)=\(F_0+6R\) | 式 (10) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 1 | 10 | 4 | 7 | 7 | 5 | 0 |
| 19 | 4 | 16 | 1 | 15 | 18 | 0 | 0 |
| 31 | 22 | 6 | 21 | 29 | 27 | 22 | 0 |

上述比较有两个用途：(i) 确认左曲率确实是新的、与已知右曲率相互独立的读数；(ii) 确认没有丢掉原 first-digit 导致镜像第二位失真。数学全称部分仅限于 (1) 的精确 Euler 积分证明及 (9)(10) 依已有已说明证明的代数替换，**不从 13 个有限测试外推**。

## 5. BRC observer、未解决点与后续精确动作

**REUSE_APPLIED / COMPOSE_APPLIED**：仍以原低段 signed binomial \(b_n\)、branch n、reflection 的 \(2m-n\) 与 \(2m+n\) 正整数分母、p-adic digit 为 carrier；observer 为加权 \(w_n\) 曲率及 JOINT LOW divided-first-digit。变换 (6) 保留所有所需标量读出，**不是** 声称保留不同未来操作下任意逐支信息；不把 signed cancellation 当非负质量或 X6 native dynamics。

**最小未完成数学动作**：直接对 (10) 中唯一未压缩低段二次混合端口
\(\mathsf X_m=\tfrac1{18}\sum b_nw_n\Lambda_n(\Lambda_n-3A_n)\)
构造**真实的**双参数 Euler–Beta/contiguous telescoper，明确它与 \(6R_m(1/2)\) 的 seam、\(-2V_m^{\rm beta}\)、\(\Delta_m\) 和 \(\chi_p\) 共同留下何种完整 finite joint residual。必须保持原 r>m 尾和 frozen pin；若不能消去，给出精确剩余项或严格有限反例。随后按原 native benchmark 对象/输入/验收条件执行，不能用本证书顶替 native 实验。

**真实恢复债。** 当前 Sites gateway 已读 version=0.6.11，site authentication 为只读 research_authority_granted=false；未取得本次真实服务签发 Researcher session/CLAIM/open/run。旧同 lane #6186 只有未认证 ACTIVE 本地投影，#6187 exact continuation 的 PREREQUISITE_NOT_SUCCEEDED 与 #6188 原 dispatch 的 FAILED/TimeoutExpired 已由前轮回读；不借 maintenance 身份，也不换 request_id 重放。aw d awmip/enterprise-math issue #1539（仓库名中的空格仅为避免正文自动链接；真实仓库为 awdawmip/enterprise-math）继续负责 Native Source-session/continuation 缺口。旧三份 staging 独立保全，不自动并入 accepted Result。仅以 Github 中立材料保存数学，**不是正式 Source checkpoint**。原研究调度与通知未修改。
