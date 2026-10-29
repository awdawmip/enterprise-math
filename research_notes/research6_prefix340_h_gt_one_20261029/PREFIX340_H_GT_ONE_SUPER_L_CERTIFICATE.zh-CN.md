# PREFIX-340：h>1 无反足对与严格超 L 恢复风险双窗口

日期 2026-10-29。状态：AUTHOR_SIDE_EXACT_RATIONAL_PROOF / UNREVIEWED / NOT_ADMITTED。贡献者：本 ChatGPT 进取数论研究6 真实对话，本地标识 EMR6-PREFIX340-LOCAL-20261029T0455Z（非 Source 身份/CLAIM）。

## 规范输入和科学模型
本轮固定 GLOBAL_KNOWLEDGE_V1 main@af7078ea2c398adb2c9009d23bbf3df01483880a 与 Enterprise Math main@c7c8b0ea6797e9a549073d0babe7ec67e78cb893，读取两份全局入口、P000（原件 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc）、ACTIVE 世界观、项目 AGENTS、研究员入口、portable research 及自主研究协议。原生控制 tasks 返回 CONTROL_QUOTA；Sites research_authority_granted=false。身份不冒用原有研究员。

接续 PREFIX-339 六来源根盒/代数全域穷尽：[完整证明](https://github.com/awdawmip/enterprise-math/blob/0f3435bba1f62bb86967edd5e7b13bb8cca31ee5/research_notes/research6_prefix339_phase_thresholds_20261029/README_PREFIX339.md)。仅限辅助静态 S7-3 BRC C³，非原生 X6、三维切片或物理相位定理。

\[
A=\begin{pmatrix}4&4&0\\0&-4&4\\-5+3i&0&-3+i\\-2-2i&4+4i&2+2i\\-2&0&5+2i\end{pmatrix},\quad U=A/8,\quad\lambda=10/61.
\]
五 Port 的每项质量在读出前保留九个有序带来源路径对：
\[
Q_j(a)=\sum_{k,l=1}^3(U_{jk}a_k)\overline{(U_{jl}a_l)}=|(Ua)_j|^2.
\]
六个来源相位轨道具有相同 q=(2125/3721,200/3721,29125/29768,5825/7442,31525/59536)，每个分量严格在 (0,1)。观察报告 R(h) 仅第三 Port 的虚部参考 h，其他九个实/虚参考均0，逐分量误差容限1。S(h) 代表完整允许状态的**未取相位商**集合。比较基准 L=1062562/458329。

## 定理 A：整个宽窗口仍超 L

前驱六个有理 Banach 认证根盒中的两个，取 a₄、a₅；规范相位 a=(x1+ix2,x3+ix4,x5)，x5>0。精确有理中心及共同根盒半径 rho=10^-8：

c₄=(3.972277190,-3.655156020,5.069231734,1.852070781,7.206948698)；
c₅=(3.826943394,0.866306597,5.391314313,-1.020335300,8.029290029)。

本轮独立从 A 构造两个盒的 F、Jacobian J、Hessian H，验证 Newton-Banach 映射 N(x)=x-J(c)^(-1)F(x) 的 eta<10^-9、K<30、eta+K*rho²/2<rho、K*rho<1；各盒有且仅有一个真来源。两盒第五坐标幅值不交，因此两来源不属于同一整体相位轨道。

令 zeta_w=(24+7i)/25、eta_w=(-3-4i)/5（均为单位模），p_w=lambda*zeta_w*a₄、v_w=lambda*eta_w*a₅。有理根盒严格证明两点第三 Port 虚部都 **大于14/25、且小于1**。故对每个 1<h<=39/25，两点均满足报告虚部窗 [h-1,h+1]，其他九项由 q_j<1 自动满足。用精确距离下界得
\[
\boxed{\forall\,1<h\le39/25:\quad\operatorname{MEB}^2(S(h))>62/25=2.48>L.}
\]

## 定理 B：更高风险的窄窗口

改取 zeta_s=(513+184i)/545、eta_s=(-133-156i)/205，两相位均有单位模。p_s=lambda*zeta_s*a₄、v_s=lambda*eta_s*a₅ 的第三 Port 虚部均**严格大于51/100、且小于1**。因此
\[
\boxed{\forall\,1<h\le151/100:\quad\operatorname{MEB}^2(S(h))>257/100=2.57>L.}
\]
特别 h=3/2 位于该窗口。

两个定理的证书均为如下**有理区间证明**：令 D₀ 是根盒中心生成的两点差，B 是其所有复坐标实/虚分量绝对值之和。两个五维根盒误差各不超过 sqrt(5)*rho，复单位相位不改变欧氏范数，故真实差向量偏差 <eps=6*lambda*rho。于是
\[
\frac{\|D_0\|^2-2\varepsilon B}{4}
\le\frac{\|p-v\|^2}{4}
\le\frac{\|D_0\|^2+2\varepsilon B+\varepsilon^2}{4}.
\]
精确程序分别检查左端>62/25、>257/100。两点最小包围球平方半径恰为 ||p-v||²/4，接触权均1/2；这只是完整 S(h) 的**下界**，不是求得整个 S(h) 的最优球。

虚部报告误差由精确线性误差
\[
\epsilon_{\rm Im}(\xi)=\frac{\lambda\rho}{8}\bigl(
|\Re(\xi A_{31})|+|\Im(\xi A_{31})|+|\Im(\xi A_{33})|
\bigr)
\]
覆盖（A_{32}=0）。对于任意 h>1，任何允许来源都具有 Im((Ua)_3)>=h-1>0；反足态 -a 的同一读出虚部为负，故整个 S(h) **不存在同时相容的反足状态对**。因此超 L 不依赖反足点存在。

## 定理 C：全六轨道统一球上界

设 u=U 第三行，||u||²=11/16，任意 a∈S(h) 满足 Im(ua)>=h-1。取显式共同球心
\[
c_h=\frac{i(h-1)}{\|u\|^2}\overline u^{\,T}.
\]
直接极化得
\[
\|a-c_h\|^2
=\|a\|^2-\frac{2(h-1)}{\|u\|^2}\Im(ua)
+\frac{(h-1)^2}{\|u\|^2}
\le\|a\|^2-\frac{(h-1)^2}{\|u\|^2}.
\]
对**全部六个**前驱冻结的有理根盒，逐个检查 lambda²||a_j||²<30014/10000。结合 PREFIX-339 已给的六根存在/穷尽证明，h=3/2 的完整纤维严格满足
\[
\boxed{257/100<\operatorname{MEB}^2(S(3/2))
<30014/10000-4/11<66/25=2.64.}
\]
全六轨道的穷尽和剩余四个盒存在性是明确依赖的前驱作者侧证书；本轮独立证明第4、第5盒的存在唯一性及所有六盒的范数区间。完整 MEB 精确最优值与其全部正接触权未解决。

## 验证及后继

实际执行 Python 3 / SymPy 精确有理校验，PASS_AUTHOR_SIDE_EXACT_RATIONAL_WITH_FROZEN_SIX_ORBIT_EXHAUSTIVENESS。覆盖全部10个非零三阶子式、45个有序来源 BRC 路径对、两根 Banach 收缩、六来源范数上界、两组单位相位及报告相容、距离区间和统一球上界。完整运行程序及实际机器 JSON另见本轮研究包，后继问题见 NEXT_PREFIX341.md。

尚未完成：六条连续相位弧的精确全体最小球、双非零报告完整球、相位商minmax、辅助 BRC 至 P000 原生 X6 / 三维切片第三坐标 / Detector / 联合关系和时间演化的保真映射。本成果是作者侧证明；不表示 Source Result、独立 Driver 审查或正式 admitted。
