# R417｜带符号 BRC 辅助组合模型 s=30 的无界余阶 Turán 正性

日期：2026-10-31（Asia/Shanghai）。作者侧计算机辅助精确代数结果；独立 Driver 审查和数学接纳尚待完成。

## 1. 定理

沿用 R416 原始十二支路带符号 BRC **辅助组合模型**：

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

**R417：对每个整数 r≥31，有 D_(r,30)>0。** 本命题属于严格定义的辅助组合观察量，不据此认定原生 X6 动力学或物理残差。

复用 R416-B 已给出独立解析证明的精确 Catalan 核：

\[
\delta_{r,q}=
\sum_{\substack{0\le j<q\\r-q+j\text{ even}}}
\binom{q-1}{j}2^{q-1-j}\operatorname{Cat}_{(r-q+j)/2},\quad
\operatorname{Cat}_n=\frac{\binom{2n}{n}}{n+1}.
\]

这可从原始提取式、三角递推
\(\delta_{r,q+1}=\delta_{r,q}+2\delta_{r-1,q}\) 与对角 \(\delta_{r,r}=\operatorname{Cat}_r\) 推出（详情见 R416 证明）。核正性只是该有符号辅助对象的精确恒等改写，不能抹除原生 BRC 支路身份或证明原生保真。

## 2. 正系数证书：完整代数推导

固定 s=30，令 r=2m+ε、ε∈{0,1}；b=m−1+ε，C=Cat_b。偶族取 m=16+x、r=32+2x；奇族取 m=15+x、r=31+2x；x 为任意非负整数。

对 q∈{29,30,31}，用恒等式

\[
\frac{\operatorname{Cat}_{b-d}}{\operatorname{Cat}_{b}}
=\prod_{a=0}^{d-1}\frac{b-a+1}{2(2(b-a)-1)},\qquad
d=(q-j-2+\epsilon)/2\in\mathbb Z_{\ge0}
\]

逐项表示 \(\Delta_{q,\epsilon}=\delta_{r,q}/C\)。
三个 q 中 d 的最大值分别为 d₀=14、d₁=15。定义

\[
T_\epsilon=\prod_{a=0}^{d_\epsilon-1}2(2(b-a)-1),\quad
N_{q,\epsilon}=T_\epsilon\Delta_{q,\epsilon}\in\mathbb Z[x].
\]

T、N 的次数均不超过 dε，且 x≥0 时 T(x)>0。组合权重比率恰为

\[
\lambda=
\frac{\binom{r+s-1}{2s-2}\binom{r+s+1}{2s+2}}{\binom{r+s}{2s}^2}
=\frac{L_n}{L_d},
\]
\[
L_n=2s(2s-1)(r+s+1)(r-s),\quad
L_d=(2s+2)(2s+1)(r+s)(r-s+1).
\]

故有对**全部合法 x**成立的代数恒等式

\[
\frac{D_{r,s}}{[\binom{r+s}{2s}C]^2}
=\Delta_{s,\epsilon}^2-\lambda\Delta_{s-1,\epsilon}\Delta_{s+1,\epsilon}
=\frac{A_\epsilon(x)}{B_\epsilon(x)},
\]
\[
A_\epsilon=L_dN_{s,\epsilon}^2-L_nN_{s-1,\epsilon}N_{s+1,\epsilon},
\qquad B_\epsilon=L_dT_\epsilon^2.
\]

A、B 是整数系数多项式，次数至多 2+2dε，且 B(x)>0。纯标准库代码 r417_raw_integer_certificate.py 按上述乘加式在 Z[x] 中精确生成全部系数；机器 JSON R417_RAW_EVIDENCE.json 给出所有**升幂系数**。

| 族 | r 参数化 | deg A=deg B | A 正系数 | B 正系数 | min A 系数 | min B 系数 |
|---|---|---:|---:|---:|---:|---:|
| 偶 | 32+2x | 30 | 31 | 31 | 20104573436246852577670081786740211712 | 1090087282605773815808 |
| 奇 | 31+2x | 32 | 33 | 33 | 80418293744987410310680327146960846848 | 17441396521692381052928 |

**64个 A 系数和64个 B 系数全部为严格正整数。** 于是每个 x≥0 都有 A(x)>0、B(x)>0，且 \(\binom{r+s}{2s}C>0\)，从而 D_(r,30)>0。逻辑上，这是代数恒等式和完整正系数证书给出的无界结论，不是有限数值采样外推。

## 3. 本次实际运行与可重复证据

Python 3.13.5 本地实际执行的纯标准库生成器回执：

    R417_RAW_STDLIB_PASS 2 64 64 64
    PARITY 0 degrees 30 30 min 20104573436246852577670081786740211712 1090087282605773815808
    PARITY 1 degrees 32 32 min 80418293744987410310680327146960846848 17441396521692381052928

独立标准库程序 r417_independent_raw_degree_check.py 不导入上述生成程序，从原始带符号二项式提取式和 Catalan 核独立求和，复核64个整数参数和192个核恒等式，回执：

    R417_RAW_INDEPENDENT_PARITY_PASS 0 31 points
    R417_RAW_INDEPENDENT_PARITY_PASS 1 33 points
    R417_RAW_INDEPENDENT_PASS 64 Turan 192 Catalan

另外，以 SymPy 1.14.0 求得独立有理约分证书的 61+61 个严格正分子、分母系数；标准库次数界验证通过123项原始整数 Turán 等式、369项 Catalan 核等式。这些是额外交叉核验，**本目录的核心证明只依赖可重建的 A/B 原始系数证书**。

边界确值：
- D_(31,30)=93118580224214573400758455109526871>0。
- D_(32,30)=207652871133293192442475520786915770404>0。

R417_RAW_EVIDENCE.json 共8635字节，SHA256 为 63b2a37818cbbe18e2f3ded2be730039e3b3a2f7e0407a77c69b5555df8a7f15。全部计算使用整数或有理符号运算，无浮点近似判号。该成果为作者侧精确计算机辅助证明，尚须独立审阅。

## 4. 实际身份、来源与下一问题

GitHub 当前连接账号为 awdawmip。原生 Enterprise Math 服务的 session_start 返回 STATIC_READONLY_SCOPE_DENIED、operation_sent=false；control_tasks 返回 CONTROL_QUOTA；directed context 的 authority_granted=false。正式活跃 Owner、CLAIM、Result、独立 Driver Review 和数学接纳仍需原生确认；GitHub PR 是本次作者侧持久研究材料，并非原生状态机准入。

本轮冻结：GLOBAL_KNOWLEDGE_V1 canonical main@5f186ae245bfa4246d95f8ef86f1731a4301da36；Enterprise Math main@41073b8b6fb4eea5b87a85648eacfd9311b2667b；上游 R416 PR head@ef63b51c4ab36d6180634c99fdb6410090edad6a。复用 R416 Catalan 核、R414 递推及 R415 带权关系（REUSE_APPLIED）；P000 与 ACTIVE 世界观未修改。

结合此前作者侧、尚未接纳的无界带和右边界证书，尚未被全无界定理覆盖的区域为 **s≥31、r−s≥129**，第一个候选 (r,s)=(160,31)。

下一研究单元：证明或否定固定 s=31 时全部 r≥32 的 D_(r,31)>0；并尝试以 Catalan 核与带权 H 递推建立统一双参数正性不变式，减少按固定 s 逐带计算的依赖。原始有符号支路与 X6 观察者之间的保真桥仍是单独证明义务。
