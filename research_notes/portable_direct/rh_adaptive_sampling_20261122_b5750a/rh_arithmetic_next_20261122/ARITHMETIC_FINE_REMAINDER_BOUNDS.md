# 算术平均结构支付双侧细余项：从三次对数到一次对数

Date: 2026-11-22 (Asia/Hong_Kong).  
Researcher provenance: `EM-DIRECT-B5750A / TASK_RESEARCH`.  
Activity: `RA-60C6D083A81B19084A74C5BA`.  
Science freeze: `enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7`.

Status: 作者推导；一个初等无条件界，以及调用已核对的 Montgomery–Vaughan 筛上界的无条件加强。完整道路正能量与真实粗骨架的无界算术估计仍未证明。根任务统一保存，无新身份、CLAIM 或独立 Review。

全部整数、合数、单位、厚度、真实端点与前史保留。以下 prime / prime-power 分解仅在已声明的辅助参考 Λ 读出内用于上界；实际道路仍为 D，有限匹配误差显式支付。Green 算子与有符号分解不改变 P000 / native X6 或 BRC 正质量。

## 1. 对象、两个误差记号与新结论

沿用同一完整道路 q，其全整数源为

\[
f_n=-\Delta^2q_n=(\kappa_n-D_n)/n,
\qquad 0<\kappa_n\le K:=2\log2.
\]

在整数窗口 [A,B] 的块 [X,Y] 中，Y≤2X。细网格包含每块真实端点；细单元 [L,R] 长 h=R−L。置 F=I_Πq、P=q−F，闭权为 n^−2。P 在全部细节点恰为零。

分别记

\[
\varepsilon_B=\sup_{n\le B}|D_n-\Lambda(n)|,
\qquad \eta_{I,B}=\sup_{n\le B}I(\log n).
\tag{1}
\]

它们在本族有相同的可用上界，但证明不同。c−c*=μI 本身只立即给 ε_B≤max τ(n)η_I,B≤2√Bη_I,B。直接的厚度插值余项另外给

\[
\boxed{\varepsilon_B\le\frac{\prod_j a_j}{(m+1)!}(\log B)^{m+1}.}
\tag{2}
\]

式 (2) 的原证明见 `rh_next_root/CHEBYSHEV_THICKNESS_BRIDGE.md` §2。为使本稿独立，所需导数界可这样验证：R_a(n)=∑_{S⊆P(n)}(−1)^|S|exp(−a∑_{p∈S}log p)。把 (∑_{p∈S}log p)^k 按多重指标展开，固定非零支撑 T 后，其余子集和是

\[
(-1)^{|T|}e^{-a\sum_{p\in T}\log p}
\prod_{p\notin T}(1-p^{-a}),
\]

绝对值≤1。所有非负多项式系数的和为 (log rad n)^k。因此 |R_a^(k)(n)|≤(log rad n)^k。再用 R_a(n)/a=∫_0^1 R'_{ta}(n)dt 与 m 节点插值余项即得 (2)，n=1 由 D_1=Λ_1=0 单列。无需从卷积公式错误地省掉 τ(n)。若只采用较粗的 2√Bη_I,B，本稿所有渐近阶仍成立，因为它也趋零。

本稿将已有双侧细余项平方 O(log³ A) 改进为：

- 仅用初等 Chebyshev：O(log² A)。
- 用已核原始 Brun–Titchmarsh 区间上界：O(log A)。
- 若细步长≤X^(3/4)/(log X)^α，α>1/4，则双侧细余项趋零；α=1/2 时平方成本为 O(1/log A)。

均对固定幂窗口 B=A^λ、λ>1 及同一终端匹配族成立。只要求网格最大步长的上界，没有隐含最小单元长度或均匀间隔条件。

## 2. 两个离散 Green 范数界

把一个长度 h≥2 的单元平移为 [0,h]，内部 Green 矩阵为

\[
G_h(i,j)=\frac{\min(i,j)(h-\max(i,j))}{h},\quad 1\le i,j<h.
\]

它非负、对称，且

\[
\sum_jG_h(i,j)=\frac{i(h-i)}2.
\]

故由矩阵的行列和界（也可直接用加权 Cauchy–Schwarz），

\[
\boxed{\|G_h v\|_2\le\frac{\lfloor h^2/4\rfloor}{2}\|v\|_2
\le\frac{h^2}{8}\|v\|_2.}
\tag{3}
\]

另一方面，对固定 j，令 a=j、b=h−j，直接对两段平方和求和得

\[
\sum_iG_h(i,j)^2=\frac{ab(2ab+1)}{6h}.
\]

