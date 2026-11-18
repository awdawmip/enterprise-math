# 有限循环因子的逐层审计与两色堆叠的提升障碍

题目 RS-OAI7-155-C-20261007-6F2A81。冻结外稿通过 $\mathbb Z^2$ 加**一个**有限循环坐标进入三维。下表核对了各阶段。新增的两色判据说明一个容易忽略的限制：即使新的总群仍然循环，若把原稿的直积替成不分裂的扩张，堆叠瓦片也可能完全无法铺砌。[任务书](https://github.com/awdawmip/enterprise-math/blob/af934cfd5c1608674d15b96d14a3bae1c56b8370/research_tasks/RS-OAI7-155-C-20261007-6F2A81.md) · [有限复算](stack_check.py) · [结果](stack_checked.json)

## 一、从编码到商映射

写 $C_m=\mathbb Z/m\mathbb Z$，$p>200$ 为素数，$N=p^2$，$D=p^4$。有 $N$ 个普通通道和两个种子；普通通道有 $p-1$ 个数字标签，种子各有一个。每个通道 $i$ 取互异素数 $a_i,b_i$，其中 $a_{\eta_1}=2,a_{\eta_2}=3$，两个种子 $b_i>D$。它们均不同于 $p$。每个数字另取素数 $r_{ij}$，在所有通道间互异，并避开上述所有素数；它须形如 $A_{ij}a_i+B_{ij}b_i$，其中两系数均非负。取任一足够大的新素数 $r\ge(a_i-1)b_i$，先解 $B_{ij}b_i\equiv r\bmod a_i$，取 $0\le B_{ij}<a_i$，再得非负 $A_{ij}$。该等式用于把一个有限集划分成指定大小的块。[外稿 §3，通道与模数](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/03-cyclic-encoding.tex#L15-L76)

| 阶段 | 实际群与核 |
|---|---|
| 水平余类及标签 | $s:\mathbb Z^2\to S=C_{p^2}^2$ 的核是 $p^2\mathbb Z^2$，自由秩二。$S$ 有 $D$ 个元素、指数 $p^2$，它与指数 $p^4$ 的 $C_D$ 间只有选定的集合双射。横向 $x$ 已存在，$S$ 没有另添到垂直群。 |
| 数字与输出 | $r_i=\prod_jr_{ij}$，$K_i=\prod_j C_{r_{ij}}\simeq C_{r_i}$，$P_i=C_{a_i}\times C_{b_i}\simeq C_{a_ib_i}$。这些 CRT 同构的核为零。存储高低数字的是 $C_{r_i^2}$，低位映射到 $C_{r_i}$ 的核 $r_i C_{r_i^2}\simeq C_{r_i}$。该短正合列不分裂：任何低位为 $1$ 的提升都有阶 $r_i^2$。水平剪切选每条纤维的坐标，进位仍由原来的循环加法决定。 |
| 全体有限坐标 | $V=C_D\times\prod_i(C_{r_i^2}\times P_i)$，阶数 $M=D\prod_i r_i^2a_ib_i$。各显式循环因子的阶两两互素，故 $V\simeq C_M$。图映射 $q_0:\mathbb Z^2\times V\to\mathbb Z^2\times\prod_i K_i$ 的核有限、阶 $D\prod_i r_i a_ib_i$，仍为循环群，自由秩零。 |
| 普通激活 | 沿斜率 $u_i=(1,-i)$，水平位移的第一分量同时指定模 $r_i,a_i,b_i$。解集为一陪集，核 $r_i a_i b_i\mathbb Z u_i$ 自由秩一。组批所用的 $r_\ell C_{r_\ell^2}$ 与 $P_\ell$ 是现有因子的子群或取值域。 |
| 种子激活 | 第一分量再指定模 $p^2$ 和另一个种子的 $a_{i'}$，第二分量只指定模 $p^2$。置 $M_i=r_i a_i b_i p^2a_{i'}$，齐次核 $M_i\mathbb Z\times p^2\mathbb Z$ 自由秩二，指数 $p^2M_i$。两个水平分量里都出现 $p^2$，属于两个既有整数变量的同余条件。 |
| 共同解与堆叠 | 对 $S$ 的分块采用大小为 $3,2,6$ 的标签空间，两个种子分别作用于这些标签。$D\equiv1\bmod 6$；$3+2\cdot2+6\cdot(D-7)/6=D$。所选 $\lambda:S\to C_D$ 及分块置换无需保持加法。叠 $s$ 个铺砌方程只增添一个新素数阶 $C_q$，$q\nmid M$，故 $V\times C_q\simeq C_Q,\ Q=Mq$。 |
| 三维提升 | $\pi:\mathbb Z^3\to\mathbb Z^2\times C_Q,\ (x,y,z)\mapsto(x,y,z\bmod Q)$，核 $\mathbb Z(0,0,Q)$ 自由秩一，在竖直整数直线中指数 $Q$。水平秩始终是二。 |

共同解里对大小 $a_i,b_i$ 的块指定循环标签，只规定块内置换，不要求 $a_i$ 或 $b_i$ 整除 $r_{ij}$。激活 CRT 也允许通过加整周期选取互异水平偏移。两者均不增加垂直素因子。[外稿 §4，激活同余](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/04-activation.tex#L67-L128) · [§5，集合标签](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/05-common-solution.tex#L144-L176) · [§6，堆叠与新素数](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/06-stacking.tex#L113-L128)

**群秩证书。** 给出不一定互素的任意循环因子 $m_j>1$。其乘积 $U$ 的最少生成元数为
\[
 d(U)=\max_{\ell\ {\rm prime}}\#\{j:\ell\mid m_j\}.
\]
下界来自 $U/\ell U$ 的向量空间维数，上界对各素数的循环初等因子按列并排，再在列内作 CRT。$\mathbb Z^2\times U$ 的最少整数生成元数正好是 $2+d(U)$，下界也可模同一个 $\ell$ 取得。因此该**群商接口**容许 $\mathbb Z^3$ 满射当且仅当 $U$ 循环（含平凡群）。若重复加入 $C_2$ 得 $C_2^2$，四维整数格才能按此接口满射；即使把水平与垂直坐标线性混合也一样。此断言限于群同态编码。外稿中单位立方体加厚和任意实平移的网格刚性另有几何论证。若 $B$ 是商铺砌中心的全逆像，$B+(0,0,Q)=B$；单方向周期可以存在。完整秩周期的推出或排除须另外处理。[外稿 §7](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/07-three-dimensions.tex)

**编码大小。** 分开书写时 $V$ 有 $3N+7$ 个循环因子，合并后最少只需一个生成元。$M$ 有 $p^2(p+1)+7$ 个不同素因子：$p$ 出现四次幂，$p^2(p-1)+2$ 个数字素数各出现平方，各通道的 $a_i,b_i$ 各出现一次。举例 $p=211$ 时，仅堆叠前即有 $9\,438\,459$ 个不同素因子。复算程序仅构造两个种子及一个截短通道的实际 CRT 证书。

还可估算满足外稿表格条件时 $\log M$ 的最小量级（自然对数）。令 $J=p^2(p-1)+2$。数字素数互不相同，故 $M\ge (J!)^2$，给出 $(6-o(1))p^3\log p$ 的下界。反向取普通通道的素数不超过 $C p^2\log p$，仅有的两个大种子素数取在 $(p^4,2p^4)$。对充分大常数 $C'$，区间 $[C'p^4(\log p)^2,2C'p^4(\log p)^2]$ 中的素数均满足相应非负分块门槛，且据素数定理可选出 $J$ 个。故可取 $\log M\le(8+o(1))p^3\log p$。这给出精确数量级 $\Theta(p^3\log p)$；未把堆叠颜色数或最后的实际瓦片体素数计入。

## 二、两种单点瓦片检测不分裂扩张

底群和扩张群均为有限交换群，采用加法记号。固定短正合列
\[
 0\longrightarrow K\longrightarrow E\xrightarrow{\pi}H\longrightarrow0 .
\]
在颜色层取非平凡子集 $A\subsetneq K$，假设 $A-A=K$，记 $C=K\setminus A$，$S=\{k\in K:A+k=A\}$。原稿还要求另一色 $C-C=K$；下列两色推导仅需第一色条件。底层两个瓦片为 $\{0\}$、$\{d\}$，$d\ne0$，二者都以 $H$ 为共同中心集。固定 $\pi(t)=d$。以 $T=A\cup(t+C)$ 作为在 $E$ 中合并后的瓦片。写 $\ell=\operatorname{ord}_H(d)$，$g=[H:\langle d\rangle]$。

**定理。** $T$ 能以平移精确铺砌 $E$ 当且仅当 $\ell t\in S$。可铺时，按实际中心子集计数，中心集个数是
\[
 \left(\frac{|K|}{|S|}\right)^g |S|^{|H|}. \tag{1}
\]

**证明。** 同一底层顶点 $x$ 上不可能有两个中心，它们的 $A$ 部分由 $A-A=K$ 必有重叠。该纤维若缺中心，其他来源仅剩 $x-d$ 上至多一个中心的 $C$ 部分，不能填满。因此每个 $x$ 恰有一个中心 $b(x)\in\pi^{-1}(x)$。在 $x+d$ 上两种来源的互补恰等价于
\[
 b(x+d)-b(x)-t\in S. \tag{2}
\]
沿每条长度 $\ell$ 的圈相加得 $\ell t\in S$。反之每圈首点有 $|K|$ 种选择，前 $\ell-1$ 个增量差可独立取自 $S$，最后一条由总和指定且仍在 $S$。逐圈相乘得 (1)。若 $S$ 非平凡，由不同中心产生的单个平移子集可能重合，(1) 的口径始终是中心集。

**可选提升的完整障碍。** 改用 $t+k$，绕圈变化为 $\ell k$。故某个提升合格当且仅当
\[
  [\ell t]=0\quad\hbox{in }K/(\ell K+S). \tag{3}
\]
此时共有 $|S|\,|(K/S)[\ell]|$ 个合格的提升，产生 $|(K/S)[\ell]|$ 个不同瓦片。逐个测试底群非平凡循环不变因子的生成元，均有合格提升，当且仅当商扩张 $E/S\to H$ 有群同态截面。确实，(3) 恰是为每个生成元选到一个同阶提升的条件，交换性保证这些选择组合成截面。存在时，全体截面数为 $|\operatorname{Hom}(H,K/S)|$。这一检验只需两个单点底层瓦片，以及一个上层互补颜色对；它可测出“用已有素数层代替新素数层”所隐藏的进位。

在具体循环链 $C_{nq}\to C_n$ 中，用 $nC_{nq}\simeq C_q$ 识别颜色层。写 $t=d+nh,\ u=\gcd(n,d),\ \ell=n/u$，则绕圈在 $C_q$ 中为 $d/u+\ell h$。存在某个合格提升恰当 $\gcd(\ell,q/|S|)=1$，因为 $d/u$ 与 $\ell$ 互素。对单个方向可用的素数复用，不一定适用于所有方向。

**49 元反例。** 取 $H=C_7$，$K=C_7$，颜色 $A=\{0,1,3\}$、$C=\{2,4,5,6\}$ 各自的差集均为 $C_7$ 且 $S=0$，取 $d=1$。在分裂群 $C_7\times C_7$ 可取 $t=(1,0)$，恰有七个中心集。在仍然循环的 $C_{49}$ 中，核为 $7C_{49}$，第一色用 $7A$；七个提升 $t=1+7h$ 全部有 $7t=7\ne0$，无一可铺。底层两式一直有共同解。故把集合大小相同的直积改写成循环扩张会改变铺砌性质。该例也解释新素数在外稿构造中同时保证了截面和最终的低生成元数。

## 三、颜色数与可复算范围

$s\ge2$ 个颜色均须具有满差集时，颜色群的阶 $q$ 至少为 $s(s+1)$。最小色类大小 $k\le q/s$，而 $q\le1+k(k-1)$，推出 $q^2-(s^2+s)q+s^2\ge0$。此二次式在 $1$ 与 $s(s+1)-1$ 均为负，两者之间不可能满足。因此两色的最小**素数**阶至少为 7，上例正好达到。原稿以随机着色保证 $s(q-1)(1-s^{-2})^{\lfloor q/2\rfloor}<1$ 即有解，取素数时还须避开 $M$ 的素因子。小规模复算遍历素数阶 $2,3,5,7$ 的全部两色划分，标号两色的可用划分数分别是 $0,0,0,28$。

**可放宽的条件。** 颜色模数无需本身为素数。对任一有限群（取加法交换群即可）中非零差 $d$，平移置换的每个圈长度皆为 $\ell=\operatorname{ord}(d)\ge2$，每圈可取 $\lfloor\ell/2\rfloor$ 条不共端点的边。若群阶为 $q$，合计至少 $q/3$ 条，随机着色的坏概率至多 $s(q-1)(1-s^{-2})^{q/3}$。因此任何足够大且与 $M$ 互素的循环模数均可沿用外稿的直积堆叠；例如可预取一个与 $M$ 互素的基数，反复取幂直到该上界小于一。两色反例定位了这里真正需要维护的群扩张与进位条件。

程序对 162 组分裂/不分裂的两色实例作精确覆盖枚举，其中含有 $|S|=2$ 的复合颜色层，并分别对照 (1)。原稿给出的字规则、整个有限铺砌系统、实中心对齐不依赖这些有限实验。尚未解决的方向是一般多色、多点瓦片在不分裂扩张中是否有同样可计算的提升闸门；两色单点的充要条件已由 (2) 完全刻画。
