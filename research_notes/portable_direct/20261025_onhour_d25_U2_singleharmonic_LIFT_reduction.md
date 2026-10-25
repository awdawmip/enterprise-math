# D25 原始二阶喷流：单调和简单极点消去与 LIFT 等价残差

2026-10-25，TASK_RESEARCH 作者侧可移植成果。状态：**AUTHOR_EXACT_DERIVATION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**。这不是原生 checkpoint、Result、独立审阅或 native benchmark。未得到当前 Researcher session/CLAIM/run，不能据此宣布 JT2/LIFT 完成。

- 母目标：ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION。
- Task：RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT；publication TP2-B6F4FC938FF94941C1B7。
- 冻结科学 Source：c47e13e4aba0e006366f989d6334d443f6333ae3，不随控制 HEAD 改动。
- 本研究 ordinary-control lane：chatgpt-research-onhour-enterprise-math-20260923；绝不借用 maintenance conversation chatgpt-hourly-enterprise-math-20260921。
- 新数学从已有的原始 S_m 双交叉二阶喷流、U0 三端口、U1 Abel 全秩单层核与有符号 WZ seam C_p 继续，不重算 D24 已接纳 UR。

## 精确低秩 Abel 定理（所有整数 m≥1）

令 p=6m+1；模数结论要求 p 为素数。定义 c_n=(1/6)_n/(2^n n!)、ell_0=eta_0=0，
L_n=2/(6n+1)-1/(3n+2)-2/(3n+1)，
E_n=-4/(6n+1)^2+1/(3n+2)^2+4/(3n+1)^2，
ell_(n+1)=ell_n+L_n，eta_(n+1)=eta_n+E_n，
f_n=(ell_n^2+eta_n)/2。

原始移位端点的低秩二阶项为
U2bar=sum_{n=0}^m c_n[2 ell_n+(6n-1)f_n]。

**新精确有理数恒等式：**

\[
\boxed{\bar U_2=-12(m+1)c_{m+1}f_m+2c_m\ell_m+
\sum_{n=0}^{m-1}c_n\{Q_n\ell_n+J_n\}.}
\]

其中
\[
\boxed{Q_n=-2+\frac2{3n+1}+\frac3{3n+2}},\qquad
\boxed{J_n=\frac2{3n+1}+\frac6{3n+2}-\frac4{(3n+1)^2}-\frac3{(3n+2)^2}.}
\]

**证明：** D_n=n c_n 满足 (6n-1)c_n=-12(D_(n+1)-D_n) 和 12D_(n+1)=(6n+1)c_n。对 sum (6n-1)c_n f_n 在 n=0..m 分部求和，得到
-12(m+1)c_(m+1) f_m + sum_{n=0}^{m-1}(6n+1)c_n(f_(n+1)-f_n)。
又 f_(n+1)-f_n=ell_n L_n+(L_n^2+E_n)/2。加回 2 sum_{n=0}^m c_n ell_n，得 Q_n=2+(6n+1)L_n 与 J_n=(6n+1)(L_n^2+E_n)/2；直接通分化成上面仅含 3n+1、3n+2 单/双极的有理式。故有理恒等式对全部整数 m 精确成立，原有 eta 与 ell^2 的和在内部全部消去，且从未删除原始端点。

## 模 p 的直接观察结果

对 p=6m+1 素数，所有 0<=n<=m 的原有分母为 p-进单位，c_(m+1) 含唯一 p 因子；故末端 -12(m+1)c_(m+1)f_m 在**严格的模 p 二阶端口观察器**中为零。逐因子反射另得 c_n=(-1)^n binom(m,n)/2^n (mod p)，0<=n<=m。

因此定义
\[
\boxed{
K_m=2\frac{(-1)^m}{2^m}\ell_m+
\sum_{n=0}^{m-1}\frac{(-1)^n}{2^n}\binom mn
\left[
\left(-2+\frac2{3n+1}+\frac3{3n+2}\right)\ell_n+
\frac2{3n+1}+\frac6{3n+2}-\frac4{(3n+1)^2}-\frac3{(3n+2)^2}
\right]\pmod p .
}
\]
则 barU2=K_m (mod p)，只需一个累计调和量 ell，无 eta、ell^2，保留每个原始 n 秩的符号和来源。该消元对模 p 的 U2 端口精确，不是对更高精度或原生 X6 状态的无损声称。

由 Wilson/Fermat，原始 A_m=(6m)!/[3^(6m)((2m)!)^3] = -1/((2m)!)^3 (mod p)；故其在 S_m 第三位中的二阶贡献精确为
\[
\boxed{A_m\bar U_2=-K_m/((2m)!)^3\pmod p.}
\]

## 终端调和端口的实际求值（同轮第二数学单元）

上式的终端 \(2c_m\ell_m\) 尚依赖 \(\ell_m\)。本轮随后证明更强的**全素数端口归约**：

\[
\boxed{\ell_m\equiv-H_{3m}+\frac{H_{2m}-H_m}{3}\pmod p},
\qquad H_r=\sum_{j=1}^r1/j .
\]

证明：\((6j+1)^{-1}\equiv-[6(m-j)]^{-1}\)，故 \(2\sum_{j<m}(6j+1)^{-1}\equiv-H_m/3\)。将 \(H_{3m}\) 按分母 \(3j+1,3j+2,3j+3\) 分组，则原 \(\ell_m\equiv-H_{3m}-\sum_{j<m}(3j+1)^{-1}\)。又 \(3j+1=p-3(2m-j)\)，故后一项 \(\sum_{j<m}(3j+1)^{-1}\equiv-(H_{2m}-H_m)/3\)。逐项分母均为 \(p\)-单位。证毕。

