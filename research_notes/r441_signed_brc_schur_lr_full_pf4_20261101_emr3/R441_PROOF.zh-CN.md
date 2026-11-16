# R441 | signed BRC：Schur–Littlewood–Richardson 全域 PF4 分类

日期 2026-11-01。状态 AUTHOR_SIDE_ANALYTIC_PLUS_CERTIFIED_EXHAUSTION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。对象仅为 signed BRC 辅助标量 Toeplitz 序列，非原生 X6/心跳世界转移定理。P000、ACTIVE 世界观不变。

## 定义与结论

H(r,s)=binom(r+s,2s)[t^r](1-t)(1+t)^(2s)(1+t²)^(r-s)，2≤s≤r；a_h=H(r,r-h)，0≤h≤n=r−2，越界为0。T_ij=a_(j−i)，i,j≥0。PF_K：全部阶数≤K的子式非负。

**R441-A（任意有限非负序列，a0>0）**：PF_K 当且仅当对每个 1≤m≤K，连续行 0,1,…,m−1 与所有列组合 0≤j1<…<jm≤n+m−1 构成的子式均非负。检查数为 sum(m=1..K) binom(n+m,m)。特别注意：不是仅查行列都连续的 solid 子式。

**R441-B（signed BRC 完整分类）**：对全部奇数 r≥5，T^(r) 是 PF4 当且仅当 7≤r≤97。r=5 与全部奇数 r≥99 具有四阶严格负例；奇数7至97的整个半无限 Toeplitz 矩阵 PF4。

**R441-C（最大 PF 阶）**：r5为3，r7为4，r9/11/13/15均为5，r17/19/…/97均为4。后一族的五阶负例继承 R434 的无限解析定理；r≥99 的最大 PF 阶数仍未确定。

## R441-A 完整证明：对偶 Jacobi–Trudi + Littlewood–Richardson

归一化 b_h=a_h/a0，b0=1，b_h=0（h<0或h>n）。这给出对称函数环的任意实数特化 φ:e_h↦b_h，无须假设相关多项式有实根。

任取 m阶 Toeplitz 子式，行指标 I=(i1<…<im)，列指标 J=(j1<…<jm)。如果存在 jt<it，则按行指标≥it的 m−t+1 个行，需要至少 m−t+1 个列指标≥it，而 J 仅有≤m−t 个，所有排列积均为0。

若逐位 j≥i，置 λ'_p=j_(m+1−p)−(m−p)、μ'_p=i_(m+1−p)−(m−p)，p=1,…,m。严格递增指标保证 λ',μ' 是弱降非负整数列，μ⊆λ 且 λ1≤m。倒排行、列再转置不会改变行列式，故

det[b_(jq−ip)]_(p,q=1..m) = det[b_(λ'_p−μ'_q−p+q)] = φ(s_(λ/μ))。

后一等式是 skew dual Jacobi–Trudi。Littlewood–Richardson 恒等式为 s_(λ/μ)=sum_ν c^(λ)_(μν) s_ν，系数是非负整数；每个出现的 ν 都包含于 λ，因此 ν1≤λ1≤m≤K。普通 s_ν 的 dual Jacobi–Trudi 正是连续行与任意列的子式；若 ν 的长度>n，最右列为零；其余所有普通形状恰对应列组合 J⊂{0,…,n+q−1}、|J|=q=ν1。所以全部指定普通子式非负蕴含全部 skew 子式非负。反向显然。原始 a 的 m阶子式是 b 对应子式乘正数 a0^m，符号不变，证毕。

经典基础来源：M. A. A. van Leeuwen, Schur Functions and Alternating Sums, Electronic Journal of Combinatorics 11(2) #A5 (2006), DOI 10.37236/1897；N. A. Loehr, Abacus Proofs of Schur Function Identities, SIAM J. Discrete Math. 24(4), 1356–1370 (2010), DOI 10.1137/090753462。这里的通用引理是经典恒等式的推论，不宣称原始独创。

## 计算、误差证明与无限参数归结

