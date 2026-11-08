# PREFIX-579-R6：门控残差的纯交叉轴三阶耦合与秩四定理

日期：2026-11-08（Asia/Shanghai）。科学状态：AUTHOR_DERIVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED。

冻结科学输入：awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d。数学模型为96个原生BRC端口、每端口六个等概率带标签原生动作，联合观察六轴奖励 R1,...,R6 和原生门控 K；n 表示原生动作长度，不是物理心跳时间。沿用 PREFIX-565 原生边、PREFIX-577-R6 二阶协方差、PREFIX-578-R6 96端口精确三阶张量。

## 定理（六轴二次交互、三阶门控残差）

定义原生门控的二阶最优线性残差

\[
Y_n=K_n-\frac{5R_1-R_2+5R_3-R_4-4R_5-4R_6}{192}.
\]

零根处因每步六轴奖励恰有一个为1，这等价于
\(Y_n=K_n-(3R_1+R_2+3R_3+R_4)/64+n/48\)。
对任意 1≤i,j≤6，定义三阶渐近联合累积量率

\[
B_{ij}=\lim_{n\to\infty}n^{-1}\operatorname{cum}(Y_n,R_i(n),R_j(n)).
\]

对于冻结九种允许根，所有极限存在、独立于初始原生端口，且共同等于

\[
\boxed{B=\frac1{73728}
\begin{pmatrix}
0&0&34&-24&-5&-5\\
0&0&-24&14&5&5\\
34&-24&0&0&-5&-5\\
-24&14&0&0&5&5\\
-5&5&-5&5&0&0\\
-5&5&-5&5&0&0
\end{pmatrix}.}
\]

这是一项纯交叉轴三阶耦合定理：六个对角元全部为0，矩阵秩恰为4，且

\[
\ker_{\mathbb Q}(B)=\operatorname{span}_{\mathbb Q}
\{(1,1,1,1,1,1),(0,0,0,0,1,-1)\}.
\]

特别地，令 D=R5-R6，则任意六轴计数的有理线性组合 A 均满足
\(\lim_n n^{-1}\operatorname{cum}(Y_n,D_n,A_n)=0\)。
但其他纯交叉项严格非零，且出现两种符号：

\[
\lim_n n^{-1}\operatorname{cum}(Y_n,R_1+R_3,R_1+R_3)=17/18432>0,
\]

\[
\lim_n n^{-1}\operatorname{cum}(Y_n,R_1+R_4,R_1+R_4)=-1/1536<0.
\]

此前证书也给出全部六项二阶正交
\(\lim_n \operatorname{Cov}(Y_n,R_i(n))/n=0\)，而
\(\lim_n\operatorname{Var}(Y_n)/n=367/73728>0\)。
以上三阶与二阶零式都是渐近率结论，不主张每一有限长度精确为零或过程独立。

## 证明

1. PREFIX-578-R6 在原生冻结96端口转移上，以整数0/1边奖励和有理数Poisson方程求出六坐标的56项三阶渐近张量；每条零根边满足六轴奖励和为1，故对任意n有 R6=n-R1-R2-R3-R4-R5。由累积量三线性无损还原七变量全部84项。
2. 写 beta=(5,-1,5,-1,-4,-4)/192，Y=K-beta·R。用三线性展开 \(B_{ij}=\kappa_{Kij}-\sum_a\beta_a\kappa_{aij}\)，逐项有理数收缩得到显示矩阵。新增证书直接重跑 PREFIX-578-R6 的96端口 BRC 计算，然后执行全部36次收缩，核验84项第五/第六轴交换等式和49项六轴守恒等式。
3. 该矩阵每行和为0且第5、6列完全相同，故两个给定向量均在核内，秩≤4。左上4×4主子式等于 det([[34,-24],[-24,14]])²=(-100)²=10000，故秩≥4，得到精确秩及完整核。两个非零组合由 2B13 和 2B14 与六个零对角元直接推出。
4. 通过 PREFIX-577-R6 完整七维协方差再次核验六项 \(\operatorname{Cov}_{rate}(Y,R_i)=0\) 与残差方差 367/73728。原生允许根间的端点奖励势差给出带权转移矩阵对角相似、谱压力一致，因此全部固定阶渐近联合累积量率根无关。

## 可复现证据与来源

在同一目录中保留以下已发布依赖并运行新增程序：

- PREFIX565_positive_marginal_certificate.py（冻结原生边；Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41）
- PREFIX578_R6_compact_third_cumulant_certificate.py（父三阶证书；Git blob 32fd52de439df1ddfff3ce5d5b2e3d643fbf61c8）
- PREFIX577_R6_PUBLISHED_RESULTS.json（二阶协方差）

执行 python PREFIX579_R6_gate_pure_pair_cumulant_certificate.py。该程序调用前述原生BRC父证书，重新求解27项一二阶Poisson右端、恢复84项三阶张量，再验证矩阵、核、主子式与交叉符号。2026-11-08本地实际运行得到 ALL_CHECKS_PASS。机器结果保存于 PREFIX579_R6_EXACT_RESULTS.json。项目数学性质为作者级精确有理数证明与复用已验证依赖，独立审查尚未发生。

## 下一科学问题与控制状态

从576条原生动作的组合配对、门控来源和支路交换直接解释六个对角零式，构造不依赖三阶张量全求解的路径证书。进一步计算四阶渐近混合累积量，判定此秩四纯交叉轴模式是否延伸到更高阶。

本轮真实Source原生任务控制返回 STATUS_DATABASE_UNAVAILABLE，operation_sent=false；未确认活跃Owner或新原生Researcher-ID会话，未写入正式CLAIM、Result、Review，也未提升Working Truth。作者级GitHub科研材料独立保存不改变P000或冻结科学输入。
