# R443｜signed BRC 奇数行 203—301 的最大 PF 阶数恰为 3

2026-11-01。状态：AUTHOR_SIDE_CERTIFIED_FINITE_EXHAUSTION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。研究对象是 signed BRC 辅助标量序列，不是原生 X6 动力学。P000 和 ACTIVE 世界观保持不变。

## 1. 目标与精确结论

对奇数 r=203,205,…,301，定义

\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad 2\le s\le r,
\qquad a_h=H(r,r-h),\;0\le h\le r-2,
\]

支持外 a_h=0；半无限 Toeplitz 矩阵 \(T^{(r)}_{ij}=a_{j-i}\)，\(i,j\ge0\)。PF_m 指全部不超过 m 阶的子式非负。

**定理 R443（作者侧计算机辅助）：对全部50个指定奇数 r，整个半无限矩阵 \(T^{(r)}\in PF_3\setminus PF_4\)。** 这是有限参数集合上的全矩阵定理，不等价于对全部奇数 r≥203 的无限参数断言。

## 2. 完备缩减与双公式输入

继承 R441-A：对 a_0>0 的有限支撑 Toeplitz 序列，PF_K 等价于只检查每阶 m≤K 的连续行 I=(0,…,m−1) 与所有严格增列 \(0\le j_1<\cdots<j_m\le n+m-1\) 的子式，n为最大支持指标。证明使用对偶斜 Jacobi–Trudi 以及 Littlewood–Richardson 非负整数展开：一般子式对应斜 Schur 特化；普通 Schur 特化对应连续行和任意列。原定理及证明见 R441_PROOF.zh-CN.md，提交 8fba98f1654ef4050ccc562be1ec197c01f31a47。

对本模型 n=r−2，每行必须完整检查 m=1,2,3 的子式数依次是 \(r-1,\binom r2,\binom{r+1}3\)，50行总计 **12,550 + 1,602,125 + 138,604,200 = 140,218,875**。

R443_GENERATE.py 对每个系数以整数核对两条独立公式：

\[
H_{\rm raw}(r,s)=\binom{r+s}{2s}\sum_{q=0}^{r-s}\binom{r-s}{q}
\left[\binom{2s}{r-2q}-\binom{2s}{r-2q-1}\right],
\]

\[
H_{\rm Cat}(2k+1,s)=\binom{2k+1+s}{2s}
\sum_{q=0}^{\min(k,\lfloor(s-1)/2\rfloor)}
\binom{s-1}{2q}4^q C_{k-q},\quad C_j=\binom{2j}{j}/(j+1).
\]

总共12,550项严格相等且全部正。每行除以正 gcd g，不改变子式符号。实际生成 R443_INPUTS.txt 为2,349,510字节；SHA256 = 58110cfb7715a59adce6b9266623567870d7a2bff13944fc2fece2ea76aa11c9。

## 3. 1至3阶完整符号认证

所有一阶严格正；所有1,602,125个二阶子式使用 Boost cpp_int 任意精度整数直接判正。

所有138,604,200个三阶子式采用**受严格误差界约束的二进制浮点判号，必要时任意精度整数回退**。每个正整数系数 a 向下保留最高至多50位，得到完全可表示的 dyadic w，满足 \(0\le(a-w)/w<\delta=2^{-49}\)。越界零值保持精确零。三因子项的截断相对误差小于 \((1+\delta)^3-1\)。

运行要求 IEC559 二进制浮点、long double≥64位有效尾数、最近舍入、g++ -fno-fast-math，代码对硬件模型、舍入、所有实际判号项的有限性作运行检查。对三阶行列式采用6项 Leibniz 展开；每项两次浮点乘法，行列式及绝对项和各最多5次加法。用 \(u\le2^{-64}\)、\(\gamma_j=ju/(1-ju)\) 的乘法及求和误差界，可严格界定

\[
|\det_{\rm exact}-\widehat D|<6\cdot10^{-15}\widehat S,
\]

其中 \(\widehat S\) 是实际计算的六个浮点单项式绝对值和。这个界保守覆盖三因子截断误差、浮点乘法和求和误差；所有非零截断输入≥1，不发生乘法下溢，程序拒绝非有限结果。