使用原始 signed 展开 H(r,s)=binom(r+s,2s) sum_(q=0..r−s) binom(r−s,q)[binom(2s,r−2q)−binom(2s,r−2q−1)]，与奇数行 Catalan 形式 H(2k+1,s)=binom(2k+1+s,2s)sum_(q≥0)binom(s−1,2q)4^q C_(k−q)，C_j=binom(2j,j)/(j+1) 逐项核对。对 r=5,7,…,99 的2448个系数全部一致，行内除正gcd不改变子式符号。

48行的 1..4 阶全部普通 Schur 子式总计 44,854,096 个；46行 r=7..97 的40,604,453个全为严格正。r5唯一四阶负例列(1,2,3,4)，归一化行列式−81；r99唯一四阶负例列(96,97,98,99)，归一化行列式为负。r29经独立 Python 任意精度整数完整检查各阶28、406、4060、31465个（合计35959），全部严格正；不是随机窗口。

完整 C++ 判号使用 IEEE binary long double，运行要求 LDBL_MANT_DIG≥64、IEC559、FE_TONEAREST；编译 g++ -O3 -std=c++17 -fno-fast-math。每个输入整数保留最高60位并以二的整数幂缩放，得到 EXACTLY REPRESENTABLE 的浮点值 x；原数与 x 的相对误差严格小于 δ=2^-59。所有输入最大265位，所有四项乘积没有溢出或下溢。Leibniz 至多24项，每项至多4次乘法；u=2^-64、γ_j=ju/(1−ju)，对有符号和 Dhat 和绝对项和 Shat 有

|D−Dhat| / Shat ≤ [((1+δ)^4−1+γ4)/(1−γ4)+γ23]/(1−γ23) < 9×10^-18。

程序仅当 |Dhat|>10^-12 Shat 时用该严格符号认证，否则回退任意精度整数行列式；实际44,854,096个均严格认证，回退次数为0。证据日志 SHA256 1e9ead5adc56beee833aa3a25142652e4c1052633b9dbce3984579b5e0c785cb。R441_EXACT_ANCHORS：小行5/7/9/11/13/15、27/29以 Python 整数 Bareiss 全枚举复核，负证据另以 Leibniz 双重计算。r7五阶负、r9/11/13/15六阶负；其中r9/11/13/15全部五阶普通子式严格正，故最大PF阶均为5。

无限尾由 R440/R432 已完成且本轮重新执行精确符号程序复核：对 r=2k+1，连续四阶边界子式 D_(4,r−3)/H(r,2)^4=−(k+2)P(k)/436590000，其中 P(k)=7936k^7−309248k^6−3408516k^5−14300148k^4−33616293k^3−46354824k²−35761465k−11787442。P(k)/k^6 在 k>0 严格递增，P(48)<0<P(49)，故所有 k≥49（即奇数r≥99）有严格负四阶子式。结合48行的有限完备判定，R441-B 成立。

复现入口：R441_GENERATE_INPUT.py 生成 R441_INPUTS.txt；g++ -O3 -std=c++17 -fno-fast-math R441_SCHUR_CERT.cpp -o R441_SCHUR_CERT；运行 ./R441_SCHUR_CERT R441_INPUTS.txt 5 99；R441_VERIFY_EXACT.py 提供独立整数锚点。完整原始 stdout、gcd系数与机器JSON保留在R441本轮精确证据包。

## 权限、作用域、下一问题

规范固定读取 GLOBAL_KNOWLEDGE_V1 main@7587da72c5f050ee4df05753ccbca1302abefddc、Enterprise Math main@993a408982a302265cb3c31f93e69e4751299500；继承 R440 提交041b43903aed0d809020adcedaab95cf3c7b0cf1，以及R432/R434参数定理。实际 GitHub 登录awdawmip；原生 DIRECTED_RESEARCH authority_granted=false，活跃owner查询CONTROL_QUOTA。没有正式CLAIM/Result/独立Driver review，作者侧成果未获数学接纳。不得将signed标量PF结果视为X6三维切片的保真证明。

后续研究奇数r≥99的最大PF阶及PF3最先失败位置（优先参数化三阶负子式），或将本轮通用Schur/LR降维方法经独立审阅提取为正式工具；无需重复数十亿次旧PF4枚举。
