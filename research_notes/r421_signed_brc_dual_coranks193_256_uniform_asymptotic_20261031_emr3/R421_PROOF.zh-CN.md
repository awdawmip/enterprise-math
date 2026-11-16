# R421｜带符号 BRC 辅助 Turán：64 条反向无限正性定理与任意固定余阶的解析尾部

日期：2026-10-31。状态：AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED。结论仅适用于原始带符号 BRC 辅助组合读出，未建立到原生 X6 动力学或物理残差的保真映射。

## 定义及定理

对 r≥s+1、s≥3，令

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

**定理 A（精确计算机辅助）：** 对全部整数 193≤m≤256 和全部整数 s≥3，均严格有 \(\boxed{D_{s+m,s}>0}\)。每个固定 m 是一个无界 s 的无限族；有限计算穷尽的是代数证书的全部系数。

**定理 B（纯解析）：** 对任意固定整数 m≥1、令 \(r=s+m\) 且 \(W_s=\binom{2s+m}{2s}\binom{2s}{s}>0\)，则

\[
\boxed{\lim_{s\to\infty}\frac{s^2D_{s+m,s}}{W_s^2}=\frac{4^m}{m+1}>0.}
\]

于是对每个 m≥1 存在有限整数 S(m)，当 s≥S(m) 时 D_{s+m,s}>0。定理 B 没有提供全 m 统一的显式 S(m)，也不直接覆盖定理 A 的全部 s≥3 域。

## 一、精确带符号恒等式及有限多项式证书

固定 m≥1，置 r=s+m。对 h∈{−1,0,+1}，记 q=s+h、n=m−h、B_q=binom(2q,q)。中心二项式比率

\[
\rho_q(d)=\binom{2q}{q+d}/B_q
=\prod_{j=0}^{d-1}\frac{q-j}{q+j+1}\quad(d\ge0)
\]

对 d>q 也给出零，负偏移按对称性取 |d|。逐项展开原始 (1−t) 带符号二项式卷积：

\[
\frac{\delta_{r,q}}{B_q}=\sum_{k=0}^{n}\binom nk
\left(\rho_q(|n-2k|)-\rho_q(|n-2k-1|)\right). \tag{1}
\]

令 x=s−3≥0、L_h=n+1。构造整数多项式

\[
Q_h(x)=\prod_{j=1}^{L_h}(q+j),\qquad
F_{h,d}(x)=\prod_{j=0}^{d-1}(q-j)\prod_{j=d+1}^{L_h}(q+j),
\]

\[
N_h(x)=\sum_{k=0}^{n}\binom nk
\left(F_{h,|n-2k|}(x)-F_{h,|n-2k-1|}(x)\right).
\]

其中 0≤d≤L_h，空积为1。显式通分立即给出 \(\delta_{r,q}/B_q=N_h/Q_h\)。定义 \(W_q=\binom{r+q}{2q}B_q\) 与

\[
\lambda=\frac{W_{s-1}W_{s+1}}{W_s^2}
=\frac{ms^2(2s+m+1)}{(m+1)(s+1)^2(2s+m)}.
\]

置

\[
P_m(x)=(m+1)(s+1)^2(2s+m)N_0^2Q_{-1}Q_{+1}
-ms^2(2s+m+1)N_{-1}N_{+1}Q_0^2,
\]

\[
T_m(x)=(m+1)(s+1)^2(2s+m)Q_0^2Q_{-1}Q_{+1}.
\]

在全部合法整数 m≥1、s≥3 上严格成立

\[
\boxed{\frac{D_{s+m,s}}{W_s^2}=\frac{P_m(s-3)}{T_m(s-3)}}.\tag{2}
\]

T_m 在 x≥0 严格正。标准库精确整数程序 r421_cert.py 从上述乘积直接展开；对 m=193,...,256，64个 P_m 均恰有 4m+6 个**严格正**的整数升幂系数，次数4m+5，合计57,856个正系数。故对全部 x≥0，P_m(x)>0，式(2)证明定理 A。此证明是完整有限整数多项式系数证书，并非有限 s 采样外推。

