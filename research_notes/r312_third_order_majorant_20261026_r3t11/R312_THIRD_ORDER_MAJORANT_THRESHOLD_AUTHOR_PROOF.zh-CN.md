# R312 — BRC 有序缺陷纤维充分证书临界根的三阶展开

日期：2026-10-26。性质：作者侧全长度渐近证明、精确符号复算、数值交叉验证；未经独立 Driver 审查，非原生 Source Result 或六维原生 X6 物理定理。

## 0. 冻结来源与保真模型

- GLOBAL_KNOWLEDGE_V1 固定使用 awdawmip/chatgpt-global-knowledge main@315eadf1bdecd0f881268b6d5d5ce35e12cfc126，已读取 00_BOOTSTRAP.md、OPERATING_MANUAL.md、项目 TASK 入口、P000、ACTIVE 我眼中的世界，以及数学、BRC、研究活动与代码规范。
- Enterprise Math 控制、便携研究规范取 main@3bc601bb1c01a3b950b4237104bb9ef7e32924f4；参照 docs/PORTABLE_RESEARCH_PROTOCOL.md 与 control_plane/current_control_authority.json。
- 已验证但仍为作者侧的科学依赖：R303 c8079dcbb383c010196cfd7a422626f1b545bf77；R305 fef7b1db71a9884f55de16ad24d94699412a38d1；R309 fb8fa9b03d5b69bfac9c00b6ef0ce0ecb812eebd；R310 a7575a0a7e8e6e9177524882ac74287f03c1a4cd；R311 a8a54beb2a3df3e2a74a60ee17800fd322519c84。
- BRC 的载体是正权有序、禁止相邻两个 0 的六边来源自动机，按完整 (epsilon,k) 效果分别统计来源并计算整数差。保留来源顺序、重数及后缀符号；整数差不是物理有符号质量、复振幅或者已证的心跳世界动力学。BRC=REUSE_APPLIED + REUSE_EXECUTED。

## 1. 定理：充分证书临界实根的倒数阶

对整数 d≥3、n≥4d+4，沿用 R309/R310 严格的分块充分比较：

\[
A_d(n)=\binom{n-2d-4}{d-1},\quad B_d(n)=\binom{n}{d-2},\quad
U_d(n)=\sum_{r=1}^{d-1}\sum_{j=1}^{\min(r,d-r)}
\binom{d-r}{j}\binom{r-1}{j-1}\binom{n}{d-r-j}.
\]

若 A_d(n)>U_d(n)，则 D_d(n)=P_n(+,2-n+2d)-P_n(-,2-n+2d)>0；反向一般不成立。将组合数按下降阶乘多项式延拓至实数 n≥4d+4，定义充分证书的唯一实交点 \(\nu_d\) 为 A_d(\nu_d)=U_d(\nu_d)。唯一性及足够大 d 的存在性见 R311 和下节严格单调性。

令 c 为 c exp(-2/c)=1 的唯一正根（c=2/W(2)），并令
\[
\beta=\frac{-4c^2+8c+7}{2(c+2)},\qquad
\gamma=\frac{6c^6-30c^5-327c^4-283c^3-54c^2+18c+1}{6c^2(c+2)^3},
\]
\[
\boxed{\eta=
\frac{12c^8+546c^7+4854c^6+7018c^5+5511c^4+877c^3-1914c^2-495c-8}
{12c^3(c+2)^5}}.
\]

**定理 R312（相对 R311 新增倒数阶）：**
\[
\boxed{\nu_d=c d^2+\beta d+\gamma+\eta/d+O(d^{-2})\quad(d\to\infty).}
\]
其中 \(\eta\approx7.07283290526706864749\)。充分证书的整数初次成功长度是 \(m_d=\lfloor\nu_d\rfloor+1\)；不可由实根的 \(O(d^{-2})\) 误差直接获得取整表达式在所有 d 上的无误差稳定性。更不能将 m_d 当成真实 D_d 正性初次长度。

## 2. 严格单调与主项的形式展开