因此定义精确的最大列平方范数

\[
d_h=\frac{\lfloor h^2/4\rfloor(2\lfloor h^2/4\rfloor+1)}{6h},
\]

便有

\[
\boxed{\|G_hv\|_2\le\sqrt{d_h}\sum_j|v_j|,
\quad d_h\le h^3/48+h/24\le h^3/32.}
\tag{4}
\]

最后一步使用 h≥2。h=1 时没有内部整数，P 精确为零；以下各式直接略去该单元。

实际细余项在本单元为 P=G_h f。式 (3) 立即给一个保留实际源平方的可计算界：

\[
\boxed{\|P\|_{w,[L,R]}^2
\le\frac{\lfloor h^2/4\rfloor^2}{4X^2}
\sum_{L<n<R}f_n^2.}
\tag{5}
\]

式 (4) 则给总变差摘要界

\[
\boxed{\|P\|_{w,[L,R]}^2
\le\frac{d_h}{X^2}\left(\sum_{L<n<R}|f_n|\right)^2.}
\tag{6}
\]

二者可逐单元取小后相加。它们不要求 q 的完整插值值，但源统计量的取得仍有自己的算术读取成本。

## 3. 初等算术平均已经去掉一个对数因子

记 ψ(t)=∑_{n≤t}Λ(n)。我们只需一个显式粗 Chebyshev 上界

\[
\boxed{\psi(t)\le4(\log2)t\quad(t\ge1).}
\tag{7}
\]

证明：每个 m<p^a≤2m 在中央二项式 C(2m,m) 的 p-adic 指数和中贡献 1，其他贡献非负，所以 ψ(2m)−ψ(m)≤log C(2m,m)≤2m log2。沿 2 的幂望远镜求和，再把 t 向上夹到下一 2 的幂，即得 (7)。此证明无素数定理或零点假设。

在块 [X,Y] 中，b=Y−X、最大细步长 δ，利用 κ,Λ≥0，有

\[
\sum_{X<n<Y}(\kappa_n-\Lambda(n))^2
\le K^2b+(\log Y)\psi(Y).
\]

Minkowski 加上匹配误差，再用 (3) 于各单元，得到

\[
\boxed{\|P\|_{w,[X,Y]}^2
\le\frac{\delta^4}{64X^4}
\left[\sqrt{K^2b+(\log Y)\psi(Y)}
+\varepsilon_B\sqrt b\right]^2.}
\tag{8}
\]

当 δ≤X^(3/4)、Y≤2X 时，

\[
\|P\|_{w,[X,Y]}^2
\le\frac1{64}
\left[\sqrt{K^2+8(\log2)\log(2X)}+\varepsilon_B\right]^2.
\tag{9}
\]

固定幂窗口有 O(log A) 个块，而 log X=O(log A)，故 (9) 总计 O(log² A)。原点态估计把每个整数都当成 Λ≈log X；这里仅用 Λ²≤(log Y)Λ 和真实总体平均上界，已经省去一个对数。

## 4. 筛上界把双侧细余项降到一次对数

### 4.1 本节唯一外部输入及核对位置

Montgomery–Vaughan, *The large sieve*, Mathematika **20** (1973), 119–134, Theorem 2，printed p.121，式 (1.12)，给出对 M>0、N>1：

\[
\boxed{\pi(M+N)-\pi(M)\le2N/\log N.}
\tag{10}
\]

已实际读取作者 PDF 的定理页面；原始来源：

