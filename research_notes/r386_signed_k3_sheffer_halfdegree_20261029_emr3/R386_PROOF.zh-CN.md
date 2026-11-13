# R386｜带符号 BRC 全余阶 Sheffer 型分解与退化点半次数精确定理

研究日期：2026-10-29。作者侧完整代数推导，尚待独立 Driver 数学审查。来源：R346 的原始十二支路带符号 K/J→B→D 递推；R384 全余阶首项及 R385 次高项同一模型。本文证明的是**辅助组合模型中的多项式恒等式**，不宣称原生 X6 动力学、全 D 阵列 TP₂ 或实际物理校准。

## 1. 原始模型及类型

令 \(\theta>-1\)，以形式变量 \(x,t\) 表示支路索引与原始次数。原始带符号核 \(K_1(t),\ldots,K_{12}(t)\) 完整保留，唯一变形为 \([t^2]K_3(t)=-8(1+\theta)\)（原项为 \(-8\)）；源 \(J_s(t)\) 不变，\(B_0(t)=1+t\)，\(B_s(t)=J_s(t)+\sum_{i=1}^{\min(12,s)}K_i(t)B_{s-i}(t)\)。

置 \(U_\theta(x,t)=\sum_{s\ge0}B_s(t)x^s=A_\theta(x,t)/(1-K_\theta(x,t))\)，其中 \(K_\theta(x,t)=\sum_{i=1}^{12}x^iK_i(t)\)，\(A_\theta(x,t)=1+t+\sum_{s\ge1}x^sJ_s(t)\)。按原始源和核直接检查：

\[
 K_\theta(x,0)=2x,\quad A_\theta(x,0)=1,\quad
 \deg_x[t^q]A_\theta\le q,\quad \deg_x[t^q]K_\theta\le q+1\;(q\ge1).
\]

所有系数在 \(\mathbb Q[\theta]\) 中；负号、支路来源及其指数均保留。本模型的 \(x\) 是形式支路计数变量，绝非 X6 坐标或空间轴。

令 \(b_{s,q}=[x^st^q]U\)，并定义

\[
 D_{q,u}=\sum_{w=0}^{u}(-1)^{u-w}\binom uw2^{q-w}b_{q+w,q},\qquad
 H_r(u;\theta)=5^{-u}D_{r+u,u}\quad(u\in\mathbb Z_{\ge0}).
\]

依据下面的形式生成函数，\(H_r(u)\) 对整值 \(u\) 的观测有唯一的次数不超过 \(r\) 的多项式延拓。继续沿用此前定义

\[
 L_r(v)=5^rH_r(v),\qquad Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1),\qquad
 c_j^{(r)}=\Delta^jQ_r(0),
\]

其中 \(r\ge1\)，\(\Delta f(v)=f(v+1)-f(v)\)，\(0\le j\le2r\)。这里的 \(PF_2\) 指有限 Newton 系数序列的非负与普通相邻 Turán 条件，不与其他 BRC 载体混淆。

## 2. 主定理：所有余阶共用同一对形式级数

在 \(\mathbb Q[\theta][[s]]\) 中设

\[
 G_\theta(x,s)=1-K_\theta\!\left(x,\frac{2s}{x}\right).
\]

由于 \(G_\theta(1/2,0)=0\)，\(\partial_xG_\theta(1/2,0)=-2\)，形式隐函数定理给出唯一 \(X_\theta(s)\) 满足 \(X_\theta(0)=1/2\)、\(G_\theta(X_\theta(s),s)=0\)。定义

\[
 \boxed{\mathcal A_\theta(s)=-\frac{A_\theta(X_\theta(s),2s/X_\theta(s))}{X_\theta(s)\,\partial_xG_\theta(X_\theta(s),s)}},\qquad
 \boxed{\mathcal B_\theta(s)=\frac{1-2X_\theta(s)}{10sX_\theta(s)}}.
\]

**定理 A（全余阶分解）**：对任何实数 \(\theta>-1\) 和任意非负整数 \(u\)，形式幂级数恒等式成立：

\[
 \boxed{\sum_{r\ge0}H_r(u;\theta)s^r=\mathcal A_\theta(s)\,\mathcal B_\theta(s)^u},\quad
 \mathcal A_\theta(0)=\mathcal B_\theta(0)=1.
\]

它在 \(\mathbb Q[\theta,u][[s]]\) 中作为多项式恒等式同样成立。特别地，令 \(p_r(u)=r!H_r(u)\)：若 \(\theta\ne15/8\)，那么 \(p_r\) 是经典非退化 Sheffer 序列，因为 \(\sum_r p_r(u)s^r/r!=\mathcal A_\theta(s)\exp\bigl(u\log\mathcal B_\theta(s)\bigr)\) 且 \([s]\log\mathcal B_\theta=(30-16\theta)/5\ne0\)。在 \(\theta=15/8\) 时指数级数的一阶项为零，故应称为 **退化 Sheffer 型分解**，不能误称为满足经典 delta-operator 非退化条件的 Sheffer 序列。

