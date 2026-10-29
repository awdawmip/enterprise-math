# PREFIX-346｜十纳量级隔离六弧 BRC 恢复风险与基准 L 的相交

**日期：**2026-10-29。**研究状态：** AUTHOR_SIDE_EXACT_RATIONAL / UNREVIEWED / NOT_ADMITTED。本笔记是可复用的静态辅助 S7-3 复三维、保留整体相位的数学证书，不是正式 TASK CLAIM、Driver Review 或原生 X6 物理证明。

## 1. 严格结论

设固定准确质量的全部真实复来源共同观测纤维为 S(h)，六个已独立认证存在的具体复来源所生成的完整允许相位弧并集为 T6(h)⊂S(h)。第三 Port 的虚部报告为 h>1，其余九项为 0，各分量容差 1。以保留整体相位的欧氏最小包围球平方半径 MEB² 度量恢复风险，定义 L=1062562/458329。

令

\[
h_-=\frac{166639681}{100000000}=1.66639681,\quad
h_+=\frac{83319841}{50000000}=1.66639682,\quad
h_+-h_-=10^{-8}.
\]

本轮对精确输入证明：

\[
\boxed{\forall\,1<h\le h_-:\quad \mathrm{MEB}^2(S(h))>L+10^{-10}.}
\]

该**全部真实来源**下界不需要 PREFIX-336/339 的六轨道全域穷尽证明。另一方面，

\[
\boxed{\mathrm{MEB}^2(T_6(h_+))<L-10^{-9}.}
\]

第二项是**六条具体来源弧的全连续相位上界**，不是未经证明的全部 S(h_+) 上界。T6(h) 在 [h_-,h_+] 上以 Hausdorff 距离连续，因此存在至少一个 h_c∈(h_-,h_+) 满足 MEB²(T6(h_c))=L。**交点唯一性、完整 S(h) 的上界、原生 X6/Detector/时间映射仍待证明。**

## 2. 冻结的真实 BRC 来源

沿用 PREFIX-342/345 已认证的五 Port 有序复振幅：

\[
A=\begin{pmatrix}
4&4&0\\0&-4&4\\-5+3i&0&-3+i\\
-2-2i&4+4i&2+2i\\-2&0&5+2i
\end{pmatrix}, \quad U=A/8,\quad\lambda=10/61,
\]

\[
q=(2125/3721,\ 200/3721,\ 29125/29768,\ 5825/7442,\ 31525/59536).
\]

六个复来源 a_j∈C³ 均在 PREFIX-342 冻结的半径 10⁻²⁹ Newton–Banach 有理根盒内唯一存在。五 Port 的45个带来源标签有序路径对 \((U_{jk}a_k)\overline{(U_{j\ell}a_\ell)}\) 由前驱检查器本轮实际重新运行核验。将 \(w_j=(Ua_j)_3\)，则 \(|w_j|^2=q_3\)。

当 \(1<h<1+\sqrt{q_3}\) 时，十项报告的唯一非自动约束是 \(\operatorname{Im}z\ge h-1\)；其它 Port 及第三 Port 实部都因各 \(q_k<1\) 自动满足。六条相位弧的端点是精确复代数状态

\[
p_{j,\pm}(h)=\frac{\big(\pm\sqrt{q_3-(h-1)^2}+i(h-1)\big)\overline{w_j}}{q_3}\,a_j.
\]

完整弧以 \(x=u\,s_h,\ u\in[-1,1],\ s_h=\sqrt{q_3-(h-1)^2}\) 参数化为 \(z_h(u)=x+i\sqrt{q_3-x^2}\)，再由 \(\overline w_j a_j/q_3\) 提升；这不仅给出紧致性，也直接证明参数 h 的 Hausdorff 连续性。

## 3. 左端点：四条互异来源的严格正对偶

在 h_- 选择四个真实相位端点 (0,-)、(1,+)、(3,-)、(4,+)，以固定权重

\[
\alpha=(140253,100513,363029,396205)/10^6,\quad
\alpha_k>0,\quad\sum\alpha_k=1
\]

定义 \(\mu=\sum \alpha_k p_k\) 及 \(V=\sum\alpha_k\|p_k\|^2-\|\mu\|^2\)。本轮精确 Fraction/整数平方根包络证明

\[
\boxed{V(h_-)>L+10^{-10}.}
\]

