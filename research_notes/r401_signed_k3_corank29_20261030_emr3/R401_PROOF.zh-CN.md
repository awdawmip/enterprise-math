# R401 — 第29余阶有符号 BRC 有限 PF₂ 精确分类：完整证明

日期：2026-10-30。作者侧状态：**AUTHOR_SIDE_EXACT / DRIVER_UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING**。本命题不是六维原生 X6/三维切片、无限 Q、完整 D 阵列 TP₂ 或物理校准定理。

## 1. 精确定义与来源

继承 R346 的原始十二支路 K/J→B→D 带符号组合递推（R346_verify.py 原始 Git blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1），输入重建路径继承 R400 的不可变 Git 提交 9a86fbbc3b1b120dad1cd1a1b8e5042a1e58113b。唯一变型是 \(K_3[t^2]=-8(1+\theta)\)，参数 \(\theta>-1\)，其它所有有符号支路保持不变。符号相消不转写为正质量 BRC。

取 \(B_0(t)=1+t\)，对 \(s\ge1\) 令 \(B_s=J_s+\sum_{i=1}^{\min(s,12)}K_iB_{s-i}\)。记 \(b_{s,q}=[t^q]B_s\) 并定义

\[
D_{q,k}=\sum_{w=0}^k(-1)^{k-w}\binom{k}{w}2^{q-w}b_{q+w,q},
\quad H_r(k)=5^{-k}D_{r+k,k},\quad L_r(v)=5^rH_r(v).
\]
\[
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1),
\quad c_j^{(r)}=\Delta^j Q_r(0),\quad T_j=c_j^2-c_{j-1}c_{j+1}.
\]

固定 \(r=29\)，取59项有限序列 \(C_{29}=(c_0,\ldots,c_{58})\)，及57项缺陷 \(T_1,\ldots,T_{57}\)。PF₂ 指该有限序列（超出区间时补零）的 Toeplitz 矩阵所有二阶子式非负。非负序列 PF₂ 当且仅当对数凹且无内部零；在本证明的严格正范围只需逐项 \(T_j\ge0\)。一般背景：F. Brenti (1989), Unimodal, Log-Concave and Pólya Frequency Sequences in Combinatorics；https://www.symmetricfunctions.com/polyaFrequency.htm。

## 2. 全实参数分类定理与证书证明

设 \(a=1868683/1000000\)、\(b=1868684/1000000\)，令 \(\eta_{29}\) 为 \(T_{29}\) 在开区间 \((a,b)\) 的唯一根，则

\[
\boxed{C_{29}(\theta)\in PF_2\quad\Longleftrightarrow\quad -1<\theta\le\eta_{29}.}
\]

显示近似 \(\eta_{29}\approx1.8686834603919513\)，浮点值不用于任何判号。

**完整性第一部分。** 程序 r401_symbolic.py 在整数系数多项式环精确展开原始有符号递推，产生59个 \(c_j(\theta)\) 及57个 \(T_j(\theta)\)。所有原始升幂整数系数可由该程序重建；在完整研究证书包中存有 R401_POLYNOMIALS.json。程序 r401_certify.py 在闭区间 \([-1,b]\) 对每一个 \(c_j\) 及除 \(T_{29}\) 外的全部56个 \(T_j\) 建立严格正的有理 Bernstein 控制系数；在 \([-1,a]\) 另对 \(T_{29}\) 做相同证明。精确有理端点计算得到 \(T_{29}(a)>0>T_{29}(b)\)，并以 \(-T'_{29}\) 在 \([a,b]\) 的全部严格正控制系数证明此处 \(T'_{29}<0\)。故 \(T_{29}\) 在开区间 \((a,b)\) 有唯一简单根，左侧为正、右侧为负；所有其它所需条件始终严格正，临界根处 PF₂ 成立。