### 定理 A 的形式留数证明

记 \(U_q(x)=[t^q]U_\theta(x,t)\)。由上面的 \(A,K\) 次数界和 \(U=A+KU\)，按 \(q\) 归纳可得

\[
 U_q(x)=\frac{P_q(x)}{(1-2x)^{q+1}},\qquad \deg P_q\le2q.
\]

基步 \(U_0=(1-2x)^{-1}\)。归纳步用 \((1-2x)U_q=A_q+\sum_{h=1}^qK_hU_{q-h}\)，通分到 \((1-2x)^{q+1}\)；\(A_q(1-2x)^q\) 的次数不超过 \(2q\)，每项 \(K_hP_{q-h}(1-2x)^{h-1}\) 的次数也不超过 \((h+1)+2(q-h)+(h-1)=2q\)。

将二项式和转为一个系数抽取，得到精确恒等式

\[
 D_{q,u}=2^{q-u}[x^{q+u}](1-2x)^uU_q(x).
\]

当 \(q<u\)，因 \((1-2x)^uU_q=P_q(1-2x)^{u-q-1}\) 的次数不超过 \(q+u-1\)，右侧为零。对于任何 \(q,u\ge0\)，有理微分

\[
 x^{-q-u-1}(1-2x)^uU_q(x)\,dx
\]

在无穷远处为 \(O(x^{-2})dx\)，有限极点只有 \(x=0\) 和 \(x=1/2\)。故关于 \(x=0\) 的系数抽取等于 \(x=1/2\) 留数的相反数。逐阶在 \(s\) 中求和，得到

\[
 \begin{aligned}
 \sum_{r\ge0}H_r(u)s^r
 &=(10s)^{-u}\sum_{q\ge0}(2s)^q[x^{q+u}](1-2x)^uU_q(x)\\
 & =-(10s)^{-u}\operatorname*{Res}_{x=1/2}\!\left[\frac{(1-2x)^u}{x^{u+1}}\frac{A_\theta(x,2s/x)}{G_\theta(x,s)}\,dx\right].
 \end{aligned}
\]

形式根 \(X_\theta(s)=1/2+O(s)\) 是 \(G\) 在 \(1/2\) 附近的唯一简单零点。用 \((x-X(s))^{-1}=\sum_{j\ge0}(X(s)-1/2)^j/(x-1/2)^{j+1}\) 作 \(s\)-进展开，留数等于在移动简单根处的留数；由此得到

\[
 -\frac{A_\theta(X,2s/X)}{X\partial_xG_\theta(X,s)}
 \left(\frac{1-2X}{10sX}\right)^u
 =\mathcal A_\theta(s)\mathcal B_\theta(s)^u.
\]

