# R444｜signed BRC 奇数行 303—321 的全矩阵 PF3 精确整数证明

日期：2026-11-01。作者侧状态：AUTHOR_SIDE_EXACT_INTEGER_EXHAUSTION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。

## 定理与模型

固定十个奇数 r∈{303,305,307,309,311,313,315,317,319,321}。对于 2≤s≤r，定义原始 signed BRC 辅助标量

\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s}.
\]

令 b_h=H(r,r-h)，0≤h≤r−2；取正整数 g=gcd(b_0,\ldots,b_{r-2})，令 a_h=b_h/g，支持外 a_h=0。定义无限 Toeplitz T_{ij}=a_{j-i} (i,j≥0)，PF_k 指所有不超过 k 阶的子式非负。

**R444（作者侧计算机辅助精确定理）：对上述十个奇数 r，T∈PF3\PF4，因此最大 PF 阶数均为 3。**

结论仅涉及该 signed BRC 辅助标量序列，不自动构成心跳世界原生 X6 动力学的正性定理。

## 无限矩阵的有限完备归约

沿用 R441-A 的 Schur/Littlewood–Richardson 归约（源：enterprise-math@8fba98f1654ef4050ccc562be1ec197c01f31a47 的 R441_PROOF.zh-CN.md）。对正首项有限支撑 a_0,...,a_n，全部 Toeplitz k≤K 子式非负当且仅当对每个 m≤K，连续行 (0,...,m−1) 和严格递增列 0≤j_1<...<j_m≤n+m−1 的行列式非负。将 a_h/a_0 视为 e_h 的特化；任意行列子式是斜 Schur 特化，Littlewood–Richardson 非负整数展开将其归约为普通 Schur 特化，而后者正是连续行任意列子式。超出上述列界的连续行行列式含全零列。a_0>0 的整体缩放不改变符号。

在本模型 n=r−2，故各行需要的完备检查数为：
m=1: C(r−1,1)，m=2: C(r,2)，m=3: C(r+1,3)。
十行合计一阶 3,110，二阶 485,325，三阶 50,669,840；总计 **51,158,275** 个子式。

## 系数输入的两条整数公式

原始展开式：
\[
H_{\rm raw}(r,s)=\binom{r+s}{2s}\sum_{q=0}^{r-s}\binom{r-s}{q}
\left(\binom{2s}{r-2q}-\binom{2s}{r-2q-1}\right).
\]

奇数 r=2k+1 的 Catalan 式：
\[
H_{\rm Cat}(2k+1,s)=\binom{2k+1+s}{2s}
\sum_{q=0}^{\min(k,\lfloor(s-1)/2\rfloor)}
\binom{s-1}{2q}4^q C_{k-q},
\quad C_j=\binom{2j}{j}/(j+1).
\]

重用 R443_GENERATE.py，输入 303 321，对十行合计3,110个系数作任意精度整数逐项相等检查且均为正。生成原始输入文件 713891 字节，SHA256: 7a74f731ab10d73368d60ec8c3ddbaac645241fc480cc754c75715931109e223。正 gcd 归一化使 m 阶子式乘以 g^{-m}，符号保持不变。

## 完备整数证书

R444_PF3_INTEGER.cpp 缓存精确二阶量 D(x,y)=a_xa_{y-1}-a_ya_{x-1}，使用
\[
\det T_{(0,1,2),(x,y,z)}
=D(x,y)a_{z-2}-D(x,z)a_{y-2}+D(y,z)a_{x-2}
\]
对全部严格列组合使用 Boost cpp_int 精确整数运算，且逐行检查实际计数等于上述二项式数。程序分两次执行：303—311 共24,354,325个，313—321 共26,803,950个，全部严格正，没有零或负子式，均退出码0和 R444_PF3_EXACT_PASS。此证明的该部分未使用浮点判号。

另用独立 Python 六项 Leibniz 展开与缓存公式对照十行1,250个确定性抽样三阶子式，全部相等且为正。抽样用于程序交叉核验，完备性由 cpp_int 穷举和 Schur/LR 归约承担。

## 四阶否证

每行取行 (0,1,2,3) 与列 (r−3,r−2,r−1,r)。复用 R443_PF4_WITNESS.py，从原始卷积重新生成全部原系数并与归一化输入核对，再以 24 项 Leibniz 任意精度整数展开求行列式。十个归一化四阶行列式全都严格负；结果文本 SHA256: c410552e48409dc00af994182234cffcc49ffcd3c5380c128ca5781bf052c538。任一负子式即可否证 PF4。由 PF3 全域正性及 PF4 负证得到本定理。

## 复现、证据及边界

运行环境 Python 3、g++ 14.2.0、Boost cpp_int；见 R444_HANDOFF.md 的完整命令、精确输入及输出 SHA256。十行原始输入、完整分段日志和十个十进制负证同时保留在本轮本地研究证据包；GitHub 保存可再生的来源程序、精确计算程序、实际统计回执、摘要和下一步。

这是一项十个参数行的精确整数计算机辅助证明，并不推出所有奇数 r≥99 都满足 PF3。复用的是原始 signed BRC 标量观察，不将 signed/amplitude 列式视为正权 Weighted-BRC 的正分支质量。未修改 P000、ACTIVE 世界观或项目正式任务状态。

前沿：R441 的完整 Schur/LR 降阶证明，R442 的 r=99—201，R443 的 r=203—301；本轮扩展到 r=321。
下一问题：优先寻找对奇数 r≥99 的三阶 Schur 子式全参数正性证书；若无法建立，继续找 r≥323 中首次三阶负子式。研究精确 Catalan 比值和三阶子式分解，尽量避免继续逐行大量枚举。

输入控制快照：GLOBAL_KNOWLEDGE_V1 main@e018eb6a288f10f039d001422932728e5b58c584；Enterprise Math main@f8cc8141ca4c92b793ec694de7bfff9ad5e3bba6。当前 GitHub 身份 awdawmip。原生服务只读 em_status 显示 research_authority_granted=false，control quota 为 5/5，control.source_sync.state=CODE_REVIEW_REQUIRED；正式活跃 Owner/CLAIM 未被本轮权威确认。此 GitHub 持久化仅为作者侧科研材料保全，仍待 Research-Activity、独立 Driver 审核及正式 Source 接纳。
