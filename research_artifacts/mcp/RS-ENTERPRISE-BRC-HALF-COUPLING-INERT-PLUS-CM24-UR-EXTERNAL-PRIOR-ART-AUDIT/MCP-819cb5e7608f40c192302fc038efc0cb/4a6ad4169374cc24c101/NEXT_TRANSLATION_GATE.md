# CM(-24) 下一最小 source translation gate

Date: 2026-10-11. Scope: directed/shared-context Driver direction scout, local memo only. Root requested this bounded analysis; no new Source session, claim, execution, branch, Result, Driver acceptance, or global prior-art classification is created.

**建议优先做一个“有向 first-normal scalar + 指定 p-adic lift”证据门。** 已有 level-3 period theorem 的 residual diagonal 公式只有 norm；补一个 H 分支不能撤销 norm 的方向丢失。只有固定来源真实给出 norm 之前、具有独立标定的 normal coordinate，并与原来的有限截断在 mod \(p^2\) 下精确比较，才值得继续把它作为 UR 等价候选。

当前研究者的 marked H→Fricke 局部证明是定向上下文中的未接受草稿；这里仅使用其报告的接口，不重复推导、不冒充独立数学评审。该草稿给出 \(P_H'(H_i)=U_i S'(216)\)，其 norm 为 \(N(U_i)S'(216)^2\)。有向导数可传送；norm-only scalar 无法单独恢复有向导数，也没有识别 \(G_p\)。

## 精确目标与截断精度

完整 exact-rational 定义保存在 EXACT_G_DEFINITION.json，来源是冻结 return §2：

\[
p=6m+1,\quad p\bmod24\in\{13,19\},\quad B_0=1,\quad
B_{k+1}/B_k=(6k+1)(3k+1)/(36(k+1)^2),
\]
\[
B_k=\frac{(1/6)_k(1/3)_k}{(k!)^2\,2^k},\quad
g_p=\sum_{k=0}^{p-1}B_k,\quad
h_p=\sum_{k=0}^{p-1}(12k+1)B_k,\quad G_p=g_p/p.
\]

全部有限项先作为 exact rational 保留；\(p\ge5,\ k<p\) 时分母均为 p-unit。UR 需要 \(g_p\bmod p^2\) 后除 p，得到 \(G_p\bmod p\)：
\[
G_p(-6Q_m'(1/2))=1,\qquad
G_p S_p^{(3A)\prime}(216)=-216^{m-1}/12\quad(\bmod p).
\]
LIFT 需要 \(g_p\bmod p^3\) 后除 p，得到 \(G_p\bmod p^2\)，并保留 \(h_p\bmod p^2\) 与原 \(R_p\)。冻结 parent 的精确式是
\[
G_p\equiv \Phi/p-\Phi_x/6+p\Phi_{xx}/72\pmod{p^2}.
\]
禁止把本轮 UR 的 mod-p 观察当作 LIFT 的完整载体。前序 valuation-profile 单元已表明 \(k>2m\) 的项具有 valuation 2：它们在 UR 的 \(g\bmod p^2\) 中消失，但除 p 后可以贡献 LIFT 的第二 digit。保持原截止 \(p-1\)，不凭无限级数、另一截断或 finite-field 名称替换它。

## 最小可判别门

选定一个固定 source 中已定义的对象 \(\rho_{p,i}\)，以及由 source 的 coordinate/q-expansion/character conventions 预先给定、不能按 UR 或回归值倒选的单位 \(c_{p,i}\)。要求实际证明或排除：
\[
g_p(1/2)\equiv p\,c_{p,i}\rho_{p,i}\pmod{p^2},
\qquad
c_{p,i}\rho_{p,i}S'(216)=-216^{m-1}/12\pmod p .
\]
第一式才是 missing divided-digit comparison；第二式才给 UR 的 exact normalization。对象所在 residue field、marked H lift、Frobenius conjugate sheet及其 descent 一并保留。不同 branch 经已证 multiplier 传送须得同一个 \(G_p\in\mathbf F_p\)，不能用 Norm 当作 descent 的默认替代。

PASS：固定 theorem/equation 提供有向 scalar、rational/CM lift、相同有限截断的 mod-p² 比较及上述 normalization，可做双向等价翻译。
PARTIAL：只有 \(g=0\bmod p\)、Hasse zero、\(S'\)、norm/inverse-square、valuations、未知单位或未知 sign。精确记录缺哪一个坐标。
KILL_THIS_SHORTCUT：只保留 norm、从平方结果任意选根、用待证 \(G_p\) 定义 \(\rho\) 或 normalization、lift 未指定、普通-locus公式跨到 supersingular 点、有限回归冒充全素数证明。此 verdict 只拒绝该接口，不宣称全球无解或数学目标完成。

## 为什么只补 branch 还不够

Betina–Lecouturier 1611.01044v3 Theorem 1.1（TeX 129–144）给
\[
\overline{\Phi}(e_i,e_i)/p=P_H'(H_i)^{-(p+1)}
\]
modulo principal units；§7.2 以 H 替代 lambda 宣称 N=3 analogue。此 observer 包含 valuation 和除 p 的首个 unit residue；精度上可以成为 UR 候选，但其 \(p+1\) 幂仍是 norm。选定 \(H_i\) 并记录 \(U_i\) 不能撤销这个幂；minus sign 在 p 为奇素数时仍不可见。完整 normalized S 或独立有向参数可以额外确定 \(S'\)，但这不是从 norm-only observer 重构，更不自动确定 \(G_p\)。

另一个独立障碍是 **p-adic lift**。令
\[
f_p(z)=\sum_{k=0}^{p-1}\frac{(1/6)_k(1/3)_k}{(k!)^2}z^k,\quad g_p=f_p(1/2).
\]
冻结系数传送给 \(f_p\bmod p=H_m(z)=Q_m(1-z)\)。对同一 mod-p 点的两个 lifts \(z_0=1/2,\ z_1=z_0+p\delta\)，有限 polynomial Taylor 展开给
\[
f_p(z_1)/p\equiv G_p-\delta Q_m'(1/2)\pmod p.
\]
SIMPLE 保证 \(Q_m'(1/2)\ne0\)，故所有 \(\delta\) 产生不同 divided digits，却具有相同 mod-p CM/Hasse fiber。只记录 supersingular branch/orientation 仍不足；source 必须匹配这里的 rational lift \(z=1/2\)，或明示并补偿 lift difference。特别不能默认 Teichmüller lift 等于 rational lift。此式是本 memo 的局部信息安全诊断，不是新 Source Result 或 UR 证明。

实际 v3 的 Introduction（TeX102/PDF extract20）只声明“Let p≥5 be a prime”；N=2 Theorem1.1 没有另列 p≡1mod4。Introduction 对 de Shalit 原 j 结果的介绍才写“up to a sign if p≡3mod4”，不能把它误写成本文主定理假设。N=3 Remark1 和 §7.2 明确要求 p≡1mod3，覆盖两目标类。这里只报告已读取的固定 v3；不推断其他版本的适用范围。

源码还有一个需要核对而非直接宣布论文错误的 sign 细节：TeX 396–405 从 exponent \(12/d\), \(d=\gcd(p-1,12)\) 的公式，以“\(\mathbf Q_p^\times/U_1\) 无 \(12/d\)-torsion”撤销幂。p≡19 mod24 时 d=6、指数2，但该群含 \(-1\) 的 2-torsion；该文字理由本身不能定 sign。N=3 §7.2 的 modular-unit exponent 是 \(24/d\)，目标 p13/p19 类分别为2/4；Appendix 另提 Fourier expansion computation，必须查其是否额外固定 sign。与 higher-curve cusp/pole normalization 一同留作 **N=3 extension/Fourier sign normalization 待核验 gate**；不因此改写历史 theorem/classification、不宣判论文错误或定理反驳。

## Gross–Koblitz/Jacobi 路线的地位

本次完整消费的两个前序 reports 与当前 report 只把 Gross–Koblitz/Jacobi/p-adic Gamma 列为未完成候选方向，没有提供一个可审核的固定 theorem/equation 来识别 \(g_p/p\)。这只是 scoped evidence gap，绝非“此类文献不存在”。

因此先用已有 N=3 来源判别上述 gate；若来源只有 norm，就把该接口保留为 structural antecedent，下一步只接收能证明 mod-p² finite-truncation comparison 的固定 Jacobi/GK 候选。最低候选卡须列出 character orders、base field F_p/F_p²、additive-character/Gauss normalization、p-adic Gamma arguments、p-uniformizer/embedding、valuation extraction、CM evaluation及 lift、有限截止与误差阶。仅 GK 把 Gauss sum 写成 Gamma product，不等于这份 carrier 已包含 \(G_p\)；零阶 finite-field trace 或 inert valuation 也不够。禁止为耗尽的共享 KQB standard 3/3 新建 turn 或换 provider 查询。

## 证据与权限

六份 Source full files 已通过 connector 在固定 enterprise-math@45e67a10aa39626e5711513726739e29c4c7e6d3 获取并逐字节重算 Git blob/SHA-256；详见 SOURCE_PINS.json / EXACT_CONNECTOR_READBACKS.json。当前 checkpoint 和 report 的 blob/SHA 与 Root/本轮 researcher 在 8d21 固定 intake 完全相同。外部 Betina TeX 复用本轮 researcher 已保存的全文；相关章节 excerpts 及全文 digest 见 EXTERNAL_SOURCE_EVIDENCE.json。不请求新 provider，不远端写入。

Native basis retains HEARTBEAT_WORLD X6; the modular-curve/scalar objects here are an explicitly external arithmetic carrier/readout and give no native spatial propagation bridge. Time is separately typed when relevant. This memo is directed/shared-context, not blind or independent formal review, and grants no Source mathematical Result, Working Truth, Foundation, canonical promotion, novelty or terminal-parent status.

