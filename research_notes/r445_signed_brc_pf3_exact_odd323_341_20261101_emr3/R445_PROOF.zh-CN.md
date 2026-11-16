# R445｜signed BRC 奇数行 323—341 的全矩阵 PF₃ 精确整数证明

日期：2026-11-01。作者侧状态：\`AUTHOR_SIDE_EXACT_INTEGER_EXHAUSTION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING\`。

## 定理

对于十个奇数 \(r\in\{323,325,327,329,331,333,335,337,339,341\}\)，定义原始带符号 BRC 辅助标量整数

\[
H_{r,s}=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad 2\le s\le r.
\]

记 \(b_h=H_{r,r-h}\;(0\le h\le r-2)\)、\(g_r=\gcd(b_0,\ldots,b_{r-2})>0\)，令 \(a_h=b_h/g_r\)，支持范围外取零。对于半无限 Toeplitz 矩阵 \(T^{(r)}_{ij}=a_{j-i}\;(i,j\ge0)\)，本轮作者侧计算机辅助精确定理为：

\[
\boxed{\text{对于上述全部十个 }r,\ T^{(r)}\in PF_3\setminus PF_4.}
\]

该命题对每一个列出的参数完整覆盖**整个半无限矩阵**，但不宣称已证明所有奇数 \(r\ge99\) 的统一 PF₃ 定理。

## 无限子式的完备归约

复用 R441-A 的经典 Schur–Littlewood–Richardson 归约：对首项正、非负且支持在 \(0,\ldots,n\) 的序列，Toeplitz PF₃ 等价于所有连续行 \((0,\ldots,m-1)\) 和严格递增列 \(0\le j_1<\cdots<j_m\le n+m-1\)、\(m\in\{1,2,3\}\) 的子式非负。证明使用斜对偶 Jacobi–Trudi 行列式展开和非负整数 Littlewood–Richardson 系数；详细通用证明保存在 R441 commit \`8fba98f1654ef4050ccc562be1ec197c01f31a47\`。R441 将其应用到该辅助标量模型，此处仅复用，不声称通用归约为新发现。

本轮 \(n=r-2\)。各 \(r\) 的完备检查数为
\[
N_1(r)=r-1,\qquad N_2(r)=\binom r2,\qquad N_3(r)=\binom{r+1}3.
\]
十行完整验证一阶 **3,310** 个、二阶 **549,625** 个、三阶 **61,044,840** 个，合计 **61,597,775** 个非结构零候选，**均严格为正**。支持外的其他矩阵子式只能是结构零，故全矩阵满足 PF₃。

## 输入与算术的独立检查

原始 signed 卷积系数用
\[
H_{\rm raw}(r,s)=\binom{r+s}{2s}\sum_{q=0}^{r-s}\binom{r-s}{q}
\left(\binom{2s}{r-2q}-\binom{2s}{r-2q-1}\right)
\]
构造，并与奇数 \(r=2k+1\) 的 Catalan 展开
\[
H_{\rm Cat}(2k+1,s)=\binom{r+s}{2s}
\sum_{q=0}^{\min(k,\lfloor(s-1)/2\rfloor)}
\binom{s-1}{2q}4^qC_{k-q},\quad C_j=\binom{2j}j/(j+1)
\]
在 **3,310 个系数上逐项整数相等检查**，全部正且一致。输入同时由独立 JavaScript BigInt 实现重算，得到与本地 Python 完全相同的 Git Blob \`882f133cf16d6440adcf7d475265900da9fef3e0\`（810,940 字节）。

C++ \`R444_PF3_INTEGER.cpp\` 以 \`boost::multiprecision::cpp_int\` 缓存
\[
D(x,y)=a_xa_{y-1}-a_ya_{x-1},
\]
并用恒等式
\[
\det_{0\le i\le2;\,j\in\{x,y,z\}}a_{j-i}
=D(x,y)a_{z-2}-D(x,z)a_{y-2}+D(y,z)a_{x-2}
\]
穷尽所有严格递增列组合。四个批次均返回退出码0及 \`R444_PF3_EXACT_PASS\`；没有使用浮点数、概率性符号判定或高精度浮点容差。独立 Python 六项 Leibniz 展开进一步验证1,250个确定性三阶样本，全部一致。

## PF₄ 否证

每个 \(r\) 取行 \(0,1,2,3\) 和列 \(r-3,r-2,r-1,r\)。从原始 signed 卷积独立重新生成输入，使用24项 Leibniz 整数求和，十个归一化四阶行列式均严格负。**全部十个精确十进制负证**在 \`R445_PF4_TEN_WITNESSES.txt\` 及 \`R445_EVIDENCE_FULL.json\`，原始和归一化整数值也已由另一个 JavaScript BigInt 实现独立重算，输出的 Git Blob 与本地 Python 结果完全一致：\`676fef32e8d34f3e7234d110541ac68bc3735df9\`。因此全部十行均非 PF₄。

## 证据、科学边界、下一问题

可再现程序及全部810,940字节精确输入、四批原始输出、十份负证、抽样记录、SHA256 清单均存放于本目录。证据覆盖的是十个离散 \(r\)，且“精确”指有限整数子式判断；无限尾域 PF₃ 仍待解析证明。作者侧重复计算与独立正式 Driver 审阅不同，不宣称本论证已获数学接纳。引用 R440 的连续四阶障碍仅作一致性校验，PF₄ 否证本身有本轮整数负子式。

BRC 范围：保留原始 signed 卷积与 Catalan 参数映射的两条精确输入路线；gcd 归一化仅缩放标量，不改变子式符号。此标量观察不是未经证明的 X6 状态保真投影，不能将 signed cancellation 解释为 positive-weighted BRC 的非负支路质量。P000、ACTIVE 世界观及原生 X6 动力学结论不变。

**下一问题**：构造覆盖一切奇数 \(r\ge99\) 的三阶单侧连续行 Schur 子式解析正性证明，优先研究 Catalan 比率与参数多项式的符号分解；若暂无统一定理，继续从 \(r=343\) 搜索首个精确三阶负例，而不把有限验证当成无穷证明。

固定读取：GLOBAL_KNOWLEDGE_V1 \`main@44d3d37324cd1999848b2180317491e02b416ce4\`；Enterprise Math \`main@ac48238d40c28c9ad139faa5b0e11cb7defdd8f9\`。本轮原生 \`research_authority_granted=false\`、Owner 查询 \`CONTROL_QUOTA\`，没有 CLAIM、Source Result、独立 Driver 审核或数学接纳。
