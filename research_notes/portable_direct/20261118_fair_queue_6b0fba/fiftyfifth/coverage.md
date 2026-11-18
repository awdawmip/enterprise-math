# 共同位移法则的残基名单与覆盖阈值

**RS-OAI7-028-C-20261007-6F2A81。** 有限剩余群上的覆盖转移可以从一个共同检查点的条件位移法则直接证明。若能控制该法则透露的起点信息，源证明用于估计命中次数的独立重采样可以省去。只关心某个有符号坐标子集时，甚至只需计算该子集名单与起点投影的互信息。下述结论逐项列出更换预算所需的输入。[登记题书](https://github.com/awdawmip/enterprise-math/blob/baa2e081153260c7659466b4fa186ff308a7b0d9/research_tasks/RS-OAI7-028-C-20261007-6F2A81.md) · [冻结外稿的覆盖定理与证明](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex)

## 一、一个晚检查点，所有坐标共用

外稿固定一条步道和早检查点 \(A_i=a_0\) 的确切时间，以新随机性向前推进到 \(A=A_{i+1}\)，记 \(Y=z_A=y(A)\)。再次从这个**确切时间**继续，至统一终时 \(t_*\)，位移 \(h=z_{t_*}-Y\) 的条件法则是 \(\nu_A\)。末尾还有一段加在共同时间上的独立均匀偏移。每次固定 \(a_0\) 就得到一个单独的混合实验；后向归纳沿检查点编号进行，实际续走均向前。下文只需有限 \(A\)、有限支撑 \(\nu_A\)，和同一实物位移在各坐标的投影。令 \(B=\nu_A,\ Z=Y+h\)。在格 \(\Lambda\) 上有 \(2k\) 个具名同态 \(\phi_c:\Lambda\to G_c\)，\(c=(j,\pm)\)，\(|G_c|=p_j\in[T,2T]\)。独立均匀选 \(s\) 个不同指标，每个再独立选一个符号，得 \(S\)。写 \(X_c=\phi_c(Y), F_S=(X_c:c\in S)\)，\(\bar L=k^{-1}\sum_j\log p_j\)。全文熵用自然对数。第 24 轮 D 处理的是固定同一终时下的跨批信息总账，第 46 轮 E 研究具有绕行位移的图投影纤维。以下直接处理 C 的概率地板和低概率残基个数。[源随机时刻](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/schedule.tex#L49-L93) · [固定早时刻后向归纳](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/schedule.tex#L447-L485) · [第 24 轮](../twentyfourth/budget.md) · [第 46 轮](../fortysixth/paths.md)

覆盖 \((\tau,\beta)\) 的原定义为 \(\#\{v:\Pr(\phi_c(Z)=v)<\tau/p_c\}<p_c^{1-\beta}\)。源的范围是 \(0<\tau\le3/8,\ 0<\delta\le1/64,\ \tau'=\tau+4\delta,\ 0<\beta'\le\beta<1,\ 0<\eta\le1,\ 0\le\eta'\le1\)。对每个支持内的 \(a\)，至多 \(\eta'\) 比例的坐标没有条件 \((\tau',\beta')\) 覆盖。例外坐标及其中的残基都可随 \(a\) 变化。源取 \(n\) 次给定 \(A\) 后条件独立的足迹 \({\cal H}=(h_1,\ldots,h_n)\)，要求
\[
\begin{gathered}
 \mathbb E_S H(F_S)\ge(1-\epsilon)s\bar L,\qquad
 H({\cal H})\le\kappa s\bar L,\qquad
 \eta'\le\eta\delta/100,\quad \epsilon+\kappa\le\eta\delta\beta'/16,\\
 p\,\exp(-\delta^2 n p^{-\beta}/2)\le\delta/100,\quad
 \delta^{-1}<p^{\beta'/2},\quad \log(2e/\delta)\le(\beta'/4)\log T .
\end{gathered}
\]
真残基入经验名单用共同边际和 Markov；名单过大事件用给定 \(A=a\) 后的二项下尾，再对 \(p\) 个候选作并界。后一步产生上述含 \(n\) 的条件。其余熵账只对这一整份数据扣一次。

## 二、确定性重叠计数与信息下界

若无条件混合覆盖失败，在该坐标取低质量集内固定的 \(K_c\)，大小 \(u=\lceil p^{1-\beta}\rceil,\ p=p_c\)。选择 \(K_c\) 依据混合分布，与单次实现及 \(S\) 的抽样无关。任取 \(\tau<t<\tau'<1\)。在每个 \(B\) 上记 \(b_c=(\phi_c)_*B\)，定义
\[
 L_c(B)=\{x\in G_c:b_c(K_c-x)\le t u/p\},\quad
 e_p=\lceil p^{1-\beta'}\rceil-1,\quad
 m_p=\min\!\left(p,\left\lfloor\frac{u e_p}{\lceil(1-t/\tau')u\rceil}\right\rfloor\right).
 \tag{1}
\]
由于 \(\mathbb E[b_c(K_c-X_c)]=\Pr(\phi_c(Z)\in K_c)<\tau u/p\)，Markov 给出真残基入名单的概率至少 \(1-\tau/t\)。固定一个条件覆盖良好的 \(a,c\)。平移 \(y(a)\) 后，位移法则有至多 \(e_p\) 个例外残基 \(E=\{v:b_c(v)<\tau'/p\}\)。名单成员必须满足 \(|(K_c-x)\cap E|\ge\lceil(1-t/\tau')u\rceil\)。对全体 \(x\) 求和恰为 \(u|E|\)，故 \(|L_c|\le m_p\)。这里没有随机抽样尾项。选 \(t=\sqrt{\tau\tau'}\) 会最大化两个比例 \((1-\tau/t)(1-t/\tau')\) 的乘积，实际熵界还可逐个 \(t\) 计算。

把大于 \(m_p\) 的名单替换为空集，得 \(D_c\)；已达标坐标可置空。设失败坐标比例 \(\theta>0\)。在失败坐标中均匀选 \(c\)，与原实验独立，定义
\[
 a_*=\Pr(X_c\in D_c),\qquad b_*=\mathbb E(|D_c|/p_c).
\]
在每个 \(A\) 最多 \(\eta'\) 比例的坐标条件覆盖失败，因而
\[
 a_*\ge 1-\tau/t-\eta'/\theta,\qquad
 b_*\le\max_c m_{p_c}/p_c .
 \tag{2}
\]
以 \(d(a\Vert b)\) 表示二元相对熵（连续端点按惯例取值）。真实实验的参照分布保留同一个 \(c,D_c\)，再独立选 \(G_c\) 上的均匀残基。两者相对熵恰为失败坐标平均 \(\log p_c-H(X_c\mid D_c)\)。只读事件“残基在名单内”，数据处理给出下界 \(d(a_*\Vert b_*)\)。每个固定 \(S\) 有
\[
 H(F_S)-I(F_S;D_S)=H(F_S\mid D_S)
 \le\sum_{c\in S}H(X_c\mid D_c),\qquad D_S=(D_c:c\in S).
\]
各坐标入选率相同，其余坐标熵亏非负。因此精确必要条件为
\[
 \boxed{\quad
 \theta\,d(a_*\Vert b_*)\ \le\
 \bar L-\frac1s\mathbb E_S H(F_S)
       +\frac1s\mathbb E_S I(F_S;D_S).\quad}
 \tag{3}
\]
若 \(a_0=1-\tau/t-\eta'/\eta>b_0=\max_c m_{p_c}/p_c\)，且 (3) 右端至多 \(\eta d(a_0\Vert b_0)\)，则 \(\theta\le\eta\)，因为 \(\theta>\eta\) 时二元相对熵在相应区间的单调性给出矛盾。\(b_0=0<a_0\) 时由空名单直接矛盾，无需熵预算。可预先用 \(\mathbb E_S I(F_S;B)\) 作上界，或只留下所有有关的位移边际法则；这也避免事先得知哪些坐标失败。\(D_S\) 只是对同一套实验的投影，整个联合分布在选 \(S\) 前已固定。

**沿用源中的其余常数。** 取 \(t=\tau+\delta\)。此时 \(1-t/\tau'\ge\delta\)，故在源的尺寸条件下 \(m_p<p^{1-\beta'/2}\)。假设 \(\theta>\eta\)，由 (2) 有 \(a_*\ge\delta/2\)。二元熵 \(h_2\) 给
\(d(a_*\Vert b_*)\ge a_*(\beta'/2)\log T-h_2(a_*)\ge(\delta\beta'/8)\log T\)，使用 \(h_2(a)\le a\log(e/a)\) 和源的对数条件。又 \(\bar L\le2\log T\)。故只要保留第一节的联合熵与其余尺寸预算，并将 \(H({\cal H})\le\kappa s\bar L\) 换成 \(\mathbb E_S I(F_S;B)\le\kappa s\bar L\)，即得同一覆盖结论，\(n\) 和有限样本 Chernoff 条件均可删除。正文 (3) 用到了较小的实际名单成本。原稿给几何步道排程核验的是 \(H({\cal H})\)；原估计本身没有给出新预算 \(\mathbb E_S I(F_S;B)\)。

**近似法则。** 若实际持有的是同一条公共记录 \(W\)，且每个 \(a,c\) 的预测边际 \(\widehat b_{W,c}\) 与真实 \(b_c\) 的总变差均不超过 \(\gamma u/p\)，可用预测边际制作名单，随即把 (2) 的 \(1-\tau/t\) 换成 \(1-(\tau+\gamma)/t\)，把 (1) 的 \(t/\tau'\) 换成 \((t+\gamma)/\tau'\)。因为每次测同一个平移集，概率误差至多 \(\gamma u/p\)。此时需 \(\tau+\gamma<t<\tau'-\gamma\)，成本取 \(I(F_S;D_S(W))\)。在近均匀的长字母表上，允许的绝对误差随 \(u/p\) 缩小。

## 三、仅看高熵时的尖锐界和失效实例

直接考察终端某个 \(p\) 字母边际 \(P\)。若 \(u<p\)，写 \(\alpha=u/p\)，则所有使 \((\tau,\beta)\) 覆盖失败的 \(P\) 满足
\[
 \log p-H(P)>d(\tau\alpha\Vert\alpha)
 =(1-\tau+\tau\log\tau)\alpha+O_\tau(\alpha^2).
 \tag{4}
\]
只记录是否落在一个 \(u\) 点低质量集合，均匀参照的命中率为 \(\alpha\)，真实命中率小于 \(\tau\alpha\)，即得严格下界。让这 \(u\) 点各取 \((\tau-\varepsilon)/p\)、余点平分剩余质量，\(\varepsilon\downarrow0\) 则达到下确界。若 \(u=p\)，要求全部残基严格低于 \(\tau/p\) 与总质量一矛盾。式 (4) 精化了冻结排程在终端基案使用的 Pinsker 平方损失。对联合变量也可令各坐标独立且均取上述近均匀坏边际，格取 \(\mathbb Z^k\)、每指标两符号取相同投影。所选 \(s\) 个不同指标的联合熵亏只是 \(s\) 倍边际亏。固定 \(\beta>0\) 时，边际亏可趋于零，同时每个坐标仍失败。[外稿的终端基案](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/schedule.tex#L418-L444)

甚至起点恰均匀、每个 \(a\) 条件覆盖良好，也不足以删去信息条件。取 \(G=\mathbb Z/101,\ Y=A\) 均匀，\(K=\{0,\ldots,10\}\)，给定 \(Y=y\) 令位移在 \((K-y)^c\) 均匀。令 \(\tau=1/4,\delta=1/64,\beta'=1/3,\beta=1/2\)。各条件终端恰缺 11 点，小于 \(101^{2/3}\)，但混合仍缺这 11 点，已达 \(\lceil101^{1/2}\rceil\)，故新覆盖失败。每套位移律可在 \(\mathbb Z\) 上取标准代表元实现。给定 \(K=[0,u-1]\)、\(u\le p/2\)，区间重叠的直接计数给
\[
 L_c(B_y)=\{x:\|x-y\|_p\le \lfloor t u(1-u/p)\rfloor\}\quad(0<t<1).
\]
本例名单有 5 点，真命中率一，101 份名单互异，联合起点泄露 \(\log101\)。只记录命中事件的相对熵为 \(\log(101/5)\)。两者均在 (3) 的正确方向。

不同坐标自行选时会改变测量对象。例如两坐标分别在两时刻为 \((U,0),(0,V)\)，其中 \(U,V\) 独立均匀。各选一次可提交均匀联合表 \((U,V)\)，而任选其中一个时刻只会出现两根坐标轴上的点，完全达不到该表的联合支撑。此有限检查说明必须固定共同终时法则及其与检查点的耦合。

## 四、表、样本和通信的分别计费

原样本在给定 \(B\) 后独立同分布，与 \(Y\) 条件独立。设 \(C_n\) 是这些实物位移的直方图。固定直方图后，词序对所有可能的 \(B\) 均为同一均匀排列，所以对每个固定 \(S\) 有
\[
 I(F_S;C_n)=I(F_S;h_1,\ldots,h_n)\uparrow I(F_S;B),\qquad
 H(h_1,\ldots,h_n)= n\,\mathbb E H(B)+ I(B;C_n).
 \tag{5}
\]
第一式的单调性来自有序样本的嵌套。有限个互异法则 \(b_i\) 的先验为 \(\pi_i>0\)，\(v_{ij}=\sum_h\sqrt{b_i(h)b_j(h)}<1\)。最大后验判错率满足 \(P_e\le\sum_{i<j}\sqrt{\pi_i\pi_j}v_{ij}^{\,n}\)，因为逐词的较小联合概率不超过两者几何均值，且乘积律使亲合系数取 \(n\) 次幂。差额 \(I(F_S;B)-I(F_S;C_n)=I(F_S;B\mid C_n)\le H(B\mid C_n)\le h_2(P_e)+P_e\log(m-1)\)，\(m\ge2\) 为法则数；\(m=1\) 时差为零。这同时给出极限与收敛速率。样本直方图的顺序无关，固定 \(n\) 时它的熵和它与残基的互信息仍是两种量。法则距离很小时，有限 \(n\) 的样本预算不能自动控制全法则信息。

若法则已由公共表给定、行索引只在掌握 \(A\) 的一方，则 (3) 是信息不等式。一次无损传给没有侧信息的另一方，法则索引的平均前缀码长度至少 \(H(B)/\log2\) 比特、可小于该值加一；零误差固定长度用 \(\lceil\log_2m\rceil\) 比特。若共享表本身也需传送，还要支付支撑、概率及精度的表示成本。仅知道同一秘密 \(A\) 就有 \(H(B\mid A)=0\)，不能据此令通信或 \(I(F_S;B)\) 为零。取独立均匀 \(Y,J\bmod p\)，给定位移律为 \(h=pJ+V,\ V\) 独立均匀于 \(0,\ldots,p-1\)，可使 \(I(Y;B)=0\)、\(H(B)=\log p\)。若改为 \(J=Y\)，则 \(I(Y;B)=\log p\)，但所有投影位移律仍相同，名单成本为零。这也解释了保留真实共同位移与选其充分投影两种账的差异。

对于显式有理表，一行含 \(d\) 个实物支撑点时，每坐标先以 \(O(d)\) 次映射或加法形成概率数组，再用 \(O(p|K_c|)\) 个有理加法/比较测试所有平移；预知的结构化区间可用重叠公式简化。共同先验与 \(y(a)\) 也须可得才能认定低概率集合、计算实际互信息。一行有 \(b\) 比特公共分母时仍须计入整数运算位长；任意实参数没有统一有限无损编码。样本次数的删除适用于具备这些分布输入或其证明界的实验。几何排程的真实位移表预算、可计算性，以及从它到原生 P000/X6 类型化操作的映射，仍待各自验证。此有限群论证不推出高斯素数图的全局分量结论。

## 五、复核

程序在 \(p=3,5,7\) 对 17,700 对位移律和集合验算 (1)，全部 14,584 个上榜残基都满足整数重叠下界。上述 \(p=101\) 的实际名单、混合低质量集及逼近 (4) 的四组质量均独立求出。两种等先验 Bernoulli 法则 \(1/4,3/4\) 的 \(n=1,\ldots,64\) 选定样本量中，直方图互信息从 0.130812 增至 0.693121 nat，有序样本熵从 0.693147 增至 36.682571 nat；至 \(n=8\) 另按有序词逐个求和交叉核对。

还有一个符合源中其余尺寸约束而能用 \(n=1\) 描述的正例。取素数 \(p=2^{127}-1\)（程序检验 Lucas–Lehmer）、\(T=p,\ k=s=1\)，两符号为同一取模同态，\(Y=A\) 在标准代表元上均匀。共同位移律固定，在模 \(p\) 的补集 \([0,p-1]\setminus[0,2^{60}-1]\) 上均匀。每个起点有 \(2^{60}<p^{1/2}\) 个例外，混合终端严格均匀。取 \(\beta'=1/2,\beta=3/4,\eta=1/2,\eta'=0,\tau=1/4,\delta=1/64\)。此时联合熵恰满、新信息费用为零，\(64^4<p,\ (2e/\delta)^8<384^8<p\)，源的单次 Chernoff 尺寸假设却失败。大字母表示例按区间恒等式和整数不等式核验；逐点枚举用于前三个小群及 \(101\) 点反例。[复算程序](coverage_check.py) · [结果](coverage_checked.json)
