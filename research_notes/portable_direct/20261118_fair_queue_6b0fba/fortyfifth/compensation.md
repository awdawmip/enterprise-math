# 第二阶段的素理想补偿、重窗代价与临界抵消

研究任务 RS-OAI7-003-D-20261007-6F2A81。取 \(F=\mathbb Q(\sqrt{-3})\)，\(p\) 始终指素理想，其主生成元满足 \(p\equiv1\bmod3\)，\(Q=q_p=Np\)。首要的算术结论是主行二项补偿的首误差恰为 \(\eta(p)Q^{-s}\)，在主角色实轴样本上保持同号到首阶。若让窗口交叠，并仍要求不同槽标记不同素理想，就出现另一项有明确常数的计数损失。两者在一个宽度为 \(1/\log P\) 的过渡区相遇。原稿用互不相交的窗口，计数损失精确为零。[登记题书](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_tasks/RS-OAI7-003-D-20261007-6F2A81.md) · [冻结外稿的两阶段](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L165-L194)

## 1　两套归一化和最紧的已列余量

|外稿量|阶段 I|阶段 II|
|---|---|---|
|几何 \((l_x,l_y,h,\ell)\)|\((1/2,1/2,1/2,0)\)|\((17/48,23/48,13/16,1/6)\)，\(l_y-l_x=1/8\)|
|位移及低界基准|\(C_{\mathrm I}(s)=s-2/3,\ C_{\mathrm I}(11/12)=1/4\)|\(C_{\mathrm{II}}(s)=s-11/16,\ C_{\mathrm{II}}(7/8)=3/16\)|
|物理探针|\(I_\eta(Z^{1/2},Z^{1/2},Z)/c_S\)|有限标记与缩放的交替和 \(I_{\eta,\mathrm{modified}}/(c_S A_T)\)|
|主行与余项共用的标量|\(c_S>0\)|\(c_S A_T\)，\(A_T=(-1)^K Z^{-\ell/6}\prod_i S_i,\ S_i=\sum_{p\in1_T,\ p\notin S} W_i(Q/P_i)Q^{-5/6}\)|
|未支付可调损失的 \(w,z\) 余量|\(1/40,\ 1/1200\)|\(23/960,\ 13/9600\)|

\(T\) 是固定射线类群的有限商，\(1_T\) 为恒等类。原截断、目标 \(\eta\) 的定义模以及 \(S\) 在各自阶段固定，阶段间可以不同。同一 \(S,\eta\)、同一高斯及同一 \(H_\eta/L_F^S\) 时，两个形式 Mellin 信号相差已知的 \(Z^{-1/48}\)。物理探针仍须分别证明低侧界和与各自信号之差的界。原稿阶段 I 的其余表列余量为中段 \(1021/25000\)、小行 \(43/300\)、大行 \(>1\)；阶段 II 设 \(0<\Delta=\beta_*-7/8\le1/24\)，是原稿反证的参数范围。[I 的余量表](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L6494-L6514) · [II 的有限探针](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L6834-L6914)

原几何取固定偶数 \(K\)，\(P_i=P=Z^{\ell/K}\)，在 \((1,2)\) 内选 \(K\) 个有正间距的光滑窗。因 \(2\ell/K<1/185\)，必有 \(K\ge62\)。其直接低界余量为 \(\Delta\)。令 \(\omega=\Delta/2\)，还有正余量。原稿定下 \(m_{\rm hi}=51\Delta/64,\ m_{\rm small}=63/800,\ m_P=7/(96K)\)。于是 \(m_{\rm hi}<m_{\rm small}\) 且 \(m_P<13/9600<23/960\)。原末段给全部高侧分项预留、尚未处理目标依赖高度前的共同数精确简化为
\[
 m=\tfrac14\min\{51\Delta/64,\ 7/(96K)\},\qquad
 \Delta_{\rm switch}=14/(153K).
\]
网格和矩损失可要求 \(K\) 比 62 更大。仅就三项主轮廓余数，给定共用损失 \(\epsilon\ge0\)，三个指数严格低于 \(C_{\rm II}(\beta_*)\) 等价于
\(0<e<\min\{(23/960-\epsilon)/(1+h),13/9600-\epsilon,m_P-\epsilon\}\)，并须满足独立的检测宽度条件。固定几何和正 \(m\) 先于目标，具体高度、常数和起始尺度可依赖目标。这个算术化简使用原稿给的余量，未重新证明产生各项余量的分析估计。[主行余项](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L15633-L15681) · [小行余量](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L15889) · [最终参数顺序](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L16231-L16363)

