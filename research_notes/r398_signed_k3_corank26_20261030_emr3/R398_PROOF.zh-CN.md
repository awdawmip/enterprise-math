# R398｜第26余阶带符号 BRC 有限 PF₂ 全参数分类与奇偶消零反例

日期：2026-10-30。作者侧精确研究（DRIVER_UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING）。

## 对象和来源

继承 R397 不可变提交 34e93b04769fec82c5eb477274af0f56a7b08569、原始 R346 signed K/J 十二支路（Git Blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1），唯一参数修改是 K₃[t²]=−8(1+θ)，θ>−1。定义
\[
B_0=1+t,\quad B_s=J_s+\sum_{i=1}^{\min(s,12)}K_iB_{s-i},\quad
b_{s,q}=[t^q]B_s,
\]
\[
D_{q,u}=\sum_{w=0}^u(-1)^{u-w}\binom uw 2^{q-w}b_{q+w,q},\quad
H_r(u)=5^{-u}D_{r+u,u},\quad L_r(v)=5^rH_r(v),
\]
\[
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1),
\quad c_j^{(r)}=\Delta^jQ_r(0),\quad T_j=c_j^2-c_{j-1}c_{j+1}.
\]
固定 r=26，有限序列 C₂₆=(c₀,…,c₅₂) 共53项，T₁,…,T₅₁ 共51项。在所有 c_j>0 时，有限 Toeplitz PF₂ 等价于全部 T_j≥0（相邻比值单调蕴含全部二阶子式非负）。

## 主定理和精确证明

令 a=1869091/1000000、b=1869092/1000000，η₂₆ 为多项式 T₂₇ 在 (a,b) 内的唯一实根，则
\[
\boxed{C_{26}(\theta)\in PF_2\iff -1<\theta\leq\eta_{26}.}
\]
显示近似 η₂₆≈1.869091559974847，严格证明使用有理区间而非显示小数。

直接由原始 K/J→B→D 递推精确生成53个整数系数 θ 多项式 c_j 和51个 T_j。对每个 c_j 在 [-1,b]、除 T₂₇ 外每个 T_j 在 [-1,b]、以及 T₂₇ 在 [-1,a]，用精确有理 Bernstein 展开证明严格正；T₂₇(a)>0>T₂₇(b)，且 -T₂₇' 在 [a,b] 的全部 Bernstein 系数严格正。因此 η₂₆ 唯一，临界点满足 PF₂，而 (η₂₆,b] 的 T₂₇<0。

对 [b,4]，十个无缝相接的闭有理子区间各自有某个 c_j 或 T_j 严格为负；负性证书由相应多项式的负值 Bernstein 控制系数全严格正给出。对 θ=4+u、u≥0，-c₀(4+u) 的所有非零幂系数严格正，排除整个无界尾部。上述四段构成 θ>−1 的完备覆盖。

Bernstein 证书逐区间精确核验恒等式 p(l+(r-l)t)=Σ β_k binom(n,k)t^k(1-t)^(n-k)，β_k 为严格有理数。β_k>0 证明整个闭区间 p>0。源代码中的自适应闭区间细分和尾部逐幂证书构成可复核的有限证明，不从有限参数采样推断全参数。

## 新增结构结论

T₂₇ 在 (1880946/1000000,1880947/1000000) 有第二个经过端点异号、导数严格为正认证的简单实根，近似 1.880946078831414；该区间 c₂₇<0，所以该缺陷转正并不恢复 PF₂。

最高系数精确恒等式：
\[
\boxed{c_{52}(\theta)=18367353072152(30-16\theta)^{52}.}
\]

在 θ*=15/8，全部如下消零阶数由整数多项式连续求导与有理值判定：
\[
\operatorname{ord}_{\theta_*}c_{27}=3,\qquad
\operatorname{ord}_{\theta_*}c_{26+s}=2s\ \ (2\le s\le26),
\]
\[
\operatorname{ord}_{\theta_*}T_{26+s}=4s\ \ (1\le s\le25).
\]
此外 c₂₅(θ*),c₂₆(θ*)>0，T₂₄(θ*),T₂₅(θ*)<0，故退化点非 PF₂。

**跨余阶精确反例：**R397 固定奇余阶 r=25 得 ord c₂₆=2；本轮固定偶余阶 r=26 得 ord c₂₇=3。因此简单猜想“所有 r 的 ord c_{r+1} 均为 2”为假。统一阶数规律需证明奇偶区别或识别额外条件，不能由本轮固定 r 结论推广全 r。

## 计算与验证边界

原始 Fraction 递推与符号 θ 多项式在七个精确有理 θ 点完成728项交叉核验。精确参数证明生成108个判号证书对象、117段连续有理叶区间，执行122次 Bernstein 检查，获得7672个严格正有理控制系数（最大细分深度9）。实际执行输出 R398_SYMBOLIC_PASS、R398_EXACT_PASS。

复现顺序：python r398_symbolic.py && python r398_certify.py（Python3、sympy），再对 R398_EVIDENCE.json 和 R398_POLYNOMIALS.json 校验 SHA256。无损证据文件见 R398_EVIDENCE.json.gz.b64，核验和解压说明见 R398_EVIDENCE_INDEX.md。上述输出限于带符号十二支路 BRC 辅助组合模型第26余阶的有限53项观察，不自动成为无限 Q、全部 D 的 TP₂ 或原生三维切片/X6 动力学的证明。

固定全球知识快照 GLOBAL_KNOWLEDGE_V1 main@f63239e195e1f1086e9017cfd97cd04344a2b3cd，项目规范 main@e59ac00b5862cb06ba46d6749b77a26d3a0bd94f。P000 与 ACTIVE 世界观未更动。GitHub 身份 awdawmip；原生 em_status v0.6.11 报 authority_granted=false，em_control_tasks 返回 CONTROL_QUOTA，当前活跃 Source Owner 无法权威确认。本轮无 CLAIM/Result/Driver Review 回执，研究为 AUTHOR_SIDE_EXACT / DRIVER_UNREVIEWED / NOT_ADMITTED。

**下一研究单元：**从十二支路原始递推推导或证伪 odd r:ord(c_{r+1})=2、even r:ord(c_{r+1})=3 的全 r 奇偶猜想；研究两个 η_r 奇偶子序列是否收敛及共同参数上界；由真正独立审阅者核查原始 BRC 输入、Bernstein 算法与全部证书。