由前人的整数组合代数关系，在实数 n≥4d+4，
\[
\frac{A_d(n)}{B_d(n)}
=\frac{n-3d-2}{d-1}
\prod_{i=0}^{d-3}\left(1-\frac{2d+4}{n-i}\right).
\tag{1}
\]
右侧随 n 严格递增。另一方面 U_d(n)/B_d(n) 的每项是非负系数乘以 \(\binom{n}{j}/\binom{n}{d-2}\)（j≤d−2），随 n 非增。故 \(H_d(n)=(A_d(n)-U_d(n))/B_d(n)\) 严格递增，至多有一个交点。

为获得精度，在 c_0>0 固定、b,g,h 有界的参数族中写 t=1/d、n=c_0/t²+b/t+g+h t。将式 (1) 的有限正乘积对数展开到 t³。置 \(a_i=(2d+4)/(n-i)\)，有 \(a_i=O(d^{-1})\)，而其对数第五阶尾的总量 \(\sum_i a_i^5=O(d^{-4})\)。由
\[
\log(1-a_i)=-\sum_{k=1}^4\frac{a_i^k}{k}+O(a_i^5),
\qquad
\frac1{(n-i)^k}=\frac1{n^k}\sum_{j\ge0}\binom{k+j-1}{j}(i/n)^j
\]
及 i=0,…,d−3 的精确整数幂和，得到一致的展开
\[
L=\sum_{i=0}^{d-3}\log(1-a_i)=-2/c_0+\ell_1t+\ell_2t^2+\ell_3t^3+O(t^4),
\]
\[
\ell_1=\frac{2b-3}{c_0^2},\quad
\ell_2=\frac{-2b^2+6b+8c_0^2+2c_0g-c_0-16/3}{c_0^3},
\]
\[
\ell_3=\frac{4b^3-18b^2+32b+4c_0^2(-4b+h+6)
+2c_0(-4bg+2b+6g-5)-21}{2c_0^4}.
\tag{2}
\]
在这一求和中只保留 k+j≤4 的项，其余均在 t⁴ 或更高阶。这只是正实有限组合积的辅助解析估计，不是用连续模型取代原生离散结构。

同时
\[
\frac{n-3d-2}{d(d-1)}=p_0+p_1t+p_2t^2+p_3t^3+O(t^4),
\]
\[
(p_0,p_1,p_2,p_3)=(c_0,b+c_0-3,b+c_0+g-5,b+c_0+g+h-5).
\tag{3}
\]
因而 \(A_d(n)/(dB_d(n))=e^L(p_0+p_1t+p_2t²+p_3t³)+O(t^4)\)，其中 t³ 系数严格为
\[
e^{-2/c_0}\Big[p_3+p_2\ell_1+p_1(\ell_2+\ell_1^2/2)
+c_0(\ell_3+\ell_1\ell_2+\ell_1^3/6)\Big].
\tag{4}
\]

## 3. 负项上界的独立展开，保留来源位置

对 U_d(n) 中 r,j 双索引，设 m=r+j−2，则
\[
\frac{\binom n{d-r-j}}{\binom n{d-2}}
=\prod_{i=0}^{m-1}\frac{d-2-i}{n-d+3+i}.
\tag{5}
\]
此表达式保留不同首返块位置和组合重数。以 Y=n−d+3、θ=d/Y、ρ=θ(1+dθ) 定义已有的逐 r 组合 majorant：
\[
0\le U_{r,d}(n)/B_d(n)\le d\,\rho^{r-1},\qquad \rho=O(d^{-1}).
\tag{6}
\]
对于 r≥5，几何和上界 \(d\rho^4/(1-\rho)=O(d^{-3})\)；除以 d 后为 O(t⁴)。于是 t³ 系数只需 r=1,2,3,4 的有限有理项。通过式 (5) 逐项展开，严格得到
\[
\frac{U_d(n)}{dB_d(n)}
=1+u_0t+u_1t^2+u_2t^3+O(t^4),
\]
\[
u_0=-1+\frac1{c_0}+\frac1{2c_0^2},\quad
u_1=-\frac4{c_0}-\frac{b+3}{c_0^2}+\frac{2-b}{c_0^3}+\frac1{6c_0^4},
\]
\[
u_2=
\frac{96c_0^5+12c_0^4(8b-2g+7)+12c_0^3(2b^2+12b-2g-51)
+4c_0^2(9b^2-36b+10)+4c_0(7-4b)+1}{24c_0^6}.
\tag{7}
\]
这里 u_2 不含 h。式 (2)-(7) 的余项对 b,g,h 的有界紧区间一致。

