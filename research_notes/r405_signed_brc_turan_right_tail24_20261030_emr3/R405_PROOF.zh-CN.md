# R405 — 带符号 BRC 的 24 条右边界 Turán 缺陷严格正性：全余阶整数多项式证书

2026-10-30 · Research3 作者侧精确研究。状态：AUTHOR_SIDE_COMPUTER_ASSISTED_PROOF / EXACT_INTEGER_REPLAY_PASS / DRIVER_UNREVIEWED / NOT_ADMITTED。

## 1. 固定模型、不可变来源

采用 R402–R404 的原始十二支路带符号 BRC K/J→B→D **辅助组合模型**，仅 K₃[t²]=−8(1+θ)，θ>−1，令 a=30−16θ。固定整数余阶 r，c_j^(r) 为有限 Newton 系数，T_j^(r)=(c_j^(r))²−c_(j−1)^(r)c_(j+1)^(r)。沿用

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

R403.1 给出在 R402 形式系数模型下的严格首项传递：
\[
[a^{4s}]T_{r+s}^{(r)}=180^{2r-2s}D_{r,s},
\qquad a^{4s}\mid T_{r+s}^{(r)}.
\]
R404 已证 s=3,4,5 全余阶的 D>0。本轮独立研究 **右边界 k=r−s 固定** 的全余阶问题；研究对象不含正质量替换、原生六维 X6 动力学及物理校准。

## 2. R405 主命题（有限个 k，全部无界 r）

**定理 R405-A（24 条无界右边界带）**：对全部整数
\[
1\le k\le24,\qquad r\ge k+3,\qquad s=r-k\ (\ge3),
\]
均有
\[
\boxed{D_{r,r-k}>0,\qquad
\operatorname{ord}_{a=0}T_{2r-k}^{(r)}=4(r-k).}
\]

特别地，结合 R404 s≤5，全部 r≤30、3≤s<r 都有 D_(r,s)>0；更重要的是每条 r−s=k≤24 都覆盖 **无限多个整数余阶 r**，不是仅对 r≤30 的数值扫描。现阶段剩余未覆盖的统一正性区域为 r≥31、s≥6、r−s≥25。

## 3. 第一重恒等式：Q_k 的封闭整数多项式

以 (z)_{\underline m}=z(z−1)···(z−m+1)，(z)_{\underline0}=1，Cat_r=binom(2r,r)/(r+1)。对任意整数 k≥0 定义整数系数多项式
\[
Q_k(r)=(r+1)\sum_{j=0}^{k-1}\binom{k}{j}(4j-2k+1)
(r)_{\underline{2j}}(r)_{\underline{2k-2j-1}}
+(2k+1)(r)_{\underline{2k}}.
\tag{R405.1}
\]
空和为零，因此 Q_0=1。

由有限二项式展开（超界项定义为零）有
\[
\delta_{r,r-k}=\sum_{j=0}^k\binom{k}{j}
\left[
\binom{2r-2k}{r-2j}-\binom{2r-2k}{r-2j-1}
\right].
\]
对泛变量 r 使用
\[
\frac{\binom{2r-2k}{r-2j}}{\mathrm{Cat}_r}
=(r+1)\frac{(r)_{\underline{2j}}(r)_{\underline{2k-2j}}}
{(2r)_{\underline{2k}}}
\]
和
\[
\binom Nm-\binom N{m-1}
=\binom Nm\frac{N-2m+1}{N-m+1}.
\]
分子 N−2m+1=4j−2k+1，分母 N−m+1=r−2k+2j+1。j<k 时后者恰是 (r)_(2k−2j) 中可约掉的一项；j=k 时与 Cat 分母所带 (r+1) 相消。可得到 **多项式恒等式**，在中间分式出现零分母的整数边界仍按消元后的多项式等式成立：
\[
\frac{\delta_{r,r-k}}{\mathrm{Cat}_r}
=\frac{Q_k(r)}{(2r)_{\underline{2k}}}.
\]
又 B_(r,r−k)=binom(2r−k,k)=(2r−k)_(k)/k!，从而
\[
\boxed{\frac{H_{r,r-k}}{\mathrm{Cat}_r}
=\frac{Q_k(r)}{k!(2r)_{\underline k}}.}
\tag{R405.2}
\]
适用的整数域为 0≤k<r；本轮取 r≥k+3，分母严格正。

## 4. 第二重恒等式：一个可核验的严格正系数证书

