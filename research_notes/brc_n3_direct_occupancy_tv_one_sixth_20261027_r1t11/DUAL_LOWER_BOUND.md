# N=3 双概率律压缩最优常数：严格正下界

日期 2026-10-27；作者侧 portable 研究，EM-R1-20261027-2005-D537A303；AUTHOR_PROVED / UNREVIEWED / NOT_ADMITTED。

**精确结论：**

\[
\boxed{\frac{15}{2527}\le K_*\le\frac16}.
\]

其中对于冻结的15前缀、8正概率终端双律树、共同即时随机决策策略，T∈{0,1,2,3}，

\[
K_*=\sup_{0<s_a,s_b<1/2,\ s_a\ne s_b}\sup_{\pi\in\mathcal P_{\rm full}}
\inf_{\sigma\in\mathcal P_{\rm compressed}}
\frac{\max_{R=P,Q}\operatorname{TV}(\mathcal L_R^\pi(T,D),\mathcal L_R^\sigma(T,D))}{|s_a-s_b|}.
\]

**上界：** 本目录 PROOF.md 的真实非对角树 Q 占用质量压缩构造，对所有完整历史行为策略同时实现两律 TV≤|s_a−s_b|/6；终止时间边际也严格保真。

**下界：** 复用并核读了之前不可变发布的 [精确 facet 定理](https://github.com/awdawmip/enterprise-math/blob/26176ded01b1bb6227b66c6dae612081a1a114df/research_notes/brc_n3_reverse_crossing_exact_facet_20261027_1801_r1/PROOF.md) 及其 RESULT.json。在 (s_a,s_b)=(2/5,1/3)，已验证所有压缩策略的观察量满足

\[
J=874P(D=Q)+1131Q(D=P)+121E_P[T]-53E_Q[T]\ge 851,
\]

但存在合法完整历史策略 π_* 使 J(π_*)=850，因此对任意压缩 σ 均有 J(σ)−J(π_*)≥1。

令 ε_R=TV(L_R^{π_*}(T,D),L_R^σ(T,D))。对 P，f_P(t,d)=874·1_{d=Q}+121t，其值域跨度 874+3×121=1237；对 Q，f_Q(t,d)=1131·1_{d=P}−53t，其值域跨度 1131+3×53=1290。利用有界函数期望对全变差的标准不等式，

\[
1\le J(\sigma)-J(\pi_*)\le1237\varepsilon_P+1290\varepsilon_Q
\le2527\max(\varepsilon_P,\varepsilon_Q).
\]

这对全部压缩 σ 成立，**没有额外要求 σ 保留时间边际**。因为本模型 |s_a−s_b|=1/15，故 K_*≥15/2527。所有系数、J(π_*)=850 及 15/2527 均通过 Python 标准库 Fraction 核算；下界的真正数学依据是前一不可变 facet 的完整历史见证与压缩普遍不等式，而非抽样枚举。

本推论明确区分某个直接平均算法的最坏误差与对全部压缩器取 inf 的真正误差。原 facet 仍是作者侧尚未独立 Driver 审查的结果；本推论是以该证明为数学依赖的作者推导，不能冒充正式 Result、Lean 证明或 P000 原生六维 Cell 定理。下一问题：提高 15/2527 或降低 1/6，求最优局部斜率及恰当的双律耦合证书。