## 4. 消项、精确代数证书与 O(d^-2) 实根夹逼

临界 c 满足 \(e^{-2/c}=1/c\)，代入 (2)-(7)。先令 t、t² 系数消失，唯一得到 R311 先前已识别的 β、γ；第三阶通分得到
\[
\boxed{\frac{H_d(c d^2+\beta d+\gamma+h/d)}d
=\frac{c+2}{c^2}(h-\eta)d^{-3}+O(d^{-4}).}
\tag{8}
\]
式 (8) 中显式 η 分式已由本轮 Python/SymPy 1.14.0 精确符号恒等式检查，和 R311 已有二阶表达一致。这一计算是代数复算证据，不把有限数值拟合当作证明。

因误差在 h 的有界区间内统一，取任意足够大的固定 C>0，将 h 置为 η−C/d 与 η+C/d。式 (8) 主项变成 \(\mp C(c+2)c^{-2}d^{-4}\)，选 C 压过统一的 O(d^-4) 余项常数，则 H_d 两端异号。结合严格单调和充分大 d 的交点存在性，
\[
c d^2+\beta d+\gamma+\eta/d-C/d^2
<\nu_d<
c d^2+\beta d+\gamma+\eta/d+C/d^2.
\]
故所述四阶项展开与实根 \(O(d^{-2})\) 精度严格成立。

## 5. 实验、权限、限制和下一问题

实际运行 R312_verify_third_order.py --numeric：
1. SymPy 1.14.0 通过八个代数项恒等式检查（PASS），包含 β/γ/η 与式 (8) 的系数；
2. mpmath 60 位对 d=30,60,100,250,400,600,1000,1500 的实根近似进行交叉检查。分组 r>45 的正尾另给出上界，但数值根本身不是经过区间算法认证的严格界。d=100、400、1000、1500 时 residual*d² 约为 1.47443、1.48335、1.48505、1.48542。完整输出见同目录 JSON；数学全 d 结论基于解析余项而非有限八点观测。

GitHub 登录 awdawmip 有仓库 admin/push。原生 em_control_tasks 返回 CONTROL_QUOTA，em_session_start 返回 STATIC_READONLY_SCOPE_DENIED 且 operation_sent=false；活跃 Owner 未获权威核实。本文件为非冲突独立作者研究，不抢占任何正式 Task 或执行 CLAIM，不构成 Result/Driver 独立数学接纳。活动 RA-R3T11-20261026-R312-THIRDORDER 已登记至项目 main，源提交 38d057473e0606d5d800bd8fa7b55c563daa28fa。P000 与 ACTIVE 世界观均未修改。

R312 只是 A>U **充分证书**的实临界根局部精化；它没有改善 R310 的全 d 正性楔形 c=47/20，也没有证明实际 D_d 在 n>=4d+4 全范围正。下一单元：对 R307 的全部 0≤s<d Newton 系数 K_s(d) 构造随 s,d 共同增长的统一正性表示或寻找大 d 精确反例；此项才可能突破当前二次充分上界的结构障碍。N_peak=81 仍开放。

科学状态：R312_AUTHOR_PROVED / SYMBOLIC_8_PASS / NUMERICAL_EIGHT_SAMPLES / NATIVE_OWNER_UNVERIFIED / NO_CLAIM / DRIVER_UNREVIEWED / NOT_ADMITTED。