原始一阶核给出 \(\partial_sG_\theta(1/2,0)=-5\)，从而 \(X_\theta'(0)=-5/2\)，保证 \(\mathcal B_\theta(0)=1\)；\(A(1/2,0)=1\) 保证 \(\mathcal A_\theta(0)=1\)。由于 \(\mathcal B=1+O(s)\)，每个 \([s^r]\mathcal A\mathcal B^u\) 是次数至多 \(r\) 的 \(u\) 多项式，因整数点无限多而给出唯一延拓，证毕。

## 3. 退化点的完全次数定理和 Newton 最高存留项

从原始 K/J 的前四层（或按定理 A 展开）得到：

\[
 \mathcal A_\theta(s)=1+6s+32s^2+(160-64\theta)s^3+O(s^4),
\]

\[
 \mathcal B_\theta(s)=1+\frac{30-16\theta}{5}s+\frac{216-96\theta}{5}s^2+\frac{1808-832\theta}{5}s^3+O(s^4).
\]

因此在唯一退化参数 \(\theta_*=15/8\) 处：

\[
 \mathcal B_*(s)=1+\frac{36}{5}s^2+\frac{248}{5}s^3+O(s^4),\qquad
 \mathcal A_*(s)=1+6s+32s^2+40s^3+O(s^4).
\]

**定理 B（全余阶精确半次数）**：对每个整数 \(r\ge0\)，

\[
 \boxed{\deg_u H_r(u;15/8)=\lfloor r/2\rfloor}. 
\]

证明：写 \(S(s)=\mathcal B_*(s)-1=b_2s^2+b_3s^3+O(s^4)\)，其中 \(b_2=36/5>0,b_3=248/5>0\)。\(\mathcal B_*^u=\sum_{k\ge0}\binom uk S^k\) 严格显示 \([s^r]\mathcal A_*\mathcal B_*^u\) 的 \(u\) 次数不超过 \(\lfloor r/2\rfloor\)。若 \(r=2k\)，其 \(u^k\) 系数为 \(b_2^k/k!\ne0\)；若 \(r=2k+1\) 且 \(k\ge1\)，系数为 \((k b_2^{k-1}b_3+6b_2^k)/k!>0\)。\(r=0,1\) 分别由 \(H_0=1,H_1(u;15/8)=6\) 处理。故次数等号对所有 \(r\) 成立。

**定理 C（全余阶 Q 次数与尾部系数闭式）**：对所有整数 \(r\ge1\)，

\[
 \boxed{\deg_v Q_r(v;15/8)=r},\qquad
 \boxed{c_r^{(r)}(15/8)=(-1)^r\binom{r}{\lfloor r/2\rfloor}180^r},\qquad
 \boxed{c_j^{(r)}(15/8)=0\ \ (r<j\le2r)}.
\]

证明：若 \(r=2k\)（\(k\ge1\)），\(L_r(v+1)L_r(v+2)\) 次数为 \(2k\)，另一乘积次数至多 \(2k-1\)，最高系数为 \(5^{2r}b_2^{2k}/(k!)^2\)；若 \(r=2k+1\)，后一乘积次数为 \(r\)，前一乘积次数为 \(r-1\)，最高系数为 \(-5^{2r}b_2^r/(k!(k+1)!)\)。由于 \(5^2 b_2=180\)，再用 \(\Delta^r Q_r(0)=r![v^r]Q_r(v)\)，得到所列闭式。\(\deg Q_r=r\) 同时推出所有更高有限差分为零。

**直接推论（无限奇数余阶精确 PF₂ 反例族）**：当 \(\theta=15/8\) 且 \(r\) 为任意正奇数，\(c_r^{(r)}<0\)。所以相应的有限 Newton 序列不能为非负序列，因而不属于 \(PF_2\)。这是同一辅助模型中的**无限参数化反例族**；对偶数余阶是否也普遍失去 PF₂，需要其它系数或 Turán 缺陷的统一证据。

## 4. 精确复现证据与范围

`R386_verify.py` 导入与 R384 同版的原始保号递推 `R384_verify.py`，没有重用已经构造好的 \(H_r\) 系数表作为预言。以 \(\theta=-1/2,0,1/2,1,15/8\) 五个精确有理参数，\(0\le r\le16\)、\(u=2,3,4,5\) 完成 **340 项**独立于拟合输入 \(u=0,1\) 的精确等式核对。另对 \(\theta=15/8,1\le r\le16\) 完成64项次数、闭式最高 Newton 系数及尾部为零的断言。全部使用整数和 `fractions.Fraction`，实际运行回执 `R386_EXACT_PASS`。`R386_EVIDENCE.json` 收录逐阶观测；`R386_SUMMARY.json` 收录核验范围及证据文件 SHA256。

无限量词的依据是第2—3节的形式留数证明，不是这340+64项有限测试。数值检查的覆盖与原生动力学对应均受本节所声明的边界约束。本文保留原始带符号支路身份，未将有符号模型误替换为正权 BRC 载体。

复现方式：在 R384 原始 `R384_verify.py` 同目录或本研究包中运行 `python R386_verify.py`，输出 `R386_EXACT_PASS` 并生成证据。GitHub 研究目录中若 R384 代码位于兄弟路径，脚本自动使用兄弟目录源。

## 5. 现有知识、来源与下一问题

源代码及模型前沿：R384 `research_notes/r384_universal_signed_k3_catalan_top_20261029_emr3/R384_verify.py`；R385 不可变研究提交 `46090af49a7bad8389fb387af8d18f4fd6b0ff80`，原有全余阶次高系数定理。经典 Sheffer 序列的生成函数定义可参见 Roman (1984) *The Umbral Calculus* 与 Wolfram MathWorld `https://mathworld.wolfram.com/UmbralCalculus.html`；这里的源模型、\(\mathcal A,\mathcal B\) 以及退化点定理均由本项目原始递推推导，不依赖外部文献作为证明前提。

下一项最小数学问题：利用同一 \(\mathcal A_*,\mathcal B_*\) 提取 \(Q_{2k}\) 的次高项及 Newton \(c_{2k-1}^{(2k)}\) 的闭式，判断能否对 **所有偶数余阶** 在 \(\theta=15/8\) 给出统一的负系数或负 Turán 缺陷证书，进而完成该退化点对所有 \(r\ge1\) 的 PF₂ 排除。单独问题：研究一般 \(\theta\) 下 \(\log\mathcal B_\theta\) 的代数方程及与 R384/R385 的全余阶顶端系数关系。

**权限与接纳状态：**本轮为作者侧便携研究 `AUTHOR_SIDE_PROOF / EXACT_FINITE_AUDIT / DRIVER_UNREVIEWED / NOT_ADMITTED`，尚需独立 Driver 审核及原生 Source 接纳。无现行 CLAIM、真实研究 Source owner 的权威确认或 X6 动力学接口验证。GLOBAL_KNOWLEDGE_V1 固定读取 `main@314ff1ecb8d348f87f9d97f51570d65256705595`，Enterprise Math 规范固定读取 `main@b519a46c64db7b40581b618e67a3467cc40a542f`；P000 及 ACTIVE 世界观保持原文未变。
