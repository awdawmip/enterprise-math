# R425｜原始带符号 BRC 辅助组合 Turán 差的全参数符号分类

时间：2026-10-31；状态：AUTHOR_SIDE_SYNTHESIS / EDGE_CLOSED_FORMS_EXACT / DRIVER_UNREVIEWED / NOT_ADMITTED。P000 与 ACTIVE Heartbeat World 不修改；仅为 signed 十二支路 BRC 的**辅助组合标量读出**，不是原生 X6 动力学或物理测量。

## 定义、完整分类

对所有整数 r≥2、1≤s<r，令

\[
\delta_{r,q}=[t^r](1-t)(1+t)^{2q}(1+t^2)^{r-q},\quad
H_{r,q}=\binom{r+q}{2q}\delta_{r,q},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

**R425-A（作者侧、待独立审阅）**：全部合法参数上的 D 都不为零，且

\[
\boxed{D_{r,s}<0\ \Longleftrightarrow\
(s=1\land r\equiv0\pmod2)\ \lor\ (r,s)\in\{(3,2),(5,2)\}.}
\]

其余参数均严格 D>0。该命题合成已有 R404—R418、R424 作者侧证明并补足 s=1、2 的新解析边界公式；没有把有限样本归纳成全称命题。

## 新证明一：s=1 的无限奇偶分类，保留签名

原始 (1−t) 不能改成正权重；直接展开得到

\[
\delta_{2k,0}=\binom{2k}k>0,\qquad
\delta_{2k+1,0}=-\binom{2k+1}k<0.
\]

R404 精确 Catalan 核（可从原始系数的三角递推重建）给出
\[
\delta_{2k,1}=0,\quad \delta_{2k,2}=2\mathrm{Cat}_{k-1},
\quad\delta_{2k+1,1}=\delta_{2k+1,2}=\mathrm{Cat}_k;
\qquad\mathrm{Cat}_j=\binom{2j}j/(j+1).
\]

对全部整数 k≥1，直接代入 H 的二项系数：

\[
\boxed{D_{2k,1}=-2\binom{2k}k\binom{2k+2}4\mathrm{Cat}_{k-1}<0,}
\tag{1}
\]
\[
\boxed{D_{2k+1,1}=\mathrm{Cat}_{k}^{2}
\left[\binom{2k+2}2^{\!2}+(2k+1)\binom{2k+3}4\right]>0.}
\tag{2}
\]
式 (2) 中 \(\binom{2k+2}2^{\!2}\) 表示 \(\left(\binom{2k+2}{2}\right)^2\)。

## 新证明二：s=2 的两个、且仅两个负例

偶数 r=2k≥4 时 H_{r,1}=0，因此
\[
\boxed{D_{2k,2}=\left[2\binom{2k+2}{4}\mathrm{Cat}_{k-1}\right]^2>0.}
\tag{3}
\]

奇数 r=2k+1≥3，记 A=\(\binom{2k+3}4\)，B=\(\binom{2k+2}2\)，C=\(\binom{2k+4}6\)。
Catalan 核给 \(\delta_{2k+1,3}=\mathrm{Cat}_k+4\mathrm{Cat}_{k-1}\)，而
\[
\frac{\mathrm{Cat}_{k-1}}{\mathrm{Cat}_k}=\frac{k+1}{2(2k-1)},\qquad
\frac{BC}{A^2}=\frac{2(2k-1)(k+2)}{5k(2k+3)}.
\]
精确代入并通分，得
\[
\begin{aligned}
D_{2k+1,2}/\mathrm{Cat}_k^2
&=A^2-BC\left(1+4\frac{\mathrm{Cat}_{k-1}}{\mathrm{Cat}_k}\right)\\
&=\boxed{A^2\frac{2k^2-3k-4}{5k(2k+3)}}.
\end{aligned}\tag{4}
\]
所有分母为正；f(k)=2k²−3k−4 在 k=1,2 分别为 −5,−2，在 k=3 为 5，且 f(k+1)−f(k)=4k−1>0。故负例恰为
\[
\boxed{D_{3,2}=-5,\qquad D_{5,2}=-140.}
\]
所有其他合法 s=2 整数对 D>0。式 (1)—(4) 是无限整数域的严格闭式，不依赖网格样本外推。

## 已完成 s≥3 域的精确覆盖及原生边界

此前作者侧精确证书按 s 完全覆盖：
* s=3…5：R404（Catalan 有理式及严格正系数）。
* s=6…16：R407（22份奇偶完整整数多项式证书）。
* s=17…21：R408（10份证书）。
* s=22…30：R409—R417（逐 s 奇偶全系数证书）。
* s=31…49：R418（其定理覆盖 s=31…128）。
* s≥50：R424-A（保留带符号负半弧的傅里叶解析估计，对 m=r−s≥1 一律严格正）。

以上各覆盖源均命题为“所有整数 r≥s+1”，而非有限测试；各源均在 Draft PR #1708 研究目录，仍需独立数学复核。把新闭式与六段覆盖合并，证明 R425-A：负例、正例、非零性已无遗漏。R419—R423 的其它证书不是这条最短证明的依赖，不应冒称独立重复证明。

## 有条件 jet 推论和标量局部 log-concavity

如果 R403 原始十二支路签名传递恒等式
\[
[a^{4s}]T_{r+s}^{(r)}=180^{2r-2s}D_{r,s},
\quad \mathrm{ord}_{a=0}T_{r+s}^{(r)}\ge4s
\]
被独立确认，则 R425-A 的非零性证明**全部**合法 (r,s) 的 jet 退化阶数恰等于 4s，首项符号按上述负例表分类；此推论不自行证明 R403 的 K/J→B→D 对应。

对于每个 r≥4，正数 H_{r,2},…,H_{r,r} 的内部标量 Turán 差均严格正。但这不意味着整行 PF₂、原始 signed 支路的正质量、矩阵 TP₂、原生 X6 保真或物理定律。

## 本轮可复现精确验证和限制

同目录 R425_VERIFY.py（纯 Python 标准库）从原始带符号卷积独立计算 δ，和 Catalan 核比对；用整数/Fraction 核对边界闭式。奇数 r 的 s=2 恒等式在清分母后为次数至多11的整数多项式，核验12个互异整数 k=1…12 都是其根即给严格多项式恒等证书；这与有限参数预测无限正性不同。

实际执行命令（默认相同）：python R425_VERIFY.py --rmax 144 --raw-rmax 70 --edge-kmax 512 --out R425_EVIDENCE.json。输出：

R425_EXACT_PASS 12 2484 10296 74 2047

即多项式恒等式12点次数证书；2484次 signed 原始 δ 与 Catalan 核的精确同一性核验；r=2…144 全部10296个参数对的精确整数判号，其中74个负值；2047次边界闭式精确检查。网格仅为诊断，s≥3 无限参数域依赖上述已有完整证书及 R424 的解析证明，本轮没有独立重新生成那些全部证书。

## 来源、状态和下一问题

冻结：GLOBAL_KNOWLEDGE_V1 canonical main@bb5d22a791f3b28aa6998efcb53f4f1b9683a12a；Enterprise Math canonical main@75b88a101f96112098c70438babbf626a1940da8；研究 Draft PR #1708 原始 R424 head@94ae64f9f7351509b21cefe20fec98e9c935aa1b。GitHub 当前真实主体 awdawmip；原生 DIRECTED_RESEARCH authority_granted=false，活跃 Owner 控制查询 CONTROL_QUOTA。没有正式 CLAIM、Result、独立 Driver Review 或 mathematical admission。BRC REUSE_APPLIED：保留原始签名、原始分支/观察者语义，不把标量符号推论为原生 X6 或物理证据。P000 / ACTIVE worldview 不变。

下一问题：尝试在不依赖 R404—R418 逐带证书条件下，把 R424 的 Fourier 统一解析充分阈值 s≥50 降到 s≥3，并开展 R424 负半弧 Beta 上界及各 s 小带证书的**真正独立审阅**；原生 signed BRC→X6 的带有观察者和未来操作的保真桥应另立 typed 证明。
