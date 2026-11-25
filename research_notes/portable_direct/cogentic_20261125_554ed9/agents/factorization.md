# Cogentic 两篇整数分解论文：可用数学提取与核对

## 读取边界与来源

固定源：google-research/google-research@4a7bc8ab0bc7，固定版本提交日期 2026-11-25。

- [A：Unconditional Integer Factorization in Time L_N[1/3,O(1)]](https://github.com/google-research/google-research/blob/4a7bc8ab0bc7/cogentic_research_papers/integer_factorization/paper.pdf)，54 页。PDF SHA256：9ac07593ca90c0f315af0b0214320823a43e7c905e6700948261ebb09a4d537d。
- [B：Unconditional Deterministic Subexponential Integer Factoring and Quadratic Nonresidue Construction](https://github.com/google-research/google-research/blob/4a7bc8ab0bc7/cogentic_research_papers/deterministic_factoring_l34/paper.pdf)，59 页。PDF SHA256：0ccf115516dab3cbeee15167f2dea62fcb29d03a19224cb4a9ae69a5ce402993。
- 两个 README 明示论文 CC-BY-4.0，Copyright 2026 Google LLC；本文对数学内容重新组织并保留出处。
- 两篇全文已取回，阅读了总论、关键定义、下列命题及其相关证明；没有完成全篇全部承重估计的逐行独立审查。
- 固定目录各含 README 和 PDF；README 声称 Lean 4 证明已完成、将在 companion 发布。该固定输入未提供 Lean 源及可执行校验结果。
- 所有外部算术内容作为进取数论的整数寄存器、有限域、系数空间或观测辅助工具吸收；不改 P000 / X6 本原定义。

## 1. 主结论应该怎样记录

A 的 Theorem 1.1（p.2）声称：单一统一经典概率多带 Turing 机对所有 N≥2 零错误输出完整素因数分解；期望位复杂度 L_N[1/3,105]，最坏随机带上的确定性工作空间 L_N[1/3,40]。其中

\[
L_N(\alpha,c)=\exp\{c(\log N)^\alpha(\log\log N)^{1-\alpha}\},
\quad
T\le L_N[\alpha,c]\iff
\limsup_{N\to\infty}
\frac{\log\max(1,T(N))}
{(\log N)^\alpha(\log\log N)^{1-\alpha}}\le c.
\]

这是论文主张；本次独立确认的是若干局部代数机制和有限验证，不将整套渐近复杂度自动标为本项目已接受定理。

B 的 Theorems 1.1–1.3（p.4）分别声称：

1. 每个合数 N≥4 可确定性找非平凡因子，代价 \(O(\exp(3(\log N)^{3/4}))=L_N[3/4,o(1)]\)。
2. 给定非完全幂合数 N 及偶数 \(\widetilde M\)，满足每个 p|N 都有 p−1|\(\widetilde M\)，可在
   \[
   C_1\exp\{C_{\rm split}\sqrt{\log N}\log\log(N+16)\}
   (\log\widetilde M)(\log N)^2
   \]
   位操作内确定性分裂；对奇素数 p，可在
   \[
   C_2\exp\{C_{\rm split}\sqrt{\log p}\log\log(p+16)\}
   \]
   内构造二次非剩余。
3. 给定奇非完全幂合数 N≥9，在上述分解量级内直接找因子，或构造共同 p−1 倍数，且
   \[
   \log\widetilde M\le \exp((\log N)^{0.65}).
   \]

### 已发现的一处摘要记号偏差

B 的 README 将 QNR 的 \(\exp(O(\sqrt{\log p}\log\log p))\) 写成 \(L_p[1/2,O(1)]\)。按它自己定义的 L 记号，后一量级应为 \(\exp(O(\sqrt{\log p}\sqrt{\log\log p}))\)，两者相差一个 \(\sqrt{\log\log p}\) 因子。PDF Theorem 1.2 没有这个错误简称。提取时采用 PDF 的精确式。此发现涉及摘要记号，没有提供否定主证明的反例。

## 2. 最值得优先拿来的局部工具

### 2.1 祖先消失扰动：增加自由度，同时严格保留已完成约束

A §4、Lemma 4.4 与 4.6（pp.35–40）将沿途已求值点 \((a_t,b_t)\) 编入

\[
P_{\rm anc}(X,Y)=\prod_{t<r}(b_tX-a_tY).
\]

任何 \(\Delta f=P_{\rm anc}H\) 在所有祖先点取零。因此在新的随机化或搜索中保留每个祖先的完整求值，而非只保留最终标量的某个近似。

可单独手证的加强接口：若还要保持基点 \(f(g_0,g_1)\) 与模 3 多项式，则用

\[
\Delta f(X,Y)=3(g_1X-g_0Y)P_{\rm anc}(X,Y)H(X,Y),
\quad \deg H=d-r-1.
\]

它保持同次次数、每个旧求值、基点值和模 3 系数。系数大小、后续可达性及条件采样分布需要另外计算。

**接入 Riesel 的直接整数版本。** 对 \(F_n(a)=a^22^n-1\)，已有通道模数 \(M=\prod_i p_i^{h_i}\)，取 \(a'=a+tM\)，则

\[
F_n(a')-F_n(a)=2^n(2atM+t^2M^2).
\]

因此所有 \(n\ge0\) 和全部旧通道的模 \(p_i^{h_i}\) 读数同时保持。若新增素数 \(q\nmid M\) 已有合法根 \(r\) 满足 \(r^22^{n_*}\equiv1\pmod q\)，则

\[
t\equiv(r-a)M^{-1}\pmod q
\]

精确接入该新约束。这是既有 CRT 扩展的“旧观测保持证书”，适合写进每次新增通道的证据。

- 要保持精确赋值 \(v_{p_i}(F_n(a))=v\)，至少需要保留模 \(p_i^{v+1}\) 的非零商信息；只有 mod p 标签不够。
- \(q\mid M\) 时应按广义 CRT 的相容条件处理，不能用逆元公式。
- 改 a 是更换初始整数寄存器；它不更改固定 X6 anchor 或既有 \(x\mapsto2x+1\) 更新规则。
- 每个根选择仍需保留联合分支，不把同一边际覆盖当成同一个完整状态。

**接入 RH 三角矩。** 在候选包络或系数参数 c 上，把已验证观测写为矩阵 Ac。新扰动只选 \(\delta c\in\ker A\)，从而保持旧观测。新增观测行不在旧行空间时才有新的可调方向。这里 c 是我们构造的包络/证书参数，真实算术序列 \(D_n\) 仍是固定输入，不能随意改动。

### 2.2 加权接受后的反向望远镜：把稀疏密度从逐层损失中消掉

A Lemma 4.6（pp.39–40）的要点是按候选权重 \(w_t(a)\) 接受，而不是先逐层乘上粗糙的稀疏性倒数。

设每层实际权重和 \(Z_t\ge\mu_t/2\)，于是候选选择核满足

\[
K_t(a\mid{\cal H}_t)\le \frac{2w_t(a)}{\mu_t}.
\]

如果在相同祖先求值条件下

\[
\sum_a {\mathbb E}[w_t(a)\mid{\cal H}_t]\le \frac32\mu_t,
\]

并且每个可达后继求值纤维上局部失败概率都至多 \(\varepsilon\)，每节点候选子节点数≤B，那么条件期望的塔式法则逐层给出

\[
{\mathbb P}(\text{某层失败})\le
\varepsilon\sum_{r=0}^{h}(3B)^r
\]

加上另行列出的超时及尾部概率。这里的稀疏密度 \(\mu_t\) 在 \((2/\mu_t){\mathbb E}w_t\) 中被消掉。

A 的具体参数是 B≤\(\log_2N\)、h≤\(0.65\log\log N\)、局部失败至多 \(2e^{-25(\log\log N)^2}\)，最终约束到 \(e^{-23(\log\log N)^2}\) 量级。

**可用场景：** 多层 CRT 候选扩展、随机骨架选择、条件关系搜索。**真正需要补的量：** 对全部可达祖先求值纤维有效的局部失败界。无条件采样成功率、固定窗口测试或只看单层边际，不能替代这个条件估计。对 RH 统一素数亏缺而言，这提供组织条件误差的方式，不提供缺失的素数亏缺上界。

### 2.3 离散 Laplace 权重的平移稳定性

A Lemma 4.2(4)（p.29，证明 pp.31–32）取截断权重

\[
G(c)=e^{-\alpha\|c\|_1}
\]

限制到整数仿射切片 \(U=(c_*+L)\cap[-W,W]^{d+1}\)。若切片分布落在 \(\|c\|_\infty>5W/8\) 的概率≤\(\varepsilon_{\rm tail}\)，扰动 \(\delta\in L\cap[-\Delta,\Delta]^{d+1}\)、\(\Delta\le W/8\)，且

\[
\varepsilon_{\rm lip}=(d+1)\alpha\Delta\le 1/2,
\]

那么对每个 \(0\le\Phi\le1\)，

\[
e^{-\varepsilon_{\rm lip}}\mathbb E\Phi(c)-\varepsilon_{\rm tail}
\le
\mathbb E\Phi(c+\delta)
\le
e^{\varepsilon_{\rm lip}}\mathbb E\Phi(c)+\varepsilon_{\rm tail}.
\]

局部证明仅用 \(|\|c+\delta\|_1-\|c\|_1|\le\|\delta\|_1\) 及边界尾质量，具有独立可复用性。它适合需要“保留旧约束，再作小扰动”的采样；概率分布必须在所声明的切片上，不能用未条件化的尾概率。

### 2.4 对称区间混合：把离散线性型估计降为区间平均

A Proposition 2.4（p.9；Appendix A，pp.51–52）：

\[
S_n(w)=\sum_{i=0}^{n} w_i a^i(-b)^{n-i},
\quad w_i\sim{\rm Unif}([-W_0,W_0]\cap\mathbb Z),
\]

其中 \(n\ge1\)、a,b 非零且互素、\(C=\max(|a|,|b|)\)、\(W_0\ge4nC\)。设 \(\widetilde q_n\) 是将各 \(w_i\) 换为连续均匀变量后的密度，\(R_n=W_0\sum_i|a|^i|b|^{n-i}\)，\(\Delta\widetilde q_n(R)=\widetilde q_n(R)-\widetilde q_n(R+1)\ge0\)。对每个 \(f:\mathbb Z\to[0,1]\)，

\[
\left|\mathbb E f(S_n)-
\sum_{R=0}^{R_n}\Delta\widetilde q_n(R)\sum_{z=-R}^R f(z)\right|
\le \frac{9n(n+1)C}{W_0}.
\]

质量和距1同样至多这个误差，且小半径部分总质量≤\(R_0/(W_0C^n)\)。这样，复杂系数随机变量的观测可由对称区间平均控制。

对本项目的价值是明确的“输入分布替换支付”；不能自动拿到比既有有理 Green 包络更小的误差，需把新增 \(9n(n+1)C/W_0\) 与原有支付比较。

### 2.5 Gevrey 截断给显式 Mellin 尾界

A Lemma 3.1（pp.15–16）给出短区间指标的上下光滑包络。若 \(0<\delta\le1/2\)、\(0<\eta\le1/8\)、\(\sigma=\eta\delta/2\)，则

\[
\psi_-\le1_{[1,1+\delta]}\le\psi_+,
\quad
\int_{\mathbb R}|\widehat\psi_\pm(it)|\,dt
\le120+4\log(1/\eta),
\]

且 \(T\ge2000/\sigma\) 时

\[
\int_{|t|>T}|\widehat\psi_\pm(it)|\,dt
\le
\frac{10^6\delta}{\sigma}(1+\sqrt{\sigma T})
e^{-\sqrt{\sigma T}/10}.
\]

它把窗口边界误差和频域截断误差分开显式支付。若对真实三角矩换核，应另计

\[
\left|\sum_n\frac{\phi(n)-\psi(n)}n(\kappa_n-D_n)\right|
\le
\sum_n\frac{|\phi(n)-\psi(n)|}n|\kappa_n-D_n|.
\]

所以优先试验已固定输入的核误差预算是否真的改善，再决定扩大窗口。


### 2.6 混合平滑权重：一个自由整数因子吸收公因子

A Definition 3.4 / Lemma 3.5（pp.18–19）定义 r=4u、\({\cal P}(y)=\{p:y/2<p\le y\}\)，令

\[
\widetilde w_{y,u}(n)=\frac1{r!}
\#\{(m,p_1,\ldots,p_{r-1}):
y/2<m\le y,\ p_j\in{\cal P}(y),\
mp_1\cdots p_{r-1}=n\}.
\]

正权重只支持 y-平滑整数，且 \(0\le\widetilde w\le1\)。把 \(n=M_{\rm sm}\prod_{q\in{\cal P}(y)}q^{e_q}\)、\(E=\sum e_q\) 分解后，精确公式是

\[
\widetilde w(n)=
\begin{cases}
1_{E=r}/\prod_qe_q!,&M_{\rm sm}=1,\\[2mm]
1_{y/2<M_{\rm sm}\le y}\,1_{E=r-1}/(r\prod_qe_q!),&M_{\rm sm}>1.
\end{cases}
\]

这里“已知完整分解后可多项式时间计算权重”是明示输入条件，不能用来循环声称已经解决分解。

若在等差数列 \(z+mt\) 中 \(g=\gcd(z,m)\le y^{3/10}\)，由于所有选取素数都大于y/2，公因子g必须进入自由整数因子。写 \(m'=m/g\)，局部密度产生精确消去

\[
\frac1g\cdot\frac{\varphi(m')}{m'}\cdot\frac1{\varphi(m')}=\frac1m.
\]

原文进一步在“可容许参数、长度区间、无坏导子因子”等条件下，证明权重等差平均与通用密度 \(\nu\) 的相对误差≤\(e^{-27(\log\log N)^2}\)。这些解析条件需要整体携带。

**对本项目的用途：** 构造可精确计算的正权重探针，使某些局部算术因子由设计抵销。它探测的是特别构造的平滑整数集合；真实素数亏缺问题仍需独立连接式。值得拿来的是“重新设计观测权重以消去局部偏差”的方法，以及上面的精确有限恒等式。

## 3. 与 CRT、模阶和“联合残差”最相关的结构

### 3.1 子群指数饱和

B Lemma 11.1（p.55）有一个很干净的独立算术核心。

给定素数 p、互异素数集合 S⊂[1,B]，m=|S|，且 \(B^k\le p-1\)。S 的 k 元多重集乘积都是小于 p 的不同正整数，因此在模 p 下仍互异：

\[
|\langle S\bmod p\rangle|
\ge {m+k-1\choose k}.
\]

若 M 对每个 s∈S 都满足 \(s^M\equiv1\pmod p\)，利用 \(\mathbb F_p^\times\) 的循环性得到 \(|G|\mid M\)。若指数 \(I=(p-1)/|G|\le K\)，则

\[
p-1\mid M\operatorname{lcm}(1,\ldots,K).
\]

原文把它同时应用于 N 的全部未知素因子，要求

\[
|S|\ge B/(6\log B),\quad
K_{\rm idx}\ge B\exp\!\left(\frac{\log N}{\log B}\log(6\log N)\right),
\quad P^-(N)>K_{\rm idx},
\]

并给出 \(\log\operatorname{lcm}(1,\dots,K_{\rm idx})=(1+o(1))K_{\rm idx}\)。

**对本项目：** 可用于模阶覆盖的确定性补全、缺失模阶预算和验证器。原文“能低成本找到大量 M”的部分仍依赖其前面的大型解析证明。不能从一个小集合无条件推出它已覆盖整个单位群。循环群前提必需；不可照搬成任意 X6 关系群的阶结论。

有限例：p=31，S={2,5}，M=15，B=5，k=2。多重集给 |G|≥3，实际 |G|=15、指数2；粗上界 K=10，因此 \(15\operatorname{lcm}(1,\ldots,10)=37800\) 是30的倍数，M本身不是。

### 3.2 Walsh 正性需要联合相容，才能消掉负尾

B Lemma 5.1（pp.20–22）构造 \(2^K-1\) 个二次域及两两双二次合成域上的相容理想特征。其承重假设包含：小整数、小范数主理想及单位上的特征均为+1，以及合成域上特征延拓相容。

设 \(b_\ell(n)\) 是域 \(\ell\) 中范数 n 的理想特征之和。原文证明存在 \(0\le b_0(n)\le\tau(n)\)，使得在 \(\gcd(n,P_Kq)=1\) 上

\[
b_0(n)+\sum_{\ell\in\mathbb F_2^K\setminus\{0\}}b_\ell(n)
\ge 2^K1_{P^+(n)\le Y}.
\]

于是

\[
\max_{\ell\ne0} S_\ell^{\rm cop}(X)
\ge
\Psi_{P_Kq}(X,Y)-\frac{X(\log X+1)}{2^K-1}.
\]

可独立吸收的有限代数事实是：若每个局部因子在群 \(\mathbb F_2^K\) 上有非负 Fourier 系数，局部因子的乘积对应非负系数的卷积，整体和为 \(2^K\) 倍的零频系数，因而非负。

这与保留联合分支、相位及符号 CRT 信息高度契合。仅有各边际符号没有保证：K=2 时随意取 \(b=(1,-1,-1,-1)\)，总和为−2；其中非零三点的符号乘积为−1，违反线性特征的相容关系。真正的收益来自已证明的联合兼容代数。

后续研究可测试 Riesel 的符号 CRT 字典能否给出某个已定义 \(\mathbb F_2^K\) 观测族及非负 Fourier 分解；其存在性需要用当前通道关系证明，不能直接把本论文的理想特征当成我们的字典。

### 3.3 素理想偶赋值之后仍有平方类残差

A Proposition 2.5（pp.9–10）对奇数次数 d 的不可约整数多项式给单生成序 \(A=\mathbb Z[\theta]\)、判别式 \(\widetilde\Delta\)，令

\[
V_A=\{x\in K^\times:l_{\mathfrak p,A}(x)\equiv0\pmod2
\text{ for all maximal }\mathfrak p\}.
\]

则

\[
\dim_{\mathbb F_2}(V_A/(K^\times)^2)
\le2d\log_2(|\widetilde\Delta|+4)+d.
\]

原文使用局部 Jordan–Hölder 长度处理非极大序，在无判别式坏素数处它退化为普通素理想赋值。价值是：清掉局部奇偶读数后，剩余单位、类群及坏素数信息进入一个有限维残差空间，而非被默认为零。这种“明确剩余空间，再添加分离观测”的做法可迁移到我们现有读数完备性研究；数域维数上界只对该数域对象成立。

### 3.4 隐藏平方根分支保证精确的 CRT 成功率

A Lemma 5.3（p.44）：N为奇数且 \(k=\omega(N)\ge2\)。独立均匀取单位 \(z_i\)，只把 \(w_i=z_i^2\bmod N\) 提供给关系构造程序。程序基于 w 和独立随机性选非空 T，并给出 \(Y^2=\prod_{i\in T}w_i\bmod N\)。最后才打开 \(Z=\prod_{i\in T}z_i\bmod N\)。则在完整可见记录条件下，

\[
\Pr(1<\gcd(Z-Y,N)<N)=1-2^{1-k}.
\]

证明是 CRT：平方根核有 \(2^k\) 个独立符号，只有全+与全−两个失败。若算法提前看到 z 并故意令Y=Z，概率变成0；“只依赖平方的记录”是实质前提。该结果不是模型盲审制度，而是精确的算术信息流条件。

## 4. 适合精度、递归与验证器的附加提取

### 4.1 从近似数恢复精确有理数

B Lemma 7.2(3)（pp.30–31）使用 Legendre 连分数准则：

\[
|x-p/q|<1/(2q^2),\ \gcd(p,q)=1
\Longrightarrow p/q \text{ 是 }x\text{ 的连分数收敛分数}.
\]

若已知分母≤Q，误差区间半径<\(1/(2Q^2)\)，同一区间最多容纳一个候选有理数。原文 TryPair 再核验输出满足 \(\ell^{E_\ell}\equiv1\bmod N\)。适合“低精度探索→区间决定能否恢复→整数回验”的路线；精度不够时继续缩小区间即可，无需预设浮点结果就是精确关系。

### 4.2 3-adic 快速精度提升后整数回验

A Lemma 5.2（pp.43–44）在模3不可约、奇次数d的数域序中，利用 \(3^d\equiv3\bmod4\) 对平方 \(\alpha_0\) 取初始根

\[
\beta_0=\alpha_0^{(3^d+1)/4}\in\mathbb F_{3^d}.
\]

随后 Newton–Hensel 逐次倍增3进精度，同时更新逆导数。原文给定系数界 \(2^{B_{\rm bit}}\)，精度达到 \(3^{2^K}>2^{B_{\rm bit}+2}\) 后用平衡代表恢复整数多项式，最后直接检验 \(\widehat\beta^2=\widetilde\Gamma\)。把局部算术恢复转成全局精确结论所需的关键量是系数界，不是单纯“迭代收敛”。

### 4.3 递归缩小输入的常数预算公式

A 总论p.5、最终复杂度证明pp.47–49，递归输入≤\(\frac12\sqrt N\)。一般地，若一次外层的递归调用预算为 \(L_N[\alpha,a]\)，每个子输入≤\(N^\theta\)，拟证 \(T(N)\le L_N[\alpha,c]\)，则指数预算应满足

\[
a+c\theta^\alpha<c
\quad\Longleftrightarrow\quad
c>\frac{a}{1-\theta^\alpha}.
\]

还需列入非递归成本及外层重启成功概率。A 使用 \(\alpha=1/3,\theta=1/2,a=21.15,c=104\)，有 \(21.15+104\cdot2^{-1/3}<104\)，最后报告105。它是适合复算的资源预算式，可用于我们需要递归下降的精确搜索与证书生成。

## 5. 有限核对记录

脚本：factorization_checks.py。已实际运行，覆盖：

- y=20、4个因子槽的混合平滑权重：640个有序表示、155个不同整数，逐项核对归一化精确公式。它只验证组合恒等式，参数不在原文渐近解析范围。
- N=15、45、105、225 的所有单位及全部平方纤维；每个纤维的隐藏根拆分比例分别为1/2、1/2、3/4、1/2。
- p=31、S={2,5} 的子群饱和例。
- \(\mathbb F_2^3\) 上非负 Fourier 系数乘法/卷积恒等式；并列出 \(\mathbb F_2^2\) 非兼容符号的负和反例。

这些是抽出的局部工具的有限证据，不是运行了两篇完整分解算法。

## 6. 建议吸收顺序

1. 立刻纳入可手证工具层：祖先约束保持、CRT旧通道保持公式、有限群 Walsh 非负卷积、隐藏平方根 CRT 概率、子群指数饱和核心、带分母界的有理恢复。
2. 用固定输入作对照实验：对称区间混合与 Gevrey 截断能否减少已有核的总误差支付；按“新误差+旧支付”比较，保留失败样例。
3. 作为新的证明路线：条件纤维上的加权望远镜、相容符号族的 Walsh 正性提升。先定义该家族和条件估计，再谈统一结论。
4. 两篇主算法按原文定理及其完整依赖树保存，等待逐段数学复核或实际 Lean 源回读；目前可用局部成果已经足够形成具体研究增量。