对任何中心 b，\(\max_k\|p_k-b\|^2\ge V+\|b-\mu\|^2\ge V\)，从而 MEB²(S(h_-))≥V。由报告单调性 \(S(h_-)\subseteq S(h)\)（h≤h_-），得到全参数结论。h>1 强制第三 Port 虚部严格为正，因此不存在可行反足对。满列秩 A 与准确质量约束确保全部 S(h) 闭合且有界；四点确保非空。

## 4. 右端点：一个有理球心覆盖全部六条连续弧

取 C³ 中完全显式、每分量分母 10¹⁵ 的中心

\[
c=(0.379558420333054-0.620581010752923i,\ 
   0.012435707126596-0.048952050756643i,\ 
   0.109614732382381-0.326659837617947i).
\]

不需要先证明 c 最优。以固定的六根有理区间和 \(s_{h_+}\) 的分母 10³⁶ 有理平方根包络直接核验十二端点：

\[
\boxed{\forall j\in\{0,\ldots,5\},\ \sigma\in\{+,-\}:\quad
L-\|p_{j,\sigma}(h_+)-c\|^2>10^{-9}.}
\]

定义 \(t_j=\langle c,a_j\rangle/w_j\)。同一个严格有理区间检查还得到 \(\operatorname{Im}t_j<-7/10\)（六个 j 全部）。对弧内 \(z=x+i\sqrt{q_3-x^2}\)，平方距离恒等于

\[
\|a_j\|^2+\|c\|^2-2x\operatorname{Re}t_j+
2\sqrt{q_3-x^2}\operatorname{Im}t_j.
\]

由于 \(\operatorname{Im}t_j<0\)，它在整个允许区间 \([-s_{h_+},s_{h_+}]\) 严格凸；其最大值必在两个端点之一。故一个有理中心严格覆盖六条**完整连续弧**，并证明上界 MEB²(T6(h_+))<L−10⁻⁹。不是角度网格或浮点优化证书；浮点数只用于事前选择候选中心，所有最终判定来自精确有理区间。

## 5. 本轮执行、边界和接续

实际在 Python 3/SymPy 环境运行 verify_prefix346.py，重新执行 PREFIX-342 的六根 Banach 证书和五 Port 共45项来源有序 BRC 路径对；所有判据使用 Fraction 与 isqrt，返回 PASS_AUTHOR_SIDE_EXACT_RATIONAL。检查器实际输入为该目录 verify_prefix346.py 与前驱不可变源 verify_prefix342.py。精确机器全文 RESULTS_PREFIX346.json 由脚本生成；本目录 RESULTS_PREFIX346_SUMMARY.json 记录保守可独立复算的严格结果。前驱脚本 SHA-256: 9fe2b8126e7ed68f52e91ccb5bcfc2ea06776bb02e3a806e4d27f2ff0c65b524；本轮实际执行脚本 SHA-256: 47e2a3509dc9c544af8aefaa9f2ae99783cbee1850560104fe99bcb0a051b9f7。

复现前驱：从 Enterprise Math 不可变科学提交 1180caebc14a3470bca9624d8cb56d1467d6dc3d 下 research_notes/research6_prefix342_exact_five_contact_20261029/PREFIX342_SOURCE_PACKAGE.tar.xz.b64 恢复 verify_prefix342.py，将其与本目录 verify_prefix346.py 放在同一目录运行 python verify_prefix346.py。完整本地程序及机器原始 JSON 另留于本次交付包，可核对脚本 SHA-256；不能把未取得的远程额外实验误报成执行成功。

输入快照：GLOBAL_KNOWLEDGE_V1 main@7a2fb21f48d9966d8bcab282c4ca459faed004a5；Enterprise Math main@3e63f90523a75fc7250c2c603f556578152fc354。GitHub 实读账户 awdawmip 具仓库写入权限；Sites 实读 research_authority_granted=false，活跃 owner 查询 CONTROL_QUOTA，因此没有以他人身份领取 CLAIM、发布正式 Source Result 或宣称独立审查。此处是普通研究笔记的作者侧保存，不是状态机数学准入。

**下一单元 PREFIX-347：** 在 [h_-,h_+] 内对候选五接触 Gram 定理给出整区间导数/正权与完整弧内含证书，从而证明该交点唯一；独立审核 PREFIX-336/339 六来源全域穷尽后，才能将此 T6 上界转为全部 S 上界。并继续跨辅助 C³、P000 X6、三维切片第三分量、联合观察/Detector/时间演化的保真转移。