定义整数多项式
\[
N_k(r)=(k+1)(2r-k)Q_k(r)^2
-k(2r-k+1)Q_{k-1}(r)Q_{k+1}(r).
\tag{R405.3}
\]
将 (R405.2) 对连续 k−1,k,k+1 代入 D 的定义，约去阶乘与下降阶乘，有完全精确的有理恒等式：
\[
\boxed{\frac{D_{r,r-k}}{\mathrm{Cat}_r^2}
=\frac{N_k(r)}
{(k+1)(2r-k)(k!)^2((2r)_{\underline k})^2}.}
\tag{R405.4}
\]
当 r≥k+3 时，右侧分母以及 Cat_r 严格正。

因此只需证明 N_k(k+3+x)>0 (x≥0)。本轮以随包保存的纯 Python 标准库 **整数多项式运算**形成有限完整代数证书：
\[
\boxed{[x^j]N_k(k+3+x)>0\quad
(1\le k\le24,\ 0\le j\le4k+1).}
\tag{R405.5}
\]
程序直接构造 (R405.1)、(R405.3)，按 Horner 算法精确平移，并检查 **全部1248个** 严格正整数系数，任何失败将抛出断言。逐 k 的次数实际为 4k+1，最高系数实际为 2^(2k+1)。这不是枚举有限个 r，而是验证 24 个 **恒定阶数的多项式证书**；每一个都对无界 x≥0 同时成立。由 (R405.4) 推出全部 r≥k+3 的 D>0，由 R403.1 推出退化阶数恰为 4(r−k)。

便于人工检查的前两条：
\[
\frac{D_{r,r-1}}{\mathrm{Cat}_r^2}
=\frac{r^3-3r^2-2r+5}{2r-1},
\quad r\ge4,
\]
其分子令 r=4+x 得 x³+9x²+22x+13；
\[
\frac{D_{r,r-2}}{\mathrm{Cat}_r^2}
=\frac{r^6-9r^5+29r^4-11r^3-84r^2+104r+3}
{3(2r-1)^2},\quad r\ge5,
\]
其分子令 r=5+x 得 x⁶+21x⁵+179x⁴+819x³+2226x²+3564x+2673。其余22条的完整正系数证书由 r405_verify.py 生成，可按 SHA256 检验，**代码为数学证书的透明证明步骤，并非形式证明助手已接受的证明**。

## 5. 实际执行、覆盖、证据级别

在 2026-10-30 的本轮本地 Python 3 环境执行：

python r405_verify.py --max-k 24 --out R405_EVIDENCE.json

实际输出：R405_EXACT_PASS；k=1..24；正的整数多项式系数共1248项；221组独立整数值交叉核验。证据 JSON 83,413 字节，SHA256 9ce7e6f86a6779dc490cb51bf34803c959be2fe11dacc5b8d9e4b6877520f1a1；执行源码 5,265 字节，SHA256 612ee7f8e5ae6675feecb2a368b300aaa07c5c35490969d0513e5ffc0981ec72。独立复制目录再执行，原始 JSON **逐字节一致**；另用 SymPy 对 k=0..12 的原始二项式求和与 Q_k 代数比值完成独立符号消元核验。R402 / R403 模型到 Turán 首项的传递仍为明确的作者侧来源依赖，待独立审阅。

数学级别：R405.1–R405.4 为有限恒等式的人工代数推导；R405.5 为在实际运行的精确整数程序下完成的有限计算机辅助符号正系数证书；合起来支持所述无界 r 的定理（带原始 R402/403 依赖）。不是 Lean/Coq 形式审定、原生 Source Result 或独立 Driver 接纳。

## 6. 后继问题与接续

优先寻找能 **对全部 k≥1** 证明 N_k(k+3+x) 正系数的统一递推、正核或组合注入，从而在 r≥s+1、s≥3 全域证明 D>0；也可先在中间区域 r≥31、6≤s、r−s≥25 寻找严格零值/负值反例。不可把仅运行 k≤24 的证书提升为全部 k 的证明。

不可重复的前沿：R402 的 Catalan 最高系数与退化次序、R403 s=1/2 精确符号、R404 s=3..5 全余阶严格正。保留签名、分支、观察范围，未经 X6 嵌入/未来操作保真证明不将辅助有符号总量当作原生状态或正权 BRC。

读取快照：GLOBAL_KNOWLEDGE_V1 main@59588fa6f735b9ba38e586201e3fbbbad6e55cef；Enterprise Math main@34b736ab077ed0b4cef6dcd4d19157597bf0b1d8；作者侧 R404 PR HEAD@89cba1614fe75643ffb61e3e715169e2de103528。原生服务 0.6.11 当前 research_authority_granted=false，executor_binding_configured=false，控制端 CODE_REVIEW_REQUIRED、5/5 quota；没有本轮有效 Source Owner / CLAIM 的确认。研究产物仅是 GitHub 上的作者侧未审材料；P000 与 ACTIVE 世界观保持原样。