中心差分使用另一个精确抵消。固定两张矩形的同一分配 \((\mathfrak b_1,\mathfrak b_2)\)、共同角色、掩码、高度 \(t\) 和逐坐标剖面。令 \(U_i=X_i/q_{\mathfrak b_i},\, V_i=Y_i/q_{\mathfrak b_i},\ U_1U_2=V_1V_2=T_0\)。乘积格点主项在两边都是 \(c^2T_0^{1+it}I_1(t)I_2(t)\)，故逐分配相减为零。原稿给 \(U_i,V_i\ge Z^r,\ r\ge0\) 时，除以 \(\sqrt{T_0}\) 后的误差为 \(O(Z^\epsilon(1+|t|)^{2J}\sqrt{T_0}Z^{-r})\)。一个共同的、只依赖外部素理想元组的互异掩码可以乘在此恒等式两边。若两边改用不同掩码或不同剖面矩，相等的乘积长度单独不能保证抵消。[冻结中心差分](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L14545-L14599)

## 2　主行局部因子的第一项

在 \(u=1,\ w=1,\ z=1/6\) 的主行留数处，记 \(\sigma=\Re s\ge7/8\)，\(\alpha(p)=p/|p|\)，并置
\[
 h_p=Q^{-1},\quad d=\eta(p)Q^{-s},\quad R=\bar\alpha(p)^6\eta(p)^6Q^{3-6s},
 \quad J=1-h_pR-(1-h_p)d.
\]
仅在本节以下公式简记 \(h=h_p\)。把外稿的 \(j=0,\rho=1,V=W=h,D=d\) 代回原表得
\[
 P_p^*=(1+h)(R-d)/(1-R),\quad
 P_p=(1+h)J/((1-h)(1-R)),\quad
 \delta_p:=-\mathcal B_p-1
 ={(1-h)[(1-h)d-R/d+hR]\over J}.                                      \tag{1}
\]
具体地，\(P_p^*\) 括号中带 \(1/(1-V)\) 的项是 \(R-dh\)，另两项是 \(-d+hR\)。再用 \(\mathcal B_p=d^{-1}P_p^*/P_p-h\) 即得。充分大的好素理想上 \(|J-1|\ll Q^{-\sigma}+Q^{2-6\sigma}\)，所以
\[
 \delta_p=d+O\!\left(Q^{-\sigma-\min\{1,\sigma,4\sigma-3\}}\right).       \tag{2}
\]
此界对高度及目标单位相位一致，因为 \(|R/d^2|=Q^{3-4\sigma}\)。原稿主行的 \(O(Q^{-7/8})\) 因而有可提取的一阶系数。主角色、实 \(s=\sigma\) 的 \(\Re\delta_p\sim Q^{-\sigma}>0\)，仅靠重新估计绝对值不能去掉它。此处读的是乘性主行修正，即使同一 \(s\) 处标量 \(1/L_F^S\) 恰为零，该局部恒等式仍成立。[局部变量及表](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L3857-L3868) · [冻结原表](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L4007-L4046) · [原主行近似](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L9048-L9080)

## 3　不同理想分配和相同主信号的代价

允许各槽支持交叠，**明确把原物理和限制到两两不同的素理想元组**。这样每个被选局部因子仍只替换一次，并保持原标记项和原缩放项。一般轮廓下先按不同元组取 \(\prod_{\rm selected}Q^{z-1}W_iG_p\prod_{\rm unselected}H_p\) 的有限和，可在 \(H_p\) 零点使用。只在已保证局部 \(H_p\ne0\) 的主行读取 \(G_p/H_p\)。在重复素理想上直接相乘两个 \(G_p/H_p\) 缺少原模型依据，例如重复标记 \(1_{p\mid A}^2=1_{p\mid A}\)。[冻结逐元组替换及全纯表达式](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L8651-L8744)