**完整性第二部分。** 对任何有理闭区间 \([l,h]\) 和整数多项式 \(p\)，证书在精确有理数域计算恒等式
\[
p(l+(h-l)t)=\sum_{k=0}^n\beta_k\binom nk t^k(1-t)^{n-k},\qquad 0\le t\le1.
\]
若全部 \(\beta_k>0\)，则 \(p>0\) 在整个闭区间成立，不依赖有限点采样。程序用13个端点相接的有理闭区间覆盖 \([b,4]\)，每个区间选择一个 \(c_j\) 或 \(T_j\) 并证明其**负号**的 Bernstein 系数全部严格正，从而每一点均违反 PF₂。对全部 \(\theta=4+u,u\ge0\)，\(-c_0(4+u)\) 的17个升幂系数严格正，因此整个无界尾部均 \(c_0<0\)。这些区间和前一段拼合覆盖整个 \(\theta>-1\)，定理得证。

## 3. 退化点的严格结构等式与局部再入反例

在 \(\theta_*=15/8\) 对整数多项式逐阶精确求导，直到首个非零有理导数，得到：

\[
\boxed{\operatorname{ord}_{\theta_*} c_{29+s}=2s\quad(1\le s\le29),\qquad
\operatorname{ord}_{\theta_*}T_{29+s}=4s\quad(1\le s\le28).}
\]

同时 \(c_{28},c_{29}<0\)，\(c_{30},\ldots,c_{58}=0\)，故退化点不属于 PF₂。此前偶数余阶 R398/R400 的首个退化系数是3阶，而本轮固定奇数余阶是2阶；这**不**自动证明所有余阶的奇偶定理。

在开区间 \((1871533/10^6,1871534/10^6)\)，同一个 \(T_{29}\) 还有一次负到正的简单零点（精确有理端点异号、导数严格正），同时全区间 \(c_{29}<0\)，因此局部 Turán 缺陷回正不等于 PF₂ 恢复。最高系数还满足在整个参数域成立的精确多项式恒等式
\[
\boxed{c_{58}(\theta)=1002242216651368(30-16\theta)^{58},}
\]
其中整数为 Catalan 数 \(\binom{58}{29}/30\)。该恒等式仅声明固定 \(r=29\)，全余阶版本尚未证明。

## 4. 运行证据、适用边界和下一问

本轮实际执行原始 Fraction 数值递推与独立整数 θ 多项式递推，对七个有理参数、59项系数及57项缺陷共812项完成精确相等核验。r401_symbolic.py 返回 **R401_SYMBOLIC_PASS**；r401_certify.py 返回 **R401_EXACT_PASS**。本轮构造120个判号证书对象、132个有理覆盖叶区间、139次精确 Bernstein 检查、9500个严格正有理控制系数，最大二分深度12。\(T_{29}\) 的首根与次根、退化阶数、负性覆盖、无界尾部和全部端点判号均是整数/精确有理运算。完整多项式与机器证据分别为 R401_POLYNOMIALS.json、R401_EVIDENCE.json，二者 SHA256 及重建说明参见 R401_EVIDENCE_INDEX.md。独立解压重新运行后，两份生成 JSON 均逐字节一致。

科学观察器固定为第29余阶有符号组合序列及 Toeplitz 二阶子式，不等同于 P000 原生六维 Cell 动力学、三维切片完整读出、无限 Q、完整 D 阵列 TP₂，也不能推出新的物理事实。未修改 P000 和 ACTIVE 世界观。原生服务报告 research_authority_granted=false，控制任务查询返回 CONTROL_QUOTA，故没有正式 CLAIM、Result、Review 或数学接纳。

**下一问题：**从十二支路组合生成函数或有限差分推导一般 \(c_{2r}=\operatorname{Cat}_r(30-16\theta)^{2r}\)，或者找到严格反例；并解释 \(c_{r+1}\) 在 \(\theta=15/8\) 的奇偶消零阶数。如无法建立统一证明，再推进 r=30 的61项有限 PF₂ 分类。

**来源读快照：**GLOBAL_KNOWLEDGE_V1 main@a8b949c4cf3a47ae30a94b8d08e8ddeeb12e1e9d；Enterprise Math main@154ab052d3f249639c7af245ed7d9899e9efd99a；R400 PR head 9a86fbbc3b1b120dad1cd1a1b8e5042a1e58113b。
