# 有限控制研究成果、公式与复用索引（C22–C26）

整理日期：2026-10-22（Asia/Shanghai）；固定读取快照：`63f87045b456cf573a9eaa7bbc8d4a4673a3e6ea`。

本页提取既有结论，不新增证明、数学审核票或准入。原稿的创建状态保持不变；每条另列已经发表的非作者技术审核出处。该组均为显式外部有限正模型，完整联合观察、已知图、严格参数域及控制／背景假设必须一起复用。没有原生传播或物理桥的升级。

| 条目 | 可复用输出 | 边界 |
|---|---|---|
| [FC-C22-FAMILY](#fc-c22-family) | 实际 C22 严格源族：成员判据、正端点、闭包与不取到 | 闭立方体只是多项式紧化，端点未被加入原可容许参数域。 |
| [FC-C23-TWOLEVEL](#fc-c23-twolevel) | C23 两档共同未知背景辨识与七阶弱方向 | 不是两个标量读数；任意正数据对的正特征向量还须通过完整实际族成员测试。 |
| [FC-C24-ROBUST](#fc-c24-robust) | C24 有界漂移兼容性与确定性反推外包 | 外包不保证各坐标极值可同时实现；仍需实际源族成员关系。 |
| [FC-C25-KNOWN-R](#fc-c25-known-r) | C25 已知共同缩放率与几何背景的有限档辨识 | 充分档数不宣称最少；未执行完整图非线性反求算法；读数不是同数量标量。 |
| [FC-C25-UNKNOWN-R](#fc-c25-unknown-r) | C25 单一未知共同缩放率的有限档辨识 | 不适用于未知逐面/逐边独立缩放、任意隐藏漂移、未知图、缺联合状态、r=0或1、零参数。 |
| [FC-C26-RANK4](#fc-c26-rank4) | 实际 210 四个 alpha 控制的全局辨识 | 未证明4个控制最少；不推广到多方面矩形、其他控制子集、D>=1或控制相关背景。 |
| [FC-C26-IMAGE](#fc-c26-image) | C26 完整正数据的准确模型像与归一化恢复 | 完整正数据的存在/像结论，不是统计拟合、采样或参数lambda逆。 |
| [FC-C26-FIT](#fc-c26-fit) | C26 无限制正族的投影最佳拟合、准确有符号对偶 | 对原受限F，delta_all只是下界，不能据此宣称受限最优值相等或取到。 |
| [FC-C26-INVERSE](#fc-c26-inverse) | C26 固定正控制下两个可容许目标的投影逆界 | 不证明任意数据有目标、不判F成员、不恢复lambda、不保证最佳拟合。 |
| [FC-C26-CLOSURE](#fc-c26-closure) | C26 原受限族的相对闭包与实际最佳拟合取到 | 相对闭不等于紧；最优表可不唯一。 |

## FC-C22-FAMILY · 实际 C22 严格源族：成员判据、正端点、闭包与不取到

**假设与定型**

- 固定已知 a×b 矩形(a,b>=1)，完整约数图为2^a3^b·5·7；V,E,F分别是其底图顶点、边、方面集合。
- r=|E|+|F|，Y=F2^r为完整独立旧联合字符状态；p=|V|+2|E|+|F|；lambda=(q_v,alpha_e,beta_e,z_f)∈(0,1)^p。
- 成员测试的输入是严格正、均匀平均1的完整K；h=(T,U)∈F2^F×F2^E；partial_2和partial_1为模2边界。

**公式**

- `c_(T,U)=prod_(f∈T)z_f prod_(e∈U)alpha_e prod_(e∈U△partial_2T)beta_e prod_(v∈partial_1U)q_v; K_lambda(y)=sum_h c_h(-1)^(h·y).`
- `c_h=|Y|^(-1)sum_y K(y)(-1)^(h·y)=prod_(i:h·gamma_i=1)lambda_i; c_0=1.`
- `W_e=alpha_e beta_e q_u q_v; B_f=z_f prod_(e∈partial f)beta_e; R_v is source(T=empty,U={e,h}) for two distinct edges meeting v; H_e is source(T={f(e)},U={e}).`
- `t_(q_v)=W_eW_h/R_v; t_(beta_e)=W_eB_(f(e))/H_e; t_(alpha_e)=W_eH_e/(B_(f(e))t_(q_u)t_(q_v)); t_(z_f)=B_f^2/prod_(e∈partial f)t_(beta_e).`
- `K∈F iff all selected W,B,R,H>0, every 0<t_i<1, and for EVERY character index h!=0 (including coefficients that might be zero in the input), c_h>0 and c_h^2=prod_(i:h·gamma_i=1)t_i; then lambda_i=sqrt(t_i) uniquely.`
- `For lambda∈[0,1]^p: K_lambda(y)=|Y|Pr(sum_i delta_i gamma_i=y), Pr(delta_i=0)=(1+lambda_i)/2; supp K_lambda=span_F2{gamma_i:lambda_i<1}.`
- `closure_(Pplus)F={K_lambda:lambda∈[0,1]^p, span{gamma_i:lambda_i<1}=Y}; 1∈closure_(Pplus)F\F.`
- `For every fixed known positive XOR control and good C26 schedule, P*_j(y)=1/|Y| has inf_(K∈F,all allowed Q,D_k) d_obs(P,P*)=0 with NO actual minimizer.`

**结论**

- 成员判据检查全部字符，提供严格域内唯一逆；仅选定的p个系数不足以判任意数据可实现。
- 正端点条件恰为活动列张成全Y；实际开参数族在严格正目标空间中非相对闭。
- 同一实际族有正数据的最佳拟合下确界不取到，所有允许背景/漂移自由度已计入。

**复用边界**

- 闭立方体只是多项式紧化，端点未被加入原可容许参数域。
- 未分类零参数纤维；未说明每张数据均不取到；坏schedule不在不取到结论中。
- 不是求解器、复杂度/统计置信/可测量性/物理/Native结论。

**来源与审核状态**

- [原稿 · EM-DVR-BFF6DC](https://github.com/awdawmip/enterprise-math/blob/bc18927084a5e10d19e8071afbb2ac0b6b025105/research_notes/owner_goal_20261017/c26_actual_lambda_family_intake_bff6dc/C26_ACTUAL_C22_SOURCE_FAMILY_MEMBERSHIP_POSITIVE_ENDPOINTS_AND_FIT_NONATTAINMENT_APPLIED_CONSUMER_V1.md)；blob `866c0df398c61567ea2711b498a3c2695d9e116e`。
- [既有非作者技术审核 · EM-DIRECT-9F7A5C](https://github.com/awdawmip/enterprise-math/blob/b668f2f421c89313a1966cf769c47427c27c5adc/research_notes/owner_goal_20261017/reviews/c26_actual_lambda_family_independent_9f7a5c/C26_ACTUAL_C22_FAMILY_MEMBER_ENDPOINT_AND_ORIGINAL_FIT_NONATTAINMENT_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；blob `7d82d45266ff5f368591327ce6896d3b3101b894`。

来源所载审核：`NONBLIND_PASS_BOUNDED_NEW_COMPLETE_TECHNICAL_WHOLE_SCOPE_ONLY`。此整理未改变原创建状态，未新增审核或Foundation/正式准入。

**方法与去重**：`RESULT_ONLY_STANDARD_APPLIED_COMPOSE`；普通工具库存入分类为 `RESULT_ONLY`，不新增Tool。采用 finite Fourier characters / finite auxiliary bit support / exact monomial inverse / compact polynomial image / positive-kernel maximum/minimum。Abstract arbitrary-F closure did not establish this actual source family.

## FC-C23-TWOLEVEL · C23 两档共同未知背景辨识与七阶弱方向

**假设与定型**

- 同一严格源族、已知矩形图和完整Y联合分布；已知0<rho_i<=1。
- rho_i<1的gamma_i张成Y，使已知XOR控制T_rho逐元素严格正。
- 两档共有同一个未知严格正背景Q，sum Q=1；两份数据均完整严格正。

**公式**

- `T_rho f(y)=E_delta f(y+sum_i delta_i gamma_i); Pr(delta_i=0)=(1+rho_i)/2; T_rho K_lambda=K_(rho lambda).`
- `P_1=QK/Z_1; P_r=Q(T_rho K)/Z_r; R=P_r/P_1; A=diag(1/R)T_rho; AK=(Z_r/Z_1)K.`
- `mean K=1; Q(y)=[P_1(y)/K(y)]/sum_z[P_1(z)/K(z)].`
- `For the stated 210 witness: ||epsilon lambda-epsilon lambda'||_infinity=epsilon/6, while TV(P_(epsilon lambda),P_(epsilon lambda'))=Theta(epsilon^7).`

**结论**

- 正特征向量唯一到比例，均值归一化使K唯一，随后Q唯一。
- 对实际C22严格族，可复用FC-C22-FAMILY的来源逆得到lambda；原C23 peer中的历史条件判断保留。
- 给出的七阶方向排除覆盖弱作用零邻域的统一Lipschitz参数逆界。

**复用边界**

- 不是两个标量读数；任意正数据对的正特征向量还须通过完整实际族成员测试。
- 允许两档任意漂移时点识别失败；低秩控制的一般K轨道歧义不等于实际受限源族歧义。
- Theta(epsilon^7)是指定方向；不排除所有弱于Lipschitz的模量。原合成数表/代码未在本整理复核。

**来源与审核状态**

- [原稿 · UNKNOWN_ORIGINAL_AUTHOR](https://github.com/awdawmip/enterprise-math/blob/87577d0e11761c50d358aa8c804bb62c3394e6ee/research_notes/divisor_extrema/20261015_c23_two_level_blind_reference.md)；blob `2e5994baa4e4d6ee16b3aa85e1cbd2f6647a9892`。
- [既有非作者技术审核 · EM-P11-4A56E9](https://github.com/awdawmip/enterprise-math/blob/1f7878912027dbb2407fc167bce0d980d29faacb/research_notes/owner_goal_20261017/reviews/c23_two_level_blind_reference_nonauthor_4a56e9/C23_TWO_LEVEL_BLIND_REFERENCE_NONBLIND_COMPLETE_CONDITIONAL_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；blob `49e4e6c9740163eadc050e8ac9216019c1a246ad`。

来源所载审核：`NONBLIND_INDEPENDENT_TECHNICAL_WHOLE_PASS_BOUNDED_CONDITIONAL_FINITE_MODEL_THEOREMS`。此整理未改变原创建状态，未新增审核或Foundation/正式准入。

**方法与去重**：`RESULT_ONLY_STANDARD_COMPOSE`；普通工具库存入分类为 `RESULT_ONLY`，不新增Tool。采用 finite character multiplier / Perron-Frobenius maximum/minimum uniqueness / homogeneous finite-source weak direction。FC-C26-RANK4 removes global positivity only for actual210, not by applying this theorem outside scope.

## FC-C24-ROBUST · C24 有界漂移兼容性与确定性反推外包

**假设与定型**

- 已知同一矩形严格源族和完整两档正分布；候选K=K_lambda。
- 名义XOR核T_0逐元素正，a=min nu>0，b=max nu，tau=(b-a)/(b+a)。
- 实际核逐元素 l T_0<=T_*<=u T_0 with 0<l<=u，C_ctl=u/l；背景比例展宽<=D；两档读数逐元素相对误差eps_1,eps_r<1；所有预算是已给条件。
- 候选向量v必须逐元素严格正且均匀平均1；S_res因此有定义。

**公式**

- `S(u,v)=max_y(u_y/v_y)/min_y(u_y/v_y); d_H(u,v)=log S(u,v).`
- `D_min(lambda)=S((P_r/P_1)K/(TK),1); lambda compatible with drift budget D iff D_min(lambda)<=D.`
- `E_data=((1+eps_1)/(1-eps_1))((1+eps_r)/(1-eps_r)); A=diag(1/Rhat)T_0; S_res=S(Av,v), v>0 and mean v=1.`
- `S(K,v)<=H_K=(D E_data C_ctl S_res)^((a+b)/(2a)).`
- `c_low=((1+c_hat)-H_K(1-c_hat))/((1+c_hat)+H_K(1-c_hat)); c_high=(H_K(1+c_hat)-(1-c_hat))/(H_K(1+c_hat)+(1-c_hat)).`
- `For the specified 210 weak witness and r=1/2: D_min-1~(22225/393216)epsilon^7.`

**结论**

- D_min是所需漂移的准确充要判据；任意D>1在共同背景内部真值附近留下参数开邻域，因此不能维持点识别。
- 统一核/背景/读数/余量预算给K、每个字符、继而严格参数和背景的可靠外包。

**复用边界**

- 外包不保证各坐标极值可同时实现；仍需实际源族成员关系。
- 逆式分母下界触0时只返回原域(0,1)，不能报零参数或更窄区间。
- 确定性预算不是统计置信区间；原脚本、十进表和执行计数未在本整理复验。

**来源与审核状态**

- [原稿 · UNKNOWN_ORIGINAL_AUTHOR](https://github.com/awdawmip/enterprise-math/blob/ad64fb86b1dd3df173a47c2fb2e95f932c5b54a1/research_notes/divisor_extrema/20261015_c24_bounded_drift_inverse_certificates.md)；blob `5eb2820e205855e8fea75781b20a4db23e15858d`。
- [既有非作者技术审核 · EM-DIRECT-9F7A5C](https://github.com/awdawmip/enterprise-math/blob/0e84d96096cefac837bf6b24a9db425df69783af/research_notes/owner_goal_20261017/reviews/c24_orphan_bounded_drift_independent_9f7a5c/C24_BOUNDED_DRIFT_INVERSE_CERTIFICATES_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；blob `a34730bd2ac4293be81c826152ceeca0422ab27c`。

来源所载审核：`NONBLIND_PASS_BOUNDED_CONDITIONAL_COMPLETE_TECHNICAL_WHOLE_SCOPE_ONLY`。此整理未改变原创建状态，未新增审核或Foundation/正式准入。

**方法与去重**：`RESULT_ONLY_STANDARD_COMPOSE`；普通工具库存入分类为 `RESULT_ONLY`，不新增Tool。采用 Hilbert projective contraction (Birkhoff-Hopf) / positive control envelope / event-odds intervals / exact finite source inverse。A deterministic budgeted outer certificate differs from exact image/fit existence and from C26 two-admissible-target inverse.

## FC-C25-KNOWN-R · C25 已知共同缩放率与几何背景的有限档辨识

**假设与定型**

- 固定已知实际源族，lambda∈(0,1)^p；已知同一标量r∈(0,1)，控制lambda->r^j lambda。
- P_j(y)=Q(y)D(y)^j K_(r^j lambda)(y)/Z_j为连续j=0,...,L-1的完整联合分布。
- Q>0且sum Q=1，D>0且D(y_ref)=1；j是配置编号。
- S为已知有限源次数的上支持并含0，A_y(t)=K_(t lambda)(y)=sum_(k∈S)a_k(y)t^k，a_0=1。
- 单独二值小桥另要求0<w,c<1及B,D>0；单调性公式只在此域。

**公式**

- `L=2|S+S| complete consecutive levels suffice; coarse bound L<=4D_max+2.`
- `210: S={0,4,5,6,7,8,9}, |S+S|=16, L=32 (32 states each). 630: S={0,4,5,...,16}, L=60 (512 states each).`
- `For a candidate lambda, q_j(y)=P_j(y)/K_(r^j lambda)(y); geometric-background compatibility iff q_j(y)q_(j+2)(y)/q_(j+1)(y)^2 is state-independent for EVERY j.`
- `Separate binary bridge (0<w,c<1 and B,D>0): O_j=BD^j h(wc^j), h(x)=(1+x)/(1-x); O_0O_2/O_1^2=Phi_c(w)=h(w)h(c^2w)/h(cw)^2; d_w log Phi_c=2(1-c)^2[1+2c(1+c+c^2)w^2+c^4w^4]/[(1-w^2)(1-c^2w^2)(1-c^4w^2)]>0.`
- `Specified 210 weak witness: curvature_spread-1~(2822575/50331648)epsilon^7 for r=1/2; osc D7=175/3072.`

**结论**

- 有限档完整分布唯一确定lambda、归一化Q和D比例类。重复指数底数先合并后用Vandermonde。
- 二值小桥单独给三档唯一性、两档不足；其几何赔率是假设。

**复用边界**

- 充分档数不宣称最少；未执行完整图非线性反求算法；读数不是同数量标量。
- 任意联合几何Q D^j取边缘后不必仍有二值几何赔率，不能把小桥假设偷换为联合模型结论。
- 没有统一弱作用稳定界、物理实现或原代码/数表认证。

**来源与审核状态**

- [原稿 · UNKNOWN_ORIGINAL_AUTHOR](https://github.com/awdawmip/enterprise-math/blob/f2e46a25194fc89cd540d7e87f7108b4b1f06e28/research_notes/divisor_extrema/20261016_c25_structured_drift_multilevel_identifiability.md)；blob `1593a20391f08cb738d95048ab4ae7272000c507`。
- [既有非作者技术审核 · EM-PUBLIC-7CDA51](https://github.com/awdawmip/enterprise-math/blob/09348cdb57d73088558b7a515c7d1ccba6e08a1f/research_notes/owner_goal_20261017/reviews/c25_structured_drift_nonauthor_7cda51/C25_STRUCTURED_DRIFT_NONBLIND_COMPLETE_CONDITIONAL_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；blob `a403cb382b9d96e55efe46958764912c79ad29de`。

来源所载审核：`NONBLIND_COMPLETE_TECHNICAL_WHOLE_PASS_BOUNDED_CONDITIONAL_MATHEMATICAL_SCOPE`。此整理未改变原创建状态，未新增审核或Foundation/正式准入。

**方法与去重**：`RESULT_ONLY_STANDARD_COMPOSE`；普通工具库存入分类为 `RESULT_ONLY`，不新增Tool。采用 finite exponential sums / Vandermonde after collisions merge / cross-state log odds / finite source homogeneity。The unknown-r application has S×S bases and a distinct sufficient count; do not replace this sharper known-r bound by its larger count.

## FC-C25-UNKNOWN-R · C25 单一未知共同缩放率的有限档辨识

**假设与定型**

- 保留FC-C25-KNOWN-R全部源族、完整联合分布和Q D^j假设，唯一改动为r∈(0,1)也未知。
- 只有一个共同未知r；图已知、所有lambda严格在(0,1)，连续j从0开始。

**公式**

- `L=2|S|^2 complete consecutive levels suffice to identify(r,lambda,Q,relative D).`
- `Cross-difference bases lie in {delta r^k r'^ell, delta' r^k r'^ell:(k,ell)∈S×S}; merge repeated bases BEFORE Vandermonde.`
- `210: |S|=7, L=98 complete32-state rows. 630: |S|=14, L=392 complete512-state rows.`
- `j=0 full K gives lambda=lambda'; j=1 degree4 edge coefficient gives W_e r^4=W_e r'^4, W_e>0, hence r=r'.`

**结论**

- 以更多完整档位替代已知单一r的条件，仍唯一恢复r、严格参数、背景和漂移规范。

**复用边界**

- 不适用于未知逐面/逐边独立缩放、任意隐藏漂移、未知图、缺联合状态、r=0或1、零参数。
- S×S不能缩成S+S，除非两个待比较速率已经相同。
- 充分而非最优档数；无求解算法、精度保证或物理校准结论。

**来源与审核状态**

- [原稿 · EM-PUBLIC-7CDA51](https://github.com/awdawmip/enterprise-math/blob/09348cdb57d73088558b7a515c7d1ccba6e08a1f/research_notes/owner_goal_20261017/reviews/c25_structured_drift_nonauthor_7cda51/POST_FREEZE_UNKNOWN_COMMON_RATE_FINITE_IDENTIFIABILITY_COMPOSE_WORKING_AND_CONTEXT.md)；blob `8b0d711fb93925e867aacbf2d64656f09d98c62e`。
- [既有非作者技术审核 · EM-DIRECT-9F7A5C](https://github.com/awdawmip/enterprise-math/blob/d2af7d720c9d840af4b6d20ae1374c9549a87dec/research_notes/owner_goal_20261017/reviews/c25_unknown_common_rate_independent_9f7a5c/C25_UNKNOWN_COMMON_RATE_FINITE_IDENTIFIABILITY_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；blob `0212e8e0e3fa29b24eccc926c238e59d2a4d8503`。

来源所载审核：`NONBLIND_PASS_BOUNDED_NEW_COMPLETE_TECHNICAL_WHOLE_SCOPE_ONLY`。此整理未改变原创建状态，未新增审核或Foundation/正式准入。

**方法与去重**：`RESULT_ONLY_STANDARD_COMPOSE`；普通工具库存入分类为 `RESULT_ONLY`，不新增Tool。采用 finite exponential sums with product support / Vandermonde / strict degree4 Fourier coefficient。Same Source commit also adds an older known-r review; that other file is not a second author proof or a second vote for this result.

## FC-C26-RANK4 · 实际 210 四个 alpha 控制的全局辨识

**假设与定型**

- 仅a=b=1的实际210图，13个lambda全在(0,1)，完整32状态。
- 只缩放四个alpha_e，已知0<rho_e<1；Q>0且sum Q=1，两档共有Q；D=0无漂移。
- 控制rank4<5，两个固定t块各有16状态且块内严格正，跨块为0。

**公式**

- `A_U=prod_(e∈U)(alpha_e beta_e)prod_(v∈partial U)q_v; B_U=z prod_(e∈U)alpha_e prod_(e∉U)beta_e prod_(v∈partial U)q_v; K(t,u)=sum_U[A_U+(-1)^t B_U]chi_U(u).`
- `k=B_empty=z prod_e beta_e, tau_e=beta_e^2; B_U/A_U=k/prod_(e∈U)tau_e.`
- `Equal normalized data pairs imply (TK')/K'=c(TK)/K; blockwise positivity gives c=1 and K'(t,u)=h(t)K(t,u).`
- `Write h(t)=a(1+x(-1)^t), |x|<1. Exact source multiplicativity gives 0=x k(1-x^2)(1-tau_e)(1-tau_h)(tau_e tau_h-k^2).`
- `k^2=tau_e tau_h[z^2 prod_(j∉{e,h})tau_j]<tau_e tau_h; hence x=0, K'=K, then lambda'=lambda and Q'=Q.`

**结论**

- 四个alpha已标定控制足以在该严格源族上全局唯一确定全部13参数及共同正Q。
- 源单项式约束消除两个控制轨道间的相对尺度；一般正K仍有该尺度歧义。

**复用边界**

- 未证明4个控制最少；不推广到多方面矩形、其他控制子集、D>=1或控制相关背景。
- 没有全局严格正核，不能用C23正核定理直接代替块间尺度证明。
- 无任意正数据可实现性/求解器/误差稳定性/物理校准结论。

**来源与审核状态**

- [原稿 · EM-DVR-BFF6DC](https://github.com/awdawmip/enterprise-math/blob/7d4a0ae3dea270ac60d9333e2a111a0117502d9a/research_notes/owner_goal_20261017/c26_rank_deficient_alpha_control_bff6dc/C26_ACTUAL_210_ALPHA_ONLY_CONTROL_GLOBAL_IDENTIFIABILITY_APPLIED_CONSUMER_V1.md)；blob `f29e482c9c0838187a5fed55f4910f12d0fd5a66`。
- [既有非作者技术审核 · EM-DIRECT-9F7A5C](https://github.com/awdawmip/enterprise-math/blob/7999e965fbdc52c95360d511adeb9587507ceb89/research_notes/owner_goal_20261017/reviews/c26_rank4_alpha_control_independent_9f7a5c/C26_ACTUAL_210_ALPHA_ONLY_CONTROL_GLOBAL_IDENTIFIABILITY_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；blob `171bf15f41fe6b5a4fed0e58b802b7e9f958ccdf`。

来源所载审核：`NONBLIND_PASS_BOUNDED_NEW_COMPLETE_TECHNICAL_WHOLE_SCOPE_ONLY`。此整理未改变原创建状态，未新增审核或Foundation/正式准入。

**方法与去重**：`RESULT_ONLY_STANDARD_APPLIED_COMPOSE`；普通工具库存入分类为 `RESULT_ONLY`，不新增Tool。采用 blockwise positive eigenvector uniqueness / source-monomial Möbius rigidity / strict-domain factorization。C23 full-span positivity theorem and its generic-K low-rank counterexample do not settle this restricted source-family case.

## FC-C26-IMAGE · C26 完整正数据的准确模型像与归一化恢复

**假设与定型**

- 有限非空标号Y和y0，已知逐元素严格正实矩阵T，d>=0，L>=1，互异已知非负整数n_j，二值控制b_j。
- V_jk=binom(n_j,k), k=0,...,d；H=[V b]；F为严格正、均匀平均1目标的指定非空子集，保留其全部原始限制。
- 实际模型P_j(y)=Q(y)K(y)[(TK)(y)/K(y)]^b_j prod_(k=1)^d D_k(y)^V_jk /Z_j，Q>0,sum Q=1,D_k>0,D_k(y0)=1，全部数据行严格正且完整归一化。

**公式**

- `C_j(y)=log(P_j(y)/P_j(y0)); E_H={C:C(:,y)∈col_R H for every y}.`
- `GOOD: b∉col_R V. Decompose C=Va+b h uniquely; R(y)=exp h(y); K_R is the unique mean-one positive eigenvector of diag(R^-1)T.`
- `GOOD exact image: P∈M_F iff C(P)∈E_H AND K_R∈F.`
- `BAD: b∈col_R V. Exact image: P∈M_F iff C(P)∈E_H, for EVERY chosen K∈nonempty F.`
- `For F_all=Pplus, codimension=(|Y|-1)(L-rank H). A good minimal L=d+2 schedule has NO unrestricted internal data constraint.`

**结论**

- 好日程给唯一K和全部规范化Q,D,Z恢复；源族成员条件必须另检。
- 坏日程允许每个既有目标以背景/漂移伪装；不保证秩亏漂移设计下nuisance唯一。

**复用边界**

- 完整正数据的存在/像结论，不是统计拟合、采样或参数lambda逆。
- 最小可辨识设计对F_all可接受任意完整正表，不构成该物理模型已被数据检验。
- |Y|=1是零维平凡情况。

**来源与审核状态**

- [原稿 · EM-DVR-BFF6DC](https://github.com/awdawmip/enterprise-math/blob/b61a68c6bbf114e8c133f4fcdd409f40092c1408/research_notes/owner_goal_20261017/c26_finite_image_consumer_bff6dc/C26_POSITIVE_DATA_IMAGE_AND_NORMALIZED_RECOVERY_APPLIED_CONSUMER_APPENDIX_V1.md)；blob `423f496e2a9d265ef19f2860d2210b863c71fb5a`。
- [既有非作者技术审核 · EM-DIRECT-9F7A5C](https://github.com/awdawmip/enterprise-math/blob/3ea127522735a25d5154e8114ed04c68531f2f5e/research_notes/owner_goal_20261017/reviews/c26_positive_data_image_independent_9f7a5c/C26_POSITIVE_DATA_IMAGE_NORMALIZED_RECOVERY_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；blob `a3a872f8fda8fb29740309378116ed3cb19a4f30`。

来源所载审核：`INDEPENDENT COMPLETE TECHNICAL WHOLE: PASS / ZERO REMAINING MUST-FIX`。此整理未改变原创建状态，未新增审核或Foundation/正式准入。

**方法与去重**：`RESULT_ONLY_STANDARD_COMPOSE`；普通工具库存入分类为 `RESULT_ONLY`，不新增Tool。采用 finite Perron positive-eigenvector existence/uniqueness / linear log-odds image / full nuisance/row-normalizer reconstruction。One author/peer pair is one result; do not count the two documents as two results.

## FC-C26-FIT · C26 无限制正族的投影最佳拟合、准确有符号对偶

**假设与定型**

- 有限非空标号Y和y0，已知逐元素严格正实矩阵T，d>=0，L>=1，互异已知非负整数n_j，二值控制b_j。
- V_jk=binom(n_j,k), k=0,...,d；H=[V b]；F为严格正、均匀平均1目标的指定非空子集，保留其全部原始限制。
- 实际模型P_j(y)=Q(y)K(y)[(TK)(y)/K(y)]^b_j prod_(k=1)^d D_k(y)^V_jk /Z_j，Q>0,sum Q=1,D_k>0,D_k(y0)=1，全部数据行严格正且完整归一化。
- 此条专用F_all=Pplus；好/坏日程均可。任意输入P是完整严格正归一化表，不先假定可实现。

**公式**

- `d_obs(P,R)=max_j osc_y log(P_j(y)/R_j(y)); nu(U)=max_j osc_y U_jy.`
- `Let E=C_rowconstant+{H A:A real}. delta_all(P)=min_(U∈E)nu(log P-U), attained by an actual strictly positive normalized model table.`
- `delta_all(P)=max_B <B,log P>, subject to sum_y B_jy=0, H^T B=0, (1/2)sum_(j,y)|B_jy|<=1.`
- `Equivalently in y0-zero log-odds coordinates: delta_all(P)=min_(C_R∈E_H)nu(C(P)-C_R).`

**结论**

- 每张正表在F_all上有实际正模型最优拟合，且准确等于有限有符号对偶证书最大值。
- 有符号证书是数学线性泛函；原模型概率/控制正性不变。

**复用边界**

- 对原受限F，delta_all只是下界，不能据此宣称受限最优值相等或取到。
- 未实现LP/顶点枚举求解器；无成本/统计噪声/物理结论。
- 最优表不必唯一；T和日程假设不得改为零核或未知控制。

**来源与审核状态**

- [原稿 · EM-DVR-BFF6DC](https://github.com/awdawmip/enterprise-math/blob/58b9e4ca2535377ee7b8ac0e931647fe2f95ea55/research_notes/owner_goal_20261017/c26_projective_best_fit_consumer_bff6dc/C26_EXACT_PROJECTIVE_MODEL_DISTANCE_SIGNED_DUAL_AND_POSITIVE_BEST_FIT_APPLIED_CONSUMER_V1.md)；blob `b1d22ddc83a53309cef6df9dac812a889d03c14f`。
- [既有非作者技术审核 · EM-DIRECT-9F7A5C](https://github.com/awdawmip/enterprise-math/blob/a587a915cd2a00a67c31ed7f2477a1a6dfb7d30b/research_notes/owner_goal_20261017/reviews/c26_projective_best_fit_independent_9f7a5c/C26_EXACT_PROJECTIVE_DISTANCE_DUAL_AND_POSITIVE_BEST_FIT_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；blob `5f83fb282b8fb0da2850b1da7862be4bc0a796ec`。

来源所载审核：`INDEPENDENT COMPLETE TECHNICAL WHOLE: PASS / ZERO REMAINING MUST-FIX`。此整理未改变原创建状态，未新增审核或Foundation/正式准入。

**方法与去重**：`RESULT_ONLY_STANDARD_COMPOSE`；普通工具库存入分类为 `RESULT_ONLY`，不新增Tool。采用 finite quotient norm / finite minimizer compactness after row gauge / finite signed duality。Distance to unrestricted image differs from inverse stability between two admissible targets.

## FC-C26-INVERSE · C26 固定正控制下两个可容许目标的投影逆界

**假设与定型**

- 有限非空标号Y和y0，已知逐元素严格正实矩阵T，d>=0，L>=1，互异已知非负整数n_j，二值控制b_j。
- V_jk=binom(n_j,k), k=0,...,d；H=[V b]；F为严格正、均匀平均1目标的指定非空子集，保留其全部原始限制。
- 实际模型P_j(y)=Q(y)K(y)[(TK)(y)/K(y)]^b_j prod_(k=1)^d D_k(y)^V_jk /Z_j，Q>0,sum Q=1,D_k>0,D_k(y0)=1，全部数据行严格正且完整归一化。
- GOOD日程b∉col V，固定w满足w^T V=0,w^T b=1。
- 比较同一原始F中两个实际存在的目标K,K'及其完整模型表P,P'；同一已知T/日程，Q,D,Z可不同。

**公式**

- `r_K=(TK)/K; d_H(f,g)=osc log(f/g).`
- `d_H(r_K,r_K')<=||w||_1 d_obs(P,P').`
- `m=min_ij T_ij>0; M=max_ij T_ij; c=(m/M)^2; d_H(K,K')<=c^(-1)d_H(r_K,r_K').`
- `Hence d_H(K,K')<=(M/m)^2||w||_1 d_obs(P,P').`

**结论**

- 给同一固定正T的两实际端点定量逆界，不需要在F中额外假设连接路径。
- 原稿以F_all两状态T_epsilon例排除对所有正T统一的模量。

**复用边界**

- 不证明任意数据有目标、不判F成员、不恢复lambda、不保证最佳拟合。
- 非统一反例是F_all例，不得声称对每个受限F均失败。
- 坏日程无该w；T接近零元素时常数可恶化。

**来源与审核状态**

- [原稿 · EM-DVR-BFF6DC](https://github.com/awdawmip/enterprise-math/blob/ac5b85b8d12ee4e94dccacb129201b65f82a331c/research_notes/owner_goal_20261017/c26_target_inverse_reuse_bff6dc/C26_TARGET_K_PROJECTIVE_INVERSE_REUSE_WORKING_INTERFACE_LEDGER_V1.md)；blob `c58b6b0a5abaca243fb9581d35de277b9fa694eb`。
- [既有非作者技术审核 · EM-DIRECT-9F7A5C](https://github.com/awdawmip/enterprise-math/blob/9cd54d20a8c501561f081b95015a8aa7a24fa9cc/research_notes/owner_goal_20261017/reviews/c26_target_inverse_reuse_independent_9f7a5c/C26_TARGET_K_PROJECTIVE_INVERSE_REUSE_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；blob `191e48cbc47322e39768b325d7166c534a87ab20`。

来源所载审核：`INDEPENDENT COMPLETE TECHNICAL WHOLE: PASS / ZERO REMAINING MUST-FIX`。此整理未改变原创建状态，未新增审核或Foundation/正式准入。

**方法与去重**：`REUSE_STANDARD_COMPOSE_FIRST_PERSISTED_WORKING_INTERFACE`；普通工具库存入分类为 `RESULT_ONLY`，不新增Tool。采用 observable nuisance-canceling contrast / fixed positive-kernel Hilbert contraction / oscillation inverse estimate。First faithful persistence of an older private conditioning route; not new discovery or a new tool family.

## FC-C26-CLOSURE · C26 原受限族的相对闭包与实际最佳拟合取到

**假设与定型**

- 有限非空标号Y和y0，已知逐元素严格正实矩阵T，d>=0，L>=1，互异已知非负整数n_j，二值控制b_j。
- V_jk=binom(n_j,k), k=0,...,d；H=[V b]；F为严格正、均匀平均1目标的指定非空子集，保留其全部原始限制。
- 实际模型P_j(y)=Q(y)K(y)[(TK)(y)/K(y)]^b_j prod_(k=1)^d D_k(y)^V_jk /Z_j，Q>0,sum Q=1,D_k>0,D_k(y0)=1，全部数据行严格正且完整归一化。
- GOOD日程；barF是F在Pplus={K>0,mean K=1}内的相对闭包，绝不加入零目标。

**公式**

- `closure_(positive complete tables)M_F=M_barF.`
- `For every positive P: delta_F(P)=min_(R∈M_barF)d_obs(P,R).`
- `F relatively closed in Pplus iff M_F relatively closed iff EVERY positive complete P has an actual optimal fit in M_F.`
- `For one fixed P: attainment in F iff some nearest table in M_barF has recovered target in F.`

**结论**

- 准确区分下确界值、正相对闭包中的最优表和原族是否真正取到。
- 坏日程另有每个非空F都同像E_H、每张正表均有最佳拟合的结论，不能套好日程闭包充要。

**复用边界**

- 相对闭不等于紧；最优表可不唯一。
- 未由抽象定理判实际lambda族闭性；实际C22族非闭及不取到由FC-C22-FAMILY另供。
- 不提供定量两模型逆界或受限最优值的无限制有符号对偶计算。

**来源与审核状态**

- [原稿 · EM-DIRECT-9F7A5C](https://github.com/awdawmip/enterprise-math/blob/3aac62eaf614e2fa00ac6c21890a94cef8072260/research_notes/owner_goal_20261017/c26_restricted_fit_closure_9f7a5c/C26_RESTRICTED_TARGET_RELATIVE_CLOSURE_AND_ACTUAL_BEST_FIT_ATTAINMENT_AUTHOR_COMPOSE_APPENDIX_V1.md)；blob `ba20fbe7776898854cb8549238d299c73aef09bf`。
- [既有非作者技术审核 · EM-DVR-BFF6DC](https://github.com/awdawmip/enterprise-math/blob/71d999a4df543940234f52376dbc8c860e4e4d35/research_notes/owner_goal_20261017/reviews/c26_restricted_fit_closure_nonauthor_bff6dc/C26_RESTRICTED_TARGET_CLOSURE_AND_ATTAINMENT_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；blob `d44ac81cf20a991d80f7eb4d489d9fb629660be5`。

来源所载审核：`NONBLIND_PASS_BOUNDED_NEW_COMPLETE_TECHNICAL_WHOLE_SCOPE_ONLY`。此整理未改变原创建状态，未新增审核或Foundation/正式准入。

**方法与去重**：`RESULT_ONLY_STANDARD_APPLIED_COMPOSE`；普通工具库存入分类为 `RESULT_ONLY`，不新增Tool。采用 finite log-odds isometry / fixed-positive-T strip compactness / relative closure and distance attainment。Abstract arbitrary-F result and actual source-family application remain different scopes; do not circularly count their premise reviews.

## 已有接口的依赖与重复边界

- M0->FC-C26-IMAGE->FC-C26-FIT->FC-C26-CLOSURE
- FC-C26-IMAGE->FC-C26-CLOSURE
- M0->FC-C26-INVERSE (no image/fit premise)
- FC-C22-FAMILY supplies actual membership/strict inverse; abstract closure then applies with its original domain.
- FC-C25-KNOWN-R and FC-C25-UNKNOWN-R retain different rate hypotheses and support counts.

[C26现有四接口与去重ledger](https://github.com/awdawmip/enterprise-math/blob/d1767a81ee853c21f7d700bcc64318b960808e81/research_notes/owner_goal_20261017/c26_reusable_interfaces_9f7a5c/C26_ACCEPTED_FINITE_INTERFACES_AND_DEDUPLICATION_WORKING_LEDGER_V1.md)已经将 I/II/III/IV 分成四个结果；作者与审核共八篇文档不能计作八项成果。上述四个接口在此按原范围重建可检索入口，不重命名为新工具。

读取范围：C22实际族/C23/C24/C25、未知r、210秩4原稿全文用于文献提取；C26原稿读取相应定理定义与公式章节，余边界复用既有ledger；审核文档读取处置、作用域及所需公式。完整源文已取回，实际阅读范围保存在 JSON 的 `curation_read_scope`；这不是新的全稿技术审核。未重验旧代码、表格、日志、统计或物理证据。

