# C302 — 125条正有理辅助路径的整数标量公因子证书

**2026-10-25 · AUTHOR_EXACT · 上游条件性证明 · NOT_SOURCE_ADMITTED**

研究对象为冻结的 C195/H168 79条正有理支路辅助模型；不适用于原生 GF(2)-BRC、带相位端口的支路运算或 P000 六维离散 Cell。全球规范只读快照 \`GLOBAL_KNOWLEDGE_V1 main@6c6422241069e69be06085e0ace553865c07a524\`；EM 基准 \`main@577a11b1f9ff2f1844b83ba0714e2a60eeae85ce\`。C300 的两个确切线性因子约去来自作者证明提交 \`5f03468054ef8cfa14b19eea69ca044d0f5a53dc\`；C301 的连续短区间分母上界来自 \`a616a2443d9d4083c0024f3f6841e782b2e62ca8\`。它们的作者级条件没有被本轮升级为独立审查。

## 严格命题与精确构造

冻结路径编号 \(i=0,\dots,124\)。对于函数 \(f_i(t)=F(w_i+t d_i)/2^{128}\)，令 C298 的79个支路公共分母为

\[
D_i^{full}(t)=s_i\prod_{q\in G_i}q(t)^{e_i(q)}
\]

其中 \(s_i=\mathrm{lcm}_{j=0}^{78}d_{ij}>0\)，\(q\in\mathbb Z[t]\) 均为本原整系数多项式，在 C293 指定短区间正值。第 \(j\) 支路按冻结的 C298 分式规范化后，具有有符号整数分子系数 \(c_{ij}\)、整数分母标量 \(d_{ij}\mid s_i\)、整数分子多项式因子列表 \(N_{ij}\) 和分母因子的次数 \(\nu_{ij}(q)\)。因此

\[
A_i^{full}(t)=\sum_{j=0}^{78}
m_{ij}\left(\prod_{n\in N_{ij}}n(t)\right)
\prod_{q\in G_i}q(t)^{e_i(q)-\nu_{ij}(q)},
\quad m_{ij}=(s_i/d_{ij})c_{ij}\in\mathbb Z.
\tag{1}
\]

定义精确正整数

\[
\boxed{L_i=\gcd\left(s_i,\;\left\{\,
|m_{ij}|\prod_{n\in N_{ij}}\operatorname{content}(n)
\,\right\}_{j=0}^{78}\right).}
\tag{2}
\]

\(\operatorname{content}(p)\) 为整系数多项式系数绝对值的 gcd。**定理：**全部125条路径都有 \(L_i>1\)。C300 两项已证明的本原一次多项式消去以后，\(L_i\) 仍同时整除约分后分子 \(A_i^{red}\) 与分母 \(D_i^{red}\) 的每个系数。因此

\[
f_i(t)=\frac{A_i^{red}(t)/L_i}{D_i^{red}(t)/L_i}
\]

为准确的整多项式标量约分，而非采样近似。它**不声称** \(L_i\) 是最大的公因子；真正的最简整数分子—分母对仍未求完。

## 证明

Gauss 引理给出各项

\[
\operatorname{content}\left[
m_{ij}\prod_{n\in N_{ij}}n
\prod_q q^{e_i(q)-\nu_{ij}(q)}
\right]=|m_{ij}|\prod_{n\in N_{ij}}\operatorname{content}(n)
\]

因为每个 \(q\) 为本原多项式。(2) 因而整除 (1) 的每项所有系数，从而整除 \(A_i^{full}\) 系数；又因 \(L_i\mid s_i\)，它整除 \(D_i^{full}\) 系数。由 C300 **精确有理留数**证明（并非只凭有限域零值），存在两个本原线性因子 \(q_{i,1},q_{i,2}\)，使
\(A_i^{full}=q_{i,1}q_{i,2}A_i^{red}\)、
\(D_i^{full}=q_{i,1}q_{i,2}D_i^{red}\)，且两个商仍在 \(\mathbb Z[t]\)。再次运用 Gauss 引理，
\(\operatorname{content}(A_i^{full})=\operatorname{content}(A_i^{red})\)。
因此 \(L_i\mid\operatorname{content}(A_i^{red})\)；同时
\(D_i^{red}=s_i\prod_{q\notin\{q_{i,1},q_{i,2}\}}q^{e_i(q)}\)，所以
\(L_i\mid\operatorname{content}(D_i^{red})\)。证毕。

若 C301 已验证的有理数连续短区间上界为
\(0<D_i^{red}(t)\le U_i\)，则标量约分后
\(0<\bar D_i(t)\le U_i/L_i<2^{H_i'}\)；
\(H_i'\) 为使该严格不等式成立的最小非负整数。对于不恰好是根的二进制有理 \(t=k/2^b\)，因为
\(\deg(\bar A_i-\bar D_i)\le d_i\)，非零整多项式评价满足
\[
\boxed{|f_i(k/2^b)-1|>2^{-d_i b-H_i'}.}
\]
继承 C297 的归一化向外区间宽度 \(<2^{134-P}\) **且该上游前提成立时**，选择 \(P\ge d_i b+H_i'+134\) 能保证非根点严格判号。精确根不具有此严格判号终止结论。

## 完整125条精确算术结果

- \(125/125\) 路径的式(2)以及整除关系：**PASS**。\(L_i\) 的位宽范围 **273–418**。
- \(125/125\) 个连续参数短区间的精确有理数分母界重新计算：**PASS**；最高 \(H_i'\) 从 **13702** 降为 **13400**（索引63）。
- 各路径的严格充分精度减少 **272–418** 位；对于 \(b=512\)，124条352次路径的统一充分精度由 **194060** 降至 **193758**（保证减少302位）。特殊索引28为265次，精度由 **146581** 降至 **146163**。
- 另外，计算 \(g_i^0=\gcd(s_i,A_i^{full}(0))\)，证实每条 \(L_i\mid g_i^0\)，且真公因子 \(g_i=\gcd(s_i,\operatorname{content}(A_i^{red}))\) 必满足 \(L_i\mid g_i\mid g_i^0\)。仅检查常数系数**不**是求得真实 \(g_i\)。
- 作者精确脚本结束回执 \`C302_CERTIFIED_SCALAR_NORMALIZATION_PASS\`。另一独立构式的 Fraction 有理函数交叉检查在索引 \`0,8,24,28,40,63,64,96,124\` 的9个中点全部通过，回执 \`C302_INDEPENDENT_RATIONAL_SPOTS_9_PASS\`。9个点不冒充125路径的独立审核。
- 算术为整数、Python Fraction、exact gcd 和模整数系数。区间连续结论继承了 C301 对全部因子单调性的解析证明；C297 区间宽度上界与 C300 的完整分母最简性均未由本轮重新独立审核。

**可复验材料：** 本提交的 C302 Python 参考程序、审计摘要及压缩的125路径整数标量证书；全部冻结 C275/C288/C293/C298/C300/C301 输入、全文扩展论证、125行未压缩证书与九点复核程序另收录于 \`EM_C302_SCALAR_CANCELLATION_125_EXACT_PORTABLE.zip\`。代码需要该包的冻结输入，在 GitHub 宿主上未单独运行。其自证哈希不是数学接纳或所有权签名。

## BRC 保真与下一问题

本轮应用 C298/C300/C301 **正有理79支路展开与共享分母工具**（\`REUSE_APPLIED\`）。标量 \(A/D\) 的约分只对目前声明的正有理总量观察量无损；C300 的两个相反留数不允许据此在原生 BRC 中抹除支路身份、相位、端口、路径及其未来操作残差。P000 世界观不改动。

**C303 的精确开放问题：** 计算125条路径全部的
\(\gcd(s_i,\operatorname{content}(A_i^{red}))\)，确定真正本原的整数分子—分母对；若用模素数或插值，须处理小素数整除范德蒙行列式/阶乘时“整数点值全为零但系数不全为零”的陷阱。后续对原生 GF(2)-BRC/X6 的保真映射须独立证明。

**控制状态：** 原生 \`em_control_tasks→CONTROL_QUOTA\`，\`em_session_start→STATIC_READONLY_SCOPE_DENIED\` 且 \`operation_sent=false\`；活动记录仅位于作者研究分支，未验证活跃 Task owner，也无 Source CLAIM/Result/Driver admission。本成果为持久的作者级独立研究记录，不是正式数学接纳。
