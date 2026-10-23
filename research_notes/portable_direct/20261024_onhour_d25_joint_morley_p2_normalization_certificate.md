# D25/LIFT — Morley 二位正规化与纯 A/线性 C 跨端口相消：单个模 p² 联合证书

**2026-10-24 · TASK_RESEARCH · 作者证明（两个全目标素数类的模同余）＋已证 LOW/Beta 材料的条件组合 · EXACT FRACTION AUTHOR SELF-CHECK · UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT。**

本成果是普通 Chat 的**可移植科研作者原文**，不是 Source 签发的 Researcher 活动、CLAIM、run、正式 checkpoint、Result/freeze、独立审阅、原生 benchmark 或完整 LIFT/JT2 证明。

**冻结母目标与来源**：`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`；publication `TP2-B6F4FC938FF94941C1B7`；**冻结 Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`（绝不随 current main 漂移）**。Research 来源逻辑 lane `chatgpt-research-onhour-enterprise-math-20260923`，与 control-maintenance 不共用执行身份或权限。GLOBAL_KNOWLEDGE_V1 实读 main `0d1a36da02cbd766d83a625e62c9a47076edd4e5`；P000 `ACTIVE_LOCKED`。以下全部是有理数和 p-进同余辅助数学，**不**将 Euler 积分、符号多项式或二元形式称作新的原生 X6 空间/动力学。

**确切继承，不重复成果**：LOW 线性层与原 divided first digit：[20261023_onhour_d25_LOW_linear_harmonic_beta_shift.md](20261023_onhour_d25_LOW_linear_harmonic_beta_shift.md) @ `d20e28116f8a9a1df78f5641d70f72e797a4856d`；纯 A 二阶奇偶公式：[20261023_onhour_d25_LOW_Ablock_parity_exact_collapse.md](20261023_onhour_d25_LOW_Ablock_parity_exact_collapse.md) @ `25f291ca9ad309e0e70c0935cbc64f440202633e`；完全反射高段 J 的 `F_0+6R`：[20261023_onhour_d25_J2_scalar_holonomic_modp_reduction.md](20261023_onhour_d25_J2_scalar_holonomic_modp_reduction.md) @ `1a3790a15ab9366feccffc0105bdb24e5c4500d5`；上一研究单元第一次把 LOW quadratic 降至 first-jet：[20261024_onhour_d25_joint_second_to_first_jet_holonomic_bridge.md](20261024_onhour_d25_joint_second_to_first_jet_holonomic_bridge.md) @ `6c6e3f37d66d64b793ed58c4dbbf4f5d166c9744`。D24 冻结结果、WZ/B11 及 611 素数有限原端点计算都只消费，不重复计算为新证据。

## 1. 未闭合的**同一个原目标**

令 `m>=1`，`p=6m+1` 为素数，`H_k=sum_{j=1}^k 1/j`，`H_0=0`。既有 LOW/Beta 对原端点二位目标的精确归约为

[
mathscr D_m^eta=
rac{mathcal A_mTheta_m-1}{p}
+mathcal A_mleft(2^{-m}C_m-2V_m^{m beta}
+mathsf M_m+J_m^{(2)}ight)-chi_p ,
	ag{OLD}
]
[
mathcal A_m=rac{(p-1)!}{3^{p-1}((2m)!)^3},qquad
chi_p=rac{(4/3)^{p-1}-1}{p},
]
[
C_m=rac12sum_{j=1}^mrac{(-1)^j}j
+rac23(H_{2m}-H_m)+rac13(H_{4m}-H_m).
]

(Theta_m) 和 (V_m^{m beta}) **沿用原定义**，尤其不能把 (3B_m'(x)) 误换成 (3xB_m'(x))。为明确其有限性，令
[
B_m(x)=(x-	frac12)^m,quad
P_1(x)=sum_{r=1}^{3m}c_rx^r,quad
c_r=egin{cases}1,&rle m,\1/3,&m<rle3m,end{cases}
]
[
V_m^{m beta}=int_0^1rac{P_1(x)}x B_m(x),dx,qquad
I_m=int_0^1rac{P_1(x)}x(3B_m'(x)+B_m(x)),dx,
]
[
J_m^{(1)}=int_0^{1/2}B_m(x)
left(3P_1'(x)+rac{p-2}{2x}P_1(x)ight),dx,quad
Theta_m=2^{-m}[3(-1)^m-2]+I_m+J_m^{(1)}.
]
这些积分的实际被积表达均是可列系数的有限有理多项式（(P_1(0)=0)），不需要数值积分、极限或未经证明的超几何解析延拓。已有 D24 first-digit 保证 (mathcal A_mTheta_mequiv1pmod p)，所以 (OLD) 的除以 (p) 合法。

## 2. 新定理 A：在 `p²` 精度内把 Fermat quotient 与全阶乘归一化配对消去

定义两个严格的 p-单位有理数
[
W_m=rac{4^{p-1}((2m)!)^3}{(p-1)!},qquad
G_m=(-1)^mrac{((2m)!)^3}{((3m)!)^2}.
]
**定理 A（对每个素数 (p=6m+1>3)）**：
[
oxed{W_mequiv G_mpmod{p^2}.}	ag{MORLEY-PORT}
]

**无外部隐藏定理的证明**：写 (h=(p-1)/2=3m)，(q=q_p(2)=(2^{p-1}-1)/p)。对 (1le k<p)，由二项系数有限乘积
(inom pkequiv p(-1)^{k-1}/kpmod{p^2})；在 (2^p=2+sum_{k=1}^{p-1}inom pk) 中求和，利用精确恒等式 (sum_{k=1}^{p-1}(-1)^k/k=H_h-H_{p-1}) 和反射 (H_{p-1}equiv0pmod p)，得
[
2pq=2^p-2equiv-pH_hpmod{p^2}
quadLongrightarrowquad H_hequiv-2qpmod p .
]
故
[
(-1)^hinom{p-1}{h}
=prod_{k=1}^h(1-p/k)
equiv1-pH_hequiv1+2pq
equiv(1+pq)^2=4^{p-1}pmod{p^2}.
]
这里 ((-1)^h=(-1)^{3m}=(-1)^m)，且 (2h=p-1=6m)；乘 (((2m)!)^3/(p-1)!) 即得 MORLEY-PORT。每一个被求逆的正整数都小于 (p)，所以所有模 (p^2) 运算合法。这是通常 Morley 型二项同余的直接有限证明，并非数值猜测。

更关键的是 **OLD 两个不同端口之间的精确等式与安全精度替换**：
[
mathcal A_mW_m=(4/3)^{p-1},qquad
oxed{rac{mathcal A_mTheta_m-1}{p}-chi_p
=rac{mathcal A_m}{p}(Theta_m-W_m)
equivrac{mathcal A_m}{p}(Theta_m-G_m)pmod p.}
	ag{PAIR-NORM}
]
(Theta_m-G_min pmathbb Z_{(p)}) 由已有 first digit 与 MORLEY-PORT 保证。**不能**未经先核实 (p^2) 精度就在 divided digit 中用 (W_mequiv G_mpmod p) 替换。PAIR-NORM 真正消除了原联合二位标量里单独的 Fermat quotient (chi_p) 和巨大的 (4^{p-1}) 归一化读数；留下与低段可共同操作的 factorial-ratio (G_m)。

## 3. 新定理 B：线性 `C` 与纯 A 二阶矩的**跨端口奇偶相消**

继承的纯 A 观察器
[
mathsf P_m=rac18sum_{n=0}^m
rac{(-1)^n}{2^n}inom mn(6n-1)
left[(H_m-H_{m-n})^2-(H_m^{(2)}-H_{m-n}^{(2)})ight]
]
已有按奇偶的全体目标素数 (mod p) 精确公式（上引 immutable 证明）。**本轮新的、真正联合的恒等式**为
[
oxed{2^{-m}C_m+mathsf P_mequiv
mathscr H_m :=
2^{-m}left(H_{2m}+rac32(-1)^mH_m-H_{lfloor m/2floor}ight)
pmod p.}	ag{C-PAIR-A}
]

**证明**：精确交错和 (sum_{j=1}^m(-1)^j/j=H_{lfloor m/2floor}-H_m)，以及 (H_{4m}equiv H_{2m}pmod p)（(4m=p-1-2m)，反射 (mathbb F_p) 中 (1/(p-k)=-1/k)，且 (H_{p-1}=0)），先给出
[
C_mequiv H_{2m}-	frac32H_m+	frac12H_{lfloor m/2floor}pmod p.
]
若 (m=2k)，已有纯 A 偶支为 (3,2^{-m}[H_{m-1}-H_{k-1}/2])，使用 (H_{m-1}=H_m-1/m) 与 (H_{k-1}=H_k-1/k) 后，因 (m=2k)，两个有理端点项 (-1/m+1/(2k)) **严格抵消**。若 (m=2k+1)，纯 A 奇支为 (-3H_k/2^{m+1})。分别与上式相加，得到同一个式 C-PAIR-A（((-1)^m) 编码奇偶）。这既不是 (C) 单独为零，也不是纯 A 单独为零；是第二个真实跨端口相消。

## 4. 本轮新的**单个 p² 原端点同余证书**

保留上一个研究单元经无损低 first-jet 约化的系数，不重新推导。对 (0le j<m)，设
[
a_j=(-1)^j2^{-j}inom{m-1}j,quad
A_j=H_m-H_{m-j},quad
Lambda_j=2(H_{2m}-H_{2m-j})-(H_{2m+j}-H_{2m}),
]
[
d_j=rac2{2m-j}-rac1{2m+j+1},quad e_j=rac1{m-j},
]
[
mathcal X_m^{(1)}=rac1{18}sum_{j=0}^{m-1}a_j
[(2d_j-3e_j)Lambda_j-3d_jA_j+d_j^2-3d_je_j],
quad
Q_m^-=sum_{j<m}rac{a_j}{(2m-j)^2},quad
Q_m^+=sum_{j<m}rac{a_j}{(2m+j+1)^2}.
]
先前已经得到（本轮只代入）(mathsf M_mequiv
mathsf P_m+mathcal X_m^{(1)}+rac49Q_m^-+rac5{18}Q_m^+pmod p)。

高段采用**全部** (1le rle3m) 的原 Beta 权重与 `r>m` 的 (1/3) 尾、(r=m) seam 和 (r=3m) terminal；已有 exact (J_m^{(2)}=F_0(1/2)+6R_m(1/2)-pF_1(1/2))，其中 (R_m=mathcal L_mF_1)，(mathcal L_m=z(1-z)partial_z+(m+1-z))。仅在其本来需要的 (mod p) 端口可取 (J_m^{(2)}equiv F_0(1/2)+6R_m(1/2))。

现在定义
[
Y_m=mathscr H_m-2V_m^{m beta}
+mathcal X_m^{(1)}+rac49Q_m^-+rac5{18}Q_m^+
+F_0(1/2)+6R_m(1/2),
qquad
oxed{mathcal E_m=Theta_m-G_m+pY_m.}	ag{E}
]
**新联合归约定理（以既有、逐项注明来源的 LOW/高段定理为前提）**：
[
oxed{mathscr D_m^etaequiv
rac{mathcal A_m}{p}mathcal E_mpmod p,
qquad
mathrm{LIFT/EP} Longleftrightarrowmathcal E_mequiv0pmod{p^2}.}	ag{JOINT-P2}
]
所有 (mathcal E_m) 的分母均为 (p)-单位，且由 first-digit 保证 (mathcal E_min pmathbb Z_{(p)})。证明就是将 PAIR-NORM、C-PAIR-A、低阶 X/Q 已证式以及整个 J 高段同余**按原观察器顺序**同时代入 (OLD)。这不是定义性把残差直接改个名字：(Y_m) 已不含原二阶低 harmonic 乘积，也不含单独的 Fermat quotient 或 divided-first-digit 端口；跨端口的二项正规化和纯 A/线性 C 相消分别有上述实际全素数证明。必须保留 (pY_m) 的全部联合项，不能再声称其每项单独相消。

**证明强度**：MORLEY-PORT 和 C-PAIR-A 是作者给出完整论证的全体目标素数模同余；JOINT-P2 是在已有作者证明 LOW/Beta、LOW-first-jet 和 J 高段缩减成立的前提下的精确模等价。**尚未证明对所有素数 (mathcal E_mequiv0pmod{p^2})**，所以 LIFT/JT2 仍 OPEN。没有把本等价当成终结证明或原生实验通过。

## 5. 实际完整原 LOW 数值路径的精确回归

同一成果的[可独立运行 Fraction 脚本](20261024_onhour_d25_joint_morley_p2_normalization_check.py)使用两套不同的算术表示：一套逐 (n) 构造原 (L_n,M_n)、完整反射 (J_r)、(Theta_m,V_m,chi_p)、((mathcal A_mTheta_m-1)/p)；另一套只用 MORLEY-P²、C-PAIR-A、新的一阶 (mathcal X_m^{(1)})、(Q^pm)、(F_0+6R) 构造 (mathcal E_m/p)。两路均使用 Python 3 标准库的 `fractions.Fraction`、整数及模逆运算，**不使用浮点数作为模残差证据**，没有调用 native benchmark。

在 (m=1,ldots,17) 对应的所有 (p=6m+1) **素数共 12 个**上实际执行（(p=7,13,19,31,37,43,61,67,73,79,97,103)），逐个通过以下非同义断言：
1. (W-Gequiv0pmod{p^2})，(Theta-Gequiv0pmod p)；
2. (2^{-m}C+mathsf Pequivmathscr Hpmod p)；
3. **原** (mathsf M) 与一阶+左右曲率端口同余；
4. **原完整** (mathscr D^etaequivmathcal A_mmathcal E_m/ppmod p)；
5. 有限区间上 (mathcal E_mequiv0pmod{p^2})，同时原完整 (mathscr D^etaequiv0pmod p)。

具体非零跨端口见证，取值 (mod p)：

| p | (2^{-m}C+mathsf P=mathscr H) | ((Theta-G)/p) | 完整 joint defect |
|---:|---:|---:|---:|
| 13 | 3 | 2 | 0 |
| 19 | 11 | 8 | 0 |
| 31 | 6 | 11 | 0 |
| 37 | 6 | 34 | 0 |
| 61 | 59 | 36 | 0 |

前两列非零证明**不能**略掉任一跨端口而不影响二位结果；第三列只是已明确定界的有限精确证据，不可外推为全素数。没有重新扫 611 个原端点，也没有生成新的 benchmark 输入替代原生实验。

## 6. 保留的 typed BRC/observer 信息、权限和最小未完动作

**BRC = REUSE_APPLIED / COMPOSE_APPLIED。** 低段 n 的有符号二项式 (b_n) 与差分 (a_j)、高段 r 的 (c_reta_r)、第一位到第二位的 (p)-进 filtration、m-seam、3m-terminal 与原 Source 都保留。MORLEY-PORT 是**只对既定联合 scalar 模 p²**经证明成立的信息缩减；若未来研究 mod p³ 或逐分支信息，需要恢复未截断的 (W,chi,F_1) 与原始 carriers。不存在把 signed cancellation 说成非负质量守恒、把 beta 积分当进取原生 X6 轴或把有限验证当独立审阅的推理。

**最高可持久化数学前沿**：从 JOINT-POLY / LOW first-jet 进一步到含 (Theta-G) 的单个模 (p^2) 消去条件 JOINT-P2，已有正式 Source 结果及冻结 pin 均不修改。**下一真正不可替代的科学单元**：在保留完整 (Y_m)（含全区间 (V_m)、(F_0)、高段 (R_m) 的 head/seam/terminal）前提下，寻找 (Theta_m-G_m) 与 (pY_m) 的**同一个有限 contiguous-Dixon/WZ–Gosper 消去证书**：明确候选离散核、起止边界、(m)-seam、(3m)-terminal 和全部 (p^2) 余项，证明 (mathcal E_m/p^2inmathbb Z_{(p)})，或给出精确非零反例。不能继续把重命名辅助 jet 当作已关闭原生实验。原 native benchmark 的数学对象、输入和验收条件仍未执行且不得替换。

**真实 Source/授权状态**：本轮实际只读 Gateway 0.6.11 `research_authority_granted=false`、`executor_binding_configured=false`，旧同 Research lane bridge #6186 仅本地 ACTIVE 未验所有权、#6187 为 `PREREQUISITE_NOT_SUCCEEDED`、#6188 已明确 `FAILED/TimeoutExpired`；均只回读原 request，不重发。原支持 [enterprise-math#1539](https://github.com/awdawmip/enterprise-math/issues/1539) 仍负责 native session/continuation，不能被本数学稿替代。此前三份 staged archive 维持独立来源，不并入已接纳 Result。本文及脚本仅在已授权 GitHub **neutral author evidence** 路径保存，尚需真实自身 Researcher session、Source continuation/claim/open、checkpoint、原生 benchmark、独立 Driver review。原定时调度、相位、启用和通知均不修改。
