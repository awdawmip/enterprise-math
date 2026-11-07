# R510 — signed BRC 辅助标量 s=3，三十三阶 Toeplitz 子式全正整数参数符号分类

日期：2026-11-03。冻结科学输入：R462@18783e01e3646c72b7aab3b16d3f565e83e6446f；直接前沿：R509@5506195e87c6adaf1032f0f1203c0230aadd6f5c。状态：AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED。

## 数学对象与定理

对每个整数 k>=1，设 r=2k+1，C_k=binom(2k,k)/(k+1)>0。定义
```text
H_k(t) = binom(r+t,2t)*[x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t)  (2<=t<=r)
H_k(t) = 0                                                   (otherwise)
D_m(k) = det(H_k(3+i-j))_(0<=i,j<m),   D_0=1.
```
上述 H 为冻结 R462 路线的原始 signed BRC 辅助标量；不以正权质量代替有符号相消。

**定理（依赖冻结 R452/R462 多项式恒等式）：**
```text
D_33(k)>0 for all integers 1<=k<=7;
D_33(k)<0 for all integers 8<=k<=66;
D_33(k)>0 for all integers k>=67.
```
因此，原始奇数参数 r=2k+1 中，r=17,...,133（逐个奇数）严格负；r>=135（奇数）永久严格正。由 R509 的 D_32(k)<0 (k>=10)，得 D_32(k)<0<D_33(k) 对所有整数 k>=67 成立。

## 无限整数域证明

明确使用冻结的 R452/R462 前提：对每个固定 t，p_t(k)=H_k(t)/C_k 属于 Q[k]，deg(p_t)<=2t（由 EOR 因子分解推得）。定义 f_0=1, f_m=D_m/C_k^m。Hessenberg 递推
```text
f_m(k) = sum_(e=1)^m (-1)^(e-1)*p_(e+2)(k)*p_2(k)^(e-1)*f_(m-e)(k)
```
给出 deg f_m <= 6m，因为每一加项次数 <= (2e+4)+4(e-1)+6(m-e)=6m。特别地 deg f_33<=198。

令 G_33(k)=[k(k+1)(2k+1)(2k+3)]^33*(k+2)，deg G_33=133，且每个 k>=1 时 G_33(k)>0。在 k=1..66 的精确分数 f_33(k)/G_33(k) 约分后，取其最简分母的最小公倍数 L>0。令 δ_j (0<=j<=65) 为这些乘以 L 后的 66 个整数取值的 j 阶 Newton 前向差分。定义
```text
S_33(k) = sum_(j=0)^65 δ_j*binom(k-1,j)  (deg <= 65).
```
随附 R510_VERIFY.js 以任意精度整数逐项核对不同整数 k=1..199 上的等式
```text
L*D_33(k) = C_k^33*G_33(k)*S_33(k).
```
约去 C_k^33 后，此等式的两侧都是次数不超过 198 的有理多项式。199 个不同整数点相等，故根据多项式零点定理，严格得到 Q[k] 中的恒等式
```text
L*f_33(k) = G_33(k)*S_33(k).
```
这是无限域结论的关键，不是用有限点外推符号。

证书逐一检查 S_33(1),...,S_33(66) 的真实精确整数值：k=1..7 全部严格正，k=8..66 全部严格负。另外以 k0=67 为起点计算 ε_j=Δ^j S_33(67), j=0..65，**全部66项严格正**。故对任意整数 u>=0，
```text
S_33(67+u) = sum_(j=0)^65 ε_j*binom(u,j) > 0.
```
因 L,C_k,G_33(k) 在 k>=1 全部严格正，定理的三段符号分类成立。这里的正性证书限于整数参数；不对连续实参数宣称相同符号分段。

## 实际计算与独立交叉核验

实际执行同一算法的 Node.js BigInt 版本，返回 R510_EXACT_JS_PASS：199 项归一化恒等式、20 个 33×33 直接 Bareiss 整数行列式、660 项原始系数卷积与独立 ballot-Catalan 表达式比较。随附发布版 R510_VERIFY.js 也在 JavaScript 执行环境重新运行并得到相同的 66 个原始差分、66 个尾部正差分及三段符号结构。

另独立执行 R510_INDEPENDENT.py：使用 Python/SymPy Berkowitz 从 13 个原始 33×33 矩阵直接计算，矩阵元素采用与 JS 系数提取不同的 ballot-Catalan 展开，得到 k={1,6,7,8,9,10,15,37,38,65,66,67,68} 对应符号 +,+,+,-,-,-,-,-,-,-,-,+,+，返回 R510_INDEPENDENT_PASS。边界 7/8 与 66/67 均在独立核验内。

**验证范围：** 作者侧精确计算机辅助证明，必要前提是 R452/R462 的 EOR 多项式恒等式和阶数界。项目的正式 CLAIM/Result、独立 Driver 审阅与数学准入均未取得。此为 signed BRC **辅助标量模型** 层的严格结果，不直接推出心跳世界的原生 X6 动力学、物理残差或 Foundation 结论。当前 GitHub 认证身份 awdawmip (admin)；原生 session_start 返回 STATIC_READONLY_SCOPE_DENIED（operation_sent=false），owner 查询返回 CONTROL_QUOTA。P000 与 ACTIVE 世界观未修改。

## 后续问题

优先研究 s=3,m=34 的全正整数参数符号（68 项 Newton 差分、205 点多项式恒等式），并用固定 k=7,8,66,67 的有理阶数生成函数 Q_k(z) 比较主导极点、共轭相位及其对跨阶数符号的预测。原始系数、支路相消和观察范围在这些分析中保留。