程序仅在 \(\widehat D>10^{-12}\widehat S\) 时认证精确行列式严格正，否则执行完整整数行列式回退。运行结果：三阶138,604,200项全认证正，回退0项，额外使用整数对33,812项规则抽样交叉核验；全样本最小 \(\widehat D/\widehat S=1.69388099089\cdot10^{-6}\)。

R443_CERTIFIED_STDOUT.txt 中实际最后一行：
R443_CERTIFIED_PASS rows=50 total=140218875 k1=12550 k2=1602125 k3=138604200 interval_cert3=138604200 integer_fallback3=0 integer_spotchecks3=33812 min_relative_margin=1.69388099089e-06

实际150条分阶输出及总计文件 SHA256 = 1cc372639d342fc2cf0ab8854014cb5ccf26f7e67a26a465dbcb8a771aac8be0。另用独立的 R443_INTEGER_EXHAUST.cpp 对 r=203 的一至三阶 **1,414,909** 个子式逐项任意精度整数穷尽核验，均严格正；其完成回执 SHA256 = 1d265273d6aafa3f27400630895be365db290456f43838a23c6208ac17c16d5f。其它49行不声称已运行全整数穷尽。

## 4. 四阶负例

每行取连续行 (0,1,2,3) 与列 (r−3,r−2,r−1,r)。R443_PF4_WITNESS.py 重新从原始 signed 卷积生成本行全部系数，再用24项整数 Leibniz 展开算子式；50个结果均严格负。正 gcd 缩放的四次方不改变负号。完整50行十进制原始及归一化负子式的本地实际输出文件 R443_PF4_NEGATIVE_WITNESSES.txt SHA256 = c1fdfe3ab7e0cb80cc41c846329ca54e6eaf894ee8bbfddf5ddd80f264f442b4。另有 R441 对全部奇数 r≥99 的解析四阶负子式定理作为独立来源。合并完整 PF3 正性与每行 PF4 负例，证明 R443 定理。

## 5. 复现和科学边界

运行 Python 3 / g++14.2+Boost：

1. python3 R443_GENERATE.py 203 301（重建精确输入并核验SHA256）
2. g++ -O3 -std=c++17 -fno-fast-math R443_CERTIFIED.cpp -o r443_certified
3. ./r443_certified R443_INPUTS.txt > R443_CERTIFIED_STDOUT.txt（对照SHA256及全部50行计数）
4. python3 R443_PF4_WITNESS.py（对照负例文件SHA256）
5. head -1 R443_INPUTS.txt > R443_EXACT_R203_INPUT.txt；编译运行 R443_INTEGER_EXHAUST.cpp 对203行整数穷尽，核对完成回执。

本轮实际执行系统 x86_64 / g++ 14.2.0；long double: is_iec559=1、digits=64、radix=2、max_exponent=16384、FE_TONEAREST。严格误差界只对这些受核验的数值语义负责；输入重构、源码、判号计数、原始证据SHA256由 R443_EVIDENCE.json 记录。数学结论等待独立复核，属于 signed 标量层，不转移到 X6 原生路径、残差或六维空间。

前沿：R441 Schur/LR（8fba98f1654ef4050ccc562be1ec197c01f31a47）；R442 已完成99—201（78a8bdc58b73343bcf60cdf81dee62ee829976af）。本轮规范读取 GLOBAL_KNOWLEDGE_V1 main@e24390a59977583b8c67ad75824da14f7cec8c17，Enterprise Math main@ace20a3785eb79ba4f7f4fa7299871fffc07a96e，包含规范入口、P000、ACTIVE 世界观和 portable research 协议。

2026-11-01：原生 DIRECTED_RESEARCH 返回 authority_granted=false，活跃 Owner 列表查询返回 CONTROL_QUOTA。因此此 GitHub PR 只作中立作者侧材料保全；正式 Source owner、CLAIM、Research-Activity、Result、独立 Driver Review、数学接纳待权限恢复与后续审阅。未修改 P000/ACTIVE 或正式状态机。

**下一问题**：从 r≥303 寻找首个三阶精确负例，或推导对所有奇数 r≥99 的三阶普通 Schur 子式统一解析非负判据。先复审本轮截断误差界，再探索特征列组合的 Catalan 参数不等式；已完成的 r203—301 不必重复。
