# R458｜signed BRC 右边缘 s=159—162 无限参数证书与精确主系数

日期：2026-11-01。级别：AUTHOR_SIDE_EXACT_SYMBOLIC / UNREVIEWED / NOT_ADMITTED。P000 及 ACTIVE 世界观均未修改。

## 固定输入和精确对象

本轮选择且保持同一 GLOBAL_KNOWLEDGE_V1 当前 main 快照 301e34842658e23e49724e5dd846a9952258ba50；Enterprise Math 主干快照 96dbd541e2c8f4f873aaf4ee37a42cf6af0f3278。已读 00_BOOTSTRAP、OPERATING_MANUAL、TASK_RESEARCH 入口、P000 原件及投影（投影 canonical_blob_sha1 与原件 Git Blob 同为 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc）、ACTIVE 世界观、JOINT 观察保真、HEARTBEAT X6、现行 portable research 协议。直接接续 R457 不可变提交 10b55e0d7da1ff24372b7a698bb9bd19cf6c4333；使用 R452 的 EOR 分解、R450 的 PF3 严格充分判据和 R447 的左端窗口，继承其作者侧证据等级。

研究对象为原始 signed BRC **辅助标量**，而非正权支路质量或原生 X6 动力学。令 r=2k+1，2≤s≤r，C_k=(2k)!/[k!(k+1)!]，

\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},
\quad B_s(k)=H(2k+1,s)/C_k.
\]

令 a_j=H(r,r-j)，j=0,…,r-2；其余为0。与 R457 保持一致，下标 s 的相邻子式使用 a_s=H(r,s) 的简写而非 Toeplitz 列 j 下标：

\[
D_{2,s}=H(r,s)^2-H(r,s-1)H(r,s+1),
\]
\[
D_{3,s}=H(r,s)^3-2H(r,s-1)H(r,s)H(r,s+1)
+H(r,s-2)H(r,s+1)^2+H(r,s-1)^2H(r,s+2)
-H(r,s-2)H(r,s)H(r,s+2).
\]

## 定理 A｜四个无限参数位置的严格正性

对每个 s∈{159,160,161,162}、所有整数 k≥floor((s+2)/2)，均有 D2_s>0、D3_s>0。

证明构造：k0=floor((s+2)/2)、u=k-k0≥0、F=(2s+4)!。对 t=s−2,…,s+2，令 Q_t(u)=F B_t(k0+u)。利用 R452/R457 精确 E_t O_t R_t 分解，Q_t 是整数系数多项式。写 A=Q_s，B=Q_(s−1)，C=Q_(s+1)，D=Q_(s−2)，E=Q_(s+2)，定义

\[
P_{2,s}=A^2-BC,\quad
P_{3,s}=A^3-2ABC+DC^2+B^2E-DAE.
\]

于是 D2_s=C_k² P2_s/F²，D3_s=C_k³ P3_s/F³；C_k、F 均正。精确 Z[u] 程序从原始 EOR 公式逐步生成两多项式，**穷尽所有系数**并逐一测试严格大于零，同时精确核对 Desnanot–Jacobi 恒等式

\[
A P_{3,s}=P_{2,s}^2-(B^2-DA)(C^2-AE).
\]

计算证据详见 R458_EVIDENCE_ALL.json 及可执行 R458_VERIFY.py。四个 s 的 (deg P2,deg P3；正系数个数；哈希) 分别为：

- 159：(636,954；1592；d58b62977aa11030fa75d6abd8413e103352c8036502286f67a760a0e652b8c8)；
- 160：(640,960；1602；65a85978e57282fe5d46d0589fe17c4a52ab319aa5704033393a035bd64380d7)；
- 161：(644,966；1612；66700c34b2a6517d2a30e4fb6a26901eca0d958003e672f459ddf8a72e6f4f71)；
- 162：(648,972；1622；f7c5c0a45f9a6da1630d2754bc18b8c3987027a41eb4e5caa724a6af7584f654)。