- [作者全文 PDF](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf)
- [密歇根大学原文存档](https://backend.production.deepblue-documents.lib.umich.edu/server/api/core/bitstreams/5adbb05b-05d0-4779-b1fd-304ec1ec257a/content)
- DOI: [10.1112/S0025579300004708](https://doi.org/10.1112/S0025579300004708)

本稿不把经典筛定理作为自己的新发现。新工作是把它与完整整数 Green 余项、匹配误差、任意细网格及明确节点成本接合。

### 4.2 正侧只需正曲率上界

在单元内写 e=D−Λ，并将 Green 像分为

\[
P=A_\kappa-B_{\rm p}-B_{\rm pp}-E,
\tag{11}
\]

其中 A_κ=G(κ/n)≥0，B_p=G(Λ1_prime/n)≥0，B_pp=G(Λ1_higher-prime-power/n)≥0，E=G(e/n)。这是完整源的精确分解，不修改 D 人口。由 |e|≤ε_B 和 Green 正性，

\[
P_+\le A_\kappa+G(|e|/n)
\le\frac{K+\varepsilon_B}{2X}(n-L)(R-n).
\]

因此令

\[
T_\Pi=\sum_{[X,Y]}\sum_{[L,R]\subset[X,Y]}
\frac{h^5-h}{120X^4},
\]

有

\[
\boxed{\|P_+\|_w\le(K+\varepsilon_B)\sqrt{T_\Pi}.}
\tag{12}
\]

若每块 δ≤X^(3/4)，则 T_Π≤N_blocks/120。

### 4.3 素数部分的负侧成本

长度 h≥2 的单元内，式 (10) 给

\[
M_{{\rm p},c}:=\sum_{L<p<R}\log p
\le\frac{2h\log Y}{\log h}.
\]

用式 (4) 及 n≥X，

\[
\|B_{\rm p}\|_{w,c}^2
\le\frac{d_h}{X^4}M_{{\rm p},c}^2
\le\frac{(\log Y)^2}{8X^4}\frac{h^5}{(\log h)^2}.
\tag{13}
\]

h^4/(log h)^2 在 h≥2 上递增。即使网格含很短的单元，也可由 h≤X^(3/4) 与 Σh=b≤X 得

\[
\boxed{\|B_{\rm p}\|_{w,[X,Y]}^2
\le\frac29\frac bX\left(\frac{\log Y}{\log X}\right)^2.}
\tag{14}
\]

这里 A≥4 足以覆盖非空 h≥2 范围。不要求全部 h≈X^(3/4)，也没有用一个小 h 的分母 log h 去放大全块。

### 4.4 高次素数幂是衰减成本

记 Q(Y)=∑_{p^a≤Y,a≥2}log p。由 (7)，

\[
Q(Y)\le4(\log2)\sqrt Y+4Y^{1/3}\log Y
\le(4\log2+24/e)\sqrt Y<12\sqrt Y.
\tag{15}
\]

第二步用 sup_{u≥1}(log u)/u^(1/6)=6/e；常数 12 可由 log2<3/4、e>8/3 作有理放宽。

不同细单元内部不交，它们的高次素数幂质量 M_pp,c 的总和≤Q(Y)。故

\[
\sum_c h_c^3M_{{\rm pp},c}^2
\le\delta^3\left(\sum_cM_{{\rm pp},c}\right)^2.
\]

再用 (4) 得

\[
\boxed{\|B_{\rm pp}\|_{w,[X,Y]}^2
\le\frac{\delta^3Q(Y)^2}{32X^4}
\le9X^{-3/4}.}
\tag{16}
\]

这项在连续倍增块上求和至多 9A^(-3/4)/(1−2^(-3/4))，随左端 A 增大趋零。

### 4.5 合并后的显式界

由 (11)，P_-≤B_p+B_pp+G(|e|/n)。设 N 为块数，A≥4，各左端按倍增排列（尾块保留真实 Y），δ≤X^(3/4)。由 (12)、(14)、(16) 及全窗口 Minkowski，

\[
\boxed{\begin{aligned}
\|P_+\|_w&\le(K+\varepsilon_B)\sqrt{N/120},\\
\|P_-\|_w&\le
\frac{\sqrt2}{3}\left(1+\frac{\log2}{\log A}\right)\sqrt N
+\frac{3A^{-3/8}}{\sqrt{1-2^{-3/4}}}
+\varepsilon_B\sqrt{N/120}.
\end{aligned}}
\tag{17}
\]

P_+、P_- 的支撑不交，因此 ||P||_w²=||P_+||_w²+||P_-||_w²。对于 B=A^λ、λ>1 固定，N≤1+(λ−1)log A/log2；稳定族 ε_B→0，故

\[
\boxed{\|q-I_\Pi q\|_w^2=O_\lambda(\log A).}
\tag{18}
\]

式 (18) 是双侧界，包括反向控制细插值过冲所需的负侧。它不把 O(log A) 说成趋零，也不为 q_+ 或原粗骨架提供无界算术消失。

## 5. 对数级加密使双侧误差真正趋零

固定 α≥0，选最大步长

\[
\delta_X\le H_X:=X^{3/4}/(\log X)^\alpha.
\]

对充分大的 X，log H_X≥(1/2)log X。式 (13) 的单调性给

\[
\|B_{\rm p}\|_{w,[X,Y]}^2
\le\frac{b_XH_X^4}{8X^4}
\left(\frac{\log Y}{\log H_X}\right)^2
=O((\log X)^{-4\alpha}).
\]

κ 与 ε 项亦具有同一 (log X)^(-4α) 因子；素数幂项由 (16) 进一步缩小。固定幂窗口内 log X≈log A，块数 O(log A)，于是

\[
\boxed{\|q-I_\Pi q\|_w^2
=O_{\lambda,\alpha}((\log A)^{1-4\alpha})+O(A^{-3/4}).}
\tag{19}
\]

ε_B 有界且趋零时可吸收到显示的常数；主项常数不依赖具体网格。结论包括

\[
\boxed{\alpha>1/4\ \Longrightarrow\ \|q-I_\Pi q\|_w\to0,}
\]

\[
\boxed{\alpha=1/2\ \Longrightarrow\ \|q-I_\Pi q\|_w^2=O(1/\log A).}
\tag{20}
\]

这只是本上界给出的充分条件，没有证明 α=1/4 是必要门槛。

取块内规则步长 floor H_X 并保留真实尾端，则当 H_X≥2 时，单元数≤2b_X/H_X+1。倍增块求和给

\[
\boxed{\#\Pi=O_{\lambda,\alpha}(B^{1/4}(\log B)^\alpha).}
\tag{21}
\]

相较原 X^(3/4) 规则，增加的是明确的对数因子。对于任意过度加密的不规则网格，误差界仍成立，但不宣称节点数还满足 (21)。

由上一批自由树精确公式及根预算比较

\[
0\le\mathcal B_* -\|\max(J_+,q_+)\|_w
\le\sqrt2\|q-I_\Pi q\|_w,
\]

在 (20) 的网格上，细插值造成的这部分差趋零。真实粗骨架覆盖项和 q 的正能量仍完整保留。

## 6. 精确交叉与本稿没有解决的部分

式 (11) 可以逐整数直接复算。参考细余项的平方具有完整交叉式

\[
\|A_\kappa-B_{\rm p}-B_{\rm pp}\|_w^2
=\|A_\kappa\|_w^2+\|B_{\rm p}+B_{\rm pp}\|_w^2
-2\langle A_\kappa,B_{\rm p}+B_{\rm pp}\rangle_w.
\tag{22}
\]

本稿的单侧上界无需假设这些项独立，也没有据此删除交叉来估计完整 q。细单元零边界消除了仿射端口，因此上述正核成本确实属于局部余项；同样手法若直接放到长度≈X 的粗块，成本会成为幂量级，不能用 (18) 支付原真实骨架。

因此本稿新增的是：用实际算术平均减少细余项的损失，并用轻度加密把它压到零。中粗尺度参考的联合 Möbius 和、真正 q_+ 能量及骨架覆盖仍是待证算术部分。没有使用 RH、素数间隔下界或随机鞅假设。

## 7. 有限复算

配套 `certify_arithmetic_fine_bounds.py` 读取原完整道路缓存和已发布网格，绝不重选厚度节点、不重新生成道路。它用原分母 10^60 的有向整数区间核对新 Green 统计界、实际双侧细余项、κ/素数/高次素数幂/匹配误差分解，并保存逐单元及逐块结果。

一般界依据上述解析证明及明确引用的 (10)；有限数据只验证实现与量化当前窗口，不能外推无界算术消失。

本次原 43 个细单元共有 31,701 个内部整数；逐点 Green 分解全部通过区间相交核对。严格平方值及上界的向上显示为：

| 细余项量 | 数值 |
|---|---:|
| 实际正侧平方能量 | 0.000022387876371496138997239435 |
| 实际负侧平方能量 | 0.000016175148719246122085339838 |
| 实际双侧平方能量 | 0.000038563025090742261082579273 |
| 旧统一双侧点态源界给出的上界 | 5.489343682248261808392301927803 |
| 新实际源 ℓ² 统计上界 (5) 的总和 | 0.287486383966583778145180925851 |
| 新实际源 ℓ¹ 统计上界 (6) 的总和 | 0.156296597806117165697730754843 |

这张表比较的是**同一细余项的通用估计方式**，不是上一批完整道路的最优包络预算。原细余项已能精算，上面较大的统计上界不应替换更好的现成数值。统计量目前仍从全部旧源取得，故也不声称减少了原始输入。新成果的主要用途是任意远窗口上可证明的阶数和 (20) 的趋零网格。

另在相同细网格的参考余项中，式 (22) 的两个对角平方之和约为 0.023774665850956949，而负交叉约为 −0.023736102825370951，留下 0.0000385630255859984。交叉抵消约 **99.8378%** 的对角和；只看对角会放大约 **616.5 倍**。完整精确区间在 JSON 的 `reference_fine_cross` 中。该观察说明当前有限样本的精度强烈依赖 κ 与 Λ 的同核配对；本稿的无条件通用上界没有宣称已解释这种精细抵消的全部算术来源。