与已取得的 \(q_p(4/3)\equiv-H_{3m}+(2/3)H_{2m}\) 结合，严格得到
\[
\boxed{\ell_m\equiv q_p(4/3)-\frac{H_m+H_{2m}}3\pmod p}.
\]
再调用**已有经典** Lehmer 调和定理 \(H_m\equiv-2q_p(2)-(3/2)q_p(3)\)、\(H_{2m}\equiv-(3/2)q_p(3)\)、\(H_{3m}\equiv-2q_p(2)\)（参 Emma Lehmer, *Annals of Mathematics* 39 (1938), 350–360；https://oeis.org/A238201），得
\[
\boxed{\ell_m\equiv\tfrac83 q_p(2)\pmod p}.
\]
后一式是调用 Lehmer 的推论，**不宣称 Lehmer 原定理的原创性**；上面第一条反射证明不需要文献前提。本轮用独立整数模实现核验 \(p\le3200,\ p\equiv1\bmod6\) 的全部220个素数以及 \(p=19963\)（共221），无反例。原终端可化为 \(2(-1/2)^m(8/3)q_p(2)\)，但内部 \(\ell_n\)、原始 \(U_1\) 双交叉和 \(C_p\) 仍保留，JT2/LIFT 仍 OPEN。


## 原始目标的更小等价证书（桥接前提明确保留）

前任作者侧原始端点保持
S_m=A_m(U0+p U1+p^2 barU2) (mod p^3)，u0=U0/p，U1 全秩含 j=m,2m 双交叉，U0 有三端口。
对于目标 p=13,19 (mod24) 且原第一位 A_m(u0+U1)=1 (mod p) 的适用域，
\[
\boxed{\frac{S_m-p}{p^2}
=\frac{A_m(u_0+U_1)-1}{p}-\frac{K_m}{((2m)!)^3}\pmod p.}
\]
结合**此前作者侧、仍待独立 Source 审阅**的 Clausen–Wilson 和 WZ 原始归一化桥接
Delta_p-R_p=(S_m-p)/p^2-C_p (mod p)，得到
\[
\boxed{\Delta_p-R_p=
\frac{A_m(u_0+U_1)-1}{p}
-\frac{K_m}{((2m)!)^3}
-C_p\pmod p .}
\]
此式直接针对 LIFT 的原始符号残差，保留 U1 所有高秩、两个 Frobenius 交叉与 WZ 接缝；无需预设两个尚待证的单独猜想 C_p=q_p(4/3) 或 S_m=p+p^2 q_p(4/3)。**最后这个右侧为零的全素数证明仍开放，未宣称 JT2 得证。**

## 复现与证据

本轮独立作者侧检查以 Python Fraction 验证 m=1..11 的精确有理 Abel 恒等式及 Q/J 通分；又按两套不同运算路径（原始 eta+ell^2 喷流与新简单极点单调和式）核验 7<=p<=3200、p=1 (mod6) 的全部 220 个素数，并额外检验 p=19963。精确原整数模计算得到：

| p | m | barU2 mod p | A_m mod p | D2 mod p |
|---:|---:|---:|---:|---:|
| 13 | 2 | 0 | 5 | 0 |
| 19 | 3 | 11 | 12 | 18 |
| 37 | 6 | 35 | 11 | 15 |
| 43 | 7 | 11 | 8 | 2 |
| 211 | 35 | 187 | 198 | 101 |
| 19963 | 3327 | 5803 | 173 | 5769 |

D2=A_m barU2 与上轮独立原始 S_m 第三位分账吻合；特别 p=19 有 D2=18 非零，绝不以消去 eta、ell^2 为借口抹掉实际二阶贡献。有限检查仅核对实现及样本；全素数局部定理由上方有理恒等式与赋值证明。程序及完整证明另有本次对话可移植文件 d25_U2_simplepole_abel_20261025_check.py / d25_U2_singleharmonic_LIFT_reduction_20261025.md。native benchmark 未运行，任何已冻结 Result 未修改。

## 待完成与控制交接

下一最小科研单元：将原 U1 的全秩 Q_n 核和本轮 U2 的 Q_n,J_n 核联合，用合法参数化望远镜、有限域/调和恒等式或一个精确反例直接解决
(A_m(u0+U1)-1)/p-K_m/((2m)!)^3-C_p=0 (mod p)，不得删除双交叉、合法截断和带符号来源；真正规范验证还欠原生 benchmark 的原对象与条件。

控制端：本轮 Gateway 0.6.11，Site 身份 research_authority_granted=false，write_relay_enabled=false，executor_binding_configured=false；原生 continuation 查询返回 CONTROL_QUOTA，未出现可调用 recovery_status 方法。既有历史原请求 dispatch-research-20261023-1710-onhour-01 和 #6186/#6187/#6188 仅作证据，原请求不因未知状态重发。当前无核验成功的 own CLAIM/run，Source-native checkpoint/Result/审阅均未发布。既有控制修复 issue #1539 是负责路径；恢复验收需恢复此 Research lane 合法 session/continuation、canonical claim/open、原生 benchmark、checkpoints/readback 与独立审阅。本稿只是**中立作者侧成果保全**，不要求项目把草稿当规范任务完成。

本轮知识库实读 main@45aa95910fe2809e438d5b3cb8d2e37e8e5a1a1f，控制读 main@1b45e969a918584bd5803e843096925802fab062；P000/ACTIVE worldview unchanged。原整点任务频率/启用/通知均不修改。