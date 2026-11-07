# R442｜signed BRC 奇数行 r=99—201 的最大 PF 阶数恰为 3

日期：2026-11-01。性质：AUTHOR_SIDE_EXACT_INTEGER_EXHAUSTION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。所研究的是带符号 BRC 的辅助标量有限序列，不是 X6 原生空间的动力学定理。P000 与 ACTIVE 世界观未修改。

## 1. 问题与严格结论

沿用 R441 的原始 signed BRC 系数，令奇整数 r≥5、2≤s≤r，

$$
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\qquad
a_h=H(r,r-h)\quad (0\le h\le n=r-2),
$$

并令支持外 a_h=0。半无限 Toeplitz 矩阵 T^(r) 的元素为 T_{ij}=a_{j-i}，i,j≥0。PF_m 表示所有不超过 m 阶的子式非负。

**R442 定理（作者侧完整整数计算机辅助证书）：**

$$
\boxed{\forall r\in\{99,101,103,\ldots,201\},\quad
T^{(r)}\in{\rm PF}_3\setminus{\rm PF}_4.}
$$

由此，52 个指定奇数行的最大 PF 阶数均为 3。量词只覆盖这 52 行；不声称全部奇数 r≥99 的 PF3 性质已证明，也不将数值测试扩展为无限参数定理。

## 2. 半无限 PF3 判定为何可完全有限化

复用 R441-A 的 Schur–Littlewood–Richardson 引理。给定 a_0>0、有限支持 0≤h≤n，检查半无限 T 的全部 ≤K 阶子式，等价于对每个 1≤m≤K 检查连续行 I=(0,1,...,m-1) 与任意严格增列组合

$$
0\le j_1<j_2<\cdots<j_m\le n+m-1
$$

形成的每一个子式。因此有限数量为

$$
N_K(n)=\sum_{m=1}^{K}\binom{n+m}{m}.
$$

简证：将 b_h=a_h/a_0 视为对称函数环上 e_h↦b_h 的特化。一般行列索引逐位不满足 j_t≥i_t 时，矩阵的三角支撑迫使子式为 0。否则由对偶斜 Jacobi–Trudi，该子式是一个斜 Schur 特化；Littlewood–Richardson 展开把它写成非负整数线性组合的普通 Schur 特化。其出现的普通形状宽度 ≤m，正对应上述连续行、任意列的候选子式。候选均非负即保证一般子式非负；反向由候选本身也是子式得到。这个通用引理继承 R441 的证明，非本轮新独创结论。

本轮 n=r−2，故对每个指定 r，仅检查 m=1,2,3 且列末端 ≤r−3+m 的组合即可。所有矩阵外部结构性零与其他行组合由上述引理覆盖，不是被忽略的有限窗口。

## 3. 两套独立的精确输入公式

一套直接从 signed 卷积展开计算：

$$
H_{\rm raw}(r,s)=\binom{r+s}{2s}
\sum_{q=0}^{r-s}\binom{r-s}{q}
\left[\binom{2s}{r-2q}-\binom{2s}{r-2q-1}\right].
$$

另一套使用 R441 的奇数行 Catalan 核（r=2k+1）：

$$
H_{\rm Cat}(2k+1,s)=\binom{2k+1+s}{2s}
\sum_{q=0}^{\min(k,\lfloor(s-1)/2\rfloor)}
\binom{s-1}{2q}4^q C_{k-q},
\quad C_j=\frac{\binom{2j}{j}}{j+1}.
$$

R442_GENERATE.py 对全部 52 行的每一个系数进行两式逐整数核对，累计 7,748 条等式，全都成立。全部系数严格正。每行除以该行正整数最大公约数 g，仅降低整数位数，不改变任何子式符号；输入总共 874,872 字节，SHA256：

d620ffe68c8b0cd6b5eaced24a701e6cbd5dca0f165d6ac303d1d0a6a31e93c5

独立 R442_VERIFY_RAW_AND_PF4.py 又直接从原始 signed 卷积重新检查 7,748 个系数与归一化结果，全部相符。没有用浮点数生成系数或判定矩阵符号。

## 4. 一至三阶完备穷尽的实际结果

实际执行 R442_INTEGER_EXHAUST.cpp，使用 Boost multiprecision cpp_int 保存任意精度整数，三阶子式以完整的六项整数公式计算，不使用浮点判号：

$$
\det\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix}
=a(ei-fh)-b(di-fg)+c(dh-eg).
$$