写 \(a_i(p)=W_i(Q/P_i)Q^{-5/6}, S_i=\sum a_i>0,\ \mu_i=a_i/S_i\)。独立取 \(p_i\sim\mu_i\)，\(\mathcal D\) 表示两两不同，\(D_K=\Pr(\mathcal D)\)。对任意复权 \(v_i\) 有分割格公式
\[
 \sum_{\mathcal D}\prod_i v_i(p_i)=
 \sum_{\Pi\vdash[K]}\ \prod_{B\in\Pi}
 \left[(-1)^{|B|-1}(|B|-1)!\sum_p\prod_{i\in B}v_i(p)\right].              \tag{3}
\]
这是对指标相等分割的 Möbius 反演，等价地展开置换并按循环分块。单元素块的 Möbius 系数为 1，其块内求和仍为该槽的权之和。原先不交的各槽只留下单元素分割。计算也可在 \(x_i^2=0\) 的代数中取 \(\prod_p(1+\sum_i v_i(p)x_i)\) 的 \(x_1\cdots x_K\) 系数，在 \(N\) 个候选理想上用 \(O(NK2^K)\) 次环运算和 \(O(2^K)\) 个环元素；同窗可改为 \(K!\) 倍初等对称函数并以 \(O(NK)\) 次运算完成。

以 \(v_i=\mu_i\)、\(v_i=\mu_i(1+\delta_p)\) 代入，分别得 \(D_K\) 和
\(\Sigma=\mathbb E[1_{\mathcal D}\prod_i(1+\delta_{p_i})]\)。对应的主行修正精确为 \(H_\eta(s)(-1)^K(\prod S_i)\Sigma\)。互异校准必须取 \(A_T^\ne=A_T D_K\)，非零当且仅当各正权支持满足 Hall 条件。若 \(|\delta_p|\le b_i\) 在第 \(i\) 槽上成立，则
\[
 |\,\Sigma/D_K-1\,|\le\prod_i(1+b_i)-1\qquad(D_K>0).                     \tag{4}
\]
证明是对已互异的分配作条件平均。任一未经归一化的**绝对**高低侧误差，在还原到同一主信号时则要除以 \(|c_S A_T|D_K\)。相对局部插入误差 (4) 不付第二次 \(D_K^{-1}\)。互不相交时 \(D_K=1\) 严格成立。对改过的物理和，动态非主行、移动掩码及二次矩仍须另证；一般元组和已经失去原产品分解。

## 4　固定槽数的临界线和射线角色

以下各槽同尺度 \(P\to\infty\)，\(K,T,S,\eta\) 及非负非零剖面固定。令 \(f_i(y)=W_i(y)y^{-5/6}\)，\(F_i=\int f_i\)，
\[
 C=|T|\sum_{i<j}\frac{\int f_i f_j}{F_i F_j},\qquad L=\log P .
\]
固定射线类的素理想定理及分部积分给出 \(\max_{p,i}\mu_i(p)\ll L/P\)，以及
\[
 D_K=1-C\,L/P+o(L/P).
\]
事实上两槽碰撞概率为 \(\sum_p\mu_i(p)\mu_j(p)\)，同时发生两个不同碰撞的概率为 \(O_K((L/P)^2)\)。相交的两条边需要三槽同理想，不相交的两条边独立。此证明允许不相同的窗口。若 \(C=0\)，由光滑非负性，所有不同槽的正权支持两两不交，\(D_K=1\)。