**实际机器证据：** 八份完整原始 JSON 总计99,327,714字节，逐份SHA256和范围见 R421_EVIDENCE_SUMMARY.json。每份运行返回 R421_EXACT_PASS。独立程序不导入生成器，核对全部57,856项正系数、64个首项及其摘要，再从原始有符号 (1−t) 系数式在每个 m 的 s=3,5,17,257,1024 上复算960项 \(\delta\)，交叉核验320项 D 精确整式恒等式，全部通过。320点是交叉诊断；无限量词由式(2)和完整正系数证书保证。大型原始 JSON 保存在本轮本地完整研究包中；GitHub 提供确定性重建程序、精确摘要、独立校验器与本证明，不能把“可重建”误认为已将99MB原件逐份上传GitHub。

## 二、任意固定 m 的严格渐近定理及通用首项恒等式

对于固定非负整数 d，上述有理乘积在 q→∞ 时满足

\[
\rho_q(d)=1-\frac{d^2}{q}+O_d(q^{-2}).
\]

这是纯整数有理函数的代数首项求解，不是物理演化的近似计算。令 n=m−h，则有限和式(1)给出

\[
\frac{\delta_{s+m,s+h}}{B_{s+h}}
=\frac{1}{s+h}\sum_{k=0}^{n}\binom nk(1-2n+4k)+O_m(s^{-2})
=\frac{2^{m-h}}{s}+O_m(s^{-2})
\]

（用 \(\sum_k\binom nk=2^n\) 和 \(\sum_k k\binom nk=n2^{n-1}\)，n=0时后者为0）。另外 \(\lambda\to m/(m+1)\)。故

\[
\frac{s^2D_{s+m,s}}{W_s^2}
=s^2\left[\left(\frac{\delta_{r,s}}{B_s}\right)^2-
\lambda\frac{\delta_{r,s-1}}{B_{s-1}}\frac{\delta_{r,s+1}}{B_{s+1}}\right]
\longrightarrow4^m-\frac{m}{m+1}4^m=\frac{4^m}{m+1}.
\]

极限严格正，定理 B 得证。这证明对每个固定 m 仅有限多个 s 有可能不满足正性，尚不限制这些可能例外是否实际存在。

还可独立得到每个 m≥1 都成立的通用代数首项恒等式：\(\deg N_h=m-h\)，首项系数 \(2^{m-h}\)，\(\deg Q_h=m-h+1\)，首项为1。将它们代入 P_m 和 T_m 的定义，得到

\[
\deg P_m=4m+5,\quad [x^{4m+5}]P_m(x)=2^{2m+1}>0;
\quad\deg T_m=4m+7,\quad[x^{4m+7}]T_m(x)=2(m+1).
\]

这是一条对**所有 m** 的解析定理，不把它外推为所有中低阶系数均正。本轮64个完整整数多项式逐个核对了通用首项式。

## 证据范围、身份和接续

继承 R420 不可变作者侧提交 d4659e227a1a1a5fd0f35db5476ba1b87ec915c2；本轮固定读取 GLOBAL_KNOWLEDGE_V1 main@d310c5f090bd5883e89df4c5827468959073541b 和 Enterprise Math main@e4da8741fc91c6b584de6a61a9c8cd6b7ae1ed66。原始有符号支路、卷积与观察者范围保留在辅助整数代数层；P000及ACTIVE世界观保持不变。结论与完整原生X6三维切片/六维时空及物理实验的映射仍须单独构造并证明。

GitHub连接账户 awdawmip 的仓库写权限已确认；原生Site静态只读连接报告 research_authority_granted=false，活跃Owner任务查询返回 CONTROL_QUOTA。本成果只属于 AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED；没有正式 CLAIM、Result、独立Driver审阅或数学准入回执。

结合 R419 的固定 s≤256 带、R420 的 m≤192 带及本轮新带，以各自实际已证范围为前提，剩余重点象限缩为 s≥257、m=r−s≥257、r<2s²。下一步寻找 P_m 的跨 m 全系数归纳不变式或给出显式统一 S(m)；可对 257≤m≤320 继续生成精确证书并定位最早可能非正系数。