每个 r、每个 m，程序枚举所有合法列索引，不抽样，不允许把负数或零数计为正。执行结果如下：

| 阶数 | 候选数总计 | 严格正 | 零 | 负 |
|---|---:|---:|---:|---:|
| 1 | 7,748 | 7,748 | 0 | 0 |
| 2 | 604,526 | 604,526 | 0 | 0 |
| 3 | 32,762,600 | 32,762,600 | 0 | 0 |
| 合计 | **33,374,874** | **33,374,874** | **0** | **0** |

对 r=99：一、二、三阶分别为 98、4,851、161,700 个。对 r=201：分别为 200、20,100、1,353,400 个。完整 52×3 行机器输出在 R442_INTEGER_FULL_STDOUT.txt；其逐字节 SHA256 为：

bdec4be26959c10ae59e44d767f0ff827fc406a1b8dd575dcfd8d0e6983f6104

该程序本轮在本地完成全部 52 行，标准输出末行为 R442_INTEGER_EXHAUST_DONE rows=52 total=33374874。不存在依赖精度阈值、IEEE 舍入或未经执行的精确回退。程序正确性仍属于作者侧可审计的计算机辅助证明，未取得独立审阅。

## 5. 每行独立的四阶整数负证

对每个指定 r，取 Toeplitz 行索引 (0,1,2,3)，列索引 (r−3,r−2,r−1,r)，定义

$$
D_r^{(4)}=\det[a_{r-3+j-i}]_{0\le i,j\le3}.
$$

R442_VERIFY_RAW_AND_PF4.py 在上述经过完整 signed 原始卷积回核的归一化整数系数上，按独立的 24 项 Leibniz 整数展开分别计算 52 个 D_r^(4)，结果每一项都严格小于零。绝非仅从 R432 无限参数结果口头继承。第 99 行负行列式绝对值 431 bit，第 201 行 886 bit。

完整每行的十进制负行列式与对应行列索引在 R442_PF4_NEGATIVE_WITNESSES.txt；该文件 SHA256 为：

502732b4b9c4103566e5c9210d68811b6320d4ead3aa36a0a7e1bb414feee503

故每一行不是 PF4。与第 4 节完成的全半无限 PF3 认证合并，证得 R442 定理。

## 6. 可移植复现、来源及限制

在同一目录保存本轮四份源码/证据文本后，使用 Python 3 与 g++/Boost headers：

1. python3 R442_GENERATE.py ；得到 R442_INPUTS.txt，应核对输入 SHA256。
2. g++ -O3 -std=c++17 R442_INTEGER_EXHAUST.cpp -o r442_integer
3. ./r442_integer R442_INPUTS.txt 99 201 > R442_INTEGER_FULL_STDOUT.txt ；比较发布的输出或其 SHA256。
4. python3 R442_VERIFY_RAW_AND_PF4.py ；重新产生负证文件与独立 signed 系数核验。
5. R442_EVIDENCE.json 给出计数、精确来源、实际 SHA256 和明确的结论范围。

继承并复用 R441 Schur/LR 完备归约（PR #1708 先前提交 8fba98f1654ef4050ccc562be1ec197c01f31a47）；不是重新宣称独立发明 Littlewood–Richardson 定理。国际文献背景可参见 Rietsch, “Totally Positive Toeplitz Matrices: Classical and Modern”, ICM 2026 Proceedings, DOI: 10.1137/25M1806727；它不直接证明本辅助 signed BRC 家族的定理。涉及分支有符号幅值的标量观察不得误当作正加权 BRC 质量，更不构成原生 X6 中三维切片、联合关系和时间更新的保真桥。

本轮固定规范读取 GLOBAL_KNOWLEDGE_V1 main@8f0185bfd4c5db854f3da9795ba8e9de3f2fd382；Enterprise Math main@9412897fb2b8e77bb30ee26391fb65edaba2a8fd。原生上下文 authority_granted=false，active owner 查询 CONTROL_QUOTA；session_start 返回 STATIC_READONLY_SCOPE_DENIED，operation_sent=false。本轮仅作者侧独立推导、精确计算及中立研究物料保存；正式 Owner、CLAIM、Result、独立 Driver review 与数学接纳均未取得。

下一精确问题：对所有奇数 r≥203，能否证明全部连续行、任意列三阶普通 Schur 子式非负？或给出最早一个精确负证。应寻找随 r 变化的统一代数符号证书，不能把本轮 52 行或任何离散抽样自动当作无限参数证明。