合计 8 个完整多项式、6428 个严格正整数系数及4项完整多项式恒等式通过。各 s 独立运行 python R458_VERIFY.py s s 均终止并打印 R458_EXACT_PASS；每个 s 在 k0、k0+1 两点、五个 t 上分别核验原始 signed 卷积、正 Catalan 变换及 EOR，合计40+40个独立整数等式交叉检查。全程 Python 任意精度整数；这是针对固定四个 s、无限多个 k 的符号证书，非有限 k 外推。

## 定理 B｜原始辅助 Toeplitz 半无限 PF3 拼接新增 r=183、185

合并 R452—R457 对 2≤s≤158 已证的作者侧右端证书与本定理 A：任意奇数 r≥165 和 2≤s≤162，所需 D2_s,D3_s>0。特别是 r=183、185：当 j≤22，调用 R447 的左端证书；j≥23 时 s=r−j≤162 且 s≥2，由右端证书覆盖。两端覆盖全部合法 j=0,…,r−2；加上系数正性和 R450 的局部充分判据，得到半无限辅助 Toeplitz T^(183)、T^(185) ∈ PF3，作者侧未审稿证明链将此前 99≤r≤181 的奇数范围延伸至 99≤r≤185。

作为直接交叉验证，R458_ROW_VERIFY.py 对两行每个合法位置的系数和相邻二、三阶子式分别进行366次严格整数判号，共1098次全部通过；另有16项原始卷积和16项交替 Catalan 等式比对。整行验证支撑该两个具体 r，本身不替代定理 A 的无限 k 证明。

## 解析增量 C｜各固定 s 的显式最高次正系数

对任意整数 s≥4，由 R451 已有 B_s(k)=c_s k^(2s)+O_s(k^(2s−1))，其中 c_s=2^(3s−2)/(2s)!>0。定义 L2_s = lim_(k→∞) [D2_s/(C_k² k^(4s))]，L3_s=lim_(k→∞) [D3_s/(C_k³ k^(6s))]。直接将 c_(s+d)/c_s = 8^d (2s)!/(2s+2d)! (d=−2,…,2) 代入行列式并作有理因式化，得到

\[
\boxed{L_{2,s}=c_s^2\,\frac{4s+1}{(s+1)(2s+1)}>0}
\]
\[
\boxed{L_{3,s}=c_s^3\,\frac{2(64s^3+96s^2+20s+3)}
{(s+1)^2(s+2)(2s+1)^2(2s+3)}>0.}
\]

此为任意 s≥4 的**解析有理恒等式**，不依赖四个 s 的符号枚举。作为交叉检查，已使用整数/有理数算术对 s=4,…,12 共9个 s 核对 EOR 多项式的最高系数，二阶、三阶公式全部相等。该公式定量刻画固定 s 时最高阶正性，但中低阶系数的统一正性仍需新论证。

## BRC 类型、权限和下一问题

BRC 复用决议：REUSE_EXECUTED（复用 R452 EOR 精确带符号消元和 R450 Toeplitz 子式判据）。支路层级的完整身份与相消信息由原始生成函数公式保留，最终 H(r,s) 是声明后的标量观察；这里仅处理该观察的相邻子式，不宣称标量读出保持原生 X6 的路径、联合关系、时间或物理演化。正 Catalan 形式是所述 scalar H 的已证代数恒等改写，不将 signed 支路解释成正质量。

本轮实读 GitHub 身份 awdawmip、仓库权限 push/admin=true；原生 Gateway status 显示 research_authority_granted=false 与 CODE_REVIEW_REQUIRED，当前活跃任务查询 em_control_tasks 返回 CONTROL_QUOTA。未确认 live owner；作者侧稿件不取得 CLAIM/Result/Driver review，不改原任务 owner。P000/ACTIVE 世界观保持原字节。

下一单元：优先检查 s=163、164 的完整 Z[u] 证书与 r=187 的拼接；并研究上式主系数的正性是否可延展为对全部 s 和所有次项的统一 Turán 正性，不以正的最高系数推断全部系数正。若系数证书失效，继续用原始整数子式逐项鉴别真实负值与证书充分条件失效。