取 \(s=\sigma(P)+it,\ \sigma(P)=1-(\log L+c)/L\)，\(t,c\) 固定。用共同有限射线群 \(\mathcal G\twoheadrightarrow T\) 实现 \(\eta\)，令 \(\kappa=1_{\eta|_{\ker(\mathcal G\to T)}=1}\)。有
\[
 \boxed{\displaystyle
 \Sigma-1={L\over P}\left[
 e^cP^{-it}\kappa\sum_i{\int f_i(y)y^{-1-it}\,dy\over F_i}-C
 \right]+o(L/P).}                                                       \tag{5}
\]
将 (2) 代入 (3)，所有含两个局部误差或同时含碰撞和局部误差的项均为 \(O_K((L/P)^2)\)，局部首项之外的余量由 (2) 给出 \(o(L/P)\)。给定 \(p\in1_T\)，角色在核上的平均恰为 \(\kappa\)；对核上各固定类分别使用素理想定理，且 \(y^{-\sigma(P)}\to y^{-1}\) 在固定环带均匀，即得 (5)。因此不能把任意目标 \(\eta\) 在 \(1_T\) 的值预设为 1。式 (5) 的实轴主角色版本比较的正、负项分别是原补偿留下的 \(d\) 和剔除同理想的概率。若 \(C>0\)，\(7/8\le\sigma<1\) 固定时前者主导，\(\sigma\ge1\) 固定时后者主导；主插入常数为 \(\sum_i\int f_i y^{-\sigma}/F_i\)。改用 \(A_T^\ne\) 校准可恰好消除后一种主偏差。[固定射线正规化](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L7004-L7041) · [Thorner–Zaman 固定扩张的 Chebotarev 定理](https://doi.org/10.2140/ant.2019.13.1039)

**精调之后的符号。** 当 \(K\ge2,\ f_i=f,\ \operatorname{supp} f\subset(1,2),\eta=1,t=0\)，设 \(F=\int f,\ E=K\int f/y\,/F,\ m_j=\int f^j\log y/\int f^j,\ m_-=\int(f/y)\log y/\int(f/y)\)。取 \(e^c E=C\) 使 (5) 的主系数消去，仍有
\[
 \Sigma-1=\frac C P\big[(\log L+c-1)m_-+m_2-m_1\big]
             +O\!\left(\frac{(\log L)^2}{PL}\right).
\]
固定类域的有效素理想定理在固定环带上给比任意 \((\log P)^{-A}\) 更小的相对余项，固定可能例外实零的项亦可吸收。分别展开素理想密度 \((L+\log y)^{-1}\) 以及 \(y^{(\log L+c)/L}\)，插入项的相对二阶系数为 \((\log L+c-1)m_-+m_1\)，两槽碰撞的为 \(2m_1-m_2\)。多重碰撞和 (2) 的余项均比所列误差小。因此在调平处最终仍有正偏差 \(C m_-\log\log P/P\)。这一精度需要有误差率的固定域素理想定理，仅靠无率的 \(\sim\) 不足。

**理想键与范数键。** 若 \(L_T/F\) 是上述 \(T\) 对应的类域，\(M=L_T\overline{L_T}\)，按相同有理范数剔除两槽会把 \(C\) 改为
\[
  C_{\mathrm{norm}}=(1+[M:L_T]^{-1})C .
\]
在 Eisenstein 域，额外删除只能来自一个分裂有理素数的两个共轭理想。该对均在 \(1_T\) 等价于其中一个理想在 \(M/F\) 完全分裂；固定域 Chebotarev 给出密度 \(1/[M:F]\)，而原恒等类为 \(1/|T|\)。按有序对计数时每枚满足的素理想恰对应其另一个共轭理想。惰性素理想范数是有理素数的平方，在 \(Q\asymp P\) 中只有 \(O(\sqrt P)\) 枚，分歧及固定排除都是有限的。若 \(L_T=\overline{L_T}\)，错误的碰撞主项恰好翻倍。

## 5　同窗多槽的算术生日阈值

只在本节将各 \(f_i=f\) 固定而允许槽数增长；这是一项独立的互异校准问题。记 \(\mu\) 为归一化槽律，\(s_j=\sum_p\mu(p)^j\)，\(a=|T|\int f^2/(\int f)^2\)。固定类素理想定理给
\(s_2\sim a L/P,\ s_3\ll(L/P)^2\)。取独立槽，\(V\) 为相同理想的无序槽对数，\(\lambda=\binom K2s_2\)。重合对事件只与含有共同槽的其他重合对相依。Chen–Stein 零计数界给
\[
 |D_K-e^{-\lambda}|
 \le\min(1,\lambda^{-1})\binom K2\big[(2K-3)s_2^2+2(K-2)s_3\big]\qquad(K\ge2).
\]
此式由每条边的 \(2K-3\) 个含自身邻边，以及 \(2(K-2)\) 个异邻边的三重相同事件得到。若 \(K^2 L/P\to v<\infty\)，则 \(D_K\to e^{-av/2}\)。若该比值趋无穷且 \(P\to\infty\)，由 \(\operatorname{Var}V\le\lambda+6\binom K3s_3\) 及 Chebyshev 得 \(D_K\to0\)。有限阈值区 \(K P^{-7/8}\to0\)，按 (4)，全局部插入对互异首信号的相对误差也趋零。[Arratia–Goldstein–Gordon 的局部相依界，定理 1](https://doi.org/10.1214/aop/1176991491)

沿用 \(P=Z^{\ell/K}\) 的尺度关系，令 \(B=\ell\log Z\)，若
\(\log P=\operatorname W(B^2)+u+o(1)\)，其中 \(\operatorname W(x)e^{\operatorname W(x)}=x\)，那么
\[
 K^2 L/P=B^2/(Le^L)\longrightarrow e^{-u},\qquad
 D_K\longrightarrow \exp[-a e^{-u}/2].
\]
故选择 \(K\sim B/(2\log B)\) 只描述阈值的量级，固定 \(u\) 才确定同一主信号需付的确切常数。原稿选择固定 \(K\)、不同窗口，始终 \(D_K=1\)。这里没有为变化的槽数提供原稿轮廓、探测矩或目标族的统一估计。

## 6　真射线与局部因子的有限核算

取模 \(36\mathcal O_F\) 的完整射线群，阶 \(36^2(1-1/4)(1-1/3)/6=108\)。主生成元 \(a+b\omega\) 在恒等类恰当 \(a\equiv1,\ b\equiv0\bmod36\)。取 \(P=3500\)，在 \(P<Q<2P\) 恰有
\[
 (-35,-72,3889),\quad(37,72,3889),\quad(-71,0,5041),\quad
 (-71,-72,5113),\quad(1,72,5113).
\]
第三枚来自惰性有理素数 71，另外两对分别共轭。对四槽依次取 \(f_i=1,y,2-y,1+y\) 在这五枚理想上赋值，可乘以一个固定光滑非负窗，使其在全部样本点等于 1 而在 \((1,2)\) 外为零，再取 \(W_i=y^{5/6}f_i\)。则
\(D_4=7569798168/39029588125\approx0.193950245\)。若只看三个范数便误得零。在 \(s=1\) 处，以 (3) 或逐一枚举所得 \(\Sigma/D_4-1\)，主角色约 \(0.00088354346\)，范数拉回的模 5 二次角色约 \(0.00025941798\)；完整有理分数随附。结果表的 distinct_vs_independent_weight 是 \(D_4\)，inserted_divided_by_distinct 是 \(\Sigma/D_4\)，两者乘积才是式 (5) 中的 \(\Sigma\)。小样本的非零不判定渐近角色平均。

脚本按 \(Q=a^2-ab+b^2\) 枚举完整主生成元，原 \(j=0\) 表和无分母 \(G_p\) 的算式对照 (1)，在 \(s=1,2\)、两角色、五素理想上共核 20 项。在 \(K=1,2,3,4\) 的带插入和纯计数上用分割格与直接有序互异指派交叉核 32 次。另在四个尺度用初等对称函数精确计算同窗无碰撞概率，最大 \(P=200000\) 有 144 枚素理想、73 个范数，\(K=11\) 的真概率约 \(0.664558\)，Poisson 对照约 \(0.671076\)。这些样本检验有限恒等式；绝对收敛、矩估计及外稿的准黎曼结论维持各自的原证据范围。一个具体未决问题是能否在保留 \(D_K\) 收益的同时，对非主行给出同样适用的互异加权矩界。[程序](compensation_check.py) · [精确核算摘要](compensation_checked.json) · [第十五轮同一行的联合矩](../fifteenth/joint.md) · [第二十八轮 Mellin 接口](../twentyeighth/mellin.md) · [第三十六轮假设零带的推论](../thirtysixth/zero_strip.md)

在笔记所在目录运行 python3 compensation_check.py 即可重现随附 JSON。
