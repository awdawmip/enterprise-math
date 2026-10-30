# R408 — 带符号 BRC：五条固定左边界 Turán 无界余阶正性定理

日期：2026-10-30。研究地位：作者侧精确计算机辅助证明；UNREVIEWED / NOT_ADMITTED。范围仅限原始十二支路有符号 BRC K/J→B→D 的辅助组合模型，不包含原生 X6 动力学、外部物理实证或正式 Result/Driver Review。P000 与 ACTIVE 世界观保持原样。

## 定理

对整数 r≥2、0≤s≤r，定义

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^{2}-H_{r,s-1}H_{r,s+1}.
\]

**R408-A：对于全部整数 17≤s≤21 和全部整数 r≥s+1，严格有 D_{r,s}>0。**

这里每个固定 s 都覆盖无限多个 r。结合 R404 s=3…5、R407 s=6…16，以及 R406 的 k=r−s≤128 正性结果，尚未覆盖的整数区域是 s≥22、r−s≥129（首个可能余阶 r=151）。本成果依赖 R404/R407 的原始组合恒等式，未对前置研究进行独立 Driver 审核。

## 精确代数证明

复用 R404 的 Catalan 正核公式

\[
\delta_{r,s}=\sum_{\substack{0\le j<s\\r-s+j\equiv0\pmod2}}\binom{s-1}{j}2^{s-1-j}
\mathrm{Cat}_{(r-s+j)/2},\qquad \mathrm{Cat}_n=\binom{2n}{n}/(n+1).
\tag{1}
\]

令 r=2m+ε，ε∈{0,1}；C₀(m)=Cat_{m−1}、C₁(m)=Cat_m、Δ_{s,ε}(m)=δ_{2m+ε,s}/Cε(m)。由 Cat_{u−1}/Cat_u=(u+1)/(2(2u−1)) 和二项式比值，获得 R407 使用的精确归一化恒等式

\[
\frac{D_{2m+\epsilon,s}}{(\binom{2m+\epsilon+s}{2s}C_{\epsilon}(m))^2}
=\Delta_{s,\epsilon}(m)^2-\lambda(2m+\epsilon,s)\Delta_{s-1,\epsilon}(m)\Delta_{s+1,\epsilon}(m),
\tag{2}
\]
\[
\lambda(r,s)=\frac{2s(2s-1)(r+s+1)(r-s)}
{(2s+2)(2s+1)(r+s)(r-s+1)}.
\]

对每组 s=17,…,21 及 ε=0,1，令 m₀=ceil((s+1−ε)/2)，x=m−m₀≥0。使用 Python 3/SymPy 的精确有理符号运算，把式 (2) 约成互素整数多项式之比 P_{s,ε}(x)/Q_{s,ε}(x)。**10组 P、Q 的所有整数幂系数严格为正**：195 个分子系数和 195 个分母系数。偶数 r 组分子/分母同为 s−1 次，奇数 r 组同为 s 次；所有完整降幂数组、逐组哈希见 R408_EVIDENCE.json.gz（gzip 解压为原始 JSON）。故任意 x≥0 均有 P>0,Q>0；归一化除数严格为正，证明所述全部无界余阶的 D>0。

本论证的无限范围来自对10组**完整符号恒等式和全系数严格正性**的机器精确检查，绝不把有限 r 抽样当成无限证明。形式证明系统认证、独立审阅均未完成。

## 实际运行

同一已运行程序 r408_verify.py 输出：

R408_EXACT_PASS 10 195 195 505 1515

其中 505 次是独立原始整数 D 与归一化 P/Q 的交叉乘法核验；1515 次是原始 (1−t)(1+t)^{2s}(1+t²)^{r−s} 二项式整数展开与 Catalan 核之间的核验。范围为每组最小合法 r 到 r≤120 的同奇偶整数值，属于排错辅助检查，并不替代符号证明。没有使用浮点判号。

重建命令：python r408_verify.py；也可 python r408_verify.py --single-s 17 --single-parity 0 查看单组 JSON。完整原始 JSON 的 SHA256 = 6b72b462c85f81f49774a379f65ad29bd30f0aebbe672356b164c8259dcf2350，实际执行源码 SHA256 = a0dec94d113a7a49ef7ee7be96d79c8a2282664e99bf52ede77db07956666967。

## 来源、权限及下一步

GLOBAL_KNOWLEDGE_V1 固定读取 main@c466fed63edfe02a40d208b3b5147cdd115ea119；Enterprise Math 控制基线 main@d9da66cf2facef49a02ae5d0c5984bdce8465cad；R404@89cba1614fe75643ffb61e3e715169e2de103528、R406@061fe73812cc1f5e1fd3fa060c860a4758288c22、R407@9e56f04779c2c4bca36b3d8a3ea4da2583cd98f8。本轮核对 P000、ACTIVE 世界观与 portable research 协议。原生 Enterprise Math gateway 报告 research_authority_granted=false，control_tasks 返回 CONTROL_QUOTA，Source Owner/CLAIM 未得到权威确认。GitHub 上持久化不代表正式研究活动登记或数学接纳：ACTIVITY_REGISTER_PENDING / DRIVER_UNREVIEWED / NOT_ADMITTED。

下一问题：研究 s≥22、r−s≥129 区域的统一 Catalan 比值不等式/严格反例；先从 s=22 的全 r 精确证书入手，也可寻找不依赖固定 s 或 k 上界的解析机制。与 R403 形式 Turán 首项传递关系组合时，仍须保留该传递接口独立审阅的条件性。